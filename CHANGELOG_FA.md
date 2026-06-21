# تغییرات

## انتقال روح آموزشی TUYA — in progress

- یادداشت حفظ یادگیری دیداری به «یادداشت انتقال روح آموزشی TUYA» تبدیل شد.
- اصل Context-first، تفکیک confirmed/provisional/unknown، یک اقدام کوچک، Flow/Absolute، درصد نسبت به Parent، Min Height، و اصلاح Rename در Structure ثبت شد.
- این تغییر هنوز بازنویسی خطی همهٔ درس‌ها نیست؛ لایهٔ یکپارچه‌سازی برای اعمال مرحلهٔ بعدی است.

## Repository Tooling 1.1.0 — LLM-ready handoff and GitHub governance

- قرارداد `AGENTS.md` و `llm/model-contract.yaml` اضافه شد.
- Task ساختاریافته و گزارش بازگشت مدل اضافه شد.
- ابزارهای ساخت Handoff قطعی، بررسی ZIP برگشتی و اجرای همه Gateها اضافه شد.
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
