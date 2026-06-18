from __future__ import annotations

from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import hashlib
import json
import re
import subprocess
import sys
import mistune

ROOT = Path(__file__).resolve().parents[2]
V31 = ROOT / 'source/v31-conceptual-reference'
HTML = ROOT / 'index.html'
CSS = ROOT / 'assets/css/workbook.css'
JS = ROOT / 'assets/js/workbook.js'
MANIFEST = ROOT / 'manifest.json'
REGISTRY = V31 / 'conceptual_reference_registry_v31.json'
SOURCE = V31 / 'CONCEPTUAL_REFERENCE_COMPLETE_V31_FA.md'
OUT = V31 / 'static_semantic_validation_v31.json'

checks: dict[str, dict[str, object]] = {}
errors: list[str] = []
warnings: list[str] = []

def record(name: str, passed: bool, detail: object = None) -> None:
    checks[name] = {'passed': bool(passed), 'detail': detail}
    if not passed:
        errors.append(f'{name}: {detail!r}')

text = HTML.read_text(encoding='utf-8')
css = CSS.read_text(encoding='utf-8')
js = JS.read_text(encoding='utf-8')
soup = BeautifulSoup(text, 'html.parser')
manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
registry = json.loads(REGISTRY.read_text(encoding='utf-8'))
source_text = SOURCE.read_text(encoding='utf-8')

# Frozen course structure preserved.
record('workbook_version_html', soup.body is not None and soup.body.get('data-workbook-version') == '31.0.0', soup.body.get('data-workbook-version') if soup.body else None)
record('workbook_version_manifest', manifest.get('version') == '31.0.0', manifest.get('version'))
record('main_lessons_21', len(soup.select('article.lesson[data-lesson]')) == 21, len(soup.select('article.lesson[data-lesson]')))
record('supplementary_lessons_7', len([a for a in soup.select('article.lesson') if not a.has_attr('data-lesson')]) == 7, len([a for a in soup.select('article.lesson') if not a.has_attr('data-lesson')]))
record('stations_6', len(soup.select('.station')) == 6, len(soup.select('.station')))
record('step_throughs_7', len(soup.select('[data-step-through-v2]')) == 7, len(soup.select('[data-step-through-v2]')))
record('settings_units_28', len(soup.select('details.settings-values-units')) == 28, len(soup.select('details.settings-values-units')))

# Source and registry integrity.
source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
record('source_sha256_registry', source_sha == registry.get('source_file_sha256'), {'actual': source_sha, 'registry': registry.get('source_file_sha256')})
record('registry_chapter_count_28', registry.get('chapter_count') == 28 and len(registry.get('chapters', [])) == 28, registry.get('chapter_count'))
record('source_top_level_chapters_28', len(re.findall(r'^#\s+[۰-۹]+\.\s+', source_text, re.M)) == 28, len(re.findall(r'^#\s+[۰-۹]+\.\s+', source_text, re.M)))

refs = soup.select('details.conceptual-reference')
record('conceptual_references_28', len(refs) == 28, len(refs))
record('all_references_closed_by_default', not any(d.has_attr('open') for d in refs))
record('all_references_have_direct_summary', all(d.find('summary', recursive=False) is not None for d in refs))
record('all_references_versioned_v31', all(d.get('data-concept-version') == '31.0.0' for d in refs))
record('each_reference_has_body', all(d.select_one(':scope > .concept-reference-body.concept-reference-v31') is not None for d in refs))
record('each_reference_has_sources_footer', all(len(d.select(':scope > .concept-reference-body > footer.concept-reference-evidence')) == 1 for d in refs))
record('each_reference_has_sections', all(len(d.select(':scope > .concept-reference-body > section.concept-reference-part')) >= 8 for d in refs), [len(d.select(':scope > .concept-reference-body > section.concept-reference-part')) for d in refs])
record('total_structured_sections_377', len(soup.select('details.conceptual-reference .concept-reference-part')) == 377, len(soup.select('details.conceptual-reference .concept-reference-part')))

# Registry SHA and content-fidelity checks.
md = mistune.create_markdown(escape=False, plugins=['table', 'url'])
chapter_re = re.compile(r'^#\s+([۰-۹]+)\.\s+(.+?)\s*$', re.M)
matches = list(chapter_re.finditer(source_text))
appendix_start = source_text.find('\n# پیوست:')
chapters = []
for i, match in enumerate(matches):
    start = match.end()
    end = matches[i + 1].start() if i + 1 < len(matches) else appendix_start
    chapters.append((match.group(2).strip(), source_text[start:end].strip() + '\n'))

fidelity_failures = []
sha_failures = []
for rec, (source_title, chapter_md) in zip(registry.get('chapters', []), chapters):
    detail = soup.find(id=rec.get('detail_id'))
    if detail is None:
        sha_failures.append((rec.get('detail_id'), 'missing detail'))
        continue
    body = detail.select_one(':scope > .concept-reference-body')
    actual_source_sha = hashlib.sha256(chapter_md.encode('utf-8')).hexdigest()
    actual_html_sha = hashlib.sha256(str(body).encode('utf-8')).hexdigest() if body else None
    if actual_source_sha != rec.get('source_markdown_sha256') or actual_html_sha != rec.get('rendered_body_sha256'):
        sha_failures.append((rec.get('detail_id'), actual_source_sha, actual_html_sha))
    # Every meaningful source block must occur in the integrated reference text.
    source_fragment = BeautifulSoup(md(chapter_md), 'html.parser')
    source_blocks = []
    for tag in source_fragment.find_all(['h2', 'h3', 'p', 'li', 'th', 'td', 'pre']):
        value = re.sub(r'\s+', ' ', tag.get_text(' ', strip=True)).strip()
        if value and value != 'منابع رسمی این فصل' and len(value) >= 3:
            source_blocks.append(value)
    integrated = re.sub(r'\s+', ' ', body.get_text(' ', strip=True)).strip() if body else ''
    missing = [block for block in source_blocks if block not in integrated]
    if missing:
        fidelity_failures.append({'detail_id': rec.get('detail_id'), 'missing_count': len(missing), 'samples': missing[:5]})
    if source_title != rec.get('title'):
        fidelity_failures.append({'detail_id': rec.get('detail_id'), 'title_mismatch': [source_title, rec.get('title')]})
record('registry_sha_integrity', not sha_failures, sha_failures[:10])
record('source_content_fidelity', not fidelity_failures, fidelity_failures[:10])

# Guide and evidence boundary.
guide = soup.find(id='appendix-v31-conceptual-reference-guide')
record('v31_release_note_present', soup.find(id='appendix-v31-release-note') is not None)
record('v31_guide_present', guide is not None)
guide_text = guide.get_text(' ', strip=True) if guide else ''
for phrase in ['insufficient_evidence', 'Variable Alias Chain', 'Container Query Native', 'V4 همیشه سریع‌تر از V3', 'هر Wrapper هزینه ثابت دارد']:
    record('guide_boundary_' + re.sub(r'\W+', '_', phrase).strip('_'), phrase in guide_text, phrase)
record('guide_official_source_groups', all(x in guide_text for x in ['Elementor', 'CSS و مرورگر', 'Performance و Accessibility']))

# Semantics, IDs, links, tables and code containment.
ids = [tag.get('id') for tag in soup.find_all(id=True)]
duplicates = [x for x, count in Counter(ids).items() if count > 1]
record('duplicate_ids_zero', not duplicates, duplicates[:20])
missing_targets = []
for a in soup.find_all('a', href=True):
    href = a['href']
    if href.startswith('#') and len(href) > 1 and soup.find(id=href[1:]) is None:
        missing_targets.append(href)
record('internal_hash_targets_resolve', not missing_targets, sorted(set(missing_targets))[:30])
record('all_details_have_summary', len(soup.find_all('details')) == len(soup.select('details > summary')), (len(soup.find_all('details')), len(soup.select('details > summary'))))
concept_tables = soup.select('.concept-reference-v31 table')
record('concept_tables_wrapped', all(t.parent and 'concept-table-scroll' in (t.parent.get('class') or []) for t in concept_tables), len(concept_tables))
record('concept_table_wrappers_keyboard_scrollable', all(t.parent.get('tabindex') == '0' and t.parent.get('role') == 'region' for t in concept_tables), len(concept_tables))
concept_pre = soup.select('.concept-reference-v31 pre')
record('concept_code_blocks_contained', all('concept-code-block' in (p.get('class') or []) and p.parent and p.parent.name == 'figure' for p in concept_pre), len(concept_pre))
record('v31_css_present', 'v31.0 — complete conceptual reference integration' in css)
record('print_reveals_concept_references', '@media print' in css and 'details.conceptual-reference > * { display: block !important; }' in css)
record('deep_link_reveal_logic_preserved', 'function revealTarget' in js and 'parent.open = true' in js)

# No active remote assets.
remote_assets = []
for tag, attr in [('script', 'src'), ('link', 'href'), ('img', 'src'), ('source', 'src'), ('video', 'src'), ('audio', 'src')]:
    for node in soup.find_all(tag):
        value = node.get(attr)
        if value and value.startswith(('http://', 'https://', '//')):
            remote_assets.append((tag, value))
record('active_remote_assets_zero', not remote_assets, remote_assets)

# JavaScript syntax check.
proc = subprocess.run(['node', '--check', str(JS)], capture_output=True, text=True)
record('javascript_syntax', proc.returncode == 0, (proc.stdout + proc.stderr).strip())

result = {
    'version': '31.0.0',
    'performed': True,
    'status': 'passed' if not errors else 'failed',
    'checks': checks,
    'errors': errors,
    'warnings': warnings,
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
if errors:
    sys.exit(1)
