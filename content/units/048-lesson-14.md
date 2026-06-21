<article class="lesson card-surface" data-lesson="14" id="lesson-14">

<h2 class="lesson-title former-h1">درس 14 — Responsive Inheritance و Breakpointها</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-14-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-14-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> Responsive را به‌عنوان تغییر کنترل‌شدهٔ همان ساختار بفهمی؛ یعنی یک DOM، یک Section و یک Component را در عرض‌های مختلف با Overrideهای حداقلی و مستند تطبیق بدهی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> ساخت Section جدا برای هر دستگاه، Container Query عملی در پنل V4، Performance کامل Responsive، یا Breakpointهای قطعی بدون خواندن تنظیمات واقعی سایت.</p>
<p><strong>در پایان باید بتوانی:</strong> TUYA را بدون Duplicate از Desktop به Mobile تبدیل کنی، Responsive Contract بنویسی، و بدانی چه چیزی inherited است، چه چیزی override شده و چه چیزی باید Reset شود.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-14-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-14-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🛠 اجرایی + 🔍 عیب‌یابی + 📱 چندعرضی</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۴۰–۶۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس باید با چند Viewport و یک DOM تست شود. اگر هنرجو برای Mobile نسخهٔ جدا بسازد، مسئله را حل نکرده؛ نگهداری را سخت‌تر کرده است.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_responsive_inheritance_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-14-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-14-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>تا درس ۱۳، Structure، Layout، Typography، Media، Position و Layering را ساختی. حالا باید همهٔ این تصمیم‌ها را در عرض‌های مختلف نگه داری. Responsive یعنی همان ساختار، اما با تغییرهای کنترل‌شده و حداقلی.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Base / Desktop
↓
Inherited values
↓
Tablet override only if needed
↓
Mobile override only if needed
↓
Reset if override is no longer needed</code></pre>
</figure>

<h3>مسئله</h3>
<p>اگر در Desktop چیزی خوب دیده شود، الزاماً در Tablet و Mobile خوب نیست. اما راه‌حل هم ساختن سه Section جدا نیست. باید بفهمی کدام مقدار از Desktop به پایین ارث می‌رسد، کجا واقعاً شکست رخ داده، و کدام کنترل با کمترین تغییر باید override شود.</p>

<h3>مدل آبشار</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<p>Desktop مثل سرچشمه است. مقدارها به Tablet و Mobile می‌ریزند، مگر اینکه در یکی از دستگاه‌ها مقدار مستقل بسازی.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop: 40px
Tablet:  inherit
Mobile:  16px  ← local override</code></pre>
</figure>
<p>اگر بعداً Desktop را 48px کنی، Mobile همچنان 16px می‌ماند؛ چون سد محلی دارد.</p>
</section>

<h3>Override با Copy کردن مقدار فرق دارد</h3>
<p>اگر در Mobile همان مقدار Desktop را دستی وارد کنی، ظاهراً یکسان است، اما دیگر inherited نیست. این کار Maintenance را سخت می‌کند. مقدار صریح را فقط وقتی بساز که تفاوت رفتاری واقعی لازم است.</p>

<h3>Reset یعنی حذف مقدار محلی</h3>
<p>اگر یک مقدار Mobile دیگر لازم نیست، آن را با کپی‌کردن Desktop «هم‌شکل» نکن؛ مقدار محلی را Reset/پاک کن تا دوباره از مقدار بالاتر پیروی کند.</p>

<h3>Breakpoint براساس شکست محتواست، نه نام دستگاه</h3>
<p>Breakpoint نباید فقط چون نامش Tablet یا Mobile است تغییر بگیرد. سؤال درست این است:</p>
<blockquote><p>Layout در چه عرضی دیگر قرارداد فعلی را حفظ نمی‌کند؟</p></blockquote>
<p>ممکن است Hero در ۸۷۰px بشکند، نه در عدد اسمی Tablet. Breakpointهای واقعی Elementor هم باید از تنظیمات سایت خوانده شوند، نه از حافظه یا حدس.</p>

<h3>Responsive Contract قبل از عدد</h3>
<p>قبل از واردکردن هر عدد، قرارداد Responsive بنویس:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop:
- Shell row
- Copy / Visual کنار هم
- Visual Stage کامل
- Logo Strip یک یا دو خط کنترل‌شده

Tablet:
- Row یا Column؟ وابسته به شکست محتوا
- Gap کمتر فقط در صورت نیاز
- Heading و Stage بازبینی شوند

Mobile:
- Shell column
- Copy اول
- Visual بعد از متن یا طبق UX
- Button تمام‌عرض در صورت نیاز
- تزئین محدود
- Nodeها ساده‌تر، نه نسخهٔ جدا</code></pre>
</figure>

<h3>Responsive یعنی Duplicate نه</h3>
<p>ساخت Section جدا برای Desktop/Tablet/Mobile آخرین راه‌حل است، نه شروع کار. Duplicate کردن سکشن‌ها باعث مشکل محتوا، SEO، Accessibility، Maintenance، Performance و هماهنگی Design System می‌شود.</p>

<h3>Fluid و Breakpoint مکمل‌اند</h3>
<p>بعضی چیزها مثل spacing و typography می‌توانند سیال باشند؛ مثلاً با clamp. اما تغییر ساختار از Row به Column با clamp حل نمی‌شود. پس Responsive دو ابزار دارد: تغییر سیال و تغییر نقطه‌ای.</p>

<h3>قاعدهٔ این درس</h3>
<p>از Desktop شروع کن، عرض را آهسته کم کن، اولین شکست واقعی را پیدا کن، فقط کمترین کنترل لازم را تغییر بده، و بعد inheritance/override/reset را مستند کن.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-14.0.0" id="lesson-14-concept-reference">
<summary>📚 مرجع مفهومی کامل — Responsive Inheritance، Override، Reset و Breakpoint</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="14" data-source-version="tuya-revised-14.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی فعلی درس را حفظ می‌کند و آن را به تصمیم‌های TUYA وصل می‌کند. هدف، تبدیل Desktop به Mobile با همان DOM است؛ نه ساخت چند نسخهٔ جدا.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-14-ref-problem">
<h3 id="lesson-14-ref-problem">۱. مسئله‌ای که Responsive حل می‌کند</h3>
<p>Responsive یعنی Layout بتواند با فضای متفاوت، محتوای متفاوت و روش تعامل متفاوت سازگار شود. Responsive فقط کوچک‌کردن Desktop نیست. گاهی در Mobile باید Direction عوض شود، دکمه تمام‌عرض شود، Grid ستون کمتری بگیرد، Typography سیال شود یا تزئین حذف/ساده شود.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-14-waterfall">
<h3 id="lesson-14-waterfall">۲. تشبیه آبشار و سدها</h3>
<p>مقدارها از Base/Desktop به پایین می‌آیند:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop
  ↓
Tablet
  ↓
Mobile</code></pre>
</figure>
<p>وقتی در Mobile مقدار مستقل وارد می‌کنی، یک سد محلی ساخته‌ای. این سد تا وقتی Reset نشود، از Desktop جدید پیروی نمی‌کند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-inheritance">
<h3 id="lesson-14-inheritance">۳. Inheritance و Responsive Override</h3>
<p>در Elementor، بسیاری از کنترل‌ها می‌توانند در Device Mode متفاوت مقدار بگیرند. اگر برای دستگاه پایین‌تر مقدار مستقل نداشته باشی، مقدار بالاتر یا Base رفتار را تعیین می‌کند. اما وقتی مقدار محلی ساختی، آن دستگاه مستقل می‌شود.</p>
<p>قانون عملی:</p>
<ul>
<li>اول مقدار Base را درست کن.</li>
<li>در Tablet/Mobile فقط وقتی override بساز که شکست واقعی رخ داده باشد.</li>
<li>اگر تفاوت دیگر لازم نیست، Reset کن.</li>
<li>مقدار بالاتر را فقط برای شبیه‌کردن ظاهری در دستگاه پایین‌تر کپی نکن.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-breakpoint">
<h3 id="lesson-14-breakpoint">۴. Breakpoint را از شکست محتوا استخراج کن</h3>
<p>Breakpoint مرز فعال‌شدن Styleهاست. اما عدد Breakpoint باید از مشاهدهٔ شکست Layout و تنظیمات واقعی سایت بیاید. نام دستگاه کافی نیست.</p>
<p>روش مشاهده:</p>
<ol>
<li>Desktop را پایدار کن.</li>
<li>عرض را آرام کم کن.</li>
<li>اولین شکست واقعی را پیدا کن: برخورد، overflow، خوانایی بد، فشردگی، crop، line break بد.</li>
<li>نوع شکست را طبقه‌بندی کن.</li>
<li>کمترین کنترل لازم را تغییر بده.</li>
<li>دوباره از Desktop تا Mobile تست کن.</li>
</ol>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-contract">
<h3 id="lesson-14-contract">۵. Responsive Contract برای TUYA</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA Responsive Contract">
<table class="data-table educational-table edu-table">
<caption>Responsive Contract پیشنهادی TUYA</caption>
<thead><tr><th scope="col">Viewport</th><th scope="col">قرارداد رفتاری</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Desktop</th><td>Shell در Row؛ Copy و Visual کنار هم؛ Stage کامل؛ Logo Strip با Wrap کنترل‌شده.</td><td><code dir="ltr">confirmed_goal</code></td></tr>
<tr><th scope="row">Tablet</th><td>Row فشرده یا Column؛ تصمیم وابسته به اولین شکست واقعی.</td><td><code dir="ltr">provisional_until_resize_test</code></td></tr>
<tr><th scope="row">Mobile</th><td>Shell معمولاً Column؛ Copy اول؛ Visual ساده‌تر؛ دکمه/CTA در صورت نیاز تمام‌عرض؛ تزئین محدود.</td><td><code dir="ltr">provisional_until_content_test</code></td></tr>
<tr><th scope="row">Between Breakpoints</th><td>عرض‌های بینابینی هم باید تست شوند، نه فقط آیکن‌های دستگاه.</td><td><code dir="ltr">required_check</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-tunya-controls">
<h3 id="lesson-14-tunya-controls">۶. چه کنترل‌هایی احتمالاً Responsive می‌شوند؟</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Responsive controls">
<table class="data-table educational-table edu-table">
<caption>کنترل‌های محتمل در TUYA</caption>
<thead><tr><th scope="col">بخش</th><th scope="col">کنترل محتمل</th><th scope="col">قاعده</th></tr></thead>
<tbody>
<tr><th scope="row">TUYA Shell</th><td>Direction، Gap، Padding</td><td>اولین شکست Layout را ببین؛ فقط حداقل override.</td></tr>
<tr><th scope="row">Copy / Visual</th><td>Basis، Width، Order</td><td>Order فقط با دلیل UX و بررسی reading/focus order.</td></tr>
<tr><th scope="row">Typography</th><td>Font size، line-height، max width</td><td>متن واقعی فارسی و Mobile تست شود.</td></tr>
<tr><th scope="row">Logo Strip</th><td>Gap، max-size، wrap</td><td>Hide فقط با دلیل محتوایی؛ اول Wrap/Size.</td></tr>
<tr><th scope="row">Visual Stage</th><td>Aspect ratio، max-size، Node offsets</td><td>Position نهایی هنوز provisional است.</td></tr>
<tr><th scope="row">Layering</th><td>Overflow و z-index</td><td>در Mobile clipping را جدا بررسی کن.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-fluid">
<h3 id="lesson-14-fluid">۷. Fluid Typography و Spacing</h3>
<p>Responsive همیشه با چند پرش Breakpoint انجام نمی‌شود. برای بعضی اندازه‌ها می‌توان از مقدارهای سیال استفاده کرد:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">padding-inline: clamp(1rem, 4vw, 5rem);
font-size: clamp(2rem, 1.25rem + 3vw, 4.5rem);</code></pre>
</figure>
<p>اما اگر ساختار باید از Row به Column تغییر کند، مقدار سیال جای تغییر Layout را نمی‌گیرد. Fluid value و Breakpoint override مکمل‌اند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-container-query">
<h3 id="lesson-14-container-query">۸. Container Query در حد آشنایی</h3>
<p>Media Query به Viewport نگاه می‌کند؛ Container Query به فضای خود Component. این مفهوم برای Componentهای قابل استفاده در چند محیط مهم است.</p>
<p>اما در این درس، Container Query را به‌عنوان CSS پیشرفته می‌شناسیم، نه کنترل قطعی پنل. برای Elementor V4، وجود کنترل Native قطعی در پنل را بدون شواهد نسخهٔ هدف ادعا نکن. اگر لازم شد، باید با Custom CSS و تست نسخهٔ واقعی بررسی شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-duplicate">
<h3 id="lesson-14-duplicate">۹. چرا Duplicate Section خطرناک است؟</h3>
<p>Duplicate کردن سکشن برای هر دستگاه شاید سریع به نظر برسد، اما هزینه دارد:</p>
<ul>
<li>متن باید در چند جای مختلف به‌روزرسانی شود؛</li>
<li>Screen Reader ممکن است محتوای تکراری ببیند، اگر پنهان‌سازی درست نباشد؛</li>
<li>Performance افت می‌کند؛</li>
<li>Design System و Classها چندشاخه می‌شوند؛</li>
<li>Debug سخت‌تر می‌شود.</li>
</ul>
<p>Duplicate فقط برای موارد بسیار خاص و با دلیل مستند قابل بررسی است؛ نه به‌عنوان روش آموزشی این پروژه.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-14-debug">
<h3 id="lesson-14-debug">۱۰. Debug Responsive</h3>
<p>اگر Mobile خراب است، این ترتیب را رعایت کن:</p>
<ol>
<li>مشکل از Layout است یا Typography یا Media یا Position یا Layering؟</li>
<li>آیا مقدار از Desktop inherited است یا Mobile override دارد؟</li>
<li>آیا override ضروری است یا باید Reset شود؟</li>
<li>آیا مشکل با یک کنترل حل می‌شود یا چند کنترل را بی‌دلیل تغییر داده‌ای؟</li>
<li>آیا فقط breakpoint iconها را تست کرده‌ای یا عرض‌های بینابینی را هم دیده‌ای؟</li>
<li>آیا content واقعی و states واقعی تست شده‌اند؟</li>
</ol>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-14-golden">
<h3 id="lesson-14-golden">۱۱. قوانین طلایی</h3>
<ul>
<li><strong>Responsive یعنی همان DOM با تغییر کنترل‌شده، نه نسخهٔ جدا برای هر دستگاه.</strong></li>
<li><strong>Breakpoint را از شکست محتوا بگیر، نه از نام دستگاه.</strong></li>
<li><strong>Override فقط وقتی لازم است که رفتار واقعاً باید فرق کند.</strong></li>
<li><strong>Reset یعنی بازگشت به مقدار بالاتر، نه کپی دستی مقدار Desktop.</strong></li>
<li><strong>اول قرارداد Responsive را بنویس، بعد عدد بده.</strong></li>
<li><strong>بین Breakpointها را هم تست کن.</strong></li>
<li><strong>Container Query را بدون شواهد نسخهٔ هدف به‌عنوان کنترل پنل V4 ادعا نکن.</strong></li>
<li><strong>Duplicate Section آخرین راه‌حل است، نه شروع کار.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفاهیم Responsive Inheritance، Override، Breakpoint، Media Query، Container Query و clamp بر پایهٔ CSS و رفتار ابزارهای responsive نوشته شده‌اند. Breakpointهای واقعی Elementor باید از تنظیمات سایت خوانده شوند و در این درس قطعی اعلام نمی‌شوند.</p>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/" rel="noopener noreferrer" target="_blank">Elementor — Responsive editing</a></li>
<li><a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries" rel="noopener noreferrer" target="_blank">MDN — Media queries</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries" rel="noopener noreferrer" target="_blank">MDN — Container queries</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/clamp" rel="noopener noreferrer" target="_blank">MDN — clamp()</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-14-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-14-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Breakpoint، Override، Reset، clamp و Responsive values</span>
</summary>
<section aria-labelledby="lesson-14-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در Responsive، مقدار مهم است؛ اما مهم‌تر این است که مقدار inherited است یا override محلی. یک عدد یکسان می‌تواند نگهداری متفاوتی داشته باشد.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۴" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Breakpoint</th><td>px/rem threshold</td><td>تنظیمات سایت و شکست محتوا</td><td>عدد فرضی را قانون جزوه کنی.</td></tr>
<tr><th scope="row">Device Override</th><td>local value</td><td>Device Mode</td><td>مقدار Desktop را بی‌دلیل کپی کنی.</td></tr>
<tr><th scope="row">Reset</th><td>حذف مقدار محلی</td><td>cascade بالاتر</td><td>به‌جای Reset، مقدار مشابه دستی وارد شود.</td></tr>
<tr><th scope="row">clamp()</th><td>min / preferred / max</td><td>viewport یا container context</td><td>جایگزین تغییر ساختار Row/Column فرض شود.</td></tr>
<tr><th scope="row">Order</th><td>number</td><td>visual order در flex/grid</td><td>با reading/focus order یکی فرض شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Mobile مقدار 24px دارد و Desktop بعداً از 32px به 40px تغییر کند، Mobile همچنان 24px می‌ماند. اگر Mobile باید پیرو Desktop باشد، مقدار محلی را Reset کن.</p></section>
<section><h3>📱 در Responsive</h3><p>فقط Desktop/Tablet/Mobile iconها را تست نکن. عرض‌های بینابینی مثل 900، 780، 640، 480 و 360 را هم بررسی کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>Computed Style، Media Query active، class target، و overrideهای Device Mode را با هم بخوان. ظاهر نهایی به‌تنهایی نمی‌گوید مقدار inherited است یا override.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-14-responsive-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Inherit، Override یا Reset؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر حالت را پیش‌بینی کن، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Responsive Step Through">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ حالت‌های Responsive</caption>
<thead><tr><th scope="col">حالت</th><th scope="col">وضعیت</th><th scope="col">چه چیزی یاد می‌گیری؟</th><th scope="col">قانون طلایی</th></tr></thead>
<tbody>
<tr><th scope="row">۱</th><td>Desktop padding 40px، Mobile بدون مقدار</td><td>Mobile inherited است.</td><td>بدون نیاز، override نساز.</td></tr>
<tr><th scope="row">۲</th><td>Mobile padding 16px</td><td>Mobile مستقل شده است.</td><td>Override فقط با دلیل.</td></tr>
<tr><th scope="row">۳</th><td>Mobile دستی 40px، مثل Desktop</td><td>ظاهر برابر، اما cascade شکسته است.</td><td>برابری ظاهری یعنی inheritance نیست.</td></tr>
<tr><th scope="row">۴</th><td>Reset مقدار Mobile</td><td>Mobile دوباره از بالا پیروی می‌کند.</td><td>Reset برای پاک‌کردن سد محلی.</td></tr>
<tr><th scope="row">۵</th><td>Row به Column</td><td>ساختار واقعاً متفاوت شده است.</td><td>clamp جای تغییر Layout را نمی‌گیرد.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-14-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-14-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Responsive Contract بدون Duplicate</h3>
<p>در این تمرین، TUYA را از Desktop تا Mobile با همان DOM بررسی می‌کنی. هنوز Section جدا، Container Query عملی، یا Performance audit نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 14">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Responsive Override</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>TUYA باید با همان Section/DOM از Desktop به Mobile تبدیل شود.</td><td>Duplicate Section ممنوع است.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Desktop base قبلاً با Flow/Flex/Media/Position ساخته شده است.</td><td>Responsive باید کمترین تغییر را اعمال کند.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Tablet contract، Mobile order، gapها، font sizeها، stage ratio.</td><td>با Resize test تعیین می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Breakpointهای واقعی سایت، متن نهایی، assets نهایی، states نهایی.</td><td>بدون UI واقعی قطعی نشوند.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — Responsive Contract را بنویس، نه عدد</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس چهارده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> نوشتن قرارداد Responsive قبل از واردکردن override.</p>
<p><strong>مسیر:</strong> Elementor Editor → Preview/Responsive Mode → Desktop/Tablet/Mobile و Resize آهسته.</p>
<p><strong>Element هدف:</strong> کل TUYA Section، اما تغییر فقط روی کنترل شکست‌خورده.</p>
<p><strong>Class فعال:</strong> Classهای موجود؛ Global جدید نساز.</p>
<p><strong>Property:</strong> Direction / Gap / Padding / Typography / Stage size / Node offsets فقط در صورت شکست واقعی.</p>
<p><strong>نباید تغییر کند:</strong> ساختار DOM، Duplicate Section، Position/Layering نهایی، Design System نهایی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Responsive Contract نوشته شد و فقط اولین شکست واقعی با کمترین override اصلاح شد.»</p>
</aside>

<h3>مرحلهٔ ۲ — جدول شکست‌ها را پر کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Responsive failure log">
<table class="data-table educational-table edu-table">
<caption>Failure Log برای Responsive</caption>
<thead><tr><th scope="col">عرض</th><th scope="col">شکست مشاهده‌شده</th><th scope="col">نوع مشکل</th><th scope="col">کمترین کنترل لازم</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Desktop stable</th><td>بدون شکست</td><td>Base</td><td>هیچ</td><td><code dir="ltr">confirmed_base</code></td></tr>
<tr><th scope="row">Tablet candidate</th><td>فشردگی Copy/Visual؟</td><td>Layout</td><td>Direction/GAP/Basis فقط در صورت نیاز</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Mobile candidate</th><td>متن، Visual یا Button؟</td><td>Typography/Layout/Media</td><td>Column/width/button/gap</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Between breakpoints</th><td>Unknown</td><td>Regression</td><td>بعد از تغییر تست شود</td><td><code dir="ltr">required_check</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — مقدارهای شروع قراردادی</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional responsive contract">
<table class="data-table educational-table edu-table">
<caption>قرارداد شروع Responsive برای TUYA</caption>
<thead><tr><th scope="col">بخش</th><th scope="col">Desktop</th><th scope="col">Tablet</th><th scope="col">Mobile</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Shell Direction</th><td>Row</td><td>Row فشرده یا Column</td><td>Column</td><td><code dir="ltr">provisional_until_resize</code></td></tr>
<tr><th scope="row">Copy/Visual Order</th><td>Copy + Visual</td><td>همان یا Column</td><td>Copy اول، Visual بعدی</td><td><code dir="ltr">provisional_until_ux</code></td></tr>
<tr><th scope="row">Gap</th><td>Base</td><td>کمتر فقط در صورت شکست</td><td>کمتر/عمودی</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Typography</th><td>Base</td><td>fluid یا override محدود</td><td>readability-first</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Visual Stage</th><td>full</td><td>max-size محدود</td><td>ساده‌تر و قابل‌خواندن</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Decoration</th><td>کامل‌تر</td><td>کمتر در صورت فشردگی</td><td>محدود</td><td><code dir="ltr">provisional</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۴ — تست Reset</h3>
<ol>
<li>یک override موقت Mobile برای Gap بساز.</li>
<li>مشاهده کن Mobile مستقل شده است.</li>
<li>Desktop gap را تغییر بده.</li>
<li>ببین Mobile هنوز مقدار خودش را دارد.</li>
<li>override Mobile را Reset کن.</li>
<li>مشاهده کن Mobile دوباره پیرو مقدار بالاتر می‌شود.</li>
</ol>

<h3>مرحلهٔ ۵ — سؤال توقف</h3>
<p>اگر Mobile فعلاً همان مقدار Desktop را لازم دارد، کار درست چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-14">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-14-a" name="stop-question-14" type="radio" value="A"/><span>A) همان مقدار Desktop را در Mobile هم دستی وارد کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-14-b" name="stop-question-14" type="radio" value="B"/><span>B) Mobile را بدون مقدار محلی نگه دارم تا inherited بماند.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-14-c" name="stop-question-14" type="radio" value="C"/><span>C) یک Section جدا برای Mobile بسازم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> اگر رفتار متفاوت لازم نیست، override محلی نساز. مقدار inherited نگهداری را ساده‌تر می‌کند.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> برای هر دستگاه یک Section جدا بسازی.</p>
<p><strong>نشانه:</strong> متن در Desktop تغییر کرده اما Mobile قدیمی مانده، یا محتوای تکراری در DOM زیاد شده است.</p>
<p><strong>قاعده:</strong> یک DOM، یک Section، override حداقلی.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<figure class="visual-figure ascii-figure">
<figcaption>Responsive خراب با Duplicate</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop Section
Tablet Section
Mobile Section

نتیجه:
- سه نسخهٔ محتوا
- سه مسیر Style
- احتمال محتوای تکراری
- Maintenance سخت
- Performance بدتر</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-79">
<fieldset>
<legend>Checkpoint درس ۱۴</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-79-1" name="chk-79-1" type="checkbox"/><span>Responsive Contract قبل از عددها نوشته شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-79-2" name="chk-79-2" type="checkbox"/><span>هیچ Section جدا برای Mobile ساخته نشده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-79-3" name="chk-79-3" type="checkbox"/><span>اولین شکست واقعی با Resize آهسته پیدا شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-79-4" name="chk-79-4" type="checkbox"/><span>فقط کمترین کنترل لازم override شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-79-5" name="chk-79-5" type="checkbox"/><span>تفاوت inherited/override/reset را روی یک کنترل تست کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-79-6" name="chk-79-6" type="checkbox"/><span>عرض‌های بین Breakpointها هم باید تست شوند.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Override و Reset را با مثال Gap توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر کارت در Sidebar باریک است اما Viewport Desktop است، چرا Container Query ممکن است مفید باشد و چرا فعلاً آن را بدون شواهد پنل V4 قطعی نمی‌کنی؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Media Query به Viewport نگاه می‌کند و Container Query به فضای خود Component؛ اما در Elementor V4 باید پشتیبانی/روش اجرا در نسخهٔ هدف بررسی شود.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-14-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — یک DOM، چند عرض</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_runtime_validation</code></p>
<ul>
<li>Desktop، Tablet، Mobile و چند عرض بینابینی را تست کن.</li>
<li>با متن واقعی فارسی، Logoهای واقعی و Visual Stage واقعی تست کن.</li>
<li>اگر مشکل فقط در یک عرض رخ می‌دهد، همان کنترل مربوط را تغییر بده، نه کل سکشن را.</li>
<li>Order بصری را با reading/focus order قاطی نکن.</li>
<li>Duplicate Section بدون دلیل مستند ممنوع است.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-14-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-14-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Mobile درست دیده می‌شود اما Maintenance خراب است</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی تصمیم Responsive<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">decision_audit</code></p>
<p>سناریو: Mobile و Desktop هر دو خوب دیده می‌شوند، اما برای Mobile یک Section جدا ساخته شده است.</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا محتوا در دو جا تکرار شده؟</li>
<li>آیا Screen Reader محتوای پنهان را می‌بیند؟</li>
<li>آیا Performance به خاطر DOM اضافی بدتر شده؟</li>
<li>آیا Classها و Variableها دو مسیر متفاوت گرفته‌اند؟</li>
<li>آیا همین نتیجه با Direction/Gap/Padding/Order محدود قابل حل بود؟</li>
<li>آیا تفاوت واقعاً ساختاری است یا فقط Style است؟</li>
</ul>
</section>
<p>نتیجهٔ درست: ظاهر درست کافی نیست؛ مسیر نگهداری و کیفیت DOM را هم Audit کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، Media Query فعال، computed value و source rule را بررسی کن. ظاهر نهایی نمی‌گوید مقدار از inherited value آمده یا override محلی است.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-14-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-14-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-82">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-82-1" name="chk-82-1" type="checkbox"/><span>می‌توانم inherited value، override و reset را توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-82-2" name="chk-82-2" type="checkbox"/><span>می‌دانم Breakpoint باید براساس شکست محتوا باشد، نه نام دستگاه.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-82-3" name="chk-82-3" type="checkbox"/><span>می‌دانم Duplicate Section راه‌حل اول Responsive نیست.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-83">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-83-1" name="chk-83-1" type="checkbox"/><span>برای TUYA Responsive Contract می‌نویسم و فقط کمترین override لازم را می‌سازم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-83-2" name="chk-83-2" type="checkbox"/><span>با Resize آهسته اولین شکست واقعی را پیدا می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-83-3" name="chk-83-3" type="checkbox"/><span>وقتی override لازم نیست، مقدار محلی را Reset می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-84">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-84-1" name="chk-84-1" type="checkbox"/><span>برای یک Card reusable می‌توانم فرق Media Query و Container Query را توضیح بدهم و بگویم چرا اجرای Container Query نیازمند شواهد نسخهٔ هدف است.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-14-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Responsive tokens و overrides</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>این responsive value باید direct override بماند یا Token شود؟</li>
<li>تغییر در Local Class کافی است یا Global Class باید responsive شود؟</li>
<li>آیا Component باید در contextهای مختلف رفتار متفاوت داشته باشد؟</li>
<li>آیا Container Query لازم است یا Media Query کافی است؟</li>
<li>آیا reset کردن مقدار محلی بهتر از ساخت token جدید است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — فعلاً Responsive overrideها local/provisional هستند. تا وقتی Contract و شکست‌های واقعی پایدار نشده‌اند، Token سراسری نساز.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-14-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-14-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا TUYA باید با یک DOM و بدون Duplicate از Desktop به Mobile تبدیل شود، اما Breakpointها و مقدارهای نهایی هنوز باید با UI واقعی اعتبارسنجی شوند.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 14</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-14-completion">
<fieldset>
<legend>ثبت پایان درس 14</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-14-complete" name="lesson-14-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
