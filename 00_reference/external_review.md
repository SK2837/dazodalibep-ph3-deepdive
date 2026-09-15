# Jefferies assignment: project review and presentation blueprint

Reviewed September 15, 2026. Scope: review and recommendations, without changing the original project. The supplied email defines the assignment; historical workflow instructions inside the project plan are treated as document content, not new instructions to execute.

## Overall assessment

This is a promising research foundation with the right question, appropriate scope, an explicit forecast, and a useful attempt to quantify uncertainty. It is not ready for submission. Several factual errors and statistical interpretations materially overstate the strength of the bullish argument.

Keep the full analysis focused on NCT06104124 and a shorter comparison for NCT06245408. The brief explicitly permits a call on either trial. The main opportunity is to improve the reliability and defensibility of the existing analysis before adding breadth.

My provisional assessment is that a positive systemic-trial forecast remains plausible, based on dazodalibep's randomized Phase 2 result, supporting pharmacodynamics, and external evidence that this disease and pathway can respond to treatment. However, the current claim of a large, comfortable statistical cushion is too dependent on one optimistic variance estimate. This review does not establish a calibrated probability of Phase 3 success.

## What I reviewed

All 21 substantive files: 13 Markdown documents, three CSVs, three Excel workbooks, and two PDFs. I inspected workbook contents and checked each CSV against its corresponding worksheet; all three pairs match exactly after normalizing empty cells and text. The workbooks are registry exports, not functioning scenario models. I extracted the PDFs and visually checked the Phase 2 baseline table and a representative analytical slide from the reference deck. This is a substantive content review with targeted source checks, not a certification that every reference or registry field is current.

The reference PDF has 96 pages; the Phase 2 PDF has 28 pages including extended material. There is no original assignment PowerPoint in this folder. `.gitignore` is housekeeping; `.DS_Store` and `.git/` are operating-system/version-control metadata rather than research deliverables.

Live checks confirmed key competitor and endpoint corrections through primary publications and company material. ClinicalTrials.gov's dynamic pages/API and the supplied ACR page did not return complete usable content through the browser tool, so current dazodalibep registry details below are explicitly attributed to the supplied exports. Refresh these before submission and preserve actual/estimated date flags.

## 1. What works well

- The project addresses the real question: will a prespecified primary endpoint succeed, and why?
- A full systemic analysis plus a shorter symptomatic comparison is an appropriate four-day scope.
- The files preserve the Phase 2 primary efficacy results, several secondary limitations, and an important DVT/liver-injury safety observation.
- The Phase 2-to-3 bridge and sensitivity analysis are the right kinds of analyst work.
- Comparing the endpoint, population, placebo response and statistical design is more useful than a long generic disease overview.
- The reference deck's strongest features are worth adopting: an early conclusion, explicit assumptions, quantitative scenarios, counterarguments, and sources next to the evidence.

The main weakness is that incorrect interpretations have propagated into several summaries. Repeating a claim across documents does not independently validate it.

## 2. Changes required before building slides

### Priority 1: correct trial outcomes and the historical comparison

**Ianalumab Phase 2b met its primary objective.** The individual 300 mg versus placebo comparison had p≈0.092, but the prespecified dose-response analysis was positive. These are different statistical tests. Replace the statement that Novartis advanced after a failed primary endpoint throughout the competitor memo, historical table, thesis and summaries. The current comparison applies a dose-response success criterion to iscalimab but a pairwise criterion to ianalumab, creating an inconsistent classification. [Bowman et al., Lancet](https://pubmed.ncbi.nlm.nih.gov/34861168/)

**Remove the “33% historical base rate” and “100% CD40-pathway success rate” as probability inputs.** The selected trials are neither a systematic sample nor a uniform endpoint class. Dazodalibep's own Phase 2 result also should not be counted as independent external evidence and then counted again in its likelihood. Use a qualitative evidence table instead.

**TRACTISS was not an ESSDAI-primary trial.** Its primary outcome was a 30% reduction in fatigue or oral dryness at week 48. **ETAP used a composite response definition**, including ESSDAI improvement, absence of new domain activity and no worsening of physician global assessment. Separate continuous ESSDAI, ESSDAI-based responder composites, symptom outcomes, dose-response tests and uncontrolled studies. [TRACTISS primary report](https://discovery.ucl.ac.uk/id/eprint/1549982/), [ETAP primary report](https://pubmed.ncbi.nlm.nih.gov/33208345/)

### Priority 2: correct the Phase 2-to-3 population bridge

The Phase 2 paper already required **ESSDAI ≥5 for Population 1** and **ESSPRI ≥5, ESSDAI <5, and residual stimulated salivary flow ≥0.1 mL/min for Population 2**. Comparing the Phase 2 observed mean with a Phase 3 eligibility minimum does not demonstrate looser inclusion criteria. Remove this argument from the baseline memo, plain-language explanation and model reasoning.

A broader Phase 3 population remains possible, but must be supported by actual differences in eligibility, regions, disease duration, concomitant autoimmune disease, medications or enrolled baseline characteristics. Lower severity could reduce both active and placebo improvement; it does not automatically widen the difference.

Add the paper's exploratory subgroup result: systemic patients without concomitant RA/SLE had a placebo-adjusted change of about −1.6, compared with −3.3 among those with RA/SLE. Small subgroup sizes preclude a strong interaction claim, but this is a more concrete transportability question than an unsupported enrollment-size haircut. Source: Phase 2 Extended Data Table 1.

### Priority 3: fix the statistical interpretation

The current calculations are broadly consistent with the assumed SD=3.65 and n≈217 per arm. The problem is how those assumptions are interpreted and presented.

Distinguish three quantities:

1. **Observed significance threshold:** with SE≈0.35 and a two-sided nominal alpha of 0.05, an observed difference of about 0.69 reaches the normal-approximation significance boundary.
2. **Effect associated with 80% power:** under those same assumptions, a true difference of about 0.98 has an 80% probability of a significant result over repeated trials.
3. **Predictive probability of trial success:** this additionally requires uncertainty about the true effect, variance, dose performance, missing data and multiplicity.

A true effect of 0.7 does not guarantee a pass; it produces roughly a coin-flip chance under this simplified model. Do not label a table of assumed true effects and calculated p-values as actual future pass/fail outcomes.

#### Variance sensitivity is essential

The Phase 2 methods used SD=5 in their planning calculation. The observed adjusted SEs do not provide an exact raw change-score SD. As another sensitivity, NEPTUNUS-1's reported difference SE≈0.66 at approximately 137 per arm corresponds to an effective two-group SD≈5.47. Neither is the known dazodalibep Phase 3 variance.

Illustrative independent-normal approximation, for one active-dose comparison:

| Variance assumption | Per-arm n | Two-sided alpha | Effect for 80% power | Conditional power if true benefit is 1.4 |
|---|---:|---:|---:|---:|
| Existing model, SD 3.65 | 217 | 0.05 | 0.98 | 98% |
| Phase 2 planning SD 5.00 | 217 | 0.05 | 1.34 | 83% |
| Competitor-based effective SD 5.47 | 217 | 0.05 | 1.47 | 76% |
| Same, illustrative stricter alpha | 217 | 0.025 | 1.62 | 66% |
| Same, illustrative information loss | 184 | 0.025 | 1.76 | 58% |

These are sensitivity calculations, not Amgen's disclosed power or an unconditional forecast. The final row approximates reduced information through a smaller effective sample; missing data in a longitudinal model are more complex than simply dropping 15% of patients.

The “same ianalumab effect would yield p=0.0002 because dazodalibep is larger” claim is misleading. Scaling NEPTUNUS-1's SE only for sample size gives 0.66×sqrt(137/217)≈0.524; an observed 1.3-point difference would then imply approximately p=0.013. The much smaller p-value in the current memo also relies on a substantially lower assumed variance. [Novartis presentation, slide 30](https://www.novartis.com/sites/novartis_com/files/novartis-immunology-portfolio-update-presentation.pdf)

#### Model the actual success rule

Two active doses introduce multiple comparisons with a shared placebo. Establish the planned allocation, dose schedules and testing hierarchy from primary documents where available. If the statistical analysis plan is unavailable, show explicit alternative assumptions rather than selecting one as fact. Alpha=0.025 above is only an illustrative sensitivity, not an assertion about the actual plan.

Replace fixed scenario p-values with conditional power curves or a heatmap. A transparent normal approximation is sufficient; Monte Carlo is optional. If you calculate an overall probability, state the distributions and weights and include parameter uncertainty. The existing 15%/60%/25% scenario weights are analyst judgments and cannot be presented as empirically estimated probabilities.

### Priority 4: include DASPRI in the symptomatic trial

Your `NCT06245408.csv` and `.xlsx` list **both ESSPRI and DASPRI change at week 48 as primary outcomes**. The current narrative omits DASPRI. This is a material design gap even for a shorter secondary section.

Describe both instruments, their recall/diary approach, validation evidence and missing-response risks. Do not assume that both must pass, either can pass, or a particular hierarchy applies merely because both are listed in the registry. That requires the protocol or analysis plan.

A smaller Phase 2 p-value supports the observed symptom signal, but does not establish lower future placebo risk or greater Phase 3 success probability. JOQUER's exploratory symptom-cluster analysis also cannot be equated automatically with a simple ESSPRI≥5 eligibility rule.

### Priority 5: correct the baseline transcription

Checked against the rendered Phase 2 Table 1, PDF page 4:

| Item | Current memo | Published Table 1 |
|---|---|---|
| Population 2 ESSPRI total, placebo / DAZ | 7.1±1.1 / 7.5±1.5 | **6.8±1.2 / 7.1±1.6** |
| Population 2 dryness, placebo / DAZ | 6.8±1.2 / 7.1±1.6 | **7.1±1.1 / 7.5±1.5** |
| Population 2 fatigue, placebo | 6.8±1.8 | **6.9±1.8** |
| Population 1 placebo OSDI | 40.0±20.9 | **47.0±20.9** |
| Population 2 placebo salivary flow | 0.83±0.83 | **0.83±0.69** |
| Schirmer's-test criterion | ≥5 mm/5 min | **≤5 mm/5 min in at least one eye** |

Keep denominators and missing measurements as published; do not silently recalculate percentages against the randomized total when a measurement has a different denominator.

### Priority 6: balance interpretation of biology and safety

- Biomarker changes support pharmacological activity; they do not prove meaningful clinical efficacy or make an endpoint explanation the default explanation for a future miss.
- Nonsignificant categorical secondary endpoints are not proof that ESSDAI is defective. Dichotomization loses information, samples are small, and multiple secondary analyses were unadjusted.
- Open-label improvements and retrospectively developed composite scores are exploratory support, not proof that a failed randomized primary endpoint missed an effective drug.
- The ≥3-point ESSDAI improvement threshold concerns within-patient improvement. Do not use it as a universal minimum placebo-adjusted group difference. Assess clinical relevance using responder distributions and supportive outcomes. [ESSDAI user guide](https://pmc.ncbi.nlm.nih.gov/articles/PMC4613159/)
- Remove the unsupported “PASylated” description in the plan. The primary paper describes an Fc-free Tn3 scaffold, nonantibody fusion protein. Use a verified molecular description and distinguish avoiding a known platelet mechanism from eliminating all thrombotic risk.
- The safety summary should also include the investigator-attributed invasive ductal breast carcinoma event in Population 2 Stage II. The paper's table reports **one death**, rather than the ambiguous “two deaths/serious infections” language. Report attribution, timing and denominator without inferring causation from one event. Source: Phase 2 pages 4–8 and Table 3.

### Priority 7: repair the document system and timeline

The supplied systemic export says primary completion July 23, 2026 and study completion August 17, 2026. The symptomatic export says active, not recruiting, with dates October 22 and December 17, 2026. These are different milestones. “Both finished” and “both use ESSDAI” in the plain-language summary contradict the underlying files.

Primary completion is not the disclosure date. Preserve actual versus estimated designations when refreshing records, and keep company readout guidance in a separate column. Do not assume the symptomatic disclosure will precede the systemic disclosure.

Update README and the project plan to reflect work already completed. Create a single evidence table containing claim, number, population, timepoint, analysis, source location and uncertainty. Build summaries from that table. Keep research history out of the presentation.

## 3. Additional topics worth adding

In priority order:

1. **Dose and exposure bridge:** what changes from the Phase 2 regimen, what supports the Phase 3 doses, and whether sustained exposure at week 48 is plausible. Use publicly available PK/PD evidence; mark undisclosed quantities.
2. **Endpoint/testing architecture:** ESSDAI versus ESSPRI versus DASPRI, dose comparisons, multiplicity, and the precise definition of a positive trial.
3. **Missing data, rescue medication and background therapy:** what benefit is being estimated, how discontinuation/rescue affects analysis, and how concomitant therapies could change placebo improvement.
4. **Domain composition and population transportability:** joint-dominant disease, RA/SLE overlap, disease duration, residual gland function, severity, regions and medication stability.
5. **Separate NEPTUNUS-1 and NEPTUNUS-2 results:** include the monthly and quarterly arms where relevant. Avoid substituting a pooled p-value for individual confirmatory trials. Reconcile the local registry's N=506 with the conference analysis's N=504 rather than choosing one silently.
6. **Iscalimab symptomatic evidence:** TWINSS systemic findings support pathway plausibility, while its symptom cohort did not achieve conventional significance (ESSPRI difference −0.57; p=0.12). This is useful counterevidence to an automatic class-wide symptom benefit. Systemic cohort N=173 and symptom cohort N=100, not N=273 for the systemic comparison. [TWINSS publication](https://pubmed.ncbi.nlm.nih.gov/39096929/)
7. **Clinical meaning of the outcome:** distinguish primary-endpoint significance, convincing patient benefit and an acceptable overall benefit-risk profile.
8. **A readout interpretation table:** prespecify what would strengthen, weaken or reverse the thesis once efficacy, dose consistency and safety are disclosed.

Do not expand into a full DCF, market sizing exercise, broad patent survey or every pipeline asset unless it directly changes the efficacy forecast. Those are not required by this brief. Limit generic disease education to approximately two slides.

## 4. Does it satisfy Jefferies' brief?

| Requirement | Current assessment | What remains |
|---|---|---|
| Clear call on one or both trials | Present | Recalibrate confidence and define success precisely |
| CD40L biological rationale | Partial | Convert discussion into a sourced mechanism-to-clinical-outcome argument |
| Phase 2 analysis | Substantial | Correct baseline and safety details; add uncertainty and subgroup caveats |
| Phase 3 design distinctions | Partial | Dose details, DASPRI, real eligibility differences, testing assumptions |
| Statistical considerations | Present but unreliable in interpretation | Variance, multiplicity, missing-data and true-effect sensitivity |
| Lessons from other trials | Present but materially flawed | Correct ianalumab and historical endpoint classifications |
| Public-source methodology | Good intent, uneven execution | Exact citations, evidence ledger, reproducible calculations |
| PowerPoint format | Not yet satisfied | Build the editable PPTX and review its exported appearance |

Verdict: the planned scope meets the assignment; the present files are a draft research package, not a completed submission. A carefully defended call on the systemic trial is sufficient. A correct shorter symptomatic comparison is an advantage.

## 5. Recommended presentation: 20 main slides plus 6 appendix slides

This is a recommendation, not a Jefferies-imposed length. The 96-page sample is a reference for analytical depth and logic; matching its length would be a poor use of a four-day assignment. For a roughly 20-minute presentation, combine slides to reach 15–18 main slides. For a read-ahead deep dive, the 20-slide structure below is appropriate.

| # | Slide purpose / provisional message | Evidence and visual |
|---:|---|---|
| 1 | Title, candidate name, analysis cutoff and trial focus | Simple title; no decorative stock imagery |
| 2 | We lean positive on systemic efficacy, with material uncertainty | Three reasons, largest risk, concise trial-call table |
| 3 | Define exactly what this forecast is predicting | Two-trial comparison: population, N, primary outcomes, timepoint, disclosure versus completion |
| 4 | Systemic activity and symptoms represent different treatment questions | Two-column patient/endpoint diagram; distinguish reversible inflammation from established damage |
| 5 | CD40L blockade has a plausible route to clinical benefit | Mechanism diagram: T-cell CD40L → CD40 on B/APC/epithelial cells → immune activity; place DAZ, iscalimab and ianalumab at the correct targets |
| 6 | Phase 2 tests two populations and only one active regimen | Two-lane randomization and dosing timeline; clearly mark day-169 primary analysis and subsequent crossover |
| 7 | Systemic Phase 2 efficacy supports the call, with substantial uncertainty | ESSDAI change over time, error bars, N, adjusted effect and reported CI level |
| 8 | Domain and responder results qualify the headline finding | Selected responder bars with denominators and exploratory RA/SLE subgroup plot; avoid overinterpreting interactions |
| 9 | Symptom and biomarker evidence support activity, with limits | Two clearly separated panels; label secondary/exploratory analyses and unadjusted p-values |
| 10 | Phase 3 changes exposure and observation time; population effects need evidence | Phase 2-to-3 bridge table: verified change, expected direction, rationale, uncertainty |
| 11 | Dose comparisons and endpoint rules determine the statistical hurdle | Testing diagram distinguishing confirmed design from undisclosed alternatives |
| 12 | Ianalumab validates the endpoint but does not determine DAZ's effect | Forest plot/table of Ph2b, NEPTUNUS-1 and NEPTUNUS-2, with analysis types and arm-level Ns |
| 13 | Same-pathway and historical studies provide mixed, relevant lessons | Compact comparator matrix; systemic and symptom endpoints in separate groups |
| 14 | Larger enrollment improves precision; variance controls the benefit | Power curves versus true ESSDAI effect under low and higher variance assumptions |
| 15 | The forecast rests on explicit, challengeable assumptions | Bull/base/bear table: effect, variance, effective N, alpha and rationale; use ranges where appropriate |
| 16 | The positive call becomes less robust as variance and effect erosion rise | Heatmap of conditional power versus effect and effective SD; alpha/missing-information sensitivity beside it |
| 17 | Symptomatic efficacy is encouraging; DASPRI creates an additional bridge question | ESSPRI/DASPRI comparison and symptom-domain Phase 2 evidence; directional conclusion without invented probability |
| 18 | An efficacy success still requires a credible benefit-risk profile | Safety table by population/stage, denominators, timing, investigator attribution |
| 19 | Here is the strongest case against our forecast | Ranked failure mechanisms and the evidence that would change the call |
| 20 | Final call and readout interpretation | Concise conclusion, result interpretation matrix, separately labeled completion/disclosure timeline |

### Appendix (approximately six slides)

1. Full Phase 3 design and eligibility comparison, with source dates.
2. Corrected baseline characteristics and background therapies.
3. Full Phase 2 endpoints, subgroup results and crossover limitations.
4. Statistical formulas, assumptions and expanded sensitivity outputs.
5. Expanded comparator and safety tables.
6. References; use an additional page if needed for legibility.

### The most valuable figures

- A mechanism diagram connecting target inhibition to clinical outcomes.
- Phase 2 and Phase 3 study-design timelines.
- Phase 2 longitudinal efficacy plots with uncertainties and sample sizes.
- A comparator forest plot with matched outcome definitions and explicit trial differences.
- An effect-retention/assumptions bridge, preferably a table unless the numerical adjustments are truly additive.
- A conditional-power heatmap that exposes how fragile or robust the conclusion is.
- A final “what would change my mind” table.

Avoid decorative mechanisms, 3-D charts, p-value-only rankings and mixing ESSDAI and ESSPRI effects on a shared numerical axis. Do not invent individual-patient data or smooth time-course points that were not published. Use source data when available; label digitized values as approximate. Keep 90% and 95% confidence intervals explicitly distinguished.

### How to build it

1. Correct the evidence and freeze a dated source table.
2. Recalculate the simple model with documented assumptions and sensitivity checks.
3. Write one conclusion per slide before formatting.
4. Build the essential figures and place them in a consistent 16:9 layout.
5. Use readable body text, one main analytical visual per slide, and concise interpretation beside it.
6. Put source, population, timepoint and analysis caveats next to each data exhibit. Identify analyst assumptions separately.
7. Add your own name; do not reproduce the reference deck's analyst attribution or imply Jefferies authorship.
8. Export to PDF, inspect every slide at presentation size, and verify that each headline follows from its exhibit.
9. Rehearse answers to the key challenges: why this effect, why this variance, what changed in Phase 3, and what would make you wrong?

Suggested remaining schedule: September 15 for evidence/model repair; September 16 for the complete storyline and figures; September 17 for PowerPoint production and verification; September 18 morning for final source/timeline checks and submission before 11:00 a.m. ET.

## File-by-file disposition

| File | Assessment and recommended action |
|---|---|
| PROJECT_PLAN.md | Good scope; stale “nothing built” status, unsupported PASylation, incomplete symptom primary-outcome framing, and unproven population broadening. Retain structure; refresh facts and dependencies. |
| README.md | Useful index; still calls Day 2 future work. Add current status, thesis/model files and known unresolved issues. |
| day1_summary.md | Useful history, but repeats wrong competitor/base-rate conclusions and overstates verification. Rewrite from corrected sources. |
| plain_english_summary.md | Requires substantial correction: both-trials-finished, both-ESSDAI, eligibility broadening and p-value-as-fluke-probability claims. Keep as rehearsal material after correction. |
| phase2_paper_explained.md | Helpful teaching aid; correct eligibility comparisons, biomarker overclaims and suggestion both populations worsen after withdrawal. Symptom benefit was largely sustained after withdrawal. |
| phase2_results.md | Core efficacy useful; safety incomplete and death wording ambiguous. Add exact analysis populations, CIs, response denominators and missing/rescue handling. |
| phase2_baseline_characteristics.md | Several confirmed transcription errors; correct against Table 1 before charting. Remove mean-versus-minimum eligibility inference. |
| essdai_measurement_properties.md | Useful topics; soften claims that failed trials prove endpoint insensitivity. Correct historical endpoint classifications, within-patient versus between-group interpretation, and composite descriptions before use. |
| ianalumab_competitor_analysis.md | Major revision: primary Ph2b success, individual NEPTUNUS-2 results, uncertainty and clinical-relevance interpretation. |
| historical_trial_evidence.md | Rebuild as an evidence table, not a numerical prior. Distinguish endpoint/test types, phases, cohorts and trial Ns. |
| nct06245408_risk_note.md | Add DASPRI; remove claims that smaller p-value proves lower placebo risk and that JOQUER enrichment is identical. |
| scenario_model.md | Keep scenario concept; rebuild variance/power presentation, multiplicity and effect uncertainty. One comparator transition cannot causally calibrate enrollment-driven shrinkage. |
| final_thesis.md | Clear forecast, overstated certainty. Rewrite only after correcting its supporting evidence and numerical sensitivities. |
| NCT06104124.csv | Useful registry snapshot; add or separately retain arms, eligibility, actual/estimated flags and protocol sources. Does not supply a full SAP. |
| NCT06104124.csv | Exact content match to CSV; convenient inspection copy, not a quantitative model. |
| NCT06245408.csv | Critical evidence that ESSPRI and DASPRI are both listed primary outcomes; narrative must catch up with this file. |
| NCT06245408.csv | Exact CSV match; same primary-outcome and timestamp caveats. |
| competitor_trials_landscape.csv | Useful 18-study inventory; includes PK, extensions, expanded access and withdrawn studies. Filter for the actual comparison question. |
| competitor_trials_landscape.csv | Exact CSV match; reconcile registry enrollment versus analyzed N before exporting comparator tables. |
| phase2_paper.pdf | Essential primary source. Use main tables, methods and extended subgroup results; not just the abstract. Some supplementary biomarker/source-data material is referenced separately. |
| reference_deck_maestro_nash.pdf | Strong analytical reference, 96 pages. Adopt thesis-first organization and explicit scenario assumptions; choose methods appropriate to continuous Sjögren's endpoints and a much shorter assignment. |
| .gitignore | Reasonable PDF/temporary-file exclusion; ensure it does not accidentally prevent delivery of the final PDF if relying on Git packaging. |

## Final recommendation

Spend the next work block correcting the evidence and statistical model. Then build a concise, defensible presentation. The project will become stronger through fewer unsupported claims, clearer assumptions and better use of its existing data—not through a much longer literature review.
