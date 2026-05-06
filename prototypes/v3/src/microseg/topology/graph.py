import networkx as nx
from typing import List

from .models import Node, Edge


class TopologyGraph:
    def __init__(self):
        """Wrap a NetworkX graph for topology storage."""
        self.graph = nx.Graph()

    def add_node(self, node: Node):
        """Add a node with its type attribute."""
        self.graph.add_node(node.id, type=node.type)

    def add_edge(self, edge: Edge):
        """Add an undirected edge between two nodes."""
        self.graph.add_edge(edge.node_a, edge.node_b)

    def get_nodes(self):
        """Return list of (node, attributes) tuples."""
        return list(self.graph.nodes(data=True))

    def get_edges(self):
        """Return list of graph edges."""
        return list(self.graph.edges())

    def neighbors(self, node_id: str):
        """Return neighboring node IDs."""
        return list(self.graph.neighbors(node_id))


def pretty_print_graph(nodes, edges):
    """
    Print formatted view of nodes (with types) and edges.
    Expects output of get_nodes() and get_edges().
    """

    print("\nNodes:")
    print("------")
    for name, attrs in nodes:
        node_type = attrs.get("type")
        print(f"{name:<10} (type: {node_type.value})")

    print("\nEdges:")
    print("------")
    for src, dst in edges:
        print(f"{src:<10} -> {dst}")
