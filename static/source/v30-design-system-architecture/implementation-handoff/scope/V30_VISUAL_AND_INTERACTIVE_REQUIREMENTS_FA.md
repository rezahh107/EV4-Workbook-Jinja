# نیازمندی‌های Visual و Interactive

## Step-Throughهای جدید

### STV2-A — Value to System

مراحل پیشنهادی:

1. literal مستقیم `padding: 24px`
2. تکرار literal در چند عنصر
3. ساخت Size Variable با نام semantic
4. مصرف Variable داخل Global Class
5. مصرف Class در چند Element
6. استفاده از همان Class داخل Master Component
7. تغییر Variable و propagation
8. تشخیص موردی که نباید Variable یا Component شود

### STV2-B — Unit Selection Tradeoffs

مراحل پیشنهادی:

1. px برای border/offset محدود
2. rem برای scale وابسته به root
3. em برای component-local scaling
4. % برای parent-relative width
5. fr برای Grid free-space distribution
6. vw/vh/dvh و viewport risk
7. keyword/function (`auto`, `min()`, `clamp()`)
8. انتخاب بر اساس intent و reference

هیچ مرحله‌ای نباید یک واحد را برندهٔ جهانی اعلام کند.

## Visualهای الزامی

- V3 vs V4 mental model card
- Design dependency graph
- Style conflict resolution map
- Component lifecycle diagram
- Anatomy of a Value diagram
- Unit smell cards

## Accessibility

- بدون autoplay.
- button واقعی.
- keyboard navigation.
- `aria-live="polite"`.
- state فعلی با متن، نه فقط رنگ.
- print fallback برای همهٔ مراحل.
- `prefers-reduced-motion`.
