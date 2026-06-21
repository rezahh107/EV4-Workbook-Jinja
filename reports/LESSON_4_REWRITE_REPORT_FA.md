# گزارش مرحله بعد — بازنویسی درس ۴ با روش Shell Sizing و Box Model

## فایل اصلاح‌شده

- `content/units/035-lesson-4.md`

## موضوع واقعی درس

عنوان فعلی درس ۴ در ریپو:

```text
درس 4 — Box Model، Width و پوستهٔ سکشن
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Context، Structure و Class Scope، درس ۴ باید Shell sizing را آموزش بدهد: Padding، Margin، Width، Max Width، Min Height و مرجع محاسبهٔ درصدها.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Box Model، Padding، Margin، Width، Max Width، Overflow و Responsive checkpoint حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور شدند.
- مقدارهای بصری به‌عنوان provisional معرفی شدند، نه مقدار قطعی جزوه.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Context → Structure → Class Scope → Box Model.
- توضیح اینکه درصد بدون Parent معنی کامل ندارد.
- افزودن تفاوت Percent و VW/VH در سطح لازم.
- اصلاح height ثابت: شروع مقاوم‌تر `height:auto` + `min-height:40vh`.
- توضیح دقیق Section/Shell/Main و وضعیت provisional برای Main.
- توصیه به padding-inline / padding داخلی به‌جای margin مخرب روی عنصر تمام‌عرض.
- تمرین TUYA فقط روی Shell sizing تمرکز دارد.
- Full Width failure به Page Layout و Theme Template وصل شد.
- Debug Overflow به Parent، Margin، Computed و Box Model وصل شد.

## تمرین TUYA

در این درس هنرجو فقط باید `TUYA Shell` را بررسی یا تنظیم کند:

- Width
- Max Width
- Padding Inline
- Min Height
- Height Auto

موارد ممنوع:

- Position
- Nodeها
- Shadow/Glow
- Background نهایی
- Typography
- Button Style
- Design نهایی

## مقدارهای شروع

این مقدارها در درس به‌عنوان `provisional` آمده‌اند:

```text
Width: 100% یا auto مناسب UI
Max Width: 1200px تا 1280px برای شروع تست
Padding Inline: 24px تا 32px برای شروع تست
Min Height: 40vh برای شروع تست
Height: auto
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
