<article class="lesson card-surface" id="lesson-v19-element-weight">
<header class="lesson-header">
<p class="lesson-kicker">تکمیلی نسخه 19 · Performance Thinking</p>
<h2 class="former-h1">درس 20A — وزن المان‌ها در Elementor 4: سبک‌ترین راه درست کدام است؟</h2>
<p class="lesson-goal">هدف این درس این است که بفهمی هر Element فقط یک شکل روی صفحه نیست؛ هر انتخاب می‌تواند روی DOM، CSS، Asset، JavaScript، Layout، Paint و نگهداری اثر بگذارد.</p>
</header>
<section class="lesson-body lesson-core-concept" data-core-concept="true">
<div class="element-weight-lab">
<h2>۱. تصویر ذهنی: هر المان یک کوله‌پشتی دارد</h2>
<p>فرض کن هر Element که داخل Elementor می‌گذاری، یک کوله‌پشتی نامرئی با خودش می‌آورد. بعضی‌ها فقط یک دفترچه دارند؛ مثل Heading ساده. بعضی‌ها لپ‌تاپ، کابل، باتری، دوربین و سه کتاب سنگین دارند؛ مثل Video/YouTube، Form پیچیده یا Interactionهای زیاد.</p>
<p>طراح حرفه‌ای فقط نمی‌پرسد «چطور این ظاهر را بسازم؟»؛ می‌پرسد: <strong>سبک‌ترین، قابل‌نگهداری‌ترین و دقیق‌ترین راه ساخت این ظاهر چیست؟</strong></p>
</div>
<div class="definition-usage-card">
<h2>۲. Definition Weight در برابر Usage Weight</h2>
<p>این همان نکته‌ای است که تفاوت Local Class و Global Class را روشن می‌کند. <strong>Usage</strong> یعنی یک Style یا Component چند بار استفاده شده. <strong>Definition</strong> یعنی خود قانون چند بار تعریف شده است.</p>
<div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — ۱. تصویر ذهنی: هر المان یک کوله‌پشتی دارد</caption><thead><tr><th scope="col">مفهوم</th><th scope="col">Definition</th><th scope="col">Usage</th><th scope="col">حکم استاد</th></tr></thead><tbody>
<tr><th scope="row">Variable</th><td>یک مقدار یک‌بار تعریف می‌شود</td><td>بارها در Element یا Class مصرف می‌شود</td><td>برای مقدارهای تکراری</td></tr>
<tr><th scope="row">Global Class</th><td>یک بسته Style یک‌بار تعریف می‌شود</td><td>به چند Element وصل می‌شود</td><td>برای ظاهرهای تکراری</td></tr>
<tr><th scope="row">Local Class</th><td>تعریف مخصوص همان Element است</td><td>مصرف واقعی‌اش معمولاً همان Element است</td><td>برای استثناهای محلی</td></tr>
<tr><th scope="row">Component</th><td>ساختار Master یک‌بار تعریف می‌شود</td><td>Instanceها از آن استفاده می‌کنند</td><td>برای ساختارهای تکراری</td></tr>
</tbody></table></div>
<p class="golden-rule">قانون طلایی: وزن بد معمولاً از Usage زیاد نمی‌آید؛ از Definition تکراری و بی‌معنی می‌آید.</p>
</div>
<section class="element-weight-lab">
<h2>۳. هفت نوع وزن در Elementor</h2>
<div class="weight-grid">
<section class="weight-dimension"><h3>وزن DOM</h3><p>چند Node و wrapper به HTML اضافه می‌شود؟ Empty wrapperها و nesting بی‌دلیل این وزن را زیاد می‌کنند.</p></section>
<section class="weight-dimension"><h3>وزن CSS</h3><p>چند selector، rule، state و responsive variant ساخته می‌شود؟ Local Classهای تکراری اینجا خطرناک‌اند.</p></section>
<section class="weight-dimension"><h3>وزن Asset</h3><p>آیا تصویر، فونت، SVG، ویدئو یا iframe وارد صفحه می‌شود؟ Image و Video اغلب وزن asset دارند.</p></section>
<section class="weight-dimension"><h3>وزن JS / Runtime</h3><p>آیا برای کارکردن به رفتار JavaScript، trigger، form action یا interaction نیاز دارد؟</p></section>
<section class="weight-dimension"><h3>وزن Layout</h3><p>آیا باعث محاسبات layout، overflow، wrap دشوار یا وابستگی خطرناک به viewport می‌شود؟</p></section>
<section class="weight-dimension"><h3>وزن Paint / Composite</h3><p>Shadowهای سنگین، blur، filter، background layers و animationها می‌توانند هزینهٔ paint/composite بسازند.</p></section>
<section class="weight-dimension"><h3>وزن Maintenance</h3><p>بعداً چقدر سخت است تغییرش بدهی؟ ۵۰ Local Class مشابه از این نظر سنگین‌تر از یک Global Class تمیز است.</p></section>
</div>
</section>
<section class="element-weight-lab">
<h2>۴. نقشهٔ وزن نسبی Elementها</h2>
<p><strong>status:</strong> <code dir="ltr">teaching_model_not_runtime_measurement</code> — این جدول برای تصمیم آموزشی است. عدد قطعی نیست و باید با Runtime، DOM و خروجی CSS واقعی سنجیده شود.</p>
<div class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — ۴. نقشهٔ وزن نسبی Elementها</caption><thead><tr><th scope="col">انتخاب</th><th scope="col">وزن نسبی</th><th scope="col">ریسک اصلی</th><th scope="col">انتخاب بهتر وقتی...</th></tr></thead><tbody>
<tr><th scope="row">Heading / Paragraph Atomic</th><td>سبک</td><td>کلاس محلی تکراری</td><td>متن واقعی داری</td></tr>
<tr><th scope="row">Button Atomic</th><td>سبک تا متوسط</td><td>stateهای تکراری و local style</td><td>CTA واقعی داری؛ با Global Class کنترلش کن</td></tr>
<tr><th scope="row">Div Block ساده</th><td>سبک</td><td>wrapper بی‌معنی</td><td>گروه‌بندی معنایی لازم است</td></tr>
<tr><th scope="row">Flexbox</th><td>سبک تا متوسط</td><td>nesting زیاد و spacer خالی</td><td>چیدمان یک‌بعدی داری</td></tr>
<tr><th scope="row">Grid</th><td>متوسط</td><td>استفاده برای کار سادهٔ یک‌بعدی</td><td>هم ردیف و هم ستون مهم‌اند</td></tr>
<tr><th scope="row">Empty Flexbox</th><td>مشکوک</td><td>DOM اضافه، maintenance، vw/vh خطرناک</td><td>فقط اگر visual slot واقعی باشد</td></tr>
<tr><th scope="row">Image Element</th><td>متوسط تا سنگین</td><td>asset، اندازهٔ نادرست، alt خالی</td><td>تصویر محتوایی است</td></tr>
<tr><th scope="row">Background Image</th><td>متوسط تا سنگین</td><td>تصویر محتوایی پنهان می‌شود</td><td>تصویر فقط تزئینی است</td></tr>
<tr><th scope="row">SVG</th><td>سبک تا متوسط</td><td>path پیچیده یا inline بزرگ</td><td>آیکون یا شکل برداری لازم است</td></tr>
<tr><th scope="row">Tabs</th><td>متوسط تا سنگین</td><td>state، accessibility، JS behavior</td><td>واقعاً محتوای تب‌بندی‌شده داری</td></tr>
<tr><th scope="row">Atomic Form</th><td>متوسط تا سنگین</td><td>هر input و action وزن اضافه دارد</td><td>فرم واقعی و ضروری داری</td></tr>
<tr><th scope="row">Interactions</th><td>متغیر</td><td>motion زیاد، trigger بی‌هدف</td><td>رفتار به فهم کاربر کمک می‌کند</td></tr>
<tr><th scope="row">YouTube / Video</th><td>سنگین</td><td>iframe/media/network/JS</td><td>ارزش محتوایی و تجاری واضح دارد</td></tr>
<tr><th scope="row">Legacy Element/Widget آماده</th><td>معمولاً سنگین‌تر</td><td>markup/behavior قدیمی‌تر</td><td>Atomic equivalent نداری یا در migration هستی</td></tr>
</tbody></table></div>
</section>
<section class="element-weight-lab">
<h2>۵. کارت وزن برای ForLesson: Empty Flexbox با <span dir="ltr">33.33vw</span> و <span dir="ltr">56vh</span></h2>
<div class="weight-badge-row"><span class="weight-badge warn">DOM: اضافه</span><span class="weight-badge warn">Layout: پرریسک</span><span class="weight-badge good">Asset: صفر</span><span class="weight-badge risky">Maintenance: مشکوک</span></div>
<p><strong>مشاهده:</strong> اگر سه پنل با <code dir="ltr">width: 33.33vw</code> کنار هم باشند، جمع نظری آن‌ها تقریباً کل viewport است؛ اما gap، padding، scrollbar و parent width هنوز وارد حساب نشده‌اند. همین‌جا خطر overflow شروع می‌شود.</p>
<p><strong>حکم استاد:</strong> اگر این‌ها فقط spacer هستند، انتخاب بد است و باید با Gap/Padding یا ساختار درست جایگزین شوند. اگر واقعاً panel تصویری یا placeholder هستند، حذفشان نکن؛ آن‌ها را معنادار کن: Image/Background واقعی، aspect-ratio، min-height، Global Class و Variable برای radius/color.</p>
</section>
<section class="element-weight-lab">
<h2>۶. چک‌لیست تصمیم سریع</h2>
<ul>
<li>آیا این Element محتوا دارد یا فقط برای هل‌دادن چیزهاست؟</li>
<li>آیا همین ظاهر در دو جای دیگر هم تکرار می‌شود؟ اگر بله، چرا هنوز Local است؟</li>
<li>آیا این مقدار باید Variable شود یا این ظاهر باید Global Class شود؟</li>
<li>آیا این ساختار کامل تکرار می‌شود؟ اگر بله، آیا Component بهتر نیست؟</li>
<li>آیا asset سنگین، interaction یا iframe واقعاً ارزش محتوایی دارد؟</li>
<li>آیا با Atomic Element ساده‌تر و سبک‌تر می‌شود ساخت؟</li>
</ul>
<p class="golden-rule">قانون طلایی: هر Element یک هزینه دارد؛ طراحی حرفه‌ای یعنی کم‌هزینه‌ترین ابزار درست را انتخاب کنی، نه فقط سریع‌ترین کلیک را.</p>
</section>
</section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="d22121d0808facdef0a414545bd1c7695aeda9c6d9814c489c98f48856052722" id="lesson-v19-element-weight-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق وزن Element؛ هزینه فقط تعداد Node نیست</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="27" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-27-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-27-section-01">مسئله‌ای که «وزن Element» حل می‌کند</h3><p>دو Element ممکن است هر دو یک Node باشند، اما هزینه یکسانی نداشته باشند:</p><ul>
<li>یک Div ساده</li>
<li>Video با Player</li>
<li>Form با Validation</li>
<li>Carousel با JavaScript</li>
<li>Image بزرگ</li>
<li>SVG پیچیده</li>
<li>Interaction وابسته به Scroll</li>
</ul><p>پس شمارش Node فقط یکی از نشانه‌هاست.</p><hr/></section><section aria-labelledby="concept-v31-27-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-27-section-02">تشبیه به دنیای واقعی: کوله‌پشتی</h3><p>در یک کوله ده وسیله داری:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">۵ جوراب
۱ لپ‌تاپ
۱ بطری آب
۱ کتاب سنگین
۲ مداد
</code></pre></figure><p>تعداد وسایل ۱۰ است، اما وزن را نوع وسیله تعیین می‌کند.</p><p>Elementها نیز چند نوع وزن دارند.</p><hr/></section><section aria-labelledby="concept-v31-27-section-03" class="concept-reference-part"><h3 id="concept-v31-27-section-03">پنج نوع وزن</h3><h4>۱. وزن ساختاری</h4><ul>
<li>تعداد Node</li>
<li>عمق Nesting</li>
<li>تعداد Child مستقیم</li>
<li>Wrapperهای اضافی</li>
</ul><h4>۲. وزن Style</h4><ul>
<li>Selectorهای پیچیده</li>
<li>Overrideهای زیاد</li>
<li>Effects و Filter</li>
<li>Shadowهای سنگین</li>
<li>Style Recalculation دامنه‌دار</li>
</ul><h4>۳. وزن Media</h4><ul>
<li>Byte تصویر و Video</li>
<li>ابعاد Decode</li>
<li>تعداد Font و Weight</li>
<li>SVG پیچیده</li>
</ul><h4>۴. وزن رفتار</h4><ul>
<li>Event Listener</li>
<li>Interaction</li>
<li>Scroll Handler</li>
<li>Timer</li>
<li>Animation</li>
</ul><h4>۵. وزن وابستگی</h4><ul>
<li>Third-party library</li>
<li>Add-on</li>
<li>Network request</li>
<li>Dynamic query</li>
<li>Form action</li>
</ul><p>یک Element ممکن است در چند دسته سنگین باشد.</p><hr/></section><section aria-labelledby="concept-v31-27-section-04" class="concept-reference-part"><h3 id="concept-v31-27-section-04">Wrapper ساده همیشه بی‌هزینه نیست، اما همیشه بد هم نیست</h3><p>یک Wrapper ساده معمولاً هزینه کمی دارد، ولی در مقیاس زیاد:</p><ul>
<li>DOM عمیق‌تر می‌شود؛</li>
<li>Selector Matching و Layout پیچیده‌تر می‌شود؛</li>
<li>Debug سخت‌تر می‌شود.</li>
</ul><p>بااین‌حال Wrapperی که Containing Block، Grid Context یا Semantic Group می‌سازد مسئولیت واقعی دارد.</p><p>به‌جای «Node را حذف کن» بگو:</p><blockquote>
<p>مسئولیت را با کمترین ساختار لازم اجرا کن.</p>
</blockquote><hr/></section><section aria-labelledby="concept-v31-27-section-05" class="concept-reference-part"><h3 id="concept-v31-27-section-05">Depth و Breadth</h3><h4>Depth زیاد</h4><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Div
└── Div
    └── Div
        └── Div
            └── Text
</code></pre></figure><p>مسیر Layout و Debug را طولانی می‌کند.</p><h4>Childهای بسیار زیاد</h4><p>یک Parent با صدها Child نیز Recalculation و مدیریت را سخت می‌کند.</p><p>هیچ عدد جهانی برای عمق یا تعداد Child وجود ندارد؛ Audit باید با صفحه واقعی انجام شود.</p><hr/></section><section aria-labelledby="concept-v31-27-section-06" class="concept-reference-part"><h3 id="concept-v31-27-section-06">Element پنهان</h3><p><code class="inline-code" dir="ltr">display:none</code> ممکن است Paint و Layout آن Subtree را حذف کند، اما:</p><ul>
<li>Markup ممکن است همچنان در DOM باشد؛</li>
<li>Data و Asset شاید قبلاً Load شده باشد؛</li>
<li>Script ممکن است ثبت شده باشد؛</li>
<li>Duplicateهای Mobile/Desktop نگهداری را دو برابر کنند.</li>
</ul><p>پس Hidden بودن مساوی «بی‌هزینه بودن کامل» نیست.</p><hr/></section><section aria-labelledby="concept-v31-27-section-07" class="concept-reference-part"><h3 id="concept-v31-27-section-07">Interaction Weight</h3><p>ده Element ساده با Scroll Interaction ممکن است از صد Div ثابت پرهزینه‌تر باشند.</p><p>هر Interaction را از این نظر بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Trigger frequency
JavaScript work
Style changes
Layout changes
Paint area
Compositor-friendly transform/opacity
</code></pre></figure><p>Transform و Opacity معمولاً برای Animation مناسب‌تر از Width/Height/Top/Left هستند، اما تضمین بی‌هزینه بودن ندارند.</p><hr/></section><section aria-labelledby="concept-v31-27-section-08" class="concept-reference-part"><h3 id="concept-v31-27-section-08">Media Weight</h3><p>یک Hero Image ۴MB می‌تواند از صد Wrapper مهم‌تر باشد.</p><p>علاوه بر Network Bytes، Decode Size را نیز ببین. تصویر فشرده ممکن است روی Disk کوچک باشد اما پس از Decode حافظه زیادی بگیرد.</p><p>Font نیز وزن دارد:</p><ul>
<li>تعداد Family</li>
<li>تعداد Weight</li>
<li>Subset</li>
<li>preload</li>
<li>fallback</li>
</ul><hr/></section><section aria-labelledby="concept-v31-27-section-09" class="concept-reference-part"><h3 id="concept-v31-27-section-09">Class و Token Weight</h3><p>Class زیاد لزوماً Runtime کند نمی‌سازد، اما Architecture را سنگین می‌کند:</p><ul>
<li>تشخیص منبع Style سخت می‌شود؛</li>
<li>Override زیاد می‌شود؛</li>
<li>CSS تولیدشده رشد می‌کند؛</li>
<li>تغییرات مرکزی پرریسک می‌شوند.</li>
</ul><p>این «وزن شناختی و نگهداری» است، نه فقط CPU.</p><hr/></section><section aria-labelledby="concept-v31-27-section-10" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-27-section-10">ماتریس وزن</h3><div aria-label="جدول آموزشی مرجع مفهومی" class="table-scroll concept-table-scroll" role="region" tabindex="0"><table class="data-table educational-table concept-reference-table"><caption>جدول آموزشی مرجع مفهومی</caption>
<thead>
<tr>
<th>Element</th>
<th style="text-align:right">ساختاری</th>
<th style="text-align:right">Media</th>
<th style="text-align:right">Behavior</th>
<th style="text-align:right">Dependency</th>
<th>توضیح</th>
</tr>
</thead>
<tbody>
<tr>
<td>Div ساده</td>
<td style="text-align:right">کم</td>
<td style="text-align:right">صفر</td>
<td style="text-align:right">صفر</td>
<td style="text-align:right">کم</td>
<td>مگر در تکرار زیاد</td>
</tr>
<tr>
<td>Image</td>
<td style="text-align:right">کم</td>
<td style="text-align:right">متوسط/زیاد</td>
<td style="text-align:right">کم</td>
<td style="text-align:right">Media</td>
<td>اندازه و LCP مهم</td>
</tr>
<tr>
<td>SVG پیچیده</td>
<td style="text-align:right">کم</td>
<td style="text-align:right">متغیر</td>
<td style="text-align:right">متغیر</td>
<td style="text-align:right">Asset</td>
<td>Path/Filter مهم</td>
</tr>
<tr>
<td>Form</td>
<td style="text-align:right">متوسط</td>
<td style="text-align:right">کم</td>
<td style="text-align:right">زیاد</td>
<td style="text-align:right">Backend</td>
<td>Validation/Actions</td>
</tr>
<tr>
<td>Carousel</td>
<td style="text-align:right">متوسط</td>
<td style="text-align:right">متوسط</td>
<td style="text-align:right">زیاد</td>
<td style="text-align:right">JS</td>
<td>Interaction و Asset</td>
</tr>
<tr>
<td>Video</td>
<td style="text-align:right">کم</td>
<td style="text-align:right">بسیار زیاد</td>
<td style="text-align:right">متوسط</td>
<td style="text-align:right">Player/Network</td>
<td>Poster و Loading مهم</td>
</tr>
</tbody>
</table></div><p>این جدول راهنماست، نه Benchmark عددی.</p><hr/></section><section aria-labelledby="concept-v31-27-section-11" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-27-section-11">در Elementor V4</h3><p>هنگام انتخاب Element فقط نپرس «چند Node می‌سازد؟» بپرس:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">چه Assetی Load می‌کند؟
چه Scriptی فعال می‌کند؟
چند State/Interaction دارد؟
آیا Wrapperهای داخلی دارد؟
آیا Dynamic Query اجرا می‌کند؟
آیا جایگزین اتمیک سبک‌تری وجود دارد؟
</code></pre></figure><p>Atomic Element ممکن است Markup ساده‌تری داشته باشد، اما نتیجه باید با Frontend واقعی سنجیده شود.</p><hr/></section><section aria-labelledby="concept-v31-27-section-12" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-27-section-12">اشتباهات رایج</h3><ul>
<li>تبدیل Performance به Node Count</li>
<li>حذف Wrapperهای مسئول</li>
<li>نادیده‌گرفتن Image و Font</li>
<li>مخفی‌کردن Duplicateها به‌جای حذف معماری تکراری</li>
<li>استفاده از Widget سنگین برای رفتار ساده</li>
<li>Animation Layout-based</li>
<li>Classهای زیاد و نامفهوم</li>
<li>عددسازی میلی‌ثانیه برای هر Wrapper</li>
</ul><hr/></section><section aria-labelledby="concept-v31-27-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-27-section-13">تصویر ذهنی نهایی</h3><p>DOM تعداد وسایل کوله است، اما وزن واقعی را جنس وسایل تعیین می‌کند. یک Video می‌تواند از صد Div سنگین‌تر باشد و یک Wrapper کوچک می‌تواند ستون نگهدارندهٔ کل ساختار باشد.</p><hr/></section><section aria-labelledby="concept-v31-27-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-27-section-14">قوانین طلایی</h3><ul>
<li><strong>«وزن Element چندبعدی است: DOM، Style، Media، Behavior و Dependency.»</strong></li>
<li><strong>«Node کم هدف نهایی نیست؛ مسئولیت روشن با ساختار کمینه هدف است.»</strong></li>
<li><strong>«Hidden مساوی رایگان نیست.»</strong></li>
<li><strong>«Asset و Interaction را در کنار Markup Audit کن.»</strong></li>
<li><strong>«هزینه را اندازه بگیر؛ برای هر Wrapper عدد ثابت نساز.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Chrome DevTools Performance and Network references</li>
<li>web.dev Core Web Vitals optimization guidance</li>
<li>Elementor performance and atomic element documentation</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-v19-element-weight-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-v19-element-weight-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — وزن Element؛ شمارش و مسئولیت، نه واحد طول</span></summary>
<section aria-labelledby="lesson-v19-element-weight-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">سبک یا سنگین بودن Element به DOM، wrapper و قابلیت‌های فعال مربوط است؛ با px و rem سنجیده نمی‌شود.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> وزن سازه را با تعداد قطعات و پیچیدگی اتصال می‌سنجی، نه عرض رنگ‌آمیزی آن.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">DOM depth</th><td><code dir="ltr">ancestor depth</code></td><td>integer</td><td>بدون واحد طول</td><td>برای فهم nesting.</td><td>یک wrapper لازم را فقط برای کم‌کردن عدد حذف نکن.</td><td><code dir="ltr">E_DIFF</code></td></tr><tr><th scope="row">Element count</th><td><code dir="ltr">node count</code></td><td>integer</td><td>بدون واحد طول</td><td>برای audit ساختار.</td><td>تعداد به‌تنهایی کیفیت را ثابت نمی‌کند.</td><td><code dir="ltr">E_DIFF</code></td></tr><tr><th scope="row">Layout capability</th><td><code dir="ltr">display engine</code></td><td>keyword</td><td>بدون واحد</td><td>سبک‌ترین موتور لازم.</td><td>Flex/Grid را فقط برای یک Gap انتخاب نکن.</td><td><code dir="ltr">E_LAYOUT</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>not_applicable — اینجا معیار شمارش و مسئولیت است، نه تبدیل واحد CSS.</p></section>
<section><h3>📱 در Responsive</h3><p>Element اضافی برای نسخه‌های تکراری Desktop/Mobile می‌تواند DOM را سنگین کند؛ Order/Direction را ابتدا بررسی کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>DOM tree و computed display را با نقش واقعی مقایسه کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/" rel="noopener noreferrer" target="_blank">Elementor — Differences between Editor V3 and V4</a>، <a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Layout</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details>
<p class="v30-value-type-note"><strong>نوع مقدار غالب این درس:</strong> <code dir="ltr">unitless / not_applicable</code>؛ محتوای واحد مصنوعی اضافه نشده است.</p></article>
