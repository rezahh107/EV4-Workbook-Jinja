<article class="lesson card-surface" data-lesson="5" id="lesson-5"><h2 class="lesson-title former-h1">درس 5 — Flexbox و ساخت دو ستون اصلی</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-5-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-5-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> چرا Main Layout پروژه Flexbox است و چگونه دو Child را کنار هم می‌چیند.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Grow و Shrink را.</p><p><strong>در پایان باید بتوانی:</strong> دو ناحیهٔ Copy و Visual را در Normal Flow کنار هم قرار دهی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-5-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-5-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۰–۲۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۲۰–۳۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> اولین Layout واقعی پروژه ساخته می‌شود.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-5-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-5-lesson-understand-4">A. بفهم</h2><h3>مسئله</h3><p>Copy و Visual زیر هم هستند، اما در Desktop باید کنار هم باشند.</p><h3>مدل ذهنی</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Parent Flexbox
|
+-- Item A
+-- Item B</pre></figure></details><p>Flexbox برای چیدمان یک‌بعدی مناسب است.</p><h3>چرا نه Absolute؟</h3><p>چون ستون‌های اصلی محتوای واقعی‌اند و باید Height والد را بسازند، با متن رشد کنند و در Mobile به‌سادگی تغییر جهت دهند.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="2550653d2296b77121ab383c358abd088dc55afd0216aa5f2973130267089df3" id="lesson-5-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Flexbox؛ چیدمان یک‌بعدی و رابطهٔ Parent/Item</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="5" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-05-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-05-section-01">مسئله‌ای که Flexbox حل می‌کند</h3><p>قبل از Flexbox، کنار هم گذاشتن، وسط‌چین‌کردن و توزیع منعطف Elementها اغلب به Float، Inline-block یا ترفندهای پیچیده نیاز داشت.</p><p>Flexbox برای یک سؤال ساخته شد:</p><blockquote>
<p>چگونه چند Item را در یک محور بچینیم و فضای اضافه یا کمبود را میان آن‌ها مدیریت کنیم؟</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-05-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-05-section-02">تشبیه به دنیای واقعی: واگن و چمدان‌ها</h3><ul>
<li>Flex Container = واگن</li>
<li>Flex Item = چمدان مستقیم داخل واگن</li>
<li>Main Axis = مسیر طولی واگن</li>
<li>Cross Axis = عرض واگن</li>
<li>Basis = اندازهٔ اولیهٔ هر چمدان</li>
<li>Grow = سهم هر چمدان از فضای اضافه</li>
<li>Shrink = سهم هر چمدان از کمبود فضا</li>
<li>Gap = فاصلهٔ ثابت میان چمدان‌ها</li>
</ul><p>نوه‌ای که داخل یکی از چمدان‌هاست، مستقیماً با قانون واگن چیده نمی‌شود.</p><hr/></section><section aria-labelledby="concept-v31-05-section-03" class="concept-reference-part concept-reference-definition"><h3 id="concept-v31-05-section-03">تعریف دقیق</h3><p>Flexbox یک مدل Layout <strong>یک‌بعدی</strong> است. یک‌بعدی یعنی تصمیم اصلی حول یک محور انجام می‌شود؛ Row یا Column.</p><p>این به معنی ناتوانی در کنترل محور دیگر نیست. Align روی محور متقاطع عمل می‌کند، اما منطق اصلی توزیع اندازه و ترتیب در Main Axis است.</p><hr/></section><section aria-labelledby="concept-v31-05-section-04" class="concept-reference-part"><h3 id="concept-v31-05-section-04">Parent چه چیزی را کنترل می‌کند؟</h3><p>Flex Container معمولاً این رفتارها را تعیین می‌کند:</p><ul>
<li>Direction</li>
<li>Wrap</li>
<li>Justify Content</li>
<li>Align Items</li>
<li>Align Content در حالت چندخطی</li>
<li>Gap</li>
</ul></section><section aria-labelledby="concept-v31-05-section-05" class="concept-reference-part"><h3 id="concept-v31-05-section-05">Item چه چیزی را کنترل می‌کند؟</h3><p>Flex Item معمولاً این موارد را حمل می‌کند:</p><ul>
<li>Basis</li>
<li>Grow</li>
<li>Shrink</li>
<li>Order</li>
<li>Align Self</li>
<li>Min/Max Size</li>
</ul><hr/></section><section aria-labelledby="concept-v31-05-section-06" class="concept-reference-part"><h3 id="concept-v31-05-section-06">مثال ساده</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.parent {
  display: flex;
  flex-direction: row;
  gap: 24px;
}
</code></pre></figure><p>فقط Childهای مستقیم <code class="inline-code" dir="ltr">.parent</code> Flex Item می‌شوند.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Parent
├── A  ← Flex Item
├── B  ← Flex Item
└── C  ← Flex Item
    └── D  ← Flex Item این Parent نیست
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-05-section-07" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-05-section-07">چرا Flex را «مذاکرهٔ اندازه» می‌نامیم؟</h3><p>Itemها فقط Width ثابت ندارند. مرورگر این اطلاعات را کنار هم می‌گذارد:</p><ol>
<li>اندازهٔ اولیه یا Basis</li>
<li>محتوای داخلی</li>
<li>Min/Max constraints</li>
<li>فضای موجود Parent</li>
<li>Grow یا Shrink</li>
<li>Gapها</li>
</ol><p>سپس Used Size را محاسبه می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-05-section-08" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-05-section-08">سناریوی Elementor: Hero دو ستونه</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Hero Flexbox — Row
├── Copy — basis 55%
└── Visual — basis 45%
</code></pre></figure><p>روی موبایل:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Hero Flexbox — Column
├── Copy
└── Visual
</code></pre></figure><p>در این مدل، تغییر Direction ساختار را Responsive می‌کند؛ نیازی نیست نسخهٔ دوم Section بسازی و یکی را مخفی کنی.</p><hr/></section><section aria-labelledby="concept-v31-05-section-09" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-05-section-09">ترتیب صحیح تنظیم Flex</h3><ol>
<li>Parent مناسب را انتخاب کن.</li>
<li>Direction را مشخص کن.</li>
<li>اندازهٔ اولیهٔ Itemها را بررسی کن.</li>
<li>فضای آزاد یا کمبود را تشخیص بده.</li>
<li>Grow/Shrink را تنظیم کن.</li>
<li>Justify/Align را اعمال کن.</li>
<li>Gap و Wrap را تنظیم کن.</li>
<li>در عرض‌های واقعی تست کن.</li>
</ol><p>اگر از مرحلهٔ ۶ شروع کنی، ممکن است Alignment کار نکند چون فضای آزادی وجود ندارد.</p><hr/></section><section aria-labelledby="concept-v31-05-section-10" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-05-section-10">تله‌های رایج</h3><ul>
<li>تصور اینکه Flex همیشه دو ستون مساوی می‌سازد</li>
<li>استفاده از Justify برای حل Width اشتباه</li>
<li>فراموش‌کردن <code class="inline-code" dir="ltr">min-width: auto</code> و محتوای بلند</li>
<li>دادن Flex به Parent اشتباه</li>
<li>استفاده از Order برای تغییر معنای محتوا بدون بررسی ترتیب Keyboard/DOM</li>
<li>استفاده از Flex برای Layout واقعاً دوبعدی و پیچیده</li>
</ul><hr/></section><section aria-labelledby="concept-v31-05-section-11" class="concept-reference-part"><h3 id="concept-v31-05-section-11">Flex یا Grid؟</h3><p>از خودت بپرس:</p><ul>
<li>آیا بیشتر دربارهٔ «توالی در یک خط/ستون» فکر می‌کنم؟ → Flex</li>
<li>آیا دربارهٔ «مختصات ردیف و ستون» فکر می‌کنم؟ → Grid</li>
</ul><hr/></section><section aria-labelledby="concept-v31-05-section-12" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-05-section-12">پل به DevTools</h3><p>Badge مربوط به <code class="inline-code" dir="ltr">flex</code> را کنار Parent فعال کن. سپس در Computed Style، <code class="inline-code" dir="ltr">display</code>، <code class="inline-code" dir="ltr">flex-direction</code>، <code class="inline-code" dir="ltr">gap</code> و اندازهٔ Childها را ببین. اگر یک Child برخلاف انتظار رفتار می‌کند، ابتدا ثابت کن Flex Item مستقیم همین Parent است؛ نوه‌ها از Flex Parent بالاتر مستقیماً فرمان نمی‌گیرند.</p></section><section aria-labelledby="concept-v31-05-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-05-section-13">تصویر ذهنی نهایی</h3><p>Flex Container واگنی است که قانون حرکت را تعیین می‌کند و Childهای مستقیم چمدان‌هایی هستند که درباره سهم فضا مذاکره می‌کنند. چمدان داخل چمدان از قانون واگن بیرونی مستقیماً فرمان نمی‌گیرد.</p></section><section aria-labelledby="concept-v31-05-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-05-section-14">قوانین طلایی</h3><ul>
<li><strong>«Flex Parent فضا را مدیریت می‌کند؛ Flex Item برای سهم خود مذاکره می‌کند.»</strong></li>
<li><strong>«فقط Child مستقیم Flex Item است.»</strong></li>
<li><strong>«Direction محور اصلی را می‌سازد؛ بقیهٔ کنترل‌ها نسبت به آن معنا می‌گیرند.»</strong></li>
<li><strong>«Alignment جای Size را نمی‌گیرد.»</strong></li>
<li><strong>«Flex برای توالی یک‌بعدی است؛ Grid برای نقشهٔ دوبعدی.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>CSS Flexible Box Layout Module</li>
<li>MDN: Basic concepts of flexbox</li>
<li>Elementor Help: Flexbox element</li>
<li>Elementor Help: Understanding how Flexbox containers work</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-5-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-5-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Flexbox؛ موتور با keyword کار می‌کند، فاصله با طول</span></summary>
<section aria-labelledby="lesson-5-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">برای فعال‌کردن Flex عدد لازم نیست. display:flex یک keyword است؛ بعد از آن Gap، Width و Basis می‌توانند واحد بگیرند.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> ابتدا ریل قطار را انتخاب می‌کنی؛ ریل «۲۰ پیکسل» نیست. فاصلهٔ واگن‌ها و طول آن‌هاست که اندازه می‌گیرد.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Display</th><td><code dir="ltr">display</code></td><td>flex</td><td>keyword</td><td>فعال‌کردن موتور Flex.</td><td>Flex را با مقدار width فعال نمی‌کنی.</td><td><code dir="ltr">E_LAYOUT</code></td></tr><tr><th scope="row">Direction</th><td><code dir="ltr">flex-direction</code></td><td>row / column / reverse</td><td>keyword</td><td>انتخاب main axis.</td><td>واحد طول روی Direction معنا ندارد.</td><td><code dir="ltr">E_LAYOUT</code></td></tr><tr><th scope="row">Gap</th><td><code dir="ltr">gap</code></td><td>PX، %، VW در Help Center Flexbox</td><td>Parent size / viewport برحسب واحد</td><td>فاصلهٔ رابطه‌ای بین childها.</td><td>Gap درصدی همراه Width درصدی می‌تواند جمع را از 100% عبور دهد.</td><td><code dir="ltr">E_FLEX_GAP</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>دو Child با width:50% به‌علاوه gap:5% مجموعاً 105% می‌شوند. برای بدون Wrap، نمونهٔ رسمی 47.5% + 5% + 47.5% = 100% است.</p></section>
<section><h3>📱 در Responsive</h3><p>Direction می‌تواند keyword متفاوت بگیرد و Gap مقدار متفاوت؛ لازم نیست واحد همهٔ کنترل‌ها تغییر کند.</p></section>
<section><h3>🔬 در DevTools</h3><p>display، flex-direction و gap را روی Parent و width/basis را روی Child بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Layout</a>، <a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a>، <a href="https://elementor.com/help/container-layout-tab-settings/" rel="noopener noreferrer" target="_blank">Elementor — Container layout settings</a>، <a href="https://www.w3.org/TR/css-flexbox-1/" rel="noopener noreferrer" target="_blank">W3C — CSS Flexible Box Layout</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-5-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-5-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA</h3><p>Element: Platform Main<br/>
کلاس هدف ویرایش: <code class="inline-code" dir="ltr">c-platform-main</code></p><p>مسیر کلی:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Style → Layout → Direction: Row</pre></figure></details><p>دو Child فعلی باید کنار هم قرار بگیرند.</p><p>فعلاً:</p><section aria-labelledby="section-hidden-88-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-88-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Direction</dt><dd>Row</dd><dt>Justify</dt><dd>Start</dd><dt>Align</dt><dd>Stretch یا حالت پیش‌فرض</dd><dt>Gap</dt><dd>موقت و کم</dd></dl></section><h3>چرا هنوز Space Between نه؟</h3><p>چون اندازهٔ ستون‌ها را تعیین نمی‌کند؛ فقط فضای آزاد را توزیع می‌کند.</p><h3>❓ سؤال توقف</h3><p>اگر Direction را Column کنی، Copy و Visual چه می‌شوند؟</p><details class="disclosure-card"><summary>پاسخ</summary>زیر هم قرار می‌گیرند.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> برای کنارهم‌گذاشتن ستون‌ها از Margin بزرگ استفاده کنی.</p><p><strong>نشانه:</strong> فاصله فقط در یک عرض درست است.</p><h3>🧪 عمداً خرابش کن</h3><p>Platform Visual را Absolute کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>Visual از Flow خارج می‌شود؛</li>
<li>ممکن است روی Copy بیفتد؛</li>
<li>ارتفاع Main فقط با Copy محاسبه شود؛</li>
<li>Mobile نیاز به Offsetهای دستی پیدا کند.</li>
</ul><p>Position را به حالت عادی برگردان.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-89-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-89-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-25"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-25-1" name="chk-25-1" type="checkbox"/><span>Copy و Visual کنار هم‌اند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-25-2" name="chk-25-2" type="checkbox"/><span>هر دو Child مستقیم Main هستند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-25-3" name="chk-25-3" type="checkbox"/><span>هیچ‌کدام Absolute نیستند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-25-4" name="chk-25-4" type="checkbox"/><span>Layout با Row ساخته شده</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Main Axis در Flexbox چیست؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> دو بخش در Mobile باید زیر هم قرار بگیرند. کدام Parent و کدام Control را بررسی می‌کنی؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-26"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-26-1" name="chk-26-1" type="checkbox"/><span>Parent دارای دو فرزند مستقیم را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-26-2" name="chk-26-2" type="checkbox"/><span>Flexbox و Direction را براساس یک‌بعدی‌بودن مسئله انتخاب کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-26-3" name="chk-26-3" type="checkbox"/><span>برای ستون‌های اصلی از Absolute یا Margin بزرگ استفاده نکرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-5-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-5-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-HYBRID-001</h3><p><strong>هدف:</strong> 👁 فقط مشاهده کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">legacy_or_hybrid</code></p><p>در یک Subtree، V4 Flexbox و عناصر Legacy کنار هم دیده می‌شوند. Hybrid بودن، Flexbox اصلی را خودبه‌خود نامعتبر نمی‌کند.</p><h3>🔬 پشت صحنه</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text language-css" dir="ltr">display: flex;
flex-direction: row;
</code></pre><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="memory-flex-display-heading" role="heading">🧠 لایهٔ حافظه — Div، Display و Flex</span></summary><section aria-labelledby="memory-flex-display-heading" class="memory-layer disclosure-content lesson-section"><p><strong>🧠 استعارهٔ ماندگار:</strong> Div یک ظرف خام است؛ Display به ظرف می‌گوید با بچه‌هایش چگونه رفتار کند؛ Flexbox موتور چیدمان یک‌بعدی است.</p><p><strong>👁 نمای تصویری / HTML Diagram:</strong> Parent با <code dir="ltr">display:flex</code> یک ریل می‌سازد و Childها روی همان ریل می‌نشینند.</p><p><strong>🧩 در Elementor V4 یعنی چه؟</strong> Div Block را برای گروه‌بندی سبک بساز؛ Flexbox Container را وقتی انتخاب کن که چیدمان یک‌محوره می‌خواهی.</p><p><strong>⚠️ تله رایج:</strong> Absolute کردن Copy و Visual فقط برای کنار هم گذاشتن، Flow را می‌شکند.</p><p class="golden-rule"><strong>📜 قانون طلایی:</strong> اول موتور چیدمان را انتخاب کن؛ بعد اندازه و فاصله را تنظیم کن.</p><details class="more-know"><summary>بیشتر بدانید</summary><p>Flexbox جایگزین بسیاری از hackهای قدیمی float و margin شد، چون خود والد می‌تواند جهت، تراز، فاصله و رفتار childها را کنترل کند.</p></details></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-5-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-5-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-28"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-28-1" name="chk-28-1" type="checkbox"/><span>می‌توانی توضیح بدهی چرا Main Layout پروژهٔ TUYA یک مسئلهٔ یک‌بعدی است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-28-2" name="chk-28-2" type="checkbox"/><span>می‌توانی Main Axis و Cross Axis را روی Row و Column مشخص کنی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-29"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-29-1" name="chk-29-1" type="checkbox"/><span>Copy و Visual را با یک Flexbox Row و بدون Absolute کنار هم قرار می‌دهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-29-2" name="chk-29-2" type="checkbox"/><span>Direction را به Column تغییر می‌دهی و نتیجه را پیش از اجرا پیش‌بینی می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-30"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-30-1" name="chk-30-1" type="checkbox"/><span>برای یک Header جدید می‌توانی تشخیص بدهی Flexbox مناسب است یا Grid و دلیل را بگویی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-5-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-5-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد ریل، تراز و فاصلهٔ بین دو ستون را تنظیم می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 5</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-5-completion"><fieldset><legend>ثبت پایان درس 5</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-5-complete" name="lesson-5-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details><details class="lesson-disclosure" id="lesson-5-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — دو ستون Desktop چگونه یک ستون Mobile می‌شوند؟</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>الگوی Desktop می‌تواند Row باشد، اما در Mobile همان parent به Column تبدیل شود. Elementor Direction را برای هر breakpoint مستقل می‌پذیرد.</p>
<p><strong>برای TUYA:</strong> Visual، Copy و Logo Strip باید در یک جریان عمودی قابل کنترل قرار بگیرند؛ تنها Nodeهای داخل Visual Stage نیازمند overlay هستند.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-5-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: دو ستون Desktop به یک ستون Mobile</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> یک layout را با Direction responsive بازچینی کن، نه با ساخت نسخهٔ دوم.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>Main را در Desktop روی Row و دو child را کنار هم قرار بده.</li><li>در Tablet رفتار inherited را مشاهده کن و فقط اگر شکست رخ داد override بده.</li><li>در Mobile Direction را Column کن و Width فرزندان را بازبینی کن.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن کدام Width یا Basis دسکتاپ پس از Column شدن دیگر معنای مناسبی ندارد.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>Direction را Column کن اما Width هر child را روی 50% نگه دار.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>Direction، Width، Flex Basis و Used Width هر child در سه breakpoint.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> Mobile تک‌ستونه است، فرزندان عرض منطقی دارند و Desktop تغییر نکرده است.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-5-responsive-build-test-done-build"><input data-persist="" id="lesson-5-responsive-build-test-done-build" name="lesson-5-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-5-responsive-build-test-done-test"><input data-persist="" id="lesson-5-responsive-build-test-done-test" name="lesson-5-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-5-responsive-build-test-done-debug"><input data-persist="" id="lesson-5-responsive-build-test-done-debug" name="lesson-5-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-5-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-5-responsive-build-test-note" name="lesson-5-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/responsive-design-using-containers/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-5-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Flex container و gap</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
