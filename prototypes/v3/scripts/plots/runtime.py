import pandas as pd
import matplotlib.pyplot as plt

from style import (
    FIGSIZE,
    TITLE_SIZE,
    LABEL_SIZE,
    LEGEND_SIZE,
    LINE_WIDTH,
    MARKER_SIZE,
    COLORS,
    MARKERS,
    apply_style,
    runtime_legend,
    save,
)


def generate(df: pd.DataFrame):

    # --------------------------------------------------
    # Prepare data
    # --------------------------------------------------

    numeric_columns = [
        "nodes",
        "heuristic_time",
        "z3_time",
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    topologies = ["star", "tree", "mesh"]
    densities = ["low", "medium", "high"]

    # --------------------------------------------------
    # Create one figure with three subplots
    # --------------------------------------------------

    fig, axes = plt.subplots(
        1,
        3,
        figsize=FIGSIZE,
        sharey=True,
    )

    for ax, topology in zip(axes, topologies):

        topology_df = (
            df[df["topology"] == topology]
            .sort_values("nodes")
        )

        for density in densities:

            current = (
                topology_df[
                    topology_df["dataset"].str.contains(density)
                ]
                .sort_values("nodes")
            )

            # Successful runs only
            heuristic = current.dropna(subset=["heuristic_time"])
            z3 = current.dropna(subset=["z3_time"])

            # --------------------------
            # Heuristic
            # --------------------------

            ax.plot(
                heuristic["nodes"],
                heuristic["heuristic_time"],
                color=COLORS[density],
                linestyle="-",
                linewidth=LINE_WIDTH,
                marker=MARKERS[density],
                markersize=MARKER_SIZE,
            )

            # --------------------------
            # Z3
            # --------------------------

            ax.plot(
                z3["nodes"],
                z3["z3_time"],
                color=COLORS[density],
                linestyle="--",
                linewidth=LINE_WIDTH,
                marker=MARKERS[density],
                markersize=MARKER_SIZE,
            )

        apply_style(ax)

        ax.set_title(
            topology.capitalize(),
            fontsize=TITLE_SIZE,
        )

        ax.set_xlabel(
            "Nodes",
            fontsize=LABEL_SIZE,
        )

    # Shared Y label

    axes[0].set_ylabel(
        "Runtime [s]",
        fontsize=LABEL_SIZE,
    )

    # Figure title

    fig.suptitle(
        "Runtime Comparison",
        fontsize=TITLE_SIZE + 2,
        fontweight="bold",
    )

    # Shared legend

    fig.legend(
        handles=runtime_legend(),
        loc="lower center",
        ncol=5,
        fontsize=LEGEND_SIZE,
        frameon=False,
        bbox_to_anchor=(0.5, -0.02),
    )

    save(fig, "01_runtime_comparison.png")