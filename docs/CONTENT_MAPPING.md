# Slide-to-thesis content mapping\n\n**Slide language: Traditional Chinese (zh-TW).** No small bottom source/resource strips; use readable in-content attribution for specific papers, and notes/end references for complete citations. See `docs/SLIDE_WRITING_RULES.md`.

This file exists to prevent slides from drifting away from the latest thesis.

| Slide(s) | Thesis source | Required fidelity check |
|---|---|---|
| 1 | `frontmatter/thesis-info.tex` | official English title/author/advisor; date to verify |
| 3–5 | `Chapter/First Chapter.tex` | motivation/objectives exactly match; no completed performance claims |
| 6–15 | `Chapter/Second Chapter.tex`, `style/chapter2_references.bib` or current bib source | distinguish bagging, boosting, random models, high-dimensional feature selection |
| 16 | `Chapter/Third Chapter.tex` §3.1, `figures/chapter3-method.drawio` | reproduce exact dependencies and stopping logic |
| 17 | §3.2.1 | term frequency and 8-mer count semantics |
| 18 | §3.2.2 and `figures/chapter3-training-split.drawio` | D_fit, D_search, held-out test and K-fold |
| 19–22 | §3.3 | equations, initialization, candidate generation and selection |
| 23–24 | §3.4 | random MNB/PSO parameterization and valid normalization |
| 25 | §3.5 and §3.1 | sample-weight update; final ensemble selection interpretation |
| 26–28 | §3.6, dataset inspection materials | label design/planned experiments; validate real dataset metadata |
| 29 | Chapters 1 and 3 | expected vs validated contribution |
| 30 | cited bibliography | accurate citations, readable format |

## Change propagation
When Chapter 3 changes, re-check slides 16–28, diagrams and speaker notes. Record the source commit hash if available. If a slide explains a method choice that is not fixed in the current source, put **[VERIFY WITH ADVISOR]** in its working notes; remove before final delivery after confirmation.
