# مولد قطعی کتاب‌کار آفلاین Elementor V4 — نسخه 32.0.0

این بسته نسخهٔ ساختاریافتهٔ جزوهٔ آفلاین Elementor V4 است. منبع ساخت دیگر یک فایل HTML یکپارچه نیست؛ ترتیب، Metadata و قرارداد واحدها در YAML ثبت می‌شود، محتوا با `markdown-it-py` پردازش می‌شود، قالب نهایی با Jinja2 ساخته می‌شود و داده‌ها با JSON Schema Draft 2020-12 اعتبارسنجی می‌شوند.

## وضعیت مهاجرت

```text
architecture_status: implemented
build_status: passed
browser_smoke_status: passed
content_migration_status: hybrid_source_preservation
```

- یک واحد v32 به‌صورت Markdown خالص ساخته شده است.
- ۸۱ واحد نسخهٔ 31 برای جلوگیری از Regression به‌صورت `trusted_html` در فایل‌های مستقل `.md` نگه‌داری شده‌اند.
- هر واحد می‌تواند بعداً مستقل به Markdown خالص تبدیل شود، به شرط پاس‌شدن آزمون‌های برابری.
- هیچ ادعایی مبنی بر تبدیل کامل محتوای v31 به Markdown خالص وجود ندارد.

## خروجی‌ها

اجرای Build دو خروجی می‌سازد:

```text
dist/
├── course/
│   ├── index.html
│   ├── assets/
│   ├── printables/
│   ├── source/
│   ├── manifest.json
│   └── SHA256SUMS.txt
├── single-file/
│   └── Elementor_V4_Offline_Interactive_Workbook_v32_0_0.html
└── build-report.json
```

- خروجی `course/` Artifact اصلی و مناسب توسعه و عیب‌یابی است.
- خروجی `single-file/` تمام CSS، JavaScript، تصویرها و Manifest را Inline می‌کند و برای جابه‌جایی یک‌فایلی مناسب است.

## پیش‌نیاز ویندوز

1. Python 3.11 یا جدیدتر را نصب کنید.
2. هنگام نصب Python گزینهٔ `Add Python to PATH` را فعال کنید.
3. PowerShell را در پوشهٔ پروژه باز کنید.

## نصب

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.lock
```

برای اجرای آزمون مرورگر، مرورگر Chromium/Chrome لازم است. Playwright در صورت در دسترس‌بودن Browser نصب‌شدهٔ سیستم از آن استفاده می‌کند. در محیطی که Browser اجرایی موجود نیست، می‌توان Browser رسمی Playwright را نصب کرد:

```powershell
python -m playwright install chromium
```

## Build

```powershell
python validate.py
python build.py
```

پس از پایان:

```text
dist\course\index.html
dist\single-file\Elementor_V4_Offline_Interactive_Workbook_v32_0_0.html
```

## اجرای آزمون‌ها

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = "1"
python -m pytest -q
node --check dist\course\assets\js\workbook.js
```

`node --check` اختیاری است و فقط در صورت نصب Node.js اجرا می‌شود. خود Build به Node وابسته نیست.

## ساخت ZIP قطعی

```powershell
python package.py
```

این فرمان Build را اجرا می‌کند و ZIP را با ترتیب فایل ثابت، Timestamp ثابت و Permission ثابت تولید می‌کند. SHA-256 کنار ZIP نوشته می‌شود.

## ساختار پروژه

```text
content/course.yaml          ترتیب و Metadata قطعی واحدها
content/units/*.md           منبع هر واحد
content/data/                Manifest وب و Baseline برابری
schemas/*.schema.json        قراردادهای Draft 2020-12
templates/                   Shell و Partialهای Jinja2
static/                      Assetها و شواهد تاریخی
src/workbook_builder/        موتور Build و Validation
tests/                       آزمون‌های واحد، برابری و مرورگر
```

## افزودن یک واحد Markdown جدید

1. فایل را در `content/units/` بسازید.
2. ورودی آن را در `content/course.yaml` اضافه کنید.
3. `format: markdown` و `allow_raw_html: false` قرار دهید.
4. `python validate.py` و سپس `python build.py` را اجرا کنید.

نمونه:

```yaml
- id: lesson-new
  kind: lesson
  tag: article
  classes:
    - lesson
    - card-surface
  attributes:
    data-lesson: "29"
  source: units/lesson-new.md
  format: markdown
  title: درس جدید
  allow_raw_html: false
```

## تبدیل یک واحد legacy به Markdown

تبدیل باید واحدبه‌واحد انجام شود:

1. از فایل `trusted_html` نسخه پشتیبان بگیرید.
2. متن روایی را به Markdown تبدیل کنید.
3. UIهای تعاملی را به Partial یا دادهٔ ساختاریافته منتقل کنید.
4. Format را به `markdown` تغییر دهید.
5. شناسهٔ واحد و Anchorهای عمومی را تغییر ندهید.
6. تمام آزمون‌ها را اجرا کنید.

جزئیات در `docs/MIGRATION_GUIDE_FA.md` آمده است.

## قواعد قطعی

- UTF-8 و Line Ending برابر LF است.
- YAML با `SafeLoader` خوانده می‌شود و Duplicate Key رد می‌شود.
- Jinja2 از `StrictUndefined` و Autoescape استفاده می‌کند.
- Raw HTML فقط برای واحدهای صریحاً Trusted مجاز است.
- شناسه‌های HTML و Anchorهای داخلی اعتبارسنجی می‌شوند.
- Runtime Asset خارجی ممنوع است؛ لینک منابع آموزشی می‌تواند اینترنتی باشد.
- Build Report و SHA-256ها با ترتیب پایدار تولید می‌شوند.
- NaN و Infinity در JSON تولیدی مجاز نیست.


## گردش‌کار تحویل به مدل زبانی

این Repository برای تحویل کامل به مدل آماده شده است. مدل باید `AGENTS.md`، قرارداد `llm/model-contract.yaml` و Task فعال را بخواند و کل Repository اصلاح‌شده را بازگرداند.

```powershell
Copy-Item llm\TASK_TEMPLATE_FA.md llm\TASK.md
# TASK.md را تکمیل و task_status را ready کنید
python tools\create_llm_handoff.py
```

خروجی در `handoff/Elementor_V4_Workbook_LLM_Handoff.zip` ایجاد می‌شود. برای بررسی بستهٔ برگشتی مدل:

```powershell
python tools\verify_returned_zip.py C:\path\returned.zip --browser
```

Script بررسی، مسیرهای تغییرکرده را با Manifest اولیه مقایسه می‌کند، تغییر خارج از `allowed_paths` را رد می‌کند و سپس Validation، Build و Testها را اجرا می‌کند.

## نگهداری در GitHub

فایل‌های GitHub Actions، Dependabot، Pull Request Template و Issue Template داخل `.github/` آماده‌اند. راهنمای قدم‌به‌قدم در `docs/GITHUB_MAINTENANCE_FA.md` قرار دارد. `dist/`، `release/` و `handoff/` تولیدی‌اند و نباید Commit شوند.

## منابع طراحی فنی

- Jinja2 API و Template Environment: `https://jinja.palletsprojects.com/en/stable/api/`
- markdown-it-py: `https://markdown-it-py.readthedocs.io/`
- JSON Schema Draft 2020-12: `https://json-schema.org/draft/2020-12`
- PyYAML: `https://pyyaml.org/`
