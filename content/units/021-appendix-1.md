<article class="appendix card-surface" id="appendix-1"><h2 class="former-h1">Elementor V4 از سردرگمی تا طراحی ساختارمند</h2><section class="appendix-body"><h2>نسخهٔ ۱۴.۱ — Pilot Edition برای تبدیل ذهن گیج به ذهن شفاف و ساختارمند</h2><p><strong>شعار دوره:</strong> یک مسیر آموزشی واقعاً مناسب برای ذهن گیج و مبتدی و تبدیل آن ذهن به یک ذهن شفاف، واضح و ساختارمند.</p><hr/><h2>این دوره برای چه کسی است؟</h2><p>این دوره برای کسی نوشته شده که می‌خواهد با <strong>Elementor Editor V4</strong> عالی کار کند، نه اینکه فعلاً به یک توسعه‌دهندهٔ کامل CSS تبدیل شود.</p><p>هدف نهایی:</p><section aria-labelledby="section-hidden-2-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-2-heading">بخش آموزشی</h2><ul><li>نه حفظ‌کردن ده‌ها گزینه</li>
<li>نه کلیک‌کردن تصادفی</li>
<li>نه ساختن صفحه با آزمون و خطای بی‌پایان</li>
<li>بلکه:</li>
<li>دیدن ساختار</li>
<li>فهمیدن نقش Elementها</li>
<li>انتخاب ابزار مناسب</li>
<li>ساختن Class System تمیز</li>
<li>حل‌کردن Responsive بدون آشفتگی</li>
<li>تشخیص Hybrid V3/V4</li>
<li>عیب‌یابی با یک مسیر روشن</li></ul></section><h2>نسبت آموزشی دوره</h2><section aria-labelledby="section-hidden-3-heading" class="smart-note-card" dir="rtl" lang="fa"><h2 class="visually-hidden" id="section-hidden-3-heading">بخش آموزشی</h2><ul><li>Elementor V4 و Workflow       ████████████████████</li>
<li>منطق طراحی و تصمیم‌گیری       ████████████████</li>
<li>CSS ضروری پشت صحنه            ██████</li>
<li>کدنویسی دستی CSS              ██</li></ul></section><p>CSS در این دوره فقط به‌اندازه‌ای آموزش داده می‌شود که کنترل‌های Elementor را عمیق بفهمی و هنگام خرابی بتوانی علت را پیدا کنی.</p><hr/><h2>سیاست سخت‌سازی RTL بلوک‌های آموزشی</h2><p>بلوک‌های فارسی و نمودارهای متنی دیگر به Fence معمولی Markdown متکی نیستند. آن‌ها با عناصر صریح زیر رندر می‌شوند:</p><ul>
<li><code class="inline-code" dir="ltr">lang="fa"</code> برای زبان؛</li>
<li><code class="inline-code" dir="ltr">dir="rtl"</code> برای جهت پایه؛</li>
<li><code class="inline-code" dir="ltr">direction: rtl !important</code> برای مقاومت در برابر Styleهای دیرهنگام Renderer؛</li>
<li><code class="inline-code" dir="ltr">text-align: right !important</code> برای قفل‌کردن تراز؛</li>
<li><code class="inline-code" dir="ltr">unicode-bidi: plaintext !important</code> برای مدیریت بهتر خط‌های ترکیبی فارسی، عدد و عبارت انگلیسی؛</li>
<li><code class="inline-code" dir="ltr">white-space: pre-wrap</code> برای حفظ نمودار و جلوگیری از خروج بی‌دلیل از عرض.</li>
</ul><p>بلوک‌های واقعی CSS، HTML، JSON و JavaScript عمداً LTR باقی می‌مانند.</p><p class="status-line"><code class="inline-code" dir="ltr">status: visual_scaffold_rtl_hardened</code></p><hr/><h2>سیاست Visual Card در نسخهٔ ۱۴.۱</h2><p>در نسخهٔ ۱۴.۱، داربست‌های بصری مهم از ASCII Art خام به <strong>Visual Cardهای HTML</strong> تبدیل شده‌اند.</p><p>دلیل تغییر:</p><ul>
<li>ASCII Art در متن‌های دوجهتهٔ فارسی/لاتین شکننده است؛</li>
<li>فونت monospace برای متن فارسی آموزشی خوانایی کمتری دارد؛</li>
<li>Visual Cardها با Flex/Grid، Label، Badge و Box بهتر مفهوم را منتقل می‌کنند؛</li>
<li>متن فارسی در این Cardها با فونت UI/وزیر نمایش داده می‌شود؛</li>
<li>کدهای واقعی CSS/HTML/JSON همچنان LTR و monospace باقی می‌مانند.</li>
</ul><p class="status-line"><code class="inline-code" dir="ltr">status: html_visual_cards_added</code></p><hr/><h2>سیاست نمایش PersianNew در HTML Viewer</h2><p>فایل HTML مستقل این نسخه با CSS اختصاصی <code class="inline-code" dir="ltr">PersianNew_v12_4_HTML_Viewer.css</code> رندر می‌شود. این CSS از منطق تم PersianNew استفاده می‌کند:</p><ul>
<li>Wrapper اصلی با <code class="inline-code" dir="ltr">id="write"</code> هماهنگ شده است؛</li>
<li>صفحه، جدول‌ها، لیست‌ها و متن‌ها RTL هستند؛</li>
<li>Code واقعی مانند CSS/HTML/JSON چپ‌به‌راست باقی می‌ماند؛</li>
<li>بلوک‌های آموزشی فارسی و ASCII با کلاس <code class="inline-code" dir="ltr">edis-rtl-text-block</code> راست‌به‌چپ و راست‌چین قفل شده‌اند؛</li>
<li>مسیر فونت‌ها به‌صورت <code class="inline-code" dir="ltr">./fonts/...</code> تنظیم شده تا اگر فونت‌ها را کنار HTML بگذاری، بارگذاری شوند.</li>
</ul><p class="status-line"><code class="inline-code" dir="ltr">status: persiannew_html_aligned</code></p><hr/><h2>سیاست داربست بصری ASCII</h2><p>در نسخهٔ ۱۴.۱، هرجا هنرجوی مبتدی باید <strong>ساختار، Flow، Overlap، خراب‌شدن یا تصمیم Layout</strong> را ببیند، یک داربست بصری کوتاه اضافه شده است.</p><p>قاعدهٔ استفاده:</p><ul>
<li>اول تصویر ساده؛</li>
<li>بعد سؤال؛</li>
<li>بعد توضیح؛</li>
<li>بعد خراب‌کردن کنترل‌شده.</li>
</ul><details class="more-know ascii-disclosure"><summary>نمای متنی ساده / ASCII اختیاری</summary><figure class="visual-figure ascii-figure"><figcaption>نمودار یا یادداشت دیداری</figcaption><pre class="ascii-diagram" dir="rtl">قانون بصری نسخهٔ ۱۴.۱

[ ببین ]
    |
    v
[ تصمیم بگیر ]
    |
    v
[ بساز ]
    |
    v
[ خراب کن و نشانه را ببین ]
    |
    v
[ اصلاح کن ]</pre></figure></details><p class="status-line"><code class="inline-code" dir="ltr">status: visual_scaffold_added</code></p><hr/><h2>وضعیت این نسخه: Pilot Edition</h2><p>نسخهٔ ۱۳ از نظر محتوا و معماری آموزشی آمادهٔ استفاده است، اما زمان‌های درس و بعضی تصمیم‌های حمایتی هنوز <strong>پیشنهادی</strong> هستند تا با رفتار یک هنرجوی واقعی سنجیده شوند.</p><pre class="code-block" dir="ltr" tabindex="0"><code class="language-text" dir="ltr">course_content_status: ready_for_pilot
lesson_time_status: proposed
runtime_elementor_validation: not_performed
real_learner_observation: required_for_next_major_revision
</code></pre><p>در Pilot این شواهد ثبت می‌شوند:</p><ul>
<li>زمان واقعی هر درس؛</li>
<li>نقطه‌ای که هنرجو مکث یا رها می‌کند؛</li>
<li>اصطلاحی که دوباره می‌پرسد؛</li>
<li>Controlی که پیدا نمی‌کند؛</li>
<li>خطا در Exit Ticket؛</li>
<li>مراجعه به کارت نجات؛</li>
<li>تفاوت احساس یادگیری با شواهد واقعی انجام کار.</li>
</ul><blockquote>
<p>زمان، معیار تسلط نیست. عبور از درس با معیارهای سطح ۱ و ۲ تعیین می‌شود.</p>
</blockquote><hr/></section></article>
