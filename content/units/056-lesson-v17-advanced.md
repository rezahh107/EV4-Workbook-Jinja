<article class="lesson card-surface" data-trackable="lesson-v17-advanced" id="lesson-v17-advanced">
<h2 class="former-h1">تکمیلی 18F — Custom CSS، Attributes و Dynamic Tags در V4</h2>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🧭 قطب‌نمای درس</span></summary><section class="disclosure-content lesson-section">
<p><strong>هدف:</strong> سه ابزار پیشرفته را از هم جدا کنی: Custom CSS برای رفتاری که UI پوشش نمی‌دهد، Attributes برای معنا و اتصال فنی، Dynamic Tags برای محتوای زنده.</p>
</section></details>
<section class="lesson-section lesson-core-concept" data-core-concept="true">
<h2>A. Custom CSS آخرین راه تمیز است، نه اولین میان‌بر</h2>
<p>اگر Elementor UI همان کار را تمیز انجام می‌دهد، اول از UI استفاده کن. Custom CSS وقتی خوب است که واقعاً یک رفتار خاص، selector دقیق، یا حالت responsive/state پیچیده لازم داری. در V4 باید همیشه بپرسی CSS را روی کدام Class می‌نویسم؟ اگر CSS را بی‌نام و بی‌نقشه بنویسی، بعداً خودت هم نمی‌فهمی چرا آنجا بوده.</p>
<p><strong>فرمول تصمیم:</strong> UI → Global Class → Variable → Custom CSS. از راست به چپ برنگرد مگر دلیل داشته باشی.</p>
</section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="e23c4b55e302f72ef8df06f86d1060ff19b52d1d133cf1fce365966670fd5098" id="lesson-v17-advanced-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Custom CSS، Attributes و Dynamic Data؛ سه لایهٔ متفاوت</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="19" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-19-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-19-section-01">مسئله‌ای که این فصل حل می‌کند</h3><p>سه ابزار زیر گاهی کنار هم دیده می‌شوند، اما مسئولیت یکسانی ندارند:</p><ul>
<li>Custom CSS ظاهر و رفتار CSS را تعریف می‌کند.</li>
<li>HTML Attribute اطلاعات و معنا به Markup می‌افزاید.</li>
<li>Dynamic Tag مقدار را از دادهٔ سایت می‌آورد.</li>
</ul><p>اگر این سه را مخلوط کنی، ممکن است Style را داخل داده، رفتار را داخل Class نامناسب یا محتوای پویا را در HTML ثابت پنهان کنی.</p><hr/></section><section aria-labelledby="concept-v31-19-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-19-section-02">تشبیه به دنیای واقعی: لباس، برچسب هویت و پرونده</h3><p>یک کارمند را تصور کن:</p><ul>
<li>لباس و ظاهر او = CSS</li>
<li>کارت شناسایی و مشخصات روی آن = Attribute</li>
<li>اطلاعاتی که از پایگاه داده شرکت می‌آید = Dynamic Data</li>
</ul><p>لباس نمی‌گوید شماره پرسنلی چیست. کارت شناسایی رنگ کت را تعیین نمی‌کند. پرونده نیز جای طراحی لباس نیست.</p><hr/></section><section aria-labelledby="concept-v31-19-section-03" class="concept-reference-part"><h3 id="concept-v31-19-section-03">Custom CSS</h3><p>Custom CSS وقتی لازم است که کنترل بصری پنل کافی نیست یا یک رفتار استاندارد CSS پیشرفته می‌خواهی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">text-wrap: balance;
container-type: inline-size;
</code></pre></figure><p>در V4، Custom CSS می‌تواند به Class، State و Device مرتبط باشد. پس قبل از نوشتن کد، Class فعال را بررسی کن.</p><p>Custom CSS نباید اولین واکنش به هر مشکل باشد. اگر Layout با Flex/Grid Control قابل حل است، CSS اضافی ممکن است منبع دوم حقیقت بسازد.</p><hr/></section><section aria-labelledby="concept-v31-19-section-04" class="concept-reference-part"><h3 id="concept-v31-19-section-04">Attributes</h3><p>Attribute بخشی از HTML است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-html inline-code" dir="ltr">&lt;button aria-expanded="false" data-panel="pricing"&gt;
</code></pre></figure><p>کاربردها:</p><ul>
<li><code class="inline-code" dir="ltr">id</code></li>
<li><code class="inline-code" dir="ltr">data-*</code></li>
<li><code class="inline-code" dir="ltr">aria-*</code></li>
<li><code class="inline-code" dir="ltr">rel</code></li>
<li><code class="inline-code" dir="ltr">target</code></li>
<li>Hook برای JavaScript یا Testing</li>
</ul><p>Attribute باید معنای درست و مقدار معتبر داشته باشد. افزودن ARIA اشتباه می‌تواند Accessibility را بدتر کند.</p><p>قانون:</p><blockquote>
<p>ARIA جای Element معنایی بومی را نمی‌گیرد.</p>
</blockquote><p>اگر Button لازم است، Div با <code class="inline-code" dir="ltr">role="button"</code> راه‌حل اول نیست.</p><hr/></section><section aria-labelledby="concept-v31-19-section-05" class="concept-reference-part"><h3 id="concept-v31-19-section-05">Dynamic Tag</h3><p>Dynamic Tag مقدار را از Context می‌آورد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Post Title
Product Price
Featured Image
Author Name
Custom Field
Site URL
</code></pre></figure><p>همان Template در صفحه‌های مختلف مقدار متفاوت می‌گیرد.</p><p>Dynamic Data یعنی Layout باید برای ناشناخته‌ها آماده باشد:</p><ul>
<li>مقدار خالی</li>
<li>متن کوتاه</li>
<li>متن بسیار بلند</li>
<li>تصویر ناموجود</li>
<li>قیمت چندخطی</li>
<li>URL طولانی</li>
</ul><hr/></section><section aria-labelledby="concept-v31-19-section-06" class="concept-reference-part"><h3 id="concept-v31-19-section-06">Dynamic Data و معماری Empty State</h3><p><code class="inline-code" dir="ltr">empty-cells</code> راه‌حل Grid یا Flex برای داده خالی نیست؛ این Property به Table Cell مربوط است.</p><p>برای Element Dynamic بپرس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">اگر داده خالی باشد، خود Element Render می‌شود؟
Wrapper خالی باقی می‌ماند؟
Gap Parent همچنان اعمال می‌شود؟
Fallback داریم؟
Display Condition لازم است؟
</code></pre></figure><p>مثال کارت مقاله:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Card
├── Featured Image (optional)
├── Category (optional)
├── Title (required)
└── Excerpt (optional)
</code></pre></figure><p>اگر Category خالی است، پنهان‌کردن Text Element ممکن است کافی نباشد؛ اگر Wrapper جدا دارد، Gap یا Height آن نیز باید بررسی شود.</p><hr/></section><section aria-labelledby="concept-v31-19-section-07" class="concept-reference-part"><h3 id="concept-v31-19-section-07">Display Conditions</h3><p>Display Condition می‌تواند Element را براساس شرط نشان دهد یا پنهان کند. این با CSS <code class="inline-code" dir="ltr">display:none</code> دستی یکسان نیست؛ رفتار Render، DOM و Frontend باید در نسخه هدف بررسی شود.</p><p>شرط‌های Dynamic برای وجود یا نبود مقدار می‌توانند از Wrapper خالی جلوگیری کنند، اما نباید بدون تست نتیجه‌گیری کرد که همه Gapها یا Markupها حذف می‌شوند.</p><hr/></section><section aria-labelledby="concept-v31-19-section-08" class="concept-reference-part"><h3 id="concept-v31-19-section-08">AI کجای این معماری قرار می‌گیرد؟</h3><p>AI ابزار Authoring است:</p><ul>
<li>متن پیشنهاد می‌دهد؛</li>
<li>تصویر تولید می‌کند؛</li>
<li>Form یا Tabs اولیه می‌سازد؛</li>
<li>CSS پیشنهاد می‌کند.</li>
</ul><p>اما پس از تولید، معماری Runtime همچنان از Element، Class، Variable، Dynamic Data و Component تشکیل می‌شود.</p><p>AI منبع حقیقت معماری نیست. خروجی آن باید مانند کد و طراحی انسانی Audit شود.</p><hr/></section><section aria-labelledby="concept-v31-19-section-09" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-19-section-09">در Elementor V4</h3><p>مثال Button Dynamic:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Text: Dynamic Product Title
Link: Dynamic Product URL
Class: button-primary
Attribute: aria-label / data-tracking-id در صورت نیاز معتبر
Custom CSS: فقط رفتار اضافی اثبات‌شده
</code></pre></figure><p>هر لایه مسئولیت خودش را دارد.</p><hr/></section><section aria-labelledby="concept-v31-19-section-10" class="concept-reference-part"><h3 id="concept-v31-19-section-10">تست محتوای پویا</h3><p>حداقل این Fixtureها را ببین:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">عنوان ۱۰ کاراکتری
عنوان ۱۲۰ کاراکتری فارسی
بدون تصویر
تصویر عمودی
قیمت کوتاه
قیمت با تخفیف و چند مقدار
فیلد اختیاری خالی
URL طولانی
</code></pre></figure><p>Layoutی که فقط با یک Post نمونه درست است، هنوز Dynamic-ready نیست.</p><hr/></section><section aria-labelledby="concept-v31-19-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-19-section-11">اشتباهات رایج</h3><ul>
<li>Custom CSS برای حل Tree اشتباه</li>
<li>استفاده از Attribute غیراستاندارد بدون <code class="inline-code" dir="ltr">data-</code></li>
<li>ARIA نادرست</li>
<li>Dynamic Data بدون Fallback</li>
<li>فرض حذف کامل Wrapper خالی</li>
<li>استفاده از <code class="inline-code" dir="ltr">:empty</code> بدون توجه به Whitespace و Markup</li>
<li>مخلوط‌کردن AI با Runtime Data</li>
<li>اعتماد به یک نمونه محتوا</li>
</ul><hr/></section><section aria-labelledby="concept-v31-19-section-12" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-19-section-12">تصویر ذهنی نهایی</h3><p>CSS لباس است، Attribute کارت شناسایی و Dynamic Tag پرونده‌ای است که از بانک اطلاعاتی می‌آید. هر سه روی یک فرد اثر دارند، اما جای یکدیگر را نمی‌گیرند.</p><hr/></section><section aria-labelledby="concept-v31-19-section-13" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-19-section-13">قوانین طلایی</h3><ul>
<li><strong>«CSS ظاهر را می‌سازد؛ Attribute معنا و Hook را؛ Dynamic Tag مقدار را.»</strong></li>
<li><strong>«Dynamic Layout را با داده خالی و متن بلند آزمایش کن.»</strong></li>
<li><strong>«Fallback و Display Condition بخشی از معماری محتوا هستند.»</strong></li>
<li><strong>«ARIA اشتباه از نبود ARIA هم می‌تواند بدتر باشد.»</strong></li>
<li><strong>«AI نقطه شروع تولید است، نه مهر تأیید معماری.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Add Custom CSS to an element</li>
<li>Elementor Help: Add and delete attributes</li>
<li>Elementor Help: Dynamic tags in V4 and Display Conditions</li>
<li>WAI-ARIA authoring guidance</li>
</ul><hr/></footer></div></details><section aria-labelledby="dynamic-case-title" class="lesson-section v30-core-lab pro-ecosystem" id="dynamic-data-case-study-v30">
<h2 id="dynamic-case-title">Case Study کامل Dynamic Data — اکوسیستم گسترده‌تر Elementor Pro</h2>
<p class="status-line"><code dir="ltr">verified_by_official_elementor_help</code> · این بخش بخشی از اکوسیستم Elementor Pro است، نه صرفاً هستهٔ Layout در Editor V4.</p>
<h3>سناریو: Custom Post Type «دوره»</h3>
<p>Post Type مشخص: <code dir="ltr">course</code>. هر دوره دادهٔ مستقل دارد و باید در Single Template و فهرست Loop Grid نمایش داده شود.</p>
<div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table">
<caption>ACF fields انتخاب‌شده و اتصال Dynamic Tags</caption><thead><tr><th scope="col">Field</th><th scope="col">ACF type</th><th scope="col">مصرف در Template</th><th scope="col">Fallback</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">course_subtitle</code></th><td>text</td><td>Dynamic Tag / Post Custom Field در Paragraph</td><td>عنوان کوتاه عمومی</td></tr>
<tr><th scope="row"><code dir="ltr">course_duration</code></th><td>number</td><td>متن مدت دوره با Before/After</td><td>«مدت اعلام نشده»</td></tr>
<tr><th scope="row"><code dir="ltr">course_level</code></th><td>select</td><td>Badge سطح</td><td>پنهان‌کردن badge یا مقدار عمومی</td></tr>
<tr><th scope="row"><code dir="ltr">course_cover</code></th><td>image</td><td>Image dynamic source</td><td>تصویر placeholder محلی</td></tr>
<tr><th scope="row"><code dir="ltr">course_start</code></th><td>date_picker</td><td>تاریخ شروع</td><td>«زمان‌بندی نشده»</td></tr>
</tbody></table></div>
<p class="warning-box">ACF Repeater در فهرست رسمی پشتیبانی‌شده نیست؛ فقط fieldهای مستندشده استفاده شده‌اند. Dynamic Tags V4 شامل Post Custom Field است.</p>
<div aria-label="جریان Dynamic Data" class="case-flow">
<ol><li><strong>Define content model:</strong> CPT course + ACF fields.</li><li><strong>Single Template:</strong> Post Title، Featured Image و Post Custom Fieldها را با Dynamic Tags متصل کن.</li><li><strong>Loop Item template:</strong> یک card برای course بساز و همان tagها را به title، cover، level و duration وصل کن.</li><li><strong>Loop Grid:</strong> template را انتخاب کن.</li><li><strong>Query Source:</strong> Posts/CPT course.</li><li><strong>Include:</strong> taxonomy «منتشرشده» یا term مشخص.</li><li><strong>Exclude:</strong> دوره‌های آرشیوی یا Manual Selection مشخص.</li><li><strong>Fallback:</strong> برای هر field مقدار جایگزین و برای نتیجهٔ خالی پیام empty state طراحی کن.</li></ol>
</div>
<h3>Empty-state contract</h3><p>اگر Query نتیجه ندارد، صفحه نباید یک grid خالی و مبهم نشان دهد. یک پیام روشن، مسیر بازگشت یا CTA مناسب قرار بده. این توصیهٔ UX عمومی با برچسب <code dir="ltr">proposed_strategy</code> است؛ نام و کنترل دقیق empty state را فقط جایی رسمی تلقی کن که مستند شده باشد.</p>
<aside class="teacher-note"><strong>نام‌گذاری صحیح:</strong> محصول رسمی از <strong>Loop Grid</strong> و بخش <strong>Query</strong> استفاده می‌کند؛ در این Workbook نام محصول جداگانه‌ای برای این workflow ساخته نشده است.</aside>
</section><details class="lesson-disclosure settings-values-units" id="lesson-v17-advanced-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-v17-advanced-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Custom CSS، Attribute و Dynamic Tag؛ نوع مقدار باید معتبر بماند</span></summary>
<section aria-labelledby="lesson-v17-advanced-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Custom CSS همهٔ grammar CSS را باز می‌کند، اما Attribute و Dynamic Tag ممکن است string یا دادهٔ پویا برگردانند. هر مقدار باید با Property مصرف‌کننده سازگار باشد.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> Dynamic Tag بسته‌ای است که محتوا در زمان اجرا می‌آید؛ قبل از گذاشتن در قفل باید بدانی کلید عدد است، رنگ است یا متن.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Custom CSS value</th><td><code dir="ltr">هر Property CSS</code></td><td>طبق grammar همان Property</td><td>وابسته به Property</td><td>برای واحدهای خارج از UI مانند clamp/dvh.</td><td>پشتیبانی CSS به‌معنای پشتیبانی کنترل UI نیست.</td><td><code dir="ltr">E_CUSTOM_CSS</code></td></tr><tr><th scope="row">Attribute</th><td><code dir="ltr">HTML attribute</code></td><td>string / token / number برحسب attribute</td><td>HTML semantics</td><td>برای data-*، aria-* و رفتار معتبر.</td><td>واحد CSS را داخل attribute نامرتبط نگذار.</td><td><code dir="ltr">E_CUSTOM_CSS</code></td></tr><tr><th scope="row">Dynamic Tag</th><td><code dir="ltr">dynamic value</code></td><td>نوع دادهٔ منبع</td><td>runtime content</td><td>برای مقدار پویا در Control سازگار.</td><td>خروجی نامعتبر ممکن است resolve نشود.</td><td><code dir="ltr">E_DYNAMIC</code></td></tr><tr><th scope="row">Functions</th><td><code dir="ltr">calc()/clamp()</code></td><td>ترکیب انواع سازگار</td><td>context CSS</td><td>برای محاسبهٔ محدود و شفاف.</td><td>واحدهای ناسازگار را جمع نکن.</td><td><code dir="ltr">MDN_CALC</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>clamp(1rem, 2vw, 2rem) با root=16px و viewport=1200px: preferred=24px و بین 16 و 32 است، پس 24px انتخاب می‌شود.</p></section>
<section><h3>📱 در Responsive</h3><p>Custom CSS و Dynamic Tag را در breakpoint و frontend واقعی تست کن؛ Preview فقط یک context است.</p></section>
<section><h3>🔬 در DevTools</h3><p>specified، computed و actual value را جدا بررسی کن؛ خطای syntax را در Styles panel ببین.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/add-custom-css-to-an-element/" rel="noopener noreferrer" target="_blank">Elementor V4 — Custom CSS</a>، <a href="https://elementor.com/help/dynamic-tags-in-v4/" rel="noopener noreferrer" target="_blank">Elementor V4 — Dynamic tags</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc" rel="noopener noreferrer" target="_blank">MDN — calc()</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp" rel="noopener noreferrer" target="_blank">MDN — clamp()</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">B. Attributes یعنی به HTML معنا می‌دهی</span></summary><section class="disclosure-content lesson-section">
<p>Attributeها مثل یادداشت‌هایی هستند که به مرورگر، ابزارهای دسترسی‌پذیری، اسکریپت‌ها و موتورهای دیگر می‌گویند این Element چه نقشی دارد. برای RTL و accessibility، Attributeهایی مثل <code class="inline-code" dir="ltr">lang</code>، <code class="inline-code" dir="ltr">dir</code>، <code class="inline-code" dir="ltr">role</code> و <code class="inline-code" dir="ltr">aria-*</code> می‌توانند حیاتی باشند.</p>
<aside class="teacher-note"><p><strong>هشدار استاد:</strong> Attribute را برای جبران HTML غلط استفاده نکن. اول Element درست را انتخاب کن، بعد اگر معنا یا اتصال اضافه لازم بود Attribute بده.</p></aside>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">C. Dynamic Tags یعنی محتوا از منبع می‌آید</span></summary><section class="disclosure-content lesson-section">
<p>وقتی متن، تصویر، لینک یا مقدار از یک منبع پویا می‌آید، Dynamic Tag وارد می‌شود. این برای سایت‌های واقعی مهم است، چون همه‌چیز متن ثابت داخل صفحه نیست. اما اگر دانش‌آموز هنوز Element، Class و Variable را نفهمیده باشد، Dynamic Tag فقط گیجی جدید می‌سازد.</p>
<table><caption>جدول آموزشی دوره — C. Dynamic Tags یعنی محتوا از منبع می‌آید</caption><thead><tr><th scope="col">ابزار</th><th scope="col">چه زمانی؟</th><th scope="col">سؤال کنترل</th></tr></thead><tbody>
<tr><td>Custom CSS</td><td>UI کافی نیست</td><td>آیا selector و Class هدف مشخص است؟</td></tr>
<tr><td>Attributes</td><td>معنا، accessibility یا integration لازم است</td><td>آیا Element درست انتخاب شده؟</td></tr>
<tr><td>Dynamic Tags</td><td>محتوا باید از منبع پویا بیاید</td><td>اگر منبع خالی بود چه می‌شود؟</td></tr>
</tbody></table>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">تمرین جمع‌بندی</span></summary><section class="disclosure-content lesson-section">
<ol><li>یک Button با Global Class بساز.</li><li>یک Attribute امن و معنادار مثل <code class="inline-code" dir="ltr">aria-label</code> فقط در صورت نیاز اضافه کن.</li><li>اگر لینک باید از منبع پویا بیاید، Dynamic Tag را بررسی کن.</li><li>فقط اگر UI کافی نبود، یک Custom CSS کوچک بنویس و کنار آن دلیلش را یادداشت کن.</li></ol>
</section></details>
<details class="lesson-disclosure" id="lesson-v17-advanced-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: CSS، Attributes و Dynamic Data</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Attribute در برابر Custom CSS</h3><p>Attribute اطلاعات معنایی یا فنی روی wrapper می‌گذارد؛ مثل <code dir="ltr">aria-*</code>، <code dir="ltr">role</code>، <code dir="ltr">data-*</code>. Custom CSS قانون ظاهری یا selector خاص می‌نویسد.</p></section>
<section class="inline-compare-card"><h3>Dynamic Tag در برابر Static Content</h3><p>Static Content متن ثابت است. Dynamic Tag از دادهٔ سایت، پست، کاربر یا فیلد پویا می‌آید. اگر مقدار باید با محتوا عوض شود، دستی ننویس.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="advanced-css-practical-findings"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="advanced-css-practical-findings-heading" role="heading">🔎 یافتهٔ عملی و خطایابی</span></summary><section aria-labelledby="advanced-css-practical-findings-heading" class="disclosure-content practical-findings">
<p class="finding-scope">این بخش فقط ادعاهایی را آموزش می‌دهد که یا در مشاهدهٔ واقعی ثبت شده‌اند یا Help Center رسمی Elementor آن‌ها را صریحاً پشتیبانی می‌کند. نتیجه‌های وابسته به Theme، نسخه یا ساختار DOM با دامنهٔ اعتبار نوشته شده‌اند.</p>
<article class="finding-card" data-verification="verified_by_official_help" id="finding-custom-css-wrong-target">
<div class="evidence-badges"><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>چرا Custom CSS من فقط در Hover، Mobile یا چند Element دیگر دیده می‌شود؟</h3>
<p><strong>قاعدهٔ رسمی V4:</strong> Custom CSS به Class انتخاب‌شده متصل می‌شود و می‌تواند برای State و device size جدا باشد. پس قبل از نوشتن CSS باید Local/Global Class، Normal/Hover و Desktop/Mobile هدف را مشخص کنی.</p>
<div class="finding-checks">
<section><h4>در Elementor</h4><p>Classes field، State فعال و responsive icon را قبل از بازکردن Custom CSS ثبت کن.</p></section>
<section><h4>وقتی اصلاً ظاهر نمی‌شود</h4><p>Syntax، cache مرورگر/سرور، Theme compatibility و Clear Files &amp; Data را بررسی کن؛ اما ابتدا مطمئن شو CSS روی target درست نوشته شده است.</p></section>
</div>
<p class="golden-rule"><strong>قانون طلایی:</strong> در V4 سؤال اول Custom CSS این نیست که «کد درست است؟»؛ سؤال اول این است که «کد به کدام Class، State و device وصل شده؟»</p>
<details class="more-know"><summary>منابع رسمی</summary><p><a href="https://elementor.com/help/add-custom-css-to-an-element/">Add Custom CSS to an element</a> و <a href="https://elementor.com/help/custom-css-not-working/">Custom CSS not working</a></p></details>
</article>
</section></details>
<p class="v30-value-type-note"><strong>نوع مقدار غالب این درس:</strong> <code dir="ltr">reference / keyword / not_applicable</code>؛ محتوای واحد مصنوعی اضافه نشده است.</p></article>
