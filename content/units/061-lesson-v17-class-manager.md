<article class="lesson card-surface" data-trackable="lesson-v17-class-manager" id="lesson-v17-class-manager">
<h2 class="former-h1">تکمیلی 18A — Class Manager و اولویت Global Classها</h2>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🧭 قطب‌نمای درس</span></summary><section class="disclosure-content lesson-section">
<p><strong>هدف:</strong> بفهمی وقتی چند Class روی یک Element نشسته‌اند، Elementor 4 چطور به تو اجازه می‌دهد آن‌ها را پیدا، مرتب، حذف، rename و اولویت‌بندی کنی.</p>
<p class="status-line"><code class="inline-code" dir="ltr">status: official_doc_aligned</code> · بررسی عملی: یک مثال واقعی را بدون حدس تحلیل کن.</p>
</section></details>
<section class="lesson-section lesson-core-concept" data-core-concept="true">
<h2>A. بفهم — Class فقط اسم نیست، قرارداد طراحی است</h2>
<p>تصور کن یک دانش‌آموز گیج سه برچسب روی یک دکمه می‌چسباند: <code class="inline-code" dir="ltr">btn</code>، <code class="inline-code" dir="ltr">btn-primary</code> و <code class="inline-code" dir="ltr">hero-cta</code>. اگر هر سه رنگ بدهند، سؤال اصلی این نیست که «کدام را دوست دارم؟» سؤال این است: <strong>کدام Class مسئول این تصمیم است؟</strong></p>
<p>در Elementor 4 هر Element یک <strong>Local Class</strong> دارد. وقتی Style فقط برای همان Element است، Local Class کافی است. وقتی همان Style باید روی چند Element تکرار شود، باید آن را به <strong>Global Class</strong> منتقل کنی. Global Class یعنی «قانون مشترک طراحی»؛ نه Spacer، نه کپی دستی، نه حافظهٔ ذهنی.</p>
<aside class="teacher-note"><p><strong>شفاف‌سازی استاد:</strong> Global Class همان چیزی است که از نظر آموزشی Global Class است، اما نام رسمی آن در UI و مستندات Elementor 4، Global Class است. پس در جزوه از این به بعد همین نام را یاد می‌گیری.</p></aside>
</section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="4d00f7e7fc97f6ceb3428fa496aebed9fc8e0d41743874f57c7f204bb05c7747" id="lesson-v17-class-manager-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Class Manager؛ سلسله‌مراتب سیستم Style</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="24" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-24-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-24-section-01">مسئله‌ای که Class Manager حل می‌کند</h3><p>در یک سایت Classمحور، مشکل فقط ساخت Class نیست. باید بدانی:</p><ul>
<li>چه Classهایی وجود دارند؛</li>
<li>کجا مصرف شده‌اند؛</li>
<li>کدام یک اولویت بالاتری دارد؛</li>
<li>کدام خالی یا بدون استفاده است؛</li>
<li>تغییر نام یا حذف چه دامنه‌ای دارد.</li>
</ul><p>Class Manager دفتر ثبت قوانین ظاهری سایت است.</p><hr/></section><section aria-labelledby="concept-v31-24-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-24-section-02">تشبیه به دنیای واقعی: آیین‌نامه‌های سازمان</h3><p>یک سازمان چند سطح قانون دارد:</p><ul>
<li>قانون عمومی شرکت</li>
<li>آیین‌نامه واحد</li>
<li>دستور خاص یک کارمند</li>
</ul><p>اگر دو آیین‌نامه درباره لباس تعارض داشته باشند، باید ترتیب اولویت معلوم باشد.</p><p>در Elementor V4:</p><ul>
<li>Local Class مانند دستور خاص همان Element است.</li>
<li>Global Class قانون قابل استفاده در چند Element است.</li>
<li>Class Manager ترتیب رقابت Global Classها را مدیریت می‌کند.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-24-section-03" class="concept-reference-part"><h3 id="concept-v31-24-section-03">Priority در Class Manager</h3><p>مستندات رسمی فعلی می‌گویند Class سمت چپ/بالاتر اولویت بیشتری از Class سمت راست/پایین دارد و Local Class همیشه بیشترین اولویت را می‌گیرد.</p><p>Drag &amp; Drop در Class Manager ترتیب Global Classها را تغییر می‌دهد.</p><p>این Priority را با Specificity عددی CSS یکی ندان. Elementor ممکن است CSS را با Source Order یا سازوکار داخلی طوری تولید کند که این قرارداد اجرا شود.</p><hr/></section><section aria-labelledby="concept-v31-24-section-04" class="concept-reference-part"><h3 id="concept-v31-24-section-04">Resolution Tree</h3><p>وقتی Property نهایی را می‌بینی، این مسیر را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Device/Breakpoint
↓
State
↓
Class فعال برای ویرایش
↓
Local Class explicit value
↓
Global Classهای متصل و Priority Registry
↓
Custom CSS همان Class/State/Device
↓
CSS Cascade مرورگر
↓
Computed Style
</code></pre></figure><p>این یک مدل عیب‌یابی است. ترتیب دقیق همه لایه‌های Custom CSS و Generated CSS باید در موارد حساس با DevTools و Fixture نسخه هدف تأیید شود.</p><hr/></section><section aria-labelledby="concept-v31-24-section-05" class="concept-reference-part"><h3 id="concept-v31-24-section-05">Indicatorهای Style</h3><p>رابط V4 برای منبع یا تعارض Style Indicatorهای رنگی نشان می‌دهد. در مستندات فعلی:</p><ul>
<li>Pink با Local Value مرتبط است.</li>
<li>Green نشان می‌دهد Class فعال برنده است.</li>
<li>Gray نشان می‌دهد مقدار از منبع دیگری می‌آید.</li>
<li>Orange نشان می‌دهد مقدار Class حاضر Override شده است.</li>
</ul><p>با کلیک روی Indicator می‌توان منبع Style و Styleهای نادیده‌گرفته‌شده را دید.</p><p>رنگ و رفتار UI ممکن است در نسخه‌های بعدی تغییر کند؛ بنابراین Screenshot نسخه و تاریخ بررسی را در جزوه نگه دار.</p><hr/></section><section aria-labelledby="concept-v31-24-section-06" class="concept-reference-part"><h3 id="concept-v31-24-section-06">ردیابی شبح Style</h3><p>فرض کن <code class="inline-code" dir="ltr">button-primary</code> را سبز کرده‌ای اما یک Button هنوز نارنجی است.</p><h4>مرحله ۱: State</h4><p>آیا روی Hover هستی و Hover مقدار نارنجی دارد؟</p><h4>مرحله ۲: Breakpoint</h4><p>آیا Mobile Override جدا دارد؟</p><h4>مرحله ۳: Local Class</h4><p>آیا Local Class همان Button رنگ صریح دارد؟</p><h4>مرحله ۴: Global Class رقیب</h4><p>آیا <code class="inline-code" dir="ltr">button-warning</code> نیز متصل است و Priority بالاتری دارد؟</p><h4>مرحله ۵: Custom CSS</h4><p>آیا Selector اختصاصی یا <code class="inline-code" dir="ltr">!important</code> وجود دارد؟</p><h4>مرحله ۶: Computed Style</h4><p>کدام Rule واقعاً برنده شده است؟</p><p>این الگوریتم از حدس‌زدن جلوگیری می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-24-section-07" class="concept-reference-part"><h3 id="concept-v31-24-section-07">Utility Classes در Class Manager</h3><p>Utilityها را با نام‌گذاری روشن نگه دار:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">u-flex-center
u-inline-full
u-overflow-clip
u-space-block-lg
</code></pre></figure><p>اگر تعداد Utilityهای متعارض زیاد شود، Class Manager تبدیل به میدان جنگ Priority می‌شود.</p><p>مثلاً هم‌زمان‌کردن این کلاس‌ها مبهم است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">u-gap-sm
u-gap-lg
u-gap-none
</code></pre></figure><p>بهتر است در هر Element فقط یک Utility از هر مسئولیت متعارض فعال باشد.</p><hr/></section><section aria-labelledby="concept-v31-24-section-08" class="concept-reference-part"><h3 id="concept-v31-24-section-08">Filter و Audit</h3><p>Class Manager می‌تواند برای پیدا کردن Classهای:</p><ul>
<li>روی همین صفحه</li>
<li>بدون استفاده</li>
<li>خالی</li>
</ul><p>مفید باشد.</p><p>اما «بدون استفاده» باید با احتیاط تفسیر شود؛ ممکن است Class در Template، Dynamic Context یا صفحه دیگری مصرف شود. دامنهٔ Filter را بخوان.</p><p>در برخی حالت‌های Filter، Drag &amp; Drop در دسترس نیست؛ برای تغییر ترتیب باید Filter را برداری.</p><hr/></section><section aria-labelledby="concept-v31-24-section-09" class="concept-reference-part"><h3 id="concept-v31-24-section-09">Rename و Delete</h3><p>Rename یک عملیات ظاهراً کوچک با دامنه مرکزی است. نام جدید باید Intent را بهتر کند.</p><p>Delete خطرناک‌تر است:</p><ul>
<li>آیا Class از Elementها جدا می‌شود؟</li>
<li>Style آن‌ها چه می‌شود؟</li>
<li>Local fallback دارند؟</li>
<li>آیا Export یا Component به ID/Class وابسته است؟</li>
</ul><p>پیش از Delete، Usage و Backup را بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-24-section-10" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-24-section-10">در Elementor V4</h3><p>فرایند نگهداری دوره‌ای:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Find unused
↓
Find empty
↓
Review duplicate intent
↓
Review conflicting utilities
↓
Review priority order
↓
Rename with semantic names
↓
Delete only after impact check
</code></pre></figure><p>Class Manager فقط محل مرتب‌سازی نیست؛ ابزار معماری است.</p><hr/></section><section aria-labelledby="concept-v31-24-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-24-section-11">اشتباهات رایج</h3><ul>
<li>تغییر Priority برای حل هر تعارض به‌جای حذف مقدار اشتباه</li>
<li>نام‌های <code class="inline-code" dir="ltr">class-1</code> و <code class="inline-code" dir="ltr">green-text</code></li>
<li>چند Utility متعارض روی یک Element</li>
<li>حذف Class بدون Usage Audit</li>
<li>اشتباه‌گرفتن Priority Elementor با Specificity CSS</li>
<li>ویرایش State یا Breakpoint اشتباه</li>
<li>Reset نکردن Local Override</li>
<li>Drag &amp; Drop در حالت Filter و تصور خرابی UI</li>
</ul><hr/></section><section aria-labelledby="concept-v31-24-section-12" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-24-section-12">پل به DevTools</h3><p>Class Manager می‌گوید سیستم Elementor چه Intentی دارد. DevTools می‌گوید مرورگر چه Ruleای را اجرا کرده است.</p><p>در Styles Panel:</p><ul>
<li>Rule خط‌خورده را ببین.</li>
<li>Selector برنده را پیدا کن.</li>
<li>Source file/order را بررسی کن.</li>
<li>Computed Value را تأیید کن.</li>
</ul><p>هر دو شاهد لازم‌اند.</p><hr/></section><section aria-labelledby="concept-v31-24-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-24-section-13">تصویر ذهنی نهایی</h3><p>Class Manager دفتر آیین‌نامه‌هاست. Local Class دستور ویژه همان اتاق است. Global Class قانون سازمانی است. اگر قوانین تعارض دارند، فقط صدای قانون را بلندتر نکن؛ منبع تعارض را پیدا کن.</p><hr/></section><section aria-labelledby="concept-v31-24-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-24-section-14">قوانین طلایی</h3><ul>
<li><strong>«Local Class همیشه بالاترین اولویت Elementor را دارد.»</strong></li>
<li><strong>«Priority Global Classها در Class Manager مدیریت می‌شود.»</strong></li>
<li><strong>«Priority Elementor و Specificity CSS یک مفهوم واحد نیستند.»</strong></li>
<li><strong>«Indicator را بخوان؛ از روی ظاهر حدس نزن.»</strong></li>
<li><strong>«حذف و Rename Class عملیات سراسری‌اند، نه ویرایش محلی.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: The Elementor Editor Class Manager</li>
<li>Elementor Help: Prioritize conflicting styles</li>
<li>Elementor Help: Classes in Elementor</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-v17-class-manager-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-v17-class-manager-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Class Manager ترتیب می‌دهد، نه واحد</span></summary>
<section aria-labelledby="lesson-v17-class-manager-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Reorder، Rename و Delete عملیات ساختاری‌اند. واحدها داخل declarationهای Class باقی می‌مانند.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> Class Manager قفسه‌بندی کتاب‌هاست؛ وزن هر کتاب را تغییر نمی‌دهد.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Class order</th><td><code dir="ltr">cascade priority</code></td><td>ترتیب</td><td>بدون واحد</td><td>برای conflict Global Classها.</td><td>ترتیب را با مقدار Property مقایسه نکن.</td><td><code dir="ltr">E_CLASS_MANAGER</code></td></tr><tr><th scope="row">Class declaration</th><td><code dir="ltr">property:value</code></td><td>نوع Property</td><td>Property context</td><td>برای Style واقعی.</td><td>دو Class با واحد متفاوت با priority حل می‌شوند، نه تبدیل خودکار.</td><td><code dir="ltr">E_CLASSES</code></td></tr><tr><th scope="row">Local Class</th><td><code dir="ltr">highest local priority</code></td><td>scope/order</td><td>بدون واحد</td><td>برای استثنای Element.</td><td>Local می‌تواند Global را بپوشاند.</td><td><code dir="ltr">E_CLASSES</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>Global A width=40rem و Global B width=50%؛ برنده را Class priority تعیین می‌کند، نه اینکه 40 از 50 کوچک‌تر است.</p></section>
<section><h3>📱 در Responsive</h3><p>priority ثابت می‌ماند اما declaration responsive ممکن است per breakpoint تغییر کند.</p></section>
<section><h3>🔬 در DevTools</h3><p>matched rules و source class را در breakpoint فعال بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/the-elementor-editor-class-manager/" rel="noopener noreferrer" target="_blank">Elementor V4 — Class Manager</a>، <a href="https://elementor.com/help/classes-in-elementor-2/" rel="noopener noreferrer" target="_blank">Elementor V4 — Classes</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">B. Class Manager را مثل اتاق کنترل ببین</span></summary><section class="disclosure-content lesson-section">
<p>Class Manager جای دیدن کل سیستم کلاس‌هاست. وقتی پروژه بزرگ می‌شود، پیدا کردن یک Class از داخل تک‌تک Elementها مثل گشتن دنبال پیچ در انبار تاریک است. Class Manager چراغ انبار است: می‌فهمی چه کلاس‌هایی داری، کجا استفاده شده‌اند، کدام خالی یا بی‌استفاده‌اند و ترتیب اولویتشان چیست.</p>
<table><caption>جدول آموزشی دوره — B. Class Manager را مثل اتاق کنترل ببین</caption><thead><tr><th scope="col">کار</th><th scope="col">تصمیم درست</th><th scope="col">اشتباه رایج</th></tr></thead><tbody>
<tr><td>Rename</td><td>نام Class را بر اساس نقش بگذار: <code class="inline-code" dir="ltr">card-feature</code></td><td>نام ظاهری مبهم: <code class="inline-code" dir="ltr">blue-box-2</code></td></tr>
<tr><td>Delete</td><td>قبل از حذف، usage را بررسی کن</td><td>حذف چون «الان دیده نمی‌شود»</td></tr>
<tr><td>Reorder</td><td>ترتیب را وقتی Propertyها تعارض دارند آگاهانه تغییر بده</td><td>جابجایی تصادفی برای «درست شدن موقت»</td></tr>
<tr><td>Locate usage</td><td>قبل از refactor ببین Class کجا نشسته</td><td>حدس زدن از روی ظاهر صفحه</td></tr>
</tbody></table>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">C. عمیق‌تر نگاه کن — Buttonهای ForLesson</span></summary><section class="disclosure-content lesson-section">
<p><strong>مشاهده از Export:</strong> در صفحات ForLesson چند دکمه و آیتم تکراری دیده می‌شوند. اگر هر دکمه padding، radius، typography و رنگ جداگانه بگیرد، صفحه فعلاً کار می‌کند اما آینده‌اش شکننده می‌شود.</p>
<p><strong>حکم استاد:</strong> برای دکمه‌هایی که نقش مشترک دارند، Global Class بساز. برای تفاوت متن یا لینک، Global Class نساز؛ آن‌ها محتوا هستند. برای تفاوت کوچک یک دکمهٔ خاص، اول ببین آیا modifier لازم داری یا Local override کافی است.</p>
<div class="callout"><strong>قانون:</strong> هر Style تکراری که اگر فردا تغییر کند باید همه‌جا همزمان تغییر کند، کاندید Global Class است.</div>
</section></details>
<details class="lesson-disclosure" id="class-priority-build-test"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">تمرین</span></summary><section class="disclosure-content lesson-section">
<ol><li>سه Button مشابه پیدا کن.</li><li>یک Global Class با نام نقش‌محور بساز.</li><li>padding، radius، font و رنگ مشترک را به آن منتقل کن.</li><li>یک تفاوت عمدی بساز و بررسی کن آیا باید Local override باشد یا Global Class دوم.</li></ol>
<p><strong>Exit Ticket:</strong> در یک جمله بگو چرا «کپی کردن استایل» با «ساختن Global Class» فرق دارد.</p>
<p class="stv2-back-link"><a href="#stv2-class-priority">↩ بازگشت به Step‑Through v2 اولویت Classها</a></p></section></details>
<details class="lesson-disclosure" id="lesson-v17-class-manager-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Class Manager در برابر Classes Field</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Classes Field</h3><p>Classes Field محل اتصال کلاس‌ها به همین Element است؛ مثل برچسب‌هایی که روی یک وسیله می‌چسبانی.</p></section>
<section class="inline-compare-card"><h3>Class Manager</h3><p>Class Manager مرکز مدیریت کل سیستم کلاس‌هاست: rename، delete، reorder، locate و priority.</p><p class="golden-rule">قانون طلایی: اتصال در Classes Field؛ سیاست و اولویت در Class Manager.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="class-manager-practical-findings"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="class-manager-practical-findings-heading" role="heading">🔎 یافتهٔ عملی و خطایابی</span></summary><section aria-labelledby="class-manager-practical-findings-heading" class="disclosure-content practical-findings">
<p class="finding-scope">این بخش فقط ادعاهایی را آموزش می‌دهد که یا در مشاهدهٔ واقعی ثبت شده‌اند یا Help Center رسمی Elementor آن‌ها را صریحاً پشتیبانی می‌کند. نتیجه‌های وابسته به Theme، نسخه یا ساختار DOM با دامنهٔ اعتبار نوشته شده‌اند.</p>
<article class="finding-card" data-verification="verified_by_official_help" id="finding-class-added-last-not-winning">
<div class="evidence-badges"><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>چرا کلاسی که آخر اضافه کردم، برنده نشد؟</h3>
<p><strong>برداشت اشتباه:</strong> آخرین Class متصل‌شده باید همیشه Style قبلی را override کند.</p>
<p><strong>قاعدهٔ رسمی V4:</strong> ترتیب priority در Class Manager تعیین‌کننده است. Class سمت چپ در Classes field اولویت بالاتری دارد و Local Class، چون همیشه چپ‌ترین است، بالاترین اولویت را نگه می‌دارد.</p>
<div class="finding-checks">
<section><h4>در Elementor</h4><p>Class Manager را باز کن، ترتیب Classها و indicatorهای رنگی هر property را ببین.</p></section>
<section><h4>راه‌حل درست</h4><p>اول conflict غیرضروری را کم کن؛ فقط وقتی contract طراحی ایجاب می‌کند priority registry را تغییر بده.</p></section>
</div>
<p class="golden-rule"><strong>قانون طلایی:</strong> زمان افزودن Class با اولویت ثبت‌شدهٔ Class یکی نیست.</p>
<details class="more-know"><summary>منابع رسمی</summary><p><a href="https://elementor.com/help/prioritize-conflicting-styles/">Prioritize conflicting styles</a> و <a href="https://elementor.com/help/the-elementor-editor-class-manager/">Class Manager</a></p></details>
</article>
</section></details><details class="lesson-disclosure step-through-v2-disclosure" id="stv2-class-priority">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="stv2-class-priority-heading" role="heading">▶ Step‑Through v2 — Local Class، Global Class و Priority — برنده چگونه تعیین می‌شود؟</span>
</summary>
<section aria-labelledby="stv2-class-priority-heading" class="disclosure-content step-through-v2" data-step-through-v2="" data-stv2-id="stv2-class-priority" data-stv2-renderer="class-priority" tabindex="0">
<header class="stv2-header">
<p class="stv2-kicker">چرخهٔ فعال: ببین ← پیش‌بینی کن ← بررسی کن ← خراب کن ← انتقال بده</p>
<p><strong>🎯 هدف:</strong> اولویت Local Class و ترتیب Global Classها را بدون تکیه بر زمان افزودن کلاس‌ها بفهم.</p>
<div aria-label="وضعیت شواهد" class="stv2-evidence-row"><span class="stv2-evidence-badge">تأییدشده با Help Center رسمی Elementor</span><span class="stv2-evidence-badge">تأییدشده با Help Center رسمی Elementor</span></div>
</header>
<div class="stv2-progress-row">
<span class="stv2-step-count" data-stv2-count="">مرحله ۱</span>
<progress data-stv2-progress="" max="7" value="1">1/4</progress>
<span class="stv2-phase" data-stv2-phase=""></span>
</div>
<div class="stv2-three-view">
<section aria-labelledby="stv2-class-priority-visual-title" class="stv2-card stv2-visual-card">
<h3 id="stv2-class-priority-visual-title">👁 نتیجهٔ بصری</h3>
<div aria-label="نمای بصری مرحله" class="stv2-visual" data-stv2-visual=""></div>
</section>
<section aria-labelledby="stv2-class-priority-elementor-title" class="stv2-card">
<h3 id="stv2-class-priority-elementor-title">🧩 تنظیم Elementor</h3>
<dl class="stv2-definition-list" data-stv2-elementor=""></dl>
</section>
<section aria-labelledby="stv2-class-priority-computed-title" class="stv2-card">
<h3 id="stv2-class-priority-computed-title">🔬 Computed / مدل محاسباتی</h3>
<dl class="stv2-definition-list" data-stv2-computed=""></dl>
<p class="stv2-model-note">اعداد نمایشی ممکن است مدل آموزشی باشند؛ برچسب شواهد هر مرحله را ببین.</p>
</section>
</div>
<section aria-labelledby="stv2-class-priority-state-title" class="stv2-explanation">
<h3 data-stv2-title="" id="stv2-class-priority-state-title"></h3>
<p data-stv2-summary=""></p>
<p data-stv2-explanation=""></p>
<p class="golden-rule"><strong>📜 قانون طلایی:</strong> <span data-stv2-golden=""></span></p>
<p><strong>وضعیت این مرحله:</strong> <code class="inline-code" data-stv2-evidence="" dir="ltr"></code></p>
</section>
<section aria-labelledby="stv2-class-priority-prediction-title" class="stv2-prediction">
<h3 id="stv2-class-priority-prediction-title">❓ پیش‌بینی کن</h3>
<p data-stv2-prompt=""></p>
<div aria-label="گزینه‌های پیش‌بینی" class="stv2-prediction-options" data-stv2-options="" role="group"></div>
<p aria-live="polite" class="stv2-feedback" data-stv2-feedback="" role="status"></p>
</section>
<div aria-label="کنترل مراحل" class="stv2-actions">
<button class="ui-btn" data-stv2-prev="" type="button">مرحلهٔ قبل</button>
<button class="ui-btn" data-stv2-reveal="" type="button">نمایش پاسخ</button>
<button class="ui-btn" data-stv2-next="" type="button">مرحلهٔ بعد</button>
<button class="ui-btn" data-stv2-reset="" type="button">شروع دوباره</button>
</div>
<p aria-live="polite" class="stv2-status" data-stv2-status="" role="status"></p>
<p class="stv2-lab-link"><a href="#class-priority-build-test">🧪 همین مفهوم را در «بساز و امتحان کن» اجرا کن</a></p>
<section aria-label="خلاصهٔ همهٔ مراحل برای چاپ" class="stv2-print-all"><div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table"><caption>خلاصهٔ همهٔ مراحل Step‑Through v2</caption><thead><tr><th scope="col">مرحله</th><th scope="col">نتیجه</th><th scope="col">وضعیت شواهد</th><th scope="col">قانون طلایی</th></tr></thead><tbody><tr><th scope="row">1 — هر Element یک Local Class دارد</th><td>Style اختصاصی همان Element از Local Class می‌آید.</td><td>verified_by_official_elementor_help</td><td>Local Class لباس اختصاصی همین Element است.</td></tr><tr><th scope="row">2 — Local Class روی Global Class غلبه می‌کند</th><td>Global Class رنگ سبز دارد، اما Local Class همچنان Navy را اعمال می‌کند.</td><td>verified_by_official_elementor_help</td><td>برای دیدن اثر Global، property متعارض Local را پاک یا بازطراحی کن.</td></tr><tr><th scope="row">3 — دو Global Class: کلاس سمت چپ اولویت دارد</th><td>Green_text در Class Manager بالاتر است و در Classes Field سمت چپ Red_text قرار می‌گیرد.</td><td>verified_by_official_elementor_help</td><td>زمان افزودن را با priority اشتباه نگیر.</td></tr><tr><th scope="row">4 — Reorder در Class Manager، نتیجهٔ Global را تغییر می‌دهد</th><td>Red_text به اولویت بالاتر منتقل شده و در نبود Local override، نتیجه قرمز است.</td><td>verified_by_official_elementor_help</td><td>Reorder کلاس، تغییر محلی کوچک نیست؛ اثر سیستم طراحی را بررسی کن.</td></tr><tr><th scope="row">5 — State روی Class انتخاب‌شده</th><td>Hover برای Global یا Local Class انتخاب‌شده declaration متفاوت می‌سازد.</td><td>verified_by_official_elementor_help</td><td>قبل از ویرایش Hover، ببین کدام Class و State واقعاً selected است.</td></tr><tr><th scope="row">6 — Custom CSS و matched-rule context</th><td>یک rule سفارشی ممکن است با specificity، source order یا importance وارد تعارض شود.</td><td>verified_by_css_spec</td><td>برای conflict سفارشی، Matched CSS Rules و Computed Style را بخوان.</td></tr><tr><th scope="row">7 — Local-first سپس Convert to Global</th><td>Prototype در Local Class ساخته و پس از اثبات reuse به Global Class تبدیل می‌شود.</td><td>verified_by_official_elementor_help</td><td>Global Class را با evidence reuse بساز و class sprawl را audit کن.</td></tr></tbody></table></div></section>
<noscript><p class="warning-box">برای تعامل مرحله‌ای JavaScript محلی باید فعال باشد؛ خلاصهٔ چاپی همهٔ مراحل در همین بخش موجود است.</p></noscript>
<script class="stv2-config" type="application/json">{"goal":"اولویت Local Class و ترتیب Global Classها را بدون تکیه بر زمان افزودن کلاس‌ها بفهم.","id":"stv2-class-priority","lab_target":"class-priority-build-test","lesson_id":"lesson-v17-class-manager","renderer":"class-priority","schema_version":"2.0.0","states":[{"computed":[["Winning source","Local Class"],["Scope","همین Element"]],"elementor":[["Classes Field","Local Class"],["Local text color","Navy"],["Global Classes","هیچ"]],"evidence":"verified_by_official_elementor_help","explanation":"Local Class مخصوص Element انتخاب‌شده است و در hierarchy بالاترین اولویت را دارد.","golden_rule":"Local Class لباس اختصاصی همین Element است.","id":"local-only","phase":"پایه","prediction":{"correct":1,"feedback_correct":"درست است؛ Local Class بالاترین priority را دارد.","feedback_wrong":"در hierarchy رسمی Elementor، Local Class همیشه در بالاترین اولویت است.","options":["Global Class","Local Class","کلاسی که دیرتر اضافه شده"],"prompt":"اگر Global Class متعارض اضافه شود ولی Local همان property را تعیین کند، کدام برنده است؟"},"summary":"Style اختصاصی همان Element از Local Class می‌آید.","title":"هر Element یک Local Class دارد","visual":{"chips":[{"kind":"local","name":"Local","priority":1}],"result":"Navy","second":"بدون تغییر","winner":"Local"}},{"computed":[["Winning source","Local"],["Indicator meaning","Local override"]],"elementor":[["Classes","Local + Green_text"],["Local color","Navy"],["Green_text color","Green"]],"evidence":"verified_by_official_elementor_help","explanation":"وجود Global Class به‌تنهایی Local property متعارض را کنار نمی‌زند.","golden_rule":"برای دیدن اثر Global، property متعارض Local را پاک یا بازطراحی کن.","id":"local-over-global","phase":"Conflict","prediction":{"correct":0,"feedback_correct":"درست است؛ Class Manager hierarchy را تعیین می‌کند.","feedback_wrong":"Elementor priority را از Class Manager بازتاب می‌دهد، نه از زمان افزودن.","options":["Class Manager","زمان کلیک کاربر","ترتیب DOM"],"prompt":"اگر رنگ Local را پاک کنیم و دو Global Class متعارض بمانند، اولویت از کجا می‌آید؟"},"summary":"Global Class رنگ سبز دارد، اما Local Class همچنان Navy را اعمال می‌کند.","title":"Local Class روی Global Class غلبه می‌کند","visual":{"chips":[{"kind":"local","name":"Local","priority":1},{"kind":"global","name":"Green_text","priority":2}],"result":"Navy","second":"Green","winner":"Local"}},{"computed":[["Winning global","Green_text"],["Reason","Manager priority / left position"]],"elementor":[["Classes Field","Local(empty) | Green_text | Red_text"],["Class Manager order","Green_text بالاتر از Red_text"]],"evidence":"verified_by_official_elementor_help","explanation":"حتی اگر Green_text بعدتر اضافه شده باشد، Manager order می‌تواند آن را به سمت چپ و اولویت بالاتر ببرد.","golden_rule":"زمان افزودن را با priority اشتباه نگیر.","id":"global-manager-order","phase":"Hierarchy","prediction":{"correct":0,"feedback_correct":"بله؛ hierarchy Global Classها تغییر می‌کند.","feedback_wrong":"تغییر Manager order روی تعارض Global Classها اثر می‌گذارد، نه DOM یا وجود Local.","options":["Global winner می‌تواند Red_text شود","Local Class حذف می‌شود","DOM order تغییر می‌کند"],"prompt":"اگر در Class Manager، Red_text بالاتر از Green_text قرار گیرد، چه چیزی تغییر می‌کند؟"},"summary":"Green_text در Class Manager بالاتر است و در Classes Field سمت چپ Red_text قرار می‌گیرد.","title":"دو Global Class: کلاس سمت چپ اولویت دارد","visual":{"chips":[{"kind":"local-empty","name":"Local (empty)","priority":1},{"kind":"global winner","name":"Green_text","priority":2},{"kind":"global","name":"Red_text","priority":3}],"result":"Green","second":"Green","winner":"Green_text"}},{"computed":[["Winning global","Red_text"],["Local override","ندارد"]],"elementor":[["Class Manager order","Red_text بالاتر"],["Classes Field","Local(empty) | Red_text | Green_text"]],"evidence":"verified_by_official_elementor_help","explanation":"تغییر hierarchy تصمیمی سیستمی است و می‌تواند روی تمام Elementهای دارای هر دو Class اثر بگذارد.","golden_rule":"Reorder کلاس، تغییر محلی کوچک نیست؛ اثر سیستم طراحی را بررسی کن.","id":"global-reordered","phase":"علت و معلول","prediction":{"correct":0,"feedback_correct":"درست است؛ Global hierarchy می‌تواند چندین Element را تغییر دهد.","feedback_wrong":"Global Class بخشی از سیستم طراحی است و دامنهٔ آن فراتر از Element فعلی است.","options":["Elementهای دیگری که هر دو Class را دارند","فقط نام صفحهٔ فعلی","فقط breakpoint Mobile"],"prompt":"پیش از Reorder کردن Global Class در سایت واقعی، چه چیزی باید بررسی شود؟"},"summary":"Red_text به اولویت بالاتر منتقل شده و در نبود Local override، نتیجه قرمز است.","title":"Reorder در Class Manager، نتیجهٔ Global را تغییر می‌دهد","visual":{"chips":[{"kind":"local-empty","name":"Local (empty)","priority":1},{"kind":"global winner","name":"Red_text","priority":2},{"kind":"global","name":"Green_text","priority":3}],"result":"Red","second":"Red","winner":"Red_text"}},{"id":"selected-state","phase":"State","title":"State روی Class انتخاب‌شده","summary":"Hover برای Global یا Local Class انتخاب‌شده declaration متفاوت می‌سازد.","explanation":"State یک context از Class فعال است؛ برنده‌بودن آن به class target، property conflict و state match وابسته است.","golden_rule":"قبل از ویرایش Hover، ببین کدام Class و State واقعاً selected است.","evidence":"verified_by_official_elementor_help","elementor":[["Selected class","Button_primary"],["State","Hover"],["Property","background"]],"computed":[["Matched context","Button_primary:hover"],["Winner","State declaration if not overridden"]],"visual":{"chips":[{"kind":"local-empty","name":"Local (empty)","priority":1},{"kind":"global winner","name":"Button_primary:hover","priority":2},{"kind":"global","name":"Button_primary","priority":3}],"winner":"Selected State","result":"Hover Gold","second":"Normal Navy"},"prediction":{"prompt":"اگر Hover را روی Local Class ویرایش کنی، دامنهٔ آن چیست؟","options":["همهٔ Button_primaryها","همین Element در Hover","کل سایت"],"correct":1,"feedback_correct":"درست است.","feedback_wrong":"Local State به همان Element محدود است."}},{"id":"custom-css-context","phase":"Matched rule","title":"Custom CSS و matched-rule context","summary":"یک rule سفارشی ممکن است با specificity، source order یا importance وارد تعارض شود.","explanation":"Class Manager فقط hierarchy Global Classهای Elementor را توضیح می‌دهد؛ Custom CSS در cascade واقعی مرورگر و selector context ارزیابی می‌شود.","golden_rule":"برای conflict سفارشی، Matched CSS Rules و Computed Style را بخوان.","evidence":"verified_by_css_spec","elementor":[["Elementor classes","Local + Button_primary"],["Custom CSS",".page .cta { background: red; }"]],"computed":[["Need inspection","specificity + order + importance"],["Winner","context-dependent"]],"visual":{"chips":[{"kind":"local","name":"Local","priority":1},{"kind":"global","name":"Button_primary","priority":2},{"kind":"winner","name":"Matched Custom CSS","priority":"CSS"}],"winner":"Computed rule","result":"Context-dependent","second":"Inspect DevTools"},"prediction":{"prompt":"کدام ابزار پاسخ قطعی می‌دهد؟","options":["فقط زمان افزودن Class","Computed Style و Matched Rules","نام رنگ Variable"],"correct":1,"feedback_correct":"درست است.","feedback_wrong":"Custom CSS با cascade مرورگر حل می‌شود."}},{"id":"local-first-convert","phase":"Workflow","title":"Local-first سپس Convert to Global","summary":"Prototype در Local Class ساخته و پس از اثبات reuse به Global Class تبدیل می‌شود.","explanation":"این workflow رسمیِ اجباری نیست، اما خود Elementor تبدیل propertyهای Local به Global Class را مستند کرده است.","golden_rule":"Global Class را با evidence reuse بساز و class sprawl را audit کن.","evidence":"verified_by_official_elementor_help","elementor":[["Start","Local prototype"],["Evidence","۳ استفادهٔ واقعی"],["Action","Convert to Global Class"]],"computed":[["Benefit","verified reuse"],["Risk","class sprawl if premature"]],"visual":{"chips":[{"kind":"local","name":"Local prototype","priority":1},{"kind":"global winner","name":"Card_elevated","priority":2}],"winner":"Global after verification","result":"Reusable","second":"Semantic naming proposed"},"prediction":{"prompt":"چه زمانی Convert مناسب‌تر است؟","options":["پس از اثبات reuse","قبل از طراحی اولین Element","برای هر exception"],"correct":0,"feedback_correct":"درست است.","feedback_wrong":"Premature global abstraction می‌تواند class sprawl بسازد."}}],"storage_key":"elementor-v4-workbook:v30:stv2:class-priority-expanded","title":"Class Conflict Architecture — Global A/B، State، Local و Custom CSS","type":"decision_propagation","verification":[{"source_id":"ELEMENTOR_CLASSES","status":"verified_by_official_elementor_help"},{"source_id":"ELEMENTOR_CLASS_PRIORITY","status":"verified_by_official_elementor_help"}]}</script>
</section>
</details><section aria-labelledby="class-lab-title" class="lesson-section v30-core-lab" id="class-architecture-lab-v30">
<h2 id="class-lab-title">آزمایشگاه معماری Class و Conflict</h2>
<p>Global Class A و B در تعارض با ترتیب Class Manager حل می‌شوند و Class سمت چپ priority بالاتری دارد؛ Local Class بالاترین priority در hierarchy رسمی Elementor را نگه می‌دارد. State برای Class انتخاب‌شده و Custom CSS برای matched-rule context جداگانه بررسی می‌شوند.</p>
<div class="class-architecture-grid">
<section><h3>Local-first prototyping</h3><p><code dir="ltr">proposed_strategy</code>: ابتدا Local، سپس بعد از reuse واقعی Convert to Global.</p></section>
<section><h3>Class-sprawl detection</h3><p>کلاس‌های هم‌پوشان، نام‌های مبهم، utilityهای تک‌مصرف و conflictهای دائمی را audit کن.</p></section>
<section><h3>Semantic / utility naming</h3><p><code dir="ltr">proposed_strategy</code>: semantic و utility هر دو ابزارند؛ هیچ‌کدام taxonomy رسمی Elementor نیستند.</p></section>
<section><h3>Computed winner</h3><p>برای Custom CSS، inherited properties و selectorهای بیرونی، DevTools و Computed Style مرجع نهایی مرورگرند.</p></section>
</div>
</section>
</article>
