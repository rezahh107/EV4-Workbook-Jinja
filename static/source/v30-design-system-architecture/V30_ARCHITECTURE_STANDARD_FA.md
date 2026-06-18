# استاندارد معماری v30

## اصل مرکزی

System First, Page Second به‌معنای حذف workflow اکتشافی نیست. دو مسیر مجازند: planned و discovery.

## مرزهای حقیقت

- انواع رسمی Variable: Color، Font، Size.
- spacing token و typography scale: `derived_educational_model` یا `proposed_strategy`.
- dependency graph با CSS cascade یکی نیست.
- Component nesting: `insufficient_evidence`.
- CSS-supported با Elementor-UI-exposed یکی نیست.

## نگاشت

Named values / Variables → declarations in Local or Global Classes → Atomic Elements and reusable structure → Components → Instances → Pages.

حل تعارض Style جداگانه است: Global Class hierarchy + selected State + Local Class + Custom CSS/browser cascade context → Computed Style.
