import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.patches import Patch

from style import (
    FIGSIZE,
    TITLE_SIZE,
    LABEL_SIZE,
    LEGEND_SIZE,
    COLORS,
    save,
)


def generate(df: pd.DataFrame):

    # --------------------------------------------------
    # Prepare data
    # --------------------------------------------------

    df["heuristic_valid"] = (
        df["heuristic_valid"]
        .fillna(False)
        .astype(bool)
    )

    df["z3_valid"] = (
        df["z3_valid"]
        .fillna(False)
        .astype(bool)
    )

    topologies = ["star", "tree", "mesh"]
    densities = ["low", "medium", "high"]

    fig, axes = plt.subplots(
        1,
        3,
        figsize=FIGSIZE,
        sharey=True,
    )

    width = 0.35

    for ax, topology in zip(axes, topologies):

        topology_df = df[df["topology"] == topology]

        heuristic_rates = []
        z3_rates = []

        for density in densities:

            current = topology_df[
                topology_df["dataset"].str.contains(density)
            ]

            total = len(current)

            if total == 0:
                heuristic_rates.append(0)
                z3_rates.append(0)
                continue

            heuristic_rates.append(
                current["heuristic_valid"].sum() / total * 100
            )

            z3_rates.append(
                current["z3_valid"].sum() / total * 100
            )

        x = range(len(densities))

        for i, density in enumerate(densities):

            # Heuristic
            ax.bar(
                i - width / 2,
                heuristic_rates[i],
                width,
                color=COLORS[density],
                edgecolor="black",
                linewidth=0.8,
            )

            # Z3
            ax.bar(
                i + width / 2,
                z3_rates[i],
                width,
                color=COLORS[density],
                edgecolor="black",
                linewidth=0.8,
                hatch="//",
            )

            # Value labels

            ax.text(
                i - width / 2,
                heuristic_rates[i] + 2,
                f"{heuristic_rates[i]:.0f}%",
                ha="center",
                fontsize=9,
            )

            ax.text(
                i + width / 2,
                z3_rates[i] + 2,
                f"{z3_rates[i]:.0f}%",
                ha="center",
                fontsize=9,
            )

        ax.set_title(
            topology.capitalize(),
            fontsize=TITLE_SIZE,
        )

        ax.set_xticks(list(x))
        ax.set_xticklabels(
            ["Low", "Medium", "High"]
        )

        ax.set_xlabel(
            "Constraint Density",
            fontsize=LABEL_SIZE,
        )

        ax.set_ylim(0, 105)

        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.35,
        )

    axes[0].set_ylabel(
        "Successful Runs [%]",
        fontsize=LABEL_SIZE,
    )

    fig.suptitle(
        "Solver Robustness",
        fontsize=TITLE_SIZE + 2,
        fontweight="bold",
    )

    legend = [

        Patch(
            facecolor="white",
            edgecolor="black",
            label="Heuristic",
        ),

        Patch(
            facecolor="white",
            edgecolor="black",
            hatch="//",
            label="Z3 Solver",
        ),

        Patch(
            facecolor=COLORS["low"],
            edgecolor="black",
            label="Low Constraints",
        ),

        Patch(
            facecolor=COLORS["medium"],
            edgecolor="black",
            label="Medium Constraints",
        ),

        Patch(
            facecolor=COLORS["high"],
            edgecolor="black",
            label="High Constraints",
        ),
    ]

    fig.legend(
        handles=legend,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.02),
        ncol=5,
        frameon=False,
        fontsize=LEGEND_SIZE,
    )

    save(
        fig,
        "03_solver_robustness.png",
    )