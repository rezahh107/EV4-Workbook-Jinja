<article class="lesson card-surface" data-trackable="lesson-v17-interactions" id="lesson-v17-interactions">
<h2 class="former-h1">تکمیلی 18E — Interactions، State و Motion</h2>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🧭 قطب‌نمای درس</span></summary><section class="disclosure-content lesson-section">
<p><strong>هدف:</strong> Hover State را با Interaction قاطی نکنی. State یعنی ظاهر عنصر در یک وضعیت؛ Interaction یعنی رفتاری که با Trigger شروع می‌شود.</p>
</section></details>
<section class="lesson-section lesson-core-concept" data-core-concept="true">
<h2>A. فرق State و Interaction با مثال ساده</h2>
<p>وقتی موس روی Button می‌رود و رنگ Button کمی تغییر می‌کند، این معمولاً State است. اما وقتی Section با Scroll کم‌کم Fade می‌شود، یا با کلیک چیزی باز و بسته می‌شود، وارد دنیای Interaction شده‌ای.</p>
<table><caption>جدول آموزشی دوره — A. فرق State و Interaction با مثال ساده</caption><thead><tr><th scope="col">موضوع</th><th scope="col">State</th><th scope="col">Interaction</th></tr></thead><tbody>
<tr><td>سؤال اصلی</td><td>در این وضعیت چه شکلی باشد؟</td><td>با چه Trigger و چه حرکتی واکنش بدهد؟</td></tr>
<tr><td>مثال</td><td>Hover، Focus، Active</td><td>Page load، Scroll into view، While scrolling، Click</td></tr>
<tr><td>ریسک</td><td>Focus حذف شود و accessibility خراب شود</td><td>حرکت زیاد، کندی، حواس‌پرتی یا motion sickness</td></tr>
</tbody></table>
</section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="7439ea35b5857a3ff14735cbabe22960ee4d5e35a8a25839e96e53af1da90d0b" id="lesson-v17-interactions-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Interactions؛ Trigger، Effect و زمان‌بندی</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="20" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-20-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-20-section-01">مسئله‌ای که Interaction حل می‌کند</h3><p>Interaction می‌گوید وقتی رویدادی رخ داد، Element چگونه واکنش نشان دهد.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">رویداد → واکنش
</code></pre></figure><p>بدون این تفکیک، Animationها به حرکت‌های تزئینی پراکنده تبدیل می‌شوند و معلوم نیست چرا، چه زمانی و برای چه کاربری اجرا می‌شوند.</p><hr/></section><section aria-labelledby="concept-v31-20-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-20-section-02">تشبیه به دنیای واقعی: زنگ، حسگر و موتور</h3><p>یک در اتوماتیک را تصور کن:</p><ul>
<li>Trigger = حسگر حضور</li>
<li>Effect = بازشدن در</li>
<li>Duration = مدت بازشدن</li>
<li>Delay = فاصله میان تشخیص و شروع</li>
<li>Direction = مسیر حرکت</li>
<li>Repeat/Timeline = الگوی تکرار یا پیشرفت</li>
</ul><p>اگر حسگر اشتباه باشد، بهترین موتور هم در زمان نادرست کار می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-20-section-03" class="concept-reference-part"><h3 id="concept-v31-20-section-03">Trigger چیست؟</h3><p>Trigger لحظهٔ آغاز است. در Interactions رسمی Elementor نمونه‌هایی مانند این‌ها وجود دارند:</p><ul>
<li>Page Load</li>
<li>Scroll Into View</li>
<li>While Scrolling</li>
<li>Hover</li>
<li>Click</li>
</ul><p>هر Trigger پیامد متفاوتی دارد.</p><p>Page Load بدون قصد کاربر اجرا می‌شود. Click به تصمیم کاربر وابسته است. While Scrolling ممکن است بار محاسباتی بیشتری ایجاد کند.</p><hr/></section><section aria-labelledby="concept-v31-20-section-04" class="concept-reference-part"><h3 id="concept-v31-20-section-04">Effect چیست؟</h3><p>Effect تغییر دیداری است:</p><ul>
<li>Fade</li>
<li>Slide</li>
<li>Scale</li>
<li>Transformهای دیگر</li>
</ul><p>Effect باید معنای تجربه را پشتیبانی کند. اگر محتوای اصلی فقط پس از Animation قابل فهم است، Progressive Enhancement ضعیف شده است.</p><hr/></section><section aria-labelledby="concept-v31-20-section-05" class="concept-reference-part"><h3 id="concept-v31-20-section-05">Duration و Delay</h3><p>Duration طول حرکت است. Delay زمان انتظار پیش از شروع.</p><p>Animation بسیار کند، رابط را سنگین می‌کند. Animation بسیار سریع ممکن است دیده نشود. Delay زیاد برای محتوای اصلی حس خرابی می‌دهد.</p><p>به‌جای عدد جادویی، از نقش حرکت شروع کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Micro feedback: کوتاه
Entrance support: متوسط و محدود
Storytelling sequence: با احتیاط و تست
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-20-section-06" class="concept-reference-part"><h3 id="concept-v31-20-section-06">Interactions و Deviceها</h3><p>مستندات رسمی فعلی می‌گویند Interactions روی تمام Deviceها اعمال می‌شوند و برای Screen Sizeهای مختلف قابل شخصی‌سازی نیستند.</p><p>پس Interactionی که در Desktop خوب است باید روی Touch، Mobile و دستگاه کم‌توان نیز آزمایش شود.</p><p>Hover Trigger روی Touch مفهوم متفاوت یا محدود دارد. طراحی نباید اطلاعات حیاتی را به Hover وابسته کند.</p><hr/></section><section aria-labelledby="concept-v31-20-section-07" class="concept-reference-part"><h3 id="concept-v31-20-section-07">Reduced Motion</h3><p>بعضی کاربران حرکت کمتر را در سیستم درخواست می‌کنند.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-css inline-code" dir="ltr">@media (prefers-reduced-motion: reduce) {
  /* حرکت را حذف یا بسیار محدود کن */
}
</code></pre></figure><p>اگر کنترل Native Interaction این Preference را پوشش نمی‌دهد، باید رفتار واقعی نسخه هدف بررسی و در صورت نیاز راهکار مکمل طراحی شود.</p><hr/></section><section aria-labelledby="concept-v31-20-section-08" class="concept-reference-part"><h3 id="concept-v31-20-section-08">INP و Main Thread</h3><p>Interaction سنگین می‌تواند پاسخ کلیک را عقب بیندازد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Click
↓
JavaScript طولانی
↓
Style recalculation
↓
Layout
↓
Paint
↓
Next frame دیر نمایش داده می‌شود
</code></pre></figure><p>INP فقط مدت Animation نیست؛ تأخیر از ورودی تا Paint بعدی را می‌سنجد. تعداد زیاد Handlerها، DOM بزرگ و Layout Thrashing می‌توانند پاسخ را کند کنند.</p><hr/></section><section aria-labelledby="concept-v31-20-section-09" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-20-section-09">در Elementor V4</h3><p>برای هر Interaction یک قرارداد بنویس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Element: Pricing Card
Trigger: Click
Effect: Expand details
Purpose: reveal optional information
Fallback: content accessible without motion
Duration: 200ms
Reduced motion: no transform
</code></pre></figure><p>از Animation به‌عنوان ادویه استفاده کن، نه غذای اصلی.</p><hr/></section><section aria-labelledby="concept-v31-20-section-10" class="concept-reference-part"><h3 id="concept-v31-20-section-10">چند Interaction روی یک Element</h3><p>وقتی چند Interaction ترکیب می‌شوند، ترتیب و تعارض مهم است:</p><ul>
<li>Hover Scale</li>
<li>Click Slide</li>
<li>Scroll Fade</li>
</ul><p>همه ممکن است Transform را تغییر دهند و روی یکدیگر سایه بیندازند. منبع Transform نهایی را در Computed Style و Timeline بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-20-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-20-section-11">اشتباهات رایج</h3><ul>
<li>Animation برای هر Element</li>
<li>Page Load Animation روی محتوای حیاتی</li>
<li>Hover-only behavior</li>
<li>Delay طولانی</li>
<li>Transformهای متعارض</li>
<li>نادیده‌گرفتن Reduced Motion</li>
<li>فرض Device-specific بودن Interactions</li>
<li>اندازه‌گیری نکردن INP و Long Task</li>
<li>استفاده از Animation برای پنهان‌کردن Layout Shift</li>
</ul><hr/></section><section aria-labelledby="concept-v31-20-section-12" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-20-section-12">پل به DevTools</h3><p>در Performance Panel یک Interaction ضبط کن. این موارد را ببین:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Event timing
Long tasks
Style recalculation
Layout
Paint
Frames
</code></pre></figure><p>در Elements Panel نیز Transform و Transition نهایی را بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-20-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-20-section-13">تصویر ذهنی نهایی</h3><p>Interaction مثل در اتوماتیک است. Trigger حسگر است و Effect موتور. اگر هرکس از جلوی ساختمان رد شد ده موتور هم‌زمان روشن شوند، مشکل از زیبایی در نیست؛ از معماری واکنش است.</p><hr/></section><section aria-labelledby="concept-v31-20-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-20-section-14">قوانین طلایی</h3><ul>
<li><strong>«Trigger می‌گوید چه وقت؛ Effect می‌گوید چه تغییر کند.»</strong></li>
<li><strong>«Animation ادویه است، نه غذای اصلی.»</strong></li>
<li><strong>«محتوا بدون حرکت نیز باید قابل فهم و قابل دسترسی باشد.»</strong></li>
<li><strong>«Interaction را روی Mobile، Touch و Reduced Motion آزمایش کن.»</strong></li>
<li><strong>«حرکت زیبا اگر پاسخ کلیک را کند کند، تجربه خوب نیست.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Interactions</li>
<li>Elementor Developers: Editor 4.0 interactions update</li>
<li>web.dev: Interaction to Next Paint guidance</li>
<li>CSS prefers-reduced-motion</li>
</ul><hr/></footer></div></details><section aria-labelledby="interactions-lab-title" class="lesson-section v30-core-lab" id="interactions-lab-v30">
<h2 id="interactions-lab-title">Interactions Lab — Trigger، Effect و Timing</h2>
<p class="status-line"><code dir="ltr">verified_by_official_elementor_help</code> برای رفتار محصول؛ <code dir="ltr">proposed_strategy</code> برای performance و accessibility guidance.</p>
<div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table">
<caption>ماتریس رسمی Interaction</caption><thead><tr><th scope="col">بعد</th><th scope="col">گزینه‌ها</th><th scope="col">معنا</th></tr></thead>
<tbody>
<tr><th scope="row">Trigger</th><td>Page Load، Scroll Into View، While Scrolling، On Hover، On Click</td><td>چه زمانی Interaction آغاز می‌شود</td></tr>
<tr><th scope="row">Effect</th><td>Fade، Slide، Scale</td><td>نوع تغییر بصری</td></tr>
<tr><th scope="row">Type</th><td>In، Out</td><td>ورود/ظاهرشدن یا خروج/ناپدیدشدن</td></tr>
<tr><th scope="row">Direction</th><td>Up، Down، Left، Right</td><td>جهت effect</td></tr>
<tr><th scope="row">Duration</th><td>milliseconds (MS)</td><td>مدت کامل‌شدن</td></tr>
<tr><th scope="row">Delay</th><td>milliseconds (MS)</td><td>فاصلهٔ trigger تا شروع</td></tr>
<tr><th scope="row">Multiple</th><td>چند Interaction روی یک Element</td><td>ترکیب effectها با دکمهٔ +</td></tr>
</tbody></table></div>
<h3>چهار مفهوم را قاطی نکن</h3>
<div class="interaction-concept-grid">
<section><h4>State</h4><p>ظاهر Class در contextی مثل Hover؛ بخشی از Style hierarchy.</p></section>
<section><h4>CSS Transition</h4><p>نحوهٔ interpolate شدن تغییر property در CSS؛ رفتار استاندارد وب.</p></section>
<section><h4>Interaction</h4><p>سیستم trigger/effect رسمی V4 در تب Interactions.</p></section>
<section><h4>Legacy Motion Effects</h4><p>قابلیت قدیمی‌تر اکوسیستم Elementor؛ با Interaction جدید یکی نیست.</p></section>
</div>
<h3>Lab: Hero reveal کنترل‌شده</h3><ol><li>Image Atomic را انتخاب کن.</li><li>Page Load + Slide + In + Down + 600ms + 0ms.</li><li>Interaction دوم: Page Load + Fade + In + 600ms + 120ms.</li><li>یک نسخهٔ On Hover یا On Click را فقط برای عنصر تعاملی مناسب آزمایش کن.</li><li>While Scrolling را با start/end مشخص و روی دستگاه ضعیف تست کن.</li></ol>
<aside class="warning-box"><strong>Performance / reduced motion:</strong> حرکت را محدود، کوتاه و معنادار نگه دار؛ محتوای حیاتی را به motion وابسته نکن و preference کاهش حرکت را در پیاده‌سازی frontend رعایت کن. این‌ها راهنمای عمومی accessibility و performance هستند، نه ادعای یک کنترل مستقل رسمی مگر مستند شود.</aside>
</section><details class="lesson-disclosure settings-values-units" id="lesson-v17-interactions-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-v17-interactions-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Interactions؛ Duration و Delay زمان‌اند، Distance طول</span></summary>
<section aria-labelledby="lesson-v17-interactions-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Interaction ترکیبی از Trigger، Effect و پارامترهاست. Duration و Delay با ms سنجیده می‌شوند؛ Direction keyword و فاصلهٔ حرکت در صورت وجود طول است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> کارگردان می‌گوید چه زمانی شروع شود، از کدام جهت بیاید و حرکت چقدر طول بکشد.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Duration</th><td><code dir="ltr">interaction duration</code></td><td>MS در Help Center</td><td>زمان</td><td>برای سرعت اثر.</td><td>1500ms یعنی 1.5s، نه 1500px.</td><td><code dir="ltr">E_INTERACTIONS</code></td></tr><tr><th scope="row">Delay</th><td><code dir="ltr">interaction delay</code></td><td>MS</td><td>زمان</td><td>برای شروع با فاصله.</td><td>Delay زیاد پاسخ‌گویی را کم می‌کند.</td><td><code dir="ltr">E_INTERACTIONS</code></td></tr><tr><th scope="row">Direction</th><td><code dir="ltr">effect direction</code></td><td>Top/Bottom/…</td><td>keyword</td><td>جهت ورود/حرکت.</td><td>در RTL جهت بصری را جدا تست کن.</td><td><code dir="ltr">E_INTERACTIONS</code></td></tr><tr><th scope="row">Distance / transform</th><td><code dir="ltr">translate</code></td><td>طول یا درصد در CSS</td><td>Element/viewport</td><td>برای دامنهٔ حرکت در CSS.</td><td>بدون reduced-motion استفاده نکن.</td><td><code dir="ltr">CSS_TRANSFORM</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>Duration=1500ms و Delay=300ms → شروع پس از 0.3s و پایان تقریبی در 1.8s، اگر effect یک‌مرحله‌ای باشد.</p></section>
<section><h3>📱 در Responsive</h3><p>Motion را روی Mobile و reduced-motion بررسی کن؛ مسیر طولانی روی صفحهٔ کوچک می‌تواند نامناسب باشد.</p></section>
<section><h3>🔬 در DevTools</h3><p>Timing، transform و class/state فعال را با Performance/Computed بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/interactions/" rel="noopener noreferrer" target="_blank">Elementor V4 — Interactions</a>، <a href="https://www.w3.org/TR/css-values-4/#time" rel="noopener noreferrer" target="_blank">W3C — CSS Values time data type</a>، <a href="https://www.w3.org/TR/css-transforms-1/" rel="noopener noreferrer" target="_blank">W3C — CSS Transforms</a></footer>
</section>
</details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">B. قانون حرکت کم، معنا زیاد</span></summary><section class="disclosure-content lesson-section">
<p>Interaction خوب مثل راهنماست، نه آتش‌بازی. اگر حرکت فقط برای هیجان است، حذفش کن. اگر حرکت به کاربر می‌گوید «این بخش وارد شد»، «این دکمه قابل کلیک است» یا «این محتوا به این اسکرول مرتبط است»، ارزش دارد.</p>
<div class="callout"><strong>قانون استاد:</strong> هر Interaction باید یک جملهٔ دفاع داشته باشد: «این حرکت به کاربر کمک می‌کند چون ...». اگر جمله نداری، حرکت احتمالاً تزئین اضافه است.</div>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">C. تمرین روی ForLesson</span></summary><section class="disclosure-content lesson-section">
<ol><li>یک کارت یا CTA انتخاب کن.</li><li>فقط یک Interaction سبک انتخاب کن.</li><li>Duration و Delay را کم نگه دار.</li><li>در موبایل و با Scroll سریع تست کن.</li><li>بررسی کن بدون Interaction هم محتوا قابل فهم است یا نه.</li></ol>
</section></details>
<details class="lesson-disclosure" id="lesson-v17-interactions-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Effects، State و Interactions</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Effects در برابر Interactions</h3><p>Effect بخشی از ظاهر است؛ Interaction سناریوی رفتاری مبتنی بر trigger است. Shadow یا blur همیشه‌فعال یک Effect است؛ حرکت با scroll یا click یک Interaction است.</p></section>
<section class="inline-compare-card"><h3>State در برابر Motion</h3><p>State وضعیت ظاهری است؛ Motion تغییر در زمان. اگر فقط رنگ hover عوض می‌شود، State. اگر عنصر حرکت می‌کند یا با scroll واکنش می‌دهد، Interaction.</p></section>
</div>
</section></details>
</article>
