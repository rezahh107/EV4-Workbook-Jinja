# طرح معماری محتوای v30

## محل فصل جدید

فصل `architecture-primer-v30` پس از درس ۱ و پیش از درس ۲ قرار گیرد. این بخش درس شماره‌دار جدید محسوب نشود تا قرارداد ۲۱ درس اصلی حفظ شود.

## نمودار ۱ — وابستگی Design System

```text
Named values / Variables
        ↓
Declarations in Local or Global Classes
        ↓
Atomic Elements and reusable structure
        ↓
Components (Master)
        ↓
Instances
        ↓
Pages / Website
```

این نمودار dependency است، نه cascade.

## نمودار ۲ — حل تعارض Style

```text
Global Class hierarchy
+ selected State
+ Local Class
+ Custom CSS / selector context
+ browser CSS cascade
        ↓
Computed Style
```

## workflow برنامه‌ریزی‌شده

```text
Design decisions
→ Variables
→ Global Classes
→ Components
→ Pages
```

## workflow اکتشافی

```text
Element
→ Local styling
→ اثبات تکرار
→ Convert to Global Class
→ استخراج مقادیر تکراری به Variables
→ Component فقط هنگام تکرار ساختار
```

هیچ‌یک به‌عنوان تنها workflow صحیح معرفی نشوند.

## مدل Unit Strategy

```text
Intent
→ Property
→ value type
→ reference
→ UI-supported unit/value
→ direct literal or reusable Variable
→ Local/Global Class placement
→ optional Component consumption
→ Responsive/Computed verification
```

## Evidence labels

- `verified_by_official_elementor_help`
- `verified_by_elementor_developer_docs`
- `verified_by_css_spec`
- `verified_by_real_fixture`
- `verified_by_controlled_experiment`
- `derived_educational_model`
- `proposed_strategy`
- `insufficient_evidence`
