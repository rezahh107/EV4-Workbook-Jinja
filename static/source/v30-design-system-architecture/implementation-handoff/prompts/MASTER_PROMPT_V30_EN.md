# MASTER PROMPT — Build Elementor V4 Offline Interactive Workbook v30

## Role

Act as a Senior Offline HTML Workbook Engineer, Elementor V4 Evidence-Based Instructional Designer, CSS Architecture Educator, Accessibility-Minded UX Reviewer, and Deterministic Patch Compiler.

## Source of truth

Use the attached `Elementor_V4_Offline_Interactive_Workbook_v29_0_settings_values_units_step_through.zip` as the only active source base.

Do not start from v28 or any earlier package.
Do not rebuild the workbook from memory.
Preserve the current project structure, lessons, stations, assets, source archives, progressive disclosure, Step-Through engine, responsive labs, validation artifacts, and offline-only behavior.

Read all files in this handoff package before implementation, especially:

- `analysis/VERIFIED_ANALYSIS_FA.md`
- `scope/V30_CHANGE_LIST_FA.md`
- `scope/V30_ARCHITECTURE_BLUEPRINT_FA.md`
- `scope/V30_CONTENT_REQUIREMENTS_FA.md`
- `scope/V30_VISUAL_AND_INTERACTIVE_REQUIREMENTS_FA.md`
- `scope/V30_VALIDATION_CONTRACT_FA.md`
- `registries/official_sources_v30.json`

## Primary objective

Produce the next complete workbook version, not a patch. The new version must connect CSS values and units to Elementor V4 design-system decisions and significantly deepen Variables, Classes, Components, Dynamic Data, and Interactions without reducing or deleting the existing Layout, Responsive, TUYA, Step-Through, or debugging content.

Recommended output filename:

`Elementor_V4_Offline_Interactive_Workbook_v30_0_design_system_architecture_unit_strategy.zip`

## Evidence policy

Use this precedence:

1. Current official Elementor V4 Help Center and Developer Docs
2. CSSWG/W3C or MDN for CSS behavior
3. Existing validated v29 content and registries
4. Controlled fixtures and deterministic assertions
5. Educational models and proposals, explicitly labeled

Never present a proposal, analogy, token taxonomy, naming convention, or workflow recommendation as an official Elementor rule.

Use these labels where appropriate:

- `verified_by_official_elementor_help`
- `verified_by_elementor_developer_docs`
- `verified_by_css_spec`
- `verified_by_real_fixture`
- `verified_by_controlled_experiment`
- `derived_educational_model`
- `proposed_strategy`
- `insufficient_evidence`

## Non-negotiable preservation

Preserve:

- all 21 main lessons
- all 7 supplementary lessons
- all six stations A–F
- TUYA progression and desktop/mobile references
- Persian RTL layout
- offline-only behavior
- all theme modes, focus mode, print support, progress, reading controls, Font Lab, IndexedDB/local persistence where present
- sidebar and internal navigation
- semantic HTML and accessibility improvements
- all current Step-Through v2 behavior and registries
- current practical findings and evidence archives
- all provenance/source materials

Do not:

- remove or summarize lessons
- flatten the workbook into a static article
- add external runtime dependencies, CDNs, remote fonts, analytics, or frameworks
- claim browser runtime validation unless actually performed
- rename official Elementor variable types
- invent Component nesting support
- present dependency diagrams as CSS cascade order

## Required implementation

### 1. Add a core architecture primer

Add an unnumbered core section after Lesson 1 and before Lesson 2. Do not change the 21-lesson count.

Persian title suggestion:

`از ساخت صفحه تا ساخت سیستم — معماری ذهنی Elementor V4`

Teach:

- System First, Page Second
- CSS Thinking instead of Widget Thinking
- Reuse Before Create
- Relationship and Dependency Thinking
- Scalability
- Separation of Content, Style, and Structure
- Architecture Before Building
- V3 Thinking versus V4 Thinking
- planned design-system workflow versus discovery/prototyping workflow

Clearly separate:

A. Design-system dependency:

`Named values / Variables → Class declarations → Components → Instances → Pages`

B. Style conflict resolution:

`Global Class hierarchy + State + Local Class + Custom CSS/cascade context → Computed Style`

Never call the first diagram a cascade chain.

### 2. Upgrade the Units atlas into a Unit Strategy system

Do not duplicate the existing v29 atlas. Extend it with:

- Anatomy of a Value
- Unit Selection Framework
- Design System Decision layer
- Unit and Value Smell Detection
- direct literal versus Size Variable versus Class declaration versus Component usage
- property/reference-aware recommendations
- explicit UI status: Elementor UI, CSS-supported, Custom CSS, Computed output

Correct definitions:

- A Variable is a named value/reference, not always `value + unit`.
- Official Elementor variable types are exactly Color, Font, and Size.
- Spacing tokens and typography scales are derived strategies using Size/Font Variables; they are not official variable types.
- `100vw` is not the default recommendation for every full-width section.
- `dvh` must not be presented as available in every Elementor control unless the current official control documentation confirms it.

Add context-aware decision fields:

- design intent
- Property
- candidate value/unit
- computation reference
- strength
- risk
- Elementor UI availability
- recommended baseline
- when an alternative is better

Do not create universal rules such as “always use rem” or “never use px.”

### 3. Add two Step-Through v2 modules

Use the existing shared data-driven engine and schema. Do not write separate ad-hoc simulators.

#### A. Literal to system

Stages:

1. direct literal
2. repeated literal smell
3. Size Variable
4. Variable used inside a Global Class
5. Class reused on elements
6. Class/Variable consumed in a Master Component
7. sitewide propagation after Variable update
8. case where Variable or Component is unnecessary

#### B. Unit-selection tradeoffs

Show calculations and tradeoffs for:

- px
- rem
- em
- percentage
- fr
- vw/vh/dvh
- keyword/function such as auto, min(), clamp()

Require prediction before next step, reveal feedback, previous/next/reset, aria-live, keyboard support, reduced motion, print fallback, evidence labels, and local progress storage.

### 4. Add a Variables Architecture Lab

Cover:

- official Color, Font, and Size Variables
- Variable as a named value
- Variables inside Classes
- primitive versus semantic tokens as `derived_educational_model`
- spacing and typography scales as strategies, not official variable types
- propagation after editing a Variable
- design-system import/export
- whole-package limitation and name-conflict choices
- Hybrid sync to V3 Global Colors/Fonts
- naming and anti-patterns
- when a literal should remain local
- when a value should not become a Variable

### 5. Expand Class Architecture and conflict debugging

Extend the existing Class Priority Step-Through rather than adding a duplicate.

Include:

- Global Class A versus B
- Class Manager priority
- State
- Local Class
- Custom CSS/matched-rule context
- Computed winner
- local-first prototyping and convert-to-global after verified reuse
- class-sprawl smells

Keep official facts separate from proposed naming/utility-class strategies.

### 6. Add a Components Lifecycle Lab

Cover only officially supported behavior:

- Atomic Elements requirement
- Pro and Admin requirements for creating/editing
- building a Master
- exposing customizable properties
- only eligible General-tab fields with the property icon
- adding Instances
- per-instance overrides that persist after Master updates
- Master update propagation
- property grouping
- Detach Component
- refactoring repeated structure into a Component
- when not to create a Component
- overlarge component and excessive-property anti-patterns

Do not claim Component nesting is supported unless a current official source or controlled fixture proves it. Otherwise use `insufficient_evidence`.

### 7. Add a Dynamic Data case study

Mark it clearly as part of the wider Elementor Pro ecosystem, not the exclusive core of Editor V4.

Use one practical case study with:

- a defined Post Type or Custom Post Type
- supported ACF fields
- V4 Dynamic Tags
- Single Template
- Loop Grid
- Query source/include/exclude
- fallback/empty-state behavior

Use official terms. Do not invent a standalone product concept called “Query Loop” when the UI/documentation uses Loop Grid and Query controls.

### 8. Add an Interactions Lab

Teach and demonstrate current official controls:

- Trigger: Page Load, Scroll Into View, While Scrolling, On Hover, On Click
- Effect: Fade, Slide, Scale
- Type: In/Out
- Direction
- Duration and Delay in milliseconds
- multiple interactions on one element
- distinction between State, CSS Transition, Interaction, and legacy Motion Effects
- performance and reduced-motion guidance, clearly labeled where it is general web/accessibility guidance

### 9. Add architecture visuals

Create accessible HTML/SVG visualizations for:

- V3 Thinking versus V4 Thinking
- Design-system dependency graph
- Style conflict resolution map
- Component lifecycle
- Anatomy of a Value
- Unit Selection decision tree
- Unit/Value smell cards

SVGs must include accessible titles/descriptions. Do not use raw ASCII as the primary visual.

### 10. Integrate design-system decisions into existing lessons

At the end of relevant Layout, Typography, Spacing, Responsive, and State lessons, add a short closed disclosure that asks:

- direct literal or Variable?
- Local or Global Class?
- style reuse or structural reuse?
- is a Component justified?

For non-unit-centric lessons, do not create artificial unit content. Explicitly mark `not_applicable`, `reference`, `keyword`, or `unitless` as appropriate.

## Progressive disclosure and visual consistency

- The main concept remains open.
- Concept reference, units, Step-Through, findings, responsive checkpoint, and exercises are closed by default.
- Single-line summaries must have a consistent minimum height and vertical padding.
- Multi-line summaries may grow naturally.
- Deep links must open all ancestor details.
- Print mode must show all hidden content.

## Validation

Update `VALIDATION_REPORT.md` and execute deterministic checks for all fields in `scope/V30_VALIDATION_CONTRACT_FA.md`.

At minimum verify:

- 21 main lessons, 7 supplementary lessons, 6 stations
- architecture primer present without changing lesson count
- official variable types exactly Color/Font/Size
- no universal `Variable = Value + Unit` claim
- no official `Space Variable` or `Typography Variable` claim
- no unsupported Component nesting claim
- dependency graph is not labeled cascade
- at least two new Unit Strategy Step-Throughs
- Variables, Components, Dynamic Data, and Interactions labs present
- no duplicate IDs
- all internal links resolve
- no active external assets or network dependencies
- semantic table validity
- control labels and details summaries
- JSON, SVG, and JavaScript parsing
- SHA-256 manifest and ZIP integrity

Separate static validation, semantic validation, and runtime browser validation. If browser testing cannot be completed, record `not_performed` or the precise environment failure. Never claim `passed` without execution evidence.

## Required output package

Return a complete next-version ZIP containing:

- updated `index.html`
- updated CSS and JS
- preserved assets and source archives
- updated `README_FA.md`
- updated `CHANGELOG_FA.md`
- updated `PATCH_SUMMARY_FA.md`
- updated `DOCUMENTATION_AUDIT_FA.md`
- updated `VALIDATION_REPORT.md`
- updated `manifest.json`
- updated `SHA256SUMS.txt`
- new v30 source registries, schemas, matrices, and validation scripts

Return the complete ZIP and a separate copy of `VALIDATION_REPORT.md`. Do not return only a patch, instructions, or partial files.
