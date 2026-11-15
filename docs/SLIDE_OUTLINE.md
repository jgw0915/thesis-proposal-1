# 論文計畫口試投影片大綱 — v0.2（繁體中文）

**投影片全程使用繁體中文，技術縮寫可保留原文；不得在頁底放細小的來源文字列。** 詳見 `docs/SLIDE_WRITING_RULES.md`。

**Working target: ~31 slides including three optional appendices, with 28 slides in the main presentation.** Presentation quality and correctness trump slide-count targets. Slides 1–31 have editable drafts in one Canva master after user-directed ending restructure; layout/source/arrow/final PowerPoint QA remains pending. All displayed slide text must be Traditional Chinese. Section organization follows the user's requested first three thesis chapters with proposal-specific experiment plan rather than fabricated results.

| # | Section | 投影片標題 | Main visual / message | Source |
|---:|---|---|---|---|
| 1 | Cover | 高維度資料分類之隨機生成多項式簡易貝氏集成方法 | Senior-inspired title page with metadata | thesis-info.tex |
| 2 | TOC | 簡報大綱 | Introduction → Literature Review → Proposed Method → Experimental Plan → Conclusion | deck structure |
| 3 | Introduction | 高維度資料的分類問題 | Count-valued sparse documents and DNA sequences: many attributes, few observations relative to feature count | Ch. 1 |
| 4 | Introduction | 研究動機：參數搜尋負擔 | Parameter dimension grows with features/classes; search cost motivation | Ch. 1 |
| 5 | Introduction | 研究目的 | feature-subspace search + random MNB + PSO; accuracy/cost trade-off is a *hypothesis* | Ch. 1 |
| 6 | Literature | 集成學習概觀 | bagging, boosting, randomly generated models, key differences | Ch. 2 §2.1 |
| 7 | Literature | 袋裝法與提升法 | independent resampling vs sequential weighting | Ch. 2 §2.1 |
| 8 | Literature | 隨機生成基本模型 | what is randomized and why model diversity matters | Ch. 2 §2.1 |
| 9 | Literature | 多項式簡易貝氏（MNB） | count features, class priors, normalized conditional probabilities | Ch. 2 §2.2 |
| 10 | Literature | 其他高維度分類方法 | short positioning of MNB relative to other approaches | Ch. 2 §2.2 |
| 11 | Literature | 高維度特徵選取 | feature ranking and selection benefits / costs | Ch. 2 §2.3 |
| 12 | Literature | 隨機特徵子集合 | compare models on subsets rather than full feature universe | Ch. 2 §2.3 |
| 13 | Literature | 高維度集成學習 | complementary ensemble + feature selection research | Ch. 2 §2.4 |
| 14 | Literature | 以 PSO 搜尋隨機基本模型 | summarize published PSO motivation, careful distinction from new proposal | Ch. 1/2 references |
| 15 | Literature | 文獻小結與研究缺口 | high-dimensional MNB parameter-space cost vs informative subspaces | Ch. 2 summary, Ch. 1 |
| 16 | Method | 研究方法整體流程 | full thesis Figure 3.1, red highlights for major stages | Ch. 3 §3.1 |
| 17 | Method | 特徵萃取：文件與 DNA | term frequencies and overlapping 8-mer counts | Ch. 3 §3.2.1 |
| 18 | Method | 資料切分與避免資料洩漏 | outer K-fold, fit/search split, held-out test | Ch. 3 §3.2.2 |
| 19 | Method | 特徵評分與初始抽樣權重 | feature score distribution/weight concept, verified equations | Ch. 3 §3.3.1 |
| 20 | Method | 候選特徵子集合抽樣 | weighted subsets and candidate groups | Ch. 3 §3.3.2 |
| 21 | Method | 建立候選 MNB 模型 | train conventional MNB on candidate feature subsets | Ch. 3 §3.3.3 |
| 22 | Method | 特徵子集合篩選 | rank/select subset candidates using search data | Ch. 3 §3.3.4 |
| 23 | Method | 隨機生成 MNB 參數 | valid class-conditional parameter vector, simplex constraints | Ch. 3 §3.4.1 |
| 24 | Method | PSO 搜尋與集成建立 | PSO refinement in selected subspaces, one best model/group | Ch. 3 §3.4.2, §3.1 |
| 25 | Method | 特徵抽樣權重更新 | iterative feedback, final-iteration ensemble according to current text | Ch. 3 §3.5 |
| 26 | Experiments | 實驗規劃（僅一頁） | planned document/DNA count data, thresholds, identical splits/member count, Chi-square + Bagging–MNB, accuracy mean/std + time | Ch. 3 §3.6 |
| 27 | Conclusion | 預期研究貢獻 | integration, iterative feature sampling, evaluation without claiming results | Ch. 1 objectives / Ch. 3 |
| 28 | Thank You | 謝謝各位老師／敬請指教 | final slide of spoken presentation / Q&A | presentation framing |
| 29 | Appendix A | 資料切分與使用範圍 | separate D_fit, D_search and held-out test; prevent leakage | Ch. 3 §3.2 |
| 30 | Appendix B | 隨機 MNB 與 PSO 有效參數 | normalized probability constraints and PSO search roles | Ch. 3 §3.4 |\n| 31 | Appendix C | JMH 與特徵抽樣權重 | one-time JMH scoring, adaptive feature probabilities and convergence | Ch. 3 §3.3/§3.5 |

## Production notes
- For slides 19, 23, 24, 25 use **verified exact equations** from current Chapter 3; do not invent notation.
- Slide 26 is the **only** experimental-plan slide. Main presentation ends with Thank You on Slide 28. Slides 29–31 are backup-only appendices, not spoken by default.
- Keep the senior's **header/footer/section navigation style**, not senior's GA/BIP/COMEP content.
- **No standalone reference page** in proposal; preserve appropriate scholarly attribution and source record in the thesis/speaker notes.
- Keep private Traditional Chinese speaker-note drafts per batch (not in this public repository); final combined notes are prepared after user design review.
