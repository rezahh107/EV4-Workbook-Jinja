# مدل آموزشی وزن المان‌ها — نسخه 19

status: teaching_model_not_runtime_measurement
version: 19.0.0

این مدل برای آموزش تصمیم طراحی در Elementor 4 ساخته شده است. وزن‌ها عدد قطعی نیستند و بدون Browser Runtime یا خروجی واقعی CSS/DOM نباید به‌عنوان حقیقت اندازه‌گیری‌شده گزارش شوند.

## ابعاد وزن

1. DOM Weight — تعداد node/wrapper و عمق nesting.
2. CSS Weight — تعداد rule، selector، state و responsive variant.
3. Asset Weight — تصویر، فونت، SVG، ویدئو، iframe و payload شبکه.
4. Runtime JS Weight — interaction، form behavior، tab state، video embed.
5. Layout Weight — reflow، overflow، viewport units، grid/flex complexity.
6. Paint/Composite Weight — shadow، blur، filter، transform و layered backgrounds.
7. Maintenance Weight — سختی تغییر آینده، تکرار Local Class، نبود Variable/Global Class/Component.

## سیاست حقیقت

- برچسب `teaching_model` برای رتبه‌بندی نسبی استفاده شود.
- برچسب `observed_runtime` فقط پس از اندازه‌گیری واقعی DOM/CSS/Asset/JS مجاز است.
- ForLesson فعلی فقط static export analysis دارد، نه runtime measurement.
