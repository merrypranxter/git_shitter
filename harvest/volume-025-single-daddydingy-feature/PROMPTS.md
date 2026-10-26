# VOLUME 025 — Daddy Dingy: TTF Vector Glyph Innovations

**MODE:** SINGLE · **FORMAT:** feature · **DATE:** 2026-10-26

**SOURCE:** [daddydingy](https://github.com/merrypranxter/daddydingy)

## 01 — Dynamic Key-Glyph Assignment Preview

**BASIS:** README: 'assign ornaments to keyboard keys, tweak placement/size/rotation, preview live typing'

**IMAGE / IMPLEMENTATION PROMPT:**

Build a feature for Daddy Dingy where users can assign SVG glyphs to keyboard keys. The UI should feature a visual keyboard layout. When a user drags an SVG from 'THE PILE' onto a key, a live preview updates in a text input area, showing how that character would render using the current font settings (size, rotation). Include controls for fine-tuning the glyph's position, scale, and rotation directly within the keyboard assignment interface. Acceptance criteria: Real-time update of preview text on key assignment and parameter changes; predictable glyph rendering based on user input. Low-cost runtime: Use a lightweight canvas element for the preview, updating only on user interaction.

**WHY IT'S WEIRD:** The 'live typing preview' is not just a static representation but dynamically updates as glyphs are assigned and manipulated on a visual keyboard, creating an immediate, interactive feedback loop for font creation.

---

## 02 — Color Trace Detail Level Slider

**BASIS:** README: 'Compact / Detailed / Maximum detail: choose tracing resolution and path simplification'

**IMAGE / IMPLEMENTATION PROMPT:**

Implement a UI slider in the '🌈 COLOR VECTOR FOUNDRY' section to control the tracing detail level. Options should map to 'Compact', 'Detailed', and 'Maximum detail'. As the slider is adjusted, a small, representative section of the currently loaded image should re-trace in the background, updating a miniature preview window. The slider should have associated tooltips explaining the trade-offs: 'Compact' for smaller files and faster processing, 'Maximum detail' for intricate shapes but higher resource usage. Acceptance criteria: Slider movement visibly affects the complexity and point count of traced paths in the preview; processing time scales with detail level. Low-cost runtime: Perform tracing on a small, pre-selected portion of the input image for preview updates.

**WHY IT'S WEIRD:** Instead of a discrete selection, a continuous slider allows for nuanced control over tracing algorithms, enabling users to 'dial in' the exact level of detail, approaching a speculative 'analog' control for digital vectorization.

---

## 03 — SVG White Transparency Threshold Control

**BASIS:** README: 'White becomes transparent... Threshold is adjustable for off-white photo backgrounds.'

**IMAGE / IMPLEMENTATION PROMPT:**

Add a fine-tuning slider for the 'white becomes transparent' feature in the '🌈 COLOR VECTOR FOUNDRY'. This slider should control a threshold value, allowing users to specify how 'white' a color must be to be considered transparent. The UI should display a small swatch of the input image that dynamically updates to show the effect of the threshold adjustment, highlighting areas that will become transparent. Tooltips should explain that higher values make more off-white colors transparent. Acceptance criteria: Slider adjustment correctly alters the transparency mask in real-time; users can recover details from slightly off-white backgrounds. Low-cost runtime: Apply the threshold logic to a representative pixel sample for the preview.

**WHY IT'S WEIRD:** This feature speculatively quantifies 'whiteness' as a continuous variable, turning a binary transparency decision into an analog control, allowing users to 'etch' away subtle background noise with granular precision.

---

## 04 — Interactive 'THE PILE' Glyph Sorting

**BASIS:** README: '...resulting nine full-color vector assets automatically appear in the pile.'

**IMAGE / IMPLEMENTATION PROMPT:**

Enhance 'THE PILE' with interactive sorting options for imported glyphs. Users should be able to click column headers (e.g., 'Name', 'Date Imported', 'Size', 'Assigned Key') to sort the displayed glyphs. Implement a drag-and-drop reordering functionality for manual arrangement. When glyphs are reordered manually, their underlying assignment order for the 'Export All SVGs' or 'Fill Keys' functions should update accordingly. Acceptance criteria: Sorting by all available metadata works correctly; drag-and-drop reordering persists and affects subsequent bulk operations. Low-cost runtime: Client-side sorting and reordering using JavaScript array manipulation and DOM updates.

**WHY IT'S WEIRD:** The 'pile' becomes a fluid, interactive 'desk' for glyphs, where manual arrangement directly influences automated processes like key filling, blurring the line between user intent and machine execution.

---

## 05 — Font Export Precision Visualizer

**BASIS:** README: 'Daddy Dingy now writes its TrueType outlines on a 4096-unit grid instead of rounding every ornament to 1000 font units.'

**IMAGE / IMPLEMENTATION PROMPT:**

Create a visualizer within the font export dialog that demonstrates the increased precision of the 4096-unit grid compared to the older 1000-unit grid. This could involve displaying a complex curve or a small, detailed glyph, and showing two representations side-by-side: one rendered with the legacy low precision, and another with the high precision. Users could toggle between them or see them animated. A tooltip explaining that this higher precision preserves finer details like counters and tight curves should be included. Acceptance criteria: Visual comparison clearly shows improved outline fidelity; users can understand the benefit of the new export grid. Low-cost runtime: Render pre-defined complex SVG paths using both coordinate systems for demonstration.

**WHY IT'S WEIRD:** This feature provides a 'time-travel' visualization for font precision, allowing users to see the ghost of lower-fidelity outlines being overwritten by a more granular, high-resolution future, directly impacting the perceived 'sharpness' of imported dingbats.

---

## 06 — Auto-Fill Keyboard Key Collision Warning

**BASIS:** README: 'Automatic assignment prioritizes `a–z`, then the remaining normal keyboard characters... Existing key assignments are never overwritten by the harvester.'

**IMAGE / IMPLEMENTATION PROMPT:**

When the 'HARVEST ALL + FILL KEYS' or 'Auto-fill next EMPTY keyboard keys' function is used, implement a warning system. If the system detects that assigning newly harvested glyphs would conflict with existing manual key assignments (even though it's set not to overwrite), it should prompt the user. The prompt would list the glyphs that cannot be assigned due to existing keys and offer options: 'Skip these glyphs', 'Reassign existing keys (with confirmation)', or 'Cancel operation'. Acceptance criteria: Warning appears when potential conflicts exist; user options are functional and correctly alter the assignment process. Low-cost runtime: Pre-scan keyboard assignments before initiating bulk fill.

**WHY IT'S WEIRD:** The system proactively flags 'ghosts' of intended assignments, not by overwriting, but by presenting a spectral list of unassigned glyphs that *would have* occupied precious key real estate, forcing a more deliberate manual curation.

---

## 07 — Custom Box Drawing for Sheet Harvester

**BASIS:** README: 'If the sheet has an irregular layout or the detector misses a design, use Draw a custom box and Add drawn design.'

**IMAGE / IMPLEMENTATION PROMPT:**

Develop an interactive drawing tool for defining custom extraction boxes in the 'Sheet Harvester'. Users should be able to click and drag on a preview of the SVG sheet to draw a rectangular or polygonal region. This region then defines the boundaries for 'Add drawn design'. The tool should provide visual guides (e.g., dashed lines, corner handles) for resizing and repositioning the box. Multiple custom boxes can be defined and added sequentially. Acceptance criteria: Users can draw, resize, and reposition arbitrary shapes on the sheet preview; extracted designs accurately match the drawn boxes. Low-cost runtime: Utilize SVG overlay elements for drawing and manipulation.

**WHY IT'S WEIRD:** Transforms the static SVG sheet into an interactive canvas where users can 'sculpt' their desired glyph regions, bypassing automated detection for a more intuitive, direct manipulation of the artwork's boundaries.

---

## 08 — Individual SVG Export Size Report

**BASIS:** README: 'If an individual SVG stays above 2 MB, Daddy Dingy reports the size and preserves the artwork instead of silently wrecking it.'

**IMAGE / IMPLEMENTATION PROMPT:**

Implement a clear, user-facing report mechanism for individual SVG exports that exceed the 2 MB target. When '↓ Selected SVG' or '↓ All SVGs · ZIP' is used and an SVG is too large, the app should pause and display a modal or inline message detailing which SVG(s) exceeded the limit and their exact file size. It should then present options: 'Export anyway (may be unstable)', 'Attempt aggressive optimization (lose detail)', or 'Skip this SVG'. Acceptance criteria: Large SVGs are correctly identified; accurate size information is displayed; user options are functional and lead to predictable outcomes. Low-cost runtime: Perform size checks on generated SVGs before initiating download.

**WHY IT'S WEIRD:** This feature introduces 'file size as a critical design parameter', turning a technical constraint into a tangible quality indicator that users must actively negotiate, making large SVGs feel like 'heavy artifacts' that require deliberate handling.

---

## 09 — Raster Trace 'Re-trace SVGs too' Visual Feedback

**BASIS:** README: 'To replace over-complicated Adobe Capture vectors with new, flatter colored paths, deliberately turn on Re-trace SVGs too.'

**IMAGE / IMPLEMENTATION PROMPT:**

When the 'Re-trace SVGs too' option is enabled in the '🌈 COLOR VECTOR FOUNDRY', provide visual feedback to the user. Before the re-tracing begins, display a confirmation prompt that clearly states: 'Existing SVG files will be rasterized and re-traced. This may reduce precision. Proceed?'. Upon proceeding, show a subtle visual indicator (e.g., a faint outline overlay or a 'rasterizing' icon) on SVGs in 'THE PILE' that are slated for re-tracing. Acceptance criteria: User is clearly informed before re-tracing happens; visual indicator reliably shows which SVGs will be affected. Low-cost runtime: Client-side state management to track the 'Re-trace SVGs too' setting.

**WHY IT'S WEIRD:** This prompt makes the often-invisible process of re-vectorization visible, casting a 'ghost' of the original complex SVG over the simpler, re-traced version, highlighting the transformation from precise vector to sampled approximation.

---

## 10 — Project Save/Load Status Indicator

**BASIS:** README: 'Save project manually; browser localStorage autosave may run out of quota.'

**IMAGE / IMPLEMENTATION PROMPT:**

Implement a clear status indicator for project saving and loading. When a user makes changes, a 'Project Unsaved' indicator should appear. Clicking a 'Save Project' button should trigger a saving process, and the indicator should change to 'Saving...' and then 'Project Saved' (perhaps with a timestamp). Conversely, when loading a project, provide feedback like 'Loading Project...' and 'Project Loaded'. Include a small, unobtrusive icon or text element, perhaps near the top of the UI, that reflects this status in real-time. Acceptance criteria: Indicator accurately reflects the project's save state; save/load operations provide timely feedback. Low-cost runtime: Client-side state management and local storage operations.

**WHY IT'S WEIRD:** This feature animates the ephemeral nature of browser-based projects, turning the silent saving process into a dynamic 'breath' of the application, where 'unsaved' states are visualized as a subtle decay or tremor in the UI.

---

