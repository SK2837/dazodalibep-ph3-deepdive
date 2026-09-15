# Dazodalibep Phase 3 Deep Dive

A clinical/statistical deep dive on Amgen's dazodalibep Phase 3 program in Sjögren's
disease (**NCT06104124** and **NCT06245408**), building toward an evidence-backed call
on whether the primary efficacy endpoint(s) will read out positive or negative.

## Scope

- **NCT06104124** (systemic disease activity, ESSDAI-based) — full treatment: biological
  rationale, Phase 2→Phase 3 bridge, statistical risk profile, competitor and historical
  benchmarking, quantitative scenario modeling, and an explicit thesis.
- **NCT06245408** (symptomatic disease, ESSPRI-based) — lighter treatment: trial design,
  risk-profile comparison against the primary trial, and a directional (non-modeled) read.

Analysis is scientific/statistical only — no valuation, peak-sales, or DCF work.

## Status: Day 1 complete (foundational research)

All Day 1 deliverables are in this repo as sourced, fact-checked reference documents.
See [`DAY1_SUMMARY.md`](DAY1_SUMMARY.md) for a plain-language walkthrough of what was
done and how each data point was sourced.

| File | Contents |
|---|---|
| [`PROJECT_PLAN.md`](PROJECT_PLAN.md) | Overall scope, day-by-day plan, and rationale for the primary/secondary trial split |
| [`phase2_results_verified.md`](phase2_results_verified.md) | Dazodalibep Phase 2 results, verified against the primary published source (both cohorts) |
| [`NCT06104124.csv`](NCT06104124.csv) / `.xlsx` | Primary trial registry data (ClinicalTrials.gov, verified) |
| [`NCT06245408.csv`](NCT06245408.csv) / `.xlsx` | Secondary trial registry data (ClinicalTrials.gov, verified) |
| [`essdai_measurement_properties.md`](essdai_measurement_properties.md) | ESSDAI measurement-property literature: MCID, placebo-response model, composite-index (CRESS/STAR) check |
| [`sjogrens_competitor_trials.csv`](sjogrens_competitor_trials.csv) / `.xlsx` | Full landscape of Sjögren's trials across dazodalibep, ianalumab, and iscalimab |
| [`ianalumab_competitor_analysis.md`](ianalumab_competitor_analysis.md) | Ianalumab Phase 2b and Phase 3 (NEPTUNUS-1/-2) design and results |
| [`historical_base_rate_table.md`](historical_base_rate_table.md) | Historical Sjögren's trial track record across 8 drugs/mechanisms |
| [`nct06245408_esspri_risk_note.md`](nct06245408_esspri_risk_note.md) | Placebo-response risk read for the secondary (ESSPRI-based) trial |

All source PDFs (the Phase 2 publication and reference materials) are kept local and
excluded from this repo via `.gitignore` due to copyright/confidentiality.

## Next: Day 2

Bull/base/bear scenario modeling for NCT06104124's primary endpoint, a
minimum-detectable-effect calculation off its actual enrollment (N=651), and the
explicit positive/negative thesis — see `PROJECT_PLAN.md` for the full day-by-day plan.
