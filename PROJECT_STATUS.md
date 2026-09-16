# Project Status — The Full Story, In Plain English

*Last updated: September 15, 2026*

This document explains the entire project so far — from what the disease is, to
exactly what was researched each day, to what the numbers mean, to why the final
answer leans positive — written so that someone with no medical or statistics
background can follow every step. Wherever a technical term shows up, it's explained
right there, the first time it's used.

If you only read one document to understand this project cold, read this one.

---

## 1. What is this project, in one paragraph?

A pharmaceutical company called **Amgen** makes a drug called **dazodalibep**. It's
being tested as a treatment for an autoimmune disease called **Sjögren's disease**,
where the body's own immune system mistakenly attacks the glands that make tears and
saliva — causing severe dry eyes, dry mouth, fatigue, and joint/muscle pain. There is
currently **no approved medicine that treats the actual disease** — only things that
ease the dryness symptoms (eye drops, saliva substitutes). Amgen has finished (or is
finishing) two large, final-stage clinical trials of dazodalibep. This project's job
is to predict — using only publicly available evidence, before the company announces
anything — whether those trials will come back as a genuine success or not, and to
explain exactly why, the same way a stock market analyst predicts an earnings result
before a company reports it.

---

## 2. The disease and the drug — why would this even work?

### What's going wrong in the body
In Sjögren's disease, two types of immune cells — **T-cells** and **B-cells** — end up
working together in a harmful way. Normally, T-cells "approve" B-cells to start
producing antibodies (proteins that fight off real infections). In Sjögren's, this
approval process goes into overdrive inside the tear and saliva glands, and the
B-cells end up producing harmful antibodies that attack the person's own tissue. Over
time, little clusters of this runaway immune activity build up inside the glands —
almost like tiny, misplaced lymph nodes — and they keep fueling the disease.

### The specific signal being blocked
The "approval" T-cells give B-cells happens through a specific molecular handshake:
a protein called **CD40L** (found on the T-cell) plugs into a matching socket called
**CD40** (found on the B-cell). Once that handshake happens, the B-cell gets the
green light to multiply and start pumping out antibodies. Block that handshake, and
the theory is you calm down the disease at its source, not just its symptoms.

Two ways exist to interrupt this handshake:
- **Block the plug** (CD40L) — this is dazodalibep's approach.
- **Block the socket** (CD40) — this is the approach of a competing drug called
  iscalimab, made by a different company (Novartis). Either approach, if it works,
  should produce the same outcome: no more "green light" reaching the B-cell.

### Why dazodalibep is built the way it is
Dazodalibep is **not a normal antibody drug**. It's an engineered protein built on
something called a **Tn3 scaffold** — think of it as a small, purpose-built molecular
clip designed to grab onto CD40L, with no "antibody tail" (called an Fc region)
attached to it. This detail matters a lot, for a specific historical reason:

**In the early 2000s, a first generation of CD40L-blocking drugs was abandoned**
because they caused dangerous blood clots. The reason: those drugs *were* normal
antibodies, and CD40L also happens to sit on the surface of blood-clotting cells
(platelets). The antibody's tail could accidentally grab onto multiple platelets at
once and stick them together, causing clots. Because dazodalibep has no antibody tail
at all, it's specifically engineered to avoid triggering that exact mechanism. That
doesn't mean zero risk of any blood clot ever (see the safety section below — one did
occur in the small early trial), but it does mean the *specific, well-understood*
mechanism that killed off the first generation of these drugs shouldn't apply the same
way to this one.

---

## 3. Day 1 — What we researched, step by step, in plain terms

Day 1's whole job was **fact-finding**: gathering every real, sourced piece of
evidence needed before making any kind of prediction. Nothing was predicted yet — that
came in Day 2.

### Step 1: Did the drug actually show any effect in its first, smaller test?
Before running the two big trials, Amgen ran a smaller early trial (called "Phase 2")
on about 180 patients total, split into two groups:
- **Group 1** ("systemic" patients): people whose disease was affecting their whole
  body, not just dryness — joints, organs, blood tests, etc.
- **Group 2** ("symptomatic" patients): people whose main problem was day-to-day
  symptoms (dryness, fatigue, pain) without much whole-body organ involvement.

Each group was randomly split again into "real drug" and "fake drug" (placebo)
sub-groups, and neither the patients nor the doctors scoring them knew who got which
— this is called a **double-blind, placebo-controlled** design, and it's the gold
standard for proving a real effect, because it removes wishful thinking from the
result.

**What "the score went down" actually means**: both groups were graded using scoring
systems that work like a checklist — a higher number means worse disease, so an
improvement means the number went *down*.
- **ESSDAI** = a doctor-filled checklist scoring how active the disease looks across
  different organs (used for Group 1).
- **ESSPRI** = a patient-filled questionnaire about pain, fatigue, and dryness (used
  for Group 2).

**The actual results:**
- **Group 1 (ESSDAI)**: the real-drug patients' score dropped by 6.3 points on
  average; the fake-drug patients' score dropped by 4.1 points. So real drug patients
  did about 2.2 points better than fake-drug patients. Statisticians ran the numbers
  and found there was only about a **1.7% chance** this 2.2-point gap happened purely
  by random luck (this "chance it's a fluke" number is called a **p-value** — smaller
  is better, and under 5% is the normal bar for "this is probably real").
- **Group 2 (ESSPRI)**: real-drug patients improved by 1.8 points; fake-drug patients
  improved by only 0.5 points — a 1.3-point gap, with only a **0.02% chance** this was
  a fluke. This was actually the single cleanest, most convincing result in the whole
  early trial.

**But not everything was clean.** When researchers checked "how many patients hit a
specific improvement target" (rather than just the average score), the real-drug
group didn't clearly beat the fake-drug group by enough to rule out chance. This
matters — it's an early hint of a bigger problem covered in Step 3 below.

### Step 2: Blood tests that back up the story
Beyond the symptom scores, doctors also checked blood markers tied directly to the
disease process:
- A marker called **CXCL13** (a chemical signal that helps build those harmful immune
  clusters inside the glands) dropped sharply in drug-treated patients, and bounced
  back up when the drug was stopped.
- **Rheumatoid factor**, a type of harmful antibody, was also significantly reduced by
  the drug.

This matters because it's **independent proof the drug is doing exactly what the
science predicted** — not just proof that a symptom score moved, which could
theoretically happen for other reasons.

**A safety note, stated precisely**: one patient in the early trial developed a blood
clot and a liver problem, and the trial doctors did officially link both to the drug.
The important nuance: this happened 180 days *after* the last dose — well outside the
window you'd expect if the mechanism were the same platelet-clumping problem that
killed off the first generation of similar drugs (described in Section 2 above). One
other patient in the trial developed a breast cancer diagnosis that doctors also
linked to the drug, and one patient died of COVID-19 complications (considered
unrelated to the drug). All of this needs to be reported honestly in a final deck — a
small early trial with a handful of serious events like this doesn't prove or disprove
anything on its own, but it shouldn't be glossed over either.

### Step 3: Is the "ruler" used to measure success actually a good ruler?
This is one of the most important — and least obvious — things this project dug into.
The ESSDAI scoring system (the doctor checklist) has a real, documented history of
being **not very sensitive** — meaning even drugs that probably work have "failed"
past trials using this exact scoring system, likely because:
- Patients getting the **fake** treatment often improve anyway, just from natural
  ups-and-downs of the disease, or from the extra medical attention that comes with
  being in a trial. This is called the **placebo effect**, and it shrinks the gap
  between "real drug" and "fake drug" scores, making a real effect harder to prove.
- Researchers even built an actual mathematical formula, based on many past trials,
  showing how much the fake-drug group tends to improve depending on how sick the
  patients were to begin with — the sicker the starting point, the bigger the fake
  improvement tends to be, purely because there's more room to naturally fluctuate
  downward.

This is a genuine risk baked into the disease and the scoring system itself, not
something specific to Amgen's drug — and it means a "failed" result in a big trial
doesn't necessarily mean the drug doesn't work; it could mean the ruler wasn't
sensitive enough to detect a real, smaller effect.

### Step 4: What happened when other companies tried this?
We researched every other drug tested for this disease over roughly the last 10
years, to build a track record. Two important, carefully-verified findings:

1. **The two drugs that block this exact same signal** (dazodalibep, blocking one
   side, and iscalimab, blocking the other side) **both technically achieved their
   own early-trial goals.** That's a modest, genuinely encouraging pattern — though
   with only two data points, it's a hint, not a proven law.
2. **A different competing drug (ianalumab, made by Novartis, using a totally
   different mechanism) already ran its own big final-stage trial and reported real,
   positive results about a year ago.** This is hugely useful, because it's actual,
   real-world proof that this kind of trial *can* succeed in this disease — it's not
   just theory. But — and this took careful double-checking to get right — **both
   times that drug "won," the win was narrow, not a landslide** (explained with exact
   numbers in Day 2 below). That's an important, honest data point: even a real
   effect in this disease might not produce an obvious, easy win.

We also researched a second registered outcome measure for the smaller trial
(explained in Step 5) and confirmed exactly how strict a statistical bar the original
small trial used, and a few other technical facts corrected during a later review
pass (documented throughout the individual research files, not repeated here in full).

### Step 5: A closer look at the second, smaller trial
Amgen's second big trial (the one testing day-to-day symptoms rather than whole-body
disease activity) actually grades success using **two separate measurements**, not
just one: the ESSPRI questionnaire mentioned above, plus a second tool called
**DASPRI** — a daily symptom diary patients fill in repeatedly, rather than a
one-time questionnaire at a doctor visit. This is a real, material detail: a diary
tool has different risks (people might skip days, for example) than a one-time
questionnaire, and nobody outside the company knows yet whether both tools need to
show a positive result, or just one, for this trial to count as a win.

---

## 4. Day 2 — Turning the research into an actual prediction

Day 1 gathered evidence. Day 2's job was to **do the math** and land on an actual
call: will the big trial pass or fail?

### The key question: how big does the effect need to be?
The big trial (NCT06104124, the systemic/whole-body one) has **651 patients** — about
nine times more than the 74 patients in the small early trial's matching group. More
patients in a trial generally makes it **easier to prove a real effect exists**, even
if that effect is smaller than what the early trial showed. The technical question is:
exactly how much smaller an effect can this bigger trial still detect and call
"real"?

To answer that, you need to know how much natural, random up-and-down "noise" to
expect in patient scores. This is the single trickiest, most important judgment call
in the whole model, and — importantly — **there isn't one universally agreed-upon
number for it.** We tested three different, reasonable estimates instead of just
picking the most convenient one:

| Which estimate | Where it comes from | How big an effect the trial needs to reliably detect it |
|---|---|---|
| The rosiest estimate | Backed out from the small early trial's own numbers | About 1 point |
| The company's own estimate | What Amgen itself assumed when originally planning the small early trial | About 1.3 points |
| The most realistic outside check | Backed out from the one real comparable trial that already happened (the competitor drug, ianalumab) | About 1.5 points |

**Why three numbers instead of one matters**: an earlier version of this analysis
used only the rosiest estimate, which made the whole prediction look far more
confident than it should have. Using the more realistic, externally-checked number
still supports a positive lean — it just means the safety margin is real, but smaller
and more honest than first described.

### Bull, base, and bear — what these words mean and the actual numbers
Because nobody can know the trial's real result in advance, three different "what if"
scenarios were built, using the more realistic effect-size estimate above:

- **Bull case** ("everything goes well"): imagine the true effect is a healthy 2.0
  points. Under this assumption, the trial would pass with a p-value under 0.1% —
  an extremely comfortable, clear win.
- **Base case** ("the most likely middle-ground guess"): imagine the true effect is a
  more modest 1.4 points — smaller than what the small early trial showed, accounting
  for the fact that positive early results often shrink somewhat once tested in a
  much bigger, more spread-out trial (a well-known pattern in medical research called
  **regression to the mean** — small early results tend to be a little lucky, and
  bigger follow-up tests bring the number back down closer to the true average).
  Under this assumption, the trial would still pass, with roughly a **0.8% chance**
  it's a fluke — a real, meaningful pass, though not an overwhelming one.
- **Bear case** ("things go poorly"): imagine the true effect shrinks a lot further,
  down to just 0.6 points. Under this assumption, the trial would **not** reach the
  normal bar for statistical significance — there'd be roughly a **1-in-4 chance**
  the whole thing is just noise, which is far too risky to call a real result.

**Important honesty check**: these three numbers are not measured predictions of what
will actually happen — they're illustrative "what if" inputs, stress-tested to see
how the trial's result would look under each assumption. Nobody knows today which of
these (if any) is the truth. Based on all the evidence gathered, a rough personal
judgment call was made about how likely each scenario is: about a **1-in-5 chance**
of the bull case, a **1-in-2 chance** of the base case, and a **roughly 1-in-3
chance** of the bear case. This weighting is a considered opinion, not a scientifically
computed probability — it's explicitly labeled as a judgment call everywhere it's
used, so it can be challenged or adjusted.

### So... why does the final answer lean positive?

Putting all of Day 1 and Day 2's evidence together, here is the actual reasoning,
ranked from strongest to weakest:

1. **The math has real breathing room.** Because the big trial has so many patients,
   it doesn't need anywhere close to the small early trial's full 2.2-point
   improvement to count as a genuine success — even the more cautious, realistic
   "base case" estimate (1.4 points, meaningfully smaller than what was already shown)
   still passes comfortably.

2. **The blood test evidence is independent proof the drug is biologically doing
   something real** — separate from the symptom scores, which are known to be a
   noisier, less sensitive way to measure this disease (see Step 3 above). This makes
   "the drug doesn't actually work" a less likely explanation for any future miss.

3. **A very similar competing drug already proved this exact kind of trial can
   succeed in this disease** — real-world evidence, not just theory — and the current
   drug's own early results were already stronger than what carried that competitor
   through its own big trial.

4. **Both drugs sharing this drug's specific biological approach (blocking either
   side of the same signal) have, so far, cleared their own early testing goals** — a
   small but genuinely encouraging pattern.

### The single strongest reason this could still fail

Being honest about the biggest real risk matters as much as the reasons for optimism.
**The one real comparable example available — the competing drug's own jump from a
small trial to a big one — only involved a modest increase in the size of the specific
group being compared (about 2.9 times bigger). This drug's jump is meaningfully larger
(about 6 times bigger).** *(Correction: an earlier version of this document compared
the wrong numbers — total trial size instead of the specific group size that actually
matters for the statistics — which made the gap look far more dramatic, 8.8× vs. 1.4×,
than it really is. The honest comparison is 6× vs. 2.9×: still a real, meaningful
difference, just not as extreme as first stated.)* There's no real precedent for what
happens to a drug's effect when the jump in trial size is that much larger. If the
true effect shrinks by more than what happened to that one comparable example, the
result could land in the exact danger zone where several other past trials in this
same disease have seen a real effect disappear into statistical noise. This is a
specific, checkable risk — not a vague worry — and it's the fair, honest counterweight
to the positive lean above.

### The second, smaller trial (day-to-day symptoms)
This one gets a lighter, less mathematically detailed treatment by design. The
takeaway: **lean positive here too, with slightly more confidence than the big
trial**, because its own small early result (the 1.3-point ESSPRI improvement
mentioned in Step 1) was the single cleanest, most convincing number in the entire
early-trial program. The trade-off: this trial's scoring tools (the ESSPRI
questionnaire and the DASPRI diary) are both entirely based on what patients say they
feel, with no doctor-measured or blood-test anchor at all — which historically makes
this kind of measurement even more exposed to the placebo effect described in Step 3.
This trial also hasn't finished collecting its data yet, unlike the big trial, so its
result will likely become known later.

---

## 5. What is the "reference deck," and how are we using it?

Jefferies supplied a real, finished example of this exact kind of analysis — a deck
one of their own analysts wrote predicting a completely different drug's (a fatty
liver disease treatment) trial result, before it was announced. It's not the topic to
copy — it's a **style and rigor template**.

**What we borrowed from it:**
- Every slide making an actual point/conclusion in its title, not a vague label.
- Building an explicit "what changed between the small trial and the big trial" table
  with real numbers, rather than hand-waving about it.
- Presenting three scenarios (bull/base/bear) with real numbers attached to each,
  rather than just saying "it could go well or badly."
- Cross-checking assumptions against other, similar real-world trials rather than
  inventing numbers out of thin air.
- Naming one specific "here's the strongest reason we could be wrong" rather than a
  vague list of risks.

**What we added or did differently:**
- Testing three different "how much natural noise to expect" assumptions instead of
  picking one — the reference deck used a single number for its size assumption.
- Being explicit about which numbers this project is *not* able to calculate (like an
  overall single percentage chance of success) because the necessary confidential
  company information isn't public — the reference deck's original author had more
  company-disclosed information to work with for its own drug.
- Treating blood-test/biological evidence as a separate check on *why* a future miss
  might happen (bad ruler vs. bad drug), which wasn't as necessary for the reference
  deck's drug since its own measurement tool was already a lab test.

---

## 6. What's left to do

The actual science and statistics work described above is essentially complete. Two
small, genuine research loose ends remain (writing down the biological-rationale
explanation as its own saved file, and pulling one specific missing data point about
the second trial's diary-based measurement), but nothing close to a full new research
cycle. The large remaining task is building the actual PowerPoint presentation from
everything already gathered — turning the research above into slides, tables, and
charts — which has not yet started.

---

## 7. Does this cover what Jefferies actually asked for?

| What they asked for | Where it stands |
|---|---|
| A clear, explicit "will it pass or fail" call | ✅ Done — see Day 2 above |
| Explanation of the biology and why the drug should work | ✅ Covered here, though it should also live as its own separate file |
| Analysis of the early small trial | ✅ Done in detail |
| Explanation of what's unique about the two big trials' designs, and the statistics involved | ✅ Done |
| Lessons learned from other companies' trials | ✅ Done, double-checked for accuracy |
| Sourced, traceable numbers throughout | ✅ Done — every number traces back to a real source, documented in a master evidence file |
| An actual PowerPoint file | ❌ Not started yet |

**Bottom line**: the thinking and the evidence are done and have already been
independently checked once for mistakes. What's left is turning it into slides.
