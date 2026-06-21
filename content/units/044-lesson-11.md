<article class="lesson card-surface" data-lesson="11" id="lesson-11">

<h2 class="lesson-title former-h1">درس 11 — Image، SVG، Background، Aspect Ratio و Object Fit</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-11-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-11-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> برای هر رسانه، نقش درست انتخاب کنی: آیا تصویر محتواست، تزئین است، لوگو/SVG است، Background است یا بخشی از Visual Stage؟ سپس Aspect Ratio و Object Fit را با همان نقش تنظیم کنی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> بهینه‌سازی پیشرفته فرمت‌ها، srcset/sizes دستی، pipeline کامل Performance، SVG sanitization عمیق، یا Position نهایی Orbit Nodeها.</p>
<p><strong>در پایان باید بتوانی:</strong> Logoها را بدون Crop نمایش بدهی، Visual Stage را با Aspect Ratio قابل پیش‌بینی نگه داری، و تشخیص بدهی چه چیزی Image Element است و چه چیزی Background تزئینی.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-11-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-11-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + ♿ دسترسی‌پذیری + 🔍 Performance-aware</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۰–۳۰ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۴۰ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۵ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> رسانه را هم‌زمان از سه زاویه ببین: معنی محتوا، رفتار قاب و هزینهٔ بارگذاری. هنرجو نباید برای هر چیز شبیه تصویر یک تصمیم واحد بگیرد.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_media_decision_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-11-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-11-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>تا اینجا Structure، Layout، Text و Logo Strip را ساختی. حالا باید رسانه‌ها را درست وارد کنی: Logoها نباید بریده شوند، Visual Stage باید شکل قابل پیش‌بینی داشته باشد، و Backgroundهای تزئینی نباید با Imageهای محتوایی اشتباه شوند.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Structure / Layout / Text
↓
Media Role
↓
Image vs Background vs SVG
↓
Aspect Ratio
↓
Object Fit / Object Position
↓
Accessibility / Performance</code></pre>
</figure>

<h3>Decision Tree رسانه</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>◇ اگر تصویر Load نشود، کاربر اطلاعاتی از دست می‌دهد؟</li>
<li>├─ بله → <strong>Image Element + alt مناسب</strong></li>
<li>└─ خیر</li>
<li>◇ آیا فقط تزئین بصری، بافت، گرادیان یا ornament است؟</li>
<li>├─ بله → <strong>Background یا Decoration</strong></li>
<li>└─ خیر</li>
<li>◇ آیا Logo/Icon/Illustration برداری است؟</li>
<li>├─ بله → <strong>SVG/Icon مناسب، با viewBox سالم</strong></li>
<li>└─ دوباره نقش محتوایی را بررسی کن</li>
</ul>
</section>

<h3>Image یا Background؟</h3>
<p>Image وقتی مناسب‌تر است که خود تصویر بخشی از محتوا باشد: محصول، چهره، Logo معنی‌دار، نمودار یا تصویری که نبودنش پیام را ناقص می‌کند. Background وقتی مناسب‌تر است که نقش تزئینی دارد: بافت، رنگ، گرادیان، ornament یا فضای بصری.</p>
<p>قاعدهٔ کوتاه: <strong>محتوا را Image کن؛ تزئین را Background.</strong></p>

<h3>Cover و Contain</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Cover vs Contain">
<table class="data-table educational-table edu-table">
<caption>Cover و Contain</caption>
<thead><tr><th scope="col">Fit</th><th scope="col">رفتار</th><th scope="col">مناسب برای</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Cover</th><td>قاب را پر می‌کند؛ ممکن است تصویر Crop شود.</td><td>Hero Photo، Card Image، Background تصویری</td><td>برای Logo استفاده شود و لوگو بریده شود.</td></tr>
<tr><th scope="row">Contain</th><td>کل تصویر دیده می‌شود؛ ممکن است فضای خالی بماند.</td><td>Logo، Icon، Illustration مهم</td><td>برای Hero Photo استفاده شود و قاب خالی بماند.</td></tr>
<tr><th scope="row">Object Position</th><td>نقطهٔ کانونی Crop را کنترل می‌کند.</td><td>تصویر با سوژهٔ مشخص</td><td>با center center صورت یا محصول بریده شود.</td></tr>
</tbody>
</table>
</div>

<h3>Aspect Ratio؛ شکل قاب قبل از رسیدن تصویر</h3>
<p>Aspect Ratio کمک می‌کند Box رسانه از قبل شکل خود را داشته باشد. این باعث می‌شود Layout قابل پیش‌بینی‌تر بماند و با Load شدن تصویر، صفحه ناگهانی نپرد.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.media-box {
  aspect-ratio: 4 / 3;
}</code></pre>
</figure>

<h3>SVG چیست و چرا ساده نیست؟</h3>
<p>SVG تصویر برداری است و برای Logo، Icon و Illustration خطی مناسب است. اما هر SVG خودبه‌خود سبک، امن یا تمیز نیست. یک SVG می‌تواند Pathهای زیاد، Filter سنگین، Metadata اضافه یا viewBox خراب داشته باشد.</p>

<h3>Logoها چه Fit می‌خواهند؟</h3>
<p>Logo معمولاً نباید بریده شود. بنابراین نقطهٔ شروع سالم برای Logoها معمولاً <code dir="ltr">contain</code> و کنترل <code dir="ltr">max-width / max-height</code> است. اگر Logo در قاب پر نشود، فضای خالی قابل قبول‌تر از بریدن برند است.</p>

<h3>Visual Stage چه می‌خواهد؟</h3>
<p>Visual Stage در TUYA باید شکل قابل پیش‌بینی داشته باشد تا بعداً Core و Orbit Nodes نسبت به یک محدودهٔ پایدار قرار بگیرند. در این درس فقط قاب Stage را با Aspect Ratio تثبیت می‌کنی؛ هنوز Nodeها را Position نمی‌کنی.</p>

<h3>Lazy Load و LCP را با هم قاطی نکن</h3>
<p>تصاویر پایین صفحه معمولاً می‌توانند Lazy Load شوند. اما اگر تصویر بالای صفحه و کاندید LCP است، Lazy Load بی‌دلیل می‌تواند شروع دانلود را عقب بیندازد. در این درس فقط اصل تصمیم را می‌آموزیم؛ Audit کامل Performance بعداً می‌آید.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-11.0.0" id="lesson-11-concept-reference">
<summary>📚 مرجع مفهومی کامل — Image، SVG، Background، Aspect Ratio و Object Fit</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="11" data-source-version="tuya-revised-11.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی کامل درس را حفظ می‌کند و آن را به پروژهٔ TUYA وصل می‌کند. هدف، انتخاب دقیق نقش رسانه است؛ نه فقط جا دادن فایل تصویر در صفحه.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-11-ref-problem">
<h3 id="lesson-11-ref-problem">۱. مسئله‌ای که این مفهوم حل می‌کند</h3>
<p>همهٔ چیزهایی که شبیه تصویر دیده می‌شوند نقش یکسان ندارند:</p>
<ul>
<li>تصویر محصول بخشی از محتواست.</li>
<li>بافت پشت Hero تزئینی است.</li>
<li>Logo ممکن است SVG باشد.</li>
<li>عکس کارت ممکن است نیاز به Crop داشته باشد.</li>
<li>Hero Image ممکن است عنصر LCP باشد.</li>
</ul>
<p>انتخاب اشتباه میان Image، Background و SVG روی Accessibility، Responsive، Performance و نگهداری اثر می‌گذارد.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-11-room">
<h3 id="lesson-11-room">۲. تشبیه عکس قاب‌شده و کاغذدیواری</h3>
<ul>
<li><strong>عکس قاب‌شده:</strong> معنا دارد؛ اگر حذف شود، بخشی از محتوا از بین می‌رود. این Image Element است.</li>
<li><strong>کاغذدیواری:</strong> فضا را زیباتر می‌کند؛ اگر حذف شود، پیام اصلی هنوز باقی است. این Background است.</li>
<li><strong>نقشهٔ برداری:</strong> با خطوط و مسیرها مقیاس‌پذیر است. این شبیه SVG است.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-aspect">
<h3 id="lesson-11-aspect">۳. Aspect Ratio و رزرو فضا</h3>
<p>اگر جعبهٔ تصویر قبل از Load شدن فایل شکل مشخصی نداشته باشد، محتوای پایین ممکن است بعد از Load تصویر جابه‌جا شود. Aspect Ratio یا width/height واقعی برای Image کمک می‌کند مرورگر زودتر شکل قاب را بداند.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.visual-stage {
  aspect-ratio: 1 / 1;
}

.logo-frame {
  aspect-ratio: 3 / 1;
}</code></pre>
</figure>
<p>برای TUYA، Visual Stage می‌تواند در این مرحله مربع یا نزدیک‌به‌مربع تست شود، اما مقدار نهایی تا قبل از Screenshot و Breakpoint Validation قطعی نیست.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-fit">
<h3 id="lesson-11-fit">۴. Object Fit و Object Position</h3>
<p><code dir="ltr">object-fit</code> می‌گوید تصویر چگونه داخل قاب بنشیند. <code dir="ltr">object-position</code> می‌گوید اگر Crop رخ دهد، نقطهٔ کانونی کجا باشد.</p>
<ul>
<li><strong>cover:</strong> قاب پر می‌شود، احتمال بریدگی هست.</li>
<li><strong>contain:</strong> کل تصویر دیده می‌شود، احتمال فضای خالی هست.</li>
<li><strong>object-position:</strong> مرکز توجه Crop را تنظیم می‌کند.</li>
</ul>
<p>برای چهره یا محصول، Cover بدون Focal Point می‌تواند سوژه را ببرد. برای Logo، Cover معمولاً خطرناک است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-svg">
<h3 id="lesson-11-svg">۵. SVG؛ برداری، اما نه همیشه سبک و امن</h3>
<p>SVG برای Logo و Icon عالی است، چون با Scale شدن شارپ می‌ماند. اما قبل از استفاده باید این‌ها را بررسی کنی:</p>
<ul>
<li>viewBox درست است؟</li>
<li>Pathها بیش از حد زیاد نیستند؟</li>
<li>Filter یا افکت سنگین ندارد؟</li>
<li>Metadata اضافه یا کد ناخواسته ندارد؟</li>
<li>از منبع معتبر آمده است؟</li>
<li>در UI واقعی به‌درستی مقیاس می‌شود؟</li>
</ul>
<p>در این درس Sanitization عمیق را انجام نمی‌دهیم، اما فرض سبک و امن بودن هر SVG ممنوع است.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-alt">
<h3 id="lesson-11-alt">۶. Alt Text و نقش محتوا</h3>
<p>برای Image محتوایی، alt باید معنی تصویر را منتقل کند. برای تصویر تزئینی، alt خالی یا مدیریت تزئینی مناسب‌تر است تا Screen Reader محتوای بی‌ارزش نخواند.</p>
<p>برای Logo، تصمیم به نقش صفحه بستگی دارد:</p>
<ul>
<li>Logo برند/مشتری/همکار که پیام اعتمادسازی دارد → معمولاً محتوایی است و alt معنی‌دار لازم دارد.</li>
<li>Logo صرفاً تزئینی و تکراری → ممکن است decorative باشد.</li>
<li>Logo لینک‌دار → alt باید مقصد یا برند را روشن کند.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-responsive-images">
<h3 id="lesson-11-responsive-images">۷. Responsive Images و فایل واقعی</h3>
<p>یک تصویر ۲۵۰۰px برای قاب ۳۲۰px معمولاً اتلاف پهنای باند است. در WordPress/Elementor، Media Library می‌تواند اندازه‌های مختلف تصویر بسازد، اما باید در Network Panel دید واقعاً چه فایل دانلود شده است.</p>
<p>در این درس فقط اصل را می‌گیریم: اندازهٔ فایل واقعی باید با اندازهٔ نمایش منطقی باشد. Audit کامل srcset/sizes در درس Performance انجام می‌شود.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-lcp">
<h3 id="lesson-11-lcp">۸. Lazy Load و تصویر بالای صفحه</h3>
<p>Lazy Loading برای تصاویر پایین صفحه مفید است؛ اما تصویر اصلی بالای صفحه که احتمالاً LCP است، نباید بی‌دلیل Lazy Load شود. این تصمیم باید با مشاهدهٔ واقعی صفحه و DevTools/Performance انجام شود.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Below fold → lazy loading معمولاً مفید
Hero / LCP candidate → اولویت بارگذاری را بررسی کن</code></pre>
</figure>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-tuya-contract">
<h3 id="lesson-11-tuya-contract">۹. قرارداد TUYA برای رسانه‌ها</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA media contract">
<table class="data-table educational-table edu-table">
<caption>قرارداد رسانه در TUYA</caption>
<thead><tr><th scope="col">رسانه</th><th scope="col">نقش</th><th scope="col">Element / Fit</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Logoهای Logo Strip</th><td>اعتمادسازی یا برند؛ نیازمند تصمیم alt</td><td>Image/SVG با contain و max-size</td><td><code dir="ltr">provisional_until_assets</code></td></tr>
<tr><th scope="row">Visual Stage</th><td>قاب بصری اصلی</td><td>Container با aspect-ratio</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Core Cloud</th><td>Illustration/SVG مرکزی</td><td>SVG/Image با contain</td><td><code dir="ltr">provisional_until_asset</code></td></tr>
<tr><th scope="row">Background ornament</th><td>تزئینی</td><td>Background یا pseudo/decorative</td><td><code dir="ltr">unknown_until_design</code></td></tr>
<tr><th scope="row">Orbit Node icon</th><td>Icon معنی‌دار یا تزئینی، بسته به متن همراه</td><td>SVG/Icon</td><td><code dir="ltr">unknown_until_node_content</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-11-devtools">
<h3 id="lesson-11-devtools">۱۰. Debug رسانه در DevTools</h3>
<p>در Elements/Computed این‌ها را بررسی کن:</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">width / height
aspect-ratio
object-fit
object-position
background-size
background-position
natural image size
rendered image size</code></pre>
</figure>
<p>در Network Panel ببین چه فایل واقعی دانلود شده است. برای Layout Shift، ابزارهای Performance/Layout Shift Regions می‌توانند نشان بدهند تصویر باعث پرش شده یا نه.</p>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-11-traps">
<h3 id="lesson-11-traps">۱۱. اشتباهات رایج</h3>
<ul>
<li>استفاده از Background برای تصویر محتوایی.</li>
<li>Alt نامناسب یا تکرار متن اطراف.</li>
<li>نداشتن ابعاد اولیه یا Aspect Ratio.</li>
<li>استفاده از Cover برای Logo و بریدن برند.</li>
<li>Cover بدون object-position برای تصویر دارای سوژه.</li>
<li>Lazy Load روی Hero/LCP candidate بدون دلیل.</li>
<li>فایل بسیار بزرگ برای نمایش کوچک.</li>
<li>فرض سبک و امن بودن هر SVG.</li>
<li>ساخت Duplicate Image برای هر Device بدون نیاز واقعی.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-11-golden">
<h3 id="lesson-11-golden">۱۲. قوانین طلایی</h3>
<ul>
<li><strong>محتوا را Image کن؛ تزئین را Background.</strong></li>
<li><strong>Aspect Ratio شکل Box را می‌سازد؛ Object Fit تصویر داخل آن را جا می‌دهد.</strong></li>
<li><strong>Logo معمولاً Contain می‌خواهد، نه Cover.</strong></li>
<li><strong>فضای تصویر را از ابتدا رزرو کن تا صفحه نپرد.</strong></li>
<li><strong>تصویر LCP را بی‌دلیل Lazy Load نکن.</strong></li>
<li><strong>SVG برداری است، اما خودبه‌خود سبک و امن نیست.</strong></li>
<li><strong>Visual Stage را فعلاً قاب‌بندی کن؛ Nodeها را هنوز Position نکن.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>رفتارهای Image، Background، aspect-ratio، object-fit، SVG و Lazy Loading بر پایهٔ CSS/HTML و رفتار مرورگر نوشته شده‌اند. تصمیم‌های TUYA تا پیش از مشاهدهٔ assetهای واقعی، Network و Breakpoint Validation قطعی نیستند.</p>
<ul>
<li><a href="https://elementor.com/help/style-tab-background/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Background</a></li>
<li><a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor — Style tab: Layout</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio" rel="noopener noreferrer" target="_blank">MDN — aspect-ratio</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit" rel="noopener noreferrer" target="_blank">MDN — object-fit</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/SVG" rel="noopener noreferrer" target="_blank">MDN — SVG</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-11-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-11-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Aspect Ratio، Fit، Position و Image Size</span>
</summary>
<section aria-labelledby="lesson-11-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Aspect Ratio عدد نسبت است؛ Object Fit keyword است؛ Width/Height/Max Size واحد طول دارند؛ File Size و Rendered Size را باید جدا ببینی.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۱" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">Aspect Ratio</th><td>ratio مثل <code dir="ltr">1/1</code> یا <code dir="ltr">16/9</code></td><td>قاب Media Box</td><td>فقط Width را بدهی و ارتفاع تصادفی شود.</td></tr>
<tr><th scope="row">Object Fit</th><td>keyword: cover / contain</td><td>Image داخل قاب</td><td>Cover برای Logo استفاده شود.</td></tr>
<tr><th scope="row">Object Position</th><td>keyword / %</td><td>نقطهٔ Crop</td><td>سوژه با center center بریده شود.</td></tr>
<tr><th scope="row">Max Width / Height</th><td>px / rem / %</td><td>حد رشد رسانه</td><td>فایل واقعی با نمایش کوچک ناسازگار باشد.</td></tr>
<tr><th scope="row">Background Size</th><td>cover / contain / length</td><td>Background painting area</td><td>Background برای محتوای معنی‌دار استفاده شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>قاب 1/1 با عرض 320px یعنی ارتفاع مؤثر 320px. قاب 16/9 با عرض 320px یعنی ارتفاع حدود 180px. نسبت قاب را قبل از Fit تعیین کن.</p></section>
<section><h3>📱 در Responsive</h3><p>Visual Stage ممکن است در Desktop مربع باشد، اما در Mobile نیاز به نسبت متفاوت یا max-size داشته باشد. مقدار نهایی را قطعی نکن.</p></section>
<section><h3>🔬 در DevTools</h3><p>natural size، rendered size، object-fit، aspect-ratio، background-size و Network downloaded file را کنار هم ببین.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-11-media-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Image، Background، Cover یا Contain؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر مورد را اول تصمیم بگیر، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="Step Through Media Decision">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تصمیم‌های رسانه</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">تصمیم اولیه</th><th scope="col">دلیل</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Logo برند در Logo Strip</th><td>Image/SVG + contain</td><td>نباید بریده شود و ممکن است محتوا باشد.</td><td><code dir="ltr">provisional_until_alt_decision</code></td></tr>
<tr><th scope="row">بافت تزئینی پشت Hero</th><td>Background</td><td>حذفش پیام اصلی را نابود نمی‌کند.</td><td><code dir="ltr">provisional_until_design</code></td></tr>
<tr><th scope="row">عکس کارت محصول</th><td>Image + cover</td><td>تصویر محتواست، ولی Crop کنترل‌شده ممکن است لازم باشد.</td><td><code dir="ltr">content_dependent</code></td></tr>
<tr><th scope="row">Visual Stage TUYA</th><td>Container + aspect-ratio</td><td>قاب پایدار برای Illustration/Nodeهای بعدی.</td><td><code dir="ltr">provisional_until_stage_lesson</code></td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-11-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-11-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — Media Role Audit و قاب‌بندی Visual Stage</h3>
<p>در این تمرین، فقط رسانه‌ها را نقش‌گذاری و قاب‌بندی می‌کنی. هنوز Orbit Nodeها، Position نهایی، Animation، Shadow/Glow، Performance audit کامل یا Optimization پیشرفته انجام نمی‌دهی.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 11">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از کار با رسانه</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Logoها نباید Crop شوند.</td><td>Contain و max-size نقطهٔ شروع سالم است.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Visual Stage باید قاب قابل پیش‌بینی داشته باشد.</td><td>Aspect Ratio را روی Stage تست می‌کنیم.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>Aspect Ratio دقیق Stage، max-size Logoها، alt text و Loading priority.</td><td>با asset واقعی و UI واقعی تست می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>فایل‌های واقعی SVG/PNG، viewBox، اندازهٔ دانلود، LCP واقعی.</td><td>در این درس قطعی نمی‌شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — رسانه‌ها را فقط نقش‌گذاری کن</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس یازده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> تشخیص نقش رسانه و قاب اولیه، نه طراحی نهایی.</p>
<p><strong>مسیر:</strong> Elementor Editor → Structure → بررسی <code dir="ltr">Logo Strip</code> و <code dir="ltr">TUYA Visual</code>.</p>
<p><strong>Element هدف:</strong> فقط Logoها، Visual Stage و رسانه‌های داخل آن.</p>
<p><strong>Class فعال:</strong> Classهای محلی رسانه؛ Global جدید نساز مگر reuse واقعی ثابت شود.</p>
<p><strong>Property:</strong> Role / alt decision / aspect-ratio / object-fit / max-size.</p>
<p><strong>نباید تغییر کند:</strong> Copy typography، Shell layout، Grid آزمایشی، Node position، Shadow/Glow، Background نهایی.</p>
<p><strong>عبارت تأیید پایانی:</strong> «هر رسانه نقش‌گذاری شد؛ Logoها Crop نمی‌شوند و Visual Stage فقط قاب‌بندی شده است.»</p>
</aside>

<h3>مرحلهٔ ۲ — قرارداد رسانه را ثبت کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Media inventory">
<table class="data-table educational-table edu-table">
<caption>دفترچهٔ رسانه‌های TUYA</caption>
<thead><tr><th scope="col">رسانه</th><th scope="col">Role</th><th scope="col">Fit/Ratio</th><th scope="col">Accessibility</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Logo Strip Logos</th><td>brand/trust یا decorative؟</td><td><code dir="ltr">contain</code> + max-size</td><td>alt تصمیم‌گیری شود</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Visual Stage</th><td>قاب بصری</td><td><code dir="ltr">aspect-ratio: 1/1</code> شروع تست</td><td>container است، نه image</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Core Cloud</th><td>illustration/icon مرکزی</td><td><code dir="ltr">contain</code></td><td>بسته به متن همراه</td><td><code dir="ltr">unknown_until_asset</code></td></tr>
<tr><th scope="row">Background Ornament</th><td>decorative</td><td>Background</td><td>نباید alt خوانده شود</td><td><code dir="ltr">unknown_until_design</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — مقدارهای شروع را تست کن</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Provisional media values">
<table class="data-table educational-table edu-table">
<caption>مقدارهای شروع رسانه</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">مقدار شروع</th><th scope="col">وضعیت</th><th scope="col">یادداشت</th></tr></thead>
<tbody>
<tr><th scope="row">Logo Fit</th><td><code dir="ltr">contain</code></td><td><code dir="ltr">recommended_start</code></td><td>Logo نباید Crop شود.</td></tr>
<tr><th scope="row">Logo max width</th><td><code dir="ltr">80px</code> تا <code dir="ltr">120px</code></td><td><code dir="ltr">provisional</code></td><td>به فایل واقعی بستگی دارد.</td></tr>
<tr><th scope="row">Logo max height</th><td><code dir="ltr">28px</code> تا <code dir="ltr">40px</code></td><td><code dir="ltr">provisional</code></td><td>نسبت تصویر حفظ شود.</td></tr>
<tr><th scope="row">Visual Stage Ratio</th><td><code dir="ltr">1 / 1</code> شروع تست</td><td><code dir="ltr">provisional</code></td><td>برای قاب پایدار Nodeهای بعدی.</td></tr>
<tr><th scope="row">Core Cloud Fit</th><td><code dir="ltr">contain</code></td><td><code dir="ltr">provisional</code></td><td>اگر SVG/Illustration نباید بریده شود.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۴ — تست Crop</h3>
<ol>
<li>یک Logo را داخل قاب کوچک‌تر تصور یا تست کن.</li>
<li>Cover را ذهنی اعمال کن؛ آیا بخشی از برند حذف می‌شود؟</li>
<li>Contain را اعمال کن؛ آیا فضای خالی قابل قبول است؟</li>
<li>اگر Logo ناخواناست، اندازهٔ قاب و max-size را بررسی کن، نه اینکه Cover بزنی.</li>
</ol>

<h3>مرحلهٔ ۵ — سؤال توقف</h3>
<p>برای Logo برند داخل Logo Strip، انتخاب اولیهٔ امن‌تر چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-11">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-11-a" name="stop-question-11" type="radio" value="A"/><span>A) Cover، چون قاب را پر می‌کند.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-11-b" name="stop-question-11" type="radio" value="B"/><span>B) Contain، چون کل Logo باید دیده شود.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-11-c" name="stop-question-11" type="radio" value="C"/><span>C) Background، چون همهٔ تصویرها باید Background باشند.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> برای Logo، دیده‌شدن کامل برند معمولاً مهم‌تر از پرکردن قاب است. Cover ممکن است بخشی از Logo را ببرد.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> چون یک تصویر زیباست، آن را Background کنی؛ یا چون SVG است، آن را خودبه‌خود سبک و امن فرض کنی.</p>
<p><strong>نشانه:</strong> Alt از دست می‌رود، Performance بد می‌شود، یا Logo در مقیاس‌های مختلف خراب می‌شود.</p>
<p><strong>قاعده:</strong> اول Role، بعد Element، بعد Ratio/Fit، بعد Performance.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<p>این تصمیم خراب را تصور کن:</p>
<figure class="visual-figure ascii-figure">
<figcaption>تصمیم رسانهٔ خراب</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-text inline-code" dir="ltr">Logo brand:
- background-image
- background-size: cover
- no alt
- no max size

نتیجه:
- برند Crop می‌شود
- Screen Reader چیزی نمی‌فهمد
- کنترل اندازه سخت‌تر می‌شود</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-61">
<fieldset>
<legend>Checkpoint درس ۱۱</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-61-1" name="chk-61-1" type="checkbox"/><span>برای هر رسانه Role نوشته‌ام: content، decorative، SVG/icon یا stage container.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-61-2" name="chk-61-2" type="checkbox"/><span>Logoها با Contain و max-size بررسی شده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-61-3" name="chk-61-3" type="checkbox"/><span>Visual Stage فقط Aspect Ratio گرفته و هنوز Nodeها Position نشده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-61-4" name="chk-61-4" type="checkbox"/><span>Alt decision و decorative decision را provisional ثبت کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-61-5" name="chk-61-5" type="checkbox"/><span>SVG را خودبه‌خود سبک/امن فرض نکرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-61-6" name="chk-61-6" type="checkbox"/><span>Performance/LCP کامل را هنوز قطعی نکرده‌ام.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Image و Background را با یک مثال توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> برای یک کارت محصول، تصویر محصول باید Image باشد یا Background؟ چرا؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید نقش محتوا را محور قرار دهد، نه ظاهر. اگر نبود تصویر باعث از دست‌رفتن اطلاعات شود، Image Element با alt مناسب معمولاً انتخاب قابل دفاع‌تری است.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-11-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Ratio و Fit در اندازه‌های مختلف</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_asset_validation</code></p>
<ul>
<li>Logoها را در Desktop، Tablet و Mobile با Contain تست کن.</li>
<li>اگر فضای خالی زیاد شد، قاب یا max-size را اصلاح کن؛ Cover نزن مگر Crop قابل قبول باشد.</li>
<li>Visual Stage را با نسبت شروع 1/1 تست کن، اما نسبت نهایی را قطعی نکن.</li>
<li>Core Cloud را بدون Crop تست کن.</li>
<li>اگر رسانه بالای صفحه است، Loading Priority/LCP را بعداً با DevTools بررسی کن.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-11-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-11-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — تصویر درست دیده می‌شود ولی تصمیم اشتباه است</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی تصمیم رسانه<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">decision_audit</code></p>
<p>سناریو: Logoها ظاهراً داخل قاب دیده می‌شوند، اما به‌عنوان Background با Cover ساخته شده‌اند.</p>
<p>قبل از پذیرش، این‌ها را ثبت کن:</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا Logo محتواست یا تزئین؟</li>
<li>آیا alt لازم دارد؟</li>
<li>آیا Cover بخشی از Logo را در breakpoint دیگر می‌برد؟</li>
<li>آیا Background باعث سخت‌تر شدن کنترل اندازه و نسبت شده؟</li>
<li>آیا SVG viewBox سالم است؟</li>
<li>آیا فایل واقعی در Network منطقی است؟</li>
</ul>
</section>
<p>نتیجهٔ درست: ظاهر فعلی کافی نیست؛ role، accessibility و رفتار responsive را هم بررسی کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، natural size و rendered size را با هم بخوان. اگر تصویر ۲۰۰۰px برای نمایش ۱۰۰px دانلود شده، ظاهر درست است اما Performance تصمیم خوبی نیست.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-11-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-11-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-64">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-64-1" name="chk-64-1" type="checkbox"/><span>می‌توانم Image و Background را براساس نقش محتوا از هم جدا کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-64-2" name="chk-64-2" type="checkbox"/><span>می‌توانم Cover، Contain و Aspect Ratio را توضیح بدهم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-64-3" name="chk-64-3" type="checkbox"/><span>می‌دانم SVG خودبه‌خود سبک و امن نیست.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-65">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-65-1" name="chk-65-1" type="checkbox"/><span>برای Logo Strip از Contain و max-size استفاده می‌کنم و Crop را رد می‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-65-2" name="chk-65-2" type="checkbox"/><span>برای Visual Stage فقط Aspect Ratio شروع را تنظیم می‌کنم و Nodeها را هنوز Position نمی‌کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-65-3" name="chk-65-3" type="checkbox"/><span>Alt/decorative decision را برای هر رسانه ثبت می‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-66">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-66-1" name="chk-66-1" type="checkbox"/><span>برای کارت محصول می‌توانم تصمیم بگیرم تصویر محصول Image Element باشد یا Background، و دلیل Accessibility/Performance آن را توضیح بدهم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-11-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-11-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا رسانه‌ها فقط نقش‌گذاری و قاب‌بندی شده‌اند؛ Position نهایی Nodeها هنوز انجام نشده است.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 11</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-11-completion">
<fieldset>
<legend>ثبت پایان درس 11</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-11-complete" name="lesson-11-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
