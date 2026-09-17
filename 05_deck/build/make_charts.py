"""Generate all chart/diagram images used in the deck."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
from scipy.stats import norm
import os

OUT = os.path.join(os.path.dirname(__file__), "assets")
NAVY = "#1B2A4A"
TEAL = "#2E7D7B"
GRAY = "#8C8C8C"
LIGHT = "#F2F2F0"
RED = "#B4453E"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 13,
    "axes.edgecolor": "#444444",
})

# ---------- Slide 5: CD40L mechanism diagram ----------
fig, ax = plt.subplots(figsize=(11, 5.2))
ax.set_xlim(0, 11)
ax.set_ylim(0, 5.2)
ax.axis("off")

def box(x, y, w, h, text, color=NAVY, textcolor="white", fontsize=13, fontweight="bold"):
    fb = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.12",
                          linewidth=1.2, edgecolor=color, facecolor=color, alpha=0.95)
    ax.add_patch(fb)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", color=textcolor,
            fontsize=fontsize, fontweight=fontweight, wrap=True)

# Main pathway
box(0.3, 2.7, 2.3, 1.3, "T-cell\n(CD40L)", color=NAVY)
box(4.1, 2.7, 2.6, 1.3, "B-cell / APC /\nepithelial cell\n(CD40)", color=NAVY)
box(8.1, 2.7, 2.5, 1.3, "Antibody production,\ngerminal center\nformation", color=RED)

ax.annotate("", xy=(4.05, 3.35), xytext=(2.65, 3.35),
            arrowprops=dict(arrowstyle="-|>", lw=2.2, color="#333333"))
ax.text(3.35, 3.65, "costimulatory\nsignal", ha="center", fontsize=10, style="italic")

ax.annotate("", xy=(8.05, 3.35), xytext=(6.75, 3.35),
            arrowprops=dict(arrowstyle="-|>", lw=2.2, color="#333333"))

# Block icons
ax.plot([3.35], [3.35], marker="X", markersize=22, color=TEAL, markeredgewidth=3)
ax.text(3.35, 4.35, "Dazodalibep\n(blocks CD40L)", ha="center", fontsize=10.5,
        fontweight="bold", color=TEAL)

ax.plot([5.4], [2.65], marker="X", markersize=22, color="#B08A00", markeredgewidth=3)
ax.text(5.4, 1.9, "Iscalimab\n(blocks CD40)", ha="center", fontsize=10.5,
        fontweight="bold", color="#B08A00")

# Separate BAFF-R branch, visually distinct
box(4.1, 0.15, 2.6, 1.1, "BAFF-R / B-cell\nsurvival signal", color=GRAY, fontsize=11)
ax.plot([5.4], [1.25], marker="X", markersize=18, color="#5B3A8E", markeredgewidth=2.5)
ax.text(0.3, 0.7, "Ianalumab (different mechanism—\nB-cell depletion + BAFF-R blockade,\nnot the CD40/CD40L handshake)",
        ha="left", fontsize=9.5, color="#5B3A8E", style="italic")
ax.annotate("", xy=(5.4, 1.3), xytext=(5.4, 2.6),
            arrowprops=dict(arrowstyle="-", lw=1, color=GRAY, linestyle="dashed"))

ax.text(5.5, 4.85, "Engineering addresses a known mechanism; clinical safety still requires evidence.",
        ha="center", fontsize=9.5, style="italic", color="#555555")

plt.tight_layout()
plt.savefig(f"{OUT}/slide5_mechanism.png", dpi=200, bbox_inches="tight", facecolor="white")
plt.close()

# ---------- Slide 6: Phase 2 timeline ----------
fig, ax = plt.subplots(figsize=(11, 3.6))
ax.set_xlim(-10, 375)
ax.set_ylim(0, 3)
ax.axis("off")

ax.text(-8, 2.55, "PBO → DAZ", fontsize=12, fontweight="bold", va="center")
ax.add_patch(plt.Rectangle((0, 2.2), 169, 0.6, color=GRAY))
ax.add_patch(plt.Rectangle((169, 2.2), 196, 0.6, color=TEAL))
ax.text(84, 2.5, "Placebo", ha="center", va="center", color="white", fontsize=10, fontweight="bold")
ax.text(267, 2.5, "Dazodalibep 1,500mg", ha="center", va="center", color="white", fontsize=10, fontweight="bold")

ax.text(-8, 1.15, "DAZ → PBO", fontsize=12, fontweight="bold", va="center")
ax.add_patch(plt.Rectangle((0, 0.8), 169, 0.6, color=TEAL))
ax.add_patch(plt.Rectangle((169, 0.8), 196, 0.6, color=GRAY))
ax.text(84, 1.1, "Dazodalibep 1,500mg", ha="center", va="center", color="white", fontsize=10, fontweight="bold")
ax.text(267, 1.1, "Placebo", ha="center", va="center", color="white", fontsize=10, fontweight="bold")

ax.axvline(169, color=RED, linestyle="--", linewidth=2.5)
ax.text(169, 3.15, "PRIMARY ANALYSIS\n(Day 169)", ha="center", fontsize=12,
        fontweight="bold", color=RED)

ax.text(365, 0.15, "Day 365\nCrossover data used for\ndurability check only,\nnot primary efficacy",
        ha="center", fontsize=9, style="italic", color="#555555")
ax.axvline(365, color="#999999", linewidth=1)

for d, lbl in [(0, "Day 0"), (169, ""), (365, "Day 365")]:
    if lbl:
        ax.text(d, -0.15, lbl, ha="center", fontsize=10, color="#444444")

plt.tight_layout()
plt.savefig(f"{OUT}/slide6_timeline.png", dpi=200, bbox_inches="tight", facecolor="white")
plt.close()

# ---------- Slide 11: dose/testing architecture ----------
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax in axes:
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

ax = axes[0]
ax.text(5, 9.3, "Confirmed (registry)", ha="center", fontsize=13, fontweight="bold", color=NAVY)
box_ax = FancyBboxPatch((0.7, 5.7), 8.6, 2.6, boxstyle="round,pad=0.1", facecolor=LIGHT, edgecolor=NAVY, linewidth=1.5)
ax.add_patch(box_ax)
ax.text(5, 6.9, "3 arms—Dose 1, Dose 2, Placebo\n\nDoses and allocation ratio\nnot disclosed", ha="center", va="center", fontsize=11)

ax = axes[1]
ax.text(5, 9.3, "Illustrative only—not confirmed", ha="center", fontsize=13, fontweight="bold", color=RED)
ax.text(5, 8.2, "Total α = 0.05", ha="center", fontsize=12, fontweight="bold")
ax.annotate("", xy=(2.7, 6.3), xytext=(4.6, 7.7), arrowprops=dict(arrowstyle="-", lw=1.3, color="#666"))
ax.annotate("", xy=(7.3, 6.3), xytext=(5.4, 7.7), arrowprops=dict(arrowstyle="-", lw=1.3, color="#666"))
box1 = FancyBboxPatch((0.7, 5.2), 4.0, 1.1, boxstyle="round,pad=0.08", facecolor="#EAF3F2", edgecolor=TEAL)
box2 = FancyBboxPatch((5.3, 5.2), 4.0, 1.1, boxstyle="round,pad=0.08", facecolor="#EAF3F2", edgecolor=TEAL)
ax.add_patch(box1); ax.add_patch(box2)
ax.text(2.7, 5.75, "Dose 1 vs. Placebo\nα = 0.025", ha="center", va="center", fontsize=10)
ax.text(7.3, 5.75, "Dose 2 vs. Placebo\nα = 0.025", ha="center", va="center", fontsize=10)
ax.text(5, 3.8, "One illustrative possibility,\nnot Amgen's actual statistical plan,\nwhich is not public.",
        ha="center", fontsize=10, style="italic", color=RED)

plt.tight_layout()
plt.savefig(f"{OUT}/slide11_testing.png", dpi=200, bbox_inches="tight", facecolor="white")
plt.close()

# ---------- Slide 16: conditional power curve ----------
fig, ax = plt.subplots(figsize=(10, 5.2))
deltas = np.linspace(0, 2.5, 200)
alpha = 0.05
z_alpha = norm.ppf(1 - alpha/2)
n = 217

for sd, color, label in [(3.65, TEAL, "SD = 3.65 (Phase 2 observed)"),
                           (5.00, "#B08A00", "SD = 5.00 (Phase 2 planning)"),
                           (5.47, RED, "SD = 5.47 (ianalumab-based)")]:
    se = sd * np.sqrt(2/n)
    power = norm.cdf(deltas/se - z_alpha) * 100
    ax.plot(deltas, power, color=color, linewidth=2.6, label=label)

for x, lbl in [(0.6, "Bear\n0.6"), (1.4, "Base\n1.4"), (2.0, "Bull\n2.0")]:
    ax.axvline(x, color="#999999", linestyle=":", linewidth=1.3)
    ax.text(x, 102, lbl, ha="center", fontsize=9.5, color="#555555")

ax.axhline(80, color="#333333", linestyle="--", linewidth=1, alpha=0.6)
ax.text(2.45, 81.5, "80% power", fontsize=9, ha="right", color="#333333")

ax.set_xlabel("Assumed true ESSDAI effect (points)", fontsize=12)
ax.set_ylabel("Conditional power (%)", fontsize=12)
ax.set_title("Statistical power vs. assumed true effect, n≈217/arm", fontsize=13, fontweight="bold", color=NAVY)
ax.set_ylim(0, 108)
ax.legend(loc="lower right", fontsize=10, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", alpha=0.25)

plt.tight_layout()
plt.savefig(f"{OUT}/slide16_power_curve.png", dpi=200, bbox_inches="tight", facecolor="white")
plt.close()

# ---------- Slide 17: variance/missing-data sensitivity dot plot ----------
fig, ax = plt.subplots(figsize=(10.5, 4.2))
rows = [
    ("SD 3.65, n=217, α=0.05", 98),
    ("SD 5.00, n=217, α=0.05", 83),
    ("SD 5.47, n=217, α=0.05", 76),
    ("SD 5.47, n=217, α=0.025", 66),
    ("SD 5.47, n=184, α=0.025", 58),
]
labels = [r[0] for r in rows][::-1]
values = [r[1] for r in rows][::-1]
colors_list = [TEAL, TEAL, "#B08A00", "#B08A00", RED][::-1]

y_pos = np.arange(len(labels))
ax.hlines(y_pos, 0, values, color="#CCCCCC", linewidth=2)
ax.scatter(values, y_pos, color=colors_list, s=180, zorder=3, edgecolor="white", linewidth=1.5)
for y, v in zip(y_pos, values):
    ax.text(v + 2.5, y, f"{v}%", va="center", fontsize=11, fontweight="bold")

ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=11)
ax.set_xlim(0, 110)
ax.set_xlabel("Conditional power at assumed true benefit = 1.4 points (%)", fontsize=11)
ax.set_title("Same assumed effect, five variance/testing scenarios", fontsize=13, fontweight="bold", color=NAVY)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.grid(axis="x", alpha=0.25)

plt.tight_layout()
plt.savefig(f"{OUT}/slide17_sensitivity.png", dpi=200, bbox_inches="tight", facecolor="white")
plt.close()

print("All charts generated in", OUT)
for f in sorted(os.listdir(OUT)):
    print(" -", f)
