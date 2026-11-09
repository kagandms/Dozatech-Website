from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse
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


EFOR_MESSAGE = 'Merhaba, Efor EF340 / EF341 hakkında bilgi almak istiyorum.'


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
        if public_path == '/':
            continue
        slash_redirect = redirects.get(f'{public_path}/')
        if (
            not slash_redirect
            or slash_redirect.get('destination') != public_path
            or slash_redirect.get('permanent') is not True
        ):
            fail(f'Missing permanent trailing-slash redirect for {public_path}.')


def verify_canonical_host_redirect() -> None:
    configuration = json.loads((ROOT_DIR / 'vercel.json').read_text(encoding='utf-8'))
    expected_source = '/:path*'
    expected_destination = f'{BASE_URL}/:path*'
    for rule in configuration.get('redirects', []):
        host_conditions = rule.get('has', [])
        if (
            rule.get('source') == expected_source
            and rule.get('destination') == expected_destination
            and rule.get('permanent') is True
            and any(
                condition.get('type') == 'host'
                and condition.get('value') == 'www.dozatech.com.tr'
                for condition in host_conditions
            )
        ):
            return
    fail('Missing permanent www-to-apex redirect that preserves the path and query.')


def verify_business_service_copy() -> None:
    homepage = get_route_output('/').read_text(encoding='utf-8')
    required_copy = (
        'yaklaşık 30 yıllık teknik deneyimimizle',
        'Dozaj pompalarının montaj, bakım ve onarım hizmetini',
        'Endüstriyel bulaşık makineleri de satıyoruz.',
    )
    for phrase in required_copy:
        if phrase not in homepage:
            fail(f'Missing business service boundary copy: {phrase}')
    if 'Kimyasal israfını sıfırlayan' in homepage:
        fail('Unsupported zero-waste claim remains in generated homepage copy.')
    generated_html = '\n'.join(
        path.read_text(encoding='utf-8')
        for path in DIST_DIR.rglob('*.html')
    ).casefold()
    unsupported_claims = (
        'enerji tasarrufu sağlar',
        'enerji tüketimi azalır',
        'enerji verimli',
        'tasarruf sağlayan',
        'maliyetlerini düşürecek',
        '"pricerange"',
    )
    for claim in unsupported_claims:
        if claim in generated_html:
            fail(f'Unsupported price or savings claim remains: {claim}')


def verify_homepage_commercial_priority() -> None:
    homepage = get_route_output('/').read_text(encoding='utf-8')
    headings = re.findall(r'<h3\b[^>]*>(.*?)</h3>', homepage)
    priority_headings = (
        'Endüstriyel Bulaşık Makinesi Kimyasalları',
        'Dozaj Pompaları ve Otomasyon',
        'Endüstriyel Bulaşık Makineleri',
    )
    positions = [headings.index(heading) if heading in headings else -1 for heading in priority_headings]
    if -1 in positions or positions != sorted(positions):
        fail('Homepage product cards do not follow chemical, pump, then dishwasher priority.')


def verify_chemical_offer_copy() -> None:
    homepage = get_route_output('/').read_text(encoding='utf-8')
    category = get_route_output('/urunler/kimyasallar').read_text(encoding='utf-8')
    chemical_groups = (
        'Endüstriyel bulaşık makinesi deterjanı',
        'Parlatıcı',
        'Yağ sökücü',
        'Kireç sökücü',
    )
    for group in chemical_groups:
        if group.casefold() not in homepage.casefold():
            fail(f'Missing homepage chemical group: {group}.')
        if group.casefold() not in category.casefold():
            fail(f'Missing chemical category group: {group}.')

    required_offer_copy = (
        'Düzenli Kimyasal Tedarikinde Pompa ve Bakım Desteği',
        'Tedarik ve Destek Koşullarını Görüşelim',
        'desteğin kapsam ve koşullarını görüşmede netleştiriyoruz',
    )
    for phrase in required_offer_copy:
        if phrase.casefold() not in homepage.casefold():
            fail(f'Missing qualified chemical support copy: {phrase}.')

    support_links = re.findall(r'<a\b[^>]*href="([^"]*wa\.me/[^"]*)"[^>]*>(.*?)</a>', homepage, re.DOTALL)
    if not any(
        'Düzenli Kimyasal Tedarikinde Pompa ve Bakım Desteği'.casefold() in link_text.casefold()
        or 'Tedarik ve Destek Koşullarını Görüşelim'.casefold() in link_text.casefold()
        for _, link_text in support_links
    ):
        fail('The support CTA must use the existing WhatsApp number and a prepared message.')
    if not any('905322063859' in href and 'whatsapp_click' in homepage for href, _ in support_links):
        fail('The prepared WhatsApp support CTA is missing or does not retain WhatsApp event tracking.')
    prepared_messages = [
        parse_qs(urlparse(href).query).get('text', [''])[0]
        for href, link_text in support_links
        if 'Tedarik ve Destek Koşullarını Görüşelim'.casefold() in link_text.casefold()
    ]
    expected_message = 'Merhaba, düzenli kimyasal tedariki ve pompa desteği koşulları hakkında görüşmek istiyorum.'
    if expected_message not in prepared_messages:
        fail('The support WhatsApp message is missing or incorrectly URL encoded.')

    for html in (homepage, category):
        forbidden_claims = ('ücretsiz kargo', 'sınırsız ücretsiz bakım', 'türkiye geneli servis', 'ücretsiz teslimat')
        if any(claim in html.casefold() for claim in forbidden_claims):
            fail('An unsupported delivery or unconditional service claim remains.')


def verify_chemical_category_cards() -> None:
    category = get_route_output('/urunler/kimyasallar').read_text(encoding='utf-8')
    cards = re.findall(r'<article\b[^>]*>(.*?)</article>', category, flags=re.DOTALL)
    expected_products = {
        'Endüstriyel bulaşık makinesi deterjanı': (
            'Endüstriyel bulaşık makinelerinde kullanılan Efor EF340 deterjan. Ambalaj: 20 L bidon.',
            'Merhaba, Efor EF340 / EF341 hakkında bilgi almak istiyorum.',
        ),
        'Parlatıcı': (
            'Bulaşık yıkama sürecinin durulama aşaması için Efor EF341 parlatıcı. Ambalaj: 20 L bidon.',
            'Merhaba, Efor EF340 / EF341 hakkında bilgi almak istiyorum.',
        ),
        'Yağ sökücü': (
            'Yağlı kirlerin temizliğine yönelik ayrı bir kimyasal ürün grubudur.',
            'Merhaba, yağ sökücü tedariki hakkında görüşmek istiyorum.',
        ),
        'Kireç sökücü': (
            'Kireç birikimlerinin giderilmesine yönelik kimyasal ürün grubudur.',
            'Merhaba, kireç sökücü tedariki hakkında görüşmek istiyorum.',
        ),
    }
    if len(cards) != 4:
        fail(f'Expected four chemical category cards, found {len(cards)}.')

    for card, (product, (description, expected_message)) in zip(cards, expected_products.items()):
        if product.casefold() not in card.casefold():
            fail(f'Chemical category card is missing the {product} heading.')
        description_match = re.search(r'<p\b[^>]*>(.*?)</p>', card, flags=re.DOTALL)
        if not description_match or re.sub(r'<[^>]+>', '', description_match.group(1)).strip() != description:
            fail(f'The {product} card needs the expected concise purpose description.')

        links = re.findall(r'<a\b[^>]*href="([^"]*wa\.me/[^"]*)"[^>]*>(.*?)</a>', card, re.DOTALL)
        if len(links) != 1:
            fail(f'The {product} card must have one WhatsApp offer link.')
        href, link_text = links[0]
        if '905322063859' not in href or 'Teklif' not in link_text:
            fail(f'The {product} card WhatsApp CTA does not preserve the number or offer label.')
        message = parse_qs(urlparse(href).query).get('text', [''])[0].casefold()
        if message != expected_message.casefold():
            fail(f'The {product} card has the wrong or unencoded WhatsApp message.')

    if '/assets/images/kirecsokucu.webp' not in cards[3]:
        fail('The existing kireç sökücü product photo must remain on its category card.')
    if '/urunler/endustriyel-kirec-sokucu' not in cards[3]:
        fail('The kireç sökücü detail page link was removed.')
    degreaser_card = cards[2].casefold()
    if 'bulaşık makinesinin içine' in degreaser_card or 'makineye dozaj' in degreaser_card:
        fail('The degreaser card must not present the product as being dosed into a dishwasher.')

    required_support = (
        'Düzenli Kimyasal Tedarikinde Pompa ve Bakım Desteği',
        'ücretsiz pompa temini ve pompa bakım desteği sunulabilir',
        'Desteğin kapsam ve koşullarını görüşmede netleştiriyoruz',
        'Tedarik ve Destek Koşullarını Görüşelim',
    )
    for phrase in required_support:
        if phrase.casefold() not in category.casefold():
            fail(f'The chemical category page is missing aligned support copy: {phrase}.')

    css_source = (ROOT_DIR / 'src' / 'css' / 'input.css').read_text(encoding='utf-8')
    if '.chemical-category-page .whatsapp-float' not in css_source:
        fail('The mobile floating WhatsApp button must not cover the chemical card content.')


def verify_homepage_heading_and_share_metadata() -> None:
    homepage = get_route_output('/').read_text(encoding='utf-8')
    if '<h1' not in homepage or 'Endüstriyel Temizlik Kimyasalları ve Dozaj Çözümleri' not in homepage:
        fail('Homepage H1 does not describe the confirmed chemical and dosing offer.')
    if 'İstanbul için' in homepage or 'İstanbul’daki restoran' in homepage or "İstanbul'daki restoran" in homepage:
        fail('Homepage metadata or hero copy still restricts the offer to Istanbul.')
    expected_description = 'Restoran, otel ve kafeler için deterjan, parlatıcı, yağ sökücü ve kireç sökücü tedariki; dozaj pompası satışı, montajı, bakımı ve onarımı. Teklif alın.'
    for marker in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        match = re.search(rf'<meta\s+{re.escape(marker)}\s+content="([^"]*)"', homepage)
        if not match or match.group(1) != expected_description:
            fail(f'Homepage {marker} does not match the confirmed offer description.')
    for restrictive in ('ana pazarımızdır', 'kapsamına göre değerlendirilir', 'tamir veya bakım hizmeti sunmuyoruz', 'tamiri ve onarımı yapmıyoruz', 'her bölgesine ulaşıyoruz'):
        if restrictive in homepage:
            fail(f'Restrictive or negative service copy must not appear on the homepage: {restrictive}')


def verify_canonical_url_origins() -> None:
    for public_path in PAGE_ROUTES.values():
        html = get_route_output(public_path).read_text(encoding='utf-8')
        canonical_urls = re.findall(r'<link rel="canonical" href="([^"]+)"', html)
        social_urls = re.findall(r'<meta property="og:url" content="([^"]+)"', html)
        expected_url = f'{BASE_URL}{public_path}'
        if canonical_urls != [expected_url]:
            fail(f'Canonical URL is missing, duplicated, or incorrect on {public_path}.')
        if social_urls != [expected_url]:
            fail(f'Open Graph URL is missing, duplicated, or incorrect on {public_path}.')
        site_urls = re.findall(r'https?://(?:www\.)?dozatech\.com\.tr[^"\s<]*', html)
        if any(not url.startswith(BASE_URL) for url in site_urls):
            fail(f'Generated metadata or structured data uses a non-canonical origin on {public_path}.')


def verify_default_branch_ci() -> None:
    workflow = (ROOT_DIR / '.github' / 'workflows' / 'main.yml').read_text(encoding='utf-8')
    if 'name: DOZATECH Web CI' not in workflow:
        fail('The repository build workflow is not named DOZATECH Web CI.')
    for event_name in ('push', 'pull_request'):
        match = re.search(
            rf'(?m)^  {event_name}:\s*\n    branches:\s*\[([^\]]+)\]',
            workflow,
        )
        if not match or 'главно' not in {branch.strip() for branch in match.group(1).split(',')}:
            fail(f'DOZATECH Web CI does not run on {event_name} for the default branch главно.')


def verify_vercel_build_config() -> None:
    configuration = json.loads((ROOT_DIR / 'vercel.json').read_text(encoding='utf-8'))
    if configuration.get('buildCommand') != 'npm run build':
        fail('Vercel build command must run npm run build.')
    if configuration.get('outputDirectory') != 'dist':
        fail('Vercel output directory must be dist/.')
    if configuration.get('installCommand') != 'npm ci':
        fail('Vercel must install from the lockfile with npm ci.')


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


def verify_mobile_detail_navigation() -> None:
    detail_paths = (
        '/cozumler/restoranlar-icin-bulasik-yikama-ve-dozaj-sistemleri',
        '/urunler/seko-pr4-deterjan-pompasi',
    )
    for public_path in detail_paths:
        html = get_route_output(public_path).read_text(encoding='utf-8')
        match = re.search(
            r'<nav\b[^>]*aria-label="Ana menü"[^>]*class="([^"]+)"',
            html,
        )
        if not match or 'hidden' not in match.group(1) or 'md:flex' not in match.group(1):
            fail(f'Header navigation is not desktop-only on {public_path}.')


def verify_seko_faq_alignment() -> None:
    public_path = '/urunler/seko-pr4-deterjan-pompasi'
    html = get_route_output(public_path).read_text(encoding='utf-8')
    expected_question = 'Montaj öncesi hangi bilgi gerekir?'
    if f'"name":"{expected_question}"' not in html:
        fail(f'Seko FAQ schema is not aligned with visible content on {public_path}.')


def verify_pump_page_content() -> None:
    public_path = '/urunler/dozaj-pompalari'
    html = get_route_output(public_path).read_text(encoding='utf-8')

    title_match = re.search(r'<title>(.*?)</title>', html)
    if not title_match or len(title_match.group(1)) > 60:
        fail(f'Pump page title is missing or longer than 60 characters on {public_path}.')

    description_match = re.search(r'<meta name="description"\s+content="([^"]*)"', html)
    if not description_match:
        fail(f'Pump page meta description is missing on {public_path}.')
    description = description_match.group(1)
    if not 150 <= len(description) <= 160:
        fail(f'Pump page meta description must be 150-160 characters, found {len(description)}.')
    for keyword in ('dozaj pompası', 'bulaşık makinesi', 'montaj'):
        if keyword not in description.casefold():
            fail(f'Pump page meta description is missing the keyword: {keyword}.')

    required_headings = (
        'Dozaj Pompası Nedir?',
        'Hangi Pompa Bana Uygun?',
        'Sık Sorulan Sorular',
        'Pompa için teklif alın',
    )
    for heading in required_headings:
        if heading not in html:
            fail(f'Pump page is missing the section or CTA: {heading}.')

    visible_faq = re.findall(
        r'<details\b[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*<p[^>]*>(.*?)</p>\s*</details>',
        html,
        flags=re.DOTALL,
    )
    faq_schemas = [
        json.loads(block)
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.DOTALL)
        if '"FAQPage"' in block
    ]
    if len(visible_faq) != 4 or len(faq_schemas) != 1:
        fail('Pump page must have four visible FAQ items and one FAQPage schema.')
    schema_items = [
        (entry['name'], entry['acceptedAnswer']['text'])
        for entry in faq_schemas[0]['mainEntity']
    ]
    if visible_faq != schema_items:
        fail('Pump page FAQPage schema does not match the visible FAQ text.')

    forbidden_phrases = (
        'tamir',
        'hizmet vermiyoruz',
        'garanti',
        'en iyi',
        'istanbul',
        'ücretsiz',
    )
    casefolded = html.casefold()
    for phrase in forbidden_phrases:
        if phrase in casefolded:
            fail(f'Pump page contains a forbidden phrase: {phrase}.')


def verify_service_page_content() -> None:
    public_path = '/hizmetler/dozaj-pompasi-montaj-bakim-onarim'
    html = get_route_output(public_path).read_text(encoding='utf-8')

    title_match = re.search(r'<title>(.*?)</title>', html)
    if not title_match or title_match.group(1) != 'Dozaj Pompası Montajı, Bakımı ve Onarımı | DOZATECH':
        fail(f'Service page title is missing or incorrect on {public_path}.')
    if len(title_match.group(1)) > 60:
        fail(f'Service page title is longer than 60 characters on {public_path}.')

    description_match = re.search(r'<meta name="description"\s+content="([^"]*)"', html)
    if not description_match or not 150 <= len(description_match.group(1)) <= 160:
        fail(f'Service page meta description must be 150-160 characters on {public_path}.')

    required_copy = (
        '<h1 class="text-4xl font-extrabold primary-text mb-4">Dozaj Pompası Montajı, Bakımı ve Onarımı</h1>',
        '>Montaj</h2>',
        '>Bakım</h2>',
        '>Onarım</h2>',
        '>İlgili Sayfalar</h2>',
        '>Sık Sorulan Sorular</h2>',
        'Düzenli kimyasal tedarikini Dozatech’ten yapan müşterilere ücretsiz pompa temini ve pompa bakım desteği sunulabilir. Desteğin kapsam ve koşullarını görüşmede netleştiriyoruz.',
        'Montaj veya bakım için yazın',
        'tel:+905322063859',
        '/assets/images/montaj_korumali_hortum.webp',
        '/assets/images/montaj_pompa_setleri.webp',
    )
    for phrase in required_copy:
        if phrase not in html:
            fail(f'Service page is missing required copy or element: {phrase[:60]}.')

    internal_links = (
        '/urunler/dozaj-pompalari',
        '/urunler/seko-pr4-deterjan-pompasi',
        '/urunler/atiker-apm-0300-deterjan-parlatici-pompasi',
        '/urunler/kimyasallar',
    )
    for link in internal_links:
        if f'href="{link}"' not in html:
            fail(f'Service page is missing internal link: {link}.')

    if 'wa.me/905322063859' not in html:
        fail(f'Service page CTA does not use the WhatsApp number on {public_path}.')

    visible_faq = re.findall(
        r'<details\b[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*<p[^>]*>(.*?)</p>\s*</details>',
        html,
        flags=re.DOTALL,
    )
    schemas = [
        json.loads(block)
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.DOTALL)
    ]
    faq_schemas = [schema for schema in schemas if schema.get('@type') == 'FAQPage']
    service_schemas = [schema for schema in schemas if schema.get('@type') == 'Service']
    if len(visible_faq) != 4 or len(faq_schemas) != 1:
        fail('Service page must have four visible FAQ items and one FAQPage schema.')
    schema_items = [
        (entry['name'], entry['acceptedAnswer']['text'])
        for entry in faq_schemas[0]['mainEntity']
    ]
    if visible_faq != schema_items:
        fail('Service page FAQPage schema does not match the visible FAQ text.')
    if len(service_schemas) != 1 or service_schemas[0].get('provider', {}).get('@id') != 'https://dozatech.com.tr/#organization':
        fail('Service page Service schema must reference the Organization by its @id.')

    casefolded = html.casefold()
    for phrase in ('tamir', 'servis', 'hizmet vermiyoruz', 'garanti', 'en iyi', 'istanbul', '30 yıl'):
        if phrase in casefolded:
            fail(f'Service page contains a forbidden phrase: {phrase}.')
    if casefolded.count('ücretsiz') != 1:
        fail('Service page must mention free pump support exactly once, in the qualified support sentence.')

    home_html = get_route_output('/').read_text(encoding='utf-8')
    if home_html.count(f'href="{public_path}"') < 2:
        fail('Homepage must link to the service page from the service card and the footer.')
    pump_html = get_route_output('/urunler/dozaj-pompalari').read_text(encoding='utf-8')
    if f'href="{public_path}"' not in pump_html:
        fail('Pump page must link to the service page.')


def verify_target_metadata() -> None:
    expected_metadata = {
        '/': (
            'Endüstriyel Temizlik Kimyasalı ve Dozaj Pompası | DOZATECH',
            'Restoran, otel ve kafeler için deterjan, parlatıcı, yağ sökücü ve kireç sökücü tedariki; dozaj pompası satışı, montajı, bakımı ve onarımı. Teklif alın.',
        ),
        '/urunler': (
            'Endüstriyel Bulaşık Makinesi Kimyasalları ve Dozaj Pompaları | DOZATECH',
            'Restoran, otel ve kafeler için endüstriyel deterjan, parlatıcı, yağ sökücü ve kireç sökücü tedariki; dozaj pompası satışı ve montajı.',
        ),
        '/urunler/kimyasallar': (
            'Bulaşık Makinesi Kimyasalları: Efor EF340, EF341 | DOZATECH',
            'Endüstriyel bulaşık makinesi deterjanı Efor EF340 ve parlatıcı Efor EF341 (20 L). Sipariş için WhatsApp\'tan yazın.',
        ),
    }
    for public_path, (title, description) in expected_metadata.items():
        html = get_route_output(public_path).read_text(encoding='utf-8')
        if f'<title>{title}</title>' not in html:
            fail(f'Target title is not generated for {public_path}.')
        if f'<meta name="description" content="{description}">' not in html:
            fail(f'Target description is not generated for {public_path}.')

    homepage_metadata = PAGE_SOCIAL_METADATA['index.html']
    if homepage_metadata[1:3] != expected_metadata['/']:
        fail('Homepage build.py social metadata differs from the expected title and description.')

    for public_path, source_file in (('/', 'index.html'), ('/urunler/kimyasallar', 'urunler_kimyasallar.html')):
        source = (ROOT_DIR / source_file).read_text(encoding='utf-8')
        generated = get_route_output(public_path).read_text(encoding='utf-8')
        metadata = PAGE_SOCIAL_METADATA[source_file]
        expected_title = metadata[1]
        expected_description = metadata[2]
        if f'<title>{expected_title}</title>' not in source:
            fail(f'Source title differs from build.py metadata on {public_path}.')
        for tag in ('og:title', 'twitter:title'):
            if not re.search(rf'<meta\s+(?:property|name)="{tag}"\s+content="{re.escape(expected_title)}"', source):
                fail(f'Source {tag} differs from build.py metadata on {public_path}.')
        for tag in ('og:description', 'twitter:description'):
            if not re.search(rf'<meta\s+(?:property|name)="{tag}"\s+content="{re.escape(expected_description)}"', source):
                fail(f'Source {tag} differs from build.py metadata on {public_path}.')
        for tag in ('og:title', 'twitter:title'):
            if not re.search(rf'<meta\s+(?:property|name)="{tag}"\s+content="{re.escape(expected_title)}"', generated):
                fail(f'Generated {tag} differs from build.py metadata on {public_path}.')
        for tag in ('og:description', 'twitter:description'):
            if not re.search(rf'<meta\s+(?:property|name)="{tag}"\s+content="{re.escape(expected_description)}"', generated):
                fail(f'Generated {tag} differs from build.py metadata on {public_path}.')

    category = get_route_output('/urunler/kimyasallar').read_text(encoding='utf-8')
    item_lists = [
        json.loads(block)
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', category, re.DOTALL)
        if '"@type": "ItemList"' in block
    ]
    if not item_lists or [item.get('name') for item in item_lists[0].get('itemListElement', [])] != [
        'Efor EF340 Endüstriyel bulaşık makinesi deterjanı',
        'Efor EF341 Parlatıcı',
        'Yağ sökücü',
        'Kireç sökücü',
    ]:
        fail('Chemical category structured data does not list exactly the confirmed groups.')


def verify_efor_product_copy() -> None:
    category = get_route_output('/urunler/kimyasallar').read_text(encoding='utf-8')
    visible_text = re.sub(r'<script\b.*?</script>', ' ', category, flags=re.DOTALL | re.IGNORECASE)
    visible_text = re.sub(r'<[^>]+>', ' ', visible_text)

    for phrase in (
        'Efor EF340',
        'Efor EF341',
        '20 L',
        'Bulaşık Makinesi Kimyasalları: Efor EF340, EF341',
    ):
        if phrase not in category:
            fail(f'Chemicals page is missing the Efor product copy: {phrase}.')
    if 'Bulaşık Makinesi Kimyasalları' not in category:
        fail('Chemicals page title must contain Bulaşık Makinesi Kimyasalları.')
    for phrase in (
        'Teslimat',
        'aynı gün veya ertesi gün',
        'Minimum sipariş',
        '2 adet Efor EF340 deterjan ve 1 adet Efor EF341 parlatıcı',
    ):
        if phrase not in visible_text:
            fail(f'Chemicals page is missing the delivery or minimum order copy: {phrase}.')

    product_names = []
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', category, flags=re.DOTALL):
        schema = json.loads(block)
        if schema.get('@type') != 'Product':
            continue
        product_names.append(schema.get('name', ''))
        if schema.get('brand', {}).get('name') != 'Efor':
            fail('Efor Product structured data must name the brand Efor.')
        if schema.get('size') != '20 L':
            fail('Efor Product structured data must state the 20 L size.')
        for key in ('offers', 'aggregateRating', 'review', 'price'):
            if key in schema:
                fail(f'Efor Product structured data must not include {key}.')
    if not any('Efor EF340' in name for name in product_names) or not any('Efor EF341' in name for name in product_names):
        fail('Product structured data is missing the Efor EF340 or EF341 product.')

    wa_hrefs = re.findall(r'<a\b[^>]*href="([^"]*wa\.me/[^"]*)"', category)
    prepared_messages = [
        parse_qs(urlparse(href).query).get('text', [''])[0]
        for href in wa_hrefs
        if '905322063859' in href
    ]
    if prepared_messages.count(EFOR_MESSAGE) < 3:
        fail('Both Efor product cards and the order CTA must use the prepared WhatsApp message.')

    lowered = visible_text.casefold()
    forbidden = (
        'tek adreste',
        'maksimum',
        'en kaliteli',
        'en iyi',
        'konum',
        'yakın',
        'tamir',
        'servis',
        'bakım yapmıyoruz',
        'sertifika',
        'klor',
        'konsantrasyon',
    )
    for phrase in forbidden:
        if phrase in lowered:
            fail(f'Chemicals page contains a forbidden phrase: {phrase}.')
    if re.search(r'\bph\b', lowered):
        fail('Chemicals page contains an unverified pH claim.')
    for symbol in ('\u2014', '\u2013', '!'):
        if symbol in visible_text:
            fail(f'Chemicals page contains a forbidden punctuation mark: {symbol!r}.')

    for public_path in ('/', '/urunler'):
        html = get_route_output(public_path).read_text(encoding='utf-8')
        if 'Efor EF340' not in html or 'Efor EF341' not in html:
            fail(f'Product names are not consistent on {public_path}.')
        for phrase in (
            'tek adreste',
            'maksimum',
            'en kaliteli',
            'bulaşık makinesi tamir',
            'bulaşık makinelerinin tamir',
            'bulaşık makinesi bakım',
            'bulaşık makinelerinin bakım',
            'bakım yapmıyoruz',
        ):
            if phrase in html.casefold():
                fail(f'{public_path} contains a forbidden phrase: {phrase}.')


def verify_category_schema_types() -> None:
    category_paths = (
        '/urunler/bulasik-makineleri',
        '/urunler/kimyasallar',
        '/urunler/dozaj-pompalari',
    )
    for public_path in category_paths:
        html = get_route_output(public_path).read_text(encoding='utf-8')
        schemas = [
            json.loads(block)
            for block in re.findall(
                r'<script type="application/ld\+json">(.*?)</script>',
                html,
                flags=re.DOTALL,
            )
        ]
        item_lists = [schema for schema in schemas if schema.get('@type') == 'ItemList']
        if not item_lists:
            fail(f'Missing ItemList schema on {public_path}.')
        if any(
            item.get('@type') == 'Product'
            for schema in item_lists
            for item in schema.get('itemListElement', [])
        ):
            fail(f'Category ItemList contains Product rich-result items on {public_path}.')
        if not any(schema.get('@type') == 'BreadcrumbList' for schema in schemas):
            fail(f'BreadcrumbList schema was lost on {public_path}.')


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
    verify_canonical_host_redirect()
    verify_generated_html()
    verify_business_service_copy()
    verify_homepage_commercial_priority()
    verify_chemical_offer_copy()
    verify_chemical_category_cards()
    verify_efor_product_copy()
    verify_homepage_heading_and_share_metadata()
    verify_canonical_url_origins()
    verify_default_branch_ci()
    verify_vercel_build_config()
    verify_analytics_injection()
    verify_seo_enrichment()
    verify_mobile_and_security_output()
    verify_mobile_detail_navigation()
    verify_seko_faq_alignment()
    verify_pump_page_content()
    verify_service_page_content()
    verify_target_metadata()
    verify_category_schema_types()
    verify_vercel_headers()
    print('Build verification passed: routes, sitemap, redirects, and output assets are valid.')


if __name__ == '__main__':
    main()
