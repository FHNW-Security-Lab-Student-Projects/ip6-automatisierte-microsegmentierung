import networkx as nx
from typing import List

from ..topology.models import Node, Edge


class TopologyGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node: Node):
        self.graph.add_node(node.id, type=node.type)

    def add_edge(self, edge: Edge):
        self.graph.add_edge(edge.node_a, edge.node_b)

    def get_nodes(self):
        return list(self.graph.nodes(data=True))

    def get_edges(self):
        return list(self.graph.edges())

    def neighbors(self, node_id: str):
        return list(self.graph.neighbors(node_id))


def pretty_print_graph(nodes, edges):
    print("\nNodes:")
    print("------")
    for name, attrs in nodes:
        node_type = attrs.get("type")
        print(f"{name:<10} (type: {node_type.value})")

    print("\nEdges:")
    print("------")
    for src, dst in edges:
        print(f"{src:<10} -> {dst}")