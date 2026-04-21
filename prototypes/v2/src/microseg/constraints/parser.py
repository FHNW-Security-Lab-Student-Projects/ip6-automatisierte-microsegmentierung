import json
from typing import List

from .types import ConstraintType
from .models import (
    AllowConstraint,
    DenyConstraint,
    LocatedAtConstraint,
    ConnectedConstraint,
)
from .base import Constraint


def parse_constraints(file_path: str) -> List[Constraint]:
    """
    Load constraints from JSON and map each entry to its Constraint subclass
    based on the "type" field. Expects required keys per type.

    Raises ValueError for unknown types.
    """

    with open(file_path, "r") as f:
        data = json.load(f)

    constraints = []

    for item in data["constraints"]:
        ctype = ConstraintType(item["type"])

        if ctype == ConstraintType.ALLOW:
            constraints.append(AllowConstraint(item["src"], item["dst"]))

        elif ctype == ConstraintType.DENY:
            constraints.append(DenyConstraint(item["src"], item["dst"]))

        elif ctype == ConstraintType.LOCATED_AT:
            constraints.append(LocatedAtConstraint(item["node"], item["switch"]))

        elif ctype == ConstraintType.CONNECTED:
            constraints.append(ConnectedConstraint(item["node_a"], item["node_b"]))

        else:
            raise ValueError(f"Unknown constraint type: {ctype}")

    return constraints


def group_constraints(constraints):
    """
    Group Constraint objects by their lowercase type name.

    Returns a dict like {"allow": [...], "deny": [...], ...}.
    """

    grouped = {}

    for c in constraints:
        key = c.type.value.lower()  # "allow", "deny", ...
        grouped.setdefault(key, []).append(c)

    return grouped
