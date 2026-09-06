import os
import re
import shutil
import subprocess
import sys
import datetime
import hashlib
import json

# Configuration
import platform
import urllib.request
import stat

# Configuration
DIST_DIR = 'dist'
SRC_CSS = 'src/css/input.css'
ASSETS_DIR = 'assets'
BASE_URL = 'https://dozatech.com.tr'
TAILWIND_VERSION = 'v3.4.17'
NODE_TAILWIND_CLI = os.path.join('node_modules', '.bin', 'tailwindcss')
NON_ROUTE_HTML_FILES = {'404.html'}
LEGACY_ANALYTICS_PATTERN = re.compile(
    r'\s*<!-- Google Analytics -->\s*'
    r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*'
    r'<script>.*?</script>',
    flags=re.DOTALL,
)
PAGE_ROUTES = {
    'index.html': '/',
    'urunler.html': '/urunler',
    'urunler_bulasikmakineleri.html': '/urunler/bulasik-makineleri',
    'urunler_kimyasallar.html': '/urunler/kimyasallar',
    'urunler_pompa.html': '/urunler/dozaj-pompalari',
    'cozumler.html': '/cozumler',
    'cozumler_restoranlar.html': '/cozumler/restoranlar-icin-bulasik-yikama-ve-dozaj-sistemleri',
    'cozumler_oteller.html': '/cozumler/oteller-icin-endustriyel-hijyen-cozumleri',
    'cozumler_toplu_yemek.html': '/cozumler/toplu-yemek-isletmeleri-icin-dozaj-sistemleri',
    'urun_seko_pr4.html': '/urunler/seko-pr4-deterjan-pompasi',
    'urun_atiker_apm_0300.html': '/urunler/atiker-apm-0300-deterjan-parlatici-pompasi',
    'urun_kirec_sokucu.html': '/urunler/endustriyel-kirec-sokucu',
}
PAGE_PRIORITIES = {
    'index.html': '1.0',
    'urunler.html': '0.9',
    'urunler_bulasikmakineleri.html': '0.8',
    'urunler_kimyasallar.html': '0.8',
    'urunler_pompa.html': '0.8',
    'cozumler.html': '0.8',
    'cozumler_restoranlar.html': '0.7',
    'cozumler_oteller.html': '0.7',
    'cozumler_toplu_yemek.html': '0.7',
    'urun_seko_pr4.html': '0.7',
    'urun_atiker_apm_0300.html': '0.7',
    'urun_kirec_sokucu.html': '0.7',
}
PAGE_SOCIAL_METADATA = {
    'cozumler_restoranlar.html': (
        'website',
        'Restoranlar İçin Bulaşık Yıkama ve Dozaj Sistemleri | DOZATECH',
        'Restoran ve kafeler için endüstriyel bulaşık makinesi, deterjan, parlatıcı ve dozaj pompası ürün gruplarını inceleyin.',
        'https://dozatech.com.tr/assets/images/montaj1.webp',
    ),
    'cozumler_oteller.html': (
        'website',
        'Oteller İçin Endüstriyel Hijyen Çözümleri | DOZATECH',
        'Otellerin profesyonel mutfakları için endüstriyel bulaşık makinesi, dozaj pompası ve hijyen kimyasalı ürün grupları.',
        'https://dozatech.com.tr/assets/images/montaj2.webp',
    ),
    'cozumler_toplu_yemek.html': (
        'website',
        'Toplu Yemek İşletmeleri İçin Dozaj Sistemleri | DOZATECH',
        'Toplu yemek işletmeleri için endüstriyel bulaşık makinesi, dozaj pompası ve hijyen kimyasalı ürün gruplarını inceleyin.',
        'https://dozatech.com.tr/assets/images/makineler_kolaj.webp',
    ),
    'urun_seko_pr4.html': (
        'product',
        'Seko PR4 Deterjan Pompası | Endüstriyel Dozaj | DOZATECH',
        'Bulaşık makineleri için Seko PR4 peristaltik deterjan pompası: IP65 gövde, 230 Vac besleme ve 4 l/saat dozaj kapasitesi.',
        'https://dozatech.com.tr/assets/images/pompa_seko_pr4.webp',
    ),
    'urun_atiker_apm_0300.html': (
        'product',
        'Atiker APM 0300 Deterjan ve Parlatıcı Pompası | DOZATECH',
        'Atiker APM 0300 devir ayarlı deterjan ve parlatıcı pompası; tek su beslemeli makineler için peristaltik dozaj çözümü.',
        'https://dozatech.com.tr/assets/images/pompa_atiker.webp',
    ),
    'urun_kirec_sokucu.html': (
        'product',
        'Endüstriyel Kireç Sökücü | Bulaşık Makinesi Bakımı | DOZATECH',
        'Endüstriyel bulaşık makineleri için güçlü kireç sökücü: rezistans, su kanalı ve püskürtme kollarında biriken kirecin temizlenmesine yardımcı olur.',
        'https://dozatech.com.tr/assets/images/kirecsokucu.webp',
    ),
}
PAGE_BREADCRUMBS = {
    'cozumler_restoranlar.html': [
        ('Ana Sayfa', '/'),
        ('Çözümler', '/cozumler'),
        ('Restoranlar', PAGE_ROUTES['cozumler_restoranlar.html']),
    ],
    'cozumler_oteller.html': [
        ('Ana Sayfa', '/'),
        ('Çözümler', '/cozumler'),
        ('Oteller', PAGE_ROUTES['cozumler_oteller.html']),
    ],
    'cozumler_toplu_yemek.html': [
        ('Ana Sayfa', '/'),
        ('Çözümler', '/cozumler'),
        ('Toplu Yemek', PAGE_ROUTES['cozumler_toplu_yemek.html']),
    ],
    'urun_seko_pr4.html': [
        ('Ana Sayfa', '/'),
        ('Ürünler', '/urunler'),
        ('Dozaj Pompaları', '/urunler/dozaj-pompalari'),
        ('Seko PR4', PAGE_ROUTES['urun_seko_pr4.html']),
    ],
    'urun_atiker_apm_0300.html': [
        ('Ana Sayfa', '/'),
        ('Ürünler', '/urunler'),
        ('Dozaj Pompaları', '/urunler/dozaj-pompalari'),
        ('Atiker APM 0300', PAGE_ROUTES['urun_atiker_apm_0300.html']),
    ],
    'urun_kirec_sokucu.html': [
        ('Ana Sayfa', '/'),
        ('Ürünler', '/urunler'),
        ('Kimyasallar', '/urunler/kimyasallar'),
        ('Kireç Sökücü', PAGE_ROUTES['urun_kirec_sokucu.html']),
    ],
}

def print_step(message):
    print(f"\033[1;34m[BUILD]\033[0m {message}", flush=True)


def get_source_html_files():
    return sorted(filename for filename in os.listdir('.') if filename.endswith('.html'))


def validate_source_pages():
    source_files = set(get_source_html_files())
    configured_files = set(PAGE_ROUTES)
    missing_files = sorted(configured_files - source_files)
    unexpected_files = sorted(source_files - configured_files - NON_ROUTE_HTML_FILES)

    if missing_files or unexpected_files:
        details = []
        if missing_files:
            details.append(f"missing configured pages: {', '.join(missing_files)}")
        if unexpected_files:
            details.append(f"unregistered pages: {', '.join(unexpected_files)}")
        raise RuntimeError('; '.join(details))

def get_tailwind_cli_name():
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == 'darwin':
        os_name = 'macos'
    elif system == 'linux':
        os_name = 'linux'
    elif system == 'windows':
        os_name = 'windows'
        return 'tailwindcss-windows-x64.exe'
    else:
        print(f"Unsupported OS: {system}")
        sys.exit(1)

    if machine in ['arm64', 'aarch64']:
        arch = 'arm64'
    elif machine in ['x86_64', 'amd64']:
        arch = 'x64'
    else:
        print(f"Unsupported architecture: {machine}")
        sys.exit(1)

    return f"tailwindcss-{os_name}-{arch}"

def download_tailwind_cli(cli_name):
    if os.path.exists(cli_name):
        return

    print_step(f"Downloading Tailwind CLI ({cli_name})...")
    url = f"https://github.com/tailwindlabs/tailwindcss/releases/download/{TAILWIND_VERSION}/{cli_name}"
    try:
        urllib.request.urlretrieve(url, cli_name)
        os.chmod(cli_name, os.stat(cli_name).st_mode | stat.S_IEXEC)
    except Exception as e:
        print(f"Failed to download Tailwind CLI: {e}")
        sys.exit(1)

def get_tailwind_command():
    if os.path.exists(NODE_TAILWIND_CLI):
        print_step("Using project-local Tailwind CLI...")
        return NODE_TAILWIND_CLI

    cli_name = get_tailwind_cli_name()
    download_tailwind_cli(cli_name)
    return f"./{cli_name}"

def clean_dist():
    print_step("Cleaning dist directory...")
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)
    os.makedirs(os.path.join(DIST_DIR, 'css'))

def build_css():
    cli_path = get_tailwind_command()

    print_step("Compiling Tailwind CSS...")

    try:
        subprocess.run([
            cli_path, 
            '-i', SRC_CSS, 
            '-o', f'{DIST_DIR}/css/style.css', 
            '--minify'
        ], check=True)
    except OSError as e:
        print(f"Error executing Tailwind CLI: {e}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error building CSS: {e}")
        sys.exit(1)


def get_css_version():
    with open(os.path.join(DIST_DIR, 'css', 'style.css'), 'rb') as css_file:
        return hashlib.sha256(css_file.read()).hexdigest()[:12]


def load_analytics_code():
    analytics_path = os.path.join('src', 'analytics.html')
    if not os.path.exists(analytics_path):
        return ''
    with open(analytics_path, 'r', encoding='utf-8') as analytics_file:
        return analytics_file.read()


def inject_social_metadata(content, filename):
    metadata = PAGE_SOCIAL_METADATA.get(filename)
    if not metadata or 'property="og:type"' in content:
        return content

    og_type, title, description, image = metadata
    tags = f'''
    <meta property="og:type" content="{og_type}">
    <meta property="og:url" content="{BASE_URL}{PAGE_ROUTES[filename]}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{image}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{image}">
    '''
    return content.replace('</head>', f'{tags}</head>', 1)


def inject_breadcrumb_schema(content, filename):
    breadcrumbs = PAGE_BREADCRUMBS.get(filename)
    if not breadcrumbs or '"BreadcrumbList"' in content:
        return content

    item_list = [
        {
            '@type': 'ListItem',
            'position': position,
            'name': name,
            'item': f'{BASE_URL}{path}',
        }
        for position, (name, path) in enumerate(breadcrumbs, start=1)
    ]
    schema = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': item_list,
    }
    script = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'
    return content.replace('</head>', f'{script}</head>', 1)


def get_mobile_navigation_markup():
    return '''
    <button id="mobile-menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menüyü aç" class="md:hidden mt-4 w-full border border-gray-200 rounded-lg px-4 py-3 text-gray-700 font-semibold text-left">
        Menü
    </button>
    <div id="mobile-menu" aria-hidden="true" class="hidden md:hidden bg-white border-t border-gray-100 mt-3">
        <a href="/" class="block py-3 px-4 text-gray-700 hover:bg-gray-100">Ana Sayfa</a>
        <a href="/urunler" class="block py-3 px-4 text-gray-700 hover:bg-gray-100">Ürünler</a>
        <a href="/cozumler" class="block py-3 px-4 text-gray-700 hover:bg-gray-100">Çözümler</a>
        <a href="/#iletisim" class="block py-3 px-4 text-gray-700 hover:bg-gray-100">İletişim</a>
    </div>'''


def normalize_mobile_navigation(content, filename):
    if filename in NON_ROUTE_HTML_FILES:
        return content

    content = re.sub(
        r'\s+onclick="document\.getElementById\(\'mobile-menu\'\)\.classList\.toggle\(\'hidden\'\)"',
        '',
        content,
    )

    def add_button_attributes(match):
        button = match.group(0)
        attributes = {
            'aria-expanded': 'false',
            'aria-controls': 'mobile-menu',
            'aria-label': 'Menüyü aç',
            'type': 'button',
        }
        for attribute, value in attributes.items():
            if f'{attribute}=' not in button:
                button = button[:-1] + f' {attribute}="{value}"' + '>'
        return button

    content = re.sub(
        r'<button\b[^>]*\bid="mobile-menu-btn"[^>]*>',
        add_button_attributes,
        content,
        flags=re.IGNORECASE,
    )
    if 'id="mobile-menu-btn"' not in content:
        navigation = get_mobile_navigation_markup()
        header_marker = '</div></header>'
        if header_marker in content:
            content = content.replace(header_marker, f'{navigation}{header_marker}', 1)
        else:
            content = content.replace('</header>', f'{navigation}</header>', 1)
    return content


def secure_external_links(content):
    def add_noopener(match):
        anchor = match.group(0)
        if re.search(r'\brel=', anchor, flags=re.IGNORECASE):
            return anchor
        return anchor[:-1] + ' rel="noopener noreferrer">'

    return re.sub(
        r'<a\b[^>]*target="_blank"[^>]*>',
        add_noopener,
        content,
        flags=re.IGNORECASE,
    )


def add_image_decoding_hint(content):
    def add_decoding(match):
        image = match.group(0)
        if 'decoding=' in image:
            return image
        return image[:-1] + ' decoding="async">'

    return re.sub(r'<img\b[^>]*>', add_decoding, content, flags=re.IGNORECASE)


def add_font_resource_hints(content):
    if 'fonts.googleapis.com' not in content or 'rel="preconnect"' in content:
        return content

    hints = '''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    '''
    return content.replace('</head>', f'{hints}</head>', 1)

def minify_html_fragment(content: str) -> str:
    content = re.sub(r'<!--(.*?)-->', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    return re.sub(r'> <', '><', content)


def minify_html(content: str) -> str:
    protected_block_pattern = re.compile(
        r'(<(?:script|style)\b[^>]*>)(.*?)(</(?:script|style)>)',
        flags=re.DOTALL | re.IGNORECASE,
    )
    minified_parts: list[str] = []
    last_index = 0

    for match in protected_block_pattern.finditer(content):
        minified_parts.append(minify_html_fragment(content[last_index:match.start()]))
        minified_parts.append(f'{match.group(1)}{match.group(2).strip()}{match.group(3)}')
        last_index = match.end()

    minified_parts.append(minify_html_fragment(content[last_index:]))
    return ''.join(minified_parts).strip()

def get_public_page_path(filename):
    return PAGE_ROUTES.get(filename, f'/{filename}')


def write_clean_route(filename: str, content: str) -> None:
    public_path = get_public_page_path(filename).strip('/')
    if not public_path:
        return

    route_dir = os.path.join(DIST_DIR, public_path)
    os.makedirs(route_dir, exist_ok=True)

    with open(os.path.join(route_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(content)


def process_html():
    print_step("Processing and Minifying HTML files...")
    html_files = get_source_html_files()
    css_version = get_css_version()
    analytics_code = load_analytics_code()
    
    for filename in html_files:
        print(f"  - Processing {filename}...")
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Nested clean URLs must resolve assets and CSS from the site root.
        content = content.replace('dist/css/style.css', f'/css/style.css?v={css_version}')
        content = LEGACY_ANALYTICS_PATTERN.sub('', content)
        content = inject_social_metadata(content, filename)
        content = inject_breadcrumb_schema(content, filename)
        content = normalize_mobile_navigation(content, filename)
        content = secure_external_links(content)
        content = add_image_decoding_hint(content)
        content = add_font_resource_hints(content)

        # INJECT SECURITY HEADERS
        security_headers = """
    <!-- Security Headers -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; base-uri 'self'; object-src 'none'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' https://placehold.co data:; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com; connect-src 'self' https://formspree.io https://www.google-analytics.com https://region1.google-analytics.com https://www.google.com; form-action 'self' https://formspree.io;">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">
        """
        if '<head>' in content:
            content = content.replace('<head>', '<head>' + analytics_code + security_headers)
        
        # Minify
        minified_content = minify_html(content)
        
        # Write to dist
        dest_path = os.path.join(DIST_DIR, filename)
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(minified_content)

        if filename in PAGE_ROUTES:
            write_clean_route(filename, minified_content)


def get_lastmod(filename):
    configured_date = os.getenv('SITE_LASTMOD', '').strip()
    if configured_date and re.fullmatch(r'\d{4}-\d{2}-\d{2}', configured_date):
        return configured_date

    git_result = subprocess.run(
        ['git', 'log', '-1', '--format=%cs', '--', filename],
        capture_output=True,
        text=True,
        check=False,
    )
    git_date = git_result.stdout.strip()
    if git_date:
        return git_date

    modified_at = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(
        modified_at, tz=datetime.timezone.utc
    ).date().isoformat()

def generate_sitemap_and_robots():
    print_step("Generating sitemap.xml and robots.txt...")
    html_files = get_source_html_files()
    
    # 1. robots.txt
    shutil.copyfile('robots.txt', os.path.join(DIST_DIR, 'robots.txt'))
        
    # 2. sitemap.xml
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    ordered_files = [filename for filename in PAGE_ROUTES if filename in html_files]
    remaining_files = []

    for filename in ordered_files + remaining_files:
        priority = PAGE_PRIORITIES.get(filename, "0.8")
        public_path = get_public_page_path(filename)
        date_str = get_lastmod(filename)
        xml_content += f'  <url>\n'
        xml_content += f'    <loc>{BASE_URL}{public_path}</loc>\n'
        xml_content += f'    <lastmod>{date_str}</lastmod>\n'
        xml_content += f'    <changefreq>weekly</changefreq>\n'
        xml_content += f'    <priority>{priority}</priority>\n'
        xml_content += f'  </url>\n'
        
    xml_content += '</urlset>'
    
    with open(os.path.join(DIST_DIR, 'sitemap.xml'), 'w') as f:
        f.write(xml_content)

def copy_assets():
    print_step("Copying Assets...")
    if os.path.exists(ASSETS_DIR):
        shutil.copytree(ASSETS_DIR, os.path.join(DIST_DIR, 'assets'), dirs_exist_ok=True)

def main():
    print_step("Starting Build Process...")
    validate_source_pages()
    clean_dist()
    build_css()
    process_html()
    generate_sitemap_and_robots()
    copy_assets()
    print_step("Build Complete! Production files are in 'dist/' folder.")

if __name__ == '__main__':
    main()
