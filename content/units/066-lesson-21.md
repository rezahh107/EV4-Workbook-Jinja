<article class="lesson card-surface" data-lesson="21" id="lesson-21"><h2 class="lesson-title former-h1">درس 21 — Boss Fight — ساخت مستقل و ذهن ساختارمند</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-21-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-21-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> تمام فرایند را بدون راهنمای خط‌به‌خط اجرا کنی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> کپی‌کردن مقدارهای Screenshot بدون تحلیل را.</p><p><strong>در پایان باید بتوانی:</strong> از Screenshot به Structure، Class System، Responsive و Audit نهایی برسی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-21-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-21-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟣 پروژه‌ای</td></tr><tr><th scope="row">نوع فعالیت</th><td>🛠 ساخت مستقل + 🔍 Audit + 🔁 انتقال</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۰–۳۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۹۰–۱۲۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۳۰–۴۵ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> Boss Fight است؛ در یک جلسهٔ خسته شروع نشود.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-21-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-21-lesson-understand-4">A. بفهم</h2><h3>مأموریت</h3><p>پروژهٔ TUYA را در یک صفحهٔ جدید فقط با تصویر مرجع و این Requirements بازسازی کن.</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">V4 elements only for the new build
one DOM for all device sizes
no absolute positioning for main columns
absolute only inside visual stage where justified
global classes for repeated styles via Global Classes
local classes only for unique adjustments
no horizontal overflow at 320px
RTL review
keyboard/focus review if interactive elements exist
zoom 200%
evidence labels for case-study conclusions</pre></figure></details><h3>چرخهٔ ذهن ساختارمند</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Observe
  ↓
Decompose
  ↓
Choose Element
  ↓
Build Tree
  ↓
Add Class
  ↓
Style one responsibility
  ↓
Test
  ↓
Explain</pre></figure></details><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="c13dd2c2c324e95f6f864a54e5dda3aa27402bc2b253d5f5699bb7a5150d43cd" id="lesson-21-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق ساخت مستقل؛ از مسئله به تصمیم قابل دفاع</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="28" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-28-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-28-section-01">مسئله‌ای که ساخت مستقل حل می‌کند</h3><p>دانشجو ممکن است هر کنترل را بشناسد، اما هنگام دیدن Screenshot تازه نداند از کجا شروع کند.</p><p>ساخت مستقل یعنی بدون دنبال‌کردن کلیک‌های مدرس بتوانی:</p><ul>
<li>ساختار را استخراج کنی؛</li>
<li>نقش هر Parent را توضیح بدهی؛</li>
<li>موتور Layout را انتخاب کنی؛</li>
<li>Responsive Contract بسازی؛</li>
<li>تصمیم‌ها را آزمایش و دفاع کنی.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-28-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-28-section-02">تشبیه به دنیای واقعی: جراحی با نقشهٔ بدن</h3><p>حفظ‌کردن اینکه «در این بیمار برش را اینجا بزن» مهارت عمومی نمی‌سازد. جراح باید بداند:</p><ul>
<li>هر عضو چه نقشی دارد؛</li>
<li>چه چیزی به چه چیزی متصل است؛</li>
<li>حذف یک بخش چه پیامدی دارد؛</li>
<li>نشانه‌های خطا چیست.</li>
</ul><p>ساخت مستقل نیز از مدل ذهنی می‌آید، نه از حافظهٔ محل دکمه‌ها.</p><hr/></section><section aria-labelledby="concept-v31-28-section-03" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-03">مرحله ۱: مشاهده را از تفسیر جدا کن</h3><h4>مشاهده</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">دو ستون دیده می‌شود.
تصویر از مرز کارت بیرون زده است.
چهار Node تزئینی اطراف تصویر هستند.
در Mobile تصویر زیر متن آمده است.
</code></pre></figure><h4>تفسیر</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">احتمالاً Parent Flex Row است.
احتمالاً Visual Stage Position Relative دارد.
Nodeها احتمالاً Absolute هستند.
</code></pre></figure><p>تفسیر را حقیقت قطعی معرفی نکن تا در Tree یا DevTools تأیید شود.</p><hr/></section><section aria-labelledby="concept-v31-28-section-04" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-04">مرحله ۲: Content Inventory</h3><p>قبل از Containerها، محتوا را فهرست کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Eyebrow
Heading
Paragraph
Button group
Main image
Decorative nodes
Logo list
</code></pre></figure><p>محتوا می‌گوید چه چیزهایی باید معنای مستقل داشته باشند.</p><hr/></section><section aria-labelledby="concept-v31-28-section-05" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-05">مرحله ۳: Grouping</h3><p>عناصر را بر اساس مسئولیت گروه‌بندی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Hero
├── Copy Group
│   ├── Eyebrow
│   ├── Heading
│   ├── Paragraph
│   └── Actions
└── Visual Stage
    ├── Main Image
    └── Decorative Nodes
</code></pre></figure><p>هر Wrapper باید یک پاسخ داشته باشد:</p><blockquote>
<p>چرا وجود داری؟</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-28-section-06" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-06">مرحله ۴: Layout Engine</h3><p>برای هر Parent انتخاب کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Normal Flow
Flex
Grid
Positioned Stage
</code></pre></figure><p>کمترین موتور لازم را انتخاب کن.</p><ul>
<li>یک ستون متن → Flow/Flex Column</li>
<li>Copy و Visual → Flex Row یا Grid</li>
<li>Card Matrix → Grid</li>
<li>Badge روی Image → Absolute در Stage</li>
</ul><hr/></section><section aria-labelledby="concept-v31-28-section-07" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-07">مرحله ۵: قرارداد اندازه</h3><p>فقط Width وارد نکن. بنویس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Copy: basis/grow/shrink/min-width
Visual: basis/grow/shrink/aspect-ratio
Parent: max-width/padding/gap
</code></pre></figure><p>اندازه‌ها باید رابطه‌ای باشند، نه مجموعه عددهای جدا.</p><hr/></section><section aria-labelledby="concept-v31-28-section-08" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-08">مرحله ۶: سیستم Style</h3><p>برای هر تصمیم مشخص کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Local Class?
Global Class?
Utility Class?
Variable?
Component?
Variant pattern?
</code></pre></figure><p>مثال:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Hero layout → Global Class اگر تکرارشونده
Brand color → Variable
CTA structure → Component در صورت تکرار ساختاری
Node offset خاص → Local value
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-28-section-09" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-09">مرحله ۷: Responsive Contract</h3><p>پیش از Device Mode بنویس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">چه چیزی ثابت می‌ماند؟
چه چیزی Direction عوض می‌کند؟
چه چیزی Wrap می‌شود؟
چه چیزی Scale می‌شود؟
چه چیزی واقعاً حذف می‌شود؟
چه چیزی نباید Duplicate شود؟
</code></pre></figure><p>سپس Overrideهای حداقلی بساز.</p><hr/></section><section aria-labelledby="concept-v31-28-section-10" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-10">مرحله ۸: State، Dynamic و Accessibility</h3><ul>
<li>Button Hover/Focus/Active</li>
<li>متن بلند</li>
<li>تصویر خالی</li>
<li>Dynamic field missing</li>
<li>Keyboard order</li>
<li>Focus visible</li>
<li>Alt/Label</li>
<li>Reduced motion</li>
</ul><p>Layout فقط Screenshot ثابت نیست.</p><hr/></section><section aria-labelledby="concept-v31-28-section-11" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-28-section-11">در Elementor V4</h3><p>Navigator یا Tree را برای اثبات رابطه Parent/Child، Classes Field را برای منبع Style، Variables/Classes Manager را برای تصمیم‌های مرکزی و Device Mode را برای Overrideها به کار ببر. سپس خروجی را در Frontend و DevTools تأیید کن؛ Editor محل تصمیم‌گیری است، اما مرورگر شاهد رفتار نهایی است.</p></section><section aria-labelledby="concept-v31-28-section-12" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-28-section-12">مرحله ۹: Audit</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Tree
Layout
Computed Style
Responsive widths
States
Dynamic data
Accessibility
Performance
</code></pre></figure><p>اگر تصمیمی را نمی‌توانی توضیح بدهی، هنوز احتمالاً تصادفی است.</p><hr/></section><section aria-labelledby="concept-v31-28-section-13" class="concept-reference-part"><h3 id="concept-v31-28-section-13">قالب تصمیم‌گیری قابل کپی برای هر Section</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">نام Section:
هدف محتوایی:

Content Inventory:
- ...

Tree:
- Parent:
- Children:
- Wrapper responsibilities:

Layout Engine:
- دلیل انتخاب Flex/Grid/Flow:

Size Contract:
- Parent width/max-width:
- Child basis/grow/shrink:
- Min/Max constraints:
- Gap/Padding:

Style System:
- Local Classes:
- Global Classes:
- Utilities:
- Variables:
- Components:

Position/Layering:
- Containing block:
- Absolute items:
- Stacking contexts:
- Overflow:

Responsive Contract:
- Desktop:
- Tablet:
- Mobile:
- Reset/Overrides:

Content Stress Cases:
- Short:
- Long:
- Empty:
- Missing image:

Accessibility:
- Semantic elements:
- Focus order:
- Focus visible:
- Labels/alt:

Performance:
- LCP candidate:
- Media weight:
- Interactions:
- Duplicate content:

Evidence:
- Editor observation:
- DevTools computed result:
- Screenshot widths:
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-28-section-14" class="concept-reference-part"><h3 id="concept-v31-28-section-14">علت‌یابی معکوس</h3><p>روی Duplicate امن، یک خطا ایجاد کن:</p><ul>
<li>Wrapper مسئول را حذف کن.</li>
<li>Direction را عوض کن.</li>
<li>Min Width را بردار.</li>
<li>Overflow Hidden اضافه کن.</li>
</ul><p>سپس بپرس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">اولین نشانهٔ شکست چیست؟
کدام مسئولیت از بین رفت؟
آیا شکست ساختاری، اندازه‌ای، لایه‌ای یا Stateی است؟
کدام شاهد در DevTools آن را تأیید می‌کند؟
</code></pre></figure><p>این تمرین مغز را از «کلیک جادویی» به «تشخیص علت» می‌برد.</p><hr/></section><section aria-labelledby="concept-v31-28-section-15" class="concept-reference-part"><h3 id="concept-v31-28-section-15">دفاع از تصمیم</h3><p>پاسخ ضعیف:</p><blockquote>
<p>چون این‌طوری درست شد.</p>
</blockquote><p>پاسخ قابل دفاع:</p><blockquote>
<p>Parent را Flex Row انتخاب کردم چون Copy و Visual یک رابطهٔ یک‌بعدی دارند. Visual Stage را Relative کردم چون فقط Nodeهای تزئینی باید Absolute باشند. Copy را در Flow نگه داشتم تا متن بلند Height Parent را افزایش دهد. در Mobile Direction را Column کردم و Offsetهای Node را کاهش دادم.</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-28-section-16" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-28-section-16">اشتباهات رایج</h3><ul>
<li>شروع از Margin و Position</li>
<li>کپی Tree بدون فهم مسئولیت</li>
<li>ساخت Wrapper برای هر Element</li>
<li>استفاده از Absolute برای محتوای اصلی</li>
<li>ساخت Class و Variable بدون Intent</li>
<li>تنظیم Responsive با تقلید عددها</li>
<li>تست فقط Screenshot اولیه</li>
<li>نادیده‌گرفتن Dynamic Content</li>
<li>ادعای موفقیت بدون Frontend و DevTools</li>
</ul><hr/></section><section aria-labelledby="concept-v31-28-section-17" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-28-section-17">تصویر ذهنی نهایی</h3><p>ساخت مستقل جراحی با نقشهٔ بدن است. هر Container عضو یا اتصال مشخصی دارد. وقتی می‌دانی هر بخش چرا وجود دارد، می‌توانی طرح تازه را بسازی، خطا را پیدا کنی و از تصمیم خود دفاع کنی.</p><hr/></section><section aria-labelledby="concept-v31-28-section-18" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-28-section-18">قوانین طلایی</h3><ul>
<li><strong>«از محتوا به Tree برو، از Tree به Layout و از Layout به Style.»</strong></li>
<li><strong>«هر Wrapper باید مسئولیت قابل توضیح داشته باشد.»</strong></li>
<li><strong>«مشاهده را با تفسیر قاطی نکن.»</strong></li>
<li><strong>«Responsive را پیش از عددها به‌صورت قرارداد بنویس.»</strong></li>
<li><strong>«تصمیمی که شاهد Editor و DevTools ندارد، هنوز تأیید نشده است.»</strong></li>
<li><strong>«هدف نهایی پیدا کردن دکمه نیست؛ ساختن مدل علت و معلول است.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Editor V4, classes, variables, components and responsive editing</li>
<li>CSS Flexbox/Grid/Position specifications</li>
<li>Chrome DevTools CSS and Performance references</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-21-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-21-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Boss Fight؛ انتخاب واحد باید قابل توضیح باشد</span></summary>
<section aria-labelledby="lesson-21-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در پروژهٔ مستقل باید برای هر عدد پاسخ بدهی: Property چیست؟ واحد نسبت به چیست؟ چرا این واحد؟ در breakpoint بعد چه می‌شود؟</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> در امتحان نهایی فقط جواب نمی‌دهی؛ روش حل و خط‌کش انتخاب‌شده را هم توضیح می‌دهی.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Layout sizing</th><td><code dir="ltr">width / height / basis</code></td><td>واحدهای مناسب context</td><td>Parent/root/viewport</td><td>براساس intent و طرح.</td><td>عدد تصادفی بدون مرجع ثبت نشود.</td><td><code dir="ltr">E_SIZE</code></td></tr><tr><th scope="row">Spacing</th><td><code dir="ltr">gap / padding / margin</code></td><td>px/rem/%/vw برحسب کنترل</td><td>رابطه یا context</td><td>Scale محدود و قابل تکرار.</td><td>Margin برای درمان Tree اشتباه ممنوع.</td><td><code dir="ltr">E_SPACING</code></td></tr><tr><th scope="row">Typography</th><td><code dir="ltr">font-size / line-height</code></td><td>rem/em/px/vw</td><td>root/parent/viewport</td><td>خوانایی و scale.</td><td>Fluid بدون حد استفاده نشود.</td><td><code dir="ltr">E_TYPO_GENERAL</code></td></tr><tr><th scope="row">Motion</th><td><code dir="ltr">duration / transform</code></td><td>ms/s، deg، length، number</td><td>زمان/زاویه/Box</td><td>کم و قابل دسترسی.</td><td>autoplay و motion غیرضروری محدود شود.</td><td><code dir="ltr">E_EFFECTS</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>برای هر تصمیم یک برگه ثبت کن: declared value → reference → computed value → responsive override → نتیجهٔ بصری.</p></section>
<section><h3>📱 در Responsive</h3><p>قبولی پروژه نیازمند تست عرض‌های بین breakpointها، RTL و frontend واقعی است.</p></section>
<section><h3>🔬 در DevTools</h3><p>برای سه تصمیم کلیدی screenshot از Computed/Box Model و source rule ذخیره کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/style-tab-size/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Size</a>، <a href="https://elementor.com/help/style-tab-spacing/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Spacing</a>، <a href="https://elementor.com/help/what-is-typography/" rel="noopener noreferrer" target="_blank">Elementor — Typography and units</a>، <a href="https://elementor.com/help/style-tab-effects/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Effects</a>، <a href="https://elementor.com/help/responsive-editing/" rel="noopener noreferrer" target="_blank">Elementor V4 — Responsive editing</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-21-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-21-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>ساخت مستقل</h3><p>فقط این Checkpointها را ببین:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">1. Shell
2. Main Layout
3. Copy Content
4. Logo Strip
5. Visual Stage
6. Core + Cloud
7. Nodes
8. Responsive
9. RTL + Accessibility
10. Audit</pre></figure></details><h3>❓ سؤال توقف نهایی</h3><p>اگر Layout در Mobile خراب شد، آیا اول باید Element جدید بسازی؟</p><details class="disclosure-card"><summary>پاسخ</summary>
<p>نه. ابتدا Element، Parent، کلاس هدف ویرایش، Device Size، State و یک Property مشکوک را بررسی کن.</p>
</details><h3>⚠️ تلهٔ نهایی</h3><p><strong>تله:</strong> برای رسیدن سریع به Screenshot، تصمیم‌هایی بسازی که نتوانی توضیح بدهی.</p><p>قاعده:</p><blockquote>
<p>هر Element، Class و Override باید یک دلیل قابل بیان داشته باشد.</p>
</blockquote><h3>🧪 تست تخریبی نهایی</h3><ul>
<li>Intro را دو برابر طولانی کن؛</li>
<li>Logo پنجم اضافه کن؛</li>
<li>Font Size را افزایش بده؛</li>
<li>Direction را RTL/LTR عوض کن؛</li>
<li>Preview را 320px کن؛</li>
<li>Zoom را 200% کن؛</li>
<li>یکی از Nodeها را بزرگ‌تر کن.</li>
</ul><h4>👀 انتظار از ساختار سالم</h4><ul>
<li>Main Flow حفظ می‌شود؛</li>
<li>Copy رشد می‌کند؛</li>
<li>Logoها Wrap می‌شوند؛</li>
<li>Visual از Parent بیرون نمی‌زند؛</li>
<li>Text با Nodeها برخورد نمی‌کند؛</li>
<li>Structure قابل فهم باقی می‌ماند.</li>
</ul><h3>Rubric ارزیابی</h3><div aria-label="جدول آموزشی دوره — Rubric ارزیابی" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — Rubric ارزیابی</caption><thead><tr><th scope="col">حوزه</th><th scope="col">۰</th><th scope="col">۱</th><th scope="col">۲</th></tr></thead><tbody><tr><th scope="row">Structure</th><td>آشفته</td><td>قابل استفاده</td><td>روشن و کم‌ابهام</td></tr><tr><th scope="row">Element choice</th><td>تصادفی</td><td>عمدتاً درست</td><td>قابل توضیح</td></tr><tr><th scope="row">Class system</th><td>تکراری</td><td>نیمه‌منظم</td><td>Global/Local روشن</td></tr><tr><th scope="row">Responsive</th><td>چند شکست</td><td>قابل استفاده</td><td>مقاوم و تست‌شده</td></tr><tr><th scope="row">Accessibility</th><td>بررسی نشده</td><td>پایه</td><td>مستند و تست‌شده</td></tr><tr><th scope="row">Evidence</th><td>ادعای قطعی</td><td>کمی تفکیک</td><td>observed/proposed روشن</td></tr></tbody></table></div><h3>Checkpoint نهایی</h3><section aria-labelledby="section-hidden-299-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-299-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-120"><fieldset><legend>Checkpoint نهایی</legend><label class="choice-row"><input data-persist="checkbox" id="chk-120-1" name="chk-120-1" type="checkbox"/><span>می‌توانم Tree را از حفظ بکشم</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-120-2" name="chk-120-2" type="checkbox"/><span>دلیل Flex/Grid/Div Block را می‌گویم</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-120-3" name="chk-120-3" type="checkbox"/><span>Classها مسئولیت روشن دارند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-120-4" name="chk-120-4" type="checkbox"/><span>Mobile، RTL و Zoom تست شده‌اند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-120-5" name="chk-120-5" type="checkbox"/><span>مشکلات را با مسیر ثابت بررسی می‌کنم</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-120-6" name="chk-120-6" type="checkbox"/><span>می‌توانم یک Hybrid section را بدون ترس تحلیل کنم</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> چرخهٔ ذهن ساختارمند چیست؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> برای یک سکشن جدید متن + تصویر، سه تصمیمی را بنویس که از TUYA منتقل می‌کنی و یک تصمیمی که باید تغییر کند.</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-121"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-121-1" name="chk-121-1" type="checkbox"/><span>حداقل سه تصمیم قابل انتقال از TUYA را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-121-2" name="chk-121-2" type="checkbox"/><span>حداقل یک تفاوت واقعی طرح جدید را توضیح داده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-121-3" name="chk-121-3" type="checkbox"/><span>ساخت مستقل را با Mobile، RTL، Zoom، محتوا و Class System اثبات کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-21-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-21-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>ایستگاه پایانی — انتقال یادگیری</h3><p>همان منطق را روی یک طرح دیگر اجرا کن:</p><figure class="visual-figure structure-content-examples"><figcaption>نمونه‌های Structure + Content</figcaption><div class="visual-card-grid"><div class="visual-box">متن + تصویر محصول</div><div class="visual-box">لیست خدمات + نمودار آماری</div><div class="visual-box">معرفی تیم + عکس گروهی</div></div></figure><p>اگر فقط TUYA را کپی کنی، Pattern را حفظ کرده‌ای. اگر همان تصمیم‌ها را روی طرح جدید توضیح بدهی، مفهوم را فهمیده‌ای.</p><h3>🔬 پشت صحنه</h3><p>موفقیت این دوره با تعداد Propertyهای حفظ‌شده سنجیده نمی‌شود؛ با کیفیت تصمیم، ساختار و Debugging سنجیده می‌شود.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-21-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-21-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-123"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-123-1" name="chk-123-1" type="checkbox"/><span>می‌توانی چرخهٔ Observe → Decompose → Choose → Build → Test → Explain را از حفظ اجرا کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-123-2" name="chk-123-2" type="checkbox"/><span>می‌توانی تفاوت کپی‌کردن Screenshot و بازسازی ساختارمند را توضیح بدهی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-124"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-124-1" name="chk-124-1" type="checkbox"/><span>پروژهٔ TUYA را در صفحه‌ای تازه با V4 و بدون راهنمای خط‌به‌خط بازسازی می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-124-2" name="chk-124-2" type="checkbox"/><span>Mobile، RTL، Zoom، Long Content و Class System را مستند تست می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-125"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-125-1" name="chk-125-1" type="checkbox"/><span>همان تصمیم‌ها را روی یک طرح «متن + تصویر محصول» اجرا می‌کنی و تفاوت‌های لازم را توضیح می‌دهی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-21-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-21-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>دوره تمام شد. از اینجا پروژه‌های واقعی تو به تمرین‌های بعدی تبدیل می‌شوند؛ نه با حدس، بلکه با مشاهده، تصمیم و اثبات.</p><hr/><hr/><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 21</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-21-completion"><fieldset><legend>ثبت پایان درس 21</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-21-complete" name="lesson-21-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details></article>
