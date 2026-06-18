# Implementation Brief — نسخهٔ بعدی

## هدف

تبدیل نسخهٔ ۱۴.۱ Premium UX به نسخه‌ای نزدیک به:

Offline Interactive Learning Workbook

## کارهای اصلی

1. حفظ ظاهر Premium UX و PersianNew.
2. تبدیل درس‌ها به `article.lesson`.
3. تبدیل بخش‌های درس به `section`.
4. تبدیل Checkpointها به checkbox واقعی.
5. تبدیل سنجش اعتماد به input/range + output/meter.
6. تبدیل سؤال‌های توقف به quiz/radio + details پاسخ.
7. تبدیل جداول داده‌ای به table واقعی.
8. تبدیل تعریف‌ها به dl.
9. تبدیل فارسی‌های آموزشی کدنما به کارت، لیست، فرم، پنل یا figure.
10. حفظ کد واقعی به‌صورت LTR و monospace.
11. ذخیره پیشرفت با LocalStorage.
12. حفظ آفلاین بودن کامل.

## خروجی مورد انتظار

- `index.html`
- CSSهای محلی
- JS محلی
- assets
- source archive
- validation report
- manifest
- checksums
- changelog
