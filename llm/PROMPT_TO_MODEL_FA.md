# متن ثابت برای تحویل Repository به مدل زبانی

ZIP ساخته‌شده با `python tools/create_llm_handoff.py` را به مدل بدهید و متن زیر را ارسال کنید:

```text
این ZIP سورس کامل و منبع حقیقت کتاب‌کار Elementor V4 است.

پیش از هر تغییر، فایل‌های زیر را به‌ترتیب کامل بخوان:
1. AGENTS.md
2. llm/model-contract.yaml
3. llm/TASK.md

فقط Task ثبت‌شده را اجرا کن. تنها مسیرهای فهرست‌شده در allowed_paths مجاز به تغییر هستند؛ برای تغییر هر مسیر حفاظت‌شده باید همان مسیر در protected_path_exceptions آمده باشد.

فایل‌های تولیدی dist/، release/ و handoff/ را دستی ویرایش نکن. تغییر را در سورس اعمال کن، سپس Gateهای قابل اجرا را واقعاً اجرا کن. تست اجرا‌نشده را موفق اعلام نکن. نبود Browser یا Dependency را BLOCKED_ENVIRONMENT گزارش کن.

در پایان:
- کل Repository اصلاح‌شده را به‌صورت ZIP بازگردان؛
- llm/RETURN_REPORT.md را ایجاد یا تکمیل کن؛
- فایل‌های تغییرکرده، دلایل، فرمان‌ها، Exit Codeها و موارد اجرا‌نشده را دقیق ثبت کن؛
- هیچ Refactor یا پیشنهاد خارج از Scope انجام نده.
```
