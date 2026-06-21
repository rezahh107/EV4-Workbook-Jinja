# گزارش مرحله بعد — بازنویسی درس ۲۱ با روش Boss Fight Capstone

## فایل اصلاح‌شده

- `content/units/066-lesson-21.md`

## موضوع واقعی درس

عنوان فعلی درس ۲۱ در ریپو:

```text
درس 21 — Boss Fight — ساخت مستقل و ذهن ساختارمند
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

درس ۲۱ ایستگاه پایانی مسیر است:

- ساخت مستقل بدون راهنمای خط‌به‌خط
- تبدیل Screenshot به Content Inventory، Tree، Layout، Style System و Audit
- One DOM برای همهٔ اندازه‌ها
- ممنوعیت Absolute برای ستون‌های اصلی
- Absolute فقط داخل Visual Stage و با دلیل
- Global Class فقط برای Style تکراری واقعی
- Local Class برای استثنای محلی
- Mobile، RTL، Zoom، Keyboard، Long Content و Performance Audit
- تفکیک observed / provisional / confirmed / unknown

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- چرخهٔ Observe → Decompose → Choose → Build → Test → Explain حفظ و دقیق‌تر شد.
- Requirements اصلی درس حفظ شدند.
- قالب تصمیم‌گیری قابل کپی برای هر Section بازنویسی و کامل‌تر شد.
- تست تخریبی نهایی حفظ و دقیق‌تر شد.
- Rubric ارزیابی حفظ و کامل‌تر شد.
- درس همچنان به‌عنوان پایان مسیر آموزشی معرفی می‌شود.

## تغییرات محتوایی مهم

- Boss Fight به یک Capstone evidence-first تبدیل شد.
- Requirements غیرقابل مذاکره به جدول عملی تبدیل شدند.
- تفکیک Observation / Interpretation / Confirmed / Unknown اضافه شد.
- Tree هدف TUYA اضافه شد.
- Layout Engine Decision Table اضافه شد.
- Size Contract قبل از عددها اضافه شد.
- Final Audit Report template اضافه شد.
- Stress Tests نهایی به جدول قابل ارزیابی تبدیل شدند.
- Rubric نهایی با حوزه‌های Structure، Element choice، Class system، Responsive، RTL/Bidi، Accessibility، Performance و Evidence کامل شد.
- پایان مسیر با انتقال یادگیری به Section تازه بسته شد.

## تمرین Boss Fight

در این درس هنرجو باید:

1. TUYA را در صفحهٔ تازه بسازد.
2. بدون راهنمای خط‌به‌خط تصمیم بگیرد.
3. Content Inventory بنویسد.
4. Tree و Wrapper responsibilities را مشخص کند.
5. Layout Engine را با دلیل انتخاب کند.
6. Size Contract بنویسد.
7. Class/Variable/Component candidateها را ثبت کند.
8. Position/Layering را فقط در Stage وارد کند.
9. Responsive، RTL، State و Performance را Audit کند.
10. Stress Tests را اجرا کند.
11. Final Audit Report بنویسد.

موارد ممنوع:

- کپی عددهای Screenshot بدون تحلیل
- Absolute برای main columns یا متن اصلی
- Duplicate Section برای Mobile
- Global کردن بدون evidence
- Component زودهنگام
- ادعای Performance بدون measurement
- موفقیت فقط با Screenshot
- ادعای confirmed بدون Editor/Frontend/DevTools evidence

## معیار قبولی

```text
Structure: روشن و مسئولیت‌دار
Element choice: قابل توضیح
Class system: Global/Local روشن
Responsive: بدون horizontal overflow و بدون duplicate
RTL/Bidi: logical/physical و isolation مستند
Accessibility: Focus/Keyboard/Alt بررسی شده
Performance: candidateها و measurement method ثبت شده
Evidence: observed/proposed/confirmed/unknown جدا
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
