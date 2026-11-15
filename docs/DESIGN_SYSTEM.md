# Senior-slide-inspired visual design system

## Observed source style (from the supplied 67-slide PPTX)
- 20.0 x 11.25 in landscape canvas (**16:9**).
- Mostly solid **#F8F8F8** near-white background.
- Source fonts most frequently: **Cormorant Garamond Bold Italics** for large titles, **Times New Roman** for content/navigation; some Cormorant Garamond regular.
- Prominent colors visible in source run styles: **#A31F34** (wine/red), **#8C6E4A** (brown/tan), black **#000000**, white **#FFFFFF**; occasional strong red or green symbols.
- Intro/content title sometimes 52–64 pt on the 20-inch wide source canvas, body 25–32 pt, navigation ~22 pt, page number ~28 pt.
- Large left-side section heading; secondary navigation at upper right and/or below header; low-contrast bottom navigation ribbon; small page number at lower right.
- Method and experiment sections often use a **subsection breadcrumb row** and a repeating **global footer navigation**.
- Sparse off-white canvases, roomy margins, diagrams and equations with very little decorative chrome.
- A number of source slides are inconsistent or crowded; **preserve visual identity but improve polish, grid alignment, legibility and content hierarchy**.

## Audience language and source treatment (mandatory, 2026-11-16)
- Slides **must be in Traditional Chinese**, not English. Keep recognized international abbreviations such as MNB, PSO, DNA, 8-mer and formula symbols.
- Use Traditional-Chinese-friendly title font `Noto Serif CJK TC` (bold; do not force awkward pseudo-italics on Chinese glyphs); body and nav `Noto Sans CJK TC` if available, document fallback when needed.
- Preserve the wine-red/off-white editorial design from the senior deck; the senior's English typography is a visual reference, not a copywriting rule.
- **No miniature source/resource strips along the lower content edge.** Put useful in-context citations next to the relevant study or diagram, and full citations in notes/references. Bottom area is reserved for navigation/page number.
- Follow `docs/SLIDE_WRITING_RULES.md` when there is a conflict with older specifications.

## Proposed normalized tokens
| Token | Value | Usage |
|---|---|---|
| `canvas` | 20 x 11.25 in, 16:9 | all slides |
| `background` | `#F8F8F8` | default |
| `ink` | `#171717` | body text |
| `accent` | `#A31F34` | title underline, active tab, key flow stage |
| `secondary` | `#8C6E4A` | subheading/breadcrumb/divider |
| `muted` | `#6F6F6F` | nonactive tab, citation |
| `rule` | `#DFD9D2` | structural lines |
| `titleFont` | `Noto Serif CJK TC` (bold) for Chinese; Cormorant Garamond italic for English only when appropriate | big titles |
| `bodyFont` | `Noto Sans CJK TC` for Chinese; Times New Roman for Roman math if needed | body / formula / navigation |
| `titleSizePt` | 52–64 pt | on original 20-inch canvas |
| `bodySizePt` | 26–32 pt | on original 20-inch canvas |
| `navSizePt` | ~22 pt | section labels |
| `citationSizePt` | ~17–20 pt | source labels |
| `numberSizePt` | ~28 pt | lower-right page counter |

Use these as **starting specifications**; adjust with rendered preview based on actual readability. If using standard 13.333 x 7.5 in, scale dimensions and fonts consistently (~two thirds), not font sizes alone. If the exact title font is unavailable, use a serif italic substitute and record the fallback in the deck metadata.

## Slide layout archetypes
1. **Cover** — giant serif italic thesis title, adviser/presenter, date and school, generous whitespace.
2. **Contents** — broad section list/roman numerals, clear section rhythm.
3. **Section explanation** — big left title, small top-right subsection breadcrumb, primary visual/text block.
4. **Contrast** — left/right or three-column comparison with restrained red and tan accents.
5. **Process flow** — editable blocks/arrows, emphasize active step in accent color.
6. **Formula and explanation** — readable equation in content region, symbols in adjacent definitions or bottom strip.
7. **Method animation-ready** — duplicate process layout across sequential slides; highlight one stage per slide rather than dense one-page graph.
8. **Experiment plan** — clear dataset–method–measure table, no fabricated results.
9. **Closing** — one-slide planned experiment summary, expected contribution and standalone Thank You/Q&A.\n10. **Appendix** — optional technical backup slides placed **after** Thank You, including the fit/search/test split, constrained random MNB/PSO, and JMH/weight updates.

## Navigation
- Header/upper-right: Traditional Chinese subsection breadcrumbs (for example, `特徵評分 · 子集合抽樣 · PSO 搜尋`).
- Footer/global menu (new standard): `目錄  |  緒論  |  文獻探討  |  研究方法  |  實驗規劃  |  附錄`. Existing Slides 1–25 still require Canva text correction with preview and approval.
- Active section: wine-red underline/marker; inactive sections: muted tan/gray.
- Lower-right: two-digit slide number (cover can be unnumbered; maintain consistent implementation).
- Keep footer navigation above content and away from figures; allocate fixed safe zones.

## Quality rules
- One research takeaway per slide; diagrams first, restrained bullets second.
- Diagrams must remain editable (native PowerPoint/Slides objects or editable vector source).
- Never paste an unreadable thesis page as a full-slide image.
- Avoid overlapping labels, inconsistent arrows, unnecessary shadows or clipart.
- Distinguish (a) observed past research, (b) our proposed algorithm, (c) planned evaluation.
- Cite papers on the slide where discussed; references can also appear at end.
- Ensure sufficient contrast; red/tan should not be sole carrier of meaning.
- When recreating, draw inspiration rather than copying copyrighted text/images from the original deck.

## Mathematical typography and canonical deck
- **Final output is a PowerPoint presentation.** Keep source LaTeX in a private per-slide manifest while authoring in Canva. After Canva→PPTX export, replace equations with native editable Office Math (OMML) objects and validate; using Canva LaTeX Math is optional for visual preview.
- Do not treat typed Unicode subscripts as a substitute for professionally typeset formulae; preserve valid equation meaning and the latest thesis indices and normalization constraints.
- Maintain a **single, editable Canva master deck**, and add future batches to that same project. Check each merged page's actual logical order.
- Where Canva API cannot invoke the app, retain readable placeholder text and document the precise LaTeX input and PowerPoint conversion-pending status. See `docs/FINAL_POWERPOINT_EQUATIONS.md`.

## Arrow and flow-diagram standard
- Use a single native connector with real endpoint arrowheads per directed edge, not a line plus a detached chevron.
- Arrow endpoints align with source/target card edges; use straight/orthogonal routing and consistent gaps. Never cross content or misrepresent fit/search/test or convergence.
- Maintain an arrow source→target audit table and check rendered PPTX and Canva imports. See `docs/ARROW_CONNECTOR_QA.md`.
