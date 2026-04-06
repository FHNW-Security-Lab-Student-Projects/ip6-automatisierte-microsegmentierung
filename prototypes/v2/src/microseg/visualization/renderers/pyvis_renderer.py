from pathlib import Path
import webbrowser
from pyvis.network import Network

from microseg.visualization.styling import generate_vlan_colors, get_node_color


def visualize_graph(G, segmentation, output_file: str = "network.html"):

    net = Network(
        height="800px",
        width="100%",
        directed=False,
        bgcolor="#ffffff",
        font_color="black",
    )

    net.force_atlas_2based()

    # ---------------------------
    # VLAN Colors
    # ---------------------------
    all_vlans = set()
    for vlans in segmentation.node_to_vlans.values():
        all_vlans.update(vlans)

    vlan_colors = generate_vlan_colors(all_vlans)

    # ---------------------------
    # Add Nodes
    # ---------------------------
    for node, data in G.nodes(data=True):

        color = get_node_color(node, data, segmentation, vlan_colors)

        title = f"""
        {node}
        VLANs: {list(segmentation.get_vlans(node))}
        """

        net.add_node(
            node,
            label=node,
            color=color,
            title=title,
            size=20,
        )

    # ---------------------------
    # Add Edges
    # ---------------------------
    for src, dst in G.edges():
        net.add_edge(
            src,
            dst,
            color="gray",
        )

    output_path = Path(__file__).parent.parent / "tmp" / output_file
    net.write_html(str(output_path))
    webbrowser.open(f"file://{output_path.resolve()}")
