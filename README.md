# Dazodalibep Phase 3 Deep Dive

A clinical/statistical deep dive on Amgen's dazodalibep Phase 3 program in Sjögren's
disease (**NCT06104124** and **NCT06245408**), building toward an evidence-backed call
on whether the primary efficacy endpoint(s) will read out positive or negative.

**Start here if you're new to this project: [`PROJECT_STATUS.md`](PROJECT_STATUS.md)**
(also available as [`PROJECT_STATUS.pdf`](PROJECT_STATUS.pdf)) — a full explanation of
what's been done, the current bull/base/bear numbers and final call, what the
reference deck says and how it's being used, and an honest review against the brief.
This README is just the file index.

## Scope

- **NCT06104124** (systemic disease activity, ESSDAI-based) — full treatment: biological
  rationale, Phase 2→Phase 3 bridge, statistical risk profile, competitor and historical
  benchmarking, quantitative scenario modeling, and an explicit thesis.
- **NCT06245408** (symptomatic disease, ESSPRI **and DASPRI**-based) — lighter
  treatment: trial design, risk-profile comparison against the primary trial, and a
  directional (non-modeled) read.

Analysis is scientific/statistical only — no valuation, peak-sales, or DCF work.

## Status: Day 1 and Day 2 complete; corrected after external review (Sept 15, 2026)

An external review identified several factual and statistical errors in the Day 1/2
work — most significantly: ianalumab's Phase 2b was originally mischaracterized as a
missed primary endpoint (it actually met its primary dose-response objective), the
historical trial comparison used inconsistent success criteria across trials, a
statistical calculation understated variance and overstated confidence, and the
secondary trial's DASPRI co-primary endpoint was missing from the narrative entirely.
All of these have been corrected — each corrected file carries its own "correction
note." The review itself was not fully accurate either (see the correction note in
`02_research/phase2_baseline_characteristics.md`) — corrections were applied only
after re-verifying against primary sources, not accepted at face value.

## Folder structure

```
├── README.md                  ← you are here
├── PROJECT_PLAN.md            ← original scope/day-by-day plan
├── PROJECT_STATUS.md/.pdf     ← full current-state explanation (read this first)
├── 00_reference/              ← source PDFs + the external review
├── 01_data/                   ← ClinicalTrials.gov registry exports (CSV)
├── 02_research/               ← Day 1 findings (Phase 2 data, ESSDAI literature, competitors)
├── 03_analysis/               ← Day 2 modeling (scenario model, final thesis)
├── 04_summaries/              ← plain-language recaps
└── 05_deck/                   ← Day 3/4 presentation output (not yet started)
```

## File index

| File | Contents |
|---|---|
| [`00_reference/phase2_paper.pdf`](00_reference/phase2_paper.pdf) | St. Clair et al. 2024, Nature Medicine — the Phase 2 trial publication (CC-BY 4.0 open access) |
| [`00_reference/reference_deck_maestro_nash.pdf`](00_reference/reference_deck_maestro_nash.pdf) | Jefferies' MAESTRO-NASH analyst deck — the supplied template for analytical depth/slide anatomy |
| [`00_reference/external_review.md`](00_reference/external_review.md) | The external review that prompted the correction pass |
| [`01_data/NCT06104124.csv`](01_data/NCT06104124.csv) | Primary trial registry data (ClinicalTrials.gov, verified) |
| [`01_data/NCT06245408.csv`](01_data/NCT06245408.csv) | Secondary trial registry data — lists both ESSPRI and DASPRI as co-primary outcomes |
| [`01_data/competitor_trials_landscape.csv`](01_data/competitor_trials_landscape.csv) | Full landscape of Sjögren's trials across dazodalibep, ianalumab, and iscalimab |
| [`02_research/phase2_results.md`](02_research/phase2_results.md) | Dazodalibep Phase 2 results, verified against the primary source (both cohorts); corrected safety detail and RA/SLE subgroup data |
| [`02_research/phase2_paper_explained.md`](02_research/phase2_paper_explained.md) | Plain-language walkthrough of the Phase 2 paper and the Phase 2→3 bridge logic |
| [`02_research/phase2_baseline_characteristics.md`](02_research/phase2_baseline_characteristics.md) | Full Table 1 baseline data, both populations |
| [`02_research/essdai_measurement_properties.md`](02_research/essdai_measurement_properties.md) | ESSDAI literature: MCID (within-patient scope, corrected), placebo-response model, CRESS/STAR check |
| [`02_research/ianalumab_competitor_analysis.md`](02_research/ianalumab_competitor_analysis.md) | Corrected: Ph2b met its primary (dose-response) objective; individual NEPTUNUS-1/-2 arm results |
| [`02_research/historical_trial_evidence.md`](02_research/historical_trial_evidence.md) | Qualitative evidence table across comparator trials — corrected TRACTISS/ETAP classifications, no probability figure |
| [`02_research/nct06245408_risk_note.md`](02_research/nct06245408_risk_note.md) | Secondary trial risk read — includes DASPRI |
| [`03_analysis/scenario_model.md`](03_analysis/scenario_model.md) | Statistical model — three-way variance sensitivity, scenario table labeled as assumptions, not forecasts |
| [`03_analysis/final_thesis.md`](03_analysis/final_thesis.md) | Final positive/negative call for NCT06104124, ranked evidence, counter-argument |
| [`03_analysis/additional_topics.md`](03_analysis/additional_topics.md) | Dose/exposure PK-PD bridge, clinical-meaning synthesis, readout interpretation table |
| [`03_analysis/evidence_table.md`](03_analysis/evidence_table.md) | Master evidence table — every material number, population/timepoint/analysis/source/uncertainty |
| [`04_summaries/day1_summary.md`](04_summaries/day1_summary.md) | Day 1 recap (historical record — see its correction note for what's superseded) |
| [`04_summaries/plain_english_summary.md`](04_summaries/plain_english_summary.md) | Full non-technical walkthrough of the whole project |

Note: the Phase 2 publication is CC-BY 4.0 open access, not restrictively
copyrighted — it's excluded from git for practical size/housekeeping reasons, not a
copyright concern. The Jefferies reference deck is excluded because it's proprietary
material, not for redistribution. Both are `*.pdf`-gitignored.

## Next: Day 3

Slide-by-slide outline for the presentation, to be built out in `05_deck/`. Per the
external review's Section 5 recommendations (a 20-slide + 6-appendix structure), this
has not yet started.
