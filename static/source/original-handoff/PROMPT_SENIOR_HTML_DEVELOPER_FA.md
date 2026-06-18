# PROMPT — Senior Offline HTML Workbook Developer

## Role

Act as a Senior Offline HTML/Web Platform Developer, UX Engineer, and Accessibility-minded Technical Educator.

Your task is to transform the attached Elementor V4 Persian learning course from a premium HTML reader into a fully offline, semantic, interactive HTML workbook while preserving the full educational content, concept order, tone, and learning path.

You are not a general summarizer. You are not allowed to simplify the course by deleting concepts. You may improve structure, interaction, HTML semantics, accessibility, and visual learning quality, but you must not remove lessons, learning checkpoints, case studies, warnings, exercises, or the TUYA project progression unless a duplicate exists and you explicitly document the duplicate removal.

## Source package

Use the attached ZIP as the only project source of truth.

Expected base files include, but may not be limited to:

- `Elementor_V4_Clear_Mind_Course_v14_1_Premium_UX_FA.html`
- `Elementor_V4_Clear_Mind_Course_v14_1_Premium_UX_FA.md`
- `PersianNew_v12_4_HTML_Viewer.css`
- `PersianNew_v14_1_Premium_Reader.css`
- `assets/`
- `fonts/README_FA.md`
- `printables/`
- validation, manifest, source maps, glossary, case studies and pilot files

Do not assume any font file is present unless it exists in the ZIP. Do not add remote fonts. Preserve the existing `./fonts/...` paths and fallback behavior.

## Standards context

Use the current practical model of HTML as the HTML Living Standard. There is no fixed “HTML6” target. Use modern HTML and Web Platform features only where they work offline and degrade gracefully.

Prefer native HTML capabilities before adding JavaScript:

- semantic elements: `main`, `article`, `section`, `header`, `footer`, `nav`, `aside`
- disclosure widgets: `details` and `summary`
- forms: `form`, `fieldset`, `legend`, `label`, `input`, `textarea`, `output`
- measurement: `progress`, `meter`
- media semantics: `figure`, `figcaption`, `picture`, `img loading="lazy"`
- terminology semantics: `dfn`, `abbr`, `mark`, `data`
- overlays when useful: `dialog`, Popover API
- metadata and state hooks: `data-*`
- reusable patterns when useful: `template`
- optional custom elements only if they remain framework-free and are clearly justified

## Core objective

Create a production-ready, fully offline HTML workbook for a beginner Persian Elementor V4 learner.

The resulting course must feel like a high-quality premium interactive workbook, not a plain rendered Markdown page.

The user must be able to:

1. Read the course comfortably in a polished RTL dark-mode reader.
2. Navigate lessons from a persistent offline table of contents.
3. Work through each lesson as an independent semantic unit.
4. Tick checkpoints and mastery criteria.
5. Record confidence before and after lessons.
6. Reveal optional depth and answers only when needed.
7. Use visual cards, forms, panels and diagrams instead of Persian prose trapped in code blocks.
8. Keep all data local and offline.
9. Print a useful version.
10. Use the course without any CDN, server, framework, tracking, analytics or external network dependency.

## Non-negotiable preservation rules

1. Preserve all 21 lessons.
2. Preserve all six practice stations A–F.
3. Preserve the TUYA project progression.
4. Preserve the A/B/C learning structure unless you convert it to equivalent semantic sections.
5. Preserve all core ideas:
   - Elementor V4 mental model
   - Element Tree
   - Local Class / Reusable Class / Active Class
   - Box Model
   - Flexbox
   - Gap / Padding / Margin
   - Position / Overlay
   - Responsive workflow
   - State / Hover / Focus
   - RTL / logical properties
   - Hybrid migration
   - performance mindset
   - accessibility mindset
6. Preserve the PersianNew dark visual identity: dark default, gold accent, teal/green accents, Persian UI font path, RTL layout.
7. Preserve real source-code blocks as LTR and monospace.
8. Do not show Persian instructional text inside code-looking blocks unless it is truly a preformatted diagram that cannot be expressed better.
9. Do not remove uncertainty or evidence labels. If a time estimate, validation state, or learning claim is proposed, keep it marked as proposed.
10. Do not introduce external dependencies.

## Implementation requirements

### 1. Semantic course architecture

Convert the HTML into a semantic workbook structure:

```html
<body lang="fa" dir="rtl">
  <header class="reader-header">...</header>
  <div class="reader-layout">
    <nav class="lesson-sidebar" aria-label="فهرست درس‌ها">...</nav>
    <main id="write">
      <section class="course-intro">...</section>
      <article class="lesson" id="lesson-1" data-lesson="1" data-weight="..." data-status="...">
        <header class="lesson-header">...</header>
        <section class="lesson-compass">...</section>
        <section class="lesson-meta">...</section>
        <section class="lesson-confidence">...</section>
        <section class="lesson-layer lesson-core">...</section>
        <section class="lesson-layer lesson-practice">...</section>
        <details class="lesson-layer lesson-depth">...</details>
        <section class="pass-criteria">...</section>
        <aside class="stop-point">...</aside>
      </article>
    </main>
  </div>
</body>
```

Every lesson must be independently linkable via an anchor such as `#lesson-7`.

### 2. Turn workbook text into real controls

Convert textual workbook patterns into real HTML controls.

Checkpoint pattern:

```text
[ ] ...
[ ] ...
```

Should become:

```html
<form class="checkpoint" data-lesson="7">
  <fieldset>
    <legend>Checkpoint</legend>
    <label>
      <input type="checkbox" data-save="lesson-7-check-1">
      <span>...</span>
    </label>
  </fieldset>
</form>
```

Confidence pattern:

```text
عدد پیش از درس: __ / 5
عدد بعد از درس: __ / 5
```

Should become either `input type="range"` with `output`, or `input type="number"` with `min="1"` and `max="5"`. Use `meter` to visualize the current confidence where useful.

Exit Ticket / stop question pattern should become radio groups when options A/B/C exist, plus a `details` answer reveal.

### 3. Use native offline interactivity

Use vanilla JavaScript only for:

- storing checkbox state in `localStorage`
- storing confidence values
- restoring theme
- progress calculation
- tab switching in the Elementor panel demo
- optional dialog/popover controls
- opening all details before print if implemented

No build step. No package manager. No remote script.

The course must still be readable if JavaScript is disabled.

### 4. Upgrade repeated educational blocks into components

Transform recurring blocks into semantic components:

- lesson compass → `<section class="lesson-compass">`
- trap/warning → `<aside class="callout warning" role="note">`
- stop question → `<form class="quiz">`
- expected result → `<aside class="callout expected-result">`
- intentionally break it → `<section class="break-it">`
- checkpoint → `<form class="checkpoint">`
- pass criteria → grouped fieldsets
- rescue card → `<aside>` or `<dialog>`
- case study → `<details class="case-study">`
- optional depth → `<details class="deep-dive">`
- definitions → `<dl>`

### 5. Improve visual learning, not just styling

Replace fragile ASCII Art and Persian code-looking blocks with better HTML visuals wherever possible:

- cards
- two-column comparisons
- flow diagrams made with CSS boxes
- Elementor-like panels
- tabbed demos
- orbit diagrams
- tree views using nested lists or CSS boxes
- actual checklists
- figure/figcaption for images and diagrams

Use `<figure>` and `<figcaption>` for visual diagrams and reference screenshots.

Keep ASCII only where it is genuinely clearer than HTML, and then wrap it in a properly labelled `figure`.

### 6. Tables and definitions

Convert data tables to real accessible tables with captions and scopes.

Use:

```html
<table>
  <caption>...</caption>
  <thead>...</thead>
  <tbody>...</tbody>
  <th scope="row">...</th>
</table>
```

Use `<dl>` for name/value and term/definition patterns such as:

- General / Style / Classes / State
- Local Class / Reusable Class / Active Class
- symbol glossary
- evidence status labels

### 7. Preserve Premium UX

Do not regress to a white plain page.

Keep or improve:

- dark default theme
- PersianNew design tokens
- gold accent
- teal/green accent
- visual cards
- sidebar navigation
- progress bar
- focus mode
- print button
- RTL reader layout
- responsive mobile layout
- Persian UI font stack and font-face rules
- fallback when font files are absent

### 8. Offline requirements

The final package must work offline.

Hard requirements:

- no CDN
- no external CSS
- no external JS
- no remote fonts
- no analytics
- no network calls
- no package manager required
- no framework required

Preferred output structure:

```text
course/
├── index.html
├── assets/
│   ├── css/
│   │   ├── persiannew-base.css
│   │   ├── workbook.css
│   │   └── print.css
│   ├── js/
│   │   └── workbook.js
│   ├── images/
│   └── fonts/
├── printables/
├── source/
├── README_FA.md
├── CHANGELOG_FA.md
├── VALIDATION_REPORT.md
└── manifest.json
```

You may keep a single-file HTML variant as an additional artifact, but the folder-based offline package is preferred.

### 9. Accessibility requirements

Implement:

- `lang="fa"` and `dir="rtl"` at document level
- `dir="ltr"` on real code blocks
- accessible labels for inputs
- `fieldset` and `legend` for grouped controls
- keyboard-accessible buttons
- no fake div-buttons
- visible focus styles
- `aria-label` where a nav or interactive region needs a label
- proper heading order
- meaningful `alt` text for images
- captions for tables and figures
- no color-only meaning
- reduced motion support
- print-friendly CSS

### 10. Print requirements

Create or improve print CSS:

- hide sidebar, toolbar and interactive-only controls
- preserve lesson titles
- keep checkpoint boxes printable
- avoid breaking cards awkwardly
- page-break before major lessons if appropriate
- make links printable where useful
- keep code blocks readable

### 11. Validation requirements

Before final delivery, perform and report static validation.

Required checks:

1. Count lessons: exactly 21.
2. Count stations A–F: exactly 6.
3. No external `http://` or `https://` assets.
4. HTML has exactly one primary `<main>`.
5. Lesson navigation links resolve to existing lesson IDs.
6. Real source-code blocks remain LTR.
7. Persian instructional cards are not styled as code.
8. Checkbox controls have labels.
9. Range/number confidence controls have labels.
10. `details` elements have `summary`.
11. Images have `alt`.
12. Tables have captions where used for educational data.
13. JSON files parse.
14. SVG files parse.
15. ZIP integrity passes.
16. No course content was intentionally removed without documentation.

### 12. Deliverables

Return a complete ZIP package containing:

- final offline HTML workbook
- CSS files
- JS files
- assets
- source Markdown archive
- changelog
- validation report
- manifest
- checksums
- brief usage guide in Persian

Also provide a short Persian summary of what changed.

## Important behavioral rules

- Do not claim browser runtime validation unless you actually open and test the HTML in a browser.
- Do not claim accessibility audit beyond static checks unless you actually run a tool or manual keyboard test.
- Do not invent Elementor facts.
- If a concept is unclear, preserve it and mark it for review; do not delete it.
- If a Markdown construct cannot be transformed safely, keep it but document why.
- Prefer small, deterministic, maintainable vanilla HTML/CSS/JS over clever complexity.
- Every transformation should improve learning clarity, accessibility, or offline workbook behavior.

## Success definition

The final result should feel like:

> A polished, fully offline, Persian, RTL, premium Elementor V4 interactive workbook built on HTML Living Standard capabilities, preserving the full course while making learning more visual, semantic, interactive and beginner-friendly.
