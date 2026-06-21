<article class="lesson card-surface" data-lesson="10" id="lesson-10">

<h2 class="lesson-title former-h1">درس 10 — Heading، Paragraph، List و Typography</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-10-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-10-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> متن را فقط از نظر ظاهر نبینی؛ برای هر متن، Element معنایی درست انتخاب کنی، سلسله‌مراتب Heading/Paragraph/List را نگه داری، و Typography را با خوانایی فارسی و متن واقعی تست کنی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> طراحی کامل Font System، Variableهای کامل Typography، Fluid type scale نهایی، یا همهٔ قواعد دسترسی‌پذیری متن.</p>
<p><strong>در پایان باید بتوانی:</strong> ستون متن TUYA را با Heading، Paragraph، Feature List و Classهای محدود بسازی؛ بدون Hard Breakهای شکننده و بدون یکی‌گرفتن نقش معنایی با ظاهر.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-10-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-10-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + 🔍 خوانایی‌سنجی</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰–۲۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۳۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس باید معنا را از ظاهر جدا کند. هنرجو نباید Heading را فقط برای بزرگ‌کردن متن یا Paragraph را فقط برای راحتی انتخاب کند. متن باید با محتوای واقعی، متن بلند و Mobile تست شود.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_semantic_typography_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-10-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-10-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>تا درس ۹، Structure، Layout، Flex، Wrap و Grid Decision را ساختی. اما Layout سالم بدون متن سالم کافی نیست. حالا باید محتوای Copy Area را از نظر معنا و خوانایی بسازی.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Structure / Layout
↓
Content Elements
↓
Semantic Hierarchy
↓
Typography
↓
Readability / Responsive Text</code></pre>
</figure>

<h3>مسئله</h3>
<p>ممکن است ظاهر یک متن درست باشد، اما Element اشتباه انتخاب شده باشد. مثلاً یک متن معمولی را Heading کرده‌ای فقط چون بزرگ‌تر بوده، یا یک لیست واقعی را با چند Paragraph پشت‌سرهم ساخته‌ای. نتیجه در Accessibility، نگهداری، Responsive و Design System ضعیف می‌شود.</p>

<h3>قانون اصلی: نقش را با ظاهر قاطی نکن</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Heading</dt><dd>عنوان یا زیربخش واقعی محتوا؛ برای ساختار سند.</dd>
<dt>Paragraph</dt><dd>متن توضیحی مستقل؛ برای خواندن پیوسته.</dd>
<dt>List</dt><dd>مجموعهٔ آیتم‌های مرتبط؛ وقتی چند مورد هم‌جنس داری.</dd>
<dt>Button / Link</dt><dd>عمل یا ناوبری؛ نه فقط متن رنگی.</dd>
<dt>Class</dt><dd>ظاهر را کنترل می‌کند؛ نقش معنایی را جایگزین نمی‌کند.</dd>
</dl>
</section>

<h3>Typography فقط Font نیست</h3>
<p>Typography معماری خواندن است. خوانایی از تعامل چند تصمیم ساخته می‌شود:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Font Family
+ Font Size
+ Font Weight
+ Line Height
+ Line Length
+ Contrast
+ Spacing
+ Language Script
+ Responsive Width</code></pre>
</figure>

<h3>فارسی را با متن واقعی فارسی تست کن</h3>
<p>Scale و فاصله‌ای که برای لاتین خوب است، الزاماً برای فارسی خوب نیست. اتصال حروف، نقطه‌ها، ارتفاع بصری، اعداد، واژه‌های انگلیسی داخل متن فارسی و جهت RTL باید با متن واقعی تست شوند.</p>

<h3>Line Height؛ فضای تنفس</h3>
<p>Line Height خیلی کم، متن فارسی را فشرده و خسته‌کننده می‌کند. Line Height خیلی زیاد، پیوند جمله‌ها را می‌شکند. برای متن بدنه، مقدار نسبی معمولاً مقاوم‌تر از عدد ثابت است، اما عدد نهایی باید با فونت و محتوای واقعی تست شود.</p>

<h3>طول خط</h3>
<p>اگر ستون متن خیلی عریض شود، چشم در پایان هر خط مسیر طولانی طی می‌کند و پیدا کردن خط بعد سخت می‌شود. اگر خیلی باریک شود، متن زیاد می‌شکند. بنابراین Typography فقط Font Size نیست؛ عرض ستون متن هم بخشی از Typography است.</p>

<h3>Hard Break را اول رد کن، بعد اگر لازم بود بپذیر</h3>
<p>قرار دادن چند <code dir="ltr">&lt;br&gt;</code> دستی در Paragraph معمولاً Responsive را شکننده می‌کند. Break هنری در Heading ممکن است در بعضی طراحی‌ها قابل دفاع باشد، اما باید آگاهانه، محدود و بعد از تست Mobile باشد.</p>

<h3>Typography Variable در برابر Typography Class</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Typography Variable vs Typography Class">
<table class="data-table educational-table edu-table">
<caption>تفاوت Variable و Class در Typography</caption>
<thead><tr><th scope="col">مفهوم</th><th scope="col">جنس</th><th scope="col">مثال</th><th scope="col">قاعده</th></tr></thead>
<tbody>
<tr><th scope="row">Typography Variable</th><td>مقدار خام</td><td><code dir="ltr">font-body</code>، <code dir="ltr">size-h2</code></td><td>مقدار را Variable کن.</td></tr>
<tr><th scope="row">Typography Class</th><td>تصمیم کامل ظاهری روی نقش</td><td><code dir="ltr">section-title</code>، <code dir="ltr">hero-lead</code></td><td>نقش متنی تکرارشونده را Class کن.</td></tr>
<tr><th scope="row">Semantic Element</th><td>نقش سند</td><td><code dir="ltr">h2</code>، <code dir="ltr">p</code>، <code dir="ltr">ul/li</code></td><td>نقش را با ظاهر عوض نکن.</td></tr>
</tbody>
</table>
</div>

<h3>قاعدهٔ این درس</h3>
<p>برای TUYA Copy، اول Element معنایی درست را بساز، بعد Class محدود و خوانا بده، بعد با متن کوتاه، متن بلند و Mobile تست کن. هنوز Font System کامل نمی‌سازیم.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-10.0.0" id="lesson-10-concept-reference">
<summary>📚 مرجع مفهومی کامل — Typography؛ متن فقط Font نیست</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="10" data-source-version="tuya-revised-10.0.0">

<p class="concept-reference-lead">این مرجع بخش مفهومی Typography را حفظ می‌کند و آن را به ستون متن TUYA وصل می‌کند. هدف حذف متن مفهومی نیست؛ هدف دقیق‌ترکردن تصمیم‌هاست.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-10-ref-problem">
<h3 id="lesson-10-ref-problem">۱. مسئله‌ای که Typography حل می‌کند</h3>
<p>کاربر قبل از دکمه و تصویر، متن را می‌خواند. اگر متن سلسله‌مراتب نامشخص، خط‌های خیلی بلند، وزن نامناسب، فاصلهٔ کم یا Breakهای دستی داشته باشد، Layout سالم هم تجربهٔ ضعیفی می‌دهد.</p>
<p>Typography یعنی طراحی مسیر خواندن: کجا شروع کنم، چه چیزی مهم‌تر است، کجا نفس بکشم و چگونه در Mobile ادامه بدهم.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-10-music">
<h3 id="lesson-10-music">۲. تشبیه موسیقی</h3>
<ul>
<li><strong>Font Family:</strong> جنس صدای ساز.</li>
<li><strong>Font Size:</strong> شدت صدا.</li>
<li><strong>Font Weight:</strong> تأکید نوازنده.</li>
<li><strong>Line Height:</strong> فاصلهٔ ضرب‌ها و فرصت نفس‌کشیدن.</li>
<li><strong>Paragraph Spacing:</strong> مکث میان جمله‌ها.</li>
<li><strong>Headingها:</strong> بخش‌های اصلی قطعه.</li>
<li><strong>Text Width:</strong> طول عبارت پیش از نفس بعدی.</li>
</ul>
<p>اگر همهٔ نت‌ها با یک شدت و بدون مکث اجرا شوند، حتی موسیقی خوب هم خفه‌کننده می‌شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-10-semantic">
<h3 id="lesson-10-semantic">۳. نقش معنایی و ظاهر را جدا کن</h3>
<p><code dir="ltr">h1</code>، <code dir="ltr">h2</code> و <code dir="ltr">h3</code> فقط برای بزرگ‌کردن متن نیستند. آن‌ها ساختار سند را می‌سازند. اگر فقط ظاهر بزرگ می‌خواهی، از Class استفاده کن، نه تغییر نقش معنایی.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">H1: عنوان اصلی صفحه
H2: بخش‌های اصلی
H3: زیربخش‌ها
Paragraph: متن توضیحی
List: مجموعهٔ آیتم‌های مرتبط</code></pre>
</figure>
<p>در Elementor، محتوای Element و نقش آن را در General/Content و ظاهر را در Style/Class مدیریت کن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-10-feature-list">
<h3 id="lesson-10-feature-list">۴. Feature List متن پشت‌سرهم نیست</h3>
<p>اگر چند ویژگی هم‌جنس داری، آن‌ها را مثل مجموعه ببین. از نظر ساختاری، هر Feature Item باید متن و نشانگر خودش را داشته باشد. Bullet یا Dot را داخل Paragraph تایپ نکن، چون Icon و Text باید مستقل Align، Gap و Style شوند.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Feature List
├── Feature Item
│   ├── Dot / Icon
│   └── Feature Text
├── Feature Item
│   ├── Dot / Icon
│   └── Feature Text
└── Feature Item
    ├── Dot / Icon
    └── Feature Text</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-10-lineheight">
<h3 id="lesson-10-lineheight">۵. Line Height و طول خط</h3>
<p>Line Height باید با فونت، زبان، اندازه و عرض ستون هماهنگ شود. برای فارسی، line-height خیلی کم باعث فشردگی نقطه‌ها و اتصال‌ها می‌شود. طول خط هم باید کنترل شود؛ متن خیلی عریض خسته‌کننده است و متن خیلی باریک زیاد می‌شکند.</p>
<p>در TUYA، Copy Area باید با متن واقعی فارسی، عدد، واژهٔ انگلیسی و Mobile تست شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-10-units">
<h3 id="lesson-10-units">۶. واحدهای Typography</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Typography units">
<table class="data-table educational-table edu-table">
<caption>واحدهای رایج Typography</caption>
<thead><tr><th scope="col">واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">px</code></th><td>طول CSS ثابت</td><td>کنترل دقیق کوچک</td><td>Scale سراسری را سخت‌تر می‌کند.</td></tr>
<tr><th scope="row"><code dir="ltr">rem</code></th><td>Root font size</td><td>Scale قابل‌مدیریت‌تر</td><td>اگر root تغییر کند، همه‌چیز تغییر می‌کند.</td></tr>
<tr><th scope="row"><code dir="ltr">em</code></th><td>Font size همان Element یا Parent، بسته به Property</td><td>فاصله‌های نسبی محلی</td><td>با nesting می‌تواند غیرمنتظره شود.</td></tr>
<tr><th scope="row"><code dir="ltr">vw</code></th><td>Viewport width</td><td>اندازهٔ سیال</td><td>بدون min/max می‌تواند خیلی کوچک/بزرگ شود.</td></tr>
<tr><th scope="row"><code dir="ltr">clamp()</code></th><td>حداقل، مقدار سیال، حداکثر</td><td>Typography سیال کنترل‌شده</td><td>جای تست واقعی را نمی‌گیرد.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-10-br">
<h3 id="lesson-10-br">۷. Hard Break و Responsive</h3>
<p>Break دستی ممکن است در Desktop یک خط هنری زیبا بسازد، اما در Mobile، ترجمه یا متن بلند همان Break در نقطهٔ بدی باقی می‌ماند. بنابراین:</p>
<ul>
<li>در Paragraph، Hard Break غیرمعنایی را پیش‌فرض رد کن.</li>
<li>در Heading، اگر Break هنری لازم است، آن را محدود و تست‌شده نگه دار.</li>
<li>برای کنترل عرض و شکست متن، اول Width، Max Width، Line Height و Font Size را بررسی کن.</li>
<li>اگر Break برای معناست، دلیلش را ثبت کن.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-10-rtl">
<h3 id="lesson-10-rtl">۸. متن انگلیسی داخل صفحهٔ فارسی</h3>
<p>در صفحهٔ RTL، واژه‌ها یا عبارت‌های انگلیسی باید با جهت مناسب و isolation مدیریت شوند تا ترتیب نشانه‌ها و اعداد به‌هم نریزد. اگر یک عبارت انگلیسی مستقل است، آن را در wrapper مناسب با <code dir="ltr">dir="ltr"</code> یا کلاس ایزوله نگه دار. این تصمیم باید با متن واقعی تست شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-10-devtools">
<h3 id="lesson-10-devtools">۹. Debug Typography</h3>
<p>در Computed Style این موارد را با هم بخوان:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">font-family
font-size
font-weight
line-height
letter-spacing
word-break
overflow-wrap
max-inline-size
direction
unicode-bidi</code></pre>
</figure>
<p>اگر Font دیگری نمایش داده می‌شود، مشکل فقط Style نیست؛ ممکن است فایل Font، وزن Font یا مسیر Load درست نباشد.</p>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-10-golden">
<h3 id="lesson-10-golden">۱۰. قوانین طلایی</h3>
<ul>
<li><strong>HTML نقش متن را تعیین می‌کند؛ Class ظاهر آن را.</strong></li>
<li><strong>Heading را برای بزرگ‌کردن متن استفاده نکن؛ برای ساختار استفاده کن.</strong></li>
<li><strong>Typography حاصل یک عدد Font Size نیست؛ حاصل یک سیستم است.</strong></li>
<li><strong>فارسی را با متن واقعی فارسی آزمایش کن.</strong></li>
<li><strong>Hard Break در Paragraph را پیش‌فرض نپذیر.</strong></li>
<li><strong>اگر متن بلند Layout را می‌شکند، فقط متن مقصر نیست؛ Container و Width را بررسی کن.</strong></li>
<li><strong>مقدار را Variable کن؛ نقش متنی تکرارشونده را Class کن.</strong></li>
<li><strong>Typography نهایی تا قبل از تست Mobile و محتوای واقعی provisional است.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>رفتارهای Typography، واحدهای CSS، Line Height، Wrap و direction بر پایهٔ CSS و مستندات Elementor/مرورگر توضیح داده شده‌اند. تشبیه‌ها آموزشی‌اند و مقدارهای TUYA تا پیش از تست Frontend قطعی نیستند.</p>
<ul>
<li><a href="https://elementor.com/help/style-tab-typography/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Typography</a></li>
<li><a href="https://elementor.com/help/what-is-typography/" rel="noopener noreferrer" target="_blank">Elementor — Typography and units</a></li>
<li><a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/line-height" rel="noopener noreferrer" target="_blank">MDN — line-height</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_text" rel="noopener noreferrer" target="_blank">MDN — CSS Text</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-10-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-10-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Typography؛ rem، em، px، vw و clamp</span>
</summary>
<section aria-labelledby="lesson-10-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Font Size فقط یک عدد نیست. <code dir="ltr">rem</code> به root، <code dir="ltr">em</code> به context محلی، <code dir="ltr">px</code> به طول CSS و <code dir="ltr">vw</code> به عرض viewport وابسته است.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۰" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Font Size</th><td><code dir="ltr">font-size</code></td><td>px, rem, em, vw, clamp</td><td>وابسته به واحد</td><td>vw بدون حد می‌تواند متن را خراب کند.</td></tr>
<tr><th scope="row">Line Height</th><td><code dir="ltr">line-height</code></td><td>number, em, px, %</td><td>font-size جاری</td><td>عدد UI را با قابلیت CSS خام یکی فرض کنی.</td></tr>
<tr><th scope="row">Font Weight</th><td><code dir="ltr">font-weight</code></td><td>keyword یا عدد 100–900</td><td>Font loaded</td><td>وزنی را انتخاب کنی که فایلش Load نشده است.</td></tr>
<tr><th scope="row">Text Width</th><td><code dir="ltr">max-inline-size</code> / width</td><td>rem, ch, %, px</td><td>Parent و font metrics</td><td>ch را برای فارسی معیار دقیق فرض کنی.</td></tr>
<tr><th scope="row">Direction</th><td><code dir="ltr">dir</code> / <code dir="ltr">direction</code></td><td>rtl / ltr</td><td>زبان و محتوا</td><td>متن انگلیسی داخل RTL را بی‌ایزوله رها کنی.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>root=16px → 2rem=32px. اگر parent font-size=20px باشد، child با 2em=40px. عدد یکسان است، اما مرجع فرق کرده است.</p></section>
<section><h3>📱 در Responsive</h3><p>Mobile فقط Font کوچک‌تر نمی‌خواهد؛ Width، Line Height، Break و Gap متن هم باید بررسی شوند.</p></section>
<section><h3>🔬 در DevTools</h3><p>font-family، font-size، line-height، loaded font، inherited source و computed width را با هم ببین.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-10-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-10-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Intro و Feature List در Copy Area</h3>
<p>در این تمرین فقط محتوای متنی Copy Area را می‌سازی: Intro، Heading، Paragraph و Feature List. هنوز Font System کامل، Variableهای Typography، Animation، Visual Stage یا Style نهایی نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 10">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از ساخت متن</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy Area محل متن، Intro، Feature List، Actions و Logo Strip است.</td><td>متن‌ها داخل TUYA Copy ساخته می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Intro متن توضیحی مستقل است، نه Heading.</td><td>Intro با Paragraph ساخته می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Classهای پیشنهادی مثل <code dir="ltr">c-platform-intro</code> و <code dir="ltr">c-feature-item</code>.</td><td>نام‌ها تا قبل از Design System نهایی قطعی نیستند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>متن نهایی فارسی، ترجمه، طول نهایی، فونت Load شده و Weight واقعی.</td><td>Typography نهایی قطعی نمی‌شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — اول Element معنایی را انتخاب کن</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس ده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ساخت متن معنایی، نه طراحی نهایی Font System.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → داخل <code dir="ltr">TUYA Copy</code> → Add Heading / Paragraph / Feature List.</p>
<p><strong>Element هدف:</strong> فقط متن‌های داخل <code dir="ltr">TUYA Copy</code>.</p>
<p><strong>Class فعال:</strong> Classهای محلی متن؛ Global جدید فقط اگر نقش تکرارشونده ثابت شود.</p>
<p><strong>Property:</strong> Element type / basic typography / line-height / text width.</p>
<p><strong>نباید تغییر کند:</strong> Shell layout، Copy/Visual basis، Logo Strip، Grid آزمایشی، Position، Nodeها، Shadow/Glow، Background نهایی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «متن‌ها با Element معنایی درست ساخته شدند و هنوز Typography نهایی قطعی نشده است.»</p>
</aside>

<h3>مرحلهٔ ۲ — ساختار پیشنهادی Copy Text</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Copy
├── Eyebrow / small intro label
├── Heading
├── Paragraph Intro
├── Feature List
│   ├── Feature Item
│   │   ├── Dot / Icon
│   │   └── Feature Text
│   └── Feature Item
├── Actions
└── Logo Strip</code></pre>
</figure>

<h3>مرحلهٔ ۳ — Feature Item را درست بساز</h3>
<ol>
<li>یک Parent برای Feature List بساز.</li>
<li>اولین Feature Item را بساز.</li>
<li>داخل Feature Item یک Dot/Icon و یک Paragraph یا Text برای Feature Text قرار بده.</li>
<li>Feature Item را با Flex Row تراز کن.</li>
<li>Gap بین Dot و Text را روی Parent Feature Item بده.</li>
<li>بعد از سالم‌بودن اولین Item، آن را تکثیر کن.</li>
</ol>
<p>Bullet را داخل متن تایپ نکن، چون Dot/Icon و Text باید مستقل Align، Gap و Style شوند.</p>

<h3>مرحلهٔ ۴ — مقدارهای شروع Typography را فقط provisional تست کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional typography values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع Typography</caption>
<thead><tr><th scope="col">بخش</th><th scope="col">Element</th><th scope="col">Class candidate</th><th scope="col">تست لازم</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Heading</th><td>Heading مناسب سلسله‌مراتب</td><td><code dir="ltr">c-hero-title</code></td><td>متن کوتاه/بلند، Mobile، line breaks</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Intro</th><td>Paragraph</td><td><code dir="ltr">c-platform-intro</code></td><td>Line Height، text width، Mobile wrap</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Feature Item</th><td>Item/Row</td><td><code dir="ltr">c-feature-item</code></td><td>Align Dot/Text، Gap، متن دوخطی</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Feature Text</th><td>Paragraph/Text</td><td><code dir="ltr">c-feature-text</code></td><td>Wrap، line-height، متن طولانی</td><td><code dir="ltr">provisional</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۵ — تست متن واقعی</h3>
<ol>
<li>یک نسخهٔ کوتاه Heading را تست کن.</li>
<li>یک نسخهٔ بلند Heading را تست کن.</li>
<li>Intro را در دو طول مختلف تست کن.</li>
<li>یک Feature Text را دوخطی کن و تراز Dot را بررسی کن.</li>
<li>Mobile را ببین و Hard Breakهای غیرضروری را حذف کن.</li>
</ol>

<h3>مرحلهٔ ۶ — سؤال توقف</h3>
<p>متن معرفی مستقل داخل TUYA Copy باید با چه Elementی ساخته شود؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-10">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-10-a" name="stop-question-10" type="radio" value="A"/><span>A) Heading، چون می‌خواهم کمی بزرگ باشد.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-10-b" name="stop-question-10" type="radio" value="B"/><span>B) Paragraph، چون متن توضیحی مستقل است.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-10-c" name="stop-question-10" type="radio" value="C"/><span>C) Button، چون رنگی‌تر دیده می‌شود.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Element بر اساس نقش محتوا انتخاب می‌شود، نه فقط ظاهر. اگر Paragraph باید بزرگ‌تر یا متفاوت دیده شود، با Class و Typography کنترل می‌شود.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> برای کنترل خط‌شکنی داخل Paragraph چند <code dir="ltr">&lt;br&gt;</code> دستی بگذاری.</p>
<p><strong>نشانه:</strong> Desktop خوب است، اما Mobile، ترجمه یا متن بلند بد می‌شکند.</p>
<p><strong>قاعده:</strong> برای کنترل خوانایی، اول text width، line-height، font-size و responsive layout را بررسی کن؛ Break دستی را فقط با دلیل روشن بپذیر.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>یک Paragraph را با چند Break دستی تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Break دستی شکننده</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Line 1&lt;br&gt;
Line 2&lt;br&gt;
Line 3

در Mobile:
Line 1 نصفه می‌شود
Line 2 در جای بد می‌شکند
Line 3 تنها می‌ماند</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-55">
<fieldset>
<legend>Checkpoint درس ۱۰</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-55-1" name="chk-55-1" type="checkbox"/><span>Intro با Paragraph ساخته شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-55-2" name="chk-55-2" type="checkbox"/><span>Heading براساس سلسله‌مراتب محتوا انتخاب شده، نه فقط اندازهٔ ظاهری.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-55-3" name="chk-55-3" type="checkbox"/><span>Featureها Itemهای تکراری مستقل‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-55-4" name="chk-55-4" type="checkbox"/><span>Dot و Text با Flexbox و Gap تراز شده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-55-5" name="chk-55-5" type="checkbox"/><span>Hard Break غیرضروری ندارم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-55-6" name="chk-55-6" type="checkbox"/><span>Typography نهایی را هنوز بدون Mobile و متن واقعی قطعی نکرده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Heading و Paragraph براساس چه چیزی انتخاب می‌شوند؟</p>
<p><strong>انتقال به موقعیت تازه:</strong> یک FAQ داری؛ سؤال‌ها و جواب‌ها را با چه Elementهایی می‌سازی و چرا؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید نقش محتوا را از ظاهر جدا کند، Hard Break را فقط با دلیل معنایی یا Art Direction محدود بپذیرد، و خوانایی را با متن واقعی و Mobile تست کند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-10-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Typography و طول خط در Mobile</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">verified_method_provisional_values</code></p>
<ul>
<li>Mobile فقط Font کوچک‌تر نمی‌خواهد؛ Width، Line Height و Wrap هم باید بررسی شوند.</li>
<li>Heading بلند را در ۳ عرض مختلف تست کن.</li>
<li>Intro را با متن کوتاه و بلند تست کن.</li>
<li>Feature Text دوخطی را تست کن و تراز Dot را ببین.</li>
<li>متن انگلیسی داخل RTL را با جهت مناسب و isolation بررسی کن.</li>
<li>وزن Font انتخاب‌شده را با Load واقعی Font بررسی کن.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-10-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-10-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 CASE-CONTENT-BR-001</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">context_dependent</code></p>
<p>در Export واقعی ممکن است چند Heading یا Paragraph دارای Break صریح باشند. Break هنری در Heading ممکن است قابل دفاع باشد؛ Break دستی در Paragraph معمولاً شکننده‌تر است.</p>

<h3>قبل از حذف یا پذیرش Break چه بررسی کنم؟</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>Break برای معناست یا فقط ظاهر Desktop؟</li>
<li>در Mobile چه اتفاقی می‌افتد؟</li>
<li>در ترجمه یا متن بلند چه اتفاقی می‌افتد؟</li>
<li>آیا با text width، line-height یا font-size بهتر حل می‌شود؟</li>
<li>آیا Break روی Accessibility یا خواندن متن اثر بد دارد؟</li>
</ul>
</section>

<h3>واژه‌ها را اشتباه نگیر</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Element</dt><dd>کل واحد HTML یا عنصر داخل Editor.</dd>
<dt>Tag</dt><dd>علامت HTML مثل <code dir="ltr">&lt;h2&gt;</code> یا <code dir="ltr">&lt;p&gt;</code>.</dd>
<dt>Class</dt><dd>نام Style قابل استفاده.</dd>
<dt>Heading</dt><dd>نقش محتوایی در ساختار متن.</dd>
</dl>
</section>

<h3>🔬 پشت صحنه</h3>
<p>Line Height، Width متن، Font metrics، word-break و overflow-wrap روی Wrap اثر می‌گذارند. قبل از واردکردن CSS یا Break دستی، اثر این عوامل را در UI و DevTools ببین.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-10-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-10-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-58">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-58-1" name="chk-58-1" type="checkbox"/><span>می‌توانم Heading، Paragraph و List را براساس معنی محتوا انتخاب کنم، نه فقط ظاهر.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-58-2" name="chk-58-2" type="checkbox"/><span>می‌توانم توضیح بدهم چرا Hard Line Break در Paragraph می‌تواند Responsive را شکننده کند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-58-3" name="chk-58-3" type="checkbox"/><span>می‌توانم بگویم Typography فقط Font Family نیست.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-59">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-59-1" name="chk-59-1" type="checkbox"/><span>Intro، Feature List و متن‌های TUYA را با Element معنایی مناسب می‌سازم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-59-2" name="chk-59-2" type="checkbox"/><span>با متن طولانی، Mobile و Zoom بررسی می‌کنم که محتوا بدون برخورد Wrap می‌شود.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-59-3" name="chk-59-3" type="checkbox"/><span>Feature Item را با Dot/Icon و Text مستقل می‌سازم، نه Bullet تایپی داخل Paragraph.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-60">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-60-1" name="chk-60-1" type="checkbox"/><span>برای یک بخش FAQ می‌توانم سلسله‌مراتب Heading و Paragraph مناسب را پیشنهاد بدهم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-10-end-comparisons">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Typography Variable در برابر Typography Class</span>
</summary>
<section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card">
<h3>Typography Variable</h3>
<p>Variable مقدار خام نگه می‌دارد؛ مثل <code dir="ltr">font-body</code> یا <code dir="ltr">size-h2</code>. این‌ها مادهٔ خام سیستم تایپوگرافی‌اند.</p>
</section>
<section class="inline-compare-card">
<h3>Typography Class</h3>
<p>Class یک تصمیم کامل ظاهری است؛ مثلاً <code dir="ltr">section-title</code> می‌تواند font، size، line-height، color و spacing را با هم کنترل کند.</p>
<p class="golden-rule">قانون طلایی: مقدار را Variable کن؛ نقش متنی تکرارشونده را Global Class کن.</p>
</section>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-10-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-10-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، طبق ترتیب واقعی جزوه ادامه می‌دهیم. متن‌های TUYA تا اینجا باید معنایی، خوانا و بدون Breakهای شکننده باشند.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 10</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-10-completion">
<fieldset>
<legend>ثبت پایان درس 10</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-10-complete" name="lesson-10-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
