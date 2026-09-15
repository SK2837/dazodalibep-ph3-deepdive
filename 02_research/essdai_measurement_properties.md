# ESSDAI Measurement-Property Literature — Day 1, Step 4

## 1. MCID / clinically meaningful improvement thresholds

Source: Seror R, et al. "Defining disease activity states and clinically meaningful
improvement in primary Sjögren's syndrome with EULAR primary Sjögren's syndrome disease
activity (ESSDAI) and patient-reported indexes (ESSPRI)." Ann Rheum Dis (widely cited
Seror ESSDAI MCII paper).

- **Minimal clinically important improvement (MCII) for ESSDAI = a decrease of ≥3 points.**
  This is the field-standard *within-patient* responder threshold — it describes how
  much an individual patient's own score needs to drop to count as a meaningful
  personal improvement. **Correction: this is not the same quantity as "the minimum
  placebo-adjusted group difference needed for a trial to be clinically meaningful,"**
  and should not be used interchangeably with a between-group delta the way earlier
  versions of this project's modeling files did. A trial could show a smaller
  group-level average difference than 3 points while still having a meaningful
  proportion of patients individually clear the 3-point MCII — clinical relevance at
  the trial level should be assessed via responder-rate distributions and supportive
  outcomes, not by holding the group-average delta to the individual-patient threshold.
- Disease activity strata: low activity (ESSDAI <5), moderate (5–13), high (≥14).
  NCT06104124's inclusion criterion of ESSDAI ≥5 enrolls the moderate-to-high band.
- ESSPRI MCII: ≥1 point absolute decrease or ≥15% relative decrease from baseline
  (used identically in the CRESS composite, below) — same within-patient caveat applies.

## 2. Placebo-response model — quantified, not just qualitative

Source: Wang ZZ, Zheng QS, Liu HX, Li LJ. "Development and Application of the Placebo
Response Model in Clinical Trials for Primary Sjögren's Syndrome." Front Immunol.
2021;12:783246. Model-based meta-analysis across prior pSS RCTs.

- Placebo arms follow an **Emax (asymptotic) trajectory**, not a flat line:
  - **Emax = 4.44 + (Baseline ESSDAI − 10.1) × 0.552**
  - **ET50 (time to reach 50% of max placebo effect) ≈ 12.2 weeks**
  - Effect continues rising gradually out to ~48 weeks
- **Higher baseline ESSDAI → larger absolute placebo response** (more room to regress
  toward the mean / fluctuate downward). This is a real confound: enrolling a
  higher-activity population (as NCT06104124 does, ESSDAI≥5) doesn't just raise the
  drug arm's ceiling — it also mechanically inflates the placebo arm's expected drop.
- Practical implication for modeling: **the placebo assumption in the bull/base/bear
  table should not be a static number carried over from Phase 2 — it should scale with
  NCT06104124's actual baseline ESSDAI distribution** (Phase 2 baseline was 10.7±4.3 in
  Population 1; Phase 3's screened population, having a hard ESSDAI≥5 cutoff, may differ).

## 3. Does ESSDAI actually have known insensitivity-to-change / failure history?

**Correction — softened framing**: nonsignificant results in prior trials are
consistent with, but do not *prove*, ESSDAI insensitivity. A missed endpoint could
reflect a genuinely ineffective drug, an underpowered trial, dichotomization losing
information, or instrument insensitivity — these are not distinguishable from a single
trial's result, and several of the historical points below rest on small samples with
unadjusted multiple comparisons. With that caveat:
- **Correction — TRACTISS was NOT an ESSDAI-primary trial.** Its actual primary
  endpoint was the proportion of patients achieving a ≥30% reduction in fatigue OR
  oral dryness VAS at week 48 (39.8% rituximab vs. 36.8% placebo, not significant) —
  see the corrected `historical_trial_evidence.md`. It is not a valid example of an
  ESSDAI-primary trial missing.
- **ASAP-III** (abatacept, single-center Ph3): missed its primary continuous-ESSDAI
  endpoint at 24 weeks (no significant abatacept-vs-placebo difference) — the same drug
  showed median ESSDAI improvement from 14.0→4.0 by week 48 in an **open-label,
  uncontrolled** extension. Open-label improvement without a concurrent placebo arm is
  exploratory support, not proof that a real drug effect was missed by the endpoint —
  natural disease fluctuation and unblinding effects can't be ruled out.
- **ETAP** (tocilizumab): missed its primary endpoint, which was actually a **composite
  responder definition** (ESSDAI improvement ≥3 points AND no new moderate/severe
  domain activity AND no PGA worsening) — 52.7% tocilizumab vs. 63.6% placebo, p=0.14.
  This is a composite-responder miss, not evidence about continuous ESSDAI specifically.

## 4. Newer composite responder indices — CRESS and STAR

Both were built specifically because of the ESSDAI problems above. **Neither is used
by NCT06104124** — confirmed directly from the ClinicalTrials.gov registration: the
primary endpoint is literally "Change from baseline in ESSDAI Score," and the only
responder-type secondary endpoint is a plain "proportion achieving ESSDAI response" —
classic ESSDAI throughout, no CRESS/STAR language anywhere in the registered outcomes.

### CRESS (Composite of Relevant Endpoints for Sjögren's Syndrome)
Source: Lancet Rheumatology 2021/2024 (Composite of Relevant Endpoints for Sjögren's
Syndrome (CRESS): development and validation of a novel outcome measure).

5 components, response = meeting ≥3 of 5:
1. Systemic disease activity — clinESSDAI <5
2. Patient-reported symptoms — ESSPRI: ≥1 pt or ≥15% decrease
3. Tear gland function — Schirmer's test / ocular staining score improvement
4. Salivary gland function — unstimulated whole saliva flow ↑≥25%, or ultrasonography ↓≥25%
5. Serology — rheumatoid factor ↓≥25%, IgG ↓≥10%

**Validation finding, presented with appropriate caveats:** when CRESS was applied
retrospectively to the **ASAP-III abatacept trial data** (the same trial that missed
its classic continuous-ESSDAI primary endpoint), CRESS showed a response rate of
**60% (24/40) on abatacept vs. 18% (7/39) on placebo.** This is a retrospectively
developed composite score applied post hoc to a trial that missed its actual
prespecified randomized primary endpoint — it is exploratory supportive evidence that
the outcome measure *can* matter, not proof that ASAP-III's real drug effect was
definitively missed by ESSDAI. A retrospective reanalysis with a different, more
lenient composite definition will often show a larger apparent effect; that is a
different claim from "the endpoint hid a real, prespecified, confirmatory result."

### STAR (Sjögren's Tool for Assessing Response)
Source: Seror et al., developed by the NECESSITY consortium (78 experts + 20 patients,
data-driven + consensus method across 9 RCTs).

- Components: clinESSDAI (10 physician domains + 1 lab domain), ESSPRI (3 items),
  Schirmer's test, stimulated salivary flow, and a biologic domain.
- Reported to show good sensitivity to change and, per developer claims, to reduce
  placebo-response contamination relative to ESSDAI alone.

## 5. What this means for the NCT06104124 call (revised)

- Because NCT06104124 uses **classic continuous ESSDAI**, not CRESS/STAR, it inherits
  some of the instrument-level risk discussed above, though the strength of that risk
  is more uncertain than earlier framing suggested — see the softened language in
  Section 3.
- The dazodalibep Phase 2 data showed a related pattern: the **continuous ESSDAI score
  endpoint hit significance (P=0.0167)**, but the **categorical ESSDAI(3)/(4) responder
  analyses did not** (P=0.33, P=0.18). **Caveat (Priority 6 correction):** this is not
  proof that ESSDAI is defective as an instrument — dichotomizing a continuous score
  into a threshold loses statistical information, Population 1's sample was small
  (n=36/38), and multiple secondary analyses here were not adjusted for multiplicity.
  A nonsignificant categorical secondary is consistent with an insensitive threshold,
  but also consistent with ordinary sampling variability at this sample size.
- **Correction: the "Phase 3's larger, ESSDAI≥5-selected population" framing has been
  removed** — Phase 2 Population 1 already required ESSDAI≥5 as its own eligibility
  floor (see the correction in `phase2_baseline_characteristics.md`), so this is not a
  looser criterion unique to Phase 3.
- For any future modeling: the Emax placebo formula above is one useful reference
  point, but should not be treated as a precise predictor — see the corrected
  `scenario_model.md` for why a single formula or single comparable trial cannot
  fully calibrate Phase 3's placebo assumption with false precision.

## Sources
- Seror R et al. ESSDAI/ESSPRI MCII and disease-activity states, Ann Rheum Dis.
- Wang ZZ et al. Placebo response model, Front Immunol. 2021;12:783246.
- TRACTISS trial primary results (rituximab).
- ASAP-III trial primary results (abatacept), Lancet Rheumatology.
- CRESS development/validation, Lancet Rheumatology 2021/2024 (PMID 38287621).
- STAR development/validation, NECESSITY consortium (PMC9209686).
- NCT06104124 registration (ClinicalTrials.gov, verified directly) — confirms classic
  ESSDAI primary/secondary endpoints, no CRESS/STAR.
