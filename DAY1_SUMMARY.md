# Day 1 Recap — In Plain English

This explains, in simple terms, everything we did today, how we got the data, and
what it sets up for Day 2.

## The big picture
The job (a take-home test for a Jefferies healthcare equity research role) is to
predict whether Amgen's drug dazodalibep will pass or fail its two big Phase 3 trials
in Sjögren's disease, and back that prediction up with real evidence — the same way a
stock analyst would before a big drug-trial result comes out. Day 1's job was pure
fact-finding: gather every piece of real evidence we'll need before we're allowed to
start making the actual prediction. Nothing got predicted or modeled yet — that's Day 2.

Everything below got saved as its own file in the project folder, so none of it is
sitting only in chat history.

---

## Step 1: What is dazodalibep and why should it work at all?
**What we did:** Explained the disease (Sjögren's = immune system attacks your
tear/saliva glands) and the biology behind why this specific drug might treat it
(it blocks a "go-ahead" signal called CD40L that T-cells use to tell B-cells to keep
making harmful antibodies). We also covered why an older generation of similar drugs
got abandoned in the 2000s (they caused blood clots) and how dazodalibep is built
differently to avoid that problem.
**How we got this:** General scientific/medical background knowledge — no data pull
needed, this is textbook immunology.
**File:** covered in chat, no separate file (background/context only).

## Step 2: Did the drug actually work in its first, smaller trial?
**What we did:** Found and read the actual published scientific paper reporting
dazodalibep's Phase 2 (early-stage) trial results, and pulled the real numbers instead
of trusting a second-hand summary.
**How we got this:** You already had the actual paper saved as a PDF in your project
folder. We opened it directly and read the results tables ourselves, rather than
relying on a web search summary (which we caught getting one detail wrong earlier —
a good reminder that primary sources beat secondhand ones).
**Key finding:** The drug showed a real, statistically meaningful improvement in the
main disease-activity score, though a secondary "did the patient clearly respond"
measure was murkier — an early hint of a bigger theme covered in Step 4.
**File:** `phase2_results_verified.md`

## Step 3: What exactly are the two big trials testing, and are they finished yet?
**What we did:** Looked up the official government registration for both of Amgen's
big trials (the ones actually being judged in this test) to get the real facts: who's
allowed to join, how many patients, what's being measured, and — most importantly —
whether the trial has actually finished yet, since we were told to double-check
rather than assume.
**How we got this:** ClinicalTrials.gov is the U.S. government's official public
registry where every clinical trial legally has to post its details. We queried it
directly (its public data feed) rather than reading it through a search engine, so we
got the exact, current, official numbers.
**Key finding:** One of the two trials had already fully finished (results just not
announced publicly yet) — this was a real surprise that changed how we should talk
about the trial's status in the deck.
**Files:** `NCT06104124.csv/.xlsx`, `NCT06245408.csv/.xlsx`

## Step 4: Is the "ruler" used to measure success actually any good?
**What we did:** Investigated the specific scoring system (called ESSDAI) both trials
use to decide "did the drug work." Checked whether it has known weaknesses, what
counts as a "real" improvement vs. noise, and whether Amgen used an older or newer
version of this scoring system.
**How we got this:** Searched published medical-research literature (scientific
journal articles about the scoring system itself, not about any one drug) to find
established facts: the accepted threshold for a meaningful improvement, and a
mathematical model researchers built showing how much people getting a fake
(placebo) treatment improve anyway just from chance/expectation.
**Key finding:** This scoring system has a real, documented history of being
"insensitive" — good drugs have failed trials using it before, not necessarily
because the drug didn't work, but because the ruler wasn't good at detecting it.
Confirmed Amgen is using the older, classic version of the ruler, not a newer improved
one — a real risk worth flagging.
**File:** `essdai_measurement_properties.md`

## Step 5: How does this compare to the competition?
**What we did:** Researched a rival drug (ianalumab, made by Novartis) that treats
the same disease through a different biological mechanism, to use as a benchmark.
**How we got this:** Combined the same government trial registry lookups (for design
facts) with general web searches for news coverage and the drug company's own official
press releases and medical-conference presentation (for actual results).
**Key finding — the big one:** The rival drug already announced real, positive
results from its own big trial a year ago — the first successful trial of its kind in
this disease ever. But the numbers show it barely passed (just barely below the usual
statistical cutoff for "significant"), and the effect was actually smaller than what
dazodalibep already showed in its own early trial. This cuts both ways: it proves a
trial like this CAN succeed, but also shows that even a "win" here tends to be a
close call, not a landslide.
**File:** `ianalumab_competitor_analysis.md`

## Step 6: What's the track record for this whole category of trials?
**What we did:** Looked up six other past drug trials in this same disease, using the
same or similar scoring systems, to see how often they've actually succeeded or failed
historically.
**How we got this:** Web searches for each individual trial's published results
(these are all trials from the last ~10 years that already fully reported their
findings, so this was just fact-gathering from existing public medical literature).
**Key finding — genuinely useful:** Most past trials using this scoring system have
failed, regardless of drug type — except trials for drugs that work through the exact
same biological pathway as dazodalibep, which have a perfect track record so far. That's
a real, meaningful pattern favoring dazodalibep specifically, not just wishful thinking.
**File:** `historical_base_rate_table.md`

## Step 7: A lighter check on the second, smaller trial
**What we did:** For the second trial (the one testing symptom relief rather than
whole-body disease activity), did a shorter version of the same kind of check — is its
particular scoring system prone to the same placebo problem, and what does history say.
**How we got this:** One more web search for the classic example trial in this
specific area, cross-referenced against the same Phase 2 paper from Step 2.
**Key finding:** This second trial actually looks somewhat safer from the placebo
problem than the first one, based on its own earlier trial data being the strongest,
cleanest result in the whole program.
**File:** `nct06245408_esspri_risk_note.md`

---

## How we made sure the information is trustworthy
A few times during today's work, we caught a web-summarizing tool getting a number or
a status wrong (once inventing a plausible-sounding but false "trial completed today"
detail, once garbling a placebo-response relationship backwards). Every time that
happened, we went back to the actual original source — the real government database,
the real published paper, the real company press release — and double-checked the
number by hand before trusting it. Every fact in these six files has been checked
against its original source at least once, not just pulled from a search summary.

## Where everything lives
All seven files above are sitting in your project folder as plain text (Markdown)
files, each with its own sources listed at the bottom. Nothing important is only in
this chat — if this conversation gets cleared or summarized, the files stay put and
are self-explanatory on their own.

---

## What's next: moving into Day 2

Day 1 was entirely about **collecting real evidence**. Day 2 is about **turning that
evidence into an actual prediction** — the part the test is really graded on. Here's
what Day 2 will do with each piece we gathered today:

1. **The Phase 2 numbers** (`phase2_results_verified.md`) become the starting point —
   the "known" result we're trying to project forward into the bigger trial.
2. **The measurement-system risks** (`essdai_measurement_properties.md`) tell us how
   much to discount or adjust that projection — since we now know the scoring system
   can understate a drug's real effect, and we have an actual formula for how much
   the "fake treatment" group tends to improve on its own depending on how sick
   patients are at the start.
3. **The competitor result and historical track record** (`ianalumab_competitor_analysis.md`,
   `historical_base_rate_table.md`) become reference points for what a "realistic"
   effect size looks like in this disease and this scoring system, and what odds this
   type of trial has historically had of succeeding.
4. **Putting all of that together**, Day 2 will build three scenarios — an optimistic
   case, a middle-of-the-road case, and a pessimistic case — each with an actual
   predicted number for how much better the drug will look than the fake treatment,
   and how likely that is to count as a statistically real result given how many
   patients are in the trial. That will lead to one clear final verdict: do we think
   this trial is going to pass or fail, and why — which is the actual deliverable this
   whole test is asking for.

In short: today we made sure every fact we'll use in the prediction is real, sourced,
and double-checked. Tomorrow (Day 2) is where we actually do the math and make the call.
