<article class="lesson card-surface" data-lesson="8" id="lesson-8">

<h2 class="lesson-title former-h1">درس 8 — Wrap و ساخت Logo Strip</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-8-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-8-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> برای آیتم‌های تکراری مثل Logoها، Parent را Flex/Wrap کنی تا در عرض کم به خط بعد بروند، بدون Overflow و بدون Marginهای تکی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Grid کامل، ساخت Component نهایی Logoها، Responsive نهایی، یا Style نهایی برند.</p>
<p><strong>در پایان باید بتوانی:</strong> یک Logo Strip داخل Copy Area بسازی که در Desktop یک ردیف منظم داشته باشد و در عرض کمتر، Logoها را با Wrap به خط بعد ببرد.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-8-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-8-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🛠 اجرایی + 🔍 عیب‌یابی + 📱 Responsive-aware</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۱۵–۲۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۰–۳۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> Wrap را با عرض واقعی و آیتم‌های تکراری آموزش بده. هنرجو نباید با Hide کردن Logoها یا Marginهای تکی، رفتار Responsive را پنهان کند.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_wrap_logo_strip_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-8-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-8-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس‌های ۵ تا ۷، Shell و دو ستون اصلی را با Flex چیدی و اندازهٔ Copy/Visual را کنترل کردی. حالا در خود Copy Area، یک گروه تکراری داریم: Logo Strip. این گروه باید با همان منطق Flex کار کند، اما در مقیاس کوچک‌تر.</p>
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
Flex Item Sizing
↓
Wrap / Repeating Items / Logo Strip</code></pre>
</figure>

<h3>مسئله</h3>
<p>چهار یا چند Logo در Desktop ممکن است در یک ردیف جا شوند؛ اما در عرض کمتر، اگر Wrap خاموش باشد یا اندازهٔ Logoها درست کنترل نشده باشد، یکی از این اتفاق‌ها می‌افتد:</p>
<ul>
<li>Logoها از Parent بیرون می‌زنند.</li>
<li>خیلی کوچک و ناخوانا می‌شوند.</li>
<li>با متن یا دکمه‌ها برخورد می‌کنند.</li>
<li>بخشی از Logoها مخفی می‌شود.</li>
</ul>

<h3>Wrap چه کار می‌کند؟</h3>
<p><code dir="ltr">flex-wrap</code> فقط به Flex Itemها اجازه می‌دهد وقتی در یک خط جا نمی‌شوند، خط جدید بسازند. Wrap به‌تنهایی عرض Logo، تعداد ستون، اندازهٔ تصویر یا کیفیت Responsive را تعیین نمی‌کند.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">nowrap:
[A][B][C][D]------------------→

wrap:
[A][B]
[C][D]</code></pre>
</figure>

<h3>Wrap با Hide فرق دارد</h3>
<p>Wrap ساختار و محتوا را حفظ می‌کند؛ Hide محتوا را حذف یا پنهان می‌کند. Responsive خوب معمولاً اول از Wrap، Gap، اندازهٔ Item و اندازهٔ تصویر کمک می‌گیرد. پنهان‌کردن Logoها فقط وقتی قابل دفاع است که از نظر محتوا، دسترسی‌پذیری و هدف صفحه دلیل روشن داشته باشد.</p>

<h3>Wrap خودش اندازهٔ Item را حل نمی‌کند</h3>
<p>اگر Logoها بیش از حد بزرگ باشند، Wrap فقط آن‌ها را به خط بعد می‌برد؛ ولی ممکن است باز هم ظاهر شلوغ بماند. بنابراین ترتیب فکرکردن این است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">عرض Parent
↓
Basis/Width Logo Itemها
↓
اندازهٔ Image داخل هر Item
↓
Gap و Padding
↓
Shrink و Min/Max Size
↓
Wrap
↓
Alignment بین Lineها</code></pre>
</figure>

<h3>align-items با align-content فرق دارد</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="align-items vs align-content">
<table class="data-table educational-table edu-table">
<caption>تفاوت Align Items و Align Content در Wrap</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">اثر</th><th scope="col">چه زمانی مهم‌تر می‌شود؟</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">align-items</code></th><td>Itemها را داخل هر Flex Line روی Cross Axis تراز می‌کند.</td><td>وقتی ارتفاع Logoها یا ظرف‌هایشان متفاوت است.</td></tr>
<tr><th scope="row"><code dir="ltr">align-content</code></th><td>خود Flex Lineها را در فضای اضافهٔ Cross Axis توزیع می‌کند.</td><td>وقتی چند Line داری و Container فضای عمودی/عرضی اضافه دارد.</td></tr>
</tbody>
</table>
</div>

<h3>Logo Strip در Tree کجا قرار می‌گیرد؟</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Copy
├── Eyebrow
├── Heading
├── Paragraph
├── Feature List
├── Actions
└── Logo Strip  ← Flex Container کوچک‌تر
    ├── Logo Item
    ├── Logo Item
    ├── Logo Item
    └── Logo Item</code></pre>
</figure>
<p>Logo Strip داخل Copy Area است، نه داخل Visual Stage. Logoها محتوا/اعتمادساز هستند؛ پس باید در Flow بمانند و با متن و دکمه‌ها هم‌رفتار Responsive داشته باشند.</p>

<h3>قاعدهٔ این درس</h3>
<p>برای Logo Strip، Parent را Flex Row + Wrap کن، فاصله را با Gap بده، اندازهٔ Logoها را با Max Width/Height کنترل کن، و هیچ Logo را فقط برای جا شدن مخفی نکن.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-8.0.0" id="lesson-8-concept-reference">
<summary>📚 مرجع مفهومی کامل — Wrap؛ وقتی یک ردیف دیگر جا ندارد</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="8" data-source-version="tuya-revised-8.0.0">

<p class="concept-reference-lead">این مرجع، هستهٔ مفهومی درس Wrap را حفظ می‌کند و آن را به Logo Strip پروژهٔ TUYA وصل می‌کند. هدف ساختن Grid کامل نیست؛ هدف اجازه‌دادن به آیتم‌های تکراری برای شکستن خط، بدون از دست دادن Flow است.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-8-ref-problem">
<h3 id="lesson-8-ref-problem">۱. مسئله‌ای که Wrap حل می‌کند</h3>
<p>یک Flex Container را تصور کن که چند آیتم تکراری دارد. در صفحهٔ بزرگ، همه کنار هم جا می‌شوند. با کم‌شدن عرض، مرورگر باید تصمیم بگیرد:</p>
<ul>
<li>Itemها را کوچک کند؛</li>
<li>آن‌ها را از کادر بیرون بزند؛</li>
<li>یا بخشی از Itemها را به خط بعد ببرد.</li>
</ul>
<p><code dir="ltr">flex-wrap</code> به سؤال سوم پاسخ می‌دهد: آیا Flex Itemها اجازه دارند بیش از یک Flex Line بسازند؟</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-8-shop-analogy">
<h3 id="lesson-8-shop-analogy">۲. تشبیه صندوق فروشگاه</h3>
<p>فرض کن فروشگاه یک صف صندوق دارد:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">[نفر ۱][نفر ۲][نفر ۳][نفر ۴][نفر ۵]</code></pre>
</figure>
<p>اگر سالن کم‌عرض شود و قانون <code dir="ltr">nowrap</code> باشد، صف از سالن بیرون می‌زند یا افراد فشرده می‌شوند. با Wrap، وقتی صف اول پر شد، خط دوم تشکیل می‌شود:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">[نفر ۱][نفر ۲][نفر ۳]
[نفر ۴][نفر ۵]</code></pre>
</figure>
<p>اما بازشدن خط دوم تعیین نمی‌کند هر نفر چقدر جا بگیرد. اندازهٔ هر Item همچنان از Basis/Width، Min/Max Size، Gap و محتوا می‌آید.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-8-flex-vs-grid">
<h3 id="lesson-8-flex-vs-grid">۳. Wrap با Grid فرق دارد</h3>
<p>Flexbox یک مدل یک‌بعدی است. هر Flex Line روی Main Axis کار می‌کند. Wrap اجازه می‌دهد خط‌های بیشتری ساخته شوند، اما آن خط‌ها مثل یک شبکهٔ از پیش طراحی‌شده نیستند.</p>
<p>اگر به کنترل دقیق ردیف و ستون نیاز داری، Grid ممکن است مناسب‌تر باشد. اما برای Logo Strip ساده که فقط باید چند لوگو کنار هم بیایند و در عرض کم بشکنند، Flex Wrap نقطهٔ شروع مناسب‌تری است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-8-order-of-thinking">
<h3 id="lesson-8-order-of-thinking">۴. ترتیب فکرکردن در Wrap</h3>
<ol>
<li>Parent واقعی Logoها کدام است؟</li>
<li>Logoها Child مستقیم آن Parent هستند؟</li>
<li>Display Parent واقعاً Flex است؟</li>
<li>Direction چیست؟ معمولاً Row.</li>
<li>Wrap روشن است؟</li>
<li>Gap چقدر فضا مصرف می‌کند؟</li>
<li>هر Logo Item چه basis/width/min/max دارد؟</li>
<li>Image داخل Logo Item چه max-width/max-height دارد؟</li>
<li>چند Line تشکیل می‌شود و align-content نیاز داری یا نه؟</li>
</ol>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-8-logo-size">
<h3 id="lesson-8-logo-size">۵. Logo فقط Image نیست؛ Logo Item هم داریم</h3>
<p>در یک Logo Strip مقاوم، معمولاً بین خود Image و Item/Wrapper تفاوت می‌گذاری:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Logo Strip  ← Flex Container
└── Logo Item  ← Flex Item
    └── Image  ← تصویر لوگو</code></pre>
</figure>
<p>Logo Item مسئول فضای هر لوگو در Flex است. Image مسئول خود تصویر است و باید با max-width/max-height کنترل شود تا از Item بیرون نزند یا بی‌نظم نشود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-8-accessibility">
<h3 id="lesson-8-accessibility">۶. Logoها محتوا هستند یا تزئین؟</h3>
<p>اگر Logoها نشان‌دهندهٔ برند، همکار، مشتری یا اعتمادسازی‌اند، معمولاً محتوای معنی‌دار هستند و باید متن جایگزین مناسب داشته باشند. اگر فقط تزئینی‌اند، باید به‌عنوان تزئینی مدیریت شوند. در این درس تصمیم محتوایی را قطعی نمی‌کنیم؛ فقط می‌گوییم قبل از حذف یا Hide کردن Logoها، نقش محتوایی آن‌ها را مشخص کن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-8-align-content">
<h3 id="lesson-8-align-content">۷. align-content فقط وقتی چند Line و فضای اضافه داری معنی جدی دارد</h3>
<p>وقتی فقط یک خط Logo داری، <code dir="ltr">align-content</code> معمولاً اثر قابل توجهی ندارد. وقتی Wrap باعث چند Line شد و Container در Cross Axis فضای اضافه داشت، align-content جای Lineها را نسبت به هم کنترل می‌کند.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Container بلند
┌─────────────────────────┐
│ [A] [B] [C]             │ ← Line 1
│                         │
│ [D] [E]                 │ ← Line 2
└─────────────────────────┘</code></pre>
</figure>
<p><code dir="ltr">align-items</code> Itemها را در هر خط می‌بیند؛ <code dir="ltr">align-content</code> خود خط‌ها را در کل Container می‌بیند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-8-tuya-contract">
<h3 id="lesson-8-tuya-contract">۸. قرارداد TUYA برای Logo Strip</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Logo Strip:
- Parent: Flex Container
- Direction: Row
- Wrap: Wrap
- Gap: 12px تا 20px provisional
- Logo Item: اندازهٔ کنترل‌شده، بدون Marginهای تکی
- Image: max-width / max-height کنترل‌شده
- Responsive: در عرض کم به خط بعد برود، نه overflow و نه hide</code></pre>
</figure>
<p>این قرارداد هنوز نهایی نیست. باید با تعداد واقعی Logoها، اندازهٔ فایل‌های SVG/PNG، عرض Copy Area و Breakpoint واقعی تست شود.</p>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-8-golden">
<h3 id="lesson-8-golden">۹. قوانین طلایی</h3>
<ul>
<li><strong>Wrap فقط اجازهٔ خط جدید می‌دهد؛ اندازهٔ Item را حل نمی‌کند.</strong></li>
<li><strong>Logoها باید Child مستقیم Logo Strip باشند تا Wrap روی آن‌ها اثر کند.</strong></li>
<li><strong>Gap برای فاصلهٔ بین Logoها بهتر از Marginهای تکی است.</strong></li>
<li><strong>Hide کردن Logoها راه‌حل اول Responsive نیست.</strong></li>
<li><strong>align-content فقط با چند Line و فضای اضافه معنی جدی دارد.</strong></li>
<li><strong>Logo Item و Image را جدا فکر کن.</strong></li>
<li><strong>نقش محتوایی Logoها را قبل از حذف یا تزئینی فرض کردن مشخص کن.</strong></li>
<li><strong>مقدارهای Gap و اندازهٔ Logoها تا قبل از تست واقعی provisional هستند.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفهوم Wrap، Flex Line، Gap، align-items و align-content بر پایهٔ رفتار CSS Flexbox و مستندات Elementor دربارهٔ Flexbox نوشته شده است. تصمیم‌های محتوایی/دسترسی‌پذیری Logoها باید با هدف صفحه و محتوای واقعی سنجیده شود.</p>
<ul>
<li><a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap" rel="noopener noreferrer" target="_blank">MDN — flex-wrap</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-content" rel="noopener noreferrer" target="_blank">MDN — align-content</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-8-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-8-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Wrap، Gap، Logo Item و Image Size</span>
</summary>
<section aria-labelledby="lesson-8-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Wrap خودش واحد ندارد؛ keyword است. Gap و اندازهٔ Logoها واحد طول دارند و باید نسبت به Parent و تعداد آیتم‌ها تست شوند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۸" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Flex Wrap</th><td>keyword: nowrap / wrap</td><td>Flex Container</td><td>فکر کنی اندازهٔ Logo را هم حل می‌کند.</td></tr>
<tr><th scope="row">Gap</th><td>px / rem / clamp</td><td>فاصلهٔ بین Itemها</td><td>با margin تکی روی هر Logo قاطی شود.</td></tr>
<tr><th scope="row">Logo Item Basis/Width</th><td>px / rem / auto</td><td>فضای Parent و اندازهٔ Logo</td><td>بیش از حد ثابت شود و Wrap شلوغ بسازد.</td></tr>
<tr><th scope="row">Image Max Width</th><td>px / rem / %</td><td>داخل Logo Item</td><td>Image از Item بیرون بزند یا نسبتش خراب شود.</td></tr>
<tr><th scope="row">Align Content</th><td>keyword</td><td>چند Flex Line و فضای Cross Axis</td><td>در یک Line انتظار اثر داشته باشی.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر چهار Logo هرکدام 120px باشند و سه Gap برابر 16px داشته باشی، حداقل عرض مفید یک‌خطی حدود 528px است. اگر Copy Area کمتر از این شود، یا باید Logoها کوچک شوند یا Wrap رخ دهد.</p></section>
<section><h3>📱 در Responsive</h3><p>Wrap در Mobile باید باعث خط جدید شود، نه مخفی‌کردن محتوا. اندازهٔ Logoها را در عرض‌های واقعی Copy Area تست کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>Flex overlay می‌تواند خط‌های Wrap، Gap و اندازهٔ Itemها را نشان دهد. Computed Style برای flex-wrap، gap، width/max-width Image و اندازهٔ Itemها مفید است.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-8-wrap-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — از nowrap تا wrap</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر حالت را پیش‌بینی کن، بعد نتیجه را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Step Through Wrap">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ حالت‌های Wrap</caption>
<thead><tr><th scope="col">حالت</th><th scope="col">وضعیت</th><th scope="col">چه چیزی یاد می‌گیری؟</th><th scope="col">قانون طلایی</th></tr></thead>
<tbody>
<tr><th scope="row">۱</th><td>nowrap + Logoهای زیاد</td><td>Overflow یا فشردگی رخ می‌دهد.</td><td>یک خط همیشه کافی نیست.</td></tr>
<tr><th scope="row">۲</th><td>wrap روشن</td><td>Logoها اجازهٔ خط جدید دارند.</td><td>Wrap فقط خط جدید می‌دهد.</td></tr>
<tr><th scope="row">۳</th><td>wrap + Gap زیاد</td><td>ممکن است تعداد Logoهای هر خط کمتر شود.</td><td>Gap هم فضا مصرف می‌کند.</td></tr>
<tr><th scope="row">۴</th><td>wrap + Image بدون max-width</td><td>Image ممکن است Item را بزرگ کند.</td><td>Logo Item و Image را جدا کنترل کن.</td></tr>
<tr><th scope="row">۵</th><td>چند Line + align-content</td><td>Lineها در Cross Axis توزیع می‌شوند.</td><td>align-content با چند Line معنی جدی دارد.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-8-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-8-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Logo Strip داخل Copy Area</h3>
<p>در این تمرین، فقط Logo Strip را داخل Copy Area می‌سازی. هنوز Grid، Component نهایی Logo، Animation، Shadow، Glow، Visual Stage یا Nodeها نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate درس ۸">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از ساخت Logo Strip</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Logo Strip بخشی از Copy Area است.</td><td>آن را داخل TUYA Copy بساز.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Logoها آیتم‌های تکراری هستند.</td><td>Parent آن‌ها می‌تواند Flex Row + Wrap باشد.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>تعداد نهایی Logoها، Gap، max-width و ترتیب.</td><td>با محتوای واقعی تست می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>نقش محتوایی یا تزئینی هر Logo، فایل واقعی SVG/PNG، alt text نهایی.</td><td>قبل از تصمیم نهایی باید روشن شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Parent Logo Strip را بساز</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس هشت">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ساخت Parent برای Logoهای تکراری، نه طراحی نهایی.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → داخل <code dir="ltr">TUYA Copy</code> → Add Container/Div برای <code dir="ltr">Logo Strip</code>.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">TUYA Logo Strip</code> و Logo Itemهای داخل آن.</p>
<p><strong>Class فعال:</strong> Class محلی Logo Strip؛ Global جدید نساز مگر reuse واقعی ثابت شود.</p>
<p><strong>Property:</strong> Display / Direction / Wrap / Gap / Image max size.</p>
<p><strong>نباید تغییر کند:</strong> Shell sizing، Copy/Visual basis، Position، Nodeها، Shadow/Glow، Background نهایی، Typography اصلی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Logo Strip داخل Copy Area ساخته شد، Logoها Child مستقیم آن هستند، و Wrap روشن است.»</p>
</aside>

<h3>مرحلهٔ ۲ — مقدارهای شروع را تست کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional logo strip values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع Logo Strip</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">مقدار شروع</th><th scope="col">وضعیت</th><th scope="col">یادداشت</th></tr></thead>
<tbody>
<tr><th scope="row">Display</th><td><code dir="ltr">Flex</code></td><td><code dir="ltr">confirmed_for_repeating_items</code></td><td>برای Logoهای تکراری در یک ردیف.</td></tr>
<tr><th scope="row">Direction</th><td><code dir="ltr">Row</code></td><td><code dir="ltr">confirmed_start</code></td><td>Logoها در Desktop کنار هم.</td></tr>
<tr><th scope="row">Wrap</th><td><code dir="ltr">Wrap</code></td><td><code dir="ltr">confirmed_method</code></td><td>در عرض کم خط جدید بسازد.</td></tr>
<tr><th scope="row">Gap</th><td><code dir="ltr">12px</code> تا <code dir="ltr">20px</code></td><td><code dir="ltr">provisional</code></td><td>با تعداد و اندازهٔ واقعی Logoها تست شود.</td></tr>
<tr><th scope="row">Logo Image max width</th><td><code dir="ltr">80px</code> تا <code dir="ltr">120px</code></td><td><code dir="ltr">provisional</code></td><td>به فایل واقعی و خوانایی بستگی دارد.</td></tr>
<tr><th scope="row">Logo Image max height</th><td><code dir="ltr">28px</code> تا <code dir="ltr">40px</code></td><td><code dir="ltr">provisional</code></td><td>نسبت تصویر حفظ شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — تست Wrap</h3>
<ol>
<li>عرض Copy Area را در ذهن یا با Responsive mode کم کن.</li>
<li>ببین Logoها به خط بعد می‌روند یا از Parent بیرون می‌زنند.</li>
<li>اگر Overflow رخ داد، اول max-width/max-height Image، Gap و basis/width Logo Item را بررسی کن.</li>
<li>Logoها را فقط برای جا شدن Hide نکن.</li>
</ol>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر Logoها در عرض کم جا نمی‌شوند، اولین راه‌حل سالم‌تر چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-8">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-8-a" name="stop-question-8" type="radio" value="A"/><span>A) Logoهای آخر را مخفی کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-8-b" name="stop-question-8" type="radio" value="B"/><span>B) Parent را Flex Wrap کنم و اندازهٔ Logo/GAP را بررسی کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-8-c" name="stop-question-8" type="radio" value="C"/><span>C) همهٔ Logoها را Absolute کنم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Wrap ساختار و محتوا را حفظ می‌کند. Hide کردن Logoها یا Absolute کردن آن‌ها راه‌حل اول نیست و می‌تواند محتوا، دسترسی‌پذیری و نگهداری را خراب کند.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> Wrap را روشن کنی اما اندازهٔ Logoها و Gap را کنترل نکنی.</p>
<p><strong>نشانه:</strong> Logoها به خط بعد می‌روند ولی همچنان شلوغ، ناهماهنگ یا بیرون‌زده‌اند.</p>
<p><strong>قاعده:</strong> Wrap + Gap + Logo Item size + Image max size را با هم بررسی کن.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>این ساختار خراب را تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Logo Strip خراب‌شده</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Logo Strip: display:flex; nowrap;
Logo 1: margin-right: 24px;
Logo 2: margin-right: 24px;
Logo 3: margin-right: 24px;
Logo 4: margin-right: 24px;

نتیجه:
- در عرض کم overflow رخ می‌دهد
- فاصله‌ها پراکنده و سخت‌نگهداری‌اند
- Parent قانون یکپارچه ندارد</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-43">
<fieldset>
<legend>Checkpoint درس ۸</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-43-1" name="chk-43-1" type="checkbox"/><span>Logo Strip داخل TUYA Copy ساخته شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-43-2" name="chk-43-2" type="checkbox"/><span>Logoها Child مستقیم Logo Strip هستند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-43-3" name="chk-43-3" type="checkbox"/><span>Wrap روشن است و Gap روی Parent تنظیم شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-43-4" name="chk-43-4" type="checkbox"/><span>هیچ Logo فقط برای جا شدن Hide نشده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-43-5" name="chk-43-5" type="checkbox"/><span>اندازهٔ Logoها هنوز provisional است و با فایل واقعی باید تست شود.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Wrap چه چیزی را حل می‌کند و چه چیزی را حل نمی‌کند؟</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر یک لیست Tag یا Feature Badge داری که در Mobile جا نمی‌شود، آیا اول Grid می‌سازی یا Flex Wrap را بررسی می‌کنی؟ چرا؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Wrap اجازهٔ خط جدید می‌دهد، اما اندازهٔ Item و Gap را حل نمی‌کند. برای آیتم‌های تکراری ساده، Flex Wrap معمولاً قبل از Grid کامل بررسی می‌شود.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-8-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Logo Strip در عرض کم</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">verified_method_provisional_values</code></p>
<ul>
<li>در Desktop، Logoها می‌توانند در یک خط باشند.</li>
<li>در Mobile یا Copy Area باریک، Logoها باید بتوانند به خط بعد بروند.</li>
<li>Gap Desktop را بدون بررسی به Mobile منتقل نکن.</li>
<li>Logoها را برای جا شدن پنهان نکن مگر نقش محتوایی آن‌ها روشن و حذفشان قابل دفاع باشد.</li>
<li>اگر Logoها خوانا نیستند، max-width/max-height و فایل واقعی Logo را بررسی کن.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-8-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-8-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Wrap روشن است ولی هنوز Overflow داریم</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: Logo Strip را Flex Wrap کرده‌ای، اما در عرض کم هنوز overflow دیده می‌شود.</p>
<p>قبل از تغییر مقدار جدید، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا Logoها Child مستقیم Logo Strip هستند؟</li>
<li>آیا Parent واقعاً <code dir="ltr">flex-wrap: wrap</code> دارد؟</li>
<li>Gap چقدر فضا مصرف می‌کند؟</li>
<li>Logo Item چه width/basis/min-width دارد؟</li>
<li>Image داخل Logo چه max-width/max-height دارد؟</li>
<li>آیا فایل SVG/PNG خودش viewBox یا ابعاد نامناسب دارد؟</li>
<li>آیا Copy Area به اندازهٔ کافی قابل Shrink است؟</li>
</ul>
</section>
<p>نتیجهٔ درست: اول Parent، Child مستقیم، اندازهٔ Item و Image را بررسی کن؛ بعد مقدار را تغییر بده.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، Flex overlay می‌تواند Flex Lineها و Gap را نشان بدهد. Computed Style می‌تواند نشان دهد wrap واقعاً فعال است یا نه و هر Image چه اندازهٔ نهایی گرفته است.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-8-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-8-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-46">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-46-1" name="chk-46-1" type="checkbox"/><span>می‌توانم توضیح بدهم Wrap اجازهٔ ساخت Flex Line جدید می‌دهد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-46-2" name="chk-46-2" type="checkbox"/><span>می‌دانم Wrap اندازهٔ Logoها را به‌تنهایی حل نمی‌کند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-46-3" name="chk-46-3" type="checkbox"/><span>می‌توانم تفاوت align-items و align-content را در حالت چند Line توضیح بدهم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-47">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-47-1" name="chk-47-1" type="checkbox"/><span>Logo Strip را داخل Copy Area می‌سازم و آن را Flex Row + Wrap می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-47-2" name="chk-47-2" type="checkbox"/><span>Logoها را با Gap و max-size کنترل می‌کنم، نه Marginهای تکی.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-47-3" name="chk-47-3" type="checkbox"/><span>در عرض کم، Wrap را تست می‌کنم و Logoها را بدون دلیل Hide نمی‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-48">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-48-1" name="chk-48-1" type="checkbox"/><span>برای Tag List یا Feature Badge List می‌توانم تصمیم بگیرم Flex Wrap کافی است یا Grid لازم می‌شود.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-8-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-8-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، وارد ادامهٔ ساختار محتوایی یا مرحلهٔ بعدی Layout می‌شویم. هنوز Position نهایی Nodeها و Visual Stage کامل را انجام نمی‌دهیم.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 8</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-8-completion">
<fieldset>
<legend>ثبت پایان درس 8</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-8-complete" name="lesson-8-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
