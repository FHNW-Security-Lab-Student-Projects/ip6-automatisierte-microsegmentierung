from typing import List

from microseg.constraints.models import AllowConstraint, DenyConstraint
from microseg.graph.path_engine import PathEngine
from microseg.validation.models import ValidationResult


class ConstraintValidator:
    def __init__(self, constraints: List, path_engine: PathEngine, segmentation):
        """
        Initialize with constraints, path engine, and computed segmentation.
        """

        self.constraints = constraints
        self.path_engine = path_engine
        self.segmentation = segmentation

    def validate(self) -> ValidationResult:
        """
        Run ALLOW and DENY checks; returns ValidationResult with violations.
        """

        result = ValidationResult()

        self._check_allow(result)
        self._check_deny(result)

        return result

    def _check_allow(self, result: ValidationResult):
        """
        Verify all ALLOW constraints; record violations if communication fails.
        """

        for c in self.constraints:
            if not isinstance(c, AllowConstraint):
                continue

            src = c.src
            dst = c.dst

            if not self._is_allowed(src, dst):
                result.allow_violations.append(f"{src} → {dst}")

    def _check_deny(self, result: ValidationResult):
        """
        Verify all DENY constraints; record violations if communication is possible.
        """

        for c in self.constraints:
            if not isinstance(c, DenyConstraint):
                continue

            src = c.src
            dst = c.dst

            if self._is_allowed(src, dst):
                result.deny_violations.append(f"{src} ↔ {dst}")

    def _is_allowed(self, src: str, dst: str) -> bool:
        """
        Check if src→dst is allowed: requires path, shared VLAN, and valid
        VLAN propagation across all nodes on the path.
        """

        path = self.path_engine.get_path(src, dst)

        if not path:
            return False

        # Check if a common VLAN exists
        src_vlans = self.segmentation.get_vlans(src)
        dst_vlans = self.segmentation.get_vlans(dst)

        common_vlans = src_vlans.intersection(dst_vlans)

        if not common_vlans:
            return False

        # Check VLAN propagation along the path
        for vlan in common_vlans:
            if self._vlan_valid_on_path(path, vlan):
                return True

        return False

    def _vlan_valid_on_path(self, path, vlan) -> bool:
        """
        Ensure given VLAN is consistently assigned to every node on the path.
        """

        for node in path:
            if vlan not in self.segmentation.get_vlans(node):
                return False
        return True
