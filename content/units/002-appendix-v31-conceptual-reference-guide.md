<article class="appendix card-surface conceptual-reference-guide-v31" id="appendix-v31-conceptual-reference-guide"><h2>راهنمای مرجع مفهومی کامل v31 و مرز اطمینان ادعاها</h2><h3>روش استفاده از این متن</h3><p>این فایل فقط <strong>محتوای مرجع مفهومی</strong> را ارائه می‌کند و هنوز در HTML جزوه ادغام نشده است. کارت‌های آموزشی، خلاصه‌ها، آزمون‌ها، Step-throughها و اجزای تعاملی بستهٔ اصلی عمداً در این نسخه بازتولید نشده‌اند؛ چون هدف این مرحله، کامل‌کردن خودِ توضیح مفاهیم است.</p><p>در این متن سه نوع گزاره از هم جدا نگه داشته شده‌اند:</p><ol>
<li><strong>رفتار CSS و مرورگر:</strong> بر پایهٔ استانداردهای CSSWG/W3C و مستندات آموزشی MDN.</li>
<li><strong>رفتار و رابط Elementor V4:</strong> بر پایهٔ Help Center رسمی Elementor، مطابق صفحات بررسی‌شده تا ۱۷ ژوئن ۲۰۲۶.</li>
<li><strong>تشبیه‌ها و قوانین طلایی:</strong> توضیح آموزشیِ مشتق‌شده‌اند؛ منبع استاندارد نیستند، اما برای ساخت تصویر ذهنی طراحی شده‌اند.</li>
</ol><hr/><h3>پیوست: وضعیت ادعاهای پیشرفته و مرز اطمینان</h3><p>این پیوست برای جلوگیری از تبدیل الگوهای پیشنهادی به «حقیقت قطعی Elementor» است.</p><div aria-label="جدول آموزشی مرجع مفهومی" class="table-scroll concept-table-scroll" role="region" tabindex="0"><table class="data-table educational-table concept-reference-table"><caption>جدول آموزشی مرجع مفهومی</caption>
<thead>
<tr>
<th>مفهوم</th>
<th>وضعیت در این سند</th>
<th>توضیح</th>
</tr>
</thead>
<tbody>
<tr>
<td>Local Class برای هر Element V4</td>
<td>مستند رسمی فعلی</td>
<td>Help Center فعلی این رفتار را بیان می‌کند.</td>
</tr>
<tr>
<td>Priority Local بر Global</td>
<td>مستند رسمی فعلی</td>
<td>Local بالاترین اولویت Elementor است.</td>
</tr>
<tr>
<td>Drag &amp; Drop ترتیب Global Class</td>
<td>مستند رسمی فعلی</td>
<td>در Class Manager؛ Filter می‌تواند Drag را محدود کند.</td>
</tr>
<tr>
<td>Master/Instance/Exposed Property/Detach</td>
<td>مستند رسمی فعلی</td>
<td>دامنه دقیق Propertyهای قابل Expose به UI نسخه وابسته است.</td>
</tr>
<tr>
<td>Slot در Component</td>
<td><code class="inline-code" dir="ltr">insufficient_evidence</code></td>
<td>مفهوم عمومی است؛ پشتیبانی Native رسمی اثبات نشده.</td>
</tr>
<tr>
<td>Variant Class روی Instance</td>
<td>الگوی پیشنهادی نیازمند Fixture</td>
<td>رفتار حفظ Class روی Instance باید آزمایش شود.</td>
</tr>
<tr>
<td>Variable Alias Chain</td>
<td><code class="inline-code" dir="ltr">insufficient_evidence</code></td>
<td>نیازمند Export واقعی و سند رسمی.</td>
</tr>
<tr>
<td>Container Query Native در پنل V4</td>
<td>اثبات‌نشده</td>
<td>به‌عنوان Custom CSS پیشرفته آموزش داده شده.</td>
</tr>
<tr>
<td>Form Submitting Appearance</td>
<td>اثبات‌نشده</td>
<td>Normal/Success/Error رسمی‌اند؛ Pending نیاز UX است.</td>
</tr>
<tr>
<td>Dynamic State Classes فرم</td>
<td>اثبات‌نشده</td>
<td>نباید بدون Fixture ادعا شود.</td>
</tr>
<tr>
<td>V4 همیشه سریع‌تر از V3</td>
<td>رد شده به‌عنوان قانون</td>
<td>فقط Benchmark واقعی تصمیم می‌دهد.</td>
</tr>
<tr>
<td>هر Wrapper هزینه ثابت دارد</td>
<td>رد شده</td>
<td>هزینه وابسته به Context و Runtime است.</td>
</tr>
<tr>
<td>عدد جهانی مناسب DOM</td>
<td>رد شده</td>
<td>Thresholdهای ابزار تشخیصی، قانون طراحی نیستند.</td>
</tr>
</tbody>
</table></div><hr/><h3>فهرست منابع رسمی پایه</h3><p>منابع زیر ستون فقرات فنی این نسخه‌اند. تاریخ بررسی محتوای نسخه: ۱۷ ژوئن ۲۰۲۶.</p><h3>Elementor</h3><ul>
<li><a href="https://elementor.com/help/get-started-with-the-elementor-editor-v4/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/get-started-with-the-elementor-editor-v4/</a></li>
<li><a href="https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4/</a></li>
<li><a href="https://elementor.com/help/classes-in-elementor-2/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/classes-in-elementor-2/</a></li>
<li><a href="https://elementor.com/help/the-elementor-editor-class-manager/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/the-elementor-editor-class-manager/</a></li>
<li><a href="https://elementor.com/help/prioritize-conflicting-styles/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/prioritize-conflicting-styles/</a></li>
<li><a href="https://elementor.com/help/variables/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/variables/</a></li>
<li><a href="https://elementor.com/help/variables-manager/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/variables-manager/</a></li>
<li><a href="https://elementor.com/help/components-2/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/components-2/</a></li>
<li><a href="https://elementor.com/help/interactions/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/interactions/</a></li>
<li><a href="https://elementor.com/help/atomic-form-element/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/atomic-form-element/</a></li>
<li><a href="https://elementor.com/help/dynamic-tags-in-v4/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/dynamic-tags-in-v4/</a></li>
<li><a href="https://elementor.com/help/add-custom-css-to-an-element/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/add-custom-css-to-an-element/</a></li>
<li><a href="https://elementor.com/help/add-and-delete-attributes/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/add-and-delete-attributes/</a></li>
<li><a href="https://elementor.com/help/how-to-import-and-export-design-systems/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/how-to-import-and-export-design-systems/</a></li>
<li><a href="https://elementor.com/help/how-to-sync-variables-and-global-elements/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/how-to-sync-variables-and-global-elements/</a></li>
<li><a href="https://elementor.com/help/mobile-editing/" rel="noopener noreferrer" target="_blank">https://elementor.com/help/mobile-editing/</a></li>
<li><a href="https://developers.elementor.com/elementor-editor-4-0-developers-update/" rel="noopener noreferrer" target="_blank">https://developers.elementor.com/elementor-editor-4-0-developers-update/</a></li>
</ul><h3>CSS و مرورگر</h3><ul>
<li><a href="https://www.w3.org/TR/css-flexbox-1/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-flexbox-1/</a></li>
<li><a href="https://www.w3.org/TR/css-grid-1/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-grid-1/</a></li>
<li><a href="https://www.w3.org/TR/css-grid-2/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-grid-2/</a></li>
<li><a href="https://www.w3.org/TR/css-position-3/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-position-3/</a></li>
<li><a href="https://www.w3.org/TR/css-logical-1/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-logical-1/</a></li>
<li><a href="https://www.w3.org/TR/css-contain-3/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-contain-3/</a></li>
<li><a href="https://www.w3.org/TR/css-values-4/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-values-4/</a></li>
<li><a href="https://www.w3.org/TR/css-text-4/" rel="noopener noreferrer" target="_blank">https://www.w3.org/TR/css-text-4/</a></li>
<li><a href="https://developer.chrome.com/docs/devtools/css/reference" rel="noopener noreferrer" target="_blank">https://developer.chrome.com/docs/devtools/css/reference</a></li>
<li><a href="https://developer.chrome.com/docs/devtools/elements/badges" rel="noopener noreferrer" target="_blank">https://developer.chrome.com/docs/devtools/elements/badges</a></li>
<li><a href="https://developer.chrome.com/docs/devtools/layers" rel="noopener noreferrer" target="_blank">https://developer.chrome.com/docs/devtools/layers</a></li>
<li><a href="https://developer.chrome.com/docs/devtools/performance/reference" rel="noopener noreferrer" target="_blank">https://developer.chrome.com/docs/devtools/performance/reference</a></li>
</ul><h3>Performance و Accessibility</h3><ul>
<li><a href="https://web.dev/articles/vitals" rel="noopener noreferrer" target="_blank">https://web.dev/articles/vitals</a></li>
<li><a href="https://web.dev/articles/optimize-lcp" rel="noopener noreferrer" target="_blank">https://web.dev/articles/optimize-lcp</a></li>
<li><a href="https://web.dev/articles/inp" rel="noopener noreferrer" target="_blank">https://web.dev/articles/inp</a></li>
<li><a href="https://web.dev/articles/optimize-cls" rel="noopener noreferrer" target="_blank">https://web.dev/articles/optimize-cls</a></li>
<li><a href="https://www.w3.org/WAI/" rel="noopener noreferrer" target="_blank">https://www.w3.org/WAI/</a></li>
</ul><hr/></article>
