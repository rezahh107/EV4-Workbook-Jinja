# دفترچهٔ شخصی الگوی خطاهای Elementor

هدف این فایل سرزنش‌کردن اشتباه نیست؛ تبدیل اشتباه‌های تکراری به یک مسیر Debug شخصی است.

| تاریخ | درس/صفحه | نشانه | تصور اولیهٔ من | علت واقعی | شاهد | اولین بررسی دفعهٔ بعد | اصلاح و Regression Test |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## نمونه

| تاریخ | درس/صفحه | نشانه | تصور اولیهٔ من | علت واقعی | شاهد | اولین بررسی دفعهٔ بعد | اصلاح و Regression Test |
|---|---|---|---|---|---|---|---|
| نمونه | Class | Reusable Class اعمال نشد | Class خراب است | Local Class همان Property را Override کرده | Active Class و Style خط‌خورده | Local Class | Override حذف شد؛ سه Element دوباره تست شدند |
| نمونه | Mobile | اسکرول افقی | Elementor Bug دارد | Visual Width ثابت بود | Computed Width از Parent بیشتر بود | Width و Shrink | Width محدود شد؛ 320/375/768 تست شدند |
| نمونه | Layering | z-index اثر نکرد | عدد کم است | Parent یک Stacking Context جدا ساخته بود | Ancestor دارای Transform | Ancestorها | Context اصلاح شد؛ Modal و Header تست شدند |

## مرور هفتگی

<pre class="edis-rtl-text-block" lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important; overflow-x:auto; tab-size:4;"><code lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important;">
کدام خطا بیشتر تکرار شد؟
کدام اولین بررسی بیشترین زمان را نجات داد؟
کدام تصور اولیه معمولاً غلط بود؟
چه چیزی باید به کارت نجات شخصی من اضافه شود؟
</code></pre>