# سورس کامل جایگزینی ریپو — Elementor V4 Workbook v26

## وضعیت

`repo_replacement_source_candidate`

این بسته برای جایگزینی در ریپو آماده شده است. محتوای داخل پوشهٔ زیر را در ریشهٔ ریپو کپی کن:

```text
repo-root/
```

## فایل اصلی جایگزین

این فایل باید جایگزین فایل HTML فعلی Workbook شود:

```text
assets/TUYA_Standalone_Workbook_v32_0_0.html
```

در همین پوشه یک نسخهٔ نام‌دار هم هست:

```text
assets/TUYA_Standalone_Workbook_v32_0_0_lessons_1_21_release_candidate_v25.html
```

## محتوای همراه

```text
content/units/
reports/
REPO_REPLACEMENT_MANIFEST.json
README_REPLACE_IN_REPO_FA.md
```

## درس‌های بازنویسی‌شده

درس‌های ۱ تا ۲۱ در این بسته وجود دارند:

```text
content/units/031-lesson-1.md
content/units/033-lesson-2.md
content/units/034-lesson-3.md
content/units/035-lesson-4.md
content/units/037-lesson-5.md
content/units/038-lesson-6.md
content/units/039-lesson-7.md
content/units/040-lesson-8.md
content/units/041-lesson-9.md
content/units/043-lesson-10.md
content/units/044-lesson-11.md
content/units/046-lesson-12.md
content/units/047-lesson-13.md
content/units/048-lesson-14.md
content/units/050-lesson-15.md
content/units/052-lesson-16.md
content/units/053-lesson-17.md
content/units/054-lesson-18.md
content/units/063-lesson-19.md
content/units/064-lesson-20.md
content/units/066-lesson-21.md
```

## گزارش‌ها

گزارش‌های ۱ تا ۲۱ در مسیر زیر هستند:

```text
reports/
```

## نتیجهٔ کنترل ساختاری HTML اصلی

```json
{
  "lesson_articles_in_primary_html": 21,
  "nav_lesson_links_in_primary_html": 21,
  "duplicate_ids_in_primary_html": {},
  "missing_expected_units": [],
  "missing_expected_reports": []
}
```

## دستور جایگزینی پیشنهادی در ویندوز

1. از ریپوی فعلی backup یا branch جدید بگیر.
2. ZIP را extract کن.
3. محتوای `repo-root/` را روی ریشهٔ ریپو کپی کن.
4. فایل‌های هم‌نام را replace کن.
5. سپس اگر پروژه build script دارد، اجرا کن:

```bash
npm install
npm run build
npm run validate
```

اگر این پروژه فقط HTML مستقل است، فایل زیر را مستقیم در مرورگر باز کن:

```text
assets/TUYA_Standalone_Workbook_v32_0_0.html
```

## QA دستی لازم قبل از انتشار

- باز شدن Lesson 1 تا 21 از sidebar
- باز و بسته شدن details
- checkbox/radio با mouse و keyboard
- responsive در 320px و 390px
- Zoom 200%
- RTL/Bidi
- Keyboard focus path

## محدودیت

در این محیط project build/validate اجرا نشده، چون toolchain کامل پروژه در handoff موجود نبود. این بسته سورس کامل جایگزینی است، نه تضمین Production بدون QA دستی.
