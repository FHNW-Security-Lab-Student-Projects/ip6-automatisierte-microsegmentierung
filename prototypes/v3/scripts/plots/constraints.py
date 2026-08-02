import pandas as pd
import matplotlib.pyplot as plt

from style import (
    FIGSIZE,
    TITLE_SIZE,
    LABEL_SIZE,
    LEGEND_SIZE,
    LINE_WIDTH,
    COLORS,
    runtime_legend,
    apply_style,
    save,
)


def generate(df: pd.DataFrame):

    # --------------------------------------------------
    # Prepare data
    # --------------------------------------------------

    numeric_columns = [
        "constraints",
        "heuristic_time",
        "z3_time",
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    topologies = ["star", "tree", "mesh"]
    densities = ["low", "medium", "high"]

    fig, axes = plt.subplots(
        1,
        3,
        figsize=FIGSIZE,
        sharey=True,
    )

    for ax, topology in zip(axes, topologies):

        topology_df = (
            df[df["topology"] == topology]
            .sort_values("constraints")
        )

        for density in densities:

            current = (
                topology_df[
                    topology_df["dataset"].str.contains(density)
                ]
                .sort_values("constraints")
            )

            heuristic = current.dropna(subset=["heuristic_time"])
            z3 = current.dropna(subset=["z3_time"])

            # -----------------------------
            # Heuristic
            # -----------------------------

            ax.plot(
                heuristic["constraints"],
                heuristic["heuristic_time"],
                color=COLORS[density],
                linestyle="-",
                linewidth=LINE_WIDTH,
            )

            # -----------------------------
            # Z3
            # -----------------------------

            ax.plot(
                z3["constraints"],
                z3["z3_time"],
                color=COLORS[density],
                linestyle="--",
                linewidth=LINE_WIDTH,
            )

        apply_style(ax)

        ax.set_title(
            topology.capitalize(),
            fontsize=TITLE_SIZE,
        )

        ax.set_xlabel(
            "Constraints",
            fontsize=LABEL_SIZE,
        )

    axes[0].set_ylabel(
        "Runtime [s]",
        fontsize=LABEL_SIZE,
    )

    fig.suptitle(
        "Runtime vs. Constraint Count",
        fontsize=TITLE_SIZE + 2,
        fontweight="bold",
    )

    fig.legend(
        handles=runtime_legend(),
        loc="lower center",
        ncol=5,
        fontsize=LEGEND_SIZE,
        frameon=False,
        bbox_to_anchor=(0.5, -0.02),
    )

    save(
        fig,
        "04_runtime_constraints.png",
    )