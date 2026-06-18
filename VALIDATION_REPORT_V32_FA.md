# گزارش اعتبارسنجی مولد کتاب‌کار Elementor V4 — نسخه 32.0.0

## وضعیت

```text
VALIDATION_STATUS: PASSED
GENERATOR_STATUS: IMPLEMENTED
CONTENT_MIGRATION_STATUS: HYBRID_SOURCE_PRESERVATION
```

این گزارش تأیید می‌کند که مولد Jinja2 + markdown-it-py + YAML/JSON Schema ساخته و در محیط حاضر اجرا شده است. این گزارش تبدیل کامل تمام محتوای legacy به Markdown خالص را تأیید نمی‌کند.

## محیط اجرا

```text
Python: 3.13.5
Jinja2: 3.1.6
markdown-it-py: 4.2.0
PyYAML: 6.0.3
jsonschema: 4.26.0
Beautiful Soup: 4.14.3
pytest: 9.0.2
Node.js: 22.16.0
Chromium: system executable
```

## فرمان‌های اجراشده

```text
python validate.py
python build.py
python -m compileall -q src tests build.py validate.py package.py
node --check dist/course/assets/js/workbook.js
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q
```

## نتایج

| Gate | نتیجه |
|---|---|
| YAML Duplicate Key Guard | PASS |
| JSON Schema Draft 2020-12 | PASS |
| Cross-file source contract | PASS |
| Jinja2 StrictUndefined build | PASS |
| Markdown raw-HTML guard | PASS |
| trusted_html root contract | PASS |
| Internal anchor validation | PASS |
| Duplicate HTML ID validation | PASS |
| External runtime asset validation | PASS |
| v31 parity assertions | PASS |
| Python compile | PASS |
| JavaScript syntax | PASS |
| Chromium single-file smoke | PASS |
| Desktop/Mobile overflow smoke | PASS |
| Test suite | 7 passed |

## خروجی محتوایی

```text
Top-level units: 82
Legacy v31 units preserved: 81
Native Markdown v32 units: 1
Lessons: 28
Stations: 6
Conceptual references: 28
Step-Through v2: 7
```

## Hashهای Artifact داخلی

```text
Folder index.html
8c73c5a5726cd25dcf6bf20eaf11d803f347ada19f2bf42bdd73e532d79a7bbf

Portable single-file HTML
ac6025c948658804902028c88efd3e1430badd64caa81d3a493d2d2c645ce6aa
```

Hash بسته‌های ZIP در فایل‌های `.sha256` کنار هر Artifact ارائه می‌شود. Hash ZIP داخل خود ZIP ثبت نمی‌شود تا خودارجاع ایجاد نشود.

## مرز ادعا

- `implemented`: مولد، Schemaها، Build و آزمون‌ها ساخته و اجرا شده‌اند.
- `validated`: Gateهای فهرست‌شده در همین محیط پاس شده‌اند.
- `not_claimed`: تبدیل کامل ۸۱ واحد legacy به Markdown خالص.
- `not_claimed`: برابری Pixel-by-pixel در تمام Browserها و سیستم‌عامل‌ها.
- `partial_processing_possible`: هر واحد legacy می‌تواند مستقل و مرحله‌ای به Markdown خالص تبدیل شود.
