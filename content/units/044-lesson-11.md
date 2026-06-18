<article class="lesson card-surface" data-lesson="11" id="lesson-11"><h2 class="lesson-title former-h1">درس 11 — Image، SVG، Background، Aspect Ratio و Object Fit</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-11-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-11-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> برای هر رسانه Element و رفتار نمایشی مناسب انتخاب کنی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> بهینه‌سازی پیشرفته فرمت‌های تصویر را.</p><p><strong>در پایان باید بتوانی:</strong> Logoها را سالم نمایش بدهی و Visual Stage را مربع نگه داری.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-11-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-11-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + ♿ دسترسی‌پذیری</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۰–۳۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۴۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۵ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> رسانه، Fit و معنی محتوا هم‌زمان بررسی می‌شوند.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-11-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-11-lesson-understand-4">A. بفهم</h2><h3>Decision Tree رسانه</h3><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="rtl">◇ تصویر معنی محتوایی دارد؟
   ├─ بله → □ Image + Alt
   └─ خیر
       ◇ تزئین Background است؟
          ├─ بله → □ Background
          └─ خیر → □ SVG/Icon مناسب</pre></figure></details><h3>Cover و Contain</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای Cover، Contain و Aspect Ratio">
<h4>راهنمای مبتدی برای Cover، Contain و Aspect Ratio</h4>
<p>تصویر را مثل عکس داخل قاب ببین: یا کل قاب را پر می‌کند، یا کامل دیده می‌شود، یا نسبتش باید حفظ شود.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="Cover">
<h4><span class="term-en" dir="ltr">Cover</span> — پر کردن قاب</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> تصویر قاب را پر می‌کند، حتی اگر بخشی از تصویر بریده شود.</li>
<li><strong>۲. مثال روزمره:</strong> مثل عکس پس‌زمینهٔ جلد مجله.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Hero Image یا Background که باید قاب را کامل پر کند.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Object Fit: Cover یا Background Size: Cover.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> برای لوگو از Cover استفاده می‌کنم و لوگو بریده می‌شود.</li>
<li><strong>۶. تصمیم درست:</strong> Cover برای عکس تزئینی یا Hero مناسب‌تر است، نه لوگو.</li>
<li><strong>۷. تمرین کوچک:</strong> یک لوگو را در قاب کوچک تصور کن؛ آیا بریدن آن قابل قبول است؟</li>
</ol>
</article>
<article class="concept-card" data-concept="Contain">
<h4><span class="term-en" dir="ltr">Contain</span> — کامل دیده شدن</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> کل تصویر داخل قاب دیده می‌شود، حتی اگر اطرافش فضای خالی بماند.</li>
<li><strong>۲. مثال روزمره:</strong> مثل قرار دادن یک پوستر کامل داخل قاب.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> لوگوها و آیکن‌هایی که نباید بریده شوند.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Object Fit: Contain یا تنظیم اندازهٔ تصویر.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> می‌خواهم قاب حتماً پر شود و لوگو را قربانی می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> برای Logo معمولاً Contain امن‌تر است.</li>
<li><strong>۷. تمرین کوچک:</strong> یک لوگو را پیدا کن و تصمیم بگیر: Cover یا Contain؟</li>
</ol>
</article>
<article class="concept-card" data-concept="Aspect Ratio">
<h4><span class="term-en" dir="ltr">Aspect Ratio</span> — نسبت عرض به ارتفاع</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> نسبت ثابت شکل تصویر یا قاب است.</li>
<li><strong>۲. مثال روزمره:</strong> مثل قاب ۴×۳ یا ۱۶×۹ تلویزیون.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> کارت‌ها یا Logo frameهایی که باید اندازهٔ قابل پیش‌بینی داشته باشند.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Aspect Ratio در ظرف والد/Image یا CSS.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> فقط عرض را تنظیم می‌کنم و ارتفاع تصادفی می‌شود.</li>
<li><strong>۶. تصمیم درست:</strong> قاب‌های تکراری را با نسبت مشخص نگه دار.</li>
<li><strong>۷. تمرین کوچک:</strong> برای یک Logo frame نسبت تقریبی را حدس بزن و یادداشت کن.</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">Cover</dt><dd>پرکردن قاب با احتمال بریدگی</dd>
<dt dir="ltr">Contain</dt><dd>نمایش کامل تصویر با احتمال فضای خالی</dd>
<dt dir="ltr">Aspect Ratio</dt><dd>نسبت عرض و ارتفاع</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">قبل از انتخاب Cover/Contain بپرس: «بریدن تصویر اشکال دارد یا نه؟»</p>
</aside>
</section><section aria-labelledby="section-hidden-165-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-165-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Cover</dt><dd>قاب را پر می‌کند؛ ممکن است Crop کند</dd><dt>Contain</dt><dd>کل تصویر را نشان می‌دهد؛ ممکن است فضای خالی بماند</dd></dl></section><p>Logo معمولاً Contain؛ عکس Card معمولاً Cover.</p><h3>Aspect Ratio</h3><p>Ratio باعث می‌شود Box با تغییر Width شکل خود را حفظ کند.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="9a715a1499c633723de9be7e700d0d8340eb3c485f2210ad153690d6294dbaf8" id="lesson-11-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Image، SVG، Background و Aspect Ratio</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="11" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-11-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-11-section-01">مسئله‌ای که این مفهوم حل می‌کند</h3><p>همهٔ چیزهایی که شبیه تصویر دیده می‌شوند نقش یکسان ندارند.</p><ul>
<li>تصویر محصول بخشی از محتواست.</li>
<li>بافت طلایی پشت Hero تزئینی است.</li>
<li>لوگو ممکن است SVG باشد.</li>
<li>عکس کارت باید Crop شود.</li>
<li>Hero Image ممکن است عنصر LCP باشد.</li>
</ul><p>انتخاب اشتباه میان Image و Background روی Accessibility، Responsive، Performance و نگهداری اثر می‌گذارد.</p><hr/></section><section aria-labelledby="concept-v31-11-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-11-section-02">تشبیه به دنیای واقعی: عکس قاب‌شده و کاغذدیواری</h3><p>یک اتاق را تصور کن:</p><ul>
<li>عکس خانوادگی داخل قاب، معنای مستقل دارد؛ اگر حذف شود بخشی از محتوا از بین می‌رود. این <strong>Image Element</strong> است.</li>
<li>طرح روی دیوار فقط فضا را زیباتر می‌کند؛ اگر حذف شود پیام اصلی هنوز باقی است. این <strong>Background</strong> است.</li>
<li>نقشهٔ معماری که با خطوط رسم شده و در هر اندازه واضح است، شبیه <strong>SVG</strong> است.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-11-section-03" class="concept-reference-part"><h3 id="concept-v31-11-section-03">Image یا Background؟</h3><p>از خودت بپرس:</p><blockquote>
<p>اگر تصویر Load نشود، آیا کاربر بخشی از اطلاعات را از دست می‌دهد؟</p>
</blockquote><p>اگر بله، معمولاً Image Element و متن جایگزین مناسب لازم است.</p><p>اگر تصویر صرفاً تزئینی است، Background می‌تواند درست‌تر باشد.</p><p>این قانون مطلق نیست، اما نقطهٔ شروع قابل دفاعی است.</p><hr/></section><section aria-labelledby="concept-v31-11-section-04" class="concept-reference-part"><h3 id="concept-v31-11-section-04">Aspect Ratio؛ شکل قاب پیش از رسیدن عکس</h3><p>مرورگر باید بداند جعبهٔ تصویر چه شکلی است. اگر تا Load شدن فایل هیچ فضایی رزرو نشود، محتوا بعداً جابه‌جا می‌شود.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.media {
  aspect-ratio: 4 / 3;
}
</code></pre></figure><p>این یعنی حتی پیش از Load کامل تصویر، Box نسبت ۴ به ۳ دارد.</p><p>برای <code class="inline-code" dir="ltr">&lt;img&gt;</code>، تعیین <code class="inline-code" dir="ltr">width</code> و <code class="inline-code" dir="ltr">height</code> واقعی نیز به مرورگر کمک می‌کند نسبت را از ابتدا محاسبه کند.</p><hr/></section><section aria-labelledby="concept-v31-11-section-05" class="concept-reference-part"><h3 id="concept-v31-11-section-05"><code class="inline-code" dir="ltr">object-fit</code>؛ عکس چگونه داخل قاب بنشیند؟</h3><h4><code class="inline-code" dir="ltr">cover</code></h4><p>قاب کاملاً پر می‌شود؛ بخشی از تصویر ممکن است Crop شود.</p><h4><code class="inline-code" dir="ltr">contain</code></h4><p>تمام تصویر دیده می‌شود؛ ممکن است اطراف آن فضای خالی بماند.</p><h4><code class="inline-code" dir="ltr">object-position</code></h4><p>نقطهٔ کانونی Crop را تعیین می‌کند.</p><p>مثلاً اگر چهره در سمت راست عکس است، <code class="inline-code" dir="ltr">center center</code> شاید صورت را ببرد. باید موقعیت را متناسب با سوژه تنظیم کنی.</p><hr/></section><section aria-labelledby="concept-v31-11-section-06" class="concept-reference-part"><h3 id="concept-v31-11-section-06">SVG چیست؟</h3><p>SVG به‌جای شبکه‌ای از Pixelها، شکل را با مسیرها و بردارها توصیف می‌کند. برای آیکون، لوگو و Illustration خطی مناسب است.</p><p>اما «SVG همیشه سبک است» درست نیست. یک SVG پیچیده می‌تواند:</p><ul>
<li>هزاران Path داشته باشد؛</li>
<li>Filter سنگین اجرا کند؛</li>
<li>کد یا Metadata اضافی داشته باشد؛</li>
<li>از نظر امنیت نیازمند Sanitization باشد.</li>
</ul><p><code class="inline-code" dir="ltr">viewBox</code> باید درست باشد تا مقیاس‌پذیری قابل پیش‌بینی بماند.</p><hr/></section><section aria-labelledby="concept-v31-11-section-07" class="concept-reference-part"><h3 id="concept-v31-11-section-07">Responsive Images</h3><p>یک تصویر ۲۵۰۰px برای کارت ۳۲۰px اتلاف پهنای باند است. مرورگر با <code class="inline-code" dir="ltr">srcset</code> و <code class="inline-code" dir="ltr">sizes</code> می‌تواند نسخه مناسب‌تری انتخاب کند.</p><p>در WordPress و Elementor معمولاً اندازه‌های مختلف Media Library در این فرایند نقش دارند، اما باید در Network Panel بررسی کنی چه فایل واقعی دانلود شده است.</p><hr/></section><section aria-labelledby="concept-v31-11-section-08" class="concept-reference-part"><h3 id="concept-v31-11-section-08">Lazy Loading و تصویر LCP</h3><p>تصاویر پایین صفحه معمولاً می‌توانند Lazy Load شوند.</p><p>اما تصویر اصلی بالای صفحه که احتمالاً LCP است، نباید بی‌دلیل Lazy Load شود؛ چون شروع دانلود آن عقب می‌افتد.</p><p>تصویر ذهنی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">زیر Fold → دیرتر بارگذاری‌شدن معمولاً مفید
تصویر اصلی Hero → باید زود کشف و دانلود شود
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-11-section-09" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-11-section-09">در Elementor V4</h3><p>برای هر تصویر این قرارداد را ثبت کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Role: content / decorative
Source: media / dynamic
Aspect ratio: 16:9
Fit: cover
Focal point: inline-start center
Alt: meaningful / empty for decorative equivalent
Responsive source: verified
Loading priority: above-fold / below-fold
</code></pre></figure><p>Background را روی Box مسئول تزئین قرار بده. اگر یک Wrapper فقط برای نگه‌داشتن Background ساخته‌ای، بپرس آیا همان Parent موجود می‌تواند این مسئولیت را بگیرد یا نه.</p><hr/></section><section aria-labelledby="concept-v31-11-section-10" class="concept-reference-part"><h3 id="concept-v31-11-section-10">مثال واقعی: کارت محصول</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Product Card
├── Media Box (aspect-ratio: 4/3)
│   └── Product Image (object-fit: cover)
├── Title
├── Price
└── Button
</code></pre></figure><p>اگر تصویر Dynamic خالی بود:</p><ul>
<li>Fallback Image داری؟</li>
<li>Media Box باید پنهان شود؟</li>
<li>Gap باقی می‌ماند؟</li>
<li>ارتفاع کارت‌ها از هم جدا می‌شود؟</li>
</ul><p>این دیگر فقط موضوع تصویر نیست؛ Dynamic Data و Layout نیز دخیل‌اند.</p><hr/></section><section aria-labelledby="concept-v31-11-section-11" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-11-section-11">پل به DevTools</h3><p>در Network Panel ببین کدام فایل تصویر دانلود شده و اندازه آن چقدر است. در Elements/Computed این موارد را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">width / height
aspect-ratio
object-fit
object-position
background-size
background-position
</code></pre></figure><p>برای CLS، گزینهٔ Layout Shift Regions در DevTools می‌تواند جابه‌جایی‌ها را نشان دهد.</p><hr/></section><section aria-labelledby="concept-v31-11-section-12" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-11-section-12">اشتباهات رایج</h3><ul>
<li>Background برای تصویر محتوایی</li>
<li>Alt نامناسب یا تکرار متن اطراف</li>
<li>نداشتن ابعاد اولیه</li>
<li><code class="inline-code" dir="ltr">cover</code> بدون نقطه کانونی</li>
<li>Lazy Load روی Hero Image</li>
<li>فایل بسیار بزرگ برای نمایش کوچک</li>
<li>فرض سبک و امن بودن هر SVG</li>
<li>ساخت Duplicate Image برای هر Device بدون نیاز واقعی</li>
</ul><hr/></section><section aria-labelledby="concept-v31-11-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-11-section-13">تصویر ذهنی نهایی</h3><p>Image عکس قاب‌شده است؛ Background کاغذدیواری. Aspect Ratio قبل از رسیدن عکس، جای قاب را نگه می‌دارد و Object Fit تعیین می‌کند عکس چگونه داخل آن بنشیند.</p><hr/></section><section aria-labelledby="concept-v31-11-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-11-section-14">قوانین طلایی</h3><ul>
<li><strong>«محتوا را Image کن؛ تزئین را Background.»</strong></li>
<li><strong>«Aspect Ratio شکل Box را می‌سازد؛ Object Fit تصویر داخل آن را جا می‌دهد.»</strong></li>
<li><strong>«فضای تصویر را از ابتدا رزرو کن تا صفحه نپرد.»</strong></li>
<li><strong>«تصویر LCP را بی‌دلیل Lazy Load نکن.»</strong></li>
<li><strong>«SVG برداری است، اما خودبه‌خود سبک و امن نیست.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Image element and V4 style controls</li>
<li>CSS Images / CSS Sizing specifications</li>
<li>web.dev: Optimize CLS and LCP</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-11-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-11-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Image؛ Box اندازه دارد، محتوا نسبت و fit دارد</span></summary>
<section aria-labelledby="lesson-11-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Width و Height Box تصویر را می‌سازند؛ Aspect Ratio نسبت است و Object Fit keyword. این سه نوع مقدار را جدا نگه دار.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> قاب عکس اندازه دارد، نسبت قاب یک کسر است و روش بریدن عکس یک دستور مثل Cover یا Contain.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Width / Min / Max</th><td><code dir="ltr">width / min-width / max-width</code></td><td>مثال رسمی: % برای width و px برای min/max</td><td>Parent یا طول ثابت</td><td>% + min/max برای تصویر سیال با حد.</td><td>height و width مستقل می‌توانند تصویر را بکشند.</td><td><code dir="ltr">E_SIZE</code></td></tr><tr><th scope="row">Aspect Ratio</th><td><code dir="ltr">aspect-ratio</code></td><td>نسبت مانند 16 / 9</td><td>بدون واحد طول</td><td>برای حفظ شکل Box.</td><td>نسبت با Width برابر نیست.</td><td><code dir="ltr">E_SIZE</code></td></tr><tr><th scope="row">Object Fit</th><td><code dir="ltr">object-fit</code></td><td>fill / cover / contain…</td><td>keyword</td><td>نحوهٔ جاگیری پیکسل‌های تصویر داخل Box.</td><td>Cover ممکن است بخش مهم تصویر را crop کند.</td><td><code dir="ltr">E_SIZE</code></td></tr><tr><th scope="row">Object Position</th><td><code dir="ltr">object-position</code></td><td>keyword، درصد یا طول در CSS</td><td>Content box</td><td>برای focal point.</td><td>بدون تست Mobile نقطهٔ کانونی ممکن است گم شود.</td><td><code dir="ltr">CSS_VALUES</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>قاب 360px با aspect-ratio:16/9 → height تقریبی 202.5px.</p></section>
<section><h3>📱 در Responsive</h3><p>Width معمولاً سیال می‌شود و Max Width سقف می‌گذارد؛ ارتفاع را تا حد امکان از ratio/auto بگیر.</p></section>
<section><h3>🔬 در DevTools</h3><p>natural size، rendered size، aspect-ratio، object-fit و object-position را بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/style-tab-size/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Size</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length" rel="noopener noreferrer" target="_blank">MDN — CSS length values</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-11-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-11-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — Logoها</h3><p>برای Imageهای Logo:</p><section aria-labelledby="section-hidden-167-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-167-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Width</dt><dd>100% داخل Frame</dd><dt>Height</dt><dd>کنترل‌شده</dd><dt>Object Fit</dt><dd>Contain</dd></dl></section><p>حالا Platform Visual را آماده کن:</p><section aria-labelledby="section-hidden-168-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-168-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Width</dt><dd>100%</dd><dt>Max Width</dt><dd>کنترل‌شده</dd><dt>Aspect Ratio</dt><dd>1 / 1</dd></dl></section><p>هنوز Core و Node نساز؛ فقط Stage مربع را ببین.</p><h3>❓ سؤال توقف</h3><p>برای Logo برند، Cover یا Contain؟</p><details class="disclosure-card"><summary>پاسخ</summary>Contain.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> Width و Height Image را طوری تنظیم کنی که نسبت طبیعی کشیده شود.</p><p><strong>نشانه:</strong> Logo یا چهره دفرمه می‌شود.</p><h3>🧪 عمداً خرابش کن</h3><p>Logo را روی <code class="inline-code" dir="ltr">object-fit: cover</code> بگذار و Frame را مربع کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>بخشی از Logo ممکن است Crop شود؛</li>
<li>نام برند ناقص دیده شود؛</li>
<li>فضای Frame پر می‌شود، اما محتوا آسیب می‌بیند.</li>
</ul><p>Contain را برگردان.</p><p>Aspect Ratio Stage را حذف کن و Width را تغییر بده.</p><h4>👀 انتظار دوم</h4><p>Stage ممکن است بیضی یا نامتناسب شود و مختصات Nodeهای آینده قابل اتکا نباشد.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-169-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-169-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-61"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-61-1" name="chk-61-1" type="checkbox"/><span>Logoها کامل دیده می‌شوند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-61-2" name="chk-61-2" type="checkbox"/><span>Visual Stage مربع باقی می‌ماند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-61-3" name="chk-61-3" type="checkbox"/><span>Image محتوایی Alt مناسب دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-61-4" name="chk-61-4" type="checkbox"/><span>Background تزئینی با Image محتوایی اشتباه نشده</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Cover و Contain چه تفاوتی دارند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> برای Logo، عکس محصول و Pattern تزئینی ابزار رسانه‌ای مناسب را انتخاب کن.</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-62"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-62-1" name="chk-62-1" type="checkbox"/><span>محتوایی یا تزئینی‌بودن رسانه را تشخیص داده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-62-2" name="chk-62-2" type="checkbox"/><span>Image/SVG/Background و Cover/Contain را با دلیل انتخاب کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-62-3" name="chk-62-3" type="checkbox"/><span>Alt، Aspect Ratio یا Object Position مرتبط را در نظر گرفته است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-11-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-11-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-IMAGE-001</h3><p><strong>هدف:</strong> ⚖️ دو روش را مقایسه کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">context_dependent</code></p><p>چهار Image Card دارای Cover، ارتفاع 15vw و Min/Max Height هستند. تمرین:</p><section aria-labelledby="section-hidden-172-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-172-heading">بخش آموزشی</h2><ul><li>روش فعلی چند محدودیتی</li>
<li>در برابر</li>
<li>Media Frame با Aspect Ratio</li></ul></section><p>نتیجه فقط پس از تست Desktop، Tablet و Mobile معتبر است.</p><h3>🔬 پشت صحنه</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text language-css" dir="ltr">aspect-ratio: 1;
object-fit: contain;
</code></pre><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-11-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-11-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-64"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-64-1" name="chk-64-1" type="checkbox"/><span>می‌توانی Image، SVG و Background را براساس محتوایی یا تزئینی بودن انتخاب کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-64-2" name="chk-64-2" type="checkbox"/><span>می‌توانی Cover، Contain، Aspect Ratio و Object Position را از هم جدا کنی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-65"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-65-1" name="chk-65-1" type="checkbox"/><span>قاب Logoها را با Contain و Visual Stage را با Aspect Ratio پایدار می‌سازی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-65-2" name="chk-65-2" type="checkbox"/><span>برای Image محتوایی Alt مناسب تعیین می‌کنی و تصویر تزئینی را درست علامت می‌زنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-66"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-66-1" name="chk-66-1" type="checkbox"/><span>برای عکس محصول، Logo برند و Pattern پس‌زمینه می‌توانی سه انتخاب متفاوت و دلیل هرکدام را بیان کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-11-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-11-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>ایستگاه C کامل شد. ستون محتوا، Logoها و Stage مربع را بدون راهنما بازسازی کن.</p><hr/><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 11</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-11-completion"><fieldset><legend>ثبت پایان درس 11</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-11-complete" name="lesson-11-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-11-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Image Element در برابر Background Image</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Image Element</h3><p>Image Element مثل قاب عکس روی دیوار است: اگر تصویر پیام، محتوا، محصول یا اطلاعات دارد، باید به‌عنوان تصویر واقعی وارد صفحه شود و alt مناسب داشته باشد.</p></section>
<section class="inline-compare-card"><h3>Background Image</h3><p>Background مثل کاغذ دیواری است: برای تزئین، texture، atmosphere یا تصویر غیرمحتوایی مناسب است.</p><p class="golden-rule">قانون طلایی: تصویر محتوایی را background نکن؛ تصویر تزئینی را بی‌دلیل Image Element نکن.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="lesson-11-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — تصویر، Crop و Visual Stage</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>تصویر خانه در Mobile نسبت به Desktop crop متفاوتی دارد. تصمیم‌های زیر باید در breakpoint Mobile بررسی شوند: <code>object-fit</code>، <code>object-position</code>، aspect ratio و focal point.</p>
<p>فایل مرجع Mobile یک تصویر طراحی است؛ از آن نمی‌توان نتیجه گرفت که تصویر باید Background باشد یا Image Element. این تصمیم باید با معنا و دسترسی‌پذیری تعیین شود.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-11-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Crop تصویر و Aspect Ratio در Mobile</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> تفاوت تغییر اندازهٔ عنصر و تغییر crop تصویر را عملاً ببین.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>تصویر خانهٔ TUYA را در Visual Stage قرار بده.</li><li>دو حالت Image Element و Background را جدا آزمایش کن.</li><li>در Mobile object-fit/background-size و position را طوری تنظیم کن که نقطهٔ کانونی حفظ شود.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن در حالت Cover کدام قسمت تصویر حذف می‌شود.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>ارتفاع Stage را ثابت و بسیار کم کن و Cover را نگه دار.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>ابعاد intrinsic، rendered size، object-fit/object-position یا background-size/position.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> Crop آگاهانه است، نسبت تصویر بی‌دلیل کشیده نشده و سوژهٔ اصلی در Mobile باقی مانده است.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-11-responsive-build-test-done-build"><input data-persist="" id="lesson-11-responsive-build-test-done-build" name="lesson-11-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-11-responsive-build-test-done-test"><input data-persist="" id="lesson-11-responsive-build-test-done-test" name="lesson-11-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-11-responsive-build-test-done-debug"><input data-persist="" id="lesson-11-responsive-build-test-done-debug" name="lesson-11-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-11-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-11-responsive-build-test-note" name="lesson-11-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/responsive-editing/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-11-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Aspect Ratio و media sizing</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
