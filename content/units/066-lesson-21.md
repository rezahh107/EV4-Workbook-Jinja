<article class="lesson card-surface" data-lesson="21" id="lesson-21">

<h2 class="lesson-title former-h1">درس 21 — Boss Fight — ساخت مستقل و ذهن ساختارمند</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-21-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-21-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> کل زنجیرهٔ V4 را بدون راهنمای خط‌به‌خط اجرا کنی: از مشاهدهٔ Screenshot تا استخراج Structure، انتخاب Element، ساخت Tree، تعیین Class System، Responsive Contract، State/RTL/A11y و Audit نهایی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> کپی‌کردن عددهای Screenshot، ساخت Layout با Offsetهای تصادفی، یا اعلام موفقیت بدون Frontend/DevTools evidence.</p>
<p><strong>در پایان باید بتوانی:</strong> یک Section تازه را با ذهن ساختارمند بسازی، برای هر Wrapper و Class دلیل بدهی، و با Long Content، Mobile، RTL، Zoom، Keyboard و Performance Audit از تصمیم خود دفاع کنی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-21-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-21-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟣 پروژه‌ای / نهایی</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🛠 ساخت مستقل + 🔍 Audit + 🔁 انتقال یادگیری</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰–۳۰ دقیقه</td></tr>
<tr><th scope="row">ساخت و تثبیت</th><td>۹۰–۱۲۰ دقیقه</td></tr>
<tr><th scope="row">Audit و گزارش</th><td>۴۵–۶۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس امتحان نهایی است. پاسخ درست فقط یک Screenshot شبیه نیست؛ پاسخ درست، Structure قابل توضیح، تصمیم‌های قابل دفاع و شواهد تست است.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_boss_fight_final_capstone</code></p>
</section>
</details>

<section aria-labelledby="lesson-21-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-21-lesson-understand-4">A. بفهم</h2>

<h3>مأموریت نهایی</h3>
<p>پروژهٔ TUYA را در یک صفحهٔ تازه و با V4 بازسازی کن. فقط تصویر مرجع و Requirements را داری. خروجی باید با همان DOM در Desktop، Tablet و Mobile کار کند. هر تصمیم باید دلیل، شاهد و وضعیت اعتبار داشته باشد.</p>

<h3>Requirements غیرقابل مذاکره</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Boss Fight requirements">
<table class="data-table educational-table edu-table">
<caption>قوانین پایهٔ Boss Fight</caption>
<thead><tr><th scope="col">Requirement</th><th scope="col">معنی عملی</th><th scope="col">Evidence لازم</th></tr></thead>
<tbody>
<tr><th scope="row">V4 elements only for the new build</th><td>ساخت جدید با منطق V4 انجام شود.</td><td>Tree و Class evidence.</td></tr>
<tr><th scope="row">One DOM for all device sizes</th><td>نسخهٔ جدا برای Desktop/Mobile نساز.</td><td>Responsive audit.</td></tr>
<tr><th scope="row">No absolute positioning for main columns</th><td>Copy و Visual ستون‌های اصلی‌اند؛ در Flow/Flex/Grid می‌مانند.</td><td>Computed position / tree screenshot.</td></tr>
<tr><th scope="row">Absolute only inside visual stage where justified</th><td>فقط Node/Badge/Decorative overlay داخل Stage مجاز است.</td><td>Containing Block + role decision.</td></tr>
<tr><th scope="row">Global classes for repeated styles</th><td>Styleهای واقعاً تکرارشونده Global Class candidate می‌شوند.</td><td>Reuse inventory.</td></tr>
<tr><th scope="row">Local classes only for unique adjustments</th><td>استثناهای خاص Local می‌مانند.</td><td>Promotion rule.</td></tr>
<tr><th scope="row">No horizontal overflow at 320px</th><td>Mobile حداقلی باید بدون scroll افقی کار کند.</td><td>320px screenshot / DevTools.</td></tr>
<tr><th scope="row">RTL review</th><td>Start/End، bidi، code/URL و alignment بررسی شود.</td><td>RTL audit.</td></tr>
<tr><th scope="row">Keyboard/focus review if interactive elements exist</th><td>CTA، link یا Node تعاملی باید focus-visible داشته باشند.</td><td>Keyboard path.</td></tr>
<tr><th scope="row">Zoom 200%</th><td>متن، Focus و Layout نباید بشکنند.</td><td>Zoom test.</td></tr>
<tr><th scope="row">Evidence labels</th><td>نتیجه‌ها با confirmed/provisional/unknown ثبت شوند.</td><td>Final audit report.</td></tr>
</tbody>
</table>
</div>

<h3>چرخهٔ ذهن ساختارمند</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Observe
↓
Separate observation from interpretation
↓
Content Inventory
↓
Group by responsibility
↓
Choose Element / Layout Engine
↓
Build Tree
↓
Add Class / Variable / Candidate Component
↓
Style one responsibility at a time
↓
Test stress cases
↓
Explain with evidence</code></pre>
</figure>

<h3>مشاهده با تفسیر فرق دارد</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Observation vs interpretation">
<table class="data-table educational-table edu-table">
<caption>مشاهده و تفسیر در Boss Fight</caption>
<thead><tr><th scope="col">نوع جمله</th><th scope="col">نمونه</th><th scope="col">برچسب</th></tr></thead>
<tbody>
<tr><th scope="row">Observation</th><td>دو ستون در Screenshot دیده می‌شود.</td><td><code dir="ltr">observed</code></td></tr>
<tr><th scope="row">Interpretation</th><td>احتمالاً Parent اصلی Flex Row است.</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Confirmed</th><td>در Tree، Copy و Visual فرزند مستقیم Shell هستند.</td><td><code dir="ltr">confirmed</code></td></tr>
<tr><th scope="row">Unknown</th><td>Performance نسخهٔ جدید بهتر است.</td><td><code dir="ltr">unknown_until_measured</code></td></tr>
</tbody>
</table>
</div>

<h3>از محتوا شروع کن، نه از Margin</h3>
<p>اگر از Margin، Position و عددهای Screenshot شروع کنی، طرح را تقلید کرده‌ای. اگر از محتوا شروع کنی، Structure قابل دفاع می‌سازی.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Content Inventory:
- Eyebrow
- Heading
- Paragraph
- CTA / Button group
- Logo Strip
- Main Visual
- Core Cloud
- Orbit Nodes
- Decorative layers</code></pre>
</figure>

<h3>Tree هدف برای TUYA</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">TUYA Section
└── TUYA Shell
    ├── Copy Area
    │   ├── Eyebrow
    │   ├── Heading
    │   ├── Paragraph
    │   ├── Actions
    │   └── Logo Strip
    └── Visual Area
        └── Visual Stage
            ├── Core Cloud
            ├── Orbit Nodes
            └── Decorative Layers</code></pre>
</figure>

<h3>Layout Engine را با کمترین ابزار لازم انتخاب کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Layout engine decision">
<table class="data-table educational-table edu-table">
<caption>انتخاب موتور Layout</caption>
<thead><tr><th scope="col">مسئله</th><th scope="col">انتخاب اولیه</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">متن‌های داخل Copy</th><td>Normal Flow / Flex Column</td><td>متن باید با محتوا رشد کند.</td></tr>
<tr><th scope="row">Copy و Visual کنار هم</th><td>Flex Row یا Grid</td><td>رابطهٔ اصلی دو ستون است.</td></tr>
<tr><th scope="row">Logo Strip</th><td>Flex Wrap</td><td>لیست کوچک تکراری است؛ Grid الزاماً لازم نیست.</td></tr>
<tr><th scope="row">Feature Matrix</th><td>Grid candidate</td><td>اگر tracks واقعی دو‌بعدی داریم.</td></tr>
<tr><th scope="row">Orbit Nodes</th><td>Positioned Stage</td><td>Overlay داخل Visual Stage است، نه layout اصلی.</td></tr>
</tbody>
</table>
</div>

<h3>Size Contract قبل از عدد</h3>
<p>برای هر Parent/Child بنویس: عرض نسبت به چیست؟ grow/shrink دارد؟ min/max چیست؟ چه چیزی در Mobile تغییر می‌کند؟</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Shell:
- width/max-width
- padding-inline/block
- gap
- display

Copy:
- basis/grow/shrink
- min-width: 0 when needed
- max text width

Visual:
- basis/grow/shrink
- stage aspect ratio
- max-size

Stage:
- position: relative
- overflow decision
- z-index/layer map candidate</code></pre>
</figure>

<h3>Style System باید کم‌ابهام باشد</h3>
<p>در Boss Fight فقط وقتی چیزی را Global کن که نوع تکرار مشخص باشد. اگر فقط مقدار تکرار شده، Variable candidate؛ اگر بستهٔ Style تکرار شده، Global Class candidate؛ اگر Structure کامل تکرار شده، Component candidate.</p>

<h3>Responsive Contract</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Desktop:
- Shell: Row
- Copy + Visual side-by-side
- Visual Stage full

Tablet:
- Row فشرده یا Column فقط بعد از شکست واقعی
- gap / basis review

Mobile:
- Shell: Column
- Copy first unless UX proves otherwise
- no horizontal overflow at 320px
- Stage simplified if needed
- no duplicate section</code></pre>
</figure>

<h3>Stress Cases نهایی</h3>
<p>ساخت مستقل تا وقتی تحت فشار تست نشده باشد، فقط ظاهر اولیه است. این موارد باید اجرا شوند:</p>
<ul>
<li>Intro / Paragraph را دو برابر طولانی کن.</li>
<li>Logo پنجم اضافه کن.</li>
<li>Font Size را افزایش بده.</li>
<li>Direction را RTL/LTR ذهنی یا واقعی عوض کن.</li>
<li>Preview را 320px کن.</li>
<li>Zoom را 200% کن.</li>
<li>یکی از Nodeها را بزرگ‌تر کن.</li>
<li>اگر Element تعاملی داری، Tab/Focus را تست کن.</li>
</ul>

<h3>انتظار از ساختار سالم</h3>
<ul>
<li>Main Flow حفظ می‌شود.</li>
<li>Copy با متن بلند رشد می‌کند.</li>
<li>Logoها Wrap می‌شوند.</li>
<li>Visual از Parent بیرون نمی‌زند.</li>
<li>Text با Nodeها برخورد نمی‌کند.</li>
<li>Structure و Classها قابل توضیح باقی می‌مانند.</li>
</ul>

<h3>قاعدهٔ نهایی</h3>
<p>اگر تصمیمی را نمی‌توانی توضیح بدهی، هنوز تصمیم نیست؛ حدس است. Boss Fight یعنی تبدیل حدس به تصمیم مستند.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-21.0.0" id="lesson-21-concept-reference">
<summary>📚 مرجع مفهومی کامل — ساخت مستقل؛ از Screenshot به تصمیم قابل دفاع</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="21" data-source-version="tuya-revised-21.0.0">

<p class="concept-reference-lead">این مرجع، درس پایانی را به یک چارچوب اجرایی تبدیل می‌کند: ساخت، تست، دفاع، انتقال. هدف این نیست که فقط TUYA را حفظ کنی؛ هدف این است که برای هر Section تازه همان منطق را اجرا کنی.</p>

<section class="concept-reference-part" aria-labelledby="lesson-21-ref-01">
<h3 id="lesson-21-ref-01">۱. ساخت مستقل یعنی چه؟</h3>
<p>ساخت مستقل یعنی وقتی Screenshot یا Brief تازه می‌بینی، بتوانی آن را به محتوا، گروه، Parent، Layout Engine، Size Contract، Style System، Responsive Contract و Audit تبدیل کنی.</p>
<p>حفظ‌کردن کلیک‌ها کافی نیست. مسیر درست این است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Screenshot → Content → Tree → Layout → Style → Responsive → State → Audit</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-21-ref-02">
<h3 id="lesson-21-ref-02">۲. قالب تصمیم قابل کپی برای هر Section</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Section Name:
Goal:

Content Inventory:
- ...

Tree:
- Parent:
- Children:
- Wrapper responsibilities:

Layout Engine:
- Flow/Flex/Grid/Positioned Stage:
- Why:

Size Contract:
- Parent width/max-width:
- Child basis/grow/shrink:
- Min/Max:
- Gap/Padding:

Style System:
- Local Classes:
- Global Classes:
- Variables:
- Component candidates:

Position/Layering:
- Containing block:
- Absolute items:
- Overflow:
- Layer map:

Responsive Contract:
- Desktop:
- Tablet:
- Mobile:
- Reset/Overrides:

RTL/Bidi:
- dir/lang:
- logical vs physical:
- code/URL isolation:

State/A11y:
- interactive elements:
- focus visible:
- labels/alt:
- keyboard order:

Performance:
- LCP candidate:
- media weight:
- third-party:
- duplicate/hidden content:

Evidence:
- Editor observation:
- DevTools computed:
- screenshots:
- stress tests:</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-21-ref-03">
<h3 id="lesson-21-ref-03">۳. علت‌یابی معکوس</h3>
<p>روی Duplicate امن یک خطا ایجاد کن و مسیر علت را یاد بگیر:</p>
<ul>
<li>Wrapper مسئول را حذف کن.</li>
<li>Direction را عوض کن.</li>
<li>Min Width را بردار.</li>
<li>Overflow Hidden اضافه کن.</li>
<li>Focus Ring را با overflow قطع کن.</li>
<li>Hero image را بدون dimensions رها کن.</li>
</ul>
<p>سپس بپرس:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">اولین نشانهٔ شکست چیست؟
کدام مسئولیت از بین رفت؟
شکست structural است، sizing است، layering است، state است یا media?
کدام شاهد در DevTools آن را تأیید می‌کند؟</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-21-ref-04">
<h3 id="lesson-21-ref-04">۴. Rubric ارزیابی</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Final rubric">
<table class="data-table educational-table edu-table">
<caption>Rubric نهایی Boss Fight</caption>
<thead><tr><th scope="col">حوزه</th><th scope="col">۰ — ضعیف</th><th scope="col">۱ — قابل قبول</th><th scope="col">۲ — قوی</th></tr></thead>
<tbody>
<tr><th scope="row">Structure</th><td>آشفته و وابسته به Screenshot</td><td>قابل استفاده اما با wrapperهای مبهم</td><td>روشن، مسئولیت‌دار و قابل دفاع</td></tr>
<tr><th scope="row">Element choice</th><td>تصادفی</td><td>عمدتاً درست</td><td>با دلیل و شاهد</td></tr>
<tr><th scope="row">Class system</th><td>تکراری و بی‌قانون</td><td>نیمه‌منظم</td><td>Global/Local/Variable روشن</td></tr>
<tr><th scope="row">Responsive</th><td>چند شکست یا Duplicate</td><td>قابل استفاده</td><td>مقاوم، تست‌شده و بدون overflow</td></tr>
<tr><th scope="row">RTL/Bidi</th><td>بررسی نشده</td><td>پایه</td><td>logical/physical و isolation مستند</td></tr>
<tr><th scope="row">Accessibility</th><td>Focus/Alt/Keyboard دیده نشده</td><td>پایه</td><td>تست‌شده و مستند</td></tr>
<tr><th scope="row">Performance</th><td>ادعا بدون evidence</td><td>candidateها ثبت شده‌اند</td><td>Audit چندمحوره و measurement method دارد</td></tr>
<tr><th scope="row">Evidence</th><td>حکم قطعی بدون شاهد</td><td>بخشی از شواهد ثبت شده</td><td>observed/proposed/confirmed تفکیک شده</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-21-ref-traps">
<h3 id="lesson-21-ref-traps">۵. اشتباهات نهایی</h3>
<ul>
<li>شروع از Margin و Position.</li>
<li>کپی Tree بدون فهم مسئولیت.</li>
<li>ساخت Wrapper برای هر Element.</li>
<li>Absolute کردن محتوای اصلی.</li>
<li>Global کردن Class و Variable بدون Intent.</li>
<li>تنظیم Responsive با تقلید عددها.</li>
<li>تست فقط Screenshot اولیه.</li>
<li>نادیده‌گرفتن Dynamic Content.</li>
<li>ادعای موفقیت بدون Frontend و DevTools.</li>
<li>فکرکردن اینکه پایان دوره یعنی پایان Audit.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-21-ref-golden">
<h3 id="lesson-21-ref-golden">۶. قوانین طلایی</h3>
<ul>
<li><strong>از محتوا به Tree برو، از Tree به Layout و از Layout به Style.</strong></li>
<li><strong>هر Wrapper باید مسئولیت قابل توضیح داشته باشد.</strong></li>
<li><strong>مشاهده را با تفسیر قاطی نکن.</strong></li>
<li><strong>Responsive را پیش از عددها به‌صورت قرارداد بنویس.</strong></li>
<li><strong>تصمیمی که شاهد Editor و DevTools ندارد، هنوز تأیید نشده است.</strong></li>
<li><strong>هدف نهایی پیدا کردن دکمه نیست؛ ساختن مدل علت و معلول است.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>این درس جمع‌بندی زنجیرهٔ قبل است. هر خروجی Boss Fight تا زمانی که در Frontend، Device widths، RTL، Zoom، Keyboard و DevTools بررسی نشده باشد، <code dir="ltr">provisional</code> است.</p>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-21-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-21-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Boss Fight؛ هر عدد باید مرجع داشته باشد</span>
</summary>
<section aria-labelledby="lesson-21-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در پروژهٔ مستقل، برای هر مقدار باید بتوانی بگویی: property چیست، واحد نسبت به چیست، چرا این مقدار انتخاب شده، در breakpoint بعد چه می‌شود و شاهد computed آن چیست.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۲۱" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Layout sizing</th><td>width / max / basis</td><td>Parent/root/viewport</td><td>براساس Size Contract</td><td>عدد Screenshot بدون مرجع.</td></tr>
<tr><th scope="row">Spacing</th><td>gap / padding / margin</td><td>رابطه یا context</td><td>Gap/Padding برای روابط پایدار</td><td>Margin برای درمان Tree اشتباه.</td></tr>
<tr><th scope="row">Typography</th><td>font-size / line-height</td><td>root/content/viewport</td><td>خوانایی و scale</td><td>Fluid بدون min/max.</td></tr>
<tr><th scope="row">Position</th><td>relative / absolute / inset</td><td>Containing Block</td><td>فقط در Stage یا overlay موجه</td><td>Absolute برای main content.</td></tr>
<tr><th scope="row">State</th><td>hover/focus/active</td><td>interaction context</td><td>Focus visible و target قابل استفاده</td><td>Hover-only.</td></tr>
<tr><th scope="row">Performance</th><td>time/bytes/nodes</td><td>measurement method</td><td>Audit candidate</td><td>Benchmark قطعی بدون شرایط.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-21-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-21-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏁 Boss Fight — ساخت مستقل TUYA</h3>
<p>این تمرین راهنمای کلیک‌به‌کلیک ندارد. فقط Checkpoint دارد. تو باید تصمیم‌ها را بسازی و بعد دفاع کنی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 21">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از Boss Fight</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Boss Fight جمع‌بندی همهٔ درس‌هاست.</td><td>همهٔ حوزه‌ها باید audit شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Main columns نباید Absolute شوند.</td><td>Flow/Flex/Grid برای layout اصلی.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>مقادیر دقیق gap، basis، stage size، node offsets.</td><td>با stress test تثبیت می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>Performance واقعی، Dynamic content نهایی، interaction نهایی.</td><td>بدون اندازه‌گیری قطعی نشود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Checkpointها</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس بیست و یک">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> ساخت مستقل همراه با گزارش تصمیم.</p>
<p><strong>مسیر:</strong> صفحهٔ تازه → Build with V4 → Document decisions → Frontend/DevTools verification.</p>
<p><strong>Element هدف:</strong> کل TUYA Section.</p>
<p><strong>Class فعال:</strong> Local/Global/Variable/Component candidate را با دلیل ثبت کن.</p>
<p><strong>Property:</strong> Tree، Layout، Size، Style، Position، Responsive، RTL، State، Performance candidates.</p>
<p><strong>نباید تغییر کند:</strong> ساخت Duplicate برای Mobile، Absolute برای متن/ستون اصلی، Global کردن بدون reuse evidence، ادعای Performance بدون measurement.</p>
<p><strong>عبارت تأیید پایانی:</strong> «TUYA مستقل ساخته شد؛ هر تصمیم کلیدی با مشاهده، دلیل و تست ثبت شد.»</p>
</aside>

<h3>مرحلهٔ ۲ — Checkpoint ساخت</h3>
<ol>
<li>Shell ساخته شد و مسئولیتش روشن است.</li>
<li>Main Layout با Copy و Visual ساخته شد؛ main columns در Flow هستند.</li>
<li>Copy Content در Flow است.</li>
<li>Logo Strip با Wrap و Gap کنترل می‌شود.</li>
<li>Visual Stage مرجع Position است.</li>
<li>Core + Cloud role مشخص دارد.</li>
<li>Nodes فقط در Stage و با دلیل Absolute هستند.</li>
<li>Responsive Contract نوشته شده است.</li>
<li>RTL + Bidi review انجام شده است.</li>
<li>State + Keyboard review برای interactive items انجام شده است.</li>
<li>Performance Audit Card نوشته شده است.</li>
</ol>

<h3>مرحلهٔ ۳ — تست تخریبی نهایی</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Final destructive tests">
<table class="data-table educational-table edu-table">
<caption>تست‌های تخریبی نهایی</caption>
<thead><tr><th scope="col">تست</th><th scope="col">انتظار از ساختار سالم</th><th scope="col">Evidence</th></tr></thead>
<tbody>
<tr><th scope="row">Intro دو برابر</th><td>Copy رشد می‌کند و Stage برخورد نمی‌کند.</td><td>Screenshot + computed height</td></tr>
<tr><th scope="row">Logo پنجم</th><td>Logo Strip wrap می‌شود.</td><td>Frontend screenshot</td></tr>
<tr><th scope="row">Font size بزرگ‌تر</th><td>متن clipped/overlap نمی‌شود.</td><td>Zoom/font stress</td></tr>
<tr><th scope="row">RTL/LTR ذهنی یا واقعی</th><td>Start/End و bidi قابل دفاع‌اند.</td><td>RTL audit</td></tr>
<tr><th scope="row">320px</th><td>horizontal overflow وجود ندارد.</td><td>DevTools width</td></tr>
<tr><th scope="row">Zoom 200%</th><td>Focus و متن بریده نمی‌شوند.</td><td>Zoom screenshot</td></tr>
<tr><th scope="row">Node بزرگ‌تر</th><td>Visual Stage کنترل را حفظ می‌کند.</td><td>Stage overflow/layer audit</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۴ — Final Audit Report</h3>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code">Final Boss Fight Report:
1. Section goal
2. Content inventory
3. Tree and wrapper responsibilities
4. Layout engine decisions
5. Size contract
6. Class/Variable/Component candidates
7. Position/Layering decisions
8. Responsive contract
9. RTL/Bidi review
10. State/A11y review
11. Performance audit candidates
12. Stress test results
13. confirmed/provisional/unknown table
14. Known limitations
15. Next refactor candidates</code></pre>
</figure>

<h3>سؤال توقف نهایی</h3>
<p>اگر Layout در Mobile خراب شد، آیا اول باید Element جدید بسازی؟</p>
<details class="disclosure-card">
<summary>پاسخ</summary>
<p>نه. ابتدا Element، Parent، Class target، Device Size، State و یک Property مشکوک را بررسی کن. Element جدید آخرین واکنش است، نه اولین واکنش.</p>
</details>

<h3>⚠️ تلهٔ نهایی</h3>
<p><strong>تله:</strong> برای رسیدن سریع به Screenshot، تصمیم‌هایی بسازی که نتوانی توضیح بدهی.</p>
<p><strong>قاعده:</strong> هر Element، Class، Value و Override باید یک دلیل قابل بیان و حداقل یک شاهد داشته باشد.</p>

<h3>Checkpoint نهایی</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-120-revised">
<fieldset>
<legend>Checkpoint نهایی</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-120r-1" name="chk-120r-1" type="checkbox"/><span>Tree را بدون نگاه‌کردن به راهنما می‌کشم و مسئولیت هر Wrapper را می‌گویم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-120r-2" name="chk-120r-2" type="checkbox"/><span>دلیل Flex/Grid/Flow/Positioned Stage را توضیح می‌دهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-120r-3" name="chk-120r-3" type="checkbox"/><span>Classها و Variableها مسئولیت روشن دارند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-120r-4" name="chk-120r-4" type="checkbox"/><span>Mobile، RTL، Zoom، Long Content و Keyboard تست شده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-120r-5" name="chk-120r-5" type="checkbox"/><span>مشکلات را با مسیر ثابت debug می‌کنم، نه با حدس.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-120r-6" name="chk-120r-6" type="checkbox"/><span>می‌توانم همین منطق را روی Section تازه منتقل کنم.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — پایان مسیر</h3>
<p><strong>بازیابی کوتاه:</strong> چرخهٔ ذهن ساختارمند را از حفظ بنویس.</p>
<p><strong>انتقال به یک موقعیت تازه:</strong> برای یک Section جدید «متن + تصویر محصول»، سه تصمیمی را بنویس که از TUYA منتقل می‌کنی و یک تصمیمی که باید تغییر کند.</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب لازم نیست طولانی باشد؛ باید نشان بدهد چه چیزی را بررسی می‌کنی، چرا، چگونه می‌سازی، و با چه evidence نتیجه را تأیید می‌کنی.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-21-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Boss Fight</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">required_before_completion</code></p>
<ul>
<li>Desktop، Tablet، Mobile، 320px و عرض‌های بینابینی تست شوند.</li>
<li>هیچ Section جدا برای Mobile ساخته نشود.</li>
<li>Main columns در Flow بمانند.</li>
<li>Node offsetها با Stage و Responsive Contract بازبینی شوند.</li>
<li>Long Text و Logo overflow بررسی شوند.</li>
<li>Zoom 200% و Keyboard/Focus اگر interactive داریم، اجباری‌اند.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-21-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-21-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — انتقال یادگیری</summary>
<h3>ایستگاه پایانی</h3>
<p>همان منطق را روی یک طرح دیگر اجرا کن:</p>
<figure class="visual-figure structure-content-examples">
<figcaption>نمونه‌های انتقال</figcaption>
<div class="visual-card-grid">
<div class="visual-box">متن + تصویر محصول</div>
<div class="visual-box">لیست خدمات + نمودار آماری</div>
<div class="visual-box">معرفی تیم + عکس گروهی</div>
</div>
</figure>
<p>اگر فقط TUYA را کپی کنی، Pattern را حفظ کرده‌ای. اگر همان تصمیم‌ها را روی طرح جدید توضیح بدهی و تفاوت‌ها را تشخیص بدهی، مفهوم را فهمیده‌ای.</p>
<h3>🔬 پشت صحنه</h3>
<p>موفقیت این دوره با تعداد Propertyهای حفظ‌شده سنجیده نمی‌شود؛ با کیفیت تصمیم، ساختار، Debugging، Evidence و قابلیت انتقال سنجیده می‌شود.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-21-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-21-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای پایان این مسیر، سطح ۱ و ۲ اجباری‌اند. سطح ۳ یعنی یادگیری به پروژهٔ تازه منتقل شده است.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-123-revised">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-123r-1" name="chk-123r-1" type="checkbox"/><span>چرخهٔ Observe → Decompose → Choose → Build → Test → Explain را اجرا می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-123r-2" name="chk-123r-2" type="checkbox"/><span>تفاوت کپی Screenshot و بازسازی ساختارمند را توضیح می‌دهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-123r-3" name="chk-123r-3" type="checkbox"/><span>مشاهده، تفسیر، پیشنهاد و نتیجهٔ تأییدشده را جدا ثبت می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-124-revised">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-124r-1" name="chk-124r-1" type="checkbox"/><span>TUYA را در صفحه‌ای تازه با V4 و بدون راهنمای خط‌به‌خط بازسازی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-124r-2" name="chk-124r-2" type="checkbox"/><span>Mobile، RTL، Zoom، Long Content، Keyboard و Class System را مستند تست می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-124r-3" name="chk-124r-3" type="checkbox"/><span>Final Audit Report با confirmed/provisional/unknown می‌نویسم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-125-revised">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-125r-1" name="chk-125r-1" type="checkbox"/><span>همان تصمیم‌ها را روی یک Section تازه اجرا می‌کنم و تفاوت‌های لازم را توضیح می‌دهم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-21-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Capstone governance</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>کدام تصمیم از TUYA قابل انتقال است و کدام وابسته به همین طرح است؟</li>
<li>کدام Class واقعاً Global است و کدام Local می‌ماند؟</li>
<li>کدام Variable candidate به usage واقعی نیاز دارد؟</li>
<li>کدام Component candidate هنوز variationهای نامعلوم دارد؟</li>
<li>کدام Performance Budget فقط candidate است؟</li>
<li>کدام نتیجه با DevTools تأیید شده و کدام هنوز proposed است؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — پایان دوره به معنی نهایی‌شدن سیستم نیست. پایان دوره یعنی اکنون می‌توانی سیستم را با evidence رشد بدهی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-21-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-21-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>این درس ایستگاه پایانی مسیر آموزشی است. از اینجا پروژه‌های واقعی تو تمرین‌های بعدی‌اند: مشاهده، تصمیم، ساخت، تست، دفاع.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 21</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-21-completion">
<fieldset>
<legend>ثبت پایان درس 21</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-21-complete" name="lesson-21-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
