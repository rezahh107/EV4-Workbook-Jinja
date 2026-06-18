<article class="appendix card-surface" id="appendix-v23-roles-evidence">
<h2 class="former-h1">نقش‌ها و سطح دسترسی در Elementor V4 — آنچه می‌دانیم و آنچه نباید حدس بزنیم</h2>
<section class="appendix-body">
<p>سطح دسترسی بخشی از مدل طراحی است: ممکن است یک کاربر Style را ببیند، اما اجازهٔ ساخت یا مدیریت دارایی سراسری را نداشته باشد. این بخش فقط ادعاهایی را قطعی می‌داند که در مستندات رسمی Elementor صریح‌اند.</p>
<div aria-label="جدول شواهد نقش‌ها و سطح دسترسی" class="table-wrap" role="region" tabindex="0"><table class="data-table educational-table edu-table">
<caption>مرز شواهد رسمی برای نقش‌ها</caption><thead><tr><th scope="col">حوزه</th><th scope="col">نتیجهٔ قابل اتکا</th><th scope="col">وضعیت شواهد</th></tr></thead><tbody>
<tr><th scope="row">Classes</th><td>قابلیت‌های Class بر اساس نقش محدود می‌شوند. Admin به قابلیت‌های Class دسترسی کامل دارد؛ Editor می‌تواند از امکانات Style استفاده کند اما نمی‌تواند Class جدید بسازد. عملیات Class Manager، ساخت، حذف، ویرایش، تغییر نام، مرتب‌سازی و اعمال/حذف Class در ماتریس رسمی نقش‌ها بررسی می‌شوند.</td><td><code class="inline-code" dir="ltr">validated_from_official_help</code></td></tr>
<tr><th scope="row">Components</th><td>ساخت و ویرایش Component به دسترسی Admin-level و Elementor Pro نیاز دارد و Component فقط با Atomic Elementها ساخته می‌شود.</td><td><code class="inline-code" dir="ltr">validated_from_official_help</code></td></tr>
<tr><th scope="row">Variables</th><td>مستندات بررسی‌شده روش ساخت، ویرایش و استفاده از Variable را توضیح می‌دهند، اما ماتریس کامل Role × Variable operation در شواهد این بسته تثبیت نشده است.</td><td><code class="inline-code" dir="ltr">insufficient_evidence</code></td></tr>
</tbody></table></div>
<h3>Workflow امن برای تیم</h3><ol><li>قبل از آموزش یا تحویل پروژه، نقش واقعی کاربر را در همان سایت بررسی کن.</li><li>برای مدیریت Design System، دسترسی Class Manager و Component را جداگانه آزمایش کن.</li><li>برای Variables از حدس‌زدن مجوزها خودداری کن؛ نسخه، نقش، افزونه‌ها و نتیجهٔ مشاهده‌شده را ثبت کن.</li><li>اگر Custom Role یا Role Manager فعال است، نتیجهٔ همان محیط بر توضیح عمومی اولویت دارد.</li></ol>
<p class="golden-rule"><strong>قانون طلایی:</strong> وجود یک کنترل در آموزش به معنی دسترسی همهٔ نقش‌ها نیست؛ مجوز را در محیط واقعی اثبات کن.</p>
</section></article>
