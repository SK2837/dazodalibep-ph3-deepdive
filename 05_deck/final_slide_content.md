# Dazodalibep Phase 3: Final Slide Content

**Ready to copy directly into PowerPoint.** This supersedes both
`slide_by_slide_outline.md` and `RECOMMENDED_PRESENTATION_CONTENT.md` as the build
source — it takes the corrected, statistically rigorous content from the second
review pass and fixes the two errors that pass introduced (a baseline-table
transcription claim that was itself wrong, and an imprecise death-timing statement),
verified directly against the primary source PDF. Every number here traces to
`02_research/`, `03_analysis/`, or the primary sources cited per slide.

### How to use this file
- Copy **On-slide copy** and the exhibit tables into PowerPoint directly.
- Use **Speaker note** for verbal explanation — don't put the whole note on the slide.
- Use **Source** for the slide footer and the reference appendix.
- Labels like "observed," "analyst assumption," and "not established" belong on the
  slide next to the relevant claim, not just in this file.

---

# Part I — Main presentation (20 slides)

## Slide 1 — Title

### Dazodalibep in Sjögren's disease: a positive systemic readout is plausible, but the margin matters

**On-slide copy**
Clinical deep dive on Amgen's Phase 3 program
- Primary forecast: NCT06104124 — systemic disease activity
- Supporting assessment: NCT06245408 — symptom burden
- Analysis cutoff: September 15, 2026
- Prepared by: Sai Adarsh Kasula, Data Scientist / Biostatistician

**Visual:** Restrained title slide, no stock imagery, two trial identifiers beneath the subtitle.
**Speaker note:** "I focus the quantitative forecast on the systemic trial, as permitted by the brief, and use the symptomatic study to assess how far the evidence extends across the program."
**Source:** Jefferies assignment brief.

---

## Slide 2 — Executive conclusion

### We expect NCT06104124 to meet its ESSDAI primary endpoint, with meaningful residual risk

**On-slide copy**
1. **Direct clinical evidence:** Phase 2 showed a −2.2-point adjusted ESSDAI difference at day 169; p=0.0167.
2. **Biological coherence:** CD40L blockade reduced immune biomarkers (CXCL13, RF); iscalimab provides additional pathway evidence.
3. **Confirmatory precedent:** ianalumab demonstrated that week-48 ESSDAI benefit can be detected in Phase 3.

**Main risk:** a smaller week-48 effect combined with higher variance or stricter multiplicity testing could turn an encouraging signal into a negative primary result.

**Exhibit**

| Forecast | Conclusion | Basis / boundary |
|---|---|---|
| Systemic trial | Expect positive | Qualitative analyst forecast; stress-tested below |
| Symptomatic trial | Positive ESSPRI lean | DASPRI and full success-rule uncertainty limit conviction |

**Speaker note:** "My positive call comes from the evidence as a whole. Larger enrollment improves precision; it does not establish that the drug will retain its Phase 2 effect."
**Source:** `03_analysis/final_thesis.md`; analyst assessment. No numerically calibrated program probability is claimed.

---

## Slide 3 — Define the question

### The program tests two distinct clinical questions at week 48

**Exhibit**

| | Systemic: NCT06104124 | Symptomatic: NCT06245408 |
|---|---|---|
| Clinical focus | Moderate-to-severe systemic activity | High symptoms with limited systemic activity |
| Core eligibility | ESSDAI ≥5 | ESSPRI ≥5; ESSDAI <5 |
| Enrollment | 651 | 434 |
| Primary outcomes | ESSDAI change from baseline | ESSPRI AND DASPRI change from baseline |
| Primary assessment | Week 48 | Week 48 |
| Status | Completed, primary completion 2026-07-23 | Active, not recruiting; primary completion est. 2026-10-22 |
| This presentation | Full efficacy forecast | Directional supporting assessment |

**On-slide takeaway:** "Positive" means success under the prespecified primary testing procedure. Statistical significance, clinical importance, and benefit-risk are assessed separately.
**Speaker note:** "Two outcomes listed as primary do not, by themselves, tell us whether both must pass or a hierarchy applies. I do not infer that rule from the registry labels."
**Visual:** Clean two-column trial card, not a registry screenshot.
**Source:** `01_data/NCT06104124.csv`, `01_data/NCT06245408.csv`. Full eligibility/testing details require the protocol, not available publicly.

---

## Slide 4 — Disease and endpoint distinction

### Reducing systemic activity and improving dryness, fatigue and pain are related — but separate — tests

**On-slide copy**
- **ESSDAI:** clinician-assessed systemic disease activity across weighted organ domains.
- **ESSPRI/DASPRI:** patient-reported dryness, fatigue, and pain.
- Symptoms can reflect several processes; immune suppression need not produce the same benefit in every domain.

**Visual:** Two columns, "Systemic activity" and "Patient symptoms," connected by a partial overlap (not an equals sign). Show representative domains, not a dense organ inventory.
**Speaker note:** "The two populations should not be reduced to 'reversible' versus 'irreversible' disease. Residual gland function may matter — Population 2's Phase 2 precursor required residual stimulated salivary flow ≥0.1 mL/min — but fatigue and pain are not simply measurements of gland damage."
**Source:** `02_research/phase2_baseline_characteristics.md`. Present the gland-function point as clinical interpretation, not proven explanation.

---

## Slide 5 — Biological rationale

### CD40L blockade interrupts immune-cell costimulation implicated in Sjögren's disease

**On-slide copy**
- CD40L–CD40 signaling supports T-cell/B-cell interactions and downstream immune activation.
- Dazodalibep blocks the ligand (CD40L); iscalimab targets the receptor (CD40).
- Dazodalibep's Fc-free Tn3-scaffold design is engineered to avoid the Fc-mediated platelet-crosslinking mechanism implicated in first-generation anti-CD40L antibody thromboembolism.

**Visual — node/arrow spec:**
- Node 1: "T-cell (CD40L)" → arrow labeled "costimulatory signal" → Node 2: "B-cell / APC / epithelial cell (CD40)" → Node 3: "Antibody production, germinal center formation"
- Block icon on the arrow: "Dazodalibep (blocks CD40L)"
- Block icon on Node 2: "Iscalimab (blocks CD40)"
- Separate branch, visually distinct: "BAFF-R / B-cell survival" → block icon "Ianalumab (different mechanism — B-cell depletion + BAFF-R blockade)"
- Small note: "Engineering addresses a known mechanism; clinical safety still requires evidence."

**Speaker note:** "The mechanism establishes plausibility. The randomized clinical results are the direct test of efficacy; pharmacodynamic data help establish whether the expected biology is engaged."
**Source:** `PROJECT_STATUS.md` Section 2; `02_research/phase2_results.md` (Tn3 scaffold, not "PASylated").

---

## Slide 6 — Phase 2 design

### Phase 2 provides two randomized efficacy tests, followed by a blinded treatment switch

**Exhibit**

| | Population 1 | Population 2 |
|---|---|---|
| Randomized N | 74 | 109 |
| Dazodalibep / placebo | 36 / 38 | 54 / 55 |
| Core entry criteria | ESSDAI ≥5 | ESSPRI ≥5, ESSDAI <5, stimulated flow ≥0.1 mL/min |
| Primary outcome | ESSDAI change, day 169 | ESSPRI change, day 169 |
| Stage I completion | 71/74 | 102/109 |

**On-slide copy:** One IV regimen — 1,500mg every 2 weeks for 3 doses, then every 4 weeks for 4 doses. No dose-ranging in this Sjögren's study.
**Visual — timeline:** Two lanes (PBO→DAZ, DAZ→PBO), Day 0–169 and 169–365, vertical dashed marker at Day 169 labeled "PRIMARY ANALYSIS" (visually dominant), small callout at Day 365: "Crossover data used for durability check only, not primary efficacy."
**Speaker note:** "The strongest evidence is the prespecified randomized first period. The crossover is supportive, with carryover and time-related limitations."
**Source:** `02_research/phase2_paper_explained.md`, `02_research/phase2_results.md`.

---

## Slide 7 — Systemic primary result

### Dazodalibep produced greater ESSDAI improvement than placebo in Phase 2

**Exhibit**

| Day-169 change | Dazodalibep | Placebo |
|---|---:|---:|
| Adjusted mean ± SE | −6.3 ±0.6 | −4.1 ±0.6 |

**Callout:** Adjusted difference **−2.2 points**; reported **90% CI** approximately −3.6 to −0.7; **p=0.0167**.
**On-slide copy:**
- The prespecified primary result supports systemic efficacy.
- The trial used two-sided α=0.10 (small-N caution); this result also clears standard 0.05.
- Small sample size leaves uncertainty about the reproducible effect.

**Visual:** ESSDAI change-from-baseline line plot, both arms, error bars, N-at-risk table beneath (mirrors paper Fig. 2a). Label the 90% CI explicitly — do not present interchangeably with a 95% CI used elsewhere.
**Speaker note:** "This is evidence against the null under the trial's analysis. The p-value is not a 1.7% probability the result is a fluke, nor does it establish the study's power."
**Source:** `02_research/phase2_results.md`.

---

## Slide 8 — Consistency and limitations

### Responder and subgroup results support a cautious interpretation of the systemic signal

**Exhibit A: day-169 response**

| Improvement threshold | DAZ | Placebo | p-value |
|---|---:|---:|---:|
| ≥3 ESSDAI points | 26/36; 72.2% | 22/37; 59.5% | 0.3283 |
| ≥4 ESSDAI points | 24/36; 66.7% | 18/37; 48.6% | 0.1823 |
| ≥5 ESSDAI points | 61.1% | 35.1% | 0.0449; post hoc |

**Exhibit B:** Exploratory adjusted difference without RA/SLE ≈−1.6; with RA/SLE ≈−3.3. Small subgroup Ns.
**On-slide takeaway:** Directionally favorable results do not establish a robust responder effect or a treatment-by-subgroup interaction.
**Visual:** Grouped responder bars with denominators (n/N) on each bar, not just %. Small separate subgroup panel labeled "exploratory, small N."
**Speaker note:** "Nonsignificant responder outcomes do not prove a faulty endpoint — dichotomizing loses information and the sample is small."
**Source:** `02_research/phase2_results.md`.

---

## Slide 9 — Symptom evidence

### The symptom cohort showed a broad signal across dryness, fatigue and pain

**Exhibit: Population 2, day 169**

| Outcome | DAZ change | Placebo change | p-value |
|---|---:|---:|---:|
| ESSPRI total — primary | −1.80 | −0.53 | 0.0002 |
| Dryness | −1.9 | −0.8 | 0.0066 |
| Fatigue | −1.7 | −0.3 | 0.0022 |
| Pain | −1.8 | −0.4 | 0.0010 |

**On-slide copy:** Adjusted total-score contrast −1.27; 90% CI −1.82 to −0.73. Directional consistency across symptom domains supports the read-through.
**Visual:** Grouped domain bars plus prominent primary-endpoint callout. Label domain tests as supportive/unadjusted for multiplicity.
**Speaker note:** "Both the total score and its components favor treatment, but Phase 3 tests a later timepoint and also lists DASPRI as a second co-primary."
**Source:** `02_research/phase2_results.md`.

---

## Slide 10 — Pharmacodynamics and durability

### Biomarker suppression supports drug activity; crossover patterns add qualified evidence

**Exhibit A: adjusted geometric mean ratio to baseline at day 169**

| Biomarker | Population 1: DAZ / Placebo | Population 2: DAZ / Placebo |
|---|---|---|
| CXCL13 | 0.67 / 1.00 | 0.56 / 1.06 |
| Rheumatoid factor | 0.66 / 1.13 | 0.54 / 0.94 |

**Exhibit B: change from baseline, day 169 → day 365 (crossover)**

| Population / sequence | Trajectory |
|---|---|
| Systemic, placebo→DAZ | ESSDAI −4.1 → −6.3 |
| Systemic, DAZ→placebo | ESSDAI −6.3 → −4.4 |
| Symptomatic, DAZ→placebo | ESSPRI −1.8 → −1.9 |

**On-slide takeaway:** Pharmacological activity is supported; durable clinical efficacy under the Phase 3 regimen remains a separate question.
**Visual:** Biomarker dot plot against baseline ratio of 1.0, both arms shown (not just DAZ), plus compact crossover table.
**Speaker note:** "Biomarker values are ratios to each arm's own baseline, not direct drug/placebo ratios. A crossover is not a 48-week parallel-group replication."
**Source:** `02_research/phase2_results.md`.

---

## Slide 11 — Phase 2-to-3 bridge

### Phase 3 increases information and changes duration and dose comparisons

**Exhibit**

| Factor | Phase 2 systemic | Phase 3 systemic | Forecast implication |
|---|---|---|---|
| Randomized total | 74 | 651 | More precision; not proportional effect growth |
| Active/control n (one comparison) | 36 / 38 | ~217 / 217 assumed | ≈6.0× per-arm increase |
| Primary assessment | Day 169 | Week 48 | Longer durability and placebo-response window |
| Active regimens | One dose | Two dose arms | Dose selection and multiplicity matter |
| ESSDAI entry floor | ≥5 | ≥5 | No established loosening of this threshold |
| Baseline/domain mix | Observed | Not established | A real transportability uncertainty |

**Speaker note:** "The per-arm comparison (≈6.0×) is the statistically relevant one — total-enrollment ratios mix in the number of arms and overstate the effective information gain."
**Visual:** Bridge table with "known" vs. "assumed/unknown" column shading. No numerical waterfall unless each adjustment has a defensible basis.
**Source:** `03_analysis/final_thesis.md`, `02_research/phase2_baseline_characteristics.md`. Allocation assumed equal; not confirmed by registry.

---

## Slide 12 — Dose rationale and testing architecture

### PK/PD supports dose selection, while clinical effect and testing rules remain separate

**On-slide copy**
- A population PK/PD model pooled 4 trials (healthy volunteers, RA, Sjögren's), relating exposure to immune biomarkers.
- Sjögren's patients clear the drug more slowly than healthy volunteers/RA patients — a real, population-specific PK finding.
- The model supports the proposed Phase 3 doses achieving sustained exposure above the Ki67+/RF biomarker IC50 — a pharmacodynamic target, not a clinical efficacy guarantee.
- Two active arms vs. one shared placebo raises a multiplicity question with no public testing-hierarchy disclosure.

**Visual — two boxes:**
- Left, "Confirmed": "3 arms — Dose 1, Dose 2, Placebo; doses/allocation not disclosed"
- Right, "Illustrative only — not confirmed": simple tree, total α=0.05 split into two α=0.025 comparisons, captioned "one possible scheme, not Amgen's actual plan"

**Speaker note:** "The model describes sustained average exposure relative to biomarker IC50 — it does not prove trough coverage for every participant, or quantify the ESSDAI gain."
**Source:** `03_analysis/additional_topics.md`, `03_analysis/scenario_model.md`.

---

## Slide 13 — Ianalumab read-through

### Ianalumab validates week-48 ESSDAI as a feasible endpoint, with modest effect sizes

**Exhibit: individual Phase 3 results**

| Trial / regimen | Effect | 95% CI | p-value |
|---|---:|---|---:|
| NEPTUNUS-1, monthly | −1.3 | −2.6 to 0.0 | 0.0496 |
| NEPTUNUS-2, monthly | −1.0 | −2.0 to 0.0 | 0.041 |
| NEPTUNUS-2, every 3 months | Not significant | — | — |

**On-slide copy**
- Monthly treatment met the endpoint in both trials; less-frequent dosing did not.
- Ph2b met its prespecified dose-response objective (4 of 5 models significant); the 300mg pairwise comparison alone (p≈0.092) does not define trial failure.

**Visual:** Forest plot — trial, frequency, arm Ns, CI shown.
**Speaker note:** "I use these data to check plausible effects and precision, not to establish cross-trial superiority."
**Source:** `02_research/ianalumab_competitor_analysis.md`. Registry lists NEPTUNUS-2 N=506; conference presentation cites N=504 — this discrepancy is unresolved, report both rather than picking one.

---

## Slide 14 — Pathway and historical lessons

### Same-pathway evidence supports systemic activity more clearly than universal symptom benefit

**Exhibit**

| Evidence | Result | What it contributes |
|---|---|---|
| Iscalimab systemic cohort, N=173 | Met dose-response objective | Supports CD40 pathway plausibility |
| Iscalimab symptom cohort, N=100 | ESSPRI −0.57; p=0.12 | Symptom benefit not assured by pathway alone |
| Abatacept ASAP-III | Missed continuous ESSDAI primary | Plausible biology can still fail clinically |
| Rituximab TRACTISS | Missed symptom-VAS responder primary | Endpoint/population selection matters |
| Tocilizumab ETAP | Missed composite-response primary | Distinct response construct, not continuous ESSDAI |

**On-slide takeaway:** Use prior trials to challenge assumptions; avoid a numerical "class success rate."
**Speaker note:** "This set is not a meta-analysis or calibrated prior. Dazodalibep's own Phase 2 is not counted again as independent external validation."
**Visual:** Evidence matrix, not a green/red success pie chart.
**Source:** `02_research/historical_trial_evidence.md`.

---

## Slide 15 — Explicit effect assumptions

### A 1.4-point base assumption retains about two-thirds of the Phase 2 effect

**Exhibit**

| Case | Assumed benefit | Retention vs. 2.2 | Rationale |
|---|---:|---:|---|
| Bull | 2.0 | 91% | Most of the Phase 2 signal persists |
| Base | 1.4 | 64% | Meaningful attenuation without loss of activity |
| Bear | 0.6 | 27% | Substantial attenuation via efficacy, measurement, or population differences |

**On-slide copy:** The base case is a judgment call, not a fitted or empirically estimated mean — tested across a range rather than one decimal point.
**Visual:** Three labeled points on a benefit axis, Phase 2's observed 2.2 shown as a separate reference marker.
**Speaker note:** "Why 1.4? A conservative departure from 2.2, in the range relevant clinical precedents suggest. The conclusion shouldn't depend on spurious decimal precision."
**Source:** `03_analysis/scenario_model.md`. Scenario weights are analyst judgment, not empirically estimated probabilities — omit numeric weights from the main slide unless prepared to defend them.

---

## Slide 16 — Conditional power

### The base effect has favorable power under nominal testing, but the margin narrows with stricter assumptions

**Exhibit: one active-dose comparison, n=217/arm, effective SD=5.47**

| Assumed true benefit | Power at α=0.05 | Power at illustrative α=0.025 |
|---|---:|---:|
| 0.6 | 21% | 14% |
| 1.0 | 48% | 37% |
| 1.4 | 76% | 66% |
| 1.6 | 86% | 79% |
| 2.0 | 97% | 94% |

**On-slide takeaway:** Statistical success remains genuinely uncertain even if the assumed biological effect is correct.
**Visual:** Conditional-power curve with vertical markers at bear/base/bull; a table is fully acceptable if a chart isn't built in time.
**Speaker note:** "These curves describe repeated samples under fixed assumptions — not the unconditional probability that Amgen's actual trial succeeds."
**Source:** `03_analysis/scenario_model.md`. SD=5.47 is a comparator-based sensitivity, not a measured dazodalibep Phase 3 SD.

---

## Slide 17 — Variance, missing data, and falsifiability

### Higher variance and information loss can materially weaken the same efficacy forecast

**Exhibit: assumed true benefit fixed at 1.4**

| Assumption | n/arm | α | Approx. power |
|---|---:|---:|---:|
| SD 3.65 | 217 | 0.05 | 98% |
| SD 5.00 (Ph2 planning) | 217 | 0.05 | 83% |
| SD 5.47 (ianalumab-based) | 217 | 0.05 | 76% |
| SD 5.47, stricter α | 217 | 0.025 | 66% |
| Same, reduced effective n | 184 | 0.025 | 58% |

**On-slide copy:**
- Raw sample size alone is insufficient — repeated measurement and adjustment affect precision.
- Phase 3's treatment of missing data/rescue medication is unknown and matters.

**Visual:** Horizontal dot plot or heatmap; five rows maximum for legibility.
**Speaker note:** "The strongest bear case is a small retained effect under realistic noise and testing requirements — not simply that the study is larger."
**Source:** `03_analysis/scenario_model.md`.

---

## Slide 18 — Symptomatic trial conclusion

### ESSPRI evidence supports optimism; DASPRI is a new, FDA-PRO-aligned instrument with zero track record for this drug

**Exhibit**

| Question | Evidence available | Interpretation |
|---|---|---|
| Does DAZ improve reported symptoms? | Positive Phase 2 ESSPRI total/domain results | Supports a positive ESSPRI lean |
| Does benefit extend to week 48? | Supportive crossover only, no parallel-group replication | Durability remains a test |
| What supports DASPRI? | **Confirmed absent from the Phase 2 paper — searched full text, zero occurrences.** DASPRI was developed as a patient-symptom diary specifically to align with FDA patient-reported-outcome guidance | No dazodalibep-specific precedent exists for this instrument at all; likely added for regulatory-alignment reasons, not because ESSPRI underperformed |
| What defines overall trial success? | Two co-primary outcomes; procedure not established | Do not assume both-pass or either-pass rule |

**On-slide takeaway:** Favorable symptom evidence on the instrument with a track record (ESSPRI); genuine, unresolvable-from-public-data uncertainty on the instrument without one (DASPRI) — this isn't a research gap to close, it's a real fact about the evidence base.
**Visual:** Table above, framed as a factual finding, not an apology for missing work.
**Speaker note:** "I checked the full text of the Phase 2 paper directly — DASPRI genuinely isn't in it. This is likely because it's a newer instrument built for FDA PRO alignment, added specifically for the Phase 3 registration package."
**Source:** `02_research/nct06245408_risk_note.md`.

---

## Slide 19 — Benefit-risk

### Fc-free engineering addresses a known mechanism; Phase 2 safety still warrants careful scrutiny

**Exhibit: selected serious observations, not an exhaustive safety table**

| Observation | Population | Attribution and precise timing |
|---|---|---|
| DVT and drug-induced liver injury, same participant | Population 1 | Both investigator-attributed as related; onset 180 days after last DAZ dose |
| Invasive ductal breast carcinoma | Population 2 | Investigator-attributed as related; onset 139 days after last dose |
| One death, unknown cause following COVID-19 diagnosis | Population 1 | SAE reported during Stage I per the paper's text; investigators considered it unrelated; the death itself is tabulated under the Stage II+follow-up safety window (46 days post-last-dose) in Table 3 — both facts are accurate and reported together here, not simplified to one label |

**On-slide copy:** Three investigator-attributed serious events in two participants, plus a separately described unrelated death. Individual events in a small trial establish neither causation nor absence of risk.
**Visual:** Compact table with denominators in a footnote (Stage I systemic DAZ n=36; Stage II systemic DAZ→placebo n=34; symptomatic safety set n=48).
**Speaker note:** "I separate investigator attribution from demonstrated causality, and primary efficacy from overall benefit-risk."
**Source:** `02_research/phase2_results.md`.

---

## Slide 20 — Close with the forecast and what will change it

### Our positive systemic forecast stands or falls on the prespecified primary result

**On-slide copy**
**Forecast:** Expect positive ESSDAI efficacy in NCT06104124; favorable ESSPRI evidence with unresolved full-trial interpretation for NCT06245408.

**Exhibit**

| Readout | Interpretation |
|---|---|
| Prespecified primary procedure met, consistent dose results | Confirms the forecast; assess magnitude and safety separately |
| Primary met, modest effect or mixed supportive outcomes | Statistical win with a more qualified clinical interpretation |
| Prespecified primary procedure not met | Forecast was wrong — evaluate why without redefining success post hoc |
| Efficacy positive, concerning safety pattern | Efficacy call may be right while benefit-risk remains unfavorable |

**Timeline footer:** Registry export: systemic primary completion July 23, 2026; study completion August 17, 2026 (both actual). Symptomatic: primary completion est. October 22, 2026; study completion est. December 17, 2026. Completion is not disclosure — no specific announcement date is established here.
**Speaker note:** "A failed primary test is a failed forecast even if the biology remains interesting. A successful primary test should not be relabeled failure merely because a secondary threshold disappoints."
**Source:** `01_data/`, `03_analysis/final_thesis.md`.

---

# Part II — Appendix (6 slides)

## Appendix 1 — Registry facts and unresolved design fields

| Field | Systemic | Symptomatic |
|---|---|---|
| NCT | NCT06104124 | NCT06245408 |
| Enrollment | 651 | 434 |
| Status | Completed | Active, not recruiting |
| Primary outcomes | ESSDAI | ESSPRI; DASPRI |
| Primary assessment | Week 48 | Week 48 |
| Primary completion | 2026-07-23 (actual) | 2026-10-22 (estimated) |
| Study completion | 2026-08-17 (actual) | 2026-12-17 (estimated) |

**Fields not represented by the registry export**: arm doses/frequency, allocation ratio, full eligibility text, background-treatment stability, rescue rules, complete outcome definitions, protocol/SAP, analysis population, actual/estimated date flags beyond what's shown. Do not present this table as a complete protocol abstraction.
**Source:** `01_data/NCT06104124.csv`, `01_data/NCT06245408.csv`.

## Appendix 2 — Baseline characteristics (verified directly against Table 1, page 4)

| Characteristic | Pop 1 Placebo | Pop 1 DAZ | Pop 2 Placebo | Pop 2 DAZ |
|---|---:|---:|---:|---:|
| N | 38 | 36 | 55 | 54 |
| Baseline ESSDAI, mean (SD) | 10.1 (4.1) | 11.4 (4.5) | 2.5 (1.6) | 3.1 (1.8) |
| Baseline ESSPRI total | 6.6 (1.8) | 6.6 (1.6) | 7.1 (1.1) | 7.5 (1.5) |
| Dryness | 6.9 (2.3) | 7.3 (1.7) | 6.8 (1.2) | 7.1 (1.6) |
| Fatigue | 6.8 (2.2) | 7.0 (1.7) | 6.8 (1.8) | 7.1 (1.8) |
| Pain | 6.1 (2.3) | 5.5 (3.0) | 6.3 (1.9) | 6.6 (2.6) |
| OSDI | 40.0 (20.9) | 48.7 (25.0) | 48.6 (19.2) | 48.2 (23.8) |
| Stimulated salivary flow, mL/min | 0.97 (0.85) | 0.88 (0.64) | 0.83 (0.83) | 1.10 (1.18) |
| Concomitant RA/SLE | 9 (23.7%) | 7 (19.4%) | 7 (12.7%) | 4 (7.4%) |

Schirmer's criterion: **≤5mm/5min in at least one eye** (corrected from an earlier
transcription error — this direction is confirmed against the source).

**Note on this table's provenance**: these values were independently re-verified
directly against the rendered Table 1 image three separate times across this
project's review history, after two different external reviews both proposed
alternate values for the Population 2 ESSPRI-total/Dryness/OSDI/salivary-flow rows.
On each re-check, the values above matched the source exactly; the proposed
alternates did not (they appear to reflect a row-transposition error, repeated across
both reviews). Use the values above.

Relevant background therapy: Population 1 had 59.5% antimalarial, 41.9%
glucocorticoid, 31.1% conventional DMARD use overall. Population 2 cholinergic
agonist use differed: 11.1% DAZ vs. 27.3% placebo.
**Source:** `02_research/phase2_baseline_characteristics.md`, verified against `00_reference/phase2_paper.pdf` Table 1.

## Appendix 3 — Supportive outcomes and domain scope

| Day-169 outcome | Population | DAZ / Placebo change | p-value |
|---|---|---:|---:|
| ESSPRI | Systemic | −1.8 / −1.1 | 0.1110 |
| FACIT-Fatigue | Systemic | +8.1 / +5.8 | 0.3028 |
| FACIT-Fatigue | Symptomatic | +8.1 / +2.8 | 0.0095 |
| OSDI | Systemic | −16.00 / −14.02 | 0.6583 |
| OSDI | Symptomatic | −13.95 / −8.52 | 0.1936 |
| Stimulated salivary flow | Systemic | +0.39 / +0.14 | 0.1330 |
| Stimulated salivary flow | Symptomatic | +0.20 / −0.01 | 0.2170 |

These are unadjusted supportive/exploratory p-values. Positive FACIT change = improvement; negative OSDI/ESSPRI change = improvement.
**Source:** `02_research/phase2_results.md`.

## Appendix 4 — Reproducible statistical method

**Definitions:** delta = assumed true positive treatment benefit; n = per-arm sample size; sigma = assumed effective SD.

```
SE = sigma * sqrt(2 / n)
critical_z = inverse_normal_cdf(1 - alpha/2)
power(delta) = normal_cdf(delta/SE - critical_z)
effect_for_80_percent_power ≈ (critical_z + inverse_normal_cdf(0.80)) * SE
```

| Sigma | n | Alpha | SE | Observed threshold | Effect for ~80% power |
|---:|---:|---:|---:|---:|---:|
| 3.65 | 217 | 0.05 | 0.350 | 0.687 | 0.982 |
| 5.00 | 217 | 0.05 | 0.480 | 0.941 | 1.345 |
| 5.47 | 217 | 0.05 | 0.525 | 1.029 | 1.471 |
| 5.47 | 217 | 0.025 | 0.525 | 1.177 | 1.619 |
| 5.47 | 184 | 0.025 | 0.570 | 1.278 | 1.758 |

**Input provenance:** 3.65 from dazodalibep's own Phase 2 SEs (approximate back-calculation); 5.00 is the Phase 2 protocol's own planning SD; 5.47 is the effective SD implied by NEPTUNUS-1's reported SE. None is the actual, undisclosed dazodalibep Phase 3 variance.
**Interpretive rule:** an assumed true delta produces conditional power, not a guaranteed p-value. NEPTUNUS-1's SE scaled only for sample size (0.66×√(137/217)=0.524) implies that an *observed* 1.3-point difference would carry p≈0.013 at dazodalibep's assumed N — a precision-scaling illustration, not a forecast.
**Source:** `03_analysis/scenario_model.md`.

## Appendix 5 — Expanded comparator and safety context

Full ianalumab arm-by-arm data (Ph2b dose-response + individual pairwise arms + both NEPTUNUS trials, including the every-3-months miss), the complete historical evidence table (TRACTISS/ETAP/ASAP-III with corrected endpoint classifications), and the full Phase 2 safety table (all AEs, not just headline SAEs) — pull directly from `02_research/ianalumab_competitor_analysis.md`, `02_research/historical_trial_evidence.md`, `02_research/phase2_results.md` for this slide's exact content; too long to reproduce inline here.

## Appendix 6 — Source library

- **St. Clair EW et al.** CD40 ligand antagonist dazodalibep in Sjögren's disease: a randomized, double-blinded, placebo-controlled, phase 2 trial. *Nature Medicine* 30, 1583–1592 (2024). DOI: 10.1038/s41591-024-03009-3. Open access (CC-BY 4.0). Local: `00_reference/phase2_paper.pdf`.
- **ClinicalTrials.gov, NCT06104124** — systemic Phase 3. Local: `01_data/NCT06104124.csv`.
- **ClinicalTrials.gov, NCT06245408** — symptomatic Phase 3. Local: `01_data/NCT06245408.csv`.
- **Bowman SJ et al.** Safety and efficacy of subcutaneous ianalumab in primary Sjögren's syndrome: phase 2b dose-finding trial. *Lancet* 399, 161–171 (2022; online 2021). PMID 34861168.
- **Fisher BA et al.** Safety and efficacy of subcutaneous iscalimab in two distinct populations of patients with Sjögren's disease (TWINSS). *Lancet* (2024). PMID 39096929.
- **Novartis Immunology Pipeline Event**, Oct 2025 — NEPTUNUS individual-arm efficacy data.
- **Seror R et al.** ESSDAI/ESSPRI MCID and disease-activity states, *Ann Rheum Dis*.
- **Der K et al.** Population PK/PD modeling of dazodalibep. ACR Convergence 2023 abstract.
- **Felten et al., ETAP.** Interleukin-6 receptor inhibition in primary Sjögren syndrome. PMID 33208345. *(Note: verify the "p=0.14" figure against this primary source before final use — flagged as unconfirmed, see `02_research/historical_trial_evidence.md`.)*
- **van Nimwegen et al., ASAP-III.** Primary randomized trial, *Lancet Rheumatology*.
- TRACTISS primary trial report.
