<article class="lesson card-surface" data-trackable="lesson-v17-atomic-forms" id="lesson-v17-atomic-forms">
<h2 class="former-h1">تکمیلی 18D — Atomic Forms در Elementor 4</h2>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🧭 قطب‌نمای درس</span></summary><section class="disclosure-content lesson-section">
<p><strong>هدف:</strong> فرم را دیگر یک Element/Widget آماده جادویی نبینی؛ فرم در Atomic Editor از Atomهای کوچک‌تر ساخته می‌شود: Label، Input، Textarea، Checkbox، Radio، Select، Submit و تنظیمات بعد از ارسال.</p>
</section></details>
<section class="lesson-section lesson-core-concept" data-core-concept="true">
<h2>A. فرم یعنی مکالمهٔ کنترل‌شده با کاربر</h2>
<p>یک دانش‌آموز گیج معمولاً فرم را این‌طور می‌بیند: «چند فیلد بگذار و تمام». اما فرم خوب یعنی پاسخ دادن به سه سؤال: چه چیزی می‌پرسم؟ چرا می‌پرسم؟ اگر کاربر اشتباه کرد، چطور کمکش می‌کنم؟</p>
<table><caption>جدول آموزشی دوره — A. فرم یعنی مکالمهٔ کنترل‌شده با کاربر</caption><thead><tr><th scope="col">Atom</th><th scope="col">نقش آموزشی</th><th scope="col">اشتباه رایج</th></tr></thead><tbody>
<tr><td>Label</td><td>اسم سؤال</td><td>Placeholder را جای Label گذاشتن</td></tr>
<tr><td>Input</td><td>پاسخ کوتاه</td><td>استفاده برای متن بلند</td></tr>
<tr><td>Textarea</td><td>پاسخ بلند</td><td>ندادن ارتفاع و راهنمای کافی</td></tr>
<tr><td>Checkbox / Radio</td><td>انتخاب چندتایی یا تک‌گزینه‌ای</td><td>قاطی کردن چندگزینه‌ای و تک‌گزینه‌ای</td></tr>
<tr><td>Submit</td><td>تعهد نهایی کاربر</td><td>متن مبهم مثل «ارسال» بدون زمینه</td></tr>
</tbody></table>
</section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="e975130934668914f18038b65ddae917741b57aa4566fc4aeb177f0276d9fd81" id="lesson-v17-atomic-forms-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Atomic Form؛ فرم به‌عنوان ساختار و جریان وضعیت</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="21" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-21-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-21-section-01">مسئله‌ای که Atomic Form حل می‌کند</h3><p>فرم فقط چند Input کنار هم نیست. فرم یک جریان ارتباطی است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">کاربر اطلاعات می‌دهد
↓
اعتبارسنجی می‌شود
↓
ارسال می‌شود
↓
Success یا Error رخ می‌دهد
</code></pre></figure><p>اگر فقط ظاهر Input را طراحی کنی، ممکن است Label، Error، Focus و پیام نتیجه فراموش شوند.</p><hr/></section><section aria-labelledby="concept-v31-21-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-21-section-02">تشبیه به دنیای واقعی: باجهٔ اداره</h3><p>یک باجه را تصور کن:</p><ul>
<li>Form Wrapper = خود باجه</li>
<li>Label = عنوان هر بخش فرم</li>
<li>Input = کادر اطلاعات</li>
<li>Required = مدارک اجباری</li>
<li>Validation = بررسی مأمور</li>
<li>Submit = تحویل پرونده</li>
<li>Success = رسید پذیرش</li>
<li>Error = اعلام نقص پرونده</li>
</ul><p>باجه زیبا بدون راهنمای درست، مردم را سردرگم می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-21-section-03" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-21-section-03">چرا Atomic؟</h3><p>در مدل Atomic، Form Wrapper شامل Elementهای مستقل‌تر است:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Atomic Form
├── Label + Input
├── Label + Select
├── Checkbox
├── Submit Button
├── Success Message
└── Error Message
</code></pre></figure><p>این ساختار کنترل بیشتری بر Layout و Style می‌دهد، اما مسئولیت بیشتری نیز دارد. طراح باید ارتباط معنایی Fieldها، IDها، Labelها و پیام‌ها را درست نگه دارد.</p><hr/></section><section aria-labelledby="concept-v31-21-section-04" class="concept-reference-part"><h3 id="concept-v31-21-section-04">State Machine فرم</h3><p>در مستندات رسمی فعلی Appearanceهای اصلی Form شامل این حالت‌هاست:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Normal
├── Success
└── Error
</code></pre></figure><p>از نظر مفهومی، در زمان ارسال یک وضعیت Pending/Submitting نیز وجود دارد، اما پشتیبانی Native آن به‌عنوان Appearance قابل Style در منابع رسمی بررسی‌شده اثبات نشده است.</p><p>پس دو سطح را جدا کن:</p><h4>وضعیت‌های رسمی قابل استناد</h4><ul>
<li>Normal</li>
<li>Success</li>
<li>Error</li>
</ul><h4>نیاز UX پیشنهادی و نیازمند بررسی پیاده‌سازی</h4><ul>
<li>Submitting/Pending</li>
<li>Disabled Submit</li>
<li>Busy Indicator</li>
<li>جلوگیری از ارسال تکراری</li>
</ul><hr/></section><section aria-labelledby="concept-v31-21-section-05" class="concept-reference-part"><h3 id="concept-v31-21-section-05">Label و Input</h3><p>Placeholder جای Label نیست.</p><p>Placeholder با تایپ ناپدید می‌شود و ممکن است Contrast کمی داشته باشد. Label باید مشخص کند Field چیست.</p><p>اتصال Label و Input معمولاً با <code class="inline-code" dir="ltr">for</code> و <code class="inline-code" dir="ltr">id</code> انجام می‌شود. IDهای Field باید یکتا و قابل پیش‌بینی باشند.</p><hr/></section><section aria-labelledby="concept-v31-21-section-06" class="concept-reference-part"><h3 id="concept-v31-21-section-06">Validation</h3><p>پیام Error باید:</p><ul>
<li>نزدیک Field مربوط باشد؛</li>
<li>فقط با رنگ منتقل نشود؛</li>
<li>قابل فهم باشد؛</li>
<li>مسیر اصلاح را بگوید؛</li>
<li>در صورت امکان برای Screen Reader اعلام شود.</li>
</ul><p>بد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Invalid input
</code></pre></figure><p>بهتر:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">شماره تلفن باید ۱۱ رقم باشد.
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-21-section-07" class="concept-reference-part"><h3 id="concept-v31-21-section-07">Focus Management</h3><p>پس از Error، کاربر باید بفهمد کجا مشکل دارد. در فرم طولانی، انتقال Focus به خلاصه خطا یا اولین Field نامعتبر می‌تواند مفید باشد، اما رفتار واقعی باید با ابزار و پیاده‌سازی موجود سنجیده شود.</p><p>پس از Success نیز پیام نتیجه باید قابل مشاهده و قابل اعلام باشد.</p><p><code class="inline-code" dir="ltr">aria-live</code> می‌تواند در بعضی سناریوها برای پیام نتیجه مناسب باشد، اما افزودن آن باید با Markup واقعی و بدون تکرار مزاحم آزمایش شود.</p><hr/></section><section aria-labelledby="concept-v31-21-section-08" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-21-section-08">در Elementor V4</h3><p>برای هر Form این نقشه را بساز:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Purpose
Fields
Required fields
Validation messages
Submit action
Success behavior
Error behavior
Email/collection action
Privacy text
Keyboard path
</code></pre></figure><p>Appearanceهای Normal، Success و Error را جدا طراحی کن. Success Message و Fail Message را حذف نکن یا صرفاً به رنگ وابسته نکن.</p><hr/></section><section aria-labelledby="concept-v31-21-section-09" class="concept-reference-part"><h3 id="concept-v31-21-section-09">Layout فرم</h3><p>در Desktop ممکن است دو Field کنار هم باشند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[نام] [نام خانوادگی]
</code></pre></figure><p>در Mobile:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">[نام]
[نام خانوادگی]
</code></pre></figure><p>Parent Layout باید اجازه دهد Label و Error همراه Field خود بمانند. Grid برای فرم‌های چندستونه مفید است، ولی ترتیب DOM باید با مسیر منطقی Tab سازگار بماند.</p><hr/></section><section aria-labelledby="concept-v31-21-section-10" class="concept-reference-part"><h3 id="concept-v31-21-section-10">Dynamic و Conditional Form</h3><p>اگر Fieldها براساس انتخاب قبلی نمایش داده می‌شوند:</p><ul>
<li>Required بودن Field مخفی را بررسی کن.</li>
<li>ترتیب Focus را آزمایش کن.</li>
<li>Error مربوط به Field پنهان نباید کاربر را گیر بیندازد.</li>
<li>Layout نباید با نمایش Field جدید جهش نامفهوم داشته باشد.</li>
</ul><p>این رفتارها ممکن است به Add-on یا قابلیت‌های خارج از Atomic Form پایه وابسته باشند و باید نسخه‌محور مستند شوند.</p><hr/></section><section aria-labelledby="concept-v31-21-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-21-section-11">اشتباهات رایج</h3><ul>
<li>Placeholder به‌جای Label</li>
<li>Error فقط قرمز</li>
<li>Success Message نامشخص</li>
<li>Field ID تکراری</li>
<li>ترتیب دیداری مخالف ترتیب Tab</li>
<li>نبود Feedback هنگام ارسال</li>
<li>چندبار ارسال‌شدن Form</li>
<li>پنهان‌کردن Error با Overflow</li>
<li>فرض وجود State Native Submitting بدون شواهد</li>
<li>ادعای Dynamic Class رسمی برای Stateهای Form بدون Fixture</li>
</ul><hr/></section><section aria-labelledby="concept-v31-21-section-12" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-21-section-12">پل به DevTools و Accessibility Tree</h3><ul>
<li>با Tab کل Form را طی کن.</li>
<li>Label مرتبط را در Accessibility Tree ببین.</li>
<li>Stateهای Error و Success را در Frontend واقعی اجرا کن.</li>
<li>Network request، Response و Disabled شدن Button را بررسی کن.</li>
<li>فقط Preview ظاهری کافی نیست.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-21-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-21-section-13">تصویر ذهنی نهایی</h3><p>فرم باجهٔ اداری است. Inputها فقط کاغذها هستند؛ تجربهٔ واقعی را راهنما، بررسی، رسید موفقیت و توضیح خطا می‌سازند.</p><hr/></section><section aria-labelledby="concept-v31-21-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-21-section-14">قوانین طلایی</h3><ul>
<li><strong>«Form یک جریان وضعیت است، نه مجموعه‌ای از کادرها.»</strong></li>
<li><strong>«Placeholder جای Label را نمی‌گیرد.»</strong></li>
<li><strong>«Error باید قابل فهم، قابل یافتن و قابل اصلاح باشد.»</strong></li>
<li><strong>«Normal، Success و Error را جدا طراحی و آزمایش کن.»</strong></li>
<li><strong>«Submitting نیاز واقعی UX است، اما قابلیت Native آن را بدون سند قطعی فرض نکن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Atomic Form element</li>
<li>WAI guidance for form labels, errors and keyboard focus</li>
<li>Elementor Help: V4 elements and form actions</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-v17-atomic-forms-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-v17-atomic-forms-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Atomic Form؛ ساختار فرم بدون واحد است، Style فیلد واحد می‌گیرد</span></summary>
<section aria-labelledby="lesson-v17-atomic-forms-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Form wrapper، field type و validation مفهوم‌اند؛ Width، Gap، Padding و Typography فیلدها اندازه می‌گیرند.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> فرم مثل پرسش‌نامه است: نوع سؤال واحد ندارد، اما اندازهٔ کادر و فاصلهٔ خطوط دارد.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Field type</th><td><code dir="ltr">input type / element</code></td><td>text/email/…</td><td>keyword/string</td><td>برای semantics و validation.</td><td>اندازهٔ فیلد نوع آن را عوض نمی‌کند.</td><td><code dir="ltr">E_FORM</code></td></tr><tr><th scope="row">Field width</th><td><code dir="ltr">width / max-width</code></td><td>واحدهای Size control</td><td>Parent</td><td>برای layout پاسخ‌گو.</td><td>width ثابت ممکن است در Mobile overflow کند.</td><td><code dir="ltr">E_SIZE</code></td></tr><tr><th scope="row">Field spacing</th><td><code dir="ltr">gap / padding / margin</code></td><td>واحدهای Spacing</td><td>Parent/font/viewport برحسب واحد</td><td>برای خوانایی و touch target.</td><td>فاصلهٔ کم دسترسی‌پذیری را ضعیف می‌کند.</td><td><code dir="ltr">E_SPACING</code></td></tr><tr><th scope="row">Typography</th><td><code dir="ltr">font-size / line-height</code></td><td>واحدهای Typography</td><td>root/parent/viewport</td><td>برای label و help text.</td><td>placeholder جای label نیست.</td><td><code dir="ltr">E_TYPO</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>دو فیلد 50% با gap 24px در Parent=600px از 600px عبور می‌کنند مگر basis/width یا gap در محاسبه جبران شود.</p></section>
<section><h3>📱 در Responsive</h3><p>در Mobile فیلدها معمولاً 100% می‌شوند؛ touch target و error text را با محتوای واقعی تست کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>width، min-width، gap، padding و focus state فیلد را بررسی کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/atomic-form-element/" rel="noopener noreferrer" target="_blank">Elementor V4 — Atomic Form</a>، <a href="https://elementor.com/help/style-tab-size/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Size</a>، <a href="https://elementor.com/help/style-tab-spacing/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Spacing</a>، <a href="https://elementor.com/help/style-tab-typography/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Typography</a></footer>
</section>
</details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">B. Style فرم را سیستماتیک کن</span></summary><section class="disclosure-content lesson-section">
<p>برای فرم، Global Classها را روی نقش‌ها بساز: <code class="inline-code" dir="ltr">form-field</code>، <code class="inline-code" dir="ltr">form-label</code>، <code class="inline-code" dir="ltr">form-submit</code>. برای رنگ و فاصله از Variables استفاده کن. این باعث می‌شود فرم با بقیهٔ سایت هم‌خانواده شود.</p>
<aside class="teacher-note"><p><strong>هشدار استاد:</strong> اگر فقط Submit را زیبا کنی اما Focus state فیلدها ضعیف باشد، فرم از نظر دسترسی‌پذیری ناقص است. کاربر کیبوردی باید دقیقاً بفهمد کجاست.</p></aside>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">تمرین</span></summary><section class="disclosure-content lesson-section">
<ol><li>یک فرم سه‌فیلدی بساز: نام، ایمیل، پیام.</li><li>برای Label و Input دو Global Class جدا بساز.</li><li>Focus state را واضح کن.</li><li>یک پیام راهنما برای خطا یا required بودن فیلد بنویس.</li><li>در موبایل بررسی کن فاصلهٔ بین فیلدها با لمس انگشت راحت است یا نه.</li></ol>
</section></details>
<details class="lesson-disclosure" id="lesson-v17-atomic-forms-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Atomic Form و دسترسی‌پذیری فرم</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Atomic Form در برابر Form Element/Widget آماده قدیمی</h3><p>Atomic Form یک wrapper اتمیک با Atomهای داخلی است؛ فرم قدیمی بیشتر شبیه widget یکپارچه بود. در V4 باید فرم را مثل ساختار قابل ترکیب ببینی.</p></section>
<section class="inline-compare-card"><h3>Label در برابر Placeholder</h3><p>Label تابلو دائمی روی در است؛ Placeholder نوشتهٔ کم‌رنگی است که با تایپ ناپدید می‌شود. برای فرم واقعی، Label را قربانی زیبایی نکن.</p></section>
</div>
</section></details>
<p class="v30-value-type-note"><strong>نوع مقدار غالب این درس:</strong> <code dir="ltr">reference / keyword / unitless</code>؛ محتوای واحد مصنوعی اضافه نشده است.</p></article>
