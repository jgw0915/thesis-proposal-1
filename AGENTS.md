# AI agent instructions — thesis-proposal-1

These instructions apply to ChatGPT, Codex, and any editing agent.

## Required first reads
1. `README.md`
2. `docs/PROJECT_CONTEXT.md`
3. `docs/SOURCE_OF_TRUTH.md`
4. `docs/DESIGN_SYSTEM.md`
5. `docs/SLIDE_OUTLINE.md`
6. `docs/DECISION_LOG.md`
7. `docs/SLIDE_WRITING_RULES.md`
8. `docs/WORK_STATUS.md`

## Presentation mandate
Create a visually polished, editable, academically rigorous ~28–30-slide **thesis proposal**, strongly inspired by the *visual language* of the lab senior's deck (NOT its experimental content). Use a clean 16:9 landscape canvas; choose exact 20 x 11.25 in to match the source deck if compatible. Warm off-white background #F8F8F8, wine red #A31F34, muted tan #8C6E4A, predominantly black typography. Use large italic serif slide titles, restrained navigation, consistent page numbers, and spacious diagram-led composition. See DESIGN_SYSTEM for specific rules.

## Mandatory audience language and source placement
- **ALL slide-facing text must be Traditional Chinese (zh-TW)**, including cover, titles, table of contents, diagrams, top breadcrumbs, footer navigation, and Q&A. Preserve standard technical acronyms (MNB/PSO/DNA/8-mer) as needed.
- **Do not add small bottom source/resource text strips** (e.g., `Sources:`, thesis path, attribution captions not relevant to audience). Keep only the planned bottom navigation and slide number.
- Put essential scholarly attribution at the relevant claim/figure in readable type; place full references in speaker notes or the references section. Do not confuse omission of distracting footnotes with omission of citations.
- Preserve manual Canva edits by inspecting the current design and making an independent backup or version rather than overwriting without notice.
- For full details, follow `docs/SLIDE_WRITING_RULES.md`; this explicit 2026-11-16 decision overrides older English-language goals.

## Scientific correctness rules
- Thesis primary source: https://github.com/jgw0915/Master-Thesis (read live content on each major edit, especially `Chapter/Third Chapter.tex`).
- Thesis title: `frontmatter/thesis-info.tex`; do not override with guessed title.
- This thesis is about **high-dimensional document/DNA data**, **count-valued features**, **MNB**, **feature-subspace construction and adaptive weighting**, **randomly generated MNB parameters**, **PSO search**, and **ensemble construction**.
- Do not accidentally import the senior's GA / BIP ensemble-selection research as this thesis's own method.
- Distinguish proposal/hypothesis/planned evaluation from completed results. No fabricated datasets, results, comparisons or metrics.
- Chapter 3 describes a final ensemble from the last feature-weight iteration in the currently inspected version; check the current source before editing.
- Use `分類方法` as preferred Chinese term in narrative when referring to classification methods.
- Do not invent unconfirmed hyperparameters, method abbreviations, defense committee names, or proposal date.
- Cite sourced methods near the relevant claims, and preserve technical distinctions including fit/search/test leakage prevention.

## Editing and QA rules
- Output should be editable PPTX or a genuinely editable Canva/Slides project. Avoid rasterizing entire slides.
- Prefer native shapes, charts, editable text and vector figures. Keep editable diagrams in `assets/figures/`.
- Maintain 16:9, section navigation, slide numbers, consistent colors and styles.
- Each slide: one clear message, a legible main visual, minimal text; do not shrink text to fit.
- Never use private senior PPTX as a committed public asset without explicit permission.
- Read `docs/SLIDE_OUTLINE.md`; propose changes in `docs/DECISION_LOG.md`; keep `docs/CONTENT_MAPPING.md` accurate.
- Verify titles/formulas/figures against thesis source. Render PDF/PNG previews and inspect for collisions/cropping.
- Update `docs/WORK_STATUS.md` with actual work completed and next actions. Do not claim generation or upload unless verified.
- Never erase a user's manual design work without requesting or recording a deliberate redesign decision.

## Preferred workflow
Read current sources → update outline/mapping → create/edit a small batch of slides → render and visually inspect → fix layout and factual errors → update notes and decisions → commit.

## Public repo hygiene
Repository was public at setup. Do not push raw lab member slides, internal documents, private research data, access tokens, unpublished materials or proprietary assets. Use links/placeholder instructions in `assets/reference/`. Make repository private through GitHub settings before adding sensitive materials, subject to permissions.
