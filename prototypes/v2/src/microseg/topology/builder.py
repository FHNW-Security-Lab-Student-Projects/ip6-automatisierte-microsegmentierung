from typing import List

from microseg.constraints.models import (
    LocatedAtConstraint,
    ConnectedConstraint,
)

from .models import Node, Edge, NodeType
from ..graph.graph import TopologyGraph


class TopologyBuilder:
    def __init__(self, constraints: List):
        self.constraints = constraints
        self.graph = TopologyGraph()

    def build(self) -> TopologyGraph:
        self._add_switches()
        self._add_hosts()
        self._add_links()

        return self.graph

    def _add_switches(self):
        switches = set()

        for c in self.constraints:
            if isinstance(c, ConnectedConstraint):
                switches.add(c.node_a)
                switches.add(c.node_b)

        for s in switches:
            self.graph.add_node(Node(id=s, type=NodeType.SWITCH))

    def _add_hosts(self):
        for c in self.constraints:
            if isinstance(c, LocatedAtConstraint):
                # add host
                self.graph.add_node(Node(id=c.node, type=NodeType.HOST))

                # ensure switch exists
                self.graph.add_node(Node(id=c.switch, type=NodeType.SWITCH))

                # connect host to switch
                self.graph.add_edge(Edge(c.node, c.switch))

    def _add_links(self):
        for c in self.constraints:
            if isinstance(c, ConnectedConstraint):
                self.graph.add_edge(Edge(c.node_a, c.node_b))
