<article class="lesson card-surface" data-lesson="19" id="lesson-19">

<h2 class="lesson-title former-h1">درس 19 — Refactor واقعی صفحهٔ Solutions</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-19-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-19-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> یک Refactor واقعی را از Observation تا Verification اجرا کنی؛ یعنی بدون ادعای خرابی اثبات‌نشده، ساختار Cardهای Solutions را قابل نگهداری‌تر کنی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Redesign صفحه، تغییر تجربهٔ کاربر، حذف کور همهٔ Absoluteها، یا ادعای Runtime defect بدون تست واقعی.</p>
<p><strong>در پایان باید بتوانی:</strong> Fact ذخیره‌شده، Refactor پیشنهادی و Defect اثبات‌شده را جدا کنی؛ سپس Cardهایی را که متن‌شان با Offset ثابت Absolute شده‌اند به Flow/Flex/Gap/Padding قابل تست تبدیل کنی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-19-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-19-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🔧 Refactor + 🔍 عیب‌یابی + ⚖ مقایسه</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۴۵–۶۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس باید مثل پروندهٔ forensic اجرا شود. هنرجو نباید بگوید «خراب است» مگر Runtime evidence داشته باشد. باید بگوید «exported fact»، «proposed refactor» یا «confirmed defect».</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_refactor_case_study_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-19-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-19-lesson-understand-4">A. بفهم</h2>

<h3>پروندهٔ اصلی</h3>
<p><code class="inline-code" dir="ltr">CASE-SOL-ABS-001</code></p>
<p>Export نشان می‌دهد در Cardهای Solutions:</p>
<ul>
<li>Parent بعضی Cardها <code dir="ltr">position: relative</code> دارند؛</li>
<li>Iconها می‌توانند به‌عنوان Overlay یا تزئین <code dir="ltr">absolute</code> باشند؛</li>
<li>Heading و Paragraph در برخی الگوها با Offset ثابت <code dir="ltr">absolute</code> شده‌اند؛</li>
<li>Styleها و مقدارهای مشابه در Cardها تکرار شده‌اند.</li>
</ul>

<h3>سه سطح ادعا را قاطی نکن</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>exported fact</dt><dd>چیزی که از Export/DOM/Computed Style واقعاً دیده شده؛ مثل position و offset ذخیره‌شده.</dd>
<dt>proposed refactor</dt><dd>تغییر پیشنهادی برای نگهداری بهتر؛ مثل برگرداندن متن به Normal Flow.</dd>
<dt>confirmed defect</dt><dd>خرابی اثبات‌شده در Runtime؛ مثل overlap در Long Text یا Zoom بعد از تست.</dd>
<dt>unknown</dt><dd>چیزی که بدون Frontend/Runtime هنوز قطعی نیست.</dd>
</dl>
</section>

<h3>تفسیر درست CASE-SOL-ABS-001</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="CASE-SOL-ABS-001 interpretation">
<table class="data-table educational-table edu-table">
<caption>تفسیر evidence در پروندهٔ Solutions</caption>
<thead><tr><th scope="col">مشاهده</th><th scope="col">برچسب</th><th scope="col">نتیجهٔ درست</th></tr></thead>
<tbody>
<tr><th scope="row">Position و offset ذخیره شده‌اند</th><td><code dir="ltr">confirmed</code></td><td>این یک Fact صادرشده است.</td></tr>
<tr><th scope="row">متن عادی با Absolute قرار گرفته</th><td><code dir="ltr">confirmed</code></td><td>کاندید Refactor است.</td></tr>
<tr><th scope="row">متن در Runtime حتماً خراب است</th><td><code dir="ltr">unknown</code></td><td>بدون Long Text/Zoom/Device test ادعا نکن.</td></tr>
<tr><th scope="row">متن به Flow برگردد</th><td><code dir="ltr">provisional_refactor</code></td><td>پیشنهاد قابل تست است، نه حکم نهایی.</td></tr>
</tbody>
</table>
</div>

<h3>Refactor با Redesign فرق دارد</h3>
<p>Refactor یعنی ساختار داخلی را بهتر کنی و رفتار مورد انتظار را حفظ کنی. Redesign یعنی ظاهر، تجربه یا هدف را تغییر دهی. اگر در Solutions هنگام Refactor رنگ، فرم، ترتیب محتوا یا تجربهٔ CTA را تغییر می‌دهی، دیگر فقط Refactor نیست؛ باید دامنهٔ تغییر را جدا ثبت کنی.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Refactor:
  preserve expected behavior
  improve structure
  reduce maintenance risk

Redesign:
  change appearance / experience / content hierarchy</code></pre>
</figure>

<h3>چرا متن معمولاً باید در Flow باشد؟</h3>
<p>Heading و Paragraph محتوای عادی هستند. متن ممکن است بلندتر شود، ترجمه شود، در Zoom بزرگ شود یا در Mobile چندخطی شود. اگر متن با Offset ثابت Absolute شده باشد، Parent معمولاً از ارتفاع واقعی متن خبر ندارد و هر تغییر محتوا می‌تواند به overlap یا خروج از Card منجر شود.</p>

<h3>Icon چه زمانی می‌تواند Absolute بماند؟</h3>
<p>اگر Icon صرفاً تزئینی یا Overlay بصری است، می‌تواند با تصمیم آگاهانه Absolute باقی بماند. اما اگر Icon بخشی از خواندن محتوا، لینک، focus target یا حالت تعاملی است، باید Accessibility و Flow/Focus آن جداگانه بررسی شود.</p>

<h3>Target architecture پیشنهادی</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Solution Card
├── Icon Layer / Icon Item  ← overlay only if justified
└── Card Body              ← normal flow
    ├── Heading
    └── Paragraph</code></pre>
</figure>

<h3>Offset را با Gap/Padding جایگزین کن</h3>
<p>Offset ثابت برای متن، شکل لحظه‌ای Desktop را نگه می‌دارد. Gap و Padding رابطهٔ فضایی را نگه می‌دارند. اگر متن بلند شود، Flow و Gap رفتار طبیعی‌تری دارند.</p>

<h3>قاعدهٔ این درس</h3>
<p>در Refactor، هر تغییر باید یک Baseline، یک تغییر کوچک و یک Verification داشته باشد. تأیید با Screenshot تنها کافی نیست؛ Long Text، Zoom، Desktop/Tablet/Mobile، Keyboard و Accessibility هم باید بررسی شوند.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-19.0.0" id="lesson-19-concept-reference">
<summary>📚 مرجع مفهومی کامل — Refactor؛ تغییر ساختار بدون گم‌کردن رفتار</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="19" data-source-version="tuya-revised-19.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی فعلی درس را حفظ می‌کند و آن را به پروندهٔ Solutions وصل می‌کند. هدف، اجرای Refactor قابل اثبات است؛ نه بازسازی سلیقه‌ای.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-19-ref-problem">
<h3 id="lesson-19-ref-problem">۱. مسئله‌ای که Refactor حل می‌کند</h3>
<p>یک صفحه ممکن است ظاهراً درست باشد، اما پشت آن wrapperهای اضافی، offsetهای ثابت، classهای تکراری، valueهای خام پراکنده، custom CSSهای جبرانی و duplicateهای device-specific وجود داشته باشد. Refactor یعنی ساختار داخلی را بهتر کنی، بدون اینکه رفتار مورد انتظار را ناخواسته بشکنی.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-19-pipes">
<h3 id="lesson-19-pipes">۲. تشبیه لوله‌کشی بدون قطع آب</h3>
<p>خانه کار می‌کند، اما لوله‌ها تکه‌تکه و پیچیده‌اند. Refactor یعنی مسیر لوله را ساده کنی، اتصالات اضافی را حذف کنی و شیرهای مرکزی بسازی؛ درحالی‌که آب همچنان باید به همهٔ اتاق‌ها برسد.</p>
<p>ظاهر یکسان کافی نیست. فشار، ایمنی، دسترسی تعمیر و مسیر بازگشت هم مهم‌اند.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-map">
<h3 id="lesson-19-map">۳. نقشهٔ Refactor</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Refactor map">
<table class="data-table educational-table edu-table">
<caption>نوع مشکل و ابزار Refactor</caption>
<thead><tr><th scope="col">نشانه</th><th scope="col">تحلیل</th><th scope="col">Refactor candidate</th></tr></thead>
<tbody>
<tr><th scope="row">یک رنگ در ۱۸ نقطه</th><td>تکرار مقدار</td><td>Variable candidate</td></tr>
<tr><th scope="row">یک Button Style در چند Element</th><td>تکرار بستهٔ Style</td><td>Global Class candidate</td></tr>
<tr><th scope="row">یک Card Tree در چند جای واقعی</th><td>تکرار Structure</td><td>Component candidate</td></tr>
<tr><th scope="row">Div فقط یک Child دارد و مسئولیت ندارد</th><td>Wrapper مشکوک</td><td>حذف آزمایشی با Baseline</td></tr>
<tr><th scope="row">Text با offset ثابت</th><td>Flow شکسته یا مشکوک</td><td>بازگشت به Flow + Gap/Padding</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-wrapper">
<h3 id="lesson-19-wrapper">۴. Wrapper چه زمانی اضافی نیست؟</h3>
<p>Wrapper ممکن است مسئولیت واقعی داشته باشد:</p>
<ul>
<li>Layout Parent؛</li>
<li>Containing Block؛</li>
<li>Stacking Context؛</li>
<li>Clip/Overflow Stage؛</li>
<li>Background Layer؛</li>
<li>Semantic Group؛</li>
<li>Container Query Context؛</li>
<li>Interaction Target.</li>
</ul>
<p>پس «هر Wrapper کمتر بهتر» قانون ناقصی است. سؤال درست:</p>
<blockquote><p>اگر این Wrapper را حذف کنم، کدام مسئولیت بی‌صاحب می‌شود؟</p></blockquote>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-safe-workflow">
<h3 id="lesson-19-safe-workflow">۵. روش امن Refactor</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Baseline
↓
یک تغییر کوچک
↓
Visual comparison
↓
Responsive comparison
↓
State comparison
↓
Accessibility comparison
↓
Performance / DOM note
↓
Commit / record</code></pre>
</figure>
<p>چند Refactor بزرگ را هم‌زمان انجام نده. اگر Regression رخ دهد، پیدا کردن علت سخت می‌شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-baseline">
<h3 id="lesson-19-baseline">۶. Baseline چیست؟</h3>
<p>قبل از تغییر ثبت کن:</p>
<ul>
<li>Screenshot در Desktop/Tablet/Mobile؛</li>
<li>Long Text نمونه؛</li>
<li>Zoom 200%؛</li>
<li>Computed Style عنصرهای حساس؛</li>
<li>DOM order و class target؛</li>
<li>Keyboard path و Focus؛</li>
<li>Dynamic data cases؛</li>
<li>Metric یا note پایهٔ Performance/DOM.</li>
</ul>
<p>Baseline حافظهٔ قابل اعتماد است؛ ذهن انسان فاصله، ترتیب و رفتار responsive را دقیق نگه نمی‌دارد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-local-global">
<h3 id="lesson-19-local-global">۷. Local به Global</h3>
<p>اگر یک Local Style در چند محل تکرار شده، فقط Copy/Paste نکن. Intent مشترک را پیدا کن.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">بد:
همه سبز و 16px هستند، پس یک Class.

بهتر:
همه Action Link اصلی‌اند، پس action-link-primary.</code></pre>
</figure>
<p>شباهت عددی همیشه به معنای هویت مشترک نیست.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-variant">
<h3 id="lesson-19-variant">۸. Variant Extraction</h3>
<p>اگر چند Card تقریباً یکسان‌اند و فقط Surface، Text Color یا Accent فرق دارد، قبل از ساخت Componentهای جدا، Base + Variant Class را بررسی کن.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">solution-card
solution-card--light
solution-card--dark
solution-card--featured</code></pre>
</figure>
<p>اما Variant را هم زود نساز. باید variation واقعی و تکرارشونده ثابت شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-solutions">
<h3 id="lesson-19-solutions">۹. پروندهٔ Solutions؛ قبل و بعد</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Solutions before after">
<table class="data-table educational-table edu-table">
<caption>Before/After پیشنهادی Solutions</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">قبل</th><th scope="col">بعد پیشنهادی</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Card Parent</th><td>Relative برای offsetها</td><td>Relative فقط اگر overlay/containing block لازم است</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Icon</th><td>Absolute</td><td>Absolute فقط اگر تزئینی/overlay؛ یا Flow item اگر محتوایی</td><td><code dir="ltr">case_by_case</code></td></tr>
<tr><th scope="row">Heading</th><td>Absolute offset</td><td>Normal Flow</td><td><code dir="ltr">proposed_refactor</code></td></tr>
<tr><th scope="row">Paragraph</th><td>Absolute offset</td><td>Normal Flow</td><td><code dir="ltr">proposed_refactor</code></td></tr>
<tr><th scope="row">Spacing</th><td>Offset ثابت</td><td>Padding + Gap</td><td><code dir="ltr">proposed_refactor</code></td></tr>
<tr><th scope="row">Shared Style</th><td>تکرار محلی</td><td>Global Class candidate</td><td><code dir="ltr">provisional_until_reuse_confirmed</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-image-card">
<h3 id="lesson-19-image-card">۱۰. CASE-SOL-IMAGE-001 و Image Cardها</h3>
<p>بعد از Card متنی، Image Cardها را جدا بررسی کن:</p>
<ul>
<li>Height constraint فعلی؛</li>
<li>Aspect Ratio alternative؛</li>
<li>Cover و Object Position؛</li>
<li>Badge overlay؛</li>
<li>Alt و role تصویر؛</li>
<li>Global Card classes؛</li>
<li>Long content و mobile crop.</li>
</ul>
<p>نتیجهٔ نهایی را فقط پس از Runtime ثبت کن. Screenshot تنها کافی نیست.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-19-verification">
<h3 id="lesson-19-verification">۱۱. Verification Matrix</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Refactor verification matrix">
<table class="data-table educational-table edu-table">
<caption>ماتریس تأیید Refactor</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">تست لازم</th><th scope="col">قبولی</th></tr></thead>
<tbody>
<tr><th scope="row">Visual</th><td>Screenshot قبل/بعد</td><td>تفاوت ناخواسته ثبت نشده باشد.</td></tr>
<tr><th scope="row">Content Growth</th><td>Paragraph دو برابر</td><td>Card رشد طبیعی داشته باشد.</td></tr>
<tr><th scope="row">Zoom</th><td>Zoom 200%</td><td>متن و Focus بریده نشوند.</td></tr>
<tr><th scope="row">Responsive</th><td>Desktop/Tablet/Mobile</td><td>Flow و Gap در همه پایدار باشند.</td></tr>
<tr><th scope="row">Accessibility</th><td>Keyboard/Focus/Heading/Alt</td><td>تعامل و خواندن خراب نشود.</td></tr>
<tr><th scope="row">Performance/DOM</th><td>DOM depth و duplicate styles</td><td>ساختار پیچیده‌تر نشده باشد.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-19-traps">
<h3 id="lesson-19-traps">۱۲. اشتباهات رایج</h3>
<ul>
<li>Refactor را فقط با شباهت Screenshot تأیید کردن؛</li>
<li>ادعای Runtime defect بدون تست؛</li>
<li>حذف Wrapper بدون بررسی مسئولیت؛</li>
<li>برگرداندن همهٔ Absoluteها بدون تشخیص overlay/decorative؛</li>
<li>Global Class ساختن فقط به دلیل شباهت عددی؛</li>
<li>Component ساختن قبل از شناخت variationها؛</li>
<li>تغییر هم‌زمان Layout، Typography، Color و Component؛</li>
<li>تست‌نکردن Long Text، Zoom و Mobile.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-19-golden">
<h3 id="lesson-19-golden">۱۳. قوانین طلایی</h3>
<ul>
<li><strong>Refactor بدون Baseline، قابل اثبات نیست.</strong></li>
<li><strong>Fact، proposed refactor و confirmed defect را جدا نگه دار.</strong></li>
<li><strong>متن عادی معمولاً در Flow می‌ماند.</strong></li>
<li><strong>Overlay تزئینی می‌تواند Absolute بماند، اما باید دلیل داشته باشد.</strong></li>
<li><strong>Offset متن را با Gap/Padding قابل رشد جایگزین کن.</strong></li>
<li><strong>یک تغییر کوچک، یک مقایسه، یک ثبت.</strong></li>
<li><strong>شباهت Screenshot کافی نیست؛ Long Text، Zoom و Responsive را تست کن.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>این درس بر پایهٔ export factهای پروندهٔ Solutions، درس‌های Position/Flow/Responsive/State و روش evidence-first نوشته شده است. Runtime defect بدون Frontend test قطعی اعلام نمی‌شود.</p>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-19-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-19-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Offset، Gap، Padding، Class و Variables در Refactor</span>
</summary>
<section aria-labelledby="lesson-19-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در Refactor، واحدها فقط عدد نیستند؛ intent هم مهم است. offset ثابت، gap، padding و variable هرکدام هدف متفاوتی دارند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۹" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">استفادهٔ بهتر</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Text Offset</th><td>top/left/right px/%</td><td>Containing Block</td><td>برای متن عادی معمولاً حذف و Flow</td><td>متن بلند/Zoom را می‌شکند.</td></tr>
<tr><th scope="row">Gap</th><td>length</td><td>Flex/Grid container</td><td>فاصلهٔ بین Childها</td><td>با marginهای پراکنده قاطی شود.</td></tr>
<tr><th scope="row">Padding</th><td>length</td><td>Box داخلی</td><td>فضای داخلی Card</td><td>برای فاصلهٔ بین چند item استفاده شود.</td></tr>
<tr><th scope="row">Card Radius</th><td>length / variable</td><td>Design token</td><td>Variable candidate اگر تکرار واقعی دارد</td><td>Token زودهنگام برای یک مورد.</td></tr>
<tr><th scope="row">Card Style</th><td>class rules</td><td>Global Class</td><td>Global Class candidate اگر Style pack تکرار می‌شود</td><td>Class Explosion.</td></tr>
<tr><th scope="row">Component</th><td>structure</td><td>Pattern reuse</td><td>بعد از شناخت variationها</td><td>Component زودهنگام.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر ۸ Card هرکدام offset متن دارند، کم‌کردن ۱۶ offset به یک Gap/Padding system، نشانهٔ کاهش بدهی ساختاری است؛ اما فقط بعد از مقایسهٔ رفتار تأیید می‌شود.</p></section>
<section><h3>📱 در Responsive</h3><p>قبل و بعد Refactor را در Desktop/Tablet/Mobile و عرض‌های بینابینی تست کن. Flow فقط وقتی موفق است که در عرض‌های واقعی پایدار بماند.</p></section>
<section><h3>🔬 در DevTools</h3><p>Matched rules، computed position، DOM order، flex gap و inherited classها را audit کن. ببین تغییر از کدام Class/State/Device آمده است.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-19-refactor-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Absolute بماند یا Flow شود؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر مورد را اول تصمیم بگیر، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Refactor Step Through">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تصمیم‌های Refactor برای Solutions</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">نقش</th><th scope="col">تصمیم اولیه</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">Paragraph Card</th><td>متن عادی</td><td>Normal Flow</td><td>باید با content رشد کند.</td></tr>
<tr><th scope="row">Heading Card</th><td>عنوان محتوایی</td><td>Normal Flow</td><td>بخشی از خواندن و hierarchy است.</td></tr>
<tr><th scope="row">Icon تزئینی گوشهٔ Card</th><td>Overlay تزئینی</td><td>Absolute candidate</td><td>اگر decorative و غیرتعاملی است.</td></tr>
<tr><th scope="row">Badge کلیک‌پذیر</th><td>Interactive</td><td>case-by-case</td><td>Focus/target/accessibility لازم دارد.</td></tr>
<tr><th scope="row">Spacing بین Heading و Paragraph</th><td>رابطهٔ فضایی</td><td>Gap / margin block</td><td>Offset ثابت نیست.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-19-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-19-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🔧 Refactor مرحله‌ای Solutions</h3>
<p>هدف این Case Study: <strong>بازسازی کن، اما اثبات‌محور</strong>. فقط یک Card را به‌عنوان Pilot انتخاب کن؛ کل صفحه را یک‌باره تغییر نده.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 19">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Refactor</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Export نشان می‌دهد Position/offset برای برخی عناصر ذخیره شده است.</td><td>Fact ثبت شود.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Heading/Paragraph متن عادی هستند.</td><td>Flow candidate قوی.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Icon ممکن است Overlay تزئینی بماند.</td><td>case-by-case تست شود.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Runtime defect قطعی.</td><td>بدون Long Text/Zoom/Device test ادعا نشود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — Baseline بگیر</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس نوزده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> Refactor یک Card، نه کل صفحه.</p>
<p><strong>مسیر:</strong> Staging → Solutions Page → انتخاب یک Card کم‌ریسک → ثبت Baseline → ساخت Card V4 جدید کنار نسخهٔ فعلی.</p>
<p><strong>Element هدف:</strong> فقط یک Solution Card pilot.</p>
<p><strong>Class فعال:</strong> Classهای موجود را مشاهده کن؛ Global Class جدید فقط candidate باشد تا چند Card تأیید شوند.</p>
<p><strong>Property:</strong> Position، Display/Flex, Gap, Padding, Typography, Long Text, Zoom, Responsive.</p>
<p><strong>نباید تغییر کند:</strong> Production، محتوای نهایی صفحه، Design System نهایی، Component نهایی، همهٔ Cardها به‌صورت batch.</p>
<p><strong>عبارت تأیید پایانی:</strong> «یک Card به‌صورت Pilot Refactor شد؛ Fact، پیشنهاد و نتیجهٔ Runtime جدا ثبت شدند.»</p>
</aside>

<h3>مرحلهٔ ۲ — Card جدید را با Flow بساز</h3>
<ol>
<li>از Card فعلی Screenshot بگیر.</li>
<li>یک V4 Card جدید در Staging بساز.</li>
<li>Card را Flexbox Column کن.</li>
<li>Icon را به‌عنوان Overlay یا Item عادی تصمیم‌گیری کن.</li>
<li>Heading و Paragraph را در Normal Flow قرار بده.</li>
<li>Gap و Padding را جایگزین Offsetهای متن کن.</li>
<li>Style مشترک را فقط به‌عنوان Global Class candidate ثبت کن.</li>
<li>Long Text و Zoom را تست کن.</li>
<li>Desktop، Tablet و Mobile را مقایسه کن.</li>
</ol>

<h3>مرحلهٔ ۳ — Compare Table</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Solutions refactor compare table">
<table class="data-table educational-table edu-table">
<caption>جدول مقایسهٔ Card قبل و بعد</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">Before</th><th scope="col">After Pilot</th><th scope="col">Pass/Fail</th></tr></thead>
<tbody>
<tr><th scope="row">Structure</th><td>Text absolute offset</td><td>Text in Flow</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Long Text</th><td>احتمال overlap/overflow</td><td>Card رشد طبیعی؟</td><td><code dir="ltr">pending_runtime</code></td></tr>
<tr><th scope="row">Zoom 200%</th><td>تست نشده</td><td>متن و Focus سالم؟</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Responsive</th><td>Desktop/Tablet/Mobile baseline</td><td>همان یا بهتر؟</td><td><code dir="ltr">pending</code></td></tr>
<tr><th scope="row">Icon</th><td>Absolute</td><td>Overlay تزئینی یا Flow item؟</td><td><code dir="ltr">case_by_case</code></td></tr>
<tr><th scope="row">Style reuse</th><td>تکرار محلی</td><td>Global Class candidate</td><td><code dir="ltr">provisional</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۴ — عمداً خرابش کن</h3>
<p>Paragraph را دو برابر طولانی کن و Font Size را افزایش بده.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Absolute vs Flow expectation">
<table class="data-table educational-table edu-table">
<caption>رفتار مورد انتظار در Long Text</caption>
<thead><tr><th scope="col">نسخه</th><th scope="col">انتظار</th><th scope="col">نتیجهٔ قابل قبول</th></tr></thead>
<tbody>
<tr><th scope="row">Absolute text</th><td>برخورد با Element بعدی، خروج از Card یا نیاز به Offset جدید</td><td>اگر رخ داد: <code dir="ltr">confirmed_defect</code></td></tr>
<tr><th scope="row">Flow text</th><td>Card بلندتر می‌شود و Gap/Padding رابطه را حفظ می‌کنند</td><td>اگر رخ داد: Refactor موفق‌تر است</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۵ — سؤال توقف</h3>
<p>کدام Element احتمالاً می‌تواند Absolute باقی بماند: Icon تزئینی یا Paragraph؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-19">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-19-a" name="stop-question-19" type="radio" value="A"/><span>A) Paragraph، چون جای دقیق‌تری می‌دهد.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-19-b" name="stop-question-19" type="radio" value="B"/><span>B) Icon تزئینی، اگر واقعاً overlay و غیرتعاملی باشد.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-19-c" name="stop-question-19" type="radio" value="C"/><span>C) هر دو، چون Screenshot فعلی درست است.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Paragraph متن عادی است و معمولاً باید در Flow باشد. Icon تزئینی می‌تواند با تصمیم آگاهانه overlay بماند، اگر accessibility و responsive آن بررسی شده باشد.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> Refactor را فقط براساس شباهت Screenshot تأیید کنی.</p>
<p><strong>تست لازم:</strong> Content growth، Keyboard، Zoom، Responsive و Accessibility.</p>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-109">
<fieldset>
<legend>Checkpoint درس ۱۹</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-109-1" name="chk-109-1" type="checkbox"/><span>قبل و بعد ثبت شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-109-2" name="chk-109-2" type="checkbox"/><span>Fact، proposed refactor و confirmed defect جدا شده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-109-3" name="chk-109-3" type="checkbox"/><span>Text در Flow است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-109-4" name="chk-109-4" type="checkbox"/><span>Icon تصمیم آگاهانه دارد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-109-5" name="chk-109-5" type="checkbox"/><span>Style مشترک بدون evidence نهایی Global نشده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-109-6" name="chk-109-6" type="checkbox"/><span>Long Text، Zoom و سه Device Size تست شده‌اند.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> چرا متن عادی معمولاً باید در Flow باشد؟</p>
<p><strong>انتقال به یک موقعیت تازه:</strong> Paragraph کارت دو برابر طولانی شده است. تفاوت رفتار نسخهٔ Absolute و Flow را پیش‌بینی کن.</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ کامل باید Fact صادرشده را از Refactor پیشنهادی و خرابی اثبات‌شده جدا کند، متن عادی را در Normal Flow نگه دارد، و Long Text، Zoom و Device Size را برای اثبات مقایسه کند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-19-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Refactor فقط Desktop نیست</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">required_before_acceptance</code></p>
<ul>
<li>قبل و بعد را در Desktop، Tablet، Mobile و چند عرض بینابینی مقایسه کن.</li>
<li>Paragraph بلند را در Mobile تست کن.</li>
<li>Zoom 200% را تست کن.</li>
<li>اگر Icon overlay است، clipping و focusability آن را بررسی کن.</li>
<li>اگر Style مشترک Global Class candidate شد، Device و State overrideهای ناخواسته را بررسی کن.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-19-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-19-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 CASE-SOL-IMAGE-001 و CASE-SOL-REUSE-001</h3>
<p><strong>هدف:</strong> ⚖️ مقایسه و 🔧 بازسازی</p>
<p>بعد از Card متنی، Image Cardها را بررسی کن:</p>
<ul>
<li>Current height constraints؛</li>
<li>Aspect Ratio alternative؛</li>
<li>Cover و Object Position؛</li>
<li>Global Card classes؛</li>
<li>Badge overlay؛</li>
<li>Alt و role تصویر؛</li>
<li>Long Text در کنار Image؛</li>
<li>Responsive crop.</li>
</ul>
<p>نتیجهٔ نهایی را فقط پس از Runtime ثبت کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>این Refactor نمونهٔ ترکیب Normal Flow، Overlay تزئینی و Global Class است. اگر یکی از این سه اشتباه طبقه‌بندی شود، Refactor ممکن است فقط ظاهر را جابه‌جا کند و بدهی ساختاری جدید بسازد.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-19-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-19-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-111">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-111-1" name="chk-111-1" type="checkbox"/><span>می‌توانم Fact ذخیره‌شده را از Refactor پیشنهادی و خرابی اثبات‌شده جدا کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-111-2" name="chk-111-2" type="checkbox"/><span>می‌توانم توضیح بدهم چرا متن عادی معمولاً باید در Flow باقی بماند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-111-3" name="chk-111-3" type="checkbox"/><span>می‌دانم Icon تزئینی می‌تواند case-by-case Absolute بماند.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-112">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-112-1" name="chk-112-1" type="checkbox"/><span>Cardهای Solutions را با متن در Flex Column و Icon با تصمیم آگاهانه Refactor می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-112-2" name="chk-112-2" type="checkbox"/><span>Long Text، Zoom و سه Device Size را برای قبل و بعد ثبت می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-112-3" name="chk-112-3" type="checkbox"/><span>Global Class candidate را بدون evidence نهایی نمی‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-113">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-113-1" name="chk-113-1" type="checkbox"/><span>در یک Card تازه می‌توانم مشخص کنم کدام Overlay تزئینی و کدام محتوا باید در Flow باشد.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-19-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Solutions Card Pattern</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>آیا Card فقط Style مشترک دارد یا Structure مشترک هم دارد؟</li>
<li>آیا Icon overlay تزئینی است یا محتوایی/تعاملی؟</li>
<li>آیا Heading و Paragraph همیشه در Flow می‌مانند؟</li>
<li>آیا Gap/Padding باید Variable candidate شود؟</li>
<li>آیا Card style باید Global Class candidate شود؟</li>
<li>آیا variationهای Card روشن شده‌اند یا Component زودهنگام است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — فعلاً یک Pilot Card و یک Global Class candidate. Component نهایی فقط بعد از شناخت variationهای واقعی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-19-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-19-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا باید Refactor را با Baseline، تغییر کوچک و Verification انجام داده باشی، نه با حدس یا شباهت Screenshot.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 19</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-19-completion">
<fieldset>
<legend>ثبت پایان درس 19</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-19-complete" name="lesson-19-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
