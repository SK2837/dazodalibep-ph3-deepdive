# Dazodalibep Phase 2 Results — Verified from Primary Source

Source: St. Clair EW, et al. "CD40 ligand antagonist dazodalibep in Sjögren's disease: a
randomized, double-blinded, placebo-controlled, phase 2 trial." Nature Medicine 30,
1583–1592 (June 2024). DOI: 10.1038/s41591-024-03009-3. NCT04129164.
Local file: phase2_paper.pdf

## Population 1 — Moderate-to-severe systemic disease activity (ESSDAI-based)
Bridges to Phase 3 NCT06104124.

- N = 74 randomized (DAZ n=36, PBO n=38); 71 (95.9%) completed Stage I
- **Primary endpoint** — ESSDAI change from baseline at Day 169 (LS mean ± SE):
  - DAZ: −6.3 ± 0.6
  - PBO: −4.1 ± 0.6
  - LS mean difference: −2.2 ± 0.9, **P = 0.0167** ✅ significant
- Secondary — ESSDAI categorical responder rates at Day 169:
  - ESSDAI(3) response: 72.2% (DAZ) vs 59.5% (PBO), P = 0.3283 — NOT significant
  - ESSDAI(4) response: 66.7% (DAZ) vs 48.6% (PBO), P = 0.1823 — NOT significant
  - ESSDAI(5) response: 61.1% (DAZ) vs 35.1% (PBO), P = 0.0449 — significant, but
    explicitly flagged by authors as **post hoc**, not pre-specified
- Secondary — ESSPRI change (Day 169): DAZ −1.8±0.3 vs PBO −1.1±0.3, P = 0.1110 (not significant)
- Domain responses: hematological domain response 26.7% (DAZ) vs — (PBO); higher
  proportion of DAZ-treated participants achieved ≥1-point domain improvement in
  several domains (see Fig. 2 in paper for full breakdown)

**Key takeaway for the deck:** the continuous ESSDAI score endpoint (the actual primary
endpoint) hit significance cleanly; the categorical/responder-threshold analyses mostly
did not, except one post hoc cut. This is direct evidence for the ESSDAI
measurement-property discussion (responder thresholds are noisier than the continuous score).

## Population 2 — Unacceptable symptom burden, limited systemic involvement (ESSPRI-based)
Bridges to Phase 3 NCT06245408.

- N = 109 randomized (DAZ n=54, PBO n=55); 102 (93.6%) completed Stage I
- **Primary endpoint** — ESSPRI change from baseline at Day 169 (LS mean ± SE):
  - DAZ: −1.8 ± 0.2
  - PBO: −0.5 ± 0.2
  - LS mean difference: −1.3 ± 0.3, **P = 0.0002** ✅ significant

## Safety (both populations combined)
- DAZ generally safe and well tolerated
- Most frequent AEs: COVID-19, diarrhea, headache, nasopharyngitis, upper respiratory
  tract infection, arthralgia, constipation, urinary tract infection
- **CORRECTION to earlier framing**: one participant (Population 1, Stage II) had both
  a DVT and a drug-induced liver injury; per Table 3 in the paper, **investigators
  classified both SAEs as related to study medication** — this is not a "no signal"
  finding. The paper's actual argument is narrower: onset was 180 days after the final
  DAZ dose, well outside the drug's expected exposure window, which the Discussion
  section argues is inconsistent with the platelet Fc-crosslinking mechanism that
  causes thromboembolism *during* dosing with first-generation anti-CD40L antibodies.
  Use the precise claim ("timing argues against the known mechanism") rather than
  "no serious safety signal" in the deck.
- **Correction**: Table 3 reports **one death** (Population 1, DAZ-PBO group, Stage
  II+follow-up, n=1), not "two deaths" as an earlier version of this note stated — a
  59-year-old female who developed COVID-19 pneumonia and died of an unknown cause 46
  days after her final DAZ dose (12 days after COVID-19 diagnosis); investigators
  considered this event unrelated to study medication given her risk factors (heart
  failure, hypertension, morbid obesity, pulmonary fibrosis).
- **Added**: Population 2 also had an SAE of **invasive ductal breast carcinoma**
  (DAZ-PBO group, a 42-year-old female, onset 139 days after her final DAZ dose),
  captured as both an SAE and an AESI of malignant neoplasm. **Investigators
  considered this event related to study medication.** This should be reported in the
  safety section alongside the DVT/liver-injury event above — report attribution,
  timing, and denominator without inferring causation from a single event in a small
  trial, in either direction.
- No dose-ranging was performed — only a single dose (1,500mg) was tested, unlike
  ianalumab (3 doses) and iscalimab (3 doses) in their respective Ph2b trials (see
  `historical_trial_evidence.md` / `ianalumab_competitor_analysis.md`) — a real
  evidentiary gap for Amgen's dose-selection rationale heading into Phase 3

## Statistical design caveat — relaxed significance threshold
The authors explicitly set significance at **p<0.10 (two-sided)**, not the standard
p<0.05, citing small sample size and wanting to avoid falsely concluding DAZ doesn't
work. The primary ESSDAI result (p=0.0167) clears both bars comfortably. But this
means some "trending positive" secondary results (e.g., Population 1 ESSPRI, p=0.1110)
do **not** clear even the paper's own loosened bar — worth being precise about which
results are genuinely robust vs. directional only, especially since Phase 3's SAP will
almost certainly use the standard p<0.05.

## Pharmacodynamic/biomarker evidence (mechanism proof, not just clinical score)
- **CXCL13** (a chemokine marker of germinal center activity): DAZ rapidly and durably
  suppressed CXCL13 in both populations by day 169 (P=0.0010 pop.1, P<0.0001 pop.2 vs.
  PBO); levels rebounded toward baseline within ~2 months after switching off DAZ in
  the crossover phase — strong independent evidence the drug is doing what the biology
  predicts (see biological-rationale slide), separate from the noisier clinical scores.
- **Rheumatoid factor (RF)** autoantibody: significantly reduced by DAZ in both
  populations (P<0.0001) — direct evidence of reduced autoantibody production, the
  core mechanism claim for CD40/CD40L blockade in Sjögren's.

## Subgroup result: concomitant RA/SLE (Extended Data Table 1) — added
Systemic patients (Population 1) **without** concomitant RA/SLE had a placebo-adjusted
ESSDAI change of approximately **−1.6**; those **with** concomitant RA/SLE showed
approximately **−3.3**. Subgroup sizes are small (RA/SLE overlap was 19.4% DAZ /
23.7% PBO of Population 1 — see `phase2_baseline_characteristics.md`), so this should
not be treated as a robust interaction effect. It is, however, a more concrete,
source-backed transportability question for Phase 3 than an inference based on
eligibility criteria alone (see the correction in `phase2_baseline_characteristics.md`
regarding the removed "looser Phase 3 entry bar" argument).

## Molecular description — correction
**"PASylated" was an incorrect description used elsewhere in this project** (originally
in `PROJECT_PLAN.md`, now corrected). The paper describes dazodalibep as built on a
**Tn3 scaffold — a non-antibody, Fc-free fusion protein platform** — not a PASylated
molecule. PASylation is a different half-life-extension technology used by other
biologics; conflating the two is a real error, now fixed throughout this project's
files that referenced it.

## Crossover (Stage II) durability data
- Population 1: PBO→DAZ switch improved ESSDAI from −4.1 (day 169) to −6.3 (day 365);
  DAZ→PBO switch declined from −6.3 (day 169) to −4.4 (day 365) — both patterns consistent
  with a real, reversible drug effect rather than a baseline-cohort artifact.
- Population 2: PBO→DAZ switch improved ESSPRI from −0.5 (day169) to −1.3 (day365);
  DAZ→PBO switch: −1.8 (day169) to −1.9 (day365) — durability held up better here than
  in Population 1's crossover-off arm.

## Full baseline characteristics
See `phase2_baseline_characteristics.md` for the complete Table 1 breakdown (both
populations, drug vs. placebo, all demographic and disease-severity variables), plus
read-across notes to the Phase 3 populations.

## Full plain-language walkthrough of the paper
See `phase2_paper_explained.md` for a non-technical explanation of the study
design, findings, and how to use this paper as the Phase 2→Phase 3 bridge.
