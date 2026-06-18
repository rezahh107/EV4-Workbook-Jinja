# Elementor V4 Clear Mind Course — نسخهٔ ۱۴.۱ Premium UX

## شعار

> یک مسیر آموزشی واقعاً مناسب برای ذهن گیج و مبتدی و تبدیل آن ذهن به یک ذهن شفاف، واضح و ساختارمند.

## ماهیت نسخهٔ ۱۳

نسخهٔ ۱۳ ساختار و محتوای نسخهٔ ۱۲ را حفظ می‌کند و بر چهار موضوع تمرکز دارد:

<pre class="edis-rtl-text-block" lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important; overflow-x:auto; tab-size:4;"><code lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important;">
خودسنجی عمومی
    ↓
آناتومی پاسخ خوب برای همان درس

زمان یکسان
    ↓
بازهٔ واقع‌بینانه + سنگینی + نوع فعالیت

تمرین تکراری
    ↓
یک نسخهٔ اصلی + فهرست ارجاع

احساس فهم
    ↓
اعتماد همراه با شاهد
</code></pre>
## Pilot Edition

زمان‌های درس در این نسخه پیشنهادی‌اند. برای نسخهٔ بعد باید رفتار یک هنرجوی واقعی ثبت شود:

- زمان واقعی؛
- نقطهٔ مکث؛
- پرسش تکراری؛
- Control پیدا‌نشده؛
- خطای Exit Ticket؛
- استفاده از کارت نجات؛
- تفاوت اعتماد قبل/بعد با شواهد واقعی.

## فایل‌های اصلی

- `Elementor_V4_Clear_Mind_Course_v13_FA.md`
- `COURSE_MAP_FA.md`
- `LESSON_TIME_AND_LOAD_MAP_FA.md`
- `MASTERY_CRITERIA_TRACKER_FA.md`
- `CONFIDENCE_AND_TIME_TRACKER_FA.md`
- `MY_ELEMENTOR_ERROR_LOG_FA.md`
- `PILOT_GUIDE_FA.md`
- `PILOT_OBSERVATION_LOG_FA.md`
- `GLOSSARY_AND_INDEX_FA.md`
- `CASE_STUDIES_FA.md`
- `TEACHER_DESIGN_NOTES_FA.md`
- `SOURCES_AND_VIDEOS_FA.md`

## معیار عبور

زمان معیار عبور نیست. برای ادامهٔ مسیر:

<pre class="edis-rtl-text-block" lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important; overflow-x:auto; tab-size:4;"><code lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important;">
سطح ۱ — فهم
سطح ۲ — اجرا
</code></pre>
باید کامل شوند. سطح ۳ — انتقال، در ایستگاه‌ها و مثال‌های تازه تثبیت می‌شود.

## اصلاح RTL در نسخهٔ ۱۳.۱

نسخهٔ ۱۳.۱ یک Patch سازگاری است. بلوک‌های فارسی و ASCII آموزشی دیگر با Code Fence معمولی رندر نمی‌شوند؛ جهت و تراز آن‌ها با HTML و CSS صریح قفل شده است.

برای مشاهدهٔ پایدارتر، فایل HTML مستقل را باز کنید:

`Elementor_V4_Clear_Mind_Course_v13_1_RTL_Hardened_FA.html`

فایل‌های کد واقعی مانند CSS و JSON همچنان چپ‌به‌راست‌اند.


## اصلاح آموزشی نسخهٔ ۱۳.۲

این نسخه برای بخش‌هایی که هنرجو باید **ساختار، Flow، Overlap یا شکست طراحی** را ببیند، داربست بصری ASCII اضافه می‌کند.

مهم‌ترین اصلاح در درس ۱ انجام شده است:

- نقشهٔ دیداری Structure / Content / Overlap / Decoration؛
- Flow در برابر Overlap؛
- تلهٔ تبدیل Screenshot به مختصات؛
- پیش‌بینی شکست در متن طولانی و Mobile؛
- Tree ذهنی درست قبل از ادامه.

فایل راهنما:

`VISUAL_ASCII_SCAFFOLD_INDEX_FA.md`


## نسخهٔ ۱۳.۳ — هماهنگی HTML با PersianNew

در این نسخه، HTML Viewer با فایل CSS زیر هماهنگ شده است:

`PersianNew_v12_4_HTML_Viewer.css`

تغییرهای اصلی:

- محتوای HTML داخل `<main id="write">` قرار گرفت تا با Selectorهای PersianNew هماهنگ شود؛
- صفحه، تیترها، جدول‌ها، لیست‌ها، Blockquote و متن‌ها RTL و راست‌چین هستند؛
- بلوک‌های فارسی آموزشی با `edis-rtl-text-block` راست‌به‌چپ قفل شده‌اند؛
- بلوک‌های واقعی CSS/HTML/JSON چپ‌به‌راست باقی مانده‌اند؛
- مسیر فونت‌ها با `./fonts/...` هماهنگ است؛
- فونت‌ها داخل بسته قرار داده نشده‌اند. راهنمای پوشهٔ `fonts` را ببین.

فایل پیشنهادی برای مطالعه:

`Elementor_V4_Clear_Mind_Course_v13_3_PersianNew_HTML_FA.html`


## نسخهٔ ۱۳.۴ — Visual Cards و فونت UI برای بلوک‌های فارسی

این نسخه مشکل خوانایی بلوک‌های فارسی داخل محیط شبیه Code را اصلاح می‌کند:

- متن‌های آموزشی فارسی داخل `edis-rtl-text-block` با `var(--font-ui)` نمایش داده می‌شوند؛
- اگر فونت وزیر در پوشهٔ `fonts` باشد، همین بلوک‌ها با وزیر رندر می‌شوند؛
- کدهای واقعی CSS/HTML/JSON همچنان monospace و LTR هستند؛
- داربست‌های اصلی درس ۱ از ASCII Art خام به Visual Cardهای HTML تبدیل شدند؛
- Visual Cardها با Flex/Grid، Badge، Panel و Nodeهای واقعی بهتر مفهوم Flow/Overlap/Absolute را نشان می‌دهند.


## نسخهٔ ۱۴.۰ — HTML-first

در این نسخه، HTML خروجی جانبی نیست؛ فایل اصلی مطالعه است.

امکانات اصلی:

- چک‌لیست واقعی برای تمرین‌ها؛
- پنل شبیه Elementor برای General / Style / Classes / State؛
- کارت مقایسهٔ Flow و Absolute؛
- تبدیل بخشی از متن‌های فارسی کوتاه به کارت‌های آموزشی؛
- حفظ کد واقعی به‌صورت LTR و monospace؛
- استفاده از PersianNew CSS و `#write`.

فایل پیشنهادی برای مطالعه:

`Elementor_V4_Clear_Mind_Course_v14_HTML_First_FA.html`


## نسخهٔ ۱۴.۱ — Premium UX

نسخهٔ ۱۴.۰ امکانات HTML-first داشت، اما ظاهر آن بیش از حد ساده و روشن شده بود. نسخهٔ ۱۴.۱ همان امکانات را حفظ می‌کند و حس PersianNew/دارک/جزوهٔ حرفه‌ای را برمی‌گرداند.

فایل پیشنهادی برای مطالعه:

`Elementor_V4_Clear_Mind_Course_v14_1_Premium_UX_FA.html`

CSS جدید:

`PersianNew_v14_1_Premium_Reader.css`
