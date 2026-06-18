<article class="lesson card-surface" data-lesson="2" id="lesson-2"><h2 class="lesson-title former-h1">درس 2 — Element Tree و انتخاب Element مناسب</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-2-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-2-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> نقش Div Block، Flexbox و Grid و رابطهٔ Parent/Child را.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام گزینه‌های Grid یا Flex را.</p><p><strong>در پایان باید بتوانی:</strong> برای هر بخش، Element مناسب را براساس نقش انتخاب کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-2-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-2-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧩 ساختاری + 🛠 اجرایی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۱۵–۲۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۱۵–۲۵ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> Tree را با نقش Elementها می‌سازی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-2-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-2-lesson-understand-4">A. بفهم</h2><h3>مسئله</h3><p>بیشتر آشفتگی‌ها از اینجا شروع می‌شوند: Element اشتباه برای نقش اشتباه.</p><h3>Decision Tree دیداری</h3><section aria-labelledby="section-hidden-45-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-45-heading">بخش آموزشی</h2><ul><li>◇ فقط Wrapper سبک لازم داری؟</li>
<li>├─ بله → □ Div Block</li>
<li>└─ خیر</li>
<li>◇ فرزندان روی یک محورند؟</li>
<li>├─ بله → □ Flexbox</li>
<li>└─ خیر</li>
<li>◇ ردیف و ستون را هم‌زمان کنترل می‌کنی؟</li>
<li>├─ بله → □ Grid</li>
<li>└─ خیر → ساختار را دوباره تحلیل کن</li></ul></section><h3>نقش‌ها</h3><div aria-label="جدول آموزشی دوره — نقش‌ها" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — نقش‌ها</caption><thead><tr><th scope="col">Element</th><th scope="col">نقش اصلی</th></tr></thead><tbody><tr><th scope="row">Div Block</th><td>پوسته و گروه‌بندی سبک</td></tr><tr><th scope="row">Flexbox</th><td>چیدمان یک‌بعدی فرزندان</td></tr><tr><th scope="row">Grid</th><td>کنترل ردیف و ستون</td></tr><tr><th scope="row">Heading</th><td>عنوان معنایی</td></tr><tr><th scope="row">Paragraph</th><td>متن مستقل</td></tr><tr><th scope="row">Image</th><td>تصویر محتوایی</td></tr><tr><th scope="row">SVG</th><td>Icon یا گرافیک برداری</td></tr></tbody></table></div><h3>Parent و Child</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای Element Tree و رابطهٔ Parent / Child">
<h4>راهنمای مبتدی برای Element Tree و رابطهٔ Parent / Child</h4>
<p>قبل از اینکه به درخت نگاه کنی، آن را مثل خانواده یا پوشه‌بندی ببین: هر چیزی یا ظرف است یا داخل ظرف دیگری قرار دارد.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="Parent">
<h4><span class="term-en" dir="ltr">Parent</span> — والد / ظرف</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Parent ظرفی است که چند عنصر داخل آن قرار می‌گیرند.</li>
<li><strong>۲. مثال روزمره:</strong> مثل جعبه‌ای که چند کارت داخلش است.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> در Screenshot معمولاً ناحیهٔ بزرگ‌تر یا ستون اصلی است.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> ظرف والد یا Section که عناصر داخلش قرار دارند.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> فقط به ظاهر نگاه می‌کنم و Parent واقعی را نمی‌سازم.</li>
<li><strong>۶. تصمیم درست:</strong> اول ظرف را بساز، بعد Childها را داخلش بگذار.</li>
<li><strong>۷. تمرین کوچک:</strong> سه چیز داخل یک ستون را پیدا کن و بگو Parent مشترکشان چیست.</li>
</ol>
</article>
<article class="concept-card" data-concept="Child">
<h4><span class="term-en" dir="ltr">Child</span> — فرزند / داخل ظرف</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Child عنصری است که داخل Parent قرار دارد.</li>
<li><strong>۲. مثال روزمره:</strong> مثل کتاب داخل قفسه.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> عنوان، متن، لوگو یا Nodeهایی که داخل ناحیهٔ بزرگ‌تر هستند.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Element/Widget آماده یا ظرف والد داخلی.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> Child را بیرون از Parent می‌سازم و بعد با Margin شبیه‌سازی می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> اگر از نظر معنایی داخل همان بخش است، واقعاً داخل همان ظرف والد بساز.</li>
<li><strong>۷. تمرین کوچک:</strong> یک دکمه را انتخاب کن و بگو داخل کدام Parent باید باشد.</li>
</ol>
</article>
<article class="concept-card" data-concept="Grandchild">
<h4><span class="term-en" dir="ltr">Grandchild</span> — فرزندِ فرزند</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Grandchild چیزی است که داخل Child قرار می‌گیرد.</li>
<li><strong>۲. مثال روزمره:</strong> مثل عکس داخل کارت داخل ستون.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> آیتم‌های کوچک‌تر داخل کارت یا Visual Stage.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Inner ظرف والد یا Element/Widget آماده داخل یک Child ظرف والد.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> همهٔ عمق‌ها را حذف می‌کنم و با فاصله ظاهری درستش می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> عمق را فقط وقتی بساز که نقش واقعی دارد.</li>
<li><strong>۷. تمرین کوچک:</strong> یک کارت ویژگی را بشکن: کارت، آیکن، متن؛ هر کدام چه نقشی دارند؟</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">Element Tree</dt><dd>نقشهٔ خانوادهٔ عناصر صفحه</dd>
<dt dir="ltr">Parent</dt><dd>ظرفی که چیزهای دیگر داخل آن هستند</dd>
<dt dir="ltr">Child</dt><dd>چیزی که داخل یک Parent قرار دارد</dd>
<dt dir="ltr">Grandchild</dt><dd>چیزی که داخل Child قرار دارد</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">در Elementor اول Navigator را مثل درخت بخوان، بعد Style بده.</p>
</aside>
</section><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Parent
|
+-- Child A
+-- Child B
    |
    +-- Grandchild</pre></figure></details><p>Controlهای Layout والد معمولاً روی فرزندان مستقیم اثر می‌گذارند.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="bc85265e9472b02817fc1466f71195a6131cb7ad26ad8f6f4a37dc8eb6615ad1" id="lesson-2-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Element Tree و انتخاب ظرف درست</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="2" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-02-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-02-section-01">مسئله‌ای که این مفهوم حل می‌کند</h3><p>بسیاری از خطاهای Layout در واقع خطای CSS نیستند. عناصر در Parent نامناسب قرار گرفته‌اند.</p><p>فرض کن عنوان و دکمه باید با هم در سمت راست کارت حرکت کنند، اما هرکدام در Wrapper جدا و دور از هم هستند. هرچقدر Margin و Position بدهی، رابطهٔ واقعی آن‌ها اصلاح نشده است.</p><hr/></section><section aria-labelledby="concept-v31-02-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-02-section-02">تشبیه به دنیای واقعی: پوشه‌های کامپیوتر</h3><p>Element Tree را مثل ساختار پوشه‌ها تصور کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Project
├── Images
│   ├── hero.jpg
│   └── logo.svg
└── Documents
    ├── proposal.pdf
    └── invoice.pdf
</code></pre></figure><p>اگر فایل‌های مربوط به یک موضوع در پوشه‌های پراکنده باشند، مدیریتشان سخت می‌شود.</p><p>در Tree:</p><ul>
<li><strong>Parent</strong> = پوشه</li>
<li><strong>Child</strong> = چیزی که مستقیم داخل پوشه است</li>
<li><strong>Sibling</strong> = دو مورد هم‌سطح با Parent مشترک</li>
<li><strong>Descendant</strong> = هر چیزی در عمق زیرشاخه</li>
<li><strong>Ancestor</strong> = هر Parent در مسیر بالاتر</li>
</ul><hr/></section><section aria-labelledby="concept-v31-02-section-03" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-02-section-03">چرا Tree وجود دارد؟</h3><p>مرورگر برای Layout، inheritance، انتخابگرهای CSS، دسترسی‌پذیری و رویدادها باید بداند چه چیزی داخل چه چیزی است.</p><p>ساختار فقط برای مرتب‌بودن پنل Navigator نیست؛ رفتار صفحه از آن ساخته می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-02-section-04" class="concept-reference-part"><h3 id="concept-v31-02-section-04">سه نوع ظرف را با یک ساختمان مقایسه کن</h3><h4>Div Block: اتاق خالی</h4><p>Div یک ظرف عمومی و سبک است. خودش الزاماً موتور پیچیدهٔ توزیع ندارد.</p><p>کاربرد:</p><ul>
<li>گروه‌بندی معنایی یا بصری</li>
<li>ساخت Shell</li>
<li>ایجاد مرجع Position</li>
<li>اعمال Background، Border یا Padding مشترک</li>
</ul><h4>Flex Container: راهروی یک‌محوره</h4><p>Flex برای توزیع Childها در یک محور اصلی طراحی شده است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Row:    A → B → C
Column: A
        ↓
        B
        ↓
        C
</code></pre></figure><h4>Grid Container: نقشهٔ خانه با ردیف و ستون</h4><p>Grid وقتی مفید است که جای‌گذاری هم‌زمان در دو بُعد مهم باشد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">┌───────┬───────┐
│   A   │   B   │
├───────┼───────┤
│   C   │   D   │
└───────┴───────┘
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-02-section-05" class="concept-reference-part"><h3 id="concept-v31-02-section-05">اصل «کمترین موتور لازم»</h3><p>قرار نیست همه‌چیز Flex یا Grid باشد.</p><p>از خودت بپرس:</p><ul>
<li>فقط گروه‌بندی می‌خواهم؟ → Div</li>
<li>توزیع روی یک محور می‌خواهم؟ → Flex</li>
<li>رابطهٔ ردیف و ستون می‌خواهم؟ → Grid</li>
</ul><p>موتور قوی‌تر همیشه انتخاب بهتر نیست. موتور اضافی کنترل‌های بیشتر، CSS بیشتر و پیچیدگی ذهنی بیشتر می‌آورد.</p><hr/></section><section aria-labelledby="concept-v31-02-section-06" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-02-section-06">مثال واقعی در Elementor</h3><p>یک کارت محصول:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Product Card
├── Media
│   ├── Image
│   └── Badge
└── Content
    ├── Title
    ├── Price Row
    │   ├── Current Price
    │   └── Old Price
    └── Button
</code></pre></figure><p>تصمیم‌ها:</p><ul>
<li>Product Card: Div یا Flex Column</li>
<li>Media: Div با <code class="inline-code" dir="ltr">position: relative</code></li>
<li>Badge: فرزند absolute داخل Media</li>
<li>Price Row: Flex Row</li>
<li>Content: Flex Column با Gap</li>
</ul><p>اگر Badge مستقیم داخل Product Card باشد، مرجع Position بزرگ‌تر و مبهم‌تر می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-02-section-07" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-02-section-07">رفتار قدم‌به‌قدم</h3><ol>
<li>تمام نقش‌ها را قبل از ساخت نام‌گذاری کن.</li>
<li>مواردی را که باید با هم حرکت، مخفی یا Style شوند زیر Parent مشترک بگذار.</li>
<li>فقط Childهای مستقیم Parent از Layout همان Parent فرمان می‌گیرند.</li>
<li>اگر یک Wrapper هیچ مسئولیتی ندارد، احتمالاً قابل حذف است.</li>
<li>اگر یک Wrapper چند مسئولیت نامرتبط دارد، احتمالاً باید شکسته شود.</li>
</ol><hr/></section><section aria-labelledby="concept-v31-02-section-08" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-02-section-08">تله‌های رایج</h3><h4>تلهٔ ۱: Wrapper برای هر Element</h4><p>هر Heading نیاز به Div جدا ندارد. Wrapper باید مسئولیت داشته باشد.</p><h4>تلهٔ ۲: Parent بسیار بزرگ</h4><p>اگر کل Section را Flex Row کنی اما فقط دو Child کوچک باید کنار هم باشند، کنترل Layout بیش از حد گسترده می‌شود.</p><h4>تلهٔ ۳: استفاده از Absolute برای جایگزینی Tree</h4><p>Absolute برای Overlay است، نه برای ساختن Layout اصلی صفحه.</p><h4>تلهٔ ۴: اشتباه‌گرفتن Child با Descendant</h4><p>Flex فقط Child مستقیم را Flex Item می‌کند؛ نوه‌ها توسط Flex Parent بالاتر مستقیماً چیده نمی‌شوند.</p><hr/></section><section aria-labelledby="concept-v31-02-section-09" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-02-section-09">روش تشخیص سریع</h3><p>از هر Wrapper بپرس:</p><blockquote>
<p>اگر این Wrapper را حذف کنم، کدام مسئولیت واقعی از بین می‌رود؟</p>
</blockquote><p>اگر پاسخ «هیچ‌چیز» است، Wrapper احتمالاً اضافی است.</p><hr/></section><section aria-labelledby="concept-v31-02-section-10" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-02-section-10">تصویر ذهنی نهایی</h3><p>Element Tree مثل ساختار پوشه‌هاست. اگر فایل‌ها در پوشهٔ اشتباه باشند، نام‌گذاری زیبا مشکل رابطه را حل نمی‌کند. هر Parent باید دقیقاً همان گروهی را مدیریت کند که یک قانون مشترک دارند.</p></section><section aria-labelledby="concept-v31-02-section-11" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-02-section-11">قوانین طلایی</h3><ul>
<li><strong>«Tree نقشهٔ قدرت است؛ Parent تعیین می‌کند Childها چگونه رفتار کنند.»</strong></li>
<li><strong>«Siblingها فقط وقتی با یک قانون مشترک چیده می‌شوند که Parent مشترک معنادار داشته باشند.»</strong></li>
<li><strong>«Div برای گروه‌بندی، Flex برای یک محور، Grid برای دو محور.»</strong></li>
<li><strong>«کمترین موتور لازم، بهترین نقطهٔ شروع است.»</strong></li>
<li><strong>«Wrapper بدون مسئولیت، بدهی ساختاری است.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Div Block element</li>
<li>Elementor Help: Flexbox element</li>
<li>Elementor Help: Grid Container</li>
<li>CSS Display, Flexbox and Grid specifications</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-2-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-2-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Element Tree واحد ندارد؛ Layout داخل آن واحد می‌گیرد</span></summary>
<section aria-labelledby="lesson-2-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Parent، Child و Sibling رابطه‌اند، نه اندازه. واحدها وقتی وارد می‌شوند که برای ظرف انتخاب‌شده Width، Gap، Padding یا Track تعریف کنی.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> نقشهٔ خانوادگی قد و وزن نیست؛ فقط می‌گوید چه کسی فرزند چه کسی است. بعداً می‌توانی برای هر عضو اندازه ثبت کنی.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">نوع Element</th><td><code dir="ltr">Div / Flexbox / Grid</code></td><td>انتخاب Element</td><td>بدون واحد</td><td>براساس مسئولیت واقعی Parent انتخاب شود.</td><td>Element سنگین‌تر را صرفاً برای داشتن یک کنترل اضافه انتخاب نکن.</td><td><code dir="ltr">E_LAYOUT</code></td></tr><tr><th scope="row">Display</th><td><code dir="ltr">display</code></td><td>block / flex / grid / none</td><td>keyword</td><td>رفتار childها را تعیین می‌کند.</td><td>Display را با Width اشتباه نگیر.</td><td><code dir="ltr">E_LAYOUT</code></td></tr><tr><th scope="row">فاصلهٔ Childها</th><td><code dir="ltr">gap</code></td><td>واحد طول یا درصد بسته به کنترل</td><td>Parent layout</td><td>فقط بعد از ساخت Tree درست.</td><td>Gap ساختار اشتباه را درمان نمی‌کند.</td><td><code dir="ltr">E_FLEX_GAP</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>not_applicable — ابتدا Tree را درست کن؛ محاسبهٔ Gap در درس‌های Flex/Grid می‌آید.</p></section>
<section><h3>📱 در Responsive</h3><p>Tree معنایی را برای هر breakpoint حفظ کن؛ فقط order/direction/size را در صورت نیاز override کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>در Elements panel رابطهٔ DOM را ببین؛ Computed فقط Style را نشان می‌دهد و جای Tree را نمی‌گیرد.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/style-tab-layout/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Layout</a>، <a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-2-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-2-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — Tree بدون Style</h3><p>در V4 این ساختار را بساز:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Div Block: Platform Section
|
+-- Flexbox: Platform Main
    |
    +-- Div Block: Platform Copy
    +-- Div Block: Platform Visual</pre></figure></details><p>فعلاً فقط نام Elementها را در Structure مرتب کن. Class مشترک هنوز نساز.</p><h3>چرا؟</h3><dl class="term-grid"><dt>Section فقط پوسته است</dt><dd>Div Block؛</dd><dt>Main دو فرزند روی یک محور دارد</dt><dd>Flexbox؛</dd><dt>Copy و Visual فعلاً فقط Wrapper هستند</dt><dd>Div Block.</dd></dl><h3>❓ سؤال توقف</h3><p>برای یک Icon و متن که باید کنار هم باشند، کدام انتخاب اولیه مناسب‌تر است؟</p><form class="interactive-form stop-question-form" data-persist-group="stop-question-2"><fieldset><legend>چک‌لیست یادگیری</legend><label class="choice-row"><input data-persist="radio" id="radio-2-a" name="stop-question-2" type="radio" value="A"/><span>A) Grid سه‌ستونه</span></label><label class="choice-row"><input data-persist="radio" id="radio-2-b" name="stop-question-2" type="radio" value="B"/><span>B) Flexbox</span></label><label class="choice-row"><input data-persist="radio" id="radio-2-c" name="stop-question-2" type="radio" value="C"/><span>C) Absolute</span></label></fieldset></form><details class="disclosure-card"><summary>پاسخ</summary>B.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> برای هر گروه کوچک یک Flexbox جدید بسازی.</p><p><strong>نشانه:</strong> Tree سریعاً چندلایه می‌شود، بدون اینکه هر لایه وظیفه‌ای داشته باشد.</p><p><strong>قاعده:</strong> هر Wrapper باید دلیل Semantic، Layout، Scope، Position یا Component داشته باشد.</p><h3>🧪 عمداً خرابش کن</h3><p>سه Wrapper خالی بین Platform Section و Platform Main اضافه کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>Structure خوانایی کمتری دارد؛</li>
<li>انتخاب Parent درست سخت‌تر می‌شود؛</li>
<li>Style ممکن است روی لایهٔ اشتباه اعمال شود؛</li>
<li>ظاهر شاید هنوز فرق نکند، اما نگهداری سخت‌تر می‌شود.</li>
</ul><p>سپس Wrapperهای بی‌دلیل را حذف کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-47-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-47-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-7"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-7-1" name="chk-7-1" type="checkbox"/><span>Tree فقط چهار Element اصلی دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-7-2" name="chk-7-2" type="checkbox"/><span>Main فرزند مستقیم Section است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-7-3" name="chk-7-3" type="checkbox"/><span>Copy و Visual فرزند مستقیم Main هستند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-7-4" name="chk-7-4" type="checkbox"/><span>هیچ Position یا Style اضافه نشده</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Parent و Child چه تفاوتی دارند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> برای Header شامل Logo، Menu و CTA یک Tree سه‌سطحی پیشنهاد بده.</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-8"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-8-1" name="chk-8-1" type="checkbox"/><span>رابطهٔ Parent/Child را درست تشخیص داده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-8-2" name="chk-8-2" type="checkbox"/><span>Div Block، Flexbox یا Grid را براساس نقش انتخاب کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-8-3" name="chk-8-3" type="checkbox"/><span>دلیل انتخاب به تعداد محورهای Layout مربوط است، نه ظاهر موقت.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-2-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-2-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-HOME2-DOM-001</h3><p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">improvement_candidate</code></p><p>در Export، چند Element ساختاری بدون Child دیده شده‌اند. این شواهد حذف فوری نیست.</p><p>سؤال‌ها:</p><section aria-labelledby="section-hidden-50-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-50-heading">بخش آموزشی</h2><ul><li>آیا Spacer یا Grid Cell هستند؟</li>
<li>آیا Selector یا Background به آن‌ها وابسته است؟</li>
<li>آیا Runtime بدون آن‌ها تغییر می‌کند؟</li></ul></section><p>نتیجهٔ درست فعلی: <code class="inline-code" dir="ltr">insufficient_evidence</code>.</p><h3>🔬 پشت صحنه</h3><p>Flexbox و Grid سیستم‌های Layout هستند؛ Div Block صرفاً یک Element عمومی است. لازم نیست کد آن‌ها را حفظ کنی.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-2-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-2-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-10"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-10-1" name="chk-10-1" type="checkbox"/><span>می‌توانی Parent، Child و Sibling را در یک Tree واقعی تشخیص بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-10-2" name="chk-10-2" type="checkbox"/><span>می‌توانی تفاوت نقش Div Block، Flexbox و Grid را بدون اشاره به ظاهر موقت توضیح بدهی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-11"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-11-1" name="chk-11-1" type="checkbox"/><span>برای پوسته، چیدمان یک‌محوری و ساختار ردیف‌وستون Element مناسب را انتخاب می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-11-2" name="chk-11-2" type="checkbox"/><span>Tree اولیهٔ TUYA را بدون Style و بدون Wrapper اضافی می‌سازی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-12"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-12-1" name="chk-12-1" type="checkbox"/><span>برای یک Header شامل Logo، Menu و Button می‌توانی Element Tree پیشنهادی خود را رسم و دلیل انتخاب‌ها را بیان کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-2-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-2-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد Class را فقط برای Elementهایی که همین حالا ساخته‌ای ایجاد می‌کنیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 2</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-2-completion"><fieldset><legend>ثبت پایان درس 2</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-2-complete" name="lesson-2-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-2-section-shell-title" role="heading">اصلاح مهم نسخه 22 — Platform Section یعنی چه؟</span></summary><section aria-labelledby="lesson-2-section-shell-title" class="smart-note-card disclosure-content terminology-fix-card">
<p>در تمرین TUYA، عبارت <strong>Platform Section</strong> نام معنایی یک لایه است، نه نام یک Element مستقل در Editor V4. دستور دقیق این است: <strong>یک Div Block بساز و نامش را Platform Section بگذار.</strong></p>
<p>پس در ذهن خودت این دو را جدا نگه دار: <span class="pill">Element واقعی: Div Block</span> <span class="pill">نقش طراحی: Section Shell</span></p>
</section></details><details class="lesson-disclosure" id="lesson-2-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — ترتیب DOM در برابر ترتیب Mobile</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p><strong>در طرح Mobile TUYA:</strong> Visual بالاتر از Copy دیده می‌شود. این مشاهده به‌تنهایی مشخص نمی‌کند ترتیب DOM عوض شده یا Custom Order استفاده شده است.</p>
<ul><li>ابتدا DOM را بر اساس ترتیب خواندن و دسترسی‌پذیری بساز.</li><li>اگر Mobile به ترتیب بصری دیگری نیاز دارد، در breakpoint مربوط Custom Order یا Direction را تنظیم کن.</li><li>برای این تغییر، نسخهٔ تکراری و مخفی از همان Section نساز.</li></ul>
<p class="evidence-line"><strong>مبنای رسمی:</strong> Elementor تغییر Order در هر breakpoint را پشتیبانی می‌کند و آن را جایگزینی برای Sectionهای تکراری و مخفی معرفی می‌کند.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-2-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: ترتیب DOM در برابر Custom Order</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> بدون Duplicate کردن سکشن، تفاوت ترتیب خواندن و ترتیب بصری را ببین.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>در Main Container سه فرزند ساده با نام‌های Visual، Copy و Logo Strip بساز.</li><li>ترتیب DOM را یک‌بار ثبت کن و در Desktop همان ترتیب را نگه دار.</li><li>در Mobile فقط در صورت نیاز با Order، Visual را پیش از Copy نمایش بده.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن Screen Reader و Tab Order از کدام ترتیب پیروی می‌کنند و ترتیب بصری چه چیزی را تغییر می‌دهد.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>یک نسخهٔ دوم از همان سکشن بساز و یکی را در Desktop و دیگری را در Mobile مخفی کن؛ سپس DOM و نگهداری را مقایسه کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>Navigator/Element Tree، کنترل Order در breakpoint Mobile و ترتیب DOM در تب Elements مرورگر.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> فقط یک ساختار اصلی وجود دارد، ترتیب خواندن منطقی است و Mobile بدون سکشن تکراری به طرح نزدیک می‌شود.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-2-responsive-build-test-done-build"><input data-persist="" id="lesson-2-responsive-build-test-done-build" name="lesson-2-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-2-responsive-build-test-done-test"><input data-persist="" id="lesson-2-responsive-build-test-done-test" name="lesson-2-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-2-responsive-build-test-done-debug"><input data-persist="" id="lesson-2-responsive-build-test-done-debug" name="lesson-2-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-2-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-2-responsive-build-test-note" name="lesson-2-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/advanced-widget-settings-order/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details></article>
