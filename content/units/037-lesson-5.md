<article class="lesson card-surface" data-lesson="5" id="lesson-5">

<h2 class="lesson-title former-h1">درس 5 — Flexbox و ساخت دو ستون اصلی</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-5-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-5-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> Shell ساخته‌شده در درس قبل را به یک Parent Flex تبدیل کنی تا دو Child مستقیم، یعنی Copy و Visual، در Desktop کنار هم قرار بگیرند و در Mobile بتوانند به Column تبدیل شوند.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Grow و Shrink عمیق، Grid، Position نهایی Nodeها، Visual Stage کامل، Shadow/Glow یا Style نهایی.</p>
<p><strong>در پایان باید بتوانی:</strong> دو ناحیهٔ Copy و Visual را در Normal Flow کنار هم بچینی، بدون Absolute و بدون ساخت نسخهٔ جداگانه برای Mobile.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-5-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-5-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + 📱 Responsive-aware</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰–۲۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۳۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این اولین Layout واقعی پروژه است. تمرکز باید روی انتخاب Parent درست، Child مستقیم، Direction و Gap باشد؛ نه روی زیبا کردن نهایی یا Position کردن Nodeها.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_flex_two_column_flow</code></p>
</section>
</details>

<section aria-labelledby="lesson-5-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-5-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس ۱ Context را شناختی. در درس ۲ Tree ساختی. در درس ۳ Class Scope را کنترل کردی. در درس ۴ Shell را از نظر Box Model آماده کردی. حالا درس ۵ به Shell یک موتور چیدمان می‌دهد: <strong>Flexbox</strong>.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Context
↓
Structure / Element Tree
↓
Class Scope
↓
Box Model / Shell Sizing
↓
Flexbox / Two-column Flow</code></pre>
</figure>

<h3>مسئله</h3>
<p>Copy و Visual در Tree موجودند، اما اگر Shell فقط یک ظرف خام باشد، ممکن است زیر هم بمانند یا با روش‌های اشتباه مثل Absolute کنار هم نشان داده شوند. در Desktop لازم است این دو Child مستقیم در یک ردیف کنار هم قرار بگیرند، اما همچنان در Flow باقی بمانند.</p>

<h3>تعریف کوتاه</h3>
<p>Flexbox یک مدل Layout یک‌بعدی است. یک‌بعدی یعنی تصمیم اصلی حول یک محور انجام می‌شود: Row یا Column. Flex برای زمانی مناسب است که چند Child مستقیم باید روی یک محور کنار هم یا زیر هم چیده شوند.</p>

<h3>Display با Flow یکی نیست</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<p><code dir="ltr">display: flex</code> یعنی Parent برای Childهای مستقیم خود یک محیط Flex می‌سازد. اما خود Parent الزاماً از Flow صفحه خارج نمی‌شود.</p>
<ul>
<li><strong>Normal Flow:</strong> بستر طبیعی چیدمان؛ Elementها جای خود را اشغال می‌کنند و Parent قد محتوا را می‌فهمد.</li>
<li><strong>Display:</strong> Propertyی که رفتار Element یا رفتار Childهای مستقیم آن را تعیین می‌کند.</li>
<li><strong>Absolute:</strong> Positioningی که Element را از Flow خارج می‌کند.</li>
</ul>
<p>پس در این درس، Shell با <code dir="ltr">display:flex</code> Childهای Copy و Visual را کنار هم می‌چیند، ولی خود Shell همچنان در Flow صفحه باقی می‌ماند.</p>
</section>

<h3>چرا برای دو ستون اصلی نه Absolute؟</h3>
<p>Copy و Visual محتوای واقعی هستند. باید Height والد را بسازند، با متن رشد کنند، و در Mobile به‌سادگی تغییر جهت دهند. اگر آن‌ها را Absolute کنی، Parent ممکن است قد واقعی محتوا را نفهمد و Mobile با Offsetهای شکننده تعمیر شود.</p>

<h3>واژه‌های اصلی Flex</h3>
<dl class="term-grid">
<dt>Flex Container</dt><dd>Parentی که Display آن Flex است.</dd>
<dt>Flex Item</dt><dd>Child مستقیم Flex Container.</dd>
<dt>Main Axis</dt><dd>محور اصلی چیدمان؛ در Row افقی و در Column عمودی است.</dd>
<dt>Cross Axis</dt><dd>محور مقابل Main Axis.</dd>
<dt>Direction</dt><dd>تعیین می‌کند Childها در Row یا Column قرار بگیرند.</dd>
<dt>Gap</dt><dd>فاصلهٔ منظم بین Childهای مستقیم؛ بهتر از Marginهای پراکنده برای فاصلهٔ بین ستون‌ها.</dd>
<dt>Justify Content</dt><dd>توزیع فضا روی Main Axis.</dd>
<dt>Align Items</dt><dd>تراز Childها روی Cross Axis.</dd>
</dl>

<h3>Parent چه چیزی را کنترل می‌کند؟ Item چه چیزی را؟</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Parent vs Item flex controls">
<table class="data-table educational-table edu-table">
<caption>تقسیم مسئولیت در Flexbox</caption>
<thead><tr><th scope="col">محل تنظیم</th><th scope="col">مسئولیت</th><th scope="col">نمونه</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Parent / Container</th><td>قانون چیدمان Childهای مستقیم</td><td>Direction، Gap، Justify، Align، Wrap</td><td>Parent اشتباه را Flex کنی و انتظار داشته باشی نوه‌ها جابه‌جا شوند.</td></tr>
<tr><th scope="row">Item / Child مستقیم</th><td>رفتار خود Child در Flex</td><td>Basis، Grow، Shrink، Order، Align Self، Min/Max</td><td>با Justify می‌خواهی مشکل اندازهٔ Item را حل کنی.</td></tr>
</tbody>
</table>
</div>

<h3>Child مستقیم مهم است</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Shell  ← display:flex
├── TUYA Copy    ← Flex Item مستقیم
└── TUYA Visual  ← Flex Item مستقیم
    └── Visual Stage  ← Flex Item مستقیم Shell نیست</code></pre>
</figure>
<p>اگر Visual Stage داخل TUYA Visual است، Shell مستقیماً Visual Stage را نمی‌چیند. Shell فقط Copy و Visual را کنار هم می‌چیند.</p>

<h3>قاعدهٔ این درس</h3>
<p>برای Desktop، Shell را Flex Row کن. برای Mobile، همان Shell را Flex Column کن. ساخت نسخهٔ دوم سکشن و مخفی‌کردن یکی از نسخه‌ها فعلاً ممنوع است، مگر بعداً با دلیل قوی ثابت شود.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-5.0.0" id="lesson-5-concept-reference">
<summary>📚 مرجع مفهومی کامل — Flexbox؛ چیدمان یک‌بعدی و دو ستون اصلی TUYA</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="5" data-source-version="tuya-revised-5.0.0">

<p class="concept-reference-lead">این مرجع بخش مفهومی Flexbox را حفظ می‌کند و آن را به پروژهٔ TUYA وصل می‌کند. هدف ساختن Layout اصلی است، نه ورود زودهنگام به Position یا تزئینات.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-5-ref-problem">
<h3 id="lesson-5-ref-problem">۱. مسئله‌ای که Flexbox حل می‌کند</h3>
<p>Flexbox برای چیدن چند Item روی یک محور طراحی شده است؛ یعنی وقتی می‌خواهی چند Child مستقیم کنار هم یا زیر هم باشند و فاصله و تراز آن‌ها قابل کنترل باشد.</p>
<p>در TUYA، سؤال اصلی این است:</p>
<blockquote><p>چگونه Copy Area و Visual Area را در Desktop کنار هم بگذاریم، اما همچنان به محتوا و Mobile اجازهٔ رشد و تغییر جهت بدهیم؟</p></blockquote>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-5-train-analogy">
<h3 id="lesson-5-train-analogy">۲. تشبیه واگن و چمدان‌ها</h3>
<ul>
<li><strong>Flex Container:</strong> واگن.</li>
<li><strong>Flex Item:</strong> چمدان مستقیم داخل واگن.</li>
<li><strong>Main Axis:</strong> مسیر طولی واگن.</li>
<li><strong>Gap:</strong> فاصلهٔ منظم بین چمدان‌ها.</li>
<li><strong>Basis:</strong> اندازهٔ اولیهٔ هر چمدان.</li>
<li><strong>Grow/Shrink:</strong> مذاکرهٔ چمدان‌ها با فضای اضافه یا کمبود.</li>
</ul>
<p>چیزی که داخل یکی از چمدان‌هاست، مستقیماً با قانون واگن چیده نمی‌شود. این همان تفاوت Child مستقیم با Descendant است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-5-flow-display">
<h3 id="lesson-5-flow-display">۳. Display، Normal Flow و Absolute را قاطی نکن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Flow Display Absolute">
<table class="data-table educational-table edu-table">
<caption>تفاوت Flow، Display و Absolute</caption>
<thead><tr><th scope="col">مفهوم</th><th scope="col">جنس</th><th scope="col">اثر</th><th scope="col">در TUYA</th></tr></thead>
<tbody>
<tr><th scope="row">Normal Flow</th><td>بستر چیدمان</td><td>Content جای خود را اشغال می‌کند و Parent قد آن را می‌فهمد.</td><td>Copy و Visual باید در Flow بمانند.</td></tr>
<tr><th scope="row">Display</th><td>Property</td><td>رفتار Element و/یا Childهای مستقیم را تعیین می‌کند.</td><td>Shell با Display Flex، Copy و Visual را می‌چیند.</td></tr>
<tr><th scope="row">Absolute</th><td>Positioning</td><td>Element را از Flow خارج می‌کند.</td><td>برای ستون‌های اصلی ممنوع؛ بعداً فقط برای Node داخل Stage بررسی می‌شود.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-5-parent-item">
<h3 id="lesson-5-parent-item">۴. ترتیب صحیح تنظیم Flex</h3>
<ol>
<li>Parent درست را انتخاب کن: در TUYA، Shell.</li>
<li>فقط Childهای مستقیم را بشمار: Copy و Visual.</li>
<li>Direction را تعیین کن: Desktop Row.</li>
<li>Gap را برای فاصلهٔ بین ستون‌ها بده.</li>
<li>Basis/Width اولیهٔ Itemها را فقط به‌عنوان provisional تعیین کن.</li>
<li>Alignment را بعد از روشن‌شدن اندازه و فضا تنظیم کن.</li>
<li>در Mobile، Direction را به Column تغییر بده.</li>
<li>بعد از تست واقعی، Grow/Shrink را بررسی کن.</li>
</ol>
<p>اگر از Justify/Align شروع کنی، ممکن است فکر کنی Flex کار نمی‌کند، در حالی که مسئله، Parent اشتباه یا اندازهٔ Itemهاست.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-5-tuya-layout">
<h3 id="lesson-5-tuya-layout">۵. Layout ذهنی TUYA در این درس</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop:
TUYA Shell — Flex Row
├── TUYA Copy    ← basis حدود 52% تا 55%، provisional
└── TUYA Visual  ← basis حدود 45% تا 48%، provisional

Mobile:
TUYA Shell — Flex Column
├── TUYA Copy
└── TUYA Visual</code></pre>
</figure>
<p>اعداد basis هنوز قطعی نیستند. باید با محتوای واقعی، عرض Parent، Gap و Breakpointها تست شوند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-5-gap-margin">
<h3 id="lesson-5-gap-margin">۶. Gap برای فاصلهٔ بین ستون‌ها بهتر از Margin پراکنده است</h3>
<p>وقتی فاصلهٔ بین دو Child مستقیم یک Flex Container را می‌خواهی، Gap معمولاً تمیزتر از Marginهای جداگانه است. Gap به Parent تعلق دارد و فاصلهٔ بین Items را یک‌دست نگه می‌دارد.</p>
<p>Margin هنوز کاربرد دارد، اما برای فاصلهٔ بین ستون‌های یک Layout اصلی، ابتدا Gap را بررسی کن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-5-responsive">
<h3 id="lesson-5-responsive">۷. Responsive Contract این درس</h3>
<p>قرارداد Responsive فعلی:</p>
<ul>
<li>Desktop: Shell در Row، Copy و Visual کنار هم.</li>
<li>Tablet: ممکن است Row فشرده یا Column شود؛ هنوز قطعی نیست.</li>
<li>Mobile: Shell به Column تبدیل شود.</li>
<li>نسخهٔ دوم سکشن ساخته نشود.</li>
<li>Order معنایی محتوا بدون دلیل عوض نشود.</li>
</ul>
<p>اگر در Mobile Visual قبل از Copy می‌آید، باید دلیل UX و محتوا داشته باشد. Order ابزار است، نه راه فرار از Tree اشتباه.</p>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-5-golden">
<h3 id="lesson-5-golden">۸. قوانین طلایی</h3>
<ul>
<li><strong>Flex روی Parent اعمال می‌شود، نه روی رابطهٔ ذهنی تو.</strong></li>
<li><strong>فقط Childهای مستقیم Flex Item می‌شوند.</strong></li>
<li><strong>دو ستون اصلی Content هستند؛ Absolute نیستند.</strong></li>
<li><strong>Gap برای فاصلهٔ بین Itemهای Flex از Margin پراکنده تمیزتر است.</strong></li>
<li><strong>Direction در Responsive تغییر می‌کند؛ Tree لازم نیست دوباره ساخته شود.</strong></li>
<li><strong>Justify مشکل Width اشتباه را حل نمی‌کند.</strong></li>
<li><strong>Basisهای پیشنهادی تا قبل از تست واقعی provisional هستند.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفهوم Flexbox، Parent/Item، Main Axis، Cross Axis، Gap و Responsive Direction بر پایهٔ رفتار CSS و مستندات Elementor دربارهٔ چیدمان Flexbox نوشته شده است. تصمیم‌های عددی مربوط به TUYA تا پیش از تست در UI واقعی قطعی نیستند.</p>
<ul>
<li><a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout" rel="noopener noreferrer" target="_blank">MDN — CSS Flexible Box Layout</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-5-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-5-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Direction، Gap، Basis و اندازهٔ Itemها</span>
</summary>
<section aria-labelledby="lesson-5-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در Flex، بعضی تنظیمات keyword هستند، بعضی اندازه می‌گیرند و بعضی نسبت به Parent یا فضای آزاد محاسبه می‌شوند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۵" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">محل</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Display</th><td>Parent</td><td>keyword</td><td>رفتار Layout</td><td>آن را با خروج از Flow اشتباه نگیر.</td></tr>
<tr><th scope="row">Direction</th><td>Parent</td><td>Row / Column</td><td>Main Axis</td><td>در Mobile فراموش شود.</td></tr>
<tr><th scope="row">Gap</th><td>Parent</td><td>px, rem, %, clamp</td><td>فاصله بین Itemها</td><td>با Padding داخلی یا Margin بیرونی قاطی شود.</td></tr>
<tr><th scope="row">Basis / Width</th><td>Item</td><td>%, px, auto</td><td>فضای Parent و محتوای Item</td><td>عدد را از Screenshot قطعی فرض کنی.</td></tr>
<tr><th scope="row">Grow / Shrink</th><td>Item</td><td>عدد بدون واحد</td><td>فضای اضافه/کمبود Parent</td><td>قبل از فهم Basis و Min Width واردش شوی.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>دو Item با basisهای 55% و 45% اگر Gap هم داشته باشند، ممکن است بیش از 100% شوند. بنابراین basisها باید همراه Gap و Parent واقعی بررسی شوند.</p></section>
<section><h3>📱 در Responsive</h3><p>در Mobile، Direction معمولاً Column می‌شود. در این حالت basisهای درصدی Desktop ممکن است بی‌معنی یا مزاحم شوند و باید بازبینی شوند.</p></section>
<section><h3>🔬 در DevTools</h3><p>در Computed می‌توانی display، gap، flex-basis، used width و min-width را ببینی. اگر Item فشرده نمی‌شود، min-width و محتوای داخلی را بررسی کن.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-5-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-5-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — دو ستون اصلی در Flow</h3>
<p>در این تمرین، فقط Layout اصلی Copy و Visual را می‌سازی. هنوز Visual Stage، Core/Node positioning، Shadow/Glow و Style نهایی را انجام نمی‌دهی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate درس ۵">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Flex کردن Shell</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy و Visual Child مستقیم Shell هستند.</td><td>Shell می‌تواند Flex Container باشد.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy و Visual محتوای اصلی‌اند.</td><td>نباید Absolute شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Basis حدودی Copy/Visual و Gap.</td><td>فقط مقدار شروع تست است.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Breakpoint دقیق تغییر Row به Column، محتوای نهایی و عرض واقعی Parent.</td><td>در این درس قطعی اعلام نمی‌شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — Parent درست را انتخاب کن</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس پنج">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> تبدیل Shell به Parent Flex برای دو Child مستقیم.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → انتخاب <code dir="ltr">TUYA Shell</code> → Style/Layout → Display/Flexbox.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">TUYA Shell</code>.</p>
<p><strong>Class فعال:</strong> Class محلی Shell یا Candidate همان Shell؛ Global جدید نساز.</p>
<p><strong>Property:</strong> Display / Direction / Gap.</p>
<p><strong>نباید تغییر کند:</strong> Position، Nodeها، Shadow، Glow، Background نهایی، Typography، Button Style، Visual Stage positioning.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Shell به Flex تبدیل شد و فقط Copy و Visual در Desktop کنار هم قرار گرفتند.»</p>
</aside>

<h3>مرحلهٔ ۲ — مقدارهای شروع را وارد کن</h3>
<p>مقدارها provisional هستند:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional flex values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع Flex برای دو ستون</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">مقدار شروع</th><th scope="col">وضعیت</th><th scope="col">یادداشت</th></tr></thead>
<tbody>
<tr><th scope="row">Display</th><td><code dir="ltr">Flex</code></td><td><code dir="ltr">confirmed_for_this_layout</code></td><td>برای دو Child مستقیم روی یک محور.</td></tr>
<tr><th scope="row">Direction Desktop</th><td><code dir="ltr">Row</code></td><td><code dir="ltr">confirmed_for_desktop_goal</code></td><td>Copy و Visual کنار هم.</td></tr>
<tr><th scope="row">Gap</th><td><code dir="ltr">24px</code> تا <code dir="ltr">40px</code> شروع تست</td><td><code dir="ltr">provisional</code></td><td>بسته به Width واقعی و محتوا.</td></tr>
<tr><th scope="row">Copy Basis</th><td><code dir="ltr">52%</code> تا <code dir="ltr">55%</code> شروع تست</td><td><code dir="ltr">provisional</code></td><td>همراه Gap و Parent بررسی شود.</td></tr>
<tr><th scope="row">Visual Basis</th><td><code dir="ltr">45%</code> تا <code dir="ltr">48%</code> شروع تست</td><td><code dir="ltr">provisional</code></td><td>همراه Gap و Parent بررسی شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — Mobile Contract را ثبت کن، ولی عمیق نشو</h3>
<p>برای Mobile فعلاً فقط قرارداد را ثبت کن:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop: TUYA Shell = Row
Mobile:  TUYA Shell = Column</code></pre>
</figure>
<p>مقدارهای دقیق Mobile، ترتیب نهایی Copy/Visual و اندازهٔ Visual در درس‌های بعدی با Screenshot واقعی بررسی می‌شوند.</p>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر Copy و Visual زیر Shell هستند و باید در Desktop کنار هم باشند، Display را روی کدام Element می‌گذاری؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-5">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-5-a" name="stop-question-5" type="radio" value="A"/><span>A) روی TUYA Copy</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-5-b" name="stop-question-5" type="radio" value="B"/><span>B) روی TUYA Shell</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-5-c" name="stop-question-5" type="radio" value="C"/><span>C) روی Nodeها</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Shell Parent مستقیم Copy و Visual است. Flex روی Parent اعمال می‌شود تا Childهای مستقیم را بچیند.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> Copy و Visual را با Position Absolute کنار هم بگذاری.</p>
<p><strong>نشانه:</strong> Parent قد واقعی را نمی‌فهمد، متن بلند باعث برخورد می‌شود، و Mobile با Offsetهای زیاد تعمیر می‌شود.</p>
<p><strong>قاعده:</strong> ستون‌های اصلی Content هستند؛ در Flow می‌مانند. Absolute بعداً فقط برای بخش‌های شناور داخل Stage بررسی می‌شود.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>تصور کن Copy و Visual هر دو Absolute هستند:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Layout خراب‌شده با Absolute</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Shell
├── Copy   position:absolute
└── Visual position:absolute

نتیجه:
- Shell قد واقعی ندارد
- متن بلند با Visual برخورد می‌کند
- Mobile با top/rightهای جدید تعمیر می‌شود</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-25">
<fieldset>
<legend>Checkpoint درس ۵</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-25-1" name="chk-25-1" type="checkbox"/><span>Flex روی TUYA Shell اعمال شده، نه روی Child اشتباه.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-25-2" name="chk-25-2" type="checkbox"/><span>Copy و Visual Child مستقیم Shell هستند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-25-3" name="chk-25-3" type="checkbox"/><span>دو ستون اصلی هنوز در Flow هستند و Absolute نشده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-25-4" name="chk-25-4" type="checkbox"/><span>Basis و Gap را provisional ثبت کرده‌ام، نه قطعی.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Flex Container و Flex Item را در Tree TUYA توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر سه کارت Feature باید کنار هم باشند، Flex را روی کارت‌ها می‌گذاری یا Parent آن‌ها؟ چرا؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Flex روی Parent کارت‌ها اعمال می‌شود، چون کارت‌ها Child مستقیم آن Parent هستند. اگر Parent اشتباه باشد، Flex روی عناصر هدف اثر نمی‌گذارد.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-5-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Row به Column بدون ساخت نسخهٔ دوم</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">verified_method_provisional_values</code></p>
<p>برای Mobile، فعلاً قرارداد این است که همان Shell به Column تبدیل شود. نسخهٔ دوم Section نساز و یکی را مخفی نکن؛ این کار نگهداری، دسترسی‌پذیری و هماهنگی محتوا را سخت‌تر می‌کند.</p>
<ul>
<li>در Desktop، Shell = Row.</li>
<li>در Mobile، Shell = Column.</li>
<li>ترتیب Copy و Visual فقط با دلیل UX تغییر کند.</li>
<li>Basisهای Desktop در Mobile بازبینی شوند.</li>
<li>متن بلند باید Shell را رشد بدهد، نه اینکه روی Visual بیفتد.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-5-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-5-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Flex کار نمی‌کند</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: Shell را Flex کرده‌ای، اما Copy و Visual کنار هم قرار نمی‌گیرند.</p>
<p>قبل از تغییر عدد جدید، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا Shell واقعاً Parent مستقیم Copy و Visual است؟</li>
<li>آیا Display روی Shell اعمال شده یا روی Child اشتباه؟</li>
<li>آیا Direction روی Row است؟</li>
<li>آیا Copy و Visual عرض یا basisهایی دارند که همراه Gap بیشتر از 100% می‌شود؟</li>
<li>آیا یکی از Childها min-width یا محتوای بلند دارد که اجازهٔ فشرده‌شدن نمی‌دهد؟</li>
<li>آیا breakpoint فعلی Mobile است و Direction به Column تغییر کرده؟</li>
</ul>
</section>
<p>نتیجهٔ درست: اول Parent و Child مستقیم را ثابت کن، بعد اندازه و Alignment را بررسی کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools می‌توانی ببینی Shell واقعاً <code dir="ltr">display:flex</code> دارد یا نه، Childهای مستقیم کدام‌اند، Gap چقدر است و used width هر Item چیست. اما در این درس هنوز DevTools فقط ابزار تأیید است؛ تصمیم اصلی از Tree و Parent درست می‌آید.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-5-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-5-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-28">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-28-1" name="chk-28-1" type="checkbox"/><span>می‌توانم Flex Container و Flex Item را در Tree TUYA مشخص کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-28-2" name="chk-28-2" type="checkbox"/><span>می‌دانم فقط Childهای مستقیم Flex Item می‌شوند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-28-3" name="chk-28-3" type="checkbox"/><span>می‌توانم تفاوت Display، Normal Flow و Absolute را توضیح بدهم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-29">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-29-1" name="chk-29-1" type="checkbox"/><span>TUYA Shell را Flex Row می‌کنم و Copy/Visual را کنار هم قرار می‌دهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-29-2" name="chk-29-2" type="checkbox"/><span>Gap را روی Parent تنظیم می‌کنم، نه marginهای پراکنده روی ستون‌ها.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-29-3" name="chk-29-3" type="checkbox"/><span>در Mobile، Direction را به Column تغییر می‌دهم و نسخهٔ دوم سکشن نمی‌سازم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-30">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-30-1" name="chk-30-1" type="checkbox"/><span>در سناریوی سه Feature Card می‌توانم Parent مناسب را انتخاب کنم و توضیح بدهم چرا Flex روی Parent اعمال می‌شود.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-5-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-5-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، وارد اندازه‌گیری دقیق‌تر Itemها، Basis/Grow/Shrink یا مرحلهٔ بعدی Layout می‌شویم. هنوز Position نهایی Nodeها و تزئینات بصری را انجام نمی‌دهیم.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 5</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-5-completion">
<fieldset>
<legend>ثبت پایان درس 5</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-5-complete" name="lesson-5-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
