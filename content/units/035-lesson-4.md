<article class="lesson card-surface" data-lesson="4" id="lesson-4"><h2 class="lesson-title former-h1">درس 4 — Box Model، Width و پوستهٔ سکشن</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-4-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-4-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> Padding، Margin، Width و Max Width را در نقش پوسته بفهمی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام واحدهای CSS را.</p><p><strong>در پایان باید بتوانی:</strong> یک سکشن تمام‌عرضِ کنترل‌شده و بدون Overflow بسازی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-4-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-4-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧩 ساختاری + 🛠 اجرایی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۱۵–۲۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۲۰–۳۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> Box Model را روی پوستهٔ واقعی اجرا می‌کنی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-4-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-4-lesson-understand-4">A. بفهم</h2><h3>🧠 مدل جعبه</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">MARGIN
  BORDER
    PADDING
      CONTENT</pre></figure></details><dl class="term-grid"><dt>Padding</dt><dd>فاصلهٔ داخل Background؛</dd><dt>Margin</dt><dd>فاصلهٔ بیرون Element؛</dd><dt>Width</dt><dd>اندازهٔ ترجیحی؛</dd><dt>Max Width</dt><dd>سقف رشد.</dd></dl><h3>تصمیم سریع</h3><section aria-labelledby="section-hidden-72-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-72-heading">بخش آموزشی</h2><dl class="term-grid"><dt>فاصله داخل رنگ سکشن؟</dt><dd>Padding</dd><dt>فاصله بیرون سکشن؟</dt><dd>Margin</dd><dt>جلوگیری از عریض‌شدن؟</dt><dd>Max Width</dd></dl></section><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="40f7eda0e41b8778c809594ff484cc434fab1cfd393556b0babc88a03311fef4" id="lesson-4-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Box Model، Width، Padding و Margin</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="4" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-04-section-01" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-04-section-01">تصویر ذهنی اصلی: خانه و حیاط</h3><p>هر Element را مثل یک خانه تصور کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">┌──────────────────────────┐
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
└──────────────────────────┘
</code></pre></figure><p>تعریف «Padding داخل است و Margin بیرون» درست است، اما برای فهم Width و Overflow کافی نیست.</p><hr/></section><section aria-labelledby="concept-v31-04-section-02" class="concept-reference-part"><h3 id="concept-v31-04-section-02">چهار لایهٔ Box</h3><ol>
<li><strong>Content Box:</strong> متن، تصویر یا محتوای اصلی</li>
<li><strong>Padding Box:</strong> فضای تنفس بین محتوا و Border</li>
<li><strong>Border Box:</strong> لبهٔ قابل‌دیدن جعبه</li>
<li><strong>Margin Box:</strong> فضای بیرونی برای رابطه با همسایه‌ها</li>
</ol><hr/></section><section aria-labelledby="concept-v31-04-section-03" class="concept-reference-part"><h3 id="concept-v31-04-section-03">Padding؛ فضای داخل ملک</h3><p>Padding خود Element را بزرگ‌تر می‌کند و Background وارد آن می‌شود.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.card {
  background: #fff;
  padding: 24px;
}
</code></pre></figure><p>Background سفید هم پشت محتوا و هم پشت Padding دیده می‌شود.</p><h4>چرا ساخته شده؟</h4><p>برای اینکه محتوا به دیوارهٔ خودش نچسبد.</p><h4>در Elementor</h4><p>Padding روی Container یا Element یعنی محتوا از لبه‌های همان جعبه فاصله می‌گیرد.</p><blockquote>
<p><strong>قانون:</strong> Padding دیوار را از وسایل داخل خانه دور می‌کند.</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-04-section-04" class="concept-reference-part"><h3 id="concept-v31-04-section-04">Margin؛ فضای بیرون ملک</h3><p>Margin بین Border یک Element و محیط اطراف آن فاصله ایجاد می‌کند. Background وارد Margin نمی‌شود.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.card {
  margin-block-end: 32px;
}
</code></pre></figure><h4>چرا ساخته شده؟</h4><p>برای رابطهٔ بیرونی جعبه با همسایه‌ها.</p><blockquote>
<p><strong>قانون:</strong> Margin خانه را از همسایه‌ها دور می‌کند.</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-04-section-05" class="concept-reference-part"><h3 id="concept-v31-04-section-05">Width واقعاً چه چیزی را اندازه می‌گیرد؟</h3><p>پاسخ به <code class="inline-code" dir="ltr">box-sizing</code> بستگی دارد.</p><h4>حالت پیش‌فرض: content-box</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.box {
  width: 300px;
  padding: 20px;
  border: 2px solid;
}
</code></pre></figure><p>عرض مرزی واقعی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">300 + 20 + 20 + 2 + 2 = 344px
</code></pre></figure><h4>حالت رایج: border-box</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.box {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 2px solid;
}
</code></pre></figure><p>در این حالت Padding و Border داخل همان 300px محاسبه می‌شوند.</p><hr/></section><section aria-labelledby="concept-v31-04-section-06" class="concept-reference-part"><h3 id="concept-v31-04-section-06">Width، Min-width و Max-width</h3><p>این سه را یک قرارداد ببین:</p><ul>
<li><code class="inline-code" dir="ltr">width</code> = اندازهٔ ترجیحی یا اعلام‌شده</li>
<li><code class="inline-code" dir="ltr">min-width</code> = از این کوچک‌تر نشو</li>
<li><code class="inline-code" dir="ltr">max-width</code> = از این بزرگ‌تر نشو</li>
</ul><p>مثال استاندارد Shell:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.shell {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}
</code></pre></figure><p>در Elementor می‌توان همان منطق را با Width، Max Width و Padding کناری ساخت.</p><hr/></section><section aria-labelledby="concept-v31-04-section-07" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-04-section-07">چرا <code class="inline-code" dir="ltr">width: 100%</code> گاهی Overflow می‌دهد؟</h3><p>در <code class="inline-code" dir="ltr">content-box</code>، 100٪ فقط Content را می‌گیرد و Padding/Border ممکن است به آن اضافه شوند.</p><p>همچنین اگر به Element تمام‌عرض Margin افقی مثبت بدهی، Outer Size از Parent بزرگ‌تر می‌شود.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Parent = 1000px
Child width = 1000px
Margin left + right = 40px
Outer width = 1040px
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-04-section-08" class="concept-reference-part"><h3 id="concept-v31-04-section-08">Margin Collapse؛ نکته‌ای که باید دقیق بدانی</h3><p>Marginهای عمودی بعضی Blockها در Normal Flow ممکن است با هم Collapse شوند؛ یعنی جمع ساده نشوند و به یک Margin مشترک تبدیل شوند.</p><p>اما این رفتار در Flex و Grid Itemها مانند Normal Block Flow رخ نمی‌دهد.</p><p>پس اگر دو Margin عمودی نتیجهٔ عجیب دارند، ابتدا نوع Layout را بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-04-section-09" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-04-section-09">پل به DevTools؛ خانه را واقعاً ببین</h3><p>در مرورگر روی Element راست‌کلیک کن و <strong>Inspect</strong> را بزن. در پنل <strong>Computed</strong> یا نمای Box Model می‌توانی چهار لایهٔ Content، Padding، Border و Margin را با اندازهٔ واقعی ببینی. اینجا تفاوت عددی <code class="inline-code" dir="ltr">content-box</code> و <code class="inline-code" dir="ltr">border-box</code> دیگر یک تعریف حفظی نیست؛ مرورگر عرض نهایی را جلوی چشمت نشان می‌دهد.</p><p>برای عیب‌یابی Overflow، فقط عدد Width را نگاه نکن. Min Width، Padding، Border، Scrollbar، Gap و محتوای نشکن را هم در Computed Style بررسی کن.</p></section><section aria-labelledby="concept-v31-04-section-10" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-04-section-10">سناریوی واقعی Elementor</h3><p>یک کارت خدمات:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Card
├── Icon
├── Heading
└── Description
</code></pre></figure><ul>
<li>فضای محتوا از لبهٔ کارت → Padding کارت</li>
<li>فاصلهٔ Icon و Heading → Gap Parent یا Margin منطقی</li>
<li>فاصلهٔ کارت با کارت بعد → Gap Grid/Flex یا Margin بیرونی</li>
<li>محدودکردن پهنای کارت → Width/Max Width</li>
</ul><hr/></section><section aria-labelledby="concept-v31-04-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-04-section-11">تله‌های رایج</h3><ul>
<li>استفاده از Margin برای فاصلهٔ محتوای داخل کارت</li>
<li>افزودن <code class="inline-code" dir="ltr">overflow: hidden</code> بدون پیدا کردن علت Overflow</li>
<li>دادن Width ثابت به محتوای Responsive</li>
<li>فراموش‌کردن Border و Padding در محاسبهٔ اندازه</li>
<li>استفاده از Marginهای پراکنده به‌جای Gap در Siblingهای تکراری</li>
</ul><hr/></section><section aria-labelledby="concept-v31-04-section-12" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-04-section-12">روش تشخیص سریع</h3><p>بپرس:</p><h4>چه چیزی باید فاصله بگیرد؟</h4><ul>
<li>محتوا از لبهٔ خودش → Padding</li>
<li>خود Element از همسایه → Margin یا Gap</li>
<li>چند Sibling با فاصلهٔ یکنواخت → Gap</li>
</ul><h4>چه چیزی از Parent بیرون زده؟</h4><p>DevTools را باز کن و Content/Padding/Border/Margin را جدا ببین.</p><hr/></section><section aria-labelledby="concept-v31-04-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-04-section-13">تصویر ذهنی نهایی</h3><p>Content وسایل خانه، Padding فضای حرکت داخل، Border دیوار و Margin حیاط بیرون است. <code class="inline-code" dir="ltr">border-box</code> می‌گوید عدد عرض، دیوار تا دیوار را شامل شود؛ <code class="inline-code" dir="ltr">content-box</code> عدد را فقط برای فضای وسایل نگه می‌دارد.</p></section><section aria-labelledby="concept-v31-04-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-04-section-14">قوانین طلایی</h3><ul>
<li><strong>«Padding فضای داخل ملک است؛ Margin فضای بیرون ملک.»</strong></li>
<li><strong>«Background وارد Padding می‌شود، وارد Margin نمی‌شود.»</strong></li>
<li><strong>«Width بدون دانستن <code class="inline-code" dir="ltr">box-sizing</code> عدد کاملی نیست.»</strong></li>
<li><strong>«اگر چند Sibling فاصلهٔ مشترک دارند، Gap معمولاً از Margin تمیزتر است.»</strong></li>
<li><strong>«Overflow را پنهان نکن؛ منبع اندازهٔ اضافه را پیدا کن.»</strong></li>
<li><strong>«<code class="inline-code" dir="ltr">min-width</code> و محتوای نشکن می‌توانند از Width قوی‌تر ظاهر شوند.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>MDN: CSS Box Model</li>
<li>MDN: box-sizing</li>
<li>Elementor Help: Style tab — Size</li>
<li>Elementor Help: Style tab — Spacing</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-4-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-4-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Width، Padding و Margin؛ واحد مشابه، مرجع متفاوت</span></summary>
<section aria-labelledby="lesson-4-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">یک واحد فقط طول را می‌سازد؛ Property مشخص می‌کند طول کجا مصرف شود. 2rem برای Width و 2rem برای Padding هر دو از root font می‌آیند، اما اثرشان متفاوت است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> یک خط‌کش ثابت داری؛ یک بار با آن عرض جعبه را می‌سنجی و بار دیگر ضخامت ضربه‌گیر داخل جعبه را.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Width / Min / Max</th><td><code dir="ltr">width / min-width / max-width</code></td><td>PX، %، VW در کنترل‌های مستند Container؛ CSS گزینه‌های بیشتری دارد</td><td>% نسبت به containing block؛ VW نسبت به viewport</td><td>برای Child سیال % و برای سقف کنترل‌شده px/rem یا max-width مناسب است.</td><td>CSS-supported را با UI-exposed یکی نگیر.</td><td><code dir="ltr">E_CONTAINER_SIZE</code></td></tr><tr><th scope="row">Margin</th><td><code dir="ltr">margin-*</code></td><td>PX، EM، %، REM در تنظیمات مستند Container</td><td>EM نسبت به font-size؛ % طبق Property/containing block</td><td>برای فاصلهٔ بیرونی و رابطه با sibling.</td><td>روی top-level full-width می‌تواند overflow بسازد.</td><td><code dir="ltr">E_CONTAINER_ADV</code></td></tr><tr><th scope="row">Padding</th><td><code dir="ltr">padding-*</code></td><td>PX، EM، %، REM در تنظیمات مستند Container</td><td>درون Border؛ درصدها باید با احتیاط تست شوند</td><td>برای فاصلهٔ داخلی Shell.</td><td>Padding را برای جابه‌جایی بیرونی استفاده نکن.</td><td><code dir="ltr">E_CONTAINER_ADV</code></td></tr><tr><th scope="row">Box sizing</th><td><code dir="ltr">box-sizing</code></td><td>content-box / border-box</td><td>keyword</td><td>برای فهمیدن اینکه Width چه ناحیه‌ای را پوشش می‌دهد.</td><td>Outer size را فقط از width حدس نزن.</td><td><code dir="ltr">CSS_VALUES</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>Parent=1200px؛ Child width=100% → 1200px. اگر margin-inline دو طرف 80px باشد، outer size تقریبی 1360px می‌شود و 160px از Parent بزرگ‌تر است.</p></section>
<section><h3>📱 در Responsive</h3><p>در Mobile معمولاً Width و padding-inline override می‌شوند؛ واحد را فقط زمانی عوض کن که مرجع محاسبه باید عوض شود.</p></section>
<section><h3>🔬 در DevTools</h3><p>Box Model، width/min/max، box-sizing و margin-inline-start/end را هم‌زمان بخوان.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/set-flexbox-container-size-behavior/" rel="noopener noreferrer" target="_blank">Elementor — Flexbox container size and behavior</a>، <a href="https://elementor.com/help/container-advanced-tab-settings/" rel="noopener noreferrer" target="_blank">Elementor — Container advanced settings</a>، <a href="https://elementor.com/help/style-tab-spacing/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Spacing</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length" rel="noopener noreferrer" target="_blank">MDN — CSS length values</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-4-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-4-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — ساخت پوسته</h3><p>Element: <code class="inline-code" dir="ltr">Platform Section</code><br/>
کلاس هدف ویرایش: <code class="inline-code" dir="ltr">c-platform-section</code></p><p>تنظیمات پیشنهادی آغازین:</p><section aria-labelledby="section-hidden-74-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-74-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Width</dt><dd>100%</dd><dt>Max Width</dt><dd>مقدار متناسب با صفحه</dd><dt>Margin Inline</dt><dd>Auto</dd><dt>Padding Inline</dt><dd>سیال و کنترل‌شده</dd><dt>Padding Block</dt><dd>سیال و کنترل‌شده</dd><dt>Background</dt><dd>خاکستری روشن</dd><dt>Border Radius</dt><dd>مقدار متوسط</dd></dl></section><p>اعداد دقیق <code class="inline-code" dir="ltr">proposed</code> هستند و باید با Preview بررسی شوند.</p><h3>❓ سؤال توقف</h3><p>برای اینکه Background خاکستری تا اطراف محتوا ادامه پیدا کند، Padding می‌خواهی یا Margin؟</p><details class="disclosure-card"><summary>پاسخ</summary>Padding.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> برای فاصلهٔ داخلی از Margin استفاده کنی.</p><p><strong>نشانه:</strong> Background کوتاه می‌شود و فضای سفید بیرون سکشن می‌بینی.</p><h3>🧪 عمداً خرابش کن</h3><p>Width را <code class="inline-code" dir="ltr">100vw</code> و Margin افقی را بزرگ کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>احتمال اسکرول افقی؛</li>
<li>خروج سکشن از محدودهٔ صفحه؛</li>
<li>مشکل در عرض‌های باریک.</li>
</ul><p>Width را به 100% برگردان و Max Width را جدا کنترل کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-75-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-75-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-19"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-19-1" name="chk-19-1" type="checkbox"/><span>Background خاکستری کل Padding را پوشش می‌دهد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-19-2" name="chk-19-2" type="checkbox"/><span>سکشن در 320px Overflow ندارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-19-3" name="chk-19-3" type="checkbox"/><span>Max Width رشد را محدود می‌کند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-19-4" name="chk-19-4" type="checkbox"/><span>Margin و Padding نقش درست دارند</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Padding و Margin چه تفاوتی دارند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> پس‌زمینهٔ سکشن کوتاه شده، اما فقط فاصلهٔ داخلی می‌خواستی. کدام Control محتمل است اشتباه باشد؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-20"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-20-1" name="chk-20-1" type="checkbox"/><span>فضای داخل و بیرون Box را از هم جدا کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-20-2" name="chk-20-2" type="checkbox"/><span>Width و Max Width را برای Parent درست تشخیص داده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-20-3" name="chk-20-3" type="checkbox"/><span>راه‌حل پیشنهادی در 320px Overflow ایجاد نمی‌کند.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-4-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-4-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-HOME2-GRID-001 — Viewport Width</h3><p><strong>هدف:</strong> 👁 فقط مشاهده کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">legacy_or_hybrid</code></p><p>Hero صفحهٔ Home2 در Export دارای <code class="inline-code" dir="ltr">100vw</code> و <code class="inline-code" dir="ltr">100vh</code> است. این مقادیر الزاماً غلط نیستند، اما نیاز به تست Scrollbar، Mobile Browser UI و Runtime دارند.</p><h3>🔬 پشت صحنه</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text language-css" dir="ltr">width: 100%;
max-width: ...;
padding: ...;
margin-inline: auto;
</code></pre><p>کد را حفظ نکن؛ رابطهٔ Controlها را بفهم.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="memory-box-model-heading" role="heading">🧠 لایهٔ حافظه — Padding، Margin و پوسته</span></summary><section aria-labelledby="memory-box-model-heading" class="memory-layer disclosure-content lesson-section"><p><strong>🧠 استعارهٔ ماندگار:</strong> Padding فضای داخل خانه است؛ Margin حیاط بیرون خانه است؛ Width اندازهٔ خود خانه است.</p><p><strong>🧩 در Elementor V4 یعنی چه؟</strong> برای فاصلهٔ متن از لبهٔ کارت، Padding بده. برای فاصلهٔ کارت از عنصر کناری، Margin یا Gap را بررسی کن.</p><p><strong>⚠️ تله رایج:</strong> با Margin داخل کارت را نفس‌دار نمی‌کنی؛ فقط خود کارت را جابه‌جا می‌کنی.</p><p class="golden-rule"><strong>📜 قانون طلایی:</strong> اول معلوم کن فاصله داخل جعبه است یا بیرون جعبه؛ بعد property را انتخاب کن.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-4-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-4-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><section aria-labelledby="box-model-step-title" class="step-simulator step-simulator-box-model" data-simulator-type="box-model" data-step-simulator="" id="box-model-step"><h3 id="box-model-step-title">Step‑Through — Box Model لایه‌به‌لایه</h3><p>با هر کلیک یک لایه اضافه می‌شود تا تفاوت فضای داخل و بیرون جعبه دیده شود.</p><div aria-live="polite" class="simulator-viewport"><p class="simulator-label" data-step-label=""></p><div class="simulator-rail simulator-rail-box-model" data-step-render=""></div><code class="simulator-code" data-step-code="" dir="ltr"></code></div><div class="simulator-actions"><button aria-label="نمایش حالت قبلی" class="ui-btn" data-step-prev="" type="button">حالت قبلی</button><button aria-label="نمایش حالت بعدی" class="ui-btn" data-step-next="" type="button">حالت بعدی</button></div><script class="simulator-data" type="application/json">[{"label":"حالت ۱ از ۴ — فقط Content: اندازهٔ داخلی بدون فضای اضافه.","code":"box-sizing: content-box; padding: 0; border: 0; margin: 0;","content":"Content","padding":0,"border":0,"margin":0},{"label":"حالت ۲ از ۴ — Padding داخل Background را بزرگ می‌کند.","code":"padding: 24px;","content":"Content","padding":24,"border":0,"margin":0},{"label":"حالت ۳ از ۴ — Border دور Padding و Content قرار می‌گیرد.","code":"padding: 24px; border: 4px solid;","content":"Content","padding":24,"border":4,"margin":0},{"label":"حالت ۴ از ۴ — Margin بیرون Border فاصله می‌سازد.","code":"padding: 24px; border: 4px solid; margin: 24px;","content":"Content","padding":24,"border":4,"margin":24}]</script><p class="golden-rule"><strong>قانون طلایی:</strong> Padding داخل Background است؛ Margin بیرون Border است.</p></section><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-22"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-22-1" name="chk-22-1" type="checkbox"/><span>می‌توانی Content، Padding، Border و Margin را روی یک Box نشان بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-22-2" name="chk-22-2" type="checkbox"/><span>می‌توانی فرق Width و Max Width را در یک Wrapper توضیح بدهی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-23"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-23-1" name="chk-23-1" type="checkbox"/><span>پوستهٔ خاکستری TUYA را با Padding داخلی، Radius و Max Width می‌سازی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-23-2" name="chk-23-2" type="checkbox"/><span>در Preview برابر 320px ثابت می‌کنی پوسته اسکرول افقی ایجاد نمی‌کند.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-24"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-24-1" name="chk-24-1" type="checkbox"/><span>در سناریوی «پس‌زمینه کوتاه شده ولی فاصلهٔ داخلی می‌خواستم» می‌توانی تشخیص بدهی Margin به‌جای Padding استفاده شده است.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-4-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-4-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>ایستگاه A کامل شد. یک‌بار Tree، Class و پوسته را بدون راهنما بازسازی کن؛ سپس وارد Layout شو.</p><hr/><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 4</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-4-completion"><fieldset><legend>ثبت پایان درس 4</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-4-complete" name="lesson-4-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-4-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: فاصله، پوسته و اندازه</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Padding در برابر Margin در برابر Gap</h3><p><strong>Padding</strong> فضای داخل جعبه است؛ <strong>Margin</strong> فاصلهٔ بیرونی یک جعبه با اطراف است؛ <strong>Gap</strong> فاصلهٔ منظم بین فرزندان یک Flex/Grid است.</p><p>اگر محتوا درون کارت نفس ندارد، Padding. اگر دو کارت به هم چسبیده‌اند، Gap یا Margin. اگر فاصله بین همهٔ فرزندان یک parent است، اول Gap را بررسی کن.</p></section>
<section class="inline-compare-card"><h3>Width در برابر Max Width</h3><p><strong>Width</strong> یعنی «همین‌قدر باش». <strong>Max Width</strong> یعنی «از این بزرگ‌تر نشو، اما می‌توانی کوچک‌تر شوی».</p><p class="golden-rule">قانون طلایی: برای صفحهٔ responsive، Max Width اغلب از Width خشک امن‌تر است.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="lesson-4-practical-findings"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-4-practical-findings-heading" role="heading">🔎 یافته‌های عملی و خطایابی</span></summary><section aria-labelledby="lesson-4-practical-findings-heading" class="disclosure-content practical-findings">
<p class="finding-scope">این بخش فقط ادعاهایی را آموزش می‌دهد که یا در مشاهدهٔ واقعی ثبت شده‌اند یا Help Center رسمی Elementor آن‌ها را صریحاً پشتیبانی می‌کند. نتیجه‌های وابسته به Theme، نسخه یا ساختار DOM با دامنهٔ اعتبار نوشته شده‌اند.</p>
<article class="finding-card real-observation" data-verification="verified_by_real_observation verified_by_official_help" id="finding-flex-margin-full-width">
<div class="evidence-badges"><span class="evidence-badge observed">مشاهدهٔ واقعی رضا</span><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>یافته ۱ — چرا margin سمت راست دیده نمی‌شد، اما با Width روی Auto درست شد؟</h3>
<ol class="case-steps">
<li><strong>چیزی که دیده شد:</strong> Flexbox خاکستری با ارتفاع <code class="inline-code" dir="ltr">40vh</code> و margin افقی ۸۰px؛ فاصلهٔ سمت چپ دیده می‌شد اما سمت راست ظاهراً نه. انتخاب صریح Width روی <code class="inline-code" dir="ltr">auto</code> بدون عدد، ظاهر را اصلاح کرد.</li>
<li><strong>برداشت اشتباه مبتدی:</strong> «margin راست در RTL یا Elementor خراب است.»</li>
<li><strong>آنچه از Capture ثابت شد:</strong> هر دو margin واقعاً ۸۰px بودند؛ خود جعبه فضای کامل موجود را گرفته بود و margin انتهایی به overflow تبدیل می‌شد.</li>
<li><strong>قاعدهٔ مستند Elementor:</strong> Containerهای Boxed و Full Width به‌طور پیش‌فرض در فضای موجود stretch می‌شوند. Help Center هشدار می‌دهد margin افقی روی top-level container می‌تواند مجموع عرض را از صفحه بیشتر و scrollbar افقی ایجاد کند؛ برای margin افقی، child container پیشنهاد می‌شود.</li>
<li><strong>چرا Auto کمک کرد؟</strong> در این مشاهده، Auto قانون sizing قبلی را کنار زد و used width دوباره محاسبه شد. این را با «همیشه shrink-to-fit» یکی ندان؛ نتیجه به parent، flex sizing و rule نهایی CSS وابسته است.</li>
</ol>
<div class="finding-checks">
<section><h4>در Elementor کجا چک کنم؟</h4><p>Layout → Content Width/Width، جایگاه top-level یا nested، و spacing والد/فرزند.</p></section>
<section><h4>در DevTools کجا چک کنم؟</h4><p>Computed: <code dir="ltr">width</code>، <code dir="ltr">inline-size</code>، marginها، <code dir="ltr">flex-basis/grow/shrink</code>؛ سپس Box Model و matched CSS rule.</p></section>
<section><h4>راه‌حل پایدار</h4><p>برای shell تمام‌عرض معمولاً <code dir="ltr">padding-inline</code> روی والد یا child محدود و وسط‌چین بهتر از margin دوطرفه روی top-level است.</p></section>
</div>
<p class="golden-rule"><strong>قانون طلایی:</strong> دیده‌نشدن margin الزاماً یعنی اعمال‌نشدن آن نیست؛ ممکن است margin بیرون از عرض قابل‌دیدن قرار گرفته باشد.</p>
<details class="more-know"><summary>منبع و دامنهٔ اعتبار</summary><p><strong>منبع رسمی:</strong> <a href="https://elementor.com/help/set-flexbox-container-size-behavior/">Set a Flexbox Container’s size and behavior</a>. <strong>مشاهدهٔ واقعی:</strong> فایل خطایابی ضمیمه‌شده در <code>source/v24-practical-findings/</code>. انتساب دقیق rule اولیه به Elementor یا Theme فقط با matched CSS rule قطعی می‌شود.</p></details>
</article>
<article class="finding-card" data-verification="verified_by_official_help" id="finding-full-width-theme-template">
<div class="evidence-badges"><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>یافته ۲ — چرا Full Width انتخاب کرده‌ام ولی صفحه هنوز محدود است؟</h3>
<p><strong>نشانه:</strong> داخل Element یا Container عرض کامل تنظیم شده، ولی canvas یا frontend همچنان در یک ستون محدود باقی می‌ماند.</p>
<p><strong>علت‌های رسمی محتمل:</strong> صفحه تنظیمات layout پیش‌فرض Theme را به ارث برده یا یک Single Page template عرض را محدود می‌کند.</p>
<div class="finding-checks">
<section><h4>اول کجا چک کنم؟</h4><p>Page Settings → Page Layout. برای حفظ Header/Footer از <strong>Elementor Full Width</strong> و برای حذف آن‌ها از <strong>Elementor Canvas</strong> استفاده کن.</p></section>
<section><h4>چه کاری نکنم؟</h4><p>قبل از بررسی Page Layout، با Widthهای بزرگ، margin منفی یا CSS اجباری مشکل را پنهان نکن.</p></section>
</div>
<p class="golden-rule"><strong>قانون طلایی:</strong> عرض Element داخل صفحه نمی‌تواند همیشه محدودیت layout خود صفحه یا Theme template را بشکند.</p>
<details class="more-know"><summary>منبع رسمی</summary><p><a href="https://elementor.com/help/full-width-not-working/">Elementor full width not working</a></p></details>
</article>
</section></details>
<details class="lesson-disclosure" id="lesson-4-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Shell، Width و Height در Mobile</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>ارتفاع <code>40vh</code> دسکتاپ را بدون بررسی به Mobile منتقل نکن. طرح Mobile پیوست‌شده محتوای بلند و عمودی دارد؛ بنابراین ارتفاع باید محتوامحور باشد یا فقط یک <code>min-height</code> کنترل‌شده بگیرد.</p>
<ul><li>فاصلهٔ لبهٔ صفحه را با <code>padding-inline</code> روی Shell مدیریت کن.</li><li>Width و Min Height را در breakpoint Mobile مستقل بررسی کن.</li><li>برای Stage تصویری از <code>aspect-ratio</code> و محدودیت‌های min/max استفاده کن؛ عدد دقیق از تصویر قابل استخراج نیست.</li></ul>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure step-through-v2-disclosure" id="stv2-width-margin-overflow">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="stv2-width-margin-overflow-heading" role="heading">▶ Step‑Through v2 — Width، Margin و Overflow — از نشانه تا علت</span>
</summary>
<section aria-labelledby="stv2-width-margin-overflow-heading" class="disclosure-content step-through-v2" data-step-through-v2="" data-stv2-id="stv2-width-margin-overflow" data-stv2-renderer="width-overflow" tabindex="0">
<header class="stv2-header">
<p class="stv2-kicker">چرخهٔ فعال: ببین ← پیش‌بینی کن ← بررسی کن ← خراب کن ← انتقال بده</p>
<p><strong>🎯 هدف:</strong> ببین چرا margin ممکن است اعمال شده باشد اما فاصلهٔ انتهایی به overflow تبدیل شود.</p>
<div aria-label="وضعیت شواهد" class="stv2-evidence-row"><span class="stv2-evidence-badge">تأییدشده با Help Center رسمی Elementor</span><span class="stv2-evidence-badge">تأییدشده با استاندارد CSS</span><span class="stv2-evidence-badge">مشاهدهٔ واقعی</span></div>
</header>
<div class="stv2-progress-row">
<span class="stv2-step-count" data-stv2-count="">مرحله ۱</span>
<progress data-stv2-progress="" max="5" value="1">1/5</progress>
<span class="stv2-phase" data-stv2-phase=""></span>
</div>
<div class="stv2-three-view">
<section aria-labelledby="stv2-width-margin-overflow-visual-title" class="stv2-card stv2-visual-card">
<h3 id="stv2-width-margin-overflow-visual-title">👁 نتیجهٔ بصری</h3>
<div aria-label="نمای بصری مرحله" class="stv2-visual" data-stv2-visual=""></div>
</section>
<section aria-labelledby="stv2-width-margin-overflow-elementor-title" class="stv2-card">
<h3 id="stv2-width-margin-overflow-elementor-title">🧩 تنظیم Elementor</h3>
<dl class="stv2-definition-list" data-stv2-elementor=""></dl>
</section>
<section aria-labelledby="stv2-width-margin-overflow-computed-title" class="stv2-card">
<h3 id="stv2-width-margin-overflow-computed-title">🔬 Computed / مدل محاسباتی</h3>
<dl class="stv2-definition-list" data-stv2-computed=""></dl>
<p class="stv2-model-note">اعداد نمایشی ممکن است مدل آموزشی باشند؛ برچسب شواهد هر مرحله را ببین.</p>
</section>
</div>
<section aria-labelledby="stv2-width-margin-overflow-state-title" class="stv2-explanation">
<h3 data-stv2-title="" id="stv2-width-margin-overflow-state-title"></h3>
<p data-stv2-summary=""></p>
<p data-stv2-explanation=""></p>
<p class="golden-rule"><strong>📜 قانون طلایی:</strong> <span data-stv2-golden=""></span></p>
<p><strong>وضعیت این مرحله:</strong> <code class="inline-code" data-stv2-evidence="" dir="ltr"></code></p>
</section>
<section aria-labelledby="stv2-width-margin-overflow-prediction-title" class="stv2-prediction">
<h3 id="stv2-width-margin-overflow-prediction-title">❓ پیش‌بینی کن</h3>
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
<p class="stv2-lab-link"><a href="#lesson-4-responsive-build-test">🧪 همین مفهوم را در «بساز و امتحان کن» اجرا کن</a></p>
<section aria-label="خلاصهٔ همهٔ مراحل برای چاپ" class="stv2-print-all"><div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table"><caption>خلاصهٔ همهٔ مراحل Step‑Through v2</caption><thead><tr><th scope="col">مرحله</th><th scope="col">نتیجه</th><th scope="col">وضعیت شواهد</th><th scope="col">قانون طلایی</th></tr></thead><tbody><tr><th scope="row">1 — عرض کامل، بدون margin</th><td>Child فضای موجود را پر می‌کند و outer size از Parent بزرگ‌تر نیست.</td><td><code class="inline-code" dir="ltr">simulated_explanation</code></td><td>قبل از افزودن فاصله، used width و فضای موجود والد را بشناس.</td></tr><tr><th scope="row">2 — عرض کامل + margin دوطرفه</th><td>margin اعمال شده، اما outer size از Parent بزرگ‌تر شده و سمت پایان بیرون می‌رود.</td><td><code class="inline-code" dir="ltr">verified_by_real_fixture</code></td><td>اعمال‌شدن property را با دیده‌شدن نتیجهٔ بصری یکی ندان.</td></tr><tr><th scope="row">3 — پنهان‌کردن علامت با Overflow Hidden</th><td>اسکرول یا بیرون‌زدگی دیده نمی‌شود، ولی outer size نامناسب همچنان وجود دارد.</td><td><code class="inline-code" dir="ltr">verified_by_css_spec</code></td><td>Overflow Hidden آخرین راه بررسی نیست؛ ابتدا عنصر overflowکننده را پیدا کن.</td></tr><tr><th scope="row">4 — Width Auto — workaround مشاهده‌شده، نه قانون جهانی</th><td>در مسئلهٔ واقعی رضا، انتخاب صریح Auto رفتار sizing را تغییر داد؛ نتیجه به layout context وابسته است.</td><td><code class="inline-code" dir="ltr">verified_by_real_fixture</code></td><td>از یک رفع مشکل واقعی، قانون عمومی نساز؛ context و matched rule را ثبت کن.</td></tr><tr><th scope="row">5 — الگوی پایدار: Padding والد + Child با Width مناسب</th><td>Shell فاصلهٔ صفحه را کنترل می‌کند و Main بدون افزودن outer margin داخل آن قرار می‌گیرد.</td><td><code class="inline-code" dir="ltr">verified_by_official_elementor_help</code></td><td>Shell فاصلهٔ صفحه را می‌سازد؛ Main داخل فضای باقی‌مانده چیدمان می‌شود.</td></tr></tbody></table></div></section>
<noscript><p class="warning-box">برای تعامل مرحله‌ای JavaScript محلی باید فعال باشد؛ خلاصهٔ چاپی همهٔ مراحل در همین بخش موجود است.</p></noscript>
<script class="stv2-config" type="application/json">{"goal":"ببین چرا margin ممکن است اعمال شده باشد اما فاصلهٔ انتهایی به overflow تبدیل شود.","id":"stv2-width-margin-overflow","lab_target":"lesson-4-responsive-build-test","lesson_id":"lesson-4","renderer":"width-overflow","schema_version":"1.0.0","states":[{"computed":[["Parent inline-size","320px — مدل آموزشی"],["Child used width","320px"],["Outer inline-size","320px"]],"elementor":[["Width","Full / فضای موجود"],["Margin inline","0"],["Overflow والد","Default"]],"evidence":"simulated_explanation","explanation":"این حالت مبناست. هنوز فاصلهٔ بیرونی به عرض جعبه اضافه نشده است.","golden_rule":"قبل از افزودن فاصله، used width و فضای موجود والد را بشناس.","id":"baseline-full","phase":"مشاهده","prediction":{"correct":1,"feedback_correct":"درست است؛ width و marginها باید با هم در outer size دیده شوند.","feedback_wrong":"دوباره Box Model را بخوان: margin بیرون border قرار می‌گیرد.","options":["همان 320px می‌ماند","تقریباً 368px می‌شود","به 272px کاهش می‌یابد"],"prompt":"اگر به Child با عرض کامل، 24px margin در هر دو سمت اضافه شود، outer size چه می‌شود؟"},"summary":"Child فضای موجود را پر می‌کند و outer size از Parent بزرگ‌تر نیست.","title":"عرض کامل، بدون margin","visual":{"margin":0,"mode":"baseline","padding":0}},{"computed":[["Parent inline-size","320px — مدل آموزشی"],["Child used width","320px"],["Outer inline-size","368px"],["Overflow","48px"]],"elementor":[["Width","Full / 100%"],["Margin inline","24px + 24px"],["Overflow والد","Default"]],"evidence":"verified_by_real_fixture","explanation":"نشانهٔ «margin کار نمی‌کند» می‌تواند در واقع overflow باشد. Computed Style باید قبل از نتیجه‌گیری بررسی شود.","golden_rule":"اعمال‌شدن property را با دیده‌شدن نتیجهٔ بصری یکی ندان.","id":"full-plus-margin","phase":"علت و معلول","prediction":{"correct":1,"feedback_correct":"دقیقاً؛ Hidden می‌تواند علامت را ببرد، نه علت را.","feedback_wrong":"Overflow نوع فاصله یا width را تغییر نمی‌دهد؛ فقط نمایش بخش بیرون‌زده را کنترل می‌کند.","options":["اصلاح می‌شود","پنهان می‌شود اما باقی می‌ماند","margin به padding تبدیل می‌شود"],"prompt":"اگر فقط overflow والد را Hidden کنیم، علت sizing چه می‌شود؟"},"summary":"margin اعمال شده، اما outer size از Parent بزرگ‌تر شده و سمت پایان بیرون می‌رود.","title":"عرض کامل + margin دوطرفه","visual":{"margin":24,"mode":"overflow","padding":0}},{"computed":[["Outer inline-size","368px"],["Clipping","فعال"],["Sizing cause","بدون تغییر"]],"elementor":[["Width","Full / 100%"],["Margin inline","24px + 24px"],["Overflow والد","Hidden"]],"evidence":"verified_by_css_spec","explanation":"این مرحله عمداً نشان می‌دهد که حذف نشانه با اصلاح ساختار تفاوت دارد.","golden_rule":"Overflow Hidden آخرین راه بررسی نیست؛ ابتدا عنصر overflowکننده را پیدا کن.","id":"clipped-symptom","phase":"خرابی عمدی","prediction":{"correct":1,"feedback_correct":"درست است؛ padding فضای داخل Shell را می‌سازد.","feedback_wrong":"هدف فاصلهٔ داخلی است؛ property باید همان رابطه را بیان کند.","options":["margin روی Main تمام‌عرض","padding-inline روی Shell","z-index روی Main"],"prompt":"برای ساخت فاصلهٔ داخلی Shell تمام‌عرض، کدام انتخاب مستقیم‌تر است؟"},"summary":"اسکرول یا بیرون‌زدگی دیده نمی‌شود، ولی outer size نامناسب همچنان وجود دارد.","title":"پنهان‌کردن علامت با Overflow Hidden","visual":{"margin":24,"mode":"clipped","padding":0}},{"computed":[["Used width","بر اساس context بازحساب می‌شود"],["Shrink-to-fit","همیشه قابل ادعا نیست"],["Matched rule","برای قطعیت لازم است"]],"elementor":[["Width","Auto"],["Margin inline","24px + 24px"],["Parent context","باید بررسی شود"]],"evidence":"verified_by_real_fixture","explanation":"Auto در همهٔ layoutها برابر shrink-to-fit نیست. اینجا به‌عنوان workaround واقعی ثبت شده، نه نسخهٔ همیشگی.","golden_rule":"از یک رفع مشکل واقعی، قانون عمومی نساز؛ context و matched rule را ثبت کن.","id":"auto-observed-workaround","phase":"مرزبندی شواهد","prediction":{"correct":1,"feedback_correct":"درست است؛ منبع قانون در Styles/Computed تعیین‌کننده است.","feedback_wrong":"بدون selector و فایل منبع، نسبت‌دادن رفتار به Theme یا Elementor قطعی نیست.","options":["فقط پنل Elementor","Matched CSS rule در DevTools","رنگ Background"],"prompt":"برای اثبات اینکه Theme یا Elementor width را تعیین کرده، کجا باید نگاه کنی؟"},"summary":"در مسئلهٔ واقعی رضا، انتخاب صریح Auto رفتار sizing را تغییر داد؛ نتیجه به layout context وابسته است.","title":"Width Auto — workaround مشاهده‌شده، نه قانون جهانی","visual":{"margin":24,"mode":"auto","padding":0}},{"computed":[["Shell content width","272px — مدل آموزشی"],["Main outer width","272px"],["Overflow","0"]],"elementor":[["Shell > Padding inline","24px"],["Main > Width","Full / 100%"],["Main > Margin inline","0"]],"evidence":"verified_by_official_elementor_help","explanation":"این الگو رابطهٔ Page Padding و Main Content را روشن‌تر می‌کند و برای پروژهٔ TUYA قابل آزمایش است.","golden_rule":"Shell فاصلهٔ صفحه را می‌سازد؛ Main داخل فضای باقی‌مانده چیدمان می‌شود.","id":"shell-padding","phase":"انتقال به TUYA","prediction":{"correct":1,"feedback_correct":"دقیقاً؛ مسئولیت spacing در Shell باقی می‌ماند.","feedback_wrong":"به نقش معماری لایه‌ها نگاه کن: Shell فاصلهٔ صفحه را کنترل می‌کند.","options":["Margin فرزند","Padding والد","Z-index"],"prompt":"در این الگو، اگر عرض viewport کم شود، کدام بخش مسئول فاصلهٔ کناری است؟"},"summary":"Shell فاصلهٔ صفحه را کنترل می‌کند و Main بدون افزودن outer margin داخل آن قرار می‌گیرد.","title":"الگوی پایدار: Padding والد + Child با Width مناسب","visual":{"margin":0,"mode":"padding","padding":24}}],"storage_key":"elementor-v4-workbook:v27:stv2:width-margin-overflow","title":"Width، Margin و Overflow — از نشانه تا علت","type":"cause_effect_debug","verification":[{"source_id":"ELEMENTOR_CONTAINER_SIZE","status":"verified_by_official_elementor_help"},{"source_id":"CSS2_USED_WIDTH","status":"verified_by_css_spec"},{"source_id":"REZA_MARGIN_OBSERVATION","status":"verified_by_real_fixture"}]}</script>
</section>
</details><details class="lesson-disclosure responsive-build-test" id="lesson-4-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Width، Margin و Shell در صفحهٔ باریک</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> ببین چرا Full Width همراه margin افقی می‌تواند overflow بسازد و padding والد چه تفاوتی دارد.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>یک Shell تمام‌عرض و یک Main child داخل آن بساز.</li><li>حالت A: روی Main عرض کامل و margin دوطرفه بده.</li><li>حالت B: margin را حذف و همان فاصله را با padding-inline روی Shell بساز.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>قبل از تست بگو در کدام حالت outer box ممکن است از عرض والد بیشتر شود.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>در Mobile ارتفاع ثابت 40vh را نگه دار و متن را طولانی کن تا clipping یا فضای نامناسب را ببینی.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>Computed Width، Box Model، margin-inline، padding-inline، scrollWidth و overflow ancestorها.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> هیچ اسکرول افقی ناخواسته وجود ندارد و ارتفاع Mobile محتوا را قطع نمی‌کند.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-4-responsive-build-test-done-build"><input data-persist="" id="lesson-4-responsive-build-test-done-build" name="lesson-4-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-4-responsive-build-test-done-test"><input data-persist="" id="lesson-4-responsive-build-test-done-test" name="lesson-4-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-4-responsive-build-test-done-debug"><input data-persist="" id="lesson-4-responsive-build-test-done-debug" name="lesson-4-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-4-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-4-responsive-build-test-note" name="lesson-4-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/set-flexbox-container-size-behavior/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
<p class="stv2-back-link"><a href="#stv2-width-margin-overflow">↩ مفهوم را با Step‑Through v2 مرور کن</a></p></section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-4-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Width، padding و max-width</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
