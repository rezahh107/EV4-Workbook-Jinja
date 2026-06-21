# گزارش مرحله بعد — بازنویسی درس ۶ با روش Axis-aware Alignment

## فایل اصلاح‌شده

- `content/units/038-lesson-6.md`

## موضوع واقعی درس

عنوان فعلی درس ۶ در ریپو:

```text
درس 6 — Direction، Align، Justify و Gap
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Flex کردن Shell در درس ۵، درس ۶ باید هنرجو را مجبور کند محور را درست بخواند:

- Direction تعیین‌کنندهٔ Main Axis است.
- Justify همیشه روی Main Axis کار می‌کند.
- Align همیشه روی Cross Axis کار می‌کند.
- Gap فاصلهٔ بین Flex Itemهای مستقیم است.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- مدل ریل، Main/Cross Axis، Justify، Align، Gap و Step-Through حفظ و بازنویسی شدند.
- خطای حفظی «Justify=افقی / Align=عمودی» صریحاً اصلاح شد.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Order نهایی Mobile قطعی نشده است.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Context → Structure → Class Scope → Box Model → Flex Container → Axis.
- توضیح دقیق‌تر Row/Column و چرخش محور.
- توضیح RTL با Start/End به‌جای حفظ چپ/راست.
- اضافه شدن Evidence Gate برای Direction/Gap/Align/Justify.
- Gap به عنوان فاصلهٔ بین Siblingها توضیح داده شد.
- Step-Through به نسخهٔ چاپی/مفهومی حفظ شد.
- Responsive checkpoint برای Row → Column اضافه شد.
- Design System decision درباره Gap/Variable/Class/Component حفظ شد.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. `TUYA Shell` را انتخاب کند.
2. Direction را بخواند.
3. Main Axis و Cross Axis را تعیین کند.
4. Gap را روی Parent بررسی کند.
5. Justify و Align را فقط بعد از پیش‌بینی محور تغییر دهد.
6. در Mobile بعد از Column شدن محور را دوباره بخواند.

موارد ممنوع:

- Position
- Nodeها
- Order نهایی
- Visual Stage positioning
- Shadow/Glow
- Background نهایی
- Typography
- Button Style

## مقدارهای شروع

```text
Desktop Direction: Row
Mobile Direction: Column
Desktop Gap: 24px تا 40px provisional
Mobile Gap: 20px تا 32px provisional
Justify/Align: وابسته به محور، فضای آزاد و تست واقعی
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
