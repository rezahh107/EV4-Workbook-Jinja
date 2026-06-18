<article class="lesson card-surface" data-lesson="18" id="lesson-18"><h2 class="lesson-title former-h1">درس 18 — صفحات Hybrid V3/V4 و نردبان مهاجرت</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-18-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-18-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> Hybrid را تشخیص بدهی و مهاجرت کنترل‌شده انجام دهی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تبدیل خودکار کل سایت یا حذف فوری V3 را.</p><p><strong>در پایان باید بتوانی:</strong> یک بخش Legacy را در Staging به V4 بازسازی و مقایسه کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-18-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-18-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟣 پروژه‌ای</td></tr><tr><th scope="row">نوع فعالیت</th><td>🔍 تحلیل + 🔧 مهاجرت + ⚖ مقایسه</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۶۰–۹۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۳۰–۴۵ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> بهتر است در دو جلسه انجام شود.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-18-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-18-lesson-understand-4">A. بفهم</h2><h3>اصل مهم</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Hybrid ≠ Invalid
Legacy ≠ Immediately wrong
V4 refactor = controlled project</pre></figure></details><p>V3 و V4 می‌توانند در یک صفحه هم‌زیستی داشته باشند. هدف دوره شناخت و Refactor آگاهانه است.</p><h3>نردبان مهاجرت</h3><section aria-labelledby="section-hidden-260-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-260-heading">بخش آموزشی</h2><ul><li>1. عنصر Legacy را تشخیص بده</li>
<li>2. نقش واقعی آن را مشخص کن</li>
<li>3. معادل V4 را انتخاب کن</li>
<li>4. در Staging یک نمونه بساز</li>
<li>5. Content و Dynamic Data را منتقل کن</li>
<li>6. Desktop را مقایسه کن</li>
<li>7. Tablet و Mobile را مقایسه کن</li>
<li>8. Accessibility را بررسی کن</li>
<li>9. فقط پس از تأیید جایگزین کن</li></ul></section><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="a0193ee736b3b06a742bc91b2e0e6382fffa9ba34f1b2cd9425446975c0de3ad" id="lesson-18-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Hybrid V3/V4؛ مهاجرت بدون بازسازی کور</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="18" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-18-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-18-section-01">مسئله‌ای که مهاجرت حل می‌کند</h3><p>یک سایت واقعی ممکن است شامل این موارد باشد:</p><ul>
<li>Widgetهای V3</li>
<li>Atomic Elementهای V4</li>
<li>Add-onهای شخص ثالث</li>
<li>Custom CSS وابسته به DOM قدیمی</li>
<li>Dynamic Tagها</li>
<li>فرم‌ها</li>
<li>Templateهای Theme Builder</li>
<li>صفحه‌های تجاری حساس</li>
</ul><p>مهاجرت یک دکمهٔ «قدیمی را جدید کن» نیست. مهاجرت مدیریت ریسک است.</p><hr/></section><section aria-labelledby="concept-v31-18-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-18-section-02">تشبیه به دنیای واقعی: بازسازی بیمارستان در حال کار</h3><p>یک بیمارستان را نمی‌توان یک‌شبه تعطیل و از نو ساخت. بعضی بخش‌ها جدید می‌شوند، بعضی موقتاً قدیمی می‌مانند و مسیرهای اتصال باید حفظ شوند.</p><ul>
<li>V3 = بال قدیمی اما فعال</li>
<li>V4 = بال جدید</li>
<li>Hybrid = راهروی اتصال</li>
<li>Staging = ماکت و محیط آزمایش</li>
<li>Rollback = مسیر بازگشت اضطراری</li>
</ul><p>هدف فقط نوکردن ساختمان نیست؛ خدمات باید حین تغییر ادامه پیدا کند.</p><hr/></section><section aria-labelledby="concept-v31-18-section-03" class="concept-reference-part"><h3 id="concept-v31-18-section-03">هم‌زیستی V3 و V4</h3><p>مستندات رسمی V4 تصریح می‌کنند Elementهای V4 و Widgetهای 3.x می‌توانند در یک صفحه کنار هم استفاده شوند.</p><p>این یعنی وجود هر دو ساختار به‌خودی‌خود خطا نیست. Hybrid یک مرحلهٔ معتبر است.</p><p>اما هم‌زیستی می‌تواند مسائل تازه بسازد:</p><ul>
<li>دو مدل Style</li>
<li>Global Colors/Fonts در برابر Variables</li>
<li>DOM متفاوت</li>
<li>کنترل‌های Responsive متفاوت</li>
<li>رفتار Add-onها</li>
<li>Custom CSS وابسته به Selector قدیمی</li>
</ul><hr/></section><section aria-labelledby="concept-v31-18-section-04" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-18-section-04">ماتریس تصمیم مهاجرت</h3><h4>سؤال ۱: Feature Parity وجود دارد؟</h4><p>آیا Element V4 تمام قابلیت لازم Widget قدیمی را دارد؟</p><h4>سؤال ۲: وابستگی شخص ثالث چیست؟</h4><p>Add-on، Script، Tracking یا Custom JS به Markup قدیمی وابسته است؟</p><h4>سؤال ۳: صفحه چقدر حساس است؟</h4><p>صفحهٔ پرداخت یا Landing Page پرفروش نیازمند آزمایش و Rollback قوی‌تر است، نه لزوماً ممنوعیت مهاجرت.</p><h4>سؤال ۴: Baseline داریم؟</h4><p>قبل از تغییر:</p><ul>
<li>Screenshot</li>
<li>Core Web Vitals/Lab Metrics</li>
<li>رفتار فرم</li>
<li>مسیر Keyboard</li>
<li>Dynamic Data</li>
<li>Conversion events</li>
</ul><p>ثبت شده‌اند؟</p><h4>خروجی تصمیم</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Keep V3
Hybridize
Pilot one section
Rebuild new page in V4
Full migration after verification
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-18-section-05" class="concept-reference-part"><h3 id="concept-v31-18-section-05">چه زمانی Pilot مناسب است؟</h3><p>یک Section کم‌ریسک انتخاب کن که:</p><ul>
<li>ساختار تکرارشونده دارد؛</li>
<li>Add-on پیچیده ندارد؛</li>
<li>Dynamic Data حساس ندارد؛</li>
<li>در چند Viewport قابل مقایسه است.</li>
</ul><p>آن را در V4 بازسازی کن و نتیجه را با نسخه قبلی مقایسه کن.</p><hr/></section><section aria-labelledby="concept-v31-18-section-06" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-18-section-06">چرا «V4 همیشه سریع‌تر است» ادعای خوبی نیست؟</h3><p>Atomic Architecture می‌تواند DOM و Style System ساده‌تری بسازد، اما Performance نهایی به پیاده‌سازی بستگی دارد:</p><ul>
<li>تعداد Elementها</li>
<li>تصاویر</li>
<li>Scriptها</li>
<li>Interactions</li>
<li>Fontها</li>
<li>Add-onها</li>
<li>Server</li>
<li>Cache</li>
</ul><p>پس باید Benchmark کرد، نه اینکه از نام نسخه نتیجه گرفت.</p><hr/></section><section aria-labelledby="concept-v31-18-section-07" class="concept-reference-part"><h3 id="concept-v31-18-section-07">Sync میان مدل‌های Design System</h3><p>V3 از Global Colors/Fonts و V4 از Variables/Classes استفاده می‌کند. Elementor امکان Sync برخی Variableها با Global Assets را ارائه می‌کند.</p><p>اما Sync به این معنی نیست که تمام قابلیت‌ها و دامنه‌ها یکسان‌اند. مثلاً محدودیت نوع Variable یا ویژگی‌های Typography باید طبق نسخه هدف بررسی شود.</p><hr/></section><section aria-labelledby="concept-v31-18-section-08" class="concept-reference-part"><h3 id="concept-v31-18-section-08">Custom CSS و DOM قدیمی</h3><p>Selector زیر ممکن است به Markup خاص V3 وابسته باشد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.elementor-widget-container &gt; .some-inner-wrapper
</code></pre></figure><p>اگر V4 Wrapperها یا Classها را تغییر دهد، CSS می‌شکند.</p><p>قبل از مهاجرت، Custom CSS را دسته‌بندی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Selector پایدار و معنایی
Selector وابسته به DOM داخلی
!importantهای زیاد
JS querySelector وابسته به Class قدیمی
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-18-section-09" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-18-section-09">مسیر عملی مهاجرت</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Inventory
↓
Dependency Map
↓
Baseline
↓
Pilot
↓
Visual/Functional/Accessibility/Performance Regression
↓
Rollback test
↓
مرحله بعد
</code></pre></figure><p>هر workaround باید نسخه، تاریخ، Plugin و شرایط بازتولید داشته باشد. Workaround بدون نسخه به‌سرعت تبدیل به افسانه می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-18-section-10" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-18-section-10">اشتباهات رایج</h3><ul>
<li>بازسازی کل سایت بدون Pilot</li>
<li>فرض سازگاری Add-onها</li>
<li>حذف V3 فقط برای «تمیزشدن»</li>
<li>مهاجرت صفحه حساس بدون Rollback</li>
<li>مقایسه Performance با یک اجرای Lighthouse</li>
<li>فراموش‌کردن Dynamic Data و فرم</li>
<li>اعتماد به Preview بدون Frontend Test</li>
<li>ترکیب خاموش قواعد V3 و V4</li>
</ul><hr/></section><section aria-labelledby="concept-v31-18-section-11" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-18-section-11">تصویر ذهنی نهایی</h3><p>مهاجرت V3 به V4 بازسازی بیمارستان فعال است. هر بخش باید مستقل بررسی شود، راهروهای اتصال شناخته شوند و مسیر بازگشت باز بماند.</p><hr/></section><section aria-labelledby="concept-v31-18-section-12" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-18-section-12">قوانین طلایی</h3><ul>
<li><strong>«Hybrid شکست نیست؛ مرحلهٔ معتبر مهاجرت است.»</strong></li>
<li><strong>«صفحه حساس مهاجرت‌ناپذیر نیست؛ فقط شواهد و کنترل بیشتری می‌خواهد.»</strong></li>
<li><strong>«Feature Parity و Add-on Compatibility را پیش از بازسازی بررسی کن.»</strong></li>
<li><strong>«Performance را اندازه بگیر؛ از نام نسخه حدس نزن.»</strong></li>
<li><strong>«هر مهاجرت بدون Baseline و Rollback یک قمار است.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Get started with Editor V4 and V3/V4 coexistence</li>
<li>Elementor Developers: Editor 4.0 update</li>
<li>Elementor Help: Sync variables and global elements</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-18-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-18-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Hybrid V3/V4؛ واحدها را هنگام مهاجرت کورکورانه یکی نکن</span></summary>
<section aria-labelledby="lesson-18-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">کنترل V3 و V4 ممکن است ظاهر یا واحدهای در دسترس متفاوت داشته باشد. هدف مهاجرت حفظ رفتار computed است، نه صرفاً کپی عدد.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> دو نقشه با مقیاس متفاوت داری؛ عدد 10 روی هر دو الزاماً فاصلهٔ یکسان نمی‌سازد.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">V3 control</th><td><code dir="ltr">legacy widget setting</code></td><td>واحدهای همان کنترل</td><td>نسخه/Widget</td><td>ثبت قبل از مهاجرت.</td><td>از حافظه واحد را حدس نزن.</td><td><code dir="ltr">E_DIFF</code></td></tr><tr><th scope="row">V4 control</th><td><code dir="ltr">standard Style controls</code></td><td>واحدهای مستند همان کنترل</td><td>Element/Class</td><td>بازسازی intent با Class/Variable.</td><td>ظاهر برابر لزوماً declaration برابر نیست.</td><td><code dir="ltr">E_DIFF</code></td></tr><tr><th scope="row">Computed output</th><td><code dir="ltr">used value</code></td><td>px یا keyword resolveشده</td><td>browser layout</td><td>معیار مقایسهٔ نهایی.</td><td>فقط screenshot کافی نیست.</td><td><code dir="ltr">CSS_VALUES</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر V3 padding=20px و V4 padding=1.25rem با root=16px باشد، اکنون برابرند؛ ولی با تغییر root دیگر الزاماً برابر نمی‌مانند.</p></section>
<section><h3>📱 در Responsive</h3><p>هر breakpoint را جدا مقایسه کن؛ inheritance V4 ممکن است با ذخیرهٔ قدیمی V3 متفاوت باشد.</p></section>
<section><h3>🔬 در DevTools</h3><p>قبل/بعد migration matched rules و computed values را ذخیره کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/" rel="noopener noreferrer" target="_blank">Elementor — Differences between Editor V3 and V4</a>، <a href="https://elementor.com/help/responsive-editing/" rel="noopener noreferrer" target="_blank">Elementor V4 — Responsive editing</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-18-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-18-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — تمرین مهاجرت مستقل</h3><p>پروژهٔ TUYA از ابتدا V4 است. برای تمرین، یک Legacy Icon List کوچک در صفحهٔ آزمایشی بساز یا از Export موجود استفاده کن.</p><p>معادل V4 پیشنهادی:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Flexbox Column
|
+-- Feature Item × N
    |
    +-- SVG
    +-- Paragraph</pre></figure></details><h3>❓ سؤال توقف</h3><p>آیا وجود یک Element/Widget آماده V3 در صفحه دلیل کافی برای بازسازی فوری کل صفحه است؟</p><details class="disclosure-card"><summary>پاسخ</summary>خیر.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> مهاجرت را فقط براساس برچسب نسخه انجام بدهی، بدون بررسی محتوا، Dynamic Data و Runtime.</p><h3>🧪 عمداً خرابش کن</h3><p>یک بخش Legacy را قبل از ثبت Screenshot و Responsive values حذف کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>مرجع مقایسه از دست می‌رود؛</li>
<li>جزئیات محتوا یا رفتار فراموش می‌شود؛</li>
<li>بازگشت سخت‌تر می‌شود.</li>
</ul><p>Undo کن و Migration Checklist را اجرا کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-262-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-262-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-102"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-102-1" name="chk-102-1" type="checkbox"/><span>Legacy و V4 را تشخیص می‌دهم</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-102-2" name="chk-102-2" type="checkbox"/><span>Hybrid را رد نمی‌کنم</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-102-3" name="chk-102-3" type="checkbox"/><span>Refactor در Staging انجام می‌شود</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-102-4" name="chk-102-4" type="checkbox"/><span>قبل/بعد در چند Width مقایسه شده</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Hybrid بودن یک صفحه به چه معناست؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> یک Icon List قدیمی سالم است. قبل از تبدیل آن به V4 چه مراحل و تست‌هایی لازم است؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-103"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-103-1" name="chk-103-1" type="checkbox"/><span>عنصر Legacy و نقش آن را قبل از مهاجرت ثبت کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-103-2" name="chk-103-2" type="checkbox"/><span>بازسازی را در Staging انجام داده و نسخهٔ قبلی را فوراً حذف نکرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-103-3" name="chk-103-3" type="checkbox"/><span>Desktop، Mobile، محتوا، Dynamic Data و Accessibility را مقایسه کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-18-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-18-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-HYBRID-001</h3><p><strong>هدف:</strong> 🔧 بازسازی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">legacy_or_hybrid</code></p><p>Subtree شامل e-flexbox، e-heading، e-paragraph، e-button و e-svg در کنار container، heading، text-editor و icon-list است.</p><p>تمرین: فقط یک زیرگروه کم‌خطر را با V4 بازسازی کن، نه کل بخش را یک‌باره.</p><h3>🔬 پشت صحنه</h3><p>Hybrid Document می‌تواند ساختارهای Saved متفاوت داشته باشد. دوره آن را به‌عنوان Evidence معتبر نگه می‌دارد.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-18-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-18-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-105"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-105-1" name="chk-105-1" type="checkbox"/><span>می‌توانی عنصر Legacy و V4 را در یک بخش Hybrid تشخیص بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-105-2" name="chk-105-2" type="checkbox"/><span>می‌توانی توضیح بدهی چرا Hybrid بودن به‌تنهایی خرابی نیست.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-106"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-106-1" name="chk-106-1" type="checkbox"/><span>یک عنصر Legacy را در Staging با معادل V4 بازسازی و Desktop/Mobile را مقایسه می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-106-2" name="chk-106-2" type="checkbox"/><span>قبل از حذف نسخهٔ قبلی، محتوا، Dynamic Data، Accessibility و Runtime را تأیید می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-107"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-107-1" name="chk-107-1" type="checkbox"/><span>برای یک Icon List قدیمی می‌توانی نردبان مهاجرت مرحله‌ای پیشنهاد بدهی، بدون بازسازی کورکورانهٔ کل صفحه.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-18-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-18-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>ایستگاه E کامل شد. Class System و Migration Ladder را یک‌بار با یک نمونهٔ کوچک اجرا کن.</p><hr/><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 18</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-18-completion"><fieldset><legend>ثبت پایان درس 18</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-18-complete" name="lesson-18-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-18-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Atomic Element در برابر Legacy Element/Widget آماده</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Atomic Element</h3><p>Atomic Element قطعهٔ سبک‌تر و سیستم‌پذیرتر V4 است: با Classes، Variables، States و ساختار قابل پیش‌بینی بهتر کار می‌کند.</p></section>
<section class="inline-compare-card"><h3>Legacy Element/Widget آماده</h3><p>Legacy Element/Widget آماده هنوز ممکن است لازم باشد، اما معمولاً ذهن V3 دارد: تنظیمات اختصاصی‌تر، رفتار کمتر کلاس‌محور و احتمال wrapper/markup بیشتر.</p><p class="golden-rule">قانون طلایی: در پروژهٔ جدید اول Atomic؛ برای قابلیت‌های غایب یا مهاجرت، Legacy با آگاهی.</p></section>
</div>
</section></details>
</article>
