# گزارش مرحله بعد — بازنویسی درس ۱۹ با روش Refactor Evidence Ladder

## فایل اصلاح‌شده

- `content/units/063-lesson-19.md`

## موضوع واقعی درس

عنوان فعلی درس ۱۹ در ریپو:

```text
درس 19 — Refactor واقعی صفحهٔ Solutions
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Migration و Design System، درس ۱۹ باید یک refactor واقعی را آموزش بدهد:

- Fact صادرشده با defect اثبات‌شده قاطی نشود.
- Refactor با Redesign قاطی نشود.
- Text عادی به Normal Flow برگردد.
- Icon فقط اگر تزئینی/overlay است می‌تواند Absolute بماند.
- Offsetهای متن با Gap/Padding جایگزین شوند.
- Style مشترک فقط candidate شود تا evidence کافی جمع شود.
- تأیید فقط با Screenshot نباشد؛ Long Text، Zoom، Responsive و Accessibility هم لازم است.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- CASE-SOL-ABS-001، CASE-SOL-IMAGE-001 و CASE-SOL-REUSE-001 حفظ و دقیق‌تر شدند.
- Refactor، Baseline، Wrapper responsibility، Local→Global، Variant Extraction و Verification حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- هیچ Runtime defect بدون تست واقعی قطعی اعلام نشد.
- Component نهایی برای Solutions Card ساخته نشد؛ فقط candidate باقی ماند.

## تغییرات محتوایی مهم

- تفکیک سه برچسب `exported fact`، `proposed refactor` و `confirmed defect`.
- توضیح اینکه متن عادی معمولاً باید در Flow باشد.
- Target architecture برای Solution Card اضافه شد.
- Verification Matrix اضافه شد.
- Compare Table برای قبل/بعد اضافه شد.
- تست Long Text و Zoom به مرکز تمرین منتقل شد.
- Icon به case-by-case تبدیل شد: overlay تزئینی یا item عادی.
- Global Class فقط candidate ماند تا چند Card و variationها تأیید شوند.
- Screenshot-only approval رد شد.

## تمرین Solutions

در این درس هنرجو فقط باید:

1. یک Solution Card pilot انتخاب کند.
2. Baseline بگیرد.
3. Card V4 جدید را در Staging کنار نسخهٔ فعلی بسازد.
4. Heading و Paragraph را در Flow قرار دهد.
5. Gap/Padding را جایگزین text offset کند.
6. Icon را با تصمیم آگاهانه overlay یا item کند.
7. Long Text و Zoom را تست کند.
8. Desktop/Tablet/Mobile را مقایسه کند.
9. Result را به Fact/Refactor/Defect طبقه‌بندی کند.

موارد ممنوع:

- Refactor کل صفحه در یک حرکت
- ادعای Runtime defect بدون test
- حذف همهٔ Absoluteها بدون تشخیص role
- Redesign پنهان
- Component نهایی زودهنگام
- Global Class نهایی بدون reuse evidence
- Screenshot-only verification
- تغییر Production

## مقدارهای شروع

```text
Card Parent:
  relative only if overlay/containing block remains

Icon:
  absolute only if decorative overlay
  otherwise flow item candidate

Heading:
  normal flow

Paragraph:
  normal flow

Spacing:
  gap + padding

Shared style:
  Global Class candidate, not final

Component:
  candidate only after real variation audit
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
