<article class="lesson card-surface" data-lesson="3" id="lesson-3">

<h2 class="lesson-title former-h1">درس 3 — Local Class، Global Class و کلاس هدف ویرایش</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-3-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-3-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> بعد از تشخیص Context و ساخت Tree، محدودهٔ Style را تشخیص بدهی: کدام Style فقط برای همین Element است، کدام Style باید بین چند Element مشترک شود، و دقیقاً کدام Class را ویرایش می‌کنی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> کل CSS Specificity، Class Manager کامل، ساخت Design System کامل، Componentها یا Variables پیشرفته.</p>
<p><strong>در پایان باید بتوانی:</strong> قبل از تغییر ظاهر، Classهای فعال یک Element را بررسی کنی، تفاوت Local و Global را توضیح بدهی، و تصمیم بگیری تغییر باید Local بماند یا به Global Class تبدیل شود.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-3-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-3-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی محدود + 🔍 عیب‌یابی</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰–۳۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۴۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۵ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> Class System یکی از هسته‌های V4 است، اما نباید در همان برخورد اول به ساخت ده‌ها Global Class تبدیل شود. تمرین باید از تشخیص کلاس هدف و محدودهٔ اثر شروع شود.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_class_scope_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-3-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-3-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس ۱ گفتیم هر تغییر در Context انجام می‌شود. در درس ۲ گفتیم Context بدون Tree قابل کنترل نیست. حالا درس ۳ می‌گوید: حتی اگر Tree درست باشد، اگر Class هدف ویرایش را اشتباه انتخاب کنی، Style در جای اشتباه اثر می‌گذارد.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Lesson 1: Context را تشخیص بده
↓
Lesson 2: Structure / Element Tree را بساز
↓
Lesson 3: Class Scope و کلاس هدف ویرایش را کنترل کن</code></pre>
</figure>

<h3>مسئله</h3>
<p>ممکن است رنگ یک Heading را تغییر بدهی و چند Heading دیگر هم تغییر کنند. یا یک Class را تغییر بدهی و روی Element موردنظر هیچ اثری نبینی. در هر دو حالت، مشکل معمولاً این است که نمی‌دانی Style روی کدام Class اعمال شده و آن Class روی کدام Elementها اثر دارد.</p>

<h3>تعریف ساده</h3>
<section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای Local Class، Global Class و کلاس هدف ویرایش">
<h4>راهنمای مبتدی برای Local Class، Global Class و کلاس هدف ویرایش</h4>
<p>Class فقط یک اسم تزئینی نیست؛ Class تصمیمی دربارهٔ محدودهٔ اثر Style است.</p>

<div class="concept-card-grid">
<article class="concept-card" data-concept="Local Class">
<h4><span class="term-en" dir="ltr">Local Class</span> — کلاس محلی</h4>
<ol class="concept-steps">
<li><strong>ساده‌ترین معنی:</strong> Style مخصوص همین Element یا همین موقعیت.</li>
<li><strong>مثال روزمره:</strong> مثل یادداشت چسبان روی همین یک کارت.</li>
<li><strong>در Elementor:</strong> هر Element حداقل یک Local Class دارد.</li>
<li><strong>اشتباه رایج:</strong> برای هر تفاوت کوچک یک Global Class می‌سازم.</li>
<li><strong>تصمیم درست:</strong> اگر فقط همین یک Element فرق دارد، Local نگه دار.</li>
</ol>
</article>

<article class="concept-card" data-concept="Global Class">
<h4><span class="term-en" dir="ltr">Global Class</span> — کلاس قابل‌استفادهٔ مجدد</h4>
<ol class="concept-steps">
<li><strong>ساده‌ترین معنی:</strong> یک بستهٔ Style که چند Element واقعاً مشترک دارند.</li>
<li><strong>مثال روزمره:</strong> مثل یونیفرم تیم؛ روی چند نفر تکرار می‌شود.</li>
<li><strong>در Elementor:</strong> Class مشترک برای استفادهٔ دوباره در بخش‌های مشابه.</li>
<li><strong>اشتباه رایج:</strong> چیزی را Global می‌کنم فقط چون اسمش قشنگ است، نه چون تکرار واقعی دارد.</li>
<li><strong>تصمیم درست:</strong> وقتی تکرار و نیاز به نگهداری مشترک وجود دارد، Global کن.</li>
</ol>
</article>

<article class="concept-card" data-concept="کلاس هدف ویرایش">
<h4><span class="term-en" dir="ltr">Editing Target</span> — کلاس هدف ویرایش</h4>
<ol class="concept-steps">
<li><strong>ساده‌ترین معنی:</strong> Classی که الان تغییرهای Style روی آن ثبت می‌شود.</li>
<li><strong>مثال روزمره:</strong> مثل لباسی که الان قیچی دستت روی آن است، نه همهٔ لباس‌های داخل کمد.</li>
<li><strong>در Elementor:</strong> در فیلد Classes باید ببینی کدام Class فعال/در حال ویرایش است.</li>
<li><strong>اشتباه رایج:</strong> فکر می‌کنم هر Class موجود در سیستم روی همین Element فعال است.</li>
<li><strong>تصمیم درست:</strong> فقط Classهای وصل‌شده به همین Element و Class هدف ویرایش را بررسی کن.</li>
</ol>
</article>
</div>
</section>

<h3>مدل ذهنی: Class تزئین می‌کند، ساختار نمی‌سازد</h3>
<p>Class روی Element موجود سوار می‌شود. Class خودش Element جدید نمی‌سازد. این مرز را از همین ابتدا حفظ کن:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="تفاوت جنس مفاهیم">
<table class="data-table educational-table edu-table">
<caption>تفاوت جنس Class با Variable و Component</caption>
<thead><tr><th scope="col">مفهوم</th><th scope="col">جنس</th><th scope="col">فعل درست</th><th scope="col">در این درس</th></tr></thead>
<tbody>
<tr><th scope="row">Variable</th><td>مقدار نام‌دار</td><td>تعریف و ارجاع</td><td>فقط اشاره می‌شود؛ درس مستقل دارد.</td></tr>
<tr><th scope="row">Class</th><td>قانون Style روی Element موجود</td><td>اعمال / ویرایش</td><td>موضوع اصلی درس.</td></tr>
<tr><th scope="row">Component</th><td>ساختار تکرارشونده</td><td>قرار دادن / استفادهٔ دوباره</td><td>فعلاً نساز؛ فقط مرز ذهنی را بدان.</td></tr>
</tbody>
</table>
</div>
<p>قانون کوتاه: <strong>Classها تزئین می‌کنند؛ Componentها ساختار را تکرار می‌کنند؛ Variableها مقدار نگه می‌دارند.</strong></p>

<h3>اولین بررسی هنگام Conflict</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<p>اگر Style آن‌طور که انتظار داری عمل نکرد، این ترتیب را رعایت کن:</p>
<ol>
<li>Element درست انتخاب شده؟</li>
<li>Class هدف ویرایش درست است؟</li>
<li>Local override وجود دارد؟</li>
<li>State درست است؟ Normal، Hover یا Focus؟</li>
<li>Device درست است؟ Desktop، Tablet یا Mobile؟</li>
<li>Classهای دیگر همین Element با این Style تعارض دارند؟</li>
</ol>
</section>

<h3>Class چه زمانی Global می‌شود؟</h3>
<p>هر Style زیبا نباید Global شود. Global Class وقتی ارزش دارد که چند شرط داشته باشی:</p>
<ul>
<li>الگو واقعاً تکرار می‌شود.</li>
<li>تغییر آینده باید روی چند Element هم‌زمان اعمال شود.</li>
<li>Style به یک نقش طراحی تعلق دارد، نه به یک وضعیت تصادفی.</li>
<li>اسم Class معنی‌دار و پایدار است.</li>
<li>با Local overrideهای زیاد خنثی نمی‌شود.</li>
</ul>

<h3>نام‌گذاری Class: اسم از نقش بیاید، نه از ظاهر لحظه‌ای</h3>
<p>اسم خوب به نقش اشاره می‌کند، نه فقط رنگ فعلی:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="نمونه نام‌گذاری کلاس">
<table class="data-table educational-table edu-table">
<caption>نمونه‌های نام‌گذاری</caption>
<thead><tr><th scope="col">ضعیف</th><th scope="col">بهتر</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><td><code dir="ltr">blue-button</code></td><td><code dir="ltr">button-primary</code></td><td>اگر رنگ برند عوض شود، اسم هنوز معتبر است.</td></tr>
<tr><td><code dir="ltr">big-title</code></td><td><code dir="ltr">hero-heading</code></td><td>نقش در صفحه روشن‌تر است.</td></tr>
<tr><td><code dir="ltr">shadow-card</code></td><td><code dir="ltr">feature-card</code></td><td>کارت ممکن است بعداً Shadow متفاوت بگیرد.</td></tr>
</tbody>
</table>
</div>

<h3>چیزی که فعلاً لازم نیست</h3>
<p>در این درس لازم نیست Class Manager کامل، اولویت‌های پیچیده یا Design System کامل را یاد بگیری. فقط باید هر بار قبل از تغییر Style بپرسی: <strong>دارم کدام Class را ویرایش می‌کنم و این Class روی چند Element اثر دارد؟</strong></p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-3.0.0" id="lesson-3-concept-reference">
<summary>📚 مرجع مفهومی کامل — Local Class، Global Class و هدف واقعی ویرایش</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="3" data-source-version="tuya-revised-3.0.0">

<p class="concept-reference-lead">این مرجع بخش مفهومی را حفظ می‌کند و آن را به تمرین واقعی وصل می‌کند. هدف، ساختن Classهای زیاد نیست؛ هدف، تشخیص Scope و جلوگیری از تغییرهای ناخواسته است.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-3-ref-problem">
<h3 id="lesson-3-ref-problem">۱. مسئله‌ای که Class System حل می‌کند</h3>
<p>در سایت واقعی، ده‌ها Button، Heading و Card داری. اگر هرکدام جداگانه Style شوند، تغییر برند یا اصلاح طراحی سخت می‌شود. Classها کمک می‌کنند Styleهای مشترک را قابل‌ردیابی و قابل‌استفادهٔ دوباره کنی.</p>
<p>اما Class System اگر بی‌قاعده استفاده شود، خودش منبع خطا می‌شود: Style در چند جای ناخواسته تغییر می‌کند، Local و Global با هم قاطی می‌شوند، و هنرجو نمی‌داند تغییر واقعاً روی کدام Class ثبت شده است.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-3-clothes-analogy">
<h3 id="lesson-3-clothes-analogy">۲. تشبیه لباس</h3>
<ul>
<li><strong>Element:</strong> آدمی است که لباس می‌پوشد.</li>
<li><strong>Local Class:</strong> لباس مخصوص همان آدم است.</li>
<li><strong>Global Class:</strong> یونیفرم یک گروه است.</li>
<li><strong>Editing Target:</strong> لباسی است که همین لحظه داری تغییرش می‌دهی.</li>
<li><strong>State:</strong> حالت موقت همان لباس است؛ مثلاً وقتی موس روی دکمه می‌رود.</li>
</ul>
<p>اگر یونیفرم تیم را تغییر بدهی، همهٔ اعضای تیم تغییر می‌کنند. اگر فقط لباس یک نفر را تغییر بدهی، نباید بقیه تغییر کنند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-3-class-hierarchy">
<h3 id="lesson-3-class-hierarchy">۳. Hierarchy و Conflict را ساده بفهم</h3>
<p>ممکن است یک Element چند Class داشته باشد. اگر دو Class برای یک Property مقدار متفاوت بدهند، باید مشخص شود کدام یکی اولویت دارد. در Elementor V4، Class Manager برای مدیریت و اولویت‌بندی Classها مطرح شده و Local Class در مستند رسمی به‌عنوان بالاترین اولویت معرفی می‌شود.</p>
<p>برای هنرجو در این مرحله، قانون عملی کافی است:</p>
<blockquote><p>اگر نتیجهٔ Style عجیب است، قبل از تغییر دوباره، Classهای فعال و Class هدف ویرایش را ببین.</p></blockquote>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-3-local-global-decision">
<h3 id="lesson-3-local-global-decision">۴. Decision Tree: Local بماند یا Global شود؟</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">آیا این Style فقط برای همین Element است؟
├── بله → Local Class
└── خیر
    آیا چند Element واقعاً همین الگو را دارند؟
    ├── بله → Global Class candidate
    └── خیر → هنوز Local یا provisional نگه دار

آیا نام Class به نقش پایدار اشاره می‌کند؟
├── بله → قابل بررسی برای Global
└── خیر → نام‌گذاری را اصلاح کن

آیا بعداً قرار است همهٔ استفاده‌ها با هم تغییر کنند؟
├── بله → Global Class قوی‌تر است
└── خیر → Local یا Class محدودتر</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-3-tuya-candidates">
<h3 id="lesson-3-tuya-candidates">۵. Class Candidateهای TUYA در این مرحله</h3>
<p>در این درس هنوز Global Class نهایی نمی‌سازیم. فقط Candidateها را دسته‌بندی می‌کنیم:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Class candidates">
<table class="data-table educational-table edu-table">
<caption>کاندیداهای Class در TUYA</caption>
<thead><tr><th scope="col">نام پیشنهادی</th><th scope="col">نوع فعلی</th><th scope="col">دلیل</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">tuya-shell</code></th><td>Local یا Global محدود پروژه</td><td>پوستهٔ اصلی همین سکشن است.</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row"><code dir="ltr">tuya-copy</code></th><td>Local</td><td>ظرف محتوای همین سکشن.</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row"><code dir="ltr">button-primary</code></th><td>Global candidate</td><td>اگر دکمهٔ اصلی در چند بخش تکرار شود.</td><td><code dir="ltr">unknown_until_reuse</code></td></tr>
<tr><th scope="row"><code dir="ltr">orbit-node</code></th><td>Global یا Component-related candidate</td><td>اگر Nodeها ساختار و Style تکراری دارند.</td><td><code dir="ltr">provisional_for_later</code></td></tr>
</tbody>
</table>
</div>
<p>نکته: اگر فقط یک‌بار از چیزی استفاده می‌کنی، Global کردن آن ممکن است بدهی طراحی بسازد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-3-source-of-truth">
<h3 id="lesson-3-source-of-truth">۶. Source of Truth برای Style</h3>
<p>برای هر Style باید بدانی منبع حقیقت کجاست:</p>
<ul>
<li>اگر مقدار فقط یک‌بار مصرف است → Local Class.</li>
<li>اگر الگو چندبار تکرار می‌شود → Global Class.</li>
<li>اگر مقدار باید در همه‌جا یکسان بماند → Variable.</li>
<li>اگر ساختار چندعنصری تکرار می‌شود → Component، نه فقط Class.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-3-golden">
<h3 id="lesson-3-golden">۷. قوانین طلایی</h3>
<ul>
<li><strong>قبل از تغییر Style، Class هدف ویرایش را ببین.</strong></li>
<li><strong>Local برای تفاوت واقعی یک Element است.</strong></li>
<li><strong>Global برای الگوی تکرارشونده است، نه برای هر ایدهٔ قشنگ.</strong></li>
<li><strong>Class ساختار نمی‌سازد؛ روی ساختار موجود Style اعمال می‌کند.</strong></li>
<li><strong>اگر Global Class را با چند Local override خنثی می‌کنی، احتمالاً Class را بد طراحی کرده‌ای.</strong></li>
<li><strong>State و Device را همیشه در کنار Class بررسی کن.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>این درس بر پایهٔ مستند رسمی Elementor دربارهٔ کلاس‌ها و تفاوت V3/V4 بازنویسی شده است. تشبیه‌ها و Class Candidateهای TUYA توضیح آموزشی‌اند و تا زمان مشاهدهٔ UI واقعی و تکرار واقعی، نباید به‌عنوان تصمیم قطعی Design System معرفی شوند.</p>
<ul>
<li><a href="https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/" rel="noopener noreferrer" target="_blank">Elementor — Differences between Editor V3 and V4</a></li>
<li><a href="https://elementor.com/help/classes-in-elementor-2/" rel="noopener noreferrer" target="_blank">Elementor — Classes in Elementor</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-3-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-3-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Class نام است، نه واحد اندازه‌گیری</span>
</summary>
<section aria-labelledby="lesson-3-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Class خودش عدد، رنگ یا واحد نیست. Class یک نام است که مجموعه‌ای از Styleها را به Element وصل می‌کند. داخل Class ممکن است مقدارهایی مثل px، rem، % یا رنگ تعریف شود، اما خود Class واحد ندارد.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> Class مثل برچسب روی جعبه است؛ برچسب خودش محتوا نیست، اما به جعبه‌ای از تنظیمات اشاره می‌کند.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع</th><th scope="col">واحد</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Class Name</th><td>Identifier / نام</td><td>بدون واحد</td><td>اسم ظاهری مثل blue-button ممکن است بعداً غلط شود.</td></tr>
<tr><th scope="row">Class Priority</th><td>Hierarchy / اولویت</td><td>بدون واحد</td><td>حل Conflict را با تغییر تصادفی مقدار اشتباه نگیر.</td></tr>
<tr><th scope="row">Style Property inside class</th><td>Property-specific</td><td>بسته به Property</td><td>ممکن است عدد داخل Class باشد، اما Class خودش عدد نیست.</td></tr>
<tr><th scope="row">State</th><td>وضعیت تعاملی</td><td>بدون واحد</td><td>Hover را تغییر می‌دهی ولی Normal را نگاه می‌کنی.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>not_applicable — این درس دربارهٔ Scope و Class target است، نه محاسبهٔ اندازه.</p></section>
<section><h3>📱 در Responsive</h3><p>Class ممکن است در Breakpointهای مختلف مقدارهای متفاوتی داشته باشد. پس همیشه Device را همراه Class هدف بررسی کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>DevTools می‌تواند نشان دهد چه Selectorی مقدار نهایی را می‌دهد، اما در Elementor باید اول Class هدف ویرایش را در UI بشناسی.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-3-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-3-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Class Audit، نه ساخت Design System کامل</h3>
<p>در درس ۲ فقط Tree حداقلی را ساختی. در درس ۳، فقط Class Scope را بررسی می‌کنی. هنوز Style نهایی، مقدارهای عددی، Nodeها و Shadowها را نهایی نمی‌کنی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate درس ۳">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از کار با Class</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>V4 کلاس‌محورتر از V3 است و هر Element حداقل یک Local Class دارد.</td><td>قبل از Style باید Class هدف ویرایش را ببینی.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Copy و Visual در Tree جدا شده‌اند.</td><td>Classها باید با همین Structure همخوان باشند.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>نام‌های پیشنهادی مثل <code dir="ltr">tuya-shell</code> یا <code dir="ltr">button-primary</code>.</td><td>فعلاً Candidate هستند، نه تصمیم نهایی.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>اینکه در پروژهٔ واقعی چند دکمه/کارت/Node تکرار خواهد شد.</td><td>بدون تکرار واقعی، Global Class نساز.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Classهای فعال را ببین</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس سه">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> تشخیص Class target، نه ساخت Classهای جدید.</p>
<p><strong>مسیر:</strong> Elementor Editor → انتخاب یک Element از Tree → Style tab → فیلد Classes.</p>
<p><strong>Element هدف:</strong> یکی از Elementهای ساخته‌شده در درس ۲، مثلاً TUYA Shell یا TUYA Copy.</p>
<p><strong>Class فعال:</strong> فقط نام Classهای موجود را بخوان و بنویس.</p>
<p><strong>Property:</strong> هنوز هیچ Property تغییر نکند.</p>
<p><strong>نباید تغییر کند:</strong> Width، Height، Position، Shadow، Background، Class جدید، Global Class جدید.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Classهای فعال Element را دیدم و هنوز چیزی را تغییر نداده‌ام.»</p>
</aside>

<h3>مرحلهٔ ۲ — Class Candidateها را روی کاغذ دسته‌بندی کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Class inventory">
<table class="data-table educational-table edu-table">
<caption>دفترچهٔ Class Candidate برای TUYA</caption>
<thead><tr><th scope="col">بخش</th><th scope="col">کاندیدای Local</th><th scope="col">کاندیدای Global</th><th scope="col">چرا هنوز قطعی نیست؟</th></tr></thead>
<tbody>
<tr><th scope="row">TUYA Shell</th><td><code dir="ltr">tuya-shell</code></td><td>نه فعلاً</td><td>ممکن است فقط همین سکشن باشد.</td></tr>
<tr><th scope="row">Primary Button</th><td>اگر فقط همین‌جاست</td><td><code dir="ltr">button-primary</code></td><td>باید ببینی در چند بخش تکرار می‌شود یا نه.</td></tr>
<tr><th scope="row">Feature item</th><td>اگر فقط یک لیست خاص است</td><td><code dir="ltr">feature-item</code></td><td>اگر الگوی کارت/آیتم در جای دیگر تکرار شود.</td></tr>
<tr><th scope="row">Orbit Node</th><td>فعلاً Local/Provisional</td><td>بعداً شاید</td><td>ممکن است به Component یا ساختار تکراری نیاز داشته باشد.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — یک تغییر محدود و قابل Undo</h3>
<p>فقط بعد از اینکه Class هدف را دیدی، یک تغییر کوچک انجام بده:</p>
<ul>
<li>یک Element آزمایشی انتخاب کن.</li>
<li>Class هدف ویرایش را بنویس.</li>
<li>فقط یک Property کم‌خطر را تغییر بده؛ مثلاً یک Border موقت یا رنگ متن موقت.</li>
<li>نتیجه را ببین.</li>
<li>Undo کن.</li>
</ul>
<aside class="warning-card" aria-label="احتیاط">
<p><strong>احتیاط:</strong> اگر Class هدف Global است، ممکن است چند Element هم‌زمان تغییر کنند. قبل از تغییر، انتظار اثر را بنویس.</p>
</aside>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر یک Button فقط در همین سکشن با بقیه فرق دارد، تصمیم اولیه چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-3">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-3-a" name="stop-question-3" type="radio" value="A"/><span>A) فوراً Global Class جدید بسازم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-3-b" name="stop-question-3" type="radio" value="B"/><span>B) فعلاً Local نگه دارم یا Candidate ثبت کنم.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-3-c" name="stop-question-3" type="radio" value="C"/><span>C) Component بسازم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> اگر فقط همین Button فرق دارد، Global Class زودهنگام است. Component هم برای تکرار ساختار است، نه فقط یک تفاوت ظاهری کوچک.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> هر چیزی که اسم خوبی دارد را Global Class کنی.</p>
<p><strong>نشانه:</strong> بعداً برای هر نمونه مجبور می‌شوی چند Local override اضافه کنی.</p>
<p><strong>قاعده:</strong> اگر Global Class با overrideهای زیاد زندگی می‌کند، احتمالاً نقش آن درست تعریف نشده است.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>تصور کن برای TUYA این Classها را ساخته‌ای:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Classهای خراب‌شده</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">blue-big-button
shadow-on-left-card
node-42px
nice-title
temporary-box</code></pre>
</figure>
<p>حالا بپرس: اگر رنگ برند عوض شود، اگر Nodeها جابه‌جا شوند، یا اگر این Style در جای دیگر تکرار نشود، این اسم‌ها هنوز معنی دارند؟</p>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-13">
<fieldset>
<legend>Checkpoint درس ۳</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-13-1" name="chk-13-1" type="checkbox"/><span>قبل از تغییر Style، Class هدف ویرایش را دیده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-13-2" name="chk-13-2" type="checkbox"/><span>می‌دانم Local برای تفاوت یک Element است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-13-3" name="chk-13-3" type="checkbox"/><span>می‌دانم Global فقط برای الگوی تکرارشونده و قابل نگهداری است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-13-4" name="chk-13-4" type="checkbox"/><span>هنوز برای TUYA Design System کامل نساخته‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Local Class و Global Class را با مثال Button توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر سه کارت Feature داری و فقط کارت دوم Shadow متفاوت دارد، چه چیزی Global می‌شود و چه چیزی Local می‌ماند؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Style مشترک کارت‌ها Global candidate است، اما تفاوت فقط کارت دوم Local می‌ماند؛ مگر اینکه آن تفاوت خودش الگوی تکرارشونده باشد.</p>
</details>

</section>
</details>

<details aria-labelledby="lesson-3-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-3-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Conflict بدون عجله در اصلاح</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: یک Heading باید رنگ برند بگیرد، اما رنگ دیگری نمایش داده می‌شود.</p>
<p>قبل از تغییر مقدار جدید، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>Element انتخاب‌شده چیست؟</li>
<li>Classهای فعال کدام‌اند؟</li>
<li>Class هدف ویرایش کدام است؟</li>
<li>آیا Local Class مقدار متفاوتی دارد؟</li>
<li>آیا در State یا Device اشتباه هستی؟</li>
<li>در DevTools کدام Selector مقدار نهایی را می‌دهد؟</li>
</ul>
</section>
<p>نتیجهٔ درست: اول تشخیص بده، بعد فقط یک تغییر محدود انجام بده.</p>

<h3>🔬 پشت صحنه</h3>
<p>در CSS نهایی، Classها به Selector تبدیل می‌شوند. اما در این جزوه تمرکز بر UI و مدل ذهنی Elementor است. DevTools برای اثبات نهایی مفید است، ولی جای تشخیص Class هدف در خود Editor را نمی‌گیرد.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-3-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-3-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-16">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-16-1" name="chk-16-1" type="checkbox"/><span>می‌توانم Local Class، Global Class و Class هدف ویرایش را از هم جدا کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-16-2" name="chk-16-2" type="checkbox"/><span>می‌دانم Class روی Element موجود Style اعمال می‌کند و ساختار نمی‌سازد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-16-3" name="chk-16-3" type="checkbox"/><span>می‌دانم چرا Global Class زودهنگام می‌تواند بدهی طراحی بسازد.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-17">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-17-1" name="chk-17-1" type="checkbox"/><span>در Editor یک Element را انتخاب می‌کنم و Classهای فعال و Class هدف را ثبت می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-17-2" name="chk-17-2" type="checkbox"/><span>قبل از ساخت Global Class، تکرار واقعی و نقش پایدار آن را بررسی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-17-3" name="chk-17-3" type="checkbox"/><span>یک تغییر کوچک و قابل Undo روی Class هدف انجام می‌دهم و نتیجه را مشاهده می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-18">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-18-1" name="chk-18-1" type="checkbox"/><span>در سناریوی سه Feature Card می‌توانم تشخیص بدهم کدام Style مشترک Global candidate است و کدام تفاوت Local می‌ماند.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-3-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-3-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، روی همین Tree و Class Scope شروع می‌کنیم به بررسی Layout/Flow/Display. هنوز نوبت Style نهایی، Shadow نهایی و مختصات قطعی Nodeها نیست.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 3</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-3-completion">
<fieldset>
<legend>ثبت پایان درس 3</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-3-complete" name="lesson-3-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
