# Case Studyهای واقعی Home2 و Solutions — نسخهٔ ۱۲

## نحوهٔ خواندن

هر پرونده دو برچسب دارد:

<pre class="edis-rtl-text-block" lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important; overflow-x:auto; tab-size:4;"><code lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important;">
Action Label     دانش‌آموز چه کاری انجام دهد؟
Evidence State   چه چیزی واقعاً ثابت شده است؟
</code></pre>
---

## CASE-HOME2-GRID-001

**هدف:** ⚖️ دو روش را مقایسه کن  
**وضعیت:** `legacy_or_hybrid`  
**منبع:** Home2 / element `750d8565`

### exported

- Legacy Grid Container؛
- Width برابر 100vw؛
- Min Height برابر 100vh؛
- دو ستون Grid؛
- وجود Elementهای V4 در همان Subtree.

### کار دانش‌آموز

Grid و Flexbox V4 را در Staging مقایسه کن. Viewport units را در چند عرض و Mobile Browser بررسی کن.

### نتیجهٔ مجاز

```text
status: insufficient_evidence
```

---

## CASE-HOME2-DOM-001

**هدف:** 🔍 عیب‌یابی کن  
**وضعیت:** `improvement_candidate`

چند Element خالی در Export دیده شده‌اند.

### کار دانش‌آموز

هر Element را جداگانه غیرفعال کن و نقش Layout، Scope یا Placeholder آن را بررسی کن.

### ممنوع

حذف گروهی و اعلام «DOM بد» بدون Runtime.

---

## CASE-HOME2-REUSE-001

**هدف:** 🔧 بازسازی کن  
**وضعیت:** `improvement_candidate`

Style signatureهای تکراری برای SVG، Heading و Paragraph دیده شده‌اند.

### کار دانش‌آموز

یک گروه را به Reusable Class یا Component تبدیل و تعداد نقاط ویرایش را مقایسه کن.

---

## CASE-SOL-ABS-001

**هدف:** 🔧 بازسازی کن  
**وضعیت:** `improvement_candidate`  
**منبع:** Solutions / element `768b396f`

### exported

- هشت Card مشابه؛
- Parent Relative؛
- Icon، Heading و Paragraph Absolute؛
- Offsetهای ثابت.

### Refactor پیشنهادی

<pre class="edis-rtl-text-block" lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important; overflow-x:auto; tab-size:4;"><code lang="fa" dir="rtl" style="display:block !important; direction:rtl !important; text-align:right !important; unicode-bidi:plaintext !important; writing-mode:horizontal-tb !important; white-space:pre-wrap !important;">
Icon: Overlay یا Flow برحسب هدف
Heading: Normal Flow
Paragraph: Normal Flow
Card: Flexbox Column
</code></pre>
خرابی Runtime هنوز اثبات نشده است.

---

## CASE-SOL-IMAGE-001

**هدف:** ⚖️ دو روش را مقایسه کن  
**وضعیت:** `context_dependent`

چهار Image Card دارای Cover، ارتفاع 15vw و Min/Max Height هستند.

### کار دانش‌آموز

روش فعلی را با Media Frame مبتنی بر Aspect Ratio در Desktop، Tablet و Mobile مقایسه کن.

---

## CASE-SOL-HYBRID-001

**هدف:** 👁 مشاهده و سپس 🔧 بازسازی کنترل‌شده  
**وضعیت:** `legacy_or_hybrid`

Subtree شامل Elementهای V4 و Widgetهای Legacy است.

### کار دانش‌آموز

فقط یک زیرگروه کم‌خطر را با نردبان مهاجرت به V4 بازسازی کن.

---

## CASE-SOL-REUSE-001

**هدف:** 🔧 بازسازی کن  
**وضعیت:** `improvement_candidate`

امضاهای تکراری برای Button، Card، Icon، Heading و Paragraph دیده شده‌اند.

### کار دانش‌آموز

```text
shared value     → Variable if supported
shared style     → Reusable Class
shared structure → Component
unique change    → Local Class
```

---

## CASE-CONTENT-BR-001

**هدف:** 🔍 عیب‌یابی کن  
**وضعیت:** `context_dependent`

چند Heading و Paragraph دارای Break صریح هستند.

### کار دانش‌آموز

Break هنری Heading و Break شکنندهٔ Paragraph را با متن طولانی، ترجمه و Mobile مقایسه کن.
