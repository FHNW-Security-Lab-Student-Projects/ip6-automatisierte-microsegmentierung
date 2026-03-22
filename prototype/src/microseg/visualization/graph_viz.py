import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(G: nx.DiGraph) -> None:
    """
    Simple visualization of the graph.
    """

    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(G, seed=42)

    # Node coloring by role
    roles = nx.get_node_attributes(G, "role")

    color_map = []
    for node in G.nodes():
        role = roles.get(node, "unknown")

        if role == "user":
            color_map.append("lightblue")
        elif role == "application":
            color_map.append("lightgreen")
        elif role == "database":
            color_map.append("orange")
        elif role in ["dns", "identity", "fileserver", "mail"]:
            color_map.append("violet")
        elif role in ["monitoring", "logging", "backup"]:
            color_map.append("grey")
        elif role in ["firewall", "vpn"]:
            color_map.append("red")
        else:
            color_map.append("white")

    # Edge weights
    weights = [G[u][v]["weight"] for u, v in G.edges()]
    scaled_weights = [w / 100 for w in weights]

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=color_map,
        node_size=600,
        font_size=8,
        width=scaled_weights,
        edge_color="gray",
    )

    plt.title("Digital Twin Network Graph")
    plt.show()