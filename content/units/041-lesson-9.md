<article class="lesson card-surface" data-lesson="9" id="lesson-9"><h2 class="lesson-title former-h1">درس 9 — Grid و زمان درست استفاده از آن</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-9-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-9-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> تفاوت مسئلهٔ یک‌محوری و دوبعدی را تشخیص بدهی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام Propertyهای CSS Grid را.</p><p><strong>در پایان باید بتوانی:</strong> بین Flexbox و Grid براساس ساختار تصمیم بگیری.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-9-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-9-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + ⚖ مقایسه‌ای + 🛠 اجرایی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۵–۳۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> انتخاب Flex یا Grid نیازمند انتقال تصمیم است.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-9-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-9-lesson-understand-4">A. بفهم</h2><h3>مسئله</h3><p>گاهی Itemها فقط در یک ردیف یا ستون حرکت می‌کنند؛ گاهی باید ردیف و ستون با هم هماهنگ باشند.</p><h3>Decision Tree</h3><section aria-labelledby="section-hidden-139-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-139-heading">بخش آموزشی</h2><ul><li>◇ فقط ترتیب روی یک محور مهم است؟</li>
<li>├─ بله → □ Flexbox</li>
<li>└─ خیر</li>
<li>◇ ستون‌ها و ردیف‌ها باید Track مشترک داشته باشند؟</li>
<li>├─ بله → □ Grid</li>
<li>└─ خیر → ساختار را دوباره بررسی کن</li></ul></section><h3>مدل دیداری</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text" dir="ltr">Flex:
[A] [B] [C] [D]

Grid:
[A] [B]
[C] [D]
</code></pre><p>Grid برای «چند Item شبیه Card با ستون‌های منظم» اغلب طبیعی‌تر است.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="6987bda4a89af93cba64466f73d8e464e5cb104e56a7664a9534e37a48a23f8a" id="lesson-9-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Grid؛ Track، Line، Cell و Area</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="9" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-09-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-09-section-01">مسئله‌ای که Grid حل می‌کند</h3><p>گاهی فقط کنار هم گذاشتن عناصر کافی نیست. می‌خواهی:</p><ul>
<li>ستون‌های چند ردیف دقیقاً هم‌راستا باشند؛</li>
<li>یک کارت دو ستون را اشغال کند؛</li>
<li>ارتفاع ردیف‌ها و عرض ستون‌ها یک قرارداد مشترک داشته باشند؛</li>
<li>جای Itemها نسبت به کل شبکه معنا داشته باشد.</li>
</ul><p>Flexbox صف را خوب مدیریت می‌کند؛ Grid برای نقشهٔ دوبعدی ساخته شده است.</p><hr/></section><section aria-labelledby="concept-v31-09-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-09-section-02">تشبیه به دنیای واقعی: هتل با راهرو و اتاق</h3><p>یک هتل را تصور کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">خط 1      خط 2      خط 3      خط 4
  │          │          │          │
──┼──────────┼──────────┼──────────┼── خط افقی 1
  │ اتاق A   │ اتاق B   │ اتاق C   │
──┼──────────┼──────────┼──────────┼── خط افقی 2
  │ اتاق D   │ اتاق E   │ اتاق F   │
──┼──────────┼──────────┼──────────┼── خط افقی 3
</code></pre></figure><p>در این تصویر:</p><ul>
<li>فاصلهٔ میان دو خط = <strong>Track</strong></li>
<li>محل تقاطع یک ردیف و ستون = <strong>Cell</strong></li>
<li>چند Cell کنار هم = <strong>Area</strong></li>
<li>دیوارهای شماره‌دار = <strong>Grid Line</strong></li>
</ul><p>Item می‌تواند در یک اتاق بماند یا چند اتاق را به هم وصل کند.</p><hr/></section><section aria-labelledby="concept-v31-09-section-03" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-09-section-03">چرا Grid ساخته شد؟</h3><p>با Flexهای تو‌در‌تو هم می‌توان بسیاری از شبکه‌ها را ساخت، اما ساختار به‌سرعت پیچیده می‌شود:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Row
├── Column
│   ├── Row
│   └── Row
└── Column
    ├── Row
    └── Row
</code></pre></figure><p>Grid اجازه می‌دهد Parent مستقیماً نقشهٔ ردیف و ستون را تعریف کند. Childها روی همان نقشه قرار می‌گیرند.</p><hr/></section><section aria-labelledby="concept-v31-09-section-04" class="concept-reference-part concept-reference-definition"><h3 id="concept-v31-09-section-04">واژگان اصلی</h3><h4>Grid Container</h4><p>Parentی که <code class="inline-code" dir="ltr">display: grid</code> دارد.</p><h4>Grid Item</h4><p>Child مستقیم Grid Container.</p><h4>Track</h4><p>فضای میان دو Grid Line؛ می‌تواند ستون یا ردیف باشد.</p><h4>Cell</h4><p>کوچک‌ترین خانهٔ حاصل از تقاطع یک ردیف و ستون.</p><h4>Area</h4><p>یک مستطیل متشکل از یک یا چند Cell.</p><h4>Gap</h4><p>فاصلهٔ میان Trackها، نه Padding داخل Itemها.</p><hr/></section><section aria-labelledby="concept-v31-09-section-05" class="concept-reference-part"><h3 id="concept-v31-09-section-05"><code class="inline-code" dir="ltr">fr</code> چیست؟</h3><p><code class="inline-code" dir="ltr">fr</code> سهمی از فضای باقی‌ماندهٔ Grid است.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">grid-template-columns: 1fr 1fr 1fr;
</code></pre></figure><p>سه ستون سهم مساوی از فضای توزیع‌پذیر می‌گیرند.</p><p>اما <code class="inline-code" dir="ltr">1fr</code> به معنی «هر شرایطی دقیقاً یک‌سوم» نیست. Min Content، Gap، Track ثابت و محدودیت Childها می‌توانند اندازهٔ واقعی را تغییر دهند.</p><p>برای اینکه Track بتواند واقعاً کوچک شود، گاهی این الگو لازم است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
</code></pre></figure><p>صفر در اینجا اجازه می‌دهد حداقل Track از Min Content پایین‌تر بیاید؛ البته محتوا همچنان ممکن است نیاز به Wrap یا Overflow Control داشته باشد.</p><hr/></section><section aria-labelledby="concept-v31-09-section-06" class="concept-reference-part"><h3 id="concept-v31-09-section-06"><code class="inline-code" dir="ltr">minmax()</code>؛ اتاقی با حداقل و حداکثر</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">grid-template-columns: repeat(3, minmax(220px, 1fr));
</code></pre></figure><p>یعنی هر ستون:</p><ul>
<li>از ۲۲۰px کوچک‌تر نشود؛</li>
<li>در صورت وجود فضای بیشتر، تا سهمی از فضای آزاد رشد کند.</li>
</ul><p>عدد ۲۲۰ یا ۲۸۰ قانون جهانی نیست. حداقل باید از محتوای واقعی کارت استخراج شود:</p><ul>
<li>طول عنوان فارسی</li>
<li>اندازهٔ دکمه</li>
<li>قیمت</li>
<li>Padding</li>
<li>تصویر</li>
<li>حداقل خوانایی</li>
</ul><hr/></section><section aria-labelledby="concept-v31-09-section-07" class="concept-reference-part"><h3 id="concept-v31-09-section-07"><code class="inline-code" dir="ltr">auto-fill</code> و <code class="inline-code" dir="ltr">auto-fit</code>؛ اتاق‌های خالی هتل</h3><p>فرض کن هتل می‌تواند چهار اتاق در یک ردیف بسازد، اما فقط دو مهمان دارد.</p><h4><code class="inline-code" dir="ltr">auto-fill</code></h4><p>اتاق‌های ممکن را حفظ می‌کند؛ حتی اگر بعضی خالی باشند.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[مهمان][مهمان][خالی][خالی]
</code></pre></figure><h4><code class="inline-code" dir="ltr">auto-fit</code></h4><p>Trackهای خالی را جمع می‌کند و فضای آن‌ها را به Trackهای موجود می‌دهد.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[     مهمان     ][     مهمان     ]
</code></pre></figure><p>الگوی رایج:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
</code></pre></figure><p>اما «همیشه auto-fit» قانون درستی نیست. اگر حفظ جای ستون‌های خالی برای Alignment یا ریتم شبکه مهم باشد، <code class="inline-code" dir="ltr">auto-fill</code> می‌تواند انتخاب مناسب‌تری باشد.</p><hr/></section><section aria-labelledby="concept-v31-09-section-08" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-09-section-08">رفتار در سه عرض</h3><p>فرض کن حداقل کارت ۲۸۰px و Gap برابر ۲۴px است.</p><h4>عرض ۱۲۰۰px</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[ کارت ][ کارت ][ کارت ][ کارت ]
</code></pre></figure><h4>عرض ۷۶۰px</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[      کارت      ][      کارت      ]
[      کارت      ][      کارت      ]
</code></pre></figure><h4>عرض ۳۶۰px</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[          کارت          ]
[          کارت          ]
[          کارت          ]
</code></pre></figure><p>Grid در این الگو بدون Breakpoint صریح، تعداد Trackهای قابل جاگیری را تغییر می‌دهد. بااین‌حال هنوز باید عرض‌های میانی و محتوای بلند را آزمایش کنی.</p><hr/></section><section aria-labelledby="concept-v31-09-section-09" class="concept-reference-part"><h3 id="concept-v31-09-section-09">Flex Item داخل Grid و Grid Item داخل Flex</h3><p>یک Element می‌تواند هم‌زمان دو نقش داشته باشد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">نسبت به Parent خودش: Grid Item
نسبت به Childهای خودش: Flex Container
</code></pre></figure><p>مثلاً کارت محصول در شبکه:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Product Grid  ← Grid Container
└── Product Card  ← Grid Item + Flex Container
    ├── Image
    ├── Content
    └── Button
</code></pre></figure><p>نقش بیرونی می‌گوید کارت در شبکه کجا و با چه اندازه‌ای قرار گیرد. موتور داخلی می‌گوید محتویات کارت چگونه چیده شوند. این دو را با هم قاطی نکن.</p><hr/></section><section aria-labelledby="concept-v31-09-section-10" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-09-section-10">در Elementor V4</h3><p>Grid Container را زمانی انتخاب کن که Trackهای مشترک واقعاً ارزش دارند. در پنل Layout:</p><ul>
<li>تعداد یا تعریف ستون‌ها</li>
<li>ردیف‌ها</li>
<li>Gap</li>
<li>Alignment</li>
<li>Placement و Span Itemها</li>
</ul><p>را کنترل کن.</p><p>برای یک شبکهٔ کارت، ابتدا Auto Placement را امتحان کن. جای‌گذاری دستی همه Itemها معمولاً سیستم را شکننده می‌کند. Placement دستی را برای Hero Card، Featured Item یا ترکیب خاص نگه دار.</p><p>اگر رابط امکان واردکردن تعریف سفارشی Track را می‌دهد، خروجی را در DevTools بررسی کن. نام کنترل رابط و CSS نهایی همیشه نباید یکسان فرض شود.</p><hr/></section><section aria-labelledby="concept-v31-09-section-11" class="concept-reference-part"><h3 id="concept-v31-09-section-11">Grid یا Flex Wrap؟</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">فقط جریان و شکستن خط مهم است؟ → Flex Wrap
تراز ستون‌ها در چند ردیف مهم است؟ → Grid
Item باید Span کند؟ → Grid
ترتیب خطی محتوا مهم‌ترین چیز است؟ → Flex را ابتدا بررسی کن
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-09-section-12" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-09-section-12">اشتباهات رایج</h3><ul>
<li>استفاده از Grid برای یک ردیف ساده</li>
<li>فرض اینکه <code class="inline-code" dir="ltr">1fr</code> هر محتوایی را مجبور به کوچک‌شدن می‌کند</li>
<li>Placement دستی تمام Itemها</li>
<li>ساخت Track با حداقل ثابت بدون آزمایش متن فارسی</li>
<li>تغییر ترتیب بصری برخلاف ترتیب DOM</li>
<li>گذاشتن Height ثابت روی ردیف‌هایی با محتوای پویا</li>
</ul><hr/></section><section aria-labelledby="concept-v31-09-section-13" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-09-section-13">پل به DevTools</h3><p>در Elements Panel روی Badge مربوط به <code class="inline-code" dir="ltr">grid</code> کلیک کن. Overlay می‌تواند:</p><ul>
<li>شماره Lineها</li>
<li>Trackها</li>
<li>Gapها</li>
<li>Areaها</li>
</ul><p>را نشان دهد. این بهترین راه برای دیدن تفاوت Line و Cell است.</p><hr/></section><section aria-labelledby="concept-v31-09-section-14" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-09-section-14">تصویر ذهنی نهایی</h3><p>Flex مثل صف مسافران است؛ Grid مثل نقشهٔ اتاق‌های هتل. در صف، ترتیب حرکت مهم است. در هتل، جای اتاق نسبت به ردیف و ستون معنا دارد.</p><hr/></section><section aria-labelledby="concept-v31-09-section-15" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-09-section-15">قوانین طلایی</h3><ul>
<li><strong>«Grid را با Track طراحی کن، نه با هل‌دادن تک‌تک Itemها.»</strong></li>
<li><strong>«<code class="inline-code" dir="ltr">fr</code> سهم فضای باقی‌مانده است، نه تضمین اندازهٔ مطلق.»</strong></li>
<li><strong>«حداقل <code class="inline-code" dir="ltr">minmax()</code> را از نیاز محتوا استخراج کن، نه از عدد جادویی.»</strong></li>
<li><strong>«Auto-fit Track خالی را جمع می‌کند؛ Auto-fill آن را نگه می‌دارد.»</strong></li>
<li><strong>«نقش Item در Parent و موتور Layout داخلی آن دو تصمیم جدا هستند.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>CSS Grid Layout Module Level 1/2</li>
<li>Elementor Help: Grid Container layout options</li>
<li>Chrome DevTools: Grid overlays and badges</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-9-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-9-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Grid؛ Trackها با fr، طول، درصد و تابع ساخته می‌شوند</span></summary>
<section aria-labelledby="lesson-9-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Grid علاوه بر Gap، خود Trackها را اندازه‌گیری می‌کند. `fr` سهمی از فضای آزاد Grid است، نه درصد ثابت Parent.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> یک زمین را به سهم تقسیم می‌کنی: 1fr و 2fr یعنی از فضای باقی‌مانده یک سهم و دو سهم، نه الزاماً 33% و 66% کل صفحه.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Columns / Rows</th><td><code dir="ltr">grid-template-*</code></td><td>در CSS: fr، px، %، auto، minmax()</td><td>Grid container/free space</td><td>برای Trackهای واقعی دوبعدی.</td><td>وجود fr در CSS به‌معنای عرضهٔ آن در همهٔ کنترل‌های Elementor نیست.</td><td><code dir="ltr">CSS_GRID</code></td></tr><tr><th scope="row">Gap</th><td><code dir="ltr">row-gap / column-gap</code></td><td>واحدهای موجود در کنترل Grid</td><td>Grid container</td><td>فاصلهٔ بین Trackها.</td><td>Gap بخشی از فضای مصرفی است.</td><td><code dir="ltr">E_GRID</code></td></tr><tr><th scope="row">Span</th><td><code dir="ltr">grid-column / row</code></td><td>integer / line names</td><td>بدون واحد طول</td><td>گسترش روی Cellها.</td><td>عدد Span اندازهٔ پیکسل نیست.</td><td><code dir="ltr">CSS_GRID</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>فضای آزاد Trackها=900px و الگو 1fr 2fr: مجموع سهم=3؛ Trackها 300px و 600px می‌شوند.</p></section>
<section><h3>📱 در Responsive</h3><p>تعداد Track، اندازهٔ Track و Gap ممکن است در breakpointها عوض شوند؛ auto-fit/minmax در Custom CSS یک ابزار CSS است، نه ادعای کنترل ثابت UI.</p></section>
<section><h3>🔬 در DevTools</h3><p>Grid overlay، computed grid-template-columns و gap را بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/grid-container-layout-options/" rel="noopener noreferrer" target="_blank">Elementor — Grid container layout options</a>، <a href="https://www.w3.org/TR/css-grid-2/" rel="noopener noreferrer" target="_blank">W3C — CSS Grid Layout</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-9-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-9-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — تصمیم آگاهانه</h3><p>Layout اصلی TUYA را به Grid تبدیل نکن. فقط تحلیل کن:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Copy | Visual</pre></figure></details><p>این ساختار هنوز یک‌محوری است و تغییر Row به Column در Mobile مهم است؛ Flexbox انتخاب مناسب باقی می‌ماند.</p><p>تمرین مستقل: یک بخش چهار Card آزمایشی بساز و آن را با Grid دو ستونه نمایش بده.</p><h3>❓ سؤال توقف</h3><p>برای چهار Card که باید ستون‌های هم‌عرض و ردیف‌های منظم داشته باشند، Flexbox یا Grid؟</p><details class="disclosure-card"><summary>پاسخ پیشنهادی</summary>Grid.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> هر Layout چندستونه را Grid بدانی.</p><p><strong>قاعده:</strong> تعداد ستون به‌تنهایی معیار نیست؛ نوع رابطهٔ آیتم‌ها مهم است.</p><h3>🧪 عمداً خرابش کن</h3><p>Card Grid را با یک Flexbox بدون Wrap بساز و متن یکی از Cardها را بسیار طولانی کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>Trackها هماهنگی کمتری دارند؛</li>
<li>توزیع Width ممکن است تابع Content شود؛</li>
<li>کنترل ردیف و ستون سخت‌تر می‌شود.</li>
</ul><p>سپس همان ساختار را با Grid مقایسه کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-141-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-141-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-49"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-49-1" name="chk-49-1" type="checkbox"/><span>TUYA Main همچنان Flexbox است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-49-2" name="chk-49-2" type="checkbox"/><span>یک Grid آزمایشی ساخته‌ام</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-49-3" name="chk-49-3" type="checkbox"/><span>دلیل انتخاب هرکدام را می‌توانم توضیح بدهم</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> تفاوت اصلی Flexbox و Grid چیست؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> برای Gallery شش‌تایی، Navigation و Hero دو ستونه ابزار مناسب هرکدام را انتخاب کن.</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-50"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-50-1" name="chk-50-1" type="checkbox"/><span>یک‌بعدی یا دوبعدی‌بودن مسئله را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-50-2" name="chk-50-2" type="checkbox"/><span>انتخاب Flex یا Grid به نیاز Layout متصل است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-50-3" name="chk-50-3" type="checkbox"/><span>برای مثال تازه نیز دلیل انتخاب را بیان کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-9-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-9-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-HOME2-GRID-001</h3><p><strong>هدف:</strong> ⚖️ دو روش را مقایسه کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">legacy_or_hybrid</code></p><p>Hero صفحهٔ Home2 در Export یک Legacy Grid Container با دو ستون دارد و داخل همان Subtree Elementهای V4 نیز دیده می‌شوند.</p><p>پرسش‌ها:</p><ul>
<li>آیا Grid واقعاً برای Trackهای Hero لازم است؟</li>
<li>آیا V4 Grid معادل تمیزتری می‌دهد؟</li>
<li>آیا Flexbox با دو Child کافی است؟</li>
</ul><p>بدون Runtime پاسخ قطعی نداریم.</p><h3>🔬 پشت صحنه</h3><p>Grid ردیف و ستون را به‌عنوان Track مدیریت می‌کند. لازم نیست Syntax آن را حفظ کنی؛ در V4 کنترل‌های Track را بفهم.</p><hr/></details><details class="lesson-section more-know lesson-disclosure"><summary class="lesson-disclosure-summary">بیشتر بدانید</summary><p>Grid Container برای دو محور هم‌زمان مناسب است: ستون و ردیف. اگر فقط یک ردیف یا یک ستون را کنترل می‌کنی، Flexbox معمولاً ساده‌تر است.</p></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-9-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-9-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-52"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-52-1" name="chk-52-1" type="checkbox"/><span>می‌توانی Flexbox یک‌بعدی را از Grid دوبعدی جدا کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-52-2" name="chk-52-2" type="checkbox"/><span>می‌توانی توضیح بدهی چرا «ظاهر چندستونه» به‌تنهایی دلیل انتخاب Grid نیست.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-53"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-53-1" name="chk-53-1" type="checkbox"/><span>یک نمونهٔ Card Grid را با Row و Column کنترل می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-53-2" name="chk-53-2" type="checkbox"/><span>Main Layout TUYA را با Grid بازسازی آزمایشی می‌کنی و تفاوت را با Flex ثبت می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-54"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-54-1" name="chk-54-1" type="checkbox"/><span>برای Gallery، Header و Pricing Cards می‌توانی ابزار مناسب را جداگانه انتخاب کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-9-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-9-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>ایستگاه B تمام شد. Main Layout، اندازه‌ها، Wrap و تفاوت Grid/Flex را یک‌بار بدون راهنما بازسازی کن.</p><hr/><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 9</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-9-completion"><fieldset><legend>ثبت پایان درس 9</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-9-complete" name="lesson-9-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-9-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Flexbox در برابر Grid</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Flexbox</h3><p>Flexbox مثل صف منعطف است: برای یک محور اصلی عالی است؛ مثلاً ردیف کارت‌ها، نوار لوگو، دکمه‌ها یا دو ستون ساده.</p></section>
<section class="inline-compare-card"><h3>Grid</h3><p>Grid مثل صفحهٔ شطرنج است: وقتی هم ردیف و هم ستون هم‌زمان مهم‌اند، انتخاب طبیعی‌تری است.</p><p class="golden-rule">قانون طلایی: یک‌بعدی؟ Flexbox. دوبعدی؟ Grid. فقط برای شیک‌بودن Grid نساز.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="lesson-9-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Flex یا Grid برای لوگوها و Nodeها؟</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>برای Logo Strip با ستون‌های منظم، Grid می‌تواند کنترل بهتری بدهد؛ برای ردیفی که فقط باید wrap شود، Flex ساده‌تر است. Nodeهای شعاعی TUYA Grid محتوایی نیستند؛ آن‌ها داخل Visual Stage رابطهٔ مکانی دارند.</p>
<p>انتخاب را بر اساس رابطهٔ عناصر انجام بده، نه صرفاً شباهت ظاهری Screenshot.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-9-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Flex یا Grid برای ردیف لوگوها</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> دو موتور layout را روی یک محتوای واقعی مقایسه کن و انتخاب را با نیاز توجیه کن.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>یک نسخه با Flex + Wrap و یک نسخه با Grid بساز.</li><li>در Grid تعداد ستون‌ها را برای breakpointهای لازم تغییر بده.</li><li>در Flex رفتار wrap و توزیع فضای آزاد را مشاهده کن.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن کدام مدل در حفظ ستون‌های هم‌اندازه و کدام در جریان آزاد ردیفی ساده‌تر است.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>برای Grid تعداد ستون ثابت زیاد نگه دار و عرض را کم کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>Computed display، grid-template-columns، flex-wrap و اندازهٔ track/itemها.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> انتخاب موتور layout بر اساس ساختار محتواست، نه عادت یا ظاهر موقت.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-9-responsive-build-test-done-build"><input data-persist="" id="lesson-9-responsive-build-test-done-build" name="lesson-9-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-9-responsive-build-test-done-test"><input data-persist="" id="lesson-9-responsive-build-test-done-test" name="lesson-9-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-9-responsive-build-test-done-debug"><input data-persist="" id="lesson-9-responsive-build-test-done-debug" name="lesson-9-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-9-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-9-responsive-build-test-note" name="lesson-9-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/responsive-design-using-containers/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-9-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Grid tracks و gap</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
