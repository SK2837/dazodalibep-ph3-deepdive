# Dazodalibep Phase 3: recommended presentation content

**Independent content recommendation and second project review | September 15, 2026**

Prepared after reviewing `05_deck/slide_by_slide_outline.md`, the revised research, model, evidence table, summaries, registry exports and the local Phase 2 publication. The existing project files are preserved. This file provides a replacement presentation narrative and identifies residual errors; it is not a completed PowerPoint.

## Start here: what I would present

**Main call:** “We expect a positive ESSDAI primary-endpoint readout from NCT06104124. The randomized Phase 2 signal and external clinical evidence support that forecast, but its robustness depends on retained efficacy, variance and the prespecified testing strategy.”

**Secondary position:** “NCT06245408 has encouraging symptom evidence. We lean positive on ESSPRI, but have less evidence to assess DASPRI and the trial's full success criteria.”

This is a clear forecast with explicit limitations. A precise overall probability is not necessary. Conditional power is useful supporting analysis, but is not a probability that the biological hypothesis is true.

**Recommended length:** 20 main slides and 6 appendix slides. Allow roughly 25–30 minutes for a full discussion, or combine slides 3/4 and 15/16 and move slide 10 into the appendix for a shorter presentation. The assignment does not specify a slide count.

**Narrative:** clinical question → biological rationale → Phase 2 strength and limits → Phase 3 changes → competitor lessons → explicit forecast assumptions → statistical stress tests → readout interpretation.

### How to use this file

- Copy the **On-slide copy** and the compact exhibits into PowerPoint.
- Use the **Speaker note** for explanation; do not place the whole note on the slide.
- Use **Source** for the slide footer and the reference appendix. Source IDs resolve to the links near the end of this file.
- Labels such as “observed,” “analyst assumption,” and “not established from available documents” belong beside the relevant claim.
- Review comments and production checks at the end of this file are for you, not for the audience.

---

# Part I — Main presentation

## Slide 1 — Title

### Dazodalibep in Sjögren's disease: a positive systemic readout is plausible, but the margin matters

**On-slide copy**

Clinical deep dive on Amgen's Phase 3 program

- Primary forecast: NCT06104124 — systemic disease activity
- Supporting assessment: NCT06245408 — symptom burden
- Analysis cutoff: September 15, 2026
- Prepared by: [candidate name]

**Visual:** restrained title slide, with the two trial identifiers beneath the subtitle.

**Speaker note:** “I focus the quantitative forecast on the systemic trial, as permitted by the brief, and use the symptomatic study to assess how far the evidence extends across the program.”

**Source:** Jefferies assignment brief; R2–R3 for trial identities. Do not reproduce Jefferies' analyst attribution or imply authorship by its research team.

## Slide 2 — Executive conclusion

### We expect NCT06104124 to meet its ESSDAI primary endpoint, with meaningful residual risk

**On-slide copy**

1. **Direct clinical evidence:** Phase 2 showed a −2.2-point adjusted ESSDAI difference at day 169; p=0.0167.
2. **Biological coherence:** CD40L blockade reduced immune biomarkers; iscalimab provides additional evidence for the pathway.
3. **Confirmatory precedent:** ianalumab demonstrated that week-48 ESSDAI benefit can be detected in Phase 3.

**Main risk:** a smaller week-48 effect combined with higher variance or stricter testing could turn an encouraging signal into a negative primary result.

**Exhibit**

| Forecast | Conclusion | Basis / boundary |
|---|---|---|
| Systemic trial | Expect positive | Qualitative analyst forecast; stress-tested below |
| Symptomatic trial | Positive ESSPRI lean | DASPRI and full success-rule uncertainty limit conviction |

**Speaker note:** “My positive call comes from the evidence as a whole. Larger enrollment improves precision; it does not establish that the drug will retain its Phase 2 effect.”

**Source:** R1, R4–R6; analyst assessment. No numerically calibrated program probability is claimed.

## Slide 3 — Define the question

### The program tests two distinct clinical questions at week 48

**Exhibit**

| | Systemic: NCT06104124 | Symptomatic: NCT06245408 |
|---|---|---|
| Clinical focus | Moderate-to-severe systemic activity | High symptoms with limited systemic activity |
| Core eligibility described in research | ESSDAI ≥5 | ESSPRI ≥5; ESSDAI <5 |
| Enrollment in saved registry export | 651 | 434 |
| Primary outcomes listed | ESSDAI change from baseline | ESSPRI and DASPRI change from baseline |
| Primary assessment | Week 48 | Week 48 |
| This presentation | Full efficacy forecast | Directional supporting assessment |

**On-slide takeaway:** “Positive” means success under the prespecified primary testing procedure. Statistical significance, clinical importance and benefit-risk are assessed separately.

**Speaker note:** “Two outcomes listed as primary do not, by themselves, tell us whether both must pass or a hierarchy applies. I do not infer that rule from the registry labels.”

**Visual:** a clean two-column trial card, not a screenshot of the registry.

**Source:** R2–R3, using local exports in `01_data`; full eligibility and testing details require the protocol/registry text. The CSVs do not contain complete inclusion/exclusion criteria.

## Slide 4 — Disease and endpoint distinction

### Reducing systemic activity and improving dryness, fatigue and pain are related—but separate—tests

**On-slide copy**

- **ESSDAI:** clinician-assessed systemic disease activity across weighted domains.
- **ESSPRI:** patient-reported dryness, fatigue and pain; improvement means a lower score.
- Symptoms can reflect several processes; immune suppression need not produce the same benefit in every domain.

**Visual:** two columns, “Systemic activity” and “Patient symptoms,” connected by a partial overlap rather than an equality sign. Show representative domains, not a dense organ inventory.

**Speaker note:** “The two populations should not be reduced to ‘reversible’ versus ‘irreversible’ disease. Residual gland function may matter, but fatigue and pain are not simply measurements of gland damage. Endpoint differences must remain part of the forecast.”

**Source:** R1 and R7. Present the final point as clinical interpretation, not a proven explanation of response differences.

## Slide 5 — Biological rationale

### CD40L blockade interrupts immune-cell costimulation implicated in Sjögren's disease

**On-slide copy**

- CD40L–CD40 signaling supports T-cell/B-cell interactions and downstream immune activation.
- Dazodalibep blocks the ligand; iscalimab targets the receptor.
- Dazodalibep's Fc-free Tn3 scaffold is designed to avoid the Fc-mediated platelet activation implicated with earlier anti-CD40L antibodies.

**Visual specification**

T cell / CD40L → CD40 on B cell and antigen-presenting cell → immune activation / antibody responses.

Place dazodalibep at CD40L and iscalimab at CD40. Put ianalumab on a separate BAFF-R/B-cell branch. Include a small note: “Engineering addresses a known mechanism; clinical safety still requires evidence.”

**Speaker note:** “The mechanism establishes plausibility. The randomized clinical results are the direct test of efficacy, and pharmacodynamic data help establish whether the expected biology is affected.”

**Source:** R1 introduction and references 13–25; R4–R5 for comparator targets. Avoid the unsupported term “PASylated.”

## Slide 6 — Phase 2 design

### Phase 2 provides two randomized efficacy tests, followed by a blinded treatment switch

**Exhibit**

| | Population 1 | Population 2 |
|---|---|---|
| Randomized N | 74 | 109 |
| Dazodalibep / placebo | 36 / 38 | 54 / 55 |
| Core entry criteria | ESSDAI ≥5 | ESSPRI ≥5, ESSDAI <5; stimulated flow ≥0.1 mL/min |
| Primary outcome | ESSDAI change, day 169 | ESSPRI change, day 169 |
| Stage I completion | 71/74 | 102/109 |

**On-slide copy:** One IV regimen: 1,500 mg every two weeks for three doses, then every four weeks for four doses. No dose-ranging in this Sjögren's study.

**Visual:** two study lanes with day 169 highlighted; show Stage II switch separately. Do not imply continuous active dosing for everyone through day 365.

**Speaker note:** “The strongest evidence is the prespecified randomized first period. The crossover is supportive, with carryover and time-related limitations.”

**Source:** R1, Results and Extended Data Figure 1.

## Slide 7 — Systemic primary result

### Dazodalibep produced greater ESSDAI improvement than placebo in Phase 2

**Exhibit data**

| Day-169 change | Dazodalibep | Placebo |
|---|---:|---:|
| Adjusted mean ± SE | −6.3 ±0.6 | −4.1 ±0.6 |

**Callout:** Adjusted difference **−2.2 points**; reported 90% CI approximately **−3.6 to −0.7**; **p=0.0167**.

**On-slide copy**

- The prespecified primary result supports systemic efficacy.
- The trial used two-sided alpha 0.10; this result also clears nominal 0.05.
- Small sample size leaves uncertainty about the reproducible effect.

**Visual:** reproduce Figure 2a using published source data if available. Otherwise use the endpoint mean/error-bar plot above; do not invent intervening timepoints. Mark error bars as SE and label the contrast CI separately.

**Speaker note:** “This is evidence against the null under the trial's analysis. The p-value is not a 1.7% probability that the result is a fluke. Nor does the observed p-value establish the study's power for the observed effect.”

**Source:** R1 Figure 2a, Table 2 and Statistical analysis.

## Slide 8 — Consistency and limitations

### Responder and subgroup results support a cautious interpretation of the systemic signal

**Exhibit A: day-169 response**

| Improvement threshold | DAZ | Placebo | p-value |
|---|---:|---:|---:|
| ≥3 ESSDAI points | 26/36; 72.2% | 22/37; 59.5% | 0.3283 |
| ≥4 ESSDAI points | 24/36; 66.7% | 18/37; 48.6% | 0.1823 |
| ≥5 ESSDAI points | 61.1% | 35.1% | 0.0449; post hoc |

**Exhibit B:** Exploratory adjusted difference without RA/SLE **−1.6** (29/29 participants); with RA/SLE **−3.3** (7/9). Active/placebo Ns shown.

**On-slide takeaway:** Directionally favorable results do not establish a robust responder effect or a treatment-by-subgroup interaction.

**Visual:** grouped responder bars; subgroup estimates in a small separate table. Add “secondary; no multiplicity adjustment” and “exploratory” beside the respective panels.

**Speaker note:** “The subgroup contrast motivates a population-composition question. It is not a validated correction factor. Nonsignificant responder outcomes also do not prove a faulty endpoint; thresholding loses information.”

**Source:** R1 Table 2, Figure 2 and Extended Data Table 1. Preserve the published placebo denominator of 37 rather than converting every percentage to N=38.

## Slide 9 — Symptom evidence

### The symptom cohort showed a broad signal across dryness, fatigue and pain

**Exhibit data: Population 2, day 169**

| Outcome | DAZ change | Placebo change | p-value |
|---|---:|---:|---:|
| ESSPRI total — primary | −1.80 | −0.53 | 0.0002 |
| Dryness | −1.9 | −0.8 | 0.0066 |
| Fatigue | −1.7 | −0.3 | 0.0022 |
| Pain | −1.8 | −0.4 | 0.0010 |

**On-slide copy:** Adjusted total-score contrast −1.27; 90% CI −1.82 to −0.73. Directional consistency across symptom domains supports the ESSPRI read-through.

**Visual:** grouped domain bars plus a prominent primary-endpoint callout. Label domain tests as supportive and unadjusted for multiplicity.

**Speaker note:** “This is more informative than simply ranking the cohorts by p-value. Both the total score and its components favor treatment, but Phase 3 tests a later timepoint and also lists DASPRI.”

**Source:** R1 Figure 3, Table 2 and Population 2 Results. Keep the systemic and symptomatic scales separate.

## Slide 10 — Pharmacodynamics and durability

### Biomarker suppression supports drug activity; crossover patterns add qualified evidence

**Exhibit A: adjusted geometric mean ratio to baseline at day 169**

| Biomarker | Population 1: DAZ / placebo | Population 2: DAZ / placebo |
|---|---|---|
| CXCL13 | 0.67 / 1.00 | 0.56 / 1.06 |
| Rheumatoid factor | 0.66 / 1.13 | 0.54 / 0.94 |

**Exhibit B: change from original baseline, day 169 → day 365**

| Population / sequence | Trajectory |
|---|---|
| Systemic, placebo → DAZ | ESSDAI −4.1 → −6.3 |
| Systemic, DAZ → placebo | ESSDAI −6.3 → −4.4 |
| Symptomatic, DAZ → placebo | ESSPRI −1.8 → −1.9 |

**On-slide takeaway:** Pharmacological activity is supported; durable clinical efficacy under the Phase 3 regimen remains a separate question.

**Visual:** simple biomarker dot plot against a baseline ratio of 1.0, with a compact crossover table. If crowded, retain CXCL13 in the main panel and move RF to appendix.

**Speaker note:** “The biomarker values are ratios to each arm's own baseline, not direct drug/placebo ratios. The systemic off-drug pattern differs from the sustained symptom pattern. A crossover is not a 48-week parallel-group replication.”

**Source:** R1 biomarker Results and Extended Data Figures 2–3. Do not claim validated biomarker surrogacy for ESSDAI.

## Slide 11 — Phase 2-to-3 bridge

### Phase 3 increases information and changes duration and dose comparisons

**Exhibit**

| Factor | Phase 2 systemic | Phase 3 systemic | Forecast implication |
|---|---|---|---|
| Randomized total | 74 | 651 | More precision; not proportional effect growth |
| Active / control n | 36 / 38 | About 217 / 217 assumed for one dose comparison | Roughly 6× per arm, not 8.8× information per comparison |
| Primary assessment | Day 169 | Week 48 | Longer durability and placebo-response test |
| Active regimens | One | Two active arms | Dose selection and multiplicity matter |
| ESSDAI entry floor | ≥5 | ≥5 in project research | No established loosening of this threshold |
| Actual baseline/domain mix | Observed | Not established from supplied results | A transportability uncertainty |

**Speaker note:** “The ninefold total-enrollment ratio mixes different numbers of arms. For power, the relevant inputs are the active and placebo groups in the comparison. Larger enrollment does not itself cause effect erosion.”

**Visual:** bridge table with “known” and “assumed/unknown” labels. Avoid a numerical waterfall unless each adjustment has a defensible quantitative basis.

**Source:** R1–R2; analyst calculation assuming equal allocation. Preserve this assumption until allocation is verified from a complete primary document.

## Slide 12 — Dose rationale and testing architecture

### PK/PD supports dose selection, while clinical effect and testing rules remain separate

**On-slide copy**

- A population model pooled four studies and related exposure to immune biomarkers.
- The model supports the proposed Phase 3 doses; biomarker exposure targets are not clinical efficacy thresholds.
- With two active arms and a shared placebo, the testing procedure affects the required evidence.

**Visual:** left: exposure → biomarker response → clinical response, with the final link marked “not quantitatively established.” Right: Dose 1 and Dose 2 versus shared placebo; note “hierarchy not established from reviewed documents.”

**Speaker note:** “The model describes sustained average exposure relative to biomarker IC50. It does not prove every participant's trough remains above the threshold, or quantify the ESSDAI gain. I show alpha sensitivities rather than inventing the sponsor's procedure.”

**Source:** R8, R2. Do not label absolute mg doses as universally undisclosed: they were not established in the sources reviewed here.

## Slide 13 — Ianalumab read-through

### Ianalumab validates week-48 ESSDAI as a feasible endpoint, with modest effect sizes

**Exhibit: individual Phase 3 results**

| Trial / regimen | DAZ-independent comparator effect | 95% CI | p-value |
|---|---:|---|---:|
| NEPTUNUS-1, monthly | −1.3 | −2.6 to 0.0 | 0.0496 |
| NEPTUNUS-2, monthly | −1.0 | −2.0 to 0.0 | 0.041 |
| NEPTUNUS-2, every 3 months | −0.5 | −1.5 to 0.5 | 0.3413 |

**On-slide copy**

- Monthly treatment met the endpoint in both trials.
- Dose-frequency differences are relevant context, not proof of an identical DAZ exposure-response relationship.
- Ph2b met its prespecified dose-response objective; the 300 mg pairwise p≈0.092 did not define trial failure.

**Visual:** forest plot, with trial, frequency, arm Ns and confidence level shown. Rounded CI boundaries can display 0.0 despite a significant unrounded test.

**Speaker note:** “I use these data to check plausible effects and precision, not to establish cross-trial superiority. Analysis-population Ns can differ from registry enrollment totals.”

**Source:** R4 and R6, slide 30. NEPTUNUS-1 n=137/138; NEPTUNUS-2 monthly/quarterly/placebo n=168/167/169 in the company presentation. The saved registry lists 506 overall; do not silently equate it to the displayed analysis N=504.

## Slide 14 — Pathway and historical lessons

### Same-pathway evidence supports systemic activity more clearly than universal symptom benefit

**Exhibit**

| Evidence | Result | What it contributes |
|---|---|---|
| Iscalimab systemic cohort, N=173 | Met dose-response objective | Supports CD40 pathway plausibility |
| Iscalimab symptom cohort, N=100 | ESSPRI −0.57; p=0.12 | Symptom benefit is not assured by pathway alone |
| Abatacept ASAP-III | Missed continuous ESSDAI primary | Plausible immune biology can fail clinically |
| Rituximab TRACTISS | Missed symptom VAS responder primary | Endpoint/population selection matters |
| Tocilizumab ETAP | Missed composite-response primary | Distinct response construct; not continuous ESSDAI |

**On-slide takeaway:** Use prior trials to challenge assumptions; avoid a numerical “class success rate.”

**Speaker note:** “This selected set is not a meta-analysis or a calibrated prior. The most relevant same-pathway result is supportive for systemic efficacy, but its symptom cohort provides a useful counterweight.”

**Visual:** evidence matrix, not a green/red success pie chart. Keep extra historical agents in appendix only if they add a distinct lesson.

**Source:** R5, R9–R11. Dazodalibep's own Phase 2 is not counted again as independent external validation.

## Slide 15 — Explicit effect assumptions

### A 1.4-point base assumption retains about two-thirds of the Phase 2 effect

**Exhibit: analyst assumptions for true week-48 benefit**

| Case | Positive benefit magnitude | Retention versus 2.2 | Rationale |
|---|---:|---:|---|
| Bull | 2.0 | 91% | Most of the Phase 2 signal persists |
| Base | 1.4 | 64% | Meaningful attenuation without loss of activity |
| Bear | 0.6 | 27% | Substantial attenuation through efficacy/measurement or population differences |

**On-slide copy:** The base is a judgmental working forecast, not an empirically estimated mean. Ianalumab and DAZ subgroup data provide context, not a validated shrinkage multiplier.

**Visual:** three labeled points on a benefit axis, with the Phase 2 observed 2.2 as a separate reference. State that positive magnitudes are used here although reported change contrasts are negative.

**Speaker note:** “Why 1.4? It is a conservative departure from the observed 2.2 and in the vicinity of relevant clinical signals. The sources do not identify 1.4 uniquely, so I test a range. The conclusion should not depend on a spurious decimal precision.”

**Source:** analyst assumptions; R1, R4 and R6 as context. Omit arbitrary scenario weights from the main deck unless prepared to defend them.

## Slide 16 — Conditional power

### The base effect has favorable power under nominal testing, but the margin narrows with stricter assumptions

**Exhibit: one active-dose comparison, n=217 per arm, effective SD=5.47**

| Assumed true benefit | Power at two-sided alpha 0.05 | Power at illustrative alpha 0.025 |
|---|---:|---:|
| 0.6 | 21% | 14% |
| 1.0 | 48% | 37% |
| 1.4 | 76% | 66% |
| 1.6 | 86% | 79% |
| 2.0 | 97% | 94% |

**On-slide takeaway:** Statistical success remains uncertain even if the assumed biological effect is correct.

**Visual:** conditional-power curves with vertical markers at bear/base/bull. A table is also acceptable. Do not put future p-values in these cells.

**Speaker note:** “The curves describe repeated samples under fixed assumptions. They do not give the unconditional probability that Amgen's actual trial will succeed. The sponsor may use a different longitudinal analysis and multiplicity procedure.”

**Source:** independent normal approximation; methods in Appendix 4. Effective SD=5.47 is a comparator-based sensitivity, not a measured DAZ Phase 3 SD.

## Slide 17 — Variance, missing data and falsifiability

### Higher variance and information loss can materially weaken the same efficacy forecast

**Exhibit: assumed true benefit fixed at 1.4**

| Assumption | n/arm | Alpha | Approximate power |
|---|---:|---:|---:|
| Effective SD 3.65 | 217 | 0.05 | 98% |
| SD 5.00 | 217 | 0.05 | 83% |
| Effective SD 5.47 | 217 | 0.05 | 76% |
| Effective SD 5.47; stricter alpha | 217 | 0.025 | 66% |
| Same; reduced effective information | 184 | 0.025 | 58% |

**On-slide copy**

- Repeated measurements and adjustment affect precision; raw sample size alone is insufficient.
- Phase 2 excluded post-rescue observations from the primary analysis; the Phase 3 treatment of rescue/discontinuation matters.
- Reduced effective n is a stress test, not a complete missing-data model.

**Visual:** horizontal dot plot or a heatmap, clearly labeling which assumptions change. Keep no more than these five main rows.

**Speaker note:** “The strongest bear case is a small retained effect under realistic noise and testing requirements. It is not simply that the study is nine times larger. I would revisit the call with actual baseline mix, precision and testing details.”

**Source:** R1 Statistical analysis; R6 for comparator precision; analyst calculations. The Phase 2 planning SD=5 is not Amgen's disclosed Phase 3 planning assumption.

## Slide 18 — Symptomatic trial conclusion

### ESSPRI evidence supports optimism; DASPRI limits confidence in the full symptomatic readout

**Exhibit**

| Question | Evidence available | Interpretation |
|---|---|---|
| Does DAZ improve reported symptoms? | Positive Phase 2 ESSPRI total and domain results | Supports a positive ESSPRI lean |
| Does benefit extend to week 48? | Supportive crossover observation; no equivalent parallel-group replication in this paper | Durability remains a test |
| What supports DASPRI? | Listed in the Phase 3 registry export; no DASPRI result located in supplied 2024 paper | Instrument bridge remains uncertain |
| What defines overall trial success? | Two outcomes listed; complete procedure not established here | Do not assume both-pass or either-pass rule |

**On-slide takeaway:** Favorable symptom evidence; lower conviction on the complete trial outcome than an ESSPRI-only summary suggests.

**Visual:** comparison table above, with concise facts rather than “TBD—extract Phase 2 DASPRI.”

**Speaker note:** “The supplied paper does not identify DASPRI among the reported endpoints. That is a limitation of the reviewed evidence, not evidence that the instrument is ineffective or that no other public evidence exists. Diary completion and scoring need primary documentation.”

**Source:** R1, R3. Avoid an unsupported assertion that the symptom instrument is categorically more placebo-prone than ESSDAI, and do not equate JOQUER's exploratory symptom clusters with trial eligibility.

## Slide 19 — Benefit-risk

### Fc-free engineering addresses a known mechanism; Phase 2 safety still warrants careful scrutiny

**Exhibit: selected serious observations, not an exhaustive safety table**

| Observation | Population / period | Reported attribution and context |
|---|---|---|
| DVT and drug-induced liver injury, same participant | Population 1, Stage II | Both considered related by investigators; DVT reported 180 days after last DAZ dose |
| Invasive ductal breast carcinoma | Population 2, Stage II | Considered related by investigators; onset 139 days after last dose |
| One death, unknown cause following COVID-19 diagnosis | Population 1, Stage I | Considered unrelated by investigators; 46 days after last DAZ dose |

**On-slide copy:** These are three investigator-attributed serious events in two participants, plus the separately described unrelated death. Individual events establish neither causation nor absence of risk.

**Visual:** compact table with denominators in a footnote: Stage I systemic DAZ n=36; Stage II systemic DAZ→placebo n=34; Stage II symptomatic DAZ→placebo safety n=48, as displayed in Table 3. Preserve differing safety-set denominators rather than reconstructing them.

**Speaker note:** “I separate investigator attribution from demonstrated causality, and primary efficacy from overall benefit-risk. Look for exposure-adjusted patterns and event narratives in the larger program.”

**Source:** R1 Safety Results and Table 3. Do not classify the death as Stage II, and do not assert a confirmed COVID cause of death when the paper says unknown cause.

## Slide 20 — Close with the forecast and what will change it

### Our positive systemic forecast stands or falls on the prespecified primary result

**On-slide copy**

**Forecast:** Expect positive ESSDAI efficacy in NCT06104124; favorable ESSPRI evidence with unresolved full-trial interpretation for NCT06245408.

**Exhibit**

| Readout | Interpretation |
|---|---|
| Prespecified primary procedure met, consistent dose results | Confirms the primary efficacy forecast; assess magnitude and safety separately |
| Primary met, modest effect or mixed supportive outcomes | Statistical win with a more qualified clinical interpretation |
| Prespecified primary procedure not met | Forecast was wrong; evaluate explanations without redefining success post hoc |
| Efficacy positive, concerning safety pattern | Efficacy call may be right while benefit-risk remains unfavorable |

**Timeline footer:** Saved systemic export: primary completion July 23, **2026**; study completion August 17, 2026. Saved symptomatic export: primary completion October 22, 2026; study completion December 17, 2026. Completion is not disclosure. The assignment anticipates later-2026 readouts; an exact announcement date is not established here.

**Speaker note:** “A failed primary test is a failed forecast even if the biology remains interesting. Conversely, a successful primary test should not be relabeled failure merely because a secondary threshold or a lower dose disappoints.”

**Source:** R2–R3 local exports and assignment email; analyst interpretation. Refresh registry status/date flags and public disclosure status before sending the deck.

---

# Part II — Appendix content

## Appendix 1 — Registry facts and unresolved design fields

| Field | Systemic | Symptomatic |
|---|---|---|
| NCT | NCT06104124 | NCT06245408 |
| Saved enrollment | 651 | 434 |
| Saved status | Completed | Active, not recruiting |
| Primary outcome listing | ESSDAI | ESSPRI; DASPRI |
| Primary assessment | Week 48 | Week 48 |
| Primary completion in CSV | 2026-07-23 | 2026-10-22 |
| Study completion in CSV | 2026-08-17 | 2026-12-17 |
| Registry update in CSV | 2026-09-14 | 2026-01-08 |

**Fields to preserve when retrieving complete records:** arm doses/frequency, allocation, full eligibility, background-treatment stability, rescue rules, outcome definitions, protocol/SAP, analysis population and actual/estimated date flags. They are not fully represented by the supplied CSV columns. Do not present the table as a complete protocol abstraction.

**Source:** R2–R3; supplied CSV snapshots. Do not populate absent fields with assumed protocol details.

## Appendix 2 — Baseline evidence that matters to transferability

Values rechecked visually against the current local Phase 2 PDF, Table 1, PDF page 4.

| Characteristic | Pop 1 placebo | Pop 1 DAZ | Pop 2 placebo | Pop 2 DAZ |
|---|---:|---:|---:|---:|
| N | 38 | 36 | 55 | 54 |
| Baseline ESSDAI, mean (SD) | 10.1 (4.1) | 11.4 (4.5) | 2.5 (1.6) | 3.1 (1.8) |
| Baseline ESSPRI total | 6.6 (1.8) | 6.6 (1.6) | **6.8 (1.2)** | **7.1 (1.6)** |
| Dryness | 6.9 (2.3) | 7.3 (1.7) | **7.1 (1.1)** | **7.5 (1.5)** |
| Fatigue | 6.8 (2.2) | 7.0 (1.7) | **6.9 (1.8)** | 7.1 (1.8) |
| Pain | 6.1 (2.3) | 5.5 (3.0) | 6.3 (1.9) | 6.6 (2.6) |
| OSDI | **47.0 (20.9)** | 48.7 (25.0) | 48.6 (19.2) | 48.2 (23.8) |
| Stimulated salivary flow, mL/min | 0.97 (0.85) | 0.88 (0.64) | **0.83 (0.69)** | 1.10 (1.18) |
| Concomitant RA/SLE | 9 (23.7%) | 7 (19.4%) | 7 (12.7%) | 4 (7.4%) |

Schirmer's criterion: **≤5 mm/5 min in at least one eye**. Keep missing-assessment denominators as published.

Relevant background therapy: Population 1 had 59.5% antimalarial, 41.9% glucocorticoid and 31.1% conventional DMARD use overall. Population 2 cholinergic agonist use differed: 11.1% DAZ versus 27.3% placebo. These are potential interpretation/transportability considerations, not proven causes of the observed contrast.

**Source:** R1 Table 1 and baseline Results. Show the full demographic table only if needed in discussion; this selected table is more relevant to the forecast.

## Appendix 3 — Supportive outcomes and domain scope

| Day-169 outcome | Population | DAZ / placebo change | p-value |
|---|---|---|---:|
| ESSPRI | Systemic | −1.8 / −1.1 | 0.1110 |
| FACIT–Fatigue | Systemic | +8.1 / +5.8 | 0.3028 |
| FACIT–Fatigue | Symptomatic | +8.1 / +2.8 | 0.0095 |
| OSDI | Systemic | −16.00 / −14.02 | 0.6583 |
| OSDI | Symptomatic | −13.95 / −8.52 | 0.1936 |
| Stimulated salivary flow | Systemic | +0.39 / +0.14 | 0.1330 |
| Stimulated salivary flow | Symptomatic | +0.20 / −0.01 | 0.2170 |

These supportive/exploratory p-values are unadjusted. Positive FACIT change indicates improvement; negative OSDI/ESSPRI change indicates improvement. Numerical gland-function changes did not meet nominal significance, so do not claim demonstrated restoration of gland function.

Population 1 had no baseline pulmonary, CNS or renal involvement in the described domain analysis. The Phase 2 result therefore should not be generalized into demonstrated efficacy across severe organ manifestations absent from the sample. Domain responder denominators include only those with baseline involvement.

**Source:** R1 Table 2, domain Results and Extended Data Figure 7.

## Appendix 4 — Reproducible statistical method

**Definitions:** delta is positive treatment benefit; n is the effective sample size per arm in an equal-sized comparison; sigma is an assumed effective SD. These are not individual-patient reanalyses.

```
SE = sigma * sqrt(2 / n)
critical_z = inverse_normal_cdf(1 - alpha/2)

power(delta) = normal_cdf(delta/SE - critical_z)
             + normal_cdf(-delta/SE - critical_z)

effect_for_80_percent_power ≈
    (critical_z + inverse_normal_cdf(0.80)) * SE
```

The 80% expression is a conventional approximation. The power function includes both tails.

| Sigma | n | Alpha | SE | Observed threshold | Effect for ~80% power |
|---:|---:|---:|---:|---:|---:|
| 3.65 | 217 | 0.05 | 0.350 | 0.687 | 0.982 |
| 5.00 | 217 | 0.05 | 0.480 | 0.941 | 1.345 |
| 5.47 | 217 | 0.05 | 0.525 | 1.029 | 1.471 |
| 5.47 | 217 | 0.025 | 0.525 | 1.177 | 1.619 |
| 5.47 | 184 | 0.025 | 0.570 | 1.278 | 1.758 |

**Input provenance:** 3.65 is an approximate back-calculation from DAZ adjusted Phase 2 SEs; 5.00 is the Phase 2 planning SD; 5.47 is an approximate effective SD from NEPTUNUS-1's reported SE. Adjusted-model SEs do not identify raw outcome SDs exactly. Neither comparator precision nor the Phase 2 planning parameter establishes DAZ Phase 3 variance.

**Limitations:** normal approximation, equal allocation assumption, one comparison, no full MMRM covariance structure, no modeled dropout mechanism, no actual sponsor hierarchy. Alpha=0.025 is an illustrative two-comparison split. Shared-placebo dependence matters for joint success probabilities, which are not computed here.

**Interpretive rule:** an assumed true delta cannot be assigned a guaranteed observed p-value. A point-scenario z-value is only the test statistic at that hypothetical observed effect. No “chance it is a fluke” interpretation is valid.

**Useful further check:** NEPTUNUS-1 SE scaled only for sample size is 0.66×sqrt(137/217)=0.524. At a hypothetical *observed* 1.3-point difference, the nominal p-value is about 0.013. This isolates precision scaling, not a forecast of the future p-value.

**Source:** R1 methods, R6 slide 30, analyst calculation.

## Appendix 5 — Clinical meaning and historical context

**Within-patient thresholds:** ESSDAI improvement ≥3; ESSPRI improvement ≥1 or ≥15% in the cited historical framework. These cannot be imposed as minimum placebo-adjusted group contrasts. Specific Phase 3 responder definitions can differ; the symptomatic export lists an ESSPRI [1.5] response outcome.

**Historical context:** CRESS and STAR broaden response assessment across domains. Discuss them briefly as alternative measurement approaches, not as substitutes for the prespecified ESSDAI primary endpoint. Retrospective favorable reanalysis cannot retrospectively convert a failed primary test into a positive confirmatory trial.

**Placebo interpretation:** improvement in a placebo arm includes natural history, regression toward average values, background treatment, measurement and contextual effects. It is not synonymous with an expectation-induced “fake” benefit. Longer follow-up can change both arms; a large placebo change alone does not establish why the treatment contrast changed.

**ETAP correction:** the published 0.14 refers to the posterior probability Pr(tocilizumab > placebo), not a conventional p-value. Do not copy the current historical table's p=0.14 label. Use the reported response proportions and analysis definition if displaying it.

**Source:** R7, R10; other historical primary reports below. Full historical tables should retain exact trial-specific endpoint wording rather than force a uniform metric.

## Appendix 6 — Source library

Use short source labels on slides; maintain these exact references in notes or a reference slide. Split references across two appendix slides if necessary for legibility.

- **R1 — St. Clair EW et al.** CD40 ligand antagonist dazodalibep in Sjögren's disease: a randomized, double-blinded, placebo-controlled, phase 2 trial. Nature Medicine 30, 1583–1592 (2024). [DOI](https://doi.org/10.1038/s41591-024-03009-3). Local source: `00_reference/phase2_paper.pdf`. Main tables, Methods and Extended Data used directly. Open access; retain attribution for reused figures.
- **R2 — ClinicalTrials.gov, NCT06104124.** [Systemic Phase 3 study](https://clinicaltrials.gov/study/NCT06104124). Dated snapshot: `01_data/NCT06104124.csv`; registry update recorded as September 14, 2026. Refresh complete record and actual/estimated flags before submission.
- **R3 — ClinicalTrials.gov, NCT06245408.** [Symptomatic Phase 3 study](https://clinicaltrials.gov/study/NCT06245408). Dated snapshot: `01_data/NCT06245408.csv`; registry update recorded as January 8, 2026. Full outcome hierarchy is not established from this export.
- **R4 — Bowman SJ et al.** Safety and efficacy of subcutaneous ianalumab in primary Sjögren's syndrome: phase 2b dose-finding trial. Lancet 399, 161–171 (2022; online 2021). [Primary publication](https://pubmed.ncbi.nlm.nih.gov/34861168/).
- **R5 — Fisher BA et al.** Safety and efficacy of subcutaneous iscalimab in two distinct populations of patients with Sjögren's disease (TWINSS). Lancet (2024). [Primary publication](https://pubmed.ncbi.nlm.nih.gov/39096929/).
- **R6 — Novartis Immunology Pipeline Event, October 30, 2025.** [Company presentation](https://www.novartis.com/sites/novartis_com/files/novartis-immunology-portfolio-update-presentation.pdf), slide 30 for NEPTUNUS individual-arm efficacy. Prefer this directly sourced exhibit over secondary conference coverage.
- **R7 — Seror et al.** [Defining disease activity states and clinically meaningful improvement](https://pubmed.ncbi.nlm.nih.gov/25480887/); [ESSDAI user guide](https://pmc.ncbi.nlm.nih.gov/articles/PMC4613159/).
- **R8 — Der K et al.** Population PK/PD modeling of dazodalibep. ACR Convergence 2023, abstract 1379. [Primary abstract](https://acrabstracts.org/abstract/population-pharmacokinetic-pharmacodynamic-modeling-of-dazodalibep-a-cd40l-antagonist-in-healthy-volunteers-and-patients-with-rheumatoid-arthritis-and-sjogrens-syndrome/). This supports model-based dose selection, not an estimated ESSDAI effect.
- **R9 — Bowman et al., TRACTISS.** [Primary trial report](https://discovery.ucl.ac.uk/id/eprint/1549982/).
- **R10 — Felten et al., ETAP.** [Interleukin 6 receptor inhibition in primary Sjögren syndrome](https://pubmed.ncbi.nlm.nih.gov/33208345/).
- **R11 — van Nimwegen et al., ASAP-III.** Primary randomized trial, Lancet Rheumatology. Project research describes N=80 and the negative week-24 continuous ESSDAI primary; confirm the exact bibliographic entry from the primary publication before retaining this row in the final reference slide.

**Reference scope:** R1 was rechecked from the supplied local paper, including rendered Table 1; R8 was checked against its primary abstract in this review. Other sources include primary material checked during the preceding review and the supplied dated exports. No fresh full registry/SAP verification is implied by citing a registry link.

---

# Part III — Review of the existing outline and remaining project issues

## Overall review

The 20-slide structure is a good starting point. The sequence broadly matches the brief, the ianalumab correction is valuable, and the variance sensitivities improve the methodology. It is still a working outline rather than presentation-ready copy: correction history, unfinished research assumptions and several contradictions remain in audience-facing text.

I would preserve the scope and most exhibits, replace the old “scale-up causes erosion” counterargument, remove fixed future p-values, and give symptom evidence its own clean slide. The new narrative above makes a clear call without turning uncertainty into an excuse to avoid forecasting.

## Slide-by-slide editorial decisions

| Existing slide | Decision | Reason / replacement |
|---|---|---|
| 1 | Keep | Clear scope and cutoff; add candidate name |
| 2 | Rewrite | Remove “appropriately powered for its size” and the 1.4×/8.8× erosion argument; use clinical evidence and variance risk |
| 3 | Correct | July 23, 2026, not 2025; “listed primary outcomes,” not a proven AND success rule |
| 4 | Simplify | Do not equate symptomatic disease with gland damage or promise reversibility |
| 5 | Keep with tighter mechanism wording | Fc-free design is relevant; biology does not itself prove efficacy |
| 6 | Keep | Clearly separate randomized first period from treatment switch |
| 7 | Keep with precise statistical wording | Replace “real, but Phase 2-sized”; state adjusted difference, CI level and sample |
| 8 | Keep and focus | Preserve responder denominators; subgroup evidence is exploratory |
| 9 | Split/reorder | Separate symptoms from biomarkers so neither becomes a crowded afterthought |
| 10 | Rewrite | Total N increases 8.8×; relevant per-comparison arm size increases roughly 6× under equal allocation |
| 11 | Rewrite | Average exposure support is not proof of trough coverage or clinical effect; cite the primary PK/PD abstract |
| 12 | Keep | Use individual NEPTUNUS results and primary company exhibit; omit pooled result if it adds no lesson |
| 13 | Keep with less sweeping headline | Selected trials are not all pathway trials or a systematic base rate |
| 14 | Rewrite | “~1.0–1.5 reliably detectable” depends on alpha and information; expanded cases reach ~1.76 for 80% power |
| 15 | Replace p-value table | Use assumed-effect rationale followed by conditional power; remove unexplained weights |
| 16 | Keep sensitivity concept | Avoid “safe margin”; state the conditional probabilities |
| 17 | Correct materially | No DASPRI result located in the supplied 2024 paper; do not promise to extract an unlocated endpoint |
| 18 | Correct materially | Three related SAEs in two people, plus one separately described death; death is Stage I and cause reported unknown |
| 19 | Replace | Strongest risk is retained effect versus variance/testing, not enrollment scale alone |
| 20 | Replace decision rules | Prespecified primary test determines efficacy success; competitor failures and a weak lower dose do not automatically reverse the systemic call |
| Appendix 1 | Correct source coverage | Current CSVs lack full eligibility/protocol fields |
| Appendix 2 | Correct numeric table | Current PDF supports the earlier baseline corrections; use values above |
| Appendix 3 | Retain | Add gland-function limits, background therapy and crossover caveats |
| Appendix 4 | Replace deterministic interpretation | Use reproducible formulas and conditional-power outputs |
| Appendix 5 | Reduce crowding | Put selected historical context here; exhaustive safety plus all competitor data will not fit legibly on one slide |
| Appendix 6 | Build primary bibliography | Internal Markdown filenames are not sufficient final data citations |

## Specific residual errors across the project

1. **Baseline memo incorrectly rejects the earlier corrections.** Rendered Table 1 clearly shows Pop 2 ESSPRI 6.8/7.1, dryness 7.1/7.5, Pop 1 placebo OSDI 47.0, and Pop 2 placebo flow SD 0.69. The original reviewer should not be treated as authoritative; the displayed source table resolves the issue.
2. **Master evidence table contains a 2025 systemic completion date.** Both supplied trial CSV and original plan indicate 2026. Correct downstream slides and summaries from the export.
3. **Death period is wrong in the “corrected” results/evidence table.** Table 3 places the death in Stage I. The prose describes unknown cause after a COVID diagnosis, not established COVID causation.
4. **DASPRI “missing extraction” is unsupported.** No occurrence or result was located in the supplied 2024 paper. Searching text alone is not proof of universal absence; the paper's endpoint descriptions and tables also do not establish the claimed result. Frame this as an evidence gap.
5. **Scenario model still assigns pass/fail and p-values to assumed true effects.** Adding an “illustrative” disclaimer does not fix this logical error. Replace those cells with conditional power.
6. **The 1.4× versus 8.8× comparison is not a validated effect-retention model.** Ianalumab Ph2b had four arms, Phase 3 NEPTUNUS-1 two. Relevant monthly-dose/control arm sizes rise roughly 47/49 to 137/138. DAZ rises 36/38 to an assumed 217/217. Use this to explain information, not causally predict effect shrinkage.
7. **The symptomatic note contradicts itself.** Earlier paragraphs still equate JOQUER enrichment with the Phase 3 rule, while the correction at the end properly rejects equivalence. Remove the superseded paragraphs, not just add a disclaimer.
8. **ETAP's 0.14 is mislabeled.** It is a posterior probability in the primary report, not a conventional p-value.
9. **The ianalumab Ph2b placebo wording remains arithmetically wrong.** Placebo −6.39 is a larger reduction than the 5 mg arm −5.64, but not the 50 mg arm −6.93. It did not outperform both lower doses numerically.
10. **Biomarker quantity labels need precision.** 0.67/0.56 and 0.66/0.54 are active-arm ratios to baseline; placebo ratios must be shown separately. They are not themselves placebo-adjusted ratios.
11. **Status documents still interpret p-values as probabilities of a fluke and say the science is complete.** They are useful process summaries, but should not feed final wording without revision.
12. **The readout matrix has unsupported automatic reversals.** One lower dose worsening, another mechanism failing, or the symptomatic trial missing does not mechanically reverse a systemic primary result. Primary efficacy and benefit-risk should be judged explicitly.
13. **Specific future announcement venues are speculative.** Do not predict a particular earnings call or congress date without company guidance. Completion dates remain separate from disclosure dates.
14. **Current approval/unmet-need statements require a dated check.** It is unnecessary to make a current “no approved therapy” claim central to this forecast; never infer that unmet need automatically lowers a safety standard.

## What meets the Jefferies brief in this recommended narrative

| Brief requirement | Where addressed |
|---|---|
| A clear positive/negative primary-endpoint call | Slides 2 and 20 |
| CD40L biological rationale | Slides 4–5 and 10 |
| Phase 2 insights, with limitations | Slides 6–10, Appendices 2–3 |
| Unique Phase 3 design and systemic/symptomatic distinction | Slides 3, 11–12 and 18 |
| Statistical considerations and methodology | Slides 15–17, Appendix 4 |
| Learnings from ianalumab and other trials | Slides 13–14, Appendix 5 |
| Public evidence and traceability | Source footers and Appendix 6 |
| Falsifiable conclusion and balanced counterargument | Slides 17–20 |
| PowerPoint format | Next production step; Markdown alone does not fulfill the final submission requirement |

## Presentation production guidance

- Use a 16:9 layout, white background, dark navy headings, one active-treatment color and gray placebo. Use color consistently rather than green for every favorable number.
- Prefer one principal exhibit and no more than three interpretation bullets per slide. Keep detailed caveats in notes, with material caveats visible next to the claim.
- Use 28–34 pt titles, around 20–24 pt body text, and legible source footers. Split tables rather than shrinking everything.
- Title a graph with the result it shows. Label axes, score direction, analysis population, error bars and timepoint.
- Do not put ESSDAI and ESSPRI on the same numerical axis. Do not mix 90% and 95% intervals without explicit labeling.
- A one-page evidence table is the input source; slides are the argument. Avoid “Day 1,” “corrected,” “TBD,” “reviewer suggested” and other process history in the actual deck.
- A power curve and heatmap are useful, but a clear numeric table is fully acceptable. No Monte Carlo decoration is needed.
- Add the candidate name, refresh trial disclosure/registry status, resolve retained source gaps, export the PPTX to PDF, and inspect every slide before delivery.

## Likely discussion questions: short answers to rehearse

**Why positive?** The direct randomized systemic signal is supported by biological activity and relevant external clinical evidence. The retained-effect assumption is plausible, while the sensitivity analysis shows the risk rather than concealing it.

**Why 1.4 points?** It is an analyst assumption retaining about 64% of the Phase 2 contrast, not a fitted prediction. The argument is tested across 0.6–2.0 points instead of relying on one decimal estimate.

**Why not use 76% as the probability of success?** It conditions on a true 1.4-point effect, a particular variance, n and alpha. Those inputs are uncertain, and the joint two-dose procedure is not modeled.

**Is a 1.4-point difference clinically meaningful?** That cannot be decided by comparing it with a 3-point within-patient threshold. Examine the distribution of individual improvements, supportive outcomes and safety.

**Does a Phase 3 miss mean the mechanism is wrong?** Not necessarily. But it does mean this primary-endpoint forecast was wrong. Biology and clinical hypothesis revision follow the result; they do not redefine the original success criterion.

**Why not fully model both trials?** The brief permits one. The systemic trial has the clearest comparator/endpoint basis for the quantitative work; the symptomatic section addresses its distinct evidence and uncertainty without an unsupported full-program probability.

**What is still unfinished?** PowerPoint production, final registry/disclosure refresh, exact testing details where available, and any remaining primary-reference verification. Missing public details are labeled, not filled with assumptions presented as facts.
