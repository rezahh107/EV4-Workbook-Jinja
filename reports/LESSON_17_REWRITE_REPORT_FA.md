# گزارش مرحله بعد — بازنویسی درس ۱۷ با روش Design System Reuse Decision

## فایل اصلاح‌شده

- `content/units/053-lesson-17.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۷ در ریپو:

```text
درس 17 — Classes، Variables و Components در Design System V4
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از State و Accessibility، درس ۱۷ باید تصمیم reuse را آموزش بدهد:

- اگر فقط مقدار تکرار شده: Variable candidate
- اگر بستهٔ Style تکرار شده: Global Class candidate
- اگر Structure + Style + رفتار/محتوا تکرار شده: Component candidate
- اگر فقط استثنای یک مورد است: Local adjustment

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Decision Tree، Variable، Class، Component، Design System، Class Explosion و Promotion حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Design System سازمانی کامل وارد این درس نشد.
- Component Library نهایی و token governance وارد این درس نشد.
- همهٔ کاندیدها تا قبل از شواهد واقعی `provisional` هستند.
- Shadow compound بدون شواهد پشتیبانی، Variable قطعی نشد.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Value → Style Package → Structure Pattern → Design System Decision.
- Reuse Inventory برای TUYA اضافه شد.
- قاعدهٔ «اول Local، بعد evidence، بعد promotion» اضافه شد.
- تفکیک Local adjustment از خطا.
- Naming Strategy اضافه شد.
- Class Manager و active editing target به درس ۳ وصل شد.
- Promotion Rule برای Local→Global اضافه شد.
- Class Explosion و Component زودهنگام به‌عنوان تله‌های اصلی معرفی شدند.
- Componentها فعلاً candidate ماندند تا variationهای واقعی روشن شوند.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. Reuse Inventory بنویسد.
2. هر مورد را به Value / Style Pack / Structure / Exception طبقه‌بندی کند.
3. Variable/Class/Component candidate ثبت کند.
4. Promotion Rule بنویسد.
5. هیچ Global/Component نهایی بدون evidence نسازد.
6. Class Explosion را با Decision Tree کنترل کند.

موارد ممنوع:

- Design System سازمانی کامل
- Component Library نهایی
- token governance
- migration کامل همهٔ Styleها
- ساخت Component زودهنگام
- ساخت Variable برای مقدار یک‌بارمصرف
- ساخت Global Class برای offsetهای provisional
- Shadow Variable قطعی بدون پشتیبانی واقعی

## مقدارهای شروع

```text
Brand colors: Variable candidate
Common spacing: Variable candidate after usage audit
Primary CTA: Global Class candidate
Orbit Node: Global Class now, Component candidate later
Feature Item: Component candidate after variants
Logo Item: Global Class candidate
Visual Stage: Local pattern until reuse
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
