# گزارش مرحله بعد — بازنویسی درس ۷ با روش Flex Item Sizing

## فایل اصلاح‌شده

- `content/units/039-lesson-7.md`

## موضوع واقعی درس

عنوان فعلی درس ۷ در ریپو:

```text
درس 7 — Grow، Shrink، Basis، Width و Max Width
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از درس ۵ و ۶ که Shell را Flex و محور را روشن کردند، درس ۷ باید رفتار اندازهٔ دو Flex Item اصلی را آموزش بدهد:

- `TUYA Copy`
- `TUYA Visual`

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Basis، Grow، Shrink، Width، Max Width و `min-width:0` حفظ و دقیق‌تر شدند.
- Step-Through موجود حفظ شد، اما به نسخهٔ متنی/مفهومی و قابل چاپ تبدیل شد.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- مقدارهای Copy/Visual به‌عنوان provisional معرفی شدند، نه عدد قطعی جزوه.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Context → Structure → Class Scope → Box Model → Flex Container → Axis → Flex Item Sizing.
- توضیح اینکه Basis روی Main Axis است و همیشه عرض نیست.
- توضیح Grow به‌عنوان سهم از فضای اضافه، نه نسبت اندازهٔ نهایی.
- توضیح Shrink به‌عنوان فعال‌شدن در کمبود فضا.
- اضافه شدن Debug برای `min-width:auto` و نقش `min-width:0`.
- تاکید بر خواندن Computed Style: width، flex-basis، flex-grow، flex-shrink، min-width، max-width.
- قرارداد TUYA: Copy منعطف‌تر، Visual کنترل‌شده‌تر.
- Responsive checkpoint برای بازبینی Basis در Mobile.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. `TUYA Copy` و `TUYA Visual` را انتخاب کند.
2. Basis/Grow/Shrink/Min Width/Max Width را به‌عنوان مقدار شروع تست کند.
3. متن بلند را برای Copy تست کند.
4. Overflow را با min-width، content wrapping، basis، max-width و gap عیب‌یابی کند.

موارد ممنوع:

- Position
- Nodeها
- Visual Stage positioning
- Shadow/Glow
- Background نهایی
- Typography
- Button Style
- عدد قطعی از Screenshot

## مقدارهای شروع

```text
TUYA Copy:
  basis: 52%–55% یا 18rem provisional
  grow: 1
  shrink: 1
  min-width: 0 در صورت نیاز

TUYA Visual:
  basis: 45%–48% یا 16rem provisional
  grow: 0 یا محدود
  shrink: 1
  max-width: کنترل‌شده provisional
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
