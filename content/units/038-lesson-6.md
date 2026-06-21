<article class="lesson card-surface" data-lesson="6" id="lesson-6">

<h2 class="lesson-title former-h1">درس 6 — Direction، Align، Justify و Gap</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-6-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-6-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> بعد از Flex کردن Shell، محور اصلی و فرعی را درست بخوانی و بفهمی Direction، Justify، Align و Gap دقیقاً روی چه چیزی اثر می‌گذارند.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Grow/Shrink عمیق، Order نهایی Mobile، Position نهایی Nodeها، Visual Stage کامل، یا مقدار قطعی فاصله‌ها از روی Screenshot.</p>
<p><strong>در پایان باید بتوانی:</strong> بعد از تغییر Row به Column، دوباره تشخیص بدهی Justify و Align روی کدام محور اثر می‌گذارند و فاصلهٔ بین Copy و Visual را با Gap کنترل کنی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-6-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-6-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + 👁 مشاهدهٔ محور</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰–۲۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۳۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> خطای رایج این درس حفظ‌کردن «Justify یعنی افقی» و «Align یعنی عمودی» است. باید هنرجو را مجبور کرد اول Direction را بخواند، سپس Main Axis و Cross Axis را دوباره استخراج کند.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_axis_alignment_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-6-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-6-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس ۵، Shell را به Flex Container تبدیل کردی تا Copy و Visual در Desktop کنار هم قرار بگیرند. حالا در درس ۶ باید یاد بگیری وقتی Direction عوض می‌شود، معنی عملی Justify و Align هم از نظر محور عوض می‌شود.</p>
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
Axis / Direction / Justify / Align / Gap</code></pre>
</figure>

<h3>بزرگ‌ترین اشتباه حفظی</h3>
<p>این جمله ناقص و خطرناک است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Justify = افقی
Align = عمودی</code></pre>
</figure>
<p>این فقط وقتی ظاهراً درست دیده می‌شود که Direction روی Row باشد. اگر Direction به Column تغییر کند، Main Axis عمودی می‌شود و Justify هم روی محور عمودی اثر می‌گذارد.</p>

<h3>مدل ریل</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Direction</dt><dd>جهت ریل را تعیین می‌کند: Row یا Column.</dd>
<dt>Main Axis</dt><dd>طول ریل؛ Justify روی این محور کار می‌کند.</dd>
<dt>Cross Axis</dt><dd>محور عمود بر ریل؛ Align روی این محور کار می‌کند.</dd>
<dt>Justify Content</dt><dd>فضای آزاد را روی Main Axis توزیع می‌کند.</dd>
<dt>Align Items</dt><dd>Itemها را روی Cross Axis تراز می‌کند.</dd>
<dt>Gap</dt><dd>فاصلهٔ ثابت بین Flex Itemها؛ به Parent تعلق دارد، نه به یک Item خاص.</dd>
</dl>
</section>

<h3>محورها در Row و Column</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Axes in row and column">
<table class="data-table educational-table edu-table">
<caption>محورها با تغییر Direction</caption>
<thead><tr><th scope="col">Direction</th><th scope="col">Main Axis</th><th scope="col">Justify روی کجا اثر دارد؟</th><th scope="col">Cross Axis</th><th scope="col">Align روی کجا اثر دارد؟</th></tr></thead>
<tbody>
<tr><th scope="row">Row</th><td>افقی / Inline</td><td>افقی، در امتداد ردیف</td><td>عمودی / Block</td><td>عمودی</td></tr>
<tr><th scope="row">Column</th><td>عمودی / Block</td><td>عمودی، در امتداد ستون</td><td>افقی / Inline</td><td>افقی</td></tr>
</tbody>
</table>
</div>

<h3>RTL را با چپ و راست حفظ نکن</h3>
<p>در زبان‌های RTL، Start و End افقی ممکن است نسبت به LTR جابه‌جا شوند. بنابراین بهتر است به‌جای حفظ‌کردن چپ و راست، از واژه‌های Main Axis، Cross Axis، Start و End استفاده کنی.</p>

<h3>Justify فقط وقتی چیزی برای توزیع وجود داشته باشد اثر می‌گذارد</h3>
<p>اگر Itemها تمام فضای Parent را مصرف کرده باشند، Justify ممکن است اثر آشکاری نشان ندهد. بنابراین قبل از اینکه بگویی «Justify کار نمی‌کند»، باید Size/Basis/Grow و فضای آزاد Parent را بررسی کنی.</p>

<h3>Gap با Margin فرق دارد</h3>
<p>Gap فاصلهٔ بین Itemهای یک Parent است. Margin فاصلهٔ بیرونی یک Item است. برای فاصلهٔ منظم بین Copy و Visual در Shell، Gap نقطهٔ شروع تمیزتری است.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-6.0.0" id="lesson-6-concept-reference">
<summary>📚 مرجع مفهومی کامل — Direction، Main/Cross Axis، Justify، Align و Gap</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="6" data-source-version="tuya-revised-6.0.0">

<p class="concept-reference-lead">این مرجع، هستهٔ مفهومی درس را حفظ می‌کند و آن را به تمرین واقعی TUYA وصل می‌کند. هدف این نیست که همهٔ کنترل‌های Flex را حفظ کنی؛ هدف این است که هر بار بعد از تغییر Direction، محور را دوباره بخوانی.</p>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-6-trap">
<h3 id="lesson-6-trap">۱. چرا حفظ افقی/عمودی خطرناک است؟</h3>
<p>در Row، Justify معمولاً افقی دیده می‌شود و Align معمولاً عمودی. اما در Column این برداشت می‌شکند. پس تعریف واقعی این است:</p>
<ul>
<li><strong>Justify:</strong> همیشه روی Main Axis.</li>
<li><strong>Align:</strong> همیشه روی Cross Axis.</li>
<li><strong>Direction:</strong> تعیین می‌کند Main Axis کدام جهت باشد.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-6-train">
<h3 id="lesson-6-train">۲. تشبیه ریل و سکو</h3>
<ul>
<li><strong>Direction:</strong> جهت ریل.</li>
<li><strong>Main Axis:</strong> طول ریل.</li>
<li><strong>Cross Axis:</strong> عرض سکو.</li>
<li><strong>Justify:</strong> پخش‌کردن قطارها در طول ریل.</li>
<li><strong>Align:</strong> قرار دادن قطارها در عرض سکو.</li>
<li><strong>Gap:</strong> فاصلهٔ ثابت بین قطارها.</li>
</ul>
<p>اگر ریل را بچرخانی، تعریف Justify عوض نمی‌شود؛ خود ریل چرخیده است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-6-axis-diagram">
<h3 id="lesson-6-axis-diagram">۳. نمودار محور چرخان</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Row:
Main  ─────────────→
Cross ↓

Column:
Cross ─────────────→
Main  ↓</code></pre>
</figure>
<p>در <code dir="ltr">row-reverse</code> و <code dir="ltr">column-reverse</code> محور اصلی همچنان همان محور است، اما جهت Start و End برعکس می‌شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-6-justify">
<h3 id="lesson-6-justify">۴. Justify Content</h3>
<p>Justify فضای آزاد را روی Main Axis توزیع می‌کند:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">flex-start:     [A][B][C].........
center:         ....[A][B][C].....
space-between:  [A].....[B].....[C]</code></pre>
</figure>
<p>اگر فضای آزاد وجود نداشته باشد، Justify چیزی برای پخش‌کردن ندارد. این معمولاً وقتی رخ می‌دهد که Itemها با basis/grow/min-width فضا را پر کرده‌اند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-6-align">
<h3 id="lesson-6-align">۵. Align Items و Align Self</h3>
<p>Align Items روی همهٔ Childهای مستقیم Flex Container و در Cross Axis اثر می‌گذارد. Align Self فقط یک Item را متفاوت می‌کند.</p>
<p>در TUYA، اگر فقط Visual باید نسبت به Copy تراز متفاوتی داشته باشد، اول بررسی کن آیا مشکل از Align Items روی Shell است یا نیاز واقعی به Align Self روی Visual وجود دارد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-6-gap">
<h3 id="lesson-6-gap">۶. Gap</h3>
<p>Gap فاصلهٔ بین Itemهاست و به Parent تعلق دارد. مزیت Gap نسبت به Margin:</p>
<ul>
<li>ابتدا و انتهای گروه فاصلهٔ اضافه ایجاد نمی‌کند.</li>
<li>با کم‌وزیاد شدن Itemها منظم‌تر می‌ماند.</li>
<li>قانون فاصله را روی Parent نگه می‌دارد.</li>
</ul>
<p>برای فاصلهٔ بین Copy و Visual، اول Gap را بررسی کن؛ Margin را فقط وقتی استفاده کن که دلیل روشن بیرونی داری.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-6-tuya">
<h3 id="lesson-6-tuya">۷. خواندن محور در TUYA</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop:
TUYA Shell = Flex Row
Main Axis  = افقی
Cross Axis = عمودی
Justify    = توزیع افقی فضای آزاد
Align      = تراز عمودی Copy و Visual
Gap        = فاصلهٔ بین Copy و Visual

Mobile:
TUYA Shell = Flex Column
Main Axis  = عمودی
Cross Axis = افقی
Justify    = توزیع عمودی فضای آزاد
Align      = تراز افقی Copy و Visual
Gap        = فاصلهٔ عمودی بین Copy و Visual</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-6-debug">
<h3 id="lesson-6-debug">۸. روش عیب‌یابی چهارمرحله‌ای</h3>
<ol>
<li>Direction چیست؟</li>
<li>Main Axis کدام است؟</li>
<li>آیا فضای آزاد وجود دارد؟</li>
<li>می‌خواهم روی Main Axis تغییر بدهم یا Cross Axis؟</li>
</ol>
<p>اگر این چهار سؤال را نپرسی، ممکن است Align را عوض کنی در حالی که باید Justify را تغییر می‌دادی، یا برعکس.</p>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-6-golden">
<h3 id="lesson-6-golden">۹. قوانین طلایی</h3>
<ul>
<li><strong>Justify را با «افقی» حفظ نکن؛ آن را به Main Axis وصل کن.</strong></li>
<li><strong>Align را با «عمودی» حفظ نکن؛ آن را به Cross Axis وصل کن.</strong></li>
<li><strong>بعد از هر Row → Column، محورها را از نو بخوان.</strong></li>
<li><strong>Gap فاصلهٔ بین Siblingهاست، نه فاصلهٔ داخل یک Item.</strong></li>
<li><strong>اگر Justify اثر ندارد، اول فضای آزاد، Basis و Grow/Shrink را بررسی کن.</strong></li>
<li><strong>Order بصری را با reading/focus order قاطی نکن.</strong></li>
<li><strong>در این درس مقدارهای Gap و Alignment تا قبل از تست Responsive، provisional هستند.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفهوم Main Axis، Cross Axis، Justify، Align و Gap بر پایهٔ رفتار CSS Flexbox و مستندات رسمی Elementor دربارهٔ کنترل‌های Flexbox نوشته شده است. تصمیم‌های عددی TUYA تا قبل از UI واقعی و Breakpoint Validation قطعی نیستند.</p>
<ul>
<li><a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout" rel="noopener noreferrer" target="_blank">MDN — CSS Flexible Box Layout</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-6-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-6-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Keywordها، Gap و محورها</span>
</summary>
<section aria-labelledby="lesson-6-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در این درس بعضی کنترل‌ها عدد نیستند. Direction، Justify و Align معمولاً keyword هستند. Gap مقدار طولی می‌گیرد، ولی اثرش وابسته به Direction و محور است.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۶" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">اثر</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Direction</th><td>keyword</td><td>تعریف Main Axis</td><td>بعد از تغییر به Column، Justify/Align را با معنی قبلی بخوانی.</td></tr>
<tr><th scope="row">Justify Content</th><td>keyword</td><td>توزیع فضای آزاد روی Main Axis</td><td>وقتی فضای آزاد نیست، انتظار اثر بزرگ داشته باشی.</td></tr>
<tr><th scope="row">Align Items</th><td>keyword</td><td>تراز روی Cross Axis</td><td>آن را همیشه عمودی فرض کنی.</td></tr>
<tr><th scope="row">Gap</th><td>length / responsive length</td><td>فاصلهٔ بین Itemها</td><td>با Padding یا Margin اشتباه گرفته شود.</td></tr>
<tr><th scope="row">Order</th><td>number</td><td>ترتیب بصری در Flex</td><td>با ترتیب خواندن و Focus یکی فرض شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>not_applicable_for_alignment — اول محور را بخوان. اگر Justify اثر ندارد، فضای آزاد و اندازهٔ Itemها را بررسی کن.</p></section>
<section><h3>📱 در Responsive</h3><p>با Row → Column، Gap ممکن است از فاصلهٔ افقی به فاصلهٔ عمودی تبدیل شود. مقدار Desktop را بدون بررسی به Mobile منتقل نکن.</p></section>
<section><h3>🔬 در DevTools</h3><p>Flex overlay مرورگر می‌تواند محور، Gap و محل Itemها را نشان دهد. از آن برای تأیید استفاده کن، نه برای حدس‌زدن مقدار قطعی.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-6-axis-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — محور را با تغییر Direction دوباره بخوان</span>
</summary>
<section class="disclosure-content lesson-section">
<p>این Step‑Through برای حفظ روح نسخهٔ تعاملی درس آمده است: هر مرحله را پیش‌بینی کن، بعد نتیجه را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Step Through Axis">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ مراحل محور و تراز</caption>
<thead><tr><th scope="col">مرحله</th><th scope="col">وضعیت</th><th scope="col">پیش‌بینی</th><th scope="col">قانون طلایی</th><th scope="col">وضعیت شواهد</th></tr></thead>
<tbody>
<tr><th scope="row">۱</th><td>Row + Justify Start + Align Center</td><td>Justify روی کدام فضا اثر دارد؟</td><td>Justify را به Main Axis وصل کن.</td><td><code dir="ltr">verified_by_css_spec</code></td></tr>
<tr><th scope="row">۲</th><td>Row + Space Between</td><td>اگر فضای آزاد نباشد چه می‌شود؟</td><td>Alignment بعد از sizing خوانده می‌شود.</td><td><code dir="ltr">verified_by_css_spec</code></td></tr>
<tr><th scope="row">۳</th><td>Column با همان کنترل‌ها</td><td>Justify حالا کجا اثر دارد؟</td><td>بعد از Row → Column، محور را از نو بخوان.</td><td><code dir="ltr">verified_by_official_help_and_css_spec</code></td></tr>
<tr><th scope="row">۴</th><td>Column + بررسی Order</td><td>Order بصری چه چیزی را تغییر نمی‌دهد؟</td><td>Visual order و reading/focus order را جدا بررسی کن.</td><td><code dir="ltr">provisional_until_accessibility_check</code></td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-6-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-6-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — محور، تراز و فاصلهٔ Copy/Visual</h3>
<p>در این تمرین، همان Shell درس ۵ را بررسی می‌کنی. هدف فقط خواندن محور و تنظیم Gap/Align/Justify است. هنوز Position، Nodeها، Visual Stage positioning، Shadow/Glow و Order نهایی نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate درس ۶">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از تنظیم محور و فاصله</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Shell در درس ۵ Flex Container شد.</td><td>Direction/Justify/Align/Gap روی Shell بررسی می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy و Visual Child مستقیم Shell هستند.</td><td>Gap بین همین دو Item اثر می‌کند.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Gap، Align و Justify دقیق برای TUYA.</td><td>فقط مقدار شروع تست هستند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Breakpoint دقیق Column، ترتیب نهایی Mobile، ترتیب خواندن و Focus.</td><td>در این درس قطعی نمی‌شوند.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — اول Direction را بخوان</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس شش">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> خواندن محور، نه طراحی نهایی.</p>
<p><strong>مسیر:</strong> Elementor Editor → انتخاب <code dir="ltr">TUYA Shell</code> → Style/Layout → Flex controls.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">TUYA Shell</code>.</p>
<p><strong>Class فعال:</strong> همان Class Shell؛ Global جدید نساز.</p>
<p><strong>Property:</strong> Direction / Gap / Justify Content / Align Items.</p>
<p><strong>نباید تغییر کند:</strong> Position، Nodeها، Order نهایی، Shadow/Glow، Background نهایی، Typography، Button Style.</p>
<p><strong>عبارت تأیید پایانی:</strong> «بعد از خواندن Direction، Main Axis و Cross Axis را دوباره مشخص کردم.»</p>
</aside>

<h3>مرحلهٔ ۲ — مقدارهای شروع را تست کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional axis values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع برای محور و فاصله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">Desktop شروع</th><th scope="col">Mobile شروع</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Direction</th><td><code dir="ltr">Row</code></td><td><code dir="ltr">Column</code></td><td><code dir="ltr">confirmed_contract</code></td></tr>
<tr><th scope="row">Gap</th><td><code dir="ltr">24px</code> تا <code dir="ltr">40px</code></td><td><code dir="ltr">20px</code> تا <code dir="ltr">32px</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Justify</th><td><code dir="ltr">Start</code> یا <code dir="ltr">Space Between</code> فقط با فضای آزاد واقعی</td><td><code dir="ltr">Start</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Align</th><td><code dir="ltr">Center</code> یا <code dir="ltr">Stretch</code> طبق ارتفاع/visual</td><td><code dir="ltr">Stretch</code> یا <code dir="ltr">Center</code> طبق تست</td><td><code dir="ltr">provisional</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — پیش‌بینی کن، بعد تغییر بده</h3>
<ol>
<li>در Desktop با Row بگو Main Axis کدام است.</li>
<li>قبل از تغییر Justify، بگو اثر باید افقی باشد یا عمودی.</li>
<li>Direction را ذهنی به Column تغییر بده.</li>
<li>حالا دوباره بگو Justify و Align کجا اثر دارند.</li>
<li>فقط بعد از پیش‌بینی، مقدار را تغییر بده و نتیجه را ثبت کن.</li>
</ol>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر Direction از Row به Column تغییر کند، Justify روی کدام محور اثر می‌گذارد؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-6">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-6-a" name="stop-question-6" type="radio" value="A"/><span>A) همچنان فقط افقی</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-6-b" name="stop-question-6" type="radio" value="B"/><span>B) روی Main Axis جدید، یعنی عمودی</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-6-c" name="stop-question-6" type="radio" value="C"/><span>C) روی z-index</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Justify همیشه روی Main Axis اثر می‌گذارد. وقتی Direction به Column تبدیل می‌شود، Main Axis عمودی می‌شود.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> فکر کنی Align همیشه عمودی و Justify همیشه افقی است.</p>
<p><strong>نشانه:</strong> در Mobile چند بار Align را تغییر می‌دهی اما فاصلهٔ عمودی درست نمی‌شود.</p>
<p><strong>قاعده:</strong> اول Direction، بعد Main Axis، بعد Justify/Align.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>این خطا را تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>خواندن اشتباه محور بعد از Column</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Mobile:
Direction = Column

اشتباه:
Justify را افقی فرض می‌کنم
Align را عمودی فرض می‌کنم

نتیجه:
فاصله و تراز را با کنترل اشتباه تعمیر می‌کنم</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-31">
<fieldset>
<legend>Checkpoint درس ۶</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-31-1" name="chk-31-1" type="checkbox"/><span>می‌توانم در Row، Main Axis و Cross Axis را مشخص کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-31-2" name="chk-31-2" type="checkbox"/><span>می‌توانم در Column، Main Axis و Cross Axis را دوباره مشخص کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-31-3" name="chk-31-3" type="checkbox"/><span>Gap را برای فاصلهٔ بین Copy و Visual روی Shell بررسی کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-31-4" name="chk-31-4" type="checkbox"/><span>Order نهایی و دسترسی‌پذیری Mobile را هنوز قطعی نکرده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> در Row و Column بگو Justify و Align روی کدام محور کار می‌کنند.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر یک لیست Feature در Mobile زیر هم شده، برای فاصلهٔ عمودی بین آیتم‌ها اول Gap را بررسی می‌کنی یا Margin تک‌تک آیتم‌ها را؟ چرا؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Direction محور را تعیین می‌کند، Justify روی Main Axis و Align روی Cross Axis است، و Gap فاصلهٔ بین Siblingها را تمیزتر از Marginهای پراکنده کنترل می‌کند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-6-responsive-build-test">
<summary class="lesson-disclosure-summary">
<span aria-level="3" role="heading">📱 ایست بازرسی Responsive — محورهای Align و Justify پس از تغییر Direction</span>
</summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">verified_method_provisional_values</code></p>
<p class="exercise-goal"><strong>هدف:</strong> با تغییر Row به Column، Main Axis و Cross Axis را دوباره تشخیص بده.</p>
<ul>
<li>Desktop را Row بخوان: Justify روی افق، Align روی عمود.</li>
<li>Mobile را Column بخوان: Justify روی عمود، Align روی افق.</li>
<li>Gap در Row فاصلهٔ افقی بین ستون‌هاست؛ در Column فاصلهٔ عمودی بین بخش‌هاست.</li>
<li>اگر Order را تغییر دادی، reading order و focus order را جداگانه بررسی کن.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-6-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-6-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Align اثر مورد انتظار ندارد</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: در Mobile، Align را تغییر می‌دهی اما فاصلهٔ عمودی Copy و Visual تغییر نمی‌کند.</p>
<p>قبل از تغییر مقدار جدید، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>Direction فعلی چیست؟</li>
<li>Main Axis کدام است؟</li>
<li>Cross Axis کدام است؟</li>
<li>فاصله‌ای که می‌خواهی تغییر بدهی روی Main Axis است یا Cross Axis؟</li>
<li>Gap روی Parent تنظیم شده یا Marginهای پراکنده روی Childها؟</li>
<li>آیا Itemها فضای آزاد باقی گذاشته‌اند؟</li>
</ul>
</section>
<p>نتیجهٔ درست: اول محور را بخوان؛ بعد کنترل درست را انتخاب کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>Flex overlay در مرورگر می‌تواند محور و Gap را نشان بدهد. این ابزار برای تأیید مفید است، اما تصمیم آموزشی همچنان از Direction و Tree شروع می‌شود.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-6-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-6-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-34">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-34-1" name="chk-34-1" type="checkbox"/><span>می‌توانم توضیح بدهم Direction چگونه Main Axis را تعیین می‌کند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-34-2" name="chk-34-2" type="checkbox"/><span>می‌دانم Justify همیشه روی Main Axis و Align همیشه روی Cross Axis کار می‌کند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-34-3" name="chk-34-3" type="checkbox"/><span>می‌توانم فرق Gap و Margin را در یک Flex Container توضیح بدهم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-35">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-35-1" name="chk-35-1" type="checkbox"/><span>در TUYA Shell، Direction، Justify، Align و Gap را فقط بعد از خواندن محور تغییر می‌دهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-35-2" name="chk-35-2" type="checkbox"/><span>بعد از Row → Column، اثر Justify و Align را دوباره پیش‌بینی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-35-3" name="chk-35-3" type="checkbox"/><span>اگر Justify اثر ندارد، فضای آزاد و sizing را بررسی می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-36">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-36-1" name="chk-36-1" type="checkbox"/><span>برای یک لیست Feature در Mobile می‌توانم تصمیم بگیرم فاصلهٔ آیتم‌ها با Gap بهتر کنترل می‌شود یا Margin.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Direction، Align، Justify و Gap</span>
</summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>Gap این گروه direct literal بماند یا Variable spacing شود؟</li>
<li>این مقدار در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li>
<li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li>
<li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — در این درس، پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است. مقدارها را هنوز قطعی نکن.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-6-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-6-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، می‌توانیم به اندازهٔ Itemها، Basis/Grow/Shrink یا ادامهٔ Responsive Layout برویم. هنوز Position نهایی Nodeها و Visual Stage کامل را انجام نمی‌دهیم.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 6</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-6-completion">
<fieldset>
<legend>ثبت پایان درس 6</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-6-complete" name="lesson-6-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
