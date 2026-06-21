<article class="lesson card-surface" data-lesson="2" id="lesson-2">

<h2 class="lesson-title former-h1">درس 2 — Element Tree و انتخاب Element مناسب</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-2-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-2-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> بعد از تشخیص Context، Screenshot را به یک Element Tree قابل‌فهم تبدیل کنی؛ یعنی بدانی هر بخش Parent است یا Child، و برای هر نقش، Div Block، Flexbox یا Grid مناسب‌تر است.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تنظیمات کامل Flex/Grid، مقدارهای نهایی Width/Gap/Padding، Position نهایی Nodeها، یا Style نهایی TUYA.</p>
<p><strong>در پایان باید بتوانی:</strong> یک Tree اولیه برای TUYA بسازی یا روی کاغذ توضیح بدهی، بدون اینکه برای جبران ساختار اشتباه سراغ Margin، Offset یا Wrapper اضافی بروی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-2-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-2-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧩 ساختاری + 👁 مشاهده‌ای + 🛠 اجرای محدود</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۱۵–۲۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۰–۳۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> درس ۲ نباید تبدیل به آموزش کامل Flex/Grid شود. هدف این است که هنرجو بفهمد Tree یعنی رابطهٔ مسئولیت‌ها؛ سپس فقط یک Tree حداقلی و قابل توضیح برای TUYA بسازد.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_context_aware_structure</code></p>
</section>
</details>

<section aria-labelledby="lesson-2-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-2-lesson-understand-4">A. بفهم</h2>

<h3>مسئله</h3>
<p>بیشتر آشفتگی‌های Elementor از انتخاب Element اشتباه شروع نمی‌شود؛ از <strong>رابطهٔ اشتباه بین Elementها</strong> شروع می‌شود. اگر Child بیرون از Parent درست ساخته شود، بعداً با Margin، Position و Wrapper اضافه تلاش می‌کنی ظاهر را نجات بدهی.</p>

<h3>پیوند با درس ۱</h3>
<p>در درس ۱ یاد گرفتی تغییر همیشه در Context انجام می‌شود. در درس ۲، اولین بخش مهم Context را می‌سازی: <strong>Element Tree</strong>.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Lesson 1: Context را تشخیص بده
↓
Lesson 2: Structure / Element Tree را بساز
↓
Lesson 3+: Layout و Style را روی Tree درست اعمال کن</code></pre>
</figure>

<h3>تعریف ساده</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Element Tree</dt><dd>نقشهٔ خانوادهٔ عناصر صفحه؛ نشان می‌دهد چه چیزی داخل چه چیزی است.</dd>
<dt>Parent</dt><dd>ظرفی که Childها را نگه می‌دارد و معمولاً بخشی از رفتار Layout آن‌ها را کنترل می‌کند.</dd>
<dt>Child</dt><dd>عنصری که مستقیم داخل Parent قرار دارد.</dd>
<dt>Sibling</dt><dd>دو Child که Parent مشترک دارند.</dd>
<dt>Descendant</dt><dd>هر عنصر در عمق زیرمجموعهٔ یک Parent، نه لزوماً Child مستقیم.</dd>
</dl>
</section>

<h3>نکتهٔ حیاتی: Parent فقط «جعبه» نیست؛ محدودهٔ مسئولیت است</h3>
<p>Parent خوب فقط برای مرتب‌کردن Navigator ساخته نمی‌شود. Parent باید یک مسئولیت واقعی داشته باشد:</p>
<ul>
<li><strong>Semantic:</strong> گروهی از محتوا از نظر معنا به هم تعلق دارند.</li>
<li><strong>Layout:</strong> چند Child باید با یک قانون مشترک چیده شوند.</li>
<li><strong>Scope:</strong> یک Style یا Class باید فقط روی همین گروه اثر بگذارد.</li>
<li><strong>Position:</strong> یک Overlay باید داخل همین محدوده مرجع داشته باشد.</li>
<li><strong>Component:</strong> ساختار قرار است دوباره استفاده شود.</li>
</ul>
<p>اگر Wrapper هیچ‌کدام از این مسئولیت‌ها را ندارد، احتمالاً بدهی ساختاری است.</p>

<h3>Decision Tree انتخاب Element</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>◇ فقط یک Wrapper سبک برای گروه‌بندی یا Scope لازم داری؟</li>
<li>├─ بله → <strong>Div Block</strong></li>
<li>└─ خیر</li>
<li>◇ Childها روی یک محور اصلی چیده می‌شوند؟</li>
<li>├─ بله → <strong>Flexbox</strong></li>
<li>└─ خیر</li>
<li>◇ هم ردیف و هم ستون را هم‌زمان کنترل می‌کنی؟</li>
<li>├─ بله → <strong>Grid</strong></li>
<li>└─ خیر → ساختار را دوباره تحلیل کن؛ شاید هنوز Parent درست را پیدا نکرده‌ای.</li>
</ul>
</section>

<h3>اصل کمترین موتور لازم</h3>
<p>Element قوی‌تر همیشه انتخاب بهتر نیست. Grid وقتی لازم است که کنترل دو‌بعدی واقعی داری. Flex وقتی مناسب است که Childها روی یک محور چیده می‌شوند. Div وقتی کافی است که فقط گروه‌بندی، Scope یا مرجع ساده لازم داری.</p>
<div aria-label="جدول نقش Elementها" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>نقش Elementها در درس ۲</caption>
<thead><tr><th scope="col">Element</th><th scope="col">نقش اصلی</th><th scope="col">زمان انتخاب</th><th scope="col">تلهٔ رایج</th></tr></thead>
<tbody>
<tr><th scope="row">Div Block</th><td>Wrapper سبک، Scope، Shell، مرجع ساده</td><td>وقتی فقط ظرف عمومی لازم است.</td><td>برای هر چیز یک Div اضافی ساختن.</td></tr>
<tr><th scope="row">Flexbox</th><td>چیدمان یک‌محورهٔ Childهای مستقیم</td><td>وقتی Childها در Row یا Column منظم می‌شوند.</td><td>فکر کردن اینکه Flex همهٔ Descendantها را مستقیم کنترل می‌کند.</td></tr>
<tr><th scope="row">Grid</th><td>چیدمان دو‌بعدی ردیف/ستون</td><td>وقتی رابطهٔ چند ردیف و ستون مهم است.</td><td>استفاده برای یک ردیف سادهٔ Icon + Text.</td></tr>
<tr><th scope="row">Heading / Paragraph / Button / Image</th><td>Content معنی‌دار</td><td>وقتی کاربر متن، تعامل یا تصویر واقعی می‌بیند.</td><td>Content را با Wrapper اشتباه گرفتن.</td></tr>
</tbody>
</table>
</div>

<h3>تفاوت Child مستقیم با Descendant</h3>
<p>یک Parent معمولاً روی Childهای مستقیم خود فرمان Layout می‌دهد. اگر یک عنصر «نوه» باشد، از Parent بالاتر مستقیم فرمان نمی‌گیرد.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Parent Flex
├── Child A  ← Flex item
└── Child B  ← Flex item
    └── Grandchild  ← Flex item مستقیم Parent نیست</code></pre>
</figure>
<p>این تفاوت برای Debug حیاتی است. اگر Child را در عمق اشتباه گذاشتی، ممکن است هرقدر روی Parent تنظیم Layout انجام دهی، عنصر مورد نظر آن‌طور که انتظار داری جابه‌جا نشود.</p>

<h3>ارتباط با Flow و Absolute</h3>
<p>Tree سالم باعث می‌شود Content اصلی در Flow باقی بماند. Absolute نباید جایگزین Tree شود. Absolute فقط وقتی وارد می‌شود که یک عنصر واقعاً باید نسبت به یک Stage مرجع جای‌گذاری شود؛ مثل Nodeهای اطراف Core در TUYA.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-2.0.0" id="lesson-2-concept-reference">
<summary>📚 مرجع مفهومی کامل — Element Tree، مسئولیت Parent و انتخاب کمترین موتور لازم</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="2" data-source-version="tuya-revised-2.0.0">

<p class="concept-reference-lead">این مرجع بخش مفهومی را حفظ می‌کند و آن را به روند تمرین‌های واقعی TUYA وصل می‌کند. هدف این نیست که هر چیزی را بسازیم؛ هدف این است که Tree درست را قبل از Style بسازیم.</p>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-2-folder-analogy">
<h3 id="lesson-2-folder-analogy">۱. تشبیه پوشه‌ها</h3>
<p>Element Tree مثل ساختار پوشه‌های یک پروژه است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Project
├── Images
│   ├── hero.jpg
│   └── logo.svg
└── Documents
    ├── proposal.pdf
    └── invoice.pdf</code></pre>
</figure>
<p>اگر <code dir="ltr">logo.svg</code> داخل Documents باشد، شاید هنوز فایل باز شود، اما ساختار اشتباه است. در Elementor هم اگر Button یا Logo بیرون از Parent معنایی خودش ساخته شود، ظاهر شاید با Margin درست شود، اما نگهداری سخت می‌شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-2-parent-power">
<h3 id="lesson-2-parent-power">۲. Parent نقشهٔ قدرت است</h3>
<p>Parent تعیین می‌کند Childها با چه قانونی کنار هم قرار بگیرند، کدام Style به چه محدوده‌ای محدود شود، کدام Overlay نسبت به چه محدوده‌ای محاسبه شود، و در Responsive کدام گروه با هم تغییر رفتار دهند.</p>
<p>پس سؤال درست این نیست: «کدام Element را سریع‌تر اضافه کنم؟» سؤال درست این است:</p>
<blockquote><p>کدام چیزها باید با هم حرکت کنند، با هم Style بگیرند، با هم مخفی شوند، یا با هم در Responsive تغییر کنند؟</p></blockquote>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-2-tuva-structure">
<h3 id="lesson-2-tuva-structure">۳. Tree پیشنهادی TUYA در این مرحله</h3>
<p>این Tree هنوز Style نهایی نیست. فقط اسکلت تصمیم‌گیری است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Section
└── TUYA Shell
    ├── Copy Area
    │   ├── Eyebrow
    │   ├── Heading
    │   ├── Paragraph
    │   ├── Feature List
    │   └── Logo Strip
    └── Visual Area
        └── Visual Stage
            ├── Core Cloud
            └── Orbit Nodes</code></pre>
</figure>
<p><strong>وضعیت اعتبار:</strong> وجود دو ناحیهٔ Copy و Visual در تصویر مرجع confirmed است. نام دقیق Elementها، عرض دقیق Shell، مقدار Gap، Height و مختصات Nodeها هنوز provisional هستند تا در درس‌های بعد با UI واقعی و Breakpointها تأیید شوند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-2-section-shell-main">
<h3 id="lesson-2-section-shell-main">۴. ابهام Section، Shell و Main را حل کن</h3>
<p>در بعضی توضیح‌ها ساختار دو‌لایه و سه‌لایه با هم قاطی می‌شود. برای درس ۲، باید مسئولیت‌ها را شفاف کنیم:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="مسئولیت Section Shell Main">
<table class="data-table educational-table edu-table">
<caption>مسئولیت لایه‌های اصلی</caption>
<thead><tr><th scope="col">لایه</th><th scope="col">مسئولیت</th><th scope="col">در این درس</th></tr></thead>
<tbody>
<tr><th scope="row">TUYA Section</th><td>محدودهٔ بیرونی صفحه، فاصله از سکشن‌های دیگر، Background کلی در صورت نیاز.</td><td>confirmed به‌عنوان محدودهٔ اصلی.</td></tr>
<tr><th scope="row">TUYA Shell</th><td>کارت/پوستهٔ اصلی و Parent مشترک Copy و Visual.</td><td>confirmed به‌عنوان Parent مرکزی تمرین.</td></tr>
<tr><th scope="row">TUYA Main</th><td>لایهٔ واسط احتمالی برای چیدمان داخلی، فقط اگر Shell نباید همزمان پوسته و Layout باشد.</td><td>provisional؛ فعلاً اضافه نمی‌شود مگر مسئولیت جداگانه ثابت شود.</td></tr>
</tbody>
</table>
</div>
<p>قانون عملی: اگر Shell هم پوستهٔ بصری است و هم دو ناحیهٔ Copy/Visual را می‌چیند، فعلاً Main جدا نساز. اگر بعداً نیاز شد پوسته و Layout را جدا کنی، Main را با دلیل اضافه کن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-2-wrapper-rules">
<h3 id="lesson-2-wrapper-rules">۵. چه زمانی Wrapper بسازیم؟</h3>
<ul>
<li>وقتی چند Child باید با یک قانون Layout مشترک چیده شوند.</li>
<li>وقتی چند عنصر باید با هم در Responsive تغییر کنند.</li>
<li>وقتی لازم است یک محدودهٔ Scope برای Class یا Background داشته باشی.</li>
<li>وقتی یک Overlay به مرجع Position مشخص نیاز دارد.</li>
<li>وقتی ساختار قرار است به Component تبدیل شود.</li>
</ul>
<p>Wrapper نساز فقط چون «بعداً شاید لازم شود». این کار Navigator را مبهم می‌کند و Debug را سخت‌تر می‌کند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-2-rename">
<h3 id="lesson-2-rename">۶. اصلاح اجرایی: Rename در Structure</h3>
<aside class="correction-card">
<p><strong>اصلاح ثبت‌شده:</strong> تغییر نام عنصر از منوی راست‌کلیک انجام نمی‌شود؛ روی نام عنصر در Structure دوبار کلیک کن.</p>
<p>در این درس، Rename فقط برای خوانایی Tree است. Rename نباید با ساخت Class جدید، تغییر Style یا تغییر Semantic Tag قاطی شود.</p>
</aside>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-2-golden">
<h3 id="lesson-2-golden">۷. قوانین طلایی</h3>
<ul>
<li><strong>Tree قبل از Style می‌آید.</strong></li>
<li><strong>Parent باید مسئولیت واقعی داشته باشد.</strong></li>
<li><strong>Child را با Margin شبیه داخل Parent نکن؛ واقعاً داخل Parent درست بساز.</strong></li>
<li><strong>کمترین موتور لازم را انتخاب کن: Div، بعد Flex، بعد Grid.</strong></li>
<li><strong>Flex فقط Child مستقیم را مستقیماً کنترل می‌کند.</strong></li>
<li><strong>Wrapper بی‌دلیل، بدهی ساختاری است.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفاهیم Parent/Child، Display، Flex و Grid بر پایهٔ رفتار CSS و مستندات رسمی Elementor/MDN توضیح داده شده‌اند. تصمیم‌های مربوط به TUYA تا وقتی با UI واقعی و Screenshotهای همان پروژه تأیید نشوند، نباید مقدار قطعی تلقی شوند.</p>
<ul>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout" rel="noopener noreferrer" target="_blank">MDN — CSS Flexbox</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout" rel="noopener noreferrer" target="_blank">MDN — CSS Grid Layout</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-2-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-2-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Element Tree واحد ندارد؛ Layout داخل آن واحد می‌گیرد</span>
</summary>
<section aria-labelledby="lesson-2-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Parent، Child و Sibling رابطه‌اند، نه اندازه. واحدها وقتی وارد می‌شوند که برای ظرف انتخاب‌شده Width، Gap، Padding یا Track تعریف کنی.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> نقشهٔ خانوادگی قد و وزن نیست؛ فقط می‌گوید چه کسی فرزند چه کسی است. بعداً می‌توانی برای هر عضو اندازه ثبت کنی.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">نوع Element</th><td><code dir="ltr">Div / Flexbox / Grid</code></td><td>انتخاب Element</td><td>بدون واحد</td><td>Element قوی‌تر را فقط برای داشتن کنترل بیشتر انتخاب نکن.</td></tr>
<tr><th scope="row">Display</th><td><code dir="ltr">display</code></td><td>keyword</td><td>رفتار Layout</td><td>Display را با Width یا Flow یکی نگیر.</td></tr>
<tr><th scope="row">Gap</th><td><code dir="ltr">gap</code></td><td>Length / درصد بسته به کنترل</td><td>Parent layout</td><td>Gap ساختار اشتباه را درمان نمی‌کند.</td></tr>
<tr><th scope="row">Order / Direction</th><td>Responsive layout control</td><td>keyword / number</td><td>Breakpoint</td><td>Tree معنایی را بی‌دلیل در هر Breakpoint عوض نکن.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>not_applicable — ابتدا Tree را درست کن؛ محاسبهٔ Width/Gap در درس‌های بعدی می‌آید.</p></section>
<section><h3>📱 در Responsive</h3><p>Tree معنایی را تا حد ممکن حفظ کن؛ در Breakpointها معمولاً Direction، Order، Size یا Gap تغییر می‌کند، نه اصل رابطهٔ Parent/Child.</p></section>
<section><h3>🔬 در DevTools</h3><p>Elements panel رابطهٔ DOM را نشان می‌دهد؛ Computed فقط Style نهایی را نشان می‌دهد و جای تحلیل Tree را نمی‌گیرد.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-2-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-2-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — ساخت Tree بدون Style</h3>
<p>در این تمرین، فقط Tree را می‌سازی یا اگر هنوز در Editor نیستی، روی کاغذ می‌نویسی. هیچ Style، Position، Width، Height، Shadow یا Class مشترک جدید نساز.</p>

<h3>مرحلهٔ ۰ — وضعیت را با Evidence Gate بنویس</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate درس ۲">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از ساخت Tree</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>TUYA به دو ناحیهٔ اصلی نیاز دارد: Copy Area و Visual Area.</td><td>این دو باید زیر یک Parent مشترک قرار بگیرند.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Core و Nodeها از نظر بصری داخل Visual هستند.</td><td>آن‌ها نباید در سطح Copy یا Section ساخته شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>وجود یا عدم وجود TUYA Main بین Section و Shell.</td><td>فعلاً اضافه نمی‌شود مگر مسئولیت جداگانه ثابت شود.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Class فعال، Breakpoint فعلی، Width واقعی سایت و تنظیمات Theme.</td><td>هیچ مقدار عددی قطعی وارد نمی‌شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Tree حداقلی را بساز</h3>
<figure class="visual-figure ascii-figure">
<figcaption>Tree حداقلی این درس</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Div Block: TUYA Section
└── Div/Flexbox: TUYA Shell
    ├── Div Block: TUYA Copy
    └── Div Block: TUYA Visual</code></pre>
</figure>

<aside class="implementation-step-card" aria-label="اقدام کوچک درس دو">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ساخت رابطهٔ Parent/Child، نه ظاهر نهایی.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure/Navigator → Add Elementها → Rename با دوبار کلیک.</p>
<p><strong>Element هدف:</strong> فقط TUYA Section، TUYA Shell، TUYA Copy، TUYA Visual.</p>
<p><strong>Class فعال:</strong> فعلاً Class مشترک جدید نساز.</p>
<p><strong>Property:</strong> هیچ Style Property تغییر نکند.</p>
<p><strong>نباید تغییر کند:</strong> Width، Height، Gap، Position، Shadow، Nodeها، Typography، Background.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Tree حداقلی ساخته شد و هنوز هیچ Style وارد نشده است.»</p>
</aside>

<h3>مرحلهٔ ۲ — مسئولیت هر Element را بگو</h3>
<dl class="term-grid">
<dt>TUYA Section</dt><dd>محدودهٔ بیرونی سکشن؛ فعلاً فقط Parent ریشهٔ این تمرین.</dd>
<dt>TUYA Shell</dt><dd>Parent مشترک Copy و Visual؛ ممکن است در درس‌های بعد مسئول پوسته و Layout شود.</dd>
<dt>TUYA Copy</dt><dd>ظرف محتوای متنی، ویژگی‌ها، دکمه و Logoها؛ در Flow می‌ماند.</dd>
<dt>TUYA Visual</dt><dd>ظرف سمت تصویری؛ در درس‌های بعد Stage داخلی برای Core/Node می‌گیرد.</dd>
</dl>

<h3>مرحلهٔ ۳ — فعلاً چه چیزهایی نسازیم؟</h3>
<ul>
<li>Nodeهای اطراف Core را فعلاً نساز.</li>
<li>Visual Stage را فقط اگر در درس بعد لازم شد اضافه کن.</li>
<li>Class مشترک نساز.</li>
<li>Width/Gap/Height نده.</li>
<li>Position Absolute نزن.</li>
<li>Shadow/Glow/Background اضافه نکن.</li>
</ul>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>برای یک Icon و متن که باید کنار هم باشند، انتخاب اولیهٔ مناسب‌تر چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-2">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-2-a" name="stop-question-2" type="radio" value="A"/><span>A) Grid چندستونه</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-2-b" name="stop-question-2" type="radio" value="B"/><span>B) Flexbox</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-2-c" name="stop-question-2" type="radio" value="C"/><span>C) Absolute</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Icon و متن معمولاً دو Child روی یک محور هستند؛ پس Flexbox نقطهٔ شروع ساده‌تر و دقیق‌تری است. Grid برای رابطهٔ دو‌بعدی واقعی است و Absolute برای Layout اصلی مناسب نیست.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> برای هر گروه کوچک یک Wrapper یا Flexbox جدید بسازی.</p>
<p><strong>نشانه:</strong> Tree سریعاً چندلایه می‌شود، بدون اینکه هر لایه وظیفه‌ای داشته باشد.</p>
<p><strong>قاعده:</strong> هر Wrapper باید دلیل Semantic، Layout، Scope، Position یا Component داشته باشد.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>سه Wrapper خالی بین TUYA Section و TUYA Shell تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Tree خراب‌شده با Wrapperهای بی‌دلیل</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Section
└── Wrapper 1
    └── Wrapper 2
        └── Wrapper 3
            └── TUYA Shell</code></pre>
</figure>
<h4>انتظار داری چه ببینی؟</h4>
<ul>
<li>Structure خوانایی کمتری دارد.</li>
<li>انتخاب Parent درست سخت‌تر می‌شود.</li>
<li>Style ممکن است روی لایهٔ اشتباه اعمال شود.</li>
<li>ظاهر شاید هنوز فرق نکند، اما نگهداری سخت‌تر می‌شود.</li>
</ul>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-7">
<fieldset>
<legend>Checkpoint درس ۲</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-7-1" name="chk-7-1" type="checkbox"/><span>Tree حداقلی فقط چهار Element اصلی دارد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-7-2" name="chk-7-2" type="checkbox"/><span>Copy و Visual فرزند مستقیم Shell هستند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-7-3" name="chk-7-3" type="checkbox"/><span>هنوز هیچ Position، Width، Height، Gap یا Shadow اضافه نشده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-7-4" name="chk-7-4" type="checkbox"/><span>هر Wrapper موجود یک مسئولیت واقعی دارد.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Parent و Child چه تفاوتی دارند؟</p>
<p><strong>انتقال به موقعیت تازه:</strong> برای Header شامل Logo، Menu و CTA یک Tree سه‌سطحی پیشنهاد بده.</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید رابطهٔ Parent/Child را توضیح بدهد، Element را براساس مسئولیت انتخاب کند، و از ظاهر موقت یا Offset برای توجیه ساختار استفاده نکند.</p>
</details>

</section>
</details>

<details aria-labelledby="lesson-2-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-2-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 CASE-HOME2-DOM-001</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">improvement_candidate</code></p>
<p>در Export واقعی ممکن است چند Element ساختاری بدون Child دیده شود. این شواهد به‌تنهایی مجوز حذف فوری نیست.</p>
<p>سؤال‌ها:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا آن Element برای Spacer، Grid Cell، Background یا Anchor استفاده شده است؟</li>
<li>آیا Selector یا Script به آن وابسته است؟</li>
<li>آیا حذف آن در Runtime ظاهر یا رفتار را تغییر می‌دهد؟</li>
</ul>
</section>
<p>نتیجهٔ درست فعلی: <code class="inline-code" dir="ltr">insufficient_evidence</code>. اول مشاهده و تست، بعد حذف.</p>

<h3>🔬 پشت صحنه</h3>
<p>Element Tree در Elementor نمای آموزشی/ویرایشی توست؛ DOM واقعی مرورگر ممکن است لایه‌ها، nodeها و جزئیات بیشتری داشته باشد. برای طراحی، Structure کافی است؛ برای Audit، DevTools لازم است.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-2-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-2-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-10">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-10-1" name="chk-10-1" type="checkbox"/><span>می‌توانم Parent، Child، Sibling و Descendant را در یک Tree واقعی تشخیص بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-10-2" name="chk-10-2" type="checkbox"/><span>می‌توانم تفاوت نقش Div Block، Flexbox و Grid را براساس مسئولیت توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-10-3" name="chk-10-3" type="checkbox"/><span>می‌دانم Wrapper باید دلیل داشته باشد.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-11">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-11-1" name="chk-11-1" type="checkbox"/><span>Tree اولیهٔ TUYA را بدون Style، بدون Position و بدون Wrapper اضافی می‌سازم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-11-2" name="chk-11-2" type="checkbox"/><span>Copy و Visual را زیر Parent مشترک قرار می‌دهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-11-3" name="chk-11-3" type="checkbox"/><span>قبل از ساخت Main واسط، مسئولیت جداگانهٔ آن را ثابت می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-12">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-12-1" name="chk-12-1" type="checkbox"/><span>برای Header شامل Logo، Menu و CTA یک Tree سه‌سطحی پیشنهاد می‌دهم و دلیل Parentها را توضیح می‌دهم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-2-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-2-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، روی همین Tree شروع می‌کنیم به تعریف Flow و Display. هنوز نوبت Style نهایی، مقدارهای عددی، Nodeها و Shadow نیست.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 2</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-2-completion">
<fieldset>
<legend>ثبت پایان درس 2</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-2-complete" name="lesson-2-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
