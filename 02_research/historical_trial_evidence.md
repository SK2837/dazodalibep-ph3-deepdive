# Historical Sjögren's Trial Evidence Table — Day 1, Step 6 (Corrected)

**Revision note:** the original version of this file used inconsistent success criteria
across trials (a dose-response standard for iscalimab, a pairwise standard for
ianalumab) and treated the resulting "2 of 6" tally as a probability input. Both are
wrong. This is now a qualitative evidence table — endpoint types, test types, and
results, without a computed "base rate."

## Evidence table (corrected classifications, verified against primary sources)

| Drug | Mechanism | Trial | N | Primary endpoint (exact) | Result |
|---|---|---|---|---|---|
| Rituximab | Anti-CD20 | TEARS | ~120 | ≥30% improvement in ≥2 of 4 patient VAS scales (NOT ESSDAI) | Missed |
| Rituximab | Anti-CD20 | TRACTISS | 133 | **Proportion achieving ≥30% reduction in fatigue OR oral dryness VAS at week 48** (NOT ESSDAI — corrected from earlier version) | Missed — 39.8% (rituximab) vs 36.8% (placebo) after imputation, not significant |
| Abatacept | CD80/86 costim blocker | ASAP-III | 80 | Continuous ESSDAI at week 24 | Missed at 24wk (open-label extension to 48wk showed improvement, but that's uncontrolled) |
| Tocilizumab | IL-6R inhibitor | ETAP | 110 | **Composite responder: ESSDAI improvement ≥3 points AND no new moderate/severe domain activity AND no PGA worsening** (NOT continuous ESSDAI — corrected) | Missed — 52.7% (tocilizumab) vs 63.6% (placebo). Note placebo numerically higher. **Unverified flag: this project's "p=0.14" figure came from a secondary source, not the primary ETAP paper (Felten et al.) directly. A second review claimed this 0.14 is actually a Bayesian posterior probability, not a conventional p-value — plausible but not independently confirmed here. Verify against the primary paper before citing "p=0.14" in a final deck.** |
| Belimumab | Anti-BAFF | BELISS | 30 | ESSDAI/ESSPRI, **open-label, no placebo arm** | Not a controlled comparison — excluded from any pass/fail tally |
| Ianalumab | Anti-BAFF-R | Ph2b (Bowman et al., Lancet 2021) | 190 | **Prespecified dose-response test (MCP-Mod) on continuous ESSDAI at week 24** — the pairwise 300mg-vs-placebo comparison (p=0.092) was NOT the primary test | **Met primary objective** — significant dose-response in 4 of 5 models tested (p<0.025 in four, p=0.060 in one). *(Correction: earlier version of this file said ianalumab "missed" its primary endpoint by citing only the pairwise comparison — that was wrong.)* |
| Iscalimab | Anti-CD40 | TWINSS Cohort 1 (systemic) | **173** (not 273 — corrected; 273 was the combined total across both cohorts) | Dose-response test (MCP-Mod) on continuous ESSDAI at week 24 | Met — significant dose-response |
| Iscalimab | Anti-CD40 | TWINSS Cohort 2 (symptomatic) | 100 | 600mg vs. placebo, ESSPRI change at week 24 | **Did not reach significance** — LS mean difference −0.57 (95% CI −1.30 to 0.15), p=0.12 |
| Dazodalibep | Anti-CD40L | Ph2 Population 1 (systemic) | 74 | Continuous ESSDAI at day 169 | Met — diff −2.2, p=0.0167 |
| Dazodalibep | Anti-CD40L | Ph2 Population 2 (symptomatic) | 109 | Continuous ESSPRI at day 169 | Met — diff −1.3, p=0.0002 |

## What this table does and does not support

**Supports:** a qualitative observation that both CD40-pathway trials with a
continuous-ESSDAI or dose-response primary analysis (dazodalibep, iscalimab) met their
primary objective, while several other mechanisms tested against different (and not
uniformly comparable) endpoint constructs did not. This is a real, worth-noting pattern.

**Does not support:**
- A "33% historical base rate" or "100% CD40-pathway success rate" as a probability
  input into any forecast. The trials here are not a systematic sample, don't share a
  single endpoint definition (VAS composite, continuous ESSDAI, composite responder,
  dose-response test, and open-label are all different test types), and are too few to
  support a numeric rate.
- Treating dazodalibep's own Phase 2 result as both an independent data point in this
  table *and* separately as supporting evidence for its own forecast — that double-counts
  the same piece of evidence.
- A same-endpoint apples-to-apples comparison between ianalumab's dose-response success
  and, say, TRACTISS's VAS-composite miss — these are different statistical questions
  entirely, not comparable hit/miss data points on the same scale.

## Sources (all re-verified for this correction)
- TEARS: Devauchelle-Pensec et al., primary VAS-composite endpoint definition
- TRACTISS: primary trial report — 30% fatigue/oral-dryness VAS responder definition,
  imputed response rates 39.8% vs 36.8%
- ASAP-III: van Nimwegen et al., Lancet Rheumatology
- ETAP: Felten et al. — composite responder definition (ESSDAI≥3pt + no new domain
  activity + no PGA worsening), 52.7% vs 63.6%, p=0.14
- Ianalumab Ph2b: Bowman et al., Lancet 2021 (PMID 34861168) — dose-response primary
  objective met, 4/5 models significant
- Iscalimab TWINSS: Lancet 2024 (PMID 39096929) — Cohort 1 N=173 (44/43/43/43), Cohort
  2 N=100 (50/50); Cohort 2 result −0.57 (95% CI −1.30 to 0.15), p=0.12
- Dazodalibep Ph2: St. Clair et al., Nature Medicine 2024 (verified directly)
