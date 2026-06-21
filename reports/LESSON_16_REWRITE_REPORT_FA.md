# گزارش مرحله بعد — بازنویسی درس ۱۶ با روش State Accessibility Contract

## فایل اصلاح‌شده

- `content/units/052-lesson-16.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۶ در ریپو:

```text
درس 16 — State، Hover، Focus و دسترسی‌پذیری
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از RTL و Responsive، درس ۱۶ باید عناصر تعاملی را قابل استفاده کند:

- State زبان بازخورد رابط است.
- Hover جای Focus را نمی‌گیرد.
- Focus باید قابل مشاهده باشد.
- Keyboard، Zoom، Contrast و Target Size باید تست شوند.
- اطلاعات مهم نباید فقط با Hover یا رنگ منتقل شود.
- Decorative element نباید focusable شود.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- State، Hover، Focus، Active، Accessibility، Keyboard، Zoom، Contrast، Target size، Color-only و Focus visible حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Interaction پیچیده و JavaScript وارد این درس نشد.
- ARIA پیشرفته و component state machine وارد این درس نشد.
- State tokenها فعلاً provisional/local نگه داشته شدند.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Normal Layout → Interactive Element → State Contract → Accessibility tests.
- Focus Ring به درس Overflow/Layering وصل شد.
- Decorative Node و Interactive Node تفکیک شدند.
- State Contract برای Primary CTA، Secondary Link، Feature Item، Orbit Node و Logo Link اضافه شد.
- Keyboard test با Tab/Shift+Tab اضافه شد.
- Zoom و Target Size به تمرین وارد شد.
- حذف outline بدون جایگزین به‌عنوان تلهٔ اصلی ثبت شد.
- Color-only و Hover-only ممنوع شدند.
- Design System decision برای Focus/State tokens اضافه شد.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. CTA و لینک‌ها را از نظر State بررسی کند.
2. Normal/Hover/Focus/Active/Disabled را ثبت کند.
3. با Tab و Keyboard تست کند.
4. Focus Ring را از نظر visibility، overflow و z-index بررسی کند.
5. Decorative Nodeها را focusable نکند.
6. Node تعاملی را بدون Focus/Name رها نکند.
7. Zoom و Target Size را در حد پایه تست کند.

موارد ممنوع:

- Interaction پیچیده با JavaScript
- ARIA dynamic state پیشرفته
- ساخت state machine
- Animation نهایی
- Shadow/Glow نهایی
- تغییر Layout/Responsive/RTL
- ساخت token سراسری پیش از تثبیت pattern

## مقدارهای شروع

مقادیر نهایی در این درس قطعی نیستند. تصمیم‌های شروع:

```text
Primary CTA:
  Normal / Hover / Focus Visible / Active / Disabled
  Focus ring visible
  Target size sufficient
  No color-only state

Secondary Link:
  underline/indicator beyond color
  focus visible

Feature Item:
  non-interactive unless real action exists

Orbit Node:
  decorative by default unless interaction is confirmed
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
