# گزارش اعتبارسنجی سورس LLM-ready و GitHub-ready

## وضعیت

```text
repository_tooling_version: 1.1.0
workbook_version: 32.0.0
source_contract_status: passed
build_status: passed
non_browser_tests_status: passed
browser_smoke_status: passed
handoff_determinism_status: passed
returned_zip_scope_check_status: passed
```

## دامنهٔ تحویل

- قرارداد الزامی مدل در `AGENTS.md`؛
- قرارداد ماشین‌خوان در `llm/model-contract.yaml`؛
- Task دارای YAML Front Matter و Schema؛
- گزارش بازگشت مدل؛
- ابزار ساخت ZIP قطعی مخصوص مدل؛
- ابزار مقایسه و بررسی ZIP برگشتی؛
- GitHub Actions برای Source Contract و Browser Smoke؛
- Release Workflow، Dependabot، PR Template و Issue Template؛
- `.editorconfig`، `.gitattributes` و `.gitignore` مناسب Repository منبع.

## نتایج اجراشده

| Gate | نتیجهٔ واقعی |
|---|---|
| `python validate.py` | PASS — 82 واحد؛ Task در وضعیت draft |
| `python build.py` | PASS — Folder Build و Single-file Build |
| `python -m compileall -q src tools tests` | PASS |
| `python -m pytest -q -m "not browser"` | PASS — 8 passed، 1 deselected |
| `python tools/check_node_syntax.py` | PASS |
| `python -m pytest -q -m browser` | PASS — 1 passed، 8 deselected |
| تولید Handoff A و B | PASS — Byte-identical |
| SHA-256 هر دو Handoff آزمایشی | `deb3a642ab344b4eda64b2019ba0859b2b9483470c5bd476e87d34ec87b87fcd` |
| `verify_returned_zip.py --skip-checks` روی Handoff بدون تغییر | PASS با Flag آزمایشی `--allow-unchanged-report` |

## یادداشت محیط

اجرای یکپارچهٔ `python tools/check_all.py --browser` در Wrapper فعلی ابزار به Timeout نشست، اما تمام Gateهای تشکیل‌دهندهٔ آن جداگانه و با Exit Code صفر اجرا شدند. بنابراین ادعای PASS فقط بر مبنای فرمان‌های مستقل اجراشده است.

## مرز ادعا

این گزارش اثبات می‌کند Repository و گردش‌کار بسته‌بندی/بازگشت در محیط حاضر اجرا شده‌اند. عملکرد مدل زبانی ثالث، کیفیت تغییرات آینده و دسترسی Browser در محیط مدل از پیش تضمین نشده است؛ نبود Browser باید `BLOCKED_ENVIRONMENT` گزارش شود.
