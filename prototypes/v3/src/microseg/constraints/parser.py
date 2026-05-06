import json
from typing import Any, Dict, List

from .types import ConstraintType
from .models import (
    AllowConstraint,
    DenyConstraint,
    LocatedAtConstraint,
    ConnectedConstraint,
)
from .base import Constraint


def parse_constraints(data: Dict[str, Any]) -> List[Constraint]:
    """
    Load constraints from JSON Dict and map each entry to its Constraint subclass
    based on the "type" field. Expects required keys per type.

    Raises ValueError for unknown types.
    """

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


def load_groups(data: Dict[str, Any]) -> dict:
    """
    Load group definitions from JSON Dict.

    Returns:
        dict[str, set[str]] mapping group name to member nodes
    """

    groups = {}

    for g in data.get("groups", []):
        name = g["name"]
        members = set(g["members"])

        groups[name] = members

    return groups


def load_dataset(file_path):
    with open(file_path) as f:
        data = json.load(f)

    constraints = parse_constraints(data)
    groups = load_groups(data)

    return constraints, groups
