<article class="lesson card-surface" data-lesson="20" id="lesson-20">

<h2 class="lesson-title former-h1">درس 20 — Performance، DOM و Audit ساختار</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-20-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-20-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> Performance را به‌عنوان نتیجهٔ ساختار، رسانه، فونت، تعامل، CSS، JS، third‑party و روش اندازه‌گیری ببینی؛ نه فقط یک عدد Lighthouse یا تعداد DOM.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Benchmark تخصصی شبکه و JavaScript، تحلیل کامل Trace، بهینه‌سازی Server/Cache، یا اصلاح Core Web Vitals در سطح Production.</p>
<p><strong>در پایان باید بتوانی:</strong> برای یک صفحه یا Section، Audit ساده اما مستند انجام بدهی: Structure، Content، Interaction، Responsive، Media، Fonts، DOM، LCP/INP/CLS candidates، و Performance Budget اولیه.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-20-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-20-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🔍 Audit + 🛠 اجرایی + 🧠 تحلیلی</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۴۵–۶۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> علت Runtime را از نشانه جدا کن. DOM زیاد، تصویر سنگین، Lazy Load اشتباه، Font زیاد، Third‑party و JS سنگین همه ممکن‌اند؛ هیچ‌کدام را بدون evidence متهم نکن.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_performance_audit_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-20-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-20-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس‌های قبل Structure، Flow، Media، Position، Layering، Responsive، RTL، State، Design System، Migration و Refactor را ساختی. Performance نتیجهٔ همهٔ این تصمیم‌هاست. اگر Structure بی‌مسئولیت، Image سنگین، Font زیاد، Animation نادرست، Third‑party زیاد یا Duplicate مخفی داشته باشی، تجربهٔ کاربر آسیب می‌بیند.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Structure
+ Media
+ Fonts
+ CSS / Classes
+ JS / Interactions
+ Third-party
+ Server / Cache
+ Runtime behavior
=
Performance experience</code></pre>
</figure>

<h3>Performance فقط Lighthouse Score نیست</h3>
<p>Score مفید است، اما کامل نیست. کاربر واقعی این‌ها را تجربه می‌کند:</p>
<ul>
<li>محتوای اصلی چه زمانی دیده می‌شود؟</li>
<li>صفحه هنگام Load چقدر می‌پرد؟</li>
<li>کلیک یا Tap چقدر زود پاسخ می‌گیرد؟</li>
<li>Scroll، Hover و Animation چقدر روان‌اند؟</li>
<li>صفحه در Mobile واقعی چقدر قابل استفاده است؟</li>
</ul>

<h3>Core Web Vitals در حد Audit</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Core Web Vitals audit">
<table class="data-table educational-table edu-table">
<caption>سه معیار اصلی در زبان عملی</caption>
<thead><tr><th scope="col">معیار</th><th scope="col">سؤال عملی</th><th scope="col">علت‌های رایج</th><th scope="col">در این درس</th></tr></thead>
<tbody>
<tr><th scope="row">LCP</th><td>محتوای اصلی چه زمانی دیده شد؟</td><td>Hero image سنگین، font/CSS blocking، server کند، lazy load اشتباه</td><td>candidate را شناسایی می‌کنیم.</td></tr>
<tr><th scope="row">INP</th><td>Interaction چقدر زود پاسخ داد؟</td><td>JS long task، event handler سنگین، DOM بزرگ، third‑party script</td><td>ریسک‌ها را ثبت می‌کنیم.</td></tr>
<tr><th scope="row">CLS</th><td>صفحه چقدر بی‌اجازه جابه‌جا شد؟</td><td>Image بدون ابعاد، embed بدون فضا، font swap، banner dynamic</td><td>منبع shift را حدس مستند می‌زنیم، نه حکم قطعی.</td></tr>
</tbody>
</table>
</div>

<h3>DOM کمتر همیشه سریع‌تر نیست</h3>
<p>DOM بزرگ می‌تواند Style Recalculation، Layout و Memory را سنگین‌تر کند. اما «کم‌بودن Node» به‌تنهایی تضمین Performance نیست. یک صفحه با DOM کم و JavaScript سنگین می‌تواند کندتر از صفحه‌ای با DOM بیشتر ولی ساده باشد.</p>
<p>پس هدف این نیست که هر Wrapper را حذف کنی؛ هدف این است که Wrapperهای بی‌مسئولیت را شناسایی کنی و Wrapperهای مسئول را نگه داری.</p>

<h3>سؤال Wrapper</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>این لایه چه مسئولیتی دارد؟</li>
<li>اگر حذف شود چه می‌شکند؟</li>
<li>Layout/Scope/Position/Meaning/Accessibility می‌دهد؟</li>
<li>Containing Block، Clip، Layer یا Semantic group است؟</li>
<li>یا فقط برای جبران یک مشکل قبلی اضافه شده؟</li>
</ul>
</section>

<h3>چهار محور Audit نهایی</h3>
<div class="concept-card-grid">
<article class="concept-card" data-concept="Structure Audit">
<h4><span class="term-en" dir="ltr">Structure Audit</span> — بررسی اسکلت</h4>
<ol class="concept-steps">
<li><strong>سؤال:</strong> Parent و Childها مسئولیت روشن دارند؟</li>
<li><strong>در Elementor:</strong> Structure/Navigator و wrapper chain را بخوان.</li>
<li><strong>تله:</strong> فقط زیبایی را بررسی کنی و اسکلت را نبینی.</li>
<li><strong>تصمیم:</strong> اول اسکلت، بعد Style.</li>
</ol>
</article>
<article class="concept-card" data-concept="Content Audit">
<h4><span class="term-en" dir="ltr">Content Audit</span> — بررسی محتوا</h4>
<ol class="concept-steps">
<li><strong>سؤال:</strong> متن، Button، Logo و Image در Flow و قابل خواندن هستند؟</li>
<li><strong>در Elementor:</strong> Copy Area، Feature List، Button، Logo Strip.</li>
<li><strong>تله:</strong> محتوا را برای زیبایی قربانی کنی.</li>
<li><strong>تصمیم:</strong> محتوا قبل از Decoration سالم باشد.</li>
</ol>
</article>
<article class="concept-card" data-concept="Interaction Audit">
<h4><span class="term-en" dir="ltr">Interaction Audit</span> — بررسی تعامل</h4>
<ol class="concept-steps">
<li><strong>سؤال:</strong> Hover، Focus، Click و Keyboard سالم هستند؟</li>
<li><strong>در Elementor:</strong> State controls، links، buttons، focusable items.</li>
<li><strong>تله:</strong> فقط با Mouse تست کنی.</li>
<li><strong>تصمیم:</strong> Keyboard و Focus را هم بررسی کن.</li>
</ol>
</article>
<article class="concept-card" data-concept="Responsive Audit">
<h4><span class="term-en" dir="ltr">Responsive Audit</span> — بررسی اندازه‌ها</h4>
<ol class="concept-steps">
<li><strong>سؤال:</strong> در Desktop/Tablet/Mobile ساختار هنوز معنی دارد؟</li>
<li><strong>در Elementor:</strong> Responsive Preview و resize بین breakpointها.</li>
<li><strong>تله:</strong> برای Mobile فقط offset اضافه کنی.</li>
<li><strong>تصمیم:</strong> ساختار سازگار شود، نه وصله‌کاری.</li>
</ol>
</article>
</div>

<h3>Media و Font معمولاً پرریسک‌اند</h3>
<p>در Elementor landing pageها، Hero image، backgroundهای بزرگ، SVGهای پیچیده، فونت‌های زیاد، وزن‌های زیاد، icon fontها، lazy load اشتباه و third‑party widgetها از ریسک‌های رایج هستند. اول آن‌ها را inventory کن.</p>

<h3>Lab و Field فرق دارند</h3>
<p>Lab Data مثل Lighthouse برای Debug خوب است، چون شرایط کنترل‌شده دارد. Field Data تجربهٔ کاربران واقعی را نشان می‌دهد. هیچ‌کدام جای دیگری را کامل نمی‌گیرد. اگر فقط یک Lighthouse run داری، نتیجه را «قطعی» اعلام نکن.</p>

<h3>روش اندازه‌گیری قابل دفاع</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Browser version
Lighthouse version
Device profile
Network throttling
CPU throttling
Cache state
Number of runs
Median result
Page state
Date / URL / build version</code></pre>
</figure>
<p>قبل و بعد را در شرایط مشابه مقایسه کن. اگر conditions فرق کنند، نتیجهٔ Performance قابل اعتماد نیست.</p>

<h3>قاعدهٔ این درس</h3>
<p>Performance Audit یعنی ادعای کوچک، evidence کوچک، و تصمیم کوچک. نه حذف کور Wrapper، نه متهم‌کردن Elementor، نه اعتماد به یک Score، و نه ادعای سرعت بدون اندازه‌گیری.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-20.0.0" id="lesson-20-concept-reference">
<summary>📚 مرجع مفهومی کامل — Performance، DOM و Audit؛ ساده‌سازی قابل اندازه‌گیری</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="20" data-source-version="tuya-revised-20.0.0">

<p class="concept-reference-lead">این مرجع، هستهٔ Performance درس فعلی را حفظ می‌کند و آن را به روند TUYA وصل می‌کند. هدف، ساخت مدل عیب‌یابی است؛ نه حفظ چند عدد جدا از context.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-20-ref-problem">
<h3 id="lesson-20-ref-problem">۱. مسئله‌ای که Performance حل می‌کند</h3>
<p>Performance زبان تجربهٔ کاربر است. اگر محتوا دیر بیاید، دکمه دیر پاسخ بدهد، Layout بپرد، یا Scroll گیر کند، طراحی هرچقدر هم زیبا باشد اعتماد کاربر کاهش می‌یابد.</p>
<p>اما Performance یک علت واحد ندارد. ساختار، asset، CSS، JS، third‑party، font، hosting و cache با هم اثر می‌گذارند.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-20-restaurant">
<h3 id="lesson-20-restaurant">۲. تشبیه رستوران</h3>
<ul>
<li><strong>LCP:</strong> غذای اصلی چه زمانی روی میز رسید؟</li>
<li><strong>INP:</strong> وقتی گارسون را صدا زدی، چقدر زود پاسخ داد؟</li>
<li><strong>CLS:</strong> آیا میز و صندلی هنگام نشستن ناگهان جابه‌جا شدند؟</li>
</ul>
<p>رستورانی که دکور سبک دارد اما غذا دیر می‌رسد، سریع نیست. سایتی با DOM کم اما Hero Image سنگین نیز لزوماً سریع نیست.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-cwv">
<h3 id="lesson-20-cwv">۳. Core Web Vitals در حد تصمیم آموزشی</h3>
<p>برای تجربهٔ خوب، راهنماهای رایج این حدود را مطرح می‌کنند:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">LCP ≤ 2.5s
INP ≤ 200ms
CLS ≤ 0.1</code></pre>
</figure>
<p>این اعداد هدف‌های راهنما هستند، نه تضمین رتبه و نه جایگزین تحلیل. Field evaluation معمولاً با صدک ۷۵ و جداگانه برای Mobile/Desktop دیده می‌شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-lcp">
<h3 id="lesson-20-lcp">۴. LCP؛ محتوای اصلی</h3>
<p>LCP معمولاً با Hero image، heading بزرگ، یا block اصلی viewport اول مرتبط است. در TUYA یا صفحات مشابه، LCP candidate احتمالاً یکی از این‌هاست:</p>
<ul>
<li>Hero Visual / Cloud image؛</li>
<li>Background image بزرگ؛</li>
<li>Heading اصلی؛</li>
<li>SVG/Illustration حجیم؛</li>
<li>Image که دیر discover می‌شود.</li>
</ul>
<p>برای LCP image، بررسی کن: ابعاد، فرمت، lazy/eager strategy، priority، width/height، aspect-ratio، srcset/sizes، و وزن فایل.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-cls">
<h3 id="lesson-20-cls">۵. CLS؛ پرش Layout</h3>
<p>CLS معمولاً از این‌ها می‌آید:</p>
<ul>
<li>Image بدون width/height یا aspect-ratio؛</li>
<li>Embed یا iframe بدون فضای رزروشده؛</li>
<li>Font swap شدید؛</li>
<li>Banner یا dynamic content که بالای صفحه وارد می‌شود؛</li>
<li>Componentی که بعد از load ارتفاعش تغییر می‌کند؛</li>
<li>Animation روی layout propertyها مثل width/height/top/left.</li>
</ul>
<p>درس‌های Media، Position و Responsive مستقیماً به CLS ربط دارند: اگر Stage فضای خود را رزرو نکند، shift محتمل است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-inp">
<h3 id="lesson-20-inp">۶. INP؛ پاسخ Interaction</h3>
<p>INP از واکنش صفحه به تعامل کاربر می‌آید. علت‌های رایج:</p>
<ul>
<li>JavaScript Long Task؛</li>
<li>Event handler سنگین؛</li>
<li>DOM بزرگ و تغییرات وسیع style/layout؛</li>
<li>Third‑party script؛</li>
<li>Animation یا interaction زیاد؛</li>
<li>Widgetهای سنگین Add-on؛</li>
<li>Layout thrashing.</li>
</ul>
<p>Animation طولانی الزاماً INP بد نمی‌سازد؛ مهم تأخیر تا frame بعد از Input است. پس بدون Trace حکم نده.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-dom">
<h3 id="lesson-20-dom">۷. DOM Size؛ معیار تشخیصی، نه حکم جهانی</h3>
<p>DOM بزرگ می‌تواند مشکل بسازد، اما اعداد Node قانون جهانی کیفیت نیستند. بعضی ابزارها هشدارهای تشخیصی برای DOM زیاد می‌دهند، اما نتیجه نهایی به نوع CSS، تغییرات runtime، device، scriptها و interactionها بستگی دارد.</p>
<p>جملهٔ غلط:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">زیر 1000 Node همیشه خوب است.
هر Wrapper حتماً X میلی‌ثانیه هزینه دارد.</code></pre>
</figure>
<p>جملهٔ درست:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="rtl"><code class="language-text inline-code">DOM را به‌عنوان risk signal بررسی کن،
نه verdict قطعی.</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-wrapper">
<h3 id="lesson-20-wrapper">۸. Wrapper مسئول و Wrapper بدهکار</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Wrapper audit">
<table class="data-table educational-table edu-table">
<caption>تحلیل Wrapper</caption>
<thead><tr><th scope="col">نوع Wrapper</th><th scope="col">مسئولیت</th><th scope="col">تصمیم</th></tr></thead>
<tbody>
<tr><th scope="row">Layout Parent</th><td>Flex/Grid/spacing</td><td>احتمالاً لازم است.</td></tr>
<tr><th scope="row">Containing Block</th><td>مرجع Position</td><td>حذفش Node/overlay را می‌شکند.</td></tr>
<tr><th scope="row">Clip/Mask Layer</th><td>Overflow/rounded media</td><td>با Focus/Glow تست شود.</td></tr>
<tr><th scope="row">Semantic Group</th><td>معنا و accessibility</td><td>حذف کور نکن.</td></tr>
<tr><th scope="row">Style workaround</th><td>جبران یک مشکل قبلی</td><td>Refactor candidate.</td></tr>
<tr><th scope="row">One-child no-duty wrapper</th><td>مسئولیت نامعلوم</td><td>Audit candidate.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-media">
<h3 id="lesson-20-media">۹. Media Audit</h3>
<p>برای هر Image/SVG/Background بپرس:</p>
<ul>
<li>محتواست یا تزئین؟</li>
<li>اندازهٔ واقعی با اندازهٔ نمایش تناسب دارد؟</li>
<li>width/height یا aspect-ratio دارد؟</li>
<li>فرمت مناسب است؟</li>
<li>SVG پیچیده یا سنگین نیست؟</li>
<li>Hero/LCP اشتباهاً lazy load نشده؟</li>
<li>Alt/decorative decision درست است؟</li>
<li>Background تصویر محتوایی را پنهان نکرده؟</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-font">
<h3 id="lesson-20-font">۱۰. Font Audit</h3>
<p>فونت‌ها می‌توانند CSS blocking، FOIT/FOUT، shift و وزن فایل بسازند. بررسی کن:</p>
<ul>
<li>چند خانوادهٔ فونت Load می‌شود؟</li>
<li>چند weight واقعی استفاده می‌شود؟</li>
<li>font-display چیست؟</li>
<li>فونت فارسی و انگلیسی نیازمند همهٔ weightها هستند؟</li>
<li>icon font به‌جای SVGهای محدود استفاده شده؟</li>
<li>تغییر font باعث CLS یا visual shift می‌شود؟</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-third-party">
<h3 id="lesson-20-third-party">۱۱. Third‑party Audit</h3>
<p>Pluginها، widgetهای Add-on، analytics، chat widget، form integration، map embed و video embed می‌توانند Performance را تعیین کنند. قبل از متهم‌کردن Structure، third‑partyها را inventory کن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-component-token">
<h3 id="lesson-20-component-token">۱۲. Component و Token چگونه غیرمستقیم اثر می‌گذارند؟</h3>
<p>Component بد طراحی‌شده ممکن است:</p>
<ul>
<li>Wrapperهای تکراری بسازد؛</li>
<li>Imageهای غیرضروری render/load کند؛</li>
<li>Variantهای مخفی را هم‌زمان در DOM نگه دارد؛</li>
<li>Interactionهای متعدد ثبت کند؛</li>
<li>Stateهای بی‌استفاده اما پرهزینه بسازد.</li>
</ul>
<p>Token بد مستقیماً LCP را کند نمی‌کند، اما می‌تواند CSS متناقض، overrideهای زیاد و maintenance بدهکار بسازد. رابطه را دقیق بیان کن؛ نه اینکه «Token بد = CLS» بنویسی.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-budget">
<h3 id="lesson-20-budget">۱۳. Performance Budget</h3>
<p>Budget یعنی از قبل بدانی چه چیزی برای پروژه قابل قبول است. Budget بدون زمینه فقط شعار است.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Performance budget">
<table class="data-table educational-table edu-table">
<caption>Budget اولیهٔ قابل تنظیم</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">Budget candidate</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">LCP</th><td>هدف راهنما، نه تضمین</td><td><code dir="ltr">provisional_until_lab_field</code></td></tr>
<tr><th scope="row">INP</th><td>interaction response target</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">CLS</th><td>layout shift target</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Hero image bytes</th><td>بسته به device و project</td><td><code dir="ltr">project_specific</code></td></tr>
<tr><th scope="row">Fonts</th><td>family/weight محدود</td><td><code dir="ltr">candidate</code></td></tr>
<tr><th scope="row">Third-party scripts</th><td>حد و دلیل روشن</td><td><code dir="ltr">required_review</code></td></tr>
<tr><th scope="row">DOM review</th><td>threshold تشخیصی، نه حکم قطعی</td><td><code dir="ltr">risk_signal</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-devtools">
<h3 id="lesson-20-devtools">۱۴. پل به DevTools</h3>
<ul>
<li><strong>Network:</strong> Image، Font، Script، waterfall و transfer size.</li>
<li><strong>Performance:</strong> Main Thread، Long Task، Interaction، Layout Shift.</li>
<li><strong>Lighthouse:</strong> Audit آزمایشگاهی و hints.</li>
<li><strong>Performance Insights/Trace:</strong> LCP/INP/CLS candidate analysis.</li>
<li><strong>Elements/Computed:</strong> DOM depth، styles، layout، dimensions.</li>
</ul>
<p>یک عدد نهایی را بدون Trace و context تحلیل نکن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-20-tuya">
<h3 id="lesson-20-tuya">۱۵. TUYA Audit Contract</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA performance audit contract">
<table class="data-table educational-table edu-table">
<caption>قرارداد Audit برای TUYA</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">سؤال</th><th scope="col">خروجی</th></tr></thead>
<tbody>
<tr><th scope="row">Structure</th><td>Wrapperها مسئولیت دارند؟</td><td>Keep / Refactor candidate</td></tr>
<tr><th scope="row">Media</th><td>Hero/Logo/SVGها اندازه و role درست دارند؟</td><td>Optimize / keep / investigate</td></tr>
<tr><th scope="row">Fonts</th><td>فونت‌ها و weightها ضروری‌اند؟</td><td>Budget candidate</td></tr>
<tr><th scope="row">Interaction</th><td>Focus/hover/click سبک و قابل استفاده‌اند؟</td><td>State audit</td></tr>
<tr><th scope="row">Responsive</th><td>موبایل با offset وصله‌کاری نشده؟</td><td>Responsive refactor candidate</td></tr>
<tr><th scope="row">CLS</th><td>Stage/Image فضای خود را رزرو کرده‌اند؟</td><td>aspect-ratio/dimensions review</td></tr>
<tr><th scope="row">Third-party</th><td>widget/script اضافی هست؟</td><td>dependency inventory</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-20-traps">
<h3 id="lesson-20-traps">۱۶. اشتباهات رایج</h3>
<ul>
<li>تمرکز فقط روی Score؛</li>
<li>یک اجرای Lighthouse و حکم قطعی؛</li>
<li>Lazy Load تصویر LCP؛</li>
<li>حذف Wrapper مسئول فقط برای Node کمتر؛</li>
<li>عدد ثابت هزینه برای هر Element؛</li>
<li>نسبت‌دادن همهٔ مشکلات به Elementor؛</li>
<li>نادیده‌گرفتن Third‑partyها؛</li>
<li>مقایسهٔ قبل/بعد با cache/network/device متفاوت؛</li>
<li>گفتن «جریمه Google» به‌جای تمرکز روی UX؛</li>
<li>ادعای بهبود Performance بدون baseline و median.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-20-golden">
<h3 id="lesson-20-golden">۱۷. قوانین طلایی</h3>
<ul>
<li><strong>Performance یک تجربه است، نه فقط یک score.</strong></li>
<li><strong>DOM size risk signal است، نه verdict جهانی.</strong></li>
<li><strong>Wrapper مسئول را برای عدد کمتر حذف نکن.</strong></li>
<li><strong>قبل/بعد را در شرایط مشابه و چند run مقایسه کن.</strong></li>
<li><strong>Hero/LCP image را جداگانه بررسی کن.</strong></li>
<li><strong>CLS را با فضای رزروشده برای media و dynamic content کنترل کن.</strong></li>
<li><strong>Third‑partyها را قبل از متهم‌کردن ساختار inventory کن.</strong></li>
<li><strong>Budget بدون context شعار است؛ Budget با پروژه و دستگاه هدف معنا دارد.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>این درس بر پایهٔ فایل فعلی Workbook، مفاهیم Core Web Vitals، رفتار مرورگر، و زنجیرهٔ آموزشی قبلی نوشته شده است. عددهای Performance، budget و benchmark بدون اجرای واقعی در محیط هدف قطعی نیستند.</p>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-20-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-20-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Metrics، Budget، DOM، Media و Measurement</span>
</summary>
<section aria-labelledby="lesson-20-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در Performance، واحدها فقط px نیستند: زمان، bytes، تعداد request، DOM nodes، long tasks، CLS score و شرایط اندازه‌گیری هم واحد تصمیم‌اند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۲۰" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>مفهوم، واحد، مرجع و تله</caption>
<thead><tr><th scope="col">مفهوم</th><th scope="col">واحد/نوع</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">LCP</th><td>ثانیه/میلی‌ثانیه</td><td>viewport اول</td><td>candidate را بدون Trace قطعی اعلام کنی.</td></tr>
<tr><th scope="row">INP</th><td>میلی‌ثانیه</td><td>تعامل‌های کاربر</td><td>Animation را بدون input trace متهم کنی.</td></tr>
<tr><th scope="row">CLS</th><td>score بدون واحد</td><td>shiftهای غیرمنتظره</td><td>Image بدون ابعاد را نادیده بگیری.</td></tr>
<tr><th scope="row">Image weight</th><td>KB/MB</td><td>Network transfer</td><td>Rendered size را با file size قاطی کنی.</td></tr>
<tr><th scope="row">DOM size</th><td>node count / depth</td><td>Elements/Tools</td><td>آن را حکم جهانی بدانی.</td></tr>
<tr><th scope="row">Font budget</th><td>family/weight/bytes</td><td>Network/CSS</td><td>هر وزن را بی‌دلیل load کنی.</td></tr>
<tr><th scope="row">Measurement</th><td>runs/median/profile</td><td>Lab method</td><td>یک run را benchmark قطعی بدانی.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Hero visual در viewport اول بزرگ‌ترین عنصر است، LCP candidate است؛ اما علت بدی LCP می‌تواند server، image size، lazy strategy، CSS یا font باشد. candidate با cause فرق دارد.</p></section>
<section><h3>📱 در Responsive</h3><p>Mobile و Desktop جدا بررسی شوند. Assetی که در Desktop قابل قبول است، در Mobile کند یا بزرگ محسوب می‌شود.</p></section>
<section><h3>🔬 در DevTools</h3><p>Network، Performance Trace، Layout Shift، LCP marker، computed dimensions و request waterfall را کنار هم ببین.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-20-performance-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — علت یا نشانه؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر سناریو را اول تشخیص بده، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Performance Step Through">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تشخیص‌های Performance</caption>
<thead><tr><th scope="col">سناریو</th><th scope="col">نشانه</th><th scope="col">اولین بررسی</th><th scope="col">حکم قطعی؟</th></tr></thead>
<tbody>
<tr><th scope="row">Hero Image بزرگ و کند</th><td>LCP ریسک دارد</td><td>Network، dimensions، lazy/priority</td><td>نه بدون Trace</td></tr>
<tr><th scope="row">صفحه هنگام load می‌پرد</th><td>CLS ریسک دارد</td><td>Image dimensions، font swap، dynamic banner</td><td>نه بدون shift source</td></tr>
<tr><th scope="row">Button دیر پاسخ می‌دهد</th><td>INP ریسک دارد</td><td>Performance trace، long task، handlers</td><td>نه با حدس</td></tr>
<tr><th scope="row">DOM زیاد است</th><td>Risk signal</td><td>Wrapper responsibility، style recalculation</td><td>نه به‌تنهایی</td></tr>
<tr><th scope="row">Score پایین است</th><td>Audit signal</td><td>Opportunities + trace + repeat runs</td><td>نه با یک run</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-20-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-20-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🔍 پروژهٔ TUYA — Performance Audit Card</h3>
<p>در این تمرین، فقط Audit مستند انجام می‌دهی. هنوز Production optimization، image pipeline، cache/server tuning یا JavaScript profiling عمیق نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 20">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Performance Audit</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Performance نتیجهٔ چند لایه است.</td><td>فقط DOM یا Score را متهم نکن.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Structure، Media، Fonts، Interaction و Third‑party باید جدا audit شوند.</td><td>Audit Card چندمحوره لازم است.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>LCP/INP/CLS candidateها در TUYA.</td><td>با Trace/measurement تأیید می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Benchmark واقعی، Field Data، Server/Cache، Production plugins.</td><td>بدون محیط واقعی قطعی نشود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Audit Card بنویس</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس بیست">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ثبت ریسک‌ها و candidateها، نه اصلاح قطعی Performance.</p>
<p><strong>مسیر:</strong> Staging/Preview → TUYA Section یا صفحهٔ هدف → DevTools/Elementor Structure → Audit Card.</p>
<p><strong>Element هدف:</strong> فقط Section یا صفحهٔ انتخاب‌شده؛ نه کل سایت.</p>
<p><strong>Class فعال:</strong> Classها را فقط برای تکرار/override بررسی کن؛ migration سراسری انجام نده.</p>
<p><strong>Property:</strong> structure depth، media role/size، font usage، interactions، third‑party، LCP/CLS/INP candidates.</p>
<p><strong>نباید تغییر کند:</strong> Production، Server/Cache، JS پیچیده، image pipeline نهایی، حذف batch wrapperها، Core Web Vitals claim قطعی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Performance Audit Card نوشته شد؛ هیچ علت قطعی بدون Trace/اندازه‌گیری اعلام نشد.»</p>
</aside>

<h3>مرحلهٔ ۲ — Performance Audit Card</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Performance audit card">
<table class="data-table educational-table edu-table">
<caption>کارت Audit عملکرد</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">مشاهده</th><th scope="col">ریسک</th><th scope="col">اقدام بعدی</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Structure</th><td>Wrapper chain / DOM depth</td><td>Style/Layout cost</td><td>Wrapper responsibility audit</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Media</th><td>Hero/Logo/SVG/Background</td><td>LCP/CLS/bytes</td><td>size/format/dimensions review</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Fonts</th><td>families/weights</td><td>blocking/shift</td><td>font budget</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Interaction</th><td>CTA/Node/Button states</td><td>INP/focus issues</td><td>keyboard + trace candidate</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Responsive</th><td>mobile layout/assets</td><td>mobile LCP/CLS</td><td>mobile-specific audit</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Third-party</th><td>plugins/widgets/scripts</td><td>JS/network cost</td><td>dependency inventory</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">CWV Candidates</th><td>LCP/INP/CLS suspected elements</td><td>unknown until trace</td><td>measure with method</td><td><code dir="ltr">provisional</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — Wrapper Responsibility Audit</h3>
<p>برای سه Wrapper مشکوک این جدول را پر کن:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Wrapper responsibility audit">
<table class="data-table educational-table edu-table">
<caption>Audit مسئولیت Wrapper</caption>
<thead><tr><th scope="col">Wrapper</th><th scope="col">مسئولیت</th><th scope="col">اگر حذف شود؟</th><th scope="col">تصمیم</th></tr></thead>
<tbody>
<tr><th scope="row">Wrapper A</th><td>Layout / Position / Meaning / Unknown</td><td>چه می‌شکند؟</td><td>Keep / Refactor candidate</td></tr>
<tr><th scope="row">Wrapper B</th><td>Layout / Position / Meaning / Unknown</td><td>چه می‌شکند؟</td><td>Keep / Refactor candidate</td></tr>
<tr><th scope="row">Wrapper C</th><td>Layout / Position / Meaning / Unknown</td><td>چه می‌شکند؟</td><td>Keep / Refactor candidate</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۴ — LCP Candidate را حدس مستند بزن</h3>
<p>در viewport اول، بزرگ‌ترین و مهم‌ترین عنصر چیست؟</p>
<ul>
<li>Heading بزرگ؟</li>
<li>Hero image؟</li>
<li>SVG Cloud؟</li>
<li>Background image؟</li>
<li>Video/embed؟</li>
</ul>
<p>این فقط <code dir="ltr">candidate</code> است. علت کندی تا قبل از Trace و Network analysis قطعی نیست.</p>

<h3>مرحلهٔ ۵ — Performance Budget اولیه</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Initial performance budget">
<table class="data-table educational-table edu-table">
<caption>Budget اولیهٔ پروژه</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">Budget candidate</th><th scope="col">نیاز به تست</th></tr></thead>
<tbody>
<tr><th scope="row">Hero media</th><td>فقط asset ضروری و بهینه</td><td>Network + rendered size</td></tr>
<tr><th scope="row">Fonts</th><td>کمترین family/weight لازم</td><td>Network + visual check</td></tr>
<tr><th scope="row">Third-party</th><td>هر script باید دلیل داشته باشد</td><td>Network + main thread</td></tr>
<tr><th scope="row">DOM review</th><td>risk signal نه حکم</td><td>Wrapper audit</td></tr>
<tr><th scope="row">Layout shift</th><td>media دارای dimensions/ratio</td><td>CLS trace</td></tr>
<tr><th scope="row">Interactions</th><td>state ساده، handler محدود</td><td>INP trace</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۶ — سؤال توقف</h3>
<p>اگر یک Section DOM زیادی دارد، تصمیم درست چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-20">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-20-a" name="stop-question-20" type="radio" value="A"/><span>A) همهٔ Wrapperها را حذف کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-20-b" name="stop-question-20" type="radio" value="B"/><span>B) Wrapper responsibility و هزینهٔ واقعی را audit کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-20-c" name="stop-question-20" type="radio" value="C"/><span>C) بگویم حتماً Elementor کند است.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> DOM زیاد یک risk signal است. باید بفهمی Wrapperها مسئول‌اند یا بدهی ساختاری‌اند، و اثر واقعی را با ابزارهای مناسب بررسی کنی.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> Performance را به یک عدد یا یک علت فروبکاهی.</p>
<p><strong>نشانه:</strong> بعد از یک Lighthouse run یا یک نگاه به DOM، حکم قطعی می‌دهی.</p>
<p><strong>قاعده:</strong> Audit چندمحوره + شرایط اندازه‌گیری + candidate/confirmed جدا.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<figure class="visual-figure ascii-figure">
<figcaption>Performance Audit خراب</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code">One Lighthouse run
Score = 62
Conclusion:
"Elementor is slow."

مشکل:
- no repeat runs
- no trace
- no network analysis
- no third-party inventory
- no LCP/INP/CLS cause separation</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-114">
<fieldset>
<legend>Checkpoint درس ۲۰</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-114-1" name="chk-114-1" type="checkbox"/><span>Performance را فقط Score یا DOM count فرض نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-114-2" name="chk-114-2" type="checkbox"/><span>Structure، Media، Fonts، Interaction، Responsive و Third-party را جدا audit کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-114-3" name="chk-114-3" type="checkbox"/><span>Wrapper مسئول را فقط برای Node کمتر حذف نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-114-4" name="chk-114-4" type="checkbox"/><span>LCP/INP/CLS را به candidate و confirmed جدا کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-114-5" name="chk-114-5" type="checkbox"/><span>روش اندازه‌گیری قبل/بعد را ثبت کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-114-6" name="chk-114-6" type="checkbox"/><span>هیچ Benchmark قطعی بدون چند run و شرایط مشابه اعلام نکرده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> چرا DOM کمتر به‌تنهایی Performance بهتر را تضمین نمی‌کند؟</p>
<p><strong>انتقال به یک موقعیت تازه:</strong> اگر Hero Image بزرگ‌ترین عنصر viewport اول است، چه چیزهایی را قبل از متهم‌کردن آن به LCP بد بررسی می‌کنی؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ کامل باید بگوید LCP candidate با علت قطعی فرق دارد و باید Network، dimensions، format، lazy/priority، CSS/font blocking، server و repeat runs بررسی شوند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-20-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Performance در Mobile جداست</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">required_before_claim</code></p>
<ul>
<li>Mobile و Desktop را جدا audit کن.</li>
<li>Hero media، fonts و third‑party در Mobile اثر بیشتری دارند.</li>
<li>Layout shift در Mobile با dynamic content و image sizing بیشتر دیده می‌شود.</li>
<li>Offsetهای Mobile و duplicate hidden content را بررسی کن.</li>
<li>اگر فقط Desktop خوب است، Performance claim کامل نیست.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-20-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-20-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Score پایین، علت نامعلوم</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">audit_first</code></p>
<p>سناریو: Lighthouse score پایین است. تیم می‌گوید «DOM زیاد است» و می‌خواهد wrapperها را حذف کند.</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا LCP image سنگین است؟</li>
<li>آیا Font blocking داریم؟</li>
<li>آیا Third-party script طولانی است؟</li>
<li>آیا DOM واقعاً باعث style/layout cost شده یا فقط زیاد است؟</li>
<li>آیا CLS از Image بدون dimensions آمده؟</li>
<li>آیا فقط یک run داریم یا median چند run؟</li>
<li>آیا Device/Network/Cache قبل و بعد یکسان است؟</li>
</ul>
</section>
<p>نتیجهٔ درست: اول cause tree بساز؛ بعد کم‌ریسک‌ترین اصلاح را انتخاب کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>در Performance Trace، markerهای LCP، long taskها و layout shift sourceها را ببین. در Network، waterfall و transfer size را بخوان. در Elements، DOM depth و wrapper responsibility را audit کن. هیچ پنل واحدی کل حقیقت نیست.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-20-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-20-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در پروژه‌های واقعی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-116">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-116-1" name="chk-116-1" type="checkbox"/><span>می‌توانم LCP، INP و CLS را در زبان کاربر توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-116-2" name="chk-116-2" type="checkbox"/><span>می‌دانم DOM size فقط risk signal است، نه حکم قطعی.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-116-3" name="chk-116-3" type="checkbox"/><span>می‌دانم Performance باید با چند محور audit شود.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-117">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-117-1" name="chk-117-1" type="checkbox"/><span>برای یک Section، Performance Audit Card می‌نویسم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-117-2" name="chk-117-2" type="checkbox"/><span>Wrapperها را با مسئولیت‌شان audit می‌کنم و حذف کور انجام نمی‌دهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-117-3" name="chk-117-3" type="checkbox"/><span>قبل از ادعای بهبود، روش اندازه‌گیری و شرایط قبل/بعد را ثبت می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-118">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-118-1" name="chk-118-1" type="checkbox"/><span>برای یک Landing Page واقعی می‌توانم cause tree بین Media، Fonts، JS، Third-party، DOM و Server بسازم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-20-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Performance Budget و Structural Budget</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>آیا این Wrapper مسئولیت واقعی دارد یا debt است؟</li>
<li>آیا این Component variant hidden DOM تولید می‌کند؟</li>
<li>آیا این Variable/Class باعث overrideهای زیاد و CSS conflict شده؟</li>
<li>آیا media budget برای Hero/Logo/Icon رعایت شده؟</li>
<li>آیا font family/weight budget لازم است؟</li>
<li>آیا third‑party script برای این صفحه ضروری است؟</li>
<li>آیا قبل/بعد با روش مشابه اندازه‌گیری شده است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — Performance Budget را candidate نگه دار تا در محیط واقعی اندازه‌گیری شود. هیچ بودجهٔ قطعی بدون Lab/Field evidence نده.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-20-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-20-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا باید بتوانی Performance را مثل یک پروندهٔ Audit بخوانی: candidateها، evidence، measurement conditions و تصمیم‌های کوچک.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 20</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-20-completion">
<fieldset>
<legend>ثبت پایان درس 20</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-20-complete" name="lesson-20-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
