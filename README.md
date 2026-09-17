# Dazodalibep Phase 3 Deep Dive

A clinical and statistical analysis of Amgen's dazodalibep Phase 3 program in
Sjögren's disease, built to answer one question: **will the primary efficacy
endpoint(s) read out positive or negative**, and why. Prepared by Sai Adarsh Kasula
(Data Scientist / Biostatistician).

**The finished deliverable is `05_deck/FinalSubmission.pptx`.** Everything else in
this repository is the evidence, modeling, and review trail behind it.

## The call

We lean **positive** on **NCT06104124** (systemic disease activity, ESSDAI primary
endpoint), with material, explicitly quantified uncertainty — not a confident
prediction. The trial's size means it does not need to fully repeat Phase 2's
observed effect to succeed, but the honest variance range narrows that cushion
considerably compared to the most optimistic assumption. We lean **positive with a
wider error bar** on **NCT06245408** (symptomatic disease, ESSPRI + DASPRI), whose own
Phase 2 precursor produced the cleanest signal in the whole program, but which adds a
second primary instrument (DASPRI) with zero track record for this drug.

The single strongest reason this could go the other way: the only real precedent
available for how much a Phase 2 effect typically shrinks going into Phase 3
(a competitor drug, ianalumab) covers a much smaller scale-up than dazodalibep's own —
so there's no real precedent for what happens to its effect at this scale. Full
reasoning: `03_analysis/final_thesis.md`.

## What this project actually is

Amgen has two large, completed-or-completing Phase 3 trials testing dazodalibep — a
non-antibody protein that blocks the CD40L signal implicated in Sjögren's disease —
and hasn't announced results yet. This project builds a sell-side-analyst-style
forecast of that unannounced result using only public information: the drug's
published Phase 2 trial, the official trial registrations, competing drugs' results in
the same disease, and the published literature on how reliable the measurement tools
themselves are. It does not include valuation, peak-sales, or market-sizing work —
the scope is deliberately science and statistics only.

## How the evidence was built and checked

This isn't a single pass of research — it went through real correction cycles, and
that history is preserved rather than hidden, because it's part of what makes the
final numbers trustworthy:

1. **Primary-source research.** Every clinical number traces back to either the
   published Phase 2 paper (not a summary of it), the official ClinicalTrials.gov
   registration for each trial, or a competing drug's own published results —
   consolidated in `03_analysis/evidence_table.md`.
2. **An independent external review** (`00_reference/external_review.md`) caught
   several real errors in the first pass — most significantly, a competitor drug's
   early trial was mischaracterized as a failure when it had actually met its real
   prespecified objective, and a statistics calculation understated the uncertainty
   in the forecast.
3. **Those corrections were themselves re-verified against the primary sources**,
   not accepted on trust — in the process, some of the reviewer's own proposed
   "corrections" turned out to be wrong and were rejected (documented directly in
   `02_research/phase2_baseline_characteristics.md`). A second, independent review
   pass caught further real errors (an arithmetic mistake, a statistical framing
   issue) which were fixed the same way — verified, not assumed.

The result is a set of research files that say, explicitly, what was wrong at each
stage and why the current number is the one to trust — rather than a single clean
narrative that hides how the analysis actually got built.

## Repository structure

| Folder | What's in it |
|---|---|
| `00_reference/` | Source materials: the Phase 2 publication, the Jefferies-supplied reference deck (style template only, not reused for branding), and the external review that drove the correction pass |
| `01_data/` | Raw ClinicalTrials.gov registry exports for both trials plus the broader competitor landscape |
| `02_research/` | The evidentiary base — Phase 2 results and baseline data, the measurement-tool literature (ESSDAI/ESSPRI reliability), the competitor drug analysis, and the historical trial track record |
| `03_analysis/` | The actual modeling — the statistical scenario model, the additional supporting analyses (dose selection, clinical-meaning framing), the master evidence table, and the final thesis document with the explicit call |
| `04_summaries/` | Non-technical walkthroughs for a reader without a clinical or statistics background |
| `05_deck/` | Everything related to the presentation itself — see below |

### Inside `05_deck/`

| Item | What it is |
|---|---|
| `FinalSubmission.pptx` | **The deliverable.** |
| `companion_report.pdf` | A 41-page plain-language walkthrough of every slide, for a reader without the technical background |
| `content/` | The slide-by-slide content specification the deck was built from, plus the drafts and review that led to it |
| `build/` | The Python tooling used to generate the deck's charts and assemble the presentation, plus the pre-edit auto-built version of the deck (before manual refinement into `FinalSubmission.pptx`) |

## What's deliberately not resolved

Stated honestly rather than papered over:
- The exact statistical analysis plan for NCT06104124 (dose allocation, multiplicity
  correction across its two dose arms) is not public — the model tests a range of
  reasonable assumptions instead of picking one.
- Dazodalibep's own DASPRI results don't exist — the instrument doesn't appear
  anywhere in the Phase 2 publication at all, confirmed by a full-text search.
- A small enrollment discrepancy for a competitor trial (506 vs. 504, depending on
  source) is reported as-is rather than silently resolved to one figure.
- The deck's visual layout has not been checked by rendering it to images in this
  environment (no presentation software available here) — only its text and table
  content has been directly verified.

## Regenerating the deck

```bash
cd 05_deck
python3 -m venv .venv && source .venv/bin/activate
pip install python-pptx matplotlib scipy
python3 build/make_charts.py    # regenerates the chart/diagram images
python3 build/build_deck.py     # assembles the .pptx from content/final_slide_content.md
```
