<article class="lesson card-surface" data-lesson="14" id="lesson-14"><h2 class="lesson-title former-h1">درس 14 — Responsive Inheritance و Breakpointها</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-14-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-14-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> Responsive را به‌عنوان تغییر کنترل‌شدهٔ همان ساختار بفهمی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> ساخت Section جدا برای هر دستگاه را.</p><p><strong>در پایان باید بتوانی:</strong> TUYA را بدون Duplicate از Desktop به Mobile تبدیل کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-14-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-14-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🛠 اجرایی + 🔍 عیب‌یابی + 📱 چندعرضی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۴۰–۶۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> چند Viewport و یک DOM را هم‌زمان تست می‌کنی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-14-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-14-lesson-understand-4">A. بفهم</h2><h3>مدل ذهنی</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Base/Desktop value
      ↓
Tablet override if needed
      ↓
Mobile override if needed</pre></figure></details><p>Responsive یعنی همان DOM و همان Component با تنظیمات مناسب فضای موجود.</p><h3>Workflow</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Build base
Resize slowly
Observe first failure
Change minimum necessary control
Retest content and states</pre></figure></details><p>Breakpoint را براساس شکست محتوا انتخاب کن، نه صرفاً نام دستگاه.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="cc24056f7e6407318b1a69797588466a8bc599b98fd96caa368e4fc84da0a568" id="lesson-14-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Responsive؛ Inheritance، Override و Breakpoint</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="14" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-14-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-14-section-01">مسئله‌ای که Responsive حل می‌کند</h3><p>Responsive یعنی یک Layout بتواند با فضای متفاوت، محتوای متفاوت و روش تعامل متفاوت سازگار شود.</p><p>Responsive فقط این نیست که Desktop را کوچک کنی. گاهی در Mobile:</p><ul>
<li>Direction عوض می‌شود؛</li>
<li>اولویت محتوا تغییر می‌کند؛</li>
<li>دکمه تمام‌عرض می‌شود؛</li>
<li>Grid ستون کمتری می‌گیرد؛</li>
<li>Typography سیال می‌شود؛</li>
<li>تزئین حذف می‌شود.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-14-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-14-section-02">تشبیه به دنیای واقعی: آبشار و سدها</h3><p>Desktop را سرچشمهٔ آبشار تصور کن. مقدارها به مراحل پایین‌تر می‌ریزند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Desktop
  ↓
Tablet
  ↓
Mobile
</code></pre></figure><p>تا وقتی در Tablet یا Mobile مقدار مستقل نسازی، آب از بالا ادامه پیدا می‌کند.</p><p>وقتی در Mobile عدد تازه‌ای وارد می‌کنی، مثل ساختن سد است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Desktop: 40px
Tablet: inherit
Mobile: 16px ← سد محلی
</code></pre></figure><p>اگر Mobile را نیز دستی روی 40px بگذاری، ظاهراً فعلاً با Desktop برابر است، اما دیگر به Desktop متصل نیست. اگر Desktop بعداً 48px شود، Mobile همچنان 40px می‌ماند.</p><hr/></section><section aria-labelledby="concept-v31-14-section-03" class="concept-reference-part"><h3 id="concept-v31-14-section-03">Reset یعنی شکستن سد</h3><p>اگر می‌خواهی Mobile دوباره از مقدار بالاتر پیروی کند، عدد Desktop را در Mobile کپی نکن. مقدار صریح Mobile را Reset یا پاک کن.</p><p>این کار DOM را سبک‌تر نمی‌کند؛ موضوع اصلی <strong>سادگی Cascade و نگهداری</strong> است.</p><p>قانون:</p><blockquote>
<p>مقدار صریح را فقط وقتی بساز که واقعاً تفاوت رفتاری لازم است.</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-14-section-04" class="concept-reference-part"><h3 id="concept-v31-14-section-04">Breakpoint چیست؟</h3><p>Breakpoint مرزی است که در آن مجموعه‌ای از Styleها فعال می‌شوند. اما Breakpoint نباید از نام دستگاه نتیجه‌گیری شود.</p><p>بهتر است بپرسی:</p><blockquote>
<p>Layout در چه عرضی دیگر قرارداد فعلی را حفظ نمی‌کند؟</p>
</blockquote><p>ممکن است Hero در ۸۷۰px بشکند، نه دقیقاً در عددی که نام Tablet دارد.</p><p>Breakpointهای سفارشی Elementor باید از تنظیمات واقعی سایت خوانده شوند؛ نباید عددهای فرضی را قانون جزوه معرفی کرد.</p><hr/></section><section aria-labelledby="concept-v31-14-section-05" class="concept-reference-part"><h3 id="concept-v31-14-section-05">Responsive Contract</h3><p>برای هر Section، قبل از واردکردن عددها یک قرارداد بنویس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Desktop:
- Hero row
- Copy 55%
- Visual 45%

Tablet:
- Hero row فشرده
- Gap کمتر
- Heading سیال

Mobile:
- Hero column
- Copy اول
- Button تمام‌عرض
- تزئین محدود
</code></pre></figure><p>این Contract تصمیم را توضیح می‌دهد. اعداد سپس برای اجرای آن می‌آیند.</p><hr/></section><section aria-labelledby="concept-v31-14-section-06" class="concept-reference-part"><h3 id="concept-v31-14-section-06">Fluid Typography و Spacing</h3><p>Responsive همیشه نیازمند چند جهش Breakpoint نیست. برای مقیاس سیال می‌توان از <code class="inline-code" dir="ltr">clamp()</code> استفاده کرد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">padding-inline: clamp(1rem, 4vw, 5rem);
font-size: clamp(2rem, 1.25rem + 3vw, 4.5rem);
</code></pre></figure><p>اما اگر ساختار باید از Row به Column تغییر کند، <code class="inline-code" dir="ltr">clamp()</code> جای Media Query یا کنترل Responsive را نمی‌گیرد.</p><hr/></section><section aria-labelledby="concept-v31-14-section-07" class="concept-reference-part"><h3 id="concept-v31-14-section-07">Container Queries؛ Component به فضای خودش نگاه می‌کند</h3><p>Media Query به Viewport نگاه می‌کند. Container Query به اندازهٔ Container نزدیک Component نگاه می‌کند.</p><p>کارت ممکن است در دو جای سایت باشد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Hero Wide Area: 700px
Sidebar: 320px
</code></pre></figure><p>Viewport در هر دو یکسان است، اما فضای کارت متفاوت است. Container Query می‌تواند کارت را براساس فضای واقعی خودش تغییر دهد.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.card-region {
  container-type: inline-size;
}

@container (min-width: 36rem) {
  .card {
    grid-template-columns: 12rem 1fr;
  }
}
</code></pre></figure><p>Container Query جایگزین کامل Media Query نیست؛ مکمل آن است.</p><p>در مستندات رسمی بررسی‌شده، کنترل بصری Native قطعی برای Container Query در پنل V4 اثبات نشده است. بنابراین این بخش باید به‌عنوان CSS پیشرفته با Custom CSS و تست نسخه هدف ارائه شود.</p><hr/></section><section aria-labelledby="concept-v31-14-section-08" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-14-section-08">در Elementor V4</h3><p>وقتی Device Mode را عوض می‌کنی:</p><ol>
<li>ببین کدام Property Indicator نشان می‌دهد مقدار از کجا آمده است.</li>
<li>فقط تفاوت لازم را Override کن.</li>
<li>اگر تفاوت دیگر لازم نیست، Reset کن.</li>
<li>Class درست و State درست را انتخاب کن.</li>
<li>Frontend واقعی را آزمایش کن؛ Preview Editor تنها شاهد کافی نیست.</li>
</ol><p>Custom CSS نیز می‌تواند Device-specific و State-specific باشد، پس منبع Style را دقیق دنبال کن.</p><hr/></section><section aria-labelledby="concept-v31-14-section-09" class="concept-reference-part"><h3 id="concept-v31-14-section-09">سناریوی واقعی: Grid کارت‌ها</h3><p>Desktop:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">4 columns
</code></pre></figure><p>Tablet:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">2 columns
</code></pre></figure><p>Mobile:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">1 column
</code></pre></figure><p>اما اگر از <code class="inline-code" dir="ltr">auto-fit/minmax()</code> استفاده می‌کنی، ممکن است برخی تغییرها بدون Breakpoint رخ دهند. باید تصمیم بگیری کنترل صریح ۴→۲→۱ مهم‌تر است یا جریان سیال براساس حداقل عرض کارت.</p><hr/></section><section aria-labelledby="concept-v31-14-section-10" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-14-section-10">اشتباهات رایج</h3><ul>
<li>کپی عدد Desktop در Mobile به‌جای Reset</li>
<li>ساخت Override برای هر Property</li>
<li>انتخاب Breakpoint فقط بر اساس نام Device</li>
<li>تست‌نکردن عرض‌های میانی</li>
<li>مخفی‌کردن محتوا به‌جای بازطراحی Layout</li>
<li>ساخت نسخهٔ Duplicate Desktop/Mobile بدون نیاز</li>
<li>کوچک‌کردن متن برای پنهان‌کردن مشکل Width</li>
<li>فرض Native بودن Container Query در Elementor بدون تست</li>
</ul><hr/></section><section aria-labelledby="concept-v31-14-section-11" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-14-section-11">پل به DevTools</h3><p>Device Toolbar را باز کن و عرض را پیوسته تغییر بده، نه فقط Presetها را. در Styles Panel Media Query فعال و Computed Value را ببین. برای Container Query نیز Badge و Overlay مربوط به Container در نسخه‌های پشتیبان DevTools مفید است.</p><hr/></section><section aria-labelledby="concept-v31-14-section-12" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-14-section-12">تصویر ذهنی نهایی</h3><p>Responsive مثل آبشاری است که مقدارها از بالا جاری می‌شوند. Override سد محلی است. هر سد باید دلیل داشته باشد؛ و وقتی دلیل از بین رفت، باید سد را برداری، نه اینکه آب را با سطل شبیه سرچشمه کنی.</p><hr/></section><section aria-labelledby="concept-v31-14-section-13" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-14-section-13">قوانین طلایی</h3><ul>
<li><strong>«Responsive یعنی تغییر قرارداد Layout، نه فقط کوچک‌کردن همه‌چیز.»</strong></li>
<li><strong>«مقدار برابر با Desktop را در Mobile تکرار نکن؛ اگر تفاوتی لازم نیست، Override را Reset کن.»</strong></li>
<li><strong>«Breakpoint را از نقطه شکست Layout استخراج کن، نه از نام دستگاه.»</strong></li>
<li><strong>«Media Query به صفحه نگاه می‌کند؛ Container Query به فضای Component.»</strong></li>
<li><strong>«Container Query مکمل Media Query است، نه جایگزین مطلق آن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Responsive editing and inherited responsive values</li>
<li>CSS Media Queries / CSS Containment specifications</li>
<li>Elementor Help: Custom CSS per device and state</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-14-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-14-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Responsive؛ breakpoint با px تعریف می‌شود، طراحی فقط px نیست</span></summary>
<section aria-labelledby="lesson-14-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Breakpoint آستانهٔ viewport است؛ داخل هر breakpoint می‌توانی از px، rem، % یا viewport units استفاده کنی. انتخاب واحد و انتخاب breakpoint دو تصمیم جدا هستند.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> Breakpoint چراغ راهنمای تغییر مسیر است؛ واحد، خط‌کش اندازه‌گیری داخل هر مسیر.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Breakpoint</th><td><code dir="ltr">media query threshold</code></td><td>معمولاً px در ابزارها</td><td>viewport width</td><td>جایی که محتوا می‌شکند.</td><td>مدل گوشی را جای معیار محتوا نگذار.</td><td><code dir="ltr">E_RESP</code></td></tr><tr><th scope="row">Viewport units</th><td><code dir="ltr">vw / vh / svh / lvh / dvh</code></td><td>Elementor بعضی کنترل‌ها VW/VH؛ CSS واحدهای جدید بیشتری دارد</td><td>viewport family</td><td>برای وابستگی به viewport با تست واقعی.</td><td>CSS-supported را به‌عنوان UI-exposed معرفی نکن.</td><td><code dir="ltr">E_UNITS</code></td></tr><tr><th scope="row">Responsive value</th><td><code dir="ltr">هر Property responsive</code></td><td>همان نوع مقدار Property</td><td>inherit/override</td><td>کمترین override لازم.</td><td>Reset ممکن است inherited value را برگرداند.</td><td><code dir="ltr">E_RESP</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>viewport width=390px؛ 10vw=39px. viewport dynamic height=760px؛ 100dvh=760px. این مثال CSS است و باید در مرورگر واقعی کنترل شود.</p></section>
<section><h3>📱 در Responsive</h3><p>خود این بخش موضوع Responsive است: مقدار، واحد، source و breakpoint را چهار ستون جدا ثبت کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>viewport size، media query فعال، computed value و source breakpoint را بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/responsive-editing/" rel="noopener noreferrer" target="_blank">Elementor V4 — Responsive editing</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length" rel="noopener noreferrer" target="_blank">MDN — CSS length values</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-14-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-14-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — Mobile Layout</h3><p>در Device Size باریک:</p><section aria-labelledby="section-hidden-209-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-209-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Platform Main Direction</dt><dd>Column</dd><dt>Align Items</dt><dd>Stretch یا Center برحسب طراحی</dd><dt>Copy Width</dt><dd>100%</dd><dt>Visual Width</dt><dd>100%</dd><dt>Visual Max Width</dt><dd>کنترل‌شده</dd><dt>Gap</dt><dd>کمتر از Desktop</dd><dt>Padding</dt><dd>متناسب‌تر</dd></dl></section><p>ترتیب DOM را حفظ کن: Copy سپس Visual، مگر اینکه دلیل محتوایی روشن برای تغییر داشته باشی.</p><h3>❓ سؤال توقف</h3><p>آیا برای Mobile باید یک سکشن TUYA دوم بسازی؟</p><details class="disclosure-card"><summary>پاسخ</summary>خیر؛ ابتدا همان ساختار را Responsive کن.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> بدون بررسی Inheritance، روی هر Device همهٔ مقادیر را دوباره وارد کنی.</p><p><strong>نشانه:</strong> نگهداری سخت و Conflict زیاد.</p><h3>🧪 عمداً خرابش کن</h3><p>Main را در Mobile همچنان Row نگه دار و Visual را Shrink=0 کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>Copy بسیار باریک می‌شود؛</li>
<li>Visual بیرون می‌زند؛</li>
<li>متن سطرهای نامناسب پیدا می‌کند؛</li>
<li>Scroll افقی محتمل است.</li>
</ul><p>Direction را Column و اندازه‌ها را منطقی کن.</p><h3>تست ضروری</h3><section aria-labelledby="section-hidden-210-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-210-heading">بخش آموزشی</h2><ul><li>320px</li>
<li>375px</li>
<li>Tablet portrait</li>
<li>Tablet landscape</li>
<li>Zoom 200%</li>
<li>متن طولانی‌تر</li></ul></section><h3>Checkpoint</h3><section aria-labelledby="section-hidden-211-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-211-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-78"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-78-1" name="chk-78-1" type="checkbox"/><span>یک DOM برای همهٔ Deviceها دارم</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-78-2" name="chk-78-2" type="checkbox"/><span>Mobile بدون Scroll افقی است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-78-3" name="chk-78-3" type="checkbox"/><span>Nodeها با Stage مقیاس می‌شوند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-78-4" name="chk-78-4" type="checkbox"/><span>Logoها Wrap می‌شوند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-78-5" name="chk-78-5" type="checkbox"/><span>Inheritance را آگاهانه استفاده کرده‌ام</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Responsive Inheritance یعنی چه؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> Hero در 700px می‌شکند. چگونه تصمیم می‌گیری Width/Wrap کافی است یا Breakpoint لازم داری؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-79"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-79-1" name="chk-79-1" type="checkbox"/><span>نقطهٔ شکست محتوا و Device Size را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-79-2" name="chk-79-2" type="checkbox"/><span>ابتدا Width، Wrap و Direction را بررسی کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-79-3" name="chk-79-3" type="checkbox"/><span>یک DOM را حفظ کرده و Duplicate Section پیشنهاد نداده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-14-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-14-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-HOME2-GRID-001 — <code class="inline-code" dir="ltr">100vh</code></h3><p><strong>هدف:</strong> ⚖️ دو روش را مقایسه کن</p><p>Min Height برابر 100vh در Export دیده شده است. در Mobile باید رفتار نوار مرورگر و گزینه‌های Viewport جدید در Runtime مقایسه شوند؛ نتیجهٔ قطعی از Export ممکن نیست.</p><h3>📂 CASE-SOL-ABS-001 — Card Mobile</h3><p>متن Absolute با Offset ثابت را با متن در Normal Flow در عرض باریک مقایسه کن.</p><h3>🔬 پشت صحنه</h3><p>V4 کنترل Responsive را در رابط ارائه می‌کند؛ نیازی نیست Media Query دستی بنویسی.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="memory-responsive-heading" role="heading">🧠 لایهٔ حافظه — Responsive sizing</span></summary><section aria-labelledby="memory-responsive-heading" class="memory-layer disclosure-content lesson-section"><p><strong>🧠 استعارهٔ ماندگار:</strong> Desktop نقشهٔ بزرگ است؛ Mobile ترجمهٔ همان معنا در فضای کوچک‌تر است، نه Screenshot فشرده.</p><p><strong>🧩 در Elementor V4 یعنی چه؟</strong> در هر Breakpoint مقدارهای width، max-width، gap، padding و order را جدا بررسی کن.</p><p><strong>⚠️ تله رایج:</strong> اگر فقط عددها را کوچک کنی اما Flow را عوض نکنی، طرح در Mobile می‌شکند.</p><p class="golden-rule"><strong>📜 قانون طلایی:</strong> در Responsive معنا را حفظ کن، نه تصویر ثابت Desktop را.</p><details class="more-know"><summary>بیشتر بدانید</summary><p>Computed Style مهم‌تر از چیزی است که فکر می‌کنی تنظیم کرده‌ای؛ چون مقدار نهایی از ترکیب inheritance، کلاس‌ها، stateها، breakpoints و CSS مرورگر ساخته می‌شود.</p></details></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-14-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-14-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-81"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-81-1" name="chk-81-1" type="checkbox"/><span>می‌توانی Responsive Inheritance و Override در Device Sizeهای مختلف را توضیح بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-81-2" name="chk-81-2" type="checkbox"/><span>می‌توانی Breakpoint را براساس شکست محتوا انتخاب کنی، نه نام دستگاه.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-82"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-82-1" name="chk-82-1" type="checkbox"/><span>Main Layout TUYA را بدون Duplicate از Row به Column تبدیل می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-82-2" name="chk-82-2" type="checkbox"/><span>Desktop، Tablet، Mobile و Zoom را با یک DOM آزمایش می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-83"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-83-1" name="chk-83-1" type="checkbox"/><span>در یک Hero جدید می‌توانی مشخص کنی مشکل با Wrap/Width حل می‌شود یا Breakpoint جدید لازم است.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-14-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-14-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>ایستگاه D نیمه‌کامل است. در درس بعد جهت RTL و Start/End را روی همین Layout بررسی می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 14</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-14-completion"><fieldset><legend>ثبت پایان درس 14</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-14-complete" name="lesson-14-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-14-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Responsive، Breakpoint و واحدهای Viewport</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Responsive Inheritance در برابر مقدار مستقل</h3><p>Inheritance یعنی مقدار desktop/default به پایین می‌آید تا وقتی در breakpoint کوچک‌تر override شود. مقدار مستقل موبایل یعنی واقعاً تصمیم طراحی متفاوتی گرفته‌ای.</p><p>برای هر breakpoint مقدار نده؛ فقط وقتی قانون طراحی عوض می‌شود مقدار بده.</p></section>
<section class="inline-compare-card"><h3><span dir="ltr">vw</span> در برابر <span dir="ltr">%</span> و <span dir="ltr">vh</span> در برابر <span dir="ltr">min-height</span></h3><p><code dir="ltr">%</code> نسبت به parent است؛ <code dir="ltr">vw</code> نسبت به viewport. <code dir="ltr">vh</code> به ارتفاع پنجره وابسته است؛ <code dir="ltr">min-height</code> حداقل قد می‌دهد و اجازه رشد می‌دهد.</p><p class="golden-rule">قانون طلایی: برای تقسیم داخل parent، اول %/Flex/Grid؛ برای Hero واقعی شاید viewport unit.</p></section>
</div>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="custom-breakpoints-title" role="heading">تکمیل نسخه 22 — Breakpoint سفارشی و واحدهای Viewport جدید</span></summary><section aria-labelledby="custom-breakpoints-title" class="smart-note-card disclosure-content">
<p>Elementor برای Responsive Editing، breakpointهای پیش‌فرض دارد و امکان افزودن/سفارشی‌سازی breakpointهای بیشتر / custom breakpoints را هم فراهم می‌کند. بنابراین در این جزوه، هیچ عدد breakpoint را قانون جهانی فرض نکن؛ آن را از تنظیمات پروژه بخوان.</p>
<div class="table-scroll"><table>
<caption>واحدهای viewport که باید بشناسی</caption>
<thead><tr><th scope="col">واحد</th><th scope="col">رفتار کلی</th><th scope="col">نکتهٔ عملی</th></tr></thead>
<tbody>
<tr><td><code class="inline-code" dir="ltr">vw / vh</code></td><td>درصدی از اندازهٔ viewport</td><td>برای layout داخل parent همیشه بهتر از <code class="inline-code" dir="ltr">width:100%</code> نیست.</td></tr>
<tr><td><code class="inline-code" dir="ltr">svw / svh</code></td><td>viewport کوچک</td><td>برای حالت‌هایی که UI مرورگر فضا را کم می‌کند مفید است.</td></tr>
<tr><td><code class="inline-code" dir="ltr">lvw / lvh</code></td><td>viewport بزرگ</td><td><code class="inline-code" dir="ltr">vw</code> معمولاً با large viewport هم‌ارز در نظر گرفته می‌شود.</td></tr>
<tr><td><code class="inline-code" dir="ltr">dvw / dvh</code></td><td>viewport پویا</td><td>با تغییر UI مرورگر به‌روزرسانی می‌شود؛ راه‌حل جادویی همهٔ overflowها نیست.</td></tr>
</tbody>
</table></div>
<p class="golden-rule"><strong>قانون طلایی:</strong> اول معلوم کن اندازه نسبت به parent است یا viewport؛ بعد واحد انتخاب کن.</p>
</section></details>
<details class="lesson-disclosure" id="lesson-14-practical-findings"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-14-practical-findings-heading" role="heading">🔎 یافتهٔ عملی و خطایابی</span></summary><section aria-labelledby="lesson-14-practical-findings-heading" class="disclosure-content practical-findings">
<p class="finding-scope">این بخش فقط ادعاهایی را آموزش می‌دهد که یا در مشاهدهٔ واقعی ثبت شده‌اند یا Help Center رسمی Elementor آن‌ها را صریحاً پشتیبانی می‌کند. نتیجه‌های وابسته به Theme، نسخه یا ساختار DOM با دامنهٔ اعتبار نوشته شده‌اند.</p>
<article class="finding-card" data-verification="verified_by_official_help" id="finding-responsive-value-still-active">
<div class="evidence-badges"><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>چرا مقدار Mobile را پاک کردم ولی فاصله یا اندازه هنوز باقی است؟</h3>
<p><strong>برداشت اشتباه:</strong> خالی‌کردن کنترل در breakpoint کوچک‌تر یعنی مقدار نهایی صفر می‌شود.</p>
<p><strong>قاعدهٔ رسمی:</strong> مقدارهای responsive به‌صورت cascade از breakpoint بزرگ‌تر به کوچک‌تر ارث می‌رسند. مقدار inherited در UI به‌شکل placeholder کم‌رنگ نمایش داده می‌شود.</p>
<div class="finding-checks">
<section><h4>در Elementor</h4><p>کنترل Desktop/Tablet/Mobile را به‌ترتیب بررسی کن و فرق «مقدار محلی» با «placeholder ارث‌رسیده» را ببین.</p></section>
<section><h4>در DevTools</h4><p>در viewport هدف، matched media query و computed value نهایی را بررسی کن.</p></section>
</div>
<p class="golden-rule"><strong>قانون طلایی:</strong> خالی‌بودن فیلد responsive همیشه به معنی خالی‌بودن computed value نیست.</p>
<details class="more-know"><summary>منبع رسمی و دامنه</summary><p><a href="https://elementor.com/help/responsive-editing/">Responsive editing</a> و <a href="https://elementor.com/help/inherited-responsive-values/">Inherited responsive values</a>. مقالهٔ دوم دربارهٔ Sections/Columns هشدار دامنه دارد؛ اصل cascade برای responsive editing در مقالهٔ جدیدتر نیز مستند شده است.</p></details>
</article>
<article class="finding-card" data-verification="verified_by_official_help" id="finding-breakpoint-cascade-direction">
<div class="evidence-badges"><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>چرا تغییر Desktop روی Mobile اثر گذاشت، ولی تغییر Mobile روی Desktop نه؟</h3>
<p>Elementor تغییرهای breakpoint بزرگ‌تر را به breakpointهای کوچک‌تر cascade می‌کند؛ جهت برعکس معمولاً اتفاق نمی‌افتد. در widescreen، Desktop نقطهٔ مرجع است و inheritance می‌تواند به سمت breakpoint بزرگ‌تر نیز تعریف شود.</p>
<p class="golden-rule"><strong>قانون طلایی:</strong> breakpointها جزیره‌های کاملاً مستقل نیستند؛ قبل از override، زنجیرهٔ inheritance را بخوان.</p>
<details class="more-know"><summary>منبع رسمی</summary><p><a href="https://elementor.com/help/additional-breakpoints/">Additional custom breakpoints</a></p></details>
</article>
</section></details>
<details class="lesson-disclosure" id="lesson-14-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Workflow رسمی Desktop → Tablet → Mobile</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<ol><li>Desktop را baseline قرار بده.</li><li>Tablet را قبل از Mobile بررسی کن، چون مقادیر بزرگ‌تر به کوچک‌تر cascade می‌شوند.</li><li>Direction، Width/Height، Order، Typography و Spacing را فقط در صورت نیاز override کن.</li><li>بین breakpointها با viewport handles تست کن؛ breakpoint نام دستگاه نیست، یک عرض viewport است.</li></ol>
<p><strong>Tablet TUYA:</strong> چون طرح Tablet تحویل نشده، رفتار آن <code>proposed_pending_designer_confirmation</code> است و نباید به‌عنوان مشاهده قطعی نوشته شود.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure step-through-v2-disclosure" id="stv2-responsive-inheritance">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="stv2-responsive-inheritance-heading" role="heading">▶ Step‑Through v2 — Responsive Inheritance — مقدار از کجا آمده است؟</span>
</summary>
<section aria-labelledby="stv2-responsive-inheritance-heading" class="disclosure-content step-through-v2" data-step-through-v2="" data-stv2-id="stv2-responsive-inheritance" data-stv2-renderer="responsive-inheritance" tabindex="0">
<header class="stv2-header">
<p class="stv2-kicker">چرخهٔ فعال: ببین ← پیش‌بینی کن ← بررسی کن ← خراب کن ← انتقال بده</p>
<p><strong>🎯 هدف:</strong> منبع هر مقدار را در Desktop، Tablet و Mobile ببین و Reset را با حذف تصادفی اشتباه نگیر.</p>
<div aria-label="وضعیت شواهد" class="stv2-evidence-row"><span class="stv2-evidence-badge">تأییدشده با Help Center رسمی Elementor</span><span class="stv2-evidence-badge">تأییدشده با Help Center رسمی Elementor</span></div>
</header>
<div class="stv2-progress-row">
<span class="stv2-step-count" data-stv2-count="">مرحله ۱</span>
<progress data-stv2-progress="" max="4" value="1">1/4</progress>
<span class="stv2-phase" data-stv2-phase=""></span>
</div>
<div class="stv2-three-view">
<section aria-labelledby="stv2-responsive-inheritance-visual-title" class="stv2-card stv2-visual-card">
<h3 id="stv2-responsive-inheritance-visual-title">👁 نتیجهٔ بصری</h3>
<div aria-label="نمای بصری مرحله" class="stv2-visual" data-stv2-visual=""></div>
</section>
<section aria-labelledby="stv2-responsive-inheritance-elementor-title" class="stv2-card">
<h3 id="stv2-responsive-inheritance-elementor-title">🧩 تنظیم Elementor</h3>
<dl class="stv2-definition-list" data-stv2-elementor=""></dl>
</section>
<section aria-labelledby="stv2-responsive-inheritance-computed-title" class="stv2-card">
<h3 id="stv2-responsive-inheritance-computed-title">🔬 Computed / مدل محاسباتی</h3>
<dl class="stv2-definition-list" data-stv2-computed=""></dl>
<p class="stv2-model-note">اعداد نمایشی ممکن است مدل آموزشی باشند؛ برچسب شواهد هر مرحله را ببین.</p>
</section>
</div>
<section aria-labelledby="stv2-responsive-inheritance-state-title" class="stv2-explanation">
<h3 data-stv2-title="" id="stv2-responsive-inheritance-state-title"></h3>
<p data-stv2-summary=""></p>
<p data-stv2-explanation=""></p>
<p class="golden-rule"><strong>📜 قانون طلایی:</strong> <span data-stv2-golden=""></span></p>
<p><strong>وضعیت این مرحله:</strong> <code class="inline-code" data-stv2-evidence="" dir="ltr"></code></p>
</section>
<section aria-labelledby="stv2-responsive-inheritance-prediction-title" class="stv2-prediction">
<h3 id="stv2-responsive-inheritance-prediction-title">❓ پیش‌بینی کن</h3>
<p data-stv2-prompt=""></p>
<div aria-label="گزینه‌های پیش‌بینی" class="stv2-prediction-options" data-stv2-options="" role="group"></div>
<p aria-live="polite" class="stv2-feedback" data-stv2-feedback="" role="status"></p>
</section>
<div aria-label="کنترل مراحل" class="stv2-actions">
<button class="ui-btn" data-stv2-prev="" type="button">مرحلهٔ قبل</button>
<button class="ui-btn" data-stv2-reveal="" type="button">نمایش پاسخ</button>
<button class="ui-btn" data-stv2-next="" type="button">مرحلهٔ بعد</button>
<button class="ui-btn" data-stv2-reset="" type="button">شروع دوباره</button>
</div>
<p aria-live="polite" class="stv2-status" data-stv2-status="" role="status"></p>
<p class="stv2-lab-link"><a href="#lesson-14-responsive-build-test">🧪 همین مفهوم را در «بساز و امتحان کن» اجرا کن</a></p>
<section aria-label="خلاصهٔ همهٔ مراحل برای چاپ" class="stv2-print-all"><div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table"><caption>خلاصهٔ همهٔ مراحل Step‑Through v2</caption><thead><tr><th scope="col">مرحله</th><th scope="col">نتیجه</th><th scope="col">وضعیت شواهد</th><th scope="col">قانون طلایی</th></tr></thead><tbody><tr><th scope="row">1 — Desktop مقدار پایه را تعریف می‌کند</th><td>Padding روی Desktop برابر 48px است و breakpointهای کوچک‌تر هنوز override ندارند.</td><td><code class="inline-code" dir="ltr">verified_by_official_elementor_help</code></td><td>وجود مقدار در Mobile الزاماً به معنی تنظیم مستقیم در Mobile نیست.</td></tr><tr><th scope="row">2 — Tablet Override، Mobile Inherited</th><td>Tablet برابر 32px شده و Mobile همان 32px را به‌صورت inherited می‌بیند.</td><td><code class="inline-code" dir="ltr">verified_by_official_elementor_help</code></td><td>عدد را تنها نبین؛ منبع عدد را هم بخوان.</td></tr><tr><th scope="row">3 — Mobile Override مستقل</th><td>Mobile برابر 20px است؛ Desktop و Tablet بدون تغییر می‌مانند.</td><td><code class="inline-code" dir="ltr">verified_by_official_elementor_help</code></td><td>Override را حداقلی و هدفمند نگه دار.</td></tr><tr><th scope="row">4 — Reset Mobile و بازگشت مقدار Inherited</th><td>20px حذف می‌شود و Mobile دوباره 32px را از Tablet دریافت می‌کند.</td><td><code class="inline-code" dir="ltr">verified_by_official_elementor_help</code></td><td>بعد از Reset، منبع جدید مقدار را بررسی کن.</td></tr></tbody></table></div></section>
<noscript><p class="warning-box">برای تعامل مرحله‌ای JavaScript محلی باید فعال باشد؛ خلاصهٔ چاپی همهٔ مراحل در همین بخش موجود است.</p></noscript>
<script class="stv2-config" type="application/json">{"goal":"منبع هر مقدار را در Desktop، Tablet و Mobile ببین و Reset را با حذف تصادفی اشتباه نگیر.","id":"stv2-responsive-inheritance","lab_target":"lesson-14-responsive-build-test","lesson_id":"lesson-14","renderer":"responsive-inheritance","schema_version":"1.0.0","states":[{"computed":[["Desktop used value","48px"],["Tablet source","Desktop"],["Mobile source","Desktop"]],"elementor":[["Desktop Padding","48px"],["Tablet","Inherited"],["Mobile","Inherited"]],"evidence":"verified_by_official_elementor_help","explanation":"در مدل پیش‌فرض، مقدار بزرگ‌تر به کوچک‌تر cascade می‌شود مگر override ایجاد شود.","golden_rule":"وجود مقدار در Mobile الزاماً به معنی تنظیم مستقیم در Mobile نیست.","id":"desktop-source","phase":"منبع","prediction":{"correct":1,"feedback_correct":"درست است؛ Mobile از نزدیک‌ترین breakpoint بزرگ‌ترِ دارای مقدار ارث می‌برد.","feedback_wrong":"Cascade را از بزرگ‌تر به کوچک‌تر و مرحله‌به‌مرحله دنبال کن.","options":["48px از Desktop","32px از Tablet","0px"],"prompt":"اگر Tablet را روی 32px override کنیم و Mobile مقدار مستقیم نداشته باشد، Mobile چه می‌گیرد؟"},"summary":"Padding روی Desktop برابر 48px است و breakpointهای کوچک‌تر هنوز override ندارند.","title":"Desktop مقدار پایه را تعریف می‌کند","visual":{"devices":[{"name":"Desktop","source":"local","value":"48px"},{"name":"Tablet","source":"inherited","value":"48px"},{"name":"Mobile","source":"inherited","value":"48px"}]}},{"computed":[["Desktop source","Desktop"],["Tablet source","Tablet"],["Mobile source","Tablet"]],"elementor":[["Desktop Padding","48px"],["Tablet Padding","32px — مستقیم"],["Mobile Padding","32px — inherited"]],"evidence":"verified_by_official_elementor_help","explanation":"رنگ یا حالت muted در Editor به تشخیص مقدار inherited کمک می‌کند.","golden_rule":"عدد را تنها نبین؛ منبع عدد را هم بخوان.","id":"tablet-override","phase":"Override","prediction":{"correct":1,"feedback_correct":"درست است؛ تغییر breakpoint کوچک‌تر به بزرگ‌تر برنمی‌گردد.","feedback_wrong":"Cascade Responsive به‌طور پیش‌فرض از بزرگ‌تر به کوچک‌تر است، نه برعکس.","options":["20px","48px باقی می‌ماند","به Auto تبدیل می‌شود"],"prompt":"اگر فقط Mobile را روی 20px تنظیم کنیم، Desktop چه می‌شود؟"},"summary":"Tablet برابر 32px شده و Mobile همان 32px را به‌صورت inherited می‌بیند.","title":"Tablet Override، Mobile Inherited","visual":{"devices":[{"name":"Desktop","source":"local","value":"48px"},{"name":"Tablet","source":"override","value":"32px"},{"name":"Mobile","source":"inherited","value":"32px"}]}},{"computed":[["Desktop used","48px"],["Tablet used","32px"],["Mobile used","20px"]],"elementor":[["Desktop","48px"],["Tablet","32px"],["Mobile","20px — مستقیم"]],"evidence":"verified_by_official_elementor_help","explanation":"این مرحله نشان می‌دهد Responsive correction باید فقط جایی انجام شود که طرح واقعاً نیاز دارد.","golden_rule":"Override را حداقلی و هدفمند نگه دار.","id":"mobile-override","phase":"Override کوچک‌تر","prediction":{"correct":0,"feedback_correct":"بله؛ با حذف override، inheritance دوباره فعال می‌شود.","feedback_wrong":"Reset را به‌عنوان بازگشت به زنجیرهٔ inheritance ببین.","options":["از Tablet، یعنی 32px","همیشه صفر می‌شود","از Theme بدون بررسی"],"prompt":"اگر Mobile override را Reset کنیم، مقدار Mobile از کجا می‌آید؟"},"summary":"Mobile برابر 20px است؛ Desktop و Tablet بدون تغییر می‌مانند.","title":"Mobile Override مستقل","visual":{"devices":[{"name":"Desktop","source":"local","value":"48px"},{"name":"Tablet","source":"override","value":"32px"},{"name":"Mobile","source":"override","value":"20px"}]}},{"computed":[["Mobile used value","32px"],["Value source","Tablet"],["Desktop effect","بدون تغییر"]],"elementor":[["Mobile direct value","Reset / حذف"],["Mobile displayed value","32px muted"],["Source indicator","Tablet"]],"evidence":"verified_by_official_elementor_help","explanation":"پاک‌کردن یک مقدار responsive لزوماً به صفر منجر نمی‌شود؛ ممکن است مقدار inherited دوباره ظاهر شود.","golden_rule":"بعد از Reset، منبع جدید مقدار را بررسی کن.","id":"mobile-reset","phase":"خطایابی","prediction":{"correct":0,"feedback_correct":"درست است؛ خود Editor منبع inherited را قابل مشاهده می‌کند.","feedback_wrong":"عدد یکسان کافی نیست؛ حالت نمایش و منبع را بررسی کن.","options":["نمایش muted و indicator منبع","فقط نام دستگاه","فقط رنگ Background"],"prompt":"برای تشخیص مقدار inherited در Editor V4، به چه نشانه‌ای توجه می‌کنی؟"},"summary":"20px حذف می‌شود و Mobile دوباره 32px را از Tablet دریافت می‌کند.","title":"Reset Mobile و بازگشت مقدار Inherited","visual":{"devices":[{"name":"Desktop","source":"local","value":"48px"},{"name":"Tablet","source":"override","value":"32px"},{"name":"Mobile","source":"inherited","value":"32px"}]}}],"storage_key":"elementor-v4-workbook:v27:stv2:responsive-inheritance","title":"Responsive Inheritance — مقدار از کجا آمده است؟","type":"layer_reveal_debug","verification":[{"source_id":"ELEMENTOR_RESPONSIVE_EDITING","status":"verified_by_official_elementor_help"},{"source_id":"ELEMENTOR_INHERITED_VALUES","status":"verified_by_official_elementor_help"}]}</script>
</section>
</details><details class="lesson-disclosure responsive-build-test" id="lesson-14-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Inheritance، Reset و Breakpoint واقعی</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> ببین مقدار خالی در Mobile لزوماً به معنی صفر نیست.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>در Desktop برای Padding یک مقدار مشخص بگذار.</li><li>به Tablet و Mobile برو و مقدار inherited را بدون تغییر مشاهده کن.</li><li>در Mobile override بده، سپس آن را Reset کن و بازگشت inheritance را ثبت کن.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن بعد از Reset مقدار نهایی از کدام breakpoint می‌آید.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>برای یک شکست کوچک، breakpoint اضافی بساز و سپس پیچیدگی cascade را مقایسه کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>مقدار muted/inherited در پنل، CSS rule فعال و viewport width واقعی.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> برای هر مقدار می‌توانی بگویی local override است یا inherited و منبع آن کدام breakpoint است.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-14-responsive-build-test-done-build"><input data-persist="" id="lesson-14-responsive-build-test-done-build" name="lesson-14-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-14-responsive-build-test-done-test"><input data-persist="" id="lesson-14-responsive-build-test-done-test" name="lesson-14-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-14-responsive-build-test-done-debug"><input data-persist="" id="lesson-14-responsive-build-test-done-debug" name="lesson-14-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-14-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-14-responsive-build-test-note" name="lesson-14-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/inherited-responsive-values/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
<p class="stv2-back-link"><a href="#stv2-responsive-inheritance">↩ مفهوم را با Step‑Through v2 مرور کن</a></p></section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-14-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Responsive overrides</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
