from typing import List, Optional
import networkx as nx

from ..topology.graph import TopologyGraph


class PathEngine:
    def __init__(self, topology: TopologyGraph):
        self.graph = topology.graph

    # -------------------------
    # Shortest Path (BFS)
    # -------------------------
    def get_path(self, src: str, dst: str) -> Optional[List[str]]:
        try:
            path = nx.shortest_path(self.graph, source=src, target=dst)
            return path
        except nx.NetworkXNoPath:
            return None
        except nx.NodeNotFound:
            return None

    # -------------------------
    # Reachability
    # -------------------------
    def is_reachable(self, src: str, dst: str) -> bool:
        try:
            return nx.has_path(self.graph, src, dst)
        except nx.NodeNotFound:
            return False

    # -------------------------
    # Nodes along path
    # -------------------------
    def get_path_nodes(self, src: str, dst: str) -> List[str]:
        path = self.get_path(src, dst)
        return path if path else []
