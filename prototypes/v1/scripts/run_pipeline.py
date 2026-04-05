from microseg.ingestion.csv_loader import load_nodes, load_traffic
from microseg.graph.graph_builder import build_graph, print_graph_summary
from microseg.analysis.analyzer import analyze_graph, print_top_nodes, inspect_node, inspect_edge
from microseg.visualization.renderers.pyvis_renderer import visualize_graph


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
    # Analyze Graph
    # ---------------------------
    analysis = analyze_graph(G)
    node_metrics = analysis["node_metrics"]
    
    print_top_nodes(node_metrics, key="degree")
    # print_top_nodes(node_metrics, key="in_degree")
    # print_top_nodes(node_metrics, key="out_degree")
    # print_top_nodes(node_metrics, key="weighted_degree")
    # print_top_nodes(node_metrics, key="betweenness")
    
    # inspect_node(G, analysis, "app01")
    # inspect_edge(G, analysis, "app01", "db01")

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