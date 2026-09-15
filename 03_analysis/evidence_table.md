# Master Evidence Table

Single source of truth for every material claim/number used across this project's
files, per the external review's Priority 7 recommendation. Format: claim, number,
population, timepoint, analysis type, source, and uncertainty/caveat. Summaries in
other files should trace back to this table; if a number changes, update it here first.

## Dazodalibep Phase 2 (St. Clair et al., Nature Medicine 2024, PMID via DOI 10.1038/s41591-024-03009-3)

| Claim | Number | Population | Timepoint | Analysis | Source | Uncertainty |
|---|---|---|---|---|---|---|
| Primary endpoint, systemic | ESSDAI: DAZ −6.3±0.6 vs PBO −4.1±0.6, diff −2.2 (90% CI −3.6,−0.7), P=0.0167 | Pop 1, n=74 (36/38) | Day 169 | MMRM, prespecified primary, α=0.10 (2-sided) | Paper Table 2 | Small N; relaxed α threshold |
| Primary endpoint, symptomatic | ESSPRI: DAZ −1.8±0.2 vs PBO −0.5±0.2, diff −1.3 (90% CI −1.82,−0.73), P=0.0002 | Pop 2, n=109 (54/55) | Day 169 | MMRM, prespecified primary | Paper Table 2 | Small N |
| ESSDAI(3) responder | 72.2% DAZ vs 59.5% PBO, OR 1.6 (0.7-3.8), P=0.3283 | Pop 1 | Day 169 | Secondary, logistic | Paper Table 2 | Not significant; dichotomization loses info |
| ESSDAI(4) responder | 66.7% DAZ vs 48.6% PBO, OR 2.0 (0.9-4.6), P=0.1823 | Pop 1 | Day 169 | Secondary | Paper Table 2 | Not significant |
| ESSDAI(5) responder | 61.1% DAZ vs 35.1% PBO, P=0.0449 | Pop 1 | Day 169 | **Post hoc** | Paper p.1585 | Not prespecified |
| CXCL13 suppression | Adj. GMR to baseline vs PBO: 0.67 (Pop1, P=0.0010), 0.56 (Pop2, P<0.0001) | Both | Day 169 | Exploratory biomarker | Paper Results | Exploratory, not efficacy proof |
| RF suppression | Adj. GMR vs PBO: 0.66 (Pop1, P<0.0001), 0.54 (Pop2, P<0.0001) | Both | Day 169 | Exploratory biomarker | Paper Results | Exploratory |
| RA/SLE subgroup interaction | Placebo-adj. ESSDAI change ≈−1.6 (no RA/SLE) vs ≈−3.3 (with RA/SLE) | Pop 1 subgroup | Day 169 | Exploratory subgroup | Extended Data Table 1 | Small subgroup N; not a robust interaction claim |
| Death | n=1 (Population 1, DAZ-PBO stage II+FU) | Pop 1 | Stage II+FU | Safety | Table 3 | Investigator: unrelated to study drug |
| DVT + drug-induced liver injury | Same participant, both events | Pop 1, Stage II | Onset 180 days post-final dose | Safety, SAE/AESI | Paper Results + Table 3 | **Investigator-attributed as related** to study drug |
| Invasive ductal breast carcinoma | n=1 (Population 2, DAZ-PBO) | Pop 2, Stage II | Onset 139 days post-final dose | Safety, SAE/AESI | Paper Results | **Investigator-attributed as related** to study drug |
| Dose tested | 1,500mg only | Both | — | Design | Paper Methods | No dose-ranging performed |
| Molecular description | Tn3 scaffold, non-antibody, Fc-free fusion protein | — | — | Design/MOA | Paper Introduction | NOT "PASylated" — corrected error |
| Statistical threshold | α=0.10, two-sided (not standard 0.05) | Both | — | Design | Paper Methods | Explicitly relaxed due to small-N concern |

## NCT06104124 (Phase 3, primary trial)

| Claim | Number | Population | Timepoint | Analysis | Source | Uncertainty |
|---|---|---|---|---|---|---|
| Status | COMPLETED | — | Primary completion 2025-07-23 (ACTUAL) | Registry | ClinicalTrials.gov, verified [date of check: see chat] | Results not yet posted as of last check |
| Enrollment | N=651, 3 arms (2 doses + placebo) | — | — | Registry | ClinicalTrials.gov | Per-arm split (~217 assumed) not disclosed |
| Primary endpoint | ESSDAI change from baseline | — | Week 48 | Registry | ClinicalTrials.gov | SAP not public |
| Eligibility | ESSDAI≥5, anti-Ro/RF+ | — | — | Registry | ClinicalTrials.gov | Same floor as Phase 2 Pop 1 — not looser |

## NCT06245408 (Phase 3, secondary trial)

| Claim | Number | Population | Timepoint | Analysis | Source | Uncertainty |
|---|---|---|---|---|---|---|
| Status | ACTIVE_NOT_RECRUITING | — | Primary completion 2026-10-22 (ESTIMATED) | Registry | ClinicalTrials.gov | Not yet completed |
| Enrollment | N=434 | — | — | Registry | ClinicalTrials.gov | — |
| Primary endpoints | **ESSPRI change AND DASPRI change** (both) | — | Week 48 | Registry | `NCT06245408.csv` | Hierarchy between the two not disclosed — corrected, previously only ESSPRI was described |

## Ianalumab (Novartis)

| Claim | Number | Population | Timepoint | Analysis | Source | Uncertainty |
|---|---|---|---|---|---|---|
| Ph2b primary objective | **Dose-response test MET** — significant in 4/5 models (p<0.025 in 4, p=0.060 in 1) | N=190 | Week 24 | Prespecified MCP-Mod dose-response | Bowman et al., Lancet 2021 (PMID 34861168) | This is the actual primary result — corrected from earlier "missed" claim |
| Ph2b pairwise (secondary) | 300mg vs PBO: diff −1.92, P=0.0921 | N=190 | Week 24 | Secondary/supportive | Same | Not significant, and not the primary test |
| NEPTUNUS-1 primary | −6.4 vs −5.1, diff −1.3 (SE 0.66), P=0.0496 | N=275 (137/138) | Week 48 | Prespecified primary | ACR Convergence 2025 presentation | Narrow margin |
| NEPTUNUS-2 primary (monthly) | −6.5 vs −5.5, diff −1.0, P=0.041 | N=506 (registry) / 504 (conference) | Week 48 | Prespecified primary | ACR Convergence 2025 | **N discrepancy unresolved** — both figures reported |
| NEPTUNUS-2 primary (every-3-months) | Did not reach significance | Same N | Week 48 | Prespecified primary | ACR Convergence 2025 | Real dose-frequency-sensitivity data point |
| Pooled monthly analysis | −6.5 vs −5.3, P=0.0031 | Combined | Week 48 | Post hoc pooled | ACR Convergence 2025 | Not a substitute for two individually significant trials |

## Iscalimab (Novartis)

| Claim | Number | Population | Timepoint | Analysis | Source | Uncertainty |
|---|---|---|---|---|---|---|
| TWINSS Cohort 1 primary | Dose-response MET | **N=173** (44/43/43/43) | Week 24 | Prespecified MCP-Mod | Lancet 2024 (PMID 39096929) | Corrected — earlier version used N=273 (combined total) for this cohort |
| TWINSS Cohort 2 primary | ESSPRI diff −0.57 (95% CI −1.30 to 0.15), P=0.12 | N=100 (50/50) | Week 24 | Prespecified primary | Lancet 2024 | **Not significant** — useful counterevidence to assuming class-wide symptom benefit |

## Historical comparator trials

| Claim | Number | Population | Timepoint | Analysis | Source | Uncertainty |
|---|---|---|---|---|---|---|
| TRACTISS primary | 39.8% (rituximab) vs 36.8% (PBO), not significant | N=133 | Week 48 | ≥30% reduction fatigue OR oral dryness VAS (NOT ESSDAI) | Primary trial report | Corrected classification — not an ESSDAI-primary trial |
| ETAP primary | 52.7% (tocilizumab) vs 63.6% (PBO), P=0.14 | N=110 | Week 24 | Composite: ESSDAI≥3pt improvement + no new domain activity + no PGA worsening | Felten et al. | Corrected — not continuous ESSDAI alone; placebo numerically higher |
| ASAP-III primary | No significant difference | N=80 | Week 24 | Continuous ESSDAI | van Nimwegen et al. | Open-label extension (14.0→4.0) is uncontrolled, not proof of missed effect |

## Statistical model parameters (scenario_model.md)

| Claim | Number | Source/derivation | Uncertainty |
|---|---|---|---|
| SD assumption A | 3.65 | Backed out from dazodalibep Ph2 SEs | Most favorable of three; not the actual Ph3 variance |
| SD assumption B | 5.00 | Dazodalibep Ph2 protocol's own planning assumption | Paper methods |
| SD assumption C | 5.47 | Backed out from NEPTUNUS-1's reported SE≈0.66 | Only real external Ph3 benchmark available |
| MDE at 80% power | 0.98 (SD=3.65) / 1.34 (SD=5.00) / 1.47 (SD=5.47) | Calculated, n≈217/arm assumed | Per-arm N not confirmed by registry |
| Observed-significance threshold | ≈0.69 (SD=3.65, α=0.05) | Calculated | Different quantity than 80%-power MDE |

## Open/unresolved items (not yet independently verified in this table)
- NEPTUNUS-2 N: 506 vs 504 discrepancy not resolved to a single source of truth
- DASPRI results for dazodalibep Phase 2 Population 2 — mentioned in the paper's
  secondary endpoints but not yet pulled into this project's files
- Actual Phase 3 statistical analysis plan (variance assumption, multiplicity control,
  testing hierarchy) — not publicly available
- Population 2 fatigue placebo value (6.8 vs 6.9) — low-confidence either direction on
  direct re-reading of Table 1
