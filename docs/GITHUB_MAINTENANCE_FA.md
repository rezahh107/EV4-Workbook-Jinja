# راهنمای نگهداری Repository در GitHub

## مدل پیشنهادی

- Repository را در صورت اختصاصی‌بودن محتوا `Private` بسازید.
- شاخهٔ اصلی `main` فقط نسخهٔ پذیرفته‌شده و پاس‌شده را نگه دارد.
- هر تغییر در شاخهٔ جدا انجام شود و با Pull Request وارد `main` شود.
- `dist/`, `release/` و `handoff/` را Commit نکنید؛ GitHub Actions آن‌ها را می‌سازد.

## ایجاد Repository با GitHub Desktop

1. ZIP سورس را Extract کنید.
2. GitHub Desktop را باز کنید.
3. `File > Add local repository` را انتخاب کنید.
4. پوشهٔ ریشه را انتخاب کنید.
5. اگر Repository Git نیست، `Create a repository` را بزنید.
6. نام پیشنهادی: `elementor-v4-offline-workbook`.
7. اولین Commit را با پیام `chore: initialize LLM-ready workbook source` ایجاد کنید.
8. `Publish repository` را بزنید و Private/Public بودن را انتخاب کنید.

## ایجاد با خط فرمان

```bash
git init
git branch -M main
git add .
git commit -m "chore: initialize LLM-ready workbook source"
git remote add origin https://github.com/USERNAME/elementor-v4-offline-workbook.git
git push -u origin main
```

## چرخهٔ هر تغییر

```bash
git switch main
git pull --ff-only
git switch -c content/lesson-14-responsive
```

Task را در `llm/TASK.md` ثبت کنید، بستهٔ مدل را بسازید و پس از دریافت نتیجه:

```bash
python tools/verify_returned_zip.py returned.zip --browser
git status
git diff --stat
git diff
git add .
git commit -m "content: improve responsive lesson"
git push -u origin content/lesson-14-responsive
```

سپس در GitHub Pull Request بسازید. فقط پس از سبزشدن Checkهای CI Merge کنید.

## Ruleset پیشنهادی برای `main`

در `Settings > Rules > Rulesets` یک Branch Ruleset برای `main` بسازید:

- Block force pushes
- Block deletions
- Require a pull request before merging
- Require status checks to pass
- Checkهای `source-contract` و `browser-smoke` را Required کنید
- Require conversation resolution
- برای Repository تک‌نفره، Approval اجباری را صفر نگه دارید؛ برای تیم حداقل یک Approval تعیین کنید

## نسخه و Release

- تغییر محتوایی کوچک: Patch، مثل `v32.0.1`
- فصل یا قابلیت جدید سازگار: Minor، مثل `v32.1.0`
- تغییر ناسازگار در قرارداد یا ساختار: Major

پس از Merge و کنترل نهایی:

```bash
git switch main
git pull --ff-only
git tag -a v32.0.1 -m "Elementor workbook v32.0.1"
git push origin v32.0.1
```

Workflow انتشار، Build و آزمون را دوباره اجرا و Artifact را در GitHub Release قرار می‌دهد.

## فایل‌های بزرگ

در وضعیت فعلی بزرگ‌ترین فایل مخزن چند مگابایت است و Git LFS لازم نیست. اگر در آینده ویدئو، PSD، ZIP یا Media بسیار بزرگ اضافه شد، پیش از Commit از Git LFS استفاده و `.gitattributes` تولیدشده را Commit کنید.

## سیاست Commit

نمونه پیام‌ها:

```text
content: clarify flex basis lesson
fix: preserve RTL table overflow
build: tighten duplicate id validation
docs: update LLM handoff guide
test: add regression for conceptual references
```

هر Commit باید یک هدف روشن داشته باشد. خروجی Build، Cache، Virtual Environment و فایل‌های موقت مدل را Commit نکنید.

## پشتیبان‌گیری

GitHub جایگزین کامل Backup نیست. حداقل این سه نسخه را نگه دارید:

- Clone محلی فعال؛
- Repository GitHub؛
- Artifact منتشرشدهٔ هر Release همراه SHA-256.
