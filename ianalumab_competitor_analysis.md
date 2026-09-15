# Ianalumab (Novartis) — Competitor Read-Through — Day 1, Step 5

This is the "HERE & HERE" readout news the assignment brief referenced but the links
weren't included in the forward. Found directly: Novartis has ALREADY reported positive
Phase 3 topline results for ianalumab in Sjögren's — this is a live, real precedent using
the exact same primary endpoint construct (ESSDAI change) that dazodalibep's NCT06104124
uses.

## Mechanism (for the biological-rationale contrast slide)
Ianalumab = anti-BAFF-receptor monoclonal antibody. Dual mechanism: B-cell depletion +
blockade of BAFF-R survival signaling. Contrast with dazodalibep's T-cell costimulation
(CD40L) blockade — different mechanism, same disease, same statistically-fraught
ESSDAI endpoint.

## Phase 2b dose-ranging trial — NCT02962895
"Study of Safety and Efficacy of Multiple VAY736 Doses in Patients With Moderate to
Severe Primary Sjögren's Syndrome." N=190. Completed 2020. **Results posted on
ClinicalTrials.gov (2024-10-29) — pulled directly from the results database.**

Population: seropositive (anti-Ro/SSA+), ESSDAI ≥6 (7-domain scoring).

**Primary endpoint — ESSDAI LS mean change from baseline at Week 24:**
| Arm | LS mean change | vs. Placebo (diff) | p-value |
|---|---|---|---|
| Placebo | −6.39 | — | — |
| VAY736 5mg | −5.64 | +0.75 (worse than placebo) | 0.5161 |
| VAY736 50mg | −6.93 | −0.55 | 0.6332 |
| VAY736 300mg | −8.30 | −1.92 | **0.0921** (not significant) |

**This Phase 2b trial MISSED its primary ESSDAI endpoint at every dose**, including the
highest (300mg, closest at p=0.0921, still not significant at α=0.05). Notably the
**placebo arm's own drop (−6.39) was larger than both the 5mg and 50mg drug arms** — a
textbook case of the placebo-response problem documented in the ESSDAI literature
(see `essdai_measurement_properties.md`). Only the top dose showed directional separation.

**Why Novartis proceeded to Phase 3 anyway** — secondary endpoints told a cleaner story:
- Physician's Global Assessment (PhGA) at Wk24: 300mg −31.99 vs placebo −23.64 — clear dose-ordered separation
- CD19+ B-cell depletion was clean, dose-dependent, and durable (PD proof of mechanism)
- This is a real example of a sponsor advancing to Ph3 off secondary/PD signal despite
  a missed primary ESSDAI endpoint — worth citing as another instance where ESSDAI's
  known insensitivity may have masked a real effect.

## Phase 3 program — NEPTUNUS-1 and NEPTUNUS-2

| | NEPTUNUS-1 (NCT05350072) | NEPTUNUS-2 (NCT05349214) |
|---|---|---|
| Design | 2-arm, ianalumab 300mg SC monthly vs. placebo, 52 wks | 3-arm, ianalumab 300mg SC monthly OR every 3 months vs. placebo, up to 52 wks |
| N | 275 (137/138 per arm) | 504 (168 per arm) |
| Status (CT.gov, verified) | **COMPLETED** — primary completion 2025-05-07 (ACTUAL), full completion 2026-06-02 (ACTUAL) | ACTIVE_NOT_RECRUITING — primary completion 2025-05-13 (ACTUAL), full completion est. 2027-04-15 (long-term follow-up ongoing) |
| Primary endpoint | ESSDAI change from baseline at Week 48 vs. placebo | Same |
| Population | Time since Sjögren's diagnosis ≤7.5 yrs, anti-Ro/SSA+ (or biopsy+), ACR/EULAR 2016 criteria | Same |
| Results posted on CT.gov? | No (as of today) | No |

**Note:** neither trial's results are posted in the CT.gov structured results database yet,
despite primary completion having occurred **16+ months ago** (May 2025) — the actual
data disclosure happened entirely through press release + conference presentation, not
the registry. Worth remembering when judging NCT06104124: a "no results posted on CT.gov"
status does not by itself mean data doesn't exist elsewhere yet — press release/conference
disclosure can run well ahead of the registry posting.

## Actual Phase 3 topline results (already public)

**Novartis press release, August 11, 2025:** both NEPTUNUS-1 and NEPTUNUS-2 announced
as meeting the primary ESSDAI endpoint with statistical significance — "the first-ever
global Phase 3 trials to demonstrate statistically significant reduction in disease
activity in Sjögren's disease." No numbers disclosed at this stage — held for congress.

**Full data presented at ACR Convergence, October 29, 2025** (Thomas Grader-Beck, MD,
Johns Hopkins Sjögren's Center):

**NEPTUNUS-1 individual result:**
- Ianalumab: −6.4 (SE 0.47) vs. Placebo: −5.1 (SE 0.46)
- LS mean difference: **−1.3 (SE 0.66; 95% CI −2.6 to 0.0); P = 0.0496**
- **This barely cleared significance** — p=0.0496 is a razor-thin pass, and the −1.3
  point effect size is **below the field's own ESSDAI MCID threshold of ≥3 points**
  (Seror et al.). Statistically significant ≠ clearly clinically meaningful by the
  field's own standard.

**Pooled analysis (NEPTUNUS-1 + NEPTUNUS-2 combined):**
- Ianalumab: −6.5 vs. Placebo: −5.3
- **P = 0.0031** (much stronger when pooled — consistent with the individual-trial
  effect being real but modest, and needing the combined N to reach robust significance)

**NEPTUNUS-1 secondary endpoints:**
- Patient's Global Assessment: LS mean difference −6.6 (95% CI −11.4 to −1.8), p=0.007
- Physician's Global Assessment: LS mean difference −5.5 (95% CI −10.1 to −0.9), p=0.018
- Improvements evident by Week 16, sustained through 52 weeks
- Stimulated salivary flow and oral dryness improved vs. placebo in patients with
  baseline flow >0.4 mL/min

**Safety:** AE and SAE incidence "comparable to placebo" in both trials — no signal
flagged (consistent with B-cell-depletion mechanism carrying different risk profile
than CD40L blockade; no thromboembolism signal relevant here since BAFF-R targeting
doesn't touch platelet CD40L).

## Regulatory status
- FDA granted **Breakthrough Therapy Designation** (announced Jan 16, 2026)
- Novartis planned global regulatory submissions for **early 2026**

## What this means for the dazodalibep (NCT06104124) thesis

1. **Proof of concept that ESSDAI-based Phase 3 trials CAN pass in Sjögren's** — this
   removes the "no ESSDAI-based Ph3 has ever succeeded" tail risk from the base-rate
   argument. It's no longer purely theoretical; there's now a real, recent, same-endpoint
   precedent.
2. **But the passing margin was thin** — p=0.0496 (barely under 0.05) on NEPTUNUS-1
   individually, with an effect size (−1.3) below the established MCID (3 points).
   This confirms rather than dispels the "ESSDAI is a noisy, low-sensitivity instrument"
   concern — even a drug that "worked" only barely broke through the noise floor at
   individual-trial N; pooling was needed for a robust p-value.
3. **Direct relevance to dazodalibep's own Phase 2 pattern**: dazodalibep's Phase 2
   primary endpoint delta was −2.2 points (−6.3 vs −4.1, p=0.0167) — a *larger* raw
   effect size than ianalumab's eventual Phase 3 pooled effect size (−1.2), and a
   *tighter* p-value at smaller N (74 vs. ianalumab's Ph2b N=190 that still missed).
   That's a genuinely bullish comparison point: dazodalibep's Ph2 effect looks
   quantitatively stronger than the effect size that just carried ianalumab to an
   actual Phase 3 win.
4. **Caution**: ianalumab's Ph2b (N=190, similar in kind to dazodalibep's Ph2 N=74)
   *missed* its primary endpoint despite eventually succeeding in Ph3 — proof that a
   single Ph2 readout, positive or negative, is not fully predictive of Ph3 outcome in
   this indication. This tempers over-reliance on the Ph2→Ph3 "bridge" as sole evidence.

## Sources
- ClinicalTrials.gov: NCT02962895 (Ph2b, incl. posted results), NCT05350072 (NEPTUNUS-1),
  NCT05349214 (NEPTUNUS-2) — verified directly via API
- Novartis press release, Aug 11, 2025 (novartis.com/news/media-releases)
- ACR Convergence 2025 abstract (acrabstracts.org) and presentation coverage
  (Cleveland Clinic Journal of Medicine ACR2025 coverage; Patient Worthy)
- FDA Breakthrough Therapy Designation news, Jan 16, 2026
