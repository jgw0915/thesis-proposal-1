# Thesis Proposal Slides — NCKU IM

A reproducible, AI-friendly workspace for developing the **master's thesis proposal presentation**.

- **Presentation repository:** https://github.com/jgw0915/thesis-proposal-1
- **Authoritative thesis source:** https://github.com/jgw0915/Master-Thesis
- **Thesis topic:** A Randomly Generated Multinomial Naive Bayes Ensemble Method for High-Dimensional Data Classification
- **Advisor:** Prof. Tzu-Tsung Wong, Institute of Information Management, National Cheng Kung University
- **Target presentation:** December 2026 thesis proposal; about 28–30 slides; scholarly, visually consistent, editable.

## Start here

1. Read [AGENTS.md](AGENTS.md) for the mandatory AI editing rules.
2. Read [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) for research goals and current scope.
3. Read [docs/DESIGN_SYSTEM.md](docs/DESIGN_SYSTEM.md) for the senior-slide-inspired design system.
4. Read [docs/SLIDE_OUTLINE.md](docs/SLIDE_OUTLINE.md) for slide-by-slide planning.
5. Check [docs/SOURCE_OF_TRUTH.md](docs/SOURCE_OF_TRUTH.md) before writing or changing scientific content.
6. Record accepted changes in [docs/DECISION_LOG.md](docs/DECISION_LOG.md).
7. Use [prompts/SESSION_START.md](prompts/SESSION_START.md) when beginning a new ChatGPT or Codex session.

## Repository organization

- `docs/` — requirements, design guidelines, mapping, QA, decisions and workflow.
- `config/` — machine-readable slide and style definitions.
- `prompts/` — reusable AI instructions for drafting and reviewing.
- `assets/reference/` — instructions for managing the lab senior's source deck privately.
- `assets/figures/` — editable diagrams and derived figure assets.
- `slides/` — editable working PPTX / design exports when available.
- `exports/` — PDF and preview exports.
- `notes/` — presentation script and rehearsal notes.
- `scripts/` — optional reproducible production tools.

## Source priority

The *latest checked* `Master-Thesis` chapter files, thesis metadata, references and figures are more authoritative than this repository's planning files. This repository is for **presentation development**, not a fork of the thesis manuscript.

## Important boundaries

- This is a **proposal**, not a completed defense. Do not invent results, experiments, accuracy numbers or performance claims.
- The reference presentation is a **style reference only**, not a scientific source for this thesis. Do not copy its method (GA/BIP ensemble selection) into the new method.
- Use Traditional Chinese terminology where appropriate; prefer **「分類方法」** in narrative slides.
- Never upload the graduate senior's complete deck or other non-public material to a public repository without permission. This repository was **public** when initialized; change visibility manually in GitHub settings if sensitive assets must be stored.
- Git stores files, but new ChatGPT conversations do not automatically read them. Ask the agent to load `AGENTS.md` and the source documents each time.
