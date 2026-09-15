# NCT06245408 (Secondary Trial) — ESSPRI/Placebo-Response Risk Note

Lightweight treatment only, per plan — directional read, not a modeled probability.

## Design recap
NCT06245408 enrolls patients with "unacceptable symptom burden and limited systemic
disease" (ESSPRI ≥5, ESSDAI <5) — the mirror-image population to NCT06104124. Primary
endpoint: ESSPRI change from baseline at Week 48 (patient-reported: pain+fatigue+dryness
average), not ESSDAI.

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
  high symptom burden, ESSPRI≥5) mirrors exactly the subgroup where JOQUER's post hoc
  analysis found signal — i.e., Amgen's population selection is aimed at the part of
  the ESSPRI trial-design space with the best historical precedent for showing an effect.
- **Bearish angle:** JOQUER's HSB signal was post hoc/exploratory, not the trial's
  pre-specified primary analysis — a positive subgroup finding in one old trial is a
  much weaker prior than a genuine ESSDAI proof of mechanism.

## Dazodalibep's own Phase 2 data point for this exact population
Population 2 of the Phase 2 trial (unacceptable symptom burden / ESSPRI-based, N=109)
is the direct precedent: **ESSPRI diff −1.3, P=0.0002** — the *cleanest, most
significant* result across the entire Phase 2 program (see `phase2_results_verified.md`).
This is materially more reassuring for NCT06245408 than the systemic/ESSDAI cohort's
result was for NCT06104124.

## Net directional read
NCT06245408 likely carries **somewhat lower placebo-response risk than NCT06104124**,
for two reasons specific to this program (not a general claim about ESSPRI vs. ESSDAI
trials writ large):
1. Its own Phase 2 precursor (Population 2) produced the strongest, cleanest signal in
   the entire Phase 2 program (P=0.0002 vs. P=0.0167 for the systemic cohort).
2. Its enrichment strategy targets the specific patient phenotype (high symptom burden)
   where the field's main ESSPRI cautionary tale (JOQUER) still found a signal in
   post hoc analysis.

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
