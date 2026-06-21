<article class="lesson card-surface" data-lesson="16" id="lesson-16">

<h2 class="lesson-title former-h1">درس 16 — State، Hover، Focus و دسترسی‌پذیری</h2>

<details class="lesson-disclosure" open>
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-16-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span>
</summary>
<section aria-labelledby="lesson-16-lesson-compass-1" class="disclosure-content lesson-section lesson-compass">
<p><strong>در این درس یاد می‌گیری:</strong> هر عنصر تعاملی را فقط در حالت Normal نبینی؛ برای Hover، Focus، Focus Visible، Active، Disabled و Selected قرارداد طراحی و تست بنویسی.</p>
<p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Interaction پیچیده با JavaScript، ARIA پیشرفته، ساخت Component interactive کامل، یا طراحی نهایی تمام حالت‌های سایت.</p>
<p><strong>در پایان باید بتوانی:</strong> CTA، لینک، Feature Item یا Node تعاملی را با Mouse، Keyboard، Zoom و Contrast تست کنی؛ بدون حذف Focus Ring و بدون وابستگی اطلاعات به Hover یا رنگ تنها.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-16-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span>
</summary>
<section aria-labelledby="lesson-16-lesson-meta-2" class="lesson-meta disclosure-content lesson-section">
<div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0">
<table class="data-table educational-table edu-table">
<caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption>
<thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead>
<tbody>
<tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr>
<tr><th scope="row">نوع فعالیت</th><td>♿ دسترسی‌پذیری + 🛠 اجرایی + 🔍 عیب‌یابی</td></tr>
<tr><th scope="row">هستهٔ فهم</th><td>۲۵–۳۵ دقیقه</td></tr>
<tr><th scope="row">تثبیت و تمرین</th><td>۳۰–۴۵ دقیقه</td></tr>
<tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr>
</tbody>
</table>
</div>
<aside aria-label="راهنمای معلم" class="teacher-note">
<p><strong>راهنمای معلم:</strong> هنرجو باید Hover، Focus و Keyboard را جدا تست کند. تمرین را با Tab و Zoom انجام بده، نه فقط با Mouse.</p>
</aside>
<p class="status-line"><code class="inline-code" dir="ltr">status: revised_state_accessibility_context</code></p>
</section>
</details>

<section aria-labelledby="lesson-16-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true">
<h2 id="lesson-16-lesson-understand-4">A. بفهم</h2>

<h3>پیوند با درس‌های قبلی</h3>
<p>در درس‌های قبل ساختار، Layout، Position، Layering، Responsive و RTL را ساختی. حالا باید عناصر تعاملی را قابل استفاده کنی. یک Button فقط یک مستطیل زیبا نیست؛ باید در Stateهای مختلف بازخورد واضح بدهد.</p>
<figure class="concept-code-figure">
<pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Normal Layout
↓
Interactive Element
↓
State Contract
↓
Hover / Focus / Active / Disabled
↓
Keyboard / Zoom / Contrast / Target Size</code></pre>
</figure>

<h3>State یعنی چه؟</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<dl class="term-grid">
<dt>Normal</dt><dd>حالت پایه؛ عنصر هنوز تعامل مستقیم نگرفته است.</dd>
<dt>Hover</dt><dd>Pointer/Mouse روی عنصر است.</dd>
<dt>Focus</dt><dd>عنصر با Keyboard یا روش ناوبری فعال است.</dd>
<dt>Focus Visible</dt><dd>Focus باید برای کاربر قابل دیدن باشد؛ معمولاً با outline/ring.</dd>
<dt>Active</dt><dd>لحظهٔ فعال‌سازی، مثل فشردن دکمه.</dd>
<dt>Disabled</dt><dd>عنصر فعلاً قابل استفاده نیست؛ باید واضح و غیرقابل تعامل باشد.</dd>
<dt>Selected / Current</dt><dd>حالت انتخاب‌شده یا صفحه/آیتم فعلی.</dd>
</dl>
</section>

<h3>Hover جای Focus را نمی‌گیرد</h3>
<p>Hover برای Mouse/Pointer است. Focus برای Keyboard، Switch Control و روش‌های ناوبری غیرماوسی حیاتی است. اگر فقط Hover طراحی شود، کاربر Keyboard ممکن است نداند کجای صفحه است.</p>

<h3>Focus Ring را حذف نکن</h3>
<p>حذف <code dir="ltr">outline</code> فقط برای تمیزترشدن ظاهر، خطای جدی است. اگر outline پیش‌فرض زیبا نیست، آن را با Focus Style بهتر جایگزین کن؛ نه اینکه Focus را نامرئی کنی.</p>

<h3>اطلاعات فقط با رنگ یا Hover منتقل نشود</h3>
<p>اگر خطا، وضعیت فعال، لینک، selected state یا پیام مهم فقط با رنگ یا Hover مشخص شود، بخشی از کاربران آن را از دست می‌دهند. از ترکیب رنگ، متن، Icon، underline، border، shape یا label استفاده کن.</p>

<h3>Target Size و فاصله</h3>
<p>عنصر قابل کلیک باید به اندازهٔ کافی بزرگ و از عناصر مجاور جدا باشد. در Mobile، دکمهٔ کوچک یا Link نزدیک به Link دیگر، خطای استفاده‌پذیری است؛ حتی اگر از نظر ظاهری تمیز باشد.</p>

<h3>Zoom 200%</h3>
<p>در Zoom بالا، متن و کنترل‌ها باید قابل خواندن و استفاده بمانند. اگر Focus Ring در Zoom بریده می‌شود، احتمالاً Overflow یا Layering قبلی باید بازبینی شود.</p>

<h3>State با Layering و Overflow مرتبط است</h3>
<p>در درس ۱۳ گفتیم <code dir="ltr">overflow:hidden</code> می‌تواند Focus Ring را ببرد. پس Accessibility فقط رنگ دکمه نیست؛ به Layout، Overflow، z-index و Position هم وابسته است.</p>

<h3>Interactive یا Decorative؟</h3>
<p>همهٔ Nodeها یا Cardها نباید تعاملی شوند. اگر Orbit Node فقط تزئینی است، نباید focusable شود. اگر واقعاً کلیک‌پذیر است، باید keyboard focus، accessible name و state داشته باشد.</p>

<h3>قاعدهٔ این درس</h3>
<p>برای هر عنصر تعاملی مهم، قبل از Style نهایی یک State Contract بنویس: Normal، Hover، Focus Visible، Active، Disabled و Selected در صورت نیاز. سپس با Mouse، Keyboard، Zoom و Contrast تست کن.</p>
<hr/>
</section>

<details class="lesson-disclosure conceptual-reference" data-concept-version="tuya-revised-16.0.0" id="lesson-16-concept-reference">
<summary>📚 مرجع مفهومی کامل — State؛ Normal، Hover، Focus، Focus Visible و Active</summary>
<div class="concept-reference-body concept-reference-v31" data-concept-index="16" data-source-version="tuya-revised-16.0.0">

<p class="concept-reference-lead">این مرجع، بخش مفهومی فعلی درس را حفظ می‌کند و آن را به پروژهٔ TUYA وصل می‌کند. هدف این نیست که همهٔ Interactionها را بسازی؛ هدف این است که هر تعامل ساده قابل استفاده، قابل دیدن و قابل تست باشد.</p>

<section class="concept-reference-part concept-reference-problem" aria-labelledby="lesson-16-ref-problem">
<h3 id="lesson-16-ref-problem">۱. مسئله‌ای که State حل می‌کند</h3>
<p>یک Button فقط یک ظاهر ثابت ندارد. کاربر باید بفهمد:</p>
<ul>
<li>آیا این عنصر قابل کلیک است؟</li>
<li>آیا Pointer روی آن قرار گرفته؟</li>
<li>آیا با Keyboard به آن رسیده‌ام؟</li>
<li>آیا همین لحظه فعال شده؟</li>
<li>آیا غیرفعال است؟</li>
<li>آیا انتخاب‌شده یا صفحهٔ فعلی است؟</li>
</ul>
<p>State زبان بازخورد رابط است. بدون State، کاربر باید حدس بزند.</p>
</section>

<section class="concept-reference-part concept-reference-analogy" aria-labelledby="lesson-16-elevator">
<h3 id="lesson-16-elevator">۲. تشبیه دکمهٔ آسانسور</h3>
<p>دکمهٔ آسانسور همیشه همان دکمه است، اما وضعیتش تغییر می‌کند:</p>
<ul>
<li><strong>Normal:</strong> خاموش و آماده است.</li>
<li><strong>Hover:</strong> دست نزدیک شده یا روی آن است.</li>
<li><strong>Focus:</strong> اکنون مقصد ورودی Keyboard است.</li>
<li><strong>Active:</strong> دکمه فشرده شده است.</li>
<li><strong>Selected:</strong> چراغ روشن شده و مقصد ثبت شده است.</li>
<li><strong>Disabled:</strong> دکمه فعلاً کار نمی‌کند.</li>
</ul>
<p>در UI هم کاربر باید این تفاوت‌ها را بدون حدس بفهمد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-hover">
<h3 id="lesson-16-hover">۳. Hover</h3>
<p>Hover کمک بصری برای Pointer است، اما نباید تنها راه دیدن اطلاعات مهم باشد. در Touch device ممکن است Hover وجود نداشته باشد یا رفتار آن متفاوت باشد.</p>
<p>Hover خوب معمولاً subtle است: تغییر رنگ، سایه، border، icon motion محدود یا background. اما اگر تغییر زیاد باشد، ممکن است Layout shift یا distraction بسازد.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-focus">
<h3 id="lesson-16-focus">۴. Focus و Focus Visible</h3>
<p>Focus نشان می‌دهد کاربر با Keyboard الان کجاست. Focus باید واضح باشد، با Contrast مناسب دیده شود و توسط Overflow یا z-index پنهان نشود.</p>
<p>Focus Visible یعنی وقتی Focus باید برای کاربر قابل مشاهده باشد، Style مخصوص دیده شود. در طراحی عملی، یک Ring یا Outline واضح‌تر از یک تغییر رنگ خیلی ظریف است.</p>
<aside class="warning-card">
<p><strong>خطا:</strong> <code dir="ltr">outline: none</code> بدون جایگزین قابل مشاهده.</p>
</aside>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-active-disabled">
<h3 id="lesson-16-active-disabled">۵. Active، Disabled و Selected</h3>
<ul>
<li><strong>Active:</strong> لحظهٔ فشردن یا فعال‌سازی. معمولاً کوتاه و tactile است.</li>
<li><strong>Disabled:</strong> غیرقابل استفاده. باید هم از نظر ظاهری و هم از نظر رفتار غیرقابل تعامل باشد؛ اما متن آن باید هنوز خوانا باشد.</li>
<li><strong>Selected/Current:</strong> آیتم انتخاب‌شده یا صفحهٔ فعلی. نباید فقط با رنگ مشخص شود.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-keyboard">
<h3 id="lesson-16-keyboard">۶. Keyboard Testing</h3>
<p>برای هر عنصر تعاملی، با این ترتیب تست کن:</p>
<ol>
<li>آیا با Tab به آن می‌رسم؟</li>
<li>آیا Focus واضح است؟</li>
<li>آیا ترتیب Tab با ترتیب خواندن و ظاهر منطقی سازگار است؟</li>
<li>آیا با Enter یا Space فعال می‌شود، اگر نقش آن Button است؟</li>
<li>آیا Focus در modal/menu گم نمی‌شود؟</li>
<li>آیا Shift+Tab هم مسیر منطقی دارد؟</li>
</ol>
<p>در این درس Modal/Menu پیچیده نمی‌سازیم، اما ذهنیت Keyboard test را همین‌جا تثبیت می‌کنیم.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-target">
<h3 id="lesson-16-target">۷. Target Size و Pointer</h3>
<p>یک لینک یا دکمهٔ کوچک روی Mobile شاید ظاهراً شیک باشد، اما قابل لمس نباشد. اگر چند لینک نزدیک هم هستند، فاصلهٔ کافی لازم است. اندازهٔ هدف تعاملی فقط متن نیست؛ padding و hit area هم مهم است.</p>
<p>در Elementor، padding دکمه را فقط برای زیبایی کم نکن. استفاده‌پذیری را هم تست کن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-contrast">
<h3 id="lesson-16-contrast">۸. Contrast و Color-only</h3>
<p>رنگ Hover یا Focus باید با پس‌زمینه قابل تشخیص باشد. اما رنگ تنها برای انتقال وضعیت کافی نیست. مثال:</p>
<ul>
<li>لینک فقط آبی‌تر نشود؛ underline یا indicator هم داشته باشد.</li>
<li>Selected فقط با رنگ پس‌زمینه نباشد؛ border/icon/label هم کمک کند.</li>
<li>Error فقط قرمز نباشد؛ متن خطا یا icon هم داشته باشد.</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-tuya-contract">
<h3 id="lesson-16-tuya-contract">۹. State Contract برای TUYA</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="TUYA State Contract">
<table class="data-table educational-table edu-table">
<caption>State Contract پیشنهادی TUYA</caption>
<thead><tr><th scope="col">عنصر</th><th scope="col">State لازم</th><th scope="col">تصمیم اولیه</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Primary CTA</th><td>Normal / Hover / Focus Visible / Active / Disabled</td><td>Focus ring واضح، target مناسب، بدون layout shift</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Secondary Link</th><td>Normal / Hover / Focus</td><td>Underline یا indicator، نه فقط رنگ</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Feature Item</th><td>اگر فقط متن است: غیرتعاملی</td><td>Focusable نشود مگر واقعاً action داشته باشد</td><td><code dir="ltr">confirmed_rule</code></td></tr>
<tr><th scope="row">Orbit Node</th><td>اگر clickable است: Focus/Active/Name</td><td>Decorative Node focusable نشود</td><td><code dir="ltr">unknown_until_interaction</code></td></tr>
<tr><th scope="row">Logo</th><td>اگر link است: Focus و accessible name</td><td>اگر decorative است: focusable نیست</td><td><code dir="ltr">case_by_case</code></td></tr>
</tbody>
</table>
</div>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-overflow">
<h3 id="lesson-16-overflow">۱۰. Focus Ring و Overflow</h3>
<p>اگر Focus Ring روی دکمه یا Node دیده نمی‌شود، قبل از تغییر رنگ بررسی کن:</p>
<ul>
<li>Parent <code dir="ltr">overflow:hidden</code> دارد؟</li>
<li>z-index یا stacking context حلقه را زیر چیزی برده؟</li>
<li>outline offset منفی یا خیلی کوچک است؟</li>
<li>contrast با پس‌زمینه کافی نیست؟</li>
<li>Focus style فقط در Hover تعریف شده؟</li>
</ul>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-zoom">
<h3 id="lesson-16-zoom">۱۱. Zoom و Reflow</h3>
<p>در Zoom بالا، متن، دکمه و Focus Ring باید هنوز قابل استفاده باشند. اگر متن داخل Button بریده شد، فقط Font را کوچک نکن؛ padding، width، wrapping، min/max size و line-height را بررسی کن.</p>
</section>

<section class="concept-reference-part" aria-labelledby="lesson-16-no-js">
<h3 id="lesson-16-no-js">۱۲. در این درس JavaScript نمی‌سازیم</h3>
<p>Stateهای پایه مثل Hover، Focus، Active و Disabled معمولاً با CSS/Elementor state controls یا pseudo-classها قابل بررسی‌اند. Interaction پیچیده با JavaScript، ARIA dynamic state یا component state machine موضوع درس‌های بعدی/پیشرفته است.</p>
</section>

<section class="concept-reference-part concept-reference-traps" aria-labelledby="lesson-16-traps">
<h3 id="lesson-16-traps">۱۳. اشتباهات رایج</h3>
<ul>
<li>فقط Normal state را طراحی کردن.</li>
<li>Focus را حذف کردن چون ظاهر را به‌هم می‌زند.</li>
<li>Hover را تنها راه دیدن اطلاعات مهم کردن.</li>
<li>State فعال را فقط با رنگ نشان دادن.</li>
<li>Decorative Node را focusable کردن.</li>
<li>Clickable Card بدون focus style ساختن.</li>
<li>Overflow hidden و بریدن Focus Ring.</li>
<li>Tab order نامنظم به‌خاطر order/absolute/duplicate.</li>
<li>Disabled بسیار کم‌کنتراست و ناخوانا ساختن.</li>
</ul>
</section>

<section class="concept-reference-part concept-reference-golden" aria-labelledby="lesson-16-golden">
<h3 id="lesson-16-golden">۱۴. قوانین طلایی</h3>
<ul>
<li><strong>Hover جای Focus را نمی‌گیرد.</strong></li>
<li><strong>Focus باید قابل دیدن باشد؛ outline را بدون جایگزین حذف نکن.</strong></li>
<li><strong>اطلاعات مهم را فقط با رنگ یا Hover منتقل نکن.</strong></li>
<li><strong>هر عنصر تعاملی باید با Keyboard قابل رسیدن و قابل تشخیص باشد.</strong></li>
<li><strong>Decorative element نباید focusable شود.</strong></li>
<li><strong>Focus Ring را با overflow:hidden یا z-index پنهان نکن.</strong></li>
<li><strong>State Contract را قبل از Style نهایی بنویس.</strong></li>
</ul>
</section>

<footer class="concept-reference-evidence">
<h3>منابع و وضعیت اعتبار</h3>
<p>مفاهیم State، Focus، Keyboard interaction، Zoom، Contrast و target usability بر پایهٔ اصول HTML/CSS و Accessibility نوشته شده‌اند. تصمیم‌های TUYA تا قبل از CTA واقعی، محتوای واقعی و تست مرورگر قطعی نیستند.</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:hover" rel="noopener noreferrer" target="_blank">MDN — :hover</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:focus" rel="noopener noreferrer" target="_blank">MDN — :focus</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible" rel="noopener noreferrer" target="_blank">MDN — :focus-visible</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button" rel="noopener noreferrer" target="_blank">MDN — button element</a></li>
</ul>
</footer>

</div>
</details>

<details class="lesson-disclosure settings-values-units" id="lesson-16-settings-values-units">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" id="lesson-16-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — State، Outline، Target و Contrast</span>
</summary>
<section aria-labelledby="lesson-16-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Stateها واحد عددی نیستند؛ اما Focus Ring، outline offset، padding، hit area و contrast قابل تنظیم‌اند.</p>
<div aria-label="جدول تنظیمات و واحدهای درس ۱۶" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع و تله</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">نوع مقدار</th><th scope="col">مرجع</th><th scope="col">تله</th></tr></thead>
<tbody>
<tr><th scope="row">State</th><td>Normal / Hover / Focus / Active</td><td>interaction context</td><td>Hover و Focus یکی فرض شوند.</td></tr>
<tr><th scope="row">Outline</th><td>color / width / style</td><td>focus indicator</td><td>بدون جایگزین حذف شود.</td></tr>
<tr><th scope="row">Outline Offset</th><td>px / rem</td><td>عنصر و overflow parent</td><td>با overflow hidden بریده شود.</td></tr>
<tr><th scope="row">Padding / Hit Area</th><td>px / rem</td><td>target usability</td><td>برای زیبایی بیش از حد کوچک شود.</td></tr>
<tr><th scope="row">Contrast</th><td>ratio / visual check</td><td>foreground/background</td><td>فقط با چشم و یک مانیتور قضاوت شود.</td></tr>
<tr><th scope="row">Transition</th><td>duration / easing</td><td>motion preference</td><td>خیلی کند یا شدید شود.</td></tr>
</tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر outline offset بیرون Button می‌افتد و Parent overflow hidden دارد، ممکن است ring بریده شود. این مشکل z-index نیست؛ clipping است.</p></section>
<section><h3>📱 در Responsive</h3><p>در Mobile، Hover قابل اتکا نیست. Touch target و active/focus behavior را جدا بررسی کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>:hover، :focus و :focus-visible را force state کن. Computed styles، outline، overflow ancestorها و tab order را بررسی کن.</p></section>
</div>
</section>
</details>

<details class="lesson-disclosure step-through-v2" id="lesson-16-state-step-through">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">🧭 Step‑Through — Mouse، Keyboard یا Touch؟</span>
</summary>
<section class="disclosure-content lesson-section">
<p>هر حالت را پیش‌بینی کن، بعد پاسخ را بخوان.</p>
<div class="table-wrap" role="region" tabindex="0" aria-label="State Step Through">
<table class="data-table educational-table edu-table">
<caption>خلاصهٔ تصمیم‌های State</caption>
<thead><tr><th scope="col">حالت</th><th scope="col">وضعیت</th><th scope="col">تصمیم درست</th><th scope="col">دلیل</th></tr></thead>
<tbody>
<tr><th scope="row">Mouse روی CTA</th><td>Hover</td><td>feedback بصری اضافه</td><td>Pointer را تأیید می‌کند.</td></tr>
<tr><th scope="row">Tab روی CTA</th><td>Focus Visible</td><td>ring/outline واضح</td><td>کاربر Keyboard باید مکان خود را ببیند.</td></tr>
<tr><th scope="row">CTA فقط با رنگ تغییر می‌کند</th><td>Selected یا Active</td><td>indicator دوم اضافه کن</td><td>Color-only کافی نیست.</td></tr>
<tr><th scope="row">Decorative Orbit Node</th><td>تزئینی</td><td>focusable نشود</td><td>کاربر Keyboard نباید روی تزئین گیر کند.</td></tr>
<tr><th scope="row">Clickable Orbit Node</th><td>تعاملی</td><td>Focus، active، name، target</td><td>تعامل باید keyboard-accessible باشد.</td></tr>
</tbody>
</table>
</div>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-16-lesson-practice-5" role="heading">B. بساز و امتحان کن</span>
</summary>
<section aria-labelledby="lesson-16-lesson-practice-5" class="disclosure-content lesson-practice lesson-section">

<h3>🏗 پروژهٔ TUYA — State Contract برای CTA و عناصر تعاملی</h3>
<p>در این تمرین فقط State Contract و تست دسترسی‌پذیری پایه را انجام می‌دهی. هنوز Interaction پیچیده، JavaScript، ARIA dynamic state یا component state machine نداریم.</p>

<h3>مرحلهٔ ۰ — Evidence Gate</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="Evidence Gate lesson 16">
<table class="data-table educational-table edu-table">
<caption>Evidence Gate قبل از طراحی State</caption>
<thead><tr><th scope="col">برچسب</th><th scope="col">در این تمرین</th><th scope="col">نتیجه</th></tr></thead>
<tbody>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Hover جای Focus را نمی‌گیرد.</td><td>هر دو جدا تست می‌شوند.</td></tr>
<tr><th scope="row"><code dir="ltr">confirmed</code></th><td>Focus باید قابل مشاهده باشد.</td><td>outline/ring حذف نمی‌شود مگر جایگزین داشته باشد.</td></tr>
<tr><th scope="row"><code dir="ltr">provisional</code></th><td>رنگ، border، shadow و ring نهایی CTA.</td><td>بعداً با Design System و Contrast تست می‌شود.</td></tr>
<tr><th scope="row"><code dir="ltr">unknown</code></th><td>آیا Orbit Nodeها interactive هستند یا decorative؟</td><td>تا قبل از تصمیم محتوایی focusable نشوند.</td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۱ — فقط State Contract بنویس</h3>
<aside class="implementation-step-card" aria-label="اقدام کوچک درس شانزده">
<h4>فقط یک اقدام کوچک</h4>
<p><strong>هدف:</strong> تعریف حالت‌ها قبل از Style نهایی.</p>
<p><strong>مسیر:</strong> Elementor Editor → انتخاب CTA / لینک‌ها / Nodeهای candidate → Style → State controls یا class state review.</p>
<p><strong>Element هدف:</strong> فقط عناصر واقعاً تعاملی: CTA، لینک، Logo link، Node clickable اگر ثابت شد.</p>
<p><strong>Class فعال:</strong> Classهای موجود؛ Global state token نساز مگر pattern واقعی تکرار شود.</p>
<p><strong>Property:</strong> Normal / Hover / Focus / Active / Disabled / Selected در صورت نیاز.</p>
<p><strong>نباید تغییر کند:</strong> Layout، Responsive Contract، RTL audit، Position نهایی Nodeها، Shadow/Glow نهایی، Animation.</p>
<p><strong>عبارت تأیید پایانی:</strong> «State Contract نوشته شد و CTA با Mouse، Keyboard و Zoom اولیه تست شد.»</p>
</aside>

<h3>مرحلهٔ ۲ — جدول State Contract</h3>
<div class="table-wrap" role="region" tabindex="0" aria-label="State Contract Table">
<table class="data-table educational-table edu-table">
<caption>State Contract برای عناصر TUYA</caption>
<thead><tr><th scope="col">عنصر</th><th scope="col">Normal</th><th scope="col">Hover</th><th scope="col">Focus Visible</th><th scope="col">Active/Disabled</th><th scope="col">وضعیت</th></tr></thead>
<tbody>
<tr><th scope="row">Primary CTA</th><td>خوانا، target کافی</td><td>feedback subtle</td><td>ring واضح و contrast کافی</td><td>active tactile، disabled خوانا</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Secondary Link</th><td>قابل تشخیص به‌عنوان لینک</td><td>underline/color/border</td><td>ring یا underline واضح</td><td>not_applicable یا state مشخص</td><td><code dir="ltr">provisional</code></td></tr>
<tr><th scope="row">Feature Item</th><td>غیرتعاملی مگر action واقعی</td><td>ندارد اگر غیرتعاملی</td><td>focusable نیست</td><td>ندارد</td><td><code dir="ltr">confirmed_rule</code></td></tr>
<tr><th scope="row">Orbit Node</th><td>decorative یا interactive؟</td><td>فقط اگر interactive</td><td>فقط اگر interactive</td><td>unknown</td><td><code dir="ltr">unknown_until_interaction</code></td></tr>
</tbody>
</table>
</div>

<h3>مرحلهٔ ۳ — تست Keyboard</h3>
<ol>
<li>از قبل مشخص کن کدام عناصر باید focusable باشند.</li>
<li>با Tab ذهنی یا واقعی از بالای Section حرکت کن.</li>
<li>هر بار بگو Focus باید کجا دیده شود.</li>
<li>اگر به عنصر تزئینی رسیدی، آن عنصر نباید focusable باشد.</li>
<li>اگر روی CTA رسیدی و حلقه دیده نشد، overflow/z-index/contrast را بررسی کن.</li>
</ol>

<h3>مرحلهٔ ۴ — تست Zoom و Overflow</h3>
<ol>
<li>CTA را در Zoom بالا تصور یا تست کن.</li>
<li>بررسی کن متن دکمه بریده نمی‌شود.</li>
<li>بررسی کن Focus Ring بریده نمی‌شود.</li>
<li>اگر Ring بریده شد، قبل از تغییر رنگ، overflow ancestorها را بررسی کن.</li>
</ol>

<h3>مرحلهٔ ۵ — سؤال توقف</h3>
<p>اگر دکمه در Hover زیباست اما با Tab هیچ نشانهٔ واضحی ندارد، مشکل چیست؟</p>
<form class="interactive-form stop-question-form" data-persist-group="stop-question-16">
<fieldset>
<legend>چک‌لیست یادگیری</legend>
<label class="choice-row"><input data-persist="radio" id="radio-16-a" name="stop-question-16" type="radio" value="A"/><span>A) مشکلی نیست؛ Hover کافی است.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-16-b" name="stop-question-16" type="radio" value="B"/><span>B) Focus Visible طراحی یا دیده نمی‌شود.</span></label>
<label class="choice-row"><input data-persist="radio" id="radio-16-c" name="stop-question-16" type="radio" value="C"/><span>C) باید Button را Absolute کنیم.</span></label>
</fieldset>
</form>
<details class="disclosure-card">
<summary>پاسخ با دلیل</summary>
<p><strong>B درست است.</strong> Hover برای Mouse است، اما Keyboard به Focus Visible نیاز دارد. Button باید با Tab هم مکان خود را نشان دهد.</p>
</details>

<h3>⚠️ تلهٔ اصلی</h3>
<p><strong>تله:</strong> outline را حذف کنی چون از نظر بصری «تمیزتر» است.</p>
<p><strong>نشانه:</strong> با Mouse همه‌چیز خوب است، اما با Keyboard معلوم نیست کجا هستی.</p>
<p><strong>قاعده:</strong> outline را حذف نکن؛ اگر لازم است، Focus Style بهتر بساز.</p>

<h3>🧪 عمداً خرابش کن — روی کاغذ</h3>
<figure class="visual-figure ascii-figure">
<figcaption>Focus خراب</figcaption>
<pre class="ascii-diagram" dir="ltr"><code class="language-css inline-code" dir="ltr">button:focus {
  outline: none;
}

نتیجه:
- کاربر Keyboard مکان خود را نمی‌بیند
- Hover هنوز کار می‌کند اما کافی نیست
- باید جایگزین visible focus ساخته شود</code></pre>
</figure>

<h3>Checkpoint</h3>
<section class="smart-note-card" dir="rtl" lang="fa">
<form class="interactive-form checklist-form" data-persist-group="checklist-91">
<fieldset>
<legend>Checkpoint درس ۱۶</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-91-1" name="chk-91-1" type="checkbox"/><span>برای CTA، Normal/Hover/Focus/Active/Disabled را ثبت کرده‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-91-2" name="chk-91-2" type="checkbox"/><span>Hover را جایگزین Focus نگرفته‌ام.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-91-3" name="chk-91-3" type="checkbox"/><span>Focus Ring قابل دیدن است و با Overflow بریده نشده است.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-91-4" name="chk-91-4" type="checkbox"/><span>اطلاعات مهم فقط با رنگ یا Hover منتقل نمی‌شود.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-91-5" name="chk-91-5" type="checkbox"/><span>Decorative Nodeها focusable نشده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-91-6" name="chk-91-6" type="checkbox"/><span>Interaction پیچیده و JavaScript هنوز وارد نشده است.</span></label>
</fieldset>
</form>
</section>

<h3>Exit Ticket — قبل از ادامه</h3>
<p><strong>بازیابی کوتاه:</strong> Hover، Focus و Active را با مثال یک CTA توضیح بده.</p>
<p><strong>انتقال به موقعیت تازه:</strong> اگر یک Card کامل clickable است، چه چیزهایی را برای Keyboard، Focus و accessible name بررسی می‌کنی؟</p>
<details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<p>پاسخ خوب باید focusable بودن، focus visible، tab order، target size، accessible name، keyboard activation و عدم وابستگی به Hover را بررسی کند.</p>
</details>

</section>
</details>

<details class="lesson-disclosure" id="lesson-16-responsive-checkpoint">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — State در Touch و Zoom</span>
</summary>
<section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> <code dir="ltr">provisional_until_runtime_validation</code></p>
<ul>
<li>Hover را برای Touch device کافی فرض نکن.</li>
<li>CTA را با اندازهٔ Target مناسب بررسی کن.</li>
<li>در Zoom بالا، متن دکمه و Focus Ring نباید بریده شود.</li>
<li>Focus Ring در Mobile/Tablet و در Parentهای دارای overflow بررسی شود.</li>
<li>Stateهای رنگی باید contrast کافی و indicator غیررنگی داشته باشند.</li>
</ul>
</section>
</details>

<details aria-labelledby="lesson-16-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure">
<summary class="lesson-disclosure-summary" id="lesson-16-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary>

<h3>📂 Case Study — Focus دیده نمی‌شود</h3>
<p><strong>هدف:</strong> 🔍 عیب‌یابی کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">debug_first</code></p>
<p>سناریو: با Tab به CTA می‌رسی، اما هیچ نشانهٔ واضحی دیده نمی‌شود.</p>
<section class="smart-note-card" dir="rtl" lang="fa">
<ul>
<li>آیا Focus style تعریف شده؟</li>
<li>آیا outline حذف شده؟</li>
<li>آیا Focus ring پشت لایهٔ دیگری رفته؟</li>
<li>آیا Parent overflow hidden دارد؟</li>
<li>آیا رنگ focus با پس‌زمینه contrast کافی ندارد؟</li>
<li>آیا فقط Hover state طراحی شده؟</li>
<li>آیا عنصر واقعاً focusable است؟</li>
</ul>
</section>
<p>نتیجهٔ درست: ابتدا Focus visibility را برگردان؛ سپس ظاهر را با Design System هماهنگ کن.</p>

<h3>🔬 پشت صحنه</h3>
<p>در DevTools، stateهای <code dir="ltr">:hover</code>، <code dir="ltr">:focus</code> و <code dir="ltr">:focus-visible</code> را force کن. سپس computed outline، box-shadow، z-index و overflow ancestorها را بررسی کن.</p>
<hr/>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-16-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span>
</summary>
<section aria-labelledby="lesson-16-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria">
<p>برای رفتن به درس بعد، سطح ۱ و ۲ اجباری‌اند. سطح ۳ در ایستگاه‌های بعدی تثبیت می‌شود.</p>

<h3>سطح ۱ — فهمیدم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-94">
<fieldset>
<legend>سطح ۱ — فهمیدم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-94-1" name="chk-94-1" type="checkbox"/><span>می‌توانم Hover، Focus، Focus Visible و Active را از هم جدا کنم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-94-2" name="chk-94-2" type="checkbox"/><span>می‌دانم Hover جای Focus را نمی‌گیرد.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-94-3" name="chk-94-3" type="checkbox"/><span>می‌دانم اطلاعات مهم نباید فقط با رنگ یا Hover منتقل شود.</span></label>
</fieldset>
</form>

<h3>سطح ۲ — می‌توانم انجام بدهم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-95">
<fieldset>
<legend>سطح ۲ — می‌توانم انجام بدهم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-95-1" name="chk-95-1" type="checkbox"/><span>برای CTA و لینک‌ها State Contract می‌نویسم.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-95-2" name="chk-95-2" type="checkbox"/><span>با Keyboard و Zoom بررسی می‌کنم Focus Ring و متن دکمه قابل استفاده‌اند.</span></label>
<label class="choice-row"><input data-persist="checkbox" id="chk-95-3" name="chk-95-3" type="checkbox"/><span>Decorative Nodeها را focusable نمی‌کنم و Node تعاملی را بدون Focus رها نمی‌کنم.</span></label>
</fieldset>
</form>

<h3>سطح ۳ — می‌توانم منتقل کنم</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-96">
<fieldset>
<legend>سطح ۳ — می‌توانم منتقل کنم</legend>
<label class="choice-row"><input data-persist="checkbox" id="chk-96-1" name="chk-96-1" type="checkbox"/><span>برای Card clickable می‌توانم state، focus، accessible name و keyboard activation را Audit کنم.</span></label>
</fieldset>
</form>
</section>
</details>

<details class="lesson-disclosure" id="lesson-16-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — State tokens و Focus styles</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions">
<li>Focus ring باید local بماند یا Global Focus Token شود؟</li>
<li>Hover color باید مستقل باشد یا از semantic color token بیاید؟</li>
<li>Disabled state چگونه خوانا و غیرتعاملی می‌ماند؟</li>
<li>Active state فقط tactile است یا معنی selection هم دارد؟</li>
<li>آیا Node واقعاً interactive است یا decorative؟</li>
<li>آیا overflow/Layer Map باعث بریدن Focus می‌شود؟</li>
</ul>
<p><code dir="ltr">proposed_strategy</code> — فعلاً Stateها را local/provisional نگه دار. وقتی pattern دکمه/لینک/کارت ثابت شد، Focus و State token بساز.</p>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="2" class="disclosure-title" id="lesson-16-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span>
</summary>
<section aria-labelledby="lesson-16-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content">
<p>در درس بعد طبق ترتیب واقعی جزوه ادامه می‌دهیم. تا اینجا عناصر تعاملی TUYA باید State Contract اولیه، Focus قابل مشاهده و Keyboard test پایه داشته باشند؛ اما Interaction پیچیده هنوز وارد نشده است.</p>
<hr/>
</section>
</details>

<details class="lesson-disclosure">
<summary class="lesson-disclosure-summary">
<span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 16</span>
</summary>
<form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-16-completion">
<fieldset>
<legend>ثبت پایان درس 16</legend>
<label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-16-complete" name="lesson-16-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label>
</fieldset>
</form>
</details>

</article>
