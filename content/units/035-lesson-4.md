<article class="lesson card-surface" data-lesson="4" id="lesson-4">

<h2 class="lesson-title former-h1">درس 4 — Box Model، Width و پوستهٔ سکشن</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-4-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-4-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> بعد از Context، Tree و Class Scope، پوستهٔ سکشن را با Box Model کنترل کنی: Padding، Margin، Width، Max Width، Min Height و مرجع محاسبهٔ درصدها.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تنظیم نهایی تمام Breakpointها، Shadow/Glow نهایی، Position نهایی Nodeها، یا تعیین قطعی اندازه‌های TUYA از روی Screenshot.</p>
<p><strong>در پایان باید بتوانی:</strong> یک Shell مقاوم بسازی که از صفحه بیرون نزند، محتوای بلند را تحمل کند، و فاصلهٔ داخل/بیرون آن قابل توضیح باشد.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-4-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-4-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧩 ساختاری + 🛠 اجرایی محدود + 📱 Responsive-aware</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۳۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> این درس نباید به حفظ واحدها تبدیل شود. هنرجو باید بفهمد هر مقدار نسبت به چه چیزی محاسبه می‌شود و کدام لایه مسئول فاصلهٔ داخلی، بیرونی و سقف عرض است.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_shell_sizing_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-4-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-4-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس ۱ Context را شناختی. در درس ۲ Tree را ساختی. در درس ۳ Class Scope را کنترل کردی. حالا درس ۴ می‌گوید: وقتی Shell را Style می‌کنی، باید بدانی هر فاصله و اندازه مربوط به کدام لایهٔ Box Model است.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Context
↓
Structure / Tree
↓
Class Scope
↓
Box Model / Width / Shell Sizing</code></pre>
</figure>

<h3>مسئله</h3>
<p>یک Shell ظاهراً ساده می‌تواند سه مشکل بسازد: از صفحه بیرون بزند، در موبایل محتوا را قیچی کند، یا فاصلهٔ داخلی و بیرونی‌اش قابل کنترل نباشد. ریشهٔ این مشکلات معمولاً اشتباه در Padding/Margin/Width/Height است، نه کمبود Style زیبا.</p>

<h3>مدل جعبه</h3>
<details class="more-know ascii-disclosure" open>
<summary>نمای متنی ساده / ASCII</summary>
<figure class="visual-figure ascii-figure">
<figcaption>Box Model در ساده‌ترین شکل</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">MARGIN
  BORDER
    PADDING
      CONTENT</code></pre>
</figure>
</details>

<dl class="term-grid">
<dt>Content</dt><dd>متن، تصویر، دکمه یا Childهای اصلی.</dd>
<dt>Padding</dt><dd>فاصلهٔ داخل خود Element؛ Background معمولاً پشت Padding هم دیده می‌شود.</dd>
<dt>Border</dt><dd>لبهٔ Element.</dd>
<dt>Margin</dt><dd>فاصلهٔ بیرونی Element نسبت به همسایه‌ها؛ Background وارد Margin نمی‌شود.</dd>
<dt>Width</dt><dd>اندازهٔ ترجیحی یا اعلام‌شده؛ بسته به Context و Box Sizing تفسیر می‌شود.</dd>
<dt>Max Width</dt><dd>سقف رشد؛ اجازه نمی‌دهد Shell در صفحه‌های بزرگ بیش از حد عریض شود.</dd>
<dt>Min Height</dt><dd>حداقل ارتفاع؛ اگر محتوا بلندتر شود، Container می‌تواند رشد کند.</dd>
</dl>

<h3>تصمیم سریع</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>فاصله داخل رنگ یا کارت؟</dt><dd>Padding</dd>
<dt>فاصله بین این سکشن و سکشن‌های دیگر؟</dt><dd>Margin یا فاصلهٔ Parent/Section، با احتیاط</dd>
<dt>جلوگیری از خیلی عریض‌شدن؟</dt><dd>Max Width</dd>
<dt>پرکردن فضای والد؟</dt><dd>Width، معمولاً با درصد یا auto، بسته به Parent</dd>
<dt>ارتفاع پایه ولی قابل رشد؟</dt><dd>Min Height، نه Height ثابت</dd>
</dl>
</section>

<h3>درصد یعنی وابستگی به Parent</h3>
<p>اگر برای Width مقدار <code dir="ltr">50%</code> می‌گذاری، باید بپرسی: ۵۰٪ از کدام Parent؟ درصد معمولاً نسبت به فضای Parent محاسبه می‌شود، نه نسبت به کل صفحه. اگر Parent خودش محدود باشد، Child هم در همان محدوده محاسبه می‌شود.</p>
<p>این نکته پایهٔ طراحی Responsive است: Shell می‌تواند نسبت به Parent سیال باشد، اما با Max Width در صفحه‌های بزرگ کنترل شود.</p>

<h3>Height ثابت خطرناک است</h3>
<p><code dir="ltr">height: 40vh</code> یعنی ارتفاع دقیقاً ۴۰٪ Viewport باشد، حتی اگر محتوا بلندتر شود. در Desktop ممکن است خوب دیده شود، اما در موبایل یا متن بلند می‌تواند Overflow بسازد.</p>
<p>برای Shellهای محتوایی، نقطهٔ شروع مقاوم‌تر معمولاً این است:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">height: auto;
min-height: 40vh;</code></pre>
</figure>
<p>این مقدار هنوز «حکم قطعی TUYA» نیست؛ فقط الگوی مقاوم‌تر است و باید در Breakpointها تأیید شود.</p>

<h3>Section، Shell و Main چه فرقی دارند؟</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Section Shell Main">
<table class="data-table educational-table edu-table">
<caption>مسئولیت لایه‌های اندازه و پوسته</caption>
<thead><tr><th scope="col">لایه</th><th scope="col">مسئولیت</th><th scope="col">در این درس</th></tr></thead>
<tbody>
<tr><th scope="row">TUYA Section</th><td>محدودهٔ بیرونی سکشن و فاصله از سکشن‌های دیگر.</td><td>می‌تواند Background عمومی یا spacing بیرونی داشته باشد.</td></tr>
<tr><th scope="row">TUYA Shell</th><td>کارت/پوستهٔ اصلی، Width/Max Width، Padding و Min Height.</td><td>هدف اصلی تمرین.</td></tr>
<tr><th scope="row">TUYA Main</th><td>لایهٔ واسط احتمالی برای جداکردن پوسته از Layout داخلی.</td><td><code dir="ltr">provisional</code>؛ فعلاً فقط اگر مسئولیت جداگانه ثابت شود.</td></tr>
</tbody>
</table>
</div>

<h3>چیزی که فعلاً لازم نیست</h3>
<p>در این درس لازم نیست همهٔ واحدهای CSS را حفظ کنی. باید بتوانی بگویی هر مقدار نسبت به کدام محدوده محاسبه می‌شود و آیا مقدار، محتوا را در Mobile می‌شکند یا نه.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-4.0.0" id="lesson-4-concept-reference">
<summary>📚 مرجع مفهومی کامل — Box Model، Width، Padding، Margin و Shell مقاوم</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="4" data-source-version="tuya-revised-4.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی موجود را حذف نمی‌کند؛ آن را به روند واقعی ساخت TUYA وصل می‌کند. هدف این است که Shell با منطق اندازه و فاصله ساخته شود، نه با عددهای تقلیدی از Screenshot.</p>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-4-house-analogy">
<h3 id="lesson-4-house-analogy">۱. تصویر ذهنی: خانه، دیوار، حیاط</h3>
<p>هر Element را مثل یک خانه ببین:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">┌──────────────────────────┐
│          Margin          │  ← حیاط بیرونی
│   ┌──────────────────┐   │
│   │      Border      │   │  ← دیوار
│   │  ┌────────────┐  │   │
│   │  │  Padding   │  │   │  ← فضای داخل
│   │  │ ┌────────┐ │  │   │
│   │  │ │Content │ │  │   │  ← وسایل خانه
│   │  │ └────────┘ │  │   │
│   │  └────────────┘  │   │
│   └──────────────────┘   │
└──────────────────────────┘</code></pre>
</figure>
<p>اگر وسایل به دیوار چسبیده‌اند، Padding لازم داری. اگر خانه به خانهٔ کناری چسبیده، Margin یا فاصلهٔ Layout لازم داری. اگر خانه از زمین بیرون می‌زند، مسئله Width/Max Width/Box sizing یا Parent است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-4-width-context">
<h3 id="lesson-4-width-context">۲. Width همیشه در Context معنا دارد</h3>
<p>وقتی می‌گویی Shell عرض دارد، باید مشخص کنی:</p>
<ul>
<li>Parent آن چیست؟</li>
<li>Width نسبت به Parent است یا Viewport؟</li>
<li>Padding روی Parent است یا روی خود Shell؟</li>
<li>Max Width سقف رشد را کنترل می‌کند یا نه؟</li>
<li>Box sizing باعث می‌شود Padding به Width اضافه شود یا داخل آن حساب شود؟</li>
</ul>
<p>بنابراین «Width: 100%» به‌تنهایی راه‌حل نیست. اگر هم‌زمان Margin یا Padding اشتباه داشته باشی، ممکن است Overflow بسازی.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-4-percent-vw">
<h3 id="lesson-4-percent-vw">۳. تفاوت Percent با VW</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Percent vs Viewport">
<table class="data-table educational-table edu-table">
<caption>مرجع محاسبهٔ واحدها</caption>
<thead><tr><th scope="col">واحد</th><th scope="col">نسبت به چه چیزی؟</th><th scope="col">کاربرد در Shell</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">%</code></th><td>معمولاً Parent</td><td>عرض سیال داخل محدودهٔ والد.</td><td>فکر کنی همیشه نسبت به کل صفحه است.</td></tr>
<tr><th scope="row"><code dir="ltr">vw</code></th><td>Viewport width</td><td>بخش‌های وابسته به عرض پنجره.</td><td>ممکن است از Parent محدود بیرون بزند.</td></tr>
<tr><th scope="row"><code dir="ltr">vh</code></th><td>Viewport height</td><td>حداقل ارتفاع بصری، با احتیاط.</td><td>Height ثابت با محتوای بلند می‌شکند.</td></tr>
<tr><th scope="row"><code dir="ltr">px</code></th><td>مقدار ثابت</td><td>Border، فاصله‌های کوچک یا محدودیت‌های دقیق.</td><td>برای Layout سیال زیاد و کورکورانه استفاده شود.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-4-padding-margin">
<h3 id="lesson-4-padding-margin">۴. Padding بهتر از Margin برای فاصلهٔ داخلی Shell است</h3>
<p>اگر می‌خواهی محتوای داخل Shell از لبه‌های کارت فاصله داشته باشد، Padding روی Shell یا Parent مناسب‌تر است. Margin بیرونی روی Childهای تمام‌عرض ممکن است باعث شود outer width از Parent بزرگ‌تر شود.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Parent = 1000px
Child width = 100%
Margin left + right = 40px
Outer size = 1040px → احتمال Overflow</code></pre>
</figure>
<p>قانون عملی: فاصلهٔ صفحه و کارت را ترجیحاً با Padding/Max Width کنترل کن، نه با marginهای دوطرفهٔ بی‌محاسبه روی عنصر تمام‌عرض.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-4-minheight">
<h3 id="lesson-4-minheight">۵. Height، Min Height و محتوا</h3>
<p>اگر محتوا پویا است، Height ثابت مثل جعبه‌ای است که اندازهٔ آن تغییر نمی‌کند. Min Height مثل جعبه‌ای است که حداقل اندازه دارد، اما اگر محتوا زیاد شود رشد می‌کند.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Height vs Min Height">
<table class="data-table educational-table edu-table">
<caption>Height و Min Height</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">رفتار</th><th scope="col">خطر</th><th scope="col">کاربرد بهتر</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">height: 40vh</code></th><td>ارتفاع دقیق و ثابت نسبت به Viewport.</td><td>Overflow یا قیچی‌شدن محتوا در Mobile.</td><td>فقط وقتی محتوای ثابت و تست‌شده داری.</td></tr>
<tr><th scope="row"><code dir="ltr">min-height: 40vh</code></th><td>حداقل ارتفاع، ولی قابل رشد با محتوا.</td><td>ممکن است فضای خالی بدهد، اما محتوا را کمتر می‌شکند.</td><td>برای Shell محتوایی مقاوم‌تر است.</td></tr>
<tr><th scope="row"><code dir="ltr">height: auto</code></th><td>ارتفاع بر اساس محتوا.</td><td>ممکن است حس بصری Desktop کوتاه شود.</td><td>با Min Height ترکیب شود.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-4-overflow-debug">
<h3 id="lesson-4-overflow-debug">۶. Debug Overflow: دیده‌شدن و اعمال‌شدن یکی نیستند</h3>
<p>گاهی Margin یا Width اعمال شده، اما نتیجهٔ بصری آن‌طور که انتظار داری دیده نمی‌شود؛ چون outer size از Parent بزرگ‌تر شده یا Overflow توسط Parent/Viewport پنهان شده است.</p>
<p>ترتیب بررسی:</p>
<ol>
<li>Parent واقعی Shell را پیدا کن.</li>
<li>Width، Max Width و Padding را ببین.</li>
<li>Marginهای افقی را بررسی کن.</li>
<li>در DevTools Box Model و Computed Width را نگاه کن.</li>
<li>اگر Full Width کار نمی‌کند، Page Layout و Theme Template را بررسی کن.</li>
</ol>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-4-golden">
<h3 id="lesson-4-golden">۷. قوانین طلایی</h3>
<ul>
<li><strong>Padding فاصلهٔ داخل است؛ Margin فاصلهٔ بیرون.</strong></li>
<li><strong>درصد بدون Parent معنی کامل ندارد.</strong></li>
<li><strong>Max Width سقف رشد Shell است.</strong></li>
<li><strong>Min Height برای محتوای پویا امن‌تر از Height ثابت است.</strong></li>
<li><strong>Margin دوطرفه روی عنصر تمام‌عرض می‌تواند Overflow بسازد.</strong></li>
<li><strong>Full Width داخل Element همیشه محدودیت Theme/Page Layout را نمی‌شکند.</strong></li>
<li><strong>مقدارهای Screenshot تا قبل از تست Responsive فقط provisional هستند.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>توضیح Box Model، width، margin، padding و sizing بر پایهٔ CSS و مستندات رسمی Elementor دربارهٔ اندازه و رفتار Containerها، Full Width و Responsive Editing است. مقدارهای TUYA تا زمان مشاهدهٔ UI واقعی و Breakpoint Validation قطعی نیستند.</p>
<ul>
<li><a href="https://elementor.com/help/set-flexbox-container-size-behavior/" rel="noopener noreferrer" target="_blank">Elementor — Set a Flexbox Container’s size and behavior</a></li>
<li><a href="https://elementor.com/help/full-width-not-working/" rel="noopener noreferrer" target="_blank">Elementor — Full width not working</a></li>
<li><a href="https://elementor.com/help/responsive-editing/" rel="noopener noreferrer" target="_blank">Elementor — Responsive editing</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model" rel="noopener noreferrer" target="_blank">MDN — The box model</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-4-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-4-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Width، Max Width، Padding و Min Height</span>
</summary>
<section aria-labelledby="lesson-4-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در این درس عددها فقط وقتی معنی دارند که مرجع محاسبه روشن باشد: Parent، Viewport، Content یا Border Box.</p>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">واحد رایج</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Width</th><td><code dir="ltr">width</code></td><td>%, px, auto</td><td>بسته به Parent و layout context</td><td>فکر کنی 100% همیشه امن است.</td></tr>
<tr><th scope="row">Max Width</th><td><code dir="ltr">max-width</code></td><td>px, %, rem</td><td>سقف اندازهٔ Element</td><td>بدون Width/Parent درست ممکن است انتظار را کامل نسازد.</td></tr>
<tr><th scope="row">Padding</th><td><code dir="ltr">padding</code></td><td>px, rem, %, clamp</td><td>داخل Element</td><td>با Margin بیرونی اشتباه گرفته شود.</td></tr>
<tr><th scope="row">Margin</th><td><code dir="ltr">margin</code></td><td>px, rem, auto</td><td>بیرون Element</td><td>روی عنصر تمام‌عرض باعث overflow شود.</td></tr>
<tr><th scope="row">Min Height</th><td><code dir="ltr">min-height</code></td><td>vh, px, rem</td><td>حداقل ارتفاع Element</td><td>با height ثابت اشتباه گرفته شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Child برابر 100% Parent باشد و margin افقی هم بگیرد، outer size ممکن است از Parent بزرگ‌تر شود. برای Shell، اول Parent و padding-inline را بررسی کن.</p></section>
<section><h3>📱 در Responsive</h3><p>Height ثابت Desktop را به Mobile منتقل نکن. Min Height و محتوای واقعی را در Breakpoint موبایل بررسی کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>Box Model، Computed width/inline-size، margin، padding و matched CSS rule را ببین. دیده‌نشدن فاصله الزاماً یعنی اعمال‌نشدن Property نیست.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-4-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-4-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Shell sizing، نه طراحی نهایی</h3>
<p>در درس ۲، Tree حداقلی را ساختی. در درس ۳، Class Scope را دیدی. در درس ۴، فقط پوستهٔ TUYA Shell را از نظر Box Model و اندازه کنترل می‌کنی. هنوز Node، Shadow، Glow و Position نهایی نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate درس ۴">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از تنظیم Shell</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Shell باید Copy و Visual را در یک محدودهٔ مشترک نگه دارد.</td><td>Shell هدف اصلی این تمرین است.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Padding برای فاصلهٔ داخلی Shell مناسب است.</td><td>برای تنفس محتوا از Padding استفاده می‌کنیم.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>عددهای دقیق Width، Max Width، Padding و Min Height.</td><td>به‌عنوان مقدار شروع تست می‌شوند، نه حکم قطعی جزوه.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>عرض واقعی صفحه، Theme template، Content Width و Breakpoint فعلی کاربر.</td><td>قبل از عدد قطعی باید UI واقعی بررسی شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط Shell را انتخاب کن</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس چهار">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> کنترل پوسته، نه طراحی کامل سکشن.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → انتخاب <code dir="ltr">TUYA Shell</code> → Style/Layout sizing controls.</p>
<p><strong>Element هدف:</strong> فقط <code dir="ltr">TUYA Shell</code>.</p>
<p><strong>Class فعال:</strong> همان Class محلی Shell یا Candidate ثبت‌شدهٔ Shell؛ Global جدید نساز.</p>
<p><strong>Property:</strong> فقط Width / Max Width / Padding / Min Height.</p>
<p><strong>نباید تغییر کند:</strong> Position، Nodeها، Shadow، Glow، Background نهایی، Typography، Button Style.</p>
<p><strong>عبارت تأیید پایانی:</strong> «Shell از نظر اندازه و فاصلهٔ داخلی کنترل شد؛ هنوز طراحی نهایی انجام نشده است.»</p>
</aside>

<h3>مرحلهٔ ۲ — مقدارهای شروع را به‌عنوان provisional وارد کن</h3>
<p>این مقدارها پیشنهاد شروع‌اند، نه مقدار قطعی جزوه:</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional shell values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع برای Shell</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">مقدار شروع</th><th scope="col">وضعیت</th><th scope="col">چرا؟</th></tr></thead>
<tbody>
<tr><th scope="row">Width</th><td><code dir="ltr">100%</code> یا حالت Auto مناسب UI</td><td><code dir="ltr">provisional</code></td><td>Shell باید فضای Parent را پر کند، اما overflow ندهد.</td></tr>
<tr><th scope="row">Max Width</th><td><code dir="ltr">1200px</code> تا <code dir="ltr">1280px</code> به‌عنوان شروع تست</td><td><code dir="ltr">provisional</code></td><td>در Desktop جلوی عریض‌شدن بیش از حد را می‌گیرد.</td></tr>
<tr><th scope="row">Padding Inline</th><td><code dir="ltr">24px</code> تا <code dir="ltr">32px</code> شروع تست</td><td><code dir="ltr">provisional</code></td><td>فاصلهٔ داخلی از لبهٔ Shell.</td></tr>
<tr><th scope="row">Min Height</th><td><code dir="ltr">40vh</code> به‌عنوان شروع تست</td><td><code dir="ltr">provisional</code></td><td>ارتفاع پایه می‌دهد اما با محتوا قابل رشد است.</td></tr>
<tr><th scope="row">Height</th><td><code dir="ltr">auto</code></td><td><code dir="ltr">recommended_start</code></td><td>محتوای بلند را قیچی نمی‌کند.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — آزمایش Overflow</h3>
<p>بعد از مقداردهی Shell، این سه تست را انجام بده:</p>
<ol>
<li>عرض صفحه را کم کن و ببین Shell از Viewport بیرون می‌زند یا نه.</li>
<li>یک متن بلندتر را ذهنی یا موقتاً تست کن و ببین Height ثابت محتوا را قیچی می‌کند یا نه.</li>
<li>اگر Full Width کار نکرد، قبل از Margin منفی یا CSS اجباری، Page Layout و Theme Template را بررسی کن.</li>
</ol>

<h3>مرحلهٔ ۴ — سؤال توقف</h3>
<p>اگر Shell باید حداقل ۴۰٪ ارتفاع Viewport را داشته باشد اما محتوای بلند هم سالم بماند، انتخاب مقاوم‌تر چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-4">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-4-a" name="stop-question-4" type="radio" value="A"/><span>A) <code dir="ltr">height: 40vh</code></span></label>
<label class="choice-row"><input data-persist="radio" id="radio-4-b" name="stop-question-4" type="radio" value="B"/><span>B) <code dir="ltr">height: auto</code> + <code dir="ltr">min-height: 40vh</code></span></label>
<label class="choice-row"><input data-persist="radio" id="radio-4-c" name="stop-question-4" type="radio" value="C"/><span>C) <code dir="ltr">overflow: hidden</code> برای پنهان‌کردن اضافه‌ها</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Min Height ارتفاع پایه می‌دهد، اما اگر محتوا بلندتر شود، Shell می‌تواند رشد کند. Height ثابت ممکن است در Mobile یا متن بلند Overflow بسازد. Overflow hidden مشکل را پنهان می‌کند، نه حل.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> برای فاصلهٔ چپ و راست Shell، روی Child تمام‌عرض margin افقی بدهی.</p>
<p><strong>نشانه:</strong> در یک سمت فاصله می‌بینی، اما سمت دیگر overflow یا اسکرول افقی ایجاد می‌شود.</p>
<p><strong>قاعده:</strong> فاصلهٔ داخلی Shell را با Padding و سقف عرض را با Max Width کنترل کن؛ margin بیرونی را آگاهانه و محدود استفاده کن.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>این حالت را تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>Outer size خراب‌شده</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Parent: 1000px
Shell width: 100%
Shell margin-left: 32px
Shell margin-right: 32px

Outer size = 1064px → احتمال overflow</code></pre>
</figure>
<p>حالا راه‌حل مقاوم‌تر را بنویس: Padding داخلی یا Parent padding + Max Width، نه margin دوطرفهٔ بی‌محاسبه روی Shell تمام‌عرض.</p>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-19">
<fieldset>
<legend>Checkpoint درس ۴</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-19-1" name="chk-19-1" type="checkbox"/><span>می‌توانم Padding و Margin را با مثال Shell توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-19-2" name="chk-19-2" type="checkbox"/><span>می‌دانم درصد نسبت به Parent معنا دارد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-19-3" name="chk-19-3" type="checkbox"/><span>برای Shell محتوایی، Height ثابت را بدون تست Mobile قطعی نمی‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-19-4" name="chk-19-4" type="checkbox"/><span>هنوز Node، Shadow، Glow و Position نهایی را تغییر نداده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> تفاوت Padding و Margin را روی TUYA Shell توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر یک کارت در موبایل محتوا را قیچی می‌کند، چرا باید Height ثابت را بررسی کنی؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید بگوید Padding داخل کارت است، Margin بیرون کارت؛ درصد نسبت به Parent محاسبه می‌شود؛ و برای محتوای پویا، Min Height معمولاً امن‌تر از Height ثابت است.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-4-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Shell، Width و Height در Mobile</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">verified_and_scoped_method</code></p>
<p>ارتفاع <code dir="ltr">40vh</code> دسکتاپ را بدون بررسی به Mobile منتقل نکن. در Mobile، متن‌ها معمولاً به خطوط بیشتری می‌شکنند و محتوا بلندتر می‌شود. بنابراین Shell باید محتوامحور باشد یا فقط یک <code dir="ltr">min-height</code> کنترل‌شده بگیرد.</p>
<ul>
<li>فاصلهٔ لبهٔ صفحه را با Padding و Max Width کنترل کن.</li>
<li>Width و Min Height را در breakpoint Mobile مستقل بررسی کن.</li>
<li>برای Visual Stage از aspect-ratio و min/max در درس‌های بعد استفاده کن؛ عدد دقیق از Screenshot قطعی نیست.</li>
<li>اگر Full Width کار نکرد، اول Page Layout و Theme Template را بررسی کن.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-4-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-4-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Width اعمال شده ولی نتیجه عجیب است</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: Shell را Full Width کرده‌ای اما هنوز صفحه محدود است یا overflow می‌دهد.</p>
<p>قبل از تغییر عدد جدید، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>Parent واقعی Shell چیست؟</li>
<li>Page Layout چیست؟ Default، Elementor Full Width یا Canvas؟</li>
<li>Theme template محدودیت عرض دارد؟</li>
<li>Width، Max Width، Padding و Margin در Computed چه هستند؟</li>
<li>آیا Child تمام‌عرض margin افقی مثبت دارد؟</li>
<li>آیا Overflow hidden فقط علامت را پنهان کرده است؟</li>
</ul>
</section>
<p>نتیجهٔ درست: اول Parent و محدودیت صفحه را پیدا کن؛ بعد مقدار را تغییر بده.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، Box Model نشان می‌دهد فضای واقعی Element چگونه از Content، Padding، Border و Margin ساخته شده است. اگر در Elementor عددی می‌بینی اما نتیجه متفاوت است، Computed Style می‌تواند نشان دهد مقدار نهایی واقعاً چیست.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-4-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-4-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-22">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-22-1" name="chk-22-1" type="checkbox"/><span>می‌توانم Content، Padding، Border و Margin را توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-22-2" name="chk-22-2" type="checkbox"/><span>می‌دانم درصد بدون Parent معنی کامل ندارد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-22-3" name="chk-22-3" type="checkbox"/><span>می‌دانم Max Width و Min Height چه نقشی در Shell دارند.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-23">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-23-1" name="chk-23-1" type="checkbox"/><span>TUYA Shell را فقط از نظر Width، Max Width، Padding و Min Height تنظیم می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-23-2" name="chk-23-2" type="checkbox"/><span>در صورت Overflow، اول Parent، marginها و Page Layout را بررسی می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-23-3" name="chk-23-3" type="checkbox"/><span>Height ثابت Desktop را بدون Mobile check قطعی نمی‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-24">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-24-1" name="chk-24-1" type="checkbox"/><span>در یک کارت دیگر می‌توانم توضیح بدهم چرا padding داخلی بهتر از margin دوطرفهٔ بی‌محاسبه روی Child تمام‌عرض است.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-4-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-4-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد، روی همین Shell و Tree، وارد Layout/Flow/Display می‌شویم. هنوز نوبت Position نهایی Nodeها و تزئینات بصری نیست.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 4</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-4-completion">
<fieldset>
<legend>ثبت پایان درس 4</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-4-complete" name="lesson-4-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
