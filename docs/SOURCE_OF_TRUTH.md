# Source of truth and verification

## Thesis GitHub repository (highest priority)
https://github.com/jgw0915/Master-Thesis

Relevant files:
- [Metadata](https://github.com/jgw0915/Master-Thesis/blob/main/frontmatter/thesis-info.tex) — official title, author, advisor
- [Chapter 1](https://github.com/jgw0915/Master-Thesis/blob/main/Chapter/First%20Chapter.tex) — motivation/objectives
- [Chapter 2](https://github.com/jgw0915/Master-Thesis/blob/main/Chapter/Second%20Chapter.tex) — prior work
- [Chapter 3](https://github.com/jgw0915/Master-Thesis/blob/main/Chapter/Third%20Chapter.tex) — method, data splitting, experiments
- [Current method diagram](https://github.com/jgw0915/Master-Thesis/blob/main/figures/chapter3-method.drawio) — editable flowchart source
- [Training split diagram](https://github.com/jgw0915/Master-Thesis/blob/main/figures/chapter3-training-split.drawio)
- [References](https://github.com/jgw0915/Master-Thesis/tree/main/style)
- [Main README](https://github.com/jgw0915/Master-Thesis/blob/main/README.md) — version history and notes

## Secondary visual reference
The graduate lab senior's supplied file: **Yizh_口試論文(1).pptx**. Inspected as a style reference. It contained 67 slides on a 20 x 11.25 inch 16:9 canvas. Treat its **layout, typography, navigation hierarchy, red/tan palette, numbering, and diagram pacing** as useful design evidence. The file is **not committed** to this public repository. Ask user to reattach or provide securely when pixel-level comparison is necessary.

## Source priority
1. Current thesis code/text and original methods (for research-specific claims).
2. Explicit professor/user corrections from the current session (track in decision log).
3. Slide repo plan and mapping documents (for communication, format, structure).
4. Senior slides (VISUAL style ONLY).
5. Verified cited published papers (external background).

## Verification checklist
- Check source commit and date before claim that something is latest.
- Cross-check every formula symbol: Chapter 2 and Chapter 3 may use `K` and `M` differently; retain local equation-specific definitions, **do not assume** symbols are globally identical.
- Identify speculative model initialization choices and unresolved settings rather than assigning values.
- 8-mer produces up to 4^8 possible DNA strings over A/C/G/T, but observed vocabulary and preprocessing rules may differ; do not claim exact feature count for a dataset without verification.
- Explicitly label future experiments/results as planned.
- Maintain references to the relevant thesis sections and papers.
