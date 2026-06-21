<article class="lesson card-surface" data-lesson="13" id="lesson-13">

<h2 class="lesson-title former-h1">درس 13 — Z-index، Overflow و Layering</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-13-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-13-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> ترتیب بصری لایه‌ها را با نقشهٔ کوچک و مستند کنترل کنی، بفهمی Z-index عدد جهانی نیست، و قبل از بالا بردن عدد، Overflow و Stacking Context را عیب‌یابی کنی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام جزئیات Stacking Context، تمام triggerهای CSS، Modal/Dropdown پیچیده، یا z-index نهایی کل سایت.</p>
<p><strong>در پایان باید بتوانی:</strong> برای Visual Stage یک Layer Map کوچک بسازی: Base/Glow/Core/Nodes. همچنین بتوانی تشخیص بدهی مشکل دیده‌نشدن Node از z-index است یا Overflow/Containing Block.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-13-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-13-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🔍 عیب‌یابی + 🛠 اجرایی محدود</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> مشکل Layering را با عددهای بزرگ حل نکن. هنرجو باید ابتدا بپرسد: «آیا عنصر در Stacking Context درست است؟ آیا Overflow آن را Clip کرده؟ آیا Position/Containing Block درست است؟»</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_layering_debug_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-13-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-13-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس ۱۲، Stage را Relative کردی و Nodeهای تستی را داخل Stage Absolute کردی. حالا باید ترتیب جلو/عقب و بریده‌شدن لایه‌ها را کنترل کنی. Layering بعد از Position می‌آید؛ نه قبل از آن.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Position / Containing Block
↓
Layering
↓
Z-index scale
↓
Overflow / Clipping
↓
Stacking Context audit</code></pre>
</figure>

<h3>مسئله</h3>
<p>گاهی Node دیده نمی‌شود. واکنش سریع معمولاً این است که <code dir="ltr">z-index:99999</code> بدهی. اما ممکن است مشکل از این‌ها باشد:</p>
<ul>
<li>Parent دارای <code dir="ltr">overflow:hidden</code> است و Node یا Glow را بریده است.</li>
<li>عنصر اصلاً Positioned نیست یا z-index روی آن اثر مورد انتظار ندارد.</li>
<li>عنصر داخل Stacking Context دیگری است و با عددهای بیرون از همان context مقایسه نمی‌شود.</li>
<li>مرجع Position اشتباه است و Node از Stage خارج شده است.</li>
</ul>

<h3>مدل کاغذها</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<p>لایه‌ها مثل چند کاغذ روی میز هستند. Z-index شمارهٔ جلو/عقب است، اما فقط داخل محدودهٔ درست معنا دارد. اگر یک کاغذ داخل پوشه‌ای باشد که زیر پوشهٔ دیگر قرار دارد، عدد بزرگ روی کاغذ داخل آن پوشه الزاماً از همه‌چیز جلوتر نمی‌آید.</p>
</section>

<h3>Z-index جدول جهانی نیست</h3>
<p>Z-index فقط در چارچوب Stacking Contextهای مربوط معنا دارد. عدد 999 داخل یک context ممکن است زیر عدد 2 در context دیگری دیده شود، اگر خود contextها ترتیب متفاوتی داشته باشند.</p>

<h3>Overflow با z-index حل نمی‌شود</h3>
<p>اگر Parent چیزی را Clip کرده باشد، z-index بیشتر معمولاً آن را از قیچی Overflow نجات نمی‌دهد. اول باید بفهمی عنصر بریده شده یا پشت عنصر دیگری رفته است.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Z-index or Overflow">
<table class="data-table educational-table edu-table">
<caption>تشخیص اولیه مشکل لایه</caption>
<thead><tr><th scope="col">نشانه</th><th scope="col">احتمال اول</th><th scope="col">اولین بررسی</th></tr></thead>
<tbody>
<tr><th scope="row">عنصر پشت عنصر دیگر است</th><td>Z-index / stacking order</td><td>Position، stacking context، DOM order</td></tr>
<tr><th scope="row">عنصر در لبهٔ Parent بریده می‌شود</th><td>Overflow / clipping</td><td>overflow روی Parentها</td></tr>
<tr><th scope="row">z-index بزرگ اثر ندارد</th><td>Stacking Context جدا</td><td>ancestorهای دارای transform/opacity/filter/position</td></tr>
<tr><th scope="row">Node دور از Stage دیده می‌شود</th><td>Containing Block اشتباه</td><td>Stage relative و جای Node در Tree</td></tr>
</tbody>
</table>
</div>

<h3>Layer Map کوچک برای TUYA</h3>
<p>به‌جای عددهای تصادفی، یک مقیاس کوچک و معنی‌دار بساز:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Stage Background / base: 0
Glow / decorative wash: 1
Core Cloud: 2
Orbit Nodes: 3
Active / Hover / Focus Node: 4
Temporary Debug Overlay: 9</code></pre>
</figure>
<p>این عددها هنوز قطعی نیستند؛ هدف یادگیری مقیاس کوچک و مستند است، نه طراحی نهایی.</p>

<h3>Overflow را کورکورانه Hidden نکن</h3>
<p><code dir="ltr">overflow:hidden</code> می‌تواند برای تمیزکردن قاب مفید باشد، اما اگر Glow، Node یا Badge باید کمی از قاب بیرون دیده شود، Hidden آن را Clip می‌کند. در Stageهای تزئینی، گاهی <code dir="ltr">visible</code> لازم است؛ در کارت‌های محتوایی، گاهی <code dir="ltr">hidden</code> لازم است. تصمیم وابسته به نقش است.</p>

<h3>قاعدهٔ این درس</h3>
<p>قبل از تغییر z-index، این ترتیب را بررسی کن: Flow/Position درست؟ Containing Block درست؟ Overflow درست؟ Stacking Context درست؟ سپس z-index کوچک و مستند.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-13.0.0" id="lesson-13-concept-reference">
<summary>📚 مرجع مفهومی کامل — Z-index، Stacking Context و Overflow</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="13" data-source-version="tuya-revised-13.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی موجود را حفظ می‌کند و آن را به Visual Stage پروژهٔ TUYA وصل می‌کند. هدف، ساختن مدل عیب‌یابی است؛ نه حفظ فهرست کامل triggerهای Stacking Context.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-13-ref-problem">
<h3 id="lesson-13-ref-problem">۱. مسئله‌ای که این مفهوم حل می‌کند</h3>
<p>یک Badge را <code dir="ltr">z-index:999999</code> می‌کنی، اما هنوز زیر Header است. یک Dropdown جلوست ولی بخشی از آن بریده می‌شود. یک Glow پشت Core باید بیرون قاب دیده شود، ولی ناپدید شده است. این‌ها نشان می‌دهند Z-index به‌تنهایی زبان کامل لایه‌ها نیست.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-13-building">
<h3 id="lesson-13-building">۲. تشبیه ساختمان‌ها و طبقه‌ها</h3>
<p>دو ساختمان کنار هم را تصور کن:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Building A         Building B
Floor 999          Floor 2</code></pre>
</figure>
<p>شمارهٔ طبقه فقط داخل همان ساختمان معنی دارد. اگر کل Building B روی سکوی جلوتر باشد، Floor 2 آن می‌تواند جلوی Floor 999 ساختمان A دیده شود. Stacking Context همین نقش ساختمان را دارد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-13-stacking-context">
<h3 id="lesson-13-stacking-context">۳. Stacking Context در حد لازم</h3>
<p>Stacking Context یک محدودهٔ مستقل برای مقایسهٔ لایه‌هاست. برخی شرایط می‌توانند context جدید بسازند، مثل Position همراه با z-index، opacity کمتر از 1، transform، filter و چند property دیگر. در این درس لازم نیست همهٔ triggerها را حفظ کنی؛ کافی است بدانی اگر z-index بزرگ اثر ندارد، شاید عنصر داخل context دیگری زندانی شده است.</p>
<p>روش عملی: در DevTools ancestorها را بررسی کن و ببین آیا transform، opacity، filter، position/z-index یا overflow باعث جداسازی و clipping شده‌اند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-13-zindex">
<h3 id="lesson-13-zindex">۴. Z-index چه زمانی اثر دارد؟</h3>
<p>Z-index معمولاً روی عناصر Positioned یا عناصر داخل contextهای خاص مثل flex/grid items با قواعد مشخص اثر می‌گذارد. اگر روی یک عنصر عادی عدد بدهی و نتیجه نگیری، اول وضعیت Position و context را بررسی کن.</p>
<p>قانون عملی برای هنرجو:</p>
<ol>
<li>آیا عنصر باید جلو/عقب شود؟</li>
<li>آیا عنصر در Stacking Context درست است؟</li>
<li>آیا عنصر Position/Layer behavior درست دارد؟</li>
<li>آیا Parent آن را با Overflow قطع نمی‌کند؟</li>
<li>آیا عدد کوچک و مستند کافی است؟</li>
</ol>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-13-overflow">
<h3 id="lesson-13-overflow">۵. Overflow و Clipping</h3>
<p>Overflow تعیین می‌کند محتوایی که از Box بیرون می‌زند چگونه رفتار کند:</p>
<ul>
<li><code dir="ltr">visible</code>: بیرون‌زدگی دیده می‌شود.</li>
<li><code dir="ltr">hidden</code>: بیرون‌زدگی بریده می‌شود.</li>
<li><code dir="ltr">auto</code>: در صورت نیاز scroll می‌آید.</li>
<li><code dir="ltr">clip</code>: مشابه clipping بدون scroll، بسته به پشتیبانی و context.</li>
</ul>
<p>برای Glow و Nodeهای تزئینی داخل Stage، Overflow تصمیم حساسی است. Hidden ممکن است Visual را تمیز کند، اما ممکن است Glow را ببرد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-13-tuya-layer-map">
<h3 id="lesson-13-tuya-layer-map">۶. Layer Map پیشنهادی TUYA</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA layer map">
<table class="data-table educational-table edu-table">
<caption>Layer Map کوچک و مستند</caption>
<thead><tr><th scope="col">لایه</th><th scope="col">نقش</th><th scope="col">z-index شروع</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Stage Base</th><td>قاب و پس‌زمینهٔ Stage</td><td><code dir="ltr">0</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Glow</th><td>نور/تزئین پشت Core</td><td><code dir="ltr">1</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Core Cloud</th><td>عنصر مرکزی</td><td><code dir="ltr">2</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Orbit Nodes</th><td>آیتم‌های شناور اطراف Core</td><td><code dir="ltr">3</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Active Node / Focus</th><td>حالت تعاملی یا تمرکز</td><td><code dir="ltr">4</code></td><td><code dir="ltr">unknown_until_interaction</code></td></tr>
<tr><th scope="row">Debug Overlay</th><td>فقط برای تست</td><td><code dir="ltr">9</code></td><td><code dir="ltr">temporary</code></td></tr>
</tbody>
</table>
</div>
<p>از <code dir="ltr">99999</code> استفاده نکن مگر برای Debug موقت و حذف‌شدنی. در Design System، اعداد باید معنا داشته باشند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-13-overflow-contract">
<h3 id="lesson-13-overflow-contract">۷. قرارداد Overflow در TUYA</h3>
<ul>
<li><strong>Visual Stage:</strong> اگر Glow/Node باید کمی بیرون دیده شود، <code dir="ltr">visible</code> را بررسی کن.</li>
<li><strong>Cardهای محتوایی:</strong> اگر تصویر باید گوشه‌های گرد را رعایت کند، <code dir="ltr">hidden</code> ممکن است درست باشد.</li>
<li><strong>Page/Shell اصلی:</strong> Hidden کورکورانه ممکن است Dropdown، Focus outline یا Glow را ببرد.</li>
<li><strong>Debug:</strong> اگر چیزی ناپدید شد، موقتاً overflow ancestorها را visible کن و علت را پیدا کن.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-13-focus">
<h3 id="lesson-13-focus">۸. Focus و Accessibility</h3>
<p>Overflow Hidden می‌تواند outline یا focus ring را هم ببرد. اگر یک عنصر تعاملی درون قاب است، فقط ظاهر Desktop را نبین؛ با keyboard focus هم بررسی کن. Focus ring بخشی از دسترسی‌پذیری است، نه تزئین اضافه.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-13-debug">
<h3 id="lesson-13-debug">۹. Debug Layering</h3>
<p>وقتی چیزی جلو/عقب یا بریده است، این ترتیب را رعایت کن:</p>
<ol>
<li>عنصر در Tree کجاست؟</li>
<li>Position و Containing Block درست است؟</li>
<li>Parentها Overflow چه دارند؟</li>
<li>آیا ancestorها Stacking Context ساخته‌اند؟</li>
<li>آیا z-index داخل context درست معنا دارد؟</li>
<li>آیا DOM order بدون z-index هم مشکل را توضیح می‌دهد؟</li>
<li>آیا عدد کوچک و مستند کافی است؟</li>
</ol>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-13-traps">
<h3 id="lesson-13-traps">۱۰. اشتباهات رایج</h3>
<ul>
<li>عددهای تصادفی بزرگ مثل <code dir="ltr">999999</code>.</li>
<li>تغییر z-index قبل از بررسی Overflow.</li>
<li>Hidden کردن Parent و بریدن Glow/Focus ring.</li>
<li>فرض اینکه z-index در کل صفحه یک جدول جهانی دارد.</li>
<li>ساختن Stacking Context ناخواسته با transform/opacity/filter.</li>
<li>دادن z-index به عنصر اشتباه به‌جای Parent/Child درست.</li>
<li>حل‌کردن مشکل Containing Block با z-index.</li>
<li>فراموش‌کردن DOM order و focus state.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-13-golden">
<h3 id="lesson-13-golden">۱۱. قوانین طلایی</h3>
<ul>
<li><strong>Z-index عدد جهانی نیست؛ داخل Stacking Context معنا دارد.</strong></li>
<li><strong>Overflow با z-index حل نمی‌شود.</strong></li>
<li><strong>عددهای لایه را کوچک، معنی‌دار و مستند نگه دار.</strong></li>
<li><strong>قبل از z-index، Position و Containing Block را بررسی کن.</strong></li>
<li><strong>Hidden فقط وقتی درست است که بیرون‌زدگی واقعاً نباید دیده شود.</strong></li>
<li><strong>Focus ring و Dropdown را با overflow:hidden کورکورانه نبر.</strong></li>
<li><strong>Layer Map را برای Stage بساز، نه برای کل دنیا.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>رفتار Z-index، Stacking Context و Overflow بر پایهٔ CSS و رفتار مرورگر نوشته شده است. عددهای TUYA تا پیش از Stage واقعی، Interaction و Breakpoint Validation قطعی نیستند.</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/z-index" rel="noopener noreferrer" target="_blank">MDN — z-index</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Understanding_z-index/Stacking_context" rel="noopener noreferrer" target="_blank">MDN — Stacking context</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow" rel="noopener noreferrer" target="_blank">MDN — overflow</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-13-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-13-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Z-index، Overflow و Layer Scale</span>
</summary>
<section aria-labelledby="lesson-13-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Z-index عدد بدون واحد است؛ Overflow keyword است؛ اما هر دو فقط در context درست معنی دارند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۳" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Z-index</th><td>number / auto</td><td>Stacking Context</td><td>عدد جهانی فرض شود.</td></tr>
<tr><th scope="row">Overflow</th><td>visible / hidden / auto / clip</td><td>Parent box</td><td>Glow یا focus ring بریده شود.</td></tr>
<tr><th scope="row">Opacity</th><td>0 تا 1</td><td>Element و descendants</td><td>Stacking Context ناخواسته بسازد.</td></tr>
<tr><th scope="row">Transform</th><td>function</td><td>Element box</td><td>Context/Containing Block رفتار را پیچیده کند.</td></tr>
<tr><th scope="row">Layer Token</th><td>semantic number</td><td>Design System</td><td>توکن زودهنگام بدون pattern واقعی ساخته شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Glow z=1 و Core z=2 داخل Stage هستند، Core جلوتر است. اما اگر کل Stage زیر یک overlay دیگر باشد، افزایش z داخلی همیشه overlay بیرونی را شکست نمی‌دهد.</p></section>
<section><h3>📱 در Responsive</h3><p>در Mobile، Overflow و اندازهٔ Stage تغییر می‌کند. Glow و Node ممکن است در عرض کوچک Clip شوند؛ فقط z-index را تغییر نده.</p></section>
<section><h3>🔬 در DevTools</h3><p>Computed z-index، overflow ancestorها، stacking context triggers و DOM order را با هم بررسی کن.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-13-layer-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — z-index یا Overflow؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر حالت را پیش‌بینی کن، بعد نتیجه را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Step Through Layering">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ حالت‌های Layering</caption>
<thead><tr><th scope="col">حالت</th><th scope="col">وضعیت</th><th scope="col">چه چیزی یاد می‌گیری؟</th><th scope="col">قانون طلایی</th></tr></thead>
<tbody>
<tr><th scope="row">۱</th><td>Glow پشت Core، overflow visible</td><td>Glow دیده می‌شود.</td><td>بیرون‌زدگی مجاز را Clip نکن.</td></tr>
<tr><th scope="row">۲</th><td>Glow پشت Core، parent hidden</td><td>Glow در لبه‌ها بریده می‌شود.</td><td>Overflow را قبل از z-index بررسی کن.</td></tr>
<tr><th scope="row">۳</th><td>Node z=999 داخل context زیرین</td><td>ممکن است هنوز زیر context بیرونی باشد.</td><td>z-index جهانی نیست.</td></tr>
<tr><th scope="row">۴</th><td>Core و Node بدون Layer Map</td><td>عددها تصادفی و نگهداری سخت می‌شوند.</td><td>مقیاس کوچک بساز.</td></tr>
<tr><th scope="row">۵</th><td>Focus ring داخل parent hidden</td><td>دسترسی‌پذیری آسیب می‌بیند.</td><td>Focus state را هم تست کن.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-13-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-13-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Layer Map کوچک برای Visual Stage</h3>
<p>در این تمرین فقط Layer Map و Overflow را تست می‌کنی. هنوز Shadow/Glow نهایی، Interaction نهایی، Animation یا z-index نهایی کل سایت نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 13">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از z-index</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Visual Stage مرجع Nodeهاست.</td><td>Layer Map داخل Stage ساخته می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Overflow می‌تواند Glow/Node را Clip کند.</td><td>قبل از z-index، overflow بررسی شود.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>عددهای Layer Map.</td><td>فقط شروع تست‌اند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Interaction، hover/focus، z-index نهایی، shadow/glow نهایی.</td><td>در این درس قطعی نمی‌شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط لایه‌های Stage را فهرست کن</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس سیزده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ساخت Layer Map کوچک، نه حل همهٔ Layerهای سایت.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → <code dir="ltr">TUYA Visual</code> → <code dir="ltr">Visual Stage</code>.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">Visual Stage</code>، Core، Glow و Nodeهای تستی.</p>
<p><strong>Class فعال:</strong> Classهای محلی Stage/Node؛ Global/Token نهایی نساز.</p>
<p><strong>Property:</strong> z-index کوچک، overflow، position check.</p>
<p><strong>نباید تغییر کند:</strong> Copy، Heading، Paragraph، Logo Strip، Shell Flex، Typography، Position نهایی همهٔ Nodeها، Shadow/Glow نهایی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Layer Map کوچک Stage ثبت شد و مشکل لایه قبل از z-index با Overflow/Context بررسی شد.»</p>
</aside>

<h3>مرحلهٔ ۲ — Layer Map شروع را وارد کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional layer values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع Layering</caption>
<thead><tr><th scope="col">لایه</th><th scope="col">z-index شروع</th><th scope="col">وضعیت</th><th scope="col">یادداشت</th></tr></thead>
<tbody>
<tr><th scope="row">Stage Base</th><td><code dir="ltr">0</code></td><td><code dir="ltr">provisional</code></td><td>قاب و پس‌زمینهٔ Stage.</td></tr>
<tr><th scope="row">Glow</th><td><code dir="ltr">1</code></td><td><code dir="ltr">provisional</code></td><td>پشت Core، احتمال بیرون‌زدگی دارد.</td></tr>
<tr><th scope="row">Core Cloud</th><td><code dir="ltr">2</code></td><td><code dir="ltr">provisional</code></td><td>عنصر مرکزی.</td></tr>
<tr><th scope="row">Orbit Node</th><td><code dir="ltr">3</code></td><td><code dir="ltr">provisional</code></td><td>جلوتر از Core در تست.</td></tr>
<tr><th scope="row">Debug Overlay</th><td><code dir="ltr">9</code></td><td><code dir="ltr">temporary</code></td><td>فقط برای تست؛ در نهایی حذف شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — تست Overflow</h3>
<ol>
<li>یک Glow یا Node را طوری تصور/تست کن که کمی از Stage بیرون بزند.</li>
<li>Overflow Stage یا Parent را موقتاً <code dir="ltr">hidden</code> کن.</li>
<li>ببین آیا Glow/Node بریده می‌شود.</li>
<li>Overflow را برگردان و نتیجه را ثبت کن.</li>
<li>قبل از تغییر z-index بگو مشکل از layer است یا clipping.</li>
</ol>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر Glow در لبهٔ Stage بریده شده، اولین بررسی درست چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-13">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-13-a" name="stop-question-13" type="radio" value="A"/><span>A) z-index را به 999999 افزایش بدهم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-13-b" name="stop-question-13" type="radio" value="B"/><span>B) Overflow Parentها و clipping را بررسی کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-13-c" name="stop-question-13" type="radio" value="C"/><span>C) Copy را Absolute کنم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> اگر چیزی در لبهٔ Parent بریده شده، مشکل احتمالاً Overflow است. Z-index بالاتر معمولاً از clipping نجاتش نمی‌دهد.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> هر مشکل جلو/عقب یا دیده‌نشدن را با z-index بزرگ حل کنی.</p>
<p><strong>نشانه:</strong> عددها به 999، 9999 و 99999 می‌رسند اما رفتار هنوز غیرقابل پیش‌بینی است.</p>
<p><strong>قاعده:</strong> Layer Map کوچک + بررسی Overflow + بررسی Stacking Context.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<figure class="visual-figure ascii-figure">
<figcaption>Layering خراب</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code">Stage overflow:hidden;
Glow z-index:99999;

نتیجه:
- Glow هنوز بریده می‌شود
- چون مشکل clipping است، نه جلو/عقب بودن</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-73">
<fieldset>
<legend>Checkpoint درس ۱۳</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-73-1" name="chk-73-1" type="checkbox"/><span>برای Visual Stage یک Layer Map کوچک نوشته‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-73-2" name="chk-73-2" type="checkbox"/><span>از عددهای بزرگ تصادفی استفاده نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-73-3" name="chk-73-3" type="checkbox"/><span>قبل از تغییر z-index، Overflow را بررسی کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-73-4" name="chk-73-4" type="checkbox"/><span>می‌دانم z-index داخل Stacking Context معنا دارد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-73-5" name="chk-73-5" type="checkbox"/><span>z-index نهایی کل سایت را هنوز قطعی نکرده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> فرق مشکل z-index و مشکل Overflow را با مثال Glow توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر Dropdown زیر Header می‌ماند ولی z-index بزرگ اثر ندارد، چه چیزهایی را بررسی می‌کنی؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید Stacking Context، overflow ancestorها، position، DOM order و عددهای کوچک/مستند را بررسی کند؛ نه اینکه مستقیم عدد را بزرگ‌تر کند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-13-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Overflow و Layering در Stage باریک</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_runtime_validation</code></p>
<ul>
<li>Stage را در Desktop، Tablet و Mobile بررسی کن.</li>
<li>Glow و Nodeها ممکن است در Mobile بیشتر Clip شوند.</li>
<li>اگر Node دیده نمی‌شود، اول Overflow و Containing Block را بررسی کن.</li>
<li>Focus state و hover/active state را در صورت تعاملی بودن Nodeها بعداً بررسی کن.</li>
<li>z-indexهای Stage را به مقیاس کوچک محدود نگه دار.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-13-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-13-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — z-index بزرگ اثر ندارد</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: یک Node با <code dir="ltr">z-index:999</code> هنوز زیر Core دیده می‌شود یا بخشی از آن ناپدید است.</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا Node و Core در یک Stacking Context هستند؟</li>
<li>آیا Node واقعاً Positioned است؟</li>
<li>آیا Parent یا ancestor دارای <code dir="ltr">overflow:hidden</code> است؟</li>
<li>آیا ancestor دارای transform/opacity/filter است؟</li>
<li>آیا Node داخل Stage است یا sibling بیرونی؟</li>
<li>آیا Core خودش context جدید ساخته است؟</li>
<li>آیا DOM order بدون z-index مسئله را توضیح می‌دهد؟</li>
</ul>
</section>
<p>نتیجهٔ درست: context و clipping را پیدا کن؛ سپس عدد کوچک و مستند بده.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، computed z-index، overflow ancestorها، stacking context triggers و bounding boxes را کنار هم ببین. اگر عنصر Clip شده، z-index بیشتر راه‌حل نیست.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-13-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-13-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-76">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-76-1" name="chk-76-1" type="checkbox"/><span>می‌دانم z-index عدد جهانی نیست و داخل Stacking Context معنا دارد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-76-2" name="chk-76-2" type="checkbox"/><span>می‌توانم Overflow visible/hidden/auto را توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-76-3" name="chk-76-3" type="checkbox"/><span>می‌دانم مشکل clipping با z-index حل نمی‌شود.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-77">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-77-1" name="chk-77-1" type="checkbox"/><span>برای Visual Stage یک Layer Map کوچک با عددهای معنی‌دار می‌سازم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-77-2" name="chk-77-2" type="checkbox"/><span>قبل از تغییر z-index، Overflow و Stacking Context را بررسی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-77-3" name="chk-77-3" type="checkbox"/><span>Hidden را فقط وقتی استفاده می‌کنم که بیرون‌زدگی واقعاً نباید دیده شود.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-78">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-78-1" name="chk-78-1" type="checkbox"/><span>برای Dropdown یا Modal می‌توانم بررسی کنم چرا z-index بزرگ به‌تنهایی کافی نیست.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-13-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Layer tokens</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>این Layer number باید direct literal بماند یا Token شود؟</li>
<li>Layer Map مخصوص Stage است یا در کل سایت reuse دارد؟</li>
<li>حالت Active/Focus واقعاً نیاز به لایهٔ جدا دارد؟</li>
<li>آیا Overflow decision باید در Class بماند یا Wrapper جدا لازم است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — فعلاً Layerها local/provisional هستند. تا وقتی pattern واقعی Stage، Node و Interaction ثابت نشده، Layer Token سراسری نساز.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-13-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-13-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا Stage، Node تستی، Layer Map کوچک و Overflow audit انجام شده‌اند؛ اما Shadow/Glow، Interaction و z-index نهایی هنوز قطعی نیستند.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 13</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-13-completion">
<fieldset>
<legend>ثبت پایان درس 13</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-13-complete" name="lesson-13-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
