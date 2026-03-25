import networkx as nx


# ---------------------------
# Core Analysis
# ---------------------------
# TODO: Calculate appropriate thresholds instead of using fixed values
HIGH_IMPORTANCE_THRESHOLD = 400
MEDIUM_IMPORTANCE_THRESHOLD = 150

def analyze_graph(G: nx.DiGraph) -> dict:
    """
    Perform graph-based communication analysis.

    Returns:
    {
        "node_metrics": {...},
        "edge_metrics": {...}
    }
    """

    # Use undirected version for centrality algorithms
    G_undirected = G.to_undirected()

    # ---------------------------
    # Node Metrics
    # ---------------------------

    degree = dict(G.degree())
    in_degree = dict(G.in_degree())
    out_degree = dict(G.out_degree())

    # weighted degree (sum of weights)
    weighted_degree = {}
    for node in G.nodes():
        total_weight = 0
        for _, _, data in G.edges(node, data=True):
            total_weight += data.get("weight", 0)
        weighted_degree[node] = total_weight

    # betweenness centrality
    betweenness = nx.betweenness_centrality(
        G_undirected,
        weight="weight",
        normalized=True
    )

    node_metrics = {}

    for node in G.nodes():
        node_metrics[node] = {
            "degree": degree.get(node, 0),
            "in_degree": in_degree.get(node, 0),
            "out_degree": out_degree.get(node, 0),
            "weighted_degree": weighted_degree.get(node, 0),
            "betweenness": betweenness.get(node, 0.0),
            "role": G.nodes[node].get("role"),
            "node_type": G.nodes[node].get("node_type"),
        }

    # ---------------------------
    # Edge Metrics
    # ---------------------------

    edge_metrics = {}

    for u, v, data in G.edges(data=True):
        weight = data.get("weight", 0)

        #importance classification
        importance = classify_importance(weight)

        edge_metrics[(u, v)] = {
            "weight": weight,
            "protocols": list(data.get("protocols", [])),
            "ports": list(data.get("ports", [])),
            "importance": importance,
        }

    return {
        "node_metrics": node_metrics,
        "edge_metrics": edge_metrics,
    }
    
def classify_importance(weight: float) -> str:
    if weight > HIGH_IMPORTANCE_THRESHOLD:
        return "high"
    elif weight > MEDIUM_IMPORTANCE_THRESHOLD:
        return "medium"
    return "low"
    
def print_top_nodes(node_metrics, key="weighted_degree", top_n=5):
    print(f"\nTop {top_n} nodes by {key}:")
    print("-" * 20)

    sorted_nodes = sorted(
        node_metrics.items(),
        key=lambda x: x[1][key],
        reverse=True
    )

    for node, metrics in sorted_nodes[:top_n]:
        print(f"{node}: {metrics[key]:.2f} ({metrics['role']})")
        

def inspect_node(G: nx.DiGraph, analysis: dict, node_id: str) -> None:
    """
    Print detailed analysis for a specific node.
    """

    if node_id not in G:
        print(f"Node '{node_id}' not found in graph.")
        return

    node_metrics = analysis["node_metrics"].get(node_id, {})

    print(f"\nNode: {node_id}")
    print("-" * 20)

    # ---------------------------
    # Basic Info
    # ---------------------------
    print("\n[Node Info]")
    print(f"Type: {node_metrics.get('node_type')}")
    print(f"Role: {node_metrics.get('role')}")

    # ---------------------------
    # Metrics
    # ---------------------------
    print("\n[Metrics]")
    for key in ["degree", "in_degree", "out_degree", "weighted_degree", "betweenness"]:
        value = node_metrics.get(key)
        print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")

    # ---------------------------
    # Outgoing Edges
    # ---------------------------
    print("\n[Outgoing Connections]")
    outgoing = list(G.out_edges(node_id, data=True))

    if not outgoing:
        print("  None")
    else:
        for _, dst, data in sorted(outgoing, key=lambda x: x[2].get("weight", 0), reverse=True):
            print(
                f"  -> {dst} | weight={data.get('weight')} "
                f"| ports={list(data.get('ports', []))}"
            )

    # ---------------------------
    # Incoming Edges
    # ---------------------------
    print("\n[Incoming Connections]")
    incoming = list(G.in_edges(node_id, data=True))

    if not incoming:
        print("  None")
    else:
        for src, _, data in sorted(incoming, key=lambda x: x[2].get("weight", 0), reverse=True):
            print(
                f"  <- {src} | weight={data.get('weight')} "
                f"| ports={list(data.get('ports', []))}"
            )
    
def inspect_edge(G: nx.DiGraph, analysis: dict, source: str, destination: str) -> None:
    """
    Print detailed analysis for a specific edge.
    """

    if not G.has_edge(source, destination):
        print(f"Edge '{source} -> {destination}' not found.")
        return

    edge_data = G[source][destination]
    edge_metrics = analysis["edge_metrics"].get((source, destination), {})

    print(f"\nEdge: {source} → {destination}")
    print("-" * 20)

    # ---------------------------
    # Basic Info
    # ---------------------------
    print("\n[Connection Details]")
    print(f"Weight (connections): {edge_data.get('weight')}")
    print(f"Protocols: {list(edge_data.get('protocols', []))}")
    print(f"Ports: {list(edge_data.get('ports', []))}")

    # ---------------------------
    # Classification
    # ---------------------------
    print("\n[Analysis]")
    print(f"Importance: {edge_metrics.get('importance')}")

    # ---------------------------
    # Node Context
    # ---------------------------
    print("\n[Context]")

    src_role = G.nodes[source].get("role")
    dst_role = G.nodes[destination].get("role")

    print(f"{source} ({src_role}) → {destination} ({dst_role})\n")
