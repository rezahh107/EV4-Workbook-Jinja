<article class="lesson card-surface" data-lesson="20" id="lesson-20"><h2 class="lesson-title former-h1">درس 20 — Performance، DOM و Audit ساختار</h2><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-20-lesson-compass-1" role="heading">🧭 قطب‌نمای درس</span></summary><section aria-labelledby="lesson-20-lesson-compass-1" class="disclosure-content lesson-section lesson-compass"><p><strong>در این درس یاد می‌گیری:</strong> Performance را به‌عنوان نتیجهٔ ساختار، رسانه و تکرار Style بررسی کنی.</p><p><strong>در این درس هنوز یاد نمی‌گیری:</strong> Benchmark تخصصی شبکه و JavaScript را.</p><p><strong>در پایان باید بتوانی:</strong> یک Audit ساده و مستند برای صفحه انجام دهی.</p></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-20-lesson-meta-2" role="heading">زمان، سنگینی و نوع فعالیت</span></summary><section aria-labelledby="lesson-20-lesson-meta-2" class="lesson-meta disclosure-content lesson-section"><div aria-label="جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table"><caption>جدول آموزشی دوره — زمان، سنگینی و نوع فعالیت</caption><thead><tr><th scope="col">مورد</th><th scope="col">پیشنهاد</th></tr></thead><tbody><tr><th scope="row">سنگینی</th><td>🔴 سنگین</td></tr><tr><th scope="row">نوع فعالیت</th><td>🔍 Audit + 🛠 اجرایی + 🧠 تحلیلی</td></tr><tr><th scope="row">هستهٔ فهم</th><td>۳۰–۴۰ دقیقه</td></tr><tr><th scope="row">تثبیت و تمرین</th><td>۴۵–۶۰ دقیقه</td></tr><tr><th scope="row">عمق اختیاری</th><td>۲۰–۳۰ دقیقه</td></tr></tbody></table></div><aside aria-label="راهنمای معلم" class="teacher-note"><p><strong>راهنمای معلم:</strong> علت Runtime را از نشانه جدا می‌کنی.</p></aside><p class="status-line"><code class="inline-code" dir="ltr">status: proposed_until_real_learner_pilot</code></p></section></details><section aria-labelledby="lesson-20-lesson-understand-4" class="lesson-section lesson-understand lesson-core-concept" data-core-concept="true"><h2 id="lesson-20-lesson-understand-4">A. بفهم</h2><h3>چهار محور Audit</h3><section class="beginner-explainer global-visual-scaffold" data-beginner-section="راهنمای مبتدی برای Audit نهایی">
<h4>راهنمای مبتدی برای Audit نهایی</h4>
<p>Audit یعنی نگاه‌کردن منظم؛ به‌جای حس کلی، هر بار یک محور را بررسی می‌کنی.</p>
<div class="concept-card-grid">
<article class="concept-card" data-concept="Structure Audit">
<h4><span class="term-en" dir="ltr">Structure Audit</span> — بررسی اسکلت</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> می‌پرسی Parent و Childها درست هستند یا نه.</li>
<li><strong>۲. مثال روزمره:</strong> مثل بررسی ستون‌های ساختمان.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Navigator و ظرف‌های والد.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Elementor Navigator / Structure panel.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> فقط رنگ و زیبایی را بررسی می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> اول اسکلت، بعد Style.</li>
<li><strong>۷. تمرین کوچک:</strong> یک Parent اشتباه احتمالی پیدا کن.</li>
</ol>
</article>
<article class="concept-card" data-concept="Content Audit">
<h4><span class="term-en" dir="ltr">Content Audit</span> — بررسی محتوا</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> می‌پرسی متن، دکمه و Logo در Flow و قابل خواندن هستند یا نه.</li>
<li><strong>۲. مثال روزمره:</strong> مثل بررسی وسایل اتاق.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Copy Area، Feature list، Button، Logos.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Widgets و ترتیب خواندن.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> محتوا را برای زیبایی قربانی می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> محتوا باید قبل از Decoration سالم باشد.</li>
<li><strong>۷. تمرین کوچک:</strong> متن را طولانی‌تر فرض کن و نتیجه را بگو.</li>
</ol>
</article>
<article class="concept-card" data-concept="Interaction Audit">
<h4><span class="term-en" dir="ltr">Interaction Audit</span> — بررسی تعامل</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> می‌پرسی Hover، Focus، Click و Keyboard سالم هستند یا نه.</li>
<li><strong>۲. مثال روزمره:</strong> مثل تست‌کردن کلیدهای یک دستگاه.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> Buttonها و Linkها.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> State panel و accessibility checks.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> فقط با ماوس تست می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> Keyboard و Focus را هم بررسی کن.</li>
<li><strong>۷. تمرین کوچک:</strong> یک مسیر Tab ذهنی بساز.</li>
</ol>
</article>
<article class="concept-card" data-concept="Responsive Audit">
<h4><span class="term-en" dir="ltr">Responsive Audit</span> — بررسی اندازه‌ها</h4>
<ol class="concept-steps">
<li><strong>۱. ساده‌ترین معنی:</strong> می‌پرسی در دسکتاپ، تبلت و موبایل ساختار هنوز معنی دارد یا نه.</li>
<li><strong>۲. مثال روزمره:</strong> مثل جمع‌کردن میز بزرگ روی میز کوچک.</li>
<li><strong>۳. در Screenshot یعنی کدام بخش؟</strong> دو ستون به یک ستون، Stage کوچک‌تر، فاصله‌ها.</li>
<li><strong>۴. در Elementor یعنی کدام Element / ظرف والد / Setting؟</strong> Responsive preview در Elementor.</li>
<li><strong>۵. اشتباه رایج مبتدی:</strong> برای موبایل فقط Offset اضافه می‌کنم.</li>
<li><strong>۶. تصمیم درست:</strong> ساختار باید سازگار شود، نه وصله‌کاری.</li>
<li><strong>۷. تمرین کوچک:</strong> بگو در موبایل Visual قبل از متن باشد یا بعد از آن؟</li>
</ol>
</article></div>
<dl class="term-translation"><dt dir="ltr">Structure Audit</dt><dd>بررسی اسکلت صفحه</dd>
<dt dir="ltr">Content Audit</dt><dd>بررسی خوانایی و Flow محتوا</dd>
<dt dir="ltr">Interaction Audit</dt><dd>بررسی حالت‌ها و کیبورد</dd>
<dt dir="ltr">Responsive Audit</dt><dd>بررسی رفتار در اندازه‌های مختلف</dd></dl>
<aside aria-label="قبل از ساخت در Elementor" class="before-elementor-card">
<h4>قبل از اینکه در Elementor چیزی بسازی</h4>
<p>اول با مداد یا ذهن خودت این سه سؤال را جواب بده؛ بعد وارد پنل Elementor شو:</p>
<ol>
<li>کدام بخش اسکلت است؟</li>
<li>کدام بخش محتواست؟</li>
<li>کدام بخش واقعاً باید هم‌پوشانی داشته باشد؟</li>
</ol>
<p class="why-note">قبل از Audit نهایی، هر بار فقط یک محور را بررسی کن تا گیج نشوی.</p>
</aside>
</section><section aria-labelledby="section-hidden-285-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-285-heading">بخش آموزشی</h2><dl class="term-grid"><dt>Structure</dt><dd>Wrapperهای لازم و بی‌دلیل</dd><dt>Style</dt><dd>Local تکراری و Class Explosion</dd><dt>Media</dt><dd>ابعاد، Alt، Format و Loading</dd><dt>Runtime</dt><dd>Overflow، Layout Shift و Interaction</dd></dl></section><p>DOM کمتر همیشه به‌تنهایی سریع‌تر نیست؛ هدف ساختار روشن و هزینهٔ منطقی است.</p><h3>سؤال Wrapper</h3><section aria-labelledby="section-hidden-286-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-286-heading">بخش آموزشی</h2><ul><li>این لایه چه مسئولیتی دارد؟</li>
<li>اگر حذف شود چه می‌شکند؟</li>
<li>آیا Layout/Scope/Position/Meaning می‌دهد؟</li></ul></section><hr/></section><details class="lesson-disclosure conceptual-reference" data-concept-version="31.0.0" data-source-sha256="2301883002f82f94b7c9f22599ca338f0896583bb34477075bc34e3d1519f889" id="lesson-20-concept-reference"><summary>📚 مرجع مفهومی کامل — درک عمیق Performance، DOM و Audit؛ ساده‌سازی قابل اندازه‌گیری</summary><div class="concept-reference-body concept-reference-v31" data-concept-index="26" data-source-version="31.0.0"><p class="concept-reference-lead">این مرجع کامل برای ساخت مدل ذهنی، عیب‌یابی و تصمیم‌گیری مستقل نوشته شده است. متن اصلی درس، کارت‌ها، آزمون‌ها و Step‑Throughها همچنان در جای خود باقی مانده‌اند.</p><section aria-labelledby="concept-v31-26-section-01" class="concept-reference-part concept-reference-problem"><h3 id="concept-v31-26-section-01">مسئله‌ای که Performance حل می‌کند</h3><p>Performance فقط امتیاز Lighthouse نیست. کاربر تجربه می‌کند:</p><ul>
<li>محتوای اصلی چه زمانی دیده می‌شود؛</li>
<li>صفحه هنگام Load چقدر می‌پرد؛</li>
<li>کلیک چقدر زود پاسخ می‌گیرد؛</li>
<li>Scroll و Animation چقدر روان‌اند.</li>
</ul><p>سه معیار اصلی Core Web Vitals این تجربه را از سه زاویه می‌بینند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">LCP: محتوای اصلی چه زمانی دیده شد؟
INP: تعامل چقدر زود پاسخ دید؟
CLS: صفحه چقدر بی‌اجازه جابه‌جا شد؟
</code></pre></figure><hr/></section><section aria-labelledby="concept-v31-26-section-02" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-26-section-02">تشبیه به دنیای واقعی: رستوران</h3><ul>
<li>LCP = غذای اصلی چه زمانی روی میز رسید؟</li>
<li>INP = وقتی گارسون را صدا زدی، چه زمانی پاسخ داد؟</li>
<li>CLS = آیا میز و صندلی هنگام نشستن ناگهان جابه‌جا شدند؟</li>
</ul><p>رستورانی که دکور سبک دارد اما غذا دیر می‌رسد، سریع نیست. سایتی با DOM کم اما Hero Image سنگین نیز لزوماً سریع نیست.</p><hr/></section><section aria-labelledby="concept-v31-26-section-03" class="concept-reference-part"><h3 id="concept-v31-26-section-03">آستانه‌های راهنما</h3><p>برای تجربه خوب، راهنمای فعلی Core Web Vitals معمولاً این هدف‌ها را مطرح می‌کند:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">LCP ≤ 2.5s
INP ≤ 200ms
CLS ≤ 0.1
</code></pre></figure><p>ارزیابی Field باید در صدک ۷۵ و جداگانه برای Mobile/Desktop دیده شود.</p><p>این اعداد هدف‌اند، نه تضمین رتبه و نه جایگزین تحلیل کاربر واقعی.</p><hr/></section><section aria-labelledby="concept-v31-26-section-04" class="concept-reference-part"><h3 id="concept-v31-26-section-04">LCP</h3><p>LCP زمان نمایش بزرگ‌ترین Image یا Text Block مهم در Viewport اولیه را می‌سنجد.</p><p>علت‌های رایج مشکل:</p><ul>
<li>Hero Image بزرگ</li>
<li>Lazy Load اشتباه روی LCP Image</li>
<li>کشف دیر Resource</li>
<li>Server Response کند</li>
<li>Font یا CSS مسدودکننده</li>
<li>Client-side rendering دیر</li>
</ul><p>برای Image اصلی:</p><ul>
<li>اندازه مناسب</li>
<li><code class="inline-code" dir="ltr">srcset/sizes</code></li>
<li>Width/Height</li>
<li>اولویت درست</li>
<li>فرمت مناسب</li>
</ul><p>را بررسی کن.</p><hr/></section><section aria-labelledby="concept-v31-26-section-05" class="concept-reference-part"><h3 id="concept-v31-26-section-05">CLS</h3><p>CLS جابه‌جایی غیرمنتظره Layout را می‌سنجد.</p><p>علت‌ها:</p><ul>
<li>Image بدون ابعاد</li>
<li>Embed بدون فضای رزروشده</li>
<li>Font Swap شدید</li>
<li>Dynamic Banner که بالای محتوا ظاهر می‌شود</li>
<li>Componentی که پس از Load ارتفاعش تغییر می‌کند</li>
<li>Animation روی Layout Property</li>
</ul><p><code class="inline-code" dir="ltr">aspect-ratio</code> یا Width/Height به رزرو فضای Image کمک می‌کند.</p><hr/></section><section aria-labelledby="concept-v31-26-section-06" class="concept-reference-part"><h3 id="concept-v31-26-section-06">INP</h3><p>INP تأخیر کلی Interactionهای کاربر را در طول بازدید می‌سنجد.</p><p>علت‌ها:</p><ul>
<li>JavaScript Long Task</li>
<li>Event Handler سنگین</li>
<li>DOM بزرگ</li>
<li>Style Recalculation گسترده</li>
<li>Layout Thrashing</li>
<li>Interactionهای زیاد</li>
<li>Third-party Script</li>
</ul><p>Animation طولانی لزوماً INP بد نمی‌سازد؛ مهم این است که پس از Input، Frame بعدی چقدر دیر آماده شود.</p><hr/></section><section aria-labelledby="concept-v31-26-section-07" class="concept-reference-part"><h3 id="concept-v31-26-section-07">DOM Size؛ معیار تشخیصی، نه حکم جهانی</h3><p>DOM بزرگ می‌تواند Memory، Style Recalculation و Layout را گران‌تر کند.</p><p>Lighthouse در Audit قدیمی/تشخیصی DOM Size از حدود ۸۰۰ Node برای هشدار و حدود ۱۴۰۰ برای وضعیت شدید استفاده کرده است، اما این اعداد قانون جهانی کیفیت نیستند.</p><p>نباید نوشت:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="auto"><code class="language-text inline-code" dir="ltr">همیشه زیر 1000 Node خوب است.
</code></pre></figure><p>یک صفحه ۷۰۰ Node با Script سنگین می‌تواند کندتر از صفحه ۱۵۰۰ Node ساده باشد.</p><p>همچنین برای هر Wrapper هزینه ثابت ۰٫۱ms یا ۰٫۳ms وجود ندارد. هزینه به Tree، Selector، Device و تغییرات Runtime وابسته است.</p><hr/></section><section aria-labelledby="concept-v31-26-section-08" class="concept-reference-part"><h3 id="concept-v31-26-section-08">Component و Token چگونه غیرمستقیم اثر می‌گذارند؟</h3><p>Component بد طراحی‌شده ممکن است:</p><ul>
<li>Wrapperهای تکراری بسازد؛</li>
<li>Imageهای غیرضروری Load کند؛</li>
<li>Interactionهای متعدد ثبت کند؛</li>
<li>Variantهای مخفی را هم‌زمان Render کند.</li>
</ul><p>Token بد طراحی‌شده مستقیماً LCP را کند نمی‌کند، اما می‌تواند:</p><ul>
<li>CSS متناقض و Overrideهای زیاد بسازد؛</li>
<li>تغییرات Style گسترده ایجاد کند؛</li>
<li>نگهداری را سخت کند.</li>
</ul><p>رابطه را علّی و دقیق بیان کن، نه اینکه «Token بد = CLS» بنویسی.</p><hr/></section><section aria-labelledby="concept-v31-26-section-09" class="concept-reference-part"><h3 id="concept-v31-26-section-09">Performance Budget</h3><p>برای پروژه Budget تعریف کن:</p><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">LCP target
INP target
CLS target
Maximum hero image bytes
Maximum third-party scripts
Interaction count review
DOM size review threshold
Font families/weights budget
</code></pre></figure><p>Budget باید متناسب با پروژه و دستگاه هدف باشد. عددهای بدون محیط تست فقط شعارند.</p><hr/></section><section aria-labelledby="concept-v31-26-section-10" class="concept-reference-part concept-reference-workflow"><h3 id="concept-v31-26-section-10">روش اندازه‌گیری قابل دفاع</h3><figure class="concept-code-figure"><pre class="ascii-diagram concept-code-block" dir="ltr"><code class="language-text inline-code" dir="ltr">Browser version
Lighthouse version
Device profile
Network throttling
CPU throttling
Cache state
Number of runs
Median result
Page state
</code></pre></figure><p>قبل و بعد را در شرایط مشابه مقایسه کن.</p><p>Lab Data برای Debug مفید است. Field Data نشان می‌دهد کاربران واقعی چه تجربه‌ای داشته‌اند. هیچ‌کدام جای دیگری را کامل نمی‌گیرد.</p><hr/></section><section aria-labelledby="concept-v31-26-section-11" class="concept-reference-part concept-reference-elementor"><h3 id="concept-v31-26-section-11">در Elementor V4</h3><p>Audit یک Section:</p><ol>
<li>Tree و Wrapperها</li>
<li>Imageها و Backgroundها</li>
<li>Fontها و Weightها</li>
<li>Interactions</li>
<li>Dynamic Content</li>
<li>Hidden duplicate content</li>
<li>Custom CSS و Selectorها</li>
<li>Third-party widgets</li>
<li>LCP candidate</li>
<li>Layout Shift sources</li>
</ol><p>Elementor فقط یکی از لایه‌های Stack است؛ Theme، Plugin، Hosting و WordPress نیز اثر دارند.</p><hr/></section><section aria-labelledby="concept-v31-26-section-12" class="concept-reference-part concept-reference-devtools"><h3 id="concept-v31-26-section-12">پل به DevTools</h3><ul>
<li>Performance Panel برای Main Thread و Interaction</li>
<li>Network Panel برای Image/Font/Script</li>
<li>Layout Shift Regions برای CLS</li>
<li>Lighthouse برای Audit آزمایشگاهی</li>
<li>Performance Insights/Trace برای LCP و INP</li>
</ul><p>یک عدد نهایی را بدون Trace تحلیل نکن.</p><hr/></section><section aria-labelledby="concept-v31-26-section-13" class="concept-reference-part concept-reference-traps"><h3 id="concept-v31-26-section-13">اشتباهات رایج</h3><ul>
<li>تمرکز فقط روی امتیاز</li>
<li>استفاده از یک اجرای Lighthouse</li>
<li>Lazy Load تصویر LCP</li>
<li>حذف Wrapper مسئول فقط برای Node کمتر</li>
<li>عدد ثابت هزینه هر Element</li>
<li>نسبت‌دادن همه مشکلات به Elementor</li>
<li>نادیده‌گرفتن Third-partyها</li>
<li>مقایسه قبل/بعد در شرایط متفاوت</li>
<li>گفتن «جریمه Google» به‌جای تمرکز بر UX</li>
</ul><hr/></section><section aria-labelledby="concept-v31-26-section-14" class="concept-reference-part concept-reference-analogy"><h3 id="concept-v31-26-section-14">تصویر ذهنی نهایی</h3><p>Performance رستوران است: غذا باید زود برسد، گارسون زود جواب دهد و میز زیر دست کاربر نپرد. کم‌بودن تعداد صندلی‌ها به‌تنهایی هیچ‌کدام را تضمین نمی‌کند.</p><hr/></section><section aria-labelledby="concept-v31-26-section-15" class="concept-reference-part concept-reference-golden"><h3 id="concept-v31-26-section-15">قوانین طلایی</h3><ul>
<li><strong>«Performance را با LCP، INP، CLS و Trace واقعی ببین، نه فقط تعداد Node.»</strong></li>
<li><strong>«عدد بدون محیط تست، مدرک نیست.»</strong></li>
<li><strong>«تصویر LCP را زود پیدا و درست اندازه‌گذاری کن.»</strong></li>
<li><strong>«فضای Media و Dynamic Content را پیشاپیش رزرو کن.»</strong></li>
<li><strong>«بهبود را اندازه بگیر؛ از روی ظاهر یا نسخه حدس نزن.»</strong></li>
</ul></section><footer class="concept-reference-evidence"><h3>منابع رسمی و وضعیت اعتبار این فصل</h3><p>رفتارهای CSS و مرورگر از استانداردها و مستندات رسمی، رفتار Elementor از Help Center رسمی، و تشبیه‌ها به‌عنوان <code class="inline-code" dir="ltr">derived_explanation</code> ارائه شده‌اند.</p><ul>
<li>web.dev: Core Web Vitals, LCP, INP and CLS</li>
<li>Chrome DevTools: Performance reference</li>
<li>Elementor performance guidance</li>
</ul><hr/></footer></div></details><details class="lesson-disclosure settings-values-units" id="lesson-20-settings-values-units">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" id="lesson-20-settings-values-units-heading" role="heading">⚙️ تنظیمات، مقدارها و واحدها — Performance؛ بعضی شاخص‌ها واحد فنی دیگری دارند</span></summary>
<section aria-labelledby="lesson-20-settings-values-units-heading" class="disclosure-content settings-units-body">
<p class="settings-units-lead">Performance فقط CSS length نیست. DOM count عدد، زمان بارگیری ms، حجم فایل KB/MB و layout shift امتیاز بدون واحد است.</p>
<aside class="unit-analogy"><strong>🧠 تصویر ذهنی:</strong> سلامت صفحه را با چند دستگاه می‌سنجی: ترازو، ساعت و شمارنده؛ یک واحد برای همه کافی نیست.</aside>
<div aria-label="جدول تنظیمات و واحدهای این درس" class="table-wrap units-table-wrap" role="region" tabindex="0">
<table class="data-table educational-table units-context-table">
<caption>تنظیمات، نوع مقدار، مرجع محاسبه و راهنمای انتخاب</caption>
<thead><tr><th scope="col">تنظیم</th><th scope="col">CSS / مفهوم</th><th scope="col">مقدار یا واحد</th><th scope="col">مرجع</th><th scope="col">کاربرد پیشنهادی</th><th scope="col">تله</th><th scope="col">شاهد</th></tr></thead>
<tbody><tr><th scope="row">DOM nodes</th><td><code dir="ltr">node count</code></td><td>integer</td><td>بدون واحد طول</td><td>برای پیچیدگی ساختار.</td><td>تعداد کمتر همیشه بهتر نیست؛ ساختار درست مهم است.</td><td><code dir="ltr">E_DIFF</code></td></tr><tr><th scope="row">Load / interaction time</th><td><code dir="ltr">time</code></td><td>ms / s</td><td>زمان</td><td>برای پاسخ‌گویی.</td><td>عدد بدون شرایط آزمایش قابل مقایسه نیست.</td><td><code dir="ltr">CSS_TIME</code></td></tr><tr><th scope="row">Asset size</th><td><code dir="ltr">file size</code></td><td>KB / MB</td><td>بایت</td><td>برای تصاویر و فایل‌ها.</td><td>ابعاد CSS px با حجم فایل یکی نیست.</td><td><code dir="ltr">MDN_VALUES</code></td></tr><tr><th scope="row">Rendered dimensions</th><td><code dir="ltr">width / height</code></td><td>CSS px</td><td>viewport/device scale</td><td>برای جلوگیری از overfetch و layout shift.</td><td>CSS px الزاماً یک device pixel نیست.</td><td><code dir="ltr">MDN_LENGTH</code></td></tr></tbody>
</table>
</div>
<div class="unit-guidance-grid">
<section><h3>🧮 محاسبهٔ راهگشا</h3><p>1000ms=1s؛ تصویر 2400×1600 که در 600×400 نمایش می‌شود ممکن است بیش‌ازحد بزرگ دریافت شده باشد، اما حجم واقعی به فشرده‌سازی هم بستگی دارد.</p></section>
<section><h3>📱 در Responsive</h3><p>Performance را روی شبکه و دستگاه واقعی Mobile نیز بررسی کن.</p></section>
<section><h3>🔬 در DevTools</h3><p>Performance، Network، Layout Shift و DOM count را جدا ثبت کن.</p></section>
</div>
<p class="unit-atlas-link"><a href="#appendix-v29-units-atlas">📐 بازگشت به اطلس مرکزی مقدارها و واحدها</a></p>
<footer class="settings-units-evidence"><strong>وضعیت:</strong> <code dir="ltr">verified_by_official_help_and_css_sources</code><br/><strong>منابع:</strong> <a href="https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/" rel="noopener noreferrer" target="_blank">Elementor — Differences between Editor V3 and V4</a>، <a href="https://www.w3.org/TR/css-values-4/#time" rel="noopener noreferrer" target="_blank">W3C — CSS Values time data type</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length" rel="noopener noreferrer" target="_blank">MDN — CSS length values</a>، <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units" rel="noopener noreferrer" target="_blank">MDN — CSS values and units</a></footer>
</section>
</details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-20-lesson-practice-5" role="heading">B. بساز و امتحان کن</span></summary><section aria-labelledby="lesson-20-lesson-practice-5" class="disclosure-content lesson-practice lesson-section"><h3>🏗 پروژهٔ TUYA — Audit نهایی</h3><p>Tree را مرور کن:</p><ul>
<li>Wrapper بی‌دلیل؟</li>
<li>Global Class تکراری؟</li>
<li>Image بزرگ‌تر از نیاز؟</li>
<li>SVGهای تزئینی قابل بهینه‌سازی؟</li>
<li>Altها درست؟</li>
<li>Width/Height یا Ratio مشخص؟</li>
<li>Scroll افقی؟</li>
<li>Nodeها در Mobile قابل کنترل؟</li>
</ul><h3>❓ سؤال توقف</h3><p>آیا هر Div اضافی الزاماً مشکل Performance است؟</p><details class="disclosure-card"><summary>پاسخ</summary>خیر؛ باید نقش و هزینهٔ واقعی بررسی شود.</details><h3>⚠️ تلهٔ اصلی</h3><p><strong>تله:</strong> برای حل Scroll افقی فقط Overflow Hidden بدهی.</p><p><strong>نشانه:</strong> مشکل دیده نمی‌شود، اما محتوا Clip شده است.</p><h3>🧪 عمداً خرابش کن</h3><p>یک Image بسیار بزرگ بدون ابعاد مشخص اضافه کن و Network را کند کن.</p><h4>👀 انتظار داری ببینی</h4><ul>
<li>دانلود بزرگ‌تر؛</li>
<li>احتمال جابه‌جایی Layout؛</li>
<li>دیرتر ظاهرشدن تصویر.</li>
</ul><p>سپس ابعاد، منبع مناسب و Loading را اصلاح کن.</p><h3>Checkpoint</h3><section aria-labelledby="section-hidden-288-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-288-heading">بخش آموزشی</h2><form class="interactive-form checklist-form" data-persist-group="checklist-114"><fieldset><legend>Checkpoint</legend><label class="choice-row"><input data-persist="checkbox" id="chk-114-1" name="chk-114-1" type="checkbox"/><span>هر Wrapper دلیل دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-114-2" name="chk-114-2" type="checkbox"/><span>Style مشترک یک منبع دارد</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-114-3" name="chk-114-3" type="checkbox"/><span>رسانه متناسب و دارای ابعاد است</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-114-4" name="chk-114-4" type="checkbox"/><span>Overflow علت‌یابی شده، نه پنهان</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-114-5" name="chk-114-5" type="checkbox"/><span>Runtime tests ثبت شده‌اند</span></label></fieldset></form></section><h3>Exit Ticket — قبل از ادامه</h3><p><strong>بازیابی کوتاه:</strong> چهار محور Audit چیست؟</p><p><strong>انتقال به یک موقعیت تازه:</strong> Scroll افقی ناپدید شده چون overflow:hidden داده‌ای. چرا هنوز مسئله حل نشده است؟</p><details class="disclosure-card">
<summary>راهنمای خودسنجی اختصاصی همین درس</summary>
<h3>آناتومی پاسخ خوب</h3>
<form class="interactive-form checklist-form" data-persist-group="checklist-115"><fieldset><legend>آناتومی پاسخ خوب</legend><label class="choice-row"><input data-persist="checkbox" id="chk-115-1" name="chk-115-1" type="checkbox"/><span>نشانه، علت فرضی و شاهد را از هم جدا کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-115-2" name="chk-115-2" type="checkbox"/><span>Structure، Style، Media و Runtime را بررسی کرده است.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-115-3" name="chk-115-3" type="checkbox"/><span>راه‌حل حداقلی را اعمال و Regression Test تعریف کرده است.</span></label></fieldset></form>
<p>پاسخ کامل لازم نیست طولانی باشد؛ باید نشان بدهد <strong>چه چیزی را بررسی می‌کنی، چرا، و چگونه نتیجه را اثبات می‌کنی</strong>.</p>
</details></section></details><details aria-labelledby="lesson-20-lesson-deep-dive-7" class="lesson-section lesson-deep-dive lesson-disclosure"><summary class="lesson-disclosure-summary" id="lesson-20-lesson-deep-dive-7">C. عمیق‌تر نگاه کن — اختیاری</summary><h3>📂 CASE-HOME2-DOM-001</h3><p><strong>هدف:</strong> 🔍 عیب‌یابی کن</p><p>Elementهای خالی را یک‌به‌یک در Runtime غیرفعال کن و نقششان را ثبت کن. حذف گروهی بدون شواهد ممنوع.</p><h3>📂 CASE-HOME2-REUSE-001</h3><p><strong>هدف:</strong> 🔧 بازسازی کن</p><p>Style signatureهای تکراری را به Global Class یا Component تبدیل کن و تعداد نقاط ویرایش را مقایسه کن.</p><h3>🔬 پشت صحنه</h3><p>Browser DOM، CSSOM، Layout و Paint را پردازش می‌کند؛ اما دوره روی تصمیم‌های قابل کنترل در Elementor تمرکز دارد.</p><hr/></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-20-lesson-pass-criteria-8" role="heading">✅ معیار عبور اختصاصی این درس</span></summary><section aria-labelledby="lesson-20-lesson-pass-criteria-8" class="disclosure-content lesson-section lesson-pass-criteria"><p>برای رفتن به درس بعد، <strong>سطح ۱ و ۲ اجباری‌اند</strong>. سطح ۳ در ایستگاه جمع‌بندی تثبیت می‌شود.</p><h3>سطح ۱ — فهمیدم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-117"><fieldset><legend>سطح ۱ — فهمیدم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-117-1" name="chk-117-1" type="checkbox"/><span>می‌توانی Audit را در چهار محور Structure، Style، Media و Runtime توضیح بدهی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-117-2" name="chk-117-2" type="checkbox"/><span>می‌توانی بگویی چرا Wrapper بیشتر یا DOM کمتر به‌تنهایی حکم Performance نیست.</span></label></fieldset></form><h3>سطح ۲ — می‌توانم انجام بدهم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-118"><fieldset><legend>سطح ۲ — می‌توانم انجام بدهم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-118-1" name="chk-118-1" type="checkbox"/><span>برای هر Wrapper پروژه یک مسئولیت ثبت می‌کنی.</span></label><label class="choice-row"><input data-persist="checkbox" id="chk-118-2" name="chk-118-2" type="checkbox"/><span>رسانه، تکرار Class، Overflow و Layout Shift را با شواهد بررسی می‌کنی.</span></label></fieldset></form><h3>سطح ۳ — می‌توانم منتقل کنم</h3><form class="interactive-form checklist-form" data-persist-group="checklist-119"><fieldset><legend>سطح ۳ — می‌توانم منتقل کنم</legend><label class="choice-row"><input data-persist="checkbox" id="chk-119-1" name="chk-119-1" type="checkbox"/><span>در سناریوی Scroll افقی می‌توانی به‌جای overflow:hidden، عنصر و Property عامل را پیدا کنی.</span></label></fieldset></form></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-20-lesson-stop-point-9" role="heading">⏸ اینجا توقف کن</span></summary><section aria-labelledby="lesson-20-lesson-stop-point-9" class="lesson-stop-point lesson-section disclosure-content"><p>فقط Boss Fight باقی مانده است: ساخت مستقل، ارزیابی و توضیح تصمیم‌ها.</p><hr/></section></details><details class="lesson-disclosure"><summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">ثبت پایان درس 20</span></summary><form class="disclosure-content lesson-completion-form interactive-form" data-persist-group="lesson-20-completion"><fieldset><legend>ثبت پایان درس 20</legend><label class="choice-row completion-choice"><input data-persist="checkbox" id="lesson-20-complete" name="lesson-20-complete" type="checkbox"/><span>این درس را با معیارهای عبور مرور کردم.</span></label></fieldset></form></details>
<details class="lesson-disclosure" id="lesson-20-end-comparisons"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">🆚 پایان درس: Performance Optimization در برابر Visual Cleanup</span></summary><section class="disclosure-content lesson-end-comparisons">
<div class="inline-compare-grid">
<section class="inline-compare-card"><h3>Visual Cleanup</h3><p>Visual Cleanup یعنی ظاهر یا پنل را مرتب‌تر می‌کنی؛ ممکن است کمک کند، اما لزوماً وزن واقعی صفحه را کم نمی‌کند.</p></section>
<section class="inline-compare-card"><h3>Performance Optimization</h3><p>Optimization یعنی DOM، CSS، asset، JS، layout و نگهداری را کم‌هزینه‌تر می‌کنی. برای حکم قطعی باید خروجی واقعی و Runtime را ببینی.</p><p class="golden-rule">قانون طلایی: هر چیزی که تمیز به نظر می‌رسد لزوماً سبک نیست؛ وزن را با شواهد بسنج.</p></section>
</div>
</section></details>
<details class="lesson-disclosure" id="lesson-20-practical-findings"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" id="lesson-20-practical-findings-heading" role="heading">🔎 یافتهٔ عملی و خطایابی</span></summary><section aria-labelledby="lesson-20-practical-findings-heading" class="disclosure-content practical-findings">
<p class="finding-scope">این بخش فقط ادعاهایی را آموزش می‌دهد که یا در مشاهدهٔ واقعی ثبت شده‌اند یا Help Center رسمی Elementor آن‌ها را صریحاً پشتیبانی می‌کند. نتیجه‌های وابسته به Theme، نسخه یا ساختار DOM با دامنهٔ اعتبار نوشته شده‌اند.</p>
<article class="finding-card" data-verification="verified_by_official_help" id="finding-editor-frontend-mismatch">
<div class="evidence-badges"><span class="evidence-badge official">تأیید Help Center</span></div>
<h3>چرا تغییر در Editor درست است ولی روی سایت زنده نمی‌آید؟</h3>
<p><strong>علت‌های رسمی محتمل:</strong> cache مرورگر، افزونه، سرور یا CDN؛ فایل‌ها و داده‌های تولیدشده؛ CSS Print Method؛ URL/SSL/permalink؛ کد یا tag بسته‌نشده؛ یا خرابی metadata یک Element.</p>
<ol class="case-steps">
<li>در یک پنجرهٔ Private/Incognito تست کن و cacheهای browser/plugin/server/CDN را پاک کن.</li>
<li>WP Admin → Elementor → Editor/Home → Tools → <strong>Clear Files &amp; Data</strong> و سپس Save Changes.</li>
<li>صفحه را Update کن و frontend را دوباره باز کن.</li>
<li>اگر mismatch باقی ماند، CSS Print Method و custom code/tagهای بسته‌نشده را بررسی کن.</li>
<li>فقط پس از این مراحل سراغ بازسازی دستی Element برو.</li>
</ol>
<p class="golden-rule"><strong>قانون طلایی:</strong> قبل از تغییر دوبارهٔ طراحی، مطمئن شو frontend همان نسل فایل و داده‌ای را می‌خواند که Editor ذخیره کرده است.</p>
<details class="more-know"><summary>منابع رسمی</summary><p><a href="https://elementor.com/help/changes-dont-appear-online/">My changes do not appear online</a>، <a href="https://elementor.com/help/regenerate-css-data/">Clear Files &amp; Data</a> و <a href="https://elementor.com/help/troubleshooting-layout-issues/">Troubleshooting layout issues</a></p></details>
</article>
</section></details>
<details class="lesson-disclosure" id="lesson-20-responsive-checkpoint"><summary class="lesson-disclosure-summary"><span aria-level="2" class="disclosure-title" role="heading">📱 ایست بازرسی Responsive — Responsive QA در frontend واقعی</span></summary><section class="disclosure-content lesson-section responsive-checkpoint">
<p class="status-chip"><strong>status:</strong> verified_and_scoped</p>
<p>Preview دستگاه نقطهٔ شروع است، نه پایان QA. Desktop، Tablet، Mobile و چند عرض بین آن‌ها را در frontend واقعی بررسی کن.</p>
<ul><li>Horizontal overflow</li><li>ترتیب خواندن و Tab</li><li>تصویر و crop</li><li>لوگوها در عرض میانی</li><li>Cache و Clear Files &amp; Data در صورت اختلاف Editor/Frontend</li></ul>
<details class="more-know"><summary>منابع رسمی این ایست</summary>
<ul>
<li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — Editor V4</a></li>
<li><a href="https://elementor.com/help/responsive-design-using-containers/">Create responsive design with containers</a></li>
<li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li>
</ul>
</details>
</section></details><details class="lesson-disclosure responsive-build-test" id="lesson-20-responsive-build-test">
<summary class="lesson-disclosure-summary"><span aria-level="3" role="heading">📱 بساز و امتحان کن — Responsive: QA واقعی بین Editor و Frontend</span></summary>
<section class="disclosure-content lesson-section responsive-build-test-content">
<p class="status-chip"><strong>status:</strong> verified_by_official_documentation</p>
<p class="exercise-goal"><strong>هدف:</strong> Responsive را فقط در preview پنل تأیید نکن.</p>
<div class="responsive-exercise-grid">
<section class="exercise-step"><h4>۱. بساز</h4><ol><li>صفحه را ذخیره و frontend واقعی را در Desktop، Tablet و Mobile باز کن.</li><li>چند عرض بین breakpointها را با DevTools یا تغییر اندازهٔ پنجره تست کن.</li><li>Console، Network و CSS source را برای خطاهای مرتبط بررسی کن.</li></ol></section>
<section class="exercise-step"><h4>۲. پیش‌بینی کن</h4><p>قبل از refresh سخت بگو کدام تفاوت ممکن است از cache یا فایل تولیدشده باشد و کدام از layout واقعی.</p></section>
<section class="exercise-step exercise-break"><h4>۳. خرابی عمدی</h4><p>یک تغییر responsive بده، بدون refresh/cache clear frontend را مقایسه کن و سپس روش صحیح را انجام بده.</p></section>
<section class="exercise-step"><h4>۴. امتحان و خطایابی</h4><p>Network CSS، matched rules، viewport width، horizontal overflow و Console.</p></section>
</div>
<p class="exercise-pass"><strong>معیار قبولی:</strong> نسخهٔ live با Editor هماهنگ است و هیچ شکست بین breakpointها یا خطای asset پنهان باقی نمانده است.</p>
<fieldset class="responsive-exercise-log">
<legend>ثبت انجام تمرین</legend>
<label for="lesson-20-responsive-build-test-done-build"><input data-persist="" id="lesson-20-responsive-build-test-done-build" name="lesson-20-responsive-build-test-done-build" type="checkbox"/> ساخت را انجام دادم و قبل از مشاهده پیش‌بینی نوشتم.</label>
<label for="lesson-20-responsive-build-test-done-test"><input data-persist="" id="lesson-20-responsive-build-test-done-test" name="lesson-20-responsive-build-test-done-test" type="checkbox"/> Desktop، Tablet، Mobile و یک عرض بین breakpointها را آزمودم.</label>
<label for="lesson-20-responsive-build-test-done-debug"><input data-persist="" id="lesson-20-responsive-build-test-done-debug" name="lesson-20-responsive-build-test-done-debug" type="checkbox"/> حداقل یک مقدار را در Computed Style یا Box Model بررسی کردم.</label>
<label class="exercise-note-label" for="lesson-20-responsive-build-test-note">نتیجهٔ یک‌خطی من
        <input data-persist="" id="lesson-20-responsive-build-test-note" name="lesson-20-responsive-build-test-note" placeholder="مثلاً: مقدار Mobile از Tablet ارث می‌گرفت." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مبنای رسمی:</strong> <a href="https://elementor.com/help/troubleshooting-layout-issues/">Help Center رسمی Elementor</a>. نتیجهٔ مشاهده‌شدهٔ تمرین به محیط، محتوا و breakpointهای پروژه وابسته است.</p>
</section>
</details><details class="lesson-disclosure design-system-decision" id="lesson-20-design-system-decision-v30">
<summary class="lesson-disclosure-summary"><span aria-level="3" class="disclosure-title" role="heading">🏛 تصمیم Design System — Performance audit</span></summary>
<section class="disclosure-content lesson-section">
<ul class="decision-questions"><li>این مقدار باید direct literal بماند یا Variable شود؟</li><li>declaration در Local Class می‌ماند یا reuse آن Global Class را توجیه می‌کند؟</li><li>فقط Style reuse داریم یا Structure نیز تکرار شده است؟</li><li>آیا Component واقعاً توجیه دارد، یا Class/Variable کافی است؟</li></ul>
<p><code dir="ltr">proposed_strategy</code> — پاسخ وابسته به intent، scope، reuse و هزینهٔ propagation است.</p>
</section></details></article>
