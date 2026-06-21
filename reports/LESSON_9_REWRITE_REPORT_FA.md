# گزارش مرحله بعد — بازنویسی درس ۹ با روش Grid Decision

## فایل اصلاح‌شده

- `content/units/041-lesson-9.md`

## موضوع واقعی درس

عنوان فعلی درس ۹ در ریپو:

```text
درس 9 — Grid و زمان درست استفاده از آن
```

این عنوان حفظ شد. بازنویسی روی همان محور انجام شد.

## هدف

بعد از Flex، Wrap و Logo Strip، درس ۹ باید تصمیم ابزار را آموزش بدهد:

- چه زمانی Flex کافی است؟
- چه زمانی Flex Wrap کافی است؟
- چه زمانی Grid واقعاً لازم است؟

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- Track، Line، Cell، Area، fr، minmax، Flex vs Grid و Decision Tree حفظ و دقیق‌تر شدند.
- تمرین‌ها مربی‌محور و evidence-first شدند.
- Grid به کل TUYA تحمیل نشد.
- دو ستون اصلی و Logo Strip همچنان با روش‌های درس‌های قبل حفظ شدند.

## تغییرات محتوایی مهم

- اتصال صریح به زنجیره: Flex Row/Column → Flex Item Sizing → Flex Wrap → Grid Decision.
- تفکیک مسئلهٔ یک‌محوره و دوبعدی.
- توضیح اینکه Grid Container فقط Childهای مستقیم را Grid Item می‌کند.
- توضیح اینکه `fr` درصد قطعی نیست.
- توضیح `minmax()` به‌عنوان حداقل/حداکثر Track، نه مقدار جهانی.
- جلوگیری از Grid زودهنگام برای Logo Strip یا دو ستون اصلی TUYA.
- Feature/Card Grid به‌عنوان Grid candidate معرفی شد.
- Orbit Nodes در این مرحله Grid نشدند؛ چون بیشتر به Stage/Position مربوط‌اند.

## تمرین TUYA

در این درس هنرجو فقط باید:

1. تصمیم بگیرد کجا Grid لازم است و کجا نیست.
2. یک Feature Grid آزمایشی کوچک بسازد.
3. دو ستون اصلی TUYA و Logo Strip را دست‌نخورده نگه دارد.
4. Grid را فقط با دلیل دوبعدی وارد کند.

موارد ممنوع:

- تبدیل TUYA Shell به Grid بدون دلیل
- تبدیل Logo Strip به Grid بدون نیاز دوبعدی
- Grid کردن Orbit Nodes
- Position
- Nodeها
- Shadow/Glow
- Background نهایی

## مقدارهای شروع

```text
Feature Grid:
  Display: Grid
  Columns: repeat(2, minmax(0, 1fr)) provisional
  Gap: 16px تا 24px provisional
  Mobile: یک ستون provisional
```

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. کنترل‌های ساختاری پایه روی فایل خروجی انجام شده‌اند.
