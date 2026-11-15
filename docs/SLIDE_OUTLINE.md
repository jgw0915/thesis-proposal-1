# Proposal slide outline — v0.1

**Working target: 30 slides.** Presentation quality and correctness trump slide-count targets. All slide titles/content are **proposed**, not yet finished presentation pages. Section organization follows the user's requested first three thesis chapters with proposal-specific experiment plan rather than fabricated results.

| # | Section | Proposed title | Main visual / message | Source |
|---:|---|---|---|---|
| 1 | Cover | A Randomly Generated Multinomial Naive Bayes Ensemble Method for High-Dimensional Data Classification | Senior-inspired title page with metadata | thesis-info.tex |
| 2 | TOC | Presentation Outline | Introduction → Literature Review → Proposed Method → Experimental Plan → Conclusion | deck structure |
| 3 | Introduction | High-Dimensional Classification | Count-valued sparse documents and DNA sequences: many attributes, few observations relative to feature count | Ch. 1 |
| 4 | Introduction | Motivation: Random MNB Search Cost | Parameter dimension grows with features/classes; search cost motivation | Ch. 1 |
| 5 | Introduction | Research Objectives and Contributions | feature-subspace search + random MNB + PSO; accuracy/cost trade-off is a *hypothesis* | Ch. 1 |
| 6 | Literature | Ensemble Learning Overview | bagging, boosting, randomly generated models, key differences | Ch. 2 §2.1 |
| 7 | Literature | Bagging vs. Boosting | independent resampling vs sequential weighting | Ch. 2 §2.1 |
| 8 | Literature | Randomly Generated Base Models | what is randomized and why model diversity matters | Ch. 2 §2.1 |
| 9 | Literature | Multinomial Naive Bayes | count features, class priors, normalized conditional probabilities | Ch. 2 §2.2 |
| 10 | Literature | High-Dimensional Classifiers | short positioning of MNB relative to other approaches | Ch. 2 §2.2 |
| 11 | Literature | Feature Selection | feature ranking and selection benefits / costs | Ch. 2 §2.3 |
| 12 | Literature | Random Feature Subspaces | compare models on subsets rather than full feature universe | Ch. 2 §2.3 |
| 13 | Literature | High-Dimensional Ensemble Learning | complementary ensemble + feature selection research | Ch. 2 §2.4 |
| 14 | Literature | PSO for Random Base-Model Search | summarize published PSO motivation, careful distinction from new proposal | Ch. 1/2 references |
| 15 | Literature | Research Gap | high-dimensional MNB parameter-space cost vs informative subspaces | Ch. 2 summary, Ch. 1 |
| 16 | Method | Proposed Framework at a Glance | full thesis Figure 3.1, red highlights for major stages | Ch. 3 §3.1 |
| 17 | Method | Feature Extraction: Documents and DNA | term frequencies and overlapping 8-mer counts | Ch. 3 §3.2.1 |
| 18 | Method | Data Partitioning and Leakage Control | outer K-fold, fit/search split, held-out test | Ch. 3 §3.2.2 |
| 19 | Method | Feature Scoring and Initial Weights | feature score distribution/weight concept, verified equations | Ch. 3 §3.3.1 |
| 20 | Method | Candidate Subspace Sampling | weighted subsets and candidate groups | Ch. 3 §3.3.2 |
| 21 | Method | Candidate MNB Model Construction | train conventional MNB on candidate feature subsets | Ch. 3 §3.3.3 |
| 22 | Method | Subspace Screening | rank/select subset candidates using search data | Ch. 3 §3.3.4 |
| 23 | Method | Random MNB Parameter Generation | valid class-conditional parameter vector, simplex constraints | Ch. 3 §3.4.1 |
| 24 | Method | PSO Search and Ensemble Assembly | PSO refinement in selected subspaces, one best model/group | Ch. 3 §3.4.2, §3.1 |
| 25 | Method | Feature Weight Update and Stopping | iterative feedback, final-iteration ensemble according to current text | Ch. 3 §3.5 |
| 26 | Experiments | Dataset Selection and Representations | documents and DNA; >=500 samples and >=5000 features are selection thresholds, not confirmed dataset statistics | Ch. 3 §3.6; dataset inspection |
| 27 | Experiments | Evaluation Protocol and Baselines | metrics, folds, Chi-square + Bagging–MNB and other planned baselines | Ch. 3 §3.6 |
| 28 | Experiments | Planned Ablations and Research Questions | feature selection/random generation/PSO contributions; no results | Ch. 3 §3.6; plan |
| 29 | Conclusion | Expected Contributions and Next Steps | hypotheses, intended contributions, limitations and future work | Ch. 1, Ch. 3 |
| 30 | References / Q&A | Selected References & Questions | key citations + Q&A; split if readability demands | bib and source |

## Production notes
- For slides 19, 23, 24, 25 use **verified exact equations** from current Chapter 3; do not invent notation.
- For slides 26–28, explicitly say `Experimental Design` or `Planned Evaluation` until evidence-backed results exist.
- Keep the senior's **header/footer/section navigation style**, not senior's GA/BIP/COMEP content.
- If Q&A and references are overcrowded, expand to 31 slides by splitting references.
- Include speaker-note draft for all slides in `notes/SPEAKER_NOTES.md`.
