from typing import List, Optional
import networkx as nx

from ..topology.graph import TopologyGraph


class PathEngine:
    """Initialize with a topology; stores underlying NetworkX graph."""

    def __init__(self, topology: TopologyGraph):
        self.graph = topology.graph

    def get_path(self, src: str, dst: str) -> Optional[List[str]]:
        """
        Return shortest path (list of nodes) from src to dst using NetworkX.
        Returns None if no path exists or nodes are missing.
        """

        try:
            path = nx.shortest_path(self.graph, source=src, target=dst)
            return path
        except nx.NetworkXNoPath:
            return None
        except nx.NodeNotFound:
            return None

    def is_reachable(self, src: str, dst: str) -> bool:
        """
        Check if dst is reachable from src.
        Returns False if no path exists or nodes are missing.
        """

        try:
            return nx.has_path(self.graph, src, dst)
        except nx.NodeNotFound:
            return False

    def get_path_nodes(self, src: str, dst: str) -> List[str]:
        """
        Get nodes along shortest path; returns empty list if no path found.
        """

        path = self.get_path(src, dst)
        return path if path else []
