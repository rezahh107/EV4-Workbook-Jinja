# گزارش مرحله بعد — بازنویسی درس ۱۲ با روش Position Stage Control

## فایل اصلاح‌شده

- `content/units/046-lesson-12.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۲ در ریپو:

```text
درس 12 — Position، Relative و Absolute
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Image/Media و Visual Stage، درس ۱۲ باید استفادهٔ کنترل‌شده از Position را آموزش بدهد:

- Stage در Flow بماند.
- Stage مرجع مختصات شود.
- Nodeهای شناور داخل Stage با Absolute کنترل شوند.
- Copy، Heading، Paragraph و Logo Strip از Flow خارج نشوند.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Normal Flow، Relative، Absolute، Containing Block، Fixed، Sticky، inset، z-index، responsive checkpoint و design-system decision حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Position نهایی همهٔ Orbit Nodeها وارد این درس نشد.
- z-index نهایی، Animation و Shadow/Glow وارد این درس نشدند.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Normal Flow → Flex/Grid Layout → Media Stage → Positioned Overlay.
- قاعدهٔ مرکزی: محتوا در Flow؛ تزئین/Node شناور داخل Stage.
- Visual Stage در Flow و Relative معرفی شد.
- Nodeها فقط داخل Stage Absolute می‌شوند.
- Containing Block از Body جدا شد.
- Relative به‌عنوان مرجع مختصات، نه لزوماً جابه‌جایی، توضیح داده شد.
- z-index به‌عنوان ابزار آخر معرفی شد.
- تمرین خرابی عمدی: حذف Relative از Stage و مشاهدهٔ فرار Node.
- Offsetها فقط provisional ثبت شدند.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. `Visual Stage` را در Flow نگه دارد.
2. `Visual Stage` را `position: relative` کند.
3. یک یا دو `Orbit Node` تستی را داخل Stage `absolute` کند.
4. حذف Relative از Stage را موقتاً تست کند.
5. Containing Block و offset را عیب‌یابی کند.

موارد ممنوع:

- Absolute کردن Copy
- Absolute کردن Heading / Paragraph
- Absolute کردن Logo Strip
- Position نهایی همهٔ Nodeها
- z-index نهایی
- Animation
- Shadow/Glow
- Background نهایی

## مقدارهای شروع

```text
Visual Stage:
  position: relative
  aspect-ratio: 1/1 provisional

Node Test A:
  position: absolute
  top: 10%
  right: 10%
  provisional

Node Test B:
  position: absolute
  bottom: 12%
  left: 12%
  provisional
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
