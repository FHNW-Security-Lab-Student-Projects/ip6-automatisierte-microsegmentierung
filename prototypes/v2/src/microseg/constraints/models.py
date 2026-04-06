from dataclasses import dataclass
from .base import Constraint
from .types import ConstraintType


@dataclass
class AllowConstraint(Constraint):
    src: str
    dst: str

    def __init__(self, src: str, dst: str):
        super().__init__(ConstraintType.ALLOW)
        self.src = src
        self.dst = dst


@dataclass
class DenyConstraint(Constraint):
    src: str
    dst: str

    def __init__(self, src: str, dst: str):
        super().__init__(ConstraintType.DENY)
        self.src = src
        self.dst = dst


@dataclass
class LocatedAtConstraint(Constraint):
    node: str
    switch: str

    def __init__(self, node: str, switch: str):
        super().__init__(ConstraintType.LOCATED_AT)
        self.node = node
        self.switch = switch


@dataclass
class ConnectedConstraint(Constraint):
    node_a: str
    node_b: str

    def __init__(self, node_a: str, node_b: str):
        super().__init__(ConstraintType.CONNECTED)
        self.node_a = node_a
        self.node_b = node_b
