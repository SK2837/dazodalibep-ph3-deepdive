# Ianalumab (Novartis) — Competitor Read-Through (Corrected)

**Major revision note:** the original version of this file stated that ianalumab's
Phase 2b trial "missed" its primary endpoint, based on the pairwise 300mg-vs-placebo
comparison (p=0.092). This was wrong. The trial's actual prespecified primary
objective was a **dose-response test**, which was met. The pairwise comparison and the
dose-response test are different statistical questions — citing only the pairwise
result was a real, material error that propagated into the historical base-rate table
and the final thesis. Corrected throughout below.

## Mechanism
Ianalumab = anti-BAFF-receptor monoclonal antibody with a dual mechanism: B-cell
depletion + blockade of BAFF-R survival signaling. Contrast with dazodalibep's T-cell
costimulation (CD40L) blockade.

## Phase 2b dose-ranging trial — NCT02962895 (Bowman et al., Lancet 2021, PMID 34861168)
N=190 (5mg/50mg/300mg/placebo, 1:1:1:1). Population: seropositive (anti-Ro/SSA+),
ESSDAI ≥6 (7-domain scoring).

**Primary objective: prespecified dose-response relationship (MCP-Mod) on continuous
ESSDAI change from baseline at Week 24 — NOT a pairwise dose-vs-placebo comparison.**

- **Result: primary objective MET.** Statistically significant dose-response
  relationship for ESSDAI in 4 of 5 dose-response models tested (p<0.025 in four
  models, p=0.060 in one).

**Individual pairwise arm results (secondary/supportive, not the primary test):**
| Arm | LS mean change | vs. Placebo (diff) | p-value |
|---|---|---|---|
| Placebo | −6.39 | — | — |
| 5mg | −5.64 | +0.75 | 0.5161 |
| 50mg | −6.93 | −0.55 | 0.6332 |
| 300mg | −8.30 | −1.92 | 0.0921 |

None of the individual pairwise comparisons reached significance at α=0.05 — but this
does not mean the trial "failed," because the pairwise comparisons were not the
primary analysis. The dose-response test the trial was actually powered and designed
around was positive.

**Correction (caught in a second review pass): the earlier claim that "placebo's own
decline exceeded 2 of 3 drug doses" was an arithmetic error.** Placebo (−6.39) only
exceeded the 5mg arm (−5.64) — the 50mg arm (−6.93) actually declined *more* than
placebo, i.e. numerically outperformed it. So placebo exceeded exactly **one** of the
three doses (5mg), not two. This is still a real, worth-noting placebo-response
observation for the lowest dose, but it doesn't extend to 50mg, and it doesn't
override the fact that a significant monotonic dose-response was demonstrated across
the full model set.

**Secondary endpoint (supportive, not primary):** Physician's Global Assessment at
Wk24 showed clear dose-ordered separation (300mg −31.99 vs placebo −23.64), and
CD19+ B-cell depletion was clean and dose-dependent — consistent with a real,
dose-ordered biological effect alongside the ESSDAI dose-response finding.

## Phase 3 program — NEPTUNUS-1 and NEPTUNUS-2

| | NEPTUNUS-1 (NCT05350072) | NEPTUNUS-2 (NCT05349214) |
|---|---|---|
| Design | 2-arm, ianalumab 300mg SC monthly vs. placebo, 52 wks | 3-arm, ianalumab 300mg SC monthly OR every 3 months vs. placebo, up to 52 wks |
| N | 275 (137/138 per arm) | **506 per ClinicalTrials.gov registry; 504 per the ACR Convergence 2025 conference presentation — this discrepancy is unresolved and both figures are reported here rather than one being silently chosen** |
| Primary endpoint | ESSDAI change from baseline at Week 48 vs. placebo | Same |
| Status (CT.gov, verified) | COMPLETED — primary completion 2025-05-07 (ACTUAL) | ACTIVE_NOT_RECRUITING — primary completion 2025-05-13 (ACTUAL) |

## Actual Phase 3 results — both trials, individual arms (not just pooled)

**NEPTUNUS-1 (2-arm, monthly only):**
- Ianalumab: −6.4 (SE 0.47) vs. Placebo: −5.1 (SE 0.46)
- LS mean difference: **−1.3 (SE 0.66; 95% CI −2.6 to 0.0); P = 0.0496**

**NEPTUNUS-2 (3-arm, monthly and every-3-months):**
- **Monthly vs. placebo: −6.5 vs. −5.5, LS mean difference −1.0 (95% CI −2.0 to 0.0), P = 0.041** — significant
- **Every-3-months vs. placebo: did NOT reach statistical significance** — the
  less-frequent dosing arm failed on this endpoint. This is a real, material data
  point about dose/frequency sensitivity that the original pooled-only presentation
  obscured.

**Pooled analysis (NEPTUNUS-1 + NEPTUNUS-2 monthly arms combined):**
- Ianalumab: −6.5 vs. Placebo: −5.3, **P = 0.0031**

**Why presenting only the pooled figure is misleading:** the pooled p-value is
naturally smaller than either individual trial's p-value simply because pooling
increases N — it should not be read as "the effect is stronger than either trial
showed," and per FDA practice a pooled analysis is not normally a substitute for two
individually significant confirmatory trials in the same submission. Both individual
monthly-arm results (p=0.0496, p=0.041) were only barely under the conventional 0.05
threshold — an important, not-glossed-over data point about how thin ianalumab's
actual margin was.

**NEPTUNUS-1 secondary endpoints:**
- Patient's Global Assessment: LS mean difference −6.6 (95% CI −11.4 to −1.8), p=0.007
- Physician's Global Assessment: LS mean difference −5.5 (95% CI −10.1 to −0.9), p=0.018

**Safety:** AE/SAE incidence "comparable to placebo" in both trials; no signal flagged.

## Corrected math: what an ianalumab-sized effect would actually mean for dazodalibep's Phase 3

**A material error in the earlier version of this analysis:** the original day2
scenario model claimed that "the same 1.3-point effect ianalumab showed would produce
p=0.0002 in dazodalibep's larger trial." That calculation used a standard deviation
assumption (SD≈3.65, derived from dazodalibep's own Phase 2 SEs) that is inconsistent
with NEPTUNUS-1's own reported variance. Redone correctly:

- NEPTUNUS-1's actual SE≈0.66 at ~137/arm implies an effective two-group SD ≈ 5.47 —
  notably larger than the SD≈3.65 assumed elsewhere in this project (which itself
  differs from the SD=5.00 the dazodalibep Phase 2 protocol used for its own power
  calculation).
- Scaling NEPTUNUS-1's SE for dazodalibep's larger assumed per-arm N (~217): SE_scaled
  = 0.66 × √(137/217) ≈ **0.524**.
- At a 1.3-point delta with this SE: z = 1.3/0.524 ≈ 2.48, two-sided **p ≈ 0.013** —
  not p=0.0002. The earlier figure was wrong because it implicitly assumed a much
  smaller variance than the one real comparable trial (NEPTUNUS-1) actually observed.

This matters: p≈0.013 is still a pass, but it is a meaningfully less dominant result
than the erroneous p=0.0002 figure suggested — the "structural size advantage" claim
in the original thesis was directionally right but overstated in magnitude. See
`scenario_model.md` (corrected) for the full variance-sensitivity treatment this
finding now feeds into.

## Regulatory status
FDA granted Breakthrough Therapy Designation (Jan 16, 2026); global regulatory
submissions planned for early 2026.

## Revised implications for the dazodalibep (NCT06104124) thesis
1. Ianalumab's Ph2b did meet its primary objective (dose-response) — this is a
   genuine, correctly-classified precedent for "CD40/BAFF pathway trials can succeed
   in Sjögren's," but it should not be conflated with "the pairwise comparison also
   passed," since it didn't.
2. Both of ianalumab's actual Phase 3 wins were **narrow** (p=0.0496 and p=0.041
   individually) — this is a caution against assuming a real drug effect in this
   disease/endpoint combination will read out with a comfortable margin. Dazodalibep's
   own Phase 2 effect (−2.2, p=0.0167) is larger, but the variance-corrected math above
   shows the margin-of-victory story is less one-sided than previously stated.
3. The every-3-months arm's failure in NEPTUNUS-2 is a real precedent for
   dose/frequency sensitivity in this disease — worth keeping in mind if dazodalibep's
   Phase 3 doses differ meaningfully from its Phase 2 regimen (see the "dose and
   exposure bridge" topic flagged as a priority addition).

## Sources
- Bowman et al., Lancet 2021 (PMID 34861168) — Ph2b dose-response primary result
- NCT02962895, NCT05350072, NCT05349214 — ClinicalTrials.gov, verified directly
- ACR Convergence 2025 presentation coverage (RheumatologyLive, Cleveland Clinic
  Journal of Medicine) — NEPTUNUS-1 and NEPTUNUS-2 individual arm results
- Novartis press release, Aug 11, 2025; FDA Breakthrough Therapy designation, Jan 2026
