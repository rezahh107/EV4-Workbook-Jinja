<article class="lesson card-surface" data-lesson="17" id="lesson-17">

<h2 class="lesson-title former-h1">درس 17 — Classes، Variables و Components در Design System V4</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-17-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-17-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> قبل از ساخت هر چیز reusable، نوع تکرار را تشخیص بدهی: فقط مقدار؟ بستهٔ Style؟ یا Structure کامل؟ سپس بین Variable، Global Class و Component تصمیم بگیری.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Design System سازمانی کامل، معماری کامل Component Library، token governance، یا migration کامل همهٔ Styleها به سیستم نهایی.</p>
<p><strong>در پایان باید بتوانی:</strong> الگوهای تکراری TUYA را بدون Class Explosion و بدون Component زودهنگام سازمان بدهی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-17-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-17-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🧩 سیستم طراحی + 🛠 اجرایی محدود</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۳۵–۵۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> نوع تکرار، ابزار مناسب را تعیین می‌کند. اگر هنرجو برای هر تفاوت کوچک Class یا Component بسازد، سیستم طراحی قبل از کامل‌شدن، سنگین و شکننده می‌شود.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_design_system_reuse_decision_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-17-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-17-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>تا درس ۱۶، TUYA را از Structure تا State قابل استفاده ساختی. حالا مسئلهٔ اصلی نگهداری است: کدام تصمیم‌ها باید reusable شوند و کدام باید محلی بمانند؟</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Value
↓
Style Package
↓
Structure Pattern
↓
Design System Decision:
Variable / Global Class / Component / Local Adjustment</code></pre>
</figure>

<h3>مسئله</h3>
<p>بدون Design System، سایت پر از مقدارهای مشابه اما ناهماهنگ می‌شود. با Design System بد هم مشکل دیگری ساخته می‌شود: Variableهای بی‌مصرف، Classهای بیش‌ازحد و Componentهای زودهنگام.</p>
<p>هدف این درس این نیست که همه‌چیز را global کنیم؛ هدف این است که نوع تکرار را درست تشخیص بدهیم.</p>

<h3>Decision Tree اصلی</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="rtl"><code class="language-text inline-code">◇ فقط یک مقدار مشترک است؟
   ├─ بله → Variable، اگر نوع آن پشتیبانی شود
   └─ خیر
      ◇ مجموعه‌ای از Styleها تکرار می‌شود؟
         ├─ بله → Global Class
         └─ خیر
            ◇ Structure + Style + رفتار/محتوا تکرار می‌شود؟
               ├─ بله → Component candidate
               └─ خیر → Local adjustment</code></pre>
</figure>

<h3>سه مفهوم، سه سطح تکرار</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Variable</dt><dd>یک مقدار قابل استفادهٔ مجدد؛ مثل رنگ، spacing، radius یا font size. Variable ساختار نمی‌سازد.</dd>
<dt>Class</dt><dd>بسته‌ای از Styleها که روی Elementهای مشابه اعمال می‌شود. Class ساختار ایجاد نمی‌کند؛ ظاهر Element موجود را کنترل می‌کند.</dd>
<dt>Component</dt><dd>ساختار تکرارشونده شامل چند Element، نقش‌ها، Styleها و گاهی رفتار. Component فقط یک ظاهر نیست؛ یک الگوی ساختمانی است.</dd>
<dt>Local Adjustment</dt><dd>تفاوت خاص همان مورد؛ وقتی هنوز تکرار واقعی ثابت نشده است.</dd>
</dl>
</section>

<h3>قاعدهٔ کوتاه</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Repeated value       → Variable
Repeated style pack  → Global Class
Repeated structure   → Component
One-off exception    → Local adjustment</code></pre>
</figure>

<h3>Class Explosion چیست؟</h3>
<p>Class Explosion یعنی برای هر جزئیات کوچک یک Class بسازی: <code dir="ltr">button-blue</code>، <code dir="ltr">button-blue-big</code>، <code dir="ltr">button-blue-big-mobile</code>، <code dir="ltr">button-blue-big-mobile-2</code>. نتیجه، سیستم قابل نگهداری نیست؛ فقط شلوغی نام‌دار است.</p>

<h3>Component زودهنگام چیست؟</h3>
<p>اگر هنوز نمی‌دانی ساختار چند بار، با چه variationهایی و با چه content placeholderهایی تکرار می‌شود، Component ساختن ممکن است زود باشد. اول الگو را در چند مورد واقعی ببین؛ بعد Component candidate را ثبت کن.</p>

<h3>Shadow Variable trap</h3>
<p>اگر ابزار هدف، مقدار compound مثل shadow کامل را به‌عنوان Variable قابل اعتماد پشتیبانی نکند، اصرار نکن آن را Variable کنی. در این پروژه، shadowهای ترکیبی فعلاً در Global Class یا Local Class کنترل می‌شوند تا پشتیبانی واقعی ابزار روشن شود.</p>

<h3>Design System یعنی نقشهٔ تصمیم‌ها</h3>
<p>Design System فقط رنگ و فونت نیست. این‌ها را هم شامل می‌شود:</p>
<ul>
<li>چه چیزی Variable می‌شود؟</li>
<li>چه چیزی Class می‌شود؟</li>
<li>چه چیزی Component candidate است؟</li>
<li>چه چیزی Local می‌ماند؟</li>
<li>چه زمانی چیزی از Local به Global ارتقا پیدا می‌کند؟</li>
<li>چه زمانی باید Reset یا حذف شود؟</li>
</ul>

<h3>قاعدهٔ این درس</h3>
<p>قبل از ساخت هر Variable، Class یا Component، جملهٔ تصمیم را بنویس: «این مورد فقط مقدار تکراری است، یا بستهٔ Style، یا Structure کامل؟»</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-17.0.0" id="lesson-17-concept-reference">
<summary>📚 مرجع مفهومی کامل — Variable، Class و Component؛ سه ابزار برای سه نوع تکرار</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="17" data-source-version="tuya-revised-17.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی فعلی درس را حفظ می‌کند و آن را به تصمیم‌های واقعی TUYA وصل می‌کند. هدف، ساخت Design System عملی است؛ نه ساختن اسامی زیاد.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-17-ref-problem">
<h3 id="lesson-17-ref-problem">۱. مسئله‌ای که Design System حل می‌کند</h3>
<p>بدون سیستم، سایت با تصمیم‌های مشابه اما کمی متفاوت پر می‌شود:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">green #004526
green #004627
green #014526

padding 30px
padding 32px
padding 34px

radius 14px
radius 16px
radius 18px</code></pre>
</figure>
<p>هر مقدار ممکن است به‌تنهایی قابل دفاع باشد، اما کل سایت زبان مشترک خود را از دست می‌دهد.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-17-kitchen">
<h3 id="lesson-17-kitchen">۲. تشبیه آشپزخانهٔ زنجیره‌ای</h3>
<ul>
<li><strong>Variable:</strong> مواد اولیهٔ استاندارد؛ مثل مقدار نمک یا رنگ سس.</li>
<li><strong>Class:</strong> دستور پخت یک ظاهر؛ مثل پوشش مشترک چند غذا.</li>
<li><strong>Component:</strong> قالب کامل یک غذا؛ ظرف، مواد، ترتیب چیدمان و دستور سرو.</li>
</ul>
<p>اگر فقط نمک مشترک است، قالب کامل غذا نساز. اگر کل غذا تکرار می‌شود، فقط یک رنگ Variable کافی نیست.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-variable">
<h3 id="lesson-17-variable">۳. Variable؛ مقدار مشترک</h3>
<p>Variable وقتی مناسب است که یک مقدار در چند جای سیستم تکرار می‌شود و تغییر آن باید هماهنگ باشد.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Variable candidates">
<table class="data-table educational-table edu-table">
<caption>کاندیدهای Variable</caption>
<thead><tr><th scope="col">نوع مقدار</th><th scope="col">مثال</th><th scope="col">وضعیت در TUYA</th></tr></thead>
<tbody>
<tr><th scope="row">Color</th><td><code dir="ltr">tuya-green-900</code>، <code dir="ltr">tuya-gold-500</code></td><td><code dir="ltr">candidate</code></td></tr>
<tr><th scope="row">Spacing</th><td><code dir="ltr">space-4</code>، <code dir="ltr">space-6</code></td><td><code dir="ltr">candidate_after_usage</code></td></tr>
<tr><th scope="row">Radius</th><td><code dir="ltr">radius-card</code>، <code dir="ltr">radius-pill</code></td><td><code dir="ltr">candidate</code></td></tr>
<tr><th scope="row">Font Size</th><td><code dir="ltr">type-title</code>، <code dir="ltr">type-body</code></td><td><code dir="ltr">candidate_after_typography_test</code></td></tr>
<tr><th scope="row">Shadow compound</th><td>چند مقدار box-shadow</td><td><code dir="ltr">avoid_until_supported</code></td></tr>
</tbody>
</table>
</div>
<p>اگر Variable فقط یک بار استفاده شده، هنوز کاندید قطعی نیست. یک بار استفاده، معمولاً value است؛ نه system token.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-class">
<h3 id="lesson-17-class">۴. Class؛ بستهٔ Style</h3>
<p>Global Class وقتی مناسب است که چند Element باید یک بستهٔ Style مشترک داشته باشند. Class ظاهر را مدیریت می‌کند، اما Childهای ساختاری نمی‌سازد.</p>
<p>نمونه‌های TUYA:</p>
<ul>
<li><code dir="ltr">tuya-button-primary</code> برای CTAهای مشابه، اگر چند CTA واقعی وجود دارد؛</li>
<li><code dir="ltr">tuya-orbit-node</code> برای ظاهر مشترک Nodeها؛</li>
<li><code dir="ltr">tuya-feature-item</code> فقط اگر Feature Itemهای مشابه واقعاً تکرار شوند؛</li>
<li><code dir="ltr">tuya-logo-item</code> برای قاب Logoها، اگر pattern تکراری ثابت شود.</li>
</ul>
<p>Class را برای یک مقدار کوچک نساز. اگر فقط رنگ مشترک است، Variable کافی‌تر است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-component">
<h3 id="lesson-17-component">۵. Component؛ ساختار تکرارشونده</h3>
<p>Component وقتی مطرح می‌شود که Structure، Style و گاهی Behavior/State با هم تکرار می‌شوند. مثال:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Feature Item Component candidate
├── Icon / Dot
└── Text

Orbit Node Component candidate
├── Icon
├── Label
└── State / Focus / Hover, if interactive</code></pre>
</figure>
<p>اگر فقط ظاهر تکرار می‌شود اما ساختار متفاوت است، Global Class کافی‌تر است. اگر ساختار تکرار می‌شود اما هنوز variationها معلوم نیستند، Component candidate ثبت کن؛ Component نهایی نساز.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-tuya-inventory">
<h3 id="lesson-17-tuya-inventory">۶. Reuse Inventory برای TUYA</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA reuse inventory">
<table class="data-table educational-table edu-table">
<caption>Inventory اولیهٔ Reuse در TUYA</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">نوع تکرار</th><th scope="col">ابزار پیشنهادی</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">رنگ‌های برند</th><td>مقدار</td><td>Variable candidate</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Spacingهای رایج</th><td>مقدار</td><td>Variable candidate بعد از usage audit</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Primary CTA</th><td>Style + State</td><td>Global Class candidate</td><td><code dir="ltr">provisional_until_reuse</code></td></tr>
<tr><th scope="row">Orbit Node</th><td>Style مشترک؛ شاید Structure مشترک</td><td>Global Class اکنون، Component candidate بعداً</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Feature Item</th><td>Structure تکراری ساده</td><td>Component candidate فقط بعد از تکرار واقعی</td><td><code dir="ltr">candidate</code></td></tr>
<tr><th scope="row">Logo Item</th><td>Style قاب و sizing</td><td>Global Class candidate</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Visual Stage</th><td>ساختار خاص همین Hero</td><td>Local/Section pattern</td><td><code dir="ltr">local_until_reuse</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-naming">
<h3 id="lesson-17-naming">۷. Naming؛ اسم باید تصمیم را توضیح دهد</h3>
<p>نام بد مثل <code dir="ltr">green-box-2</code> آینده ندارد. نام خوب نقش و سطح را توضیح می‌دهد:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Naming examples">
<table class="data-table educational-table edu-table">
<caption>نمونهٔ نام‌گذاری</caption>
<thead><tr><th scope="col">بد</th><th scope="col">بهتر</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">green1</code></th><td><code dir="ltr">color-brand-primary</code></td><td>نقش رنگ را توضیح می‌دهد.</td></tr>
<tr><th scope="row"><code dir="ltr">box-32</code></th><td><code dir="ltr">space-section-inline</code></td><td>کاربرد spacing مشخص‌تر است.</td></tr>
<tr><th scope="row"><code dir="ltr">btn-big</code></th><td><code dir="ltr">button-primary</code></td><td>نقش component/style روشن‌تر است.</td></tr>
<tr><th scope="row"><code dir="ltr">node-style</code></th><td><code dir="ltr">orbit-node</code></td><td>Context و الگوی UI را نشان می‌دهد.</td></tr>
</tbody>
</table>
</div>
<p>اما نام‌گذاری را بیش از حد انتزاعی نکن. اگر هنوز pattern واقعی ثابت نشده، نام candidate یا local بماند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-promotion">
<h3 id="lesson-17-promotion">۸. چه زمانی Local را Global کنیم؟</h3>
<p>یک قانون عملی:</p>
<ol>
<li>اول Local بساز و با پروژه واقعی تست کن.</li>
<li>وقتی یک تصمیم حداقل در دو یا سه جای واقعی با intent مشابه تکرار شد، candidate ثبت کن.</li>
<li>اگر فقط مقدار تکرار شده، Variable کن.</li>
<li>اگر بستهٔ Style تکرار شده، Global Class کن.</li>
<li>اگر Structure کامل تکرار شده، Component candidate کن.</li>
<li>بعد از ارتقا، نمونه‌های پراکنده را به سیستم وصل کن.</li>
</ol>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-class-manager">
<h3 id="lesson-17-class-manager">۹. Class Manager و اولویت Classها</h3>
<p>در V4، Classها بخشی از ذهنیت سیستم طراحی هستند. اما مهم‌تر از پنل، تصمیم است: کدام Class در حال ویرایش است؟ آیا Local Class دارد override می‌کند؟ آیا Global Class واقعاً shared است؟</p>
<p>قبل از تغییر Style، همان قاعدهٔ درس ۳ را تکرار کن:</p>
<ul>
<li>Element درست را انتخاب کرده‌ای؟</li>
<li>Class درست را ویرایش می‌کنی؟</li>
<li>Local override ناخواسته داری؟</li>
<li>State/Device درست است؟</li>
<li>این تغییر باید shared باشد یا local؟</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-avoid">
<h3 id="lesson-17-avoid">۱۰. چه چیزهایی را فعلاً Global نکن؟</h3>
<ul>
<li>Offsetهای provisional Nodeها؛</li>
<li>z-indexهای provisional Stage؛</li>
<li>Responsive overrideهایی که هنوز با Resize test ثابت نشده‌اند؛</li>
<li>Shadowهای compound که پشتیبانی Variable آن روشن نیست؛</li>
<li>Styleهای فقط یک‌بار مصرف؛</li>
<li>Componentهایی که variationهای واقعی‌شان مشخص نیست؛</li>
<li>CTA state tokenهای نهایی قبل از تست contrast/focus.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-17-debug">
<h3 id="lesson-17-debug">۱۱. Debug Design System</h3>
<p>اگر سیستم طراحی شلوغ شده، این سؤالات را بپرس:</p>
<ol>
<li>آیا این Class فقط یک مقدار را تکرار می‌کند؟ پس شاید Variable کافی است.</li>
<li>آیا این Variable فقط یک بار استفاده شده؟ پس شاید premature token است.</li>
<li>آیا این Component فقط یک Style مشترک دارد؟ پس شاید Class کافی است.</li>
<li>آیا Local overrideها رفتار Global Class را پنهان کرده‌اند؟</li>
<li>آیا نام‌ها نقش را توضیح می‌دهند یا فقط ظاهر لحظه‌ای را؟</li>
<li>آیا State/Responsive/RTL variationها ثبت شده‌اند؟</li>
</ol>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-17-traps">
<h3 id="lesson-17-traps">۱۲. اشتباهات رایج</h3>
<ul>
<li>برای هر رنگ یک Class ساختن؛</li>
<li>برای هر کارت یک Component جدا ساختن؛</li>
<li>Variable ساختن برای مقداری که فقط یک بار استفاده شده؛</li>
<li>Global کردن offsetهای provisional؛</li>
<li>Class جدید برای هر Device/State بدون ساختار naming؛</li>
<li>فراموش‌کردن Class target و ویرایش اشتباه Local/Global؛</li>
<li>تبدیل کورکورانهٔ همه‌چیز به system token؛</li>
<li>نداشتن گزارش promotion از Local به Global.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-17-golden">
<h3 id="lesson-17-golden">۱۳. قوانین طلایی</h3>
<ul>
<li><strong>همهٔ تکرارها Component نمی‌خواهند.</strong></li>
<li><strong>همهٔ مقدارهای یک‌بارمصرف Variable نمی‌خواهند.</strong></li>
<li><strong>Class ظاهر را تکرار می‌کند؛ Component ساختار را.</strong></li>
<li><strong>Variable مقدار را نگه می‌دارد؛ نه رفتار و نه ساختار.</strong></li>
<li><strong>اول Local، بعد evidence، بعد promotion.</strong></li>
<li><strong>Global کردن تصمیم provisional یعنی بدهی سیستم طراحی.</strong></li>
<li><strong>نام‌ها باید نقش و intent را توضیح دهند، نه فقط ظاهر لحظه‌ای.</strong></li>
<li><strong>Class Explosion را با Decision Tree کنترل کن.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>این درس بر مبنای مدل مفهومی V4 برای Classes، Variables و Components، و زنجیرهٔ آموزشی قبلی نوشته شده است. جزئیات دقیق پنل، نوع Variableهای پشتیبانی‌شده، و رفتار Componentها باید در نسخهٔ هدف Elementor V4 اعتبارسنجی شوند.</p>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-17-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-17-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Variable، Class، Component و Promotion</span>
</summary>
<section aria-labelledby="lesson-17-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در این درس مهم‌ترین «واحد» عدد نیست؛ سطح reuse است. مقدار، Style، Structure و State هرکدام ابزار متفاوت می‌خواهند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۷" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>سطح reuse، ابزار و تله</caption>
<thead><tr><th scope="col">سطح</th><th scope="col">ابزار</th><th scope="col">مثال</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Value</th><td>Variable</td><td>رنگ، spacing، radius، size</td><td>Variable برای ساختار بسازی.</td></tr>
<tr><th scope="row">Style Pack</th><td>Global Class</td><td>button-primary، orbit-node</td><td>برای هر مقدار کوچک Class بسازی.</td></tr>
<tr><th scope="row">Structure</th><td>Component candidate</td><td>Feature Item، Card pattern</td><td>Component زودهنگام بسازی.</td></tr>
<tr><th scope="row">Exception</th><td>Local adjustment</td><td>یک مورد خاص</td><td>استثنا را بی‌دلیل Global کنی.</td></tr>
<tr><th scope="row">State variation</th><td>Class state / token candidate</td><td>focus ring، hover</td><td>قبل از تست accessibility token نهایی بسازی.</td></tr>
<tr><th scope="row">Responsive variation</th><td>Device override / token candidate</td><td>gap mobile</td><td>مقدار provisional را global کنی.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر یک رنگ در ۶ جای مختلف با intent برند استفاده شده، Variable candidate است. اگر یک دکمه با ۶ property مشترک در چند جای واقعی تکرار شده، Global Class candidate است.</p></section>
<section><h3>📱 در Responsive</h3><p>Responsive overrideها را فوری token نکن. اول شکست واقعی و قرارداد دستگاه‌ها ثابت شود.</p></section>
<section><h3>🔬 در Debug</h3><p>وقتی Style تغییر نمی‌کند، Class target، Local override، Device mode و State فعال را بررسی کن.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-17-reuse-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Variable، Class یا Component؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر سناریو را اول تصمیم بگیر، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Reuse Decision Step Through">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تصمیم‌های reuse</caption>
<thead><tr><th scope="col">سناریو</th><th scope="col">نوع تکرار</th><th scope="col">تصمیم</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">یک رنگ برند در چند جای واقعی</th><td>Value</td><td>Variable candidate</td><td>فقط مقدار مشترک است.</td></tr>
<tr><th scope="row">چند CTA با font، padding، radius، state مشابه</th><td>Style Pack</td><td>Global Class candidate</td><td>بستهٔ Style تکرار شده است.</td></tr>
<tr><th scope="row">چند Feature Item با Icon و Text</th><td>Structure</td><td>Component candidate</td><td>ساختار Childها تکرار شده است.</td></tr>
<tr><th scope="row">یک Node با offset خاص فقط در یک Hero</th><td>Exception</td><td>Local adjustment</td><td>تکرار واقعی ثابت نشده است.</td></tr>
<tr><th scope="row">Shadow compound نامطمئن</th><td>Style Pack / unsupported variable</td><td>Class، نه Variable قطعی</td><td>پشتیبانی ابزار باید بررسی شود.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-17-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-17-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Reuse Audit، نه Design System کامل</h3>
<p>در این تمرین فقط Inventory می‌سازی و تصمیم‌ها را طبقه‌بندی می‌کنی. هنوز Design System سازمانی، Component Library، token governance یا migration کامل انجام نمی‌دهی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 17">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Reuse Decision</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Variable برای مقدار، Class برای بستهٔ Style، Component برای ساختار تکراری است.</td><td>Decision Tree اجرا می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>همهٔ تکرارها Component نمی‌خواهند.</td><td>Component زودهنگام ممنوع است.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>کاندیدهای TUYA برای Variable/Class/Component.</td><td>با تکرار واقعی و UI نسخهٔ هدف اعتبارسنجی می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>پشتیبانی دقیق Variableها، Component workflow، Shadow variable support.</td><td>بدون تست نسخهٔ هدف قطعی نشود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Inventory بنویس</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس هفده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> تشخیص نوع تکرار، نه ساختن سیستم نهایی.</p>
<p><strong>مسیر:</strong> Elementor Editor → TUYA Section → مرور رنگ‌ها، spacing، CTA، Logo Item، Feature Item، Orbit Node، Visual Stage.</p>
<p><strong>Element هدف:</strong> کل TUYA برای Audit؛ اما تغییر مستقیم فقط بعد از تصمیم مستند.</p>
<p><strong>Class فعال:</strong> Classهای موجود را مشاهده کن؛ Class/Variable/Component جدید را فعلاً فقط candidate ثبت کن.</p>
<p><strong>Property:</strong> Reuse type / promotion status / naming candidate.</p>
<p><strong>نباید تغییر کند:</strong> Layout، Responsive، RTL، State، Position نهایی، Token سراسری، Component نهایی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Reuse Inventory نوشته شد و هیچ Global/Component نهایی بدون evidence ساخته نشد.»</p>
</aside>

<h3>مرحلهٔ ۲ — TUYA Reuse Inventory</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA Reuse Audit">
<table class="data-table educational-table edu-table">
<caption>جدول Audit تکرار در TUYA</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">تکرار دیده‌شده</th><th scope="col">ابزار candidate</th><th scope="col">نام candidate</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Brand Green</th><td>Value</td><td>Variable</td><td><code dir="ltr">color-brand-primary</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Brand Gold</th><td>Value</td><td>Variable</td><td><code dir="ltr">color-accent-gold</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Section Padding</th><td>Value</td><td>Variable بعد از usage audit</td><td><code dir="ltr">space-section-inline</code></td><td><code dir="ltr">candidate</code></td></tr>
<tr><th scope="row">Primary CTA</th><td>Style + State</td><td>Global Class</td><td><code dir="ltr">button-primary</code></td><td><code dir="ltr">candidate_until_reuse</code></td></tr>
<tr><th scope="row">Orbit Node</th><td>Style مشترک</td><td>Global Class اکنون، Component بعداً</td><td><code dir="ltr">orbit-node</code></td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Feature Item</th><td>Structure ساده</td><td>Component candidate</td><td><code dir="ltr">feature-item</code></td><td><code dir="ltr">candidate_until_variants</code></td></tr>
<tr><th scope="row">Visual Stage</th><td>ساختار خاص Hero</td><td>Local pattern</td><td><code dir="ltr">tuya-visual-stage</code></td><td><code dir="ltr">local_until_reuse</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — Promotion Rule را بنویس</h3>
<p>برای هر candidate این جمله را کامل کن:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="rtl"><code class="language-text inline-code">این مورد فعلاً Local / Candidate / Global است،
چون فقط مقدار / Style / Structure تکرار شده،
و قبل از ارتقا باید این شواهد را داشته باشد:
- تکرار واقعی در حداقل دو جای پروژه
- نیاز مشترک
- variationهای شناخته‌شده
- State/Responsive/RTL مشخص</code></pre>
</figure>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر فقط رنگ طلایی در چند جای TUYA تکرار شده، ابزار مناسب‌تر چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-17">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-17-a" name="stop-question-17" type="radio" value="A"/><span>A) Component بسازم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-17-b" name="stop-question-17" type="radio" value="B"/><span>B) Variable candidate ثبت کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-17-c" name="stop-question-17" type="radio" value="C"/><span>C) برای هر مورد Class جدا بسازم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> اگر فقط مقدار رنگ تکرار شده، Variable candidate منطقی‌تر است. Component برای ساختار تکراری است و Class برای بستهٔ Style.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> هر چیز تکراری را Component کنی یا هر مقدار را Class کنی.</p>
<p><strong>نشانه:</strong> لیست Classها و Componentها زیاد شده اما تصمیم‌ها شفاف‌تر نشده‌اند.</p>
<p><strong>قاعده:</strong> اول نوع تکرار؛ بعد ابزار.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<figure class="visual-figure ascii-figure">
<figcaption>Design System خراب</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code">button-green-big
button-green-big-hover
button-green-big-mobile
button-gold-big-mobile
feature-card-1
feature-card-2

نتیجه:
- Class Explosion
- Componentهای بی‌معنا
- تغییرات سراسری سخت
- Local overrideهای پنهان</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-97">
<fieldset>
<legend>Checkpoint درس ۱۷</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-97-1" name="chk-97-1" type="checkbox"/><span>می‌توانم Variable، Class و Component را با نوع تکرار توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-97-2" name="chk-97-2" type="checkbox"/><span>برای TUYA یک Reuse Inventory نوشته‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-97-3" name="chk-97-3" type="checkbox"/><span>Component زودهنگام نساخته‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-97-4" name="chk-97-4" type="checkbox"/><span>Class Explosion را با Decision Tree کنترل کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-97-5" name="chk-97-5" type="checkbox"/><span>Shadow compound را بدون شواهد پشتیبانی Variable نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-97-6" name="chk-97-6" type="checkbox"/><span>هیچ Token/Global نهایی بدون evidence واقعی نساخته‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> برای هرکدام یک مثال بزن: Variable، Global Class، Component.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر سه Pricing Card داری که ساختار مشترک، قیمت، CTA و Feature List دارند، چه چیزی Variable است، چه چیزی Class، و چه چیزی Component candidate؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید رنگ/spacing/radius را Variable candidate، ظاهر CTA/Card را Class candidate، و ساختار کامل Pricing Card را Component candidate بداند؛ اما قبل از Component نهایی variationها را بررسی کند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-17-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Reuse در Deviceها</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_system_validation</code></p>
<ul>
<li>Responsive overrideهای ناپایدار را Token سراسری نکن.</li>
<li>Classهای Device-specific را بدون naming strategy نساز.</li>
<li>اگر Mobile فقط تفاوت محلی دارد، Local adjustment یا Device override کافی است.</li>
<li>اگر pattern responsive در چند Component تکرار شد، آن وقت token/class candidate ثبت کن.</li>
<li>Component باید variationهای Desktop/Tablet/Mobile را هم در نظر بگیرد.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-17-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-17-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Class Explosion</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">system_audit</code></p>
<p>سناریو: پروژه ده‌ها Class شبیه هم دارد و هیچ‌کس نمی‌داند کدام را باید ویرایش کند.</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>کدام Classها فقط مقدار رنگ/spacing را تکرار می‌کنند؟</li>
<li>کدام Classها بستهٔ Style واقعی هستند؟</li>
<li>کدام Classها به خاطر Device/State ساخته شده‌اند؟</li>
<li>کدام Local overrideها رفتار Global Class را پنهان کرده‌اند؟</li>
<li>آیا naming strategy نقش را توضیح می‌دهد؟</li>
<li>آیا بعضی Classها باید حذف و به Variable متصل شوند؟</li>
</ul>
</section>
<p>نتیجهٔ درست: حذف و ادغام بی‌برنامه نکن. اول inventory، بعد mapping، بعد migration کوچک.</p>

<h3>🔬 پشت صحنه</h3>
<p>در Class Manager یا پنل Classها، همیشه active editing target را ببین. تغییر روی Local Class می‌تواند باعث شود Global Class ظاهراً کار نکند. State و Device mode هم می‌توانند نتیجه را تغییر دهند.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-17-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-17-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-100">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-100-1" name="chk-100-1" type="checkbox"/><span>می‌توانم Variable، Class و Component را براساس نوع تکرار تفکیک کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-100-2" name="chk-100-2" type="checkbox"/><span>می‌دانم Class ظاهر را تکرار می‌کند و Component ساختار را.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-100-3" name="chk-100-3" type="checkbox"/><span>می‌دانم Local adjustment همیشه خطا نیست و گاهی انتخاب درست است.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-101">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-101-1" name="chk-101-1" type="checkbox"/><span>برای TUYA Reuse Inventory و Promotion Rule می‌نویسم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-101-2" name="chk-101-2" type="checkbox"/><span>قبل از Global کردن، evidence واقعی تکرار و intent مشترک را بررسی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-101-3" name="chk-101-3" type="checkbox"/><span>از ساخت Component زودهنگام و Class Explosion پرهیز می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-102">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-102-1" name="chk-102-1" type="checkbox"/><span>برای یک Pricing Card می‌توانم Variable، Class و Component candidateها را تفکیک کنم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-17-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Promotion از Local به Global</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>آیا فقط مقدار تکرار شده یا بستهٔ Style یا Structure کامل؟</li>
<li>آیا حداقل دو استفادهٔ واقعی با intent مشابه داریم؟</li>
<li>آیا State، Responsive و RTL variationها مشخص‌اند؟</li>
<li>آیا نام پیشنهادی نقش را توضیح می‌دهد؟</li>
<li>آیا Local override ناخواسته وجود دارد؟</li>
<li>آیا این تصمیم اگر Global شود، بدهی سیستم طراحی می‌سازد؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — اول inventory و candidate، بعد promotion کوچک و مستند. هیچ Global/Component نهایی بدون evidence واقعی نساز.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-17-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-17-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا TUYA باید Reuse Inventory اولیه داشته باشد، اما Design System نهایی هنوز ساخته نشده است.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 17</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-17-completion">
<fieldset>
<legend>ثبت پایان درس 17</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-17-complete" name="lesson-17-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
