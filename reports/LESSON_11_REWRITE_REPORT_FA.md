# گزارش مرحله بعد — بازنویسی درس ۱۱ با روش Media Role Decision

## فایل اصلاح‌شده

- `content/units/044-lesson-11.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۱ در ریپو:

```text
درس 11 — Image، SVG، Background، Aspect Ratio و Object Fit
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از ساخت Structure، Layout، Typography و Logo Strip، درس ۱۱ باید نقش رسانه را روشن کند:

- Image یا Background؟
- Logo/SVG یا عکس raster؟
- Cover یا Contain؟
- Aspect Ratio قاب چیست؟
- رسانه محتوایی است یا تزئینی؟
- Lazy Load و LCP در حد تصمیم اولیه چگونه دیده می‌شود؟

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Decision Tree رسانه، Cover/Contain، Aspect Ratio، SVG، Image/Background، DevTools، LCP/Lazy Load و خطاهای رایج حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Position نهایی Nodeها وارد این درس نشد.
- Optimization پیشرفته و Performance audit کامل وارد این درس نشد.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Structure/Layout/Text → Media Role → Image vs Background → Aspect Ratio → Object Fit.
- قاعدهٔ مرکزی: محتوا را Image کن؛ تزئین را Background.
- Logoها به عنوان Contain-first معرفی شدند، نه Cover.
- Visual Stage فقط با Aspect Ratio قاب‌بندی می‌شود؛ Nodeها هنوز Position نمی‌شوند.
- SVG به‌عنوان برداری ولی نه خودبه‌خود سبک/امن توضیح داده شد.
- Alt/decorative decision برای هر رسانه ثبت شد.
- LCP/Lazy Load در حد تصمیم اولیه مطرح شد، نه Audit کامل.
- قرارداد رسانهٔ TUYA با وضعیت provisional/unknown ثبت شد.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. Logoها، Visual Stage، Core Cloud و Background ornament را نقش‌گذاری کند.
2. Logoها را با Contain و max-size بررسی کند.
3. Visual Stage را با aspect-ratio شروع تست کند.
4. Alt/decorative decision را provisional ثبت کند.
5. SVGها را از نظر viewBox/پیچیدگی/منبع معتبر فقط در حد یادآوری بررسی کند.

موارد ممنوع:

- Position نهایی Nodeها
- Orbit layout
- Animation
- Shadow/Glow نهایی
- Performance audit کامل
- srcset/sizes دستی
- Optimization پیشرفته
- ساخت Duplicate Image برای هر Device

## مقدارهای شروع

```text
Logo Fit: contain
Logo max-width: 80px تا 120px provisional
Logo max-height: 28px تا 40px provisional
Visual Stage aspect-ratio: 1/1 provisional
Core Cloud fit: contain provisional
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
