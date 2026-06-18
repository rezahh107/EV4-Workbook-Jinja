# راستی‌آزمایی پیشنهاد جدید درباره Units و Design System

## حکم کلی

```text
status: accepted_with_corrections
```

جهت اصلی پیشنهاد درست است: بخش Units نباید فقط به «این واحد چگونه محاسبه می‌شود؟» پاسخ دهد؛ باید به سؤال معماری «این مقدار مستقیم نوشته شود، Variable شود، در Class مصرف شود یا در یک Component به‌کار رود؟» نیز پاسخ دهد.

## موارد پذیرفته‌شده

1. افزودن لایهٔ `Design System Decision` به اطلس و بخش‌های محلی واحدها.
2. ساخت `Unit Selection Framework` به‌صورت context-aware، نه قوانین مطلق.
3. اتصال Size Variableها به spacing scale، typography scale و مقادیر مشترک.
4. افزودن `Anatomy of a Value` برای تفکیک Property، number، unit، keyword، function و reference.
5. افزودن `Unit / Value Smell Detection` برای کشف literalهای تکراری و scaleهای نامنظم.
6. استفاده از Step-Through برای نمایش مسیر literal → variable → class → component usage و propagation.
7. کم‌کردن محتوای مصنوعی در درس‌هایی که unit-centric نیستند؛ در این درس‌ها `not_applicable` یا نوع مقدار reference/keyword/unitless کافی است.
8. پررنگ‌ترکردن Variables، Classes، Components، Dynamic Data و Interactions در معماری کلی دوره.

## اصلاحات ضروری

### Variable برابر Value + Unit نیست

تعریف رسمی Elementor این است که Variable نام یا مرجعی برای یک مقدار است. فقط **Size Variable** ممکن است یک مقدار اندازه همراه واحد داشته باشد. Color Variable و Font Variable واحد طول ندارند.

عبارت مجاز:

```text
Size Variable = یک مقدار اندازهٔ نام‌دار که ممکن است واحد داشته باشد.
Variable = یک مقدار نام‌دار/مرجع قابل استفاده مجدد.
```

عبارت ممنوع:

```text
Variable همیشه برابر Value + Unit است.
```

### Space Variable و Typography Variable نوع رسمی نیستند

Elementor سه نوع رسمی دارد:

- Color Variable
- Font Variable
- Size Variable

`spacing token` و `typography scale` استراتژی‌های آموزشی/معماری هستند که می‌توانند با Size و Font Variable ساخته شوند؛ باید با برچسب `derived_educational_model` معرفی شوند.

### Unit Selection نسخهٔ مطلق ندارد

جدول‌هایی مانند «Typography همیشه rem» یا «Full Width همیشه vw» نباید ساخته شوند. انتخاب به Property، containing block، طرح، Accessibility، Responsive و واحدهای واقعی کنترل Elementor بستگی دارد.

به‌ویژه:

- `100vw` انتخاب پیش‌فرض مناسبی برای همهٔ سکشن‌های Full Width نیست و می‌تواند overflow بسازد.
- `dvh` یک قابلیت CSS است؛ عرضه‌شدن آن در تمام کنترل‌های Elementor تأیید نشده است.
- تغییر root font-size می‌تواند remها را تغییر دهد، اما نباید به‌عنوان workflow عمومی Elementor توصیه شود.

### زنجیرهٔ اجباری وجود ندارد

این زنجیره نباید به‌عنوان قانون اجباری معرفی شود:

```text
Unit → Variable → Class → Component
```

مدل دقیق‌تر:

```text
Value یا Variable
→ در declaration یک Local/Global Class مصرف می‌شود
→ Component می‌تواند آن Classها و Variableها را در ساختار خود استفاده کند
→ Instance از Master و Propertyهای exposeشده پیروی می‌کند
```

### Design dependency با CSS cascade یکی نیست

نمودار Variables → Classes → Components → Instances → Pages یک **نقشهٔ وابستگی** است، نه زنجیرهٔ Cascade. حل تعارض Style باید در نمودار جداگانه نمایش داده شود.

## مواردی که در v29 از قبل وجود دارند و نباید دوباره به‌عنوان قابلیت جدید ساخته شوند

- ۲۸ بخش «تنظیمات، مقدارها و واحدها»
- اطلس مرکزی واحدها
- Step-Through محاسباتی ۸ مرحله‌ای
- تفکیک Elementor UI / CSS / Custom CSS / Computed Style
- مثال Size Variable در درس Design System
- Class Priority Simulator
- Responsive Inheritance Simulator

نسخهٔ بعدی باید این‌ها را **گسترش و یکپارچه** کند، نه دوباره از صفر بسازد.
