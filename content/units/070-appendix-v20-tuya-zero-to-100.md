<article class="appendix card-surface" id="appendix-v20-tuya-zero-to-100">
<h2 class="former-h1">ضمیمهٔ نهایی نسخه 20 — TUYA از صفر تا صد</h2>
<section class="appendix-body">
<figure class="visual-figure tuya-reference-figure final-tuya-reference">
<img alt="تصویر مرجع نهایی پروژه TUYA برای بازسازی کامل در Elementor V4" loading="lazy" src="assets/images/tuya-reference.jpg"/>
<figcaption>مرجع نهایی: این تصویر را مثل نقشهٔ ساخت بخوان، نه مثل عکسی که باید کورکورانه کپی شود.</figcaption>
</figure>
<h2>۰. اول تصویر را مثل مهندس بخوان</h2>
<p>این سکشن از بیرون ساده به نظر می‌رسد، اما چند تصمیم مهم در آن پنهان است: سمت چپ یک ناحیهٔ Copy با متن، لیست و Logo Strip داریم؛ سمت راست یک Visual Stage داریم که تصویر خانه، ابر TUYA، مدار دایره‌ای و nodeهای شناور را با هم ترکیب می‌کند.</p>
<div aria-label="لایه‌های تصویر TUYA" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>لایه‌های تصویر TUYA</caption>
<thead><tr><th scope="col">لایه</th><th scope="col">در تصویر چیست؟</th><th scope="col">تصمیم Elementor V4</th></tr></thead>
<tbody>
<tr><th scope="row">Structure</th><td>سکشن اصلی، ستون متن، ستون Visual</td><td>در Normal Flow با ظرف والد/Flexbox یا Grid ساخته شود.</td></tr>
<tr><th scope="row">Content</th><td>متن معرفی، bulletها، لوگوها و عبارت TUYA</td><td>با Heading/Paragraph/List/Image یا SVG معنادار ساخته شود.</td></tr>
<tr><th scope="row">Overlap</th><td>ابر مرکزی، مدار و nodeهای اطراف</td><td>فقط داخل Visual Stage از Absolute استفاده شود.</td></tr>
<tr><th scope="row">Decoration</th><td>تصویر داخلی خانه، سایه‌ها، زمینه روشن و glow</td><td>با Background/Image، Shadow و opacity کنترل‌شده.</td></tr>
</tbody>
</table>
</div>
<h2>۱. درخت پیشنهادی Elementها</h2>
<p>قبل از Style دادن، Tree را بساز. اگر Tree درست نباشد، هر عددی که وارد کنی فقط یک وصلهٔ موقت است.</p>
<details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>Tree پیشنهادی برای بازسازی TUYA</figcaption><pre class="ascii-diagram" dir="ltr">Platform Section
└── Platform Shell
    ├── Copy Area
    │   ├── Intro Text
    │   ├── Feature List
    │   └── Logo Strip
    └── Visual Stage
        ├── Home Image Layer
        ├── Orbit Ring
        ├── Core Cloud
        └── Icon Node × 6</pre></figure></details>
<p><strong>حکم استاد:</strong> ستون‌های اصلی را Absolute نکن. Absolute فقط برای nodeهایی مجاز است که واقعاً روی Visual Stage شناورند.</p>
<h2>۲. Class System را قبل از جزئیات بساز</h2>
<p>در این طرح، چند الگو تکرار می‌شوند؛ پس اگر همه‌چیز را Local Class کنی، بعداً با کابوس ویرایش روبه‌رو می‌شوی.</p>
<div aria-label="کلاس‌های پیشنهادی TUYA" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>کلاس‌های پیشنهادی TUYA</caption>
<thead><tr><th scope="col">نام پیشنهادی</th><th scope="col">مسئولیت</th><th scope="col">چرا Global؟</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">platform-section</code></th><td>پوستهٔ کلی سکشن</td><td>الگوی سکشن‌های مشابه سایت را قابل تکرار می‌کند.</td></tr>
<tr><th scope="row"><code dir="ltr">platform-shell</code></th><td>عرض، padding و چیدمان دو ناحیه</td><td>تعریف یکپارچهٔ layout می‌سازد.</td></tr>
<tr><th scope="row"><code dir="ltr">platform-copy</code></th><td>عرض و فاصلهٔ متن و لوگوها</td><td>Copy Area در صفحات دیگر هم قابل تکرار است.</td></tr>
<tr><th scope="row"><code dir="ltr">platform-logo-frame</code></th><td>قاب یکنواخت هر لوگو</td><td>Logo Strip چند آیتم هم‌شکل دارد.</td></tr>
<tr><th scope="row"><code dir="ltr">tuya-orbit-node</code></th><td>ظاهر nodeهای دایره‌ای</td><td>۶ node با ظاهر مشترک داریم؛ فقط موقعیتشان Local یا modifier است.</td></tr>
<tr><th scope="row"><code dir="ltr">tuya-core-cloud</code></th><td>ابر مرکزی TUYA</td><td>ظاهر مرکزی مشخص و قابل نگهداری می‌شود.</td></tr>
</tbody>
</table>
</div>
<h2>۳. Variableها را مثل مواد خام تعریف کن</h2>
<p>Variable یعنی مقدار مشترک؛ Global Class یعنی بستهٔ Style. برای این تصویر، Variableهای زیر به ذهن طراحی نظم می‌دهند.</p>
<ul>
<li><code dir="ltr">color-panel-bg</code> برای زمینهٔ روشن سمت چپ.</li>
<li><code dir="ltr">color-tuya-orange</code> برای ابر و تأکید TUYA.</li>
<li><code dir="ltr">radius-section</code> برای گردی پوسته.</li>
<li><code dir="ltr">space-section-x</code> و <code dir="ltr">space-section-y</code> برای padding سکشن.</li>
<li><code dir="ltr">shadow-soft</code> برای nodeها و لایه‌های شناور.</li>
</ul>
<h2>۴. واحدها: کجا px، کجا %، کجا viewport؟</h2>
<p>این تصویر وسوسه می‌کند که همه چیز را با عددهای دقیق بسازی، اما طراحی مقاوم یعنی انتخاب واحد براساس نقش.</p>
<div aria-label="واحدهای پیشنهادی TUYA" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>واحدهای پیشنهادی TUYA</caption>
<thead><tr><th scope="col">بخش</th><th scope="col">واحد بهتر</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">عرض Shell</th><td><code dir="ltr">max-width</code> + <code dir="ltr">%</code></td><td>صفحه روی مانیتورهای مختلف کنترل می‌شود.</td></tr>
<tr><th scope="row">فاصله داخلی سکشن</th><td><code dir="ltr">clamp()</code> یا Size Variable</td><td>فاصله با viewport نرم تغییر می‌کند.</td></tr>
<tr><th scope="row">دو ستون اصلی</th><td>Flex/Grid + سهم نسبی</td><td>والد، نه viewport، منبع اندازه‌گیری باشد.</td></tr>
<tr><th scope="row">Visual Stage</th><td><code dir="ltr">aspect-ratio</code> یا <code dir="ltr">min-height</code></td><td>ارتفاع بدون قفل شدن به viewport کنترل می‌شود.</td></tr>
<tr><th scope="row">Nodeهای اطراف</th><td><code dir="ltr">%</code> داخل Stage</td><td>موقعیت نسبت به همان صحنه حفظ می‌شود.</td></tr>
</tbody>
</table>
</div>
<h2>۵. ترتیب ساخت در Elementor V4</h2>
<ol>
<li>یک ظرف والد اصلی برای سکشن بساز و فقط مسئول پوسته و background باشد.</li>
<li>داخل آن یک Shell بساز که دو ناحیهٔ Copy و Visual را نگه دارد.</li>
<li>Copy Area را با Heading/Paragraph/List و Logo Strip بساز؛ فاصلهٔ بین لوگوها با Gap باشد، نه Margin تکی.</li>
<li>Visual Stage را به‌عنوان صحنهٔ کنترل‌شده بساز؛ تصویر خانه، ring، cloud و nodeها داخل همین صحنه باشند.</li>
<li>برای nodeها یک Global Class مشترک بده و فقط موقعیت هر node را جداگانه تنظیم کن.</li>
<li>روی Mobile اول چیدمان دو ستون را stack کن؛ بعد اندازهٔ Stage و Logo Strip را تنظیم کن.</li>
</ol>
<h2>۶. Responsive، RTL و Accessibility</h2>
<p>در Mobile، هدف حفظ تصویر Screenshot نیست؛ هدف حفظ معناست. Copy باید خوانا بماند، Logoها باید wrap شوند، و Visual نباید overflow افقی بسازد. در RTL، از Start/End فکر کن نه Left/Right؛ متن و لیست باید طبیعی باشند اما تصویر خانه و مدار TUYA لازم نیست الزاماً آینه شوند.</p>
<p>اگر لوگوها تصویرند، alt مناسب بده. اگر فقط تزئینی‌اند، decorative handling لازم است. اگر nodeها آیکون‌های اطلاعاتی هستند، باید نام یا توضیح قابل فهم داشته باشند؛ اگر تزئینی‌اند، نباید مزاحم screen reader شوند.</p>
<h2>۷. Audit وزن قبل از تحویل</h2>
<ul>
<li>آیا Empty Flexbox فقط برای فاصله‌سازی داریم؟ اگر بله، Gap/Padding را بررسی کن.</li>
<li>آیا ۶ node با ۶ Local Class تکراری ساخته شده‌اند؟ اگر بله، Global Class لازم است.</li>
<li>آیا از <code dir="ltr">vw</code> برای چیزی استفاده شده که باید نسبت به parent باشد؟ اگر بله، احتمال overflow را بررسی کن.</li>
<li>آیا تصویر خانه بیش از حد بزرگ یا بدون lazy-loading است؟ Asset Weight را بررسی کن.</li>
<li>آیا Shadow/Blur/Filter زیاد است؟ Paint Weight را کنترل کن.</li>
</ul>
<h2>۸. چک‌لیست صفر تا صد</h2>
<form class="interactive-form checklist-form" data-persist-group="tuya-v20-zero-to-100">
<fieldset>
<legend>چک‌لیست بازسازی TUYA</legend>
<label class="choice-row"><input data-persist="checkbox" id="tuya-v20-1" name="tuya-v20-1" type="checkbox"/><span>چهار لایهٔ Structure، Content، Overlap و Decoration را مشخص کردم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="tuya-v20-2" name="tuya-v20-2" type="checkbox"/><span>ستون‌های اصلی در Normal Flow هستند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="tuya-v20-3" name="tuya-v20-3" type="checkbox"/><span>Absolute فقط داخل Visual Stage استفاده شده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="tuya-v20-4" name="tuya-v20-4" type="checkbox"/><span>Global Classها برای الگوهای تکراری ساخته شده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="tuya-v20-5" name="tuya-v20-5" type="checkbox"/><span>Variableها برای رنگ، فاصله، radius و shadowهای مشترک تعریف شده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="tuya-v20-6" name="tuya-v20-6" type="checkbox"/><span>Mobile، RTL، Zoom 200% و عدم overflow افقی بررسی شده‌اند.</span></label>
</fieldset>
</form>
<p class="golden-rule"><strong>قانون طلایی:</strong> TUYA را با چشم Screenshot نساز؛ با ذهن Structure بساز. هر چیزی که معنی دارد در Flow بماند، هر چیزی که شناور است فقط داخل Stage شناور شود، و هر Style تکراری به Global Class تبدیل شود.</p>
</section>
<section aria-labelledby="reza-tuya-margin-heading-appendix" class="lesson-section real-reza-experiment">
<h2 id="reza-tuya-margin-heading-appendix">🧪 آزمایش واقعی رضا — مشکل <span dir="ltr">margin-inline-start/end</span> در TUYA</h2>
<ol class="case-steps">
<li><strong>چیزی که رضا دید:</strong> برای سکشن TUYA کد زیر را گذاشت، اما سمت راست از لبه فاصلهٔ واضح نگرفت.</li>
<li><strong>حدس اشتباه مبتدی:</strong> «در RTL، margin-inline-start کار نمی‌کند.»</li>
<li><strong>قانون CSS / Elementor V4:</strong> در RTL معمولاً <code dir="ltr">margin-inline-start</code> به سمت راست و <code dir="ltr">margin-inline-end</code> به سمت چپ نگاشت می‌شود؛ اما این نگاشت به <code dir="ltr">direction</code> و <code dir="ltr">writing-mode</code> وابسته است. اگر خود عنصر <code dir="ltr">width: 100%</code> یا stretch باشد، <code dir="ltr">100% + 80px + 80px</code> می‌تواند overflow بسازد و یک سمت چسبیده به نظر برسد.</li>
<li><strong>در پنل Elementor کجا چک کنم؟</strong> Advanced / Spacing برای Margin و Padding، Layout برای Width/Full Width، و Direction والد/صفحه را بررسی کن.</li>
<li><strong>در DevTools / Computed Style کجا چک کنم؟</strong> Box Model، Computed <code dir="ltr">direction</code>، <code dir="ltr">writing-mode</code>، <code dir="ltr">width</code>، <code dir="ltr">margin-inline-start</code> و <code dir="ltr">margin-inline-end</code> را ببین.</li>
<li><strong>راه‌حل درست:</strong> اگر هدف فاصلهٔ داخلی است، <code dir="ltr">padding-inline</code> بده. اگر هدف آوردن کل جعبه به داخل صفحه است، padding را روی parent/shell بده یا برای خود Main از عرض محاسبه‌شده/Max Width همراه با <code dir="ltr">margin-inline: auto</code> استفاده کن.</li>
<li><strong>قانون طلایی:</strong> Margin جعبه را از بیرون دور می‌کند؛ Padding محتوای داخل جعبه را دور می‌کند. اگر جعبه خودش 100٪ عرض دارد، margin دوطرفه ممکن است overflow بسازد.</li>
</ol>
<pre class="code-block" dir="ltr"><code>.elementor .e-e3036d8 {
  height: 40vh;
  margin-inline-start: 80px;
  margin-inline-end: 80px;
  background-color: var(--solidf1);
  flex-direction: row;
  row-gap: 16px;
  border-radius: var(--border_radios);
}</code></pre>
<div class="code-pair-grid">
<section aria-labelledby="tuya-fix-padding-heading-appendix" class="code-fix-card"><h3 id="tuya-fix-padding-heading-appendix">وقتی هدف فاصلهٔ صفحه است</h3><pre class="code-block" dir="ltr"><code>.platform-section {
  padding-inline: 80px;
}

.platform-main {
  width: 100%;
}</code></pre></section>
<section aria-labelledby="tuya-fix-width-heading-appendix" class="code-fix-card"><h3 id="tuya-fix-width-heading-appendix">وقتی هدف جعبهٔ محدود و وسط‌چین است</h3><pre class="code-block" dir="ltr"><code>.platform-main {
  width: min(100% - 160px, 1200px);
  margin-inline: auto;
}</code></pre></section>
</div>
<p><strong>برای TUYA:</strong> معمولاً Section/Shell بیرونی padding صفحه را کنترل می‌کند؛ Platform Main داخل آن می‌نشیند؛ Copy و Visual فرزندان Main هستند.</p>
<p><strong>برای قطعیت، Computed Style و Box Model را بررسی کن.</strong></p>
<details class="more-know">
<summary>بیشتر بدانید</summary>
<p>Logical properties برای RTL مهم‌اند چون به جای چپ/راست فیزیکی، از start/end منطقی استفاده می‌کنند. با این حال، اگر width، overflow یا parent اشتباه باشد، logical margin هم خروجی درست نمی‌سازد.</p>
</details>
</section></article>
