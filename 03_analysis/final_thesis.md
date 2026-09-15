# Thesis — NCT06104124 (Primary Trial), Revised

**Revision note:** the original version of this file overstated statistical certainty
(treating a favorable variance assumption as settled), miscited ianalumab's Phase 2b
as a "failed primary endpoint," used an unsupported "population enrichment" argument
(Phase 2 Population 1 already required ESSDAI≥5 — the same floor as Phase 3 — so a
lower Phase 3 average baseline is not established by the eligibility criteria alone),
and presented a "33%/100% base rate" as if it were a probability input. All corrected
below. The directional call is unchanged; the confidence framing and supporting math
are substantially revised.

## Headline call

**We lean positive on NCT06104124's ESSDAI primary endpoint, with material
uncertainty that should not be understated.** The trial's large enrollment means it
does not need to fully replicate Phase 2's observed effect to reach significance — but
how much smaller an effect it can tolerate depends heavily on which variance
assumption is used, and the true variance for this specific Phase 3 trial is not
publicly known. This is a defensible lean, not a high-confidence prediction.

---

## Supporting evidence (ranked, corrected)

**1. Phase 2's randomized primary result is real and appropriately powered for its own
size.** ESSDAI delta −2.2 (−6.3 vs. −4.1), P=0.0167, in a trial that used a relaxed
α=0.10 threshold specifically because of small-N concerns — the primary result cleared
even the standard 0.05 bar despite that built-in caution.

**2. Pharmacodynamic evidence supports real target engagement**, separate from and
more reliable than the clinical scores: CXCL13 and rheumatoid factor were both
significantly suppressed on-drug and rebounded off-drug during the crossover. This
supports pharmacological activity — it does not, on its own, establish that the
clinical benefit is large enough to be reliably detected by ESSDAI at Phase 3 scale,
and should not be treated as proof that any future miss must be attributed to the
endpoint rather than the drug.

**3. External evidence that this disease and pathway can respond to treatment at
Phase 3 scale**: ianalumab (different mechanism, BAFF-R) actually won both of its
individual Phase 3 monthly-arm comparisons (NEPTUNUS-1 p=0.0496, NEPTUNUS-2 monthly
p=0.041) — narrowly, but really. This removes "no ESSDAI-based Phase 3 has ever
succeeded" as a reason to doubt the endpoint construct itself, while also showing that
even a real effect in this disease tends to produce a narrow, not dominant, margin.

**4. A qualitative (not statistically weighted) observation**: both CD40-pathway
trials with a comparable primary analysis (dazodalibep's continuous-ESSDAI test,
iscalimab's dose-response test) met their primary objective. This is worth noting as
context. It is not a "2-for-2, therefore X% base rate" probability input — the sample
is too small and the endpoint constructs too varied across trials to support a
computed rate. See `historical_trial_evidence.md`.

---

## Single strongest counter-argument (revised)

**The variance assumption that made this trial's cushion look large was the most
optimistic of at least three plausible ones, and the real external benchmark (the only
comparable Phase 3 trial available) points to a meaningfully larger variance.**

Using dazodalibep's own Phase 2 SEs (SD≈3.65), the trial appears comfortably powered —
even a 1.4-point effect would look highly significant. But dazodalibep's own Phase 2
protocol assumed SD=5.00 for its own planning, and the only real Phase 3 benchmark
available (NEPTUNUS-1) implies an effective SD≈5.47. Under that more conservative,
externally-anchored variance, the effect needed for 80% power rises to ~1.47 — and a
true effect of 1.4 (a plausible base case) drops from "98% conditional power" to
**"76% conditional power."** That's still favorable, but it is a meaningfully
different confidence level than the original framing conveyed, and it does not yet
account for the multiplicity correction that two active dose arms likely require,
which could push the effective bar higher still.

**Reinforcing detail, corrected**: ianalumab's own two individual Phase 3 wins
(p=0.0496, p=0.041) were both narrow — real effects in this exact disease/endpoint
combination have not, in the one available precedent, produced comfortable margins.
That is a better-grounded caution than the earlier version's generic "regression to
the mean" argument.

---

## Additional risk item, now partially mitigated: dose selection

**No empirical dose-ranging was done in Phase 2** — only one dose (1,500mg) was
tested, unlike both iscalimab and ianalumab's proper multi-dose Ph2b designs. This is
**partially, not fully, mitigated**: a population PK/PD model spanning four trials
(healthy volunteers, RA, Sjögren's) found Sjögren's patients clear the drug more
slowly than other populations, and explicitly states the proposed Phase 3 doses are
modeled to sustain exposure above the target biomarker IC50 throughout the dosing
interval. This is a real, quantitative dose-selection basis — but it supports a
*pharmacodynamic* target (biomarker suppression), not a guarantee about the resulting
*clinical* (ESSDAI) effect size. See `additional_topics.md` for the full writeup,
including the readout interpretation table and the clinical-meaning synthesis
(distinguishing statistical significance, convincing patient benefit, and acceptable
benefit-risk as three separate questions this thesis's "positive" call only answers
the first of).

---

## What was removed from the original thesis, and why

- **"Phase 3's ESSDAI≥5 entry bar is looser than Phase 2's population" — removed.**
  Phase 2 Population 1 also required ESSDAI≥5 as an eligibility criterion (per the
  paper's own methods); its enrolled population happening to average 10.7 does not
  establish that Phase 3 will enroll a different (or similar) average severity. This
  was an unsupported inference from observed mean to eligibility floor.
- **"33% historical base rate" / "100% CD40-pathway success rate" — removed as
  probability inputs.** Kept only as a qualitative observation (see above).
- **"ianalumab missed its Phase 2b primary endpoint" — corrected.** It met its actual
  primary objective (a dose-response test); only the secondary pairwise comparison
  missed significance.
- **"Same effect would yield p=0.0002" — corrected to p≈0.013** using a
  variance assumption consistent with the one real comparable trial available, instead
  of an internally-generated, more favorable variance estimate.

## New evidence added (from Phase 2 subgroup data, per Extended Data Table 1)

Systemic patients (Population 1) **without** concomitant RA/SLE had a placebo-adjusted
ESSDAI change of approximately **−1.6**; those **with** concomitant RA/SLE showed
approximately **−3.3**. Subgroup sizes are small and this should not be treated as a
robust interaction effect, but it's a more concrete, source-backed transportability
question for Phase 3 (which likely has a different RA/SLE-overlap proportion than
Phase 2's 19–24%) than the removed enrollment-size argument above.

---

## Directional read — NCT06245408 (secondary trial), corrected

**Correction: NCT06245408's registered primary outcomes include both ESSPRI change
and DASPRI change at Week 48** — not ESSPRI alone. The original secondary-trial note
only discussed ESSPRI. See the corrected `nct06245408_risk_note.md` for the
DASPRI addition; the directional lean (cautiously positive, given Population 2's own
Phase 2 result was the cleanest in the program at p=0.0002) is unchanged, but the
registered endpoint structure is now accurately described, and no assumption is made
about whether both instruments must pass, either can pass, or a hierarchy applies —
that requires the protocol, which is not public.

---

## What would change this call
- Disclosure of the actual Phase 3 statistical analysis plan (variance assumption,
  multiplicity control, testing hierarchy) — would replace the sensitivity ranges here
  with real numbers
- Any information on the enrolled population's actual baseline ESSDAI distribution
- A negative or narrow NCT06245408 readout, given the shared molecule/mechanism
- Confirmation of which figure (N=506 vs. N=504) is correct for NEPTUNUS-2, and
  resolution of similar small data-reconciliation gaps noted in `ianalumab_competitor_analysis.md`

## Sources
Synthesizes the corrected versions of: `phase2_results.md`,
`phase2_paper_explained.md`, `essdai_measurement_properties.md`,
`ianalumab_competitor_analysis.md`, `historical_trial_evidence.md`,
`nct06245408_risk_note.md`, `scenario_model.md`.
