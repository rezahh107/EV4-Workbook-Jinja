# گزارش مرحله بعد — بازنویسی درس ۵ با روش Flex Two-column Flow

## فایل اصلاح‌شده

- `content/units/037-lesson-5.md`

## موضوع واقعی درس

عنوان فعلی درس ۵ در ریپو:

```text
درس 5 — Flexbox و ساخت دو ستون اصلی
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Context، Structure، Class Scope و Shell sizing، درس ۵ باید Layout اصلی دو ستون را آموزش بدهد: `TUYA Shell` به عنوان Flex Container و `TUYA Copy` و `TUYA Visual` به عنوان Flex Item مستقیم.

## سیاست حفظ محتوا

- بخش مفهومی Flexbox حذف نشده است.
- مفاهیم Parent/Item، Main Axis، Cross Axis، Direction، Gap، Basis، Grow/Shrink و Why not Absolute حفظ و دقیق‌تر شدند.
- Grow/Shrink عمیق هنوز آموزش داده نمی‌شود؛ فقط در حد مرز دانستن آمده است.
- تمرین‌ها مربی‌محور و evidence-first شدند.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Context → Structure → Class Scope → Box Model → Flexbox.
- توضیح تفاوت Display، Normal Flow و Absolute.
- تأکید بر اینکه `display:flex` خروج از Flow نیست.
- تأکید بر Child مستقیم: Shell فقط Copy و Visual را می‌چیند، نه Visual Stage داخلی را.
- منع Absolute برای دو ستون اصلی.
- استفاده از Gap برای فاصلهٔ بین ستون‌ها، نه marginهای پراکنده.
- قرارداد Responsive: Desktop Row، Mobile Column.
- Basisهای Copy/Visual و Gap به‌عنوان provisional معرفی شدند.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. `TUYA Shell` را انتخاب کند.
2. Display را Flex کند.
3. Direction دسکتاپ را Row بگذارد.
4. Gap شروع را provisional تنظیم کند.
5. Copy و Visual را کنار هم در Flow ببیند.
6. برای Mobile فقط قرارداد Column را ثبت کند.

موارد ممنوع:

- Position
- Nodeها
- Visual Stage positioning
- Shadow/Glow
- Background نهایی
- Typography
- Button Style
- نسخهٔ دوم سکشن برای Mobile

## مقدارهای شروع

```text
Display: Flex
Direction Desktop: Row
Gap: 24px تا 40px provisional
Copy Basis: 52% تا 55% provisional
Visual Basis: 45% تا 48% provisional
Mobile Direction: Column
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
