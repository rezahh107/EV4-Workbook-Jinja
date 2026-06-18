# AGENTS.md — قرارداد الزامی مدل زبانی

این مخزن «سورس قابل ویرایش» کتاب‌کار آفلاین Elementor V4 است. هر مدل یا عامل خودکار باید پیش از تغییر، این فایل، `llm/model-contract.yaml` و `llm/TASK.md` را کامل بخواند.

## منبع حقیقت و تقدم

1. `llm/TASK.md` برای دامنهٔ تغییر همین نوبت؛
2. این فایل و `llm/model-contract.yaml`؛
3. Schemaهای نسخه‌دار در `schemas/`؛
4. `content/course.yaml` و فایل‌های منبع `content/units/`؛
5. تست‌ها و Baselineهای معتبر؛
6. پیاده‌سازی Builder؛
7. پیشنهادهای مکالمه‌ای یا حدس‌ها.

در صورت تعارض، منبع با اولویت بالاتر را اجرا و تعارض را در گزارش نهایی ثبت کن. قواعد ناسازگار را خاموش با هم ترکیب نکن.

## مرز منبع و خروجی

- `content/`, `templates/`, `static/`, `schemas/`, `src/` و `tests/` منبع هستند.
- `dist/`, `release/` و `handoff/` تولیدی‌اند و نباید دستی ویرایش یا به‌عنوان منبع حقیقت استفاده شوند.
- تغییر محتوای دوره باید در `content/units/*.md` انجام شود، نه در HTML تولیدشده.
- ترتیب و Metadata واحدها فقط از `content/course.yaml` می‌آید.

## قواعد تغییر

- فقط مسیرهای مجازشده در Front Matter فایل `llm/TASK.md` را تغییر بده.
- شناسه‌های عمومی HTML، Anchorها، `data-*`ها، قرارداد Local Storage و رفتار تعاملی را تغییر نده مگر صریحاً در Task مجاز شده باشد.
- فایل‌های `trusted_html` را به Markdown خالص تبدیل نکن مگر Task همان واحد را مشخص کرده باشد.
- تست، Schema یا Baseline را برای پنهان‌کردن Regression ضعیف، حذف یا بازنویسی نکن.
- Dependency جدید فقط با دلیل، Pin نسخه و اصلاح مستندات مجاز است.
- ادعای `passed` یا `verified` فقط برای فرمانی مجاز است که واقعاً اجرا شده و Exit Code آن صفر بوده باشد.
- هر نبود شواهد را با `status: insufficient_evidence` گزارش کن؛ مقدار، رفتار یا قابلیت Elementor را حدس نزن.

## فرمان‌های الزامی

پس از تغییر، از ریشهٔ مخزن اجرا کن:

```bash
python validate.py
python build.py
python -m pytest -q -m "not browser"
```

اگر Browser در محیط موجود است:

```bash
python -m pytest -q -m browser
```

فرمان جامع:

```bash
python tools/check_all.py --browser
```

اگر Browser قابل اجرا نیست، نتیجه را `BLOCKED_ENVIRONMENT` ثبت کن؛ آن را Pass اعلام نکن.

## قرارداد خروجی مدل

مدل باید «کل مخزن اصلاح‌شده» را بازگرداند، نه فقط Patch یا چند Snippet. این فایل‌ها باید موجود بمانند:

- `AGENTS.md`
- `llm/TASK.md`
- `llm/model-contract.yaml`
- `content/course.yaml`
- `schemas/`
- `src/`
- `templates/`
- `tests/`
- `README.md`

مدل باید در `llm/RETURN_REPORT.md` بنویسد:

- فایل‌های تغییرکرده؛
- دلیل هر تغییر؛
- فرمان‌های اجراشده و Exit Code واقعی؛
- آزمون‌های اجرا‌نشده و علت؛
- تغییر نسخه یا Schema، اگر وجود دارد؛
- موارد `insufficient_evidence` یا `BLOCKED_ENVIRONMENT`.

## ممنوع

- ویرایش دستی `dist/` یا `release/`؛
- حذف فایل‌های تاریخی یا Evidence بدون درخواست صریح؛
- تغییر دامنهٔ Task برای «بهبودهای فرصت‌طلبانه»؛
- بازنویسی کامل معماری برای یک تغییر محتوایی؛
- افزودن متن یا رفتار ساختگی به‌عنوان حقیقت Elementor؛
- اعلام موفقیت بدون اجرای واقعی Gateها.
