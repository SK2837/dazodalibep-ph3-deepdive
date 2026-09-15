# Historical Sjögren's Trial Base-Rate Table — Day 1, Step 6

Cross-trial benchmark of prior randomized, controlled trials in Sjögren's, to calibrate
whether hitting on ESSDAI in NCT06104124 is a realistic bet. Direct analogue of the
MAESTRO-NASH reference deck's cross-trial NASH-resolution benchmarking table.

## Summary table

| Drug | Mechanism | Trial | N | Primary endpoint | Result |
|---|---|---|---|---|---|
| Rituximab | Anti-CD20 (B-cell depletion) | TEARS | ~120 | Composite: ≥30% improvement in ≥2 of 4 VAS scales (NOT ESSDAI) | **Missed** — numerically favored rituximab on fatigue/dryness VAS but not significant |
| Rituximab | Anti-CD20 | TRACTISS | 133 | ESSDAI / ESSPRI at Wk48 | **Missed** — SRM rituximab −0.33 vs placebo −0.13; no significant improvement |
| Abatacept | CD80/86 costim blocker (T-cell) | ASAP-III | 80 | ESSDAI at Wk24 | **Missed** — no significant difference vs. placebo at 24wks (but open-label extension to 48wks showed median ESSDAI 14.0→4.0, 50% reaching low disease activity — signal appeared once unblinded/longer duration) |
| Tocilizumab | IL-6 receptor inhibitor | ETAP | 110 | ESSDAI (and ESSPRI) | **Missed** — no significant improvement in ESSDAI or ESSPRI; only articular subgroup showed benefit |
| Belimumab | Anti-BAFF | BELISS | 30 | ESSDAI/ESSPRI (**open-label, no placebo arm**) | "Positive" (ESSDAI 8.8→5.59, p<0.0001) but **not placebo-controlled** — cannot rule out natural fluctuation/regression to mean; not a fair comparator for placebo-response risk |
| Ianalumab | Anti-BAFF-R (B-cell depletion) | Ph2b (NCT02962895) | 190 | ESSDAI at Wk24 | **Missed** at every dose (best case 300mg: diff −1.92, p=0.0921); placebo arm (−6.39) outperformed 2 of 3 drug doses. **But went on to Phase 3 success** (NEPTUNUS-1/2, see `ianalumab_competitor_analysis.md`) |
| **Iscalimab** | **Anti-CD40 (receptor blocker)** | TWINSS Ph2b | 273 | ESSDAI at Wk24, dose-response | **Hit** — 150mg diff −3.0, 600mg diff −2.9, both p<0.005; dose-response p=0.004 |
| **Dazodalibep** | **Anti-CD40L (ligand blocker)** | Ph2 (NCT04129164) | 74 (systemic cohort) | ESSDAI at Day 169 | **Hit** — diff −2.2, p=0.0167 |

## The single most important pattern in this table

**Every CD40-pathway trial to date has hit its ESSDAI primary endpoint in Phase 2 —
both the ligand-blocking approach (dazodalibep) and the receptor-blocking approach
(iscalimab).** Every other mechanism tested against classic ESSDAI (anti-CD20, IL-6
inhibition, T-cell costimulation via CD80/86, first-generation anti-BAFF-R) has missed
its primary ESSDAI readout in a genuine placebo-controlled setting — the sole possible
exception, ianalumab, only succeeded in the *second-generation, larger* study
(Phase 3, after missing Phase 2b at the same endpoint).

This is a real, citable, mechanism-specific base-rate uplift argument for
NCT06104124: it isn't just "CD40/CD40L biology is plausible" — it's "the CD40/CD40L
pathway specifically already has a 2-for-2 record on this exact endpoint construct in
Sjögren's," a materially better track record than the ESSDAI base rate as a whole.

## Naive base rate (for the probability model)

Excluding TEARS (different endpoint construct) and BELISS (no placebo arm, not a fair
comparator): of the 6 genuinely comparable randomized, placebo-controlled, ESSDAI-primary
Phase 2/2b trials in this table (TRACTISS, ASAP-III, ETAP, ianalumab Ph2b, iscalimab Ph2b,
dazodalibep Ph2), **2 of 6 (33%) hit their primary endpoint** — but both hits are the
CD40-pathway drugs. Restricting the reference class to "CD40/CD40L-pathway drugs
specifically" gives 2 of 2 (100%, small-sample). The honest read for modeling: the
overall ESSDAI base rate is unfavorable (~33%), but the mechanism-specific base rate is
the more relevant prior for dazodalibep specifically, and it's much better.

## Caveats to carry into the Day 2 model
- Small sample sizes throughout (N as low as 2 for the mechanism-specific base rate) —
  don't over-claim precision; frame this as a qualitative uplift, not a hard probability multiplier.
- Ph2→Ph3 track record is genuinely mixed even within a single mechanism: ianalumab
  missed Ph2b then won Ph3. This argues against assuming a Ph2 hit guarantees a Ph3 hit
  — NCT06104124's Ph3 win is not a foregone conclusion just because Ph2 hit.
- ASAP-III's story (missed double-blind primary, but strong open-label extension) is a
  reminder that ESSDAI's insensitivity can produce false negatives within a trial's
  primary window even when the drug plausibly works — cuts in dazodalibep's favor as
  a risk to flag, not a certainty.

## Sources
- TEARS: Devauchelle-Pensec et al., Ann Intern Med 2014 (PMID 24727841)
- TRACTISS: primary trial publication + SRM data (Ann Rheum Dis)
- ASAP-III: van Nimwegen et al., Lancet Rheumatology (primary + OLE phase)
- ETAP: Felten et al. (ScienceDirect/ACR abstract)
- BELISS: ACR abstracts / Ann Rheum Dis open-label Ph2 publication
- Ianalumab Ph2b: NCT02962895 results (ClinicalTrials.gov, verified directly)
- Iscalimab TWINSS: ACR abstract + Lancet 2024 (PMID 39096929)
- Dazodalibep Ph2: St. Clair et al., Nature Medicine 2024 (verified directly, see `phase2_results_verified.md`)
