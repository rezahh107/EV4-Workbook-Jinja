# گزارش مرحله بعد — بازنویسی درس ۱۰ با روش Semantic Typography

## فایل اصلاح‌شده

- `content/units/043-lesson-10.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۰ در ریپو:

```text
درس 10 — Heading، Paragraph، List و Typography
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از ساخت Structure و Layout، درس ۱۰ باید محتوای Copy Area را معنایی و خوانا کند:

- Heading براساس سلسله‌مراتب محتوا
- Paragraph برای متن مستقل
- List/Feature Item برای مجموعهٔ واقعی
- Typography براساس خوانایی و متن واقعی فارسی

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- انتخاب Element معنایی، Typography، Line Height، طول خط، Hard Break، DevTools و Responsive checkpoint حفظ و دقیق‌تر شدند.
- Typography Variable vs Typography Class حفظ شد.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Font System کامل یا Design System نهایی وارد این درس نشد.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Structure/Layout → Content Elements → Semantic Hierarchy → Typography.
- تفکیک نقش معنایی از ظاهر.
- تأکید بر تست Typography فارسی با متن واقعی.
- توضیح Hard Break در Paragraph به عنوان شکننده.
- تفکیک Feature List، Feature Item، Dot/Icon و Feature Text.
- توضیح Variable/Class/Element در Typography.
- اضافه شدن Evidence Gate برای متن‌های TUYA.
- تأکید بر Mobile، متن بلند، Zoom و Load واقعی Font.
- مدیریت متن انگلیسی داخل RTL با جهت/ایزولیشن مناسب.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. متن‌های داخل `TUYA Copy` را بسازد.
2. Heading، Paragraph و Feature List را براساس نقش محتوا انتخاب کند.
3. Feature Item را با Dot/Icon و Text مستقل بسازد.
4. Typography را فقط provisional تست کند.
5. متن کوتاه/بلند و Mobile را بررسی کند.
6. Hard Break غیرضروری را حذف کند.

موارد ممنوع:

- Font System کامل
- Typography Variables نهایی
- Style نهایی
- Visual Stage
- Nodeها
- Shadow/Glow
- تغییر Shell/Flex/Grid قبلی

## مقدارهای شروع

مقادیر Typography در این مرحله قطعی نیستند. فقط candidateهای زیر ثبت شدند:

```text
c-hero-title
c-platform-intro
c-feature-item
c-feature-text
```

همه `provisional` هستند تا بعداً با Design System نهایی بررسی شوند.

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
