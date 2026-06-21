# گزارش مرحله بعد — بازنویسی درس ۳ با روش Class Scope و Evidence-first

## فایل اصلاح‌شده

- `content/units/034-lesson-3.md`

## اصلاح مسیر

در پیام قبلی، قدم بعدی را به‌صورت مفهومی Flow/Display معرفی کرده بودم؛ اما فایل واقعی درس ۳ در ریپو با عنوان زیر است:

```text
درس 3 — Local Class، Global Class و کلاس هدف ویرایش
```

بنابراین عنوان و ترتیب رسمی دوره حفظ شد و درس ۳ با همین موضوع بازنویسی شد. Flow/Display باید در درس مرتبط با Layout/Position وارد شود، نه با تغییر عنوان درس ۳.

## هدف

بعد از Context و Structure، درس ۳ باید Scope تغییرهای ظاهری را آموزش بدهد: Style روی کدام Class ثبت می‌شود و آن Class روی چند Element اثر دارد.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- مفاهیم Local Class، Global Class، کلاس هدف ویرایش، conflict، State و Device حفظ شده‌اند.
- تمرین‌ها مربی‌محور شدند.
- Design System کامل یا ساخت Global Classهای زودهنگام وارد تمرین نشده است.

## تغییرات محتوایی مهم

- اتصال صریح به درس‌های ۱ و ۲: Context → Structure → Class Scope.
- تعریف Class به‌عنوان محدودهٔ اثر Style.
- توضیح اینکه Class ساختار نمی‌سازد؛ روی Element موجود Style اعمال می‌کند.
- تفکیک Variable / Class / Component در حد لازم.
- Decision Tree برای Local ماندن یا Global شدن.
- Evidence Gate قبل از کار با Class.
- تمرین TUYA به Class Audit تبدیل شد، نه ساخت Design System کامل.
- تأکید بر Class target، State و Device قبل از تغییر Style.
- Class Candidateهای TUYA با وضعیت provisional/unknown ثبت شدند.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. یک Element از Tree درس ۲ را انتخاب کند.
2. Classهای فعال را ببیند.
3. Class هدف ویرایش را بنویسد.
4. Candidateهای Local/Global را روی کاغذ دسته‌بندی کند.
5. فقط یک تغییر کوچک و قابل Undo انجام دهد.

موارد ممنوع:

- ساخت Design System کامل
- ساخت Global Class بدون تکرار واقعی
- تعیین نهایی Node classها
- تعیین نهایی Shadow/Glow/Width/Height/Position
- Component ساختن

## منابع رسمی بررسی‌شده

- Elementor — Differences between Editor V3 and V4
- Elementor — Classes in Elementor
- Elementor — Style tab: Layout

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
