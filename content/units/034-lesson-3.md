<article class="lesson card-surface" data-lesson="3" id="lesson-3"><h2 class="lesson-title former-h1">درس 3 — Local Class، Global Class و کلاس هدف ویرایش</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-3-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-3-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> تفاوت Local Class و Global Class و اهمیت کلاس هدف ویرایش را.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام جزئیات CSS Specificity را.</p><p><strong>در پایان باید بتوانی:</strong> Style مشترک را از تفاوت منحصربه‌فرد جدا کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-3-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-3-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + 🔍 عیب‌یابی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۰–۳۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۴۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۵ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> Class System یکی از مفاهیم مرکزی V4 است.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-3-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-3-lesson-understand-4">A. بفهم</h2><h3>مدل ذهنی</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای Local Class، Global Class و کلاس هدف ویرایش">
<h4>راهنمای مبتدی برای Local Class، Global Class و کلاس هدف ویرایش</h4>
<p>Classها فقط اسم نیستند؛ تصمیمی هستند دربارهٔ اینکه Style یک‌بار مصرف است یا باید دوباره استفاده شود.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="Local Class">
<h4><span class="term-en" dir="ltr">Local Class</span> — کلاس محلی</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> Style مخصوص همین عنصر یا همین موقعیت.</li>
<li><strong>۲. مثال روزمره:</strong> مثل یادداشت چسبان روی همین یک کارت.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> یک تفاوت کوچک فقط روی همان عنصر.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Class یا Style محلی روی همان Element.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> برای هر تغییر کوچک یک Global Class بزرگ می‌سازم.</li>
<li><strong>۶. تصمیم درست:</strong> اگر فقط همین یک عنصر فرق دارد، Local نگه دار.</li>
<li><strong>۷. تمرین کوچک:</strong> یک دکمه را پیدا کن که فقط همان‌جا کمی فرق دارد.</li>
</ol>
</article>
<article class="concept-card" data-concept="Global Class">
<h4><span class="term-en" dir="ltr">Global Class</span> — کلاس قابل استفادهٔ مجدد</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> یک بستهٔ Style که چند عنصر واقعاً مشترک دارند.</li>
<li><strong>۲. مثال روزمره:</strong> مثل یونیفرم تیم؛ روی چند نفر تکرار می‌شود.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> کارت‌ها، دکمه‌ها یا Badgeهای تکراری.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Global/Global Class در Elementor V4.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> چیزی را Global Class می‌کنم فقط چون اسمش قشنگ است، نه چون تکرار دارد.</li>
<li><strong>۶. تصمیم درست:</strong> وقتی حداقل چند استفادهٔ واقعی دارد Global Class کن.</li>
<li><strong>۷. تمرین کوچک:</strong> دو عنصر با ظاهر یکسان پیدا کن و بگو Class مشترکشان چیست.</li>
</ol>
</article>
<article class="concept-card" data-concept="کلاس هدف ویرایش">
<h4><span class="term-en" dir="ltr">کلاس هدف ویرایش</span> — کلاس فعال</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> کلاسی که الان روی عنصر انتخاب‌شده اثر می‌گذارد.</li>
<li><strong>۲. مثال روزمره:</strong> مثل لباسی که الان پوشیده‌ای، نه لباس داخل کمد.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> در پنل Elementor روی Element انتخاب‌شده دیده می‌شود.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> کلاس متصل یا انتخاب‌شده در پنل Style/Class.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> فکر می‌کنم هر Class موجود در سیستم روی این عنصر فعال است.</li>
<li><strong>۶. تصمیم درست:</strong> فقط کلاس‌های وصل‌شده به همین Element را بررسی کن.</li>
<li><strong>۷. تمرین کوچک:</strong> یک Element را انتخاب کن و نام Classهای واقعاً فعالش را بنویس.</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">Local Class</dt><dd>تغییر مخصوص همین عنصر</dd>
<dt dir="ltr">Global Class</dt><dd>بستهٔ Style مشترک برای چند عنصر</dd>
<dt dir="ltr">کلاس هدف ویرایش</dt><dd>کلاسی که اکنون روی عنصر اثر دارد</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">قبل از ساخت Class بپرس: «این Style چند بار واقعاً تکرار می‌شود؟»</p>
</aside>
</section><section aria-labelledby="section-hidden-58-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-58-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Global Class</dt><dd>لباس مشترک چند Element</dd><dt>Local Class</dt><dd>اصلاح مخصوص همین Element</dd><dt>کلاس هدف ویرایش</dt><dd>لباسی که همین لحظه ویرایش می‌کنی</dd></dl></section><p>هر Element حداقل یک Local Class دارد. Class مشترک را وقتی می‌سازیم که رفتار واقعاً تکرار می‌شود.</p><h3>مثال ساده</h3><p>سه Button:</p><figure class="visual-figure visual-term-map class-map"><figcaption>نگاشت نقش کلاس‌ها در Button</figcaption><dl class="term-grid"><dt>button-base</dt><dd>ظاهر مشترک</dd><dt>button-primary</dt><dd>نوع اصلی</dd><dt>Local Class</dt><dd>تفاوت فقط همین Button</dd></dl></figure><h3>اولین بررسی هنگام Conflict</h3><section aria-labelledby="section-hidden-59-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-59-heading">بخش آموزشی</h2><ul><li>Element درست؟</li>
<li>کلاس هدف ویرایش درست؟</li>
<li>Local override وجود دارد؟</li>
<li>State و Device درست؟</li></ul></section><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="4d948ce22247be35bf7e1bbe841cdc138c94edd7e7ff46e7694ee81f0b99789e" id="lesson-3-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Local Class، Global Class و هدف واقعی ویرایش</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="3" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-03-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-03-section-01">مسئله‌ای که این مفهوم حل می‌کند</h3><p>در V4 ممکن است رنگ یک Heading را تغییر دهی و ناگهان چند Heading دیگر نیز تغییر کنند. یا یک Global Class را ویرایش کنی اما روی Element موردنظر هیچ تغییری نبینی.</p><p>علت معمول این است که نمی‌دانی:</p><ul>
<li>الان کدام Class فعال است؛</li>
<li>تغییر تو Local است یا Global؛</li>
<li>کدام Class در تعارض اولویت دارد.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-03-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-03-section-02">تشبیه به دنیای واقعی: لباس شخصی و یونیفرم</h3><ul>
<li><strong>Global Class</strong> مثل یونیفرم شرکت است.</li>
<li><strong>Local Class</strong> مثل تغییر اختصاصی خیاط روی لباس یک کارمند است.</li>
<li><strong>Variable</strong> مثل کد رنگ پارچه است که هم یونیفرم و هم لباس اختصاصی می‌توانند از آن استفاده کنند.</li>
</ul><p>اگر شرکت رنگ یونیفرم را تغییر دهد، همهٔ لباس‌های وابسته تغییر می‌کنند؛ مگر اینکه خیاط روی لباس یک نفر رنگ دیگری دوخته باشد.</p><hr/></section><section aria-labelledby="concept-v31-03-section-03" class="concept-reference-part concept-reference-definition"><h3 id="concept-v31-03-section-03">تعریف دقیق</h3><h4>Local Class</h4><p>هر Element در V4 حداقل یک Local Class دارد. این Class مخصوص همان Element است و طبق مستندات رسمی Elementor بالاترین اولویت را در تعارض‌های Class دارد.</p><h4>Global Class</h4><p>یک بستهٔ Style نام‌دار است که می‌توان آن را روی چند Element اعمال کرد.</p><p>مثلاً:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">.button-base
.button-primary
.button-large
</code></pre></figure><p>هر Class یک مسئولیت روشن دارد.</p><hr/></section><section aria-labelledby="concept-v31-03-section-04" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-03-section-04">چرا Class ساخته شده است؟</h3><p>بدون Class، هر Element نسخهٔ جداگانه‌ای از تنظیمات را حمل می‌کند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Button 1: background #6D5DFB, radius 12, padding 16
Button 2: background #6D5DFB, radius 12, padding 16
Button 3: background #6D5DFB, radius 12, padding 16
</code></pre></figure><p>سه ظاهر شبیه داریم، اما رابطه‌ای میان آن‌ها نیست.</p><p>با Class:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">.button-primary
</code></pre></figure><p>هر سه Button از یک قانون مشترک پیروی می‌کنند.</p><hr/></section><section aria-labelledby="concept-v31-03-section-05" class="concept-reference-part"><h3 id="concept-v31-03-section-05">هدف واقعی ویرایش را قبل از لمس کنترل مشخص کن</h3><p>از خودت بپرس:</p><h4>آیا این تغییر فقط برای همین Element است؟</h4><p>Local Class.</p><h4>آیا این یک الگوی تکرارشونده است؟</h4><p>Global Class.</p><h4>آیا فقط مقدار مشترک است؟</h4><p>Variable.</p><h4>آیا ساختار چندElementی تکرار می‌شود؟</h4><p>Component.</p><hr/></section><section aria-labelledby="concept-v31-03-section-06" class="concept-reference-part"><h3 id="concept-v31-03-section-06">مثال واقعی</h3><p>سه دکمه داری:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">دکمهٔ اصلی: خرید
دکمهٔ اصلی: ثبت‌نام
دکمهٔ ثانویه: اطلاعات بیشتر
</code></pre></figure><p>سیستم مناسب:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">.button-base       ← Typography، Padding، Radius
.button-primary    ← رنگ اصلی
.button-secondary  ← Border و Background ثانویه
</code></pre></figure><p>روی دکمهٔ خرید:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Local Class
+ button-base
+ button-primary
</code></pre></figure><p>اگر فقط دکمهٔ خرید نیاز به عرض کامل در Hero دارد، Width را در Local Class یا یک Utility Class معنادار قرار بده؛ نه اینکه <code class="inline-code" dir="ltr">button-primary</code> را برای همه خراب کنی.</p><hr/></section><section aria-labelledby="concept-v31-03-section-07" class="concept-reference-part"><h3 id="concept-v31-03-section-07">تعارض چگونه رخ می‌دهد؟</h3><p>فرض کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">.text-red   → color: red
.text-green → color: green
</code></pre></figure><p>هر دو روی یک Paragraph هستند.</p><p>Elementor باید تصمیم بگیرد کدام برنده است. ترتیب Global Classها در Class Manager برای این اولویت اهمیت دارد، اما Local Class بالاتر از Global Classها قرار می‌گیرد.</p><p>پس اگر Global Class را عوض کردی و نتیجه دیده نشد، اول Local Class را بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-03-section-08" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-03-section-08">در Elementor V4</h3><p>قبل از هر Style:</p><ol>
<li>Classes Field را ببین.</li>
<li>Class فعال را تشخیص بده.</li>
<li>مطمئن شو State درست را ویرایش می‌کنی.</li>
<li>اگر Global Class است، دامنهٔ مصرف آن را در ذهن داشته باش.</li>
<li>تغییر را روی چند مصرف‌کننده آزمایش کن.</li>
</ol><hr/></section><section aria-labelledby="concept-v31-03-section-09" class="concept-reference-part"><h3 id="concept-v31-03-section-09">Utility Class؛ ابزار کوچک، مسئولیت کوچک</h3><p>گاهی یک رفتار کوچک در ده‌ها نقطه تکرار می‌شود، اما ساخت Component برای آن زیاده‌روی است. اینجا می‌توان از یک Global Class کمکی استفاده کرد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">u-flex-center
u-full-width
u-overflow-hidden
u-space-block-end-lg
</code></pre></figure><p>Utility Class را مثل آچار کوچکی تصور کن که فقط یک کار روشن انجام می‌دهد. اگر یک Class هم‌زمان رنگ، Typography، Layout و Responsive را کنترل کند، دیگر Utility نیست؛ تبدیل به بسته‌ای مبهم شده است.</p><p>برای سایت فارسی، Utilityها را تا جای ممکن با Logical Propertyها طراحی کن. <code class="inline-code" dir="ltr">padding-inline</code> از <code class="inline-code" dir="ltr">padding-left</code> و <code class="inline-code" dir="ltr">padding-right</code> قابل‌حمل‌تر است، چون با RTL و LTR سازگار می‌ماند. Utility Class یک «نوع رسمی جداگانه» در Elementor نیست؛ یک الگوی معماری است که با Global Class پیاده می‌شود.</p></section><section aria-labelledby="concept-v31-03-section-10" class="concept-reference-part"><h3 id="concept-v31-03-section-10">درخت ردیابی منبع Style</h3><p>وقتی یک Style اعمال نمی‌شود، فقط به Specificity فکر نکن. در V4 ابتدا این زنجیره را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Breakpoint فعال
↓
State فعال
↓
Class انتخاب‌شده برای ویرایش
↓
Local Class
↓
Global Classهای رقیب و ترتیب Class Manager
↓
Custom CSS
↓
Cascade واقعی مرورگر و Computed Style
</code></pre></figure><p>Local Class در قرارداد Elementor بالاترین اولویت را دارد. میان Global Classها، کلاسی که در Class Manager اولویت بالاتری دارد برنده می‌شود. سپس Custom CSS، Selector Specificity، Source Order و <code class="inline-code" dir="ltr">!important</code> نیز ممکن است در خروجی واقعی دخالت کنند. بنابراین «اولویت Elementor» و «Specificity CSS» یک چیز نیستند.</p></section><section aria-labelledby="concept-v31-03-section-11" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-03-section-11">تله‌های رایج</h3><ul>
<li>ساخت Global Class برای یک استثنای تک‌مصرف</li>
<li>قرار دادن همهٔ Styleها در Local Class و ازبین‌بردن قابلیت نگهداری</li>
<li>نام‌گذاری بر اساس ظاهر لحظه‌ای، مثل <code class="inline-code" dir="ltr">.blue-text</code>، وقتی نقش واقعی <code class="inline-code" dir="ltr">.text-accent</code> است</li>
<li>ویرایش Global Class بدون بررسی سایت</li>
<li>حل تعارض با افزودن Class جدید به‌جای پاک‌کردن Property متعارض</li>
</ul><hr/></section><section aria-labelledby="concept-v31-03-section-12" class="concept-reference-part"><h3 id="concept-v31-03-section-12">قانون نام‌گذاری</h3><p>نام خوب می‌گوید Class چه <strong>نقشی</strong> دارد:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">خوب: card-title
خوب: button-primary
خوب: stack-sm
ضعیف: text-18-blue
ضعیف: box2-final-new
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-03-section-13" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-03-section-13">تصویر ذهنی نهایی</h3><p>Local Class لباس سفارشی یک نفر است؛ Global Class یونیفرم یک گروه؛ Utility Class ابزار کوچکی مثل کمربند یا کلاه؛ Variable رنگ و اندازه‌ای است که از انبار مرکزی می‌آید. پیش از ویرایش، مشخص کن دستت روی کدام لایه است.</p></section><section aria-labelledby="concept-v31-03-section-14" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-03-section-14">قوانین طلایی</h3><ul>
<li><strong>«Local Class استثنای همان Element است؛ Global Class قرارداد مشترک چند Element.»</strong></li>
<li><strong>«قبل از ویرایش Style، اول Class فعال را بخوان.»</strong></li>
<li><strong>«اگر Global Class دیده نمی‌شود، Local Class را به‌عنوان مظنون اول بررسی کن.»</strong></li>
<li><strong>«Class باید نقش را نام‌گذاری کند، نه تصادف ظاهری امروز را.»</strong></li>
<li><strong>«تکرار اثبات‌شده را Global کن؛ حدس دربارهٔ تکرار آینده را نه.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>Elementor Help: Classes in Elementor</li>
<li>Elementor Help: Prioritize conflicting styles</li>
<li>Elementor Help: The Elementor Editor Class Manager</li>
<li>CSS Cascade specification</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-3-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-3-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Class واحد ندارد؛ Propertyهای داخل Class واحد دارند</span></summary>
<section aria-labelledby="lesson-3-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Local و Global Class ظرف Style هستند. خود Class با px یا rem سنجیده نمی‌شود؛ هر declaration داخل آن نوع مقدار مستقل دارد.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> کلاس مثل یک کیف ابزار است. خود کیف «۲۰ پیکسل» نیست؛ اما داخلش آچار ۱۰ میلی‌متری و متر ۲ متری می‌تواند باشد.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Local / Global Class</th><td><code dir="ltr">class selector</code></td><td>نام و priority</td><td>بدون واحد</td><td>برای scope و reuse.</td><td>نام Class را با مقدار CSS ترکیب نکن.</td><td><code dir="ltr">E_CLASSES</code></td></tr><tr><th scope="row">Size Variable داخل Class</th><td><code dir="ltr">var(...)</code></td><td>Color / Font / Size variable</td><td>نوع Variable</td><td>برای مقدار مشترک و قابل تغییر.</td><td>Variable اشتباه را به Property ناسازگار وصل نکن.</td><td><code dir="ltr">E_VARIABLES</code></td></tr><tr><th scope="row">Priority</th><td><code dir="ltr">cascade order</code></td><td>ترتیب</td><td>عدد نمایشی/بدون واحد</td><td>از Class Manager خوانده شود.</td><td>زمان افزودن Class معیار priority نیست.</td><td><code dir="ltr">E_CLASS_MANAGER</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>اگر Local width برابر 50% و Global width برابر 40rem باشد، برنده با priority/cascade تعیین می‌شود؛ واحد بزرگ‌تر یا کوچک‌تر معیار نیست.</p></section>
<section><h3>📱 در Responsive</h3><p>ممکن است همان Class در breakpointهای مختلف declaration متفاوت داشته باشد؛ scope و source را جدا ثبت کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>Matched Rules نشان می‌دهد declaration برنده از کدام Class آمده و declaration مغلوب چرا خط خورده است.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/classes-in-elementor-2/" rel="noopener noreferrer" target="_blank">Elementor V4 — Classes</a>، <a href="https://elementor.com/help/the-elementor-editor-class-manager/" rel="noopener noreferrer" target="_blank">Elementor V4 — Class Manager</a>، <a href="https://elementor.com/help/variables/" rel="noopener noreferrer" target="_blank">Elementor V4 — Variables</a>، <a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">W3C — CSS Values and Units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-3-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-3-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — Classها Just-in-Time</h3><p>حالا برای چهار Element موجود Class بساز:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Platform Section → c-platform-section
Platform Main    → c-platform-main
Platform Copy    → c-platform-copy
Platform Visual  → c-platform-visual</pre></figure></details><p>فعلاً Class مربوط به Node، Logo یا Feature Item نساز؛ آن Elementها هنوز وجود ندارند.</p><h3>❓ سؤال توقف</h3><p>اگر <code class="inline-code" dir="ltr">c-platform-main</code> روی چند سکشن استفاده شود و فقط یکی Gap متفاوت بخواهد، Gap متفاوت کجا قرار می‌گیرد؟</p><details class="disclosure-card"><summary>پاسخ</summary>
<p>در Local Class همان Element، یا در یک Variant Class معنی‌دار؛ نه با تغییر Class مشترک برای همه.</p>
</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> Global Class کار نمی‌کند، پس فوراً Class جدید بسازی.</p><p><strong>علت محتمل:</strong> Local Class همان Property را Override کرده است.</p><p><strong>اولین بررسی:</strong> کلاس هدف ویرایش و Local Class.</p><h3>🧪 عمداً خرابش کن</h3><p>روی Global Class رنگ متن خاکستری بگذار. سپس روی Local Class همان Element رنگ قرمز بگذار.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>Element قرمز می‌شود؛</li>
<li>تغییر Global Class روی همان Property ظاهراً اثر ندارد؛</li>
<li>سایر Elementهای دارای Global Class همچنان مقدار مشترک را می‌گیرند.</li>
</ul><p>Local override را پاک کن و دوباره نتیجه را ببین.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-61-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-61-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-13"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-13-1" name="chk-13-1" type="checkbox"/><span>فقط چهار Class ساخته شده</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-13-2" name="chk-13-2" type="checkbox"/><span>می‌دانم کدام Class فعال است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-13-3" name="chk-13-3" type="checkbox"/><span>Style مشترک در Global Class است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-13-4" name="chk-13-4" type="checkbox"/><span>تفاوت یکتا در Local Class است</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Local Class و Global Class چه تفاوتی دارند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> سه Card تغییر کرده‌اند ولی چهارمی نه؛ همه یک Global Class دارند. اولین بررسی چیست؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-14"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-14-1" name="chk-14-1" type="checkbox"/><span>Local، Global و کلاس هدف ویرایش را از هم جدا کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-14-2" name="chk-14-2" type="checkbox"/><span>Property مشترک و تفاوت منحصربه‌فرد را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-14-3" name="chk-14-3" type="checkbox"/><span>قبل از ساخت Class جدید، Local Override و Priority را بررسی کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-3-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-3-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-HOME2-REUSE-001</h3><p><strong>هدف:</strong> ⚖️ دو روش را مقایسه کن<br/>
<strong>وضعیت:</strong> <code class="inline-code" dir="ltr">improvement_candidate</code></p><p>Export نشان می‌دهد چندین SVG، Heading و Paragraph امضای Style یکسان دارند. پیشنهاد:</p><section aria-labelledby="section-hidden-64-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-64-heading">بخش آموزشی</h2><ul><li>Local Style تکراری</li>
<li>در برابر</li>
<li>Global Class یا Component</li></ul></section><p>هنوز Runtime و Intent کامل را نداریم؛ پس آن را «خرابی» نمی‌نامیم.</p><h3>🔬 پشت صحنه</h3><p><code class="inline-code" dir="ltr">.class</code> در CSS یعنی Class Selector. لازم نیست کد بنویسی؛ فقط بدان V4 همین مفهوم را از طریق رابط مدیریت می‌کند.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="class-system-v4-update-heading" role="heading">به‌روزرسانی دقیق سیستم Class در Elementor V4</span></summary><section aria-labelledby="class-system-v4-update-heading" class="disclosure-content lesson-section class-system-update">
<div class="definition-card-grid">
<article class="definition-card"><h3>Local Class</h3><p>کلاس محلی / مخصوص همان عنصر است. هر Element حداقل یک Local Class دارد و این کلاس برای همان Element بیشترین اولویت محلی را دارد.</p></article>
<article class="definition-card"><h3>Global Class</h3><p>کلاس سراسری / قابل استفاده مجدد در سیستم طراحی است. وقتی یک ایدهٔ استایلی باید در چند جای سایت تکرار شود، آن را به Global Class تبدیل کن.</p></article>
<article class="definition-card"><h3>States</h3><p>لایهٔ رفتار همان کلاس است: <span dir="ltr">Normal</span>، <span dir="ltr">Hover</span>، <span dir="ltr">Focus</span> و <span dir="ltr">Active</span>.</p></article>
</div>
<section aria-labelledby="class-memory-heading" class="memory-layer">
<h3 id="class-memory-heading">🧠 استعارهٔ ماندگار</h3>
<p><strong>Local Class</strong> = لباس اختصاصی همین عنصر. <strong>Global Class</strong> = یونیفرم قابل استفاده در چند جای سایت. <strong>States</strong> = حالت‌های رفتار همان کلاس.</p>
<p><strong>🧩 در Elementor V4 یعنی چه؟</strong> اگر اول فقط یک دکمه را ساختی، با Local Class شروع می‌کنی. وقتی همان ظاهر باید الگوی سایت شود، از گزینهٔ تبدیل به Global Class استفاده می‌کنی.</p>
<p class="golden-rule"><strong>📜 قانون طلایی:</strong> چیزی را فقط وقتی Global Class کن که معنی طراحی مشترک و تکرارشونده دارد؛ نه فقط چون اسم مشترک قشنگ است.</p>
</section>
<details class="more-know">
<summary>بیشتر بدانید</summary>
<p>در Elementor V4 چیزی که قبلاً ممکن بود به‌صورت ذهنی «قابل استفاده مجدد» صدا بزنیم، در عمل با Global Class توضیح داده می‌شود. این نام را از خود UI و Class Manager دنبال کن تا مفهوم جداگانهٔ ساختگی نسازی.</p>
</details>
</section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-3-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-3-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-16"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-16-1" name="chk-16-1" type="checkbox"/><span>می‌توانی Local Class، Global Class و کلاس هدف ویرایش را از هم جدا کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-16-2" name="chk-16-2" type="checkbox"/><span>می‌توانی توضیح بدهی چرا Style مشترک نباید در چند Local Class تکرار شود.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-17"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-17-1" name="chk-17-1" type="checkbox"/><span>برای اولین Element ساخته‌شده، Global Class را همان لحظه و با نام معنایی ایجاد می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-17-2" name="chk-17-2" type="checkbox"/><span>در یک Conflict واقعی بررسی می‌کنی آیا Local Class همان Property را Override کرده است.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-18"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-18-1" name="chk-18-1" type="checkbox"/><span>برای چهار Card مشابه می‌توانی مشخص کنی کدام Style مشترک، کدام Variant و کدام تنظیم منحصربه‌فرد است.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-3-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-3-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>در درس بعد اولین Class واقعی پروژه، یعنی پوستهٔ خاکستری، Style می‌گیرد.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 3</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-3-completion"><fieldset><legend>ثبت پایان درس 3</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-3-complete" name="lesson-3-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-3-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Local Class، Global Class و تعریف در برابر استفاده</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Local Class در برابر Global Class</h3><p><strong>تصویر ذهنی:</strong> Local Class لباس دوخته‌شده برای یک نفر است؛ Global Class یونیفرم قابل استفاده برای چند نفر.</p><p><strong>تعریف دقیق:</strong> Local Class مخصوص همان Element است. Global Class یک تعریف مشترک Style است که روی چند Element استفاده می‌شود و در Class Manager مدیریت می‌شود.</p><p><strong>دام رایج:</strong> اینکه فکر کنیم چون هر دو روی چند Element «استفاده» می‌شوند، پس از نظر نگهداری یکی هستند. تفاوت اصلی در <strong>Definition</strong> است، نه Usage.</p></section>
<section class="inline-compare-card"><h3>Definition در برابر Usage</h3><p><strong>Definition</strong> یعنی خود قانون Style کجا و چند بار تعریف شده. <strong>Usage</strong> یعنی آن قانون چند بار به Elementها وصل شده است.</p><p>اگر ۲۰ دکمه هرکدام Local Class جدا با استایل مشابه داشته باشند، تعریف‌ها تکرار شده‌اند. اگر یک <code dir="ltr">btn-primary</code> داشته باشی و ۲۰ بار استفاده‌اش کنی، تعریف یکی است و Usage بیست تا.</p><p class="golden-rule">قانون طلایی: ظاهر تکراری را Global کن؛ استثنای واقعی را Local نگه دار.</p></section>
</div>
</section></details>
</article>
