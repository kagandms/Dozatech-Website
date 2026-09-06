from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree


ROOT_DIR = Path(__file__).resolve().parents[1]
DIST_DIR = ROOT_DIR / 'dist'
sys.path.insert(0, str(ROOT_DIR))

from build import (  # noqa: E402
    BASE_URL,
    PAGE_BREADCRUMBS,
    PAGE_ROUTES,
    PAGE_SOCIAL_METADATA,
)


SITEMAP_NAMESPACE = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


def fail(message: str) -> None:
    raise AssertionError(message)


def assert_exists(path: Path) -> None:
    if not path.is_file():
        fail(f'Missing build output: {path.relative_to(ROOT_DIR)}')


def get_route_output(public_path: str) -> Path:
    if public_path == '/':
        return DIST_DIR / 'index.html'
    return DIST_DIR / public_path.strip('/') / 'index.html'


def verify_route_outputs() -> None:
    for source_file, public_path in PAGE_ROUTES.items():
        assert_exists(ROOT_DIR / source_file)
        assert_exists(get_route_output(public_path))

    assert_exists(DIST_DIR / '404.html')
    assert_exists(DIST_DIR / 'robots.txt')
    assert_exists(DIST_DIR / 'sitemap.xml')
    assert_exists(DIST_DIR / 'css' / 'style.css')


def verify_sitemap() -> None:
    sitemap = ElementTree.parse(DIST_DIR / 'sitemap.xml')
    locations = [
        element.text
        for element in sitemap.findall('sitemap:url/sitemap:loc', SITEMAP_NAMESPACE)
    ]
    expected = [f'{BASE_URL}{public_path}' for public_path in PAGE_ROUTES.values()]

    if locations != expected:
        fail('Sitemap URLs do not match the configured public routes.')
    if len(locations) != len(set(locations)):
        fail('Sitemap contains duplicate URLs.')

    robots_text = (DIST_DIR / 'robots.txt').read_text(encoding='utf-8')
    if f'Sitemap: {BASE_URL}/sitemap.xml' not in robots_text:
        fail('robots.txt does not point to the generated sitemap.')


def verify_vercel_routes() -> None:
    configuration = json.loads((ROOT_DIR / 'vercel.json').read_text(encoding='utf-8'))
    rewrites = {rule['source'] for rule in configuration.get('rewrites', [])}
    redirects = {
        rule['source']: rule
        for rule in configuration.get('redirects', [])
    }

    for source_file, public_path in PAGE_ROUTES.items():
        if public_path != '/' and public_path not in rewrites:
            fail(f'Missing Vercel rewrite for {public_path}.')
        if source_file != 'index.html':
            redirect = redirects.get(f'/{source_file}')
            if not redirect or redirect.get('destination') != public_path:
                fail(f'Missing legacy redirect for /{source_file}.')


def verify_generated_html() -> None:
    for public_path in PAGE_ROUTES.values():
        html = get_route_output(public_path).read_text(encoding='utf-8')
        if 'href="dist/css/style.css"' in html:
            fail(f'Root-relative CSS path was not generated for {public_path}.')


def verify_analytics_injection() -> None:
    for public_path in PAGE_ROUTES.values():
        html = get_route_output(public_path).read_text(encoding='utf-8')
        analytics_script_count = html.count('googletagmanager.com/gtag/js?id=G-QBSSV93GCS')
        if analytics_script_count != 1:
            fail(f'Expected one GA4 loader on {public_path}, found {analytics_script_count}.')
        if html.count("window.gtag('config', 'G-QBSSV93GCS')") != 1:
            fail(f'Expected one GA4 config call on {public_path}.')
        if "sendEvent('cta_click'" not in html:
            fail(f'CTA tracking handler is missing on {public_path}.')
        if 'connect-src' not in html or 'https://formspree.io' not in html:
            fail(f'Formspree is not allowed by the generated CSP on {public_path}.')

    home_html = get_route_output('/').read_text(encoding='utf-8')
    for required_handler in ("sendEvent('form_start'", "sendEvent('form_success'", "sendEvent('form_error'"):
        if required_handler not in home_html:
            fail(f'Missing form analytics handler: {required_handler}.')


def verify_seo_enrichment() -> None:
    for source_file, metadata in PAGE_SOCIAL_METADATA.items():
        html = get_route_output(PAGE_ROUTES[source_file]).read_text(encoding='utf-8')
        for marker in ('og:type', 'og:url', 'og:title', 'og:description', 'og:image'):
            if marker not in html:
                fail(f'Missing social metadata {marker} on {PAGE_ROUTES[source_file]}.')
        if 'twitter:card' not in html or 'twitter:image' not in html:
            fail(f'Missing Twitter metadata on {PAGE_ROUTES[source_file]}.')

    for source_file in PAGE_BREADCRUMBS:
        html = get_route_output(PAGE_ROUTES[source_file]).read_text(encoding='utf-8')
        if '"BreadcrumbList"' not in html:
            fail(f'Missing BreadcrumbList schema on {PAGE_ROUTES[source_file]}.')


def verify_mobile_and_security_output() -> None:
    for public_path in PAGE_ROUTES.values():
        html = get_route_output(public_path).read_text(encoding='utf-8')
        if html.count('id="mobile-menu-btn"') != 1 or html.count('id="mobile-menu"') != 1:
            fail(f'Expected one accessible mobile menu on {public_path}.')
        if 'aria-controls="mobile-menu"' not in html or 'aria-expanded="false"' not in html:
            fail(f'Mobile menu accessibility attributes are missing on {public_path}.')
        blank_links = re.findall(r'<a\b[^>]*target="_blank"[^>]*>', html, flags=re.IGNORECASE)
        if any('rel=' not in anchor.lower() for anchor in blank_links):
            fail(f'External blank link without rel protection on {public_path}.')
        image_tags = re.findall(r'<img\b[^>]*>', html, flags=re.IGNORECASE)
        if any('decoding="async"' not in image.lower() for image in image_tags):
            fail(f'Image decoding hint is missing on {public_path}.')
        if 'fonts.googleapis.com' in html and 'rel="preconnect"' not in html:
            fail(f'Font preconnect hint is missing on {public_path}.')

    css = (DIST_DIR / 'css' / 'style.css').read_text(encoding='utf-8')
    if 'prefers-reduced-motion' not in css:
        fail('Reduced-motion CSS support is missing.')


def verify_vercel_headers() -> None:
    configuration = json.loads((ROOT_DIR / 'vercel.json').read_text(encoding='utf-8'))
    header_rules = configuration.get('headers', [])
    security_keys = {
        header['key']
        for rule in header_rules
        for header in rule.get('headers', [])
    }
    required_keys = {
        'Strict-Transport-Security',
        'X-Content-Type-Options',
        'X-Frame-Options',
        'Referrer-Policy',
        'Permissions-Policy',
        'Content-Security-Policy',
    }
    if not required_keys.issubset(security_keys):
        fail('Vercel security headers are incomplete.')

    asset_rules = [rule for rule in header_rules if rule.get('source') in {'/assets/(.*)', '/css/(.*)'}]
    if len(asset_rules) != 2:
        fail('Immutable cache rules for assets and CSS are incomplete.')


def main() -> None:
    verify_route_outputs()
    verify_sitemap()
    verify_vercel_routes()
    verify_generated_html()
    verify_analytics_injection()
    verify_seo_enrichment()
    verify_mobile_and_security_output()
    verify_vercel_headers()
    print('Build verification passed: routes, sitemap, redirects, and output assets are valid.')


if __name__ == '__main__':
    main()
