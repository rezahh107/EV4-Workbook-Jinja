<article class="lesson card-surface" data-lesson="10" id="lesson-10"><h2 class="lesson-title former-h1">درس 10 — Heading، Paragraph، List و Typography</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-10-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-10-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> Element محتوایی درست و سلسله‌مراتب متن را انتخاب کنی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Typography پیشرفته یا طراحی Font System کامل را.</p><p><strong>در پایان باید بتوانی:</strong> ستون متن TUYA را معنایی، خوانا و قابل‌تغییر بسازی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-10-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-10-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۰–۲۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۲۰–۳۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> معنا و محتوا را از ظاهر جدا می‌کنی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-10-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-10-lesson-understand-4">A. بفهم</h2><h3>مسئله</h3><p>ظاهر متن ممکن است درست باشد، اما اگر Element اشتباه انتخاب شود، ساختار، دسترسی‌پذیری و نگهداری ضعیف می‌شود.</p><h3>انتخاب Element</h3><section aria-labelledby="section-hidden-152-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-152-heading">بخش آموزشی</h2><dl class="term-grid"><dt>عنوان بخش؟</dt><dd>Heading</dd><dt>متن مستقل؟</dt><dd>Paragraph</dd><dt>مجموعهٔ واقعی؟</dt><dd>List یا آیتم‌های تکراری معنایی</dd><dt>عمل یا ناوبری؟</dt><dd>Button/Link</dd></dl></section><h3>Typography مهم برای Elementor</h3><ul>
<li>Font Family؛</li>
<li>Font Size؛</li>
<li>Weight؛</li>
<li>Line Height؛</li>
<li>Text Width؛</li>
<li>Alignment.</li>
</ul><p>لازم نیست تمام Propertyهای CSS را بدانی؛ باید اثر هر Control را روی خوانایی ببینی.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="469ab18fb781f3ea19da2c9e3b1a3ebe68fd8f301d270956b17e9ea4fa3da2df" id="lesson-10-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Typography؛ متن فقط Font نیست</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="10" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-10-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-10-section-01">مسئله‌ای که Typography حل می‌کند</h3><p>کاربر پیش از دیدن دکمه، رنگ و تصویر، باید متن را بفهمد. اگر متن:</p><ul>
<li>بیش از حد متراکم باشد؛</li>
<li>خط‌های خیلی بلند داشته باشد؛</li>
<li>سلسله‌مراتب نامشخصی داشته باشد؛</li>
<li>در Mobile بشکند؛</li>
<li>یا وزن‌های فونت درست Load نشوند؛</li>
</ul><p>زیباترین Layout هم قابل استفاده نخواهد بود.</p><p>Typography فقط انتخاب نام یک Font نیست. Typography <strong>معماری خواندن</strong> است.</p><hr/></section><section aria-labelledby="concept-v31-10-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-10-section-02">تشبیه به دنیای واقعی: موسیقی و نفس‌کشیدن</h3><p>یک قطعه موسیقی را تصور کن:</p><ul>
<li>Font Family = جنس صدای ساز</li>
<li>Font Size = شدت صدا</li>
<li>Font Weight = تأکید نوازنده</li>
<li>Line Height = فاصلهٔ ضرب‌ها و فرصت نفس‌کشیدن</li>
<li>Paragraph Spacing = مکث میان جمله‌های موسیقی</li>
<li>Headingها = بخش‌های اصلی قطعه</li>
<li>Width ستون = طول هر عبارت پیش از نفس بعدی</li>
</ul><p>اگر همهٔ نت‌ها با یک شدت و بدون مکث اجرا شوند، حتی موسیقی خوب خفه‌کننده می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-10-section-03" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-10-section-03">چرا Typography چند تصمیم هم‌زمان است؟</h3><p>خوانایی از تعامل چند عامل به وجود می‌آید:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Font Family
+ Font Size
+ Font Weight
+ Line Height
+ Line Length
+ Contrast
+ Spacing
+ Language Script
</code></pre></figure><p>برای فارسی، شکل حروف، اتصال‌ها، نقطه‌ها و ارتفاع بصری ممکن است با فونت لاتین متفاوت باشد. بنابراین نسخهٔ ظاهراً مناسب یک Scale لاتین را نباید بدون آزمایش روی متن واقعی فارسی پذیرفت.</p><hr/></section><section aria-labelledby="concept-v31-10-section-04" class="concept-reference-part"><h3 id="concept-v31-10-section-04">نقش معنایی و ظاهر را جدا کن</h3><p><code class="inline-code" dir="ltr">h1</code> یا <code class="inline-code" dir="ltr">h2</code> فقط برای بزرگ‌کردن متن نیست. Heading ساختار سند را تعریف می‌کند.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">H1: عنوان اصلی صفحه
H2: بخش‌های اصلی
H3: زیربخش‌ها
Paragraph: متن توضیحی
List: مجموعهٔ آیتم‌های مرتبط
</code></pre></figure><p>ظاهر می‌تواند با Class تغییر کند، اما نقش معنایی باید درست بماند.</p><p>در Elementor V4، Level یا نوع Element را در General/Content و ظاهر را در Style مدیریت کن.</p><hr/></section><section aria-labelledby="concept-v31-10-section-05" class="concept-reference-part"><h3 id="concept-v31-10-section-05">Line Height؛ فضای تنفس عمودی</h3><p>Line Height خیلی کم باعث برخورد بصری سطرها می‌شود. خیلی زیاد، پیوند جمله‌ها را از بین می‌برد.</p><p>برای متن بدنه معمولاً Line Height نسبی بهتر از عدد ثابت پیکسلی است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">line-height: 1.7;
</code></pre></figure><p>عدد مناسب به فونت، اندازه و زبان وابسته است. برای فارسی باید با پاراگراف واقعی، اعداد، پرانتز، لینک و کلمات لاتین ترکیبی آزمایش شود.</p><hr/></section><section aria-labelledby="concept-v31-10-section-06" class="concept-reference-part"><h3 id="concept-v31-10-section-06">طول خط</h3><p>ستون بسیار عریض چشم را مجبور می‌کند مسیر طولانی طی کند و پیدا کردن آغاز خط بعد سخت می‌شود.</p><p>می‌توان با <code class="inline-code" dir="ltr">max-inline-size</code> طول خط را کنترل کرد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.article-text {
  max-inline-size: 42rem;
}
</code></pre></figure><p>واحد <code class="inline-code" dir="ltr">ch</code> می‌تواند برای تخمین طول خط مفید باشد، اما بر اساس عرض نویسهٔ صفر لاتین محاسبه می‌شود؛ پس برای فارسی معیار دقیق نیست. اگر از <code class="inline-code" dir="ltr">60ch</code> استفاده می‌کنی، نتیجه را با فونت واقعی فارسی بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-10-section-07" class="concept-reference-part"><h3 id="concept-v31-10-section-07">Typography سیال با <code class="inline-code" dir="ltr">clamp()</code></h3><p>به‌جای جهش ناگهانی Font Size در چند Breakpoint، می‌توان اندازه را در یک بازه سیال کرد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">font-size: clamp(1.75rem, 1.2rem + 2vw, 3.5rem);
</code></pre></figure><p>تصویر ذهنی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">حداقل ← اندازهٔ سیال با عرض صفحه ← حداکثر
</code></pre></figure><ul>
<li>مقدار اول اجازه نمی‌دهد متن بیش از حد کوچک شود.</li>
<li>مقدار میانی باعث رشد سیال می‌شود.</li>
<li>مقدار آخر جلوی بزرگ‌شدن بی‌نهایت را می‌گیرد.</li>
</ul><p><code class="inline-code" dir="ltr">clamp()</code> معجزه نیست. باید در عرض‌های بسیار کوچک، بسیار بزرگ و با متن طولانی آزمایش شود.</p><hr/></section><section aria-labelledby="concept-v31-10-section-08" class="concept-reference-part"><h3 id="concept-v31-10-section-08">Scale تایپوگرافی</h3><p>به‌جای Font Sizeهای پراکنده:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">17px
21px
29px
34px
43px
</code></pre></figure><p>یک Scale محدود تعریف کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">text-sm
text-md
text-lg
heading-sm
heading-md
heading-lg
</code></pre></figure><p>این نام‌ها می‌توانند Variable یا بخشی از Global Class باشند. هدف این است که هر عدد تصادفی تبدیل به تصمیمی قابل ردیابی شود.</p><hr/></section><section aria-labelledby="concept-v31-10-section-09" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-10-section-09">در Elementor V4</h3><p>برای Typography این سؤال‌ها را بپرس:</p><ol>
<li>نقش معنایی Element چیست؟</li>
<li>Style باید Local باشد یا Global؟</li>
<li>Font Family، Size یا Color باید Variable باشد؟</li>
<li>آیا State مثل Hover برای Link تعریف شده است؟</li>
<li>آیا Mobile فقط Font کوچک‌تر می‌خواهد یا Width و Line Height نیز باید تغییر کنند؟</li>
<li>آیا فونت و Weight انتخاب‌شده واقعاً در Frontend Load می‌شوند؟</li>
</ol><p>Typography یک Heading تکرارشونده معمولاً بهتر است با Global Class و Variableهای محدود مدیریت شود، نه با تنظیم جداگانهٔ ده‌ها Heading.</p><hr/></section><section aria-labelledby="concept-v31-10-section-10" class="concept-reference-part"><h3 id="concept-v31-10-section-10">مثال واقعی: Hero فارسی</h3><p>عنوان کوتاه در طراحی اولیه:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">آینده را بسازید
</code></pre></figure><p>اما عنوان واقعی ممکن است باشد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">زیرساخت یکپارچه برای مدیریت هوشمند عملیات سازمانی
</code></pre></figure><p>اگر فقط با متن کوتاه تست کرده باشی:</p><ul>
<li>ارتفاع Hero تغییر می‌کند؛</li>
<li>دکمه‌ها پایین می‌روند؛</li>
<li>تصویر از تراز خارج می‌شود؛</li>
<li>در ۷۶۸px یک کلمه تنها می‌ماند.</li>
</ul><p>پس تست Typography باید شامل کوتاه‌ترین و بلندترین محتوای واقعی باشد.</p><hr/></section><section aria-labelledby="concept-v31-10-section-11" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-10-section-11">پل به DevTools</h3><p>در Computed Style این موارد را ببین:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">font-family
font-size
font-weight
line-height
letter-spacing
word-break
overflow-wrap
max-inline-size
</code></pre></figure><p>در Inspect Tooltip معمولاً Font، Contrast و ابعاد Box نیز قابل مشاهده‌اند. اگر فونت دیگری نمایش داده می‌شود، مشکل فقط Style نیست؛ ممکن است فایل فونت، Weight یا مسیر Load درست نباشد.</p><hr/></section><section aria-labelledby="concept-v31-10-section-12" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-10-section-12">اشتباهات رایج</h3><ul>
<li>استفاده از Heading فقط برای بزرگ‌کردن متن</li>
<li>اندازه‌های پراکنده بدون Scale</li>
<li>Line Height بسیار کم در فارسی</li>
<li>استفاده از <code class="inline-code" dir="ltr">ch</code> بدون آزمایش فونت فارسی</li>
<li>تست فقط با Lorem Ipsum یا متن کوتاه</li>
<li>تنظیم Font Weightای که فایل آن Load نشده است</li>
<li>کوچک‌کردن افراطی متن Mobile برای جا دادن Layout اشتباه</li>
</ul><hr/></section><section aria-labelledby="concept-v31-10-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-10-section-13">تصویر ذهنی نهایی</h3><p>Typography مثل موسیقی است. Font جنس صداست، اما ریتم خواندن را فاصله، طول خط، وزن و سلسله‌مراتب می‌سازند.</p><hr/></section><section aria-labelledby="concept-v31-10-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-10-section-14">قوانین طلایی</h3><ul>
<li><strong>«HTML نقش متن را تعیین می‌کند؛ Class ظاهر آن را.»</strong></li>
<li><strong>«خوانایی حاصل یک عدد Font Size نیست؛ حاصل یک سیستم است.»</strong></li>
<li><strong>«Typography فارسی را با متن واقعی فارسی آزمایش کن.»</strong></li>
<li><strong>«<code class="inline-code" dir="ltr">clamp()</code> اندازه را سیال می‌کند، اما جای تست را نمی‌گیرد.»</strong></li>
<li><strong>«اگر متن بلند Layout را می‌شکند، فقط متن مقصر نیست؛ قرارداد Container را بررسی کن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>CSS Values and Units / CSS Text specifications</li>
<li>Elementor Help: Typography controls, Variables and Editor V4 differences</li>
<li>Chrome DevTools CSS and font inspection references</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-10-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-10-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Typography؛ rem، em، px و vw مرجع‌های متفاوت دارند</span></summary>
<section aria-labelledby="lesson-10-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Font Size فقط یک عدد نیست. `rem` به root، `em` در font-size به والد، `px` به طول CSS و `vw` به عرض viewport وابسته است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> چهار خط‌کش داری: خط‌کش ثابت px، خط‌کش دفترچهٔ مرکزی rem، خط‌کش محلی والد em و خط‌کش پهنای پنجره vw.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Font Size</th><td><code dir="ltr">font-size</code></td><td>PX، EM، REM، VW در Help Center</td><td>px ثابت؛ em والد؛ rem root؛ vw viewport</td><td>rem انتخاب پایهٔ مناسب برای scale سراسری است.</td><td>vw تنها بدون حد می‌تواند متن خیلی کوچک/بزرگ بسازد.</td><td><code dir="ltr">E_TYPO_GENERAL</code></td></tr><tr><th scope="row">Line Height</th><td><code dir="ltr">line-height</code></td><td>در Help قدیمی px یا em؛ در CSS عدد بدون واحد هم معتبر است</td><td>font-size جاری</td><td>عدد بدون واحد برای نسبت پایدار در CSS مفید است.</td><td>واحدهای UI را با قابلیت CSS اشتباه نگیر.</td><td><code dir="ltr">E_TYPO_GENERAL</code></td></tr><tr><th scope="row">Letter / Word spacing</th><td><code dir="ltr">letter-spacing / word-spacing</code></td><td>PX یا EM در Help Center</td><td>font-size جاری در em</td><td>برای تنظیم ظریف و محدود.</td><td>Spacing زیاد خوانایی را کاهش می‌دهد.</td><td><code dir="ltr">E_TYPO_GENERAL</code></td></tr><tr><th scope="row">Font Weight</th><td><code dir="ltr">font-weight</code></td><td>keyword یا عدد مانند 400/700</td><td>بدون واحد</td><td>براساس font موجود.</td><td>عدد وزن با px ارتباط ندارد.</td><td><code dir="ltr">E_TYPO</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>root=16px → 2rem=32px. اگر parent font-size=20px باشد، child با 2em=40px. همان «2» دو نتیجهٔ متفاوت دارد چون مرجع فرق کرده است.</p></section>
<section><h3>📱 در Responsive</h3><p>مقدار Font Size می‌تواند per breakpoint override شود. واحد را فقط برای تغییر منطق scaling عوض کن، نه صرفاً برای کوچک‌کردن عدد.</p></section>
<section><h3>🔬 در DevTools</h3><p>font-size، line-height و inherited source را در Computed بررسی کن؛ root font-size را هم ثبت کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/style-tab-typography/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Typography</a>، <a href="https://elementor.com/help/what-is-typography/" rel="noopener noreferrer" target="_blank">Elementor — Typography and units</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length" rel="noopener noreferrer" target="_blank">MDN — CSS length values</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-10-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-10-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — Intro و Feature List</h3><p>داخل Platform Copy:</p><ol>
<li>Paragraph برای متن معرفی بساز؛</li>
<li>Class <code class="inline-code" dir="ltr">c-platform-intro</code> را همان لحظه ایجاد کن؛</li>
<li>Div Block برای Feature List بساز؛</li>
<li>اولین Feature Item را با Flexbox Row بساز؛</li>
<li>یک Dot یا SVG کوچک و یک Paragraph داخل آن قرار بده؛</li>
<li>حالا Classهای <code class="inline-code" dir="ltr">c-feature-item</code> و <code class="inline-code" dir="ltr">c-feature-text</code> را بساز؛</li>
<li>Item را تکثیر کن.</li>
</ol><h3>چرا Bullet را داخل متن تایپ نمی‌کنیم؟</h3><p>چون Icon و Text باید مستقل Align، Gap و Style شوند.</p><h3>❓ سؤال توقف</h3><p>متن معرفیٔ مستقل Heading است یا Paragraph؟</p><details class="disclosure-card"><summary>پاسخ</summary>Paragraph.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> برای کنترل خط‌شکنی، داخل Paragraph چند <code class="inline-code" dir="ltr">&lt;br&gt;</code> دستی بگذاری.</p><p><strong>نشانه:</strong> Desktop خوب است، ولی Mobile یا ترجمه بد می‌شکند.</p><h3>🧪 عمداً خرابش کن</h3><p>داخل هر خط ویژگی یک Break دستی اضافه کن و عرض Copy را کم کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>شکست‌ها در محل نامناسب می‌مانند؛</li>
<li>فاصله‌های عجیب یا سطرهای کوتاه ایجاد می‌شوند؛</li>
<li>متن ترجمه‌شده احتمالاً نامتعادل می‌شود.</li>
</ul><p>Breakهای غیرمعنایی را حذف کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-154-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-154-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-55"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-55-1" name="chk-55-1" type="checkbox"/><span>Intro با Paragraph ساخته شده</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-55-2" name="chk-55-2" type="checkbox"/><span>Featureها Itemهای تکراری مستقل‌اند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-55-3" name="chk-55-3" type="checkbox"/><span>Dot و Text با Flexbox تراز شده‌اند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-55-4" name="chk-55-4" type="checkbox"/><span>Break دستی غیرضروری ندارم</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Heading و Paragraph براساس چه چیزی انتخاب می‌شوند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> یک Paragraph با چند <code class="inline-code" dir="ltr">&lt;br&gt;</code> در Mobile بد Wrap می‌شود؛ راه تصمیم‌گیری تو چیست؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-56"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-56-1" name="chk-56-1" type="checkbox"/><span>Element معنایی را براساس نقش محتوا انتخاب کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-56-2" name="chk-56-2" type="checkbox"/><span>Heading hierarchy و Paragraph را با ظاهر یکی نگرفته است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-56-3" name="chk-56-3" type="checkbox"/><span>Hard Break را فقط با دلیل معنایی یا Art Direction پذیرفته است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-10-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-10-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-CONTENT-BR-001</h3><p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">context_dependent</code></p><p>در Export چند Heading و Paragraph دارای Break صریح‌اند. Break هنری در Heading ممکن است قابل دفاع باشد؛ Break دستی در Paragraph معمولاً شکننده‌تر است.</p><h3>واژه‌ها را اشتباه نگیر</h3><section aria-labelledby="section-hidden-157-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-157-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Element</dt><dd>کل واحد HTML</dd><dt>Tag</dt><dd>علامت شروع/پایان</dd><dt>Class</dt><dd>نام Style قابل استفاده</dd><dt>Heading</dt><dd>نقش محتوایی</dd></dl></section><h3>🔬 پشت صحنه</h3><p>Line Height و Width متن روی Wrap اثر می‌گذارند. نیازی به نوشتن دستی CSS نیست.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-10-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-10-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-58"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-58-1" name="chk-58-1" type="checkbox"/><span>می‌توانی Heading، Paragraph و List را براساس معنی محتوا انتخاب کنی، نه فقط ظاهر.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-58-2" name="chk-58-2" type="checkbox"/><span>می‌توانی توضیح بدهی چرا Hard Line Break در Paragraph می‌تواند Responsive را شکننده کند.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-59"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-59-1" name="chk-59-1" type="checkbox"/><span>Intro، Feature List و متن‌های TUYA را با Element معنایی مناسب می‌سازی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-59-2" name="chk-59-2" type="checkbox"/><span>با متن طولانی و Zoom بررسی می‌کنی که محتوا بدون برخورد Wrap می‌شود.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-60"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-60-1" name="chk-60-1" type="checkbox"/><span>برای یک بخش FAQ می‌توانی سلسله‌مراتب Heading و Paragraph مناسب را پیشنهاد بدهی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-10-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-10-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد رسانه‌ها، Logoها و قاب Visual را کامل می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 10</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-10-completion"><fieldset><legend>ثبت پایان درس 10</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-10-complete" name="lesson-10-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-10-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Typography Variable در برابر Typography Class</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Typography Variable</h3><p>Variable مقدار خام نگه می‌دارد؛ مثل <code dir="ltr">font-body</code> یا <code dir="ltr">size-h2</code>. این‌ها مادهٔ خام سیستم تایپوگرافی‌اند.</p></section>
<section class="inline-compare-card"><h3>Typography Class</h3><p>Class یک تصمیم کامل ظاهری است؛ مثلاً <code dir="ltr">section-title</code> می‌تواند font، size، line-height، color و spacing را با هم کنترل کند.</p><p class="golden-rule">قانون طلایی: مقدار را Variable کن؛ نقش متنی تکرارشونده را Global Class کن.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="lesson-10-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Typography و طول خط در Mobile</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>Elementor اجازه می‌دهد Typography و spacing را برای Mobile جدا تنظیم کنی. در طرح TUYA، پاراگراف و لیست در ستون باریک‌تر قرار گرفته‌اند؛ اندازه، line-height و عرض متن باید در Mobile بررسی شوند.</p>
<p>متن انگلیسی داخل صفحهٔ RTL باید در wrapper دارای <code>dir="ltr"</code> یا isolation مناسب قرار بگیرد.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-10-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Typography، طول خط و متن واقعی</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> Typography را با محتوای واقعی و عرض واقعی Mobile آزمایش کن.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>Heading، Paragraph و List پروژه TUYA را با متن نهایی وارد کن.</li><li>Desktop را baseline بگیر و Tablet/Mobile را از نظر شکست خط و فاصله بررسی کن.</li><li>فقط مقادیر لازم Typography و spacing را در breakpoint کوچک‌تر override کن.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>قبل از تغییر font-size بگو مشکل از اندازهٔ فونت است یا Width/Max Width ستون متن.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>Heading را با اندازهٔ Desktop و Width بسیار باریک نگه دار.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>font-size، line-height، letter-spacing، Width/Max Width و تعداد خطوط.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> متن خواناست، سطرها بیش از حد کوتاه یا بلند نیستند و inheritance بی‌دلیل شکسته نشده است.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-10-responsive-build-test-done-build"><input data-persist="" id="lesson-10-responsive-build-test-done-build" name="lesson-10-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-10-responsive-build-test-done-test"><input data-persist="" id="lesson-10-responsive-build-test-done-test" name="lesson-10-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-10-responsive-build-test-done-debug"><input data-persist="" id="lesson-10-responsive-build-test-done-debug" name="lesson-10-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-10-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-10-responsive-build-test-note" name="lesson-10-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/responsive-editing/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-10-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Typography scale</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
