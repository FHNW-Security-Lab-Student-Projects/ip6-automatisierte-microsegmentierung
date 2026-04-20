from z3 import Solver, Bool, And, Or, Not, Sum, If, sat

from microseg.constraints.models import AllowConstraint, DenyConstraint
from microseg.synthesis.models import SegmentationResult


class Z3Synthesizer:
    def __init__(self, constraints, path_engine, nodes, vlans):
        self.constraints = constraints
        self.path_engine = path_engine
        self.nodes = nodes
        self.vlans = vlans

        self.solver = Solver()

        # V(node, vlan) → Bool
        self.V = {
            (node, vlan): Bool(f"V_{node}_{vlan}") for node in nodes for vlan in vlans
        }

    # -------------------------
    # Public API
    # -------------------------
    def solve(self):
        self._add_host_constraints()
        self._add_allow_constraints()
        self._add_deny_constraints()

        if self.solver.check() != sat:
            print("UNSAT")
            return None

        model = self.solver.model()
        return self._extract_solution(model)

    # -------------------------
    # Host Constraint
    # -------------------------
    def _add_host_constraints(self):
        for node in self.nodes:
            node_type = self.path_engine.graph.nodes[node]["type"]

            if node_type == "host":
                vars_for_node = [self.V[(node, v)] for v in self.vlans]

                # Exactly one VLAN
                self.solver.add(Sum([If(v, 1, 0) for v in vars_for_node]) == 1)

    # -------------------------
    # ALLOW Constraints
    # -------------------------
    def _add_allow_constraints(self):
        for c in self.constraints:
            if not isinstance(c, AllowConstraint):
                continue

            path = self.path_engine.get_path(c.src, c.dst)
            if not path:
                continue

            vlan_conditions = []

            for v in self.vlans:
                cond = And(
                    self.V[(c.src, v)],
                    self.V[(c.dst, v)],
                    *[self.V[(node, v)] for node in path],
                )
                vlan_conditions.append(cond)

            self.solver.add(Or(vlan_conditions))

    # -------------------------
    # DENY Constraints
    # -------------------------
    def _add_deny_constraints(self):
        for c in self.constraints:
            if not isinstance(c, DenyConstraint):
                continue

            path = self.path_engine.get_path(c.src, c.dst)
            if not path:
                continue

            for v in self.vlans:
                self.solver.add(
                    Not(
                        And(
                            self.V[(c.src, v)],
                            self.V[(c.dst, v)],
                            *[self.V[(node, v)] for node in path],
                        )
                    )
                )

    # -------------------------
    # Extract Solution
    # -------------------------
    def _extract_solution(self, model):
        result = SegmentationResult()

        for node in self.nodes:
            for v in self.vlans:
                if model.evaluate(self.V[(node, v)]):
                    result.assign(node, v)

        result.finalize()
        return result
