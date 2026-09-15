# The Whole Project, Explained Simply

This walks through everything done so far — what we were trying to figure out, what
we found, what we actually did to find it, and what assumptions we had to make along
the way — in plain English, no clinical or statistics background required.

**Correction notice (added after an external review caught several errors in this
project):** two factual mistakes in the original version of this file are fixed below
— only one of the two trials has actually finished, not both, and the two trials use
different measuring sticks, not the same one. A few other overstated conclusions
elsewhere in this document (about a competing drug's early trial result, and about how
confident to be in the statistics) have also been corrected. See the individual
technical files for the full detail on each correction.

---

## The question we're trying to answer

A company called Amgen makes a drug called **dazodalibep**. It's being tested as a
treatment for **Sjögren's disease** — an illness where the body's immune system
mistakenly attacks the glands that make tears and saliva, causing severe dryness,
fatigue, and pain. There's currently no approved medicine that treats the root cause
of this disease, only things that ease the symptoms.

Amgen is running two big, final-stage tests of this drug (called "Phase 3 trials") to
see if it actually works well enough to get approved. **Correction: only one of the
two has actually finished** collecting its data (the one testing whole-body disease
activity) — its results just haven't been announced publicly yet. The second trial
(testing day-to-day symptoms) is still active and not expected to finish until later
this year. Both facts matter, so it's worth being precise about which trial is at
which stage rather than treating them as interchangeable.

**Our job:** predict, using everything publicly available, whether these trials are
going to come back as a "win" (the drug clearly worked) or a "loss" (it didn't), and
explain exactly why — the same way a stock analyst tries to predict an earnings result
before the company announces it.

---

## Part 1: What we found (the research)

### The disease and why this drug might work
Sjögren's disease involves immune cells called T-cells and B-cells "teaming up" in a
harmful way — T-cells send B-cells a "go ahead" signal (via something called CD40L)
telling them to keep producing harmful antibodies. Dazodalibep is designed to block
that signal. An older generation of similar drugs was abandoned in the 2000s because
it caused blood clots, but dazodalibep is engineered differently to try to avoid that
problem. (Full explanation in earlier chat, not a separate file.)

### The first, smaller trial (Phase 2) already happened, and we found real data
Before running the two big trials, Amgen ran a smaller test first. We read the actual
published scientific paper reporting those results (not a summary — the real paper),
saved locally as a PDF. Key things we learned:
- The drug showed a real, statistically meaningful improvement in the main
  disease-activity measurement for one group of patients, and an even cleaner result
  for a second group of patients with different symptoms.
- Blood tests showed the drug was doing exactly what the underlying science predicted
  (reducing specific markers tied to the disease process) — solid proof the drug
  is biologically active, not just a fluke.
- One safety concern came up: one patient had a blood clot and a liver problem, and the
  study doctors did officially link both to the drug — worth being upfront about, not
  brushing under the rug.
- The study only tested one dose of the drug, and used a slightly relaxed statistical
  bar for calling a result "real" (more on that below), which are both worth keeping
  in mind.
*(Files: `phase2_paper_explained.md`, `phase2_results.md`,
`phase2_baseline_characteristics.md`)*

### The two big trials' actual design and status
We looked up the official government registry (ClinicalTrials.gov) — the place every
US clinical trial is legally required to post its details — to get the real facts
about both big trials: who's allowed to join, how many patients, exactly what's being
measured, and whether they're actually finished yet.

Surprise finding: one of the two trials had **already fully finished** months ago —
just without any public announcement of the results yet. This mattered a lot, because
it meant we were no longer looking at "a trial that's coming up," we were looking at
"a trial that's done, we're just waiting to hear the answer."
*(Files: `NCT06104124.csv/.xlsx`, `NCT06245408.csv/.xlsx`)*

### Is the measuring stick any good?
**Correction: the two trials actually use different measuring sticks, not the same
one.** The first (already-finished) trial grades success using a doctor-scored
checklist called **ESSDAI**. The second trial grades success using **two different
patient-reported measures** — a one-time symptom questionnaire and a daily symptom
diary — because it's testing day-to-day symptoms rather than whole-body disease
activity. We researched whether the doctor-scored checklist (ESSDAI) is actually
reliable, and found it has a real,
documented history of problems: even genuinely effective drugs have "failed" trials
that used this scoring system before, likely because the system isn't very sensitive —
patients who got a fake (placebo) treatment often score better anyway, just by chance
or expectation, which shrinks the gap between "real drug" and "fake drug" scores and
makes it harder to prove the real drug worked.
*(File: `essdai_measurement_properties.md`)*

### What happened to similar drugs from other companies (corrected)
We researched every other drug that's been tested for this same disease, going back
about 10 years. **Correction: our first pass at this drew too strong a conclusion.**
These past trials didn't all grade success the same way — some used the doctor-scored
checklist, some used a completely different patient-symptom yardstick, and one used a
mix of several rules combined. Because they're not really measuring the same thing,
you can't fairly stack them up into one "most failed, but this one type always
succeeds" scorecard the way we initially did. What's still fair to say: the two drugs
using the same biological approach as dazodalibep (blocking the same signal, from
either side) both technically hit their own early-trial goals — worth noting as a
mildly encouraging pattern, not as a proven track record, since it's only two data
points measured in different ways.

One of those competitor drugs (made by a different company, a different approach)
already announced a real, positive result from its own big trial about a year ago —
genuinely useful, since it's proof this kind of trial *can* succeed. **Correction: we
also initially got that competitor's own earlier, smaller trial result wrong** — we'd
said it "failed," when it actually hit its own stated goal (a more technical statistical
test than a simple pass/fail on one number). And when its big trial did succeed, the
win was narrow both times it ran the trial — not a landslide. That's a useful,
more honest data point: a real effect in this disease, when it exists, may look like a
close call rather than an obvious win.
*(Files: `historical_trial_evidence.md`, `ianalumab_competitor_analysis.md`)*

---

## Part 2: What we actually did (the process)

1. **Read the real source documents ourselves**, rather than trusting quick summaries.
   A few times, a tool we used to summarize a webpage got a detail wrong (once
   inventing a plausible-but-false detail, once describing a relationship backwards).
   Every time that happened, we went back to the original document and corrected it by
   hand before trusting the number.

2. **Pulled official data directly from primary sources**: the government trial
   registry's own data feed, the actual scientific paper (not a review of it), and
   official company press releases and medical-conference presentations — rather than
   relying on news articles about news articles.

3. **Cross-checked our own predictions against a real example.** Rather than just
   guessing how the small early trial's results might change in the bigger trial, we
   found one real case (the competitor drug mentioned above) where this exact kind of
   jump — small trial to big trial, same disease, same scoring system — already
   happened, and used the actual, real change in numbers from that case to sanity-check
   our own math, adjusting our estimate accordingly.

4. **Did the actual math**, using the real numbers gathered: how many patients are in
   the trial, how much natural random noise to expect, and what size of a result would
   actually count as "statistically real" given how many people were tested.

5. **Built three future scenarios** — an optimistic case, a middling case, and a
   pessimistic case — each with real numbers attached, rather than just saying "it
   could go well or it could go badly."

---

## Part 3: The assumptions we had to make (and why)

Nobody can know a trial's real result in advance — so any prediction has to rest on
assumptions. Being upfront about these matters as much as the conclusion itself:

- **We assumed the three treatment groups in the big trial have roughly equal numbers
  of patients.** The government registry doesn't disclose the exact split, so we
  divided the total evenly as our best guess.

- **We estimated how much natural variation to expect in patient scores** based on
  numbers reported in the small early trial — but the small trial used a more
  complex statistical method, so our estimate is a reasonable approximation, not an
  exact figure.

- **Correction — we no longer assume this.** An earlier version of this summary assumed
  the big trial's average starting patient would be less severely affected than the
  small early trial's, because we thought the big trial's entry rule was more lenient.
  On double-checking, the small early trial actually used the exact same minimum entry
  rule — it just happened to enroll somewhat sicker patients than that minimum required.
  So there's no real basis yet for assuming the big trial's patients will be more or
  less severely affected on average; we genuinely don't know until enrollment details
  are published, and we've removed the assumption rather than guess.

- **We now use a range of guesses for "how much natural noise to expect,"** instead of
  picking just one. Our first attempt used the most optimistic of three reasonable
  guesses, which made the prediction look more solid than it should have. Using a more
  cautious guess (based on how much a very similar competitor drug's real big trial
  actually varied) still points the same direction, but with a noticeably smaller
  safety margin than we first described.

- **We assumed the small early trial's own "positive" result won't hold up perfectly
  in the bigger trial** — bigger, more spread-out trials often show smaller effects
  than small early trials did, a well-known pattern in medical research (sometimes
  called "regression to the mean" — basically, small early results tend to be a bit
  lucky, and later, bigger tests bring the number back down closer to the true
  average). We used the one real comparable example we found to estimate roughly how
  much smaller the effect might get, rather than guessing blindly.

- **We assumed this one comparable example is a fair guide**, even though the bigger
  trial we're predicting is scaling up by a much larger amount than that example did.
  This is genuinely the single weakest link in the whole prediction, and we said so
  directly rather than hiding it.

- **We assumed the trial's official rule for "did the drug work" is simply whether the
  statistical result is unlikely to be due to chance** (specifically, less than a 5%
  chance it's a fluke — the standard scientific bar), matching how the trial was
  actually registered, rather than requiring the improvement to feel like a big deal
  to patients day-to-day. **One thing we can't account for**: the big trial is
  actually testing two different doses of the drug against one shared comparison
  group, which usually means the "5% chance" bar gets stricter to keep the overall
  odds of a false alarm the same — but the company hasn't published exactly how much
  stricter, so our numbers may be a bit more optimistic than the trial's real rule.

---

## Part 4: Where this landed (softened after correction)

Putting it all together, our current best guess is:

**We lean toward thinking the bigger of the two trials will come back as a real
success — but this is a lean, not a confident prediction, and an earlier version of
this document overstated how sure we could be.** The main reason for leaning positive
is simple: this trial has enough patients that it doesn't need to fully repeat the
small early trial's improvement to count as a real, provable result. But exactly how
much smaller an improvement it can tolerate and still pass depends on a guess we can't
fully pin down (how much natural noise to expect) — using a more cautious version of
that guess, the safety margin is real but noticeably smaller than we first described.

**But there's one real, specific reason this could still fail**, and it's worth taking
seriously rather than dismissing: the one real comparable example we found for "what
happens to a drug's results when you go from a small trial to a much bigger one"
involved a much smaller jump in size than this trial is making. If the drug's true
benefit shrinks by a lot more than that example showed — which is plausible precisely
because this trial is scaling up so much further — the result could land in the range
where this same disease's tricky scoring system has swallowed real effects before,
in several other companies' past trials.

**For the second, smaller trial** (testing a different group of patients, focused more
on day-to-day symptoms than whole-body disease activity), we're leaning positive too,
and slightly more confident — because its own early small trial produced the single
cleanest, most convincing result out of the entire research program so far.

---

## A note on how confident to be in this whole document
This is a reasoned, evidence-based prediction — not a certainty. Every real number
used here traces back to an official source (government trial registry, published
paper, company announcement), and every assumption is written out explicitly above so
it can be argued with or adjusted. If new information comes out (for example, if the
company announces results before this analysis is finished, or if more details about
who actually enrolled in the big trial become public), this prediction should be
revisited rather than treated as fixed.
