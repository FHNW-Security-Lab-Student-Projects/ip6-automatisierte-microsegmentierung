import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.lines import Line2D

from style import (
    FIGSIZE,
    TITLE_SIZE,
    LABEL_SIZE,
    LEGEND_SIZE,
    MARKER_SIZE,
    COLORS,
    MARKERS,
    save,
)


def generate(df: pd.DataFrame):

    # --------------------------------------------------
    # Prepare data
    # --------------------------------------------------

    numeric_columns = [
        "nodes",
        "heuristic_vlans",
        "z3_vlans",
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
            .sort_values("nodes")
        )

        for density in densities:

            current = (
                topology_df[
                    topology_df["dataset"].str.contains(density)
                ]
                .sort_values("nodes")
            )

            heuristic = current.dropna(subset=["heuristic_vlans"])
            z3 = current.dropna(subset=["z3_vlans"])

            # ----------------------------------------
            # Heuristic
            # ----------------------------------------

            ax.scatter(
                heuristic["nodes"],
                heuristic["heuristic_vlans"],
                color=COLORS[density],
                marker=MARKERS[density],
                s=80,
                edgecolors="black",
                linewidths=0.6,
                zorder=3,
            )

            # ----------------------------------------
            # Z3
            # ----------------------------------------

            ax.scatter(
                z3["nodes"],
                z3["z3_vlans"],
                facecolors="white",
                edgecolors=COLORS[density],
                marker=MARKERS[density],
                s=90,
                linewidths=2,
                zorder=3,
            )

        ax.grid(
            True,
            linestyle="--",
            alpha=0.35,
        )

        ax.set_title(
            topology.capitalize(),
            fontsize=TITLE_SIZE,
        )

        ax.set_xlabel(
            "Number of Nodes",
            fontsize=LABEL_SIZE,
        )

    axes[0].set_ylabel(
        "Used VLANs",
        fontsize=LABEL_SIZE,
    )

    fig.suptitle(
        "Segment Quality (Used VLANs)",
        fontsize=TITLE_SIZE + 2,
        fontweight="bold",
    )

    legend = [

        Line2D(
            [0],
            [0],
            marker="o",
            color="black",
            linestyle="",
            markersize=8,
            label="Heuristic",
        ),

        Line2D(
            [0],
            [0],
            marker="o",
            markerfacecolor="white",
            markeredgecolor="black",
            linestyle="",
            markersize=8,
            label="Z3 Solver",
        ),

        Line2D(
            [0],
            [0],
            marker="o",
            color=COLORS["low"],
            linestyle="",
            markersize=8,
            label="Low Constraints",
        ),

        Line2D(
            [0],
            [0],
            marker="s",
            color=COLORS["medium"],
            linestyle="",
            markersize=8,
            label="Medium Constraints",
        ),

        Line2D(
            [0],
            [0],
            marker="^",
            color=COLORS["high"],
            linestyle="",
            markersize=8,
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
        "02_vlan_usage.png",
    )