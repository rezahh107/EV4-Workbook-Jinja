# گزارش مرحله بعد — بازنویسی درس ۱۵ با روش RTL Logical Audit

## فایل اصلاح‌شده

- `content/units/050-lesson-15.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۵ در ریپو:

```text
درس 15 — RTL، Start و End
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Responsive، Position و Layering، درس ۱۵ باید جهت‌پذیری پروژه را آموزش بدهد:

- RTL فقط `text-align:right` نیست.
- Start/End با Direction تغییر می‌کنند.
- Left/Right فیزیکی‌اند.
- Logical Properties برای Componentهای دو‌زبانه مقاوم‌ترند.
- Code/URL/version fragments باید LTR/isolated بمانند.
- direction سند با flex-direction قاطی نشود.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- RTL، Logical Properties، Inline/Block، Physical→Logical mapping، Bidi، Elementor V4، Flexbox Start/End و خطاهای رایج حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- هدف درس بازطراحی Layout نیست؛ فقط RTL Audit و تصمیم logical/physical است.
- همهٔ left/rightها کورکورانه تبدیل نشدند؛ case-by-case حفظ شد.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Semantic/Layout/Responsive → RTL/LTR Direction → Logical Start/End → Bidi-safe content.
- تفکیک `dir/direction` از `flex-direction`.
- هشدار درباره row-reverse افراطی و اثر روی reading/focus order.
- RTL Contract برای TUYA اضافه شد.
- جدول Audit برای Feature Item، Button، Visual Node، Code/URL و Logo Strip اضافه شد.
- Bidi test برای version، CSS fragment، URL و شماره تلفن اضافه شد.
- تصمیم logical/physical برای Positionهای Stage به case-by-case تبدیل شد.
- Design System decision برای Logical utilities اضافه شد.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. left/rightهای مهم را audit کند.
2. تشخیص دهد فاصله یا Position logical است یا physical.
3. Feature Item و Button را برای RTL/LTR بررسی کند.
4. code/URL/version fragments را LTR/isolated نگه دارد.
5. از direction برای جابه‌جایی ظاهری Icon استفاده نکند.
6. از row-reverse بدون بررسی reading/focus order استفاده نکند.

موارد ممنوع:

- بازطراحی Layout
- تغییر Position نهایی Nodeها
- تغییر Responsive Contract
- ساخت Utility جهانی بدون pattern واقعی
- تبدیل کورکورانهٔ همهٔ left/rightها
- RTL کردن code blockها

## مقدارهای شروع

مقادیر نهایی در این درس قطعی نیستند. تصمیم‌های شروع:

```text
Feature spacing: gap یا margin-inline، provisional
Button icon/text order: unknown_until_cta
Code/URL/version: LTR or bdi/auto as needed
Visual Node inset: physical/logical case-by-case
Logo Strip spacing: parent gap
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
