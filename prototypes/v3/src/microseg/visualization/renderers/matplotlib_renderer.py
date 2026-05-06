import matplotlib.pyplot as plt
import networkx as nx

from microseg.visualization.styling import generate_vlan_colors, get_node_color


def visualize_graph(G, segmentation, heading: str = "Network Segmentation"):
    """
    Visualize graph with NetworkX/Matplotlib: assigns colors per VLAN,
    maps node colors based on segmentation, and renders labeled layout.
    """

    fig = plt.figure(figsize=(12, 8))
    fig.canvas.manager.set_window_title(heading)

    pos = nx.spring_layout(G, seed=42)

    # VLAN Colors
    all_vlans = set()
    for vlans in segmentation.node_to_vlans.values():
        all_vlans.update(vlans)

    vlan_colors = generate_vlan_colors(all_vlans)

    # Node colors
    color_map = [
        get_node_color(node, G.nodes[node], segmentation, vlan_colors)
        for node in G.nodes()
    ]

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=color_map,
        node_size=800,
        font_size=8,
        edge_color="gray",
    )

    plt.title(
        heading,
        fontsize=16,
        fontweight="bold",
        pad=20,
    )

    plt.show()
