# Batch 06 — Slides 26–30 QA (2026-11-16)

**Production state:** All thirty proposed slides now exist as editable drafts in one continuing Canva master. This does **not** mean presentation-ready/final approval.

## Source fidelity
- Checked authoritative `Master-Thesis/Chapter/Third Chapter.tex` (blob `84ba2e5423370aca802298eecafde2311921599f`) §3.6 for K-fold evaluation, classification accuracy mean/std, execution time, and comparison with Chi-square feature selection + Bagging–MNB.
- Checked Chapter 1 research objectives and the current `style/chapter2_references.bib` (blob `23f4fc00bc76d1f809fbe44a26d79d296c829a3e`) for the bibliography slide.
- Slide 26: documents and overlapping DNA 8-mer count representations. At least **500 samples** and **5,000 features** are a **planned dataset-selection threshold**, not real verified statistics. Example vectors are explicitly marked demonstrative.
- Slides 27–28: comparison is planned, not completed. Uses identical data splits and ensemble member counts for the proposed method and Chi-square + Bagging–MNB; metrics are accuracy and elapsed computation time. No made-up accuracy, standard deviation, timing, or class-count results.
- Slides 29–30: proposed contributions only; brief references use Chinese-first ordering, then English by first author's family name, all grounded in the current thesis bibliography.

## Visual and structure QA
- Authored native/editable 20 × 11.25 inch (16:9) PPTX: five slides, traditional Chinese with source-method abbreviations allowed, warm off-white/wine/tan design and persistent numbered footer navigation.
- PDF and PNG previews generated and visually inspected.
- **Five native directed connectors**: 3 on Slide 27 and 2 on Slide 29; all source/target endpoints lie on centered card edges, all point right, and all use a native arrowhead (not detached chevrons).
- PPTX XML checked: five `a:tailEnd type="triangle"` objects and five `p:cxnSp` connectors. No objects outside slide bounds.
- Embedded Traditional Chinese speaker notes for all five slides. No formal display equations in this batch; still retain final PowerPoint Office Math review for earlier slides.

## Canva continuation verification
- Imported an intermediate editable five-page presentation **only to append**, not as a new canonical master.
- Appended pages individually to the user's existing single Canva master to avoid reversed order.
- Verified Canva returns **30 total pages**. The titles of Slides 26–30 appear in correct ascending order, and all text was returned as editable rich-text content.
- Existing hand-edited pages 1–25 were not replaced.

## Still pending
1. Review user's forthcoming feedback for the current Canva slides and refine requested pages without overwriting unrelated manual changes.
2. Previously arrow-redesigned slides 6, 7, 8, 11, 12, 14, 15 are **not yet swapped into the live Canva master**. User approval of the exact replacement scope is required.
3. Canva → PowerPoint export visual fidelity (especially arrows and spacing) **not tested** because the available Canva connector cannot export the master PPTX. Test the actual user-exported file.
4. LaTeX placeholders in earlier batches need PowerPoint-native OMML conversion after the user uploads the final exported PPTX.
5. Verify final dataset list and any final hyperparameters with the advisor; no unsupported precision is introduced here.

## Publication hygiene
The presentation repository is public while the thesis source is private. Do not commit source-derived slide binaries, speaker scripts, private editable Canva links, or senior deck assets to public GitHub.
