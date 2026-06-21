<article class="lesson card-surface" data-lesson="15" id="lesson-15">

<h2 class="lesson-title former-h1">درس 15 — RTL، Start و End</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-15-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-15-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> RTL را فقط راست‌چین‌کردن متن نبینی؛ جهت سند، محور Inline، Start/End، Logical Properties و محتوای دوجهته را درست تحلیل کنی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام جزئیات Unicode Bidirectional Algorithm، پیاده‌سازی کامل CSS logical fallback، یا پشتیبانی دقیق همهٔ propertyها در تمام مرورگرها.</p>
<p><strong>در پایان باید بتوانی:</strong> در TUYA تشخیص بدهی کدام فاصله، inset، icon order یا text direction باید logical باشد و کدام واقعاً فیزیکی است.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-15-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-15-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + 🔍 RTL Audit</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰–۳۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۴۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۵ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس باید عادت «راست/چپ» را به «شروع/پایان مسیر متن» تبدیل کند. هنرجو نباید با <code dir="ltr">text-align:right</code> یا <code dir="ltr">row-reverse</code> همهٔ مشکلات RTL را حل‌شده فرض کند.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_rtl_logical_direction_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-15-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-15-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>تا درس ۱۴، TUYA را با یک DOM، Flow سالم، Layout responsive، Typography و Media ساختی. حالا باید مطمئن شوی همین ساختار برای فارسی، انگلیسی و محتوای مخلوط قابل نگهداری است. این درس روی جهت و منطق Start/End تمرکز دارد.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Semantic content
↓
Typography / Layout
↓
Responsive
↓
RTL / LTR Direction
↓
Logical Start / End
↓
Bidi-safe content</code></pre>
</figure>

<h3>مسئله</h3>
<p>طرح ممکن است در فارسی ظاهراً درست باشد، اما با تغییر زبان یا محتوای مخلوط خراب شود: Icon در سمت اشتباه بماند، Margin سمت نادرست اعمال شود، URL ترتیب جمله را به‌هم بزند، یا کد و عدد داخل متن فارسی بد نمایش داده شود.</p>

<h3>RTL فقط text-align:right نیست</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li><strong>RTL:</strong> جهت پایهٔ خواندن و جریان Inline برای زبان‌هایی مثل فارسی.</li>
<li><strong>text-align:right:</strong> فقط تراز متن به سمت راست؛ جایگزین RTL نیست.</li>
<li><strong>Start/End:</strong> شروع و پایان منطقی مسیر متن؛ در RTL و LTR عوض می‌شود.</li>
<li><strong>Left/Right:</strong> سمت فیزیکی صفحه؛ با زبان عوض نمی‌شود.</li>
</ul>
</section>

<h3>Start و End با Direction تغییر می‌کنند</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">LTR: inline-start = left
RTL: inline-start = right

LTR: inline-end = right
RTL: inline-end = left</code></pre>
</figure>
<p>پس اگر فاصله به «شروع متن» مربوط است، بهتر است به‌جای left/right به Inline Start/End فکر کنی.</p>

<h3>Inline و Block</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Inline and Block axis">
<table class="data-table educational-table edu-table">
<caption>محورهای منطقی در نوشتار افقی فارسی</caption>
<thead><tr><th scope="col">محور</th><th scope="col">معنی</th><th scope="col">در فارسی معمول</th><th scope="col">مثال</th></tr></thead>
<tbody>
<tr><th scope="row">Inline Axis</th><td>مسیر حرکت متن در یک خط</td><td>راست به چپ</td><td><code dir="ltr">margin-inline-start</code></td></tr>
<tr><th scope="row">Block Axis</th><td>مسیر چیده‌شدن سطرها/پاراگراف‌ها</td><td>بالا به پایین</td><td><code dir="ltr">margin-block-start</code></td></tr>
</tbody>
</table>
</div>

<h3>Physical به Logical</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Physical to Logical properties">
<table class="data-table educational-table edu-table">
<caption>جایگزین‌های منطقی رایج</caption>
<thead><tr><th scope="col">Physical</th><th scope="col">Logical</th><th scope="col">زمان مناسب</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">margin-left/right</code></th><td><code dir="ltr">margin-inline-start/end</code></td><td>فاصلهٔ مرتبط با شروع/پایان متن</td></tr>
<tr><th scope="row"><code dir="ltr">padding-left/right</code></th><td><code dir="ltr">padding-inline-start/end</code></td><td>Padding افقی وابسته به جهت متن</td></tr>
<tr><th scope="row"><code dir="ltr">left/right</code></th><td><code dir="ltr">inset-inline-start/end</code></td><td>Position وابسته به جهت نوشتار</td></tr>
<tr><th scope="row"><code dir="ltr">top/bottom</code></th><td><code dir="ltr">inset-block-start/end</code></td><td>Position در محور Block</td></tr>
<tr><th scope="row"><code dir="ltr">width</code></th><td><code dir="ltr">inline-size</code></td><td>اندازه در مسیر Inline</td></tr>
<tr><th scope="row"><code dir="ltr">height</code></th><td><code dir="ltr">block-size</code></td><td>اندازه در مسیر Block</td></tr>
</tbody>
</table>
</div>

<h3>direction و flex-direction یکی نیستند</h3>
<p><code dir="ltr">direction:rtl</code> جهت پایهٔ متن و بعضی رفتارهای Inline را تعیین می‌کند. <code dir="ltr">flex-direction</code> چیدمان Flex Itemها را تعیین می‌کند. اگر فقط برای جابه‌جایی یک Icon، direction کل Parent را دستکاری کنی، ممکن است متن، اعداد و محتوای دوجهته خراب شود.</p>

<h3>row-reverse ابزار خطرناک است</h3>
<p><code dir="ltr">row-reverse</code> فقط ظاهر ترتیب را برعکس می‌کند. DOM order، reading order و focus order الزاماً مطابق ظاهر جدید نمی‌شوند. اگر فقط برای اینکه Icon «سمت درست» بیاید row-reverse بزنی، احتمالاً مسئله را با ابزار اشتباه حل کرده‌ای.</p>

<h3>محتوای دوجهته یا Bidi</h3>
<p>در فارسی معمولاً متن‌هایی مثل نسخه، URL، CSS، ایمیل، نام محصول انگلیسی یا شماره تلفن وارد جمله می‌شوند:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">نسخه 4.1.3
CSS: flex: 1 1 0
example.com/path
شماره 0912...</code></pre>
</figure>
<p>برای عبارت‌های خارجی، از <code dir="ltr">dir="ltr"</code>، <code dir="ltr">dir="auto"</code> یا isolation مثل <code dir="ltr">&lt;bdi&gt;</code> بر اساس نوع محتوا استفاده کن. هدف این است که جهت عبارت خارجی، جملهٔ فارسی اطراف را خراب نکند.</p>

<h3>قاعدهٔ این درس</h3>
<p>در TUYA، هرجا فاصله یا Position به جریان متن مربوط است، اول logical فکر کن. هرجا واقعاً موقعیت فیزیکی صفحه منظور است، physical می‌تواند قابل دفاع باشد. تصمیم را ثبت کن.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-15.0.0" id="lesson-15-concept-reference">
<summary>📚 مرجع مفهومی کامل — RTL و Logical Properties؛ Start و End به‌جای حدس راست و چپ</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="15" data-source-version="tuya-revised-15.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی فعلی درس را حفظ می‌کند و آن را به پروژهٔ TUYA وصل می‌کند. هدف ساخت ذهنیت دو‌زبانه و جهت‌پذیر است، نه فقط راست‌چین‌کردن متن.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-15-ref-problem">
<h3 id="lesson-15-ref-problem">۱. مسئله‌ای که RTL حل می‌کند</h3>
<p>در صفحهٔ فارسی، جهت خواندن از راست به چپ است، اما Layout فقط متن نیست. فاصله، Icon، Border، Position، Order، Focus و Dynamic Text هم باید با جهت سند سازگار باشند.</p>
<p>اگر طراحی را فقط با <code dir="ltr">left</code> و <code dir="ltr">right</code> بسازی، ممکن است:</p>
<ul>
<li>نسخهٔ انگلیسی برعکس یا پرهزینه شود؛</li>
<li>Icon سمت نادرست بماند؛</li>
<li>Marginها برای RTL و LTR دو CSS جدا بخواهند؛</li>
<li>Component قابل استفادهٔ مجدد نباشد؛</li>
<li>متن Dynamic مخلوط ترتیب جمله را خراب کند.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-15-door">
<h3 id="lesson-15-door">۲. تشبیه درِ شروع و پایان</h3>
<p>در یک سالن، به‌جای «در سمت راست» می‌توانی بگویی «در شروع مسیر». در سالن فارسی شروع مسیر از راست است؛ در سالن انگلیسی از چپ. Logical Propertyها نیز نقش مسیر را بیان می‌کنند، نه سمت فیزیکی را.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">LTR: inline-start = left
RTL: inline-start = right</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-15-elementor">
<h3 id="lesson-15-elementor">۳. در Elementor V4 چگونه فکر کن؟</h3>
<p>در Elementor، UI ممکن است بسیاری از کنترل‌ها را با عنوان‌های بصری نشان دهد، اما ذهن تو باید direction-aware باشد:</p>
<ol>
<li>زبان و جهت سند/بخش را درست تشخیص بده.</li>
<li>Alignment را با نقش محتوا انتخاب کن، نه عادت «همه‌چیز راست».</li>
<li>فاصله‌های مرتبط با متن را logical طراحی کن.</li>
<li>Badgeها و Nodeهای وابسته به متن را با inset-inline فکر کن.</li>
<li>Icon و Text داخل Button را در RTL و LTR تست کن.</li>
<li>Dynamic Tagهای عددی، URL و عنوان‌های ترکیبی را تست کن.</li>
</ol>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-15-button">
<h3 id="lesson-15-button">۴. Icon و Text داخل Button</h3>
<p>در دکمهٔ فارسی، شاید Icon باید بعد از متن بیاید، نه الزاماً سمت چپ یا راست فیزیکی. برای دکمهٔ دو‌زبانه، بهتر است رابطهٔ Icon/Text را با start/end یا order معنایی مدیریت کنی، نه با left/right کور.</p>
<p>اما مراقب باش: تغییر visual order نباید focus order و خواندن محتوا را بی‌معنی کند. اگر DOM order برای accessibility مهم است، فقط ظاهر را با احتیاط تغییر بده.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-15-position">
<h3 id="lesson-15-position">۵. Position در RTL</h3>
<p>از درس Position می‌دانی Nodeها داخل Stage absolute می‌شوند. حالا باید بپرسی:</p>
<ul>
<li>این Node واقعاً باید سمت فیزیکی چپ Stage باشد؟</li>
<li>یا باید در انتهای Inline جریان متن قرار بگیرد؟</li>
<li>آیا با تغییر زبان، جای آن باید تغییر کند؟</li>
</ul>
<p>اگر پاسخ به جهت زبان وابسته است، logical inset را بررسی کن. اگر پاسخ واقعاً فیزیکی است، left/right قابل دفاع است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-15-bidi">
<h3 id="lesson-15-bidi">۶. Bidi و Isolation</h3>
<p>الگوریتم Bidi مرورگر بیشتر موارد را حل می‌کند، اما ترکیب فارسی با عدد، URL، کد و نام انگلیسی می‌تواند پیچیده شود. نمونه‌های حساس:</p>
<ul>
<li>Version number: <code dir="ltr">v4.1.3</code></li>
<li>CSS fragment: <code dir="ltr">flex: 1 1 0</code></li>
<li>URL: <code dir="ltr">example.com/path</code></li>
<li>English product name inside Persian sentence</li>
</ul>
<p>ابزارهای رایج:</p>
<ul>
<li><code dir="ltr">dir="ltr"</code> برای عبارت واضحاً انگلیسی/کد؛</li>
<li><code dir="ltr">dir="auto"</code> برای متن dynamic ناشناخته؛</li>
<li><code dir="ltr">&lt;bdi&gt;</code> برای isolate کردن قطعه‌ای که نباید جهت جملهٔ اطراف را خراب کند؛</li>
<li>code blockها همیشه LTR بمانند.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-15-tuya-contract">
<h3 id="lesson-15-tuya-contract">۷. قرارداد RTL برای TUYA</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA RTL contract">
<table class="data-table educational-table edu-table">
<caption>RTL Contract پیشنهادی TUYA</caption>
<thead><tr><th scope="col">بخش</th><th scope="col">تصمیم</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">TUYA Section</th><td>lang و dir باید با محتوای فارسی هماهنگ باشد.</td><td><code dir="ltr">confirmed_need</code></td></tr>
<tr><th scope="row">Copy Text</th><td>RTL طبیعی؛ code/URL/English fragments ایزوله شوند.</td><td><code dir="ltr">provisional_until_text</code></td></tr>
<tr><th scope="row">Feature List</th><td>Dot/Icon و Text با gap منطقی؛ نه margin-left/right کور.</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Button</th><td>Icon/Text order با معنا و accessibility تست شود.</td><td><code dir="ltr">unknown_until_cta</code></td></tr>
<tr><th scope="row">Logo Strip</th><td>خود Logoها معمولاً جهت‌ناپذیرند، اما spacing گروه باید منطقی باشد.</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Visual Stage Nodes</th><td>اگر وابسته به زبان/جریان متن نیستند، physical می‌تواند قابل دفاع باشد؛ اگر وابسته‌اند، logical بررسی شود.</td><td><code dir="ltr">case_by_case</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-15-traps">
<h3 id="lesson-15-traps">۸. اشتباهات رایج</h3>
<ul>
<li><code dir="ltr">text-align:right</code> به‌عنوان راه‌حل کامل RTL؛</li>
<li>استفاده از margin-left/right برای Component قابل ترجمه؛</li>
<li>تغییر direction فقط برای جابه‌جایی Icon؛</li>
<li>استفاده افراطی از row-reverse؛</li>
<li>نادیده گرفتن order خواندن و focus؛</li>
<li>RTL کردن code block یا CSS snippet؛</li>
<li>نادیده گرفتن URL، شماره نسخه و اعداد داخل متن فارسی؛</li>
<li>فرض اینکه همهٔ Positionها باید logical شوند، حتی وقتی واقعاً فیزیکی‌اند.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-15-golden">
<h3 id="lesson-15-golden">۹. قوانین طلایی</h3>
<ul>
<li><strong>RTL فقط راست‌چین‌کردن متن نیست.</strong></li>
<li><strong>Start/End با Direction تغییر می‌کند؛ Left/Right فیزیکی‌اند.</strong></li>
<li><strong>برای Componentهای دو‌زبانه، logical properties معمولاً مقاوم‌ترند.</strong></li>
<li><strong>direction سند را با flex-direction قاطی نکن.</strong></li>
<li><strong>row-reverse را برای حل سریع Icon order افراطی استفاده نکن.</strong></li>
<li><strong>کد واقعی، URL و قطعه‌های لاتین را LTR/isolated نگه دار.</strong></li>
<li><strong>هر left/right را کورکورانه جایگزین نکن؛ اول بپرس فیزیکی است یا منطقی.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفاهیم RTL، logical properties، writing mode، Bidi isolation و direction بر پایهٔ CSS/HTML و رفتار مرورگر نوشته شده‌اند. تصمیم‌های TUYA باید با محتوای واقعی فارسی/انگلیسی و Dynamic Text تست شوند.</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values" rel="noopener noreferrer" target="_blank">MDN — CSS Logical Properties and Values</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir" rel="noopener noreferrer" target="_blank">MDN — HTML dir global attribute</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi" rel="noopener noreferrer" target="_blank">MDN — bdi element</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/direction" rel="noopener noreferrer" target="_blank">MDN — CSS direction</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-15-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-15-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Logical Properties، Direction و Bidi</span>
</summary>
<section aria-labelledby="lesson-15-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در این درس، مقدار فقط عدد نیست؛ جهت و محور مرجع مهم است. <code dir="ltr">inline-start</code> در RTL و LTR به سمت فیزیکی متفاوت اشاره می‌کند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۵" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">dir</code></th><td>rtl / ltr / auto</td><td>زبان محتوا</td><td>برای جابه‌جایی ظاهری استفاده شود.</td></tr>
<tr><th scope="row"><code dir="ltr">direction</code></th><td>rtl / ltr</td><td>جریان Inline و متن</td><td>با flex-direction قاطی شود.</td></tr>
<tr><th scope="row"><code dir="ltr">margin-inline-start</code></th><td>length</td><td>شروع Inline</td><td>وقتی منظور فیزیکی چپ است استفاده شود.</td></tr>
<tr><th scope="row"><code dir="ltr">padding-inline</code></th><td>length</td><td>محور Inline</td><td>با padding-left/right کور جایگزین شود.</td></tr>
<tr><th scope="row"><code dir="ltr">inset-inline-start</code></th><td>length / %</td><td>Containing Block + جهت Inline</td><td>برای Node فیزیکی غیرزبانی استفاده شود.</td></tr>
<tr><th scope="row"><code dir="ltr">bdi</code></th><td>HTML element</td><td>قطعهٔ محتوای دوجهته</td><td>به‌جای حل ساختاری، همه‌جا بی‌دلیل استفاده شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>در RTL، <code dir="ltr">margin-inline-start: 16px</code> سمت راست را فاصله می‌دهد. در LTR همان declaration سمت چپ را فاصله می‌دهد. معنی declaration ثابت است: فاصله از شروع متن.</p></section>
<section><h3>📱 در Responsive</h3><p>با تغییر Row/Column، مفهوم Start/End را دوباره با Direction و Axis بخوان. Reverse کردن Visual order را با reading/focus order قاطی نکن.</p></section>
<section><h3>🔬 در DevTools</h3><p>Computed value ممکن است physical شود. source rule را هم ببین تا بفهمی declaration logical بوده یا left/right فیزیکی.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-15-rtl-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Left/Right یا Start/End؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر حالت را پیش‌بینی کن، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="RTL Step Through">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تصمیم‌های RTL</caption>
<thead><tr><th scope="col">حالت</th><th scope="col">وضعیت</th><th scope="col">تصمیم بهتر</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">Feature Dot کنار متن</th><td>فاصله بین Dot و Text</td><td>Gap یا margin-inline</td><td>رابطهٔ آیتم‌ها جهت‌پذیر است.</td></tr>
<tr><th scope="row">Badge همیشه گوشهٔ فیزیکی تصویر</th><td>وابسته به زبان نیست</td><td>left/right قابل دفاع</td><td>موقعیت واقعاً فیزیکی است.</td></tr>
<tr><th scope="row">Icon قبل/بعد متن Button</th><td>وابسته به زبان و معنا</td><td>start/end یا order مستند</td><td>باید RTL/LTR و focus تست شود.</td></tr>
<tr><th scope="row">Code snippet داخل متن فارسی</th><td>لاتین/کد</td><td><code dir="ltr">dir="ltr"</code> و isolation</td><td>خوانایی کد باید حفظ شود.</td></tr>
<tr><th scope="row">URL dynamic</th><td>محتوای ناشناخته/لاتین</td><td><code dir="ltr">dir="auto"</code> یا <code dir="ltr">bdi</code></td><td>جهت عبارت نباید جمله را خراب کند.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-15-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-15-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — RTL Audit بدون بازطراحی</h3>
<p>در این تمرین فقط جهت و logical بودن تصمیم‌ها را Audit می‌کنی. هنوز Layout را بازطراحی نمی‌کنی، Nodeهای نهایی را جابه‌جا نمی‌کنی و همهٔ CSS را به logical تبدیل نمی‌کنی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 15">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از RTL Audit</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>TUYA محتوای فارسی/RTL دارد.</td><td>dir/lang و Start/End باید بررسی شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Code، CSS، URL و نسخه‌های لاتین باید LTR بمانند.</td><td>ایزولیشن لازم است.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Icon order، button order، logical insetهای Node.</td><td>با محتوای واقعی و UX تست می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>نسخهٔ انگلیسی نهایی، dynamic tags، URLها، CTA واقعی.</td><td>بدون دادهٔ واقعی قطعی نشود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط RTL Audit انجام بده</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس پانزده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> یافتن left/rightهای مشکوک و محتوای bidi، نه تغییر گستردهٔ پروژه.</p>
<p><strong>مسیر:</strong> Elementor Editor → TUYA Section → بررسی Copy، Feature List، Button، Logo Strip، Visual Stage.</p>
<p><strong>Element هدف:</strong> فقط مواردی که فاصله یا جهت آن‌ها به متن وابسته است.</p>
<p><strong>Class فعال:</strong> Classهای موجود؛ Global/Utility جدید نساز مگر pattern واقعی تکرار شود.</p>
<p><strong>Property:</strong> direction، alignment، gap، margin/padding inline، inset-inline، dir/auto/bdi برای متن dynamic.</p>
<p><strong>نباید تغییر کند:</strong> DOM اصلی، Responsive Contract، Position نهایی Nodeها، Layer Map نهایی، Typography System نهایی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «RTL Audit انجام شد؛ هر left/right به فیزیکی یا logical طبقه‌بندی شد.»</p>
</aside>

<h3>مرحلهٔ ۲ — RTL Audit Table</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="RTL Audit Table">
<table class="data-table educational-table edu-table">
<caption>جدول Audit جهت و Logical Properties</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">سؤال</th><th scope="col">تصمیم اولیه</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Feature Dot/Text</th><td>فاصله بین Icon و Text جهت‌پذیر است؟</td><td>Gap یا inline spacing</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Button Icon/Text</th><td>Icon قبل/بعد متن با زبان تغییر می‌کند؟</td><td>order مستند، نه row-reverse کور</td><td><code dir="ltr">unknown_until_cta</code></td></tr>
<tr><th scope="row">Visual Node</th><td>جای Node فیزیکی است یا منطقی؟</td><td>case-by-case</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Code/URL</th><td>قطعهٔ LTR داخل فارسی است؟</td><td><code dir="ltr">dir="ltr"</code> یا <code dir="ltr">bdi/auto</code></td><td><code dir="ltr">confirmed_need</code></td></tr>
<tr><th scope="row">Logo Strip Gap</th><td>فاصلهٔ گروه وابسته به جریان است؟</td><td>Gap روی Parent</td><td><code dir="ltr">confirmed_method</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — تست دو زبانه ذهنی</h3>
<ol>
<li>یک Feature Item را در فارسی بخوان: شروع متن کجاست؟</li>
<li>همان را انگلیسی تصور کن: start به کجا می‌رود؟</li>
<li>اگر فاصله با margin-left/right ساخته شده، آیا هنوز درست است؟</li>
<li>اگر با gap یا margin-inline ساخته شده، آیا intent حفظ می‌شود؟</li>
<li>نتیجه را ثبت کن.</li>
</ol>

<h3>مرحلهٔ ۴ — تست Bidi</h3>
<p>این متن‌ها را در Copy یا نمونهٔ آزمایشی بررسی کن:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">نسخه v4.1.3 برای Elementor
کلاس CSS: .tuya-node { flex: 1 1 0; }
آدرس: example.com/docs/fa
شماره تماس: 0912...</code></pre>
</figure>
<p>اگر ترتیب نشانه‌ها یا جمله خراب شد، isolation را بررسی کن.</p>

<h3>مرحلهٔ ۵ — سؤال توقف</h3>
<p>برای فاصلهٔ بین Icon و Text در یک Feature Item دو‌زبانه، انتخاب مقاوم‌تر چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-15">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-15-a" name="stop-question-15" type="radio" value="A"/><span>A) margin-left ثابت</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-15-b" name="stop-question-15" type="radio" value="B"/><span>B) gap روی Parent یا margin-inline متناسب با نقش</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-15-c" name="stop-question-15" type="radio" value="C"/><span>C) تغییر direction فقط برای جابه‌جایی Icon</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> اگر فاصله به رابطهٔ Icon/Text مربوط است، بهتر است از Gap یا inline spacing استفاده شود. margin-left ثابت در LTR/RTL معنای متفاوتی پیدا می‌کند و direction برای جابه‌جایی Icon ابزار درستی نیست.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> با <code dir="ltr">text-align:right</code> یا <code dir="ltr">row-reverse</code> فکر کنی کل RTL حل شده است.</p>
<p><strong>نشانه:</strong> متن خوب دیده می‌شود، اما Icon، URL، کد، focus order یا نسخهٔ انگلیسی خراب می‌شود.</p>
<p><strong>قاعده:</strong> اول dir/lang و Start/End؛ بعد alignment و order.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<figure class="visual-figure ascii-figure">
<figcaption>RTL خراب با left/right کور</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code">.feature-icon {
  margin-left: 12px;
}

در RTL شاید درست به نظر برسد.
در LTR ممکن است فاصله سمت اشتباه باشد.
Intent واقعی: فاصله بین icon و text، نه الزاماً سمت چپ.</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-85">
<fieldset>
<legend>Checkpoint درس ۱۵</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-85-1" name="chk-85-1" type="checkbox"/><span>RTL را با text-align:right یکی نگرفته‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-85-2" name="chk-85-2" type="checkbox"/><span>left/rightهای مهم را به physical یا logical طبقه‌بندی کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-85-3" name="chk-85-3" type="checkbox"/><span>کد، URL و قطعه‌های لاتین LTR/isolated مانده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-85-4" name="chk-85-4" type="checkbox"/><span>direction را برای جابه‌جایی ظاهری Icon دستکاری نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-85-5" name="chk-85-5" type="checkbox"/><span>row-reverse را بدون بررسی reading/focus order استفاده نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-85-6" name="chk-85-6" type="checkbox"/><span>تصمیم نهایی Icon/Button order هنوز با CTA واقعی باید تست شود.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> تفاوت Start/End و Left/Right را با مثال Feature Item توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> برای یک کارت دو‌زبانه با Badge گوشه‌ای، چه زمانی از inset-inline-end استفاده می‌کنی و چه زمانی right فیزیکی قابل دفاع است؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید اگر Badge باید در پایان مسیر متن باشد، logical بهتر است؛ اگر واقعاً گوشهٔ فیزیکی تصویر/کارت مهم است، right/left فیزیکی قابل دفاع است.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-15-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — RTL در عرض‌های مختلف</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_bilingual_validation</code></p>
<ul>
<li>Feature List را در عرض‌های مختلف تست کن؛ dot/text alignment نباید با دوخطی‌شدن خراب شود.</li>
<li>Button Icon/Text را در RTL و LTR ذهنی یا واقعی تست کن.</li>
<li>URL و نسخهٔ انگلیسی داخل Paragraph را در Mobile بررسی کن.</li>
<li>Nodeهای Stage را اگر language-dependent هستند با logical inset بررسی کن؛ اگر decorative هستند case-by-case بمانند.</li>
<li>code blockها و CSS snippets را LTR نگه دار.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-15-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-15-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — فارسی درست است، انگلیسی خراب می‌شود</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">bilingual_audit</code></p>
<p>سناریو: نسخهٔ فارسی TUYA درست دیده می‌شود، اما اگر متن انگلیسی شود، فاصلهٔ Icon، جهت Button و حاشیه‌ها اشتباه می‌شوند.</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا از margin-left/right برای رابطهٔ icon/text استفاده شده؟</li>
<li>آیا text-align جای dir را گرفته؟</li>
<li>آیا row-reverse بدون بررسی DOM/focus استفاده شده؟</li>
<li>آیا URL یا code snippet ایزوله نشده؟</li>
<li>آیا spacing باید logical باشد یا physical؟</li>
<li>آیا Component واقعاً دو‌زبانه است یا فقط فارسی خواهد بود؟</li>
</ul>
</section>
<p>نتیجهٔ درست: intent فاصله و جهت را بنویس؛ بعد logical/physical بودن را تصمیم بگیر.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، source rule و computed style را با هم ببین. ممکن است declaration تو <code dir="ltr">margin-inline-start</code> باشد اما computed خروجی physical نمایش داده شود. این طبیعی است؛ مهم source intent است.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-15-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-15-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-88">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-88-1" name="chk-88-1" type="checkbox"/><span>می‌توانم توضیح بدهم RTL با text-align:right فرق دارد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-88-2" name="chk-88-2" type="checkbox"/><span>می‌دانم Start/End با Direction تغییر می‌کند و Left/Right فیزیکی‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-88-3" name="chk-88-3" type="checkbox"/><span>می‌توانم inline/block axis را در فارسی توضیح بدهم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-89">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-89-1" name="chk-89-1" type="checkbox"/><span>در TUYA، left/rightهای مهم را audit و به logical/physical طبقه‌بندی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-89-2" name="chk-89-2" type="checkbox"/><span>Feature Item و Button را برای RTL/LTR و focus order بررسی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-89-3" name="chk-89-3" type="checkbox"/><span>کد، URL، نسخه و قطعه‌های لاتین را LTR/isolated نگه می‌دارم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-90">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-90-1" name="chk-90-1" type="checkbox"/><span>برای یک کارت دو‌زبانه می‌توانم تشخیص بدهم کدام Position واقعاً فیزیکی است و کدام باید logical باشد.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-15-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Logical utilities</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>این spacing باید direct value بماند یا Utility logical شود؟</li>
<li>آیا Component واقعاً دو‌زبانه/جهت‌پذیر است؟</li>
<li>آیا left/right فیزیکی هدف واقعی است؟</li>
<li>آیا bdi/dir:auto برای dynamic text لازم است؟</li>
<li>آیا order بصری با reading/focus order سازگار است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — فعلاً logical utilityها را فقط برای patternهای تکراری بساز. همهٔ left/rightها را کورکورانه تبدیل نکن.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-15-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-15-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا TUYA باید از نظر RTL، Start/End، bidi و logical/physical decision قابل دفاع باشد؛ اما تصمیم‌های CTA، dynamic text و نسخهٔ انگلیسی هنوز باید با محتوای واقعی اعتبارسنجی شوند.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 15</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-15-completion">
<fieldset>
<legend>ثبت پایان درس 15</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-15-complete" name="lesson-15-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
