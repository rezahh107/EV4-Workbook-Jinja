# Elementor V4 Offline Interactive Workbook — LLM-ready source

این Repository سورس کامل و قابل بازتولید کتاب‌کار آفلاین Elementor V4 است. محتوا، Metadata، قالب‌ها، Assetها، Schemaها، Builder پایتون و آزمون‌ها در یک مخزن نگه‌داری می‌شوند تا بتوان هر تغییر را به‌صورت کنترل‌شده به یک مدل زبانی یا توسعه‌دهنده سپرد.

## شروع سریع

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.lock
python tools\check_all.py
```

خروجی در `dist/` ساخته می‌شود. این پوشه تولیدی است و در Git Commit نمی‌شود.

## تحویل به مدل زبانی

1. `llm/TASK.md` را از روی `llm/TASK_TEMPLATE_FA.md` تکمیل کنید.
2. مقدار `task_status` را به `ready` تغییر دهید.
3. مسیرهای مجاز تغییر را دقیق بنویسید.
4. بستهٔ مخصوص مدل را بسازید:

```powershell
python tools\create_llm_handoff.py
```

5. ZIP ساخته‌شده در `handoff/` را همراه این دستور به مدل بدهید:

> کل ZIP را بخوان. ابتدا `AGENTS.md`، سپس `llm/model-contract.yaml` و `llm/TASK.md` را اجرا کن. فقط مسیرهای مجاز را تغییر بده، Gateهای قابل اجرا را اجرا کن و کل Repository اصلاح‌شده را همراه `llm/RETURN_REPORT.md` بازگردان.

پس از دریافت ZIP مدل:

```powershell
python toolserify_returned_zip.py path	oeturned.zip --browser
```

## ساختار اصلی

- `content/units/`: محتوای قابل ویرایش دوره
- `content/course.yaml`: ترتیب و Metadata واحدها
- `templates/`: قالب‌های Jinja2
- `static/`: CSS، JavaScript، تصاویر و شواهد تاریخی
- `schemas/`: قراردادهای JSON Schema Draft 2020-12
- `src/workbook_builder/`: Builder قطعی
- `tests/`: آزمون‌های قرارداد، Build و Browser
- `llm/`: قرارداد تحویل و بازگشت مدل
- `.github/`: CI، Templateهای PR/Issue و Dependabot

راهنمای کامل فارسی در `README_FA.md` و راهنمای GitHub در `docs/GITHUB_MAINTENANCE_FA.md` است.
