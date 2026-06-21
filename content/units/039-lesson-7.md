<article class="lesson card-surface" data-lesson="7" id="lesson-7">

<h2 class="lesson-title former-h1">درس 7 — Grow، Shrink، Basis، Width و Max Width</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-7-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-7-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> بعد از ساخت دو ستون Flex و خواندن محور، رفتار اندازهٔ Flex Itemها را بفهمی: Basis نقطهٔ شروع روی Main Axis است، Grow سهم از فضای اضافه است، Shrink سهم از کمبود فضاست، Width اندازهٔ معمولی‌تر است و Max Width سقف رشد می‌گذارد.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> الگوریتم رسمی کامل Flexbox، تمام shorthandهای CSS، محاسبهٔ دقیق نهایی مرورگر، Position نهایی Nodeها، Visual Stage کامل یا مقادیر قطعی طراحی نهایی TUYA.</p>
<p><strong>در پایان باید بتوانی:</strong> Copy را انعطاف‌پذیر و Visual را کنترل‌شده نگه داری؛ یعنی Copy بتواند با متن بلند Shrink شود و Visual از Parent بیرون نزند.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-7-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-7-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + 🔍 عیب‌یابی Responsive</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۵–۳۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس نباید به فرمول‌زدگی تبدیل شود. هدف این است که هنرجو بفهمد Flex Itemها با فضای اضافه و کمبود فضا مذاکره می‌کنند. مقدارهای Copy/Visual باید با متن واقعی و عرض‌های مختلف تست شوند.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_flex_item_sizing_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-7-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-7-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس ۵، TUYA Shell را Flex کردی. در درس ۶، محور را خواندی. حالا درس ۷ می‌گوید هر Item روی Main Axis چگونه اندازهٔ اولیه می‌گیرد، چگونه فضای اضافه را می‌گیرد و چگونه در فضای کم جمع می‌شود.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Context
↓
Structure
↓
Class Scope
↓
Box Model
↓
Flex Container
↓
Axis / Direction
↓
Flex Item Sizing: Basis / Grow / Shrink / Width / Max Width</code></pre>
</figure>

<h3>مدل ساده</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Basis</dt><dd>اندازهٔ شروع Flex Item روی Main Axis؛ در Row معمولاً شبیه عرض اولیه، و در Column معمولاً شبیه ارتفاع اولیه رفتار می‌کند.</dd>
<dt>Grow</dt><dd>وقتی Parent فضای اضافه دارد، سهم Item از آن فضای اضافه.</dd>
<dt>Shrink</dt><dd>وقتی فضای Parent کم است، اجازه و سهم Item برای کوچک‌شدن.</dd>
<dt>Width</dt><dd>اندازهٔ معمولی‌تر Element؛ در Flex ممکن است با Basis و اندازهٔ محتوا وارد مذاکره شود.</dd>
<dt>Max Width</dt><dd>سقف رشد؛ اجازه نمی‌دهد Item از یک حد بیشتر عریض شود.</dd>
<dt>Min Width</dt><dd>کف کوچک‌شدن؛ اگر زیاد یا auto باشد، ممکن است اجازهٔ Shrink واقعی ندهد.</dd>
</dl>
</section>

<h3>Basis همیشه «عرض» نیست</h3>
<p><code dir="ltr">flex-basis</code> اندازهٔ شروع روی <strong>Main Axis</strong> است. اگر Direction روی Row باشد، Main Axis افقی است و Basis شبیه عرض اولیه دیده می‌شود. اگر Direction روی Column باشد، Main Axis عمودی است و Basis شبیه ارتفاع اولیه رفتار می‌کند.</p>
<p>بنابراین بعد از هر تغییر Direction، معنی عملی Basis را دوباره بخوان.</p>

<h3>Grow فقط فضای اضافه را تقسیم می‌کند</h3>
<p>Grow به این معنا نیست که Item همیشه بزرگ می‌شود. اگر Parent فضای اضافه نداشته باشد، Grow چیزی برای تقسیم ندارد.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Parent = 1000px
Copy basis = 500px
Visual basis = 350px
Gap = 40px
فضای مصرف‌شده = 890px
فضای اضافه = 110px

اگر Copy grow=1 و Visual grow=0:
Copy می‌تواند آن فضای اضافه را بگیرد؛ Visual سقف/کنترل خودش را حفظ می‌کند.</code></pre>
</figure>

<h3>Shrink فقط در کمبود فضا فعال می‌شود</h3>
<p>Shrink وقتی مهم می‌شود که مجموع Basisها، Gap و محدودیت‌ها از فضای Parent بیشتر شود. اگر Shrink صفر باشد یا Min Width اجازه ندهد، Item ممکن است Overflow بسازد.</p>
<p>نکتهٔ مهم: Shrink فقط با عدد خودش کار نمی‌کند؛ Basis، Min Width، محتوای داخلی و Max/Min محدودیت‌ها هم اثر دارند.</p>

<h3>تلهٔ مشهور min-width:auto</h3>
<p>گاهی یک Flex Item با متن طولانی، URL، تصویر یا Child عریض حاضر نیست به اندازهٔ لازم کوچک شود. در CSS خام، یک راه‌حل رایج برای اجازه‌دادن به Shrink واقعی این است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.flex-item {
  min-width: 0;
}</code></pre>
</figure>
<p>در Elementor، اول باید ببینی کنترل Min Width، Overflow، اندازهٔ تصویر و رفتار محتوای داخلی چه تولید کرده‌اند. فقط زیادکردن Shrink مشکل را حل نمی‌کند.</p>

<h3>الگوی ذهنی TUYA</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Copy</dt><dd>محتوایی و انعطاف‌پذیر است؛ باید بتواند رشد کند، با متن بلند مدیریت شود و در عرض کمتر Shrink شود.</dd>
<dt>Visual</dt><dd>کنترل‌شده‌تر است؛ باید سقف اندازه داشته باشد و از Parent بیرون نزند.</dd>
</dl>
</section>

<h3>Basis در برابر Width</h3>
<p>Width اندازهٔ معمولی Element است. Basis سهم اولیهٔ Item در مذاکرهٔ Flexbox است. در یک Parent Flex، برای ستون‌های Responsive معمولاً Basis روشن‌تر از Width است، چون به زبان خود Flexbox حرف می‌زند.</p>

<h3>قاعدهٔ این درس</h3>
<p>برای TUYA، Copy و Visual را هنوز قطعی عددگذاری نکن. فقط قرارداد رفتاری بساز: Copy انعطاف‌پذیرتر، Visual محدودتر، هر دو بدون Overflow و بدون Absolute.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-7.0.0" id="lesson-7-concept-reference">
<summary>📚 مرجع مفهومی کامل — Flex Basis، Grow، Shrink، Width و Max Width</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="7" data-source-version="tuya-revised-7.0.0">

<p class="concept-reference-lead">این مرجع، هستهٔ مفهومی درس موجود را حفظ می‌کند و آن را به پروژهٔ TUYA وصل می‌کند. هدف محاسبهٔ کامل الگوریتم Flexbox نیست؛ هدف ساختن قرارداد اندازهٔ قابل Debug است.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-7-ref-problem">
<h3 id="lesson-7-ref-problem">۱. مسئله‌ای که این مفهوم حل می‌کند</h3>
<p>دو ستون ممکن است در Desktop هر دو شبیه 50/50 دیده شوند، اما رفتارشان در عرض کم متفاوت باشد. یکی با Width ثابت آمده، یکی با Basis و Shrink. ظاهر شبیه است، اما قرارداد Responsive متفاوت است.</p>
<p>پس سؤال درست این نیست: «ظاهرش چند درصد است؟» سؤال درست این است:</p>
<blockquote><p>این Item با فضای اضافه و کمبود فضا چه رفتاری دارد؟</p></blockquote>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-7-table-analogy">
<h3 id="lesson-7-table-analogy">۲. تشبیه میز غذا</h3>
<ul>
<li><strong>Basis:</strong> سهم اولیهٔ هر نفر از میز.</li>
<li><strong>Grow:</strong> سهم از فضای اضافه وقتی میز بزرگ‌تر از نیاز اولیه است.</li>
<li><strong>Shrink:</strong> سهم از کمبود جا وقتی میز کوچک‌تر از نیاز اولیه است.</li>
<li><strong>Min/Max:</strong> محدودیت حداقل و حداکثر هر نفر.</li>
</ul>
<p>مرورگر اول سهم اولیه را می‌بیند، بعد فضای اضافه یا کمبود را تقسیم می‌کند. اما محدودیت‌ها و محتوای واقعی هم در تصمیم نهایی دخالت دارند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-7-basis">
<h3 id="lesson-7-basis">۳. Flex Basis</h3>
<p>Basis اندازهٔ آغازین Flex Item روی Main Axis است. اگر Direction روی Row باشد، با عرض ذهنی نزدیک است؛ اگر Column باشد، با ارتفاع ذهنی نزدیک می‌شود.</p>
<p>اگر Basis روی <code dir="ltr">auto</code> باشد، مرورگر ممکن است از Width/Height، اندازهٔ محتوا و محدودیت‌ها برای تعیین اندازهٔ پایه کمک بگیرد.</p>
<aside class="warning-card">
<p><strong>تله:</strong> خالی‌گذاشتن Width در UI لزوماً به معنای <code dir="ltr">flex-basis:0</code> نیست. باید در Computed Style بررسی شود.</p>
</aside>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-7-grow">
<h3 id="lesson-7-grow">۴. Flex Grow</h3>
<p>Grow فقط فضای مثبت باقی‌مانده را تقسیم می‌کند. Grow نسبت اندازهٔ نهایی نیست؛ نسبت سهم از فضای اضافه است.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">A basis = 200px
B basis = 200px
Parent free space = 600px

A grow = 1
B grow = 2

فضای اضافه با نسبت 1 به 2 تقسیم می‌شود؛
نه اینکه B الزاماً دو برابر A نهایی باشد.</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-7-shrink">
<h3 id="lesson-7-shrink">۵. Flex Shrink</h3>
<p>Shrink در فضای منفی فعال می‌شود؛ یعنی وقتی مجموع Basisها، Gap و محدودیت‌ها از فضای Parent بزرگ‌تر است.</p>
<p>اگر Shrink صفر باشد، Item اجازهٔ کوچک‌شدن نمی‌دهد و ممکن است Overflow ایجاد شود. اما اگر Min Width یا محتوای داخلی بزرگ باشد، حتی Shrink یک هم ممکن است کافی نباشد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-7-minwidth">
<h3 id="lesson-7-minwidth">۶. Min Width و Overflow</h3>
<p>در Flexbox، Min Width خیلی مهم است. یک Item ممکن است به خاطر محتوای طولانی یا تصویر بزرگ اجازهٔ کوچک‌شدن ندهد. برای Debug، این‌ها را بررسی کن:</p>
<ul>
<li>Min Width روی Item چیست؟</li>
<li>متن یا URL می‌تواند بشکند؟</li>
<li>تصویر max-width مناسب دارد؟</li>
<li>Overflow پنهان شده یا واقعاً حل شده؟</li>
<li>Computed Style چه می‌گوید؟</li>
</ul>
<p><code dir="ltr">min-width:0</code> یک «ترفند کور» نیست؛ اجازه‌ای است برای اینکه Flex Item بتواند از حداقل اندازهٔ محتوایی خود کوچک‌تر شود، اگر طراحی این اجازه را می‌دهد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-7-tuya-contract">
<h3 id="lesson-7-tuya-contract">۷. قرارداد اندازهٔ TUYA</h3>
<p>در این درس، هنوز مقدار نهایی نداریم. فقط قرارداد رفتاری داریم:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Shell = Flex Row

Copy:
- basis شروع: حدود 52% تا 55% یا یک مقدار rem مناسب، provisional
- grow: 1، اگر فضای اضافه باید به متن برسد
- shrink: 1، برای جلوگیری از overflow
- min-width: 0، اگر متن طولانی مانع shrink شود

Visual:
- basis شروع: حدود 45% تا 48% یا مقدار rem مناسب، provisional
- grow: 0 یا محدود
- shrink: 1
- max-width: کنترل‌شده، provisional</code></pre>
</figure>
<p>این قرارداد قطعی نیست. باید با Gap، Parent واقعی، متن واقعی، تصویر واقعی و Breakpointها تست شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-7-width-maxwidth">
<h3 id="lesson-7-width-maxwidth">۸. Width و Max Width در کنار Basis</h3>
<p>Width هنوز مفید است، اما وقتی Parent Flex است، Basis زبان مستقیم‌تر Flex است. Max Width برای Visual مهم است چون نمی‌خواهی Visual در Desktop بیش از حد عریض شود یا در فضای کم از Parent بیرون بزند.</p>
<p>قانون عملی:</p>
<ul>
<li>برای شروع سهم Flex Itemها → Basis.</li>
<li>برای سقف رشد Visual → Max Width.</li>
<li>برای جلوگیری از Overflow متن → Min Width / content wrapping.</li>
<li>برای کنترل نهایی در DevTools → Computed Style.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-7-responsive">
<h3 id="lesson-7-responsive">۹. Responsive Checkpoint</h3>
<p>Basis یا Widthی که در Desktop دو ستون می‌سازد، ممکن است در Mobile باعث فشردگی یا Overflow شود. وقتی Direction به Column تغییر می‌کند، Basis روی Main Axis جدید معنی پیدا می‌کند؛ پس باید دوباره بررسی شود.</p>
<ul>
<li>در Mobile، آیا Itemها Width قابل‌انطباق دارند؟</li>
<li>آیا Basis Desktop باعث ارتفاع یا عرض ناخواسته شده؟</li>
<li>آیا Copy با متن بلند می‌تواند بشکند و جمع شود؟</li>
<li>آیا Visual سقف مناسب دارد؟</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-7-golden">
<h3 id="lesson-7-golden">۱۰. قوانین طلایی</h3>
<ul>
<li><strong>Basis نقطهٔ شروع است، نه اندازهٔ نهایی.</strong></li>
<li><strong>Basis روی Main Axis کار می‌کند؛ همیشه عرض نیست.</strong></li>
<li><strong>Grow فقط فضای اضافه را تقسیم می‌کند.</strong></li>
<li><strong>Shrink فقط در کمبود فضا فعال می‌شود.</strong></li>
<li><strong>Min Width می‌تواند اجازهٔ Shrink واقعی را مسدود کند.</strong></li>
<li><strong>Max Width برای کنترل Visual ضروری‌تر از حدس‌زدن عرض از Screenshot است.</strong></li>
<li><strong>Computed Style را بخوان: width، flex-basis، flex-grow، flex-shrink، min-width، max-width.</strong></li>
<li><strong>مقادیر Copy و Visual تا قبل از تست واقعی provisional هستند.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفاهیم Basis، Grow، Shrink، Min/Max و محور اصلی بر پایهٔ رفتار CSS Flexbox و مستندات Elementor دربارهٔ Flexbox و Responsive Editing نوشته شده‌اند. تصمیم‌های عددی TUYA تا پیش از UI واقعی و Breakpoint Validation قطعی نیستند.</p>
<ul>
<li><a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis" rel="noopener noreferrer" target="_blank">MDN — flex-basis</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow" rel="noopener noreferrer" target="_blank">MDN — flex-grow</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink" rel="noopener noreferrer" target="_blank">MDN — flex-shrink</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-7-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-7-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Basis، Grow، Shrink، Width و Max Width</span>
</summary>
<section aria-labelledby="lesson-7-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در این درس بعضی مقدارها واحد طول دارند و بعضی بدون واحدند. Grow و Shrink عدد بدون واحدند؛ Basis، Width و Max Width می‌توانند px، %، rem یا auto باشند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۷" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Flex Basis</th><td>length / % / auto</td><td>Main Axis و Parent</td><td>همیشه عرض فرض شود.</td></tr>
<tr><th scope="row">Flex Grow</th><td>number بدون واحد</td><td>فضای اضافهٔ Parent</td><td>نسبت اندازهٔ نهایی فرض شود.</td></tr>
<tr><th scope="row">Flex Shrink</th><td>number بدون واحد</td><td>کمبود فضای Parent</td><td>بدون توجه به min-width تغییر داده شود.</td></tr>
<tr><th scope="row">Width</th><td>length / % / auto</td><td>Parent و layout context</td><td>با Basis یکی فرض شود.</td></tr>
<tr><th scope="row">Max Width</th><td>length / % / rem</td><td>سقف رشد Item</td><td>بدون تست واقعی برای Visual قطعی شود.</td></tr>
<tr><th scope="row">Min Width</th><td>length / auto / 0</td><td>کف کوچک‌شدن Item</td><td>فراموش شود و Shrink بی‌اثر به نظر برسد.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Copy basis 55% و Visual basis 45% باشند و Gap هم داشته باشی، مجموع مؤثر می‌تواند از Parent بیشتر شود. Basisها را همراه Gap و Max/Min بررسی کن.</p></section>
<section><h3>📱 در Responsive</h3><p>در Mobile، Direction معمولاً Column است. Basis روی Main Axis جدید خوانده می‌شود؛ پس Basisهای Desktop را بدون بازبینی نگه ندار.</p></section>
<section><h3>🔬 در DevTools</h3><p>Computed Style را با هم بخوان: <code dir="ltr">width</code>، <code dir="ltr">flex-basis</code>، <code dir="ltr">flex-grow</code>، <code dir="ltr">flex-shrink</code>، <code dir="ltr">min-width</code> و <code dir="ltr">max-width</code>.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-7-flex-sizing-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Basis، Grow و Shrink روی Main Axis</span>
</summary>
<section class="disclosure-content lesson-section">
<p>این Step‑Through برای حفظ روح نسخهٔ تعاملی درس آمده است. هر حالت را اول پیش‌بینی کن، بعد نتیجه را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Step Through Flex Sizing">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ حالت‌های Flex sizing</caption>
<thead><tr><th scope="col">حالت</th><th scope="col">وضعیت</th><th scope="col">چه چیزی یاد می‌گیری؟</th><th scope="col">قانون طلایی</th></tr></thead>
<tbody>
<tr><th scope="row">۱</th><td>Copy 55% / Visual 45%</td><td>Basis نقطهٔ شروع روی Main Axis است.</td><td>ظاهر 55/45 هنوز اندازهٔ نهایی قطعی نیست.</td></tr>
<tr><th scope="row">۲</th><td>Grow 1 در برابر Grow 2</td><td>Grow فضای اضافه را تقسیم می‌کند.</td><td>Grow نسبت اندازهٔ نهایی نیست.</td></tr>
<tr><th scope="row">۳</th><td>ظرف باریک + Shrink 1</td><td>Shrink در کمبود فضا فعال می‌شود.</td><td>Min Width و محتوا هم اثر دارند.</td></tr>
<tr><th scope="row">۴</th><td>Shrink 0</td><td>ممکن است Overflow بسازد.</td><td>هر Itemی نباید از کوچک‌شدن منع شود.</td></tr>
<tr><th scope="row">۵</th><td>Copy منعطف + Visual محدود + min-width:0</td><td>قرارداد مقاوم‌تر برای Hero/TUYA.</td><td>Computed Style را بخوان.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-7-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-7-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Copy منعطف، Visual کنترل‌شده</h3>
<p>در این تمرین، فقط رفتار اندازهٔ Copy و Visual را تنظیم و تست می‌کنی. هنوز Position، Nodeها، Visual Stage positioning، Shadow/Glow، Background نهایی و Typography نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate درس ۷">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از تنظیم Basis/Grow/Shrink</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy و Visual Flex Item مستقیم Shell هستند.</td><td>Basis/Grow/Shrink روی همین دو Item بررسی می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy باید با متن واقعی کار کند و Visual نباید از Parent بیرون بزند.</td><td>Copy منعطف‌تر و Visual محدودتر طراحی می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Basis، Max Width، Min Width و Grow/Shrink دقیق.</td><td>فقط مقدار شروع تست هستند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>طول نهایی متن، اندازهٔ تصویر، Breakpoint دقیق، خروجی CSS واقعی کنترل‌های UI.</td><td>Computed Style و تست Responsive لازم است.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Itemها را انتخاب کن</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس هفت">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> تنظیم رفتار اندازهٔ دو Flex Item، نه طراحی نهایی.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → انتخاب <code dir="ltr">TUYA Copy</code> و <code dir="ltr">TUYA Visual</code> → Style/Layout → Flex item sizing controls.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">TUYA Copy</code> و <code dir="ltr">TUYA Visual</code>.</p>
<p><strong>Class فعال:</strong> Classهای همان دو Item؛ Global جدید نساز.</p>
<p><strong>Property:</strong> Basis / Grow / Shrink / Min Width / Max Width.</p>
<p><strong>نباید تغییر کند:</strong> Position، Nodeها، Shadow/Glow، Background نهایی، Typography، Button Style، Visual Stage positioning.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Copy منعطف است، Visual کنترل‌شده است، و Overflow با متن بلند بررسی شد.»</p>
</aside>

<h3>مرحلهٔ ۲ — مقدارهای شروع را به‌عنوان provisional تست کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional item sizing values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع برای Copy و Visual</caption>
<thead><tr><th scope="col">Item</th><th scope="col">Basis</th><th scope="col">Grow</th><th scope="col">Shrink</th><th scope="col">Min/Max</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">TUYA Copy</th><td><code dir="ltr">52%–55%</code> یا <code dir="ltr">18rem</code> شروع تست</td><td><code dir="ltr">1</code></td><td><code dir="ltr">1</code></td><td><code dir="ltr">min-width:0</code> در صورت نیاز</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">TUYA Visual</th><td><code dir="ltr">45%–48%</code> یا <code dir="ltr">16rem</code> شروع تست</td><td><code dir="ltr">0</code> یا محدود</td><td><code dir="ltr">1</code></td><td><code dir="ltr">max-width</code> کنترل‌شده</td><td><code dir="ltr">provisional</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — تست متن بلند</h3>
<p>برای اثبات اینکه Copy واقعاً منعطف است، این تست را انجام بده:</p>
<ol>
<li>یک متن بلندتر یا یک خط طولانی‌تر در Copy تصور یا موقتاً وارد کن.</li>
<li>عرض صفحه را کم کن.</li>
<li>بررسی کن آیا Copy می‌تواند بشکند و کوچک شود یا باعث Overflow می‌شود.</li>
<li>اگر Overflow دیدی، قبل از تغییر basis، min-width، content wrapping و اندازهٔ Visual را بررسی کن.</li>
</ol>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر Copy متن طولانی دارد و در عرض کم باعث overflow می‌شود، اولین بررسی درست چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-7">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-7-a" name="stop-question-7" type="radio" value="A"/><span>A) Shrink را کورکورانه زیاد کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-7-b" name="stop-question-7" type="radio" value="B"/><span>B) Min Width، content wrapping، basis و max-width Visual را بررسی کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-7-c" name="stop-question-7" type="radio" value="C"/><span>C) Copy را Absolute کنم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Shrink تنها عامل نیست. اگر min-width یا محتوای داخلی اجازهٔ کوچک‌شدن ندهد، Shrink به‌تنهایی Layout را نجات نمی‌دهد. Absolute هم مسئله را از Flow خارج و شکننده‌تر می‌کند.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> ظاهر Desktop را با دو عدد درصدی قطعی کنی و فکر کنی Responsive حل شده است.</p>
<p><strong>نشانه:</strong> در Mobile، ستون‌ها فشرده یا بیرون‌زده می‌شوند، یا متن Copy با Visual برخورد می‌کند.</p>
<p><strong>قاعده:</strong> Basis، Grow، Shrink، Min/Max و Gap را با هم بخوان؛ نه جداگانه.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>این قرارداد خراب را تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>قرارداد خراب‌شدهٔ Flex Itemها</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Copy:   flex-basis: 60%; flex-shrink: 0;
Visual: flex-basis: 45%; flex-shrink: 0;
Gap:    40px;

نتیجه:
- مجموع از Parent بیشتر می‌شود
- هیچ‌کدام کوتاه نمی‌آیند
- Overflow محتمل است</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-37">
<fieldset>
<legend>Checkpoint درس ۷</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-37-1" name="chk-37-1" type="checkbox"/><span>می‌توانم Basis را به‌عنوان اندازهٔ شروع روی Main Axis توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-37-2" name="chk-37-2" type="checkbox"/><span>می‌دانم Grow فقط فضای اضافه را تقسیم می‌کند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-37-3" name="chk-37-3" type="checkbox"/><span>می‌دانم Shrink فقط در کمبود فضا فعال می‌شود و min-width می‌تواند مانع آن شود.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-37-4" name="chk-37-4" type="checkbox"/><span>Copy و Visual را هنوز با عدد قطعی از Screenshot نهایی نکرده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Basis، Grow و Shrink را در یک جمله برای TUYA Copy توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> برای Search Bar شامل Input و Button بگو کدام Item باید Grow کند و کدام نباید Shrink شود، و چرا.</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Input معمولاً باید Grow کند و Button اندازهٔ کنترل‌شده‌تری داشته باشد؛ اما Button نباید آن‌قدر Shrink شود که متن یا دسترسی‌پذیری آن خراب شود.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-7-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Basis، Grow و Width را برای صفحهٔ باریک بازبینی کن</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">verified_method_provisional_values</code></p>
<p>Basis یا Width ستونی که در Desktop دو ستون می‌سازد، ممکن است در Mobile باعث فشردگی یا Overflow شود.</p>
<ul>
<li>در Mobile، Itemهای اصلی را روی Width قابل‌انطباق بررسی کن.</li>
<li>وجود <code dir="ltr">flex-grow</code>، <code dir="ltr">flex-shrink</code> و <code dir="ltr">flex-basis</code> را در Computed Style ببین.</li>
<li>مشاهدهٔ طرح Mobile به‌تنهایی عدد 100% یا auto را اثبات نمی‌کند.</li>
<li>اگر Direction به Column تغییر کرده، Basis را دوباره با Main Axis جدید بخوان.</li>
</ul>
</section>
</details>

<details class="lesson-disclosure responsive-build-test" id="lesson-7-responsive-build-test">
<summary class="lesson-disclosure-summary">
<span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Basis، Grow و Shrink در عرض‌های کوچک</span>
</summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_runtime_validation</code></p>
<p class="exercise-goal"><strong>هدف:</strong> ثابت کن که Copy با متن بلند در عرض کوچک باعث overflow نمی‌شود.</p>
<ol>
<li>Desktop را با Row و دو Item تست کن.</li>
<li>عرض را کم کن.</li>
<li>Mobile Column را بررسی کن.</li>
<li>اگر overflow دیدی، اول min-width و content wrapping را بررسی کن.</li>
<li>بعد max-width Visual و basisها را بازبینی کن.</li>
</ol>
</section>
</details>

<details aria-labelledby="lesson-7-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-7-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Shrink کار نمی‌کند</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: Copy باید کوچک شود، اما متن بلند باعث overflow می‌شود.</p>
<p>قبل از تغییر مقدار جدید، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>Direction فعلی چیست و Main Axis کدام است؟</li>
<li>Copy چه <code dir="ltr">flex-basis</code> مؤثری دارد؟</li>
<li><code dir="ltr">flex-shrink</code> چند است؟</li>
<li><code dir="ltr">min-width</code> مؤثر چیست؟</li>
<li>آیا متن امکان شکست خط دارد؟</li>
<li>Visual چه Max Width یا Basis دارد؟</li>
<li>Gap چقدر از فضا را مصرف کرده است؟</li>
</ul>
</section>
<p>نتیجهٔ درست: اول قرارداد اندازه را بخوان؛ بعد یک تغییر محدود انجام بده.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، کنار هم خواندن width، flex-basis، flex-grow، flex-shrink، min-width و max-width از خواندن یک عدد تنها قابل اعتمادتر است. در Elementor هم باید خروجی واقعی کنترل‌های UI را با Computed Style تأیید کنی.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-7-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-7-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-40">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-40-1" name="chk-40-1" type="checkbox"/><span>می‌توانم Grow، Shrink و Basis را به زبان اندازهٔ شروع، سهم رشد و توان جمع‌شدن توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-40-2" name="chk-40-2" type="checkbox"/><span>می‌توانم نقش Width، Max Width و <code dir="ltr">min-width:0</code> را در Flex Item تشخیص بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-40-3" name="chk-40-3" type="checkbox"/><span>می‌دانم flex-basis همیشه عرض نیست و روی Main Axis کار می‌کند.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-41">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-41-1" name="chk-41-1" type="checkbox"/><span>Copy را منعطف و Visual را محدود می‌کنم تا در عرض متوسط Overflow ایجاد نشود.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-41-2" name="chk-41-2" type="checkbox"/><span>با متن طولانی ثابت می‌کنم Copy می‌تواند Shrink شود و Parent را عریض نمی‌کند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-41-3" name="chk-41-3" type="checkbox"/><span>Computed Style را برای width، basis، grow، shrink، min-width و max-width بررسی می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-42">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-42-1" name="chk-42-1" type="checkbox"/><span>برای Search Bar شامل Input و Button می‌توانم بگویم کدام Item باید Grow کند و کدام نباید Shrink شود.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-7-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-7-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد ردیف Logoها را می‌سازیم و Wrap را به‌صورت واقعی تجربه می‌کنیم. هنوز Nodeها و Position نهایی Visual Stage را انجام نمی‌دهیم.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 7</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-7-completion">
<fieldset>
<legend>ثبت پایان درس 7</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-7-complete" name="lesson-7-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
