<article class="lesson card-surface" data-lesson="13" id="lesson-13"><h2 class="lesson-title former-h1">درس 13 — Z-index، Overflow و Layering</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-13-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-13-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> ترتیب بصری لایه‌ها و اثر Overflow را بفهمی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام جزئیات Stacking Context را.</p><p><strong>در پایان باید بتوانی:</strong> Core، Cloud، Glow و Nodeها را بدون عددهای تصادفی مدیریت کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-13-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-13-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🔍 عیب‌یابی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> Stacking Context با عدد Z-index حل نمی‌شود.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-13-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-13-lesson-understand-4">A. بفهم</h2><h3>مدل لایه‌ها</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای Z-index، Overflow و Layering">
<h4>راهنمای مبتدی برای Z-index، Overflow و Layering</h4>
<p>لایه‌ها را مثل چند کاغذ روی میز ببین: بعضی جلوترند، بعضی عقب‌تر، و بعضی ممکن است از قاب بیرون بزنند.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="Layering">
<h4><span class="term-en" dir="ltr">Layering</span> — چند لایه روی هم</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Layering یعنی ترتیب جلو/عقب عناصر.</li>
<li><strong>۲. مثال روزمره:</strong> مثل کاغذهایی که روی هم گذاشته‌ای.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Glow پشت Core، Nodeها جلوتر، Badge روی تصویر.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> ترتیب DOM، Position و Z-index.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> بدون برنامه عددهای بزرگ تصادفی می‌گذارم.</li>
<li><strong>۶. تصمیم درست:</strong> برای هر پروژه یک مقیاس کوچک و مستند بساز.</li>
<li><strong>۷. تمرین کوچک:</strong> سه لایهٔ TUYA را از عقب به جلو نام ببر.</li>
</ol>
</article>
<article class="concept-card" data-concept="Z-index">
<h4><span class="term-en" dir="ltr">Z-index</span> — شمارهٔ جلو/عقب</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Z-index می‌گوید عنصر Positioned در چه لایه‌ای باشد.</li>
<li><strong>۲. مثال روزمره:</strong> مثل شمارهٔ طبقه در ساختمان.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Core، Node، Badge، Glow در Visual Stage.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Z-index روی عناصر Positioned در Elementor/CSS.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> برای حل هر مشکل عدد 99999 می‌گذارم.</li>
<li><strong>۶. تصمیم درست:</strong> عددها را کوچک، معنی‌دار و محدود نگه دار.</li>
<li><strong>۷. تمرین کوچک:</strong> برای Glow/Core/Node سه عدد کوچک پیشنهاد بده.</li>
</ol>
</article>
<article class="concept-card" data-concept="Overflow">
<h4><span class="term-en" dir="ltr">Overflow</span> — رفتار بیرون‌زدگی</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Overflow تعیین می‌کند چیزی که از قاب بیرون می‌زند بریده شود یا دیده شود.</li>
<li><strong>۲. مثال روزمره:</strong> مثل نقاشی که از کادر بیرون زده است.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Glow اطراف Core یا Badge بیرون کارت.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Overflow: visible/hidden روی Parent.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> Parent را hidden می‌کنم و Glow بریده می‌شود.</li>
<li><strong>۶. تصمیم درست:</strong> فقط وقتی مطمئنی بیرون‌زدگی نباید دیده شود hidden کن.</li>
<li><strong>۷. تمرین کوچک:</strong> یک Glow را تصور کن؛ آیا باید از قاب بیرون دیده شود؟</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">Layering</dt><dd>ترتیب قرارگیری لایه‌ها</dd>
<dt dir="ltr">Z-index</dt><dd>عدد کنترل جلو/عقب</dd>
<dt dir="ltr">Overflow</dt><dd>بریده‌شدن یا دیده‌شدن بیرون‌زدگی</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">قبل از تغییر Z-index بپرس: «مشکل ترتیب لایه است یا Overflow؟»</p>
</aside>
</section><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Stage base   0
Core/Glow    1
Cloud        2
Nodes        3</pre></figure></details><p>عدد دقیق مهم نیست؛ رابطهٔ روشن مهم است.</p><h3>Overflow</h3><section aria-labelledby="section-hidden-196-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-196-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Visible</dt><dd>بیرون‌زدگی دیده می‌شود</dd><dt>Hidden</dt><dd>بیرون‌زدگی بریده می‌شود</dd><dt>Auto</dt><dd>در صورت نیاز Scroll ایجاد می‌شود</dd></dl></section><p>Node و Glow ممکن است کمی از Box بیرون بزنند؛ Hidden می‌تواند آن‌ها را Clip کند.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="3e827f87dd03729cea161f830143446dbf5fc5d942a08181977a2dc51b144e60" id="lesson-13-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Z-index، Stacking Context و Overflow</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="13" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-13-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-13-section-01">مسئله‌ای که این مفهوم حل می‌کند</h3><p>یک Badge را <code class="inline-code" dir="ltr">z-index: 999999</code> می‌کنی اما هنوز زیر Header است. یک Dropdown روی همه چیز جلوست ولی بخشی از آن بریده می‌شود. یک Parent دارای Transform باعث می‌شود Modal رفتار عجیبی پیدا کند.</p><p>مشکل این است که Z-index یک جدول جهانی از اعداد نیست.</p><hr/></section><section aria-labelledby="concept-v31-13-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-13-section-02">تشبیه به دنیای واقعی: ساختمان‌ها و طبقه‌ها</h3><p>دو ساختمان کنار هم را تصور کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">ساختمان A        ساختمان B
طبقه 999         طبقه 2
</code></pre></figure><p>شمارهٔ طبقه فقط داخل همان ساختمان معنا دارد. اگر کل ساختمان B روی سکوی بالاتری قرار گرفته باشد، طبقهٔ ۲ آن می‌تواند جلوی طبقهٔ ۹۹۹ ساختمان A دیده شود.</p><p>هر ساختمان یک <strong>Stacking Context</strong> است.</p><hr/></section><section aria-labelledby="concept-v31-13-section-03" class="concept-reference-part"><h3 id="concept-v31-13-section-03">Stacking Context چیست؟</h3><p>Stacking Context یک فضای مستقل برای ترتیب Paint است. Childهای داخل آن ابتدا با هم مرتب می‌شوند و سپس کل Context به‌عنوان یک واحد نسبت به Contextهای هم‌سطح قرار می‌گیرد.</p><p>تصویر:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Root Context
├── Header Context (z: 10)
│   └── Icon (z: 1)
└── Main Context (z: 1)
    └── Badge (z: 9999)
</code></pre></figure><p>Badge با عدد ۹۹۹۹ داخل Main نمی‌تواند الزاماً از Header Context با z برابر ۱۰ عبور کند؛ چون ابتدا جای خود Main Context مقایسه می‌شود.</p><hr/></section><section aria-labelledby="concept-v31-13-section-04" class="concept-reference-part"><h3 id="concept-v31-13-section-04">چه چیزهایی Context می‌سازند؟</h3><p>بسته به شرایط، مواردی مانند این‌ها می‌توانند Stacking Context جدید بسازند:</p><ul>
<li>Position همراه Z-index غیر Auto</li>
<li><code class="inline-code" dir="ltr">opacity</code> کمتر از ۱</li>
<li><code class="inline-code" dir="ltr">transform</code></li>
<li><code class="inline-code" dir="ltr">filter</code></li>
<li><code class="inline-code" dir="ltr">isolation: isolate</code></li>
<li>بعضی حالت‌های Flex/Grid Item با Z-index</li>
<li>Top Layer برای Dialog و Popoverهای خاص</li>
</ul><p>هدف حفظ‌کردن تمام فهرست نیست. هدف این است که وقتی Z-index بی‌اثر شد، Ancestorها را بررسی کنی.</p><hr/></section><section aria-labelledby="concept-v31-13-section-05" class="concept-reference-part"><h3 id="concept-v31-13-section-05">Paint Order و Z-index</h3><p>مرورگر فقط عدد Z-index را نگاه نمی‌کند. Background Parent، Elementهای Flow، Positioned Elementها و Contextها ترتیب Paint مشخصی دارند.</p><p>پس گاهی Element بدون Z-index به‌دلیل Paint Order بعدی جلوتر دیده می‌شود؛ و گاهی Z-index فقط پس از Position یا در نقش خاص Item اثر مورد انتظار را دارد.</p><hr/></section><section aria-labelledby="concept-v31-13-section-06" class="concept-reference-part"><h3 id="concept-v31-13-section-06">Overflow؛ قیچی Parent</h3><p><code class="inline-code" dir="ltr">overflow: hidden</code> فقط Scrollbar را پنهان نمی‌کند. محتوای بیرون مرز را Clip می‌کند.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Parent با Overflow Hidden
┌──────────────────┐
│          Badge   │── بخش بیرون‌زده بریده می‌شود
└──────────────────┘
</code></pre></figure><p>حتی اگر Badge Z-index بالایی داشته باشد، نمی‌تواند از قیچی همان Clip عبور کند.</p><p>این دو سؤال جدا هستند:</p><ol>
<li>Element از نظر لایه جلوست یا عقب؟</li>
<li>Element اجازه دارد خارج مرز Ancestor دیده شود یا نه؟</li>
</ol><hr/></section><section aria-labelledby="concept-v31-13-section-07" class="concept-reference-part"><h3 id="concept-v31-13-section-07">درخت عیب‌یابی Z-index</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">آیا Element واقعاً overlap دارد؟
↓
Position/role آن چیست؟
↓
Stacking Context خودش کدام است؟
↓
کدام Ancestor Context جدید ساخته؟
↓
Contextهای sibling چه ترتیبی دارند؟
↓
آیا Overflow یا Clip آن را می‌بُرد؟
↓
آیا عنصر باید در Top Layer/Portal دیگری باشد؟
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-13-section-08" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-13-section-08">در Elementor V4</h3><p>برای یک Stage تصویری:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Visual Stage: position relative; isolation isolate
├── Background shape: z 0
├── Main image: z 1
├── Decorative nodes: z 2
└── Badge: z 3
</code></pre></figure><p><code class="inline-code" dir="ltr">isolation: isolate</code> می‌تواند عمداً Context محلی بسازد تا عددهای لایه‌بندی داخل Stage به بیرون نشت مفهومی نداشته باشند.</p><p>اما Dropdown، Tooltip یا Modal شاید نباید داخل Parent دارای Overflow Hidden زندانی شود. ساختار Element Tree در اینجا مهم‌تر از افزایش عدد است.</p><hr/></section><section aria-labelledby="concept-v31-13-section-09" class="concept-reference-part"><h3 id="concept-v31-13-section-09">Top Layer</h3><p>بعضی عناصر بومی مانند Dialog بازشده به‌صورت Modal وارد Top Layer مرورگر می‌شوند. Top Layer بالاتر از Stacking Contextهای عادی Document قرار می‌گیرد و Z-index عادی منطق آن را کنترل نمی‌کند.</p><p>این مفهوم نشان می‌دهد چرا «همه چیز با 999999 حل می‌شود» از پایه اشتباه است.</p><hr/></section><section aria-labelledby="concept-v31-13-section-10" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-13-section-10">اشتباهات رایج</h3><ul>
<li>عددهای نجومی بدون تحلیل Context</li>
<li>Transform روی Parent بدون توجه به Context جدید</li>
<li>Overflow Hidden برای حذف Scrollbar و بریدن Dropdown</li>
<li>قرار دادن Modal داخل Stage محلی</li>
<li>تصور اینکه Child می‌تواند سقف Context Parent را بشکند</li>
<li>استفاده از Z-index برای حل ترتیب DOM یا Layout اشتباه</li>
</ul><hr/></section><section aria-labelledby="concept-v31-13-section-11" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-13-section-11">پل به DevTools</h3><ul>
<li>Ancestorها را در Elements Panel بالا برو.</li>
<li>در Computed، <code class="inline-code" dir="ltr">transform</code>، <code class="inline-code" dir="ltr">opacity</code>، <code class="inline-code" dir="ltr">position</code>، <code class="inline-code" dir="ltr">z-index</code> و <code class="inline-code" dir="ltr">overflow</code> را بررسی کن.</li>
<li>Layers Panel یک نمای سه‌بعدی از Composition می‌دهد، اما Layer Compositing دقیقاً همان Stacking Context نیست؛ آن را ابزار کمکی بدان، نه تعریف مفهوم.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-13-section-12" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-13-section-12">تصویر ذهنی نهایی</h3><p>Z-index شماره طبقه است، نه ارتفاع جهانی از زمین. ابتدا ببین در کدام ساختمان هستی؛ سپس شماره طبقه را مقایسه کن. Overflow هم نگهبانی است که حتی طبقهٔ بالا را از پنجره بیرون نمی‌گذارد.</p><hr/></section><section aria-labelledby="concept-v31-13-section-13" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-13-section-13">قوانین طلایی</h3><ul>
<li><strong>«Z-index را داخل Stacking Context بخوان.»</strong></li>
<li><strong>«Child با عدد بزرگ نمی‌تواند همیشه از Context Parent فرار کند.»</strong></li>
<li><strong>«Overflow می‌تواند Element جلویی را هم Clip کند.»</strong></li>
<li><strong>«اول درخت لایه‌ها را اصلاح کن، بعد عدد را.»</strong></li>
<li><strong>«Modal و Dropdown را در Context مناسب قرار بده، نه در زندان Stage.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>CSS Positioned Layout and Painting/Stacking rules</li>
<li>Chrome DevTools Layers and Top Layer references</li>
<li>Elementor Help: Position and overflow controls</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-13-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-13-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Layering؛ z-index و opacity طول نیستند</span></summary>
<section aria-labelledby="lesson-13-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">برای لایه‌گذاری بیشتر با عددهای بدون واحد و keywordها سروکار داری. Overflow نیز keyword است و اندازه‌ای به جعبه اضافه نمی‌کند.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> شمارهٔ طبقه متر نیست؛ فقط ترتیب را نشان می‌دهد. پردهٔ نیمه‌شفاف هم با نسبت شفافیت کنترل می‌شود، نه سانتی‌متر.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Z-index</th><td><code dir="ltr">z-index</code></td><td>auto / integer</td><td>بدون واحد</td><td>ترتیب داخل stacking context.</td><td>عدد بزرگ‌تر خارج از context خود قدرت ندارد.</td><td><code dir="ltr">CSS_POSITION</code></td></tr><tr><th scope="row">Overflow</th><td><code dir="ltr">overflow</code></td><td>visible / hidden / clip / auto / scroll</td><td>keyword</td><td>نمایش یا clipping محتوای بیرون.</td><td>hidden علت overflow را حل نمی‌کند.</td><td><code dir="ltr">E_CONTAINER</code></td></tr><tr><th scope="row">Opacity</th><td><code dir="ltr">opacity</code></td><td>عدد 0 تا 1 یا درصد در CSS مدرن</td><td>نسبت بدون طول</td><td>برای شفافیت کل Element.</td><td>opacity می‌تواند stacking context بسازد.</td><td><code dir="ltr">E_EFFECTS</code></td></tr><tr><th scope="row">Shadow blur/offset</th><td><code dir="ltr">box-shadow</code></td><td>lengthها + color</td><td>Box</td><td>برای عمق بصری.</td><td>Shadow بخشی از layout size نیست.</td><td><code dir="ltr">E_EFFECTS</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>opacity:0.4 یعنی 40٪ کدری، نه 0.4px. z-index:5 نیز پنج پیکسل جلوتر نیست.</p></section>
<section><h3>📱 در Responsive</h3><p>Layering باید در Mobile دوباره تست شود؛ clipping و stacking context ممکن است با transform یا overflow breakpoint تغییر کند.</p></section>
<section><h3>🔬 در DevTools</h3><p>stacking context، z-index، opacity و overflow ancestorها را ثبت کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/style-tab-effects/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Effects</a>، <a href="https://elementor.com/help/container-layout-tab-settings/" rel="noopener noreferrer" target="_blank">Elementor — Container layout settings</a>، <a href="https://www.w3.org/TR/css-position-3/" rel="noopener noreferrer" target="_blank">W3C — CSS Positioned Layout</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-13-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-13-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — تکمیل لایه‌ها</h3><p>شش Node را Duplicate کن. برای هرکدام Local Position جدا تنظیم کن.</p><p>ترتیب پیشنهادی:</p><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text" dir="ltr">Core: 1
Cloud: 2
Nodes: 3
</code></pre><p>Glow را با Shadow روی Core بساز.</p><h3>❓ سؤال توقف</h3><p>اگر <code class="inline-code" dir="ltr">z-index:99999</code> روی Node اثر نکند، اولین احتمال چیست؟</p><details class="disclosure-card"><summary>پاسخ پیشنهادی</summary>Node در Stacking Context متفاوت یا Parent نامناسب قرار دارد.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> برای هر Conflict فقط عدد Z-index را بزرگ‌تر کنی.</p><p><strong>اولین بررسی:</strong> Parentها، Context و Sibling بودن عناصر.</p><h3>🧪 عمداً خرابش کن</h3><p>Overflow Platform Visual را Hidden کن و Nodeها را کمی بیرون ببر.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>بخشی از Nodeها بریده می‌شود؛</li>
<li>Shadow یا Glow ناقص می‌شود؛</li>
<li>ظاهر ممکن است در یک عرض خوب و در عرض دیگر بد باشد.</li>
</ul><p>Overflow مناسب را برگردان.</p><p>سپس روی یکی از Parentها Transform یا Opacity قرار بده و Layering را دوباره ببین.</p><h3>Checkpoint</h3><form class="interactive-form checklist-form" data-persist-group="lesson-13-layering-checkpoint"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="lesson-13-layering-check-1" type="checkbox"/><span>شش Node دیده می‌شوند</span></label><label class="choice-row"><input data-persist="checkbox" id="lesson-13-layering-check-2" type="checkbox"/><span>Glow بریده نمی‌شود</span></label><label class="choice-row"><input data-persist="checkbox" id="lesson-13-layering-check-3" type="checkbox"/><span>Z-index Scale کوچک و مستند است</span></label><label class="choice-row"><input data-persist="checkbox" id="lesson-13-layering-check-4" type="checkbox"/><span>عددهای بسیار بزرگ تصادفی ندارم</span></label></fieldset></form><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Stacking Context چیست؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> z-index بسیار بزرگ روی Badge اثر ندارد. کدام Ancestorها را بررسی می‌کنی؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-73"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-73-1" name="chk-73-1" type="checkbox"/><span>فقط افزایش عدد Z-index را پیشنهاد نداده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-73-2" name="chk-73-2" type="checkbox"/><span>Stacking Context، Ancestor و Overflow را بررسی کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-73-3" name="chk-73-3" type="checkbox"/><span>رابطهٔ Core، Cloud، Glow و Nodeها را به‌صورت لایه‌ای توضیح داده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-13-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-13-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-IMAGE-001 — Overlay Badge</h3><p><strong>هدف:</strong> 👁 فقط مشاهده کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">good_pattern</code> با شرط Runtime</p><p>Parent Relative و Badge Absolute می‌تواند برای Overlay تزئینی الگوی مناسبی باشد. تفاوت آن با متن Absolute این است که Badge Decoration است، نه محتوای اصلی.</p><h3>🔬 پشت صحنه</h3><p>Z-index فقط در Context مربوط مقایسه می‌شود. جزئیات کامل برای این دوره ضروری نیست؛ Tree و Parent را بررسی کن.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="memory-z-overflow-heading" role="heading">🧠 لایهٔ حافظه — Z-index و Overflow</span></summary><section aria-labelledby="memory-z-overflow-heading" class="memory-layer disclosure-content lesson-section"><p><strong>🧠 استعارهٔ ماندگار:</strong> Z-index طبقهٔ آسانسور است؛ Overflow دیوار اتاق است که می‌تواند چیزهای بیرون‌زده را نشان دهد یا ببرد.</p><p><strong>🧩 در Elementor V4 یعنی چه؟</strong> قبل از بالا بردن z-index، ببین عنصر داخل کدام parent و stacking context است.</p><p><strong>⚠️ تله رایج:</strong> z-index بزرگ روی عنصری که در parent بریده می‌شود مشکل overflow را حل نمی‌کند.</p><p class="golden-rule"><strong>📜 قانون طلایی:</strong> اول parent و overflow را پیدا کن؛ بعد z-index بده.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-13-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-13-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><section aria-labelledby="stacking-step-title" class="step-simulator step-simulator-stacking" data-simulator-type="stacking" data-step-simulator="" id="stacking-step"><h3 id="stacking-step-title">Step‑Through — DOM Order، Z-index و Stacking Context</h3><p>چهار حالت نشان می‌دهند چرا عدد بزرگ همیشه لایه را به جلوی کل صفحه نمی‌آورد.</p><div aria-live="polite" class="simulator-viewport"><p class="simulator-label" data-step-label=""></p><div class="simulator-rail simulator-rail-stacking" data-step-render=""></div><code class="simulator-code" data-step-code="" dir="ltr"></code></div><div class="simulator-actions"><button aria-label="نمایش حالت قبلی" class="ui-btn" data-step-prev="" type="button">حالت قبلی</button><button aria-label="نمایش حالت بعدی" class="ui-btn" data-step-next="" type="button">حالت بعدی</button></div><script class="simulator-data" type="application/json">[{"label":"حالت ۱ از ۴ — بدون z-index، ترتیب paint و DOM قابل مشاهده است.","code":".a, .b { position: relative; }","mode":"dom"},{"label":"حالت ۲ از ۴ — داخل یک stacking context، z-index بالاتر جلو می‌آید.","code":".a { z-index: 1; } .b { z-index: 2; }","mode":"same-context"},{"label":"حالت ۳ از ۴ — Child با z-index بزرگ داخل Context پایین‌تر زندانی است.","code":".context-a { z-index: 1; } .context-b { z-index: 2; } .child { z-index: 9999; }","mode":"trapped"},{"label":"حالت ۴ از ۴ — overflow:hidden می‌تواند لایهٔ بیرون‌زده را clip کند.","code":".context { overflow: hidden; }","mode":"clipped"}]</script><p class="golden-rule"><strong>قانون طلایی:</strong> Z-index فقط داخل stacking context قابل مقایسه است و overflow می‌تواند نتیجه را clip کند.</p></section><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-75"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-75-1" name="chk-75-1" type="checkbox"/><span>می‌توانی توضیح بدهی چرا z-index بزرگ همیشه برنده نمی‌شود.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-75-2" name="chk-75-2" type="checkbox"/><span>می‌توانی Overflow، Clipping و Stacking Context را از هم جدا کنی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-76"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-76-1" name="chk-76-1" type="checkbox"/><span>ترتیب Core، Glow، Cloud و Nodeهای TUYA را بدون عددهای تصادفی تنظیم می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-76-2" name="chk-76-2" type="checkbox"/><span>علت Clip شدن Node را پیدا می‌کنی و به‌جای پنهان‌کردن مشکل، Context را اصلاح می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-77"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-77-1" name="chk-77-1" type="checkbox"/><span>در سناریوی «z-index:9999 کار نمی‌کند» می‌توانی Ancestorهای Contextساز را بررسی کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-13-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-13-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد کل سکشن را برای Device Sizeهای مختلف تطبیق می‌دهیم.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 13</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-13-completion"><fieldset><legend>ثبت پایان درس 13</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-13-complete" name="lesson-13-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-13-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Z-index و Overflow</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Z-index در برابر DOM Order</h3><p>DOM Order ترتیب ورود بازیگران است؛ Z-index لایهٔ صحنه است. اگر stacking context را نفهمی، عدد بزرگ‌تر همیشه مشکل را حل نمی‌کند.</p></section>
<section class="inline-compare-card"><h3>Overflow Hidden در برابر حل واقعی مشکل</h3><p>Overflow hidden قیچی‌کردن بیرون‌زدگی است؛ حل واقعی مشکل یعنی فهمیدن چرا عنصر بیرون زده. برای تزئین قابل دفاع است، برای محتوای اصلی معمولاً زنگ خطر است.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="visibility-step"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="visibility-step-title" role="heading">Step‑Through — display ، visibility و opacity</span></summary><section aria-labelledby="visibility-step-title" class="disclosure-content step-simulator" data-step-simulator="">
<p>هر سه می‌توانند چیزی را «نامرئی» نشان دهند، اما اثرشان روی layout و interaction یکسان نیست.</p>
<div aria-live="polite" class="simulator-viewport">
<p class="simulator-label" data-step-label="">حالت 1 از 3 — display</p>
<div class="simulator-rail" data-step-render=""></div>
<code class="simulator-code" data-step-code="" dir="ltr">display: none;</code>
</div>
<div class="simulator-actions"><button class="ui-btn" data-step-prev="" type="button">حالت قبلی</button><button class="ui-btn" data-step-next="" type="button">حالت بعدی</button></div>
<script class="simulator-data" type="application/json">[
    {"label":"display:none: عنصر از layout حذف می‌شود و جای آن هم جمع می‌شود.","code":"display: none;","items":["item","removed","item"]},
    {"label":"visibility:hidden: عنصر دیده نمی‌شود، اما جای آن در layout حفظ می‌شود.","code":"visibility: hidden;","items":["item","ghost","item"]},
    {"label":"opacity:0: عنصر نامرئی است، جای خود را دارد و ممکن است هنوز interaction بگیرد.","code":"opacity: 0;","items":["item","transparent","item"]}
  ]</script>
<p class="golden-rule"><strong>قانون طلایی:</strong> نامرئی‌بودن کافی نیست؛ بپرس آیا عنصر هنوز جا می‌گیرد و آیا هنوز قابل تعامل است؟</p>
</section></details>
<details class="lesson-disclosure" id="lesson-13-practical-findings"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-13-practical-findings-heading" role="heading">🔎 یافتهٔ عملی و خطایابی</span></summary><section aria-labelledby="lesson-13-practical-findings-heading" class="disclosure-content practical-findings">
<p class="finding-scope">این بخش فقط ادعاهایی را آموزش می‌دهد که یا در مشاهدهٔ واقعی ثبت شده‌اند یا Help Center رسمی Elementor آن‌ها را صریحاً پشتیبانی می‌کند. نتیجه‌های وابسته به Theme، نسخه یا ساختار DOM با دامنهٔ اعتبار نوشته شده‌اند.</p>
<article class="finding-card" data-verification="derived_from_official_help" id="finding-overflow-hidden-hides-symptom">
<div class="evidence-badges"><span class="evidence-badge derived">نتیجهٔ مشتق از Help Center</span></div>
<h3>چرا Overflow: Hidden اسکرول افقی را ناپدید کرد، ولی مشکل واقعاً حل نشد؟</h3>
<p><strong>رفتار مستند:</strong> حالت Hidden فقط بخش بیرون از مرز Container را مخفی می‌کند؛ حالت Auto برای محتوای خارج از مرز scrollbar می‌سازد.</p>
<p><strong>نتیجهٔ آموزشی:</strong> اگر با Hidden اسکرول ناپدید شد، هنوز باید عنصرِ بزرگ‌تر از والد، margin بیرون‌زننده یا absolute child را پیدا کنی. Hidden می‌تواند symptom را پنهان کند.</p>
<div class="finding-checks">
<section><h4>در DevTools</h4><p>Overflow را موقتاً روی Visible بگذار، سپس عرض و Box Model فرزندان را مقایسه کن.</p></section>
<section><h4>چه زمانی Hidden درست است؟</h4><p>وقتی clipping بخشی از نیت طراحی است؛ نه صرفاً برای خاموش‌کردن scrollbar ناشناخته.</p></section>
</div>
<p class="golden-rule"><strong>قانون طلایی:</strong> پنهان‌کردن خروجیِ خطا با رفع علت خطا یکی نیست.</p>
<details class="more-know"><summary>منبع و نوع استنتاج</summary><p><a href="https://elementor.com/help/set-flexbox-container-size-behavior/">Set a Flexbox Container’s size and behavior — Overflow</a>. جملهٔ «ممکن است symptom را پنهان کند» یک نتیجهٔ آموزشی مستقیم از تعریف رسمی Hidden است.</p></details>
</article>
</section></details>
<details class="lesson-disclosure" id="lesson-13-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Overflow و دایرهٔ بزرگ Mobile</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>دایرهٔ سفید و Nodeها نزدیک لبه‌های Stage قرار دارند. قبل از انتخاب <code>overflow:hidden</code> مشخص کن چه چیزی باید clip شود و چه چیزی نباید.</p>
<p>Hidden روی صفحه یا body ممکن است فقط علامت overflow را پنهان کند. clipping را تا حد امکان روی Stage محلی نگه دار.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-13-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Overflow، clipping و پیدا کردن علت</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> فرق رفع overflow با پنهان‌کردن اسکرول‌بار را تجربه کن.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>Visual Stage و Nodeهای نزدیک لبه بساز.</li><li>overflow: visible و hidden را مقایسه کن.</li><li>عنصر واقعی overflowکننده را با اندازه‌ها و Box Model پیدا کن.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن Hidden کدام قسمت را clip می‌کند و آیا علت اندازهٔ نامناسب را تغییر می‌دهد.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>یک child را از عرض Stage بزرگ‌تر کن و فقط روی body یا parent overflow:hidden بگذار.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>scrollWidth/clientWidth، overflow-x/y، Bounding Rect و ancestor clipping.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> مشکل sizing اصلاح شده و Hidden فقط وقتی استفاده شده که clipping بخشی از طراحی است.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-13-responsive-build-test-done-build"><input data-persist="" id="lesson-13-responsive-build-test-done-build" name="lesson-13-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-13-responsive-build-test-done-test"><input data-persist="" id="lesson-13-responsive-build-test-done-test" name="lesson-13-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-13-responsive-build-test-done-debug"><input data-persist="" id="lesson-13-responsive-build-test-done-debug" name="lesson-13-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-13-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-13-responsive-build-test-note" name="lesson-13-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/container-layout-tab-settings/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-13-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — z-index، opacity و overflow</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
