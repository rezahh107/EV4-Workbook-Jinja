# گزارش مرحله بعد — بازنویسی درس ۱۳ با روش Layering Debug

## فایل اصلاح‌شده

- `content/units/047-lesson-13.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۳ در ریپو:

```text
درس 13 — Z-index، Overflow و Layering
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Position و Visual Stage، درس ۱۳ باید Layering را آموزش بدهد:

- Z-index عدد جهانی نیست.
- Overflow می‌تواند Glow/Node/Focus را Clip کند.
- Stacking Context باعث می‌شود عددهای بزرگ همیشه اثر نداشته باشند.
- Layer Map کوچک و مستند بهتر از عددهای تصادفی است.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Z-index، Overflow، Layering، Stacking Context، Step-Through، Design System Decision و Debug حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Shadow/Glow نهایی، Interaction نهایی و z-index سراسری وارد این درس نشدند.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Position / Containing Block → Layering → Z-index Scale → Overflow.
- قاعدهٔ مرکزی: قبل از z-index، Position/Containing Block/Overflow/Stacking Context را بررسی کن.
- توضیح اینکه z-index داخل Stacking Context معنا دارد، نه به‌عنوان جدول جهانی.
- توضیح اینکه Overflow با z-index حل نمی‌شود.
- Layer Map کوچک برای Visual Stage تعریف شد.
- Focus ring و clipping به Accessibility وصل شد.
- از z-indexهای بزرگ تصادفی جلوگیری شد.
- Layer tokenها تا تثبیت pattern واقعی، provisional/local نگه داشته شدند.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. Layerهای Visual Stage را فهرست کند.
2. یک Layer Map کوچک بسازد.
3. Overflow را با Glow/Node تست کند.
4. قبل از تغییر z-index، clipping را بررسی کند.
5. Debug Overlay را فقط موقت استفاده کند.

موارد ممنوع:

- Shadow/Glow نهایی
- Interaction نهایی
- z-index سراسری سایت
- ساخت Layer Token نهایی
- Animation
- Position نهایی همهٔ Orbit Nodeها
- تغییر Copy/Typography/Logo Strip

## مقدارهای شروع

```text
Stage Base: 0 provisional
Glow: 1 provisional
Core Cloud: 2 provisional
Orbit Node: 3 provisional
Active / Focus Node: 4 unknown_until_interaction
Debug Overlay: 9 temporary
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
