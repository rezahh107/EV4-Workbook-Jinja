from __future__ import annotations

from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'source/v31-conceptual-reference/runtime_browser_validation_v31.json'
LOG = ROOT / 'source/v31-conceptual-reference/runtime_browser_validation_v31.log'

results = {
    'version': '31.0.0',
    'performed': True,
    'browser': 'Chromium system executable',
    'checks': {},
    'console_errors': [],
    'page_errors': [],
    'external_requests': [],
    'status': 'failed',
}

def record(name, passed, detail=None):
    results['checks'][name] = {'passed': bool(passed), 'detail': detail}

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def handler(*args, **kwargs):
    return QuietHandler(*args, directory=str(ROOT), **kwargs)

def build_inline_document() -> str:
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    for node in soup.find_all('link', rel=lambda value: value and ('stylesheet' in value or 'manifest' in value)):
        node.decompose()
    for node in soup.find_all('script', src=True):
        node.decompose()
    style = soup.new_tag('style')
    style.string = (ROOT / 'assets/css/workbook.css').read_text(encoding='utf-8')
    soup.head.append(style)
    placeholder = 'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%221%22 height=%221%22/%3E'
    for img in soup.find_all('img'):
        img['src'] = placeholder
        img.attrs.pop('srcset', None)
    script = soup.new_tag('script')
    script.string = (ROOT / 'assets/js/workbook.js').read_text(encoding='utf-8')
    soup.body.append(script)
    return str(soup)

INLINE_DOCUMENT = build_inline_document()

server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()
base = ROOT.as_uri().rstrip('/') + '/'
http_base = f'http://127.0.0.1:{server.server_port}/'

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox', '--disable-dev-shm-usage'])
        context = browser.new_context(viewport={'width': 1366, 'height': 900}, reduced_motion='reduce')
        page = context.new_page()
        page.set_default_timeout(8000)
        page.set_default_navigation_timeout(20000)
        page.on('console', lambda msg: results['console_errors'].append(msg.text) if msg.type == 'error' else None)
        page.on('pageerror', lambda err: results['page_errors'].append(str(err)))
        page.on('request', lambda req: results['external_requests'].append(req.url) if not req.url.startswith(('data:', 'about:')) else None)
        page.set_content(INLINE_DOCUMENT, wait_until='load')
        page.wait_for_timeout(700)

        record('page_loaded_v31', page.locator('body[data-workbook-version="31.0.0"]').count() == 1)
        record('conceptual_references_28', page.locator('details.conceptual-reference').count() == 28, page.locator('details.conceptual-reference').count())
        record('structured_sections_377', page.locator('details.conceptual-reference .concept-reference-part').count() == 377, page.locator('details.conceptual-reference .concept-reference-part').count())
        record('all_references_initially_closed', page.locator('details.conceptual-reference[open]').count() == 0, page.locator('details.conceptual-reference[open]').count())

        # Direct interaction preserves disclosure behavior.
        first = page.locator('#lesson-1-concept-reference')
        first.locator(':scope > summary').click()
        record('reference_opens_by_click', first.evaluate('(el) => el.open === true'))
        first_text = first.locator('.concept-reference-body').inner_text()
        record('complete_reference_content_loaded', len(first_text) > 5000 and 'ساختن یک شهر' in first_text and 'منابع رسمی' in first_text, len(first_text))

        # Deep link opens the target and its ancestor details.
        page.evaluate("location.hash='#concept-v31-15-section-03'")
        page.wait_for_timeout(250)
        rtl_ref = page.locator('#lesson-15-concept-reference')
        record('deep_link_opens_reference', rtl_ref.evaluate('(el) => el.open === true'))
        record('deep_link_target_visible', page.locator('#concept-v31-15-section-03').is_visible())

        # Existing interactive framework still initializes.
        ready = page.locator('[data-step-through-v2][data-stv2-ready="1"]').count()
        record('step_throughs_initialized_7', ready == 7, ready)
        before = page.locator('html').get_attribute('data-theme')
        page.locator('#themeToggle').evaluate('(el)=>el.click()')
        after = page.locator('html').get_attribute('data-theme')
        record('theme_toggle_preserved', before != after, [before, after])

        # Mobile containment of long-form content, code and tables.
        mobile = context.new_page()
        mobile.set_viewport_size({'width': 390, 'height': 844})
        mobile.on('console', lambda msg: results['console_errors'].append('mobile:' + msg.text) if msg.type == 'error' else None)
        mobile.on('pageerror', lambda err: results['page_errors'].append('mobile:' + str(err)))
        mobile.set_content(INLINE_DOCUMENT, wait_until='load')
        mobile.evaluate("location.hash='#lesson-15-concept-reference'")
        mobile.wait_for_timeout(500)
        mobile.locator('#lesson-15-concept-reference > summary').click()
        mobile.wait_for_timeout(150)
        dims = mobile.evaluate('''() => ({
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          tableWrappers: [...document.querySelectorAll('#lesson-15-concept-reference .concept-table-scroll')].map(x => ({scrollWidth:x.scrollWidth, clientWidth:x.clientWidth})),
          codeBlocks: [...document.querySelectorAll('#lesson-15-concept-reference pre')].map(x => ({scrollWidth:x.scrollWidth, clientWidth:x.clientWidth}))
        })''')
        record('mobile_page_no_global_horizontal_overflow', dims['scrollWidth'] <= dims['clientWidth'] + 2, dims)
        record('mobile_tables_contained', all(x['clientWidth'] <= dims['clientWidth'] and x['scrollWidth'] >= x['clientWidth'] for x in dims['tableWrappers']), dims['tableWrappers'])
        record('mobile_code_contained', all(x['clientWidth'] <= dims['clientWidth'] for x in dims['codeBlocks']), dims['codeBlocks'])
        mobile.close()

        # Print stylesheet exposes conceptual references without scripting.
        print_page = context.new_page()
        css_text = (ROOT / 'assets/css/workbook.css').read_text(encoding='utf-8').replace('</style>', r'<\/style>')
        print_page.set_content(f'<style>{css_text}</style><details class="conceptual-reference"><summary>مرجع</summary><div class="concept-reference-body">متن</div></details>', wait_until='load')
        print_page.emulate_media(media='print', reduced_motion='reduce')
        display = print_page.locator('.concept-reference-body').evaluate('(el) => getComputedStyle(el).display')
        record('print_reference_visible', display != 'none', display)
        print_page.close()

        record('no_external_network_requests', not results['external_requests'], results['external_requests'])
        record('no_console_errors', not results['console_errors'], results['console_errors'])
        record('no_page_errors', not results['page_errors'], results['page_errors'])
        browser.close()
finally:
    server.shutdown()
    server.server_close()

failed = [name for name, item in results['checks'].items() if not item['passed']]
results['failed_checks'] = failed
results['status'] = 'passed' if not failed else 'failed'
OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
LOG.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(results, ensure_ascii=False, indent=2))
if failed:
    sys.exit(1)
