# Arrow audit and Batch 04 methodology QA

**Date:** 2026-11-16. **Canonical Canva master:** one continuing presentation (keep access URL out of public repository).

## Arrow audit — prior slides 1–15

From the currently available local PPTX authoring sources, the seven arrow-bearing pages were **6, 7, 8, 11, 12, 14 and 15**. Pages 1–5, 9–10, and 13 showed no directed arrow shape in the sources.

- Pages **6–7:** multiple repeated line + chevron components, overly complicated branching; replaced with native connectors and aligned source/target links.
- Page **8:** two linear transitions between literature-study panels; replaced chevrons with true directed connectors.
- Page **11:** selected-feature input flow; replaced with one horizontal native connector.
- Page **12:** three group→base-model transitions; replaced with vertically centered native arrows pointing downward.
- Page **14:** PSO path and process summary arrows; replaced with native direction-bearing lines; conceptual path remains illustrative.
- Page **15:** three research strands converging into proposed-method overview; replaced with three vertically aligned native arrows.

**Created:** one 7-page private/local editable replacement deck, and an accompanying rendered PNG contact sheet. Shape QA: 36 native segments, including 28 actual end-arrowheads; zero objects outside slide canvas. **These redesigned pages have not been substituted into the canonical Canva master.** Its API does not offer connector editing, and destructive page replacement must first be reviewed with the user's modifications protected. Local PPTX reconstruction cannot prove that every user-added Canva arrow is identical to the previous local authoring source. Mark the live Canva arrow-repair request as **pending approval of exact page replacements**.

## Batch 04 — Slides 16–20

- Read current authoritative `Master-Thesis/Chapter/Third Chapter.tex` and `figures/chapter3-method.drawio` to preserve actual algorithm ordering and data-split behavior.
- Built five slides with Traditional Chinese captions, editable objects and PPTX native arrowhead connectors: **16** method framework, **17** document/DNA count features, **18** outer train/test plus fit/search split, **19** JMH feature scoring and initial weights, **20** weighted without-replacement subspace sampling.
- Specifically distinguish `D_fit` for feature scores and candidate MNB estimation, `D_search` for selection/PSO scoring, and held-out test for **final-only evaluation**.
- Illustrate the last feature-weight iteration's ensemble as the final model; do not depict testing as a feedback/screening source.
- Keep all formulas as Canva-stage readable placeholders with their exact current LaTeX sources in a private manifest for final exported PPTX→native Office Math (OMML) post-processing.
- Slide 20's 3 groups × 3 displayed candidates is a **diagram illustration only**, not fixed `G=3` or `L=3`. No fabricated experimental results.
- Rendered local PPTX to PDF and PNG and visually reviewed; confirmed 5 slides, 25 native connector segments including 16 true end-arrowheads, and zero PPTX elements outside canvas.
- Appended each page individually, in order, to the **existing canonical Canva master**. Connector returned 20 pages, and extracted editable Chinese titles for Slides 16–20 in ascending order; preceding user edits were not replaced.
- **Canva API limitation:** page text/editability and returned thumbnail metadata can be verified; exact arrowhead visuals in the live Canva renderer should still be checked in Canva before final presentation and after PPTX export.

## Next production

Batch 05: Slides 21–25, candidate MNB estimation/screening, random MNB probability generation, PSO search/ensemble vote, weight update & convergence. Re-read Chapter 3 and current method diagram first; use native connected arrows, exact formulas via LaTeX source manifest, and render QA. Continue appending to same single Canva project.

**Public repo safeguard:** neither private theorem/formula files, speaker scripts, deck binaries nor Canva edit links belong in this public repository.
