<article class="appendix card-surface responsive-workshop" id="appendix-v25-tuya-responsive-workshop">
<h2 class="former-h1">کارگاه Responsive TUYA — از Desktop به Mobile بدون ساخت نسخهٔ تکراری</h2>
<section class="workshop-core lesson-core-concept" id="tuya-responsive-core">
<h3>مفهوم اصلی: طرح Mobile خوب است، اما هنوز یک قرارداد کامل Responsive نیست</h3>
<p>طرح پیوست‌شده از نظر ترکیب‌بندی Mobile <strong>قابل دفاع و قابل پیاده‌سازی</strong> است: ساختار تک‌ستونه است، Visual پیش از Copy آمده و Logo Strip در پایان قرار گرفته است. این تصمیم‌ها با صفحهٔ باریک سازگارند.</p>
<p>بااین‌حال Screenshot مقدار دقیق breakpoint، Width، Gap، Padding، Order و رفتار Tablet را ثابت نمی‌کند. این موارد باید در Elementor و با تأیید طراح نهایی شوند.</p>
<div class="tuya-reference-grid">
<figure class="responsive-reference-card"><img alt="مرجع Desktop پروژه TUYA" loading="lazy" src="assets/images/tuya-reference.jpg"/><figcaption>مرجع Desktop موجود در بسته</figcaption></figure>
<figure class="responsive-reference-card mobile-reference"><img alt="طرح Mobile TUYA با Visual در بالا، متن در میانه و Logo Strip در پایین" loading="lazy" src="assets/images/tuya-mobile-reference-v25.png"/><figcaption>مرجع Mobile مشاهده‌شده — 881×2047، پس‌زمینهٔ بیرونی شفاف</figcaption></figure>
</div>
</section>
<details class="workshop-disclosure"><summary><span aria-level="3" role="heading">۱. چه چیزهایی از طرح Mobile واقعاً مشاهده می‌شود؟</span></summary>
<ul><li>یک جریان عمودی و تک‌ستونه؛</li><li>Visual پیش از Copy؛</li><li>Copy پیش از Logo Strip؛</li><li>شش Node پیرامون Core؛</li><li>Visual Stage بزرگ‌تر از عرض Core و دارای overlap کنترل‌شده.</li></ul>
<p><strong>نکته:</strong> نوارهای تیرهٔ دو طرف، بخشی از طراحی نیستند؛ ناحیهٔ بیرونی PNG شفاف است.</p>
</details>
<details class="workshop-disclosure"><summary><span aria-level="3" role="heading">۲. چه چیزهایی هنوز insufficient_evidence هستند؟</span></summary>
<ul><li>Breakpoint دقیق ورود به این ترکیب؛</li><li>رفتار Tablet؛</li><li>واحدهای دقیق اندازه‌گیری؛</li><li>این‌که Visual با Custom Order بالا آمده یا DOM از ابتدا همین ترتیب را دارد؛</li><li>این‌که Nodeها تعاملی‌اند یا فقط تصویری.</li></ul>
</details>
<details class="workshop-disclosure"><summary><span aria-level="3" role="heading">۳. قرارداد ساخت در Elementor V4</span></summary>
<ol><li>یک Shell اصلی در Flow بساز.</li><li>یک Main Container برای Visual، Copy و Logo Strip نگه دار.</li><li>Desktop: Main می‌تواند Row باشد.</li><li>Mobile: Direction را Column کن و فقط در صورت نیاز Custom Order بده.</li><li>Visual Stage را Relative نگه دار؛ Nodeها را داخل آن Absolute کن.</li><li>Width/Height و Typography را با breakpoint controls بازبینی کن.</li><li>نسخهٔ تکراری Desktop/Mobile نساز، مگر نیاز واقعی و مستند وجود داشته باشد.</li></ol>
</details>
<details class="workshop-disclosure"><summary><span aria-level="3" role="heading">۴. رفتار پیشنهادی Tablet — هنوز مشاهده نشده</span></summary>
<p><strong>status:</strong> proposed_pending_designer_confirmation</p>
<p>Tablet را نباید از روی حدس به Mobile یا Desktop برابر دانست. ابتدا نسخهٔ Desktop را در عرض‌های میانی کوچک کن. هرجا Copy، Visual یا Logo Strip شروع به شکست کرد، همان رفتار را با طراح تأیید کن.</p>
<p>پیشنهاد آزمایشی—not observed—این است که Main پیش از Mobile به Column تبدیل شود، اما اندازهٔ Visual و Typography بین Desktop و Mobile باقی بماند.</p>
</details>
<details class="workshop-disclosure"><summary><span aria-level="3" role="heading">۵. مراحل اجرا در Responsive Mode</span></summary>
<ol><li>Desktop baseline را بساز.</li><li>از Top Bar وارد Tablet شو و مقادیر inherited را تشخیص بده.</li><li>فقط Direction/Width/Gap/Order لازم را override کن.</li><li>وارد Mobile شو و crop تصویر، اندازهٔ Stage، Typography و Logo Strip را تنظیم کن.</li><li>با viewport handles عرض‌های بین breakpointها را تست کن.</li><li>در frontend واقعی overflow و ترتیب خواندن را بررسی کن.</li></ol>
</details>
<details class="workshop-disclosure"><summary><span aria-level="3" role="heading">۶. چک‌لیست پذیرش TUYA Responsive</span></summary>
<ul class="checklist-grid"><li>هیچ اسکرول افقی ناخواسته وجود ندارد.</li><li>Copy در DOM و صفحه خوانا است.</li><li>Visual Stage ارتفاع Flow را نمی‌شکند.</li><li>Nodeها از Stage خارج و توسط body clip نمی‌شوند.</li><li>لوگوها در عرض‌های میانی خوانا می‌مانند.</li><li>متن انگلیسی LTR و صفحه RTL درست است.</li><li>Focus/Touch وابسته به Hover نیست.</li><li>Desktop بعد از Mobile overrides تغییر نکرده است.</li></ul>
</details>
<details class="workshop-disclosure"><summary><span aria-level="3" role="heading">۷. منابع رسمی Elementor</span></summary>
<ul><li><a href="https://elementor.com/help/responsive-editing/">Responsive editing — V4</a></li><li><a href="https://elementor.com/help/responsive-design-using-containers/">Responsive design with containers</a></li><li><a href="https://elementor.com/help/mobile-editing/">Responsive editing for mobile and tablets</a></li><li><a href="https://elementor.com/help/container-layout-tab-settings/">Define container layout</a></li><li><a href="https://elementor.com/help/how-to-resolve-common-mobile-layout-issues-in-elementor/">Common mobile layout issues</a></li></ul>
</details>
<details class="workshop-disclosure responsive-build-test capstone-lab" id="tuya-responsive-build-test-capstone">
<summary><span aria-level="3" role="heading">۸. 📱 بساز و امتحان کن — Boss Lab کامل TUYA Responsive</span></summary>
<p class="status-chip"><strong>status:</strong> hybrid_observed_and_experimental</p>
<p><strong>هدف:</strong> نسخهٔ Desktop موجود را بدون Duplicate کردن ساختار به یک خروجی Mobile نزدیک به طرح مرجع تبدیل کن و علت هر override را ثبت کن.</p>
<section class="capstone-phase">
<h4>فاز A — Baseline و Evidence Capture</h4>
<ol>
<li>قبل از تغییر، Screenshot و ساختار Element Tree نسخهٔ Desktop را ذخیره کن.</li>
<li>Width، Direction، Gap، Order، Position و Overflow عناصر اصلی را ثبت کن.</li>
<li>در Tablet و Mobile فقط مشاهده کن؛ هنوز مقدارها را تغییر نده.</li>
</ol>
</section>
<section class="capstone-phase">
<h4>فاز B — تبدیل ساختار بدون نسخهٔ تکراری</h4>
<ol>
<li>Main را در Mobile از Row به Column تبدیل کن.</li>
<li>Visual، Copy و Logo Strip را با DOM منطقی یا Custom Order مستند مرتب کن.</li>
<li>Copy و Logo Strip را در Flow نگه دار؛ Absolute فقط داخل Visual Stage.</li>
</ol>
</section>
<section class="capstone-phase">
<h4>فاز C — Sizing و Media</h4>
<ol>
<li>عرض Shell/Main، اندازهٔ Stage و Width/Basis فرزندان را بازبینی کن.</li>
<li>ارتفاع 40vh را با auto/min-height مقایسه کن؛ نتیجه را از روی محتوا انتخاب کن.</li>
<li>Crop تصویر، Core، Nodeها، Typography و Logo Strip را در Mobile تنظیم کن.</li>
</ol>
</section>
<section class="capstone-phase exercise-break">
<h4>فاز D — پنج خرابی عمدی</h4>
<ol>
<li>Full Width + margin افقی؛</li>
<li>No Wrap + لوگوهای عریض؛</li>
<li>Height ثابت + متن بلند؛</li>
<li>Absolute child بدون Relative parent؛</li>
<li>Reset مقدار Mobile و بازگشت inheritance.</li>
</ol>
<p>هر بار symptom، Computed Style، علت و راه‌حل را جدا ثبت کن.</p>
</section>
<section class="capstone-phase">
<h4>فاز E — تست بین breakpointها و Frontend</h4>
<ol>
<li>viewport را تدریجی تغییر بده؛ فقط به سه preset دستگاه تکیه نکن.</li>
<li>هر شکست را قبل از ساخت breakpoint جدید با Flex/Width/Wrap حل کن.</li>
<li>نسخهٔ frontend را با Editor مقایسه و CSS/Network/overflow را بررسی کن.</li>
</ol>
</section>
<fieldset class="responsive-exercise-log capstone-log">
<legend>گیت قبولی Boss Lab</legend>
<label for="tuya-capstone-structure"><input data-persist="" id="tuya-capstone-structure" name="tuya-capstone-structure" type="checkbox"/> فقط یک ساختار اصلی Desktop/Mobile دارم.</label>
<label for="tuya-capstone-overflow"><input data-persist="" id="tuya-capstone-overflow" name="tuya-capstone-overflow" type="checkbox"/> در عرض‌های آزموده‌شده اسکرول افقی ناخواسته ندارم.</label>
<label for="tuya-capstone-inheritance"><input data-persist="" id="tuya-capstone-inheritance" name="tuya-capstone-inheritance" type="checkbox"/> منبع هر override یا مقدار inherited را می‌دانم.</label>
<label for="tuya-capstone-flow"><input data-persist="" id="tuya-capstone-flow" name="tuya-capstone-flow" type="checkbox"/> Copy و Logo Strip در Flow و Nodeها داخل Stage کنترل شده‌اند.</label>
<label for="tuya-capstone-front"><input data-persist="" id="tuya-capstone-front" name="tuya-capstone-front" type="checkbox"/> frontend واقعی و عرض‌های بین breakpointها را تست کردم.</label>
<label class="exercise-note-label" for="tuya-capstone-note">مهم‌ترین یافتهٔ من
      <input data-persist="" id="tuya-capstone-note" name="tuya-capstone-note" placeholder="مثلاً: تغییر Direction کافی نبود و Width فرزندان هم باید override می‌شد." type="text"/>
</label>
</fieldset>
<p class="evidence-line"><strong>مرز شواهد:</strong> ترکیب Mobile از تصویر مرجع مشاهده شده است؛ رفتار Tablet، breakpoint دقیق و مقادیر نهایی باید با طراح و اجرای واقعی تأیید شوند.</p>
</details></article>
