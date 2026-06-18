<article class="lesson card-surface" data-trackable="lesson-v17-variables" id="lesson-v17-variables">
<h2 class="former-h1">تکمیلی 18B — Variables Manager و Design Tokens</h2>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🧭 قطب‌نمای درس</span></summary><section class="disclosure-content lesson-section">
<p><strong>هدف:</strong> بفهمی Variable یعنی «مقدار مرکزی»، نه «ترفند سریع». وقتی رنگ، فونت، فاصله یا اندازه را چند بار استفاده می‌کنی، Variable ذهن تو را از حفظ کردن عددها نجات می‌دهد.</p>
</section></details>
<section class="lesson-section lesson-core-concept" data-core-concept="true">
<h2>A. بفهم — Variable یعنی یک منبع حقیقت برای مقدار</h2>
<p>فرض کن در صفحه ۱۲ بار رنگ سبز برند را زده‌ای. اگر رنگ برند عوض شود و تو ۱۲ جا را دستی تغییر بدهی، داری با صفحه مذاکره می‌کنی، نه طراحی سیستماتیک. Variable می‌گوید: «این مقدار یک نام دارد، و همه‌جا از همان نام استفاده می‌کنیم.»</p>
<table><caption>جدول آموزشی دوره — A. بفهم — Variable یعنی یک منبع حقیقت برای مقدار</caption><thead><tr><th scope="col">نوع Variable</th><th scope="col">مثال خوب</th><th scope="col">کجا استفاده شود؟</th></tr></thead><tbody>
<tr><td>Color</td><td><code class="inline-code" dir="ltr">color-brand-primary</code></td><td>text، background، border، stateها</td></tr>
<tr><td>Font</td><td><code class="inline-code" dir="ltr">font-body</code></td><td>Typography و خانوادهٔ فونت</td></tr>
<tr><td>Size</td><td><code class="inline-code" dir="ltr">space-m</code> یا <code class="inline-code" dir="ltr">radius-s</code></td><td>spacing، size، radius در جاهایی که UI اجازه می‌دهد</td></tr>
</tbody></table>
<aside class="teacher-note"><p><strong>شفاف‌سازی استاد:</strong> Variable را برای «مقداری که معنا دارد» بساز، نه برای هر عددی که می‌بینی. <code class="inline-code" dir="ltr">24px</code> فقط عدد است؛ <code class="inline-code" dir="ltr">space-section-y</code> تصمیم طراحی است.</p></aside>
</section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="89198659d93a95102e67ec3f140ee48b1d20a7355a42d32783710d64f9232c0e" id="lesson-v17-variables-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Variable و Design Token؛ مقدار نام‌دار با دامنهٔ اثر</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="23" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-23-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-23-section-01">مسئله‌ای که Variable حل می‌کند</h3><p>در یک سایت بزرگ، مقدارهای مشترک در صدها Property مصرف می‌شوند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">رنگ برند
Font اصلی
فاصله استاندارد
Radius
اندازه عنوان
</code></pre></figure><p>اگر مقدار خام را در همه‌جا تکرار کنی، تغییر آن دشوار و ردیابی مصرف‌ها مبهم می‌شود.</p><p>Variable یک مقدار نام‌دار و مرکزی می‌سازد.</p><hr/></section><section aria-labelledby="concept-v31-23-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-23-section-02">تشبیه به دنیای واقعی: شمارهٔ تماس مرکزی</h3><p>فرض کن روی صد بروشور شماره مستقیم یک کارمند چاپ شده است. با تغییر کارمند، باید همه بروشورها را عوض کنی.</p><p>اگر به‌جای شماره مستقیم نوشته باشد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">تماس با پشتیبانی مرکزی
</code></pre></figure><p>و سیستم مرکزی شماره واقعی را نگه دارد، فقط یک نقطه تغییر می‌کند.</p><p>Variable همین لایهٔ ارجاع است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">brand-primary → #004526
</code></pre></figure><p>مصرف‌کننده نام را می‌شناسد؛ مقدار از Registry می‌آید.</p><hr/></section><section aria-labelledby="concept-v31-23-section-03" class="concept-reference-part"><h3 id="concept-v31-23-section-03">Value و Reference را جدا کن</h3><p>این دو یکسان نیستند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Observed value: #004526
Saved reference: brand-primary
</code></pre></figure><p>در Editor ممکن است رنگ نهایی را ببینی، اما سند در واقع Reference را ذخیره کند. این تفکیک برای Export، Migration و Debugging بسیار مهم است.</p><p>اگر Variable حذف شود، Reference ممکن است Unresolved شود. نباید مقدار قبلی را بی‌صدا حدس زد.</p><hr/></section><section aria-labelledby="concept-v31-23-section-04" class="concept-reference-part"><h3 id="concept-v31-23-section-04">نام‌گذاری Primitive و Semantic</h3><h4>Primitive</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">color-green-900
space-6
radius-2
</code></pre></figure><p>ساختار Scale را توصیف می‌کند.</p><h4>Semantic</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">color-brand-primary
space-section-inline
radius-card
</code></pre></figure><p>نقش را توصیف می‌کند.</p><p>هر دو سطح مفیدند. Primitive برای Palette و Scale، Semantic برای Intent.</p><hr/></section><section aria-labelledby="concept-v31-23-section-05" class="concept-reference-part"><h3 id="concept-v31-23-section-05">Token Tiering</h3><p>مدل مفهومی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Primitive
green-900 = #004526
       ↓
Semantic
brand-primary = green-900
       ↓
Component use
button background = brand-primary
</code></pre></figure><p>این زنجیره ذهن سیستم‌ساز را قوی می‌کند، اما پشتیبانی Variable-to-Variable Reference در Elementor باید با Export واقعی نسخه هدف تأیید شود.</p><p>راه مطمئن‌تر تا زمان اثبات:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Variable معنایی
↓
Global Class
↓
Component
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-23-section-06" class="concept-reference-part concept-reference-definition"><h3 id="concept-v31-23-section-06">Variable چه چیزی نیست؟</h3><p>Variable مجموعه Style نیست.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">card-surface = background + padding + border + shadow
</code></pre></figure><p>این دیگر یک Value ساده نیست؛ Global Class یا Component Style مناسب‌تر است.</p><p>Variable همچنین ساختار تولید نمی‌کند.</p><hr/></section><section aria-labelledby="concept-v31-23-section-07" class="concept-reference-part"><h3 id="concept-v31-23-section-07">دامنهٔ اثر</h3><p>تغییر Variable مرکزی ممکن است ده‌ها مصرف‌کننده را تغییر دهد.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">space-lg
├── Section Padding
├── Card Gap
├── Form Row Gap
└── Header Height calculation
</code></pre></figure><p>اگر یک Variable در نقش‌های نامرتبط استفاده شده باشد، تغییر آن باعث اثرهای ناخواسته می‌شود. به این وضعیت Coupling پنهان می‌گوییم.</p><p>مثلاً استفاده از یک Variable به نام <code class="inline-code" dir="ltr">space-32</code> در همه‌جا شاید ساده باشد، اما اگر بعداً Section Padding باید 40 و Card Gap باید 24 شود، نقش‌ها از هم جدا می‌شوند.</p><p>Semantic Token این Coupling را آشکارتر می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-23-section-08" class="concept-reference-part"><h3 id="concept-v31-23-section-08">Type Compatibility</h3><p>هر Variable برای هر Property مناسب نیست. Color، Font Family و Size نوع‌های متفاوتی دارند.</p><p>دسترسی Variableها نیز ممکن است به نسخه، Plan و Property وابسته باشد. مستندات فعلی باید برای قابلیت دقیق نسخه هدف بررسی شوند؛ نباید فرض کرد هر Property Effects، Shadow یا Layout حتماً Variable می‌پذیرد.</p><hr/></section><section aria-labelledby="concept-v31-23-section-09" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-23-section-09">در Elementor V4</h3><p>Variables Manager محل ساخت و مدیریت Variableهاست. هنگام استفاده:</p><ol>
<li>نقش Variable را نام‌گذاری کن.</li>
<li>Type آن را درست انتخاب کن.</li>
<li>مصرف‌کنندگان نماینده را ثبت کن.</li>
<li>پیش از Delete، Referenceهای وابسته را پیدا کن.</li>
<li>در Hybrid V3/V4، Sync با Global Colors/Fonts را جداگانه بررسی کن.</li>
<li>Export Design System را برای انتقال Variables و Classes استفاده کن، اما ZIP را به‌عنوان شواهد نسخه‌دار نگه دار.</li>
</ol><hr/></section><section aria-labelledby="concept-v31-23-section-10" class="concept-reference-part"><h3 id="concept-v31-23-section-10">چه زمانی Variable نسازیم؟</h3><p>یک مقدار یک‌بارمصرف که هویت معنایی و نیاز تغییر مرکزی ندارد، لزوماً Variable نمی‌خواهد.</p><p>مثال:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">offset تزئینی خاص یک Illustration = 13px
</code></pre></figure><p>اگر فقط در همان Stage معنا دارد، Local Value می‌تواند خواناتر باشد.</p><p>هدف حذف تمام Literalها نیست؛ هدف مدیریت تصمیم‌های مشترک است.</p><hr/></section><section aria-labelledby="concept-v31-23-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-23-section-11">اشتباهات رایج</h3><ul>
<li>Variable برای هر عدد</li>
<li>نام‌گذاری فقط با رنگ فعلی</li>
<li>استفاده یک Token برای نقش‌های نامرتبط</li>
<li>حذف Variable بدون بررسی Referenceها</li>
<li>فرض زنجیره Alias بدون شواهد</li>
<li>فرض پشتیبانی همه Propertyها</li>
<li>Sync V3/V4 بدون درک محدودیت‌ها</li>
<li>استفاده از Variable به‌جای Global Class</li>
</ul><hr/></section><section aria-labelledby="concept-v31-23-section-12" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-23-section-12">تصویر ذهنی نهایی</h3><p>Variable شمارهٔ تماس مرکزی است. اگر هر بروشور شماره خام خودش را چاپ کند، تغییر پرهزینه است. اما اگر همه به دفتر مرکزی اشاره کنند، تغییر یکجا انجام می‌شود—به شرطی که دفتر مرکزی نقش‌های نامرتبط را با یک شماره قاطی نکرده باشد.</p><hr/></section><section aria-labelledby="concept-v31-23-section-13" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-23-section-13">قوانین طلایی</h3><ul>
<li><strong>«Variable یک Value نام‌دار است، نه بسته Style.»</strong></li>
<li><strong>«Reference و مقدار Resolveشده را دو چیز جدا بدان.»</strong></li>
<li><strong>«نام معنایی دامنهٔ تغییر را روشن می‌کند.»</strong></li>
<li><strong>«هر Variable مرکزی یک Dependency Graph دارد.»</strong></li>
<li><strong>«Alias Chain و پشتیبانی Propertyها را با نسخه واقعی تأیید کن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Variables and Variables Manager</li>
<li>Elementor Help: Import/export design systems</li>
<li>Elementor Help: Sync variables and global elements</li>
</ul><hr/></footer></div></details><section aria-labelledby="variables-lab-title" class="lesson-section v30-core-lab" id="variables-architecture-lab-v30">
<h2 id="variables-lab-title">آزمایشگاه معماری Variables</h2>
<p class="status-line"><code dir="ltr">verified_by_official_elementor_help + derived_educational_model + proposed_strategy</code></p>
<div aria-label="انواع رسمی Variable" class="official-types-strip"><strong>انواع رسمی دقیق:</strong><span>Color</span><span>Font</span><span>Size</span></div>
<p><strong>Variable یک مقدار نام‌دار یا reference است.</strong> فقط Size Variable ممکن است اندازه و unit داشته باشد؛ Color و Font با «value + unit» تعریف نمی‌شوند.</p>
<div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table">
<caption>لایه‌های Variable Architecture</caption><thead><tr><th scope="col">لایه</th><th scope="col">نقش</th><th scope="col">Evidence label</th><th scope="col">نمونه</th></tr></thead>
<tbody>
<tr><th scope="row">Official Variable</th><td>Color، Font یا Size named value</td><td><code dir="ltr">verified_by_official_elementor_help</code></td><td><code dir="ltr">color-brand-primary</code></td></tr>
<tr><th scope="row">Primitive token</th><td>مقدار پایه مثل blue-600 یا size-4</td><td><code dir="ltr">derived_educational_model</code></td><td>نام‌گذاری پیشنهادی، نه نوع رسمی</td></tr>
<tr><th scope="row">Semantic token</th><td>معنای کاربردی مثل surface-accent یا space-card</td><td><code dir="ltr">derived_educational_model</code></td><td>می‌تواند با Variable رسمی پیاده شود</td></tr>
<tr><th scope="row">Spacing scale</th><td>راهبرد استفاده از Size Variables</td><td><code dir="ltr">proposed_strategy</code></td><td>space-1 / space-2 / space-3</td></tr>
<tr><th scope="row">Typography scale</th><td>راهبرد ترکیب Font و Size Variables</td><td><code dir="ltr">proposed_strategy</code></td><td>type-body / type-heading</td></tr>
</tbody></table></div>
<div class="architecture-principles-grid">
<section><h3>Variable داخل Class</h3><p>Class declaration می‌تواند Variable را مصرف کند. با ویرایش Variable، همهٔ مصرف‌کنندگان آن reference تغییر می‌کنند؛ دامنهٔ propagation را پیش از update بررسی کن.</p></section>
<section><h3>Import / Export Design System</h3><p>Design System به‌صورت یک ZIP شامل Variables و Classes صادر و وارد می‌شود. import انتخابیِ یک Variable یا Class منفرد پشتیبانی مستند ندارد؛ conflict نام با replace یا keep existing مدیریت می‌شود.</p></section>
<section><h3>Hybrid sync</h3><p>Color و Font Variableهای Atomic می‌توانند برای workflow ترکیبی با V3 به Global Colors یا Global Fonts sync شوند. sync فونت به Typography محدود است و همهٔ ویژگی‌های فونت را منتقل نمی‌کند.</p></section>
<section><h3>Naming convention</h3><p><code dir="ltr">proposed_strategy</code>: نام باید role، scope و intent را روشن کند؛ اما semantic/primitive naming قانون رسمی Elementor نیست.</p></section>
</div>
<h3>Anti-patternها</h3>
<ul class="audit-list"><li>Variable برای هر مقدار one-off؛</li><li>یک Size Variable برای نقش‌های معنایی نامرتبط؛</li><li>نام‌هایی مثل <code dir="ltr">blue-24-final-2</code> بدون role؛</li><li>ساخت «Space Variable» یا «Typography Variable» به‌عنوان نوع رسمی ساختگی؛</li><li>انتظار import انتخابی از بستهٔ کامل؛</li><li>تغییر Variable بدون بررسی Classها، Components، breakpointها و صفحات مصرف‌کننده.</li></ul>
<aside class="teacher-note"><strong>چه چیزی Variable نشود؟</strong> مقدار محلی یکتا، آزمایشی، ناپایدار یا وابسته به یک exception که معنای مشترک و reuse قابل دفاع ندارد.</aside>
</section><details class="lesson-disclosure settings-values-units" id="lesson-v17-variables-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-v17-variables-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Size Variable؛ واحد بخشی از مقدار است</span></summary>
<section aria-labelledby="lesson-v17-variables-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Variable Size فقط عدد نیست؛ 16px، 1rem و 5vw سه intent متفاوت‌اند. نام Variable باید intent را منتقل کند، نه فقط عدد را.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> روی ظرف ادویه فقط «16» ننویس؛ بنویس 16 گرم یا 16 میلی‌لیتر و کاربردش چیست.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Color Variable</th><td><code dir="ltr">color token</code></td><td>color</td><td>بدون طول</td><td>برای رنگ سیستم.</td><td>با Size Variable جابه‌جا نشود.</td><td><code dir="ltr">E_VAR_MANAGER</code></td></tr><tr><th scope="row">Font Variable</th><td><code dir="ltr">font token</code></td><td>font family</td><td>بدون طول</td><td>برای خانوادهٔ فونت.</td><td>Font Variable اندازه نیست.</td><td><code dir="ltr">E_VAR_MANAGER</code></td></tr><tr><th scope="row">Size Variable</th><td><code dir="ltr">size token</code></td><td>عدد + واحد</td><td>واحد ذخیره‌شده</td><td>برای spacing/size مشترک سازگار.</td><td>یک token را برای contextهای نامرتبط استفاده نکن.</td><td><code dir="ltr">E_VAR_MANAGER</code></td></tr><tr><th scope="row">Literal fallback</th><td><code dir="ltr">property value</code></td><td>همان grammar Property</td><td>context Property</td><td>برای مقدار محلی یا fallback.</td><td>Literal زیاد consistency را کم می‌کند.</td><td><code dir="ltr">E_VARIABLES</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>--space-4=1rem با root=16px → 16px؛ --hero-height=40vh با viewport height=900px → 360px. هر دو Size هستند اما مرجع متفاوت دارند.</p></section>
<section><h3>📱 در Responsive</h3><p>قبل از Variable مشترک تصمیم بگیر آیا مقدار باید در breakpointها ثابت، override یا fluid باشد.</p></section>
<section><h3>🔬 در DevTools</h3><p>نام Variable، مقدار تعریف‌شده و مقدار resolveشده را ثبت کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/variables/" rel="noopener noreferrer" target="_blank">Elementor V4 — Variables</a>، <a href="https://elementor.com/help/variables-manager/" rel="noopener noreferrer" target="_blank">Elementor V4 — Variables Manager</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">B. Export واقعی ForLesson چه می‌گوید؟</span></summary><section class="disclosure-content lesson-section">
<p><strong>مشاهده:</strong> Export همراه این جزوه در نسخهٔ 16 نشان داد که Global Class وجود دارد، اما Variable واقعی در بسته صفر است. یعنی صفحه از نظر ظاهری می‌تواند ساخته شده باشد، اما Design System آن هنوز کامل نشده است.</p>
<p><strong>حکم استاد:</strong> این یک فرصت آموزشی عالی است: دقیقاً چون صفحه را خودت ساخته‌ای و مقادیرش برایت ملموس است، می‌توانی ببینی چه مقدارهایی باید به Token تبدیل شوند.</p>
<table><caption>جدول آموزشی دوره — B. Export واقعی ForLesson چه می‌گوید؟</caption><thead><tr><th scope="col">مقدار دیده‌شده</th><th scope="col">ریسک اگر محلی بماند</th><th scope="col">Variable پیشنهادی</th></tr></thead><tbody>
<tr><td><code class="inline-code" dir="ltr">#b2b2b2</code></td><td>رنگ placeholder در چند جا پخش می‌شود</td><td><code class="inline-code" dir="ltr">color-surface-muted</code></td></tr>
<tr><td><code class="inline-code" dir="ltr">8px</code> radius</td><td>گوشه‌ها ناسازگار می‌شوند</td><td><code class="inline-code" dir="ltr">radius-s</code></td></tr>
<tr><td>Gapهای تکراری</td><td>فاصله‌ها با چشم تنظیم می‌شوند</td><td><code class="inline-code" dir="ltr">space-m</code> / <code class="inline-code" dir="ltr">space-l</code></td></tr>
<tr><td>فونت بدنه و عنوان</td><td>Typography تکه‌تکه می‌شود</td><td><code class="inline-code" dir="ltr">font-body</code> / <code class="inline-code" dir="ltr">font-heading</code></td></tr>
</tbody></table>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">تمرین</span></summary><section class="disclosure-content lesson-section">
<ol><li>از صفحهٔ خودت ۵ مقدار تکراری پیدا کن.</li><li>برای هرکدام نام معنایی بساز.</li><li>سه مورد را در Variables Manager بساز.</li><li>روی یک Global Class استفاده کن، نه فقط روی یک Element.</li><li>یک مقدار Variable را تغییر بده و ببین چند بخش همزمان تغییر می‌کند.</li></ol>
<p><strong>Exit Ticket:</strong> یک مثال بزن که Variable ساختن برای آن زیاده‌روی است.</p>
</section></details>
<details class="lesson-disclosure" id="lesson-v17-variables-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Variable خام در برابر تصمیم طراحی</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Color/Size/Font Variable</h3><p>Variable فقط مقدار را نگه می‌دارد؛ مثل <code dir="ltr">radius-card = 8px</code> یا <code dir="ltr">space-m = 16px</code>.</p></section>
<section class="inline-compare-card"><h3>Class مصرف‌کنندهٔ Variable</h3><p>Class می‌گوید این مقدار کجا و با چه ترکیبی مصرف شود؛ مثلاً <code dir="ltr">card-base</code> از radius، padding، color و shadow استفاده می‌کند.</p></section>
</div>
</section></details>
</article>
