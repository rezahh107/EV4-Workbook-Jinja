# یادداشت نسخه 32.0 — مولد ساختاریافته و قابل بازتولید

`status: implemented_and_validated`

این نسخه معماری نگهداری جزوه را از یک فایل HTML یکپارچه به یک خط تولید صریح منتقل می‌کند:

```text
Markdown / trusted HTML + YAML
→ JSON Schema validation
→ markdown-it-py
→ Jinja2
→ Offline folder build + Single-file build
→ deterministic hashes
```

محتوای پیچیدهٔ نسخهٔ 31 در مرحلهٔ نخست بدون بازنویسی پرریسک، به‌صورت واحدهای مستقل `trusted_html` نگه‌داری شده است. هر واحد می‌تواند بعداً مستقل به Markdown خالص تبدیل شود؛ شناسه‌ها، لینک‌ها، Local Storage، آزمون‌ها و رفتار آفلاین باید ثابت بمانند.

> قانون مهاجرت: ابتدا برابری رفتاری، سپس پاک‌سازی تدریجی منبع.
