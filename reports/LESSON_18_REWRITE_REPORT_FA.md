# گزارش مرحله بعد — بازنویسی درس ۱۸ با روش Hybrid Migration Ladder

## فایل اصلاح‌شده

- `content/units/054-lesson-18.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۸ در ریپو:

```text
درس 18 — صفحات Hybrid V3/V4 و نردبان مهاجرت
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Design System و State، درس ۱۸ باید برخورد با صفحات واقعی Hybrid را آموزش بدهد:

- Hybrid به‌خودی‌خود خطا نیست.
- Legacy به‌خودی‌خود یعنی حذف فوری نیست.
- Migration یک پروژهٔ کنترل ریسک است.
- اول Baseline، سپس Staging Pilot، سپس Compare، سپس Replace کنترل‌شده.
- Feature Parity، Dynamic Data، Custom CSS، Add-ons، Tracking، Forms و Rollback باید بررسی شوند.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Hybrid، Migration Ladder، Staging، Feature Parity، Baseline، Dynamic Data، Performance، Custom CSS، Rollback و Compare حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- حذف فوری V3 و migration خودکار کل سایت وارد این درس نشد.
- Production change ممنوع شد؛ تمرین فقط در Staging است.
- ادعای «V4 همیشه سریع‌تر است» رد شد و benchmark لازم شد.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: V3/Legacy + V4/Atomic + Add-ons/Dynamic/CSS = Hybrid Page.
- نردبان مهاجرت از ۹ مرحله به یک روند کامل‌تر شامل baseline، dependency map، staging، QA و rollback توسعه یافت.
- Baseline checklist اضافه شد.
- Migration Decision Matrix اضافه شد.
- Risk level برای Low/Medium/High/Critical اضافه شد.
- TUYA به‌عنوان Pilot migration scenario استفاده شد، نه اینکه خود TUYA خراب شود.
- Migration Card و Compare Table اضافه شد.
- Custom CSS و DOM قدیمی به‌عنوان ریسک مستقل توضیح داده شدند.
- Behavior parity برای فرم، tracking و dynamic data وارد شد.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. یک بخش Legacy فرضی یا واقعی کم‌ریسک را انتخاب کند.
2. Migration Card بنویسد.
3. Baseline ثبت کند.
4. وابستگی‌های CSS/JS/Add-on/Dynamic/Form/Tracking را فهرست کند.
5. نسخهٔ V4 را فقط در Staging بسازد.
6. Desktop/Tablet/Mobile، Accessibility، Behavior و Performance را مقایسه کند.
7. فقط بعد از QA و Rollback جایگزینی را مجاز بداند.

موارد ممنوع:

- حذف فوری V3
- Migration در Production
- بازسازی کل سایت
- ادعای Performance بدون benchmark
- Replace بدون Baseline
- Replace بدون Rollback
- مقایسهٔ Desktop-only
- نادیده‌گرفتن Dynamic Data / Form / Tracking

## مقدارهای شروع

```text
Migration decision:
  Keep V3
  Hybridize
  Pilot one section
  Rebuild new page in V4
  Replace controlled after verification

Risk:
  Low / Medium / High / Critical

Required evidence:
  Baseline
  Dependency map
  Staging pilot
  Compare table
  QA
  Rollback
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
