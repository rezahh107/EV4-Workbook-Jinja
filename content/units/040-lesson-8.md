<article class="lesson card-surface" data-lesson="8" id="lesson-8"><h2 class="lesson-title former-h1">درس 8 — Wrap و ساخت Logo Strip</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-8-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-8-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> Wrap را برای آیتم‌های تکراری و رفتار ردیف Logoها بفهمی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Grid کامل یا Responsive نهایی را.</p><p><strong>در پایان باید بتوانی:</strong> Logoها را بدون Marginهای تکی و بدون Overflow در ردیف منعطف بچینی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-8-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-8-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr><tr><th scope="row">نوع فعالیت</th><td>🛠 اجرایی + 🔍 عیب‌یابی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۱۵–۲۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۲۰–۳۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> Wrap را با عرض واقعی و محتوای تکراری می‌آزمایی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-8-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-8-lesson-understand-4">A. بفهم</h2><h3>مسئله</h3><p>چهار Logo در Desktop در یک ردیف جا می‌شوند، اما در عرض باریک باید به خط بعد بروند.</p><h3>مدل ذهنی</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text" dir="ltr">nowrap:
[A][B][C][D]------------------&gt;

wrap:
[A][B]
[C][D]
</code></pre><p>Wrap به فرزندان اجازه می‌دهد وقتی فضای کافی نیست، خط جدید بسازند.</p><h3>فرق Wrap و Hide</h3><p>Wrap ساختار را حفظ می‌کند؛ Hide محتوا را حذف می‌کند. Responsive خوب معمولاً ابتدا از Wrap و تغییر اندازه استفاده می‌کند، نه حذف محتوا.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="af3d465aae109f8ea5e8ba4f8b9086acfe54589367a53277d9180f3071a2e12c" id="lesson-8-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Wrap؛ وقتی یک ردیف دیگر جا ندارد</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="8" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-08-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-08-section-01">مسئله‌ای که Wrap حل می‌کند</h3><p>یک Flex Container را تصور کن که شش کارت داخل آن قرار گرفته است. در صفحهٔ بزرگ، همهٔ کارت‌ها کنار هم جا می‌شوند. اما با کم‌شدن عرض، مرورگر باید تصمیم بگیرد:</p><ul>
<li>کارت‌ها را کوچک کند؛</li>
<li>آن‌ها را از کادر بیرون بزند؛</li>
<li>یا بخشی از کارت‌ها را به خط بعد ببرد.</li>
</ul><p><code class="inline-code" dir="ltr">flex-wrap</code> فقط به سؤال سوم پاسخ می‌دهد: <strong>آیا Flex Itemها اجازه دارند بیش از یک Flex Line بسازند؟</strong></p><p>Wrap خودش عرض کارت‌ها، تعداد ستون‌ها یا حداقل اندازهٔ آن‌ها را تعیین نمی‌کند. فقط در را برای ساخت خط جدید باز می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-08-section-02" class="concept-reference-part concept-reference-analogy concept-reference-workflow"><h3 id="concept-v31-08-section-02">تشبیه به دنیای واقعی: صندوق‌های فروشگاه</h3><p>فرض کن فروشگاه فقط یک صف صندوق دارد.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[نفر ۱][نفر ۲][نفر ۳][نفر ۴][نفر ۵]
</code></pre></figure><p>اگر فضا کم شود و قانون <code class="inline-code" dir="ltr">nowrap</code> باشد، همه مجبورند در همان یک صف بمانند؛ یا به هم فشرده می‌شوند یا صف از سالن بیرون می‌زند.</p><p>با Wrap، وقتی صف اول پر شد، صندوق دوم باز می‌شود:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[نفر ۱][نفر ۲][نفر ۳]
[نفر ۴][نفر ۵]
</code></pre></figure><p>اما بازشدن صندوق دوم تعیین نمی‌کند هر نفر چقدر جا بگیرد. اندازهٔ هر Item همچنان از Width، Basis، Min/Max Size و محتوای آن می‌آید.</p><hr/></section><section aria-labelledby="concept-v31-08-section-03" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-08-section-03">چرا CSS این مفهوم را ساخته است؟</h3><p>Flexbox یک مدل یک‌بعدی است. در هر Flex Line، Itemها روی Main Axis مذاکره می‌کنند. گاهی یک Line کافی نیست، اما هنوز می‌خواهیم منطق اصلی «صف» حفظ شود.</p><p>Wrap برای همین ساخته شد:</p><blockquote>
<p>یک جریان یک‌بعدی را نگه دار، ولی اجازه بده در صورت کمبود فضا خط‌های بیشتری تشکیل شوند.</p>
</blockquote><p>این با Grid فرق دارد. در Grid، ردیف و ستون از ابتدا بخشی از شبکه‌اند. در Flex Wrap، خط دوم نتیجهٔ کمبود فضاست، نه لزوماً یک ردیف از پیش طراحی‌شده.</p><hr/></section><section aria-labelledby="concept-v31-08-section-04" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-08-section-04">رفتار قدم‌به‌قدم</h3><p>فرض کن Parent عرض مفید ۹۶۰px دارد و سه کارت هرکدام Basis برابر ۳۰۰px دارند، با Gap برابر ۳۰px:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">300 + 300 + 300 + 30 + 30 = 960px
</code></pre></figure><p>سه کارت دقیقاً جا می‌شوند.</p><p>اگر Parent به ۸۰۰px برسد، چند اتفاق ممکن است بیفتد:</p><ol>
<li>اگر Shrink اجازه دهد و Min Size مانع نباشد، کارت‌ها کوچک می‌شوند.</li>
<li>اگر Shrink نتواند فضای لازم را پس بگیرد و Wrap خاموش باشد، Overflow رخ می‌دهد.</li>
<li>اگر Wrap روشن باشد، یکی از کارت‌ها به خط بعد می‌رود.</li>
</ol><p>پس ترتیب فکرکردن چنین است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">عرض Parent
↓
Basis/Width Itemها
↓
Gap و Padding
↓
Shrink و Min Size
↓
Wrap
↓
Alignment بین Lineها
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-08-section-05" class="concept-reference-part"><h3 id="concept-v31-08-section-05">فرق <code class="inline-code" dir="ltr">align-items</code> و <code class="inline-code" dir="ltr">align-content</code></h3><p>وقتی فقط یک Line وجود دارد، <code class="inline-code" dir="ltr">align-content</code> تقریباً موضوعی برای کارکردن ندارد.</p><ul>
<li><code class="inline-code" dir="ltr">align-items</code> جای Itemها را داخل هر Line روی Cross Axis کنترل می‌کند.</li>
<li><code class="inline-code" dir="ltr">align-content</code> خودِ Lineها را در فضای اضافهٔ Cross Axis توزیع می‌کند.</li>
</ul><p>تصویر ذهنی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Container بلند
┌─────────────────────────┐
│ [A] [B] [C]             │ ← Line 1
│                         │
│ [D] [E]                 │ ← Line 2
└─────────────────────────┘
</code></pre></figure><p><code class="inline-code" dir="ltr">align-items</code> قد Itemها را در هر خط می‌بیند؛ <code class="inline-code" dir="ltr">align-content</code> فاصله و جای دو خط را در کل Container می‌بیند.</p><hr/></section><section aria-labelledby="concept-v31-08-section-06" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-08-section-06">در Elementor V4</h3><p>در تنظیمات Layout یک Flex Container، Wrap را فقط بعد از تعیین قرارداد اندازه Childها فعال کن.</p><p>سناریوی Logo Strip:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Logo Strip
├── Logo 1
├── Logo 2
├── Logo 3
├── Logo 4
└── Logo 5
</code></pre></figure><p>تنظیم منطقی ممکن است چنین باشد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Parent: Row + Wrap
Gap: 24px
Logo item: Width/Basis کنترل‌شده
Image: Max Width مشخص
</code></pre></figure><p>اگر فقط Wrap را فعال کنی ولی هر لوگو <code class="inline-code" dir="ltr">width: 100%</code> داشته باشد، احتمالاً هر لوگو یک خط کامل می‌گیرد. اگر لوگوها Shrink نامحدود داشته باشند، ممکن است آن‌قدر کوچک شوند که هرگز Wrap رخ ندهد.</p><h4>تستی که باید انجام دهی</h4><p>فقط Desktop، Tablet و Mobile را نبین. عرض‌های میان آن‌ها را نیز امتحان کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">1200 → 1024 → 900 → 768 → 600 → 480 → 360
</code></pre></figure><p>بسیاری از شکست‌های Wrap دقیقاً بین Breakpointهای رسمی دیده می‌شوند.</p><hr/></section><section aria-labelledby="concept-v31-08-section-07" class="concept-reference-part"><h3 id="concept-v31-08-section-07">Wrap یا Grid؟</h3><p>این درخت تصمیم را به خاطر بسپار:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">آیا Itemها یک جریان طبیعی دارند و فقط در کمبود فضا باید به خط بعد بروند؟
└── Flex + Wrap

آیا ستون‌ها باید در چند ردیف دقیقاً با هم تراز بمانند؟
└── Grid

آیا یک Item باید دو یا چند ستون را بگیرد؟
└── Grid

آیا تعداد Itemها متغیر است و ترتیب خطی محتوا مهم است؟
└── Flex + Wrap را ابتدا بررسی کن
</code></pre></figure><p>چیدمان ۴→۲→۱ فقط مخصوص Grid نیست؛ Flex Wrap هم می‌تواند آن را بسازد. تفاوت اصلی در «رابطهٔ دوبعدی» و «تراز Trackها» است.</p><hr/></section><section aria-labelledby="concept-v31-08-section-08" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-08-section-08">اشتباهات رایج</h3><h4>انتظار Wrap در حالی که Childها Shrink می‌شوند</h4><p>اگر Itemها می‌توانند تا اندازه‌ای بسیار کوچک جمع شوند، مرورگر شاید هرگز مجبور به ساخت خط دوم نشود.</p><h4>Height ثابت روی Parent چندخطی</h4><p>وقتی تعداد Lineها تغییر می‌کند، Height ثابت می‌تواند خط‌های بعدی را Clip کند یا Overflow بسازد.</p><h4>تغییر ترتیب بصری</h4><p>استفاده از <code class="inline-code" dir="ltr">order</code> یا Wrap معکوس ممکن است ترتیب دیداری را از ترتیب DOM جدا کند. کاربر کیبورد و Screen Reader همچنان ترتیب DOM را دنبال می‌کند.</p><h4>ساخت نسخهٔ جداگانه Mobile بدون نیاز</h4><p>گاهی یک Row با Wrap و Basis درست، نیاز به Duplicate کردن کل محتوا برای Mobile را از بین می‌برد.</p><hr/></section><section aria-labelledby="concept-v31-08-section-09" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-08-section-09">پل به DevTools</h3><p>در Chrome DevTools کنار Flex Container روی Badge مربوط به <code class="inline-code" dir="ltr">flex</code> کلیک کن. Overlay جای Childها و Lineها را نشان می‌دهد. سپس در Computed Style این موارد را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">flex-wrap
flex-basis
flex-shrink
min-width
gap
width
</code></pre></figure><p>اگر Wrap رخ نمی‌دهد، فقط به <code class="inline-code" dir="ltr">flex-wrap</code> خیره نشو؛ معمولاً علت در Basis، Shrink یا Min Size است.</p><hr/></section><section aria-labelledby="concept-v31-08-section-10" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-08-section-10">تصویر ذهنی نهایی</h3><p>Flex Wrap مانند فروشگاهی است که در شلوغی صندوق دوم باز می‌کند. بازشدن صندوق دوم مشکل اندازهٔ سبدها را حل نمی‌کند؛ فقط مسیر تازه‌ای برای صف می‌سازد.</p><hr/></section><section aria-labelledby="concept-v31-08-section-11" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-08-section-11">قوانین طلایی</h3><ul>
<li><strong>«Wrap اجازهٔ خط جدید می‌دهد؛ اندازهٔ Item را تعیین نمی‌کند.»</strong></li>
<li><strong>«قبل از Wrap، Basis، Shrink و Min Size را بررسی کن.»</strong></li>
<li><strong>«Align Items برای Itemهاست؛ Align Content برای Lineها.»</strong></li>
<li><strong>«Flex Wrap جریان می‌سازد؛ Grid شبکه می‌سازد.»</strong></li>
<li><strong>«عرض‌های بین Breakpointها را آزمایش کن؛ شکست‌های واقعی آنجا پنهان‌اند.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>CSS Flexible Box Layout Module Level 1</li>
<li>Elementor Help: Flexbox Container layout and responsive container behavior</li>
<li>Chrome DevTools: Flex overlay and CSS badges</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-8-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-8-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Wrap keyword است؛ عرض Logo و Gap واحد می‌گیرند</span></summary>
<section aria-labelledby="lesson-8-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Wrap فقط اجازهٔ ساخت Line جدید را می‌دهد. اینکه چه زمانی Line جدید ساخته شود به مجموع Width/Basis و Gap وابسته است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> Wrap اجازه می‌دهد وقتی یک قفسه پر شد، کتاب‌ها به قفسهٔ بعدی بروند؛ اندازهٔ کتاب و فاصلهٔ میان آن‌ها تعیین می‌کند چه زمانی قفسه پر شود.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Wrap</th><td><code dir="ltr">flex-wrap</code></td><td>nowrap / wrap / wrap-reverse</td><td>keyword</td><td>اجازه یا منع Line جدید.</td><td>Wrap به‌تنهایی اندازهٔ Logo را اصلاح نمی‌کند.</td><td><code dir="ltr">E_CONTAINER</code></td></tr><tr><th scope="row">Gap</th><td><code dir="ltr">gap</code></td><td>PX، %، VW</td><td>Parent/viewport</td><td>فاصلهٔ بین Logo frameها.</td><td>Gap درصدی در عرض کم می‌تواند بزرگ بماند.</td><td><code dir="ltr">E_FLEX_GAP</code></td></tr><tr><th scope="row">Logo frame width</th><td><code dir="ltr">width / max-width</code></td><td>PX، % یا واحدهای موجود در کنترل</td><td>Parent</td><td>برای قاب‌های سازگار و سقف اندازه.</td><td>تصویر را فقط با height ثابت نکش.</td><td><code dir="ltr">E_SIZE</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>Parent=360px، سه Logo هرکدام 120px و دو Gap=16px → 392px؛ بدون shrink یا wrap، overflow محتمل است.</p></section>
<section><h3>📱 در Responsive</h3><p>روی عرض‌های میانی تست کن؛ شکست فقط در سه preset دستگاه رخ نمی‌دهد.</p></section>
<section><h3>🔬 در DevTools</h3><p>خطوط Flex، scrollWidth/clientWidth، width قاب و gap را ثبت کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/container-layout-tab-settings/" rel="noopener noreferrer" target="_blank">Elementor — Container layout settings</a>، <a href="https://elementor.com/help/adjusting-the-contained-elements/" rel="noopener noreferrer" target="_blank">Elementor — Arrange elements in a Flexbox container</a>، <a href="https://elementor.com/help/style-tab-size/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Size</a>، <a href="https://www.w3.org/TR/css-flexbox-1/" rel="noopener noreferrer" target="_blank">W3C — CSS Flexible Box Layout</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-8-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-8-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — ساخت Logo Strip</h3><p>داخل Platform Copy یک Flexbox بساز:</p><figure class="visual-figure visual-term-map logo-strip-map"><figcaption>ویژگی‌های Logo Strip</figcaption><dl class="term-grid"><dt>نام بخش</dt><dd>Logo Strip</dd><dt>Class</dt><dd>c-logo-strip</dd><dt>Direction</dt><dd>Row</dd><dt>Wrap</dt><dd>Wrap</dd><dt>Align</dt><dd>Center</dd><dt>Gap</dt><dd>مقدار متوسط</dd></dl></figure><p>سپس برای هر Logo یک Div Block سبک بساز:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="rtl">Logo Frame
Class: c-logo-frame
|
+-- Image یا SVG</pre></figure></details><p>Class <code class="inline-code" dir="ltr">c-logo-frame</code> را همین حالا بساز، چون اولین Frame واقعی ایجاد شده است.</p><h3>❓ سؤال توقف</h3><p>اگر Logoها از عرض Parent بیشتر شوند و Wrap خاموش باشد، چه چیزی محتمل است؟</p><details class="disclosure-card"><summary>پاسخ</summary>فشردگی نامناسب یا Overflow افقی.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> به تک‌تک Logoها Margin بدهی.</p><p><strong>نشانه:</strong> Logo اول و آخر نیز فاصلهٔ اضافی از لبه دارند و Responsive سخت می‌شود.</p><p><strong>راه بهتر:</strong> Gap روی Parent.</p><h3>🧪 عمداً خرابش کن</h3><p>Wrap را خاموش کن و Preview را به 320px نزدیک کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>Logoها در یک خط می‌مانند؛</li>
<li>یکی از Logoها بیش از حد کوچک می‌شود یا ردیف بیرون می‌زند؛</li>
<li>ممکن است Scroll افقی ایجاد شود.</li>
</ul><p>Wrap را دوباره فعال کن و عرض Frameها را بررسی کن.</p><h3>🔍 روش بررسی</h3><ul>
<li>Parent درست انتخاب شده؟</li>
<li>Wrap روی Logo Strip است؟</li>
<li>Frameها Min Width غیرمنطقی ندارند؟</li>
<li>Image از Frame عریض‌تر نیست؟</li>
</ul><h3>Checkpoint</h3><section aria-labelledby="section-hidden-129-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-129-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-43"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-43-1" name="chk-43-1" type="checkbox"/><span>Logo Strip یک Flexbox مستقل است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-43-2" name="chk-43-2" type="checkbox"/><span>فاصله با Gap ساخته شده</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-43-3" name="chk-43-3" type="checkbox"/><span>Logoها در عرض باریک Wrap می‌شوند</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-43-4" name="chk-43-4" type="checkbox"/><span>هر Logo داخل Frame مشترک است</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Wrap چه مشکلی را حل می‌کند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> Badgeهای یک Card در 320px از صفحه بیرون می‌زنند. قبل از افزودن Breakpoint چه چیزی را بررسی می‌کنی؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-44"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-44-1" name="chk-44-1" type="checkbox"/><span>Wrap و Gap را از هم جدا کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-44-2" name="chk-44-2" type="checkbox"/><span>نشانهٔ Overflow یا فشردگی را پیش‌بینی کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-44-3" name="chk-44-3" type="checkbox"/><span>قبل از افزودن Breakpoint، رفتار Flex و Width را بررسی کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-8-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-8-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-SOL-REUSE-001 — Buttonها و آیتم‌های تکراری</h3><p><strong>هدف:</strong> ⚖️ دو روش را مقایسه کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">improvement_candidate</code></p><p>Export نشان می‌دهد چند Button و Card امضای Style تکراری دارند. Wrap فقط چیدمان را حل می‌کند؛ Global Class تکرار Style را حل می‌کند. این دو مسئله را با هم اشتباه نگیر.</p><h3>🔬 پشت صحنه</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text language-css" dir="ltr">display: flex;
flex-wrap: wrap;
gap: ...;
</code></pre><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-8-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-8-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-46"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-46-1" name="chk-46-1" type="checkbox"/><span>می‌توانی توضیح بدهی Wrap چه زمانی Line جدید می‌سازد و Gap چه چیزی را فاصله می‌دهد.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-46-2" name="chk-46-2" type="checkbox"/><span>می‌توانی فرق اندازهٔ ذاتی Logo و قاب Logo را بیان کنی.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-47"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-47-1" name="chk-47-1" type="checkbox"/><span>Logo Strip را با Flexbox، Wrap و Gap می‌سازی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-47-2" name="chk-47-2" type="checkbox"/><span>در 320px ثابت می‌کنی Logoها Wrap می‌شوند و اسکرول افقی باقی نمی‌ماند.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-48"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-48-1" name="chk-48-1" type="checkbox"/><span>برای فهرست Tagها یا Badgeهای یک Card می‌توانی تصمیم بگیری Wrap لازم است یا نه.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-8-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-8-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>ایستگاه B نزدیک است. در درس بعد Grid را یاد می‌گیری تا بدانی چه زمانی Flexbox انتخاب اشتباهی است.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 8</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-8-completion"><fieldset><legend>ثبت پایان درس 8</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-8-complete" name="lesson-8-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-8-practical-findings"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-8-practical-findings-heading" role="heading">🔎 یافتهٔ عملی و خطایابی</span></summary><section aria-labelledby="lesson-8-practical-findings-heading" class="disclosure-content practical-findings">
<p class="finding-scope">این بخش فقط ادعاهایی را آموزش می‌دهد که یا در مشاهدهٔ واقعی ثبت شده‌اند یا Help Center رسمی Elementor آن‌ها را صریحاً پشتیبانی می‌کند. نتیجه‌های وابسته به Theme، نسخه یا ساختار DOM با دامنهٔ اعتبار نوشته شده‌اند.</p>
<article class="finding-card" data-verification="verified_by_official_help" id="finding-wrap-overflow">
<div class="evidence-badges"><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>چرا آیتم‌های Logo Strip در یک خط فشرده یا بیرون‌زده‌اند؟</h3>
<p><strong>نشانه:</strong> با کم‌شدن عرض، آیتم‌ها کوچک، فشرده یا خارج از مرز می‌شوند و انتظار داشتی خودکار به خط بعد بروند.</p>
<p><strong>قاعدهٔ رسمی:</strong> Wrap تعیین می‌کند آیتم‌ها مجبور به ماندن در یک خط باشند یا برای حفظ محتوا به ردیف/ستون‌های اضافه بروند.</p>
<div class="finding-checks">
<section><h4>در Elementor</h4><p>Container → Layout → Wrap و سپس Width/Basis هر child را بررسی کن.</p></section>
<section><h4>تلهٔ رایج</h4><p>فعال‌کردن Wrap به‌تنهایی طراحی responsive را کامل نمی‌کند؛ min-width، gap و اندازهٔ واقعی childها همچنان مهم‌اند.</p></section>
</div>
<p class="golden-rule"><strong>قانون طلایی:</strong> Wrap اجازهٔ ساخت خط جدید می‌دهد؛ فضای لازم هر آیتم را تولید نمی‌کند.</p>
<details class="more-know"><summary>منبع رسمی</summary><p><a href="https://elementor.com/help/how-do-flexbox-containers-work/">Understanding how Flexbox containers work — Wrap</a></p></details>
</article>
</section></details>
<details class="lesson-disclosure" id="lesson-8-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Logo Strip در عرض‌های میانی</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>طرح Mobile چهار نشان را در یک ردیف نشان می‌دهد، اما این فقط یک viewport مرجع است. بین Tablet و Mobile ممکن است لوگوها بیش از حد کوچک شوند.</p>
<ul><li>Wrap یا Grid را در عرض‌های میانی آزمایش کن.</li><li>برای هر لوگو حداقل عرض خوانا تعریف کن.</li><li>مخفی‌کردن لوگو را جایگزین حل layout نکن مگر تصمیم UX داشته باشی.</li></ul>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-8-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: Wrap و Logo Strip در عرض‌های میانی</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> رفتار لوگوها را فقط در سه آیکون دستگاه نسنج؛ عرض‌های بین آن‌ها را هم آزمایش کن.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>چهار لوگو با اندازه‌های متفاوت داخل یک Container قرار بده.</li><li>حالت No Wrap و Wrap را مقایسه کن.</li><li>Gap و حداقل عرض لوگوها را طوری تنظیم کن که خوانایی حفظ شود.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>قبل از کاهش عرض بگو اولین شکست در کدام لوگو یا فاصله رخ می‌دهد.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>No Wrap را نگه دار و برای لوگوها Width ثابت بزرگ تعیین کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>flex-wrap، gap، Width/Min Width آیتم‌ها و scrollWidth Container.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> در عرض‌های بین Tablet و Mobile، لوگوها نه له می‌شوند و نه اسکرول افقی می‌سازند.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-8-responsive-build-test-done-build"><input data-persist="" id="lesson-8-responsive-build-test-done-build" name="lesson-8-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-8-responsive-build-test-done-test"><input data-persist="" id="lesson-8-responsive-build-test-done-test" name="lesson-8-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-8-responsive-build-test-done-debug"><input data-persist="" id="lesson-8-responsive-build-test-done-debug" name="lesson-8-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-8-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-8-responsive-build-test-note" name="lesson-8-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/responsive-design-using-containers/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-8-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Wrap و Logo Strip spacing</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
