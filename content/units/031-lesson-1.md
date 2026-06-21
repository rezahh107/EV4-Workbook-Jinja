<article class="lesson card-surface" data-lesson="1" id="lesson-1">

<h2 class="lesson-title former-h1">درس 1 — V4 چگونه فکر می‌کند؟</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-1-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-1-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> قبل از هر تغییر ظاهری، Context تغییر را تشخیص بدهی: کدام Element انتخاب شده، Parent آن چیست، کدام Class فعال است، در کدام State و Device کار می‌کنی، و تغییر قرار است در چه محدوده‌ای اثر بگذارد.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> ساخت کامل سکشن TUYA، تعیین مختصات قطعی Nodeها، طراحی نهایی Shadow/Glow، یا حفظ کردن تمام CSS.</p>
<p><strong>در پایان باید بتوانی:</strong> یک Screenshot یا وضعیت واقعی Elementor را به سه دستهٔ <code dir="ltr">confirmed</code>، <code dir="ltr">provisional</code> و <code dir="ltr">unknown</code> تقسیم کنی و فقط یک اقدام کوچک بعدی پیشنهاد بدهی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-1-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-1-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟢 سبک، ولی پایه‌ای</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>👁 مشاهده‌ای + 🧠 مفهومی + 🧪 تمرین تشخیص</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۱۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۱۵–۲۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۰–۱۵ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> هدف این درس ساختن صفحه نیست؛ هدف ساختن «روش نگاه» است. هنرجو باید یاد بگیرد قبل از تغییر دادن، وضعیت را ببیند، محدودهٔ اثر را تشخیص دهد و فقط یک تغییر کوچک قابل Undo انجام دهد.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_tuya_context_first_method</code></p>
</section>
</details>

<section aria-labelledby="lesson-1-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-1-lesson-understand-4">A. بفهم</h2>

<h3>مسئله</h3>
<p>در Elementor ممکن است یک Element را انتخاب کنی، رنگ یا فاصله‌ای را تغییر بدهی، ولی نتیجه‌ای که می‌بینی با انتظار تو فرق کند. مشکل معمولاً این نیست که «CSS بلد نیستی». مشکل این است که هنوز نمی‌دانی تغییر در کدام Context انجام شده است.</p>

<h3>اصل کلیدی: تغییر همیشه در Context انجام می‌شود</h3>
<section class="smart-note-card" dir="rtl" lang="fa" aria-labelledby="lesson-1-context-principle">
<h4 id="lesson-1-context-principle">Context یعنی محدودهٔ اثرگذاری تغییر</h4>
<p>هر تغییر در V4 باید با این پرسش شروع شود: «من دقیقاً دارم چه چیزی را، در کدام محدوده، برای کدام وضعیت تغییر می‌دهم؟»</p>
<p>اگر تغییر دیده نمی‌شود یا بیش از حد اثر می‌گذارد، قبل از اضافه‌کردن عددهای جدید، این پنج نقطه را بررسی کن:</p>
<ol>
<li><strong>Element:</strong> آیا عنصر درست انتخاب شده است؟</li>
<li><strong>Parent:</strong> آیا Parent درست مسئول چیدمان است؟</li>
<li><strong>Class:</strong> آیا Local Class یا Global Class درست فعال است؟</li>
<li><strong>State:</strong> آیا Normal، Hover، Focus یا وضعیت دیگری را ویرایش می‌کنی؟</li>
<li><strong>Device:</strong> آیا در Desktop، Tablet یا Mobile هستی؟</li>
</ol>
</section>

<h3>General و Style در V4</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>General</dt><dd>این Element چیست، چه محتوا یا نقش اجرایی دارد و دادهٔ اصلی آن کجاست؟</dd>
<dt>Style</dt><dd>این Element چگونه نمایش داده می‌شود: Layout، Size، Spacing، Position، Typography، Border، Background و Effects.</dd>
<dt>Classes</dt><dd>Style روی کدام بستهٔ قابل‌ردیابی اعمال می‌شود: Local برای همین Element، یا Global برای الگوی مشترک.</dd>
</dl>
</section>

<h3>مدل ذهنی زنجیره‌ای دوره</h3>
<p>درس‌های جزوه نباید مجموعه‌ای از مفهوم‌های جدا باشند. هر فصل باید حلقه‌ای از یک زنجیره باشد:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Context
↓
Structure
↓
Flow / Display
↓
Size / Units
↓
Position / Layering
↓
Responsive
↓
Design System
↓
DOM / Audit</code></pre>
</figure>
<p>یعنی در هر تمرین، قبل از مقداردهی ظاهری، ابتدا Context و Structure بررسی می‌شود؛ بعد Flow/Display، بعد Size/Units، بعد Position، و در پایان Responsive و Audit.</p>

<h3>سه برچسب اجباری برای فکر کردن</h3>
<div aria-label="جدول برچسب‌های اطمینان" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>برچسب‌های تصمیم‌گیری در تمرین‌های جزوه</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">معنی</th><th scope="col">در تمرین چه کار می‌کنیم؟</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>از Screenshot، گزارش کاربر، رابط واقعی یا مستند رسمی تأیید شده است.</td><td>می‌توانی بر اساس آن اقدام محدود انجام بدهی.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>پیشنهاد بصری یا برداشت موقت است، اما هنوز قطعی نیست.</td><td>فقط به‌عنوان مقدار آزمایشی، قابل Undo و قابل اصلاح استفاده می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>شاهد کافی وجود ندارد.</td><td>نباید عدد قطعی، عنصر جدید یا تصمیم ساختاری بر اساس آن بسازی.</td></tr>
</tbody>
</table>
</div>

<h3>مثال ساده: Border دکمه قرمز است، اما آبی انتظار داشتی</h3>
<p>واکنش مبتدی این است: یک رنگ آبی دیگر انتخاب کند. واکنش درست V4 این است:</p>
<ol>
<li>آیا Button درست انتخاب شده است؟</li>
<li>آیا Class فعال همان Classی است که باید ویرایش شود؟</li>
<li>آیا در State درست هستی؟ مثلاً Hover را تغییر نداده‌ای در حالی که Normal را می‌بینی؟</li>
<li>آیا در Device درست هستی؟ شاید مقدار Mobile با Desktop فرق داشته باشد.</li>
<li>آیا Style از Class دیگری Override شده است؟</li>
</ol>

<h3>چیزی که فعلاً لازم نیست</h3>
<p>در این درس لازم نیست کل CSS Cascade یا همهٔ پنل‌های Elementor را حفظ کنی. باید یک عادت اصلی بسازی: <strong>قبل از تغییر، Context را ثابت کن.</strong></p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-1.0.0" id="lesson-1-concept-reference">
<summary>📚 مرجع مفهومی کامل — درک عمیق Context، Structure و روش فکر در Elementor V4</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="1" data-source-version="tuya-revised-1.0.0">

<p class="concept-reference-lead">این مرجع برای حذف بخش مفهومی نیست؛ برای دقیق‌تر کردن آن است. تمرین‌ها باید مربی‌محور شوند، اما مرجع مفهومی باید همچنان کامل، قابل‌رجوع و زنجیره‌ای باقی بماند.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-1-ref-problem">
<h3 id="lesson-1-ref-problem">۱. مسئله‌ای که این درس حل می‌کند</h3>
<p>کاربر مبتدی معمولاً Screenshot را می‌بیند و فوراً می‌پرسد: «این چند px از بالا فاصله دارد؟» این سؤال زود مطرح شده است. سؤال درست‌تر این است:</p>
<blockquote><p>این بخش چه نقشی دارد، داخل کدام Parent است، در Flow می‌ماند یا نیاز به Stage/Overlay دارد؟</p></blockquote>
<p>اگر این سؤال‌ها جواب داده نشوند، طراحی به مجموعه‌ای از Offsetهای شکننده تبدیل می‌شود.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-1-city-analogy">
<h3 id="lesson-1-city-analogy">۲. تشبیه شهر: Context یعنی زمین، Stage یعنی قطعهٔ حصارکشی‌شده</h3>
<ul>
<li><strong>صفحه:</strong> شهر بزرگ است.</li>
<li><strong>Section:</strong> یک محدوده از شهر است.</li>
<li><strong>Shell:</strong> قطعه‌زمین اصلی پروژه است.</li>
<li><strong>Stage:</strong> محدودهٔ حصارکشی‌شده‌ای است که Overlay فقط داخل آن اتفاق می‌افتد.</li>
<li><strong>Core:</strong> مرکز Visual است.</li>
<li><strong>Node:</strong> نقاط یا آیتم‌هایی هستند که نسبت به Core چیده می‌شوند.</li>
</ul>
<p>قانون مهم: اگر Stage محدودهٔ روشن نداشته باشد، Nodeها به خیابان اصلی شهر می‌ریزند. در CSS یعنی عنصرهای Absolute ممکن است نسبت به مرجع نادرست جای‌گذاری شوند.</p>
</section>

<section class="concept-reference-part concept-reference-definition" aria-labelledby="lesson-1-structure-flow">
<h3 id="lesson-1-structure-flow">۳. Structure، Flow، Display و Absolute را جدا بفهم</h3>
<dl class="term-grid">
<dt>Structure</dt><dd>درخت منطقی Parent/Child؛ اینکه کدام Element داخل کدام ظرف قرار گرفته است.</dd>
<dt>Normal Flow</dt><dd>چیدمان طبیعی؛ عنصرها جای خود را اشغال می‌کنند و اگر محتوا بلندتر شود، Parent و عناصر بعدی از آن خبر دارند.</dd>
<dt>Display</dt><dd>Propertyی که رفتار خود عنصر و گاهی رفتار فرزندانش را تعیین می‌کند؛ مثل block، flex، grid یا none.</dd>
<dt>Absolute</dt><dd>Positioningی که عنصر را از Flow خارج می‌کند و با مختصات نسبت به مرجع جای‌گذاری می‌کند.</dd>
</dl>
<p><strong>تفاوت حیاتی:</strong> Display و Flow یکی نیستند. Display دستور است؛ Flow رفتار و بستر چیدمان است. یک Container با <code dir="ltr">display:flex</code> هنوز می‌تواند خودش در Flow صفحه باقی بماند، اما فرزندانش را با قواعد Flex بچیند.</p>
<p><strong>قانون طلایی:</strong> Structure و Content اصلی را در Flow نگه دار؛ Absolute را فقط برای دلیل روشن استفاده کن، مثل Nodeهای اطراف Core یا Decoration کنترل‌شده داخل Stage.</p>
</section>

<section class="concept-reference-part concept-reference-workflow" aria-labelledby="lesson-1-tuva-tree">
<h3 id="lesson-1-tuva-tree">۴. Tree ذهنی TUYA در همین نقطه از دوره</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">TUYA Section
└── TUYA Shell
    ├── Copy Area
    │   ├── Eyebrow / Intro
    │   ├── Heading
    │   ├── Paragraph
    │   ├── Feature List
    │   └── Logo Strip
    └── Visual Area
        └── Visual Stage
            ├── Core Cloud
            └── Orbit Nodes</code></pre>
</figure>
<p>این Tree هنوز به معنای ساخت همهٔ عناصر نیست. در درس ۱ فقط آن را به‌عنوان نقشهٔ تصمیم‌گیری می‌بینی. ساخت واقعی باید در درس‌های بعد، مرحله‌به‌مرحله انجام شود.</p>
</section>

<section class="concept-reference-part concept-reference-units" aria-labelledby="lesson-1-units-context">
<h3 id="lesson-1-units-context">۵. مقدارها و واحدها: هر عددی معنی قطعی ندارد</h3>
<p>واحد <code dir="ltr">%</code> معمولاً نسبت به Parent محاسبه می‌شود، اما <code dir="ltr">VW</code> و <code dir="ltr">VH</code> نسبت به Viewport هستند. بنابراین اگر می‌گویی Width برابر ۵۰٪ است، باید بگویی ۵۰٪ از کدام Parent.</p>
<p>برای ارتفاع‌های سکشن یا Shell، <code dir="ltr">min-height</code> معمولاً از <code dir="ltr">height</code> ثابت مقاوم‌تر است، چون اگر محتوا بلندتر شود، Container می‌تواند رشد کند. <code dir="ltr">height: 40vh</code> ممکن است در Desktop زیبا دیده شود، اما در Mobile یا متن بلند باعث Overflow شود. مقدار قطعی باید در Breakpoint واقعی تست شود.</p>
</section>

<section class="concept-reference-part concept-reference-design-system" aria-labelledby="lesson-1-design-system">
<h3 id="lesson-1-design-system">۶. Variable، Class و Component از یک جنس نیستند</h3>
<div aria-label="مقایسه Variable Class Component" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>تفاوت جنس مفاهیم طراحی سیستم</caption>
<thead><tr><th scope="col">مفهوم</th><th scope="col">جنس</th><th scope="col">فعل درست</th><th scope="col">اشتباه رایج</th></tr></thead>
<tbody>
<tr><th scope="row">Variable</th><td>داده/مقدار نام‌دار</td><td>تعریف و ارجاع</td><td>آن را مثل Element تصور کردن.</td></tr>
<tr><th scope="row">Local Class</th><td>Style محدود به یک Element</td><td>اعمال روی همان Element</td><td>تغییر اختصاصی را Global کردن.</td></tr>
<tr><th scope="row">Global Class</th><td>Style قابل‌استفادهٔ مجدد</td><td>اعمال روی چند Element مشابه</td><td>مختصات اختصاصی یک Node را Global کردن.</td></tr>
<tr><th scope="row">Component</th><td>ساختار تکرارشونده</td><td>قرار دادن / استفاده دوباره</td><td>برای فقط یک رنگ یا Shadow، Component ساختن.</td></tr>
</tbody>
</table>
</div>
<p>قانون یادگیری: «کلاس‌ها ظاهر را تزئین می‌کنند؛ Componentها ساختار را تکرار می‌کنند.»</p>
</section>

<section class="concept-reference-part concept-reference-dom" aria-labelledby="lesson-1-dom-tree">
<h3 id="lesson-1-dom-tree">۷. درخت Elementor همان DOM کامل مرورگر نیست</h3>
<p>Structure panel در Elementor یک نمای طراحی‌شده برای کاربر است. DOM واقعی مرورگر شامل head، script، style، text node، event و stateهای بیشتری است. برای طراح Elementor، Structure panel نقطهٔ شروع خوبی است؛ برای Audit فنی، DevTools لازم می‌شود.</p>
<p>پس در درس ۱ می‌گوییم: «Structure را ببین»، اما ادعا نمی‌کنیم آنچه در Structure می‌بینی کل DOM مرورگر است.</p>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-1-golden">
<h3 id="lesson-1-golden">۸. قوانین طلایی درس</h3>
<ul>
<li><strong>اول Context، بعد تغییر.</strong></li>
<li><strong>اول Parent/Child، بعد Style.</strong></li>
<li><strong>Content اصلی در Flow می‌ماند، مگر خلافش با دلیل روشن ثابت شود.</strong></li>
<li><strong>Overlay باید Stage داشته باشد.</strong></li>
<li><strong>مقدارهای بصری تا پیش از Screenshot/Breakpoint Validation فقط provisional هستند.</strong></li>
<li><strong>تمرین خوب فقط دستور نمی‌دهد؛ وضعیت، دلیل، مسیر UI، هدف، مقدار، واحد و تأیید پایانی دارد.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>این بخش ترکیبی از مستندات رسمی Elementor، اصول CSS، و تجربهٔ پروژهٔ TUYA است. ادعاهای مربوط به V4، Classes، General/Style، Units و Layout باید با Help Center رسمی Elementor و وضعیت واقعی رابط کاربر سنجیده شوند. تشبیه‌های شهر، Stage/Core/Node و مربی مرحله‌به‌مرحله توضیح آموزشی‌اند، نه مستند رسمی.</p>
<ul>
<li><a href="https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/" rel="noopener noreferrer" target="_blank">Elementor — Differences between Editor V3 and V4</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display" rel="noopener noreferrer" target="_blank">MDN — CSS Display</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position" rel="noopener noreferrer" target="_blank">MDN — CSS Position</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-1-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-1-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — تمرین مشاهده و تشخیص، نه ساخت کامل</h3>
<figure class="visual-figure tuya-reference-figure lesson-tuya-reference">
<img alt="تصویر مرجع سکشن TUYA شامل متن و لوگوها در سمت چپ، ابر TUYA و Nodeهای دایره‌ای روی تصویر داخلی خانه در سمت راست" loading="lazy" src="assets/images/tuya-reference.jpg"/>
<figcaption>تصویر مرجع TUYA: سکشن دارای Copy Area، Logo Strip، Visual Stage، Core Cloud، Orbit Nodes و تصویر داخلی خانه است.</figcaption>
</figure>

<aside class="teacher-note" aria-label="قانون تمرین درس یک">
<p><strong>قانون این تمرین:</strong> هنوز هیچ Element یا Style جدید نساز. فقط وضعیت را دسته‌بندی کن، مغایرت با جزوه را ببین، و یک اقدام کوچک بعدی تعریف کن.</p>
</aside>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<p>قبل از هر دستور اجرایی، وضعیت را با سه برچسب جدا کن:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence gate">
<table class="data-table educational-table edu-table">
<caption>نمونهٔ Evidence Gate برای TUYA</caption>
<thead><tr><th scope="col">وضعیت</th><th scope="col">نمونه در این تمرین</th><th scope="col">اجازهٔ اقدام</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>در تصویر مرجع دو ناحیهٔ کلی دیده می‌شود: Copy Area و Visual Area.</td><td>می‌توانی این دو را به‌عنوان Structure اولیه علامت بزنی.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>جای دقیق Nodeها، میزان Shadow، Width نهایی Shell و فاصله‌ها.</td><td>فقط به‌عنوان فرض بصری ثبت کن، نه مقدار نهایی.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>وضعیت واقعی Editor کاربر، Class فعال، Breakpoint فعلی، Content Width سایت.</td><td>بدون Screenshot یا گزارش کاربر، مقدار قطعی نده.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — Screenshot را به چهار گروه تبدیل کن</h3>
<p>تصویر مرجع را باز کن و فقط این چهار گروه را پیدا کن. هنوز عدد نده.</p>
<section class="beginner-explainer beginner-four-groups" data-beginner-concepts="Structure Content Decoration Overlap Flow Overlay Stage Core Node">
<div class="concept-card-grid four-group-cards">

<article class="concept-card" data-concept="Structure">
<h4><span class="term-en" dir="ltr">Structure</span> — اسکلت صفحه</h4>
<ol class="concept-steps">
<li><strong>ساده‌ترین معنی:</strong> جعبه‌ها و رابطهٔ Parent/Child.</li>
<li><strong>در TUYA:</strong> Section، Shell، Copy Area و Visual Area.</li>
<li><strong>در Elementor:</strong> معمولاً Container/Flexbox/Divهایی که بقیه داخلشان قرار می‌گیرند.</li>
<li><strong>اشتباه رایج:</strong> کل Structure را با Absolute ساختن.</li>
<li><strong>تصمیم درست:</strong> Structure در Normal Flow بماند.</li>
</ol>
</article>

<article class="concept-card" data-concept="Content">
<h4><span class="term-en" dir="ltr">Content</span> — محتوای معنی‌دار</h4>
<ol class="concept-steps">
<li><strong>ساده‌ترین معنی:</strong> چیزهایی که کاربر می‌خواند یا با آن تعامل می‌کند.</li>
<li><strong>در TUYA:</strong> Heading، Paragraph، Feature List، Button و Logoها.</li>
<li><strong>در Elementor:</strong> Heading، Text، Button، Image/Logo یا Icon List.</li>
<li><strong>اشتباه رایج:</strong> Content را Absolute کردن.</li>
<li><strong>تصمیم درست:</strong> Content در Flow بماند تا با تغییر متن و موبایل نشکند.</li>
</ol>
</article>

<article class="concept-card" data-concept="Overlap">
<h4><span class="term-en" dir="ltr">Overlap</span> — هم‌پوشانی کنترل‌شده</h4>
<ol class="concept-steps">
<li><strong>ساده‌ترین معنی:</strong> چند چیز عمداً روی هم یا اطراف هم قرار می‌گیرند.</li>
<li><strong>در TUYA:</strong> Core Cloud و Orbit Nodes.</li>
<li><strong>در Elementor:</strong> Visual Stage مرجع می‌شود و Nodeها داخل همان Stage جای‌گذاری می‌شوند.</li>
<li><strong>اشتباه رایج:</strong> چون چند Node روی تصویر دیده می‌شود، کل Section را Absolute کردن.</li>
<li><strong>تصمیم درست:</strong> Overlap فقط داخل Stage.</li>
</ol>
</article>

<article class="concept-card" data-concept="Decoration">
<h4><span class="term-en" dir="ltr">Decoration</span> — تزئین و حس بصری</h4>
<ol class="concept-steps">
<li><strong>ساده‌ترین معنی:</strong> زیبایی اضافه می‌کند، اما پیام اصلی را نمی‌سازد.</li>
<li><strong>در TUYA:</strong> Glow، Shadow، Background و خطوط تزئینی.</li>
<li><strong>در Elementor:</strong> Background، Box Shadow، Effects یا Element تزئینی.</li>
<li><strong>اشتباه رایج:</strong> Decoration را آن‌قدر مهم دیدن که Structure را به‌خاطرش خراب کنی.</li>
<li><strong>تصمیم درست:</strong> Decoration نباید خوانایی و Flow را کنترل کند.</li>
</ol>
</article>

</div>
</section>

<h3>مرحلهٔ ۲ — فقط یک اقدام کوچک بعدی</h3>
<aside class="implementation-step-card" aria-label="فقط یک اقدام کوچک">
<h4>اقدام کوچک پیشنهادی</h4>
<p><strong>هدف:</strong> تمرین تشخیص، نه ساخت.</p>
<p><strong>مسیر:</strong> Screenshot یا تصویر مرجع را نگاه کن → چهار گروه را روی کاغذ یا در ذهن علامت بزن.</p>
<p><strong>Element هدف:</strong> هنوز هیچ Element داخل Elementor انتخاب نمی‌شود.</p>
<p><strong>Class فعال:</strong> هنوز هیچ Class ویرایش نمی‌شود.</p>
<p><strong>Property:</strong> هیچ Property تغییر نمی‌کند.</p>
<p><strong>واحد:</strong> هیچ واحدی وارد نمی‌شود.</p>
<p><strong>نباید تغییر کند:</strong> Content Width، Position، Shadow، Node coordinates، Classها و Structure واقعی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «چهار گروه را جدا کردم: Structure، Content، Overlap و Decoration.»</p>
</aside>

<h3>مرحلهٔ ۳ — اگر وارد Elementor شدی، فقط Structure را بخوان</h3>
<p>اگر این تمرین را کنار Elementor انجام می‌دهی، هنوز چیزی نساز. فقط پنجرهٔ Structure را باز کن و نام‌ها را بخوان. اگر نیاز به تغییر نام بود، این اصلاح ثبت‌شده را رعایت کن:</p>
<aside class="correction-card" aria-label="اصلاح روش تغییر نام در Structure">
<p><strong>اصلاح اجرایی:</strong> تغییر نام عنصر از منوی راست‌کلیک انجام نمی‌شود؛ روی نام عنصر در Structure دوبار کلیک کن.</p>
<p><strong>احتیاط:</strong> این فقط Rename است، نه تغییر Style، نه تغییر Class و نه ساخت Element جدید.</p>
</aside>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>در پروژهٔ TUYA، کدام بخش واقعاً به Overlay نیاز دارد؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-1">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-1-a" name="stop-question-1" type="radio" value="A"/><span>A) ستون متن</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-1-b" name="stop-question-1" type="radio" value="B"/><span>B) کل سکشن</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-1-c" name="stop-question-1" type="radio" value="C"/><span>C) Nodeهای اطراف Core داخل Visual Stage</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل هر گزینه</summary>
<div class="quiz-answer-breakdown">
<p><strong>A غلط است،</strong> چون ستون متن Content اصلی است و باید در Flow بماند.</p>
<p><strong>B غلط است،</strong> چون کل سکشن Stage هم‌پوشانی نیست؛ Section باید Layout اصلی را نگه دارد.</p>
<p><strong>C درست است،</strong> چون Nodeها باید نسبت به Core اطراف آن قرار بگیرند، آن هم داخل محدودهٔ Visual Stage.</p>
</div>
</details>

<h3>🧪 عمداً خرابش کن — روی کاغذ، نه در Editor</h3>
<p>تصور کن همهٔ چیزها Absolute شده‌اند: متن، لوگو، Core و Nodeها. چه می‌شکند؟</p>
<ul>
<li>متن طولانی Parent را بلند نمی‌کند.</li>
<li>Logoها با Visual برخورد می‌کنند.</li>
<li>Mobile با چند Offset جداگانه تعمیر می‌شود.</li>
<li>Parent کوتاه‌تر از محتوای واقعی دیده می‌شود.</li>
</ul>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-1">
<fieldset>
<legend>Checkpoint درس ۱</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-1-1" name="chk-1-1" type="checkbox"/><span>بخش مفهومی را حذف نکرده‌ام؛ فقط دقیق‌تر فهمیده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-1-2" name="chk-1-2" type="checkbox"/><span>می‌توانم Structure، Content، Overlap و Decoration را جدا کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-1-3" name="chk-1-3" type="checkbox"/><span>هنوز مقدار قطعی از Screenshot حدس نزده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-1-4" name="chk-1-4" type="checkbox"/><span>می‌دانم اقدام بعدی باید کوچک، قابل Undo و قابل تأیید باشد.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> پنج نقطهٔ Context را بنویس: Element، Parent، Class، State، Device.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر Border یک Button قرمز است ولی انتظار آبی داری، اولین سه بررسی را به‌ترتیب بنویس.</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی</summary>
<p>پاسخ خوب باید بگوید: اول Element و Parent را بررسی می‌کنم، بعد Class فعال و State/Device را می‌بینم، سپس فقط یک تغییر کوچک قابل Undo انجام می‌دهم.</p>
</details>

</section>
</details>

<details aria-labelledby="lesson-1-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-1-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Hybrid بودن را فقط مشاهده کن</h3>
<p><strong>هدف:</strong> 👁 فقط مشاهده کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">legacy_or_hybrid</code></p>
<p>در پروژه‌های واقعی ممکن است بخشی از صفحه با الگوهای قدیمی‌تر و بخشی با Elementهای V4 ساخته شده باشد. وجود V3/V4 کنار هم به‌تنهایی خطا نیست؛ خطا وقتی است که Scope تغییر، Class فعال یا Parent مسئول چیدمان مبهم بماند.</p>

<h3>🔬 پشت صحنهٔ اختیاری: Elementor Tree، DOM و Render</h3>
<p>Editor در نهایت HTML و CSS تولید می‌کند، اما Structure panel همان DOM کامل مرورگر نیست. برای فهم آموزشی، Structure کافی است؛ برای Audit فنی، DevTools و Computed Style لازم می‌شود.</p>

<h3>✅ تصویر ذهنی درست تا اینجا</h3>
<figure class="visual-figure visual-tree-card">
<figcaption>Tree درست قبل از ادامه</figcaption>
<div class="visual-tree">
<div class="tree-node root">TUYA Section</div>
<div class="tree-branch">
<div class="tree-node main">TUYA Shell <span>Normal Flow</span></div>
<div class="tree-children">
<div class="tree-node copy">Copy Area <span>Content در Flow</span></div>
<div class="tree-node visual">Visual Area <span>Stage برای Overlay</span>
<div class="tree-children nested">
<div class="tree-node core">Core Cloud</div>
<div class="tree-node nodes">Orbit Nodes <span>Overlay کنترل‌شده</span></div>
</div>
</div>
</div>
</div>
</div>
<p class="visual-note">اگر این Tree را بتوانی بدون نگاه‌کردن توضیح بدهی، آمادهٔ درس بعدی هستی.</p>
</figure>
</details>

<details class="lesson-section more-know lesson-disclosure">
<summary class="lesson-disclosure-summary">بیشتر بدانید</summary>
<p><code dir="ltr">display</code> به عنصر رفتار چیدمان می‌دهد. یک Div بدون Display مناسب فقط ظرف خام است؛ وقتی Flex یا Grid می‌شود، قواعد چیدمان فرزندان تغییر می‌کند. اما خود آن Container الزاماً از Flow صفحه خارج نمی‌شود. خروج از Flow معمولاً با Positioning مثل <code dir="ltr">absolute</code> رخ می‌دهد.</p>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-1-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-1-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-4">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-4-1" name="chk-4-1" type="checkbox"/><span>می‌توانم بگویم Context یعنی محدودهٔ اثرگذاری تغییر.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-4-2" name="chk-4-2" type="checkbox"/><span>می‌توانم پنج نقطهٔ بررسی را نام ببرم: Element، Parent، Class، State، Device.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-4-3" name="chk-4-3" type="checkbox"/><span>می‌توانم confirmed، provisional و unknown را از هم جدا کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-5">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-5-1" name="chk-5-1" type="checkbox"/><span>در یک Screenshot، Structure، Content، Overlap و Decoration را جدا می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-5-2" name="chk-5-2" type="checkbox"/><span>قبل از افزودن Element یا Class جدید، فقط یک اقدام کوچک و قابل Undo پیشنهاد می‌دهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-5-3" name="chk-5-3" type="checkbox"/><span>مقدارهای بصری را تا قبل از Validation قطعی معرفی نمی‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-6">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-6-1" name="chk-6-1" type="checkbox"/><span>در سناریوی «Border قرمز است ولی آبی انتظار داشتم» می‌توانم اولین سه بررسی را به‌ترتیب بیان کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-6-2" name="chk-6-2" type="checkbox"/><span>می‌توانم توضیح بدهم چرا Copy Area در Flow می‌ماند ولی Orbit Nodes ممکن است داخل Stage به Overlay نیاز داشته باشند.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-1-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-1-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، Screenshot را به یک Element Tree واقعی تبدیل می‌کنیم. هنوز Style نهایی، Shadow نهایی و مختصات قطعی Nodeها را تعیین نمی‌کنیم.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 1</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-1-completion">
<fieldset>
<legend>ثبت پایان درس 1</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-1-complete" name="lesson-1-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
