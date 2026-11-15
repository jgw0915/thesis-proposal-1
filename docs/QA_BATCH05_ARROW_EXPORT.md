# QA — Batch 05 (Slides 21–25) and arrow export comparison

**Date:** 2026-11-16. **Scope:** Five new editable Traditional Chinese Chapter 3 slides.

## Completed
- Verified the current private thesis Chapter 3 (blob `84ba2e5423370aca802298eecafde2311921599f`) and original method diagram before authoring.
- Produced Slides 21–25: MNB candidate estimation, within-group subspace screening, randomized constrained MNB initialization, PSO and majority-vote ensemble, feature-sampling weight update/stopping logic.
- Used source-grounded `D_fit` versus `D_search` roles and final-only held-out testing; did not manufacture empirical results or hyperparameter values.
- Created all graphics as editable native PowerPoint objects and used **11 real line-arrowhead connectors** (not disjoint line+chevron parts). Each arrow has audited endpoints and explicit source/target semantics; **zero off-canvas shapes**.
- Corrected initial draft on Slide 25: removed two unattached branch arrows, replacing them with clearly labeled mutually exclusive outcomes.
- Rendered the PPTX to PDF and PNG, inspected all five slides. Saved exact source LaTeX and Traditional Chinese speaker notes in local/private delivery only, for final Office Math conversion.
- Imported a temporary Canva intermediary and appended pages **one by one** to the user's existing canonical Canva master. Verified the **25-page** count and correct titles/order 21–25 from Canva rich-text extraction. Prior 20 pages were not replaced.

## What the conversion tests do and do not prove
A local **PPTX → LibreOffice → PPTX** round trip preserved every native end-arrowhead on Slides 21–25: `2,1,2,3,3` before and after, total **11/11**.

The **old Batch 02 slides** used separate chevrons plus lines. After the same round trip, the original components remained separate: Slide 6 `11 chevrons + 15 lines`, Slide 7 `11 chevrons + 14 lines`, Slide 8 `2 chevrons + 2 lines` (unchanged). **Conversion alone did not repair these arrows.**

**This is not a Canva → PowerPoint export test.** No Canva-to-PPTX export capability is exposed by current connected Canva tools. Exact downstream fidelity of the current user-edited Canva master requires an actual Canva-exported `.pptx` for verification. Do not claim the issue is resolved automatically.

## Outstanding item
The locally redesigned arrow versions for prior Slides **6, 7, 8, 11, 12, 14, 15** have **not** replaced the user's hand-adjusted original Canva slides; approval and preservation of user edits are needed before page replacement.

## Next batch
Slides 26–30: experimental datasets/feature representation, evaluation procedure and comparisons, planned analyses, contributions/future work, references/Q&A. Keep Traditional Chinese, no tiny irrelevant bottom sources, one master Canva deck, explicit distinction between proposed and completed research, and export-level arrow QA.
