<article class="lesson card-surface" data-lesson="9" id="lesson-9">

<h2 class="lesson-title former-h1">درس 9 — Grid و زمان درست استفاده از آن</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-9-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-9-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> تشخیص بدهی چه زمانی مسئله هنوز یک‌محوره است و Flex کافی است، و چه زمانی واقعاً به نقشهٔ دوبعدی ردیف/ستون نیاز داری و Grid انتخاب طبیعی‌تر است.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> همهٔ Propertyهای CSS Grid، Subgrid، Masonry، Grid Template Areas پیچیده، یا بازطراحی کامل TUYA با Grid.</p>
<p><strong>در پایان باید بتوانی:</strong> برای یک بخش جدید تصمیم بگیری: Flex، Wrap یا Grid؟ و دلیل تصمیم را با Parent، Child مستقیم، Track، Cell و Area توضیح بدهی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-9-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-9-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + ⚖ مقایسه‌ای + 🛠 اجرایی محدود</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۵–۳۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> هدف این درس تغییر همه‌چیز به Grid نیست. هنرجو باید بفهمد Grid برای مسئلهٔ دوبعدی است. اگر مسئله هنوز صف، ردیف، ستون یا Wrap ساده است، Flex همچنان انتخاب درست‌تری است.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_grid_decision_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-9-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-9-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس‌های ۵ تا ۸ چند نوع مسئلهٔ Flex را دیدی: دو ستون اصلی، جهت و محور، اندازهٔ Itemها، و Wrap برای Logo Strip. حالا باید بدانی چه زمانی این مدل کافی نیست و باید به Grid فکر کنی.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Flex Row / Column
↓
Flex Item Sizing
↓
Flex Wrap
↓
Grid Decision: آیا مسئله دوبعدی است؟</code></pre>
</figure>

<h3>مسئله</h3>
<p>گاهی Itemها فقط روی یک محور حرکت می‌کنند؛ Flex مناسب است. گاهی چند ردیف و چند ستون باید با Trackهای مشترک هماهنگ شوند؛ Grid مناسب‌تر است.</p>
<p>خطای رایج این است که هر چیزی که «چندتا آیتم کنار هم» دارد را Grid کنیم، یا برعکس، برای یک layout دوبعدی واقعی با چند Flex تو‌در‌تو طرح را پیچیده کنیم.</p>

<h3>Decision Tree</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>◇ فقط ترتیب روی یک محور مهم است؟</li>
<li>├─ بله → <strong>Flexbox</strong></li>
<li>└─ خیر</li>
<li>◇ آیتم‌ها باید در چند ردیف/ستون با Track مشترک هماهنگ شوند؟</li>
<li>├─ بله → <strong>Grid</strong></li>
<li>└─ خیر</li>
<li>◇ فقط چند آیتم شبیه هم در عرض کم به خط بعد می‌روند؟</li>
<li>├─ بله → <strong>Flex Wrap</strong> را اول بررسی کن</li>
<li>└─ خیر → ساختار و نیاز واقعی را دوباره تحلیل کن</li>
</ul>
</section>

<h3>مدل دیداری</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Flex:
[A] [B] [C] [D]

Flex Wrap:
[A] [B]
[C] [D]

Grid:
┌─────┬─────┐
│  A  │  B  │
├─────┼─────┤
│  C  │  D  │
└─────┴─────┘</code></pre>
</figure>

<h3>Grid چه چیزی اضافه می‌کند؟</h3>
<p>Grid به Parent اجازه می‌دهد یک نقشهٔ ردیف/ستون تعریف کند. Childها روی آن نقشه قرار می‌گیرند. این وقتی مهم است که هم‌راستایی ردیف‌ها و ستون‌ها، Track مشترک، Cell، Area یا span چند خانه‌ای لازم داشته باشی.</p>

<h3>واژگان اصلی</h3>
<dl class="term-grid">
<dt>Grid Container</dt><dd>Parentی که <code dir="ltr">display:grid</code> دارد.</dd>
<dt>Grid Item</dt><dd>Child مستقیم Grid Container.</dd>
<dt>Grid Line</dt><dd>خط‌های فرضی عمودی و افقی که شبکه را می‌سازند.</dd>
<dt>Track</dt><dd>فضای بین دو Grid Line؛ یک ستون یا یک ردیف.</dd>
<dt>Cell</dt><dd>خانهٔ حاصل از تقاطع یک ردیف و یک ستون.</dd>
<dt>Area</dt><dd>مستطیلی از چند Cell که یک Item می‌تواند اشغال کند.</dd>
<dt>Gap</dt><dd>فاصلهٔ بین Trackها، نه Padding داخل Itemها.</dd>
<dt>fr</dt><dd>سهمی از فضای قابل توزیع Grid، نه همیشه یک درصد قطعی.</dd>
</dl>

<h3>Flex Wrap با Grid یکی نیست</h3>
<p>Wrap اجازه می‌دهد Flex Itemها خط جدید بسازند، اما هنوز هر خط یک Flex Line است و Track مشترک واقعی بین همهٔ ردیف‌ها تعریف نمی‌شود. Grid از ابتدا نقشهٔ ستون‌ها و ردیف‌ها را تعریف می‌کند.</p>

<h3>Grid را زود تحمیل نکن</h3>
<p>برای TUYA تا اینجا، دو ستون اصلی با Flex، Logo Strip با Flex Wrap، و Copy/Visual sizing با Flex Item controls قابل توضیح است. پس Grid را فقط جایی وارد کن که نیاز دوبعدی واقعی داری؛ مثلاً یک Feature Matrix یا Card Grid با ستون‌های هم‌راستا.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-9.0.0" id="lesson-9-concept-reference">
<summary>📚 مرجع مفهومی کامل — Grid؛ Track، Line، Cell و Area</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="9" data-source-version="tuya-revised-9.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی Grid را حفظ می‌کند و به تصمیم واقعی وصل می‌کند: Grid ابزار قدرتمند است، اما فقط وقتی که مسئله واقعاً دوبعدی باشد.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-9-ref-problem">
<h3 id="lesson-9-ref-problem">۱. مسئله‌ای که Grid حل می‌کند</h3>
<p>Grid وقتی مفید است که فقط کنار هم چیدن عناصر کافی نیست. مثال‌ها:</p>
<ul>
<li>ستون‌های چند ردیف باید دقیقاً هم‌راستا باشند.</li>
<li>یک کارت باید دو ستون یا دو ردیف را اشغال کند.</li>
<li>ارتفاع ردیف‌ها و عرض ستون‌ها باید قرارداد مشترک داشته باشند.</li>
<li>جای Itemها نسبت به کل شبکه معنا دارد، نه فقط نسبت به همسایهٔ قبلی.</li>
</ul>
<p>Flexbox صف را خوب مدیریت می‌کند؛ Grid نقشهٔ دوبعدی را.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-9-hotel">
<h3 id="lesson-9-hotel">۲. تشبیه هتل</h3>
<p>یک هتل را تصور کن:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Line 1      Line 2      Line 3
  │           │           │
──┼───────────┼───────────┼── Row Line 1
  │ Room A    │ Room B    │
──┼───────────┼───────────┼── Row Line 2
  │ Room C    │ Room D    │
──┼───────────┼───────────┼── Row Line 3</code></pre>
</figure>
<ul>
<li>فاصلهٔ بین دو خط = Track</li>
<li>تقاطع یک ردیف و ستون = Cell</li>
<li>چند Cell کنار هم = Area</li>
<li>خط‌های شماره‌دار = Grid Line</li>
</ul>
<p>Item می‌تواند در یک اتاق بماند یا چند اتاق را اشغال کند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-9-flex-nesting">
<h3 id="lesson-9-flex-nesting">۳. چرا چند Flex تو‌در‌تو گاهی بد می‌شود؟</h3>
<p>با Flexهای تو‌در‌تو می‌توان طرح‌های زیادی ساخت، اما اگر هدف یک جدول/ماتریس واقعی باشد، ساختار به‌سرعت پیچیده می‌شود:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Row
├── Column
│   ├── Row
│   └── Row
└── Column
    ├── Row
    └── Row</code></pre>
</figure>
<p>Grid اجازه می‌دهد Parent مستقیماً Trackهای مشترک را تعریف کند. این یعنی Childها روی یک نقشهٔ مشترک قرار می‌گیرند، نه داخل چند صف جداگانه.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-9-fr">
<h3 id="lesson-9-fr">۴. fr چیست؟</h3>
<p><code dir="ltr">fr</code> سهمی از فضای باقی‌ماندهٔ Grid است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">grid-template-columns: 1fr 1fr 1fr;</code></pre>
</figure>
<p>اما <code dir="ltr">1fr</code> همیشه یعنی «دقیقاً یک‌سوم نهایی» نیست. Gap، Track ثابت، min-content و محدودیت Childها می‌توانند اندازهٔ واقعی را تغییر دهند.</p>
<p>برای جلوگیری از فشار min-content در بعضی شبکه‌ها، ممکن است این الگو لازم شود:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);</code></pre>
</figure>
<p>این الگو باید با محتوای واقعی تست شود، نه به‌عنوان نسخهٔ جادویی برای همه‌جا.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-9-minmax">
<h3 id="lesson-9-minmax">۵. minmax()</h3>
<p><code dir="ltr">minmax()</code> یعنی یک Track حداقل و حداکثر دارد:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">grid-template-columns: repeat(3, minmax(220px, 1fr));</code></pre>
</figure>
<p>یعنی هر ستون از ۲۲۰px کوچک‌تر نشود و در صورت وجود فضای بیشتر، سهمی از فضای آزاد بگیرد. عدد ۲۲۰ قانون جهانی نیست؛ از محتوای واقعی، خوانایی، Padding، دکمه، تصویر و عرض Parent می‌آید.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-9-auto-fit-fill">
<h3 id="lesson-9-auto-fit-fill">۶. auto-fit و auto-fill را زود قطعی نکن</h3>
<p><code dir="ltr">auto-fit</code> و <code dir="ltr">auto-fill</code> برای Gridهای Responsive مفیدند، اما در این درس فقط به‌عنوان مفهوم آشنا می‌شوند. قبل از استفاده، باید بدانی:</p>
<ul>
<li>حداقل عرض کارت چقدر است؟</li>
<li>چند ستون در Desktop هدف است؟</li>
<li>در Tablet و Mobile چه تعداد ستون قابل خواندن است؟</li>
<li>Gap چقدر فضا مصرف می‌کند؟</li>
<li>آیا Cardها ارتفاع‌های متفاوت دارند؟</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-9-tuya-use">
<h3 id="lesson-9-tuya-use">۷. در TUYA کجا Grid مناسب است و کجا نیست؟</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Grid decision in TUYA">
<table class="data-table educational-table edu-table">
<caption>تصمیم Grid در بخش‌های TUYA</caption>
<thead><tr><th scope="col">بخش</th><th scope="col">تصمیم اولیه</th><th scope="col">دلیل</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">دو ستون Copy/Visual</th><td>Flex</td><td>مسئلهٔ اصلی یک‌محوره است: دو Child مستقیم در Row/Column.</td><td><code dir="ltr">confirmed_method_so_far</code></td></tr>
<tr><th scope="row">Logo Strip</th><td>Flex Wrap</td><td>آیتم‌های تکراری ساده که در عرض کم به خط بعد می‌روند.</td><td><code dir="ltr">confirmed_method_so_far</code></td></tr>
<tr><th scope="row">Feature Matrix / Card Grid</th><td>Grid candidate</td><td>اگر ردیف و ستون باید Track مشترک داشته باشند.</td><td><code dir="ltr">provisional_until_content</code></td></tr>
<tr><th scope="row">Orbit Nodes</th><td>نه فعلاً</td><td>این‌ها بیشتر Position/Stage مسئله‌اند، نه Grid معمولی.</td><td><code dir="ltr">unknown_until_visual_stage</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-9-debug">
<h3 id="lesson-9-debug">۸. Debug Grid</h3>
<p>اگر Grid آن‌طور که انتظار داری کار نمی‌کند، این ترتیب را بررسی کن:</p>
<ol>
<li>Parent درست Grid Container است؟</li>
<li>Itemها Child مستقیم Grid Container هستند؟</li>
<li>چند ستون/ردیف تعریف شده؟</li>
<li>Gap چقدر فضا مصرف می‌کند؟</li>
<li>Trackها ثابت‌اند، fr هستند یا minmax؟</li>
<li>Childها min-width یا محتوای عریض دارند؟</li>
<li>آیا واقعاً Grid لازم بود یا Flex کافی بود؟</li>
</ol>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-9-golden">
<h3 id="lesson-9-golden">۹. قوانین طلایی</h3>
<ul>
<li><strong>Grid را برای مسئلهٔ دوبعدی استفاده کن، نه برای هر چند آیتم کنار هم.</strong></li>
<li><strong>Grid Container فقط Childهای مستقیم را Grid Item می‌کند.</strong></li>
<li><strong>Track مشترک، دلیل اصلی Grid است.</strong></li>
<li><strong>fr سهم از فضای توزیع‌پذیر است، نه درصد قطعی.</strong></li>
<li><strong>minmax() باید از محتوای واقعی و حداقل خوانایی بیاید.</strong></li>
<li><strong>Flex Wrap هنوز برای لیست‌های سادهٔ تکراری ارزشمند است.</strong></li>
<li><strong>اگر چند Flex تو‌در‌تو فقط برای شبیه‌سازی جدول ساخته‌ای، Grid را بررسی کن.</strong></li>
<li><strong>در TUYA، Grid را فقط با دلیل محتوایی/ساختاری وارد کن.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفاهیم Grid Container، Grid Item، Track، Cell، Area، fr و minmax بر پایهٔ CSS Grid و مستندات Elementor دربارهٔ Layout نوشته شده‌اند. تصمیم‌های TUYA تا پیش از محتوای واقعی و UI Validation قطعی نیستند.</p>
<ul>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout" rel="noopener noreferrer" target="_blank">MDN — CSS Grid Layout</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/fr" rel="noopener noreferrer" target="_blank">MDN — fr unit</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/minmax" rel="noopener noreferrer" target="_blank">MDN — minmax()</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-9-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-9-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Grid Tracks، fr، minmax و Gap</span>
</summary>
<section aria-labelledby="lesson-9-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در Grid، بخشی از کنترل‌ها keyword هستند، بخشی Track definition و بخشی واحد طول یا سهم از فضای باقی‌مانده.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۹" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Display Grid</th><td>keyword</td><td>Grid Container</td><td>روی Parent اشتباه اعمال شود.</td></tr>
<tr><th scope="row">Grid Template Columns</th><td>track list</td><td>عرض Container و محتوای Track</td><td>fr را درصد قطعی فرض کنی.</td></tr>
<tr><th scope="row">Grid Template Rows</th><td>track list</td><td>ارتفاع Container و محتوا</td><td>ارتفاع محتوا را نادیده بگیری.</td></tr>
<tr><th scope="row">fr</th><td>fraction unit</td><td>فضای توزیع‌پذیر</td><td>فکر کنی همیشه یک سهم مساوی نهایی است.</td></tr>
<tr><th scope="row">minmax()</th><td>function</td><td>حداقل/حداکثر Track</td><td>حداقل را بدون محتوای واقعی حدس بزنی.</td></tr>
<tr><th scope="row">Gap</th><td>length</td><td>فاصله بین Trackها</td><td>با Padding داخل Card اشتباه گرفته شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر سه ستون minmax(220px, 1fr) و دو Gap برابر 24px داشته باشی، حداقل عرض لازم حدود 708px است. اگر Parent کمتر باشد، تعداد ستون‌ها یا حداقل Track باید بازبینی شود.</p></section>
<section><h3>📱 در Responsive</h3><p>Gridهای Card در Mobile معمولاً به یک ستون یا دو ستون محدود می‌شوند. تعداد ستون را از خوانایی و محتوای واقعی استخراج کن، نه از Screenshot Desktop.</p></section>
<section><h3>🔬 در DevTools</h3><p>Grid overlay می‌تواند خطوط، Trackها، Gap و Areaها را نشان دهد. این برای اثبات تصمیم دوبعدی مفید است.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-9-grid-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Flex، Wrap یا Grid؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر سناریو را اول تصمیم بگیر، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Step Through Grid Decision">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تصمیم‌های Flex/Wrap/Grid</caption>
<thead><tr><th scope="col">سناریو</th><th scope="col">انتخاب اولیه</th><th scope="col">دلیل</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Copy و Visual کنار هم</th><td>Flex</td><td>دو Child روی یک محور.</td><td><code dir="ltr">confirmed_method_so_far</code></td></tr>
<tr><th scope="row">Logoهای تکراری که خط جدید می‌سازند</th><td>Flex Wrap</td><td>لیست سادهٔ آیتم‌های تکراری.</td><td><code dir="ltr">confirmed_method_so_far</code></td></tr>
<tr><th scope="row">سه کارت Feature در دو ردیف با ستون‌های هم‌راستا</th><td>Grid candidate</td><td>نیاز به Track مشترک.</td><td><code dir="ltr">provisional_until_content</code></td></tr>
<tr><th scope="row">Orbit Nodes دور Core</th><td>نه Grid در این مرحله</td><td>مسئله Stage/Position است، نه Grid معمولی.</td><td><code dir="ltr">unknown_until_visual_stage</code></td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-9-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-9-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Grid Decision، نه بازطراحی کل سکشن</h3>
<p>در این تمرین، Grid را فقط برای تصمیم‌گیری و یک نمونهٔ کوچک Card/Feature Grid بررسی می‌کنی. دو ستون اصلی TUYA و Logo Strip را به Grid تبدیل نمی‌کنی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 9">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از استفاده از Grid</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy/Visual با Flex قابل توضیح است.</td><td>آن‌ها را Grid نکن.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Logo Strip با Flex Wrap قابل توضیح است.</td><td>آن را Grid نکن مگر نیاز دوبعدی واقعی پیدا شود.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Feature/Card Grid ممکن است Grid candidate باشد.</td><td>فقط اگر Track مشترک لازم باشد.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>تعداد واقعی Cardها، طول متن، تصویر و Breakpointها.</td><td>Grid template قطعی نده.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط یک نمونهٔ کوچک Grid بساز</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس نه">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> تشخیص مسئلهٔ دوبعدی، نه بازطراحی TUYA.</p>
<p><strong>مسیر:</strong> Elementor Editor → داخل Copy Area یا بخش تمرینی جدا → Add Container/Div برای <code dir="ltr">Feature Grid</code>.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">Feature Grid</code> آزمایشی و چند Feature Card.</p>
<p><strong>Class فعال:</strong> Class محلی Feature Grid؛ Global جدید نساز.</p>
<p><strong>Property:</strong> Display Grid / Columns / Gap.</p>
<p><strong>نباید تغییر کند:</strong> TUYA Shell، Copy/Visual Flex، Logo Strip، Position، Nodeها، Shadow/Glow، Background نهایی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Grid فقط برای بخش دوبعدی آزمایشی استفاده شد؛ بخش‌های Flex قبلی تغییر نکردند.»</p>
</aside>

<h3>مرحلهٔ ۲ — مقدارهای شروع را به‌عنوان provisional تست کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional grid values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع برای Feature Grid</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">مقدار شروع</th><th scope="col">وضعیت</th><th scope="col">یادداشت</th></tr></thead>
<tbody>
<tr><th scope="row">Display</th><td><code dir="ltr">Grid</code></td><td><code dir="ltr">provisional_for_feature_grid</code></td><td>فقط برای بخش دوبعدی آزمایشی.</td></tr>
<tr><th scope="row">Columns</th><td><code dir="ltr">repeat(2, minmax(0, 1fr))</code></td><td><code dir="ltr">provisional</code></td><td>برای شروع دو ستون هم‌عرض.</td></tr>
<tr><th scope="row">Gap</th><td><code dir="ltr">16px</code> تا <code dir="ltr">24px</code></td><td><code dir="ltr">provisional</code></td><td>با اندازهٔ Cardها تست شود.</td></tr>
<tr><th scope="row">Mobile</th><td>یک ستون</td><td><code dir="ltr">provisional</code></td><td>طبق خوانایی و عرض واقعی.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — سه سؤال قبل از Grid</h3>
<ol>
<li>آیا واقعاً ردیف و ستون مشترک لازم دارم؟</li>
<li>آیا Childها مستقیم زیر Parent Grid هستند؟</li>
<li>آیا Flex Wrap همین مسئله را ساده‌تر حل می‌کند؟</li>
</ol>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>برای Logo Strip ساده که فقط باید در عرض کم به خط بعد برود، انتخاب اولیه چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-9">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-9-a" name="stop-question-9" type="radio" value="A"/><span>A) Grid کامل</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-9-b" name="stop-question-9" type="radio" value="B"/><span>B) Flex Wrap</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-9-c" name="stop-question-9" type="radio" value="C"/><span>C) Absolute کردن هر Logo</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Logo Strip یک لیست سادهٔ آیتم‌های تکراری است که باید خط جدید بسازد. Grid فقط وقتی بهتر است که Trackهای ردیف/ستون مشترک واقعاً لازم باشند.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> چون Grid حرفه‌ای‌تر به نظر می‌رسد، هر layout چندآیتمی را Grid کنی.</p>
<p><strong>نشانه:</strong> برای یک ردیف ساده یا Wrap ساده، template و track تعریف می‌کنی و نگهداری سخت‌تر می‌شود.</p>
<p><strong>قاعده:</strong> اول مسئله را تشخیص بده؛ ابزار را بعد انتخاب کن.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>تصور کن دو ستون اصلی TUYA را با Grid ساخته‌ای، ولی در Mobile فقط باید Copy و Visual زیر هم بیایند:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Grid تحمیلی برای مسئلهٔ یک‌محوره</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Shell: display:grid;
columns: 55% 45%;

مشکل:
- برای دو Child روی یک محور، Flex ساده‌تر بود
- تغییر به Mobile ممکن است با templateهای اضافه پیچیده شود
- ابزار قوی‌تر دلیل بهتر بودن نیست</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-49">
<fieldset>
<legend>Checkpoint درس ۹</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-49-1" name="chk-49-1" type="checkbox"/><span>می‌توانم فرق مسئلهٔ یک‌محوره و دوبعدی را توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-49-2" name="chk-49-2" type="checkbox"/><span>می‌دانم Grid Container فقط Childهای مستقیم را Grid Item می‌کند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-49-3" name="chk-49-3" type="checkbox"/><span>می‌توانم Track، Cell، Area و Gap را توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-49-4" name="chk-49-4" type="checkbox"/><span>دو ستون اصلی TUYA و Logo Strip را بی‌دلیل Grid نکرده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> یک مثال بزن که Flex مناسب است و یک مثال بزن که Grid مناسب‌تر است.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر یک Pricing Section با سه کارت و ردیف‌های قیمت/ویژگی هم‌راستا داری، چرا Grid candidate است؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Pricing Section ممکن است به Track مشترک برای ستون‌ها/ردیف‌ها نیاز داشته باشد؛ بنابراین Grid candidate است. اما اگر فقط چند Tag کنار هم هستند، Flex Wrap کافی‌تر است.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-9-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Grid را با خوانایی واقعی تنظیم کن</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_content_validation</code></p>
<ul>
<li>تعداد ستون‌های Desktop را از عرض واقعی و محتوای Card استخراج کن.</li>
<li>در Tablet ممکن است دو ستون یا یک ستون بهتر باشد؛ قطعی نیست.</li>
<li>در Mobile معمولاً یک ستون خواناتر است.</li>
<li>Gap و minmax را همراه با طول متن و تصویر واقعی بررسی کن.</li>
<li>Grid overlay را برای دیدن Trackها و Gap استفاده کن.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-9-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-9-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Grid کار می‌کند اما لازم نبود</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی تصمیم طراحی<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">decision_audit</code></p>
<p>سناریو: یک لیست سادهٔ Badgeها را با Grid ساختی، اما بعداً در Mobile تعداد آیتم‌ها تغییر می‌کند و templateهای زیادی لازم می‌شود.</p>
<p>قبل از ادامه، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا ردیف و ستون مشترک واقعاً لازم بود؟</li>
<li>آیا Flex Wrap همان نیاز را ساده‌تر حل می‌کرد؟</li>
<li>آیا Childها اندازهٔ مشابه و ترتیب طبیعی دارند؟</li>
<li>آیا Grid فقط برای حس حرفه‌ای‌تر بودن انتخاب شده؟</li>
<li>آیا نگهداری Responsive سخت‌تر شده؟</li>
</ul>
</section>
<p>نتیجهٔ درست: تصمیم ابزار را Audit کن؛ ابزار قوی‌تر همیشه تصمیم بهتر نیست.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، Grid overlay برای دیدن خطوط، Trackها و Gap مفید است. اگر هیچ Track مشترک مهمی نمی‌بینی، شاید Grid فقط پیچیدگی اضافه کرده باشد.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-9-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-9-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-52">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-52-1" name="chk-52-1" type="checkbox"/><span>می‌توانم توضیح بدهم Flex برای یک محور و Grid برای مسئلهٔ دوبعدی مناسب‌تر است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-52-2" name="chk-52-2" type="checkbox"/><span>می‌توانم Track، Cell، Area و Grid Line را توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-52-3" name="chk-52-3" type="checkbox"/><span>می‌دانم fr درصد قطعی نیست و با فضای توزیع‌پذیر کار می‌کند.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-53">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-53-1" name="chk-53-1" type="checkbox"/><span>قبل از استفاده از Grid، دلیل دوبعدی بودن مسئله را می‌نویسم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-53-2" name="chk-53-2" type="checkbox"/><span>برای یک Feature/Card Grid آزمایشی، Grid Container و Grid Itemها را درست می‌سازم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-53-3" name="chk-53-3" type="checkbox"/><span>Logo Strip و دو ستون اصلی TUYA را بدون دلیل به Grid تبدیل نمی‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-54">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-54-1" name="chk-54-1" type="checkbox"/><span>برای Pricing Section یا Feature Matrix می‌توانم توضیح بدهم چرا Grid candidate است.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-9-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-9-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، طبق ترتیب واقعی جزوه ادامه می‌دهیم. Grid را فقط وقتی وارد پروژه کن که مسئله واقعاً دوبعدی باشد.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 9</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-9-completion">
<fieldset>
<legend>ثبت پایان درس 9</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-9-complete" name="lesson-9-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
