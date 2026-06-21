# گزارش مرحله بعد — بازنویسی درس ۲ با روش Context-aware Structure

## فایل اصلاح‌شده

- `content/units/033-lesson-2.md`

## هدف

بعد از درس ۱ که Context را تثبیت کرد، درس ۲ باید Structure و Element Tree را به عنوان حلقهٔ بعدی زنجیره آموزش بدهد.

## سیاست حفظ محتوا

- بخش مفهومی حذف نشده است.
- مفهوم‌های اصلی فعلی حفظ شده‌اند: Element Tree، Parent/Child، Div Block، Flexbox، Grid، کمترین موتور لازم.
- تمرین از «بساز» به «بساز، ولی فقط Tree و بدون Style» تبدیل شده است.
- تمرین با Evidence Gate شروع می‌شود و مقدارهای قطعی را ممنوع می‌کند.

## تغییرات محتوایی مهم

- اتصال صریح درس ۲ به درس ۱: Context → Structure.
- تعریف Parent به عنوان «محدودهٔ مسئولیت»، نه فقط جعبه.
- اضافه شدن معیارهای ساخت Wrapper: Semantic، Layout، Scope، Position، Component.
- روشن شدن تفاوت Child مستقیم با Descendant.
- تفکیک Div/Flex/Grid بر اساس «کمترین موتور لازم».
- حل ابهام Section/Shell/Main به شکل provisional.
- ثبت اصلاح Rename: دوبار کلیک روی نام عنصر در Structure.
- تأکید بر اینکه Structure panel همان DOM کامل مرورگر نیست.

## تمرین TUYA

تمرین فعلی فقط باید این Tree حداقلی را بسازد:

```text
Div Block: TUYA Section
└── Div/Flexbox: TUYA Shell
    ├── Div Block: TUYA Copy
    └── Div Block: TUYA Visual
```

موارد ممنوع در این درس:

- ساخت Nodeها
- اضافه‌کردن Visual Stage مگر در درس بعد
- Class مشترک جدید
- Width/Gap/Height
- Position Absolute
- Shadow/Glow/Background

## وضعیت تست

در این محیط build/validate پروژه اجرا نشده است. فقط کنترل‌های محتوایی و ساختاری پایه انجام شده‌اند.
