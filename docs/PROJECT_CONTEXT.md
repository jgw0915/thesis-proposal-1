# Project context

## Purpose
Create an English-language, academically professional **first thesis proposal** presentation for a master's student in the Institute of Information Management, National Cheng Kung University, supervised by Prof. Tzu-Tsung Wong (翁慈宗).

Official thesis metadata from `Master-Thesis/frontmatter/thesis-info.tex`:
- English: **A Randomly Generated Multinomial Naive Bayes Ensemble Method for High-Dimensional Data Classification**
- Chinese: **高維度資料分類之隨機生成多項式簡易貝氏集成方法**
- Author: **Kuan-Wei Chiang / 江冠緯**
- Advisor: **Tzu-Tsung Wong / 翁慈宗**

Do not treat the above proposal's date as fixed; check latest event date before filling cover.

## Research problem
Direct random generation of the complete MNB conditional probability table has a search dimension that grows with feature count and class count. High-dimensional inputs can make repeated candidate generation and PSO expensive. Restricting each base model to informative feature subsets, with iterative sampling-weight updates, may help balance predictive quality and construction time.

## Actual method in current thesis Chapter 3 (verify against latest)
1. Extract **count-valued** features for text (term frequency) or DNA sequences (overlapping **8-mers**, per checked 2026-11 thesis version).
2. Use stratified K-fold evaluation and separate train and test; inside training use `D_fit` and `D_search` for different roles.
3. Score features and initialize sampling weights; sample candidate feature subspaces.
4. Estimate conventional MNB models for sampled subspaces using `D_fit`; screen/select candidates using `D_search`.
5. Within selected subspaces, randomly generate MNB parameters and apply PSO to search candidate models.
6. Assemble one selected model per retained group into an ensemble; update feature sampling weights based on selected subspaces and repeat as defined.
7. On termination, use the ensemble specified by latest method text; evaluate on held-out test fold.
8. Compare against designated baselines and ablations without leaking test information into development.

The original text contains precise algorithm, notation and thresholds; these notes **do not replace the source**.

## Planned data and evaluation
- Target categories: **documents** and **genetic/DNA sequences**.
- Preferred high-dimensional dataset scale: at least **5,000 features** and **500 samples**.
- Key outcomes: classification accuracy and training/model-search computation cost; evaluate stability and other metrics only when backed by thesis plan.
- Proposed versus completed experiment must be visually and verbally differentiated.

## Scope of slide production
- Working target ~30 slides (including cover/contents/references); it may be adjusted based on readability.
- Prior prior-session direction: ~2 slides for cover+TOC, ~3 introduction, ~10 literature review and ~10 method; use rest for experiment plan, contribution, closing, references.
- The **quality of communication** takes precedence over exact chapter quotas.
- The deck should be English, with Traditional Chinese speaker notes optional.

## Explicit non-goals
- Not a complete post-experiment defense. Do not borrow the senior's actual experiment outcome pages.
- Not a reproduction of the senior's GA approach.
- Not an automatic copy of old presentations. Preserve design grammar, redesign visuals around this research.
