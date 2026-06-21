<article class="lesson card-surface" data-lesson="12" id="lesson-12">

<h2 class="lesson-title former-h1">درس 12 — Position، Relative و Absolute</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-12-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-12-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> Absolute را فقط برای هم‌پوشانی هدفمند و داخل Containing Block درست استفاده کنی؛ یعنی Visual Stage در Flow بماند، اما Nodeهای شناور داخل همان Stage موقعیت بگیرند.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام جزئیات Positioned Layout، Sticky پیچیده، Fixed advanced، z-index عمیق، یا Position نهایی تمام Orbit Nodeها.</p>
<p><strong>در پایان باید بتوانی:</strong> Core و یک یا دو Node پایه را داخل Visual Stage کنترل کنی، بدون اینکه Main Flow، Copy، Logo Strip، Heading یا Paragraph خراب شود.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-12-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-12-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی محدود + 🔍 عیب‌یابی</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس نقطهٔ خطر است. اگر هنرجو Absolute را برای حل هر مشکل Layout استفاده کند، همهٔ درس‌های Flow، Flex، Typography و Media خراب می‌شوند. تمرکز باید روی Containing Block و خروج از Flow باشد.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_position_stage_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-12-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-12-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>تا درس ۱۱، Structure، Text، Media و Visual Stage را آماده کردی. حالا فقط برای عناصر شناور داخل Visual Stage وارد Position می‌شوی. این یعنی Position ابزار تکمیل Stage است، نه جایگزین Flow و Layout.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Normal Flow
↓
Flex/Grid Layout
↓
Media Stage
↓
Positioned Overlay
↓
Relative Stage + Absolute Node</code></pre>
</figure>

<h3>مسئله</h3>
<p>گاهی باید یک Badge روی گوشهٔ تصویر، یک Node دور Core، یا یک Ornament داخل قاب بصری قرار بگیرد. اینجا Absolute می‌تواند مفید باشد. اما اگر متن، ستون اصلی، Logo Strip یا Section را Absolute کنی، Parent ارتفاع واقعی را نمی‌فهمد و Responsive به مجموعه‌ای از Offsetهای شکننده تبدیل می‌شود.</p>

<h3>مدل ذهنی</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Normal Flow</dt><dd>صف طبیعی صفحه؛ عناصر جای خود را اشغال می‌کنند و Parent ارتفاع واقعی می‌گیرد.</dd>
<dt>Relative Parent</dt><dd>اتاق مرجع؛ خودش معمولاً در Flow می‌ماند و مختصات Childهای Absolute را محدود می‌کند.</dd>
<dt>Absolute Child</dt><dd>استیکر داخل اتاق؛ از Flow خارج می‌شود و نسبت به Containing Block موقعیت می‌گیرد.</dd>
<dt>Containing Block</dt><dd>مرجع مختصات برای عنصر Positioned؛ همیشه Body نیست.</dd>
<dt>Inset / Top / Right / Bottom / Left</dt><dd>مختصات فاصله از مرجع؛ در RTL بهتر است logical inset را هم بشناسی.</dd>
</dl>
</section>

<h3>تصمیم سریع</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Position decision">
<table class="data-table educational-table edu-table">
<caption>چه چیزی در Flow بماند و چه چیزی Absolute شود؟</caption>
<thead><tr><th scope="col">نوع محتوا</th><th scope="col">انتخاب اولیه</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">Heading / Paragraph / Feature List</th><td>Normal Flow</td><td>متن باید ارتفاع واقعی بسازد و با محتوا رشد کند.</td></tr>
<tr><th scope="row">Copy / Logo Strip</th><td>Normal Flow</td><td>جزء محتوای اصلی است و نباید برای overlap از Flow خارج شود.</td></tr>
<tr><th scope="row">TUYA Visual Stage</th><td>Normal Flow + Relative</td><td>قاب باید در Flow بماند و مرجع Nodeها باشد.</td></tr>
<tr><th scope="row">Core Cloud</th><td>Flow یا controlled absolute، بسته به ساخت Stage</td><td>در این درس هنوز قطعی نیست؛ اول ساده نگه دار.</td></tr>
<tr><th scope="row">Orbit Node</th><td>Absolute داخل Stage</td><td>شناور/Overlay است و باید نسبت به Stage مختصات بگیرد.</td></tr>
<tr><th scope="row">Background Ornament</th><td>Absolute/Background تزئینی داخل Stage</td><td>اگر حذف شود پیام اصلی از بین نمی‌رود.</td></tr>
</tbody>
</table>
</div>

<h3>Relative یعنی الزاماً جابه‌جایی نیست</h3>
<p>در این درس، <code dir="ltr">position: relative</code> را روی Visual Stage می‌گذاری تا Stage مرجع مختصات Nodeها شود. لازم نیست خود Stage را با top/left جابه‌جا کنی.</p>

<h3>Absolute یعنی خروج از Flow</h3>
<p>Absolute دیگر در محاسبهٔ ارتفاع Parent مثل یک Child عادی مشارکت نمی‌کند. بنابراین برای محتوای متغیر مثل متن و لیست، انتخاب اول نیست.</p>

<h3>Containing Block همیشه Body نیست</h3>
<p>Absolute مختصاتش را از Containing Block می‌گیرد. اگر Visual Stage مرجع نشده باشد، Node ممکن است نسبت به ancestor دیگری یا حتی صفحه موقعیت بگیرد و از قاب بیرون برود.</p>

<h3>قاعدهٔ این درس</h3>
<p>Visual Stage را در Flow و Relative نگه دار. فقط Nodeهای محدود و تزئینی/شناور را داخل همان Stage Absolute کن. هنوز Position نهایی همهٔ Nodeها را قطعی نکن.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-12.0.0" id="lesson-12-concept-reference">
<summary>📚 مرجع مفهومی کامل — Position؛ Flow، مرجع مختصات و Overlay</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="12" data-source-version="tuya-revised-12.0.0">

<p class="concept-reference-lead">این مرجع بخش مفهومی Position را حفظ می‌کند و آن را به TUYA Visual Stage وصل می‌کند. هدف، استفادهٔ محدود و قابل Debug از Position است؛ نه تبدیل کل Layout به Offsetهای دستی.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-12-ref-problem">
<h3 id="lesson-12-ref-problem">۱. مسئله‌ای که Position حل می‌کند</h3>
<p>Position برای مواردی مفید است که جای عنصر باید نسبت به یک قاب خاص کنترل شود: Badge روی کارت، Node دور Core، دکمهٔ fixed، یا header sticky. اما اگر Position را برای ساخت layout اصلی استفاده کنی، Flow طبیعی را از بین می‌بری.</p>
<p>در TUYA، Position فعلاً فقط برای Stage و Nodeهای شناور معنی دارد. Copy، Text، Logo و دو ستون اصلی قبلاً با Flow/Flex حل شده‌اند.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-12-sticker">
<h3 id="lesson-12-sticker">۲. تشبیه صف، اتاق و استیکر</h3>
<ul>
<li><code dir="ltr">static</code>: فردی که در صف عادی ایستاده است.</li>
<li><code dir="ltr">relative</code>: فردی که جای خود را در صف نگه می‌دارد و می‌تواند یک قاب مرجع بسازد.</li>
<li><code dir="ltr">absolute</code>: استیکری که از صف خارج شده و به نزدیک‌ترین سطح مرجع می‌چسبد.</li>
<li><code dir="ltr">fixed</code>: برچسب روی شیشهٔ اتوبوس؛ نسبت به viewport ثابت می‌ماند، مگر شرایط خاص ancestor رفتار را عوض کند.</li>
<li><code dir="ltr">sticky</code>: یادداشتی که تا آستانه‌ای scroll می‌کند، بعد در محدودهٔ parent/scroll container می‌چسبد.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-normal-flow">
<h3 id="lesson-12-normal-flow">۳. Normal Flow چیست؟</h3>
<p>Normal Flow روش طبیعی مرورگر برای چیدن Boxهاست. Blockها معمولاً زیر هم، Inlineها داخل متن، و Flex/Grid جریان‌های سازمان‌یافتهٔ داخل Flow هستند.</p>
<p>محتوای اصلی باید تا جای ممکن در Flow بماند، چون:</p>
<ul>
<li>Parent ارتفاع واقعی می‌گیرد؛</li>
<li>متن بلند فضا را گسترش می‌دهد؛</li>
<li>عناصر بعدی به‌درستی هل داده می‌شوند؛</li>
<li>Responsive طبیعی‌تر می‌شود؛</li>
<li>نیاز به offsetهای دستی کمتر می‌شود.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-relative">
<h3 id="lesson-12-relative">۴. position: relative</h3>
<p>Relative دو نقش مهم دارد:</p>
<ol>
<li>Element در Flow باقی می‌ماند و جای اولیه‌اش رزرو می‌شود.</li>
<li>می‌تواند Containing Block برای فرزند Absolute بسازد.</li>
</ol>
<p>اگر فقط برای مرجع‌کردن Parent از Relative استفاده می‌کنی، لازم نیست خود Parent را با <code dir="ltr">top</code> یا <code dir="ltr">left</code> جابه‌جا کنی.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-absolute">
<h3 id="lesson-12-absolute">۵. position: absolute</h3>
<p>Absolute از Normal Flow خارج می‌شود. دیگر به Parent برای محاسبهٔ ارتفاع کمک نمی‌کند. مختصات آن نسبت به Containing Block محاسبه می‌شود.</p>
<blockquote><p>جملهٔ غلط: Absolute همیشه به Body می‌چسبد.</p></blockquote>
<blockquote><p>جملهٔ درست: Absolute مختصاتش را از Containing Block خود می‌گیرد؛ اگر مرجع مورد انتظار ساخته نشده باشد، نتیجه ممکن است از Stage بیرون بزند.</p></blockquote>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-fixed-sticky">
<h3 id="lesson-12-fixed-sticky">۶. Fixed و Sticky در حد آشنایی</h3>
<p>Fixed معمولاً نسبت به Viewport قرار می‌گیرد و برای چیزهایی مثل back-to-top یا floating action مناسب است. Sticky ابتدا در Flow است و بعد از رسیدن به inset تعیین‌شده، در محدودهٔ scroll container می‌چسبد.</p>
<p>در این درس از Fixed و Sticky استفادهٔ عملی نمی‌کنیم؛ فقط تفاوتشان را می‌شناسیم تا با Absolute قاطی نشوند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-tuya-stage">
<h3 id="lesson-12-tuya-stage">۷. معماری Stage در TUYA</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Visual     ← در Flow
└── Visual Stage ← position: relative; aspect-ratio: provisional
    ├── Core Cloud  ← ساده و قابل کنترل
    ├── Orbit Node 1 ← position: absolute
    ├── Orbit Node 2 ← position: absolute
    └── Ornament    ← decorative absolute/background</code></pre>
</figure>
<p>در این معماری، فقط عناصر شناور داخل Stage از Flow خارج می‌شوند. خود Stage هنوز در Flow است و فضای Visual Area را می‌سازد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-inset">
<h3 id="lesson-12-inset">۸. Inset و مختصات</h3>
<p>برای Absolute می‌توان از <code dir="ltr">top/right/bottom/left</code> یا shorthandهایی مثل <code dir="ltr">inset</code> استفاده کرد. در محیط RTL و طراحی منطقی، بهتر است مفهوم inline/block و start/end را هم بشناسی.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Inset controls">
<table class="data-table educational-table edu-table">
<caption>Insetهای فیزیکی و منطقی</caption>
<thead><tr><th scope="col">نوع</th><th scope="col">مثال</th><th scope="col">نکته</th></tr></thead>
<tbody>
<tr><th scope="row">Physical</th><td><code dir="ltr">top: 16px; right: 16px;</code></td><td>چپ/راست فیزیکی؛ در RTL هم همان فیزیکی می‌ماند.</td></tr>
<tr><th scope="row">Logical</th><td><code dir="ltr">inset-block-start</code>، <code dir="ltr">inset-inline-end</code></td><td>با جهت نوشتار سازگارتر است.</td></tr>
<tr><th scope="row">Transform centering</th><td><code dir="ltr">left:50%; transform:translateX(-50%)</code></td><td>برای مرکزکردن دقیق، اما باید با RTL/axis آگاهانه استفاده شود.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-zindex">
<h3 id="lesson-12-zindex">۹. z-index هنوز درس اصلی نیست</h3>
<p>وقتی عناصر Overlay می‌شوند، z-index وسوسه‌انگیز است. اما اگر Containing Block، Position و DOM order درست نباشد، زیادکردن z-index فقط مسئله را پنهان می‌کند. زنجیرهٔ درست:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Flow درست؟
↓
Parent مرجع درست؟
↓
Position درست؟
↓
Inset درست؟
↓
Stacking / z-index در صورت نیاز</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-12-debug">
<h3 id="lesson-12-debug">۱۰. Debug Position</h3>
<p>اگر Node جای عجیبی رفت، این ترتیب را بررسی کن:</p>
<ol>
<li>آیا Node واقعاً داخل Visual Stage است؟</li>
<li>آیا Visual Stage <code dir="ltr">position: relative</code> دارد؟</li>
<li>آیا Stage اندازه و aspect-ratio دارد؟</li>
<li>آیا Node absolute است؟</li>
<li>Insetها نسبت به کدام مرجع محاسبه شده‌اند؟</li>
<li>آیا Transform، overflow یا ancestor دیگری Containing Block ساخته است؟</li>
<li>آیا z-index را قبل از حل مرجع مختصات تغییر داده‌ای؟</li>
</ol>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-12-traps">
<h3 id="lesson-12-traps">۱۱. اشتباهات رایج</h3>
<ul>
<li>Absolute کردن Heading/Paragraph برای رسیدن به یک Screenshot.</li>
<li>Absolute کردن Copy و Logo Strip برای overlap ظاهری.</li>
<li>فراموش‌کردن <code dir="ltr">position: relative</code> روی Stage.</li>
<li>قرار دادن Node بیرون از Stage و انتظار مختصات Stage.</li>
<li>استفاده از top/right ثابت بدون تست Mobile.</li>
<li>حل هر مشکل overlap با z-index.</li>
<li>نداشتن اندازهٔ پایدار برای Stage.</li>
<li>تغییر Position قبل از فهم Flow.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-12-golden">
<h3 id="lesson-12-golden">۱۲. قوانین طلایی</h3>
<ul>
<li><strong>اول بپرس عنصر باید در Flow بماند یا از Flow خارج شود؛ بعد Position را انتخاب کن.</strong></li>
<li><strong>Visual Stage در Flow می‌ماند؛ Nodeها می‌توانند داخل آن Absolute شوند.</strong></li>
<li><strong>Relative روی Parent الزاماً به معنی جابه‌جایی Parent نیست.</strong></li>
<li><strong>Absolute بدون Containing Block درست، مختصات قابل پیش‌بینی ندارد.</strong></li>
<li><strong>Copy، Heading، Paragraph و Logo Strip را برای حل overlap از Flow خارج نکن.</strong></li>
<li><strong>z-index ابزار آخر است، نه اولین واکنش.</strong></li>
<li><strong>Offsetها تا قبل از تست Desktop/Tablet/Mobile provisional هستند.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>رفتار Position، Containing Block، Flow، inset و sticky/fixed بر پایهٔ CSS Positioned Layout و رفتار مرورگر نوشته شده است. تصمیم‌های عددی TUYA تا پیش از مشاهدهٔ Stage واقعی و Breakpoint Validation قطعی نیستند.</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position" rel="noopener noreferrer" target="_blank">MDN — position</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block" rel="noopener noreferrer" target="_blank">MDN — Containing block</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://elementor.com/help/responsive-editing/" rel="noopener noreferrer" target="_blank">Elementor — Responsive editing</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-12-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-12-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Position، Inset، Transform و Stage</span>
</summary>
<section aria-labelledby="lesson-12-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Positionها keyword هستند؛ offsetها واحد طول یا درصد دارند؛ درصدهای inset نسبت به Containing Block معنی می‌گیرند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۲" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Position</th><td>keyword</td><td>Element و flow context</td><td>Absolute برای محتوای اصلی استفاده شود.</td></tr>
<tr><th scope="row">Top/Right/Bottom/Left</th><td>px, rem, %, auto</td><td>Containing Block</td><td>مرجع مختصات اشتباه باشد.</td></tr>
<tr><th scope="row">Logical Inset</th><td>px, rem, %, auto</td><td>Block/Inline axis</td><td>با left/right فیزیکی قاطی شود.</td></tr>
<tr><th scope="row">Transform</th><td>function</td><td>خود Element و transform box</td><td>Containing Block یا stacking رفتار را پیچیده کند.</td></tr>
<tr><th scope="row">z-index</th><td>number / auto</td><td>stacking context</td><td>قبل از حل Position استفاده شود.</td></tr>
<tr><th scope="row">Stage Size</th><td>width / max / aspect-ratio</td><td>Visual Area</td><td>Stage اندازهٔ پایدار نداشته باشد.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Stage عرض 400px دارد و Node با <code dir="ltr">left:50%</code> قرار می‌گیرد، نقطهٔ left آن در 200px Stage است؛ اما خود Node هنوز از همان نقطه شروع می‌شود مگر با Transform اصلاح شود.</p></section>
<section><h3>📱 در Responsive</h3><p>Offset ثابت Desktop را بدون بازبینی به Mobile منتقل نکن. نسبت Stage، اندازهٔ Node و فضای Visual در Mobile ممکن است تغییر کند.</p></section>
<section><h3>🔬 در DevTools</h3><p>offsetParent، bounding box، position، inset values، transform و containing block chain را بررسی کن.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-12-position-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Relative Parent و Absolute Child</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر حالت را پیش‌بینی کن، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Step Through Position">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ حالت‌های Position</caption>
<thead><tr><th scope="col">حالت</th><th scope="col">وضعیت</th><th scope="col">چه چیزی یاد می‌گیری؟</th><th scope="col">قانون طلایی</th></tr></thead>
<tbody>
<tr><th scope="row">۱</th><td>Stage در Flow و static</td><td>Node absolute ممکن است مرجع مورد انتظار نگیرد.</td><td>Parent مرجع بساز.</td></tr>
<tr><th scope="row">۲</th><td>Stage relative، Node absolute</td><td>Node نسبت به Stage کنترل می‌شود.</td><td>Overlay را داخل قاب محدود کن.</td></tr>
<tr><th scope="row">۳</th><td>حذف Relative از Stage</td><td>Node به ancestor دیگری می‌چسبد.</td><td>Containing Block را حدس نزن.</td></tr>
<tr><th scope="row">۴</th><td>Copy absolute</td><td>متن از Flow خارج و Parent height خراب می‌شود.</td><td>محتوای اصلی را absolute نکن.</td></tr>
<tr><th scope="row">۵</th><td>Mobile با offset ثابت</td><td>جای Node ممکن است خراب شود.</td><td>Offsetها provisional و breakpoint-aware هستند.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-12-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-12-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Visual Stage در Flow، Nodeها داخل Stage</h3>
<p>در این تمرین، فقط Containing Block و یک یا دو Node پایه را تست می‌کنی. هنوز همهٔ Orbit Nodeها، Position نهایی، z-index نهایی، Animation یا Shadow/Glow نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 12">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Position</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy، Text و Logo Strip باید در Flow بمانند.</td><td>آن‌ها را Absolute نکن.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Nodeهای شناور باید داخل Visual Stage کنترل شوند.</td><td>Stage را Relative کن.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Aspect Ratio Stage، اندازهٔ Node و offsetها.</td><td>فقط مقدار شروع تست هستند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Position نهایی همهٔ Orbit Nodeها، z-index نهایی، اندازهٔ واقعی SVGها.</td><td>در این درس قطعی نمی‌شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Stage را مرجع کن</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس دوازده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ساخت Containing Block کنترل‌شده برای Nodeها.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → <code dir="ltr">TUYA Visual</code> → انتخاب <code dir="ltr">Visual Stage</code> → Layout/Position.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">Visual Stage</code> و یک یا دو <code dir="ltr">Orbit Node</code> تستی.</p>
<p><strong>Class فعال:</strong> Class محلی Stage و Node؛ Global جدید نساز مگر reuse واقعی ثابت شود.</p>
<p><strong>Property:</strong> Stage: Relative / aspect ratio. Node: Absolute / inset تستی.</p>
<p><strong>نباید تغییر کند:</strong> Copy، Heading، Paragraph، Logo Strip، Shell Flex، Typography، Background نهایی، Shadow/Glow.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Stage در Flow و Relative است؛ Node تستی داخل Stage Absolute شده و متن/لوگو از Flow خارج نشده‌اند.»</p>
</aside>

<h3>مرحلهٔ ۲ — ساختار Stage را بررسی کن</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Visual
└── Visual Stage  ← position: relative; aspect-ratio: provisional
    ├── Core Cloud
    ├── Orbit Node Test A ← position: absolute
    └── Orbit Node Test B ← position: absolute</code></pre>
</figure>

<h3>مرحلهٔ ۳ — مقدارهای شروع را فقط برای تست وارد کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional position values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع Position</caption>
<thead><tr><th scope="col">Element</th><th scope="col">تنظیم</th><th scope="col">مقدار شروع</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Visual Stage</th><td>Position</td><td><code dir="ltr">Relative</code></td><td><code dir="ltr">confirmed_method</code></td></tr>
<tr><th scope="row">Visual Stage</th><td>Aspect Ratio</td><td><code dir="ltr">1 / 1</code> شروع تست</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Node Test A</th><td>Position</td><td><code dir="ltr">Absolute</code></td><td><code dir="ltr">confirmed_for_overlay_test</code></td></tr>
<tr><th scope="row">Node Test A</th><td>Inset</td><td><code dir="ltr">top: 10%; right: 10%</code> یا logical equivalent</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Node Test B</th><td>Inset</td><td><code dir="ltr">bottom: 12%; left: 12%</code> یا logical equivalent</td><td><code dir="ltr">provisional</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۴ — خرابی عمدی</h3>
<ol>
<li>قبل از حذف Relative از Stage، پیش‌بینی کن Node نسبت به کجا موقعیت می‌گیرد.</li>
<li>Relative را موقتاً حذف کن.</li>
<li>جای Node را ببین.</li>
<li>Relative را برگردان.</li>
<li>نتیجه را در یک جمله بنویس.</li>
</ol>

<h3>مرحلهٔ ۵ — سؤال توقف</h3>
<p>اگر Orbit Node باید فقط داخل Visual Stage کنترل شود، Position را روی چه عناصری می‌گذاری؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-12">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-12-a" name="stop-question-12" type="radio" value="A"/><span>A) Stage: Relative، Node: Absolute</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-12-b" name="stop-question-12" type="radio" value="B"/><span>B) Copy: Absolute، Logo Strip: Absolute</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-12-c" name="stop-question-12" type="radio" value="C"/><span>C) همهٔ سکشن: Fixed</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>A درست است.</strong> Stage مرجع مختصات می‌شود و Nodeها داخل آن از Flow خارج می‌شوند. محتوای اصلی مثل Copy و Logo Strip باید در Flow باقی بماند.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> برای رسیدن به یک ظاهر Screenshot، Copy یا Heading را Absolute کنی.</p>
<p><strong>نشانه:</strong> متن بلند overlap می‌کند، Parent height صفر یا کم می‌شود، و Mobile با offsetهای دستی تعمیر می‌شود.</p>
<p><strong>قاعده:</strong> محتوا در Flow؛ تزئین شناور داخل Stage.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>این ساختار خراب را تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Layout خراب با Absolute کردن محتوا</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Section
├── Copy position:absolute
├── Visual position:absolute
└── Logo Strip position:absolute

نتیجه:
- Section ارتفاع واقعی ندارد
- متن بلند روی Visual می‌افتد
- Responsive با offsetهای دستی شکننده می‌شود</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-67">
<fieldset>
<legend>Checkpoint درس ۱۲</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-67-1" name="chk-67-1" type="checkbox"/><span>Visual Stage در Flow مانده و Relative شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-67-2" name="chk-67-2" type="checkbox"/><span>فقط Node تستی داخل Stage Absolute شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-67-3" name="chk-67-3" type="checkbox"/><span>Copy، Heading، Paragraph و Logo Strip Absolute نشده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-67-4" name="chk-67-4" type="checkbox"/><span>حذف Relative از Stage را تست کرده‌ام و اثرش را فهمیده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-67-5" name="chk-67-5" type="checkbox"/><span>Offsetهای Node هنوز provisional هستند.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Relative Parent و Absolute Child را با مثال Stage و Node توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> برای Badge روی کارت محصول، چه چیزی Relative می‌شود و چه چیزی Absolute؟ چرا؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید کارت یا image-stage مرجع Relative می‌شود، Badge Absolute می‌شود، و محتوای اصلی کارت در Flow باقی می‌ماند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-12-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Absolute فقط داخل Visual Stage</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">verified_and_scoped</code></p>
<p>در Mobile، Nodeها پیرامون Core هم‌پوشانی دارند. راه پایدار این است که Visual Stage در Flow بماند و فقط Nodeهای شناور نسبت به Stage موقعیت‌دهی شوند.</p>
<ul>
<li>Copy و Logo Strip را Absolute نکن.</li>
<li>Stage را در Desktop، Tablet، Mobile و یک عرض بین breakpointها تست کن.</li>
<li>Offsetهای درصدی را با نسبت Stage و اندازهٔ Node بازبینی کن.</li>
<li>اگر Node بیرون زد، اول Stage size و containing block را بررسی کن، نه z-index را.</li>
</ul>
</section>
</details>

<details class="lesson-disclosure responsive-build-test" id="lesson-12-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Visual Stage و Containing Block در Mobile</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_runtime_validation</code></p>
<p class="exercise-goal"><strong>هدف:</strong> Absolute را فقط در ناحیهٔ تصویری کنترل‌شده به کار ببر.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>Visual Stage را در Flow و روی Position: Relative نگه دار.</li><li>دو Node را داخل آن Absolute کن و موقعیت را در Desktop و Mobile بازبینی کن.</li><li>Copy و Logo Strip را در Normal Flow نگه دار.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>قبل از حذف Relative بگو Nodeها نسبت به کدام ancestor موقعیت می‌گیرند.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>Position: Relative را از Stage حذف کن یا Node را بیرون Stage منتقل کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>offset parent، bounding box، top/right/bottom/left، inset و ancestor chain را بررسی کن.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> Nodeها داخل Stage کنترل می‌شوند و متن/لوگو برای overlap از Flow خارج نشده‌اند.</p>
</section>
</details>

<details aria-labelledby="lesson-12-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-12-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Node از Stage فرار می‌کند</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: Node را داخل Visual گذاشته‌ای، اما در خروجی جایی دور از Core دیده می‌شود.</p>
<p>قبل از تغییر offset جدید، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>Node واقعاً داخل Visual Stage است یا sibling آن؟</li>
<li>Visual Stage واقعاً <code dir="ltr">position: relative</code> دارد؟</li>
<li>Stage اندازهٔ واقعی و aspect-ratio دارد؟</li>
<li>Computed position Node چیست؟</li>
<li>offsetParent یا Containing Block چیست؟</li>
<li>آیا transform یا overflow ancestor دیگری رفتار را تغییر داده است؟</li>
<li>آیا فقط با z-index مشکل را پنهان کرده‌ای؟</li>
</ul>
</section>
<p>نتیجهٔ درست: مرجع مختصات را پیدا کن، بعد offset را تنظیم کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، bounding box Stage و Node را ببین. اگر Node نسبت به Box اشتباهی محاسبه می‌شود، مسئله با تغییر top/right تصادفی حل نمی‌شود؛ باید Containing Block درست شود.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-12-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-12-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-70">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-70-1" name="chk-70-1" type="checkbox"/><span>می‌توانم توضیح بدهم Absolute از Flow خارج می‌شود.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-70-2" name="chk-70-2" type="checkbox"/><span>می‌دانم Relative Parent می‌تواند مرجع مختصات Child Absolute شود.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-70-3" name="chk-70-3" type="checkbox"/><span>می‌توانم Containing Block را از Body جدا کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-71">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-71-1" name="chk-71-1" type="checkbox"/><span>Visual Stage را Relative می‌کنم و Node تستی را داخل آن Absolute می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-71-2" name="chk-71-2" type="checkbox"/><span>Copy، Heading، Paragraph و Logo Strip را در Flow نگه می‌دارم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-71-3" name="chk-71-3" type="checkbox"/><span>قبل از تغییر z-index، Containing Block و inset را بررسی می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-72">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-72-1" name="chk-72-1" type="checkbox"/><span>برای Badge روی کارت محصول می‌توانم Stage/Card مرجع و Badge Absolute را توضیح بدهم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-12-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Position offsets</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>این offset باید direct literal بماند یا Variable شود؟</li>
<li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li>
<li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li>
<li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — فعلاً offsetها provisional هستند. تا وقتی Node pattern و Stage واقعی قطعی نشده‌اند، Variable/Global نهایی نساز.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-12-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-12-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا فقط Containing Block و چند Node تستی ساخته شده‌اند؛ Position نهایی Orbit و z-index نهایی هنوز قطعی نشده است.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 12</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-12-completion">
<fieldset>
<legend>ثبت پایان درس 12</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-12-complete" name="lesson-12-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
