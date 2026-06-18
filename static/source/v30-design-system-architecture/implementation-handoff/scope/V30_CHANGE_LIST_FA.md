# فهرست نهایی تغییرات نسخهٔ v30

## P0 — الزامی

### 1. فصل محوری «از ساخت صفحه تا ساخت سیستم»

یک فصل/پیش‌درآمد هسته‌ای پیش از ورود جدی به ساخت TUYA اضافه شود، بدون حذف یا تغییر شمارش ۲۱ درس اصلی.

محتوا:

- System First, Page Second
- CSS Thinking instead of Widget Thinking
- Reuse Before Create
- Relationship / Dependency Thinking
- Scalability
- Separation of Content, Style and Structure
- Architecture Before Building
- مقایسهٔ V3 Thinking و V4 Thinking
- workflow برنامه‌ریزی‌شده و workflow اکتشافی

### 2. ارتقای Units به Unit Strategy

به اطلس واحدها و بخش‌های مرتبط اضافه شود:

- Anatomy of a Value
- Unit Selection Framework
- Direct literal vs Size Variable vs Class declaration vs Component usage
- Unit/Value Smell Detection
- Spacing Scale و Typography Scale با برچسب مدل آموزشی
- تفاوت CSS-supported، Elementor-UI-exposed و Custom-CSS-only
- راهنمای context-aware برای px/rem/em/%/vw/vh/dvh/fr/ms/deg/keyword/function/reference

### 3. دو Step-Through جدید

1. `Literal → Size Variable → Global Class → Component usage → sitewide update`
2. `Unit selection tradeoffs` با محاسبات واقعی و بدون اعلام یک برندهٔ جهانی

هر Step-Through باید prediction، reveal، previous/next/reset، aria-live، print fallback و evidence label داشته باشد.

### 4. Variables Architecture Lab

- سه نوع رسمی Color / Font / Size
- Variable به‌عنوان مقدار نام‌دار
- Variable داخل Class
- semantic naming و primitive/semantic token به‌عنوان مدل آموزشی
- spacing و typography scale به‌عنوان کاربرد Size/Font Variables
- propagation تغییر
- Import/Export Design System
- name conflict و محدودیت انتخاب‌نکردن آیتم منفرد
- Hybrid sync با Global Colors/Fonts
- anti-patternها و «چه چیزی Variable نشود»

### 5. Components Lifecycle Lab

- ساخت Master از Atomic Elements
- exposed properties فقط در General tab و فقط فیلدهای دارای property icon
- ساخت و استفاده از Instance
- overrideهای Instance و ماندگاری آن‌ها
- update propagation از Master
- Detach Component
- گروه‌بندی Propertyها
- Admin/Editor permissions و Pro requirement
- refactor یک ساختار تکراری به Component
- چه زمانی Component نسازیم
- عدم ادعای Component Nesting تا وجود سند/fixture معتبر

### 6. Dynamic Data Case Study

یک Case Study کامل و اختیاری برای اکوسیستم Elementor Pro:

- Custom Post Type یا Post Type مشخص
- ACF fieldهای پشتیبانی‌شده
- Dynamic Tags V4
- Single Template
- Loop Grid
- Query و Include/Exclude
- fallback و empty state
- مرزبندی V4 core با Elementor Pro ecosystem

### 7. Interactions Lab

- Trigger: Page Load, Scroll Into View, While Scrolling, Hover, Click
- Effect: Fade, Slide, Scale
- Type: In / Out
- Direction
- Duration و Delay با ms
- چند Interaction روی یک Element
- تفاوت State، Transition، Interaction و Motion Effect
- performance و reduced motion

### 8. گسترش Class Conflict Debugging

Simulator موجود گسترش یابد تا این سناریوها را نشان دهد:

- Global Class A vs B و Class Manager priority
- State
- Local Class
- Custom CSS / matched rule context
- Computed winner

دو نمودار مستقل:

- Design System Dependency Graph
- Style Conflict Resolution Map

## P1 — مهم

### 9. Visualهای معماری

- V3 Thinking vs V4 Thinking
- Value Anatomy diagram
- Unit Selection decision tree
- Variables → Class declarations → Components → Instances → Pages
- Component lifecycle / dependency graph
- Unit smell heatmap یا audit card

### 10. تزریق Design System Decision به درس‌ها

در پایان درس‌های Layout، Typography، Spacing و Responsive یک سؤال کوتاه اضافه شود:

- literal یا Variable؟
- Local یا Global Class؟
- فقط style reuse یا structure reuse؟
- آیا Component لازم است؟

در درس‌های غیر unit-centric محتوای واحد مصنوعی اضافه نشود؛ `not_applicable` یا reference/keyword/unitless ثبت شود.

### 11. Progressive disclosure و UX

- مفهوم اصلی باز بماند.
- مرجع، واحدها، Step-Through، یافته، Responsive و تمرین در شروع بسته باشند.
- ارتفاع summaryهای تک‌خطی یکسان؛ چندخطی با رشد طبیعی.
- لینک عمیق disclosure والد را باز کند.
- چاپ همهٔ محتوا را نمایش دهد.

## P2 — اختیاری

- ضمیمهٔ کوتاه Theme Builder / Loop Grid / Popup architecture map.
- Angie AI فقط به‌عنوان ضمیمهٔ اختیاری، نه هستهٔ معماری.
- DOM weight visualization برای Dynamic/Loop/Form scenarios.
