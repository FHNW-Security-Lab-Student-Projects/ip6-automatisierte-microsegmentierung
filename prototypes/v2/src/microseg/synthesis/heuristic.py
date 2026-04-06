from typing import List

from microseg.constraints.models import AllowConstraint, DenyConstraint
from microseg.graph.path_engine import PathEngine
from microseg.topology.models import NodeType
from .models import SegmentationResult


class HeuristicSynthesizer:
    def __init__(self, constraints: List, path_engine: PathEngine):
        self.constraints = constraints
        self.path_engine = path_engine
        self.result = SegmentationResult()
        self.current_vlan = 10  # Start value

        self.deny_constraints = [
            c for c in self.constraints if isinstance(c, DenyConstraint)
        ]

    def run(self) -> SegmentationResult:
        allow_constraints = [
            c for c in self.constraints if isinstance(c, AllowConstraint)
        ]

        for constraint in allow_constraints:
            self._handle_allow(constraint)

        self.result.finalize()
        return self.result

    # -------------------------
    # ALLOW processing
    # -------------------------
    def _handle_allow(self, constraint: AllowConstraint):
        src = constraint.src
        dst = constraint.dst

        path = self.path_engine.get_path(src, dst)

        if not path:
            return

        vlan = self._select_vlan(path)

        # Assign VLAN to all nodes along the path
        for node in path:
            self._assign_node(node, vlan)

    # -------------------------
    # VLAN selection (DENY-aware)
    # -------------------------
    def _select_vlan(self, path):
        candidate_vlans = set()

        for node in path:
            candidate_vlans.update(self.result.get_vlans(node))

        # Try to reuse an existing VLAN if it does not violate DENY constraints
        for vlan in candidate_vlans:
            if not self._violates_deny(path, vlan):
                return vlan

        # Otherwise allocate a new VLAN
        return self._new_vlan()

    # -------------------------
    # Assignment with host constraint check
    # -------------------------
    def _assign_node(self, node: str, vlan: int):
        node_type = self._get_node_type(node)

        if node_type == NodeType.HOST:
            existing_vlans = self.result.get_vlans(node)

            # A host must belong to exactly one VLAN
            if existing_vlans and vlan not in existing_vlans:
                raise ValueError(
                    f"Host {node} cannot be assigned to multiple VLANs: {existing_vlans} + {vlan}"
                )

        self.result.assign(node, vlan)

    # -------------------------
    # DENY constraint validation
    # -------------------------
    def _violates_deny(self, path, vlan):
        for node in path:
            for other_node, vlans in self.result.node_to_vlans.items():
                if vlan not in vlans:
                    continue

                if self._is_denied(node, other_node):
                    return True

        return False

    def _is_denied(self, a, b):
        for c in self.deny_constraints:
            if (c.src == a and c.dst == b) or (c.src == b and c.dst == a):
                return True
        return False

    # -------------------------
    # Node type lookup helper
    # -------------------------
    def _get_node_type(self, node_id: str):
        return self.path_engine.graph.nodes[node_id]["type"]

    # -------------------------
    # VLAN ID generator
    # -------------------------
    def _new_vlan(self):
        vlan = self.current_vlan
        self.current_vlan += 10
        return vlan
