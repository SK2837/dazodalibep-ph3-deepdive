# ESSDAI Measurement-Property Literature — Day 1, Step 4

## 1. MCID / clinically meaningful improvement thresholds

Source: Seror R, et al. "Defining disease activity states and clinically meaningful
improvement in primary Sjögren's syndrome with EULAR primary Sjögren's syndrome disease
activity (ESSDAI) and patient-reported indexes (ESSPRI)." Ann Rheum Dis (widely cited
Seror ESSDAI MCII paper).

- **Minimal clinically important improvement (MCII) for ESSDAI = a decrease of ≥3 points.**
  This is the field-standard responder threshold, used across trials (including the
  Phase 2 dazodalibep paper's "ESSDAI(3) response" analysis).
- Disease activity strata: low activity (ESSDAI <5), moderate (5–13), high (≥14).
  NCT06104124's inclusion criterion of ESSDAI ≥5 enrolls the moderate-to-high band.
- ESSPRI MCII: ≥1 point absolute decrease or ≥15% relative decrease from baseline
  (used identically in the CRESS composite, below).

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

Yes — well documented via trial track record, not just theory:
- **TRACTISS** (rituximab, Ann Rheum Dis / primary paper): missed on ESSDAI-based
  endpoints. Standardized response mean (SRM) at primary endpoint: **rituximab −0.33 vs
  placebo −0.13** — a small separation, consistent with an insensitive instrument
  rather than necessarily "no biological effect."
- **ASAP-III** (abatacept, single-center Ph3): **missed its primary ESSDAI endpoint at
  24 weeks** (no significant abatacept-vs-placebo difference) — despite the same drug
  showing median ESSDAI improvement from 14.0→4.0 by week 48 in open-label extension,
  and 50% of patients reaching low disease activity. This is a strong case study for
  "the drug may work; the classic ESSDAI primary read did not detect it in the
  double-blind window."
- General critique in the literature (multiple RCT reviews): ESSDAI as primary endpoint
  has repeatedly shown **large placebo-arm improvement alongside active-arm
  improvement**, compressing the treatment-vs-placebo delta and increasing false-negative
  risk — the exact mechanism the newer composite indices below were built to fix.

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

**Key validation finding — directly relevant to your thesis:** when CRESS was applied
retrospectively to the **ASAP-III abatacept trial data** (the same trial that *missed*
its classic ESSDAI primary endpoint), CRESS showed a response rate of
**60% (24/40) on abatacept vs. 18% (7/39) on placebo** — a 42-point separation the
classic ESSDAI primary endpoint completely failed to surface in that same dataset.
This is the cleanest available proof that **the outcome measure, not just the drug's
biology, can determine whether a Sjögren's trial reads out positive or negative.**

### STAR (Sjögren's Tool for Assessing Response)
Source: Seror et al., developed by the NECESSITY consortium (78 experts + 20 patients,
data-driven + consensus method across 9 RCTs).

- Components: clinESSDAI (10 physician domains + 1 lab domain), ESSPRI (3 items),
  Schirmer's test, stimulated salivary flow, and a biologic domain.
- Reported to show good sensitivity to change and, per developer claims, to reduce
  placebo-response contamination relative to ESSDAI alone.

## 5. What this means for the NCT06104124 call

- Because NCT06104124 uses **classic ESSDAI**, not CRESS/STAR, it inherits the exact
  instrument-level risk documented above: real drug effect can be masked by placebo-arm
  drift, especially given Phase 3's larger, ESSDAI≥5-selected population.
- The dazodalibep Phase 2 data already showed this pattern in miniature: the
  **continuous ESSDAI score endpoint hit significance (P=0.0167)**, but the
  **categorical ESSDAI(3)/(4) responder analyses did not** (P=0.33, P=0.18) — i.e.,
  the same "instrument sensitivity" issue documented at the field level (TRACTISS,
  ASAP-III) already showed up in dazodalibep's own Phase 2 data.
- For the bull/base/bear model (Day 2): use the Emax placebo formula above to derive a
  **baseline-ESSDAI-adjusted placebo assumption** for NCT06104124 rather than reusing
  the flat Phase 2 placebo delta (−4.1), since Phase 3's enrollment criteria and larger
  N will pull in a different baseline distribution.

## Sources
- Seror R et al. ESSDAI/ESSPRI MCII and disease-activity states, Ann Rheum Dis.
- Wang ZZ et al. Placebo response model, Front Immunol. 2021;12:783246.
- TRACTISS trial primary results (rituximab).
- ASAP-III trial primary results (abatacept), Lancet Rheumatology.
- CRESS development/validation, Lancet Rheumatology 2021/2024 (PMID 38287621).
- STAR development/validation, NECESSITY consortium (PMC9209686).
- NCT06104124 registration (ClinicalTrials.gov, verified directly) — confirms classic
  ESSDAI primary/secondary endpoints, no CRESS/STAR.
