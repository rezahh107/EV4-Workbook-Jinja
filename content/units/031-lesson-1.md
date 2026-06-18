<article class="lesson card-surface" data-lesson="1" id="lesson-1"><h2 class="lesson-title former-h1">درس 1 — V4 چگونه فکر می‌کند؟</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-1-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-1-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> تفاوت نگاه V4 با کلیک‌کردن تصادفی و نقش General، Style و Class را.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام تنظیمات Editor یا CSS را.</p><p><strong>در پایان باید بتوانی:</strong> قبل از تغییر ظاهر، Element، کلاس هدف ویرایش، State و Device را بررسی کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-1-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-1-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟢 سبک</td></tr><tr><th scope="row">نوع فعالیت</th><td>👁 مشاهده‌ای + 🧠 مفهومی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۱۰–۱۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۱۰–۱۵ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۰–۱۵ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> برای شروع آرام و ساختن مسیر بررسی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-1-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-1-lesson-understand-4">A. بفهم</h2><h3>مسئله</h3><p>در Editor یک Element را انتخاب می‌کنی، چند گزینه را تغییر می‌دهی، اما نمی‌دانی تغییر روی همان عنصر، Class مشترک یا Mobile اعمال شده است.</p><h3>🧠 مدل ذهنی چهار سؤال</h3><section aria-labelledby="section-hidden-31-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-31-heading">بخش آموزشی</h2><ul><li>1. چه Elementی انتخاب شده؟</li>
<li>2. چه Classی فعال است؟</li>
<li>3. در چه Stateی هستم؟</li>
<li>4. در چه Device Sizeی هستم؟</li></ul></section><h3>General و Style</h3><section aria-labelledby="section-hidden-32-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-32-heading">بخش آموزشی</h2><dl class="term-grid"><dt>General</dt><dd>این Element چیست و چه محتوایی دارد؟</dd><dt>Style</dt><dd>این Element چگونه نمایش داده می‌شود؟</dd></dl></section><h3>مثال ساده</h3><p>یک Button را انتخاب کن:</p><ul>
<li>در General متن و Link را می‌بینی؛</li>
<li>در Style ظاهر و Layout را می‌بینی؛</li>
<li>در Classes مشخص می‌کنی کدام بستهٔ Style ویرایش شود؛</li>
<li>در State می‌توانی Normal، Hover یا Focus را ویرایش کنی.</li>
</ul><h3>چیزی که فعلاً لازم نیست</h3><p>نیازی نیست Syntax CSS یا تمام منطق Cascade را حفظ کنی. فقط بدان تغییر همیشه در یک <strong>Context</strong> انجام می‌شود.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="84aa70716f22693de3c93db3897b3801fddb897155546f158dcd41bf607e789a" id="lesson-1-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Elementor V4؛ واقعاً چگونه فکر می‌کند؟</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="1" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-01-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-01-section-01">مسئله‌ای که این مفهوم حل می‌کند</h3><p>مبتدی معمولاً Elementor را مجموعه‌ای از دکمه‌ها می‌بیند:</p><ul>
<li>اینجا رنگ را عوض کن.</li>
<li>آنجا فاصله بده.</li>
<li>این گزینه را روی Row بگذار.</li>
<li>اگر درست نشد، Margin اضافه کن.</li>
</ul><p>این روش ممکن است یک صفحه را ظاهراً درست کند، اما ذهن طراح را وابسته به آزمون‌وخطا نگه می‌دارد. با اضافه‌شدن هر Element جدید یا تغییر اندازهٔ صفحه، دوباره همه‌چیز مبهم می‌شود.</p><p>مشکل اصلی کمبود کنترل نیست؛ <strong>نبودن مدل ذهنی</strong> است.</p><hr/></section><section aria-labelledby="concept-v31-01-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-01-section-02">تشبیه به دنیای واقعی: ساختن یک شهر</h3><p>Elementor V4 را مثل ساختن یک شهر تصور کن:</p><ul>
<li><strong>Element</strong> = ساختمان، تابلو، پل یا فضای سبز</li>
<li><strong>Element Tree</strong> = نقشهٔ خیابان‌ها و رابطهٔ محله‌ها</li>
<li><strong>Display و Layout</strong> = قانون حرکت و نحوهٔ توزیع فضا</li>
<li><strong>Class</strong> = آیین‌نامهٔ ظاهری یک گروه از ساختمان‌ها</li>
<li><strong>Variable</strong> = دفتر مرکزی مقادیر مشترک، مثل رنگ رسمی یا فاصلهٔ استاندارد</li>
<li><strong>Component</strong> = ساختمانی با نقشهٔ مادر که در چند محله تکرار می‌شود</li>
<li><strong>State</strong> = وضعیت موقتی یک بخش هنگام تعامل</li>
<li><strong>Responsive Rule</strong> = مقررات شهر برای زمین‌های کوچک‌تر</li>
</ul><p>اگر فقط نمای ساختمان را رنگ کنی اما خیابان اشتباه باشد، شهر درست کار نمی‌کند.</p><hr/></section><section aria-labelledby="concept-v31-01-section-03" class="concept-reference-part concept-reference-definition"><h3 id="concept-v31-01-section-03">تعریف دقیق با زبان ساده</h3><p>مدل فکری درست در V4 این ترتیب را دارد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">معنا و نقش
↓
ساختار و رابطهٔ Parent/Child
↓
موتور چیدمان
↓
اندازه و فاصله
↓
Style و State
↓
قواعد قابل‌استفادهٔ مجدد
↓
Responsive و آزمون نهایی
</code></pre></figure><p>یعنی قبل از اینکه بپرسی «چه رنگی باشد؟» باید بپرسی:</p><blockquote>
<p>این Element چیست و چرا در این نقطه از Tree قرار گرفته است؟</p>
</blockquote><p>Elementor V4 استفاده از Elementهای اتمیک، پنل Style استانداردتر و ویرایش Classمحور را پررنگ کرده است. در مستندات رسمی، هر Element حداقل یک Local Class دارد و Styleهای قابل‌استفادهٔ مجدد می‌توانند در Global Classها نگه‌داری شوند.</p><hr/></section><section aria-labelledby="concept-v31-01-section-04" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-01-section-04">چرا V4 به این سمت طراحی شده است؟</h3><p>در یک سایت کوچک، تغییر دستی ده دکمه شاید قابل تحمل باشد. در یک سایت واقعی با ده‌ها صفحه، این روش سه مشکل می‌سازد:</p><ol>
<li><strong>عدم یکنواختی:</strong> هر دکمه کمی با دیگری فرق می‌کند.</li>
<li><strong>هزینهٔ تغییر:</strong> تغییر برند باید در ده‌ها نقطه انجام شود.</li>
<li><strong>ابهام در خطا:</strong> معلوم نیست Style از کجا آمده است.</li>
</ol><p>V4 می‌خواهد تصمیم‌ها از حالت «تنظیم پراکنده» به «سیستم قابل ردیابی» نزدیک شوند.</p><hr/></section><section aria-labelledby="concept-v31-01-section-05" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-01-section-05">رفتار را قدم‌به‌قدم دنبال کن</h3><p>فرض کن باید یک Hero بسازی.</p><h4>مرحلهٔ ۱: نقش‌ها را جدا کن</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Hero Shell
├── Copy Group
│   ├── Eyebrow
│   ├── Heading
│   ├── Paragraph
│   └── Actions
└── Visual Group
    └── Image
</code></pre></figure><p>هنوز رنگ و Padding مهم نیست. ابتدا باید معلوم شود هر چیز چه نقشی دارد.</p><h4>مرحلهٔ ۲: Parent مشترک را درست کن</h4><p>Copy و Visual باید کنار هم قرار بگیرند؛ پس Parent آن‌ها باید موتور چیدمان مناسبی داشته باشد.</p><h4>مرحلهٔ ۳: موتور چیدمان را انتخاب کن</h4><p>برای دو گروه کنار هم معمولاً Flex Row کافی است. اگر جای‌گذاری دقیق در چند ردیف و ستون لازم باشد، Grid بررسی می‌شود.</p><h4>مرحلهٔ ۴: اندازه و فاصله را تعریف کن</h4><p>ابتدا Width/Basis و سپس Gap/Padding. Margin نباید جای ساختار اشتباه را بگیرد.</p><h4>مرحلهٔ ۵: Style را در محل درست قرار بده</h4><ul>
<li>استثنای یک Element → Local Class</li>
<li>الگوی تکراری → Global Class</li>
<li>مقدار مشترک → Variable</li>
<li>ساختار تکراری چندعنصری → Component</li>
</ul><h4>مرحلهٔ ۶: Responsive Contract را تعیین کن</h4><p>مثلاً:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Desktop: Row، تصویر 45٪
Tablet: Row فشرده یا Column
Mobile: Column، متن و دکمه تمام‌عرض
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-01-section-06" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-01-section-06">در Elementor V4</h3><p>وقتی Element را انتخاب می‌کنی، به‌جای حرکت تصادفی میان کنترل‌ها، این پرسش‌ها را به‌ترتیب پاسخ بده:</p><ol>
<li>این Element محتوایی است یا فقط Wrapper؟</li>
<li>Parent آن چیست؟</li>
<li>Display و Layout Parent چه هستند؟</li>
<li>کدام Class را ویرایش می‌کنم؟</li>
<li>مقدار Literal است یا باید Variable باشد؟</li>
<li>این تغییر در Breakpointهای دیگر چه اثری دارد؟</li>
</ol><hr/></section><section aria-labelledby="concept-v31-01-section-07" class="concept-reference-part"><h3 id="concept-v31-01-section-07">مدل ذهنی نهایی فصل</h3><p>هر بار که وارد Editor می‌شوی، این زنجیره را در ذهن مرور کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">محتوا چه معنایی دارد؟
↓
درخت درست آن چیست؟
↓
کدام Parent مسئول چیدمان است؟
↓
Flex، Grid یا Flow عادی؟
↓
اندازه و فاصله چگونه مذاکره می‌شوند؟
↓
این تصمیم Local است، Global است، Variable است یا Component؟
↓
در Stateها و Breakpointها چه تغییری می‌کند؟
↓
در DevTools واقعاً چه CSSای تولید شده است؟
</code></pre></figure><p>در V3 بیشتر وسوسه می‌شوی هر Widget را جداگانه تنظیم کنی. در V4 باید بیشتر به «سیستم» فکر کنی: Element اتمیک، Parent، Class، Variable، Component و منبع Style. این مقایسه مطلق نیست—V3 نیز Container و Global Setting دارد و V3/V4 می‌توانند کنار هم باشند—اما برای تغییر عادت ذهنی مفید است.</p></section><section aria-labelledby="concept-v31-01-section-08" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-01-section-08">بزرگ‌ترین اشتباه مبتدی‌ها</h3><p>مبتدی نتیجهٔ بصری را می‌بیند و مستقیم سراغ Style می‌رود.</p><p>مثلاً برای کنار هم بردن دو عنصر:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Margin-left: 180px
</code></pre></figure><p>اما مسئلهٔ واقعی شاید این باشد که Parent باید Flex Row و <code class="inline-code" dir="ltr">justify-content: space-between</code> باشد.</p><p>Style نمی‌تواند ساختار اشتباه را سالم کند؛ فقط آن را پنهان می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-01-section-09" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-01-section-09">روش تشخیص سریع</h3><p>وقتی چیزی درست نیست، این ترتیب را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Tree → Parent → Display → Size → Spacing → Position → Style → State
</code></pre></figure><p>نه برعکس.</p><hr/></section><section aria-labelledby="concept-v31-01-section-10" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-01-section-10">قوانین طلایی</h3><ul>
<li><strong>«در V4 اول نقش را انتخاب کن، بعد Element را.»</strong></li>
<li><strong>«ساختار قبل از Style می‌آید.»</strong></li>
<li><strong>«هر مشکلی که با Margin عجیب حل شده، احتمالاً یک سؤال ساختاریِ حل‌نشده پشت خود دارد.»</strong></li>
<li><strong>«Class بستهٔ رفتار ظاهری است؛ Variable فقط یک مقدار نام‌دار است.»</strong></li>
<li><strong>«Component برای تکرار ساختار است، نه فقط تکرار رنگ.»</strong></li>
<li><strong>«پنل‌ها ابزارند؛ مدل ذهنی، روش تصمیم‌گیری است.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Get started with the Elementor Editor V4</li>
<li>Elementor Help: Differences between Editor 3.x and V4</li>
<li>Elementor Help: Classes in Elementor</li>
<li>CSS Display Module</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-1-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-1-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — نوع مقدار در V4؛ همه‌چیز واحد طول نیست</span></summary>
<section aria-labelledby="lesson-1-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">در Editor V4 بعضی کنترل‌ها طول می‌گیرند، بعضی keyword، بعضی عدد بدون واحد و بعضی reference به Class یا Variable. پیش از واردکردن عدد باید نوع مقدار را بشناسی.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> پنل Elementor مثل یک فرم اداری است: هر فیلد نوع خودش را دارد. در فیلد «نام» متر وارد نمی‌کنی؛ در فیلد «زمان» هم درصد نمی‌نویسی.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Display / Layout</th><td><code dir="ltr">display</code></td><td>Block, Flex, Inline-block, None</td><td>keyword</td><td>برای تعیین رفتار layout؛ واحد طول ندارد.</td><td>از px یا % برای کنترل keyword استفاده نکن.</td><td><code dir="ltr">E_LAYOUT</code></td></tr><tr><th scope="row">Size</th><td><code dir="ltr">width / height / min / max</code></td><td>طول، درصد، auto یا کنترل‌های رابط</td><td>وابسته به Property</td><td>بعد از مشخص‌شدن ساختار انتخاب شود.</td><td>عدد پنل همیشه اندازهٔ نهایی Computed نیست.</td><td><code dir="ltr">E_SIZE</code></td></tr><tr><th scope="row">Classes</th><td><code dir="ltr">class binding</code></td><td>نام/Reference</td><td>بدون واحد</td><td>برای scope و reuse Style.</td><td>Class و Variable را با «عدد» یکی نگیر.</td><td><code dir="ltr">E_CLASSES</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>not_applicable — این درس دربارهٔ تشخیص نوع کنترل است، نه محاسبهٔ طول.</p></section>
<section><h3>📱 در Responsive</h3><p>هر Control ممکن است responsive یا غیرresponsive باشد؛ وجود عدد به‌تنهایی responsive بودن را ثابت نمی‌کند.</p></section>
<section><h3>🔬 در DevTools</h3><p>در Styles و Computed ببین مقدار نهایی keyword است، length است یا reference resolveشده.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/" rel="noopener noreferrer" target="_blank">Elementor — Differences between Editor V3 and V4</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a>، <a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Layout</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-1-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-1-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — فقط مشاهده</h3>
<figure class="visual-figure tuya-reference-figure lesson-tuya-reference">
<img alt="تصویر مرجع سکشن TUYA شامل متن و لوگوها در سمت چپ، ابر TUYA و nodeهای دایره‌ای روی تصویر داخلی خانه در سمت راست" loading="lazy" src="assets/images/tuya-reference.jpg"/>
<figcaption>تصویر مرجع نسخه 20: سکشن TUYA با Copy Area، Logo Strip، Visual Stage، Core Cloud، Orbit Nodes و تصویر داخلی خانه.</figcaption>
</figure>
<p>تصویر مرجع را باز کن و هنوز چیزی نساز.</p><p>چهار گروه را علامت بزن:</p><section aria-labelledby="section-hidden-34-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-34-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Structure</dt><dd>پوسته و دو ناحیهٔ اصلی</dd><dt>Content</dt><dd>متن، ویژگی‌ها و Logoها</dd><dt>Overlap</dt><dd>Core و Nodeها</dd><dt>Decoration</dt><dd>Background، Shadow و Glow</dd></dl></section><h3>👁 نقشهٔ دیداری چهار گروه</h3><section class="beginner-explainer beginner-four-groups" data-beginner-concepts="Structure Content Decoration Overlap Flow Overlay Stage Core Node">
<h4>اول معنی واژه‌ها را ساده کن؛ بعد نمودار را ببین</h4>
<p>در این بخش هنوز لازم نیست همهٔ اصطلاحات Elementor را حفظ کنی. فقط باید بفهمی هر چیز در Screenshot، «اسکلت»، «محتوا»، «تزئین» یا «هم‌پوشانی کنترل‌شده» است.</p>
<div class="concept-card-grid four-group-cards">
<article class="concept-card" data-concept="Structure">
<h4><span class="term-en" dir="ltr">Structure</span> — اسکلت صفحه</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Structure یعنی جعبه‌ها، ستون‌ها و چیدمان اصلی صفحه؛ همان چیزی که بقیهٔ اجزا داخل آن قرار می‌گیرند.</li>
<li><strong>۲. مثال روزمره:</strong> Structure = اسکلت ساختمان؛ اگر اسکلت کج باشد، دیوار و وسایل هم درست نمی‌نشینند.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> در پروژهٔ TUYA یعنی سکشن اصلی، ستون متن و ناحیهٔ Visual.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> معمولاً ظرف والد یا Section اصلی، ظرف‌های داخلی Copy Area و Visual Area، و تنظیمات Layout مثل Flex یا Grid.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> همهٔ اسکلت صفحه را با Position Absolute می‌سازم چون در Screenshot دقیق به نظر می‌رسد.</li>
<li><strong>۶. تصمیم درست:</strong> Structure را در Normal Flow نگه دار؛ فقط اگر دلیل خیلی روشن داری از Absolute استفاده کن.</li>
<li><strong>۷. تمرین کوچک:</strong> در Screenshot با انگشت فقط جعبه‌های بزرگ را پیدا کن؛ هنوز به Glow و Node نگاه نکن.</li>
</ol>
</article>
<article class="concept-card" data-concept="Content">
<h4><span class="term-en" dir="ltr">Content</span> — چیزهایی که معنی دارند</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Content یعنی متن‌ها، دکمه‌ها، لوگوها و چیزهایی که کاربر می‌خواند یا با آن‌ها تعامل می‌کند.</li>
<li><strong>۲. مثال روزمره:</strong> Content = وسایل داخل اتاق؛ اگر تعداد وسایل بیشتر شود، اتاق باید بتواند جا بدهد.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> در پروژه یعنی عنوان، پاراگراف، لیست ویژگی‌ها، دکمه‌ها و لوگوها.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Widgetهای Heading، Text Editor، Button، Icon List، Image یا Logo داخل Copy Area.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> متن و لوگو را Absolute می‌کنم؛ بعد وقتی متن طولانی شد همه‌چیز روی هم می‌افتد.</li>
<li><strong>۶. تصمیم درست:</strong> Content معمولاً باید در Flow بماند تا Parent قد محتوا را بفهمد.</li>
<li><strong>۷. تمرین کوچک:</strong> یک پاراگراف را دو برابر طولانی‌تر تصور کن؛ آیا Layout هنوز سالم می‌ماند؟</li>
</ol>
</article>
<article class="concept-card" data-concept="Decoration">
<h4><span class="term-en" dir="ltr">Decoration</span> — چیزهای تزئینی</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Decoration یعنی چیزی که زیبایی اضافه می‌کند اما اگر حذف شود معنی صفحه از بین نمی‌رود.</li>
<li><strong>۲. مثال روزمره:</strong> Decoration = رنگ دیوار و نورپردازی؛ نبودنش ساختمان را خراب نمی‌کند، فقط حسش را ساده‌تر می‌کند.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> در پروژه یعنی Glow، Shadow، Background، خطوط تزئینی و هاله‌های پشت Visual.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Background، Box Shadow، Pseudo-element، یا یک Decorative Element با aria-hidden در صورت نیاز.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> تزئین را مثل Content مهم می‌بینم و برای آن ساختار اصلی صفحه را خراب می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> Decoration را پشت یا اطراف محتوا نگه دار و اجازه نده خوانایی و Flow را کنترل کند.</li>
<li><strong>۷. تمرین کوچک:</strong> یک Glow را ذهنی حذف کن؛ اگر پیام صفحه هنوز فهمیده می‌شود، آن بخش Decoration است.</li>
</ol>
</article>
<article class="concept-card" data-concept="Overlap">
<h4><span class="term-en" dir="ltr">Overlap</span> — هم‌پوشانی کنترل‌شده</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Overlap یعنی چند چیز عمداً روی هم یا اطراف هم قرار می‌گیرند؛ نه اینکه کل صفحه از Flow خارج شود.</li>
<li><strong>۲. مثال روزمره:</strong> Overlap = برچسب‌هایی که روی یک پوستر چسبانده‌ای؛ پوستر هنوز اندازهٔ خودش را دارد.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> در این پروژه فقط Core و Nodeهای اطراف آن واقعاً Overlap لازم دارند.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> یک Visual Stage با position: relative و Nodeهای داخل همان Stage؛ نه کل Section.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> چون Nodeها روی Core دیده می‌شوند، کل سکشن، متن، لوگو و دکمه را Absolute می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> Overlap را داخل Stage کوچک و قابل کنترل انجام بده؛ بقیهٔ صفحه در Flow بماند.</li>
<li><strong>۷. تمرین کوچک:</strong> با خودت بگو: «اگر این قسمت روی هم نیفتد، طرح از نظر آموزشی خراب می‌شود یا فقط کمی متفاوت می‌شود؟»</li>
</ol>
</article>
</div>
<dl class="term-translation"><dt dir="ltr">Structure</dt><dd>اسکلت و جعبه‌بندی اصلی</dd>
<dt dir="ltr">Content</dt><dd>چیزی که کاربر می‌خواند یا با آن تعامل می‌کند</dd>
<dt dir="ltr">Decoration</dt><dd>چیزی که فقط زیبایی اضافه می‌کند</dd>
<dt dir="ltr">Overlap</dt><dd>چیزی که عمداً روی چیز دیگر یا اطراف آن قرار می‌گیرد</dd>
<dt dir="ltr">Normal Flow</dt><dd>چیدمان عادی مرورگر؛ عنصرها یکی بعد از دیگری جا می‌گیرند</dd>
<dt dir="ltr">Overlay</dt><dd>قرار دادن کنترل‌شدهٔ یک چیز روی چیز دیگر</dd>
<dt dir="ltr">Stage</dt><dd>ناحیهٔ کنترل‌شده‌ای که Overlay فقط داخل آن اتفاق می‌افتد</dd>
<dt dir="ltr">Core</dt><dd>مرکز Visual که Nodeها نسبت به آن چیده می‌شوند</dd>
<dt dir="ltr">Node</dt><dd>نقطه یا آیتم کوچک اطراف Core</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note"><strong>چرا؟</strong> اگر این سه سؤال را جواب ندهی، احتمالاً Screenshot را به Offsetهای تصادفی تبدیل می‌کنی.</p>
</aside><aside aria-label="یادداشت رنگ و خوانایی" class="smart-note-card palette-note-card"><h4>یادداشت رنگ در این نسخه</h4><p>سطح‌های تیره کمی به سمت Slate/Near-black رفته‌اند تا عمق دارک مود بهتر شود؛ آبی کنترل‌شده فقط برای نشانه‌های تعاملی و اطلاعاتی استفاده می‌شود و جای طلایی اصلی جزوه را نمی‌گیرد.</p></aside>
<aside aria-label="اشتباه رایج رضا" class="common-confusion-card">
<h4>اشتباه رایج رضا در این بخش</h4>
<p>فکر می‌کنم چون در Screenshot چند چیز روی هم دیده می‌شوند، پس کل سکشن باید Absolute باشد.</p>
<p><strong>درستش این است:</strong> فقط همان قسمت کوچک که واقعاً روی هم می‌افتد Overlay می‌شود؛ بقیه در Flow می‌ماند.</p>
</aside>
<figure aria-label="توضیح مرحله‌ای چهار گروه دیداری" class="visual-figure beginner-staged-map">
<figcaption>نقشهٔ دیداری چهار گروه — مرحله‌به‌مرحله، نه یک‌باره</figcaption>
<div class="staged-visual-steps">
<article class="stage-step-card">
<span class="step-badge">Step 1</span>
<h4>اول فقط دو ناحیه را ببین</h4>
<div class="mini-layout two-areas"><span>ستون متن</span><span>ناحیه Visual</span></div>
<p class="why-note">چرا؟ چون قبل از هر Style باید بدانی صفحه چند ناحیهٔ اصلی دارد.</p>
</article>
<article class="stage-step-card">
<span class="step-badge">Step 2</span>
<h4>حالا معنی محتوا را ببین</h4>
<div class="mini-layout content-areas"><span>متن + ویژگی‌ها + لوگوها</span><span>Core و Nodeها</span></div>
<p class="why-note">متن و لوگو باید بتوانند زیاد یا کم شوند؛ پس معمولاً در Flow می‌مانند.</p>
</article>
<article class="stage-step-card">
<span class="step-badge">Step 3</span>
<h4>فقط داخل Visual هم‌پوشانی داریم</h4>
<div class="mini-layout overlap-areas"><span>متن در Flow می‌ماند</span><span>Nodeها دور Core می‌چرخند</span></div>
<p class="why-note">Overlay فقط در محدودهٔ Stage امن است، نه روی کل سکشن.</p>
</article>
<article class="stage-step-card">
<span class="step-badge">Step 4</span>
<h4>Decoration لایهٔ زیبایی است</h4>
<div class="mini-layout decoration-layer"><span>Background / Glow / Shadow پشت همه</span></div>
<p class="why-note">اگر Decoration حذف شود، معنا باقی می‌ماند؛ پس نباید اسکلت را کنترل کند.</p>
</article>
</div>
</figure>
</section><h3>👁 Flow در برابر Overlap</h3><section class="beginner-explainer flow-overlap-explainer" data-beginner-concepts="Normal Flow Overlap Absolute Stage">
<h4>تفاوت Flow و Overlap با زبان خیلی ساده</h4>
<div class="plain-language-pair">
<article class="plain-card good-flow-card">
<h4><span dir="ltr">Flow</span> یعنی صف منظم</h4>
<p>Flow یعنی عنصرها مثل آدم‌های صف، یکی بعد از دیگری جا می‌گیرند. اگر یکی بلندتر شود، بقیه را هل می‌دهد و Parent هم بلندتر می‌شود.</p>
</article>
<article class="plain-card controlled-overlap-card">
<h4><span dir="ltr">Overlap</span> یعنی روی‌هم‌افتادن عمدی</h4>
<p>Overlap یعنی عنصرها عمداً روی هم یا اطراف هم قرار می‌گیرند. اینجا مرورگر دیگر مثل صف رفتار نمی‌کند؛ باید Stage و محدوده داشته باشی.</p>
</article>
</div>
<div class="comparison-card-grid">
<article class="comparison-card good">
<h4>نمونهٔ خوب Flow — ستون متن</h4>
<ul>
<li>Title</li>
<li>Paragraph</li>
<li>Feature list</li>
<li>Logos</li>
</ul>
<p><strong>اگر Paragraph طولانی شود:</strong> ستون بلندتر می‌شود، Parent هم بلندتر می‌شود و Mobile کمتر می‌شکند.</p>
</article>
<article class="comparison-card good">
<h4>نمونهٔ Overlap کنترل‌شده — Visual Stage</h4>
<ul>
<li>Core در وسط</li>
<li>Nodeها اطراف Core</li>
<li>همه داخل Visual Area</li>
<li>نه روی کل Section</li>
</ul>
<p><strong>تصمیم درست:</strong> Visual Stage را کنترل کن؛ Copy Area را در Flow نگه دار.</p>
</article>
<article class="comparison-card bad">
<h4>نمونهٔ بد Overlap — همه‌چیز Absolute</h4>
<ul>
<li>Text، Logo، Core و Nodeها همگی Absolute می‌شوند.</li>
<li>Parent قد محتوا را نمی‌فهمد.</li>
<li>Mobile با Offsetهای زیاد و شکننده تعمیر می‌شود.</li>
</ul>
<p><strong>علامت خطر:</strong> اگر برای هر تغییر متن چند عدد top/right جدید می‌نویسی، Layout را اشتباه فهمیده‌ای.</p>
</article>
</div>
<figure class="visual-figure visual-flow-overlap">
<figcaption>کدام بخش باید Overlay شود؟</figcaption>
<div class="visual-flow-grid">
<div class="visual-flow-column">
<div class="visual-label">Normal Flow</div>
<div class="visual-flow-row">
<div class="visual-box visual-copy">ستون متن<br/><span>متن طولانی Parent را بلند می‌کند</span></div>
<div class="visual-box visual-stage-box">ناحیهٔ Visual<br/><span>Stage مخصوص هم‌پوشانی</span></div>
</div>
</div>
<div class="visual-overlap-diagram">
<div class="visual-label">Overlap فقط اینجاست</div>
<div class="orbit">
<span class="orbit-node top">Node</span>
<span class="orbit-node right">Node</span>
<span class="orbit-node bottom">Node</span>
<span class="orbit-node left">Node</span>
<span class="orbit-core">Core</span>
</div>
</div>
</div>
<p class="visual-note">قانون: اگر عنصر محتوای اصلی است، اول آن را در Flow نگه دار. اگر تزئینی یا شناور است، بعداً Overlay را بررسی کن.</p>
</figure>
</section><h3>❓ قبل از ادامه</h3><p>کدام بخش واقعاً به هم‌پوشانی نیاز دارد؟</p><form class="interactive-form stop-question-form" data-persist-group="stop-question-1"><fieldset><legend>چک‌لیست یادگیری</legend><label class="choice-row"><input data-persist="radio" id="radio-1-a" name="stop-question-1" type="radio" value="A"/><span>A) ستون متن</span></label><label class="choice-row"><input data-persist="radio" id="radio-1-b" name="stop-question-1" type="radio" value="B"/><span>B) کل سکشن</span></label><label class="choice-row"><input data-persist="radio" id="radio-1-c" name="stop-question-1" type="radio" value="C"/><span>C) Nodeهای اطراف Core</span></label></fieldset></form><details class="disclosure-card"><summary>پاسخ با دلیل هر گزینه</summary>
<div class="quiz-answer-breakdown">
<p><strong>A غلط است،</strong> چون ستون متن Content اصلی است و باید در Flow بماند. اگر متن طولانی شود، باید Parent را بلند کند.</p>
<p><strong>B غلط است،</strong> چون کل سکشن Stage هم‌پوشانی نیست؛ سکشن باید Layout اصلی را نگه دارد.</p>
<p><strong>C درست است،</strong> چون Nodeها باید نسبت به Core اطراف آن قرار بگیرند، پس فقط این بخش Overlay لازم دارد.</p>
</div>
<aside aria-label="چطور در Elementor تصمیم بگیرم؟" class="elementor-decision-card">
<h4>چطور در Elementor تصمیم بگیرم؟</h4>
<ul>
<li>اگر متن، دکمه یا لوگو است → اول Flow</li>
<li>اگر تزئین یا Node اطراف یک Core است → احتمالاً Overlay</li>
<li>اگر کل سکشن را Absolute می‌کنی → احتمالاً داری اشتباه می‌روی</li>
</ul>
</aside></details><h3>👁 تله را تصویری ببین</h3><section class="beginner-explainer screenshot-trap-explainer" data-beginner-concepts="Parent Absolute Coordinates Flow">
<h4>تلهٔ تبدیل Screenshot به مختصات یعنی چه؟</h4>
<p>تله یعنی به‌جای اینکه بپرسی «این عنصر داخل چه Parentی است؟»، فقط می‌پرسی «چند پیکسل از بالا و چپ فاصله دارد؟»</p>
<div class="comparison-card-grid">
<article class="comparison-card bad bad-thinking-card">
<h4>فکر اشتباه مبتدی</h4>
<dl class="coordinate-list">
<dt>Text</dt><dd><code dir="ltr">top:80</code></dd>
<dt>Feature</dt><dd><code dir="ltr">top:180</code></dd>
<dt>Logo</dt><dd><code dir="ltr">top:330</code></dd>
<dt>Core</dt><dd><code dir="ltr">right:80</code></dd>
<dt>Node</dt><dd><code dir="ltr">right:230</code></dd>
</dl>
<p>این یعنی من Layout را نفهمیده‌ام؛ فقط دارم ظاهر عکس را با عدد تقلید می‌کنم.</p>
</article>
<article class="comparison-card good good-thinking-tree">
<h4>فکر درست قبل از ساخت</h4>
<div aria-label="ساختار درست Section، Main Layout، Copy Area و Visual Stage" class="html-tree-diagram" role="img">
<span>Section</span>
<span>↳ Main Layout</span>
<span>↳ Copy Area: Text / Feature list / Logos</span>
<span>↳ Visual Area</span>
<span>↳ Visual Stage: Core + Nodes</span>
</div>
<p>اول Parentها را پیدا کن؛ بعد جای دقیق را با Flex/Grid/Stage بساز.</p>
</article>
</div>
<figure class="visual-figure visual-danger-card">
<figcaption>تلهٔ خطرناک: تبدیل Screenshot به مختصات</figcaption>
<div class="bad-absolute-layout">
<div class="bad-section-label">Section</div>
<div class="bad-chip bad-text">Text<br/><span>top:80 / left:60</span></div>
<div class="bad-chip bad-feature">Feature<br/><span>top:180 / left:60</span></div>
<div class="bad-chip bad-logo">Logo<br/><span>top:330 / left:60</span></div>
<div class="bad-chip bad-core">Core<br/><span>top:90 / right:80</span></div>
<div class="bad-chip bad-node">Node<br/><span>top:20 / right:230</span></div>
</div>
</figure>
<aside aria-label="نشانه‌های دیباگ" class="debug-signs-card">
<h4>Debug signs — از کجا بفهمم در تله افتاده‌ام؟</h4>
<ul>
<li>اگر با تغییر متن همه‌چیز برخورد کرد → احتمالاً Content را Absolute کرده‌ای.</li>
<li>اگر موبایل با ۱۰ Offset جدید درست می‌شود → احتمالاً Structure را اشتباه ساخته‌ای.</li>
<li>اگر Parent کوتاه‌تر از محتواست → احتمالاً عناصر اصلی از Flow خارج شده‌اند.</li>
</ul>
</aside>
</section><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> ظاهر Screenshot را مستقیماً به مختصات تبدیل کنی.</p><p><strong>نشانه:</strong> می‌خواهی برای همه‌چیز Absolute و Offset بنویسی.</p><p><strong>اولین اصلاح:</strong> ابتدا Parent/Child و Flow را تشخیص بده.</p><h3>🧪 عمداً خرابش کن</h3><p>هنوز در پروژه چیزی نساز. روی کاغذ همهٔ عناصر را Absolute تصور کن.</p><h3>👁 آزمایش خراب‌شده روی کاغذ</h3><figure class="visual-figure visual-break-test"><figcaption>اگر همه‌چیز Absolute شود چه می‌شکند؟</figcaption>
<div class="break-panels">
<div class="break-panel">
<div class="break-title">متن طولانی‌تر می‌شود</div>
<div class="break-section">
<div class="break-text">Text خیلی طولانی‌تر می‌شود...</div>
<div class="break-collision">برخورد با Feature / Logo / Visual</div>
</div>
</div>
<div class="break-panel">
<div class="break-title">Mobile می‌شود</div>
<div class="break-mobile">
<div>Text absolute</div>
<div>Logos absolute</div>
<div>Core absolute</div>
<div class="break-out">Nodeها بیرون می‌زنند</div>
</div>
</div>
</div>
</figure><h4>👀 انتظار داری ببینی</h4><ul>
<li>متن طولانی Parent را بلند نمی‌کند؛</li>
<li>Mobile به Offsetهای جدید نیاز دارد؛</li>
<li>تغییر Font باعث برخورد عناصر می‌شود.</li>
</ul><h3>Checkpoint</h3><section aria-labelledby="section-hidden-35-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-35-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-1"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-1-1" name="chk-1-1" type="checkbox"/><span>Structure از Decoration جدا شده</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-1-2" name="chk-1-2" type="checkbox"/><span>هنوز مقدار دقیق از Screenshot حدس نزده‌ام</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-1-3" name="chk-1-3" type="checkbox"/><span>می‌دانم کدام بخش باید در Flow بماند</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> چهار نقطهٔ شروع بررسی در V4 چیست؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> Border یک Button قرمز است، ولی انتظار آبی داری. سه بررسی اول را به‌ترتیب بنویس.</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-2"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-2-1" name="chk-2-1" type="checkbox"/><span>Element انتخاب‌شده و Parent مربوط را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-2-2" name="chk-2-2" type="checkbox"/><span>کلاس هدف ویرایش، Device Size و State را به‌ترتیب بررسی کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-2-3" name="chk-2-3" type="checkbox"/><span>بدون افزودن Class یا Element جدید، یک تغییر محدود و قابل Undo پیشنهاد داده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-1-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-1-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 Case Study — Hybrid بودن را فقط مشاهده کن</h3><p><strong>هدف:</strong> 👁 فقط مشاهده کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">legacy_or_hybrid</code></p><p>Export واقعی نشان می‌دهد بعضی Subtreeها هم Elementهای V4 و هم Widgetهای 3.x دارند. وجود هر دو به‌تنهایی به معنی خرابی نیست.</p><h3>🔬 پشت صحنهٔ اختیاری</h3><p>Editor در نهایت HTML و CSS تولید می‌کند، اما این درس فقط Context و Scope تغییر را آموزش می‌دهد.</p><hr/><h3>✅ تصویر ذهنی درست تا اینجا</h3><figure class="visual-figure visual-tree-card"><figcaption>Tree درست قبل از ادامه</figcaption>
<div class="visual-tree">
<div class="tree-node root">Section</div>
<div class="tree-branch">
<div class="tree-node main">Main Layout <span>Normal Flow</span></div>
<div class="tree-children">
<div class="tree-node copy">Copy Area <span>متن و Logoها در Flow</span></div>
<div class="tree-node visual">Visual Area <span>Stage برای Overlay</span>
<div class="tree-children nested">
<div class="tree-node core">Core</div>
<div class="tree-node nodes">Nodes <span>Overlay کنترل‌شده</span></div>
</div>
</div>
</div>
</div>
</div>
<p class="visual-note">اگر این Tree را بتوانی بدون نگاه‌کردن توضیح بدهی، آمادهٔ ادامه‌ای.</p>
</figure></details><details class="lesson-section more-know lesson-disclosure"><summary class="lesson-disclosure-summary">بیشتر بدانید</summary><p><code dir="ltr">display</code> به یک عنصر رفتار چیدمان می‌دهد. یک Div بدون Display مناسب فقط ظرف خام است؛ وقتی Flex یا Grid می‌شود، قواعد چیدمان childها عوض می‌شود.</p></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-1-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-1-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-4"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-4-1" name="chk-4-1" type="checkbox"/><span>می‌توانی تفاوت «کلیک تصادفی» و «بررسی ساختارمند» را با یک مثال توضیح بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-4-2" name="chk-4-2" type="checkbox"/><span>می‌توانی چهار نقطهٔ شروع بررسی را نام ببری: Element، Parent/Child، کلاس هدف ویرایش، Device/State.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-5"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-5-1" name="chk-5-1" type="checkbox"/><span>در Editor یک Element را انتخاب می‌کنی و نام Element، Parent، کلاس هدف ویرایش، Device Size و State را ثبت می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-5-2" name="chk-5-2" type="checkbox"/><span>قبل از افزودن Class یا Element جدید، فقط یک Property را تغییر می‌دهی و نتیجه را Undo می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-6"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-6-1" name="chk-6-1" type="checkbox"/><span>در سناریوی «Border قرمز است ولی آبی انتظار داشتم» می‌توانی اولین سه بررسی را به‌ترتیب بیان کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-1-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-1-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد Screenshot را به یک Element Tree واقعی تبدیل می‌کنیم؛ هنوز Style نمی‌دهیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 1</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-1-completion"><fieldset><legend>ثبت پایان درس 1</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-1-complete" name="lesson-1-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details></article>
