<article class="lesson card-surface" data-lesson="7" id="lesson-7"><h2 class="lesson-title former-h1">درس 7 — Grow، Shrink، Basis، Width و Max Width</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-7-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-7-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> رفتار اندازهٔ Flex Itemها را بدون محاسبات پیچیده بفهمی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> الگوریتم رسمی کامل Flexbox را.</p><p><strong>در پایان باید بتوانی:</strong> Copy منعطف و Visual کنترل‌شده بسازی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-7-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-7-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + 🔍 عیب‌یابی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۵–۳۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> رفتار اندازهٔ Flex Itemها برای مبتدی معمولاً دشوار است.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-7-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-7-lesson-understand-4">A. بفهم</h2><h3>مدل ساده</h3><section aria-labelledby="section-hidden-113-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-113-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Basis</dt><dd>اندازهٔ شروع</dd><dt>Grow</dt><dd>سهم از فضای اضافه</dd><dt>Shrink</dt><dd>اجازهٔ کوچک‌شدن</dd><dt>Max</dt><dd>سقف رشد</dd></dl></section><p>الگوی ذهنی پروژه:</p><section aria-labelledby="section-hidden-114-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-114-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Copy</dt><dd>رشد می‌کند و می‌تواند کوچک شود</dd><dt>Visual</dt><dd>سقف اندازه دارد و از Parent بیرون نمی‌زند</dd></dl></section><h3><code class="inline-code" dir="ltr">min-width:0</code></h3><p>بعضی Flex Itemها به‌خاطر محتوای طولانی حاضر نیستند به‌اندازهٔ لازم کوچک شوند. در چنین موقعیتی Min Width صفر می‌تواند اجازهٔ Shrink واقعی بدهد.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="975e038a6f5ef9b02e24a4f488cbaf6178720f1b013ad49e372a2ae77d957347" id="lesson-7-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Flex Basis، Grow و Shrink</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="7" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-07-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-07-section-01">مسئله‌ای که این مفهوم حل می‌کند</h3><p>دو ستون ممکن است هر دو 50٪ دیده شوند، اما رفتارشان در عرض کم کاملاً متفاوت باشد.</p><p>یکی با Width ساخته شده، دیگری با Basis و Grow. ظاهر Desktop یکسان است، اما قرارداد Responsive آن‌ها یکسان نیست.</p><hr/></section><section aria-labelledby="concept-v31-07-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-07-section-02">تشبیه: تقسیم میز غذا</h3><p>سه نفر دور یک میز نشسته‌اند:</p><ul>
<li>Basis = سهم اولیهٔ هر نفر</li>
<li>Grow = سهم از غذای اضافه</li>
<li>Shrink = سهم از کمبود جا</li>
<li>Min/Max = محدودیت رژیم یا ظرفیت بشقاب</li>
</ul><p>مرورگر ابتدا سهم اولیه را می‌بیند، سپس فضای اضافه یا کمبود را تقسیم می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-07-section-03" class="concept-reference-part"><h3 id="concept-v31-07-section-03">Flex Basis</h3><p><code class="inline-code" dir="ltr">flex-basis</code> اندازهٔ آغازین Flex Item روی Main Axis است.</p><ul>
<li>در Row معمولاً به عرض اولیه مربوط می‌شود.</li>
<li>در Column معمولاً به ارتفاع اولیه مربوط می‌شود.</li>
</ul><p><code class="inline-code" dir="ltr">auto</code> یعنی مرورگر از اندازهٔ اصلی، Width/Height و محتوا برای تعیین Basis کمک می‌گیرد.</p><hr/></section><section aria-labelledby="concept-v31-07-section-04" class="concept-reference-part"><h3 id="concept-v31-07-section-04">Flex Grow</h3><p>Grow فقط <strong>فضای مثبت باقی‌مانده</strong> را تقسیم می‌کند.</p><p>مثال:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Container = 1000px
Basis A = 200px
Basis B = 200px
Gap = 20px
فضای باقی‌مانده = 580px
</code></pre></figure><p>اگر:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">A grow = 1
B grow = 1
</code></pre></figure><p>هرکدام نیمی از 580px اضافه را می‌گیرند.</p><p>اگر:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">A grow = 2
B grow = 1
</code></pre></figure><p>فضای اضافه با نسبت 2 به 1 تقسیم می‌شود؛ نه اینکه اندازهٔ نهایی الزاماً دقیقاً 2 برابر شود.</p><hr/></section><section aria-labelledby="concept-v31-07-section-05" class="concept-reference-part"><h3 id="concept-v31-07-section-05">Flex Shrink</h3><p>Shrink وقتی فعال می‌شود که مجموع اندازه‌های اولیه، Gap و محدودیت‌ها از Parent بزرگ‌تر باشد.</p><p>Shrink مشخص می‌کند هر Item چقدر در حذف فضای منفی مشارکت کند.</p><p>اما محاسبه فقط نسبت ساده نیست؛ اندازهٔ پایه و Min Size نیز اثر دارند.</p><hr/></section><section aria-labelledby="concept-v31-07-section-06" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-07-section-06">تلهٔ مشهور <code class="inline-code" dir="ltr">min-width: auto</code></h3><p>Flex Itemها معمولاً به‌طور پیش‌فرض حاضر نیستند از اندازهٔ حداقلی محتوای خود کوچک‌تر شوند.</p><p>یک URL طولانی، متن بدون شکست یا تصویر می‌تواند باعث Overflow شود.</p><p>راه‌حل رایج در CSS خام:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.flex-item {
  min-width: 0;
}
</code></pre></figure><p>در Elementor باید Min Width، Overflow و رفتار محتوای Child را بررسی کنی؛ فقط Shrink را زیاد نکن.</p><hr/></section><section aria-labelledby="concept-v31-07-section-07" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-07-section-07">مثال Elementor: متن و تصویر</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Hero
├── Copy: basis 60%, grow 1, shrink 1
└── Image: basis 40%, grow 0, shrink 1
</code></pre></figure><p>این قرارداد می‌گوید:</p><ul>
<li>Copy سهم اولیهٔ بیشتری دارد.</li>
<li>Copy می‌تواند فضای اضافه را بگیرد.</li>
<li>هر دو در کمبود جا می‌توانند کوچک شوند.</li>
</ul><p>اما اگر تصویر <code class="inline-code" dir="ltr">min-width: 500px</code> داشته باشد، Shrink ممکن است نتواند Layout را نجات دهد.</p><hr/></section><section aria-labelledby="concept-v31-07-section-08" class="concept-reference-part"><h3 id="concept-v31-07-section-08">مهندسی معکوس Flex در پنل V4</h3><p>دانستن <code class="inline-code" dir="ltr">flex: 1 1 0</code> کافی نیست؛ باید بفهمی کنترل‌های V4 چه CSSای تولید کرده‌اند. این سه مقدار در CSS یعنی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">flex-grow: 1;
flex-shrink: 1;
flex-basis: 0;
</code></pre></figure><p>اما خالی‌گذاشتن Width در رابط لزوماً به معنای <code class="inline-code" dir="ltr">flex-basis: 0</code> نیست؛ ممکن است Basis مؤثر <code class="inline-code" dir="ltr">auto</code> باشد و اندازهٔ محتوا وارد مذاکره شود. پس جدول زیر «ترجمه نیت» است، نه وعدهٔ خروجی ثابت:</p><div aria-label="جدول آموزشی مرجع مفهومی" class="table-scroll concept-table-scroll" role="region" tabindex="0"><table class="data-table educational-table concept-reference-table"><caption>جدول آموزشی مرجع مفهومی</caption>
<thead>
<tr>
<th>نیت طراحی</th>
<th>تنظیم اولیه در V4</th>
<th>چیزی که در DevTools باید تأیید شود</th>
</tr>
</thead>
<tbody>
<tr>
<td>دو ستون منعطف بر اساس محتوا</td>
<td>Width بدون مقدار صریح، Grow برابر، Shrink فعال</td>
<td><code class="inline-code" dir="ltr">flex-basis</code> مؤثر و Min Size</td>
</tr>
<tr>
<td>دو سهم واقعاً مساوی از پایه صفر</td>
<td>کنترل‌هایی که Basis صفر تولید کنند</td>
<td><code class="inline-code" dir="ltr">flex: 1 1 0</code> یا معادل آن</td>
</tr>
<tr>
<td>سایدبار ثابت و محتوای شناور</td>
<td>Sidebar: Width 300px، Grow 0، Shrink 0؛ Content: Grow 1، Shrink 1</td>
<td>ثابت‌ماندن Sidebar و <code class="inline-code" dir="ltr">min-width: 0</code> روی Content در صورت نیاز</td>
</tr>
</tbody>
</table></div><p>در Flex Row، <code class="inline-code" dir="ltr">width: 100%</code> روی تمام Childها معمولاً با هدف چندستونه تعارض دارد؛ چون هر Child می‌خواهد عرض کامل Parent را مبنا بگیرد. اما این مقدار «همیشه سم» نیست: در Flex Column یا زمانی که عمداً هر Item باید یک ردیف کامل بگیرد، می‌تواند درست باشد.</p><h4>قانون عملی</h4><blockquote>
<p>در Flex Row، وقتی Grow قرار است فضا را تقسیم کند، Width را بی‌دلیل روی 100٪ قفل نکن. ابتدا Basis، Grow، Shrink و Min Size را به‌عنوان یک قرارداد واحد ببین.</p>
</blockquote></section><section aria-labelledby="concept-v31-07-section-09" class="concept-reference-part"><h3 id="concept-v31-07-section-09">Width یا Basis؟</h3><p>در Flex، Basis معمولاً زبان مستقیم‌تری برای سهم اولیه در Main Axis است.</p><p>اما Width هنوز مهم است:</p><ul>
<li>خارج از Flex</li>
<li>به‌عنوان ورودی <code class="inline-code" dir="ltr">flex-basis: auto</code></li>
<li>برای Min/Max constraints</li>
<li>برای اندازهٔ خود محتوا یا Child</li>
</ul><p>پس این دو دشمن هم نیستند؛ باید بدانیم کدام مرحله از محاسبه را کنترل می‌کنند.</p><hr/></section><section aria-labelledby="concept-v31-07-section-10" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-07-section-10">ترتیب عیب‌یابی</h3><ol>
<li>Direction چیست؟</li>
<li>Main Size Parent چقدر است؟</li>
<li>Basis هر Item چیست؟</li>
<li>Gapها چقدرند؟</li>
<li>فضای مثبت داریم یا منفی؟</li>
<li>Grow یا Shrink چه نسبت‌هایی دارند؟</li>
<li>Min/Max و محتوای نشکن مانع هستند؟</li>
</ol><hr/></section><section aria-labelledby="concept-v31-07-section-11" class="concept-reference-part"><h3 id="concept-v31-07-section-11">مثال 50/50 قابل‌اعتماد</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.item {
  flex: 1 1 0;
  min-width: 0;
}
</code></pre></figure><p>این الگو فضای موجود را از پایهٔ صفر با Grow مساوی تقسیم می‌کند. اما همیشه بهترین انتخاب نیست؛ محتوای دو ستون ممکن است نیاز واقعی متفاوتی داشته باشد.</p><hr/></section><section aria-labelledby="concept-v31-07-section-12" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-07-section-12">تصویر ذهنی نهایی</h3><p>Basis پیشنهاد اولیه هر مسافر برای جاست؛ Grow تقسیم صندلی‌های خالی و Shrink تقسیم کمبود جاست. Min Size می‌تواند بگوید یک مسافر از اندازه‌ای کوچک‌تر نمی‌شود، حتی اگر بقیه آماده فشرده‌شدن باشند.</p></section><section aria-labelledby="concept-v31-07-section-13" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-07-section-13">قوانین طلایی</h3><ul>
<li><strong>«Basis اندازهٔ شروع مذاکره است؛ Grow و Shrink نتیجهٔ مذاکره را تغییر می‌دهند.»</strong></li>
<li><strong>«Grow اندازهٔ نهایی را نسبت‌بندی نمی‌کند؛ فقط فضای اضافه را نسبت‌بندی می‌کند.»</strong></li>
<li><strong>«Shrink بدون بررسی Min Size و محتوای نشکن کامل نیست.»</strong></li>
<li><strong>«ظاهر 50/50 در Desktop، قرارداد Responsive را ثابت نمی‌کند.»</strong></li>
<li><strong>«در Flex ابتدا Basis را بفهم، بعد Width را تفسیر کن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>MDN: flex-basis</li>
<li>MDN: flex-grow</li>
<li>MDN: flex-shrink</li>
<li>CSS Flexible Box Layout specification</li>
<li>Elementor Help: Set Flexbox Container size and behavior</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-7-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-7-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Grow و Shrink عدد بدون واحدند؛ Basis و Width اندازه‌اند</span></summary>
<section aria-labelledby="lesson-7-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Grow و Shrink نسبت توزیع‌اند، نه پیکسل. Basis اندازهٔ آغازین main axis را می‌دهد و Width در برخی contextها ورودی دیگری برای sizing است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> Grow سهم هر نفر از کیک اضافه است؛ Shrink سهم هر نفر از کمبود فضا؛ Basis اندازهٔ بشقاب اولیه است.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Grow</th><td><code dir="ltr">flex-grow</code></td><td>عدد بدون واحد؛ معمولاً 0،1،2…</td><td>نسبت فضای آزاد</td><td>برای تقسیم فضای اضافه.</td><td>grow:2 یعنی دو برابر پیکسل نیست؛ دو سهم است.</td><td><code dir="ltr">CSS_FLEX</code></td></tr><tr><th scope="row">Shrink</th><td><code dir="ltr">flex-shrink</code></td><td>عدد بدون واحد</td><td>نسبت کم‌شدن همراه base size</td><td>برای مدیریت کمبود فضا.</td><td>min-width و content می‌توانند مانع shrink شوند.</td><td><code dir="ltr">CSS_FLEX</code></td></tr><tr><th scope="row">Basis</th><td><code dir="ltr">flex-basis</code></td><td>auto، طول یا درصد در CSS</td><td>main axis</td><td>اندازهٔ آغازین Flex item.</td><td>در Column به محور عمودی مربوط می‌شود، نه همیشه Width.</td><td><code dir="ltr">CSS_FLEX</code></td></tr><tr><th scope="row">Custom Width</th><td><code dir="ltr">width</code></td><td>PX، %، VW در کنترل‌های مستند</td><td>Parent یا viewport</td><td>برای intent صریح.</td><td>Width و Basis می‌توانند با هم تعامل داشته باشند.</td><td><code dir="ltr">E_CONTAINER_ADV</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>فضای آزاد 300px و Growهای 1 و 2: مجموع سهم=3؛ Child اول 100px و Child دوم 200px از فضای آزاد می‌گیرد.</p></section>
<section><h3>📱 در Responsive</h3><p>در Mobile اغلب Basis/Width به 100% و Grow به 0 یا مقدار ساده‌تر تغییر می‌کند؛ نتیجه را با content واقعی تست کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>flex-basis، flex-grow، flex-shrink، min-width و used width را با هم بخوان.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://www.w3.org/TR/css-flexbox-1/" rel="noopener noreferrer" target="_blank">W3C — CSS Flexible Box Layout</a>، <a href="https://elementor.com/help/container-advanced-tab-settings/" rel="noopener noreferrer" target="_blank">Elementor — Container advanced settings</a>، <a href="https://elementor.com/help/style-tab-size/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Size</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-7-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-7-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA</h3><p>Platform Copy:</p><section aria-labelledby="section-hidden-116-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-116-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Grow</dt><dd>1</dd><dt>Shrink</dt><dd>1</dd><dt>Basis</dt><dd>مقدار آغازین پیشنهادی</dd><dt>Min Width</dt><dd>0</dd></dl></section><p>Platform Visual:</p><section aria-labelledby="section-hidden-117-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-117-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Grow</dt><dd>0</dd><dt>Shrink</dt><dd>1</dd><dt>Width</dt><dd>100% در محدودهٔ خودش</dd><dt>Max Width</dt><dd>سقف کنترل‌شده</dd></dl></section><p>اعداد دقیق را از روی Screenshot حقیقت ندان؛ با Preview تنظیم کن.</p><h3>❓ سؤال توقف</h3><p>کدام ستون باید معمولاً فضای اضافه را بیشتر بگیرد: Copy یا Visual؟ چرا؟</p><details class="disclosure-card"><summary>پاسخ پیشنهادی</summary>
<p>Copy، چون متن انعطاف‌پذیر است و Visual سقف مشخص دارد.</p>
</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> Visual را Width ثابت و Shrink صفر کنی.</p><p><strong>نشانه:</strong> در Tablet صفحه Overflow می‌گیرد.</p><h3>🧪 عمداً خرابش کن</h3><p>Visual را روی Width بسیار بزرگ و Shrink=0 بگذار.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>Copy بیش از حد فشرده می‌شود؛</li>
<li>Main از Parent بیرون می‌زند؛</li>
<li>Scroll افقی ممکن است ظاهر شود.</li>
</ul><p>سپس Max Width و Shrink را اصلاح کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-118-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-118-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-37"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-37-1" name="chk-37-1" type="checkbox"/><span>Copy فضای باقی‌مانده را می‌گیرد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-37-2" name="chk-37-2" type="checkbox"/><span>Visual سقف اندازه دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-37-3" name="chk-37-3" type="checkbox"/><span>Copy دارای Min Width صفر است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-37-4" name="chk-37-4" type="checkbox"/><span>عرض باریک Overflow ندارد</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Grow، Shrink و Basis به‌ترتیب چه می‌گویند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> یک Input باید فضای خالی را بگیرد و Button نباید مچاله شود؛ تنظیم رفتاری هرکدام را توضیح بده.</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-38"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-38-1" name="chk-38-1" type="checkbox"/><span>Basis، Grow و Shrink را با نقش متفاوت توضیح داده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-38-2" name="chk-38-2" type="checkbox"/><span>عنصر منعطف و عنصر محدود را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-38-3" name="chk-38-3" type="checkbox"/><span>در صورت Overflow، min-width و محتوای ذاتی را هم بررسی کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-7-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-7-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-ABS-001 — Card Width</h3><p><strong>هدف:</strong> ⚖️ دو روش را مقایسه کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">improvement_candidate</code></p><p>هشت Card در Export روی Desktop عرض 24% و ارتفاع 20vw دارند. این ساختار برای مقایسهٔ Width درصدی، Flex behavior و Grid tracks مناسب است؛ خرابی Runtime اثبات نشده.</p><h3>🔬 پشت صحنه</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text language-css" dir="ltr">flex: 1 1 ...;
min-width: 0;
max-width: ...;
</code></pre><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="reza-flex-duplicate-heading" role="heading">🧪 آزمایش واقعی رضا — Flex Row، یک Div و Duplicate</span></summary><section aria-labelledby="reza-flex-duplicate-heading" class="real-reza-experiment disclosure-content lesson-section">
<ol class="case-steps">
<li><strong>چیزی که رضا دید:</strong> وقتی یک <span dir="ltr">Flex Row</span> ساخت و داخلش یک <span dir="ltr">Div Block</span> گذاشت، Div ظاهراً کل ردیف را گرفت. بعد از Duplicate، دو Div حدوداً ۵۰٪ / ۵۰٪ دیده شدند.</li>
<li><strong>حدس اشتباه مبتدی:</strong> «پس Elementor خودش Div را از ۱۰۰٪ به ۵۰٪ تبدیل کرد.»</li>
<li><strong>قانون CSS / Elementor V4:</strong> یک فرزند ممکن است به‌خاطر <span dir="ltr">width</span>، <span dir="ltr">flex-basis</span>، <span dir="ltr">flex-grow</span>، کشش والد، یا پیش‌فرض‌های Elementor فضای موجود را پر کند. دو فرزند Duplicate شده هم تنظیمات محاسبه‌شدهٔ مشابهی می‌گیرند و ممکن است بصری نصف‌نصف شوند؛ این قانون جهانی نیست و باید از Computed Style تأیید شود.</li>
<li><strong>در پنل Elementor کجا چک کنم؟</strong> Element را انتخاب کن و در Layout / Size یا Advanced، مقدار Width، Flex Basis، Grow، Shrink، Align و Stretch را ببین. همچنین بررسی کن آیا کلاس محلی یا Global Class روی اندازه اثر گذاشته است.</li>
<li><strong>در DevTools / Computed Style کجا چک کنم؟</strong> در تب Computed مقدارهای <code dir="ltr">width</code>، <code dir="ltr">flex-basis</code>، <code dir="ltr">flex-grow</code>، <code dir="ltr">flex-shrink</code> و Box Model را نگاه کن.</li>
<li><strong>راه‌حل درست:</strong> اگر نیت تو دو ستون برابر است، آن را صریح طراحی کن؛ مثلاً basis/grow را آگاهانه تنظیم کن، نه اینکه فقط به ظاهر Duplicate تکیه کنی. اگر از اول <code dir="ltr">width: 50%</code> می‌دهی، نیتت با حالت auto/grow فرق دارد، حتی اگر خروجی نهایی شبیه شود.</li>
<li><strong>قانون طلایی:</strong> ظاهر نهایی را با نیت طراحی اشتباه نگیر؛ width، basis و grow مشخص می‌کنند عنصر چرا آن اندازه شده است.</li>
</ol>
<div aria-label="نمای تصویری تفاوت یک فرزند، دو فرزند و شروع از ۵۰ درصد" class="flex-experiment-visual">
<div class="experiment-row"><span class="experiment-label">یک فرزند</span><div class="experiment-track"><span class="experiment-box fill">Div fills available row</span></div></div>
<div class="experiment-row"><span class="experiment-label">دو فرزند</span><div class="experiment-track"><span class="experiment-box half">Div</span><span class="experiment-box half">Div</span></div></div>
<div class="experiment-row"><span class="experiment-label">از اول ۵۰٪</span><div class="experiment-track"><span class="experiment-box half">Div 50٪</span><span class="experiment-space">فضای خالی</span></div></div>
<div class="experiment-row"><span class="experiment-label">بعد Duplicate</span><div class="experiment-track"><span class="experiment-box half">Div 50٪</span><span class="experiment-box half">Div 50٪</span></div></div>
</div>
<section aria-labelledby="width-basis-memory-heading" class="memory-layer">
<h3 id="width-basis-memory-heading">🧠 استعارهٔ ماندگار</h3>
<p><strong>Width</strong> مثل اندازهٔ پیشنهادی لباس است؛ <strong>Flex Basis</strong> اندازهٔ شروع در ریل Flex است؛ <strong>Grow</strong> سهم از فضای اضافه است؛ <strong>Shrink</strong> اجازهٔ کوچک‌شدن هنگام کمبود جاست.</p>
<p><strong>⚠️ تله رایج:</strong> دو مسیر می‌توانند ظاهر یکسان بسازند اما Responsive متفاوت داشته باشند.</p>
</section>
<details class="more-know">
<summary>بیشتر بدانید</summary>
<p><code dir="ltr">auto</code> معمولاً یعنی مرورگر از اندازهٔ محتوا یا width استفاده کند. <code dir="ltr">width: 50%</code> یعنی نیت اندازه صریح است. <code dir="ltr">flex-basis</code> در محور اصلی Flex نقش شروع اندازه را دارد و اگر با width هم‌زمان مقدار غیر-auto بگیرد، باید Computed Style را معیار قرار دهی.</p>
</details>
</section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="debug-elementor-v4-heading" role="heading">Debug in Elementor V4 — جدول عیب‌یابی سریع</span></summary><section aria-labelledby="debug-elementor-v4-heading" class="disclosure-content lesson-section">
<div aria-label="جدول عیب‌یابی Elementor V4" class="table-wrap debug-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table debug-table">
<caption>عیب‌یابی عملی Layout در Elementor V4</caption>
<thead>
<tr><th scope="col">چیزی که دیدی</th><th scope="col">علت احتمالی</th><th scope="col">در Elementor کجا چک کنم؟</th><th scope="col">در DevTools کجا چک کنم؟</th><th scope="col">راه‌حل</th></tr>
</thead>
<tbody>
<tr><th scope="row">یک Div ظاهراً full width است</th><td>width، basis، grow یا stretch والد</td><td>Layout / Size و کلاس فعال</td><td>Computed: width, flex-basis, flex-grow</td><td>نیت اندازه را صریح کن؛ auto و grow را تفکیک کن.</td></tr>
<tr><th scope="row">دو Div بعد از Duplicate حدوداً 50/50 دیده می‌شوند</th><td>تنظیمات مشابه و تقسیم فضای آزاد</td><td>تنظیمات هر دو child و کلاس مشترک</td><td>Computed هر دو child را کنار هم مقایسه کن</td><td>برای ستون برابر، basis/grow را آگاهانه تعریف کن.</td></tr>
<tr><th scope="row">در RTL فاصلهٔ سمت راست دیده نمی‌شود</th><td>logical margin، width 100%، overflow یا parent بدون padding</td><td>Advanced / Spacing و Direction</td><td>Box Model و computed margin-inline-start/end</td><td>برای فاصلهٔ داخلی padding-inline یا shell padding بده.</td></tr>
<tr><th scope="row">ارتفاع Parent شامل محتوا نیست</th><td>فرزند absolute از Flow خارج شده یا float/position خاص</td><td>Position هر child</td><td>Layout pane و Box Model parent/child</td><td>محتوای اصلی را در Normal Flow نگه دار.</td></tr>
<tr><th scope="row">Absoluteها غیرمنتظره روی هم می‌افتند</th><td>containing block اشتباه یا offset یکسان</td><td>Position parent و child</td><td>Computed position, inset, z-index</td><td>Stage را relative کن و فقط داخل آن absolute بساز.</td></tr>
<tr><th scope="row">Global Class اثر نمی‌کند</th><td>کلاس فعال نیست، ترتیب/اولویت یا Local Class override کرده</td><td>Class field و Class Manager</td><td>Styles pane: rule source و specificity</td><td>کلاس هدف ویرایش، ترتیب و conflict را جدا بررسی کن.</td></tr>
<tr><th scope="row">Hover/Focus با Normal فرق دارد</th><td>State فعال یا rule جداگانه برای pseudo-class</td><td>State selector: Normal / Hover / Focus / Active</td><td>Force state و rule source</td><td>State را جدا تنظیم کن و Focus را برای دسترسی حذف نکن.</td></tr>
</tbody>
</table>
</div>
</section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-7-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-7-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><section aria-labelledby="flex-sizing-step-title" class="step-simulator step-simulator-flex-sizing" data-simulator-type="flex-sizing" data-step-simulator="" id="flex-sizing-step"><h3 id="flex-sizing-step-title">Step‑Through — Basis، Grow و Shrink روی main axis</h3><p>عرض ظرف و قرارداد هر Item تغییر می‌کند؛ نتیجه را به‌عنوان رفتار Flex ببین، نه درصد ثابت.</p><div aria-live="polite" class="simulator-viewport"><p class="simulator-label" data-step-label=""></p><div class="simulator-rail simulator-rail-flex-sizing" data-step-render=""></div><code class="simulator-code" data-step-code="" dir="ltr"></code></div><div class="simulator-actions"><button aria-label="نمایش حالت قبلی" class="ui-btn" data-step-prev="" type="button">حالت قبلی</button><button aria-label="نمایش حالت بعدی" class="ui-btn" data-step-next="" type="button">حالت بعدی</button></div><script class="simulator-data" type="application/json">[{"label":"حالت ۱ از ۵ — Basis نقطهٔ شروع روی main axis است.","code":"A { flex: 0 1 55%; } B { flex: 0 1 45%; }","container":"wide","items":[{"name":"Copy","basis":"55%","grow":0,"shrink":1},{"name":"Visual","basis":"45%","grow":0,"shrink":1}]},{"label":"حالت ۲ از ۵ — Grow فضای اضافه را با نسبت 1 به 2 تقسیم می‌کند.","code":"A { flex: 1 1 10rem; } B { flex: 2 1 10rem; }","container":"wide","items":[{"name":"A · grow 1","basis":"10rem","grow":1,"shrink":1},{"name":"B · grow 2","basis":"10rem","grow":2,"shrink":1}]},{"label":"حالت ۳ از ۵ — در ظرف باریک Shrink کمبود فضا را پخش می‌کند.","code":"A, B { flex-basis: 65%; flex-shrink: 1; }","container":"narrow","items":[{"name":"A · shrink 1","basis":"65%","grow":0,"shrink":1},{"name":"B · shrink 1","basis":"65%","grow":0,"shrink":1}]},{"label":"حالت ۴ از ۵ — Shrink صفر روی هر دو Item می‌تواند Overflow بسازد.","code":"A, B { flex: 0 0 65%; }","container":"narrow","items":[{"name":"A · shrink 0","basis":"65%","grow":0,"shrink":0},{"name":"B · shrink 0","basis":"65%","grow":0,"shrink":0}]},{"label":"حالت ۵ از ۵ — Copy منعطف، Visual محدود و min-width صفر.","code":".copy { flex: 1 1 18rem; min-width: 0; } .visual { flex: 0 1 16rem; max-width: 42%; }","container":"wide","items":[{"name":"Copy","basis":"18rem","grow":1,"shrink":1,"minWidth":"0"},{"name":"Visual","basis":"16rem","grow":0,"shrink":1,"maxWidth":"42%"}]}]</script><p class="golden-rule"><strong>قانون طلایی:</strong> Basis شروع است؛ Grow و Shrink فقط با فضای اضافه یا کمبود فعال می‌شوند.</p></section><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-40"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-40-1" name="chk-40-1" type="checkbox"/><span>می‌توانی Grow، Shrink و Basis را به زبان اندازهٔ شروع، سهم رشد و توان جمع‌شدن توضیح بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-40-2" name="chk-40-2" type="checkbox"/><span>می‌توانی نقش Width، Max Width و min-width:0 را در Flex Item تشخیص بدهی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-41"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-41-1" name="chk-41-1" type="checkbox"/><span>Copy را منعطف و Visual را محدود می‌کنی تا در عرض متوسط Overflow ایجاد نشود.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-41-2" name="chk-41-2" type="checkbox"/><span>با متن طولانی ثابت می‌کنی Copy می‌تواند Shrink شود و Parent را عریض نمی‌کند.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-42"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-42-1" name="chk-42-1" type="checkbox"/><span>برای Search Bar شامل Input و Button می‌توانی بگویی کدام Item باید Grow کند و کدام نباید Shrink شود.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-7-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-7-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد ردیف Logoها را می‌سازیم و Wrap را به‌صورت واقعی تجربه می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 7</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-7-completion"><fieldset><legend>ثبت پایان درس 7</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-7-complete" name="lesson-7-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-7-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Flex Basis، Width، Grow و Shrink</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Flex Basis در برابر Width</h3><p>Width اندازهٔ معمولی عنصر است؛ Flex Basis سهم اولیهٔ عنصر در مذاکرهٔ Flexbox است. در parentهای flex، مرورگر اول Basis را می‌بیند و بعد Grow/Shrink تصمیم می‌گیرند.</p><p>برای دو ستون responsive، Basis اغلب از Width روشن‌تر است؛ چون به زبان خود Flexbox حرف می‌زند.</p></section>
<section class="inline-compare-card"><h3>Grow در برابر Shrink</h3><p><strong>Grow</strong> می‌گوید وقتی جا اضافه بود چقدر سهم بگیرم. <strong>Shrink</strong> می‌گوید وقتی جا کم بود چقدر کوتاه بیایم.</p><p class="golden-rule">قانون طلایی: Grow برای تقسیم فضای اضافه است؛ Shrink برای جلوگیری از له‌شدن یا اجازهٔ فشرده‌شدن.</p></section>
</div>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="flex-basis-main-axis-title" role="heading">اصلاح دقیق نسخه 22 — flex-basis همیشه «عرض» نیست</span></summary><section aria-labelledby="flex-basis-main-axis-title" class="smart-note-card disclosure-content">
<p><code class="inline-code" dir="ltr">flex-basis</code> اندازهٔ شروع flex item روی <strong>main axis</strong> است. اگر <code class="inline-code" dir="ltr">flex-direction: row</code> باشد، معمولاً شبیه عرض عمل می‌کند؛ اگر <code class="inline-code" dir="ltr">flex-direction: column</code> باشد، روی محور عمودی و شبیه ارتفاع اولیه اثر می‌گذارد.</p>
<div class="memory-layer compact-memory"><p><strong>🧠 استعارهٔ ماندگار:</strong> basis جای رزرو اولیهٔ صندلی است؛ grow و shrink بعداً تصمیم می‌گیرند صندلی بزرگ‌تر یا کوچک‌تر شود.</p><p><strong>⚠️ تله رایج:</strong> دو آیتم ممکن است ظاهراً 50/50 شوند، اما یکی با width آمده باشد و دیگری با basis/grow.</p><p><strong>📜 قانون طلایی:</strong> همیشه در Computed Style این چهار مقدار را با هم بخوان: <code class="inline-code" dir="ltr">width</code>، <code class="inline-code" dir="ltr">flex-basis</code>، <code class="inline-code" dir="ltr">flex-grow</code>، <code class="inline-code" dir="ltr">flex-shrink</code>.</p></div>
</section></details><details class="lesson-disclosure" id="lesson-7-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Basis، Grow و Width را برای صفحهٔ باریک بازبینی کن</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>Basis یا Width ستونی که در Desktop دو ستون می‌سازد ممکن است در Mobile باعث فشردگی یا overflow شود.</p>
<ul><li>در Mobile، itemهای اصلی را روی Width قابل‌انطباق بررسی کن.</li><li>وجود <code>flex-grow</code>، <code>flex-shrink</code> و <code>flex-basis</code> را در Computed Style ببین.</li><li>مشاهدهٔ طرح Mobile به‌تنهایی عدد 100% یا auto را اثبات نمی‌کند.</li></ul>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-7-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Basis، Grow و Shrink در عرض‌های کوچک</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> تفاوت مقدار شروع، تقسیم فضای آزاد و فشرده‌شدن را در Responsive ببین.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>دو child با Basis برابر بساز و Grow/Shrink آن‌ها را ثبت کن.</li><li>عرض preview را تدریجی کم کن و Used Size هر child را ببین.</li><li>در Mobile Basis یا Width را فقط جایی override کن که layout واقعاً می‌شکند.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن در فضای اضافه Grow و در کمبود فضا Shrink چه نقشی دارند.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>برای هر دو child min-width بزرگ یا shrink صفر قرار بده و overflow را مشاهده کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>flex-basis، flex-grow، flex-shrink، min-width و اندازهٔ نهایی در Computed.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> می‌توانی تفاوت مقدار تنظیم‌شده با Used Width را توضیح بدهی.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-7-responsive-build-test-done-build"><input data-persist="" id="lesson-7-responsive-build-test-done-build" name="lesson-7-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-7-responsive-build-test-done-test"><input data-persist="" id="lesson-7-responsive-build-test-done-test" name="lesson-7-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-7-responsive-build-test-done-debug"><input data-persist="" id="lesson-7-responsive-build-test-done-debug" name="lesson-7-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-7-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-7-responsive-build-test-note" name="lesson-7-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/container-advanced-tab-settings/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-7-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Basis، Width و Max Width</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
