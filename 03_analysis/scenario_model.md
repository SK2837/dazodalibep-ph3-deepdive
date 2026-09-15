# Day 2 — Statistical Model: NCT06104124 Primary Endpoint (ESSDAI)

**Major revision note:** the original version of this file (a) used a single,
optimistic variance assumption without testing sensitivity to alternatives, (b)
conflated "assumed true effect" with "actual p-value," presenting a table of
hypothetical scenarios as if they were forecasts, (c) contained a scaling error that
understated ianalumab's implied p-value by two orders of magnitude, and (d) did not
account for multiple comparisons (two active doses vs. one placebo) or missing data.
Corrected below.

## Three distinct quantities — kept separate this time

1. **Observed significance threshold**: the delta needed to be "statistically
   significant" in a single trial, given its size and a variance assumption.
2. **Effect associated with a given power level**: the true delta that would produce
   an 80% or 90% probability of a significant result *if the trial were repeated many
   times* — a property of the design, not a prediction of any single outcome.
3. **Predictive probability of trial success**: requires integrating over uncertainty
   in the true effect, the true variance, dose performance, missing data, and the
   multiple-comparison correction — this file does not compute this number, because
   the inputs needed to do so honestly are not publicly available.

A single point estimate of "the true delta is X" does not exist before the readout.
Everything below is conditional on stated assumptions, not a forecast of what will
happen.

## Variance sensitivity — the central correction

The original model used SD≈3.65, backed out from dazodalibep's own Phase 2 SEs. Two
other variance assumptions are directly relevant and were omitted:
- **The dazodalibep Phase 2 protocol's own planning assumption used SD=5.00** (per the
  paper's methods) — larger than the SD≈3.65 implied by the observed Phase 2 SEs.
- **NEPTUNUS-1's reported SE (≈0.66 at ~137/arm) implies an effective two-group SD≈5.47**
  — the only real external benchmark available for this specific endpoint/population
  combination.

None of these is the actual (undisclosed) Phase 3 variance for dazodalibep. Presenting
only the most favorable one (3.65) as if it were settled was the core problem with the
original model.

**Sensitivity table** (independent-normal approximation, one active-dose-vs-placebo
comparison, per-arm n≈217 unless noted):

| Variance assumption | Per-arm n | Two-sided α | Effect for 80% power | Conditional power if true benefit = 1.4 |
|---|---:|---:|---:|---:|
| Original model, SD 3.65 | 217 | 0.05 | 0.98 | 98% |
| Phase 2 planning assumption, SD 5.00 | 217 | 0.05 | 1.34 | 83% |
| Competitor-based effective SD 5.47 (NEPTUNUS-1) | 217 | 0.05 | 1.47 | 76% |
| Same, illustrative stricter α (multiplicity) | 217 | 0.025 | 1.62 | 66% |
| Same, illustrative missing-data/information loss | 184 | 0.025 | 1.76 | 58% |

**Observed-significance threshold at SE≈0.35 (the original model's SD=3.65 case):** a
delta of about **0.69** reaches p<0.05 — not the 1.0 figure loosely used as "the MDE"
in earlier versions of this file. 0.98 is specifically the delta needed for *80%
power*, a different quantity than the bare significance threshold.

**A true effect of 0.7 does not guarantee a pass** — under the SD=3.65 assumption it
produces roughly a coin-flip probability of reaching significance in any single trial,
not a certainty. Conditional power tables describe probabilities across repeated
trials, not the outcome of the one trial that will actually happen.

## Corrected ianalumab-based calculation

The earlier version of this file claimed "an ianalumab-sized 1.3-point effect would
produce p=0.0002 in dazodalibep's larger trial." This used the SD=3.65 assumption,
which is inconsistent with the variance ianalumab's own Phase 3 actually exhibited.
Recalculated using NEPTUNUS-1's own implied variance, scaled only for dazodalibep's
larger assumed N:

SE_scaled = 0.66 × √(137/217) ≈ 0.524
At delta = 1.3: z ≈ 2.48, **two-sided p ≈ 0.013** — a real pass, but not the dramatic
p=0.0002 previously claimed. The "structural size advantage" argument is directionally
correct (a larger trial does help) but was overstated in magnitude by using an
unrealistically low variance assumption.

## The actual success rule is not fully known

NCT06104124 has **two active dose arms** compared against one shared placebo. This
means:
- There are at least two dose-vs-placebo comparisons, which raises a multiplicity
  question (family-wise error control) unless a specific testing hierarchy or
  alpha-splitting scheme is used.
- The registered outcome measures do not disclose whether the trial uses a
  hierarchical gatekeeping procedure, a fixed alpha split, or some other multiplicity
  control — the Statistical Analysis Plan is not publicly available.
- The illustrative α=0.025 row above represents one simple possibility (splitting
  0.05 evenly across two doses) — it is **not** an assertion about Amgen's actual
  statistical plan, which remains unknown.

Any single "the trial will pass/fail" statement needs to carry this caveat: the
multiplicity-adjusted significance bar could be meaningfully stricter than a naive
single-comparison 0.05 threshold, depending on the undisclosed testing hierarchy.

## Scenario table — relabeled as illustrative assumptions, not forecasts

The bull/base/bear framing below describes **assumed true effect sizes**, each checked
against the SD=5.47 (competitor-based) sensitivity row as the more conservative,
externally-anchored variance assumption, rather than the original SD=3.65:

| Scenario | Assumed true delta | SE (SD=5.47, n=217) | z | Two-sided p | Read |
|---|---|---|---|---|---|
| Bull | 2.0 | 0.524 | 3.82 | <0.001 | Would pass clearly if true |
| Base | 1.4 | 0.524 | 2.67 | ≈0.008 | Would pass, with real but not enormous margin |
| Bear | 0.6 | 0.524 | 1.15 | ≈0.25 | Would not reach significance if true |

These are **assumed inputs, not predicted outcomes** — the actual true effect is
unknown, and the weights below are explicitly the analysts' qualitative judgment, not
an empirically estimated probability distribution.

**Illustrative weights (analyst judgment only):** Bull ~20% / Base ~50% / Bear ~30%.
These numbers describe subjective confidence, not a computed or validated probability
model, and should not be presented in a final deck as if they were.

## What a single real comparable transition (ianalumab) can and cannot tell us

Ianalumab's Ph2b→Ph3 transition (dose-response test met in Ph2b; both Phase 3 monthly
arms individually significant but narrow, p=0.0496 and p=0.041) is the only real
external data point available for "what happens to a Sjögren's ESSDAI effect going
from a smaller trial to a larger one in this disease." It is informative context, but
**one transition cannot causally calibrate how much dazodalibep's specific,
much-larger enrollment scale-up (74→651, ~8.8×, versus ianalumab's ~1.4×) will affect
its own effect retention.** Any adjustment based on this single precedent should be
treated as a qualitative sanity check, not a quantitative multiplier applied with
false precision.

## What this file no longer claims
- No "minimum detectable effect" is presented as a single fixed number — it depends on
  which variance assumption is used, shown as a range (0.98–1.76 depending on
  assumptions).
- No scenario table cell is presented as an actual forecasted p-value for the real
  trial — each is conditional on an assumed true effect that is not known.
- No probability of trial success is computed — doing so honestly would require
  integrating over effect, variance, dose, missing-data, and multiplicity uncertainty,
  none of which is fully specified by public information.

## Sources / methodology notes
- SD=5.00: dazodalibep Phase 2 protocol's own planning assumption (per paper methods)
- SD≈5.47: backed out from NEPTUNUS-1's reported SE≈0.66 at ~137/arm
- SD≈3.65: backed out from dazodalibep's own Phase 2 observed SEs (the original,
  most-favorable assumption — retained here only as one row in the sensitivity table,
  not as the headline number)
- Allocation ratio (~217/arm) assumes roughly equal 3-way split; not confirmed by
  ClinicalTrials.gov, which does not disclose randomization ratio or the testing
  hierarchy across the two dose arms
- See `ianalumab_competitor_analysis.md` for the corrected ianalumab-based calculation
  and its sourcing
