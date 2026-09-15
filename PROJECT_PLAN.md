# Dazodalibep Ph.3 Deep Dive — Project Plan (Jefferies take-home test)

## What This Project Is About

This is a take-home test for a Jefferies healthcare equity research job application. Amgen has a drug called dazodalibep in Phase 3 trials for Sjögren's disease, and it hasn't read out results yet. The candidate's job is to act like a sell-side biotech analyst and make a clear, well-supported prediction — will the drug's main trial results come back positive or negative — using the science, the trial design, and statistics, and present that prediction as a PowerPoint deck by the deadline (Friday 9/18, 11:00am ET).

## Context

This is a take-home test for a Jefferies Healthcare Equity Research role (associate/analyst track), due **Friday 9/18, 11:00am ET**. The brief: produce a "deep dive" PowerPoint that lays out analysis of Amgen's dazodalibep Phase 3 program in Sjögren's disease (**NCT06245408** & **NCT06104124**) and lands on an explicit, evidence-backed call — will the primary endpoint(s) read out positive or negative. The attached MDGL/MAESTRO-NASH deck is the template for the *kind* of thinking and slide anatomy expected, not the topic.

**Status as of Sept 15, 2026 (updated — this section originally said "nothing has been
built yet," which is now stale): Day 1 and Day 2 research/modeling are complete** — see
`README.md` for the current file index and `day1_summary.md`/`final_thesis.md` for
what's been produced. An external review (`external_review.md`) subsequently
identified several factual and statistical errors in that work, which have been
corrected across the affected files (see each file's own correction notes). Day 3
(slide-by-slide outline) and Day 4 (deck build) have not yet started.

This plan originally existed to agree on scope and process **before** any research or
slide-building started, per the instruction: plan first, then move step-by-step,
explaining the reasoning at each stage before producing content. That process has now
happened through Day 1/2; this document is retained for its scope rationale below.

**Decisions already locked in (from your answers):**
- **Primary trial — NCT06104124 (systemic disease-activity study):** the full deep-dive treatment — Ph2→Ph3 bridge, bull/base/bear scenario modeling, minimum-effect-size/power calc, competitor + historical benchmarking, and the explicit positive/negative thesis.
- **Secondary trial — NCT06245408 (symptomatic study):** a lighter section covering design and statistical-risk differences vs. the primary trial (population/enrichment, endpoint construct, placebo-response profile) — **no** full scenario/probability buildout for this one.
- **Why this split (your reasoning, recorded for the record):**
  1. NCT06104124 already completed primary completion in **July 2026**, making it the trial most likely to actually read out "later this year" as the email frames it — the higher-stakes, more time-relevant call. *(This gets a direct CT.gov verification pass on Day 1 — nothing in this plan gets asserted without a source check, including this.)*
  2. With a 4-day build, splitting full quantitative depth across both trials risked two shallow models instead of one rigorous one — and the reference deck's whole strength is depth (back-solved effect sizes, explicit bull/base/bear math) on a single readout, not breadth across many.
  - **Trade-off acknowledged:** doing both trials fully would more literally satisfy the brief's "systemic vs. symptomatic settings" comparison framing and show engagement with the full assignment scope — but the brief explicitly allows "either one, or both," so this focused approach is a legitimate, and given the deadline, safer choice.
- **Science/statistics only** — no DCF/valuation/peak-sales section. All effort goes into the biological rationale, trial design, and statistical call.
- **Real, editable output** — a `.pptx` built via a script (not hand-wavy), plus a PDF export for easy review, since the brief requires "PowerPoint format."
- **Per-slide sourcing + attribution formatting**, mirroring the reference deck (a "Source:" line on every data slide, a references appendix, and a title-slide/footer attribution block using a placeholder name until you give me the real one).

---

## What Jefferies Is Actually Testing (deconstructing the brief)

Reading the instructions against the reference deck, the bar isn't "summarize the disease and the trials" — it's **"build a falsifiable, numbers-backed call the way a sell-side biotech analyst would before a readout."** Concretely, the reference deck's recurring pattern is:

1. **Every slide headline is a conclusion, not a topic.** ("We think MDGL will hit NASH resolution but may be mixed on fibrosis" — not "NASH resolution overview.")
2. **Biological rationale is used to justify a specific quantitative prediction**, not just described (MRI-PDFF↔NASH-resolution correlation → predicted response rate).
3. **Phase 2→Phase 3 "bridging" is made explicit and quantified**: what changed (dose, duration, population, N) and how each change is expected to move the treatment/placebo response, built up in a bull/base/bear table.
4. **A statistical grounding wire runs through the whole deck**: powering assumptions → minimum effect size needed for significance → Monte Carlo–style probability-of-significant-readout, not just "we think it'll work."
5. **Cross-trial/competitor benchmarking is used to sanity-check assumptions** (other NASH drugs' placebo/drug response rates by trial size), not just listed as background.
6. **A dedicated "what could break the thesis" and risk section**, and a catalyst timeline.
7. **Every number is sourced** (paper, company slide, press release) — nothing is asserted without a citation trail.

The Dazodalibep analogue of each of these is mapped out in the framework below. The single hardest and most differentiating piece — and the one I'll spend the most analytical effort on — is #3/#4: **quantifying how Sjögren's-specific statistical risk (placebo response variability, ESSDAI/ESSPRI measurement properties) changes the odds of a positive readout**, which is exactly the kind of angle a generic "CD40L is a good target" essay would miss.

---

## Research & Analysis Framework — split into Primary (full) vs. Secondary (light) treatment

### Primary trial — NCT06104124 (systemic), full treatment

1. **Disease + biological rationale.** Sjögren's pathophysiology (lymphocytic infiltration of exocrine glands, ectopic germinal centers, no approved systemic therapy today), why the CD40–CD40L costimulatory axis is implicated (T cell–B cell help, germinal center/autoantibody formation), why blocking the **ligand** (dazodalibep) vs. the **receptor** (comparator: iscalimab) is a live design question, and dazodalibep's specific molecule — **corrected**: a Tn3-scaffold, Fc-free, non-antibody fusion protein (not "PASylated," an unrelated half-life-extension technology this plan originally and incorrectly used) — including *why* first-generation anti-CD40L antibodies (e.g., ruplizumab/hu5c8) were abandoned for thromboembolism and how dazodalibep's engineering avoids that specific known mechanism (platelet Fc-receptor crosslinking) without eliminating all thrombotic risk categorically. Written once; shared background for both trials. This becomes the "biological rationale" slides and directly informs the safety-risk slide.

2. **Phase 2 deep dive** (St. Clair et al., Sjögren's Ph2, published 2024) — read for both cohorts from the single paper, but the **systemic disease-activity cohort (ESSDAI-based)** is the one that bridges directly into NCT06104124 and gets the deeper effect-size/responder-analysis treatment; the symptomatic cohort's numbers are only pulled at the level needed for the secondary section below. This is the single most important input — the Ph2→Ph3 "bridge" anchor, exactly like MDGL's Ph2 MRI-PDFF/NASH-resolution data was for MAESTRO-NASH.

3. **Phase 3 design specifics for NCT06104124**, pulled verbatim from ClinicalTrials.gov and any Amgen/Horizon investor materials or ACR/EULAR posters: population/inclusion criteria, arms, N, primary/secondary endpoints as registered, statistical analysis plan/powering language if disclosed, and — importantly — verification of the actual current trial status and primary-completion date (the July 2026 completion is the premise for calling this the time-relevant trial, so it gets checked directly rather than assumed).

4. **Sjögren's-specific statistical considerations**, scoped to **ESSDAI** — the deck's statistical spine: ESSDAI measurement-property literature (known insensitivity-to-change and placebo-response issues), minimal-clinically-important-difference thresholds, and whether this Ph3 uses a newer composite responder index (e.g., CRESS, STAR) instead of classic ESSDAI. This is also the endpoint type most of the historical failed/succeeded Sjögren's trials used — part of why this trial supports the more rigorous quantitative build. Directly drives the modeling in step 7.

5. **Competitor read-through — Ianalumab (Novartis, anti-BAFF-receptor).** Different mechanism (B-cell depletion vs. T-cell costimulation blockade) but same indication and same ESSDAI-based endpoint-design problem. Pull its Ph2b dose-ranging data and the Ph3 (NEPTUNUS-1/-2) design, plus search for the specific readout news the brief's "HERE & HERE" links likely point to (Novartis press releases / CT.gov results postings), since the literal links weren't included in what was forwarded to me.

6. **Historical base-rate table** — prior ESSDAI-based systemic Sjögren's drug trials and whether they hit or missed (rituximab TEARS/TRACTISS, abatacept ASAP-III, tocilizumab, belimumab, iscalimab anti-CD40 Ph2), with their endpoints and effect sizes. Direct analogue of the reference deck's cross-trial NASH-resolution/fibrosis benchmarking table — calibrates whether a given Ph3 assumption for NCT06104124 is realistic.

7. **Full quantitative scenario modeling** — bull/base/bear tables bridging Ph2 assumptions into NCT06104124's Ph3 (adjusting for N, population/enrichment changes, placebo drift), each with implied delta/odds ratio/p-value; a minimum-detectable-effect calculation from the trial's actual N; and a probability-of-significant-readout view, built the same way the MDGL deck's Monte Carlo delta-distribution slides were.

8. **Final thesis, risks, catalysts for NCT06104124** — one explicit "positive" or "negative" call, ranked supporting evidence, the strongest counter-argument, a risk list, and a catalyst/timeline slide.

### Secondary trial — NCT06245408 (symptomatic), light treatment

- Pull its actual CT.gov design (population, N, ESSPRI-based endpoint, estimated/actual completion date) — enough for an accurate side-by-side comparison table against NCT06104124, not a full standalone deep dive.
- One section covering **how and why its risk profile differs** from the primary trial: population/enrichment differences, the ESSPRI-based (patient-reported) endpoint construct vs. ESSDAI, and the historical placebo-response literature specific to symptom-based Sjögren's endpoints (e.g., the HCQ/JOQUER-type placebo-response problem).
- A short **directional** read (not a modeled probability) on how that risk profile likely compares to the primary trial's — e.g., "more/less placebo-response risk than NCT06104124, for these reasons."
- **Explicitly out of scope for this trial:** bull/base/bear scenario table, minimum-detectable-effect calculation, dedicated competitor/historical-base-rate subsection. That analytical depth stays reserved for the primary trial.

---

## Day-by-Day Plan

*(Today is Mon 9/14; due Fri 9/18 11:00am ET — 4 working days plus a Friday-morning buffer. Note: an earlier version of this plan mislabeled today as Sunday, which implied a 5th research day that doesn't actually exist — Day 1 below now folds together what was originally split across a Sun/Mon pair, so the schedule matches the "4 working days" framing it was always meant to have.)*

### Day 1 (Mon) — Foundational research on both trials + statistical framework + competitor & historical base rates
- Pull the full ClinicalTrials.gov record for **NCT06104124** (primary): arms, N, in/exclusion criteria, primary/secondary endpoints, statistical plan text, and direct verification of its current status and July 2026 primary-completion date.
- Pull the ClinicalTrials.gov record for **NCT06245408** (secondary) at comparison-table depth: population, N, endpoint construct, estimated/actual completion date.
- Pull the Ph2 paper (St. Clair et al., both cohorts) and dazodalibep MOA sourcing (Horizon/Viela Bio patents and pipeline materials, ACR/EULAR posters, Amgen pipeline pages).
- Nail down ESSDAI measurement-property literature (MCID, known placebo-response drivers) and check whether NCT06104124 uses a composite responder index instead of classic ESSDAI.
- Research Ianalumab's Ph2b data and Ph3 (NEPTUNUS) design, and search for any topline readout news — read primarily against the ESSDAI/systemic endpoint construct.
- Build the historical Sjögren's trial success/failure table (ESSDAI-based trials).
- Draft the lightweight ESSPRI/placebo-response risk-profile note for the NCT06245408 secondary section (no modeling).
- **🔲 Checkpoint:** I present (a) confirmation of NCT06104124's status/timeline against your rationale — flagging immediately if the registry shows something different — (b) the two-trial comparison table, and (c) the statistical-risk framework plus competitor/historical tables, before building the quantitative model on top of them. This is a heavier single day than the original split, so I'll flag early if it needs to spill into Tuesday morning.

### Day 2 (Tue) — Quantitative scenario modeling + thesis formation (NCT06104124 only)
- Build bull/base/bear scenario tables for NCT06104124's primary endpoint (Ph2→Ph3 bridge assumptions, explicit like the reference deck's).
- Run the minimum-detectable-effect / power sanity check off NCT06104124's actual N.
- Draft the explicit thesis statement (positive or negative) for NCT06104124, ranked supporting evidence, and the single strongest counter-argument.
- Draft the short directional read for NCT06245408 (how its risk profile compares to the primary call).
- **🔲 Checkpoint:** I present the full analytical call in plain text/tables (pre-slide form) so we can sanity-check *the call itself* before any time goes into deck design.

### Day 3 (Wed) — Slide-by-slide content draft
- Write the full slide-by-slide outline for the **NCT06104124 primary section** (headline conclusion + bullets + table/chart spec + source line for every slide), mirroring the reference deck's structure.
- Write a condensed slide outline (roughly 3–4 slides) for the **NCT06245408 secondary section**: design-comparison table, risk-profile-differences, and the directional take — placed after the primary thesis, before risks/catalysts.
- **🔲 Checkpoint:** You review/edit the full text outline — cheapest point to fix structure, emphasis, or the thesis wording before touching PowerPoint.

### Day 4 (Thu) — Build the deck
- Python (`python-pptx`) build script producing the real `.pptx`: title, executive summary/thesis, background & MOA, Ph2 review, **NCT06104124** Ph3 design, statistical considerations, competitor benchmarking, historical base rates, scenario model, primary thesis, **NCT06245408 secondary section**, risks, catalysts, references appendix.
- Native tables/charts in the deck (matplotlib-rendered images where a chart is cleaner than a native table).
- Export a matching PDF.
- QC pass: every numeric claim traced to a source, consistent formatting/footers/page numbers, spellcheck.

### Fri AM buffer
- Final proofread, drop in your real name/title on the attribution placeholder, package the files.

---

## What you'll get at each step
- **Now:** this plan.
- **Day 1 (Mon):** two-trial comparison memo + confirmation (or correction) of NCT06104124's status/timeline + statistical-risk framework + competitor/historical-base-rate tables + the symptomatic-trial risk note.
- **Day 2 (Tue):** scenario model + the actual bull/bear thesis for NCT06104124, plus the directional read on NCT06245408, in plain text.
- **Day 3 (Wed):** full slide-by-slide text outline for both the primary and secondary sections.
- **Day 4 (Thu):** `dazodalibep_ph3_deepdive.pptx` + matching `.pdf` + a references list.
- **Fri AM:** final proofread + packaged files, ahead of the 11:00am ET deadline.

## Open items to confirm as we go
- **NCT06104124's actual current status/primary-completion date** — proceeding on your stated July 2026 completion; this gets a direct CT.gov check on Day 1 and I'll flag immediately if the registry shows something different.
- **Your name/title** for the attribution placeholder — needed by Day 4 build, can be given any time before then.

## Working style for execution (per your instruction)
No multi-day silent batch work — at each step I'll say what I'm about to research/compute and why, then show the result, before moving to the next step, so you can redirect early rather than after a big deliverable lands.
