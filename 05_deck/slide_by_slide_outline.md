# Day 3 — Slide-by-Slide Outline

Detailed content for all 20 main slides + 6 appendix slides, built from the corrected
evidence base (`02_research/`, `03_analysis/`). Each slide has: headline (a
conclusion, not a topic, per the reference-deck convention), body content, the
table/chart spec, and its source.

## Build brief (read this before building anything)

**If you are a fresh session building this deck**: you have no memory of how this
project was researched. Everything you need is in this repo — start with
`../README.md` for the file index, `../PROJECT_STATUS.md` for the full narrative, and
`../PROJECT_PLAN.md` for original scope decisions. Do not invent numbers not found in
these files; where a slide below says a number is "TBD" or "not yet pulled," leave it
marked as such in the deck rather than filling it in.

**Format**: build a real, editable `.pptx` (python-pptx recommended, per
`../PROJECT_PLAN.md`), 16:9 widescreen layout throughout, plus a matching PDF export.
One main analytical visual per slide with concise interpretation text beside it, not
crammed multi-chart slides. Put a "Source:" line on every data slide (sources are
listed per-slide below).

**Hard constraints**:
- **Do not reuse the reference deck's (`../00_reference/reference_deck_maestro_nash.pdf`)
  branding, logo, analyst name, or footer, and do not imply Jefferies authorship.**
  This deck is the candidate's own work, referencing that deck only as a style
  template. Put the candidate's own name/title in the attribution — see "Open items"
  at the bottom of this file for the current placeholder status.
- Avoid decorative 3D charts, mixing ESSDAI and ESSPRI/DASPRI effects on one shared
  axis, and p-value-only rankings without effect sizes alongside them.
- Distinguish 90% CIs (used in the dazodalibep Phase 2 paper) from 95% CIs (standard
  elsewhere) explicitly wherever both appear — do not present them interchangeably.
- A table is an acceptable, non-apologetic substitute for a chart wherever noted below
  as time-constrained — do not treat table-only slides as incomplete.

---

## MAIN DECK (20 slides)

### Slide 1 — Title
**Headline:** Dazodalibep in Sjögren's Disease: A Phase 3 Readout Preview
**Content:** Candidate name/title (placeholder — needs your real name), analysis
cutoff date (Sept 15, 2026), trial focus line ("NCT06104124, systemic disease
activity — full analysis; NCT06245408, symptomatic disease — directional read").
**Visual:** Plain text title slide. No stock imagery, no decorative mechanism art.
**Source:** —

---

### Slide 2 — The call, up front
**Headline:** We lean positive on NCT06104124's systemic efficacy endpoint, with material uncertainty
**Content (three reasons + the largest risk, per the review's spec):**
1. Phase 2's own randomized result was real and appropriately powered for its size
   (ESSDAI diff −2.2, P=0.0167)
2. Pharmacodynamic biomarker evidence (CXCL13, RF suppression, reversible on
   crossover) supports genuine target engagement
3. A real-world precedent (ianalumab) proves this exact disease/endpoint
   combination can produce a Phase 3 win, and dazodalibep's own Phase 2 effect
   already exceeds the size that carried that competitor through
- **Largest risk**: our only calibration point for Phase 2→3 effect shrinkage
  (ianalumab, ~1.4× scale-up) doesn't cover a scale-up as large as dazodalibep's
  (~8.8×) — if erosion is proportionally worse, the true effect could fall below
  the detection floor
**Visual:** Concise trial-call table:

| Trial | Endpoint | Our call | Confidence |
|---|---|---|---|
| NCT06104124 (systemic) | ESSDAI change, Wk48 | Positive lean | Material uncertainty |
| NCT06245408 (symptomatic) | ESSPRI + DASPRI change, Wk48 | Positive lean | Wider uncertainty, later catalyst |

**Source:** `03_analysis/final_thesis.md`

---

### Slide 3 — What exactly is being forecast
**Headline:** Two trials, two populations, two different completion clocks
**Content:** Define precisely what "positive/negative" means for each trial —
statistical significance on the registered primary endpoint, not a broader claim.
**Visual:** Two-trial comparison table:

| | NCT06104124 | NCT06245408 |
|---|---|---|
| Population | ESSDAI≥5, systemic | ESSPRI≥5, ESSDAI<5, symptomatic |
| N | 651 | 434 |
| Primary endpoint(s) | ESSDAI change, Wk48 | ESSPRI change AND DASPRI change, Wk48 |
| Status | COMPLETED (primary completion 2025-07-23, actual) | ACTIVE_NOT_RECRUITING (primary completion 2026-10-22, estimated) |
| Results disclosed? | Not yet | Not yet — trial not finished |

**Note explicitly on this slide**: completion date ≠ disclosure date — flag this
distinction so the audience doesn't assume a result is imminent just because a trial
finished.
**Source:** `03_analysis/evidence_table.md`, `01_data/NCT06104124.csv`, `01_data/NCT06245408.csv`

---

### Slide 4 — Systemic activity vs. symptoms are different treatment questions
**Headline:** NCT06104124 targets active inflammation; NCT06245408 targets residual symptom burden in glands that still function
**Content:** Population 2's own Phase 2 eligibility required *residual* stimulated
salivary flow ≥0.1 mL/min — meaning symptomatic-trial patients still have some
working gland function, unlike patients with fully damaged/fibrotic glands. This
distinguishes reversible inflammatory activity (the systemic trial's target) from a
population whose remaining problem may be a mix of ongoing inflammation and
already-accumulated gland damage that a purely anti-inflammatory drug may reach less
completely.
**Visual — explicit layout for the builder** (two boxes side by side, no free
interpretation needed):
- Left box, header "Systemic (NCT06104124)": bullet list of ESSDAI domains
  (articular, cutaneous, glandular, lymphadenopathy, hematologic, constitutional,
  pulmonary, renal, CNS, PNS, muscular) → arrow down to "Treatable while active"
- Right box, header "Symptomatic (NCT06245408)": bullets "Dryness / Fatigue / Pain
  (ESSPRI+DASPRI)" and "Entry requires residual stimulated salivary flow ≥0.1 mL/min"
  → arrow down to "Partly reversible, partly structural"
- No connecting arrows between the two boxes needed — they represent two different
  patient populations, not a progression from one to the other.
**Source:** `02_research/phase2_baseline_characteristics.md`, `01_data/NCT06245408.csv`

---

### Slide 5 — CD40L blockade has a plausible route to clinical benefit
**Headline:** Blocking the T-cell→B-cell "go-ahead" signal has a direct, testable mechanistic path to reduced autoantibody production
**Content:** T-cell CD40L → CD40 (on B-cells/APCs/epithelial cells) → B-cell
activation/antibody production/germinal-center formation. Two ways to interrupt: block
the ligand (dazodalibep) or the receptor (iscalimab). Contrast with ianalumab's
different mechanism (BAFF-R, B-cell depletion). Cover the first-generation anti-CD40L
antibody thromboembolism history and why dazodalibep's Tn3-scaffold, Fc-free design
specifically avoids the platelet-crosslinking mechanism (not all thrombotic risk
categorically).
**Visual — explicit node/arrow list for the builder:**
- Node 1 (left): "T-cell" with a small tag "CD40L"
- Node 2 (center): "B-cell / APC / epithelial cell" with a small tag "CD40"
- Arrow from Node 1 → Node 2, labeled "costimulatory signal"
- Node 3 (right, downstream of Node 2): "Antibody production, germinal center
  formation" → this is the harmful process being interrupted
- Block/X icon placed ON the arrow between Node 1 and Node 2, labeled "Dazodalibep
  (blocks CD40L, the ligand)"
- Block/X icon placed ON Node 2 itself, labeled "Iscalimab (blocks CD40, the receptor)"
- A separate, visually distinct fourth node off to the side: "B-cell survival signal
  (BAFF-R)" with its own block icon labeled "Ianalumab (different mechanism — B-cell
  depletion + BAFF-R blockade, not part of the CD40/CD40L handshake)" — keep this
  visually separated from the main CD40/CD40L flow so it's not implied to act on the
  same pathway.
**Source:** Biological rationale content now consolidated in `PROJECT_STATUS.md`
Section 2; `02_research/phase2_results.md` (Tn3 scaffold correction, DVT timing argument)

---

### Slide 6 — Phase 2 design: two populations, one dose, a crossover
**Headline:** Phase 2 tested two distinct populations against a single 1,500mg regimen, with no dose-ranging
**Content:** Randomized, double-blind, placebo-controlled, with a crossover stage
after Day 169. Population 1 (n=74) and Population 2 (n=109) tested in parallel. Flag
explicitly: only one dose tested (unlike ianalumab/iscalimab's proper Ph2b dose-ranging
designs) — now partially mitigated by population PK/PD modeling supporting Phase 3
dose selection (see Slide 11).
**Visual — explicit timeline for the builder:** horizontal timeline, Day 0 to Day 365,
with two parallel lanes:
- Lane 1: "PBO → DAZ" — solid bar Day 0–169 labeled "Placebo," solid bar Day 169–365
  labeled "Dazodalibep 1,500mg"
- Lane 2: "DAZ → PBO" — solid bar Day 0–169 labeled "Dazodalibep 1,500mg," solid bar
  Day 169–365 labeled "Placebo"
- Vertical dashed line at Day 169 labeled "PRIMARY ANALYSIS" — this is the single most
  important marker on this slide; make it visually dominant
- Small callout at Day 365: "Crossover data used for durability check only, not
  primary efficacy"
**Source:** `02_research/phase2_paper_explained.md`, `02_research/phase2_results.md`

---

### Slide 7 — Systemic Phase 2 efficacy supports the call, with real uncertainty
**Headline:** ESSDAI improved 2.2 points more on drug than placebo (P=0.0167) — real, but Phase 2-sized
**Content:** DAZ −6.3±0.6 vs. PBO −4.1±0.6 at Day 169. Note the paper's own relaxed
α=0.10 threshold (small-N caution) — this result clears the standard 0.05 bar anyway.
**Visual:** ESSDAI change-from-baseline line plot over time (Baseline→Day169), both
arms, with error bars and N-at-risk table beneath (mirrors the paper's own Fig. 2a).
Adjusted effect (−2.2) and 90% CI (−3.6, −0.7) labeled explicitly — **note: this is a
90% CI, not 95%, per the paper's own relaxed design — label this distinction clearly,
don't silently present it as a standard 95% CI.**
**Source:** `02_research/phase2_results.md`

---

### Slide 8 — Domain and responder results qualify the headline finding
**Headline:** The continuous ESSDAI score passed; categorical responder thresholds mostly didn't
**Content:** ESSDAI(3) response 72.2% vs 59.5%, P=0.33 (not significant); ESSDAI(4)
66.7% vs 48.6%, P=0.18 (not significant); ESSDAI(5) response significant but
explicitly post hoc. This is consistent with (not proof of) ESSDAI's known
instrument-sensitivity limitations — dichotomizing loses information and the sample
is small, so don't overstate this as "ESSDAI is defective." Exploratory RA/SLE
subgroup: placebo-adjusted change ≈−1.6 (no RA/SLE) vs. ≈−3.3 (with RA/SLE) — small
subgroups, not a robust interaction claim.
**Visual:** Responder-rate bar chart with denominators (n/N) labeled on each bar, not
just percentages; separate small panel for the RA/SLE subgroup plot, explicitly
labeled "exploratory, small N."
**Source:** `02_research/phase2_results.md`

---

### Slide 9 — Symptom and biomarker evidence support activity, with limits
**Headline:** CXCL13 and rheumatoid factor suppression show real target engagement, independent of the noisier clinical scores
**Content:** CXCL13 significantly suppressed both populations (P=0.0010 Pop1,
P<0.0001 Pop2), rebounding toward baseline off-drug. RF significantly reduced both
populations (P<0.0001). Label explicitly: this is exploratory biomarker evidence
supporting pharmacological activity — it does not, alone, prove clinically meaningful
efficacy, and should not be the default explanation if Phase 3 misses.
**Visual:** Two clearly separated panels — (1) CXCL13/RF suppression over time, (2)
ESSPRI Population 2 result (−1.3, P=0.0002) — labeled as the cleanest Phase 2 result
in the program. Unadjusted secondary p-values labeled as such throughout.
**Source:** `02_research/phase2_results.md`

---

### Slide 10 — What changes in Phase 3, and what's actually unknown
**Headline:** Phase 3 extends duration and multiplies N by ~9×; population differences are not yet established
**Content:** **Corrected framing**: Phase 2 Population 1 already required ESSDAI≥5 —
the same eligibility floor as NCT06104124 — so Phase 3 is *not* known to enroll a
broader/less-severe population; that requires actual enrollment data, not yet public.
What IS verified: N goes from 74→651 (~8.8×), duration from 24wk→48wk, and two dose
arms replace Phase 2's single dose.
**Visual:** Phase 2→3 bridge table:

| Factor | Phase 2 | Phase 3 (NCT06104124) | Status |
|---|---|---|---|
| N (this population) | 74 | 651 | Verified |
| Duration | 24 wks | 48 wks | Verified |
| Dose arms | 1 | 2 | Verified (doses undisclosed) |
| Population severity | Baseline ESSDAI 10.1–11.4 | Unknown | **Not established** — removed from earlier drafts as unsupported |
| RA/SLE overlap | 19–24% | Unknown | Open — real transportability question if it differs |

**Source:** `03_analysis/final_thesis.md`, `02_research/phase2_baseline_characteristics.md`

---

### Slide 11 — Dose selection has a real, if partial, quantitative basis
**Headline:** Population PK/PD modeling supports the Phase 3 dose choice, but targets a biomarker threshold, not a guaranteed clinical effect size
**Content:** A 4-trial population PK/PD model found Sjögren's patients clear the drug
more slowly than healthy volunteers/RA patients; Phase 3 doses are modeled to sustain
exposure above the IC50 for Ki67+ B cells and RF throughout the dosing interval. Two
active dose arms vs. one placebo raises a multiplicity question — no public
information on the testing hierarchy/alpha-split Amgen is using.
**Visual — two side-by-side boxes:**
- Left box, header "Confirmed (registry)": "3 arms — Dose 1, Dose 2, Placebo" / "Doses
  and allocation ratio not disclosed"
- Right box, header "Illustrative only — not confirmed": simple tree, "Total α=0.05"
  splitting into "Dose 1 vs. Placebo, α=0.025" and "Dose 2 vs. Placebo, α=0.025" — an
  even split shown only as one possible scheme, with a bold caption underneath: "This
  is one illustrative possibility, not Amgen's actual statistical plan, which is not
  public."
**Source:** `03_analysis/additional_topics.md`, `03_analysis/scenario_model.md`

---

### Slide 12 — Ianalumab validates the endpoint, not dazodalibep's specific effect
**Headline:** A different mechanism already won on this exact endpoint construct — narrowly, both times
**Content:** Ph2b: dose-response primary objective MET (corrected from earlier
mischaracterization as a "miss" — only the secondary pairwise 300mg comparison
missed, at p=0.092). NEPTUNUS-1: −1.3, P=0.0496. NEPTUNUS-2 monthly: −1.0, P=0.041;
every-3-months arm: not significant. Pooled: P=0.0031 (not a substitute for two
individually significant trials).
**Visual:** Forest plot / table across Ph2b (dose-response test + pairwise arms),
NEPTUNUS-1, and NEPTUNUS-2 (both dosing arms), each row labeled with its actual
analysis type (primary dose-response test vs. secondary pairwise vs. primary
confirmatory) and arm-level N — do not present these as if they were all the same
kind of comparison.
**Source:** `02_research/ianalumab_competitor_analysis.md`

---

### Slide 13 — Same-pathway and historical studies: mixed, relevant lessons
**Headline:** Both CD40-pathway trials met their primary objective; most other mechanisms tested against different endpoint constructs did not
**Content:** Qualitative evidence table, not a computed base rate (explicitly avoid
restating a "33%/100%" figure). TRACTISS and ETAP corrected to their actual endpoint
definitions (VAS-composite and multi-part composite responder, respectively — neither
is a simple continuous-ESSDAI miss).
**Visual:** Compact comparator matrix, systemic (ESSDAI/dose-response) and symptom
(ESSPRI) endpoints grouped separately, each row showing drug/mechanism/N/exact
endpoint/result:

| Drug | Endpoint type | Result |
|---|---|---|
| Dazodalibep | Continuous ESSDAI | Met |
| Iscalimab (Cohort 1) | Dose-response ESSDAI | Met |
| Ianalumab (Ph2b) | Dose-response ESSDAI | Met |
| Abatacept (ASAP-III) | Continuous ESSDAI | Missed (double-blind) |
| Tocilizumab (ETAP) | Composite responder | Missed |
| Rituximab (TRACTISS) | VAS composite (not ESSDAI) | Missed |
| Iscalimab (Cohort 2) | ESSPRI | Missed (p=0.12) |

**Source:** `02_research/historical_trial_evidence.md`

---

### Slide 14 — Larger enrollment improves precision; variance controls how much
**Headline:** NCT06104124 needs only ~1.0–1.5 ESSDAI points to be reliably detectable — well below Phase 2's observed 2.2
**Content:** Present the three variance assumptions side by side rather than picking
one. Emphasize: this describes detectability, not a guarantee of the true effect size.
**Visual:** Line chart — x-axis: true ESSDAI effect (0–2.5), y-axis: statistical
power (%), three lines for SD=3.65 / 5.00 / 5.47. **[Chart not yet built — Day 4
task; table version already exists and can substitute if time-constrained.]**
**Formula to generate this chart** (n≈217/arm, two-sided α=0.05, independent-normal
approximation): for each SD, compute SE = SD × √(2/217), then for a range of assumed
true deltas, Power(delta) = Φ(delta/SE − 1.96), where Φ is the standard normal CDF.
Plug in SD=3.65, 5.00, 5.47 for the three lines. This reproduces the discrete points
already tabulated in `03_analysis/scenario_model.md`'s sensitivity table — use it to
fill in the curve between those points, not to generate new headline numbers.
**Source:** `03_analysis/scenario_model.md`

---

### Slide 15 — The forecast rests on explicit, challengeable assumptions
**Headline:** Bull/base/bear are assumed inputs being stress-tested, not predictions
**Content:** Present the three scenarios plainly labeled as illustrative, with the
qualitative (not computed) weighting stated as a judgment call.
**Visual:** Bull/base/bear table:

| Scenario | Assumed delta | SD used | p-value | Weight (judgment) |
|---|---|---|---|---|
| Bull | 2.0 | 5.47 | <0.001 | ~20% |
| Base | 1.4 | 5.47 | ≈0.008 | ~50% |
| Bear | 0.6 | 5.47 | ≈0.25 | ~30% |

**Source:** `03_analysis/scenario_model.md`

---

### Slide 16 — The call gets less robust as variance and effect erosion rise
**Headline:** At higher, more conservative variance, the "safe" margin shrinks — but doesn't disappear
**Content:** Show how conditional power at a fixed assumed effect (1.4) drops from
98% (optimistic SD) to 76% (externally-anchored SD) to potentially lower still if
multiplicity correction applies.
**Visual:** Sensitivity table (already built) presented as the primary exhibit;
upgrade to a heatmap (effect × effective SD) in Day 4 if time allows — **table is an
acceptable substitute, not a placeholder to apologize for.**
**Source:** `03_analysis/scenario_model.md`

---

### Slide 17 — Symptomatic efficacy is encouraging; DASPRI adds an open question
**Headline:** NCT06245408's own Phase 2 precursor was the program's cleanest result — but two co-primary instruments, not one, must be understood
**Content:** ESSPRI diff −1.3, P=0.0002 (Population 2). **DASPRI's own dazodalibep
Phase 2 numbers are not yet pulled into this project — open gap, flag explicitly
rather than inventing a number.** No public information on whether both instruments
must pass or either is sufficient.
**Visual:** ESSPRI/DASPRI side-by-side comparison table (DASPRI column marked "TBD —
pending extraction from Phase 2 paper's secondary endpoints"); JOQUER precedent noted
as conceptually related, not procedurally identical.
**Source:** `02_research/nct06245408_risk_note.md`

---

### Slide 18 — An efficacy win still needs a credible benefit-risk profile
**Headline:** Two investigator-attributed SAEs in Phase 2 warrant explicit disclosure, not a "no signal" framing
**Content:** DVT + drug-induced liver injury (same participant, Stage II, onset 180
days post-dose, investigator-attributed to drug); invasive ductal breast carcinoma
(Population 2, investigator-attributed to drug); one COVID-19-related death
(investigator: unrelated). Precise argument: onset timing argues against the specific
first-gen platelet-crosslinking mechanism — not "no serious safety signal."
**Visual:** Safety table by population/stage, with denominators, exact timing, and
investigator attribution as separate explicit columns — no vague summary language.
**Source:** `02_research/phase2_results.md`

---

### Slide 19 — The strongest case against our forecast
**Headline:** Our only Phase 2→3 calibration point covers a much smaller scale-up than dazodalibep's own
**Content:** Ianalumab's Ph2b→Ph3 transition (~1.4× scale-up) retained 68% of its
effect. Dazodalibep's transition is ~8.8×, with no precedent for effect retention at
that scale. If erosion is proportionally worse, the true delta falls into the range
(0.6–1.0) where multiple other Sjögren's trials' real effects vanished into noise.
Reinforced by Phase 2's own categorical-responder near-misses.
**Visual:** Ranked failure-mechanism list (this one first, others — multiplicity
correction, dose-selection uncertainty, DASPRI ambiguity — ranked below), each paired
with "what evidence would change this."
**Source:** `03_analysis/final_thesis.md`

---

### Slide 20 — Final call and readout interpretation
**Headline:** Positive lean on NCT06104124; positive lean with wider uncertainty on NCT06245408 — here's exactly what would confirm or break each
**Content:** One-paragraph restatement of the call. Explicit note distinguishing
statistical significance from convincing patient benefit from acceptable benefit-risk
(three separate questions — this call only answers the first).
**Visual:** The full readout interpretation matrix — **already built, ready to use
directly**:

| Dimension | Strengthens | Weakens | Reverses |
|---|---|---|---|
| Efficacy (statistical) | Δ≥1.4, p<0.01 | Δ 0.7–1.0, p near 0.05 | Δ<0.7, non-significant |
| Efficacy (clinical meaning) | Responder analyses also pass | Continuous passes, responders miss again | Any dose arm worse than placebo |
| Dose/exposure | Higher sustained exposure than Ph2 disclosed | No dose rationale disclosed | Dose deviated from PK/PD target |
| NCT06245408 | Clean positive readout | Narrow/mixed result | Clear negative |
| Safety | No new signals | Modest infection/thromboembolic uptick | Replicated thromboembolic signal above background |
| External | Nipocalimab also succeeds | No new info | A closely related CD40L asset fails |

Separately labeled timeline: completion (already occurred, 2025-07-23) vs. likely
disclosure window (Amgen Q3 earnings, late Oct/early Nov 2026, or ACR Convergence,
Nov 6–11, 2026) — kept as two distinct dates, not conflated.
**Source:** `03_analysis/additional_topics.md`, `03_analysis/final_thesis.md`

---

## APPENDIX (6 slides)

### Appendix 1 — Full Phase 3 design and eligibility comparison
Full inclusion/exclusion criteria for both trials, with source dates and
actual-vs-estimated date flags preserved. **Source:** `01_data/NCT06104124.csv`, `01_data/NCT06245408.csv`

### Appendix 2 — Corrected baseline characteristics and background therapies
Full Table 1 reproduction (both populations), with the Schirmer's-test correction
and the flagged, unresolved discrepancy against the external review's other four
proposed baseline corrections (kept as originally transcribed, per re-verification).
**Source:** `02_research/phase2_baseline_characteristics.md`

### Appendix 3 — Full Phase 2 endpoints, subgroups, and crossover data
Complete secondary endpoint listing, the RA/SLE subgroup finding, and full crossover
(Stage II) durability numbers for both populations. **Source:** `02_research/phase2_results.md`

### Appendix 4 — Statistical formulas, assumptions, and expanded sensitivity outputs
The full variance-sensitivity table (all 5 rows, including the illustrative
multiplicity/missing-data rows), the corrected ianalumab-based p-value recalculation
(0.013, not the earlier erroneous 0.0002), and the observed-significance-threshold vs.
80%-power distinction spelled out. **Source:** `03_analysis/scenario_model.md`

### Appendix 5 — Expanded comparator and safety tables
Full ianalumab arm-by-arm data (Ph2b + both NEPTUNUS trials), the full historical
evidence table, and the complete Phase 2 safety table (Table 3 equivalent) with all
AEs, not just the headline SAEs. **Source:** `02_research/ianalumab_competitor_analysis.md`, `02_research/historical_trial_evidence.md`, `02_research/phase2_results.md`

### Appendix 6 — References
Compile a single reference list from every file's "Sources" section — not yet built
as a standalone bibliography; can be assembled directly from `03_analysis/evidence_table.md`'s
source column plus each research file's sources section. **[Not yet compiled — Day 4 task.]**

---

## Open items to close before Day 4 build
1. Real name/title for the attribution placeholder (Slide 1, and deck footer if
   mirroring the reference deck's per-slide attribution convention)
2. Dazodalibep's actual DASPRI numbers for Population 2 (Slide 17)
3. Appendix 6's compiled reference list
4. Decision: build the literal power-curve/heatmap charts (Slides 14, 16) or keep the
   table versions — both are legitimate, chart is nicer if time allows
