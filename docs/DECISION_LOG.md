# Design and content decision log

| Date | Decision | Reason | Status |
|---|---|---|---|
| 2026-11-16 | Use dedicated `thesis-proposal-1` repository for slide work; reference `Master-Thesis` for content | prevent context loss and scientific drift | adopted |
| 2026-11-16 | Match senior's red/tan/off-white serif editorial design, with improvements to grid and accessibility | preserve lab-family visual identity | adopted |
| 2026-11-16 | Do not upload senior's original PPTX to current public repo | protect private/copyrighted source | adopted |
| 2026-11-16 | Outline 30 proposed slides with 3 intro, 10 literature, 10 method, 3 experiment, 2 closing, 2 cover/TOC | user preference and communication pacing | provisional |
| 2026-11-16 | No fabricated experimental results or confirmed hyperparameter claims | this is a proposal | adopted |
| 2026-11-16 | Source priority: current thesis text over remembered draft or senior's contents | academic consistency | adopted |
| 2026-11-16 | Supersede prior auto-generated deck design with a fresh editorial build; work in 5-slide batches | user rejected earlier visual quality; review in manageable units | adopted |
| 2026-11-16 | Build native-editable 20×11.25 in PowerPoint layouts; import into a separate Canva project | maintain technical editability and ease of iterative edits | adopted |
| 2026-11-16 | Use Georgia bold italic fallback for Cormorant Garamond and Lato for compact navigation | source font unavailable; improved visual legibility | working design |
| 2026-11-16 | Do not commit the thesis-derived slide content, speaker script, binary deck or edit URLs while this repo is public and Master-Thesis is private | avoid inadvertently disclosing unpublished/private thesis material | adopted |
| 2026-11-16 | Flag disagreement between current manuscript and secondary editable flow diagram for advisor verification in future method batch | prevent silent invention or inconsistent final-ensemble rule | pending verification |

| 2026-11-16 | Use Traditional Chinese for every slide-facing label; English permitted for standard research abbreviations only | explicit user correction after inspecting Canva deck | adopted (overrides original English plan) |\n| 2026-11-16 | Remove irrelevant miniature bottom resource/source strings; preserve appropriate contextual scholarly citation and references | user identified unnecessary source strips as distracting | adopted |\n| 2026-11-16 | Create a new Chinese Canva batch rather than overwrite user's manually adjusted original; preserve adjusted five-section contents format | protect user edits during reconstruction | adopted |\n\n| 2026-11-16 | Produce literature review slides 6–10 as separate editable batch, retaining chapter subsection numbering and citation placement rules | efficient QA without overwriting user's Canva adjustments | adopted; batch delivered |


| 2026-11-16 | Use Canva's LaTeX Math app for formal equations and preserve original TeX inputs; do not claim app usage if tool access is missing | user requested professional notation rather than Unicode-only equations | adopted; plugin-insertion pending |
| 2026-11-16 | Continue future slide batches in a single canonical Canva presentation (original first-batch design), preserving manual edits | user explicitly rejected one presentation per batch | adopted; slides 1–10 consolidated |
| 2026-11-16 | Repair the appended batch order to 6,7,8,9,10 after Canva merged the five pages in reverse | ensure coherent slide sequence | verified |

| 2026-11-16 | Final presentation will be an exported PowerPoint PPTX; defer formal LaTeX→native Office Math (OMML) conversion until exported PPTX is uploaded | keeps Canva workflow fast and ensures equations can be edited in desktop PowerPoint | adopted; replaces mandatory Canva LaTeX-app insertion |
| 2026-11-16 | Maintain private LaTeX equation manifests during Canva production, and QA final OMML math independently after export | correct scientific notation and PowerPoint editability | adopted |

| 2026-11-16 | Keep Batch 03 as native-editable Traditional Chinese literature-review pages and append individually to the canonical Canva project | preserve user changes, avoid reversed group ordering | adopted; verified 15 pages |
| 2026-11-16 | Plan native Office Math conversion only on the final Canva-exported PPTX; keep mathematical source manifests during slide authoring | final presentation is PowerPoint and needs editable equations | adopted; pending final export |

| 2026-11-16 | Replace manually separated line+chevron arrow graphics with native arrowhead connectors; require source-target and Canva post-import QA | existing arrow alignment and direction were unreliable | adopted; seven local replacement pages prepared, live swap pending approval |
| 2026-11-16 | Continue method Slides 16–20 in the existing canonical Canva presentation, one page per merge for reliable order | preserve users edits and prevent reversed insertion | adopted; 20-page master verified |

| 2026-11-16 | Do not assume Canva-to-PowerPoint conversion repairs faulty arrow geometry; require testing the actual Canva-exported PPTX | round-trip of original chevrons preserved broken component structure, whereas native connectors retained arrowheads | adopted; actual export QA pending |
| 2026-11-16 | Append Batch 05 editable slides 21–25 to same master; remove floating branch arrows at design stage | rigorous method flow and connector alignment | adopted; canonical 25-page master verified |

| 2026-11-16 | Deliver Slides 26–30 as editable planned-evaluation and conclusion/Q&A draft; append them to the existing master and preserve manual edits | user asked to complete next batch, full thesis results not yet available | adopted; all 30 drafts verified |
| 2026-11-16 | Label dataset count thresholds as eligibility criteria, not measured dataset statistics; keep reference list selected and traceable to the thesis BibTeX | academic accuracy and no fabricated results | adopted |

## Pending confirmation (not blockers to drafting)
- Final list of experimental datasets and fixed hyperparameters.
- Confirm actual font fidelity in the online editor and final PowerPoint projector environment.
- Change the presentation repository's visibility to private before committing unpublished slide content and speech notes.
