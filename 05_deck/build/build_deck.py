#!/usr/bin/env python3
"""Build the dazodalibep Phase 3 deep-dive deck (26 slides) from
final_slide_content.md. All numbers below are transcribed verbatim from
that file (and its cited sources) -- nothing here is invented or smoothed.
"""
import os
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

from deck_lib import (
    new_deck, blank_slide, set_bg, add_text, add_title, add_footer, add_notes,
    add_bullets, add_numbered, callout_box, card_box, add_picture_fit, add_table,
    NAVY, TEAL, GRAY, LIGHT, RED, GOLD, WHITE, DARK, RED_TINT, GOLD_TINT,
    TEAL_TINT, GRAY_TINT, FONT, PAGE_W, PAGE_H, L, R, CW, TITLE_TOP, BODY_TOP,
    FOOTER_TOP, LEFT_W, RIGHT_X, RIGHT_W,
)

ASSETS = os.path.join(os.path.dirname(__file__), "assets")

prs = new_deck()

# =====================================================================
# SLIDE 1 -- Title
# =====================================================================

def slide_01():
    s = blank_slide(prs)
    set_bg(s, WHITE)
    add_text(s, "Dazodalibep in Sjögren’s disease:", L, 2.0, CW, 1.0,
             size=32, color=NAVY, bold=True)
    add_text(s, "forecasting the Phase 3 readout, and what could move it",
             L, 2.75, CW, 1.0, size=32, color=TEAL, bold=True)
    add_text(s, "Clinical deep dive on Amgen’s Phase 3 program", L, 4.0, CW, 0.5,
             size=17, color=GRAY, italic=True)
    bullets = [
        "Primary forecast: NCT06104124 — systemic disease activity",
        "Supporting assessment: NCT06245408 — symptom burden",
        "Analysis cutoff: September 15, 2026",
        "Prepared by: Sai Adarsh Kasula, Data Scientist / Biostatistician",
    ]
    add_bullets(s, bullets, L, 4.6, CW - 1.0, 2.0, size=16,
                color=DARK, bullet_char="–", gap_after=8)
    add_text(s, "Source: Jefferies assignment brief.", L, FOOTER_TOP, CW, 0.4,
             size=10, color=GRAY, italic=True)
    add_notes(s, "I focus the quantitative forecast on the systemic trial, as "
              "permitted by the brief, and use the symptomatic study to assess "
              "how far the evidence extends across the program.")
    return s

# =====================================================================
# SLIDE 2 -- Executive conclusion
# =====================================================================

def slide_02():
    s = blank_slide(prs)
    add_title(s, "We expect NCT06104124 to meet its ESSDAI primary endpoint, "
              "with meaningful residual risk")
    items = [
        ("Direct clinical evidence: ", "Phase 2 showed a −2.2-point adjusted "
         "ESSDAI difference at day 169; p=0.0167."),
        ("Biological coherence: ", "CD40L blockade reduced immune biomarkers "
         "(CXCL13, RF); iscalimab provides additional pathway evidence."),
        ("Confirmatory precedent: ", "ianalumab demonstrated that week-48 ESSDAI "
         "benefit can be detected in Phase 3."),
    ]
    add_numbered(s, items, L, BODY_TOP, CW, 2.15, size=15.5, gap_after=10)
    callout_box(s, L, 3.85, CW, 0.85, "MAIN RISK",
                "A smaller week-48 effect combined with higher variance or "
                "stricter multiplicity testing could turn an encouraging signal "
                "into a negative primary result.", body_size=13.5)
    data = [
        ["Forecast", "Conclusion", "Basis / boundary"],
        ["Systemic trial", "Expect positive", "Qualitative analyst forecast; "
         "stress-tested below"],
        ["Symptomatic trial", "Positive ESSPRI lean", "DASPRI and full "
         "success-rule uncertainty limit conviction"],
    ]
    add_table(s, data, L, 4.95, CW, 1.55, col_widths=[18, 22, 60], font_size=13,
              header_size=13, row_heights=[0.5, 0.55, 0.5])
    add_notes(s, "My positive call comes from the evidence as a whole. Larger "
              "enrollment improves precision; it does not establish that the "
              "drug will retain its Phase 2 effect.")
    add_footer(s, "03_analysis/final_thesis.md; analyst assessment. No "
               "numerically calibrated program probability is claimed.", "02")
    return s

# =====================================================================
# SLIDE 3 -- Define the question
# =====================================================================

def slide_03():
    s = blank_slide(prs)
    add_title(s, "The program tests two distinct clinical questions at week 48")
    data = [
        ["", "Systemic: NCT06104124", "Symptomatic: NCT06245408"],
        ["Clinical focus", "Moderate-to-severe systemic activity",
         "High symptoms with limited systemic activity"],
        ["Core eligibility", "ESSDAI ≥5", "ESSPRI ≥5; ESSDAI <5"],
        ["Enrollment", "651", "434"],
        ["Primary outcomes", "ESSDAI change from baseline",
         "ESSPRI AND DASPRI change from baseline"],
        ["Primary assessment", "Week 48", "Week 48"],
        ["Status", "Completed, primary completion 2026-07-23",
         "Active, not recruiting; primary completion est. 2026-10-22"],
        ["This presentation", "Full efficacy forecast",
         "Directional supporting assessment"],
    ]
    add_table(s, data, L, BODY_TOP, CW, 4.55, col_widths=[20, 40, 40],
              font_size=12.5, header_size=13,
              row_heights=[0.5, 0.62, 0.5, 0.42, 0.58, 0.42, 0.62, 0.5],
              banding=GRAY_TINT)
    add_text(s, "“Positive” means success under the prespecified primary "
             "testing procedure. Statistical significance, clinical importance, "
             "and benefit-risk are assessed separately.", L, 6.32, CW, 0.6,
             size=13, italic=True, color=NAVY)
    add_notes(s, "Two outcomes listed as primary do not, by themselves, tell us "
              "whether both must pass or a hierarchy applies. I do not infer "
              "that rule from the registry labels.")
    add_footer(s, "01_data/NCT06104124.csv, 01_data/NCT06245408.csv. Full "
               "eligibility/testing details require the protocol, not "
               "available publicly.", "03")
    return s

# =====================================================================
# SLIDE 4 -- Disease and endpoint distinction
# =====================================================================

def slide_04():
    s = blank_slide(prs)
    add_title(s, "Reducing systemic activity and improving dryness, fatigue and "
              "pain are related — but separate — tests")
    add_bullets(s, [
        ("ESSDAI: ", "clinician-assessed systemic disease activity across "
         "weighted organ domains."),
        ("ESSPRI/DASPRI: ", "patient-reported dryness, fatigue, and pain."),
        ("", "Symptoms can reflect several processes; immune suppression need "
         "not produce the same benefit in every domain."),
    ], L, BODY_TOP, CW, 1.7, size=15.5, lead_bold_split=True, gap_after=8)

    # Venn-style overlap diagram
    diag_top = 3.35
    diag_h = 2.9
    left_c = card_box(s, L, diag_top, 5.6, diag_h, fill=NAVY)
    right_c = card_box(s, PAGE_W - R - 5.6, diag_top, 5.6, diag_h, fill=TEAL)
    overlap = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(PAGE_W / 2 - 1.55),
                                  Inches(diag_top + 0.55), Inches(3.1), Inches(diag_h - 1.1))
    overlap.fill.solid()
    overlap.fill.fore_color.rgb = GRAY
    overlap.line.fill.background()
    overlap.shadow.inherit = False
    from pptx.oxml.ns import qn
    sp = overlap.fill.fore_color._xFill.find(qn('a:srgbClr'))
    alpha = sp.makeelement(qn('a:alpha'), {'val': '55000'})
    sp.append(alpha)
    tf = overlap.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "Partial overlap\n(not equivalent)"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = WHITE
    r.font.name = FONT

    add_text(s, "Systemic activity", L + 0.3, diag_top + 0.22, 5.0, 0.4,
             size=17, color=WHITE, bold=True)
    add_bullets(s, ["Joint / musculoskeletal", "Glandular / hematologic",
                     "Cutaneous, renal, pulmonary", "Clinician-scored domains"],
                L + 0.3, diag_top + 0.75, 2.55, 1.9, size=12.5, color=WHITE, gap_after=6)

    add_text(s, "Patient symptoms", PAGE_W - R - 5.3, diag_top + 0.22, 5.0, 0.4,
             size=17, color=WHITE, bold=True, align=PP_ALIGN.RIGHT)
    add_bullets(s, ["Dryness (eyes, mouth)", "Fatigue", "Pain",
                     "Patient-reported diary/questionnaire"],
                PAGE_W - R - 2.85, diag_top + 0.75, 2.55, 1.9, size=12.5,
                color=WHITE, gap_after=6)

    add_notes(s, "The two populations should not be reduced to ‘reversible’ "
              "versus ‘irreversible’ disease. Residual gland function may "
              "matter — Population 2’s Phase 2 precursor required residual "
              "stimulated salivary flow ≥0.1 mL/min — but fatigue and pain are "
              "not simply measurements of gland damage.")
    add_footer(s, "02_research/phase2_baseline_characteristics.md. The "
               "gland-function point is clinical interpretation, not proven "
               "explanation.", "04")
    return s

# =====================================================================
# SLIDE 5 -- Biological rationale
# =====================================================================

def slide_05():
    s = blank_slide(prs)
    add_title(s, "CD40L blockade interrupts immune-cell costimulation "
              "implicated in Sjögren’s disease")
    add_picture_fit(s, os.path.join(ASSETS, "slide5_mechanism.png"), L, 1.55,
                     CW, 3.55, align="center")
    add_bullets(s, [
        ("CD40L–CD40 signaling ", "supports T-cell/B-cell interactions and "
         "downstream immune activation."),
        ("Dazodalibep blocks the ligand ", "(CD40L); iscalimab targets the "
         "receptor (CD40)."),
        ("Fc-free Tn3-scaffold design ", "is engineered to avoid the "
         "Fc-mediated platelet-crosslinking mechanism implicated in "
         "first-generation anti-CD40L antibody thromboembolism."),
    ], L, 5.25, CW, 1.65, size=13, gap_after=5)
    add_notes(s, "The mechanism establishes plausibility. The randomized "
              "clinical results are the direct test of efficacy; "
              "pharmacodynamic data help establish whether the expected "
              "biology is engaged.")
    add_footer(s, "PROJECT_STATUS.md Section 2; 02_research/phase2_results.md "
               "(Tn3 scaffold, not “PASylated”).", "05")
    return s

# =====================================================================
# SLIDE 6 -- Phase 2 design
# =====================================================================

def slide_06():
    s = blank_slide(prs)
    add_title(s, "Phase 2 provides two randomized efficacy tests, followed by "
              "a blinded treatment switch")
    add_picture_fit(s, os.path.join(ASSETS, "slide6_timeline.png"), L, 1.5,
                     CW, 2.15, align="center")
    data = [
        ["", "Population 1", "Population 2"],
        ["Randomized N", "74", "109"],
        ["Dazodalibep / placebo", "36 / 38", "54 / 55"],
        ["Core entry criteria", "ESSDAI ≥5",
         "ESSPRI ≥5, ESSDAI <5, stimulated flow ≥0.1 mL/min"],
        ["Primary outcome", "ESSDAI change, day 169", "ESSPRI change, day 169"],
        ["Stage I completion", "71/74", "102/109"],
    ]
    add_table(s, data, L, 3.85, CW, 2.15, col_widths=[24, 30, 46], font_size=11.5,
              header_size=12, row_heights=[0.34, 0.32, 0.32, 0.5, 0.34, 0.32],
              banding=GRAY_TINT)
    add_text(s, "One IV regimen — 1,500mg every 2 weeks for 3 doses, then every "
             "4 weeks for 4 doses. No dose-ranging in this Sjögren’s study.",
             L, 6.12, CW, 0.5, size=12.5, italic=True, color=NAVY)
    add_notes(s, "The strongest evidence is the prespecified randomized first "
              "period. The crossover is supportive, with carryover and "
              "time-related limitations.")
    add_footer(s, "02_research/phase2_paper_explained.md, "
               "02_research/phase2_results.md.", "06")
    return s

# =====================================================================
# SLIDE 7 -- Systemic primary result
# =====================================================================

def slide_07():
    s = blank_slide(prs)
    add_title(s, "Dazodalibep produced greater ESSDAI improvement than placebo "
              "in Phase 2")
    data = [
        ["Day-169 change", "Dazodalibep", "Placebo"],
        ["Adjusted mean ± SE", "−6.3 ±0.6", "−4.1 ±0.6"],
    ]
    add_table(s, data, L, BODY_TOP, LEFT_W, 1.05, col_widths=[46, 27, 27],
              font_size=15, header_size=14.5, align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT},
              row_heights=[0.5, 0.55])
    callout_box(s, L, 2.85, LEFT_W, 1.45, "ADJUSTED DIFFERENCE: −2.2 POINTS",
                "Reported 90% CI approximately −3.6 to −0.7; p=0.0167. "
                "This is a 90% CI — not the 95% CI used elsewhere in this deck.",
                fill=TEAL_TINT, border=TEAL, label_color=TEAL, body_size=13)
    add_bullets(s, [
        "The prespecified primary result supports systemic efficacy.",
        "The trial used two-sided α=0.10 (small-N caution); this result also "
        "clears standard 0.05.",
        "Small sample size leaves uncertainty about the reproducible effect.",
    ], L, 4.55, LEFT_W, 2.2, size=13, gap_after=8)
    # right-side note panel (no chart asset for this slide; table above mirrors paper)
    card_box(s, RIGHT_X, BODY_TOP, RIGHT_W, 5.0, fill=GRAY_TINT)
    add_text(s, "READING THE EVIDENCE", RIGHT_X + 0.22, BODY_TOP + 0.22, RIGHT_W - 0.5, 0.35,
             size=12, bold=True, color=NAVY)
    add_bullets(s, [
        "Higher ESSDAI = worse disease; a larger negative change = more "
        "improvement.",
        "Both arms improved from baseline — the placebo arm’s own "
        "−4.1-point drop reflects the known placebo-response pattern in "
        "this endpoint.",
        "The 90% CI excludes zero, consistent with the reported p=0.0167.",
        "N-at-risk and the full ESSDAI trajectory (paper Fig. 2a) are not "
        "reproduced numerically here beyond the day-169 readout above.",
    ], RIGHT_X + 0.22, BODY_TOP + 0.65, RIGHT_W - 0.44, 4.2, size=12, gap_after=10)
    add_notes(s, "This is evidence against the null under the trial's analysis. "
              "The p-value is not a 1.7% probability the result is a fluke, "
              "nor does it establish the study's power.")
    add_footer(s, "02_research/phase2_results.md.", "07")
    return s

# =====================================================================
# SLIDE 8 -- Consistency and limitations
# =====================================================================

def slide_08():
    s = blank_slide(prs)
    add_title(s, "Responder and subgroup results support a cautious "
              "interpretation of the systemic signal")
    add_text(s, "EXHIBIT A — DAY-169 RESPONSE", L, BODY_TOP, LEFT_W, 0.3,
             size=12, bold=True, color=NAVY)
    dataA = [
        ["Improvement threshold", "DAZ", "Placebo", "p-value"],
        ["≥3 ESSDAI points", "26/36; 72.2%", "22/37; 59.5%", "0.3283"],
        ["≥4 ESSDAI points", "24/36; 66.7%", "18/37; 48.6%", "0.1823"],
        ["≥5 ESSDAI points", "61.1%", "35.1%", "0.0449;\npost hoc"],
    ]
    add_table(s, dataA, L, BODY_TOP + 0.32, LEFT_W, 1.9, col_widths=[33, 22, 22, 23],
              font_size=11.5, header_size=11,
              align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT, 3: PP_ALIGN.RIGHT},
              row_heights=[0.45, 0.43, 0.43, 0.59])
    card_box(s, L, 4.5, LEFT_W, 1.55, fill=GOLD_TINT)
    add_text(s, "EXHIBIT B", L + 0.18, 4.62, LEFT_W - 0.4, 0.28, size=11, bold=True, color=GOLD)
    add_text(s, "Exploratory adjusted difference without RA/SLE ≈−1.6; with "
             "RA/SLE ≈−3.3. Small subgroup Ns.", L + 0.18, 4.9, LEFT_W - 0.4, 1.05,
             size=12.5, color=DARK)
    add_text(s, "exploratory, small N", L + 0.18, 5.7, LEFT_W - 0.4, 0.3, size=10.5,
             italic=True, color=GOLD)

    add_text(s, "ON-SLIDE TAKEAWAY", RIGHT_X, BODY_TOP, RIGHT_W, 0.3, size=12,
             bold=True, color=NAVY)
    add_text(s, "Directionally favorable results do not establish a robust "
             "responder effect or a treatment-by-subgroup interaction.",
             RIGHT_X, BODY_TOP + 0.4, RIGHT_W, 1.1, size=14, italic=True, color=DARK)
    card_box(s, RIGHT_X, 3.15, RIGHT_W, 3.0, fill=GRAY_TINT)
    add_text(s, "Bars show n/N, not just %, to keep small-sample denominators "
             "visible — e.g. 26/36 (72.2%) vs. 22/37 (59.5%) at the ≥3-point "
             "threshold. None of the three dichotomized thresholds reaches "
             "significance at the prespecified level; only the post hoc "
             "≥5-point cut does.",
             RIGHT_X + 0.2, 3.4, RIGHT_W - 0.4, 2.5, size=12.5, color=DARK, line_spacing=1.15)
    add_notes(s, "Nonsignificant responder outcomes do not prove a faulty "
              "endpoint — dichotomizing loses information and the sample is "
              "small.")
    add_footer(s, "02_research/phase2_results.md.", "08")
    return s

# =====================================================================
# SLIDE 9 -- Symptom evidence
# =====================================================================

def slide_09():
    s = blank_slide(prs)
    add_title(s, "The symptom cohort showed a broad signal across dryness, "
              "fatigue and pain")
    add_text(s, "EXHIBIT — POPULATION 2, DAY 169", L, BODY_TOP, LEFT_W, 0.3,
             size=12, bold=True, color=NAVY)
    data = [
        ["Outcome", "DAZ change", "Placebo change", "p-value"],
        ["ESSPRI total — primary", "−1.80", "−0.53", "0.0002"],
        ["Dryness", "−1.9", "−0.8", "0.0066"],
        ["Fatigue", "−1.7", "−0.3", "0.0022"],
        ["Pain", "−1.8", "−0.4", "0.0010"],
    ]
    add_table(s, data, L, BODY_TOP + 0.32, LEFT_W, 2.15, col_widths=[36, 22, 24, 18],
              font_size=12, header_size=11.5,
              align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT, 3: PP_ALIGN.RIGHT},
              row_heights=[0.46, 0.45, 0.42, 0.42, 0.42],
              cell_shades={(1, 0): TEAL_TINT, (1, 1): TEAL_TINT, (1, 2): TEAL_TINT, (1, 3): TEAL_TINT})
    callout_box(s, L, 4.85, LEFT_W, 1.15, "PRIMARY ENDPOINT CONTRAST",
                "Adjusted total-score contrast −1.27; 90% CI −1.82 to −0.73. "
                "This is a 90% CI, consistent with Slide 7.", fill=TEAL_TINT,
                border=TEAL, label_color=TEAL, body_size=13)

    card_box(s, RIGHT_X, BODY_TOP, RIGHT_W, 5.0, fill=GRAY_TINT)
    add_text(s, "READING THE EVIDENCE", RIGHT_X + 0.2, BODY_TOP + 0.2, RIGHT_W - 0.4, 0.32,
             size=12, bold=True, color=NAVY)
    add_bullets(s, [
        "All four rows favor dazodalibep, and the primary ESSPRI-total result "
        "is the strongest p-value in the whole Phase 2 program.",
        "Directional consistency across dryness, fatigue and pain supports "
        "read-through beyond the single total score.",
        "Domain-level tests (dryness/fatigue/pain) are supportive and "
        "unadjusted for multiplicity — read them as consistency checks, not "
        "independently confirmatory results.",
        "Phase 3 tests a later timepoint (week 48, not day 169) and adds "
        "DASPRI as a second co-primary (see Slide 18).",
    ], RIGHT_X + 0.2, BODY_TOP + 0.6, RIGHT_W - 0.4, 4.2, size=12, gap_after=9)
    add_notes(s, "Both the total score and its components favor treatment, but "
              "Phase 3 tests a later timepoint and also lists DASPRI as a "
              "second co-primary.")
    add_footer(s, "02_research/phase2_results.md.", "09")
    return s

# =====================================================================
# SLIDE 10 -- Pharmacodynamics and durability
# =====================================================================

def slide_10():
    s = blank_slide(prs)
    add_title(s, "Biomarker suppression supports drug activity; crossover "
              "patterns add qualified evidence")
    add_text(s, "EXHIBIT A — ADJUSTED GEOMETRIC MEAN RATIO TO BASELINE, DAY 169",
             L, BODY_TOP, LEFT_W, 0.4, size=11, bold=True, color=NAVY)
    dataA = [
        ["Biomarker", "Pop 1: DAZ/Pbo", "Pop 2: DAZ/Pbo"],
        ["CXCL13", "0.67 / 1.00", "0.56 / 1.06"],
        ["Rheumatoid factor", "0.66 / 1.13", "0.54 / 0.94"],
    ]
    add_table(s, dataA, L, BODY_TOP + 0.4, LEFT_W, 1.35, col_widths=[34, 33, 33],
              font_size=12.5, header_size=11.5,
              align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT},
              row_heights=[0.5, 0.44, 0.44])
    add_text(s, "Ratios <1.0 = suppression relative to each arm’s own baseline "
             "(not a direct drug/placebo ratio).", L, 3.55, LEFT_W, 0.55, size=10.5,
             italic=True, color=GRAY)

    add_text(s, "EXHIBIT B — CHANGE FROM BASELINE, DAY 169 → DAY 365 (CROSSOVER)",
             L, 4.25, LEFT_W, 0.4, size=11, bold=True, color=NAVY)
    dataB = [
        ["Population / sequence", "Trajectory"],
        ["Systemic, placebo→DAZ", "ESSDAI −4.1 → −6.3"],
        ["Systemic, DAZ→placebo", "ESSDAI −6.3 → −4.4"],
        ["Symptomatic, DAZ→placebo", "ESSPRI −1.8 → −1.9"],
    ]
    add_table(s, dataB, L, 4.65, LEFT_W, 1.65, col_widths=[52, 48], font_size=12,
              header_size=11.5, row_heights=[0.42, 0.42, 0.42, 0.42])

    card_box(s, RIGHT_X, BODY_TOP, RIGHT_W, 5.0, fill=GRAY_TINT)
    add_text(s, "ON-SLIDE TAKEAWAY", RIGHT_X + 0.2, BODY_TOP + 0.2, RIGHT_W - 0.4, 0.32,
             size=12, bold=True, color=NAVY)
    add_text(s, "Pharmacological activity is supported; durable clinical "
             "efficacy under the Phase 3 regimen remains a separate question.",
             RIGHT_X + 0.2, BODY_TOP + 0.58, RIGHT_W - 0.4, 1.1, size=14, italic=True, color=DARK)
    add_bullets(s, [
        "Switching to dazodalibep (placebo→DAZ) improved further; switching "
        "off it (DAZ→placebo) partially reversed — both consistent with an "
        "active drug effect.",
        "A crossover after unblinding is not a 48-week parallel-group "
        "replication; carryover and expectation effects are real limitations.",
    ], RIGHT_X + 0.2, BODY_TOP + 1.9, RIGHT_W - 0.4, 2.8, size=12.5, gap_after=10)
    add_notes(s, "Biomarker values are ratios to each arm's own baseline, not "
              "direct drug/placebo ratios. A crossover is not a 48-week "
              "parallel-group replication.")
    add_footer(s, "02_research/phase2_results.md.", "10")
    return s

# =====================================================================
# SLIDE 11 -- Phase 2-to-3 bridge
# =====================================================================

def slide_11():
    s = blank_slide(prs)
    add_title(s, "Phase 3 increases information and changes duration and dose "
              "comparisons")
    data = [
        ["Factor", "Phase 2 systemic", "Phase 3 systemic", "Forecast implication"],
        ["Randomized total", "74", "651", "More precision; not proportional "
         "effect growth"],
        ["Active/control n (one comparison)", "36 / 38", "~217 / 217 assumed",
         "≈6.0× per-arm increase"],
        ["Primary assessment", "Day 169", "Week 48", "Longer durability and "
         "placebo-response window"],
        ["Active regimens", "One dose", "Two dose arms", "Dose selection and "
         "multiplicity matter"],
        ["ESSDAI entry floor", "≥5", "≥5", "No established loosening of "
         "this threshold"],
        ["Baseline/domain mix", "Observed", "Not established", "A real "
         "transportability uncertainty"],
    ]
    add_table(s, data, L, BODY_TOP, CW, 4.55, col_widths=[22, 16, 20, 42],
              font_size=12.5, header_size=12.5,
              row_heights=[0.55, 0.5, 0.6, 0.5, 0.5, 0.5, 0.65],
              cell_shades={(2, 2): GOLD_TINT, (6, 2): GOLD_TINT, (6, 3): GOLD_TINT},
              banding=GRAY_TINT)
    sw = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(L), Inches(6.32),
                             Inches(0.22), Inches(0.18))
    sw.fill.solid(); sw.fill.fore_color.rgb = GOLD_TINT
    sw.line.color.rgb = GOLD; sw.line.width = Pt(0.75); sw.shadow.inherit = False
    add_text(s, "= assumed or not established, not confirmed by the registry",
             L + 0.32, 6.28, CW - 0.5, 0.3, size=11, italic=True, color=GRAY)
    add_notes(s, "The per-arm comparison (≈6.0×) is the statistically relevant "
              "one — total-enrollment ratios mix in the number of arms and "
              "overstate the effective information gain.")
    add_footer(s, "03_analysis/final_thesis.md, "
               "02_research/phase2_baseline_characteristics.md. Allocation "
               "assumed equal; not confirmed by registry.", "11")
    return s

# =====================================================================
# SLIDE 12 -- Dose rationale and testing architecture
# =====================================================================

def slide_12():
    s = blank_slide(prs)
    add_title(s, "PK/PD supports dose selection, while clinical effect and "
              "testing rules remain separate")
    add_bullets(s, [
        ("A population PK/PD model ", "pooled 4 trials (healthy volunteers, "
         "RA, Sjögren’s), relating exposure to immune biomarkers."),
        ("Sjögren’s patients clear the drug more slowly ", "than healthy "
         "volunteers/RA patients — a real, population-specific PK finding."),
        ("The model supports ", "the proposed Phase 3 doses achieving "
         "sustained exposure above the Ki67+/RF biomarker IC50 — a "
         "pharmacodynamic target, not a clinical efficacy guarantee."),
        ("Two active arms vs. one shared placebo ", "raises a multiplicity "
         "question with no public testing-hierarchy disclosure."),
    ], L, BODY_TOP, CW, 2.25, size=14, gap_after=6)
    add_picture_fit(s, os.path.join(ASSETS, "slide11_testing.png"), L, 4.0,
                     CW, 2.75, align="center")
    add_notes(s, "The model describes sustained average exposure relative to "
              "biomarker IC50 — it does not prove trough coverage for every "
              "participant, or quantify the ESSDAI gain.")
    add_footer(s, "03_analysis/additional_topics.md, "
               "03_analysis/scenario_model.md.", "12")
    return s

# =====================================================================
# SLIDE 13 -- Ianalumab read-through
# =====================================================================

def _forest_row(s, x0, chart_w, y, vmin, vmax, label, point, lo, hi, color,
                 not_sig=False):
    def mx(v):
        return x0 + (v - vmin) / (vmax - vmin) * chart_w
    add_text(s, label, x0 - 2.55, y - 0.14, 2.45, 0.32, size=11, color=DARK,
              align=PP_ALIGN.RIGHT)
    if not_sig:
        add_text(s, "not significant — CI not reported", x0, y - 0.14,
                  chart_w, 0.3, size=10.5, italic=True, color=GRAY)
        return
    ln = s.shapes.add_connector(1, Inches(mx(lo)), Inches(y), Inches(mx(hi)), Inches(y))
    ln.line.color.rgb = color
    ln.line.width = Pt(2.25)
    for v in (lo, hi):
        tick = s.shapes.add_connector(1, Inches(mx(v)), Inches(y - 0.06),
                                       Inches(mx(v)), Inches(y + 0.06))
        tick.line.color.rgb = color
        tick.line.width = Pt(1.5)
    dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(mx(point) - 0.06), Inches(y - 0.06),
                              Inches(0.12), Inches(0.12))
    dot.fill.solid(); dot.fill.fore_color.rgb = color
    dot.line.color.rgb = WHITE; dot.line.width = Pt(0.75)
    dot.shadow.inherit = False


def slide_13():
    s = blank_slide(prs)
    add_title(s, "Ianalumab validates week-48 ESSDAI as a feasible endpoint, "
              "with modest effect sizes")
    add_text(s, "EXHIBIT — INDIVIDUAL PHASE 3 RESULTS", L, BODY_TOP, LEFT_W, 0.3,
             size=12, bold=True, color=NAVY)
    data = [
        ["Trial / regimen", "Effect", "95% CI", "p-value"],
        ["NEPTUNUS-1, monthly", "−1.3", "−2.6 to 0.0", "0.0496"],
        ["NEPTUNUS-2, monthly", "−1.0", "−2.0 to 0.0", "0.041"],
        ["NEPTUNUS-2, every 3 months", "Not significant (n.s.)", "—", "—"],
    ]
    add_table(s, data, L, BODY_TOP + 0.32, LEFT_W, 2.0, col_widths=[34, 26, 22, 18],
              font_size=11.5, header_size=11, align_cols={1: PP_ALIGN.RIGHT},
              row_heights=[0.42, 0.4, 0.4, 0.6])
    add_bullets(s, [
        "Monthly treatment met the endpoint in both trials; less-frequent "
        "dosing did not.",
        "Ph2b met its prespecified dose-response objective (4 of 5 models "
        "significant); the 300mg pairwise comparison alone (p≈0.092) does "
        "not define trial failure.",
    ], L, 3.55, LEFT_W, 2.0, size=13, gap_after=8)

    card_box(s, RIGHT_X, BODY_TOP, RIGHT_W, 5.0, fill=GRAY_TINT)
    add_text(s, "FOREST PLOT — EFFECT VS. PLACEBO", RIGHT_X + 0.2, BODY_TOP + 0.18,
             RIGHT_W - 0.4, 0.3, size=12, bold=True, color=NAVY)
    add_text(s, "(ESSDAI points, 95% CI)", RIGHT_X + 0.2, BODY_TOP + 0.47,
             RIGHT_W - 0.4, 0.28, size=10.5, italic=True, color=GRAY)
    vmin, vmax = -3.0, 0.6
    x0 = RIGHT_X + 2.75
    chart_w = RIGHT_W - 3.15
    _forest_row(s, x0, chart_w, 2.45, vmin, vmax, "NEPTUNUS-1\nmonthly", -1.3, -2.6, 0.0, TEAL)
    _forest_row(s, x0, chart_w, 3.05, vmin, vmax, "NEPTUNUS-2\nmonthly", -1.0, -2.0, 0.0, TEAL)
    _forest_row(s, x0, chart_w, 3.65, vmin, vmax, "NEPTUNUS-2\nq3 months", None, None, None, GRAY, not_sig=True)
    zero_x = x0 + (0 - vmin) / (vmax - vmin) * chart_w
    zl = s.shapes.add_connector(1, Inches(zero_x), Inches(2.2), Inches(zero_x), Inches(3.9))
    zl.line.color.rgb = RGBColor(0x99, 0x99, 0x99)
    zl.line.width = Pt(1)
    zl.line.dash_style = 2
    axis = s.shapes.add_connector(1, Inches(x0), Inches(4.05), Inches(x0 + chart_w), Inches(4.05))
    axis.line.color.rgb = GRAY
    axis.line.width = Pt(1)
    for v in (-3, -2, -1, 0):
        tx = x0 + (v - vmin) / (vmax - vmin) * chart_w
        add_text(s, str(v), tx - 0.25, 4.1, 0.5, 0.25, size=9.5, color=GRAY,
                  align=PP_ALIGN.CENTER)
    add_text(s, "← favors dazodalibep/ianalumab      favors placebo →",
             x0, 4.4, chart_w, 0.3, size=9, italic=True, color=GRAY,
             align=PP_ALIGN.CENTER)
    add_text(s, "Registry lists NEPTUNUS-2 N=506; conference presentation cites "
             "N=504 — this discrepancy is unresolved, reported both rather "
             "than picking one.", RIGHT_X + 0.2, 4.85, RIGHT_W - 0.4, 1.1,
             size=10.5, italic=True, color=DARK)
    add_notes(s, "I use these data to check plausible effects and precision, "
              "not to establish cross-trial superiority.")
    add_footer(s, "02_research/ianalumab_competitor_analysis.md.", "13")
    return s

# =====================================================================
# SLIDE 14 -- Pathway and historical lessons
# =====================================================================

def slide_14():
    s = blank_slide(prs)
    add_title(s, "Same-pathway evidence supports systemic activity more "
              "clearly than universal symptom benefit")
    data = [
        ["Evidence", "Result", "What it contributes"],
        ["Iscalimab systemic cohort, N=173", "Met dose-response objective",
         "Supports CD40 pathway plausibility"],
        ["Iscalimab symptom cohort, N=100", "ESSPRI −0.57; p=0.12",
         "Symptom benefit not assured by pathway alone"],
        ["Abatacept ASAP-III", "Missed continuous ESSDAI primary",
         "Plausible biology can still fail clinically"],
        ["Rituximab TRACTISS", "Missed symptom-VAS responder primary",
         "Endpoint/population selection matters"],
        ["Tocilizumab ETAP", "Missed composite-response primary",
         "Distinct response construct, not continuous ESSDAI"],
    ]
    add_table(s, data, L, BODY_TOP, CW, 3.65, col_widths=[27, 30, 43],
              font_size=13, header_size=13, row_heights=[0.5, 0.6, 0.6, 0.6, 0.6, 0.6],
              banding=GRAY_TINT)
    add_text(s, "ON-SLIDE TAKEAWAY: use prior trials to challenge assumptions; "
             "avoid a numerical “class success rate.”", L, 5.55, CW, 0.6,
             size=14, italic=True, color=NAVY)
    add_notes(s, "This set is not a meta-analysis or calibrated prior. "
              "Dazodalibep's own Phase 2 is not counted again as independent "
              "external validation.")
    add_footer(s, "02_research/historical_trial_evidence.md.", "14")
    return s

# =====================================================================
# SLIDE 15 -- Explicit effect assumptions
# =====================================================================

def slide_15():
    s = blank_slide(prs)
    add_title(s, "A 1.4-point base assumption retains about two-thirds of the "
              "Phase 2 effect")
    data = [
        ["Case", "Assumed benefit", "Retention vs. 2.2", "Rationale"],
        ["Bull", "2.0", "91%", "Most of the Phase 2 signal persists"],
        ["Base", "1.4", "64%", "Meaningful attenuation without loss of "
         "activity"],
        ["Bear", "0.6", "27%", "Substantial attenuation via efficacy, "
         "measurement, or population differences"],
    ]
    add_table(s, data, L, BODY_TOP, LEFT_W, 2.1, col_widths=[16, 20, 20, 44],
              font_size=12, header_size=12,
              align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT},
              row_heights=[0.55, 0.55, 0.5, 0.5],
              cell_shades={(1, 0): TEAL_TINT, (2, 0): GOLD_TINT, (3, 0): RED_TINT})
    add_text(s, "The base case is a judgment call, not a fitted or empirically "
             "estimated mean — tested across a range rather than one decimal "
             "point.", L, 4.35, LEFT_W, 1.1, size=13, italic=True, color=NAVY)

    card_box(s, RIGHT_X, BODY_TOP, RIGHT_W, 5.0, fill=GRAY_TINT)
    add_text(s, "ASSUMED BENEFIT (ESSDAI POINTS)", RIGHT_X + 0.2, BODY_TOP + 0.2,
             RIGHT_W - 0.4, 0.3, size=11.5, bold=True, color=NAVY)
    ax0 = RIGHT_X + 0.5
    aw = RIGHT_W - 1.0
    vmin, vmax = 0.0, 2.5
    axis_y = 2.75
    axis = s.shapes.add_connector(1, Inches(ax0), Inches(axis_y), Inches(ax0 + aw), Inches(axis_y))
    axis.line.color.rgb = GRAY
    axis.line.width = Pt(1.25)
    for v, lbl, col in [(0.6, "Bear\n0.6", RED), (1.4, "Base\n1.4", GOLD), (2.0, "Bull\n2.0", TEAL)]:
        x = ax0 + (v - vmin) / (vmax - vmin) * aw
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x - 0.075), Inches(axis_y - 0.075),
                                  Inches(0.15), Inches(0.15))
        dot.fill.solid(); dot.fill.fore_color.rgb = col
        dot.line.color.rgb = WHITE; dot.line.width = Pt(1)
        dot.shadow.inherit = False
        add_text(s, lbl, x - 0.5, axis_y + 0.15, 1.0, 0.5, size=11, bold=True,
                  color=col, align=PP_ALIGN.CENTER)
    xref = ax0 + (2.2 - vmin) / (vmax - vmin) * aw
    refline = s.shapes.add_connector(1, Inches(xref), Inches(axis_y - 0.55), Inches(xref), Inches(axis_y + 0.05))
    refline.line.color.rgb = NAVY
    refline.line.width = Pt(1.5)
    refline.line.dash_style = 2
    add_text(s, "Phase 2 observed: 2.2", xref - 1.0, axis_y - 0.95, 2.0, 0.35,
              size=10.5, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    for v in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5):
        x = ax0 + (v - vmin) / (vmax - vmin) * aw
        add_text(s, str(v), x - 0.25, axis_y + 0.02, 0.5, 0.25, size=8.5,
                  color=GRAY, align=PP_ALIGN.CENTER)
    add_text(s, "Three scenario points on the assumed-benefit axis, with "
             "Phase 2’s observed 2.2-point effect shown as a separate "
             "reference marker (not a fourth scenario).",
             RIGHT_X + 0.2, 3.85, RIGHT_W - 0.4, 1.1, size=11.5, italic=True, color=DARK)
    add_notes(s, "Why 1.4? A conservative departure from 2.2, in the range "
              "relevant clinical precedents suggest. The conclusion shouldn't "
              "depend on spurious decimal precision.")
    add_footer(s, "03_analysis/scenario_model.md. Scenario weights are analyst "
               "judgment, not empirically estimated probabilities — omitted "
               "from this slide.", "15")
    return s

# =====================================================================
# SLIDE 16 -- Conditional power
# =====================================================================

def slide_16():
    s = blank_slide(prs)
    add_title(s, "The base effect has favorable power under nominal testing, "
              "but the margin narrows with stricter assumptions")
    add_picture_fit(s, os.path.join(ASSETS, "slide16_power_curve.png"), L, 1.5,
                     7.55, 3.35, align="left")
    add_text(s, "EXHIBIT — ONE ACTIVE-DOSE COMPARISON, n=217/ARM, EFFECTIVE SD=5.47",
              L + 7.75, 1.5, CW - 7.75, 0.75, size=10.5, bold=True, color=NAVY)
    data = [
        ["Assumed true benefit", "Power @ α=0.05", "Power @ illustrative α=0.025"],
        ["0.6", "21%", "14%"],
        ["1.0", "48%", "37%"],
        ["1.4", "76%", "66%"],
        ["1.6", "86%", "79%"],
        ["2.0", "97%", "94%"],
    ]
    add_table(s, data, L + 7.75, 2.25, CW - 7.75, 2.6, col_widths=[40, 30, 30],
              font_size=10, header_size=9.5,
              align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT},
              row_heights=[0.55, 0.4, 0.4, 0.4, 0.4, 0.4])
    add_text(s, "ON-SLIDE TAKEAWAY: statistical success remains genuinely "
             "uncertain even if the assumed biological effect is correct.",
             L, 5.05, CW, 0.6, size=15, italic=True, color=NAVY)
    add_notes(s, "These curves describe repeated samples under fixed "
              "assumptions — not the unconditional probability that Amgen's "
              "actual trial succeeds.")
    add_footer(s, "03_analysis/scenario_model.md. SD=5.47 is a comparator-based "
               "sensitivity, not a measured dazodalibep Phase 3 SD.", "16")
    return s

# =====================================================================
# SLIDE 17 -- Variance, missing data, falsifiability
# =====================================================================

def slide_17():
    s = blank_slide(prs)
    add_title(s, "Higher variance and information loss can materially weaken "
              "the same efficacy forecast")
    add_picture_fit(s, os.path.join(ASSETS, "slide17_sensitivity.png"), L, 1.5,
                     CW, 2.75, align="center")
    add_text(s, "EXHIBIT — ASSUMED TRUE BENEFIT FIXED AT 1.4", L, 4.35, LEFT_W,
             0.3, size=11.5, bold=True, color=NAVY)
    data = [
        ["Assumption", "n/arm", "α", "Approx. power"],
        ["SD 3.65", "217", "0.05", "98%"],
        ["SD 5.00 (Ph2 planning)", "217", "0.05", "83%"],
        ["SD 5.47 (ianalumab-based)", "217", "0.05", "76%"],
        ["SD 5.47, stricter α", "217", "0.025", "66%"],
        ["Same, reduced effective n", "184", "0.025", "58%"],
    ]
    add_table(s, data, L, 4.65, LEFT_W, 1.75, col_widths=[42, 18, 16, 24],
              font_size=10.5, header_size=10.5,
              align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT, 3: PP_ALIGN.RIGHT},
              row_heights=[0.32, 0.29, 0.29, 0.29, 0.29, 0.29])
    add_bullets(s, [
        "Raw sample size alone is insufficient — repeated measurement and "
        "adjustment affect precision.",
        "Phase 3’s treatment of missing data/rescue medication is unknown "
        "and matters.",
    ], RIGHT_X, 4.65, RIGHT_W, 2.1, size=13, gap_after=8)
    add_notes(s, "The strongest bear case is a small retained effect under "
              "realistic noise and testing requirements — not simply that the "
              "study is larger.")
    add_footer(s, "03_analysis/scenario_model.md.", "17")
    return s

# =====================================================================
# SLIDE 18 -- Symptomatic trial conclusion
# =====================================================================

def slide_18():
    s = blank_slide(prs)
    add_title(s, "ESSPRI evidence supports optimism; DASPRI is a new, "
              "FDA-PRO-aligned instrument with zero track record for this drug",
              size=25)
    data = [
        ["Question", "Evidence available", "Interpretation"],
        ["Does DAZ improve reported symptoms?", "Positive Phase 2 ESSPRI "
         "total/domain results", "Supports a positive ESSPRI lean"],
        ["Does benefit extend to week 48?", "Supportive crossover only, no "
         "parallel-group replication", "Durability remains a test"],
        ["What supports DASPRI?", "Confirmed absent from the Phase 2 paper — "
         "searched full text, zero occurrences. DASPRI was developed as a "
         "patient-symptom diary specifically to align with FDA "
         "patient-reported-outcome guidance", "No dazodalibep-specific "
         "precedent exists for this instrument at all; likely added for "
         "regulatory-alignment reasons, not because ESSPRI underperformed"],
        ["What defines overall trial success?", "Two co-primary outcomes; "
         "procedure not established", "Do not assume both-pass or "
         "either-pass rule"],
    ]
    add_table(s, data, L, 1.95, CW, 4.15, col_widths=[24, 40, 36], font_size=11.5,
              header_size=12, row_heights=[0.42, 0.55, 0.55, 1.55, 0.7],
              cell_shades={(3, 1): GOLD_TINT}, banding=GRAY_TINT)
    add_text(s, "This isn’t a research gap to close — it’s a real fact about the "
             "evidence base.", L, 6.18, CW, 0.4, size=13, italic=True, color=NAVY)
    add_notes(s, "I checked the full text of the Phase 2 paper directly — "
              "DASPRI genuinely isn't in it. This is likely because it's a "
              "newer instrument built for FDA PRO alignment, added "
              "specifically for the Phase 3 registration package.")
    add_footer(s, "02_research/nct06245408_risk_note.md.", "18")
    return s

# =====================================================================
# SLIDE 19 -- Benefit-risk
# =====================================================================

def slide_19():
    s = blank_slide(prs)
    add_title(s, "Fc-free engineering addresses a known mechanism; Phase 2 "
              "safety still warrants careful scrutiny")
    add_text(s, "EXHIBIT — SELECTED SERIOUS OBSERVATIONS, NOT AN EXHAUSTIVE "
             "SAFETY TABLE", L, BODY_TOP, CW, 0.3, size=11.5, bold=True, color=NAVY)
    data = [
        ["Observation", "Population", "Attribution and precise timing"],
        ["DVT and drug-induced liver injury, same participant", "Population 1",
         "Both investigator-attributed as related; onset 180 days after "
         "last DAZ dose"],
        ["Invasive ductal breast carcinoma", "Population 2", "Investigator-"
         "attributed as related; onset 139 days after last dose"],
        ["One death, unknown cause following COVID-19 diagnosis",
         "Population 1", "SAE reported during Stage I per the paper’s text; "
         "investigators considered it unrelated; the death itself is "
         "tabulated under the Stage II+follow-up safety window (46 days "
         "post-last-dose) in Table 3 — both facts are accurate and reported "
         "together here, not simplified to one label"],
    ]
    add_table(s, data, L, BODY_TOP + 0.32, CW, 3.55, col_widths=[34, 16, 50],
              font_size=12, header_size=12, row_heights=[0.55, 0.85, 0.65, 1.5],
              banding=GRAY_TINT)
    add_text(s, "Three investigator-attributed serious events in two "
             "participants, plus a separately described unrelated death. "
             "Individual events in a small trial establish neither causation "
             "nor absence of risk.", L, 5.6, CW, 0.6, size=13, italic=True, color=NAVY)
    add_text(s, "Denominators: Stage I systemic DAZ n=36; Stage II systemic "
             "DAZ→placebo n=34; symptomatic safety set n=48.", L, 6.22, CW,
             0.4, size=10.5, italic=True, color=GRAY)
    add_notes(s, "I separate investigator attribution from demonstrated "
              "causality, and primary efficacy from overall benefit-risk.")
    add_footer(s, "02_research/phase2_results.md.", "19")
    return s

# =====================================================================
# SLIDE 20 -- Close
# =====================================================================

def slide_20():
    s = blank_slide(prs)
    add_title(s, "Our positive systemic forecast stands or falls on the "
              "prespecified primary result")
    callout_box(s, L, BODY_TOP, CW, 0.85, "FORECAST",
                "Expect positive ESSDAI efficacy in NCT06104124; favorable "
                "ESSPRI evidence with unresolved full-trial interpretation "
                "for NCT06245408.", fill=TEAL_TINT, border=TEAL,
                label_color=TEAL, body_size=14)
    data = [
        ["Readout", "Interpretation"],
        ["Prespecified primary procedure met, consistent dose results",
         "Confirms the forecast; assess magnitude and safety separately"],
        ["Primary met, modest effect or mixed supportive outcomes",
         "Statistical win with a more qualified clinical interpretation"],
        ["Prespecified primary procedure not met", "Forecast was wrong — "
         "evaluate why without redefining success post hoc"],
        ["Efficacy positive, concerning safety pattern", "Efficacy call may "
         "be right while benefit-risk remains unfavorable"],
    ]
    add_table(s, data, L, 2.55, CW, 2.85, col_widths=[46, 54], font_size=13,
              header_size=13, row_heights=[0.45, 0.62, 0.62, 0.58, 0.58],
              banding=GRAY_TINT)
    add_text(s, "Registry export: systemic primary completion July 23, 2026; "
             "study completion August 17, 2026 (both actual). Symptomatic: "
             "primary completion est. October 22, 2026; study completion est. "
             "December 17, 2026. Completion is not disclosure — no specific "
             "announcement date is established here.", L, 5.65, CW, 1.05,
             size=11.5, italic=True, color=DARK)
    add_notes(s, "A failed primary test is a failed forecast even if the "
              "biology remains interesting. A successful primary test should "
              "not be relabeled failure merely because a secondary threshold "
              "disappoints.")
    add_footer(s, "01_data/, 03_analysis/final_thesis.md.", "20")
    return s


# =====================================================================
# APPENDIX 1 -- Registry facts and unresolved design fields
# =====================================================================

def slide_a1():
    s = blank_slide(prs)
    add_title(s, "Appendix 1 — Registry facts and unresolved design fields")
    data = [
        ["Field", "Systemic", "Symptomatic"],
        ["NCT", "NCT06104124", "NCT06245408"],
        ["Enrollment", "651", "434"],
        ["Status", "Completed", "Active, not recruiting"],
        ["Primary outcomes", "ESSDAI", "ESSPRI; DASPRI"],
        ["Primary assessment", "Week 48", "Week 48"],
        ["Primary completion", "2026-07-23 (actual)", "2026-10-22 (estimated)"],
        ["Study completion", "2026-08-17 (actual)", "2026-12-17 (estimated)"],
    ]
    add_table(s, data, L, BODY_TOP, CW, 3.9, col_widths=[26, 37, 37], font_size=13.5,
              header_size=13.5, row_heights=[0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.55, 0.55],
              banding=GRAY_TINT)
    add_text(s, "Fields not represented by the registry export: arm doses/"
             "frequency, allocation ratio, full eligibility text, background-"
             "treatment stability, rescue rules, complete outcome definitions, "
             "protocol/SAP, analysis population, actual/estimated date flags "
             "beyond what’s shown. Do not present this table as a complete "
             "protocol abstraction.", L, 5.65, CW, 1.0, size=12.5, italic=True,
             color=NAVY)
    add_footer(s, "01_data/NCT06104124.csv, 01_data/NCT06245408.csv.", "A1")
    return s

# =====================================================================
# APPENDIX 2 -- Baseline characteristics
# =====================================================================

def slide_a2():
    s = blank_slide(prs)
    add_title(s, "Appendix 2 — Baseline characteristics (verified directly "
              "against Table 1, page 4)", size=25)
    data = [
        ["Characteristic", "Pop 1\nPlacebo", "Pop 1\nDAZ", "Pop 2\nPlacebo", "Pop 2\nDAZ"],
        ["N", "38", "36", "55", "54"],
        ["Baseline ESSDAI, mean (SD)", "10.1 (4.1)", "11.4 (4.5)", "2.5 (1.6)", "3.1 (1.8)"],
        ["Baseline ESSPRI total", "6.6 (1.8)", "6.6 (1.6)", "7.1 (1.1)", "7.5 (1.5)"],
        ["Dryness", "6.9 (2.3)", "7.3 (1.7)", "6.8 (1.2)", "7.1 (1.6)"],
        ["Fatigue", "6.8 (2.2)", "7.0 (1.7)", "6.8 (1.8)", "7.1 (1.8)"],
        ["Pain", "6.1 (2.3)", "5.5 (3.0)", "6.3 (1.9)", "6.6 (2.6)"],
        ["OSDI", "40.0 (20.9)", "48.7 (25.0)", "48.6 (19.2)", "48.2 (23.8)"],
        ["Stimulated salivary flow, mL/min", "0.97 (0.85)", "0.88 (0.64)",
         "0.83 (0.83)", "1.10 (1.18)"],
        ["Concomitant RA/SLE", "9 (23.7%)", "7 (19.4%)", "7 (12.7%)", "4 (7.4%)"],
    ]
    add_table(s, data, L, 1.85, CW, 2.85, col_widths=[32, 17, 17, 17, 17],
              font_size=10.5, header_size=10.5,
              align_cols={1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT, 3: PP_ALIGN.RIGHT, 4: PP_ALIGN.RIGHT},
              row_heights=[0.34, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26],
              banding=GRAY_TINT)
    add_text(s, "Schirmer’s criterion: ≤5mm/5min in at least one eye "
             "(corrected from an earlier transcription error — this direction "
             "is confirmed against the source).", L, 4.85, CW, 0.35, size=10,
             italic=True, color=GRAY)
    add_text(s, "Provenance: values re-verified directly against the rendered "
             "Table 1 image three separate times across this project’s review "
             "history, after two external reviews proposed alternate Pop. 2 "
             "ESSPRI-total/Dryness/OSDI/salivary-flow values. Each re-check "
             "matched the values above, not the proposed alternates (which "
             "appear to reflect a row-transposition error repeated across "
             "both reviews). Use the values above.", L, 5.25, CW, 0.95, size=10,
             color=DARK, line_spacing=1.05)
    add_text(s, "Relevant background therapy: Population 1 had 59.5% "
             "antimalarial, 41.9% glucocorticoid, 31.1% conventional DMARD use "
             "overall. Population 2 cholinergic agonist use differed: 11.1% "
             "DAZ vs. 27.3% placebo.", L, 6.25, CW, 0.55, size=10, italic=True,
             color=GRAY)
    add_footer(s, "02_research/phase2_baseline_characteristics.md, verified "
               "against 00_reference/phase2_paper.pdf Table 1.", "A2")
    return s

# =====================================================================
# APPENDIX 3 -- Supportive outcomes and domain scope
# =====================================================================

def slide_a3():
    s = blank_slide(prs)
    add_title(s, "Appendix 3 — Supportive outcomes and domain scope")
    data = [
        ["Day-169 outcome", "Population", "DAZ / Placebo change", "p-value"],
        ["ESSPRI", "Systemic", "−1.8 / −1.1", "0.1110"],
        ["FACIT-Fatigue", "Systemic", "+8.1 / +5.8", "0.3028"],
        ["FACIT-Fatigue", "Symptomatic", "+8.1 / +2.8", "0.0095"],
        ["OSDI", "Systemic", "−16.00 / −14.02", "0.6583"],
        ["OSDI", "Symptomatic", "−13.95 / −8.52", "0.1936"],
        ["Stimulated salivary flow", "Systemic", "+0.39 / +0.14", "0.1330"],
        ["Stimulated salivary flow", "Symptomatic", "+0.20 / −0.01", "0.2170"],
    ]
    add_table(s, data, L, BODY_TOP, CW, 3.9, col_widths=[30, 22, 30, 18],
              font_size=13, header_size=13,
              align_cols={2: PP_ALIGN.RIGHT, 3: PP_ALIGN.RIGHT},
              row_heights=[0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45],
              banding=GRAY_TINT)
    add_text(s, "These are unadjusted supportive/exploratory p-values. "
             "Positive FACIT change = improvement; negative OSDI/ESSPRI "
             "change = improvement.", L, 5.7, CW, 0.6, size=13, italic=True,
             color=NAVY)
    add_footer(s, "02_research/phase2_results.md.", "A3")
    return s

# =====================================================================
# APPENDIX 4 -- Reproducible statistical method
# =====================================================================

def slide_a4():
    s = blank_slide(prs)
    add_title(s, "Appendix 4 — Reproducible statistical method")
    add_text(s, "delta = assumed true positive treatment benefit;  n = "
             "per-arm sample size;  sigma = assumed effective SD.", L, BODY_TOP,
             CW, 0.35, size=12, italic=True, color=DARK)
    formula = ("SE = sigma * sqrt(2 / n)\n"
               "critical_z = inverse_normal_cdf(1 - alpha/2)\n"
               "power(delta) = normal_cdf(delta/SE - critical_z)\n"
               "effect_for_80_percent_power ≈ (critical_z + "
               "inverse_normal_cdf(0.80)) * SE")
    card_box(s, L, 1.95, CW, 1.35, fill=GRAY_TINT)
    add_text(s, formula, L + 0.22, 2.08, CW - 0.44, 1.1, size=12.5,
             color=NAVY, font="Courier New", line_spacing=1.25)
    data = [
        ["Sigma", "n", "Alpha", "SE", "Observed\nthreshold", "Effect for\n~80% power"],
        ["3.65", "217", "0.05", "0.350", "0.687", "0.982"],
        ["5.00", "217", "0.05", "0.480", "0.941", "1.345"],
        ["5.47", "217", "0.05", "0.525", "1.029", "1.471"],
        ["5.47", "217", "0.025", "0.525", "1.177", "1.619"],
        ["5.47", "184", "0.025", "0.570", "1.278", "1.758"],
    ]
    add_table(s, data, L, 3.5, CW, 1.85, col_widths=[13, 13, 13, 15, 23, 23],
              font_size=11.5, header_size=10.5,
              align_cols={0: PP_ALIGN.RIGHT, 1: PP_ALIGN.RIGHT, 2: PP_ALIGN.RIGHT,
                          3: PP_ALIGN.RIGHT, 4: PP_ALIGN.RIGHT, 5: PP_ALIGN.RIGHT},
              row_heights=[0.42, 0.29, 0.29, 0.29, 0.29, 0.29])
    add_text(s, "Input provenance: 3.65 from dazodalibep’s own Phase 2 SEs "
             "(approximate back-calculation); 5.00 is the Phase 2 protocol’s "
             "own planning SD; 5.47 is the effective SD implied by "
             "NEPTUNUS-1’s reported SE. None is the actual, undisclosed "
             "dazodalibep Phase 3 variance.", L, 5.55, CW, 0.75, size=10.5,
             color=DARK, line_spacing=1.05)
    add_text(s, "Interpretive rule: an assumed true delta produces "
             "conditional power, not a guaranteed p-value. NEPTUNUS-1’s SE "
             "scaled only for sample size (0.66×√(137/217)=0.524) implies "
             "that an observed 1.3-point difference would carry p≈0.013 at "
             "dazodalibep’s assumed N — a precision-scaling illustration, not "
             "a forecast.", L, 6.32, CW, 0.62, size=10, italic=True, color=GRAY)
    add_footer(s, "03_analysis/scenario_model.md.", "A4")
    return s

# =====================================================================
# APPENDIX 5 -- Expanded comparator and safety context (pointer slide)
# =====================================================================

def slide_a5():
    s = blank_slide(prs)
    add_title(s, "Appendix 5 — Expanded comparator and safety context")
    add_text(s, "This is a pointer slide: the underlying material is too "
             "extensive to reproduce legibly here. Each item below is pulled "
             "directly from its source file for the full detail.", L, BODY_TOP,
             CW, 0.6, size=14, italic=True, color=DARK)
    cards = [
        ("Ianalumab — full arm-by-arm data",
         "Ph2b dose-response model plus individual pairwise arms, and both "
         "NEPTUNUS trials, including the every-3-months miss.",
         "02_research/ianalumab_competitor_analysis.md"),
        ("Historical evidence — complete table",
         "TRACTISS, ETAP, and ASAP-III, with corrected endpoint "
         "classifications.",
         "02_research/historical_trial_evidence.md"),
        ("Phase 2 safety — full AE table",
         "All adverse events, not only the headline SAEs discussed on "
         "Slide 19.",
         "02_research/phase2_results.md"),
    ]
    cw3 = (CW - 0.7) / 3
    for i, (title, body, src) in enumerate(cards):
        x = L + i * (cw3 + 0.35)
        card_box(s, x, 2.55, cw3, 3.6, fill=GRAY_TINT)
        add_text(s, title, x + 0.22, 2.78, cw3 - 0.44, 0.85, size=14.5, bold=True,
                  color=NAVY, line_spacing=1.05)
        add_text(s, body, x + 0.22, 3.75, cw3 - 0.44, 1.55, size=12.5, color=DARK,
                  line_spacing=1.15)
        add_text(s, "Source: " + src, x + 0.22, 5.55, cw3 - 0.44, 0.5, size=10,
                  italic=True, color=GRAY)
    add_footer(s, "02_research/ianalumab_competitor_analysis.md, "
               "02_research/historical_trial_evidence.md, "
               "02_research/phase2_results.md.", "A5")
    return s

# =====================================================================
# APPENDIX 6 -- Source library
# =====================================================================

def slide_a6():
    s = blank_slide(prs)
    add_title(s, "Appendix 6 — Source library")
    left_items = [
        ("St. Clair EW et al. ", "CD40 ligand antagonist dazodalibep in "
         "Sjögren’s disease: a randomized, double-blinded, placebo-"
         "controlled, phase 2 trial. Nature Medicine 30, 1583–1592 (2024). "
         "DOI: 10.1038/s41591-024-03009-3. Open access (CC-BY 4.0). Local: "
         "00_reference/phase2_paper.pdf."),
        ("ClinicalTrials.gov, NCT06104124 — ", "systemic Phase 3. Local: "
         "01_data/NCT06104124.csv."),
        ("ClinicalTrials.gov, NCT06245408 — ", "symptomatic Phase 3. "
         "Local: 01_data/NCT06245408.csv."),
        ("Bowman SJ et al. ", "Safety and efficacy of subcutaneous ianalumab "
         "in primary Sjögren’s syndrome: phase 2b dose-finding trial. "
         "Lancet 399, 161–171 (2022; online 2021). PMID 34861168."),
        ("Fisher BA et al. ", "Safety and efficacy of subcutaneous iscalimab "
         "in two distinct populations of patients with Sjögren’s disease "
         "(TWINSS). Lancet (2024). PMID 39096929."),
        ("Novartis Immunology Pipeline Event, ", "Oct 2025 — NEPTUNUS "
         "individual-arm efficacy data."),
    ]
    right_items = [
        ("Seror R et al. ", "ESSDAI/ESSPRI MCID and disease-activity states, "
         "Ann Rheum Dis."),
        ("Der K et al. ", "Population PK/PD modeling of dazodalibep. ACR "
         "Convergence 2023 abstract."),
        ("Felten et al., ETAP. ", "Interleukin-6 receptor inhibition in "
         "primary Sjögren syndrome. PMID 33208345. Note: verify the "
         "“p=0.14” figure against this primary source before final use — "
         "flagged as unconfirmed, see "
         "02_research/historical_trial_evidence.md."),
        ("van Nimwegen et al., ASAP-III. ", "Primary randomized trial, "
         "Lancet Rheumatology."),
        ("TRACTISS ", "primary trial report."),
    ]
    add_bullets(s, left_items, L, BODY_TOP, LEFT_W, 5.3, size=11.5,
                lead_bold_split=True, gap_after=12, line_spacing=1.1)
    add_bullets(s, right_items, RIGHT_X, BODY_TOP, RIGHT_W, 5.3, size=11.5,
                lead_bold_split=True, gap_after=12, line_spacing=1.1)
    add_footer(s, "Full citation list compiled across 00_reference/, "
               "02_research/, and 03_analysis/.", "A6")
    return s


if __name__ == "__main__":
    slide_01(); slide_02(); slide_03(); slide_04(); slide_05()
    slide_06(); slide_07(); slide_08(); slide_09(); slide_10()
    slide_11(); slide_12(); slide_13(); slide_14(); slide_15()
    slide_16(); slide_17(); slide_18(); slide_19(); slide_20()
    slide_a1(); slide_a2(); slide_a3(); slide_a4(); slide_a5(); slide_a6()
    out = os.path.join(os.path.dirname(__file__), "dazodalibep_ph3_deepdive.pptx")
    prs.save(out)
    print("saved", out, "slides:", len(prs.slides))
