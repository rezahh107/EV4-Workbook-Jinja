# نیازمندی‌های محتوایی v30

## استاندارد نگارش

- فارسی، روشن، گرم و دقیق.
- استعاره فقط برای تصویر ذهنی؛ تعریف فنی باید جداگانه بیاید.
- از «همیشه»، «هرگز» و «بهترین واحد» بدون دامنه پرهیز شود.
- مسیر UI فقط بر اساس نسخهٔ فعلی Help Center رسمی ثبت شود.
- قابلیت CSS که در UI تأیید نشده با برچسب `CSS / Custom CSS` بیاید.

## Anatomy of a Value

حداقل این مثال‌ها:

```css
padding: 1.5rem;
width: 50%;
transition-duration: 200ms;
padding: var(--space-lg);
width: min(100%, 75rem);
```

برای هرکدام:

- Property
- number / keyword / function / reference
- unit یا unitless status
- reference used for computation
- declared value
- computed/used value

## Unit Selection Framework

جدول باید ستون‌های زیر را داشته باشد:

- design intent
- Property
- candidate value/unit
- reference
- strengths
- risks
- Elementor UI status
- recommended baseline
- when another choice is better

هیچ جدول سادهٔ «هدف → واحد قطعی» مجاز نیست.

## Unit / Value Smells

حداقل:

- repeated literal smell
- arbitrary spacing smell
- arbitrary typography scale
- mixed units without intent
- viewport overuse
- fixed height with variable content
- `%` without known reference
- `100vw` plus horizontal spacing
- unnecessary responsive overrides
- variable for a one-off value
- one Size Variable reused for unrelated semantic roles

## Variables

- رسمی: Color / Font / Size.
- `space-*` و `type-*` naming یک strategy است، نه نوع رسمی.
- Variable می‌تواند داخل Class استفاده شود.
- Import/Export کل Design System و conflict handling توضیح داده شود.
- Selective individual import ادعا نشود.

## Components

- Master/Instance/Property/Override/Detach.
- فقط Atomic Elements.
- Pro + Admin برای ساخت و ویرایش.
- Editor می‌تواند Instance و exposed property را استفاده کند، اگر طبق سند فعلی مجاز باشد.
- Component nesting تا سند معتبر: `insufficient_evidence`.

## Dynamic Data

- اصطلاح‌های رسمی Dynamic Tags، Post Custom Field، Loop Grid و Query.
- ACF فقط fieldهای پشتیبانی‌شده معرفی شوند.
- این فصل به‌عنوان Elementor Pro ecosystem مشخص شود.

## Interactions

- Trigger، Effect، Type، Direction، Duration، Delay.
- Duration/Delay به ms.
- reduced motion و performance به‌عنوان راهنمای UX/CSS، نه ادعای کنترل رسمی مستقل مگر سند داشته باشد.
