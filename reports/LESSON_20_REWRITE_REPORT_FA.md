# گزارش مرحله بعد — بازنویسی درس ۲۰ با روش Performance Audit Evidence

## فایل اصلاح‌شده

- `content/units/064-lesson-20.md`

## موضوع واقعی درس

عنوان فعلی درس ۲۰ در ریپو:

```text
درس 20 — Performance، DOM و Audit ساختار
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Refactor و Migration، درس ۲۰ باید Performance را به شکل Audit مستند آموزش بدهد:

- Performance فقط Lighthouse Score نیست.
- DOM size فقط risk signal است، نه verdict جهانی.
- Structure، Media، Fonts، Interaction، Responsive، Third-party و Measurement Method باید جدا بررسی شوند.
- LCP/INP/CLS candidate با علت قطعی فرق دارد.
- حذف Wrapper مسئول فقط برای کاهش Node ممنوع است.
- Benchmark بدون شرایط اندازه‌گیری قابل دفاع نیست.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- چهار محور Structure/Content/Interaction/Responsive حفظ شدند و به Audit عملی وصل شدند.
- Core Web Vitals، LCP، INP، CLS، DOM Size، Component/Token effects، Performance Budget، DevTools و traps حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Benchmark تخصصی، Server/Cache tuning و JS profiling عمیق وارد این درس نشد.
- هیچ ادعای Performance قطعی بدون Trace/اندازه‌گیری مطرح نشد.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیرهٔ آموزشی: Structure + Media + Fonts + CSS + JS + Third-party + Runtime.
- تفکیک score، signal، candidate و confirmed cause.
- توضیح دقیق اینکه DOM کمتر همیشه سریع‌تر نیست.
- Wrapper Responsibility Audit اضافه شد.
- Media Audit و Font Audit اضافه شد.
- Third-party Audit اضافه شد.
- Performance Audit Card برای TUYA اضافه شد.
- Budget اولیه با وضعیت `candidate` اضافه شد.
- روش اندازه‌گیری قابل دفاع با Browser/Lighthouse/Device/Network/CPU/Cache/Runs/Median ثبت شد.
- سؤال توقف دربارهٔ DOM زیاد به «Audit مسئولیت» هدایت شد، نه حذف کور.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. Performance Audit Card بنویسد.
2. Structure، Media، Fonts، Interaction، Responsive و Third-party را جدا ثبت کند.
3. Wrapperها را با مسئولیت‌شان audit کند.
4. LCP/INP/CLS candidateها را ثبت کند اما علت قطعی اعلام نکند.
5. Budget اولیهٔ پروژه را candidate نگه دارد.
6. شرایط اندازه‌گیری قبل/بعد را ثبت کند.

موارد ممنوع:

- حذف batch wrapperها
- Production optimization
- server/cache tuning
- image pipeline نهایی
- JS profiling عمیق
- ادعای Core Web Vitals قطعی بدون measurement
- مقایسهٔ یک run
- متهم‌کردن Elementor بدون cause tree
- عدد ثابت هزینه برای هر DOM node

## مقدارهای شروع

```text
Audit axes:
  Structure
  Content
  Interaction
  Responsive
  Media
  Fonts
  Third-party
  CWV candidates

Evidence labels:
  confirmed
  provisional
  unknown
  candidate
  risk_signal
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
