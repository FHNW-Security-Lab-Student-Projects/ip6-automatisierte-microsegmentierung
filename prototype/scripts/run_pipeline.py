from microseg.ingestion.csv_loader import load_nodes, load_traffic
from microseg.graph.graph_builder import build_graph, print_graph_summary
from microseg.visualization.graph_viz import visualize_graph


def main():
    # ---------------------------
    # Load Data
    # ---------------------------
    nodes = load_nodes("datasets/syntethic/30_Nodes_Company_Network/nodes.csv")
    traffic = load_traffic("datasets/syntethic/30_Nodes_Company_Network/traffic.csv")

    # ---------------------------
    # Build Graph
    # ---------------------------
    G = build_graph(nodes, traffic)

    # ---------------------------
    # Debug Output
    # ---------------------------
    print_graph_summary(G)

    # ---------------------------
    # Visualization
    # ---------------------------
    visualize_graph(G)


if __name__ == "__main__":
    main()