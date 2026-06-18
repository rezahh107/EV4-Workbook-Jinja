<article class="lesson card-surface" data-trackable="lesson-v17-components" id="lesson-v17-components">
<h2 class="former-h1">تکمیلی 18C — Components، Master و Instance</h2>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🧭 قطب‌نمای درس</span></summary><section class="disclosure-content lesson-section">
<p><strong>هدف:</strong> فرق Global Class، Variable و Component را طوری بفهمی که دیگر این سه را با هم قاطی نکنی.</p>
</section></details>
<section class="lesson-section lesson-core-concept" data-core-concept="true">
<h2>A. سه چیز شبیه، اما کاملاً متفاوت</h2>
<table><caption>جدول آموزشی دوره — A. سه چیز شبیه، اما کاملاً متفاوت</caption><thead><tr><th scope="col">مفهوم</th><th scope="col">چه چیزی را مشترک می‌کند؟</th><th scope="col">مثال</th><th scope="col">اشتباه رایج</th></tr></thead><tbody>
<tr><td>Variable</td><td>مقدار</td><td>رنگ برند، فاصله، فونت</td><td>ساخت Variable برای هر عدد اتفاقی</td></tr>
<tr><td>Global Class</td><td>قانون Style</td><td>ظاهر دکمه یا کارت</td><td>استفاده برای محتوای متفاوت</td></tr>
<tr><td>Component</td><td>ساختار و الگوی چند Element</td><td>CTA block، Testimonial، Pricing card</td><td>اشتباه گرفتن با Template یا فقط Class</td></tr>
</tbody></table>
<p>Component مثل قالب زنده است: یک Master دارد و چند Instance. اگر Master را اصلاح کنی، Instanceها هم به‌روزرسانی می‌شوند؛ اما می‌توانی برخی Propertyها را برای هر Instance قابل تغییر نگه داری.</p>
</section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="7bb2f6f9e10b316ba90a70e3c955a68db8c261624e2e281419569013f2f3de86" id="lesson-v17-components-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Component، Master و Instance</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="22" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-22-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-22-section-01">مسئله‌ای که Component حل می‌کند</h3><p>فرض کن یک Pricing Card در دوازده صفحه داری. همهٔ آن‌ها ساختار یکسانی دارند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Badge
Title
Price
Feature List
Button
</code></pre></figure><p>اگر هر Card یک کپی مستقل باشد، تغییر ساختار باید دوازده بار انجام شود. یکی از نسخه‌ها جا می‌ماند و سایت به‌تدریج ناهماهنگ می‌شود.</p><p>Component برای تکرار کنترل‌شدهٔ <strong>ساختار و Style پایه</strong> ساخته شده است.</p><hr/></section><section aria-labelledby="concept-v31-22-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-22-section-02">تشبیه به دنیای واقعی: نقشهٔ مادر ساختمان</h3><p>یک شرکت ساختمانی یک نقشهٔ مادر برای شعبه‌های خود دارد.</p><ul>
<li>Master Component = نقشهٔ اصلی</li>
<li>Instance = شعبه‌ای که با آن نقشه ساخته شده</li>
<li>Exposed Property = بخش‌هایی که مدیر شعبه اجازه دارد تغییر دهد، مثل نام، تصویر یا لینک</li>
<li>Propagation = رسیدن اصلاح نقشه به تمام شعبه‌ها</li>
<li>Detach = اعلام اینکه این شعبه از این پس مستقل است و دیگر نقشهٔ مرکزی را دنبال نمی‌کند</li>
</ul><p>اگر دیوار اصلی در نقشه جابه‌جا شود، همهٔ شعبه‌ها تحت تأثیرند. اگر فقط نام روی تابلو عوض شود، لازم نیست نقشهٔ ساختمان تغییر کند.</p><hr/></section><section aria-labelledby="concept-v31-22-section-03" class="concept-reference-part"><h3 id="concept-v31-22-section-03">Master چه چیزی را مالک است؟</h3><p>Master معمولاً این موارد را کنترل می‌کند:</p><ul>
<li>ساختار Elementها</li>
<li>ترتیب آن‌ها</li>
<li>Style پایه</li>
<li>Classها و Variableهای پایه</li>
<li>Propertyهایی که اجازهٔ سفارشی‌سازی دارند</li>
<li>حذف یا افزودن بخش‌ها</li>
</ul><p>تغییر Master دامنهٔ سراسری دارد و باید با احتیاط منتشر شود.</p><hr/></section><section aria-labelledby="concept-v31-22-section-04" class="concept-reference-part"><h3 id="concept-v31-22-section-04">Instance چه چیزی را مالک است؟</h3><p>Instance مقدار Propertyهایی را کنترل می‌کند که Master صریحاً Expose کرده است.</p><p>مستندات فعلی Elementor می‌گویند تنظیمات واجد آیکون Property در General Tab می‌توانند در Master به‌عنوان Property قابل سفارشی‌سازی ارائه شوند. متن و تصویر مثال‌های رایج‌اند، اما فهرست فقط به آن‌ها محدود نیست.</p><p>تصویر:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Master: Team Card
├── Photo → exposed
├── Name → exposed
├── Role → exposed
├── Link → exposed
└── Layout/Style → synchronized
</code></pre></figure><p>هر Instance عکس و نام خودش را دارد، اما ساختار و Style پایه را از Master می‌گیرد.</p><hr/></section><section aria-labelledby="concept-v31-22-section-05" class="concept-reference-part"><h3 id="concept-v31-22-section-05">Propagation؛ سرایت تغییر</h3><p>تغییر Master مثل ویرایش نقشهٔ مرکزی است. اگر Padding، ترتیب Elementها یا Button Style را عوض کنی، همه Instanceها تغییر می‌کنند.</p><p>پیش از تغییر Master، نمونه‌های نماینده را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Instance با متن کوتاه
Instance با متن بلند فارسی
Instance در Container باریک
Instance در Desktop
Instance در Mobile
Instance با تمام Overrideهای مجاز
</code></pre></figure><p>عدد ثابت «پنج نمونه» قانون نیست؛ مهم پوشش حالت‌های متفاوت است.</p><hr/></section><section aria-labelledby="concept-v31-22-section-06" class="concept-reference-part"><h3 id="concept-v31-22-section-06">Detach چیست؟</h3><p>Detach ارتباط Instance با Master را قطع می‌کند. پس از Detach، ساختار مستقل می‌شود و تغییرات Master را دریافت نمی‌کند.</p><p>Detach برای استثنای واقعی معتبر است. اما اگر برای تغییر رایجی مثل رنگ یا Label دائماً Instanceها را Detach می‌کنی، این یک <strong>بوی معماری</strong> است:</p><ul>
<li>شاید Property مناسب Expose نشده؛</li>
<li>شاید Variant Class لازم است؛</li>
<li>شاید Variable یا Global Class در محل درست نیست؛</li>
<li>شاید واقعاً دو Component متفاوت داری.</li>
</ul><p>قانون درست این نیست که «Detach همیشه اشتباه است». قانون درست این است:</p><blockquote>
<p>Detach باید تصمیم آگاهانه برای استقلال باشد، نه میانبر روزمره برای دورزدن Master.</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-22-section-07" class="concept-reference-part"><h3 id="concept-v31-22-section-07">Base + Variant</h3><p>فرض کن Pricing Card دو ظاهر دارد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Normal
Featured
</code></pre></figure><p>اگر ساختار یکی است و فقط Surface، Border یا Badge فرق دارد، ساخت دو Master جدا ممکن است تکرار غیرضروری باشد.</p><p>الگوی معماری:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Component: pricing-card
Class پایه: card-base
Variant Class: card-featured
</code></pre></figure><p>اما باید در نسخه هدف تأیید شود که افزودن Class به Instance یا Root آن بدون Detach چگونه ذخیره می‌شود و پس از تغییر Master باقی می‌ماند. بنابراین Variant Class یک الگوی پیشنهادی است، نه Entity رسمی اثبات‌شده‌ای به نام Variant در Elementor.</p><hr/></section><section aria-labelledby="concept-v31-22-section-08" class="concept-reference-part concept-reference-elementor concept-reference-problem"><h3 id="concept-v31-22-section-08">Slot چیست و چرا نباید با قطعیت به Elementor نسبت داده شود؟</h3><p>در معماری عمومی Component، Slot محل خالی کنترل‌شده‌ای است که مصرف‌کننده می‌تواند محتوای دلخواه در آن قرار دهد.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Card Component
├── Header Slot
├── Body Slot
└── Footer Slot
</code></pre></figure><p>اما در مستندات رسمی فعلی Components Elementor، قابلیت مشخص و قراردادی با نام Slot اثبات نشده است.</p><p>پس می‌توان Slot را به‌عنوان مفهوم عمومی آموزش داد، اما نباید نوشت:</p><blockquote>
<p>Componentهای V4 حتماً Slot Native دارند.</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-22-section-09" class="concept-reference-part"><h3 id="concept-v31-22-section-09">Component چه زمانی مناسب نیست؟</h3><ul>
<li>فقط یک مقدار رنگ تکرار شده → Variable</li>
<li>فقط Style یک Button تکرار می‌شود → Global Class</li>
<li>فقط یک Wrapper ساده در یک صفحه وجود دارد → شاید Component لازم نیست</li>
<li>دو Card ساختار و رفتار کاملاً متفاوت دارند → شاید دو Component مستقل بهتر باشند</li>
</ul><p>Component بیش از حد، Dependency Graph بزرگی می‌سازد و تغییرات مرکزی را پرریسک می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-22-section-10" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-22-section-10">در Elementor V4</h3><p>فرایند فکری:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">آیا ساختار تکرار می‌شود؟
↓ بله
آیا تفاوت Instanceها قابل تعریف و محدود است؟
↓ بله
Master بساز
↓
Propertyهای ضروری را Expose کن
↓
Instanceهای نماینده را آزمایش کن
↓
تغییر Master را با دامنه اثر منتشر کن
</code></pre></figure><p>Master را در یک صفحهٔ تصادفی و بدون دیدن مصرف‌کنندگان تغییر نده.</p><hr/></section><section aria-labelledby="concept-v31-22-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-22-section-11">اشتباهات رایج</h3><ul>
<li>ساخت Master جدا برای هر رنگ</li>
<li>Expose کردن همه تنظیمات و از بین بردن انسجام</li>
<li>Expose نکردن محتوای لازم و مجبورکردن Detach</li>
<li>تغییر Master بدون بررسی Instanceهای بلند و باریک</li>
<li>فرض رسمی بودن Slot یا Variant</li>
<li>استفاده از Component برای یک Value</li>
<li>Detach بدون ثبت دلیل</li>
<li>ساخت Component تو‌در‌تو بدون نقشه Dependency</li>
</ul><hr/></section><section aria-labelledby="concept-v31-22-section-12" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-22-section-12">تصویر ذهنی نهایی</h3><p>Master نقشهٔ مادر است و Instance شعبه. Exposed Property پنجره‌ای است که مدیر شعبه اجازه دارد تغییر دهد. Detach یعنی شعبه از زنجیره جدا شده است؛ آزادی بیشتری می‌گیرد، اما دیگر به‌روزرسانی مرکزی دریافت نمی‌کند.</p><hr/></section><section aria-labelledby="concept-v31-22-section-13" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-22-section-13">قوانین طلایی</h3><ul>
<li><strong>«Master ساختار و Style پایه را کنترل می‌کند؛ Instance فقط Propertyهای Exposeشده را.»</strong></li>
<li><strong>«تغییر Master، تغییر محلی نیست؛ دامنهٔ سراسری دارد.»</strong></li>
<li><strong>«Detach برای استثناست، نه برای هر تغییر رایج.»</strong></li>
<li><strong>«تفاوت صرفاً ظاهری را پیش از Component دوم، با Class و Variable بررسی کن.»</strong></li>
<li><strong>«Slot و Variant را بدون سند به‌عنوان قابلیت Native Elementor معرفی نکن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Components</li>
<li>Elementor Help: Classes and Variables</li>
<li>Elementor Help: Editor V4 architecture</li>
</ul><hr/></footer></div></details><section aria-labelledby="components-lab-title" class="lesson-section v30-core-lab" id="components-lifecycle-lab-v30">
<h2 id="components-lab-title">Components Lifecycle Lab</h2>
<p class="status-line"><code dir="ltr">verified_by_official_elementor_help</code></p>
<svg aria-labelledby="component-life-title component-life-desc" class="architecture-svg component-lifecycle-svg" role="img" viewbox="0 0 1040 350">
<title id="component-life-title">چرخهٔ عمر Component در Elementor V4</title>
<desc id="component-life-desc">ساختار تکراری Atomic به Master تبدیل می‌شود، propertyهای مجاز expose می‌شوند، Instanceها ساخته و override می‌شوند، Master به‌روزرسانی می‌شود و در صورت نیاز Instance detach می‌شود.</desc>
<g class="svg-node"><rect height="64" rx="14" width="180" x="30" y="45"></rect><text text-anchor="middle" x="120" y="73">Repeated Atomic</text><text text-anchor="middle" x="120" y="97">structure</text></g>
<g class="svg-node"><rect height="64" rx="14" width="150" x="250" y="45"></rect><text text-anchor="middle" x="325" y="85">Create Master</text></g>
<g class="svg-node"><rect height="64" rx="14" width="190" x="440" y="45"></rect><text text-anchor="middle" x="535" y="73">Expose eligible</text><text text-anchor="middle" x="535" y="97">General fields</text></g>
<g class="svg-node"><rect height="64" rx="14" width="150" x="670" y="45"></rect><text text-anchor="middle" x="745" y="85">Add Instances</text></g>
<g class="svg-node"><rect height="64" rx="14" width="150" x="860" y="45"></rect><text text-anchor="middle" x="935" y="73">Instance</text><text text-anchor="middle" x="935" y="97">overrides</text></g>
<g class="svg-node svg-winner"><rect height="64" rx="14" width="180" x="250" y="225"></rect><text text-anchor="middle" x="340" y="253">Update Master</text><text text-anchor="middle" x="340" y="277">propagates</text></g>
<g class="svg-node"><rect height="64" rx="14" width="180" x="500" y="225"></rect><text text-anchor="middle" x="590" y="253">Overrides persist</text><text text-anchor="middle" x="590" y="277">per Instance</text></g>
<g class="svg-node"><rect height="64" rx="14" width="180" x="750" y="225"></rect><text text-anchor="middle" x="840" y="253">Detach Component</text><text text-anchor="middle" x="840" y="277">breaks sync</text></g>
<path class="svg-arrow" d="M210 77H250M400 77H440M630 77H670M820 77H860M935 109V170H340V225M430 257H500M680 257H750"></path>
</svg>
<div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table">
<caption>رفتارهای رسمی چرخهٔ Component</caption><thead><tr><th scope="col">مرحله</th><th scope="col">رفتار مستند</th><th scope="col">مرز</th></tr></thead>
<tbody>
<tr><th scope="row">Requirements</th><td>فقط Atomic Elements؛ ایجاد و ویرایش نیازمند Elementor Pro و Admin-level permission</td><td>Editor permission را حدس نزن</td></tr>
<tr><th scope="row">Master creation</th><td>ساختار Atomic تکراری به Master تبدیل می‌شود</td><td>برای style-only از Class/Variable استفاده کن</td></tr>
<tr><th scope="row">Exposed properties</th><td>فقط fieldهای General tab که property icon دارند قابل شخصی‌سازی‌اند</td><td>هر Style field قابل expose نیست</td></tr>
<tr><th scope="row">Instance</th><td>نمونه به Master متصل است</td><td>Content variation فقط از propertyهای exposeشده</td></tr>
<tr><th scope="row">Override</th><td>مقدار Instance اختصاصی است و بعد از Master update باقی می‌ماند</td><td>overrideهای زیاد نشانهٔ Component بدطراحی‌شده می‌تواند باشد</td></tr>
<tr><th scope="row">Master update</th><td>تغییر Master به Instanceها sync می‌شود</td><td>blast radius را preview کن</td></tr>
<tr><th scope="row">Property grouping</th><td>propertyها قابلیت گروه‌بندی دارند</td><td>برای خوانایی و workflow</td></tr>
<tr><th scope="row">Detach</th><td>Instance از Component جدا و از updateهای بعدی مستقل می‌شود</td><td>sync از بین می‌رود</td></tr>
<tr><th scope="row">Component nesting</th><td><code dir="ltr">status: insufficient_evidence</code></td><td>بدون سند فعلی یا fixture ادعا نمی‌شود</td></tr>
</tbody></table></div>
<h3>Refactor exercise</h3><ol><li>سه Feature Card تکراری را شناسایی کن.</li><li>ابتدا Style مشترک را با Class/Variable جدا کن.</li><li>اگر Structure نیز تکراری و پایدار است، Master بساز.</li><li>فقط title، text، image یا link واجد icon را expose کن.</li><li>دو Instance با override متفاوت بساز و Master را تغییر بده.</li><li>ماندگاری override و propagation را بررسی کن.</li></ol>
<aside class="warning-box"><strong>چه وقت Component نسازیم؟</strong> ساختار یک‌بارمصرف، تفاوت‌های ساختاری زیاد، Component بسیار بزرگ، propertyهای بیش‌ازحد یا زمانی که فقط یک Style مشترک داریم.</aside>
</section><details class="lesson-disclosure settings-values-units" id="lesson-v17-components-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-v17-components-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Component واحد ندارد؛ Propertyهای Master و Instance دارند</span></summary>
<section aria-labelledby="lesson-v17-components-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Component یک ساختار و قرارداد reuse است. اندازه‌های داخل Master یا overrideهای Instance نوع و واحد مستقل دارند.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> قالب محصول متر نیست؛ ابعاد هر قطعهٔ داخل قالب اندازه‌گیری می‌شود.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Component identity</th><td><code dir="ltr">master / instance reference</code></td><td>reference</td><td>بدون واحد</td><td>برای sync ساختار.</td><td>Component را با Size Variable اشتباه نگیر.</td><td><code dir="ltr">E_COMPONENTS</code></td></tr><tr><th scope="row">Master style</th><td><code dir="ltr">class/property values</code></td><td>واحدهای Propertyهای داخلی</td><td>Property context</td><td>برای baseline مشترک.</td><td>عدد بدون intent را در Master قفل نکن.</td><td><code dir="ltr">E_COMPONENTS</code></td></tr><tr><th scope="row">Instance override</th><td><code dir="ltr">per-instance value</code></td><td>نوع همان Property</td><td>Instance context</td><td>برای تغییر مجاز محلی.</td><td>override زیاد ارزش Component را کم می‌کند.</td><td><code dir="ltr">E_COMPONENTS</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Master padding=1rem و root=16px، همهٔ Instanceها 16px می‌گیرند مگر override یا context متفاوت وجود داشته باشد.</p></section>
<section><h3>📱 در Responsive</h3><p>Contract مشخص کند کدام Sizeها در Master responsive هستند و کدام override Instance مجاز است.</p></section>
<section><h3>🔬 در DevTools</h3><p>منبع declaration را بین Master/Class/Local override تفکیک کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/components-2/" rel="noopener noreferrer" target="_blank">Elementor V4 — Components</a>، <a href="https://elementor.com/help/classes-in-elementor-2/" rel="noopener noreferrer" target="_blank">Elementor V4 — Classes</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">B. چه زمانی Component بسازم؟</span></summary><section class="disclosure-content lesson-section">
<p>وقتی فقط رنگ و فاصله مشترک است، Global Class کافی است. وقتی یک ساختار کامل تکرار می‌شود — مثلاً تصویر، عنوان، متن، Button و Badge با هم — Component فکر درست‌تری است.</p>
<div class="callout"><strong>قانون استاد:</strong> اگر چیزی را با یک Class نمی‌توانی توضیح بدهی، شاید Component است. اگر فقط یک مقدار است، Variable است. اگر فقط یک ظاهر مشترک است، Global Class است.</div>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">C. تمرین ملموس با صفحات خودت</span></summary><section class="disclosure-content lesson-section">
<ol><li>یک کارت تکراری در Home2 یا Solutions پیدا کن.</li><li>تصمیم بگیر کدام بخش‌ها ثابت‌اند: ساختار، spacing، radius، icon position.</li><li>تصمیم بگیر کدام بخش‌ها باید برای هر Instance تغییر کنند: عنوان، متن، لینک، تصویر.</li><li>اول با Global Class تمیزش کن؛ اگر هنوز ساختار تکراری است، آن را کاندید Component بدان.</li></ol>
<p><strong>Exit Ticket:</strong> چرا ساختن Component برای یک Button ساده معمولاً زیاده‌روی است؟</p>
</section></details>
<details class="lesson-disclosure" id="lesson-v17-components-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Component در برابر Template / Pattern</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Component</h3><p>Component قطعهٔ ساختاری تکرارشونده با Master و Instance است؛ مثل Product Card یا Testimonial Card.</p></section>
<section class="inline-compare-card"><h3>Template / Pattern</h3><p>Template یا Pattern معمولاً محدودهٔ بزرگ‌تر یا الگوی صفحه/سکشن است. Component برای قطعهٔ قابل تکرار و کنترل‌پذیر مناسب‌تر است.</p></section>
</div>
</section></details>
</article>
