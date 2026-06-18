<article class="architecture-primer card-surface" data-core-primer="true" id="architecture-primer-v30">
<h2>از ساخت صفحه تا ساخت سیستم — معماری ذهنی Elementor V4</h2>
<p class="status-line"><code dir="ltr">evidence: verified_by_elementor_developer_docs + verified_by_official_elementor_help + derived_educational_model</code></p>
<section aria-labelledby="architecture-primer-core-title" class="lesson-section architecture-core">
<h3 id="architecture-primer-core-title">System First, Page Second</h3>
<p>در V4 فقط به این فکر نمی‌کنیم که «این Widget را چگونه زیبا کنم؟»؛ ابتدا تصمیم می‌گیریم کدام ارزش‌ها، Styleها و ساختارها باید در کل سایت رابطه و قابلیت استفادهٔ مجدد داشته باشند. این نگاه، <strong>CSS Thinking به‌جای Widget Thinking</strong>، <strong>Reuse Before Create</strong>، <strong>Relationship and Dependency Thinking</strong> و <strong>Scalability</strong> را به یک مسیر عملی تبدیل می‌کند.</p>
<div class="architecture-principles-grid">
<section><h4>تفکیک Content، Style و Structure</h4><p>Content داده و پیام است؛ Style declarationها و Stateها هستند؛ Structure رابطهٔ Elementها و الگوی تکرارشونده است. مخلوط‌کردن این سه، refactor و Responsive را پرهزینه می‌کند.</p></section>
<section><h4>Architecture Before Building</h4><p>پیش از ساخت، مرزهای design decision، کلاس‌های قابل استفادهٔ مجدد و ساختارهای واقعاً تکراری را مشخص کن؛ اما برای اکتشاف محلی نیز فضا بگذار.</p></section>
<section><h4>Reuse Before Create</h4><p>پیش از ساخت Style یا Component جدید، بررسی کن آیا Variable، Global Class یا Master موجود همان نیاز را پوشش می‌دهد.</p></section>
<section><h4>Scalability</h4><p>تصمیم خوب فقط امروز درست نیست؛ باید تغییر آینده، تیم، breakpointها و propagation را نیز قابل کنترل کند.</p></section>
</div>
</section>
<section aria-labelledby="v3-v4-thinking-title" class="lesson-section">
<h3 id="v3-v4-thinking-title">V3 Thinking در برابر V4 Thinking</h3>
<svg aria-labelledby="v3v4-svg-title v3v4-svg-desc" class="architecture-svg" role="img" viewbox="0 0 960 340">
<title id="v3v4-svg-title">مقایسهٔ مدل ذهنی V3 و V4</title>
<desc id="v3v4-svg-desc">در سمت راست مسیر پراکندهٔ تنظیم هر ویجت جداگانه و در سمت چپ مسیر سیستم‌محور ارزش‌ها، کلاس‌ها، ساختار و نمونه‌ها نمایش داده شده است.</desc>
<rect class="svg-panel svg-panel-risk" height="280" rx="24" width="440" x="20" y="30"></rect>
<rect class="svg-panel svg-panel-good" height="280" rx="24" width="440" x="500" y="30"></rect>
<text class="svg-heading" text-anchor="middle" x="240" y="72">V3 Thinking</text>
<text class="svg-heading" text-anchor="middle" x="720" y="72">V4 Thinking</text>
<g class="svg-node"><rect height="54" rx="12" width="130" x="70" y="105"></rect><text text-anchor="middle" x="135" y="138">Widget A</text></g>
<g class="svg-node"><rect height="54" rx="12" width="130" x="260" y="105"></rect><text text-anchor="middle" x="325" y="138">Widget B</text></g>
<g class="svg-node"><rect height="54" rx="12" width="130" x="70" y="205"></rect><text text-anchor="middle" x="135" y="238">Literal A</text></g>
<g class="svg-node"><rect height="54" rx="12" width="130" x="260" y="205"></rect><text text-anchor="middle" x="325" y="238">Literal B</text></g>
<path class="svg-arrow" d="M135 159V205M325 159V205"></path>
<g class="svg-node"><rect height="48" rx="12" width="130" x="555" y="94"></rect><text text-anchor="middle" x="620" y="124">Variables</text></g>
<g class="svg-node"><rect height="48" rx="12" width="130" x="755" y="94"></rect><text text-anchor="middle" x="820" y="124">Classes</text></g>
<g class="svg-node"><rect height="48" rx="12" width="130" x="555" y="205"></rect><text text-anchor="middle" x="620" y="235">Components</text></g>
<g class="svg-node"><rect height="48" rx="12" width="130" x="755" y="205"></rect><text text-anchor="middle" x="820" y="235">Pages</text></g>
<path class="svg-arrow" d="M685 118H755M820 142V205M755 229H685"></path>
</svg>
<p class="evidence-note"><code dir="ltr">derived_educational_model</code> — این مقایسه مدل آموزشی است، نه taxonomy رسمی محصول.</p>
</section>
<section aria-labelledby="design-dependency-title" class="lesson-section">
<h3 id="design-dependency-title">نمودار وابستگی Design System — نه CSS Cascade</h3>
<svg aria-labelledby="dependency-svg-title dependency-svg-desc" class="architecture-svg dependency-svg" role="img" viewbox="0 0 1080 230">
<title id="dependency-svg-title">وابستگی Design System در Elementor V4</title>
<desc id="dependency-svg-desc">Named values یا Variables وارد declarationهای Local یا Global Class می‌شوند، سپس Atomic Elements و ساختار قابل استفاده مجدد، Components، Instances و Pages از آن‌ها استفاده می‌کنند.</desc>
<g class="svg-node"><rect height="72" rx="14" width="155" x="20" y="75"></rect><text text-anchor="middle" x="98" y="104">Named values</text><text text-anchor="middle" x="98" y="130">Variables</text></g>
<g class="svg-node"><rect height="72" rx="14" width="170" x="205" y="75"></rect><text text-anchor="middle" x="290" y="102">Declarations in</text><text text-anchor="middle" x="290" y="128">Local / Global Classes</text></g>
<g class="svg-node"><rect height="102" rx="14" width="180" x="405" y="60"></rect><text text-anchor="middle" x="495" y="92">Atomic Elements</text><text text-anchor="middle" x="495" y="118">and reusable</text><text text-anchor="middle" x="495" y="144">structure</text></g>
<g class="svg-node"><rect height="72" rx="14" width="135" x="615" y="75"></rect><text text-anchor="middle" x="683" y="105">Components</text><text text-anchor="middle" x="683" y="131">Master</text></g>
<g class="svg-node"><rect height="72" rx="14" width="125" x="780" y="75"></rect><text text-anchor="middle" x="843" y="118">Instances</text></g>
<g class="svg-node"><rect height="72" rx="14" width="125" x="935" y="75"></rect><text text-anchor="middle" x="998" y="118">Pages</text></g>
<path class="svg-arrow" d="M175 111H205M375 111H405M585 111H615M750 111H780M905 111H935"></path>
<text class="svg-caption" text-anchor="middle" x="540" y="205">Dependency map — این زنجیره قانون اجباری یا ترتیب cascade نیست.</text>
</svg>
</section>
<section aria-labelledby="style-conflict-title" class="lesson-section">
<h3 id="style-conflict-title">نقشهٔ حل تعارض Style</h3>
<svg aria-labelledby="conflict-svg-title conflict-svg-desc" class="architecture-svg conflict-svg" role="img" viewbox="0 0 980 390">
<title id="conflict-svg-title">حل تعارض Style تا رسیدن به Computed Style</title>
<desc id="conflict-svg-desc">Global Class hierarchy، State انتخاب‌شده، Local Class و Custom CSS همراه context انتخابگر و cascade مرورگر به Computed Style می‌رسند.</desc>
<g class="svg-node"><rect height="62" rx="14" width="260" x="70" y="35"></rect><text text-anchor="middle" x="200" y="73">Global Class hierarchy</text></g>
<g class="svg-node"><rect height="62" rx="14" width="250" x="365" y="35"></rect><text text-anchor="middle" x="490" y="73">Selected State</text></g>
<g class="svg-node"><rect height="62" rx="14" width="260" x="650" y="35"></rect><text text-anchor="middle" x="780" y="73">Local Class</text></g>
<g class="svg-node"><rect height="72" rx="14" width="280" x="170" y="155"></rect><text text-anchor="middle" x="310" y="185">Custom CSS / matched rule</text><text text-anchor="middle" x="310" y="211">selector context</text></g>
<g class="svg-node"><rect height="72" rx="14" width="280" x="530" y="155"></rect><text text-anchor="middle" x="670" y="185">Browser CSS cascade</text><text text-anchor="middle" x="670" y="211">specificity / order / importance</text></g>
<g class="svg-node svg-winner"><rect height="68" rx="18" width="270" x="355" y="300"></rect><text text-anchor="middle" x="490" y="342">Computed Style</text></g>
<path class="svg-arrow" d="M200 97V128H310V155M490 97V265H490V300M780 97V128H670V155M310 227V265H490M670 227V265H490"></path>
</svg>
<p><code dir="ltr">verified_by_official_elementor_help</code> برای hierarchy کلاس‌ها و State؛ <code dir="ltr">verified_by_css_spec</code> برای cascade مرورگر و matched-rule context.</p>
</section>
<details class="lesson-disclosure architecture-workflows" id="architecture-workflows-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🧭 دو workflow معتبر: برنامه‌ریزی‌شده و اکتشافی</span></summary>
<section class="disclosure-content lesson-section">
<div class="workflow-grid">
<section><h4>Planned workflow</h4><ol><li>Design decisions</li><li>Variables</li><li>Global Classes</li><li>Components</li><li>Pages</li></ol><p><code dir="ltr">proposed_strategy</code> — برای تیم یا سیستم از قبل تعریف‌شده مناسب است.</p></section>
<section><h4>Discovery workflow</h4><ol><li>Element + Local styling</li><li>اثبات تکرار</li><li>Convert to Global Class</li><li>استخراج مقدارهای تکراری به Variable</li><li>Component فقط برای تکرار Structure</li></ol><p><code dir="ltr">proposed_strategy</code> — برای prototype و کشف تدریجی مناسب است.</p></section>
</div>
<p class="warning-box">هیچ‌یک تنها workflow صحیح نیست. تصمیم را با intent، دامنهٔ reuse، هزینهٔ propagation و قابلیت refactor بگیر.</p>
</section>
</details>
</article>
