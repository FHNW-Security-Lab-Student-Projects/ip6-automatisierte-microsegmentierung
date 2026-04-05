import networkx as nx
from typing import List, Dict


def build_graph(nodes: List[Dict], traffic: List[Dict]) -> nx.DiGraph:
    """
    Build a directed graph (Digital Twin) from normalized data.

    Parameters:
    - nodes: list of node dicts
    - traffic: list of traffic dicts

    Returns:
    - NetworkX DiGraph
    """

    G = nx.DiGraph()

    # ---------------------------
    # Add Nodes
    # ---------------------------
    for n in nodes:
        node_id = n["node_id"]

        G.add_node(
            node_id,
            node_type=n.get("node_type"),
            role=n.get("role"),
        )

    # ---------------------------
    # Add / Aggregate Edges
    # ---------------------------
    for t in traffic:
        src = t["source"]
        dst = t["destination"]

        protocol = t["protocol"]
        port = t["port"]
        weight = t["connections"]

        # Edge already exists → aggregate
        if G.has_edge(src, dst):
            G[src][dst]["weight"] += weight
            G[src][dst]["protocols"].add(protocol)
            G[src][dst]["ports"].add(port)

        else:
            G.add_edge(
                src,
                dst,
                weight=weight,
                protocols={protocol},
                ports={port},
            )

    return G

def print_graph_summary(G: nx.DiGraph) -> None:
    print("Graph Summary")
    print("------------------")
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")

    roles = {}
    for _, data in G.nodes(data=True):
        role = data.get("role", "unknown")
        roles[role] = roles.get(role, 0) + 1

    print("\nNode roles:")
    for r, count in roles.items():
        print(f"  {r}: {count}")