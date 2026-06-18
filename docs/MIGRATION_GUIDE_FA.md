# راهنمای مهاجرت تدریجی از trusted_html به Markdown

## اصل

مهاجرت منبع نباید هم‌زمان با Redesign یا Refactor Runtime انجام شود.

```text
یک واحد
→ تبدیل منبع
→ Build
→ مقایسه ساختاری
→ آزمون مرورگر
→ Commit مستقل
```

## چه چیزی به Markdown منتقل شود؟

- Headingها
- Paragraphها
- Listها
- Blockquoteها
- Code Blockها
- جدول‌های ساده
- لینک منابع

## چه چیزی به Jinja Partial منتقل شود؟

- کارت‌های آموزشی تکراری
- Disclosureها
- Quiz UI
- Step-Through
- Progress Controls
- جدول‌هایی با Accessibility Contract خاص
- ساختارهایی که Class و ARIA ثابت دارند

## چه چیزی به JSON/YAML داده‌ای منتقل شود؟

- سؤال و گزینه‌های آزمون
- پاسخ صحیح و Feedback
- Stateهای Step-Through
- Registry منابع
- Navigation و ترتیب
- Metadata درس

## Gate تبدیل هر واحد

- ID واحد ثابت است.
- IDهای داخلی حذف یا تکراری نشده‌اند.
- لینک‌های Fragment سالم‌اند.
- تعداد کنترل‌های Persist تغییر ناخواسته ندارد.
- Local Storage Keyها ثابت‌اند.
- State اولیهٔ Disclosureها ثابت است.
- Desktop و Mobile Overflow ندارند.
- Console Error وجود ندارد.
- Browser Smoke Pass است.

## پایان مهاجرت

تنها زمانی می‌توان وضعیت را `markdown_normalized` اعلام کرد که تمام واحدهای `trusted_html` حذف شده باشند و آزمون‌های برابری همچنان پاس شوند.
