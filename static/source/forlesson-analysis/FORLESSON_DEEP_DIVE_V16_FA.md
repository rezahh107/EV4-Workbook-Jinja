# تحلیل عمیق ForLesson برای نسخه 16.0.0

status: observed_export_analysis  
source: `ForLesson.zip`  
elementor_version: `4.1.3`  
verification_state: `observed_from_export`; تصمیم‌های آموزشی و اصلاحی با برچسب `teacher_evaluation` یا `proposed_refactor` آمده‌اند.

## 1. وضعیت محیط واقعی

- Elementor: `4.1.3`
- Elementor Pro: `4.1.0`
- Theme: `Blocksy 2.1.45`
- فعال بودن مسیر V4: `e_atomic_elements`, `e_classes`, `e_variables`, `e_variables_manager`, `e_components`, `e_interactions`
- تعداد Global Classes در export: `1`
- تعداد Variables در export: `0`

برداشت آموزشی: این فایل برای آموزش Atomic/Classes عالی است، اما چون Variables واقعی ندارد، درس Variables باید صادقانه بگوید که نمونهٔ فعلی هنوز Design System کامل نیست و باید مرحلهٔ بعدی آن با Variables ساخته شود.

## 2. جدول اسناد تحلیل‌شده

| سند | عنوان | تعداد Element | Empty layout | Absolute styled | Local class refs |
|---|---:|---:|---:|---:|---:|
| `HOME2` | Home2 | 127 | 5 | 0 | 122 |
| `SOLUTIONS` | Solutions | 155 | 0 | 28 | 121 |
| `MEGA_MENU_FEATURES` | Mega Menu - Features | 46 | 0 | 0 | 0 |
| `FOOTER` | Footer | 31 | 0 | 0 | 28 |

## 3. CASE-HOME2-DOM-001 — Empty Flexbox، اما نه همیشه Spacer

### observed
در Home2 پنج layout element بدون فرزند دیده شد. سه مورد مهم واقعاً Style دارند:

| id | path | width | height | background | radius | تفسیر |
|---|---:|---:|---:|---:|---:|---|
| `24a44a5b` | `2/1/0` | `33.33vw` | `56vh` | `#b2b2b2` | `8px` | پنل تصویری/Placeholder |
| `5d2f068c` | `2/1/1` | `33.33vw` | `56vh` | `#b2b2b2` | `8px` | پنل تصویری/Placeholder |
| `49dd1cd4` | `2/1/2` | `33.33vw` | `56vh` | `#b2b2b2` | `8px` | پنل تصویری/Placeholder |

### teacher_evaluation
این انتخاب اگر فقط برای Wireframe یا Placeholder تصویری بوده، قابل دفاع است. اما اگر هدف فقط فاصله‌سازی بوده، اشتباه است. Empty Flexbox نباید به‌عنوان spacer خام استفاده شود؛ چون DOM را شلوغ می‌کند، معنا ندارد، و در موبایل با `vh/vw` می‌تواند ناگهانی بزرگ یا کوچک شود.

### واحدها
- `33.33vw`: هر پنل یک‌سوم عرض viewport است. سه پنل کنار هم تقریباً 100vw می‌شوند. اگر Parent خودش padding یا gap داشته باشد، ریسک overflow افقی بالا می‌رود.
- `56vh`: ارتفاع به viewport وابسته است، نه به محتوا. روی موبایل‌های کوتاه یا مرورگرهایی با نوار آدرس متغیر ممکن است بسیار بلند یا ناپایدار دیده شود.
- `8px`: برای Radius قابل قبول است، اما اگر Design System داری بهتر است به Variable مثل `radius-card` تبدیل شود.

### نسخهٔ بهتر
- اگر این‌ها تصویر نهایی هستند: از Image/Background واقعی با Aspect Ratio و Object Fit استفاده کن.
- اگر Placeholder طراحی هستند: نام کلاس را واضح کن، مثلاً `c-hero-visual-panel`، و بعداً با محتوای واقعی جایگزین کن.
- اگر فقط فاصله می‌خواستند: حذف کن و فاصله را با Gap/Padding روی Parent کنترل کن.

## 4. CASE-HOME2-GRID-001 — Hero Grid با `100vw` و `100vh`

### observed
Root Home2 یک Container Grid دارد: `width=100vw`, `min_height=100vh`, `grid_columns=2fr`, `grid_rows=0.5fr 1fr`, background image cover.

### teacher_evaluation
برای Hero تمام‌صفحه، ایدهٔ Grid و تصویر پس‌زمینه درست است. اما `100vw` روی container سطح بالا ریسک scrollbar افقی دارد. Elementor هم در مستندات Container هشدار می‌دهد جمع عرض و margin/padding می‌تواند container را از صفحه بیرون بزند. گزینهٔ امن‌تر معمولاً `width: 100%` با Content Width مناسب و کنترل padding است.

### پیشنهاد
- برای سکشن اصلی: `width: 100%` یا Full Width تنظیم‌شده در Elementor؛ نه الزاماً `100vw`.
- برای ارتفاع: `min-height` بهتر از `height` است، اما با محتوای طولانی و موبایل تست شود.
- برای دو ستون: اگر دو ناحیهٔ واقعی داری، Grid خوب است؛ اگر فقط متن و چند دکمه داری، Flexbox ساده‌تر است.

## 5. CASE-HOME2-CTA-001 — دکمه‌های تکراری

### observed
دو Button در Hero تقریباً Style مشترک دارند: `width=250px`, `height=70px`, font family مشترک، weight مشترک، font-size `22px`, radius `8px`. تفاوت‌ها بیشتر رنگ، border و margin است.

### teacher_evaluation
این دقیقاً جایی است که Local-only بودن باعث تکرار می‌شود. در V4 بهتر است یک Shared Class پایه برای دکمه بسازی و تفاوت‌ها را در کلاس modifier نگه داری.

### نسخهٔ بهتر
- `c-btn`: اندازه، radius، typography، display/alignment
- `c-btn-primary`: background و color
- `c-btn-outline`: border، color، background
- فاصلهٔ بین دکمه‌ها: Gap روی Parent، نه margin جدا روی هر Button

## 6. CASE-SOLUTIONS-ABS-001 — Absolute زیاد، اما قابل توضیح

### observed
در صفحه Solutions تعداد 28 عنصر با `position:absolute` در styleهای desktop دیده شد. بسیاری از آن‌ها SVG/Heading/Paragraphهای overlay داخل Card هستند.

### teacher_evaluation
Absolute برای تزئین، Badge، Icon و Node شناور قابل قبول است؛ اما برای متن اصلی یا ساخت Layout توصیه نمی‌شود. اگر Title/Paragraph با Absolute قرار گرفته، در محتوای طولانی یا ترجمه فارسی/RTL احتمال شکست زیاد است.

### نسخهٔ بهتر
- Parent هر Card: `position: relative`
- تزئین یا Icon شناور: `position: absolute`
- متن واقعی Card: تا حد امکان در Normal Flow
- در Mobile: یا Absolute را خاموش کن، یا اندازه/offset مستقل بده

## 7. CASE-MEGA-MENU-REUSE-001 — بهترین نمونه برای Shared Class

### observed
در Mega Menu هشت Card با امضای Style تکراری دیده شد: `flex-direction=row`, `gap=15px`, `padding=15px`, `border-radius=15px`.

### teacher_evaluation
این یکی از بهترین تمرین‌های واقعی تو برای Design System است. اینجا نباید هر Card جداگانه local-style شود. این بخش باید به یک Shared Class تبدیل شود.

### نسخهٔ بهتر
- `c-mega-card`: row، gap، padding، radius، background/hover پایه
- `c-mega-card-icon`: اندازه و رفتار آیکن
- `c-mega-card-copy`: فاصله داخلی متن
- برای مقدارهای تکراری `15px`: Variable پیشنهادی `space-card-s` یا `space-15`

## 8. CASE-FOOTER-GRID-001 — Footer پنج‌ستونه

### observed
Footer root یک Grid با پنج ستون `1fr` و `width=100vw` دارد.

### teacher_evaluation
پنج ستون `fr` برای دسکتاپ قابل دفاع است؛ اما `100vw` همان ریسک overflow را دارد. برای Footer معمولاً `100%` + padding-inline کنترل‌شده بهتر است. برای موبایل باید evidence جدا داشته باشیم که ستون‌ها stack یا wrap می‌شوند.

## 9. واژه‌های اصلاح‌شده در نسخه 16

- `Reusable Class` → `Shared Class / Class قابل استفاده مجدد`
- `Active Class` → `کلاس هدف ویرایش`
- `State فعال` جدا از `کلاس هدف ویرایش` توضیح داده شد.
- `Component/Template/Pattern` از هم جدا شد.
- Design System به Classes + Variables + Components + Import/Export متصل شد.

## 10. منابع رسمی استفاده‌شده

- Elementor V4 Get Started: https://elementor.com/help/get-started-with-the-elementor-editor-v4/
- Classes in Elementor: https://elementor.com/help/classes-in-elementor-2/
- Class Manager: https://elementor.com/help/the-elementor-editor-class-manager/
- Prioritize conflicting styles: https://elementor.com/help/prioritize-conflicting-styles/
- Variables Manager: https://elementor.com/help/variables-manager/
- Sync variables and global elements: https://elementor.com/help/how-to-sync-variables-and-global-elements/
- Flexbox Container layout/gap: https://elementor.com/help/container-layout-tab-settings/
- Container size behavior: https://elementor.com/help/set-flexbox-container-size-behavior/
- Atomic Form element: https://elementor.com/help/atomic-form-element/
- Interactions: https://elementor.com/help/interactions/
- Atomic Elements data structure: https://developers.elementor.com/docs/data-structure/atomic-elements/
