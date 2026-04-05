import matplotlib.pyplot as plt
import networkx as nx

from microseg.visualization.styling import get_role_color, scale_weight

def visualize_graph(G: nx.DiGraph) -> None:
    """
    Simple visualization of the graph using matplotlib.
    """

    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(G, seed=42)

    # Node coloring by role
    roles = nx.get_node_attributes(G, "role")
    color_map = [
        get_role_color(roles.get(node, "unknown"))
        for node in G.nodes()
    ]

    # Edge weights (preserve original matplotlib behavior: allow thin edges)
    weights = [
        scale_weight(G[u][v].get("weight", 1), min_width=0.0)
        for u, v in G.edges()
    ]

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=color_map,
        node_size=600,
        font_size=8,
        width=weights,
        edge_color="gray",
    )

    plt.title("Digital Twin Network Graph")
    plt.show()