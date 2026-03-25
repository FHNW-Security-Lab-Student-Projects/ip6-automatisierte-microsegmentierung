from pathlib import Path
import webbrowser
import os
from pyvis.network import Network
import networkx as nx

from microseg.visualization.styling import get_role_color, scale_weight

def visualize_graph(G: nx.DiGraph, output_file: str = "network.html") -> None:
    """
    Interactive visualization using Pyvis.
    """

    net = Network(
        height="800px",
        width="100%",
        directed=True,
        bgcolor="#ffffff",
        font_color="black",
    )

    # Better layout (physics-based)
    net.force_atlas_2based(
    gravity=-50,
    central_gravity=0.01,
    spring_length=200,
    spring_strength=0.08,
    damping=0.4,
)

    # ---------------------------
    # Add Nodes
    # ---------------------------
    for node, data in G.nodes(data=True):
        role = data.get("role", "unknown")
        node_type = data.get("node_type", "N/A")

        title = f"""
        {node}
        Role: {role}
        Type: {node_type}
        """

        net.add_node(
            node,
            label=node,
            color=get_role_color(role),
            title=title,
            size=20,
        )

    # ---------------------------
    # Add Edges
    # ---------------------------
    for src, dst, data in G.edges(data=True):
        weight = data.get("weight", 1)

        protocols = ", ".join(sorted(data.get("protocols", [])))
        ports = ", ".join(map(str, sorted(data.get("ports", []))))

        title = f"""
        {src} → {dst}
        Connections: {weight}
        Protocols: {protocols}
        Ports: {ports}
        """

        net.add_edge(
            src,
            dst,
            value=scale_weight(weight, min_width=1.0),  # controls thickness
            title=title,
            color="gray",
            arrows="to",
        )

    # ---------------------------
    # Optional UI controls
    # ---------------------------
    net.show_buttons(filter_=["physics"])

    # ---------------------------
    # Export
    # ---------------------------
    output_path = Path(__file__).parent.parent / "tmp" / output_file

    net.write_html(str(output_path))
    webbrowser.open(f"file://{output_path.resolve()}")