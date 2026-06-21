<article class="lesson card-surface" data-lesson="18" id="lesson-18">

<h2 class="lesson-title former-h1">درس 18 — صفحات Hybrid V3/V4 و نردبان مهاجرت</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-18-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-18-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> صفحهٔ Hybrid را خطا فرض نکنی؛ آن را به‌عنوان وضعیت گذار بخوانی، ریسک‌ها را ثبت کنی و فقط با نردبان مهاجرت کنترل‌شده از V3 به V4 حرکت کنی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تبدیل خودکار کل سایت، حذف فوری همهٔ Widgetهای V3، migration script، یا بازنویسی کامل Theme Builder و Add-onهای شخص ثالث.</p>
<p><strong>در پایان باید بتوانی:</strong> یک بخش Legacy کم‌ریسک را در Staging بازسازی V4 کنی، با Baseline مقایسه کنی، Dynamic Data و Accessibility را چک کنی، و فقط بعد از تأیید جایگزین کنی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-18-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-18-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟣 پروژه‌ای</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🔍 تحلیل + 🔧 مهاجرت کنترل‌شده + ⚖ مقایسه</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۶۰–۹۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۳۰–۴۵ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس را بهتر است در دو جلسه اجرا کنی: جلسهٔ اول تشخیص و Baseline؛ جلسهٔ دوم Pilot در Staging و مقایسه. هنرجو نباید از روی هیجان V3 را حذف کند.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_hybrid_migration_ladder_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-18-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-18-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس‌های قبل روش V4 را برای Structure، Layout، Typography، Media، Position، Responsive، RTL، State و Design System ساختی. حالا با واقعیت سایت‌های موجود روبه‌رو می‌شوی: همه‌چیز از ابتدا V4 نیست. صفحات واقعی می‌توانند ترکیبی از ساختارهای قدیمی، V4، Add-onها، Custom CSS و Dynamic Data باشند.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">V3 / Legacy
+
V4 / Atomic Elements
+
Add-ons / Dynamic Data / Custom CSS
=
Hybrid Page</code></pre>
</figure>

<h3>اصل مهم</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Hybrid ≠ Invalid
Legacy ≠ Immediately wrong
V4 refactor = controlled project</code></pre>
</figure>
<p>Hybrid بودن صفحه به‌خودی‌خود خطا نیست. Legacy بودن هم الزاماً یعنی «فوراً حذف کن» نیست. مهاجرت V4 یک پروژهٔ کنترل ریسک است، نه یک دکمهٔ سریع برای نوکردن سایت.</p>

<h3>چه چیزهایی Hybrid را حساس می‌کنند؟</h3>
<ul>
<li>Widgetهای V3 در کنار Elementهای V4؛</li>
<li>Global Colors/Fonts قدیمی در کنار Variables/Classes جدید؛</li>
<li>Custom CSS وابسته به DOM یا selector قدیمی؛</li>
<li>Add-onهای شخص ثالث با markup یا script اختصاصی؛</li>
<li>Dynamic Tagها، ACF، فرم‌ها، Queryها و Templateها؛</li>
<li>صفحات تجاری حساس مثل Checkout، Landing پرفروش یا فرم Lead؛</li>
<li>Tracking، conversion event، analytics و scriptهای وابسته به selector.</li>
</ul>

<h3>نردبان مهاجرت</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<ol>
<li>Legacy/Hybrid را تشخیص بده.</li>
<li>نقش واقعی بخش را بنویس.</li>
<li>وابستگی‌ها را فهرست کن: CSS، JS، Add-on، Dynamic Data، Form، Tracking.</li>
<li>Baseline بگیر: Screenshot، DOM/selector، Performance، Accessibility، Responsive، Conversion event.</li>
<li>معادل V4 را فقط در Staging بساز.</li>
<li>Content و Dynamic Data را منتقل کن.</li>
<li>Desktop را مقایسه کن.</li>
<li>Tablet و Mobile را مقایسه کن.</li>
<li>Keyboard، Focus، Alt، Heading، Contrast و Zoom را بررسی کن.</li>
<li>Tracking/Form/Conversion را تست کن.</li>
<li>Rollback plan داشته باش.</li>
<li>فقط بعد از تأیید جایگزین کن.</li>
</ol>
</section>

<h3>Baseline یعنی چه؟</h3>
<p>قبل از مهاجرت باید وضعیت موجود را ثبت کنی. بدون Baseline، نمی‌دانی V4 بهتر شده، بدتر شده یا فقط متفاوت شده است.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Migration baseline checklist">
<table class="data-table educational-table edu-table">
<caption>Baseline حداقلی قبل از Migration</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">چه چیزی ثبت شود؟</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Visual</th><td>Desktop/Tablet/Mobile screenshot و notes</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">Content</th><td>متن، تصاویر، alt، dynamic fields</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">Behavior</th><td>Form submit، link، hover/focus، interaction</td><td><code dir="ltr">required_if_applicable</code></td></tr>
<tr><th scope="row">CSS/JS</th><td>Custom selectorها، add-on dependency، tracking</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">Performance</th><td>اندازهٔ DOM، assetها، Core Web Vitals/Lab note</td><td><code dir="ltr">provisional_without_lab</code></td></tr>
<tr><th scope="row">Accessibility</th><td>Keyboard، Focus، headings، alt، contrast</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">Rollback</th><td>backup، duplicate، snapshot، restore path</td><td><code dir="ltr">required</code></td></tr>
</tbody>
</table>
</div>

<h3>Migration Decision Matrix</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Migration decision matrix">
<table class="data-table educational-table edu-table">
<caption>خروجی‌های ممکن تصمیم Migration</caption>
<thead><tr><th scope="col">وضعیت</th><th scope="col">تصمیم</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">V3 کار می‌کند و کم‌ریسک نیست</th><td>Keep V3 موقت</td><td>حذف فوری ریسک بیشتری از سود دارد.</td></tr>
<tr><th scope="row">بخش کم‌ریسک و قابل مقایسه است</th><td>Pilot one section</td><td>یک نمونهٔ V4 در Staging بساز و مقایسه کن.</td></tr>
<tr><th scope="row">Feature parity ناقص است</th><td>Hybridize یا defer</td><td>V4 هنوز جایگزین کامل آن بخش نیست.</td></tr>
<tr><th scope="row">Custom CSS وابسته به markup قدیمی است</th><td>Refactor CSS first</td><td>قبل از migration selectorها باید نقشه‌برداری شوند.</td></tr>
<tr><th scope="row">صفحه حساس تجاری است</th><td>Staging + QA + rollback</td><td>مهاجرت بدون test plan ممنوع است.</td></tr>
<tr><th scope="row">Baseline و QA پاس شده‌اند</th><td>Replace controlled</td><td>جایگزینی با سند و امکان بازگشت.</td></tr>
</tbody>
</table>
</div>

<h3>Feature Parity</h3>
<p>قبل از بازسازی V4، بپرس: «معادل V4 همهٔ قابلیت‌های لازم Widget قدیمی را دارد؟» اگر نه، migration کامل premature است. ممکن است فقط بخشی از UI را V4 کنی، یا موقتاً Hybrid نگه داری.</p>

<h3>Performance را ادعا نکن، اندازه بگیر</h3>
<p>V4 می‌تواند ساختار استانداردتر و مدیریت Style جدیدتری بدهد، اما Performance نهایی به تعداد Elementها، تصاویر، scriptها، Add-onها، fontها، server و cache وابسته است. پس جملهٔ «V4 همیشه سریع‌تر است» جای Benchmark را نمی‌گیرد.</p>

<h3>قاعدهٔ این درس</h3>
<p>در Migration، اول شناسایی و Baseline، بعد Pilot در Staging، بعد مقایسه، بعد جایگزینی کنترل‌شده. حذف فوری Legacy بدون Rollback، روش این دوره نیست.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-18.0.0" id="lesson-18-concept-reference">
<summary>📚 مرجع مفهومی کامل — Hybrid V3/V4؛ مهاجرت بدون بازسازی کور</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="18" data-source-version="tuya-revised-18.0.0">

<p class="concept-reference-lead">این مرجع، هستهٔ مفهومی درس Hybrid را حفظ می‌کند و آن را به روش evidence-first تبدیل می‌کند. Migration یعنی مدیریت ریسک، نه پاکسازی هیجانی.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-18-ref-problem">
<h3 id="lesson-18-ref-problem">۱. مسئله‌ای که Migration حل می‌کند</h3>
<p>سایت واقعی معمولاً تمیز و یک‌دست نیست. ممکن است یک صفحه هم‌زمان شامل Widgetهای قدیمی، Elementهای V4، فرم‌های Add-on، Dynamic Tag، Custom CSS و scriptهای tracking باشد. Migration باید این شبکهٔ وابستگی را با حداقل ریسک تغییر دهد.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-18-hospital">
<h3 id="lesson-18-hospital">۲. تشبیه بیمارستان در حال کار</h3>
<p>یک بیمارستان را نمی‌توان یک‌شبه تعطیل و از نو ساخت. بعضی بخش‌ها قدیمی می‌مانند، بعضی بخش‌ها بازسازی می‌شوند، و مسیر برگشت اضطراری لازم است.</p>
<ul>
<li><strong>V3:</strong> بال قدیمی اما فعال؛</li>
<li><strong>V4:</strong> بال جدید؛</li>
<li><strong>Hybrid:</strong> راهروی اتصال؛</li>
<li><strong>Staging:</strong> محیط آزمایش؛</li>
<li><strong>Rollback:</strong> مسیر بازگشت اضطراری.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-why-hybrid-valid">
<h3 id="lesson-18-why-hybrid-valid">۳. چرا Hybrid الزاماً خطا نیست؟</h3>
<p>Hybrid مرحله‌ای طبیعی در مهاجرت است. هدف این نیست که صفحه با دیدن یک Widget قدیمی «خراب» اعلام شود. هدف این است که بفهمی آن Widget چه نقشی دارد، چه وابستگی‌هایی دارد، و آیا V4 جایگزین معادل و کم‌ریسک دارد یا نه.</p>
<p>در این درس، هر ادعای مربوط به قابلیت دقیق نسخهٔ هدف باید در همان نصب Elementor و مستندات همان نسخه verify شود. Workbook فقط مسیر تصمیم می‌دهد؛ نه تضمین همهٔ قابلیت‌های نسخهٔ آینده.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-risk-levels">
<h3 id="lesson-18-risk-levels">۴. سطح ریسک Migration</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Migration risk levels">
<table class="data-table educational-table edu-table">
<caption>سطح ریسک Migration</caption>
<thead><tr><th scope="col">ریسک</th><th scope="col">نمونه</th><th scope="col">اقدام</th></tr></thead>
<tbody>
<tr><th scope="row">Low</th><td>بخش استاتیک ساده، بدون فرم و Dynamic Data</td><td>Pilot مناسب است.</td></tr>
<tr><th scope="row">Medium</th><td>بخش با CSS اختصاصی یا چند asset</td><td>Baseline و CSS mapping لازم است.</td></tr>
<tr><th scope="row">High</th><td>فرم Lead، query، dynamic template، add-on پیچیده</td><td>QA plan، rollback و تست دقیق لازم است.</td></tr>
<tr><th scope="row">Critical</th><td>Checkout، signup، landing پرفروش</td><td>بدون staging، backup و تأیید business جایگزین نکن.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-css">
<h3 id="lesson-18-css">۵. Custom CSS و DOM قدیمی</h3>
<p>بسیاری از Migrationها به خاطر CSS وابسته به DOM می‌شکنند. قبل از بازسازی، selectorها را ثبت کن:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code">.elementor-widget-legacy .some-inner-wrapper {
  margin-top: -20px;
}</code></pre>
</figure>
<p>بعد بپرس: این selector به markup قدیمی وابسته است یا intent قابل انتقال دارد؟ اگر intent فقط spacing یا typography است، آن را به Class/Variable/Style جدید منتقل کن. اگر به wrapper خاص وابسته است، احتمالاً باید refactor شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-dynamic">
<h3 id="lesson-18-dynamic">۶. Dynamic Data و Forms</h3>
<p>Migration ظاهری کافی نیست. اگر بخش Legacy Dynamic Data دارد، باید fieldها، fallbackها، empty stateها و conditional visibility تست شوند. اگر فرم دارد، submit، validation، success/error message، integration، email و tracking را تست کن.</p>
<p>قاعده: اگر بخش درآمد، lead، data یا conversion را لمس می‌کند، migration بدون تست رفتاری ناقص است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-compare">
<h3 id="lesson-18-compare">۷. مقایسهٔ قبل و بعد</h3>
<p>مقایسه فقط «چشم من شبیه دید» نیست. حداقل این‌ها را کنار هم ببین:</p>
<ul>
<li>Screenshot در Desktop/Tablet/Mobile؛</li>
<li>Text content و dynamic values؛</li>
<li>Spacing و breakpoint behavior؛</li>
<li>Heading hierarchy و focus order؛</li>
<li>Alt text و role رسانه‌ها؛</li>
<li>Form behavior یا link behavior؛</li>
<li>Network/asset size و تعداد scriptهای اثرگذار؛</li>
<li>Custom CSS selectorهای باقی‌مانده.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-tuya">
<h3 id="lesson-18-tuya">۸. TUYA در این درس چه کار می‌کند؟</h3>
<p>TUYA خودش تا اینجا به‌عنوان تمرین V4 ساخته شده است. در درس ۱۸، به‌جای خراب‌کردن TUYA، یک سناریوی آموزشی اضافه می‌کنیم: فرض کن یک بخش Legacy مشابه TUYA در سایت وجود دارد. تو باید آن را در Staging با روش V4 بازسازی و مقایسه کنی.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA Migration Pilot">
<table class="data-table educational-table edu-table">
<caption>سناریوی Pilot برای TUYA</caption>
<thead><tr><th scope="col">مرحله</th><th scope="col">اقدام</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Legacy source</th><td>بخش قدیمی مشابه Hero/Feature را شناسایی کن.</td><td><code dir="ltr">simulated_or_real</code></td></tr>
<tr><th scope="row">Baseline</th><td>Screenshot، متن، CSS، assets، interactions را ثبت کن.</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">V4 rebuild</th><td>با Section/Shell/Copy/Visual/Classes بازسازی کن.</td><td><code dir="ltr">staging_only</code></td></tr>
<tr><th scope="row">Compare</th><td>Visual، Responsive، Accessibility، Dynamic Data را مقایسه کن.</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">Replace</th><td>فقط بعد از تأیید و Rollback plan.</td><td><code dir="ltr">not_in_this_lesson</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-staging">
<h3 id="lesson-18-staging">۹. Staging و Rollback</h3>
<p>هر migration جدی باید در Staging انجام شود. Staging یعنی جای امن برای شکستن و تست‌کردن. Rollback یعنی قبل از تغییر بدانیم اگر خروجی بد شد، چگونه برمی‌گردیم.</p>
<p>بدون Rollback، migration پرریسک است؛ حتی اگر از نظر فنی ساده به نظر برسد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-18-debug">
<h3 id="lesson-18-debug">۱۰. Debug Migration</h3>
<p>اگر نسخهٔ V4 شبیه نسخهٔ Legacy نشد، این ترتیب را بررسی کن:</p>
<ol>
<li>آیا نقش ساختاری بخش را درست فهمیده‌ای؟</li>
<li>آیا Content و Dynamic Data منتقل شده‌اند؟</li>
<li>آیا CSS قدیمی هنوز روی DOM جدید اثر می‌گذارد؟</li>
<li>آیا responsive contract قدیمی با V4 mapping شده؟</li>
<li>آیا Add-on یا JS به selector قدیمی وابسته است؟</li>
<li>آیا Visual mismatch از typography/media/spacing است یا layout؟</li>
<li>آیا Accessibility در نسخهٔ جدید بهتر، بدتر یا برابر است؟</li>
</ol>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-18-traps">
<h3 id="lesson-18-traps">۱۱. اشتباهات رایج</h3>
<ul>
<li>Hybrid را فوراً خطا دانستن؛</li>
<li>حذف همهٔ V3 بدون Baseline؛</li>
<li>Migration روی Production؛</li>
<li>مقایسه نکردن Dynamic Data؛</li>
<li>فراموش‌کردن form behavior و tracking؛</li>
<li>ادعای Performance بدون benchmark؛</li>
<li>تغییر همه‌چیز به‌جای Pilot کوچک؛</li>
<li>بی‌توجهی به Custom CSS قدیمی؛</li>
<li>نبود Rollback plan؛</li>
<li>جایگزینی بعد از شباهت ظاهری، بدون Accessibility و Responsive QA.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-18-golden">
<h3 id="lesson-18-golden">۱۲. قوانین طلایی</h3>
<ul>
<li><strong>Hybrid الزاماً خطا نیست؛ وضعیت گذار است.</strong></li>
<li><strong>Legacy را تا وقتی نقش و وابستگی‌اش روشن نشده حذف نکن.</strong></li>
<li><strong>Migration بدون Baseline یعنی حرکت کور.</strong></li>
<li><strong>Staging قبل از Production.</strong></li>
<li><strong>Feature Parity را قبل از rebuild کامل بسنج.</strong></li>
<li><strong>Custom CSS و Dynamic Data را جداگانه نقشه‌برداری کن.</strong></li>
<li><strong>V4 performance را اندازه بگیر، نه ادعا.</strong></li>
<li><strong>Rollback plan بخشی از Migration است، نه گزینهٔ اختیاری.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>این درس بر پایهٔ فایل فعلی Workbook، اصول migration، و وضعیت مستندات V4 نوشته شده است. قابلیت‌های دقیق V4، sync، کلاس‌ها، و هم‌زیستی با ساختارهای قدیمی باید در نسخهٔ هدف Elementor و محیط Staging همان پروژه اعتبارسنجی شوند.</p>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-18-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-18-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Migration Baseline، Risk، Parity و Rollback</span>
</summary>
<section aria-labelledby="lesson-18-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در Migration، مهم‌ترین واحد اندازه‌گیری فقط px و rem نیست؛ ریسک، Baseline، وابستگی و parity است.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۸" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>مفهوم، نوع سنجش و تله</caption>
<thead><tr><th scope="col">مفهوم</th><th scope="col">نوع سنجش</th><th scope="col">مثال</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Baseline</th><td>Evidence snapshot</td><td>Screenshot، metrics، behavior</td><td>بعد از تغییر دنبال مدرک بگردی.</td></tr>
<tr><th scope="row">Feature Parity</th><td>Capability comparison</td><td>Widget قدیمی vs V4 element</td><td>ظاهر مشابه را parity کامل فرض کنی.</td></tr>
<tr><th scope="row">Risk Level</th><td>Low/Medium/High/Critical</td><td>Form، Checkout، Add-on</td><td>همهٔ sectionها را یکسان ببینی.</td></tr>
<tr><th scope="row">Rollback</th><td>restore path</td><td>backup، duplicate، version history</td><td>بعد از خراب‌شدن به فکر برگشت بیفتی.</td></tr>
<tr><th scope="row">Dependency</th><td>CSS/JS/Data map</td><td>selector، dynamic tag، tracking</td><td>وابستگی پنهان را نادیده بگیری.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر یک بخش ۵ dependency دارد و ۳ تای آن تست‌نشده است، Migration آمادهٔ جایگزینی نیست؛ حتی اگر ظاهر Desktop شبیه شده باشد.</p></section>
<section><h3>📱 در Responsive</h3><p>نسخهٔ V4 باید فقط در Desktop مقایسه نشود. اختلاف‌های Tablet/Mobile معمولاً دیرتر دیده می‌شوند و ریسک واقعی‌اند.</p></section>
<section><h3>🔬 در DevTools</h3><p>Selectorهای CSS قدیمی، event listenerها، DOM depth، asset load و computed styles را با نسخهٔ V4 مقایسه کن.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-18-migration-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Keep، Pilot یا Replace؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر سناریو را اول تصمیم بگیر، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Migration Step Through">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تصمیم‌های مهاجرت</caption>
<thead><tr><th scope="col">سناریو</th><th scope="col">تصمیم بهتر</th><th scope="col">دلیل</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Widget V3 ساده، بدون dynamic و add-on</th><td>Pilot in Staging</td><td>ریسک پایین و قابل مقایسه است.</td><td><code dir="ltr">candidate</code></td></tr>
<tr><th scope="row">فرم Lead با integration</th><td>Baseline + QA plan</td><td>رفتار مهم‌تر از ظاهر است.</td><td><code dir="ltr">high_risk</code></td></tr>
<tr><th scope="row">Checkout یا صفحهٔ پرفروش</th><td>Defer یا controlled migration با rollback</td><td>ریسک تجاری بالا است.</td><td><code dir="ltr">critical</code></td></tr>
<tr><th scope="row">Custom CSS وابسته به selector قدیمی</th><td>Map/refactor CSS first</td><td>DOM جدید selector را می‌شکند.</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">V4 معادل کامل ندارد</th><td>Hybridize/defer</td><td>Feature parity ناقص است.</td><td><code dir="ltr">confirmed_risk</code></td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-18-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-18-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Migration Pilot، فقط در Staging</h3>
<p>در این تمرین، یک بخش Legacy فرضی یا واقعی مشابه TUYA را برای Pilot انتخاب می‌کنی. TUYA اصلی را خراب نمی‌کنی و هیچ جایگزینی Production انجام نمی‌دهی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 18">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Migration</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Hybrid به‌خودی‌خود خطا نیست.</td><td>اول تحلیل و Baseline.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Migration باید در Staging انجام شود.</td><td>Production تغییر نمی‌کند.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>معادل V4 بخش Legacy.</td><td>تا Feature Parity و QA تأیید نشود قطعی نیست.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>وابستگی‌های واقعی Add-on، CSS، JS، tracking، Dynamic Data.</td><td>باید inventory شوند.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Migration Card بساز</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس هجده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ثبت تصمیم Migration قبل از هر بازسازی.</p>
<p><strong>مسیر:</strong> Staging → انتخاب یک Section Legacy کم‌ریسک → ثبت Baseline → ساخت نسخهٔ V4 کنار نسخهٔ قدیمی.</p>
<p><strong>Element هدف:</strong> فقط یک بخش Legacy انتخاب‌شده؛ نه کل سایت.</p>
<p><strong>Class فعال:</strong> Classهای V4 candidate؛ Global جدید فقط بعد از reuse evidence.</p>
<p><strong>Property:</strong> ساختار V4، Content parity، Responsive parity، Accessibility parity.</p>
<p><strong>نباید تغییر کند:</strong> Production، Checkout، Formهای حساس، Tracking اصلی، Theme Templateهای زنده.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Migration Card ساخته شد؛ Baseline ثبت شد؛ بازسازی فقط در Staging انجام شد.»</p>
</aside>

<h3>مرحلهٔ ۲ — Migration Card</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Migration Card">
<table class="data-table educational-table edu-table">
<caption>کارت تصمیم Migration</caption>
<thead><tr><th scope="col">فیلد</th><th scope="col">مقدار نمونه</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Legacy Section</th><td>Hero/Feature مشابه TUYA</td><td><code dir="ltr">selected_for_pilot</code></td></tr>
<tr><th scope="row">Risk Level</th><td>Low/Medium/High/Critical</td><td><code dir="ltr">to_assess</code></td></tr>
<tr><th scope="row">Dynamic Data</th><td>None / ACF / Posts / Form</td><td><code dir="ltr">unknown_until_inventory</code></td></tr>
<tr><th scope="row">Custom CSS</th><td>selectors mapped?</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">Add-ons</th><td>dependency list</td><td><code dir="ltr">required_if_any</code></td></tr>
<tr><th scope="row">Baseline</th><td>screenshots + behavior + metrics</td><td><code dir="ltr">required</code></td></tr>
<tr><th scope="row">V4 Equivalent</th><td>Section/Shell/Copy/Visual/Classes</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Rollback</th><td>backup/snapshot/version</td><td><code dir="ltr">required</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — Pilot Build محدود</h3>
<ol>
<li>نسخهٔ Legacy را دست‌نخورده نگه دار.</li>
<li>در Staging یک نسخهٔ V4 کنار آن بساز.</li>
<li>Structure را با درس ۲ تا ۵ بساز.</li>
<li>Typography و Media را با درس ۱۰ و ۱۱ بسنج.</li>
<li>Position/Layering را فقط در صورت نیاز با درس ۱۲ و ۱۳ وارد کن.</li>
<li>Responsive و RTL را با درس ۱۴ و ۱۵ تست کن.</li>
<li>State و Accessibility را با درس ۱۶ تست کن.</li>
<li>Classes/Variables را با درس ۱۷ فقط در حد candidate ثبت کن.</li>
</ol>

<h3>مرحلهٔ ۴ — Compare Table</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Migration compare table">
<table class="data-table educational-table edu-table">
<caption>جدول مقایسهٔ Legacy و V4</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">Legacy Baseline</th><th scope="col">V4 Pilot</th><th scope="col">Pass/Fail</th></tr></thead>
<tbody>
<tr><th scope="row">Desktop Visual</th><td>ثبت شده</td><td>مقایسه شود</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Tablet/Mobile</th><td>ثبت شده</td><td>مقایسه شود</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Content/Dynamic</th><td>ثبت شده</td><td>برابر یا بهبود؟</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Accessibility</th><td>ثبت شده</td><td>Keyboard/Focus/Alt/Heading</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Performance</th><td>baseline note</td><td>asset/script/DOM note</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Tracking/Form</th><td>ثبت شده</td><td>رفتار تست شود</td><td><code dir="ltr">pending_if_applicable</code></td></tr>
<tr><th scope="row">Rollback</th><td>مسیر برگشت</td><td>آماده</td><td><code dir="ltr">required_before_replace</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۵ — سؤال توقف</h3>
<p>اگر یک بخش V3 هنوز کار می‌کند و Dynamic/Form/Tracking حساس دارد، اولین اقدام درست چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-18">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-18-a" name="stop-question-18" type="radio" value="A"/><span>A) فوراً حذف و با V4 جایگزین کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-18-b" name="stop-question-18" type="radio" value="B"/><span>B) Baseline، وابستگی‌ها و ریسک را ثبت کنم و فقط در Staging Pilot بسازم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-18-c" name="stop-question-18" type="radio" value="C"/><span>C) فقط Desktop را شبیه کنم و منتشر کنم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> بخش حساس باید با Baseline، dependency map، staging pilot، QA و rollback جلو برود. شباهت ظاهری Desktop کافی نیست.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> Hybrid را خطا بدانی و بدون Baseline پاکسازی کنی.</p>
<p><strong>نشانه:</strong> ظاهر شاید بهتر شود، اما فرم، Dynamic Data، SEO، Tracking یا Accessibility خراب می‌شود.</p>
<p><strong>قاعده:</strong> Migration = evidence + staging + compare + rollback.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<figure class="visual-figure ascii-figure">
<figcaption>Migration خراب</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code">Production page
↓
Delete V3 section
↓
Rebuild V4 by eye
↓
Publish

Problems:
- no baseline
- no dynamic data check
- no form/tracking QA
- no rollback
- desktop-only comparison</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-103">
<fieldset>
<legend>Checkpoint درس ۱۸</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-103-1" name="chk-103-1" type="checkbox"/><span>Hybrid را به‌خودی‌خود خطا فرض نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-103-2" name="chk-103-2" type="checkbox"/><span>Migration Card برای یک بخش کم‌ریسک نوشته شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-103-3" name="chk-103-3" type="checkbox"/><span>Baseline قبل از rebuild ثبت شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-103-4" name="chk-103-4" type="checkbox"/><span>بازسازی فقط در Staging انجام شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-103-5" name="chk-103-5" type="checkbox"/><span>Dynamic Data، Custom CSS، Add-ons و Tracking inventory شده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-103-6" name="chk-103-6" type="checkbox"/><span>Replace بدون QA و Rollback انجام نشده است.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Hybrid چرا الزاماً خطا نیست؟</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر یک Landing Page پرفروش با V3 ساخته شده و Custom CSS و فرم دارد، migration ladder را چگونه اجرا می‌کنی؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید Baseline، risk level، dependency map، staging pilot، feature parity، responsive/accessibility QA، tracking/form test و rollback را ذکر کند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-18-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Migration فقط Desktop نیست</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">required_before_replace</code></p>
<ul>
<li>Legacy و V4 Pilot را در Desktop، Tablet، Mobile و عرض‌های بینابینی مقایسه کن.</li>
<li>اگر V4 در Desktop بهتر و در Mobile بدتر است، migration آمادهٔ جایگزینی نیست.</li>
<li>Dynamic Data و text length در breakpointها تست شود.</li>
<li>Position/Layering و Focus در Mobile جدا بررسی شود.</li>
<li>تصمیم Replace فقط بعد از Pass شدن Compare Table انجام می‌شود.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-18-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-18-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — ظاهر خوب، رفتار خراب</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی Migration<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">migration_audit</code></p>
<p>سناریو: بخش V4 از نظر تصویر شبیه نسخهٔ V3 است، اما فرم submit نمی‌شود یا event analytics ثبت نمی‌شود.</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا form action/integration منتقل شده؟</li>
<li>آیا selector tracking هنوز به markup قدیمی اشاره می‌کند؟</li>
<li>آیا Custom JS event listener روی class قدیمی بوده؟</li>
<li>آیا success/error state تست شده؟</li>
<li>آیا hidden fields یا dynamic values منتقل شده‌اند؟</li>
<li>آیا accessibility و focus بعد از submit حفظ شده؟</li>
</ul>
</section>
<p>نتیجهٔ درست: visual parity کافی نیست؛ behavior parity لازم است.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، Network، Console، Event Listeners و DOM selectorها را بررسی کن. اگر tracking یا form به selector قدیمی وصل بوده، rebuild ظاهری V4 آن را خودکار منتقل نمی‌کند.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-18-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-18-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در پروژه‌های واقعی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-106">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-106-1" name="chk-106-1" type="checkbox"/><span>می‌توانم توضیح بدهم Hybrid چرا الزاماً خطا نیست.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-106-2" name="chk-106-2" type="checkbox"/><span>می‌دانم Migration بدون Baseline حرکت کور است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-106-3" name="chk-106-3" type="checkbox"/><span>می‌توانم نردبان مهاجرت را مرحله‌به‌مرحله توضیح بدهم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-107">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-107-1" name="chk-107-1" type="checkbox"/><span>برای یک بخش Legacy کم‌ریسک Migration Card می‌نویسم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-107-2" name="chk-107-2" type="checkbox"/><span>Baseline، dependency map، compare table و rollback plan را ثبت می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-107-3" name="chk-107-3" type="checkbox"/><span>فقط در Staging Pilot می‌سازم و Production را بدون QA تغییر نمی‌دهم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-108">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-108-1" name="chk-108-1" type="checkbox"/><span>برای یک Landing Page حساس می‌توانم migration risk، feature parity، behavior parity و rollback را Audit کنم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-18-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Sync میان V3 Global Assets و V4 Variables/Classes</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>آیا Global Color/Font قدیمی باید به Variable جدید map شود؟</li>
<li>آیا Class جدید باید جایگزین یک CSS selector قدیمی شود؟</li>
<li>آیا Dynamic Data روی Style یا Content اثر دارد؟</li>
<li>آیا V4 equivalent همهٔ state/responsive/RTL behavior را پوشش می‌دهد؟</li>
<li>آیا Migration باعث حذف ناخواستهٔ tracking یا form behavior می‌شود؟</li>
<li>آیا Rollback مسیر واقعی دارد؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — Sync و mapping را candidate نگه دار تا در نسخهٔ هدف و Staging تست شود. هیچ migration سراسری بدون evidence انجام نده.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-18-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-18-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا باید Migration را به‌عنوان پروژهٔ کنترل ریسک بفهمی؛ نه حذف فوری Legacy.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 18</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-18-completion">
<fieldset>
<legend>ثبت پایان درس 18</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-18-complete" name="lesson-18-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
