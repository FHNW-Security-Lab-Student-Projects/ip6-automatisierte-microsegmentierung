from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# -------------------------------------------------------------------
# Figure settings
# -------------------------------------------------------------------

FIGSIZE = (15, 5)

DPI = 300

TITLE_SIZE = 16
LABEL_SIZE = 12
TICK_SIZE = 10
LEGEND_SIZE = 10

LINE_WIDTH = 2.5
MARKER_SIZE = 6

# -------------------------------------------------------------------
# Colors
# -------------------------------------------------------------------

COLORS = {
    "low": "#2ca02c",
    "medium": "#ff7f0e",
    "high": "#d62728",
}

MARKERS = {
    "low": "o",
    "medium": "s",
    "high": "^",
}

# -------------------------------------------------------------------
# Styling
# -------------------------------------------------------------------

def apply_style(ax):

    ax.grid(
        True,
        which="both",
        linestyle="--",
        linewidth=0.5,
        alpha=0.35,
    )

    ax.tick_params(labelsize=TICK_SIZE)

    ax.set_yscale("log")


# -------------------------------------------------------------------
# Runtime legend
# -------------------------------------------------------------------

def runtime_legend():

    return [

        Line2D(
            [0], [0],
            color="black",
            linestyle="-",
            linewidth=LINE_WIDTH,
            label="Heuristic",
        ),

        Line2D(
            [0], [0],
            color="black",
            linestyle="--",
            linewidth=LINE_WIDTH,
            label="Z3 Solver",
        ),

        Line2D(
            [0], [0],
            color=COLORS["low"],
            linewidth=LINE_WIDTH,
            label="Low Constraints",
        ),

        Line2D(
            [0], [0],
            color=COLORS["medium"],
            linewidth=LINE_WIDTH,
            label="Medium Constraints",
        ),

        Line2D(
            [0], [0],
            color=COLORS["high"],
            linewidth=LINE_WIDTH,
            label="High Constraints",
        ),
    ]


# -------------------------------------------------------------------
# Save helper
# -------------------------------------------------------------------

def save(fig, filename):

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / filename,
        dpi=DPI,
        bbox_inches="tight",
    )

    plt.close(fig)