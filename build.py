import os
import re
import shutil
import subprocess
import sys

# Configuration
import platform
import urllib.request
import stat

# Configuration
DIST_DIR = 'dist'
SRC_CSS = 'src/css/input.css'
ASSETS_DIR = 'assets'
TAILWIND_VERSION = 'v3.4.17'
NODE_TAILWIND_CLI = os.path.join('node_modules', '.bin', 'tailwindcss')

def print_step(message):
    print(f"\033[1;34m[BUILD]\033[0m {message}", flush=True)

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

def minify_html(content):
    # Remove HTML Comments
    content = re.sub(r'<!--(.*?)-->', '', content, flags=re.DOTALL)
    
    # Simple Minification: 
    # 1. Replace multiple spaces/newlines with single space
    content = re.sub(r'\s+', ' ', content)
    # 2. Remove space between tags
    content = re.sub(r'> <', '><', content)
    
    return content.strip()

def process_html():
    print_step("Processing and Minifying HTML files...")
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        print(f"  - Processing {filename}...")
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # FIX PATHS FOR DIST
        # 1. CSS Path: 'dist/css/style.css' -> 'css/style.css'
        # 1. CSS Path: 'dist/css/style.css' -> 'css/style.css'
        import time
        timestamp = int(time.time())
        content = content.replace('dist/css/style.css', f'css/style.css?v={timestamp}')

        # INJECT SECURITY HEADERS (Skill: security-auditor)
        # Updated CSP to allow Google Analytics and GTM
        security_headers = """
    <!-- Security Headers -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self' https:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' https: data: https://www.google-analytics.com; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com; connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com;">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">
        """
        if '<head>' in content:
            # Inject Analytics Code (Skill: growth-hacker)
            analytics_code = ""
            if os.path.exists('src/analytics.html'):
                with open('src/analytics.html', 'r', encoding='utf-8') as af:
                    analytics_code = af.read()
            
            content = content.replace('<head>', '<head>' + analytics_code + security_headers)
        
        # Minify
        minified_content = minify_html(content)
        
        # Write to dist
        dest_path = os.path.join(DIST_DIR, filename)
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(minified_content)

def generate_sitemap_and_robots():
    print_step("Generating sitemap.xml and robots.txt...")
    base_url = "https://dozatech.com.tr"
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # 1. robots.txt
    robots_content = f"""User-agent: *
Allow: /
Sitemap: {base_url}/sitemap.xml
"""
    with open(os.path.join(DIST_DIR, 'robots.txt'), 'w') as f:
        f.write(robots_content)
        
    # 2. sitemap.xml
    import datetime
    date_str = datetime.date.today().isoformat()
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for filename in html_files:
        priority = "1.0" if filename == "index.html" else "0.8"
        xml_content += f'  <url>\n'
        xml_content += f'    <loc>{base_url}/{filename}</loc>\n'
        xml_content += f'    <lastmod>{date_str}</lastmod>\n'
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
    clean_dist()
    build_css()
    process_html()
    generate_sitemap_and_robots()
    copy_assets()
    print_step("Build Complete! Production files are in 'dist/' folder.")

if __name__ == '__main__':
    main()
