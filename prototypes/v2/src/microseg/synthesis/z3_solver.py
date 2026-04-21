from z3 import Solver, Bool, And, Or, Not, Sum, If, sat

from microseg.constraints.models import AllowConstraint, DenyConstraint
from microseg.synthesis.models import SegmentationResult


class Z3Synthesizer:
    def __init__(self, constraints, path_engine, nodes, vlans):
        """
        Initialize Z3 model: stores inputs, creates solver, and defines
        boolean vars V(node,vlan). Also prepares tracking for unsat cores.
        """

        self.constraints = constraints
        self.path_engine = path_engine
        self.nodes = nodes
        self.vlans = vlans

        self.solver = Solver()

        # Tracking and Mapping
        self.tracked_constraints = []
        self.constraint_map = {}

        # V(node, vlan) → Bool
        self.V = {
            (node, vlan): Bool(f"V_{node}_{vlan}") for node in nodes for vlan in vlans
        }

    def solve(self):
        """
        Build and solve constraints (host, ALLOW, DENY).
        Returns SegmentationResult if SAT, otherwise prints grouped UNSAT core.
        """

        self._add_host_constraints()
        self._add_allow_constraints()
        self._add_deny_constraints()

        if self.solver.check() != sat:
            print("UNSAT")

            core = self.solver.unsat_core()

            # GROUPING LOGIC
            grouped = {}

            for c in core:
                name = str(c)

                # Remove VLAN suffix for grouping
                if "_v" in name:
                    base = name.split("_v")[0]
                else:
                    base = name

                if base not in grouped:
                    grouped[base] = []

                grouped[base].append(name)

            # PRETTY OUTPUT
            print("\nConflict Constraints:")

            for base, variants in grouped.items():
                if variants[0] in self.constraint_map:
                    real = self.constraint_map[variants[0]]
                    print(f"- {base} → {real}")
                else:
                    print(f"- {base}")

            return None

        model = self.solver.model()
        return self._extract_solution(model)

    def _add_host_constraints(self):
        """
        Enforce host nodes belong to exactly one VLAN using cardinality constraint.
        """

        for node in self.nodes:
            node_type = self.path_engine.graph.nodes[node]["type"]

            if node_type == "host":
                vars_for_node = [self.V[(node, v)] for v in self.vlans]

                # Exactly one VLAN
                self.solver.add(Sum([If(v, 1, 0) for v in vars_for_node]) == 1)

    def _add_allow_constraints(self):
        """
        Encode ALLOW: src, dst, and all nodes on a path must share at least one VLAN.
        Adds tracked constraints for UNSAT debugging.
        """

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

            name = f"ALLOW_{c.src}_{c.dst}"
            constraint = Or(vlan_conditions)

            self.solver.assert_and_track(constraint, name)
            self.tracked_constraints.append(name)
            self.constraint_map[name] = c

    def _add_deny_constraints(self):
        """
        Encode DENY: src, dst, and path nodes must not share the same VLAN.
        Adds per-VLAN tracked constraints.
        """

        for c in self.constraints:
            if not isinstance(c, DenyConstraint):
                continue

            path = self.path_engine.get_path(c.src, c.dst)
            if not path:
                continue

            for v in self.vlans:
                name = f"DENY_{c.src}_{c.dst}_v{v}"

                constraint = Not(
                    And(
                        self.V[(c.src, v)],
                        self.V[(c.dst, v)],
                        *[self.V[(node, v)] for node in path],
                    )
                )

                self.solver.assert_and_track(constraint, name)
                self.tracked_constraints.append(name)
                self.constraint_map[name] = c

    def _extract_solution(self, model):
        """
        Convert Z3 model into SegmentationResult by collecting true V(node,vlan).
        """

        result = SegmentationResult()

        for node in self.nodes:
            for v in self.vlans:
                if model.evaluate(self.V[(node, v)]) == True:
                    result.assign(node, v)

        result.finalize()
        return result
