---
task_status: draft
task_id: CONTENT-YYYY-MM-DD-01
change_type: content
workbook_version_policy: keep
allowed_paths:
  - content/units/031-lesson-1.md
  - CHANGELOG_FA.md
protected_path_exceptions: []
required_checks:
  - validate
  - build
  - unit_tests
  - browser_if_available
---

# هدف تغییر

[دقیقاً بنویس چه چیزی باید اصلاح، حذف یا اضافه شود.]

# ورودی‌ها و شواهد

- فایل یا متن مرجع:
- بخش‌های هدف:
- ادعاهایی که باید حفظ شوند:
- مواردی که فقط پیشنهادند و نباید حقیقت قطعی معرفی شوند:

# معیار پذیرش

- [ ] محتوای خواسته‌شده کامل اعمال شده است.
- [ ] شناسه‌ها و رفتارهای خارج از Scope تغییر نکرده‌اند.
- [ ] `python validate.py` پاس شده است.
- [ ] `python build.py` پاس شده است.
- [ ] آزمون‌های لازم اجرا شده‌اند.
- [ ] `llm/RETURN_REPORT.md` نتیجهٔ واقعی را ثبت کرده است.

# ممنوعیت‌های مخصوص این Task

- Refactor نامرتبط انجام نشود.
- فایل تولیدی `dist/` دستی ویرایش نشود.
- ادعای Elementor بدون منبع یا شواهد ساخته نشود.
