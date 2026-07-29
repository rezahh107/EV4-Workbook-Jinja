# تغییرات

## انتقال روح آموزشی TUYA — in progress

- یادداشت ۰۸۱ بدون تغییر عنوان course index حفظ شد تا با `content/course.yaml` هم‌خوان بماند؛ داخل همان یادداشت، زیرعنوان و محتوای «انتقال روح آموزشی TUYA» اضافه شد.
- تأکید شد که بخش مفهومی نباید حذف یا فشرده شود؛ بخش مفهومی باید کامل‌تر، دقیق‌تر و مستندتر شود و تغییر اصلی در تمرین‌ها به‌صورت مربی مرحله‌به‌مرحله انجام شود.
- قالب تمرین‌های آینده ثبت شد: confirmed/provisional/unknown، نسبت با جزوه، فقط یک اقدام کوچک، مسیر UI، Element هدف، Class فعال، Property، مقدار، واحد، مرز اثر و تأیید پایانی.
- زنجیرهٔ مفهومی دوره ثبت شد: Context → Structure → Flow/Display → Size/Units → Position/Layering → Responsive → Design System → DOM/Audit.
- اصلاحات محتوایی مرحلهٔ بعد ثبت شد: تفاوت Flow و Display، محدودیت Absolute، درصد نسبت به Parent، ترجیح Min Height برای محتوای پویا، Rename با دوبار کلیک در Structure، تفاوت DOM با درخت بصری، و تفاوت جنس Variable/Class/Component.
- این تغییر هنوز بازنویسی خطی همهٔ درس‌ها نیست؛ لایهٔ روش‌شناسی و نقشهٔ ادغام برای اعمال مرحلهٔ بعدی است.

## Repository Tooling 1.1.0 — LLM-ready handoff and GitHub governance

- قرارداد `AGENTS.md` و `llm/model-contract.yaml` اضافه شد.
- Task ساختاریافته و گزارش بازگشت مدل اضافه شد.
- ابزارهای ساخت Handoff قطعی، بررسی ZIP برگشتی و اجرای همه Gateها اضافه شدند.
- GitHub Actions، Dependabot، PR Template، Issue Template، `.gitattributes` و `.editorconfig` اضافه شدند.
- خروجی‌های تولیدی از Repository منبع جدا و در `.gitignore` ثبت شدند.

# تغییرات نسخه 32.0.0

## پیاده‌سازی‌شده

- افزودن مولد Python مبتنی بر Jinja2 و markdown-it-py
- افزودن Manifest مرکزی YAML
- افزودن JSON Schema Draft 2020-12 برای Course، Unit و Build Report
- Duplicate-key rejection برای YAML
- Jinja2 StrictUndefined و Autoescape
- جداسازی ۸۱ واحد legacy در فایل‌های مستقل
- افزودن یک واحد Markdown خالص برای یادداشت v32
- خروجی پوشه‌ای آفلاین
- خروجی Single-file با CSS، JavaScript، Image و Manifest Inline
- Build Report و SHA-256 پایدار
- ZIP قطعی با ترتیب و Timestamp ثابت
- آزمون برابری با v31
- آزمون مرورگر Chromium روی Single-file

## عمداً انجام‌نشده

- بازنویسی کامل ۸۱ واحد legacy به Markdown خالص
- تغییر طراحی، محتوا یا قرارداد Local Storage
- مهاجرت به Astro، Eleventy یا Runtime Framework
