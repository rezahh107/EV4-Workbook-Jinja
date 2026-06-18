<article class="lesson card-surface" data-lesson="15" id="lesson-15"><h2 class="lesson-title former-h1">درس 15 — RTL، Start و End</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-15-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-15-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> جهت نوشتار و مفهوم Start/End را در Layout بفهمی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> تمام جزئیات Unicode Bidirectional Algorithm را.</p><p><strong>در پایان باید بتوانی:</strong> Layout را بدون وابستگی بی‌دلیل به Left/Right برای فارسی و انگلیسی آماده کنی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-15-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-15-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🟡 متوسط</td></tr><tr><th scope="row">نوع فعالیت</th><td>🧠 مفهومی + 🛠 اجرایی + RTL</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۲۰–۲۵ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۲۵–۳۵ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۱۵–۲۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> جهت منطقی را روی دو زبان بررسی می‌کنی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-15-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-15-lesson-understand-4">A. بفهم</h2><h3>مسئله</h3><p>طرح در انگلیسی درست است، اما در فارسی فاصله، Icon یا Alignment وارونه می‌شود.</p><h3>مدل ذهنی</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای RTL و Logical Properties">
<h4>راهنمای مبتدی برای RTL و Logical Properties</h4>
<p>RTL فقط راست‌چین‌کردن متن نیست؛ یعنی جهت خواندن، فاصله‌ها و شروع/پایان باید با زبان فارسی هماهنگ باشند.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="RTL">
<h4><span class="term-en" dir="ltr">RTL</span> — راست به چپ</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> جهت طبیعی خواندن فارسی و عربی است.</li>
<li><strong>۲. مثال روزمره:</strong> مثل شروع خواندن کتاب فارسی از سمت راست.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> متن‌ها، ناوبری، دکمه‌ها و ترتیب معنایی فارسی.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> dir="rtl" و تنظیمات alignment منطقی.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> فقط text-align:right می‌زنم و فکر می‌کنم RTL کامل شده.</li>
<li><strong>۶. تصمیم درست:</strong> ساختار document باید dir و lang درست داشته باشد.</li>
<li><strong>۷. تمرین کوچک:</strong> یک بخش فارسی را پیدا کن و بگو شروع متن کدام سمت است.</li>
</ol>
</article>
<article class="concept-card" data-concept="Logical Properties">
<h4><span class="term-en" dir="ltr">Logical Properties</span> — شروع/پایان منطقی</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> به‌جای left/right از start/end استفاده می‌کنی تا در RTL و LTR درست بماند.</li>
<li><strong>۲. مثال روزمره:</strong> مثل گفتن «سمت شروع مسیر» به‌جای «سمت چپ».</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Padding و Margin سمت شروع متن فارسی.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> margin-inline-start/end، padding-inline، inset-inline.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> left/right را hard-code می‌کنم و در RTL جابه‌جا می‌شود.</li>
<li><strong>۶. تصمیم درست:</strong> برای فاصله‌های مرتبط با متن از logical استفاده کن.</li>
<li><strong>۷. تمرین کوچک:</strong> یک margin-left را پیدا کن و بپرس آیا باید margin-inline-start باشد؟</li>
</ol>
</article>
<article class="concept-card" data-concept="Inline Direction">
<h4><span class="term-en" dir="ltr">Inline Direction</span> — جهت خط</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> مسیر حرکت متن در یک خط است.</li>
<li><strong>۲. مثال روزمره:</strong> مثل خط نوشتن روی کاغذ فارسی.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> متن فارسی RTL و کد انگلیسی LTR داخل همان درس.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> dir="ltr" برای کد واقعی، dir="rtl" برای توضیح فارسی.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> کد را RTL می‌کنم و خواندن CSS/HTML خراب می‌شود.</li>
<li><strong>۶. تصمیم درست:</strong> کد واقعی LTR بماند؛ توضیح فارسی RTL بماند.</li>
<li><strong>۷. تمرین کوچک:</strong> یک code block را پیدا کن و جهتش را بررسی کن.</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">RTL</dt><dd>جهت راست‌به‌چپ برای فارسی</dd>
<dt dir="ltr">Logical Properties</dt><dd>start/end به‌جای left/right</dd>
<dt dir="ltr">Inline Direction</dt><dd>جهت حرکت متن در یک خط</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">قبل از تنظیم فاصله بپرس: «این فاصله سمت چپ است یا سمت شروع متن؟»</p>
</aside>
</section><section aria-labelledby="section-hidden-221-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-221-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Inline Start / End</dt><dd>ابتدا و انتهای خط</dd><dt>Block Start / End</dt><dd>ابتدا و انتهای جریان بلوکی</dd></dl></section><p>Start و End با Direction تغییر می‌کنند؛ Left و Right فیزیکی‌اند.</p><h3>مثال</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text" dir="ltr">LTR: Start = left
RTL: Start = right
</code></pre><p>برای Spacing و Position مرتبط با جریان متن، Logical Direction معمولاً مقاوم‌تر است.</p><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="f092b4b627ba3b4d671d0be14b92afee6bc10c9a2db982e6c3ca813079bc5a3c" id="lesson-15-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق RTL و Logical Properties؛ Start و End به‌جای حدس راست و چپ</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="15" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-15-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-15-section-01">مسئله‌ای که RTL حل می‌کند</h3><p>در یک صفحهٔ فارسی، جهت نوشتن از راست به چپ است. اما Layout فقط متن نیست. فاصله، Icon، Border، Position و ترتیب بصری نیز باید با جهت سند سازگار باشند.</p><p>اگر طراحی را فقط با <code class="inline-code" dir="ltr">left</code> و <code class="inline-code" dir="ltr">right</code> بسازی، ممکن است:</p><ul>
<li>نسخهٔ انگلیسی برعکس شود؛</li>
<li>Icon سمت نادرست بماند؛</li>
<li>Marginها در RTL و LTR نیازمند دو CSS جدا شوند؛</li>
<li>Component قابل استفاده مجدد نباشد.</li>
</ul><hr/></section><section aria-labelledby="concept-v31-15-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-15-section-02">تشبیه به دنیای واقعی: درِ ورودی و خروجی</h3><p>فرض کن یک سالن دو در دارد، اما به‌جای اینکه بگویی «در سمت راست»، می‌گویی:</p><ul>
<li>درِ شروع مسیر</li>
<li>درِ پایان مسیر</li>
</ul><p>در سالن فارسی، شروع از راست است. در سالن انگلیسی، شروع از چپ.</p><p>Logical Propertyها نیز به‌جای مختصات فیزیکی، نقش جهت را بیان می‌کنند.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">LTR: inline-start = left
RTL: inline-start = right
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-15-section-03" class="concept-reference-part"><h3 id="concept-v31-15-section-03">محور Inline و Block</h3><p>در نوشتار معمول افقی:</p><ul>
<li>Inline Axis مسیر حرکت متن است.</li>
<li>Block Axis مسیر روی‌هم‌قرارگرفتن سطرها و پاراگراف‌هاست.</li>
</ul><p>برای فارسی:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Inline: از راست به چپ
Block: از بالا به پایین
</code></pre></figure><p>Logical Propertyها با این دو محور کار می‌کنند.</p><hr/></section><section aria-labelledby="concept-v31-15-section-04" class="concept-reference-part"><h3 id="concept-v31-15-section-04">تبدیل‌های مهم</h3><div aria-label="جدول آموزشی مرجع مفهومی" class="table-scroll concept-table-scroll" role="region" tabindex="0"><table class="data-table educational-table concept-reference-table"><caption>جدول آموزشی مرجع مفهومی</caption>
<thead>
<tr>
<th>Physical Property</th>
<th>Logical Property</th>
<th>معنی</th>
</tr>
</thead>
<tbody>
<tr>
<td><code class="inline-code" dir="ltr">margin-left/right</code></td>
<td><code class="inline-code" dir="ltr">margin-inline-start/end</code></td>
<td>فاصله در آغاز/پایان مسیر متن</td>
</tr>
<tr>
<td><code class="inline-code" dir="ltr">padding-left/right</code></td>
<td><code class="inline-code" dir="ltr">padding-inline-start/end</code></td>
<td>فضای داخلی آغاز/پایان</td>
</tr>
<tr>
<td><code class="inline-code" dir="ltr">top/bottom</code></td>
<td><code class="inline-code" dir="ltr">inset-block-start/end</code></td>
<td>جای‌گذاری در محور Block</td>
</tr>
<tr>
<td><code class="inline-code" dir="ltr">left/right</code></td>
<td><code class="inline-code" dir="ltr">inset-inline-start/end</code></td>
<td>جای‌گذاری در محور Inline</td>
</tr>
<tr>
<td><code class="inline-code" dir="ltr">width</code></td>
<td><code class="inline-code" dir="ltr">inline-size</code></td>
<td>اندازه در مسیر Inline</td>
</tr>
<tr>
<td><code class="inline-code" dir="ltr">height</code></td>
<td><code class="inline-code" dir="ltr">block-size</code></td>
<td>اندازه در مسیر Block</td>
</tr>
<tr>
<td><code class="inline-code" dir="ltr">border-left/right</code></td>
<td><code class="inline-code" dir="ltr">border-inline-start/end</code></td>
<td>Border منطقی</td>
</tr>
</tbody>
</table></div><p>این جایگزینی همیشه اجباری نیست؛ گاهی واقعاً «سمت فیزیکی چپ صفحه» منظور است. اما برای Componentهای جهت‌پذیر، Logical Property معمولاً بیان بهتری است.</p><hr/></section><section aria-labelledby="concept-v31-15-section-05" class="concept-reference-part concept-reference-definition"><h3 id="concept-v31-15-section-05"><code class="inline-code" dir="ltr">direction</code> چیست و چه چیزی نیست؟</h3><p><code class="inline-code" dir="ltr">direction: rtl</code> جهت پایهٔ متن و بعضی رفتارهای Inline را تعیین می‌کند. اما نباید از آن برای برعکس‌کردن تصادفی Layout استفاده کنی.</p><p>برای Flexbox:</p><ul>
<li><code class="inline-code" dir="ltr">direction</code> سند روی Start/End اثر دارد.</li>
<li><code class="inline-code" dir="ltr">flex-direction</code> محور و ترتیب Flex را تعیین می‌کند.</li>
</ul><p>این دو را با هم قاطی نکن.</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">Document direction = زبان و جریان نوشتن
Flex direction = جهت چیدمان Itemها در Container
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-15-section-06" class="concept-reference-part"><h3 id="concept-v31-15-section-06">محتوای دوطرفه یا Bidi</h3><p>در متن فارسی ممکن است این موارد کنار هم باشند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">نسخه 4.1.3
CSS: flex: 1 1 0
example.com/path
شماره 0912...
</code></pre></figure><p>الگوریتم Bidi مرورگر تلاش می‌کند ترتیب نمایش را درست کند، اما عبارت‌های Inline با جهت متفاوت گاهی نیاز به Isolation دارند.</p><p>برای متن Dynamic ناشناخته، <code class="inline-code" dir="ltr">dir="auto"</code> یا Elementهایی مانند <code class="inline-code" dir="ltr">bdi</code> می‌توانند کمک کنند. هدف این است که جهت یک عبارت خارجی، ترتیب جملهٔ اطراف را خراب نکند.</p><hr/></section><section aria-labelledby="concept-v31-15-section-07" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-15-section-07">در Elementor V4</h3><p>برای طراحی فارسی:</p><ol>
<li>زبان و <code class="inline-code" dir="ltr">dir</code> سند را درست تنظیم کن.</li>
<li>Alignment را با نقش محتوا انتخاب کن، نه فقط با عادت «همه‌چیز راست».</li>
<li>Utility Classهای فاصله را Logical بساز.</li>
<li>Badgeهای Absolute را با <code class="inline-code" dir="ltr">inset-inline-start/end</code> قرار بده.</li>
<li>Icon و متن Button را در RTL و LTR آزمایش کن.</li>
<li>Dynamic Tagهای عددی، URL و عنوان‌های ترکیبی را بررسی کن.</li>
</ol><p>مثال Utility:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-css inline-code" dir="ltr">.u-space-after {
  margin-inline-end: 1rem;
}
</code></pre></figure><p>همین Class در RTL و LTR معنای «بعد از عنصر» را حفظ می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-15-section-08" class="concept-reference-part"><h3 id="concept-v31-15-section-08">Flexbox و Start/End</h3><p>در <code class="inline-code" dir="ltr">row</code>، Main Start به Direction نوشتار وابسته است. در صفحهٔ RTL، Row از سمت راست آغاز می‌شود. اما <code class="inline-code" dir="ltr">row-reverse</code> ترتیب Main Axis را دوباره برعکس می‌کند.</p><p>به‌جای حفظ‌کردن چهار حالت، محور را روی کاغذ بکش:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">RTL + row:          ← مسیر دیداری از start راست به end چپ
RTL + row-reverse:  → برعکس همان محور
</code></pre></figure><p>ترتیب DOM و ترتیب دیداری را نیز جدا بررسی کن؛ Reverse کردن Layout نباید معنای محتوا یا ترتیب Focus را خراب کند.</p><hr/></section><section aria-labelledby="concept-v31-15-section-09" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-15-section-09">اشتباهات رایج</h3><ul>
<li><code class="inline-code" dir="ltr">text-align: right</code> به‌عنوان راه‌حل تمام RTL</li>
<li>استفاده از Margin Left/Right برای Component قابل ترجمه</li>
<li>تغییر <code class="inline-code" dir="ltr">direction</code> برای جابه‌جایی یک Icon</li>
<li>استفاده افراطی از <code class="inline-code" dir="ltr">row-reverse</code></li>
<li>ندیدن ترتیب Focus و Screen Reader</li>
<li>ترکیب عدد، URL و فارسی بدون تست Bidi</li>
<li>ترجمهٔ UI بدون تغییر <code class="inline-code" dir="ltr">lang</code> و <code class="inline-code" dir="ltr">dir</code></li>
</ul><hr/></section><section aria-labelledby="concept-v31-15-section-10" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-15-section-10">پل به DevTools</h3><p>در Elements Panel مقدارهای <code class="inline-code" dir="ltr">dir</code> و <code class="inline-code" dir="ltr">lang</code> را روی Ancestorها ببین. سپس در Computed Style این موارد را بررسی کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">direction
writing-mode
margin-inline-*
padding-inline-*
inset-inline-*
text-align
flex-direction
</code></pre></figure><p>اگر یک Property منطقی به مقدار فیزیکی تبدیل شده، Computed Style جهت نهایی را نشان می‌دهد.</p><hr/></section><section aria-labelledby="concept-v31-15-section-11" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-15-section-11">تصویر ذهنی نهایی</h3><p>به‌جای گفتن «سمت راست سالن»، بگو «ابتدای مسیر». راست و چپ با زبان عوض می‌شوند؛ Start و End نقش خود را حفظ می‌کنند.</p><hr/></section><section aria-labelledby="concept-v31-15-section-12" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-15-section-12">قوانین طلایی</h3><ul>
<li><strong>«RTL فقط راست‌چین‌کردن متن نیست؛ جهت یک قرارداد سراسری است.»</strong></li>
<li><strong>«برای Component قابل‌حمل، Start و End از Left و Right معنایی‌ترند.»</strong></li>
<li><strong>«<code class="inline-code" dir="ltr">direction</code> سند و <code class="inline-code" dir="ltr">flex-direction</code> دو مسئولیت متفاوت دارند.»</strong></li>
<li><strong>«Reverse دیداری را با ترتیب معنایی DOM اشتباه نگیر.»</strong></li>
<li><strong>«فارسی، عدد، URL و کد را کنار هم آزمایش کن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>CSS Logical Properties and Values</li>
<li>W3C Internationalization guidance for inline bidi markup</li>
<li>CSS Flexible Box Layout specification</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-15-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-15-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — RTL؛ واحد همان است، جهت مرجع تغییر می‌کند</span></summary>
<section aria-labelledby="lesson-15-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">`1rem` در RTL کوچک یا بزرگ نمی‌شود. آنچه تغییر می‌کند نگاشت Start/End به ضلع فیزیکی و جهت محور inline است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> متر همان متر است؛ فقط نقطهٔ شروع مسیر از سمت دیگر خوانده می‌شود.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">Direction</th><td><code dir="ltr">direction</code></td><td>rtl / ltr</td><td>keyword</td><td>جهت inline و متن.</td><td>Direction Flex و direction متن را یکی ندان.</td><td><code dir="ltr">CSS_LOGICAL</code></td></tr><tr><th scope="row">Logical spacing</th><td><code dir="ltr">margin/padding-inline-*</code></td><td>همان واحدهای Spacing</td><td>inline start/end</td><td>برای layout دوطرفه.</td><td>ترکیب physical و logical می‌تواند cascade مبهم بسازد.</td><td><code dir="ltr">E_SPACING</code></td></tr><tr><th scope="row">Logical inset</th><td><code dir="ltr">inset-inline-*</code></td><td>length / percentage / auto در CSS</td><td>containing block و direction</td><td>برای Position سازگار با جهت.</td><td>Start همیشه Right نیست؛ writing-mode مؤثر است.</td><td><code dir="ltr">CSS_LOGICAL</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>padding-inline:1rem با root=16px در هر دو جهت 16px است؛ فقط start/end به ضلع فیزیکی متفاوت نگاشت می‌شود.</p></section>
<section><h3>📱 در Responsive</h3><p>RTL را در همهٔ breakpointها تست کن؛ wrapping و order ممکن است خطا را فقط در Mobile نشان دهد.</p></section>
<section><h3>🔬 در DevTools</h3><p>direction، writing-mode، logical property و مقدار physical computed را کنار هم ببین.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://www.w3.org/TR/css-logical-1/" rel="noopener noreferrer" target="_blank">W3C — CSS Logical Properties</a>، <a href="https://elementor.com/help/style-tab-spacing/" rel="noopener noreferrer" target="_blank">Elementor V4 — Style tab: Spacing</a>، <a href="https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/" rel="noopener noreferrer" target="_blank">Elementor — Units of measurement</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-15-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-15-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — RTL Audit</h3><p>Direction صفحه را RTL کن و موارد زیر را بررسی کن:</p><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="ltr">Platform Main
Feature Item
Logo Strip
Paragraph alignment
Node positions</pre></figure></details><p>نکته: Nodeهای شعاعی Decoration هستند و مختصاتشان ممکن است نیاز به تصمیم طراحی جدا داشته باشد. آن‌ها را کورکورانه Mirror نکن.</p><h3>❓ سؤال توقف</h3><p><code class="inline-code" dir="ltr">margin-inline-start</code> در RTL به کدام سمت فیزیکی اشاره می‌کند؟</p><details class="disclosure-card"><summary>پاسخ</summary>معمولاً سمت راست.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> تمام Offsetها را با Left/Right ثابت بسازی.</p><p><strong>نشانه:</strong> نسخهٔ فارسی به Overrideهای متعدد نیاز دارد.</p><h3>🧪 عمداً خرابش کن</h3><p>Feature Dot را با Margin Left ثابت فاصله بده و Direction را RTL کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>فاصله در سمت نادرست قرار می‌گیرد؛</li>
<li>Icon و Text ممکن است به هم بچسبند؛</li>
<li>نیاز به Override جدا ایجاد می‌شود.</li>
</ul><p>از Gap یا Logical Spacing استفاده کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-223-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-223-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-84"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-84-1" name="chk-84-1" type="checkbox"/><span>متن فارسی Alignment منطقی دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-84-2" name="chk-84-2" type="checkbox"/><span>Feature Item در RTL سالم است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-84-3" name="chk-84-3" type="checkbox"/><span>Logo Strip به Direction وابستگی شکننده ندارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-84-4" name="chk-84-4" type="checkbox"/><span>Nodeها با تصمیم طراحی بررسی شده‌اند</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> Start و End چه مزیتی نسبت به Left و Right دارند؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> دکمه‌ای در RTL درست و در LTR اشتباه است. دنبال چه نوع تنظیمی می‌گردی؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-85"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-85-1" name="chk-85-1" type="checkbox"/><span>Start/End را از Left/Right جدا کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-85-2" name="chk-85-2" type="checkbox"/><span>Writing Direction و Logical Property مرتبط را مشخص کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-85-3" name="chk-85-3" type="checkbox"/><span>پاسخ در RTL و LTR آزمایش‌پذیر است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-15-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-15-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 Case Study — Hard-coded physical offsets</h3><p><strong>هدف:</strong> 🔍 عیب‌یابی کن</p><p>هرجا Offset یا Margin فیزیکی ذخیره شده، سؤال کن آیا آن مقدار باید با زبان تغییر کند یا نه. همهٔ Left/Rightها اشتباه نیستند؛ بعضی Decorationها فیزیکی‌اند.</p><h3>🔬 پشت صحنه</h3><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text language-css" dir="ltr">margin-inline-start: ...;
inset-inline-end: ...;
</code></pre><p>کد را حفظ نکن؛ مفهوم Start/End را در پنل و طراحی دنبال کن.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="reza-tuya-margin-heading" role="heading">🧪 آزمایش واقعی رضا — مشکل margin-inline-start/end در TUYA</span></summary><section aria-labelledby="reza-tuya-margin-heading" class="real-reza-experiment disclosure-content lesson-section">
<ol class="case-steps">
<li><strong>چیزی که رضا دید:</strong> برای سکشن TUYA کد زیر را گذاشت، اما سمت راست از لبه فاصلهٔ واضح نگرفت.</li>
<li><strong>حدس اشتباه مبتدی:</strong> «در RTL، margin-inline-start کار نمی‌کند.»</li>
<li><strong>قانون CSS / Elementor V4:</strong> در RTL معمولاً <code dir="ltr">margin-inline-start</code> به سمت راست و <code dir="ltr">margin-inline-end</code> به سمت چپ نگاشت می‌شود؛ اما این نگاشت به <code dir="ltr">direction</code> و <code dir="ltr">writing-mode</code> وابسته است. اگر خود عنصر <code dir="ltr">width: 100%</code> یا stretch باشد، <code dir="ltr">100% + 80px + 80px</code> می‌تواند overflow بسازد و یک سمت چسبیده به نظر برسد.</li>
<li><strong>در پنل Elementor کجا چک کنم؟</strong> Advanced / Spacing برای Margin و Padding، Layout برای Width/Full Width، و Direction والد/صفحه را بررسی کن.</li>
<li><strong>در DevTools / Computed Style کجا چک کنم؟</strong> Box Model، Computed <code dir="ltr">direction</code>، <code dir="ltr">writing-mode</code>، <code dir="ltr">width</code>، <code dir="ltr">margin-inline-start</code> و <code dir="ltr">margin-inline-end</code> را ببین.</li>
<li><strong>راه‌حل درست:</strong> اگر هدف فاصلهٔ داخلی است، <code dir="ltr">padding-inline</code> بده. اگر هدف آوردن کل جعبه به داخل صفحه است، padding را روی parent/shell بده یا برای خود Main از عرض محاسبه‌شده/Max Width همراه با <code dir="ltr">margin-inline: auto</code> استفاده کن.</li>
<li><strong>قانون طلایی:</strong> Margin جعبه را از بیرون دور می‌کند؛ Padding محتوای داخل جعبه را دور می‌کند. اگر جعبه خودش 100٪ عرض دارد، margin دوطرفه ممکن است overflow بسازد.</li>
</ol>
<pre class="code-block" dir="ltr"><code>.elementor .e-e3036d8 {
  height: 40vh;
  margin-inline-start: 80px;
  margin-inline-end: 80px;
  background-color: var(--solidf1);
  flex-direction: row;
  row-gap: 16px;
  border-radius: var(--border_radios);
}</code></pre>
<div class="code-pair-grid">
<section aria-labelledby="tuya-fix-padding-heading" class="code-fix-card"><h3 id="tuya-fix-padding-heading">وقتی هدف فاصلهٔ صفحه است</h3><pre class="code-block" dir="ltr"><code>.platform-section {
  padding-inline: 80px;
}

.platform-main {
  width: 100%;
}</code></pre></section>
<section aria-labelledby="tuya-fix-width-heading" class="code-fix-card"><h3 id="tuya-fix-width-heading">وقتی هدف جعبهٔ محدود و وسط‌چین است</h3><pre class="code-block" dir="ltr"><code>.platform-main {
  width: min(100% - 160px, 1200px);
  margin-inline: auto;
}</code></pre></section>
</div>
<p><strong>برای TUYA:</strong> معمولاً Section/Shell بیرونی padding صفحه را کنترل می‌کند؛ Platform Main داخل آن می‌نشیند؛ Copy و Visual فرزندان Main هستند.</p>
<p><strong>برای قطعیت، Computed Style و Box Model را بررسی کن.</strong></p>
<details class="more-know">
<summary>بیشتر بدانید</summary>
<p>Logical properties برای RTL مهم‌اند چون به جای چپ/راست فیزیکی، از start/end منطقی استفاده می‌کنند. با این حال، اگر width، overflow یا parent اشتباه باشد، logical margin هم خروجی درست نمی‌سازد.</p>
</details>
</section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="memory-rtl-heading" role="heading">🧠 لایهٔ حافظه — RTL logical properties</span></summary><section aria-labelledby="memory-rtl-heading" class="memory-layer disclosure-content lesson-section"><p><strong>🧠 استعارهٔ ماندگار:</strong> Start و End مثل ابتدا و انتهای مسیر خواندن‌اند؛ Left و Right مثل دیوارهای ثابت اتاق‌اند.</p><p><strong>🧩 در Elementor V4 یعنی چه؟</strong> برای صفحهٔ فارسی، spacing و inset را تا حد امکان با inline-start/end و padding-inline/margin-inline فکر کن.</p><p><strong>⚠️ تله رایج:</strong> Start همیشه «چپ» نیست؛ در RTL معمولاً سمت راست است.</p><p class="golden-rule"><strong>📜 قانون طلایی:</strong> برای زبان، logical فکر کن؛ برای تصویر تزئینی، آگاهانه تصمیم بگیر آینه شود یا نشود.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-15-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-15-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-87"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-87-1" name="chk-87-1" type="checkbox"/><span>می‌توانی Start/End را از Left/Right جدا کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-87-2" name="chk-87-2" type="checkbox"/><span>می‌توانی توضیح بدهی چرا Logical Properties برای سایت دو‌زبانه مقاوم‌ترند.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-88"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-88-1" name="chk-88-1" type="checkbox"/><span>پروژهٔ TUYA را در RTL و LTR بدون جابه‌جایی دستی Left/Right بررسی می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-88-2" name="chk-88-2" type="checkbox"/><span>یک Property فیزیکی پرریسک را پیدا و با مفهوم منطقی جایگزین می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-89"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-89-1" name="chk-89-1" type="checkbox"/><span>در سناریوی «Button در فارسی درست و در انگلیسی سمت اشتباه است» می‌توانی محل بررسی را مشخص کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-15-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-15-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>ایستگاه D کامل شد. قبل از ادامه، Desktop، Mobile و RTL را یک‌بار بدون یادداشت بررسی کن.</p><hr/><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 15</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-15-completion"><fieldset><legend>ثبت پایان درس 15</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-15-complete" name="lesson-15-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-15-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: RTL، Alignment و Logical Sides</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>RTL Direction در برابر Text Alignment</h3><p>Direction مسیر معنایی نوشتار است؛ Text Align محل ایستادن متن داخل جعبه. فارسی فقط <code dir="ltr">text-align:right</code> نیست.</p></section>
<section class="inline-compare-card"><h3>Start/End در برابر Left/Right</h3><p>Start/End سمت شروع و پایان زبان است؛ Left/Right مختصات فیزیکی صفحه است. برای سایت دو‌زبانه و RTL، Start/End ذهن تو را از چپ/راست خام نجات می‌دهد.</p></section>
</div>
</section></details>
<details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="rtl-flex-direction-title" role="heading">تکمیل نسخه 22 — RTL فقط متن نیست؛ محور Flex هم اثر می‌گیرد</span></summary><section aria-labelledby="rtl-flex-direction-title" class="smart-note-card disclosure-content">
<p>در CSS، <code class="inline-code" dir="ltr">flex-direction: row</code> در امتداد inline direction حرکت می‌کند. در صفحهٔ RTL، main-start معمولاً سمت راست است. پس اگر سه آیتم را در Row می‌بینی، ترتیب بصری می‌تواند با ذهن LTR فرق کند.</p>
<p><code class="inline-code" dir="ltr">margin-inline-start/end</code> هم فقط به راست/چپ ساده خلاصه نمی‌شود؛ نگاشت آن به <code class="inline-code" dir="ltr">direction</code>، <code class="inline-code" dir="ltr">writing-mode</code> و <code class="inline-code" dir="ltr">text-orientation</code> وابسته است.</p>
<div class="visual-card-grid two"><div class="visual-card"><strong>LTR row</strong><div class="mini-flow ltr"><span>1</span><span>2</span><span>3</span></div><p>main-start از چپ شروع می‌شود.</p></div><div class="visual-card"><strong>RTL row</strong><div class="mini-flow rtl"><span>1</span><span>2</span><span>3</span></div><p>main-start از راست شروع می‌شود.</p></div></div>
<p class="golden-rule"><strong>قانون طلایی:</strong> در RTL، اول direction و writing-mode را در Computed Style ببین؛ بعد دربارهٔ start/end قضاوت کن.</p>
</section></details><details class="lesson-disclosure" id="lesson-15-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Responsive و RTL را جداگانه تست کن</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>Row/Column، Start/End و ترتیب بصری در RTL به context جهت وابسته‌اند. در Mobile TUYA محتوای انگلیسی و لوگوهای لاتین باید LTR بمانند، اما Shell صفحه می‌تواند RTL باشد.</p>
<p>پس از هر تغییر breakpoint، <code>direction</code>، logical margins/padding و ترتیب واقعی را در Computed Style بررسی کن.</p>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-15-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: RTL، Logical Sides و Responsive</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> جهت متن، جهت Flex و logical spacing را جداگانه آزمایش کن.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>یک Container RTL با متن فارسی و یک Logo Strip/label انگلیسی LTR بساز.</li><li>margin-inline-start/end و padding-inline را در Desktop و Mobile مقایسه کن.</li><li>Direction فلکس را جدا از direction متن تغییر بده و نتیجه را ثبت کن.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>پیش‌بینی کن inline-start در context فعلی به کدام سمت فیزیکی نگاشت می‌شود.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>برای یک فاصله از margin-left/right فیزیکی استفاده کن و direction را عوض کن.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>direction، writing-mode، margin-inline-start/end و computed physical margins.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> فاصله‌ها با تغییر جهت معنای درست دارند و متن انگلیسی/لوگوها بی‌دلیل RTL نشده‌اند.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-15-responsive-build-test-done-build"><input data-persist="" id="lesson-15-responsive-build-test-done-build" name="lesson-15-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-15-responsive-build-test-done-test"><input data-persist="" id="lesson-15-responsive-build-test-done-test" name="lesson-15-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-15-responsive-build-test-done-debug"><input data-persist="" id="lesson-15-responsive-build-test-done-debug" name="lesson-15-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-15-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-15-responsive-build-test-note" name="lesson-15-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/responsive-editing/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-15-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — logical properties</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
