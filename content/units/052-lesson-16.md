<article class="lesson card-surface" data-lesson="16" id="lesson-16"><h2 class="lesson-title former-h1">درس 16 — State، Hover، Focus و دسترسی‌پذیری</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-16-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-16-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> Stateهای مهم و تفاوت Hover با Focus را بفهمی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> ساخت Interaction پیچیده با JavaScript را.</p><p><strong>در پایان باید بتوانی:</strong> عناصر تعاملی را برای Mouse، Keyboard و Zoom قابل استفاده کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-16-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-16-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>♿ دسترسی‌پذیری + 🛠 اجرایی + 🔍 عیب‌یابی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۵–۳۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> Hover، Focus و Keyboard باید جدا سنجیده شوند.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-16-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-16-lesson-understand-4">A. بفهم</h2><h3>مدل ذهنی</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای State، Hover و Focus">
<h4>راهنمای مبتدی برای State، Hover و Focus</h4>
<p>State یعنی وضعیت فعلی یک عنصر؛ یک دکمه همیشه فقط یک ظاهر ثابت ندارد.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="State">
<h4><span class="term-en" dir="ltr">State</span> — وضعیت عنصر</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> State یعنی عنصر الان عادی است، Hover شده، Focus دارد یا Active است.</li>
<li><strong>۲. مثال روزمره:</strong> مثل چراغ راهنما که حالت‌های مختلف دارد.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> دکمه، لینک یا کارت تعاملی در TUYA.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> پنل State در Elementor یا CSS pseudo-class.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> فقط حالت Normal را طراحی می‌کنم و بقیه را فراموش می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> برای هر کنترل مهم حداقل Normal/Hover/Focus را بررسی کن.</li>
<li><strong>۷. تمرین کوچک:</strong> یک دکمه را انتخاب کن و سه حالتش را نام ببر.</li>
</ol>
</article>
<article class="concept-card" data-concept="Hover">
<h4><span class="term-en" dir="ltr">Hover</span> — وقتی نشانگر روی عنصر است</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Hover وقتی رخ می‌دهد که Mouse/Pointer روی عنصر قرار بگیرد.</li>
<li><strong>۲. مثال روزمره:</strong> مثل وقتی دستت را روی یک کلید نگه می‌داری.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> دکمه‌ای که با ماوس روشن‌تر می‌شود.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Hover state در Style panel.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> اطلاعات مهم را فقط با Hover نشان می‌دهم.</li>
<li><strong>۶. تصمیم درست:</strong> Hover کمک بصری است؛ نباید تنها راه فهمیدن باشد.</li>
<li><strong>۷. تمرین کوچک:</strong> یک اثر Hover پیدا کن و بگو بدون ماوس هم قابل فهم هست یا نه.</li>
</ol>
</article>
<article class="concept-card" data-concept="Focus">
<h4><span class="term-en" dir="ltr">Focus</span> — وقتی عنصر با کیبورد فعال است</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Focus یعنی کاربر با Tab یا کیبورد به آن عنصر رسیده است.</li>
<li><strong>۲. مثال روزمره:</strong> مثل خط‌کش روی فرم که نشان می‌دهد کجا هستی.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> دکمه‌ها، لینک‌ها و ورودی‌های workbook.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Focus style یا outline قابل مشاهده.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> Focus را حذف می‌کنم چون از نظر ظاهری ساده‌تر است.</li>
<li><strong>۶. تصمیم درست:</strong> Focus باید واضح و قابل دیدن باشد.</li>
<li><strong>۷. تمرین کوچک:</strong> با Tab ذهنی حرکت کن و بگو الان کدام دکمه باید مشخص شود.</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">State</dt><dd>وضعیت فعلی یک عنصر</dd>
<dt dir="ltr">Hover</dt><dd>وضعیت اشاره‌گر روی عنصر</dd>
<dt dir="ltr">Focus</dt><dd>وضعیت فعال برای کیبورد</dd>
<dt dir="ltr">Active</dt><dd>لحظهٔ فعال‌سازی</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">قبل از تحویل یک Button، آن را فقط با ماوس تست نکن؛ Focus کیبورد را هم ببین.</p>
</aside>
</section><section aria-labelledby="section-hidden-235-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-235-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Normal</dt><dd>حالت پایه</dd><dt>Hover</dt><dd>Pointing device روی Element</dd><dt>Focus</dt><dd>عنصر فعال برای Keyboard</dd><dt>Active</dt><dd>هنگام فعال‌سازی</dd></dl></section><p>Hover جای Focus را نمی‌گیرد.</p><h3>Accessibility ضروری برای Elementor</h3><ul>
<li>Heading hierarchy؛</li>
<li>Alt Text؛</li>
<li>Focus قابل مشاهده؛</li>
<li>Contrast مناسب؛</li>
<li>Target قابل کلیک؛</li>
<li>Zoom 200%؛</li>
<li>عدم وابستگی اطلاعات به رنگ یا Hover تنها.</li>
</ul><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="be442ba828a89c0b31bacf730bcdec5f2221ad455f74ab575d4f9cd0b5e23725" id="lesson-16-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق State؛ Normal، Hover، Focus، Focus Visible و Active</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="16" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-16-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-16-section-01">مسئله‌ای که State حل می‌کند</h3><p>یک Button فقط یک مستطیل ثابت نیست. کاربر باید بفهمد:</p><ul>
<li>آیا قابل کلیک است؟</li>
<li>آیا Pointer روی آن قرار دارد؟</li>
<li>آیا با Keyboard به آن رسیده است؟</li>
<li>آیا همین لحظه فشرده شده است؟</li>
<li>آیا انتخاب شده یا Disabled است؟</li>
</ul><p>State زبان بازخورد رابط است.</p><hr/></section><section aria-labelledby="concept-v31-16-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-16-section-02">تشبیه به دنیای واقعی: دکمهٔ آسانسور</h3><p>دکمهٔ آسانسور همیشه همان دکمه است، اما وضعیتش تغییر می‌کند:</p><ul>
<li>Normal: منتظر است.</li>
<li>Hover: دست به آن نزدیک شده است.</li>
<li>Focus: اکنون مقصد ورودی Keyboard است.</li>
<li>Focus Visible: چراغ راهنما زمانی روشن شده که کاربر برای پیدا کردن موقعیتش به آن نیاز دارد.</li>
<li>Active: انگشت دقیقاً در حال فشار دادن است.</li>
<li>Selected: انتخابی پایدارتر ثبت شده است.</li>
</ul><p>Element عوض نشده؛ شرایط تعامل عوض شده است.</p><hr/></section><section aria-labelledby="concept-v31-16-section-03" class="concept-reference-part"><h3 id="concept-v31-16-section-03">Normal</h3><p>Normal پایهٔ ظاهری Element است. Stateهای دیگر باید تغییر معناداری نسبت به آن بسازند، نه اینکه تمام طراحی را از نو تعریف کنند.</p><p>مثلاً Button پایه:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Background: brand-primary
Text: on-primary
Border: transparent
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-16-section-04" class="concept-reference-part"><h3 id="concept-v31-16-section-04">Hover</h3><p>Hover وقتی Pointer روی Element قرار می‌گیرد فعال می‌شود.</p><p>هدف:</p><blockquote>
<p>نشان دادن امکان تعامل پیش از کلیک.</p>
</blockquote><p>اما Hover نباید تنها راه نمایش اطلاعات ضروری باشد، چون:</p><ul>
<li>Touch Deviceها Hover واقعی ندارند؛</li>
<li>کاربر Keyboard ممکن است هرگز آن را نبیند؛</li>
<li>Hover پیچیده می‌تواند باعث Layout Shift شود.</li>
</ul><p>تغییر رنگ، Shadow یا Transform کوچک معمولاً بهتر از تغییر Size و Flow است.</p><hr/></section><section aria-labelledby="concept-v31-16-section-05" class="concept-reference-part"><h3 id="concept-v31-16-section-05">Focus</h3><p>Focus یعنی ورودی بعدی Keyboard یا تعامل به این Element مربوط است.</p><p>Input هنگام تایپ، Button هنگام ناوبری با Tab و Link هنگام انتخاب Keyboard Focus می‌گیرند.</p><p>حذف کامل Outline بدون جایگزین، کاربر Keyboard را بی‌نقشه می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-16-section-06" class="concept-reference-part"><h3 id="concept-v31-16-section-06">Focus Visible</h3><p><code class="inline-code" dir="ltr">:focus-visible</code> تلاش می‌کند Indicator را زمانی نشان دهد که مرورگر تشخیص می‌دهد کاربر احتمالاً به آن نیاز دارد؛ معمولاً در ناوبری Keyboard.</p><p>این راهی برای تعادل میان زیبایی و Accessibility است، نه مجوز حذف Focus.</p><p>الگوی رایج:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.button:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-16-section-07" class="concept-reference-part"><h3 id="concept-v31-16-section-07">Active</h3><p>Active کوتاه‌ترین State است؛ لحظهٔ بین Press و Release.</p><p>یک Transform کوچک می‌تواند حس فشرده‌شدن بدهد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.button:active {
  transform: translateY(1px);
}
</code></pre></figure><p>اما Active نباید تنها نشانه ثبت عمل باشد. بعد از کلیک ممکن است Loading، Success یا Error نیز لازم باشد.</p><hr/></section><section aria-labelledby="concept-v31-16-section-08" class="concept-reference-part"><h3 id="concept-v31-16-section-08">State روی Class، نه فقط Element</h3><p>در Elementor V4، State را برای Class انتخاب‌شده ویرایش می‌کنی. این نکته بسیار مهم است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Global Class button-primary + Hover
</code></pre></figure><p>یعنی Hover تمام Elementهایی را که از همان Global Class استفاده می‌کنند تغییر می‌دهد.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Local Class + Hover
</code></pre></figure><p>یعنی استثنای همان Element.</p><p>پس قبل از تغییر State نگاه کن کدام Class فعال است.</p><hr/></section><section aria-labelledby="concept-v31-16-section-09" class="concept-reference-part"><h3 id="concept-v31-16-section-09">تعارض Stateها و Style Ghosting</h3><p>وقتی رنگ Normal را تغییر می‌دهی اما Button خاصی تغییر نمی‌کند، این زنجیره را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Breakpoint فعلی؟
State فعلی؟
Local Class مقدار دارد؟
Global Class دیگری بالاتر است؟
Custom CSS برای Hover/Focus وجود دارد؟
</code></pre></figure><p>ممکن است Property در Hover صریحاً تعریف شده باشد و تغییر Normal هنگام Hover دیده نشود.</p><p>Indicatorهای V4 می‌توانند نشان دهند مقدار از Local، Global یا Class رقیب آمده است. روی Indicator کلیک کن و منبع Style را پیدا کن؛ نام دقیق دکمه Reset را از UI نسخه هدف بخوان و مقدار صریح را پاک کن.</p><hr/></section><section aria-labelledby="concept-v31-16-section-10" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-16-section-10">در Elementor V4</h3><p>سناریوی Button:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">button-base
├── Normal: structure, typography, radius
├── Hover: background shift + subtle shadow
├── Focus Visible: clear outline
└── Active: small press feedback
</code></pre></figure><p>اگر <code class="inline-code" dir="ltr">button-base</code> Global است، Stateهای عمومی نیز همان‌جا قرار می‌گیرند. اگر فقط یک CTA خاص رفتار متفاوت دارد، Local Class یا Variant Pattern بررسی می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-16-section-11" class="concept-reference-part"><h3 id="concept-v31-16-section-11">Accessibility</h3><p>State خوب فقط زیبا نیست:</p><ul>
<li>Contrast کافی دارد.</li>
<li>Focus Indicator واضح است.</li>
<li>تغییر فقط با رنگ منتقل نمی‌شود، اگر معنا مهم باشد.</li>
<li>Reduced Motion را در Animationهای State رعایت می‌کند.</li>
<li>Disabled را از Normal قابل تشخیص می‌کند.</li>
<li>Hover اطلاعات حیاتی را انحصاری نمی‌کند.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-16-section-12" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-16-section-12">پل به DevTools</h3><p>در Styles Panel روی <code class="inline-code" dir="ltr">:hov</code> کلیک کن و Stateهای زیر را Force کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">:hover
:active
:focus
:focus-visible
</code></pre></figure><p>این روش اجازه می‌دهد Style State را بدون نگه‌داشتن موس یا Keyboard بررسی کنی.</p><hr/></section><section aria-labelledby="concept-v31-16-section-13" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-16-section-13">اشتباهات رایج</h3><ul>
<li>حذف Outline بدون جایگزین</li>
<li>طراحی فقط Hover</li>
<li>تغییر Width یا Padding در Hover و تکان‌دادن Layout</li>
<li>ویرایش Hover روی Local Class در حالی که قصد Global داری</li>
<li>تعریف رنگ‌های متعارض در چند Class</li>
<li>استفاده از Active به‌جای Loading Feedback</li>
<li>فرض Hover واقعی در Mobile</li>
</ul><hr/></section><section aria-labelledby="concept-v31-16-section-14" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-16-section-14">تصویر ذهنی نهایی</h3><p>State لباس تازهٔ Element نیست؛ حالت چهرهٔ همان Element در یک لحظه است. Hover قصد نزدیک‌شدن، Focus مرکز توجه و Active لحظهٔ فشار است.</p><hr/></section><section aria-labelledby="concept-v31-16-section-15" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-16-section-15">قوانین طلایی</h3><ul>
<li><strong>«State وضعیت موقت است، نه Element جدید.»</strong></li>
<li><strong>«Hover برای Pointer است؛ Focus برای ناوبری؛ Focus Visible برای راه‌یابی قابل دسترس.»</strong></li>
<li><strong>«Focus را حذف نکن؛ آن را درست طراحی کن.»</strong></li>
<li><strong>«State را روی Class درست و Breakpoint درست ویرایش کن.»</strong></li>
<li><strong>«بازخورد State نباید Layout را بلرزاند.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Element states and Custom CSS per state</li>
<li>CSS Selectors / UI pseudo-classes</li>
<li>WAI accessibility guidance for keyboard focus</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-16-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-16-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — State و Motion؛ زمان، زاویه، نسبت و طول</span></summary>
<section aria-labelledby="lesson-16-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Hover و Focus keyword/state هستند؛ Transition زمان می‌گیرد، Rotate زاویه، Scale عدد بدون واحد و Move طول یا درصد.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> برای یک حرکت چهار سؤال داری: چه حالتی؟ چقدر جابه‌جا؟ چند درجه بچرخد؟ در چه مدت؟</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Transition duration</th><td><code dir="ltr">transition-duration</code></td><td>ms یا s در CSS؛ Elementor نمونهٔ 200ms دارد</td><td>زمان</td><td>حرکت کوتاه و قابل درک.</td><td>1000ms=1s؛ زمان طولانی UI را کند می‌کند.</td><td><code dir="ltr">E_EFFECTS</code></td></tr><tr><th scope="row">Rotate</th><td><code dir="ltr">transform: rotate()</code></td><td>deg / rad / turn</td><td>زاویه</td><td>برای چرخش محدود.</td><td>360deg و 1turn برابرند.</td><td><code dir="ltr">CSS_TRANSFORM</code></td></tr><tr><th scope="row">Move</th><td><code dir="ltr">translate</code></td><td>length یا percentage</td><td>Box خود عنصر برای درصد</td><td>برای حرکت بصری بدون تغییر Flow.</td><td>ترجمه ممکن است عنصر را خارج و clip کند.</td><td><code dir="ltr">CSS_TRANSFORM</code></td></tr><tr><th scope="row">Scale / Opacity</th><td><code dir="ltr">scale / opacity</code></td><td>عدد بدون واحد</td><td>نسبت</td><td>برای feedback کوچک.</td><td>Hover تنها حامل معنا نباشد.</td><td><code dir="ltr">E_EFFECTS</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>200ms = 0.2s؛ rotate(0.25turn)=90deg؛ scale(1.05)=105٪ اندازهٔ بصری.</p></section>
<section><h3>📱 در Responsive</h3><p>روی touch، hover ممکن است وجود نداشته باشد؛ motion و duration را با prefers-reduced-motion و Focus آزمایش کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>transition-duration، transform matrix، opacity و state selector فعال را بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/style-tab-effects/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Effects</a>، <a href="https://www.w3.org/TR/css-transforms-1/" rel="noopener noreferrer" target="_blank">W3C — CSS Transforms</a>، <a href="https://www.w3.org/TR/css-values-4/#time" rel="noopener noreferrer" target="_blank">W3C — CSS Values time data type</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-16-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-16-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — Audit</h3><p>پروژهٔ TUYA بیشتر اطلاعاتی است، اما این موارد را بررسی کن:</p><ul>
<li>Logo لینک‌دار Focus واضح دارد؛</li>
<li>اگر سکشن CTA دارد، Button در Hover و Focus قابل تشخیص است؛</li>
<li>Imageهای محتوایی Alt مناسب دارند؛</li>
<li>Nodeهای تزئینی برای Screen Reader مزاحمت ایجاد نمی‌کنند؛</li>
<li>Zoom 200% باعث هم‌پوشانی متن و Visual نمی‌شود.</li>
</ul><h3>❓ سؤال توقف</h3><p>اگر Button فقط در Hover تغییر کند، کاربر Keyboard چه چیزی را از دست می‌دهد؟</p><details class="disclosure-card"><summary>پاسخ</summary>نشانهٔ واضح Focus و بازخورد تعامل.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> Outline Focus را حذف کنی چون ظاهرش را دوست نداری.</p><p><strong>راه درست:</strong> Focus Style جایگزین و واضح طراحی کن.</p><h3>🧪 عمداً خرابش کن</h3><p>Focus Style Button آزمایشی را حذف کن و فقط با Tab حرکت کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>نمی‌دانی کدام Element فعال است؛</li>
<li>مسیر Keyboard مبهم می‌شود؛</li>
<li>Hover با Keyboard فعال نمی‌شود.</li>
</ul><p>Focus واضح را برگردان.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-237-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-237-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-90"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-90-1" name="chk-90-1" type="checkbox"/><span>مسیر Tab قابل دنبال‌کردن است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-90-2" name="chk-90-2" type="checkbox"/><span>Focus پشت Sticky یا Overlay پنهان نمی‌شود</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-90-3" name="chk-90-3" type="checkbox"/><span>Zoom 200% محتوا را غیرقابل استفاده نمی‌کند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-90-4" name="chk-90-4" type="checkbox"/><span>Alt و Decoration از هم تفکیک شده‌اند</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Focus چه تفاوتی با Hover دارد؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> Menu فقط با Hover باز می‌شود. برای Keyboard و Touch چه چیزی کم است؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-91"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-91-1" name="chk-91-1" type="checkbox"/><span>State دقیق Normal/Hover/Focus را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-91-2" name="chk-91-2" type="checkbox"/><span>Keyboard و Touch را در کنار Mouse در نظر گرفته است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-91-3" name="chk-91-3" type="checkbox"/><span>Focus قابل دیدن و مسیر تعامل مستقل از Hover را بررسی کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-16-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-16-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-REUSE-001 — Button State</h3><p><strong>هدف:</strong> 🔧 بازسازی کن</p><p>Buttonهای تکراری فرصت مناسبی برای Class پایه، Variant و State مشترک هستند.</p><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">button-base
button-primary
Hover/Focus state
Local content/link</pre></figure><h3>🔬 پشت صحنه</h3><p><code class="inline-code" dir="ltr">:hover</code> و <code class="inline-code" dir="ltr">:focus-visible</code> مفاهیم CSS پشت Stateهای رابط هستند؛ نیازی به نوشتن دستی آن‌ها نداری.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-16-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-16-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-93"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-93-1" name="chk-93-1" type="checkbox"/><span>می‌توانی Normal، Hover و Focus را به‌عنوان Stateهای متفاوت توضیح بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-93-2" name="chk-93-2" type="checkbox"/><span>می‌توانی بگویی چرا Hover تنها مسیر نمایش اطلاعات نیست.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-94"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-94-1" name="chk-94-1" type="checkbox"/><span>برای عنصر تعاملی Focus واضح و Hover مکمل می‌سازی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-94-2" name="chk-94-2" type="checkbox"/><span>صفحه را فقط با Keyboard طی می‌کنی و Focus پنهان یا Trap را ثبت می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-95"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-95-1" name="chk-95-1" type="checkbox"/><span>برای Card کلیک‌پذیر می‌توانی تفاوت Style Hover و رفتار دسترسی‌پذیر Keyboard را توضیح بدهی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-16-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-16-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد Classها، Variableها و Componentها را به یک Design System کوچک تبدیل می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 16</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-16-completion"><fieldset><legend>ثبت پایان درس 16</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-16-complete" name="lesson-16-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-16-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: State، Interaction، Hover و Transition</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>State در برابر Interaction</h3><p>State می‌پرسد «در این وضعیت چه شکلی باشد؟» Interaction می‌پرسد «وقتی کاربر کاری کرد یا صفحه حرکت کرد، چه رفتاری رخ دهد؟»</p></section>
<section class="inline-compare-card"><h3>Hover State در برابر Transition</h3><p>Hover State مقصد است؛ Transition مسیر رسیدن به مقصد. اول بگو Hover چه شکلی است، بعد مدت و نرمی تغییر را تنظیم کن.</p></section>
</div>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="states-extra-title" role="heading">تکمیل نسخه 22 — Stateهای مهم‌تر از Hover</span></summary><section aria-labelledby="states-extra-title" class="smart-note-card disclosure-content">
<p>در Elementor، بسته به Element/Element/Widget آماده، معمولاً حالت‌هایی مثل Normal، Hover و گاهی Active دیده می‌شود. در CSS عمومی، stateهای بیشتری هم وجود دارند که برای دسترسی‌پذیری و لینک‌ها مهم‌اند.</p>
<div class="table-scroll"><table>
<caption>Stateهای رایج در UI؛ شامل Focus، Active و Visited</caption>
<thead><tr><th scope="col">State</th><th scope="col">کی فعال می‌شود؟</th><th scope="col">تلهٔ رایج</th></tr></thead>
<tbody>
<tr><td><code class="inline-code" dir="ltr">Normal</code></td><td>حالت پایه</td><td>همه‌چیز را در Hover تعریف نکن.</td></tr>
<tr><td><code class="inline-code" dir="ltr">Hover</code></td><td>وقتی pointer روی عنصر است</td><td>در موبایل همیشه همان رفتار دسکتاپ را ندارد.</td></tr>
<tr><td><code class="inline-code" dir="ltr">Focus</code></td><td>وقتی عنصر با keyboard/input فعال است</td><td>حذف outline بدون جایگزین، مشکل دسترسی‌پذیری است.</td></tr>
<tr><td><code class="inline-code" dir="ltr">Focus-visible</code></td><td>وقتی مرورگر تشخیص می‌دهد focus باید دیده شود</td><td>برای keyboard UX مهم‌تر از focus خام است.</td></tr>
<tr><td><code class="inline-code" dir="ltr">Active</code></td><td>لحظهٔ کلیک/فعال‌سازی یا حالت آیتم فعال</td><td>با Hover یکی نیست.</td></tr>
<tr><td><code class="inline-code" dir="ltr">Visited</code> / <code class="inline-code" dir="ltr">:visited</code></td><td>برای لینک‌های دیده‌شده</td><td>در طراحی لینک‌ها باید آگاهانه تصمیم بگیری.</td></tr>
</tbody>
</table></div>
<p class="golden-rule"><strong>قانون طلایی:</strong> Button بدون Focus قابل‌دیدن، برای کاربر keyboard نیمه‌خراب است؛ فقط Hover را طراحی نکن.</p>
</section></details><details class="lesson-disclosure" id="lesson-16-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Hover روی Mobile قرارداد کافی نیست</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>در تجربهٔ لمسی Hover پایدار وجود ندارد. اطلاعات یا کنترل ضروری را فقط پشت Hover نگذار.</p>
<ul><li>Focus و Active را تست کن.</li><li>Targetهای تعاملی را برای لمس قابل استفاده نگه دار.</li><li>اگر Nodeهای TUYA صرفاً تصویری‌اند، آن‌ها را به کنترل جعلی تبدیل نکن.</li></ul>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-16-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Touch، Focus و نبود Hover پایدار</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> اطلاعات ضروری را از وابستگی به Hover نجات بده.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>برای یک Node یا Button حالت‌های Normal، Hover، Focus و Active بساز.</li><li>با keyboard و شبیه‌سازی touch آن را آزمایش کن.</li><li>اطلاعات ضروری را در Normal یا یک کنترل قابل فعال‌سازی نگه دار.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن کدام feedback در دستگاه لمسی بدون hover واقعی در دسترس می‌ماند.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>متن یا عملکرد ضروری را فقط در Hover نمایان کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>pseudo-class فعال، focus indicator، tab order و اندازهٔ target لمسی.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> کاربر بدون Hover هم به محتوا و عمل اصلی دسترسی دارد و Focus قابل مشاهده است.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-16-responsive-build-test-done-build"><input data-persist="" id="lesson-16-responsive-build-test-done-build" name="lesson-16-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-16-responsive-build-test-done-test"><input data-persist="" id="lesson-16-responsive-build-test-done-test" name="lesson-16-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-16-responsive-build-test-done-debug"><input data-persist="" id="lesson-16-responsive-build-test-done-debug" name="lesson-16-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-16-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-16-responsive-build-test-note" name="lesson-16-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/responsive-editing/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-16-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — State و transition</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
