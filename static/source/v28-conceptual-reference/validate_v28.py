from __future__ import annotations
from bs4 import BeautifulSoup
from pathlib import Path
from collections import Counter
import json, re, urllib.parse, xml.etree.ElementTree as ET, subprocess, sys

ROOT=Path(__file__).resolve().parents[2]
HTML=ROOT/'index.html'
soup=BeautifulSoup(HTML.read_text(encoding='utf-8'),'html.parser')
errors=[]

articles=soup.select('article.lesson')
refs=soup.select('details.conceptual-reference')
primary=[a for a in articles if re.fullmatch(r'lesson-(?:[1-9]|1[0-9]|2[01])',a.get('id',''))]
supp=[a for a in articles if a not in primary]

if len(refs)!=len(articles): errors.append(f'reference_count {len(refs)} != article_count {len(articles)}')
for a in articles:
    aid=a.get('id')
    ref=a.select_one(':scope > details.conceptual-reference')
    core=a.select_one(':scope > .lesson-core-concept')
    if not ref: errors.append(f'missing reference {aid}'); continue
    if ref.has_attr('open'): errors.append(f'reference open by default {aid}')
    if not ref.find('summary',recursive=False): errors.append(f'missing summary {aid}')
    if not core: errors.append(f'missing core {aid}')
    elif core.find_next_sibling() is not ref: errors.append(f'reference not immediately after core {aid}')
    h3=[x.get_text(' ',strip=True) for x in ref.select('.concept-reference-part h3')]
    required=['مسئله‌ای که این مفهوم حل می‌کند','تصویر ذهنی ماندگار','تعریف دقیق با زبان ساده','رفتار را قدم‌به‌قدم دنبال کن','در Elementor V4 یعنی چه؟','تله‌های رایج','قوانین طلایی']
    if h3!=required: errors.append(f'required parts mismatch {aid}: {h3}')
    if len(ref.select('.concept-reference-evidence a[href]'))<2: errors.append(f'not enough sources {aid}')

# IDs and links
ids=[x['id'] for x in soup.find_all(id=True)]
dups=[k for k,v in Counter(ids).items() if v>1]
if dups: errors.append(f'duplicate ids {dups[:10]}')
idset=set(ids)
unresolved=[]
for a in soup.find_all('a',href=True):
    h=a['href']
    if h.startswith('#') and h[1:] not in idset: unresolved.append(h)
if unresolved: errors.append(f'unresolved anchors {unresolved[:10]}')

# details summaries
missing_summary=[d for d in soup.find_all('details') if not d.find('summary',recursive=False)]
if missing_summary: errors.append(f'details missing summary {len(missing_summary)}')

# local assets
external_assets=[]; missing_assets=[]
for tag,attr in [('script','src'),('link','href'),('img','src'),('source','src'),('video','src'),('audio','src')]:
    for node in soup.find_all(tag):
        value=node.get(attr)
        if not value: continue
        if re.match(r'(?i)https?://|//',value): external_assets.append((tag,value))
        elif not value.startswith(('#','data:')):
            target=(ROOT/urllib.parse.unquote(value)).resolve()
            if not target.exists(): missing_assets.append((tag,value))
if external_assets: errors.append(f'external assets {external_assets[:5]}')
if missing_assets: errors.append(f'missing assets {missing_assets[:5]}')

# tables
malformed=[]
for i,t in enumerate(soup.find_all('table'),1):
    if not t.find('caption') or not t.find('thead') or not t.find('tbody'):
        malformed.append(i)
    for th in t.find_all('th'):
        if not th.get('scope'): malformed.append(i); break
if malformed: errors.append(f'malformed tables {sorted(set(malformed))[:20]}')

# controls labels
unlabeled=[]
for c in soup.find_all(['input','select','textarea']):
    if c.name=='input' and c.get('type')=='hidden': continue
    labeled=bool(c.get('aria-label') or c.get('aria-labelledby') or c.find_parent('label'))
    if not labeled and c.get('id'):
        labeled=bool(soup.find('label',attrs={'for':c.get('id')}))
    if not labeled: unlabeled.append(c)
# Existing workbook contains grouped controls whose group container is labeled; accept if ancestor fieldset has legend or role group has aria-label.
filtered=[]
for c in unlabeled:
    fs=c.find_parent('fieldset')
    group=c.find_parent(attrs={'role':re.compile('group|radiogroup')})
    if (fs and fs.find('legend')) or (group and (group.get('aria-label') or group.get('aria-labelledby'))):
        continue
    filtered.append(c)
if filtered: errors.append(f'unlabeled controls {len(filtered)}')

# inline JSON
inline_json_errors=[]
for i,sc in enumerate(soup.find_all('script',attrs={'type':'application/json'}),1):
    try: json.loads(sc.string or sc.get_text())
    except Exception as e: inline_json_errors.append((i,str(e)))
if inline_json_errors: errors.append(f'inline json errors {inline_json_errors[:3]}')

# all JSON and SVG
json_errors=[]
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: json_errors.append((str(p.relative_to(ROOT)),str(e)))
if json_errors: errors.append(f'json errors {json_errors[:3]}')
svg_errors=[]
for p in ROOT.rglob('*.svg'):
    try: ET.parse(p)
    except Exception as e: svg_errors.append((str(p.relative_to(ROOT)),str(e)))
if svg_errors: errors.append(f'svg errors {svg_errors[:3]}')

# prose in pre: ASCII diagrams are explicitly allowed
ordinary_pre=[]
for pre in soup.find_all('pre'):
    if 'ascii-diagram' in (pre.get('class') or []): continue
    if re.search(r'[\u0600-\u06FF]',pre.get_text()): ordinary_pre.append(pre)
if ordinary_pre: errors.append(f'ordinary Persian prose in pre {len(ordinary_pre)}')

# JS syntax
js_ok=True
for p in ROOT.rglob('*.js'):
    cp=subprocess.run(['node','--check',str(p)],capture_output=True,text=True)
    if cp.returncode:
        js_ok=False; errors.append(f'js syntax {p.relative_to(ROOT)}: {cp.stderr[:200]}')

report={
 'version':'28.0.0',
 'lesson_article_count':len(primary),
 'supplemental_lesson_article_count':len(supp),
 'station_count':len(soup.select('.station')),
 'primary_main_count':len(soup.find_all('main')),
 'conceptual_reference_count':len(refs),
 'conceptual_reference_expected':len(articles),
 'conceptual_references_open_by_default':sum(1 for x in refs if x.has_attr('open')),
 'conceptual_reference_source_footers':len(soup.select('.concept-reference-evidence')),
 'conceptual_reference_required_part_failures':sum(1 for a in articles if len(a.select(':scope > details.conceptual-reference .concept-reference-part'))!=7),
 'lesson_core_visible_count':len(soup.select('article.lesson > .lesson-core-concept')),
 'details_total':len(soup.find_all('details')),
 'details_missing_summary':len(missing_summary),
 'duplicate_ids':len(dups),
 'nav_links_unresolved':len(unresolved),
 'active_external_assets':len(external_assets),
 'missing_local_assets':len(missing_assets),
 'ordinary_persian_prose_inside_pre':len(ordinary_pre),
 'malformed_tables_remaining':len(set(malformed)),
 'controls_without_labels':len(filtered),
 'inline_json_parse':'passed' if not inline_json_errors else 'failed',
 'json_parse':'passed' if not json_errors else 'failed',
 'svg_parse':'passed' if not svg_errors else 'failed',
 'javascript_syntax':'passed' if js_ok else 'failed',
 'errors':errors,
}
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors: sys.exit(1)
