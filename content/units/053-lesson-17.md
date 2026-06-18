<article class="lesson card-surface" data-lesson="17" id="lesson-17"><h2 class="lesson-title former-h1">درس 17 — Classes، Variables و Components در Design System V4</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-17-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-17-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> مرز میان Class، Variable و Component را تشخیص بدهی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Design System سازمانی کامل را.</p><p><strong>در پایان باید بتوانی:</strong> الگوهای تکراری TUYA را بدون Class Explosion سازمان بدهی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-17-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-17-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🧩 سیستم طراحی + 🛠 اجرایی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۳۵–۵۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> نوع تکرار، ابزار مناسب را تعیین می‌کند.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-17-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-17-lesson-understand-4">A. بفهم</h2><h3>Decision Tree</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="rtl">◇ فقط یک مقدار مشترک است؟
   ├─ بله → □ Variable، اگر نوع آن پشتیبانی شود
   └─ خیر
       ◇ مجموعه‌ای از Styleها تکرار می‌شود؟
          ├─ بله → □ Global Class
          └─ خیر
              ◇ Structure + Style + رفتار تکرار می‌شود؟
                 ├─ بله → □ Component
                 └─ خیر → Local adjustment</pre></figure></details><h3>مدل ذهنی</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای Variable، Class و Component">
<h4>راهنمای مبتدی برای Variable، Class و Component</h4>
<p>همهٔ چیزهای تکراری یکسان نیستند؛ گاهی فقط یک مقدار تکرار شده، گاهی یک سبک، گاهی یک ساختار کامل.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="Variable">
<h4><span class="term-en" dir="ltr">Variable</span> — یک مقدار مشترک</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Variable فقط یک مقدار است؛ مثل رنگ، فاصله یا شعاع.</li>
<li><strong>۲. مثال روزمره:</strong> مثل شمارهٔ رنگی که همه‌جا استفاده می‌کنی.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> رنگ طلایی، فاصلهٔ ثابت، Radius کارت‌ها.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Design System Variables در Elementor.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> برای یک کارت کامل Variable می‌سازم.</li>
<li><strong>۶. تصمیم درست:</strong> Variable برای مقدار است، نه ساختار.</li>
<li><strong>۷. تمرین کوچک:</strong> یک رنگ تکراری پیدا کن و نام Variable پیشنهادی بده.</li>
</ol>
</article>
<article class="concept-card" data-concept="Class">
<h4><span class="term-en" dir="ltr">Class</span> — یک بستهٔ Style</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Class چند Style را برای چند عنصر نگه می‌دارد.</li>
<li><strong>۲. مثال روزمره:</strong> مثل لباس فرم برای چند کارت.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Button یا Cardهایی که ظاهر مشابه دارند.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Global Class.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> برای هر مقدار کوچک Class جدید می‌سازم.</li>
<li><strong>۶. تصمیم درست:</strong> وقتی چند Style با هم تکرار شدند Class بساز.</li>
<li><strong>۷. تمرین کوچک:</strong> یک Style بسته‌ای پیدا کن که روی چند Element می‌آید.</li>
</ol>
</article>
<article class="concept-card" data-concept="Component">
<h4><span class="term-en" dir="ltr">Component</span> — ساختار تکرارشونده</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Component مجموعه‌ای از Structure، Content placeholder و Style است.</li>
<li><strong>۲. مثال روزمره:</strong> مثل قالب آمادهٔ یک کارت محصول.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> کارت یا بخش تکراری با چند Child.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Component/Template/Pattern بسته به ابزار.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> هر تفاوت کوچک را Component جدا می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> وقتی ساختار کامل تکرار می‌شود به Component فکر کن.</li>
<li><strong>۷. تمرین کوچک:</strong> یک بخش تکراری را بشکن: چه Childهایی دارد؟</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">Variable</dt><dd>یک مقدار قابل استفادهٔ مجدد</dd>
<dt dir="ltr">Class</dt><dd>بسته‌ای از Styleهای قابل تکرار</dd>
<dt dir="ltr">Component</dt><dd>ساختار کامل قابل تکرار</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">قبل از Reuse بپرس: «فقط مقدار تکرار شده، یا Style، یا کل ساختار؟»</p>
</aside>
</section><section aria-labelledby="section-hidden-247-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-247-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Variable</dt><dd>یک مقدار</dd><dt>Class</dt><dd>یک بستهٔ Style</dd><dt>Component</dt><dd>یک ساختار قابل استفادهٔ مجدد</dd></dl></section><p>همهٔ تکرارها Component نمی‌خواهند؛ همهٔ تفاوت‌ها نیز Local Class جدید نمی‌خواهند.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="022f2848417605ebd1dcd6274e87fd0c1b6bcf23eee51b7c0dfdef84865f9893" id="lesson-17-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Design System؛ رابطهٔ Variable، Class و Component</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="17" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-17-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-17-section-01">مسئله‌ای که Design System حل می‌کند</h3><p>بدون سیستم، سایت پر از تصمیم‌های مشابه اما ناهماهنگ می‌شود:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">سبز #004526
سبز #004627
سبز #014526
Padding 30px
Padding 32px
Padding 34px
</code></pre></figure><p>هر مقدار به‌تنهایی ممکن است «تقریباً درست» باشد، اما کل سایت به‌مرور زبان مشترک خود را از دست می‌دهد.</p><p>Design System فقط مجموعه رنگ‌ها نیست؛ <strong>نقشهٔ تصمیم‌های قابل استفاده مجدد</strong> است.</p><hr/></section><section aria-labelledby="concept-v31-17-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-17-section-02">تشبیه به دنیای واقعی: آشپزخانهٔ زنجیره‌ای</h3><p>یک رستوران زنجیره‌ای را تصور کن:</p><ul>
<li>Ingredient Standard = Variable؛ مثلاً سس اصلی یا وزن نمک</li>
<li>Recipe = Global Class؛ ترکیب مواد و روش ارائه</li>
<li>Dish Template = Component؛ ساختار کامل غذا</li>
<li>Local Adjustment = Local Class؛ استثنای همان بشقاب</li>
</ul><p>اگر قیمت نمک عوض شود، Recipe را از نو نمی‌نویسی. اگر شکل کامل غذا تکرار می‌شود، فقط رنگ بشقاب را کپی نمی‌کنی؛ Template لازم است.</p><hr/></section><section aria-labelledby="concept-v31-17-section-03" class="concept-reference-part"><h3 id="concept-v31-17-section-03">سه سؤال اصلی</h3><h4>آیا فقط یک مقدار مشترک است؟</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">#004526
1.5rem
8px
</code></pre></figure><p>→ Variable</p><h4>آیا یک بسته Style روی Elementهای مختلف تکرار می‌شود؟</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Typography + Color + Padding + Border
</code></pre></figure><p>→ Global Class</p><h4>آیا یک ساختار چندElementی با رابطه و رفتار مشترک تکرار می‌شود؟</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Card
├── Image
├── Title
├── Price
└── Button
</code></pre></figure><p>→ Component</p><p>تعداد تکرار علامت است، نه قانون. ممکن است یک Brand Color از همان روز اول Variable باشد، حتی اگر هنوز فقط دو مصرف دارد.</p><hr/></section><section aria-labelledby="concept-v31-17-section-04" class="concept-reference-part"><h3 id="concept-v31-17-section-04">Token Tiering؛ از ماده خام تا نقش</h3><p>در Design Systemهای مدرن می‌توان سه سطح مفهومی دید:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Primitive Token
purple-500 = #6D5DFB
        ↓
Semantic Token
brand-primary = purple-500
        ↓
Component Token
button-background = brand-primary
</code></pre></figure><h4>Primitive</h4><p>مقدار خام را نام‌گذاری می‌کند.</p><h4>Semantic</h4><p>نقش مقدار را توضیح می‌دهد.</p><h4>Component Token</h4><p>مصرف آن در Component خاص را بیان می‌کند.</p><p>این مدل از نظر معماری بسیار مفید است، اما نباید بدون شواهد ادعا کرد Elementor فعلی زنجیره Variable-to-Variable چندسطحی را Native پشتیبانی می‌کند. در پیاده‌سازی مطمئن می‌توان زنجیره را چنین ساخت:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Variable معنایی
↓
Global Class Property
↓
Component Style
</code></pre></figure><p>پشتیبانی Alias Chain باید با Export واقعی نسخه هدف تأیید شود.</p><hr/></section><section aria-labelledby="concept-v31-17-section-05" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-17-section-05">چرا نام معنایی بهتر است؟</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">green-900
</code></pre></figure><p>رنگ را توصیف می‌کند.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">surface-brand
</code></pre></figure><p>نقش را توصیف می‌کند.</p><p>اگر برند از سبز به آبی تغییر کند، نام <code class="inline-code" dir="ltr">green-900</code> در صدها مصرف دروغ می‌شود، اما <code class="inline-code" dir="ltr">surface-brand</code> هنوز درست است.</p><p>Primitive و Semantic هر دو می‌توانند مفید باشند؛ مهم این است که نقش هر Tier روشن باشد.</p><hr/></section><section aria-labelledby="concept-v31-17-section-06" class="concept-reference-part"><h3 id="concept-v31-17-section-06">Base + Variant</h3><p>یک الگوی معماری مفید:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">card-base
card-featured
card-dark
</code></pre></figure><ul>
<li>Base مسئول Style مشترک است.</li>
<li>Variant فقط تفاوت معنادار را اضافه می‌کند.</li>
</ul><p>اما «Variant» یک مفهوم معماری است، نه الزاماً Entity رسمی جدا در Elementor. باید با Global Class و رفتار واقعی Component نسخه هدف آزمایش شود.</p><p>قانون ساده:</p><blockquote>
<p>Component برای ساختار تکراری، Class برای ظاهر تکراری و Variable برای مقدار تکراری است.</p>
</blockquote><p>این قانون راهنماست، نه دیوار آهنی. Component Style پایه نیز دارد و Global Class ممکن است بخشی از معماری Component باشد.</p><hr/></section><section aria-labelledby="concept-v31-17-section-07" class="concept-reference-part"><h3 id="concept-v31-17-section-07">Utility Class در کنار Design System</h3><p>Utilityها ابزارهای کوچک‌اند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">u-flex-center
u-text-center
u-full-width
u-space-block-lg
</code></pre></figure><p>آن‌ها نباید جای Component و Semantic Class را بگیرند. اگر یک Card از ده Utility نامفهوم تشکیل شود، درک قصد طراحی سخت می‌شود.</p><p>تعادل:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Semantic Class برای هویت
Utility Class برای تغییر کوچک و روشن
Variable برای مقدار مرکزی
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-17-section-08" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-17-section-08">در Elementor V4</h3><p>Design System Panel و Class/Variables Manager محل مدیریت مرکزی‌اند. برای هر تصمیم بپرس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">آیا این مقدار باید هم‌زمان در کل سایت تغییر کند؟
آیا این Style روی نوع‌های مختلف Element تکرار می‌شود؟
آیا این ساختار باید از یک Master پیروی کند؟
آیا این فقط استثنای یک Element است؟
</code></pre></figure><p>همچنین V3 Global Colors/Fonts و V4 Variables می‌توانند در فرایند Hybrid نیازمند Sync باشند. Sync را با یکسان‌بودن کامل مدل‌ها اشتباه نگیر.</p><hr/></section><section aria-labelledby="concept-v31-17-section-09" class="concept-reference-part"><h3 id="concept-v31-17-section-09">نقشهٔ وابستگی</h3><p>قبل از تغییر یک Variable یا Class مرکزی، دامنه اثر را ببین:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">brand-primary
├── button-primary
│   ├── Header CTA
│   └── Pricing CTA
├── link-default
└── badge-featured
</code></pre></figure><p>هرچه Dependency مرکزی‌تر است، تغییر آن باید با نمونه‌های نماینده آزمایش شود.</p><hr/></section><section aria-labelledby="concept-v31-17-section-10" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-17-section-10">اشتباهات رایج</h3><ul>
<li>Variable برای هر عدد یک‌بارمصرف</li>
<li>Global Class با مسئولیت‌های نامرتبط</li>
<li>Component برای دو Element صرفاً هم‌رنگ</li>
<li>نام‌های ظاهری بدون معنا</li>
<li>ساخت Variantهای متعدد بدون Base روشن</li>
<li>Alias Chain فرضی بدون تست</li>
<li>تبدیل همه‌چیز به Utility و از دست‌دادن Intent</li>
<li>تغییر Token مرکزی بدون بررسی مصرف‌کنندگان</li>
</ul><hr/></section><section aria-labelledby="concept-v31-17-section-11" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-17-section-11">تصویر ذهنی نهایی</h3><p>Variable مادهٔ اولیه است، Class دستور پخت و Component قالب کامل سرو غذا. اگر این سه را جابه‌جا کنی، آشپزخانه پر از نسخه‌های کپی و دستورهای متناقض می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-17-section-12" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-17-section-12">قوانین طلایی</h3><ul>
<li><strong>«Variable مقدار را تکرار می‌کند؛ Class Style را؛ Component ساختار را.»</strong></li>
<li><strong>«نام معنایی نقش را حفظ می‌کند، حتی اگر مقدار عوض شود.»</strong></li>
<li><strong>«تعداد مصرف معیار کمکی است، نه قانون قطعی سیستم‌سازی.»</strong></li>
<li><strong>«Variant الگوی معماری است؛ آن را قابلیت Native اثبات‌نشده معرفی نکن.»</strong></li>
<li><strong>«هر تصمیم مرکزی یک دامنه اثر دارد؛ پیش از تغییر، مصرف‌کنندگان را ببین.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Variables, Variables Manager, Classes and Components</li>
<li>Elementor Help: Import/export design systems and V3/V4 synchronization</li>
<li>Design Tokens Community Group material for conceptual token architecture</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-17-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-17-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Design System؛ Size Variable واحد را حمل می‌کند</span></summary>
<section aria-labelledby="lesson-17-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در V4 Variable می‌تواند Color، Font یا Size باشد. Size Variable مقدار و واحد را مرکزی می‌کند؛ Class آن را روی Property مصرف می‌کند.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> Variable برچسب «16px» یا «1rem» در انبار است؛ Class می‌گوید این برچسب را برای padding یا font-size کجا استفاده کن.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Size Variable</th><td><code dir="ltr">variable reference</code></td><td>مقدار Size با واحد ذخیره‌شده</td><td>نوع Variable</td><td>برای مقادیر مشترک.</td><td>یک Size واحد ممکن است برای هر Property معنای طراحی مناسبی نداشته باشد.</td><td><code dir="ltr">E_VAR_MANAGER</code></td></tr><tr><th scope="row">Font Variable</th><td><code dir="ltr">font family reference</code></td><td>نام فونت</td><td>بدون واحد طول</td><td>برای خانوادهٔ فونت مشترک.</td><td>Font variable با font-size یکی نیست.</td><td><code dir="ltr">E_VARIABLES</code></td></tr><tr><th scope="row">Color Variable</th><td><code dir="ltr">color reference</code></td><td>color value</td><td>بدون واحد طول</td><td>برای رنگ مشترک.</td><td>رنگ را با Size variable جایگزین نکن.</td><td><code dir="ltr">E_VAR_MANAGER</code></td></tr><tr><th scope="row">Class</th><td><code dir="ltr">declaration bundle</code></td><td>انواع مقدار متعدد</td><td>وابسته به Property</td><td>برای بستهٔ Style.</td><td>Class واحد واحدی ندارد.</td><td><code dir="ltr">E_CLASSES</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر --space-md = 1.5rem و root=16px باشد، مقدار resolveشده 24px است؛ تغییر root یا Variable می‌تواند همهٔ مصرف‌کننده‌ها را تغییر دهد.</p></section>
<section><h3>📱 در Responsive</h3><p>قبل از ساخت Variable responsive بررسی کن آیا باید مقدار مشترک بماند یا override محلی نیاز است.</p></section>
<section><h3>🔬 در DevTools</h3><p>var(...)، مقدار resolveشده و declaration مصرف‌کننده را جدا ببین.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/variables/" rel="noopener noreferrer" target="_blank">Elementor V4 — Variables</a>، <a href="https://elementor.com/help/variables-manager/" rel="noopener noreferrer" target="_blank">Elementor V4 — Variables Manager</a>، <a href="https://elementor.com/help/classes-in-elementor-2/" rel="noopener noreferrer" target="_blank">Elementor V4 — Classes</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-17-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-17-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — پاک‌سازی</h3><p>اکنون Elementهای واقعی ساخته شده‌اند. Classها را بررسی کن:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">c-platform-section
c-platform-main
c-platform-copy
c-platform-visual
c-platform-intro
c-feature-item
c-feature-text
c-logo-strip
c-logo-frame
c-platform-core
c-platform-node</pre></figure></details><p>هر Class باید مسئولیت روشن داشته باشد.</p><p>تصمیم‌ها:</p><dl class="term-grid"><dt>Feature Item اگر در سایت تکرار می‌شود</dt><dd>Component Candidate؛</dd><dt>Nodeها Style مشترک دارند</dt><dd>Global Class؛</dd><dt>مختصات هر Node</dt><dd>Local Class؛</dd><dt>رنگ Accent مشترک</dt><dd>Variable، اگر Field مربوط پشتیبانی شود.</dd></dl><h3>❓ سؤال توقف</h3><p>شش Node ساختار و ظاهر مشترک دارند، اما موقعیت متفاوت. چه چیزی مشترک و چه چیزی Local است؟</p><details class="disclosure-card"><summary>پاسخ</summary>ظاهر مشترک در Global Class؛ مختصات در Local Class.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> برای هر تفاوت کوچک یک Class جدید بسازی.</p><p><strong>نشانه:</strong> نام‌ها زیاد و هدف Classها مبهم می‌شود.</p><h3>🧪 عمداً خرابش کن</h3><p>برای هر Node یک Global Class کامل و جدا بساز و Background، Radius و Shadow را شش‌بار تکرار کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>تغییر مشترک باید شش‌بار انجام شود؛</li>
<li>احتمال ناهماهنگی بالا می‌رود؛</li>
<li>Class Manager شلوغ می‌شود.</li>
</ul><p>سپس Style مشترک را به <code class="inline-code" dir="ltr">c-platform-node</code> برگردان.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-249-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-249-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-96"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-96-1" name="chk-96-1" type="checkbox"/><span>هر Class مسئولیت روشن دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-96-2" name="chk-96-2" type="checkbox"/><span>Style تکراری یک منبع مشترک دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-96-3" name="chk-96-3" type="checkbox"/><span>Local Class فقط تفاوت یکتا را نگه می‌دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-96-4" name="chk-96-4" type="checkbox"/><span>Component فقط برای Structure تکراری ساخته شده</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Class، Variable و Component چه نوع تکراری را حل می‌کنند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> چهار Button ساختار و Style مشترک دارند ولی متن متفاوت است؛ چه چیزهایی را مشترک می‌کنی؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-97"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-97-1" name="chk-97-1" type="checkbox"/><span>نوع تکرار را تشخیص داده: Style، Value، Structure یا تفاوت یکتا.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-97-2" name="chk-97-2" type="checkbox"/><span>Global Class، Variable، Component یا Local Class را مطابق همان تکرار انتخاب کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-97-3" name="chk-97-3" type="checkbox"/><span>از Class یا Component اضافی بدون مسئولیت خودداری کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-17-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-17-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-HOME2-REUSE-001 و CASE-SOL-REUSE-001</h3><p><strong>هدف:</strong> 🔧 بازسازی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">improvement_candidate</code></p><p>Export دارای امضاهای Style تکراری برای SVG، Heading، Paragraph، Button و Card است. تمرین:</p><ol>
<li>یک گروه واقعی را انتخاب کن؛</li>
<li>Style مشترک را فهرست کن؛</li>
<li>Global Class بساز؛</li>
<li>اگر Structure نیز تکراری است، Component Candidate را ارزیابی کن؛</li>
<li>Runtime را مقایسه کن.</li>
</ol><h3>🔬 پشت صحنه</h3><p>Variableها و Classها در نهایت CSS مشترک تولید می‌کنند، اما در دوره فقط Scope و Reuse مهم است.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="class-system-v4-update-heading-17" role="heading">به‌روزرسانی دقیق سیستم Class در Elementor V4</span></summary><section aria-labelledby="class-system-v4-update-heading-17" class="disclosure-content lesson-section class-system-update">
<div class="definition-card-grid">
<article class="definition-card"><h3>Local Class</h3><p>کلاس محلی / مخصوص همان عنصر است. هر Element حداقل یک Local Class دارد و این کلاس برای همان Element بیشترین اولویت محلی را دارد.</p></article>
<article class="definition-card"><h3>Global Class</h3><p>کلاس سراسری / قابل استفاده مجدد در سیستم طراحی است. وقتی یک ایدهٔ استایلی باید در چند جای سایت تکرار شود، آن را به Global Class تبدیل کن.</p></article>
<article class="definition-card"><h3>States</h3><p>لایهٔ رفتار همان کلاس است: <span dir="ltr">Normal</span>، <span dir="ltr">Hover</span>، <span dir="ltr">Focus</span> و <span dir="ltr">Active</span>.</p></article>
</div>
<section aria-labelledby="class-memory-heading-17" class="memory-layer">
<h3 id="class-memory-heading-17">🧠 استعارهٔ ماندگار</h3>
<p><strong>Local Class</strong> = لباس اختصاصی همین عنصر. <strong>Global Class</strong> = یونیفرم قابل استفاده در چند جای سایت. <strong>States</strong> = حالت‌های رفتار همان کلاس.</p>
<p><strong>🧩 در Elementor V4 یعنی چه؟</strong> اگر اول فقط یک دکمه را ساختی، با Local Class شروع می‌کنی. وقتی همان ظاهر باید الگوی سایت شود، از گزینهٔ تبدیل به Global Class استفاده می‌کنی.</p>
<p class="golden-rule"><strong>📜 قانون طلایی:</strong> چیزی را فقط وقتی Global Class کن که معنی طراحی مشترک و تکرارشونده دارد؛ نه فقط چون اسم مشترک قشنگ است.</p>
</section>
<details class="more-know">
<summary>بیشتر بدانید</summary>
<p>در Elementor V4 چیزی که قبلاً ممکن بود به‌صورت ذهنی «قابل استفاده مجدد» صدا بزنیم، در عمل با Global Class توضیح داده می‌شود. این نام را از خود UI و Class Manager دنبال کن تا مفهوم جداگانهٔ ساختگی نسازی.</p>
</details>
</section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-17-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-17-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-99"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-99-1" name="chk-99-1" type="checkbox"/><span>می‌توانی Classes، Variables و Components در Design System V4 را براساس نوع تکرار انتخاب کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-99-2" name="chk-99-2" type="checkbox"/><span>می‌توانی Style مشترک را از Value مشترک و Structure مشترک جدا کنی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-100"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-100-1" name="chk-100-1" type="checkbox"/><span>Nodeهای TUYA را با Class مشترک، مقدارهای مشترک پشتیبانی‌شده و ساختار تکراری منظم می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-100-2" name="chk-100-2" type="checkbox"/><span>تغییر یک منبع مشترک را روی همهٔ مصرف‌کننده‌ها بررسی می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-101"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-101-1" name="chk-101-1" type="checkbox"/><span>برای Button System می‌توانی Base Class، Variant، Variable و Component را از هم تفکیک کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-17-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-17-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد صفحات Hybrid را بدون ترس و بدون مهاجرت شتاب‌زده تحلیل می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 17</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-17-completion"><fieldset><legend>ثبت پایان درس 17</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-17-complete" name="lesson-17-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-17-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Design System بدون قاطی‌کاری</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Variable در برابر Global Class</h3><p>Variable مادهٔ خام است؛ Global Class دستور پخت. <code dir="ltr">color-brand</code> یک مقدار است؛ <code dir="ltr">btn-primary</code> یک تصمیم کامل ظاهری است که می‌تواند از آن مقدار استفاده کند.</p></section>
<section class="inline-compare-card"><h3>Global Class در برابر Component</h3><p>Global Class ظاهر را reuse می‌کند؛ Component ساختار را reuse می‌کند. اگر فقط Style تکرار شده، Class. اگر تصویر، عنوان، متن و دکمه با هم تکرار شده‌اند، Component.</p></section>
</div>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="design-system-split-title" role="heading">تکمیل نسخه 22 — درس 17 را به سه لایه ذهنی تقسیم کن</span></summary><section aria-labelledby="design-system-split-title" class="smart-note-card disclosure-content">
<p>درس 17 عمداً دروازهٔ Design System است، اما برای یادگیری بهتر آن را در ذهن به سه درس کوچک‌تر تقسیم کن:</p>
<div class="visual-card-grid three"><div class="visual-card"><strong>1) Classes</strong><p>Local Class برای همان عنصر؛ Global Class برای سبک قابل استفاده در چند جای سایت.</p></div><div class="visual-card"><strong>2) Variables</strong><p>توکن‌هایی مثل رنگ، فاصله، radius و typography که مقدار مرکزی می‌دهند.</p></div><div class="visual-card"><strong>3) Components</strong><p>الگوی ساختاری قابل تکرار؛ فقط وقتی ساختار و سبک با هم باید تکرار شوند.</p></div></div>
<p>Global Fonts و Global Colors یک لایهٔ سراسری برای هویت بصری سایت هستند. Variables Manager در جریان V4 به تو اجازه می‌دهد مقدارهای طراحی را مرکزی‌تر و قابل مدیریت‌تر نگه داری، و در بعضی مسیرها می‌توان Variables را با Global Colors/Fonts همگام کرد.</p>
<p class="golden-rule"><strong>قانون طلایی:</strong> Class رفتار ظاهری را گروه‌بندی می‌کند؛ Variable مقدار را مرکزی می‌کند؛ Component ساختار قابل تکرار می‌سازد.</p>
</section></details><details class="lesson-disclosure design-system-decision" id="lesson-17-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Design System</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
