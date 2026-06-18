# قرارداد Responsive پروژه TUYA — نسخه 25.0

status: hybrid_observed_and_proposed
source_base: v24.0
mobile_reference: observed_design_reference
mobile_reference_dimensions: 881×2047
tablet_behavior: proposed_pending_designer_confirmation

## آنچه در طرح موبایل مشاهده می‌شود

- ساختار عمودی و تک‌ستونه است.
- Visual پیش از Copy نمایش داده شده است.
- لوگوها پس از متن قرار دارند.
- Visual یک Stage مستقل دارد و Nodeها پیرامون Core قرار گرفته‌اند.
- نوارهای تیرهٔ کناری بخشی از طراحی نیستند؛ پیکسل‌های بیرونی تصویر شفاف‌اند.

## آنچه از تصویر قابل اثبات نیست

- breakpoint دقیق؛
- واحدهای دقیق Width، Gap و Padding؛
- رفتار Tablet؛
- استفاده از DOM order یا Custom Order؛
- اندازه‌های نهایی production.

## قرارداد آموزشی

1. Desktop baseline در Elementor ساخته می‌شود.
2. پیش از تثبیت هر بخش، Tablet و Mobile بررسی می‌شوند.
3. Direction، Width/Height و Custom Order فقط در breakpoint لازم override می‌شوند.
4. نسخهٔ تکراری و مخفی Section ساخته نمی‌شود، مگر نیاز واقعی و مستند وجود داشته باشد.
5. Visual Stage تنها ناحیه‌ای است که Absolute Positioning در آن مجاز است.
6. ارتفاع Mobile محتوامحور است؛ مقدار 40vh دسکتاپ بدون بررسی به Mobile منتقل نمی‌شود.
7. تمام تصمیم‌های غیرقابل مشاهده در تصویر با وضعیت proposed یا insufficient_evidence ثبت می‌شوند.
