# گزارش مرحله بعد — بازنویسی درس ۸ با روش Wrap و Logo Strip

## فایل اصلاح‌شده

- `content/units/040-lesson-8.md`

## موضوع واقعی درس

عنوان فعلی درس ۸ در ریپو:

```text
درس 8 — Wrap و ساخت Logo Strip
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Flex Item sizing در درس ۷، درس ۸ وارد آیتم‌های تکراری کوچک‌تر می‌شود: Logo Strip داخل Copy Area.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Wrap، nowrap، تفاوت Wrap و Hide، تفاوت align-items و align-content، و Step-Through حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Grid کامل یا Component نهایی وارد این درس نشد.
- مقدارهای Logo/GAP به‌عنوان provisional معرفی شدند.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Context → Structure → Class Scope → Box Model → Flex Container → Axis → Flex Item Sizing → Wrap.
- تأکید بر اینکه Wrap فقط اجازهٔ Flex Line جدید می‌دهد و اندازهٔ Item را حل نمی‌کند.
- تفکیک Logo Strip، Logo Item و Image.
- توضیح اینکه Logo Strip داخل Copy Area است، نه Visual Stage.
- Gap برای فاصلهٔ Logoها جایگزین Marginهای تکی شد.
- Hide کردن Logoها به‌عنوان راه‌حل اول Responsive رد شد.
- تفاوت align-items و align-content در چند خط روشن‌تر شد.
- نقش محتوایی/تزئینی Logoها و alt text به عنوان unknown ثبت شد.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. `TUYA Logo Strip` را داخل `TUYA Copy` بسازد.
2. Logoها را Child مستقیم Logo Strip کند.
3. Logo Strip را Flex Row + Wrap کند.
4. Gap را روی Parent تنظیم کند.
5. max-width/max-height Logo Image را به صورت provisional تست کند.
6. در عرض کم، Wrap را تست کند.

موارد ممنوع:

- Grid کامل
- Component نهایی Logo
- Animation
- Visual Stage
- Nodeها
- Shadow/Glow
- Background نهایی
- Typography اصلی
- Hide کردن Logoها فقط برای جا شدن

## مقدارهای شروع

```text
Display: Flex
Direction: Row
Wrap: Wrap
Gap: 12px تا 20px provisional
Logo Image max width: 80px تا 120px provisional
Logo Image max height: 28px تا 40px provisional
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
