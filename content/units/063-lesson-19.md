<article class="lesson card-surface" data-lesson="19" id="lesson-19"><h2 class="lesson-title former-h1">درس 19 — Refactor واقعی صفحهٔ Solutions</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-19-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-19-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> یک Refactor واقعی را از Observation تا Verification اجرا کنی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> ادعای خرابی بدون Runtime را.</p><p><strong>در پایان باید بتوانی:</strong> Cardهای Absolute و Styleهای تکراری را به Pattern قابل نگهداری تبدیل کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-19-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-19-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🔧 Refactor + 🔍 عیب‌یابی + ⚖ مقایسه</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۴۵–۶۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> قبل و بعد با Long Text و Zoom مقایسه می‌شوند.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-19-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-19-lesson-understand-4">A. بفهم</h2><h3>پروندهٔ اصلی</h3><p><code class="inline-code" dir="ltr">CASE-SOL-ABS-001</code></p><p>Export نشان می‌دهد هشت Card:</p><ul>
<li>Parent Relative دارند؛</li>
<li>Icon Absolute است؛</li>
<li>Heading و Paragraph نیز با Offset ثابت Absolute هستند؛</li>
<li>Styleهای تکراری دارند.</li>
</ul><h3>تفسیر درست</h3><section aria-labelledby="section-hidden-273-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-273-heading">بخش آموزشی</h2><ul><li>exported fact:</li>
<li>Position و offsets ذخیره شده‌اند</li>
<li>proposed refactor:</li>
<li>Text به Normal Flow برگردد</li>
<li>not proven:</li>
<li>Runtime defect</li></ul></section><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="50e21efba96b9624bc1bee10a3e9ba3e1d576b86c437e1602d87d1ac8c444e33" id="lesson-19-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Refactor؛ تغییر ساختار بدون گم‌کردن رفتار</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="25" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-25-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-25-section-01">مسئله‌ای که Refactor حل می‌کند</h3><p>یک صفحه ممکن است ظاهراً درست باشد اما پشت آن:</p><ul>
<li>Wrapperهای اضافی</li>
<li>Classهای تکراری</li>
<li>Valueهای خام پراکنده</li>
<li>Custom CSSهای جبرانی</li>
<li>Duplicateهای Desktop/Mobile</li>
<li>Componentهای مشابه</li>
</ul><p>وجود داشته باشد.</p><p>Refactor یعنی ساختار داخلی را بهتر کنی، بدون اینکه رفتار مورد انتظار را ناخواسته بشکنی.</p><hr/></section><section aria-labelledby="concept-v31-25-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-25-section-02">تشبیه به دنیای واقعی: بازسازی لوله‌کشی بدون قطع آب</h3><p>خانه کار می‌کند، اما لوله‌ها پیچیده و تکه‌تکه‌اند. Refactor یعنی مسیر لوله را ساده کنی، اتصالات اضافی را حذف کنی و شیرهای مرکزی بسازی—درحالی‌که آب باید همچنان به همه اتاق‌ها برسد.</p><p>ظاهر یکسان کافی نیست. فشار آب، ایمنی و تعمیرپذیری نیز باید حفظ شوند.</p><hr/></section><section aria-labelledby="concept-v31-25-section-03" class="concept-reference-part"><h3 id="concept-v31-25-section-03">Refactor با Redesign فرق دارد</h3><h4>Refactor</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">هدف: حفظ رفتار، بهبود ساختار
</code></pre></figure><h4>Redesign</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">هدف: تغییر تجربه یا ظاهر
</code></pre></figure><p>اگر هنگام حذف Wrapper، فاصله یا ترتیب Mobile را عمداً تغییر می‌دهی، شاید کار دیگر Refactor خالص نیست. تغییرات را نام‌گذاری کن تا دامنه کار مبهم نشود.</p><hr/></section><section aria-labelledby="concept-v31-25-section-04" class="concept-reference-part"><h3 id="concept-v31-25-section-04">نقشه Refactor</h3><h4>تکرار Value</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">#004526 در 18 نقطه
</code></pre></figure><p>→ Variable را بررسی کن.</p><h4>تکرار Style</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">همان Button Style در 12 Element
</code></pre></figure><p>→ Global Class را بررسی کن.</p><h4>تکرار Structure</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">همان Card Tree در 8 صفحه
</code></pre></figure><p>→ Component را بررسی کن.</p><h4>Wrapper بدون مسئولیت</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Div فقط یک Child دارد و Layout/Style/Meaning نمی‌دهد
</code></pre></figure><p>→ حذف آزمایشی را بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-25-section-05" class="concept-reference-part"><h3 id="concept-v31-25-section-05">Wrapper چه زمانی اضافی نیست؟</h3><p>Wrapper ممکن است مسئولیت واقعی داشته باشد:</p><ul>
<li>Layout Parent</li>
<li>Containing Block</li>
<li>Stacking Context</li>
<li>Clip/Overflow Stage</li>
<li>Background Layer</li>
<li>Semantic Group</li>
<li>Container Query Context</li>
<li>Interaction Target</li>
</ul><p>پس «هر Wrapper کمتر بهتر» قانون ناقصی است.</p><p>از خودت بپرس:</p><blockquote>
<p>اگر این Wrapper را حذف کنم، کدام مسئولیت بی‌صاحب می‌شود؟</p>
</blockquote><p>اگر جواب «هیچ» است، کاندید حذف است.</p><hr/></section><section aria-labelledby="concept-v31-25-section-06" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-25-section-06">روش امن Refactor</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Baseline
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
Performance comparison
↓
Commit/record
</code></pre></figure><p>چند Refactor بزرگ را هم‌زمان انجام نده؛ پیدا کردن علت Regression سخت می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-25-section-07" class="concept-reference-part"><h3 id="concept-v31-25-section-07">Baseline چیست؟</h3><p>پیش از تغییر ثبت کن:</p><ul>
<li>Screenshot عرض‌های اصلی</li>
<li>Computed Style Elementهای حساس</li>
<li>ترتیب DOM</li>
<li>مسیر Keyboard</li>
<li>Form behavior</li>
<li>Dynamic data cases</li>
<li>Performance trace یا حداقل Metric پایه</li>
</ul><p>Baseline حافظه قابل اعتماد است؛ ذهن انسان جزئیات فاصله و رفتار را دقیق نگه نمی‌دارد.</p><hr/></section><section aria-labelledby="concept-v31-25-section-08" class="concept-reference-part"><h3 id="concept-v31-25-section-08">Local به Global</h3><p>اگر یک Local Style در چند محل تکرار شده، فقط Copy/Paste نکن. Intent مشترک را پیدا کن.</p><p>بد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">همه سبز و 16px هستند، پس یک Class
</code></pre></figure><p>بهتر:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">همه Action Link اصلی‌اند، پس action-link-primary
</code></pre></figure><p>شباهت عددی همیشه به معنای هویت مشترک نیست.</p><hr/></section><section aria-labelledby="concept-v31-25-section-09" class="concept-reference-part"><h3 id="concept-v31-25-section-09">Variant Extraction</h3><p>دو Component تقریباً یکسان‌اند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Card Light
Card Dark
</code></pre></figure><p>اگر فقط Surface و Text Color فرق دارند، Base + Variant Class را بررسی کن.</p><p>اگر Structure، Interaction یا Property Contract فرق دارد، ادغام ممکن است معماری را پیچیده‌تر کند.</p><hr/></section><section aria-labelledby="concept-v31-25-section-10" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-25-section-10">در Elementor V4</h3><p>ابزارهای مفید:</p><ul>
<li>Class Manager برای Classهای Empty/Unused و Priority</li>
<li>Variables Manager برای Valueهای مرکزی</li>
<li>Component Master برای ساختار تکراری</li>
<li>Navigator/Tree برای Wrapperها</li>
<li>DevTools برای CSS واقعی</li>
</ul><p>Refactor را فقط در Editor انجام نده؛ Frontend و Data Dynamic را نیز بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-25-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-25-section-11">اشتباهات رایج</h3><ul>
<li>حذف Wrapper فقط برای کاهش Node</li>
<li>ادغام Classهای صرفاً هم‌رنگ</li>
<li>ساخت Variable برای هر Literal</li>
<li>تبدیل همه چیز به Component</li>
<li>Refactor و Redesign هم‌زمان</li>
<li>تغییر Master بدون Baseline</li>
<li>اعتماد به Screenshot Desktop</li>
<li>حذف Class «بدون استفاده» بدون بررسی دامنه</li>
<li>ادعای بهبود Performance بدون اندازه‌گیری</li>
</ul><hr/></section><section aria-labelledby="concept-v31-25-section-12" class="concept-reference-part"><h3 id="concept-v31-25-section-12">تمرین علت‌یابی معکوس</h3><p>روی Duplicate صفحه، هر بار یک خطای کنترل‌شده بساز:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Direction را عوض کن
Min Width ضروری را حذف کن
Overflow Hidden اضافه کن
Wrapper مسئول را حذف کن
</code></pre></figure><p>سپس بدون نگاه فوری به نسخه سالم، علت شکست را با Tree و Computed Style توضیح بده. هدف خراب‌کردن پروژه نیست؛ هدف دیدن مسئولیت هر قطعه است.</p><hr/></section><section aria-labelledby="concept-v31-25-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-25-section-13">تصویر ذهنی نهایی</h3><p>Refactor بازسازی لوله‌کشی خانه‌ای است که هنوز باید آب داشته باشد. حذف هر لوله خوب نیست؛ فقط لوله‌ای را حذف کن که مسئولیتی ندارد یا مسیرش با سیستم مرکزی جایگزین شده است.</p><hr/></section><section aria-labelledby="concept-v31-25-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-25-section-14">قوانین طلایی</h3><ul>
<li><strong>«Refactor رفتار را حفظ می‌کند؛ Redesign رفتار را تغییر می‌دهد.»</strong></li>
<li><strong>«هر Wrapper را با مسئولیتش قضاوت کن، نه فقط با تعداد Node.»</strong></li>
<li><strong>«شباهت عددی لزوماً هویت مشترک نیست.»</strong></li>
<li><strong>«یک تغییر کوچک، یک مقایسه روشن.»</strong></li>
<li><strong>«بدون Baseline، Refactor قابل اثبات نیست.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: V4 classes, variables, components and performance guidance</li>
<li>Chrome DevTools CSS and performance references</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-19-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-19-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Refactor؛ واحد را با intent استاندارد کن، نه با سلیقه</span></summary>
<section aria-labelledby="lesson-19-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">هدف Refactor تبدیل همه‌چیز به rem یا px نیست. باید واحدهایی را انتخاب کنی که مرجع محاسبه‌شان با intent طراحی سازگار است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> بازسازی انبار یعنی هر ابزار در قفسهٔ درست، نه اینکه همهٔ ابزارها را یک‌رنگ کنی.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Spacing scale</th><td><code dir="ltr">padding / gap / margin</code></td><td>معمولاً px/rem/variables</td><td>root یا context</td><td>Scale محدود و نام‌گذاری‌شده.</td><td>واحدهای مخلوط بدون دلیل نگه ندار.</td><td><code dir="ltr">E_VAR_MANAGER</code></td></tr><tr><th scope="row">Layout width</th><td><code dir="ltr">width / max-width</code></td><td>%، px/rem، viewport</td><td>Parent/root/viewport</td><td>Width سیال + سقف معنادار.</td><td>100vw داخل wrapper می‌تواند overflow بسازد.</td><td><code dir="ltr">E_SIZE</code></td></tr><tr><th scope="row">Typography scale</th><td><code dir="ltr">font-size / line-height</code></td><td>rem/em/px/vw</td><td>root/parent/viewport</td><td>Scale خوانا و محدود.</td><td>فقط ظاهر Desktop را معیار نکن.</td><td><code dir="ltr">E_TYPO_GENERAL</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر 17 مقدار spacing پراکنده به 5 Size Variable تبدیل شوند، تعداد intentها کم می‌شود؛ این یک شاخص طراحی است، نه محاسبهٔ CSS.</p></section>
<section><h3>📱 در Responsive</h3><p>قبل و بعد Refactor در Desktop/Tablet/Mobile و frontend مقایسه شود.</p></section>
<section><h3>🔬 در DevTools</h3><p>فهرست واحدها، duplicate values و matched sources را audit کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/variables-manager/" rel="noopener noreferrer" target="_blank">Elementor V4 — Variables Manager</a>، <a href="https://elementor.com/help/style-tab-size/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Size</a>، <a href="https://elementor.com/help/what-is-typography/" rel="noopener noreferrer" target="_blank">Elementor — Typography and units</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-19-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-19-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🔧 Refactor مرحله‌ای</h3><p>هدف این Case Study: <strong>بازسازی کن</strong>.</p><ol>
<li>از Card فعلی Screenshot بگیر؛</li>
<li>یک V4 Card جدید در Staging بساز؛</li>
<li>Card را Flexbox Column کن؛</li>
<li>Icon را Overlay یا Item عادی انتخاب کن؛</li>
<li>Heading و Paragraph را در Normal Flow قرار بده؛</li>
<li>Gap و Padding را جایگزین Offsetهای متن کن؛</li>
<li>Style مشترک را Global Class کن؛</li>
<li>Long Text و Zoom را تست کن؛</li>
<li>Desktop، Tablet و Mobile را مقایسه کن.</li>
</ol><h3>❓ سؤال توقف</h3><p>کدام Element احتمالاً می‌تواند Absolute باقی بماند: Icon تزئینی یا Paragraph؟</p><details class="disclosure-card"><summary>پاسخ</summary>Icon تزئینی.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> Refactor را فقط براساس شباهت Screenshot تأیید کنی.</p><p><strong>تست لازم:</strong> Content growth، Keyboard، Zoom و Responsive.</p><h3>🧪 عمداً خرابش کن</h3><p>Paragraph را دو برابر طولانی کن و Font Size را افزایش بده.</p><h4>👀 انتظار در نسخهٔ Absolute</h4><ul>
<li>برخورد با Element بعدی؛</li>
<li>خروج از Card؛</li>
<li>نیاز به تغییر Offset.</li>
</ul><h4>👀 انتظار در نسخهٔ Flow</h4><ul>
<li>Card بلندتر می‌شود؛</li>
<li>محتوا جای طبیعی خود را حفظ می‌کند؛</li>
<li>فاصله با Gap/Padding کنترل می‌شود.</li>
</ul><h3>Checkpoint</h3><section aria-labelledby="section-hidden-275-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-275-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-108"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-108-1" name="chk-108-1" type="checkbox"/><span>قبل و بعد ثبت شده</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-108-2" name="chk-108-2" type="checkbox"/><span>Text در Flow است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-108-3" name="chk-108-3" type="checkbox"/><span>Icon تصمیم آگاهانه دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-108-4" name="chk-108-4" type="checkbox"/><span>Style مشترک تکرار نشده</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-108-5" name="chk-108-5" type="checkbox"/><span>Long Text و Zoom تست شده</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> چرا متن عادی معمولاً باید در Flow باشد؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> Paragraph کارت دو برابر طولانی شده است. تفاوت رفتار نسخهٔ Absolute و Flow را پیش‌بینی کن.</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-109"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-109-1" name="chk-109-1" type="checkbox"/><span>Fact صادرشده را از Refactor پیشنهادی جدا کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-109-2" name="chk-109-2" type="checkbox"/><span>متن عادی را در Normal Flow نگه داشته است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-109-3" name="chk-109-3" type="checkbox"/><span>Long Text، Zoom و Device Size را برای اثبات مقایسه کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-19-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-19-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-IMAGE-001 و CASE-SOL-REUSE-001</h3><p><strong>هدف:</strong> ⚖️ مقایسه و 🔧 بازسازی</p><p>بعد از Card متنی، Image Cardها را بررسی کن:</p><ul>
<li>Current height constraints؛</li>
<li>Aspect Ratio alternative؛</li>
<li>Cover و Object Position؛</li>
<li>Global Card classes؛</li>
<li>Badge overlay.</li>
</ul><p>نتیجهٔ نهایی را فقط پس از Runtime ثبت کن.</p><h3>🔬 پشت صحنه</h3><p>این Refactor نمونهٔ ترکیب Normal Flow، Overlay تزئینی و Global Class است.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-19-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-19-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-111"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-111-1" name="chk-111-1" type="checkbox"/><span>می‌توانی Fact ذخیره‌شده را از Refactor پیشنهادی و خرابی اثبات‌شده جدا کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-111-2" name="chk-111-2" type="checkbox"/><span>می‌توانی توضیح بدهی چرا متن عادی معمولاً باید در Flow باقی بماند.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-112"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-112-1" name="chk-112-1" type="checkbox"/><span>Cardهای Solutions را با متن در Flex Column و Icon با تصمیم آگاهانه Refactor می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-112-2" name="chk-112-2" type="checkbox"/><span>Long Text، Zoom و سه Device Size را برای قبل و بعد ثبت می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-113"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-113-1" name="chk-113-1" type="checkbox"/><span>در یک Card تازه می‌توانی مشخص کنی کدام Overlay تزئینی و کدام محتوا باید در Flow باشد.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-19-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-19-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد صفحه را از نظر DOM، رسانه، Class و عملکرد Audit می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 19</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-19-completion"><fieldset><legend>ثبت پایان درس 19</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-19-complete" name="lesson-19-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details><details class="lesson-disclosure design-system-decision" id="lesson-19-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Refactor صفحهٔ Solutions</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
