"""
Analysis of ASV (Amplicon Sequence Variant) data using scikit-bio.
This script:
  • Loads and inspects the ASV table
  • Computes alpha diversity metrics (Observed richness, Shannon)
  • Saves barplots and boxplots
  • Computes Bray–Curtis distances + PCoA
  • Saves PCoA scatterplot
All plots are saved to .png files and NOT displayed.
"""

# -----------------------------
# Import libraries
# -----------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skbio
print(f"Scikit-bio version: {skbio.__version__}")

from skbio.diversity import alpha, beta_diversity
from skbio.stats.ordination import pcoa


# -----------------------------
# Load OTU/ASV data
# -----------------------------
otu = pd.read_csv("asv_table.tsv", sep="\t", index_col=0)

print("\nASV table preview:")
print(otu.head())


# -----------------------------
# Alpha diversity calculations
# -----------------------------
observed_features = {}
shannon = {}
pielou = {}

# Loop over each sample column in the table
for sample in otu:
    observed_features[sample] = alpha.sobs(otu[sample])
    shannon[sample] = alpha.shannon(otu[sample])
    pielou[sample] = alpha.pielou_e(otu[sample])

# Convert to pandas Series for convenience
observed_features = pd.Series(observed_features)
shannon = pd.Series(shannon)
pielou = pd.Series(pielou)


# -----------------------------
# Plot: Observed Richness
# -----------------------------
values = observed_features.values
samples = observed_features.index

# Manually grouping into 3 groups of 4 samples each (adjust if needed)
group1 = values[0:4]
group2 = values[4:8]
group3 = values[8:12]
data = np.concatenate([group1, group2, group3])

# Color coding (4 + 4 + 4)
colors = ["navy"]*4 + ["green"]*4 + ["orange"]*4

plt.figure(figsize=(10, 5))
plt.bar(range(len(data)), data, color=colors)

plt.xticks(
    [1.5, 5.5, 9.5],
    ["soil", "viable cells", "viable cells after\nLive-FISH"]
)

plt.title("Observed Richness")
plt.ylabel("Number of ASVs")
plt.xlabel("Treatment")
plt.tight_layout()

# Save instead of showing
plt.savefig("observed_richness.png", dpi=300)
plt.close()


# -----------------------------
# Plot: Shannon Diversity (Boxplot)
# -----------------------------
values = shannon.values

group1 = values[0:4]
group2 = values[4:8]
group3 = values[8:12]
data = [group1, group2, group3]

colors = ["navy", "green", "orange"]

plt.figure(figsize=(8, 5))
bp = plt.boxplot(data, patch_artist=True)

# Color each box
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

plt.xticks([1, 2, 3], ["soil", "viable cells", "viable cells after\nLive-FISH"])
plt.title("Shannon Diversity Boxplot")
plt.ylabel("Shannon (H')")

plt.tight_layout()
plt.savefig("shannon_diversity_boxplot.png", dpi=300)
plt.close()


# -----------------------------
# Beta diversity (Bray–Curtis)
# assumes rows = ASVs, columns = samples in the dataframe
# -----------------------------
dm = beta_diversity(
    metric="braycurtis",
    counts=otu.T.values,   # scikit-bio expects samples-as-rows
    ids=otu.columns
)

ord1 = pcoa(dm)

print("\nPCoA coordinate head:")
print(ord1.samples.head())

print("\nProportion explained:")
print(ord1.proportion_explained)


# -----------------------------
# Plot: PCoA scatterplot
# -----------------------------
pc = ord1.samples
pc1_label = pc.columns[0]
pc2_label = pc.columns[1]

# % variance explained
pe = ord1.proportion_explained
pc1_var = pe[pc1_label] * 100
pc2_var = pe[pc2_label] * 100

# Color rules based on sample name prefixes
def color_for(sample_name: str) -> str:
    s = str(sample_name).lower()
    if s.startswith("soil"):
        return "navy"
    if s.startswith("viable cells"):
        return "green"
    if s.startswith("live-fish") or s.startswith("live_fish") or s.startswith("live fish"):
        return "orange"
    return "gray"

colors = [color_for(s) for s in pc.index]

# legend mapping
label_order = [
    ("soil", "navy"),
    ("viable cells", "green"),
    ("Live-FISH", "orange")
]
present = [(lab, col) for lab, col in label_order if col in colors]

plt.figure(figsize=(6, 5))
plt.scatter(pc[pc1_label], pc[pc2_label], s=60, edgecolor="k", c=colors)

# Annotate each point
for sample in pc.index:
    plt.text(pc.loc[sample, pc1_label],
             pc.loc[sample, pc2_label],
             sample,
             fontsize=8,
             va="bottom")

# Legend with proxy points
for lab, col in present:
    plt.scatter([], [], c=col, edgecolor="k", s=60, label=lab)
plt.legend(frameon=True, title="Group", loc="best")

plt.xlabel(f"{pc1_label} ({pc1_var:.1f}%)")
plt.ylabel(f"{pc2_label} ({pc2_var:.1f}%)")
plt.title("PCoA (Bray–Curtis)")
plt.tight_layout()

plt.savefig("pcoa_braycurtis.png", dpi=300)
plt.close()
