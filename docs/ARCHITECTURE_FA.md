# معماری مولد v32

## هدف

هدف این معماری جداسازی چهار مسئولیت است:

```text
Content
Metadata
Presentation
Validation/Packaging
```

## Pipeline

```text
content/course.yaml
+ content/units/*.md
+ templates/*.j2
+ static/*
        ↓
Duplicate-key-safe YAML load
        ↓
JSON Schema Draft 2020-12
        ↓
Cross-file contract validation
        ↓
markdown-it-py rendering
        ↓
Jinja2 StrictUndefined rendering
        ↓
HTML semantic validation
        ↓
Folder artifact + single-file artifact
        ↓
Build report + SHA-256
```

## مرزهای مسئولیت

### YAML

فقط Metadata و ترتیب قطعی را نگه می‌دارد. HTML یا متن بلند در YAML قرار نمی‌گیرد.

### Markdown

محتوای روایی را نگه می‌دارد. Raw HTML در حالت معمول ممنوع است.

### trusted_html

مسیر مهاجرت legacy است. فقط فایل‌های موجود و ممیزی‌شده اجازه استفاده دارند. این وضعیت نباید برای محتوای جدید انتخاب پیش‌فرض باشد.

### Jinja2

Shell، Wrapperها و اجزای تکراری را تولید می‌کند. Templateها دادهٔ دامنه‌ای جدید ایجاد نمی‌کنند.

### JSON Schema

شکل ورودی و خروجی را کنترل می‌کند. بررسی‌های بین‌فایلی مانند Unique ID، وجود فایل و Anchorهای شکسته در Python انجام می‌شوند؛ چون JSON Schema برای تمام این روابط کافی نیست.

## سیاست امنیتی

- YAML با Loader امن و Duplicate-key rejection خوانده می‌شود.
- Markdown عادی با `html: false` پردازش می‌شود.
- HTML Trusted فقط با Flag صریح پذیرفته می‌شود.
- Autoescape در Jinja2 فعال است.
- خروجی نباید Script، Style، Image یا Preload خارجی داشته باشد.
- لینک‌های آموزشی `https://` مجازند، چون Runtime Asset نیستند.

## سیاست Determinism

- واحدها فقط مطابق ترتیب `course.yaml` ساخته می‌شوند.
- پیمایش فایل‌ها همیشه Sort می‌شود.
- JSON با Key Order ثابت نوشته می‌شود.
- ZIP با Timestamp ثابت `1980-01-01` تولید می‌شود.
- Permission فایل‌های ZIP برابر `0644` است.
- SHA-256 روی Byteهای نهایی محاسبه می‌شود.
- Build Report خودش را Hash نمی‌کند تا حلقهٔ خودارجاع ایجاد نشود.

## قرارداد برابری v31

Baseline فقط برای Validation است و در تولید محتوا دخالت ندارد. موارد زیر ثابت نگه داشته می‌شوند:

- ترتیب ۸۱ واحد legacy
- ۲۸ درس
- ۶ ایستگاه
- ۲۸ مرجع مفهومی
- ۷ Step-Through v2
- تعداد Detailها و کنترل‌های Persist
- Assetهای اصلی CSS و JavaScript
- شناسه‌ها و Anchorهای داخلی
