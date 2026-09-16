# NCT06245408 (Secondary Trial) — ESSPRI/DASPRI Placebo-Response Risk Note

Lightweight treatment only, per plan — directional read, not a modeled probability.

**Correction: this trial has TWO registered primary outcomes, not one.** Per
`NCT06245408.csv`, the primary outcomes are **"Change from baseline in ESSPRI score"
AND "Change from baseline in Diary for Assessing Sjögren's Patient Reported Index
(DASPRI) score,"** both at Week 48. The original version of this note discussed only
ESSPRI — a material gap, since DASPRI is a daily patient diary instrument (recall-based,
completed repeatedly rather than once at a visit), a meaningfully different
measurement approach than a single-timepoint ESSPRI questionnaire. No information is
public on whether both instruments must reach significance, either one is sufficient,
or a prespecified hierarchy applies between them — that requires the protocol/SAP,
which is not available. This should not be assumed either way.

## Design recap
NCT06245408 enrolls patients with "unacceptable symptom burden and limited systemic
disease" (ESSPRI ≥5, ESSDAI <5) — the mirror-image population to NCT06104124. Primary
endpoints: ESSPRI change AND DASPRI change from baseline at Week 48 (both
patient-reported: pain+fatigue+dryness domains), not ESSDAI.

## DASPRI — what it is and why it's a distinct risk profile from ESSPRI
DASPRI is a diary-based instrument — patients record symptoms repeatedly (e.g. daily)
rather than answering a single questionnaire at a clinic visit. This changes the
risk profile in ways worth naming rather than assuming away:
- **Missing-response risk**: diary compliance can be incomplete, and how missing diary
  days are handled (imputation, averaging, discontinuation rules) can materially affect
  the analysis — this is a different risk than ESSPRI's single-timepoint recall.
- **Validation evidence**: DASPRI is a newer, less extensively validated instrument
  than ESSPRI (which has a longer track record, including the Seror et al. MCID work
  cited in `essdai_measurement_properties.md`). Less external validation data exists to
  calibrate what a "real" DASPRI effect size looks like across trials.
- **Correction (verified directly against the PDF's full text — searched, zero
  occurrences): DASPRI does not appear anywhere in the 2024 Phase 2 paper.** An
  earlier version of this note assumed the paper reported DASPRI results without
  actually checking — that assumption was wrong. There is no dazodalibep-specific
  Phase 2 precedent for DASPRI at all, for either population. This is a bigger gap
  than "the number wasn't extracted yet" — the number doesn't exist in the published
  Phase 2 record.
- **Why this is likely, not a red flag**: DASPRI was developed as a patient-reported
  symptom diary specifically to align with **FDA patient-reported-outcome (PRO)
  guidance** for clinical trials — a newer, more regulatory-aligned instrument than
  ESSPRI. It's plausible Amgen added it for Phase 3 specifically to strengthen the
  regulatory submission package, not because ESSPRI performed poorly. Frame this as
  "a new instrument added for a likely regulatory reason, with zero track record for
  this drug," not as a hidden problem.

## Why ESSPRI-based endpoints carry a different, and generally worse, placebo-response risk than ESSDAI
ESSPRI is a fully patient-reported, subjective symptom scale (0–10 VAS averaged across
3 domains) with no physician/lab anchor at all — historically even more prone to
placebo response than ESSDAI, since there's no objective organ-damage signal to
"ground" the score the way ESSDAI's organ-domain items do.

**Key precedent: JOQUER trial** (hydroxychloroquine vs. placebo, N=120, 24 weeks) —
the classic ESSPRI-based Sjögren's trial. Overall result: **no significant benefit**.
But a post hoc stratification found the **"high symptom burden" (HSB) subgroup**
(n=32) *did* show a relative ESSPRI improvement (1.49 points at 12 weeks) — and this
HSB phenotype is essentially the same population NCT06245408 deliberately enriches
for. Read both ways:
- **Bullish angle:** NCT06245408's enrichment strategy (screening specifically for
  high symptom burden, ESSPRI≥5) targets a patient phenotype conceptually similar to
  the subgroup where JOQUER's post hoc analysis found signal — not procedurally
  identical (JOQUER's "high symptom burden" subgroup was defined by its own
  exploratory clustering method, not a simple ESSPRI≥5 cutoff), but a directionally
  relevant precedent for the part of the ESSPRI trial-design space more likely to show
  an effect.
- **Bearish angle:** JOQUER's HSB signal was post hoc/exploratory, not the trial's
  pre-specified primary analysis — a positive subgroup finding in one old trial is a
  much weaker prior than a genuine ESSDAI proof of mechanism.

## Dazodalibep's own Phase 2 data point for this exact population
Population 2 of the Phase 2 trial (unacceptable symptom burden / ESSPRI-based, N=109)
is the direct precedent: **ESSPRI diff −1.3, P=0.0002** — the *cleanest, most
significant* result across the entire Phase 2 program (see `phase2_results.md`).
This is materially more reassuring for NCT06245408 than the systemic/ESSDAI cohort's
result was for NCT06104124.

## Net directional read (softened — corrected)
**Correction**: a smaller Phase 2 p-value (0.0002 vs. 0.0167) reflects the observed
Phase 2 signal strength — it does not, on its own, establish lower *future* placebo
risk or a higher Phase 3 success probability. Those are different claims, and the
earlier version of this note conflated them. Similarly, JOQUER's post hoc "high symptom
burden" subgroup was defined by its own exploratory clustering method, not the same
rule as NCT06245408's ESSPRI≥5 eligibility criterion — the two populations are related
in spirit, not procedurally identical, and shouldn't be treated as interchangeable.

With that softened: NCT06245408 has two supportive-but-not-conclusive data points in
its favor:
1. Its own Phase 2 precursor (Population 2) produced the strongest, cleanest observed
   signal in the entire Phase 2 program (P=0.0002 vs. P=0.0167 for the systemic cohort)
   — a fact about the observed Phase 2 result, not a calibrated forecast for Phase 3.
2. Its enrichment strategy targets a patient phenotype conceptually similar to (not
   identical to) the one subgroup where JOQUER's exploratory post hoc analysis found
   a signal.

Countervailing factor: ESSPRI as an instrument is still fully subjective/patient-reported
with no objective anchor, so if anything goes wrong with blinding integrity, expectation
effects, or trial conduct, it has less structural resistance to placebo drift than ESSDAI
does. This is a real, generic ESSPRI risk that applies regardless of the favorable
population-specific precedent above.

## Sources
- JOQUER trial: Gottenberg et al. and stratified reanalysis (Rheumatology International,
  PMC8316226)
- Dazodalibep Phase 2, Population 2 (St. Clair et al., Nature Medicine 2024)
- NCT06245408 registration (ClinicalTrials.gov, verified directly)
