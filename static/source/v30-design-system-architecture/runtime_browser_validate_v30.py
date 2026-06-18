from __future__ import annotations
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
import json, sys

ROOT=Path(__file__).resolve().parents[2]
results={'version':'30.0.0','performed':True,'browser':'Chromium system executable','checks':{},'console_errors':[],'page_errors':[],'external_requests':[],'status':'failed'}

def record(name, value, detail=None):
    results['checks'][name]={'passed':bool(value),'detail':detail}

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def handler(*args, **kwargs):
    return QuietHandler(*args, directory=str(ROOT), **kwargs)

server=ThreadingHTTPServer(('127.0.0.1', 0), handler)
thread=Thread(target=server.serve_forever, daemon=True)
thread.start()
url=f'http://127.0.0.1:{server.server_port}/index.html'
try:
  with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    context=browser.new_context(reduced_motion='reduce')
    page=context.new_page()
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(15000)
    page.on('console',lambda msg: results['console_errors'].append(msg.text) if msg.type=='error' else None)
    page.on('pageerror',lambda err: results['page_errors'].append(str(err)))
    def on_request(req):
      if not req.url.startswith(f'http://127.0.0.1:{server.server_port}/'):
        results['external_requests'].append(req.url)
    page.on('request',on_request)
    print('runtime: load', flush=True)
    page.goto(url,wait_until='load')
    page.wait_for_timeout(500)
    record('page_loaded',page.locator('body[data-workbook-version="30.0.0"]').count()==1)
    record('main_lessons_21',page.locator('article.lesson[data-lesson]').count()==21,page.locator('article.lesson[data-lesson]').count())
    record('supplementary_lessons_7',page.locator('article.lesson:not([data-lesson])').count()==7,page.locator('article.lesson:not([data-lesson])').count())
    record('stations_6',page.locator('.station').count()==6,page.locator('.station').count())
    record('step_throughs_7',page.locator('[data-step-through-v2]').count()==7,page.locator('[data-step-through-v2]').count())
    ready=page.locator('[data-step-through-v2][data-stv2-ready="1"]').count()
    record('step_throughs_initialized',ready==7,ready)
    record('no_autoplay',page.locator('audio[autoplay],video[autoplay]').count()==0)

    print('runtime: structure', flush=True)
    # Deep link opens ancestor details.
    page.evaluate("location.hash='#stv2-literal-to-system'")
    page.wait_for_timeout(100)
    record('deep_link_opens_details',page.locator('#stv2-literal-to-system').evaluate('(el)=>el.open===true'))

    print('runtime: deep-link', flush=True)
    # New Step-Through A: reveal, next, keyboard, reset, persistence.
    root=page.locator('#stv2-literal-to-system [data-step-through-v2]')
    page.locator('#stv2-literal-to-system [data-stv2-reveal]').click()
    page.locator('#stv2-literal-to-system [data-stv2-next]').click()
    count2=page.locator('#stv2-literal-to-system [data-stv2-count]').inner_text()
    record('literal_to_system_next',('2' in count2),count2)
    page.locator('#stv2-literal-to-system [data-stv2-reveal]').click()
    root.focus(); page.keyboard.press('ArrowRight')
    count3=page.locator('#stv2-literal-to-system [data-stv2-count]').inner_text()
    record('literal_to_system_keyboard',('3' in count3),count3)
    storage=page.evaluate("JSON.parse(localStorage.getItem('elementor-v4-workbook:v30:stv2:stv2-literal-to-system'))")
    record('literal_to_system_persistence',isinstance(storage,dict) and storage.get('index')==2,storage)
    page.locator('#stv2-literal-to-system [data-stv2-reset]').click()
    count1=page.locator('#stv2-literal-to-system [data-stv2-count]').inner_text()
    record('literal_to_system_reset',('1' in count1),count1)

    print('runtime: step-a', flush=True)
    # New Step-Through B calculation module.
    page.evaluate("location.hash='#stv2-unit-selection-tradeoffs'")
    page.wait_for_timeout(100)
    page.locator('#stv2-unit-selection-tradeoffs [data-stv2-reveal]').click()
    page.locator('#stv2-unit-selection-tradeoffs [data-stv2-next]').click()
    record('unit_tradeoff_progress', '2' in page.locator('#stv2-unit-selection-tradeoffs [data-stv2-count]').inner_text())
    record('unit_tradeoff_visual_rendered',page.locator('#stv2-unit-selection-tradeoffs [data-stv2-visual] > *').count()>0)

    print('runtime: step-b', flush=True)
    # Expanded class simulator has 7 progress max and renders custom states after repeated reveal/next.
    page.evaluate("location.hash='#stv2-class-priority'"); page.wait_for_timeout(100)
    maxval=page.locator('#stv2-class-priority [data-stv2-progress]').get_attribute('max')
    record('class_simulator_7_states',maxval=='7',maxval)
    for _ in range(5):
      page.locator('#stv2-class-priority [data-stv2-reveal]').click()
      page.locator('#stv2-class-priority [data-stv2-next]').click()
    title=page.locator('#stv2-class-priority [data-stv2-title]').inner_text()
    record('class_simulator_custom_css_state','Custom CSS' in title,title)

    print('runtime: class-simulator', flush=True)
    # Themes, focus, and progress controls remain operational.
    before=page.locator('html').get_attribute('data-theme')
    page.locator('#themeToggle').evaluate('(el)=>el.click()'); after=page.locator('html').get_attribute('data-theme')
    record('theme_toggle_operational',before!=after,(before,after))
    page.locator('#focusToggle').evaluate('(el)=>el.click()')
    record('focus_mode_operational',page.locator('body').get_attribute('data-focus-mode')=='true' or page.locator('body').get_attribute('data-focus')=='true' or 'focus-mode' in (page.locator('body').get_attribute('class') or ''), {'body_attrs':page.locator('body').evaluate('(e)=>({focus:e.dataset.focusMode,cls:e.className})')})

    print('runtime: ui-controls', flush=True)
    # Reduced motion is checked in the actual workbook context. Print fallback is
    # computed in a lightweight page using the exact workbook stylesheet, avoiding
    # an expensive full-document print layout of 446 disclosures in CI.
    reduced=page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")
    record('reduced_motion_media_active',reduced,reduced)
    css_text=(ROOT/'assets/css/workbook.css').read_text(encoding='utf-8').replace('</style>', r'<\/style>')
    print_page=context.new_page()
    print_page.set_default_timeout(5000)
    print_page.set_content(f'<style>{css_text}</style><div class="stv2-print-all">print fallback</div>', wait_until='load')
    print_page.emulate_media(media='print', reduced_motion='reduce')
    display=print_page.locator('.stv2-print-all').evaluate('(el)=>getComputedStyle(el).display')
    record('print_fallback_visible',display!='none',display)
    print_page.close()

    print('runtime: print-motion', flush=True)
    record('aria_live_present',page.locator('[data-step-through-v2] [aria-live="polite"]').count()>=14,page.locator('[data-step-through-v2] [aria-live="polite"]').count())
    record('all_details_have_summary',page.locator('details').count()==page.locator('details > summary').count(),(page.locator('details').count(),page.locator('details > summary').count()))
    record('no_external_network_requests',len(results['external_requests'])==0,results['external_requests'])
    record('no_console_errors',len(results['console_errors'])==0,results['console_errors'])
    record('no_page_errors',len(results['page_errors'])==0,results['page_errors'])
    print('runtime: final-checks', flush=True)
    browser.close()
finally:
  server.shutdown()
  server.server_close()

failed=[k for k,v in results['checks'].items() if not v['passed']]
results['status']='passed' if not failed else 'failed'
results['failed_checks']=failed
out=ROOT/'source/v30-design-system-architecture/runtime_browser_validation_v30.json'
out.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'source/v30-design-system-architecture/runtime_browser_validation_v30.log').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=False,indent=2))
if failed: sys.exit(1)
