from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Load cleaned Serena Williams data
serena = pd.read_csv("data/serena_matches.csv")

# Create output directory
output_dir = Path("figures")
output_dir.mkdir(parents = True, exist_ok = True)

# Set colors by match result
colors = {
    "win": "blue",
    "loss": "red"
}

# Create scatter plot
fig, ax = plt.subplots(figsize = (12, 7))

for result in ["win", "loss"]:
    data = serena[serena["result"] == result]

    ax.scatter(
        data["serena_age"],
        data["age_difference"],
        color = colors[result],
        label = result.capitalize(),
        alpha = 0.6,
        s = 18
    )

# Reference line
ax.axhline(0, color = "black", linewidth = 1)

# Labels and title
ax.set_xlabel("Serena Williams' age")
ax.set_ylabel("Age difference from opponent")
ax.set_title(
    "Serena Williams' Professional Matches, Age 14 to 40"
)

# Styling
ax.set_facecolor("white")
ax.grid(True, alpha = 0.2)
ax.legend()

# Caption
fig.text(
    0.5,
    0.02,
    "Source: Tennis Abstract",
    ha = "center",
    fontsize = 10
)

# Save figure
output_file = output_dir / "serena_age_plot.png"

fig.savefig(
    output_file,
    dpi = 300,
    bbox_inches = "tight"
)

plt.close(fig)

print(f"Plot saved successfully: {output_file}")