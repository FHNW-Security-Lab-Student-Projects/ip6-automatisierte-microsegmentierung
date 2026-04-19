from typing import List

from microseg.constraints.models import AllowConstraint, DenyConstraint
from microseg.graph.path_engine import PathEngine
from microseg.validation.models import ValidationResult


class ConstraintValidator:
    def __init__(self, constraints: List, path_engine: PathEngine, segmentation):
        self.constraints = constraints
        self.path_engine = path_engine
        self.segmentation = segmentation

    def validate(self) -> ValidationResult:
        result = ValidationResult()

        self._check_allow(result)
        self._check_deny(result)

        return result

    # -------------------------
    # ALLOW Check
    # -------------------------
    def _check_allow(self, result: ValidationResult):
        for c in self.constraints:
            if not isinstance(c, AllowConstraint):
                continue

            src = c.src
            dst = c.dst

            if not self._is_allowed(src, dst):
                result.allow_violations.append(f"{src} → {dst}")

    # -------------------------
    # DENY Check
    # -------------------------
    def _check_deny(self, result: ValidationResult):
        for c in self.constraints:
            if not isinstance(c, DenyConstraint):
                continue

            src = c.src
            dst = c.dst

            if self._is_allowed(src, dst):
                result.deny_violations.append(f"{src} ↔ {dst}")

    # -------------------------
    # Core Logic
    # -------------------------
    def _is_allowed(self, src: str, dst: str) -> bool:
        path = self.path_engine.get_path(src, dst)

        if not path:
            return False

        # Prüfe ob ein gemeinsames VLAN existiert
        src_vlans = self.segmentation.get_vlans(src)
        dst_vlans = self.segmentation.get_vlans(dst)

        common_vlans = src_vlans.intersection(dst_vlans)

        if not common_vlans:
            return False

        # Prüfe VLAN Propagation entlang des Pfads
        for vlan in common_vlans:
            if self._vlan_valid_on_path(path, vlan):
                return True

        return False

    def _vlan_valid_on_path(self, path, vlan) -> bool:
        for node in path:
            if vlan not in self.segmentation.get_vlans(node):
                return False
        return True