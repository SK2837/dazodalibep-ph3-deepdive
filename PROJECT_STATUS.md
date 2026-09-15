# Project Status — Complete Explanation

*Last updated: September 15, 2026*

This is the single comprehensive document explaining the whole project: what the
assignment is, what's been done, what the current bull/base/bear numbers and final
call are, what the reference deck says and how we're using it, what tables/charts the
eventual presentation will contain, and an honest review of whether the work actually
satisfies the brief. Read this first if you're picking the project back up cold.

---

## 1. The assignment, restated

Jefferies (Healthcare Equity Research) sent a take-home test: produce a PowerPoint
"deep dive" on Amgen's dazodalibep Phase 3 program in Sjögren's disease
(**NCT06104124** and **NCT06245408**) and land on an explicit, evidence-backed call —
will the primary efficacy endpoint(s) read out positive or negative. Required topics
(not exhaustive): biological rationale of CD40L targeting + Phase 2 insights; unique
features of the Phase 3 designs (symptomatic vs. systemic) + statistical
considerations; lessons from other trials (ianalumab). A reference deck (MDGL/
MAESTRO-NASH) was supplied as a template for analytical depth and slide anatomy, not
as the topic. Due Friday, September 18, 11:00am ET.

---

## 2. What's been done — the process, end to end

### Day 1 (foundational research) — complete
Pulled and verified: the Phase 2 published paper (both patient populations), both
Phase 3 trials' official registrations and current status, the ESSDAI measurement
literature (MCID, placebo-response modeling, composite indices), the ianalumab
competitor program (Phase 2b and Phase 3), a historical table of comparator Sjögren's
trials, and a risk note for the secondary trial. See `README.md` for the file-by-file
index.

### Day 2 (quantitative modeling) — complete
Built a statistical bridge from Phase 2's observed result to a Phase 3 forecast: a
minimum-detectable-effect / variance-sensitivity analysis, a bull/base/bear scenario
table, and an explicit final thesis with a ranked counter-argument.

### External review and correction pass — complete
An outside review (`external_review.md`) caught several real errors —
most importantly, that ianalumab's Phase 2b trial was mischaracterized as a "miss"
(it actually met its real primary objective, a dose-response test), that a
statistical calculation understated variance and overstated confidence, and that the
secondary trial's second co-primary endpoint (DASPRI) was missing from the narrative
entirely. All of these were independently re-verified against primary sources (not
accepted at face value — the review itself had some errors too, documented in
`phase2_baseline_characteristics.md`) and corrected across every affected file.

### Additional topics pass — partially complete
Of 8 "additional topics worth adding" the review suggested, 3 were judged high-value/
low-effort and completed (dose/exposure PK-PD bridge, clinical-meaning synthesis,
readout interpretation table — see `additional_topics.md`); 2 were already
covered as a byproduct of the correction pass (NEPTUNUS-1/2 individual results,
iscalimab's symptomatic-cohort miss); 3 were deprioritized as low-payoff for a 4-day
assignment (missing-data/rescue-medication treatment, and deeper endpoint-architecture/
population-transportability work beyond what's already captured).

### Not yet started
Day 3 (slide-by-slide text outline) and Day 4 (actual `.pptx` build + PDF export).

---

## 3. The current bull/base/bear numbers and final call

**This is the load-bearing quantitative result of the whole project.** Full detail and
methodology in `scenario_model.md`; the call itself in `final_thesis.md`.

### The statistical setup
NCT06104124 has N=651 across 3 arms (2 dazodalibep doses + placebo; ~217/arm assumed,
since the actual allocation ratio isn't disclosed). Three different variance
(standard deviation) assumptions were tested, because picking just one — as an earlier
version of this project did — silently determines how confident the whole forecast
looks:

| Variance assumption | Source | Effect needed for 80% power |
|---|---|---|
| SD = 3.65 | Backed out from dazodalibep's own Phase 2 standard errors | 0.98 points |
| SD = 5.00 | Dazodalibep's own Phase 2 protocol's planning assumption | 1.34 points |
| SD = 5.47 | Backed out from ianalumab's real Phase 3 trial (NEPTUNUS-1) — the only real external benchmark available | 1.47 points |

The middle-to-conservative rows are treated as more credible than the first, since the
first is the most self-flattering assumption and the other two are either the drug's
own original planning basis or a real outside data point.

### Bull / base / bear (illustrative assumed-effect scenarios, using SD=5.47)

| Scenario | Assumed true ESSDAI delta | Resulting p-value | Read |
|---|---|---|---|
| **Bull** | 2.0 | <0.001 | Would pass clearly |
| **Base** | 1.4 | ≈0.008 | Would pass, real but not enormous margin |
| **Bear** | 0.6 | ≈0.25 | Would not reach significance |

**These are assumed inputs being stress-tested, not predicted outcomes** — nobody
knows the true effect before the readout. The qualitative weighting given to these
(Bull ~20% / Base ~50% / Bear ~30%) is an analyst judgment call, explicitly labeled as
such, not a computed probability.

### The final call
**We lean positive on NCT06104124's ESSDAI primary endpoint, with material
uncertainty that should not be understated.** Ranked reasons: (1) Phase 2's own
randomized result is real and appropriately powered for its size; (2) pharmacodynamic
biomarker evidence (CXCL13, rheumatoid factor suppression, reversible on crossover)
supports genuine target engagement; (3) ianalumab's real Phase 3 wins prove this
disease/endpoint combination *can* produce a positive readout, and dazodalibep's own
Phase 2 effect already exceeds the size that carried ianalumab through; (4) both
CD40-pathway trials to date (dazodalibep, iscalimab) met their respective primary
objectives — a real but small-sample pattern, not a computed base rate.

**The single strongest counter-argument**: the only real precedent for calibrating how
much a Phase 2 effect shrinks going into Phase 3 (ianalumab, which scaled up ~1.4×)
retained 68% of its original effect. Dazodalibep's own scale-up is ~8.8× — far larger,
with no precedent for what happens to effect retention at that scale. If erosion is
proportionally worse than ianalumab's, the true delta could fall into the exact range
(0.6–1.0) where several other Sjögren's trials' real effects have vanished into
placebo noise before.

**For NCT06245408** (secondary trial): directionally positive, with more confidence
than the primary trial (its own Phase 2 precursor was the cleanest result in the
program, p=0.0002), a wider error bar (its instruments — ESSPRI and now-added DASPRI —
have no objective anchor), and a later, less certain catalyst timeline.

---

## 4. What tables and charts the presentation will need

Drawn from the reference deck's own visual patterns (see Section 5 below) and this
project's actual content. Not yet built — this is the plan for Day 3/4.

| Planned exhibit | Data source (already built) |
|---|---|
| Trial comparison table (population, N, endpoints, timepoints, status) | `evidence_table.md`, the two trial CSVs |
| CD40/CD40L mechanism diagram | Conceptual — needs to be drawn fresh, no existing file |
| Phase 2 ESSDAI/ESSPRI longitudinal plots with error bars | Data in `phase2_results.md`; original figures are in the Phase 2 PDF and can be redrawn or referenced |
| Phase 2 domain/responder bar charts | `phase2_results.md` |
| Ianalumab comparator forest plot/table (Ph2b + NEPTUNUS-1 + NEPTUNUS-2, arm-level) | `ianalumab_competitor_analysis.md` |
| Historical trial comparator matrix | `historical_trial_evidence.md` (already qualitative, not a probability table — matches the review's guidance) |
| Variance/power sensitivity table or heatmap | `scenario_model.md` |
| Bull/base/bear assumption table | `scenario_model.md` |
| Phase 2→3 bridge table (what changed, verified vs. assumed) | `final_thesis.md`, `phase2_baseline_characteristics.md` |
| Safety summary table (by population/stage, denominators, attribution) | `phase2_results.md` |
| Readout interpretation matrix (what would strengthen/weaken/reverse) | Already fully built in `additional_topics.md` — ready to drop into a slide with light formatting |
| Final call slide (headline + ranked evidence + counter-argument) | `final_thesis.md` |

---

## 5. What the reference deck (MAESTRO-NASH) says, and how we're using it

**File**: `reference_deck_maestro_nash.pdf` (96 pages), a real Jefferies analyst
deck by Akash Tewari predicting Madrigal Pharmaceuticals' (MDGL) Phase 3 NASH-drug
(resmetirom) readout before it happened.

### What it actually contains
- **A conclusion-first headline on every slide** (e.g., "we think this trial will
  likely hit on NASH resolution but may be mixed on fibrosis"), never a neutral topic
  label.
- **A biological-rationale section** connecting the drug's mechanism (a thyroid
  hormone receptor-beta agonist) to a specific, quantified prediction, not just a
  disease-education slide.
- **A statistical-design deep dive**: multiple-endpoint testing methods (Bonferroni,
  Hochberg, Truncated Holm), what the sponsor's own disclosed power assumptions imply
  about the minimum effect size needed, and how alpha might be split or recycled
  across two primary endpoints.
- **An explicit Phase 2→Phase 3 bridge table**: starting from Phase 2's actual
  response rate, then a column-by-column build-up of every design change (updosing,
  duration, population enrichment, regression to the mean) leading to a Phase 3
  response rate — repeated for bull, base, and bear cases with real odds
  ratios/p-values attached to each.
- **Cross-trial benchmarking**: a table of many other NASH drugs' placebo and drug
  response rates, used to sanity-check whether the assumed Phase 3 numbers are
  realistic, not invented.
- **A named "biggest risk" and a dedicated section on what could break the thesis** —
  not just supporting evidence.
- **A separate valuation section** (investor survey, DCF, scenario-weighted price
  targets) — explicitly **not** something this project is replicating, per the
  original scope decision (science/statistics only, no valuation).

### What we are taking as direct reference (methodology, not content)
1. The **conclusion-first slide headline** convention — adopted throughout
   `final_thesis.md` and planned for every slide in Day 3/4.
2. The **explicit Phase 2→Phase 3 bridge table structure** — directly mirrored in
   `scenario_model.md`'s bridge-construction table.
3. **Presenting bull/base/bear with real numbers and rationale for each assumption**,
   not just a qualitative "could go well or badly" — mirrored in the same file.
4. **Cross-trial benchmarking to sanity-check assumptions** — mirrored in
   `historical_trial_evidence.md` and `ianalumab_competitor_analysis.md`, using real
   Sjögren's trials instead of NASH trials.
5. **A dedicated, named "strongest counter-argument"** rather than a vague risk list —
   mirrored in `final_thesis.md`.

### What we've done differently or added beyond the reference deck
1. **A formal variance-sensitivity table across three distinct assumptions**, rather
   than committing to one. The reference deck's own power/effect-size analysis (pages
   26-27) uses a single assumed cohort size and doesn't stress-test the variance
   assumption itself the way `scenario_model.md` now does.
2. **An explicit statement of what the model does NOT compute** (a true probability of
   trial success, which would require integrating over effect/variance/dose/
   missing-data/multiplicity uncertainty) — the reference deck's Monte Carlo section
   (page 50) does compute an overall probability (83%) for MDGL, which we deliberately
   did not attempt to replicate for dazodalibep without equivalent disclosed inputs
   (MDGL's deck had sponsor-disclosed power assumptions to build from; we don't have
   dazodalibep's SAP).
3. **A live external-review correction cycle** — the reference deck is a finished,
   polished analyst product; this project's working files carry visible correction
   notes documenting what was wrong and why, which is unusual for a finished deck but
   appropriate for a working research repository.
4. **Pharmacodynamic/biomarker evidence as an independent evidence line** (CXCL13, RF
   suppression) — the reference deck's biology section supports its *prediction*
   directly; our project uses biomarker data as a separate check on *whether a future
   miss should be attributed to the drug or to the endpoint*, which the NASH deck
   didn't need since MRI-PDFF is itself a quantitative biomarker already built into its
   prediction chain.
5. **The "clinical meaning of the outcome" synthesis** (`additional_topics.md`,
   item 2) — distinguishing statistical significance from patient-level benefit from
   benefit-risk — is a framing this project added explicitly; the reference deck
   folds an equivalent distinction implicitly into its valuation section instead
   (which this project is not building).

---

## 6. Does this satisfy the brief? — Self-review

| Requirement | Status | Detail |
|---|---|---|
| Clear call on one or both trials | ✅ Done | `final_thesis.md` — explicit positive lean on NCT06104124, directional positive on NCT06245408 |
| CD40L biological rationale | 🟡 Partial gap | Discussed in chat early in the project but **never saved to its own file** — this is a real gap for a self-contained repo; recommend creating `biological_rationale.md` before Day 3 |
| Phase 2 analysis | ✅ Done | `phase2_results.md`, `phase2_baseline_characteristics.md`, `phase2_paper_explained.md` |
| Phase 3 design distinctions (symptomatic vs. systemic) + statistical considerations | ✅ Done | `essdai_measurement_properties.md`, `nct06245408_risk_note.md` (now includes DASPRI), `scenario_model.md` |
| Lessons from other trials (ianalumab) | ✅ Done, corrected | `ianalumab_competitor_analysis.md`, `historical_trial_evidence.md` |
| Public-source methodology, exact citations | ✅ Done | Every file carries sources; `evidence_table.md` consolidates all of them with uncertainty flags |
| PowerPoint format | ❌ Not started | Day 3 (outline) and Day 4 (build) remain |

**Net assessment**: the analytical substance the brief actually asks for is
essentially complete and has been independently reviewed and corrected once already.
The two real remaining gaps are (1) the missing standalone biological-rationale file,
and (2) the entire presentation-building phase, which is a real, substantial
remaining effort — not a small finishing touch — given ~3 days left before the
deadline.

---

## 7. Honest risk to the timeline
Day 3 (full slide-by-slide outline) and Day 4 (actual editable `.pptx` + PDF export)
have not started, and building an editable, well-sourced 20-slide deck plus appendix
in the remaining time is the largest single piece of work left. Recommend prioritizing
getting a complete, even if rough, first-pass deck built soon rather than continuing
to deepen the research further.
