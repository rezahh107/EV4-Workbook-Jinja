from __future__ import annotations
from bs4 import BeautifulSoup
from pathlib import Path
from collections import Counter
import json, re, urllib.parse, xml.etree.ElementTree as ET, subprocess, sys, hashlib, zipfile

ROOT=Path(__file__).resolve().parents[2]
HTML=ROOT/'index.html'
CSS=ROOT/'assets/css/workbook.css'
JS=ROOT/'assets/js/workbook.js'
text=HTML.read_text(encoding='utf-8')
soup=BeautifulSoup(text,'html.parser')
css=CSS.read_text(encoding='utf-8')
js=JS.read_text(encoding='utf-8')
errors=[]; warnings=[]
checks={}

def check(name, condition, detail=None):
    checks[name]=bool(condition)
    if not condition: errors.append(f'{name}: {detail or "failed"}')

# Structure
primary=soup.select('article.lesson[data-lesson]')
supp=[a for a in soup.select('article.lesson') if not a.has_attr('data-lesson')]
check('lesson_article_count_21',len(primary)==21,len(primary))
check('supplementary_lesson_count_7',len(supp)==7,len(supp))
check('station_count_6',len(soup.select('.station'))==6,len(soup.select('.station')))
check('primary_main_count_1',len(soup.find_all('main'))==1,len(soup.find_all('main')))
check('architecture_primer_present',soup.find(id='architecture-primer-v30') is not None)
check('architecture_primer_unnumbered',soup.find(id='architecture-primer-v30') is not None and not soup.find(id='architecture-primer-v30').has_attr('data-lesson'))
if soup.find(id='lesson-1') and soup.find(id='architecture-primer-v30') and soup.find(id='lesson-2'):
    sequence=[x.get('id') for x in soup.find('main').find_all(['article'],recursive=False)]
    check('architecture_primer_position',sequence.index('lesson-1') < sequence.index('architecture-primer-v30') < sequence.index('lesson-2'),sequence)
else: check('architecture_primer_position',False,'missing anchors')
check('settings_values_units_sections_count_28',len(soup.select('details.settings-values-units'))==28,len(soup.select('details.settings-values-units')))
check('unit_strategy_atlas_present',soup.find(id='appendix-v29-units-atlas') is not None and 'Unit Strategy' in soup.find(id='appendix-v29-units-atlas').get_text(' ',strip=True))
check('no_duplicate_unit_atlas',len(soup.select('.units-atlas'))==1,len(soup.select('.units-atlas')))
for req in ['anatomy-of-a-value-v30','unit-selection-framework-v30','unit-value-smells-v30','design-system-decision-layer-v30']:
    check(req+'_present',soup.find(id=req) is not None)

# Core architecture visuals
for req in ['v3v4-svg-title','dependency-svg-title','conflict-svg-title','component-life-title','value-anatomy-title','unit-tree-title']:
    check('svg_'+req,soup.find(id=req) is not None)
for svg in soup.find_all('svg'):
    title=svg.find('title'); desc=svg.find('desc')
    if not title or not desc: errors.append('inline_svg_missing_title_or_desc')
    try: ET.fromstring(str(svg))
    except Exception as e: errors.append(f'inline_svg_parse: {e}')
check('design_dependency_graph_present',soup.find(id='dependency-svg-title') is not None)
check('style_conflict_resolution_map_present',soup.find(id='conflict-svg-title') is not None)
primer=soup.find(id='architecture-primer-v30')
primer_text=primer.get_text(' ',strip=True) if primer else ''
check('dependency_graph_not_presented_as_css_cascade','Dependency map' in primer_text and 'قانون اجباری یا ترتیب cascade نیست' in primer_text)
check('planned_and_discovery_workflows_present','Planned workflow' in primer_text and 'Discovery workflow' in primer_text)

# Step-Through configs
configs=[]
for root in soup.select('[data-step-through-v2]'):
    sc=root.select_one('.stv2-config')
    try: cfg=json.loads(sc.string or sc.get_text())
    except Exception as e: errors.append(f'stv2_json:{e}'); continue
    configs.append(cfg)
    for key in ['id','title','goal','renderer','storage_key','states']:
        if key not in cfg: errors.append(f'stv2_missing_{key}:{cfg.get("id")}')
    if not cfg.get('storage_key'): errors.append(f'stv2_no_storage:{cfg.get("id")}')
    for st in cfg.get('states',[]):
        for key in ['id','phase','title','summary','explanation','golden_rule','evidence','elementor','computed','visual','prediction']:
            if key not in st: errors.append(f'stv2_state_missing_{key}:{cfg.get("id")}:{st.get("id")}')
        pred=st.get('prediction',{})
        if pred.get('correct',-1) >= len(pred.get('options',[])): errors.append(f'stv2_bad_correct_index:{cfg.get("id")}:{st.get("id")}')
ids_cfg=[x.get('id') for x in configs]
check('step_through_v2_total_7',len(configs)==7,len(configs))
check('new_unit_strategy_step_through_count_at_least_2',all(x in ids_cfg for x in ['stv2-literal-to-system','stv2-unit-selection-tradeoffs']))
for sid in ['stv2-literal-to-system','stv2-unit-selection-tradeoffs']:
    cfg=next((c for c in configs if c.get('id')==sid),None)
    check(sid+'_8_states',cfg is not None and len(cfg['states'])==8,len(cfg['states']) if cfg else None)
    root=soup.select_one(f'[data-stv2-id="{sid}"]')
    for feature,sel in [('prediction','[data-stv2-options]'),('reveal','[data-stv2-reveal]'),('previous','[data-stv2-prev]'),('next','[data-stv2-next]'),('reset','[data-stv2-reset]'),('aria_live','[aria-live]'),('print_fallback','.stv2-print-all')]:
        check(f'{sid}_{feature}',root is not None and root.select_one(sel) is not None)
class_cfg=next((c for c in configs if c.get('id')=='stv2-class-priority'),None)
check('expanded_class_conflict_simulator_present',class_cfg is not None and len(class_cfg.get('states',[]))>=7)
if class_cfg:
    class_blob=json.dumps(class_cfg,ensure_ascii=False)
    for term in ['Global','State','Local','Custom CSS','Computed']:
        check('class_sim_'+re.sub(r'\W+','_',term).strip('_'),term in class_blob)

# Labs
for req in ['variables-architecture-lab-v30','class-architecture-lab-v30','components-lifecycle-lab-v30','dynamic-data-case-study-v30','interactions-lab-v30']:
    check(req+'_present',soup.find(id=req) is not None)

# Official variable types exactly Color, Font, Size
v30dir=ROOT/'source/v30-design-system-architecture'
unit_registry=json.loads((v30dir/'unit_strategy_matrix_v30.json').read_text(encoding='utf-8'))
check('official_variable_types_exact',unit_registry.get('official_variable_types')==['Color','Font','Size'],unit_registry.get('official_variable_types'))
strip=soup.select_one('.official-types-strip')
strip_types=[x.get_text(strip=True) for x in strip.find_all('span')] if strip else []
check('official_variable_types_html_exact',strip_types==['Color','Font','Size'],strip_types)

# Semantic guardrails
lower=text.lower()
for pattern,name in [
 (r'variable\s*=\s*value\s*\+\s*unit','variable_equals_value_plus_unit_universal_claims'),
 (r'نوع رسمی[^<\n]{0,30}space variable','official_space_variable_claim'),
 (r'نوع رسمی[^<\n]{0,30}typography variable','official_typography_variable_claim'),
 (r'همیشه\s+rem','universal_always_rem_claim'),
 (r'هرگز\s+px','universal_never_px_claim'),
 (r'همیشه\s+100vw','universal_100vw_claim')]:
    check(name,re.search(pattern,lower,re.I) is None)
check('variable_named_value_definition','Variable یک مقدار نام‌دار یا reference است' in text)
check('dvh_ui_boundary_present','dvh' in lower and ('همهٔ کنترل' in text or 'every control' in lower) and 'تأیید نشده' in text)
check('component_nesting_insufficient_evidence','Component nesting' in text and 'insufficient_evidence' in text)
# No positive nesting support claim
check('no_unsupported_component_nesting_claim',not re.search(r'component nesting.{0,80}(supported|پشتیبانی می‌شود|مجاز است)',lower,re.S))
check('design_system_import_export_present','یک ZIP شامل Variables و Classes' in text or 'ZIP شامل Variables و Classes' in text)
check('individual_variable_import_claims_zero','import انتخابیِ یک Variable یا Class منفرد پشتیبانی مستند ندارد' in text)
check('hybrid_sync_scope_explained','Global Colors یا Global Fonts' in text and 'Typography محدود' in text)
check('variables_inside_classes_explained','Variable داخل Global Class' in text or 'Class declaration می‌تواند Variable را مصرف کند' in text)
check('loop_grid_and_query_present','Loop Grid' in text and 'Query Source' in text and 'Include' in text and 'Exclude' in text)
check('no_query_loop_product_concept','Query Loop' not in text)
for term in ['Page Load','Scroll Into View','While Scrolling','On Hover','On Click','Fade','Slide','Scale','In، Out','milliseconds']:
    check('interactions_'+re.sub(r'\W+','_',term).strip('_'),term in text)

# Design decision blocks and non-unit types
check('design_system_decision_blocks_present',len(soup.select('details.design-system-decision'))>=15,len(soup.select('details.design-system-decision')))
check('non_unit_lessons_value_types',all(soup.find(id=x) and soup.find(id=x).select_one('.v30-value-type-note') for x in ['lesson-v17-atomic-forms','lesson-v17-advanced','lesson-v19-element-weight']))

# Progressive disclosure and accessibility
all_details=soup.find_all('details')
check('all_non_core_disclosures_closed_by_default',not any(d.has_attr('open') for d in all_details))
check('details_have_summaries',all(d.find('summary',recursive=False) for d in all_details))
check('single_line_summary_min_height_consistent','min-block-size: 2.6rem' in css or 'min-block-size:2.6rem' in css)
check('multi_line_summary_can_grow',not re.search(r'\.lesson-disclosure-summary[^}]*?(?:^|[;{])\s*height\s*:',css,re.S|re.M))
check('deep_links_open_ancestor_disclosures','function revealTarget' in js and 'parent.open = true' in js)
check('print_mode_reveals_content','@media print' in css and '.stv2-print-all { display: block !important; }' in css and 'details.lesson-deep-dive:not([open])' in css)
check('reduced_motion_handling','prefers-reduced-motion' in css)
check('keyboard_support','ArrowLeft' in js and 'ArrowRight' in js)
check('local_progress_persistence','localStorage' in js and all(c.get('storage_key') for c in configs))

# IDs, anchors, assets
all_ids=[x['id'] for x in soup.find_all(id=True)]
dups=[k for k,v in Counter(all_ids).items() if v>1]
check('duplicate_ids_zero',not dups,dups[:20])
idset=set(all_ids); unresolved=[]
for a in soup.find_all('a',href=True):
    h=a['href']
    if h.startswith('#') and h[1:] not in idset: unresolved.append(h)
check('all_internal_links_resolve',not unresolved,unresolved[:20])
external_assets=[]; missing_assets=[]
for tag,attr in [('script','src'),('link','href'),('img','src'),('source','src'),('video','src'),('audio','src')]:
    for node in soup.find_all(tag):
        value=node.get(attr)
        if not value: continue
        if re.match(r'(?i)https?://|//',value): external_assets.append((tag,value))
        elif not value.startswith(('#','data:')):
            target=(ROOT/urllib.parse.unquote(value)).resolve()
            if not target.exists(): missing_assets.append((tag,value))
check('active_external_assets_zero',not external_assets,external_assets[:10])
check('missing_local_assets_zero',not missing_assets,missing_assets[:10])
check('offline_only_behavior',not external_assets and 'fetch(' not in js and 'XMLHttpRequest' not in js)

# Tables and controls
table_errors=[]
for i,t in enumerate(soup.find_all('table'),1):
    if not t.find('caption') or not t.find('thead') or not t.find('tbody'): table_errors.append(i); continue
    if any(not th.get('scope') for th in t.find_all('th')): table_errors.append(i)
    heads=len(t.select('thead tr:last-child th'))
    for tr in t.select('tbody tr'):
        if len(tr.find_all(['th','td'],recursive=False)) != heads: table_errors.append(i); break
check('tables_valid_and_semantically_complete',not table_errors,sorted(set(table_errors))[:30])
unlabeled=[]
for c in soup.find_all(['input','select','textarea']):
    if c.name=='input' and c.get('type')=='hidden': continue
    labeled=bool(c.get('aria-label') or c.get('aria-labelledby') or c.find_parent('label'))
    if not labeled and c.get('id'): labeled=bool(soup.find('label',attrs={'for':c.get('id')}))
    fs=c.find_parent('fieldset'); group=c.find_parent(attrs={'role':re.compile('group|radiogroup')})
    if not labeled and ((fs and fs.find('legend')) or (group and (group.get('aria-label') or group.get('aria-labelledby')))): labeled=True
    if not labeled: unlabeled.append(str(c)[:120])
check('controls_have_labels',not unlabeled,unlabeled[:10])

# JSON, SVG, JS syntax
json_errors=[]
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: json_errors.append((str(p.relative_to(ROOT)),str(e)))
check('json_parse_passed',not json_errors,json_errors[:5])
svg_errors=[]
for p in ROOT.rglob('*.svg'):
    try: ET.parse(p)
    except Exception as e: svg_errors.append((str(p.relative_to(ROOT)),str(e)))
check('svg_files_parse_passed',not svg_errors,svg_errors[:5])
js_errors=[]
for p in ROOT.rglob('*.js'):
    cp=subprocess.run(['node','--check',str(p)],capture_output=True,text=True)
    if cp.returncode: js_errors.append((str(p.relative_to(ROOT)),cp.stderr[:300]))
check('javascript_syntax_passed',not js_errors,js_errors[:5])
ordinary_pre=[]
for pre in soup.find_all('pre'):
    if 'ascii-diagram' in (pre.get('class') or []): continue
    if re.search(r'[\u0600-\u06FF]',pre.get_text()): ordinary_pre.append(pre)
check('ordinary_persian_prose_inside_pre_zero',not ordinary_pre,len(ordinary_pre))

# Preserved source and handoff
base_zip=ROOT/'source/v30-design-system-architecture/implementation-handoff/base/Elementor_V4_Offline_Interactive_Workbook_v29_0_settings_values_units_step_through.zip'
check('v29_base_archive_preserved',base_zip.exists())
if base_zip.exists():
    sha=hashlib.sha256(base_zip.read_bytes()).hexdigest()
    check('v29_base_archive_sha256',sha=='3b0335721d623c477513a56716594cafd4222028b8f0fd316b4180197ea49d58',sha)
for old in ['v17-official-coverage','v18-comparison-cards','v19-element-weight','v20-tuya-rebuild','v21-mental-model-debug','v23-semantic-qa','v24-practical-findings','v25-responsive-tuya','v26-responsive-build-test','v27-step-through-v2','v28-conceptual-reference','v29-settings-values-units']:
    check('preserved_'+old,(ROOT/'source'/old).exists())

# SHA manifest if present (exclude self by convention)
sha_file=ROOT/'SHA256SUMS.txt'
sha_errors=[]
if sha_file.exists():
    for line in sha_file.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        expected,rel=line.split(None,1); rel=rel.strip().lstrip('*')
        p=ROOT/rel
        if not p.exists(): sha_errors.append((rel,'missing')); continue
        got=hashlib.sha256(p.read_bytes()).hexdigest()
        if got!=expected: sha_errors.append((rel,got))
check('sha256_manifest_passed',sha_file.exists() and not sha_errors,sha_errors[:10] if sha_file.exists() else 'missing')

report={
 'version':'30.0.0','source_base':'Elementor_V4_Offline_Interactive_Workbook_v29_0_settings_values_units_step_through.zip',
 'static_validation':{
  'lesson_article_count':len(primary),'supplementary_lesson_count':len(supp),'station_count':len(soup.select('.station')),
  'settings_values_units_sections_count':len(soup.select('details.settings-values-units')),'step_through_v2_total':len(configs),
  'step_through_state_total':sum(len(c.get('states',[])) for c in configs),'details_total':len(all_details),'svg_inline_total':len(soup.find_all('svg')),
  'duplicate_ids':len(dups),'nav_links_unresolved':len(unresolved),'active_external_assets':len(external_assets),'missing_local_assets':len(missing_assets),
  'tables_invalid':len(set(table_errors)),'controls_without_labels':len(unlabeled),'json_parse':'passed' if not json_errors else 'failed','svg_parse':'passed' if not svg_errors else 'failed','javascript_syntax':'passed' if not js_errors else 'failed','sha256_manifest':'passed' if sha_file.exists() and not sha_errors else 'failed'
 },
 'semantic_validation':{k:v for k,v in checks.items() if any(token in k for token in ['official','variable','component','dependency','workflow','lab','query','interaction','claim','decision','dvh','loop_grid','class_sim'])},
 'checks':checks,'warnings':warnings,'errors':errors,'status':'passed' if not errors else 'failed'
}
out=ROOT/'source/v30-design-system-architecture/static_semantic_validation_v30.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors: sys.exit(1)
