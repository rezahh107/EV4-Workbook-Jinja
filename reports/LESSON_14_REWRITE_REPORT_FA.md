# گزارش مرحله بعد — بازنویسی درس ۱۴ با روش Responsive Inheritance

## فایل اصلاح‌شده

- `content/units/048-lesson-14.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۴ در ریپو:

```text
درس 14 — Responsive Inheritance و Breakpointها
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از ساخت Structure، Layout، Media، Position و Layering، درس ۱۴ باید Responsive را به‌عنوان تغییر کنترل‌شدهٔ همان DOM آموزش بدهد:

- یک DOM و یک Section
- Inheritance از Desktop/Base
- Override فقط در صورت شکست واقعی
- Reset برای حذف مقدار محلی
- Breakpoint براساس شکست محتوا
- ممنوعیت Duplicate Section به عنوان راه‌حل اول

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- مدل آبشار، Override، Reset، Breakpoint، Responsive Contract، clamp، Container Query، Device Mode و Debug حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Container Query به‌عنوان CSS پیشرفته/نیازمند شواهد نسخهٔ هدف نگه داشته شد، نه قابلیت قطعی پنل V4.
- Breakpointهای واقعی بدون خواندن تنظیمات سایت قطعی اعلام نشدند.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Base/Desktop → Inheritance → Tablet/Mobile Override → Reset.
- قاعدهٔ مرکزی: Responsive یعنی همان DOM با تغییر کنترل‌شده، نه نسخهٔ جدا برای هر دستگاه.
- توضیح اینکه کپی‌کردن مقدار Desktop در Mobile با inheritance فرق دارد.
- Responsive Contract برای TUYA اضافه شد.
- Failure Log برای Resize test اضافه شد.
- تست Reset به تمرین اضافه شد.
- Duplicate Section به‌عنوان تلهٔ اصلی معرفی شد.
- Order بصری با reading/focus order تفکیک شد.
- Responsive tokens فعلاً local/provisional نگه داشته شدند.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. Responsive Contract بنویسد.
2. Desktop را base فرض کند.
3. عرض را آهسته کم کند.
4. اولین شکست واقعی را ثبت کند.
5. فقط کمترین کنترل لازم را override کند.
6. Reset را روی یک مقدار تست کند.
7. از Duplicate Section پرهیز کند.

موارد ممنوع:

- ساخت Section جدا برای Mobile
- ادعای Breakpoint قطعی بدون تنظیمات سایت
- Container Query قطعی در پنل V4 بدون شواهد نسخهٔ هدف
- Token سراسری Responsive قبل از تثبیت Contract
- تغییرات گستردهٔ Design System
- Position/Layering نهایی

## مقدارهای شروع

مقادیر نهایی در این درس قطعی نیستند. قرارداد شروع:

```text
Desktop:
  Shell Row
  Copy/Visual side-by-side
  Visual Stage کامل

Tablet:
  Row فشرده یا Column فقط بعد از شکست واقعی
  Gap کمتر فقط در صورت نیاز

Mobile:
  Shell Column
  Copy اول
  Visual بعدی
  Button تمام‌عرض فقط در صورت نیاز
  تزئین محدود
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
