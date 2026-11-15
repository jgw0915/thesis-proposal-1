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
| `titleFont` | `Cormorant Garamond` with bold italic | big titles |
| `bodyFont` | `Times New Roman` | body / formula / navigation |
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
9. **Closing** — focused contribution, planned next steps and Q&A.

## Navigation
- Header/upper-right: current subsection breadcrumbs (for example, `Feature Scoring · Subspace Sampling · PSO Search`).
- Footer/global menu: `Contents  |  Introduction  |  Literature Review  |  Method  |  Experimental Plan  |  References`.
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
