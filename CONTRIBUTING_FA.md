# مشارکت و تغییر کنترل‌شده

1. تغییر را در Issue یا `llm/TASK.md` دقیق تعریف کنید.
2. شاخه‌ای با پیشوند `content/`, `fix/`, `build/`, `docs/` یا `test/` بسازید.
3. منبع را تغییر دهید؛ فایل‌های `dist/` را ویرایش نکنید.
4. `python tools/check_all.py --browser` را اجرا کنید.
5. Changelog و گزارش مدل را به‌روز کنید.
6. Pull Request بسازید و تا پاس‌شدن Checkها Merge نکنید.

تغییر Schema، Baseline یا Builder باید جدا از تغییر محتوایی معمولی باشد و دلیل نسخه‌گذاری روشن داشته باشد.
