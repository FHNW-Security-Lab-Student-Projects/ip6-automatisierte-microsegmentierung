from dataclasses import dataclass
from enum import Enum


class NodeType(str, Enum):
    HOST = "host"
    SWITCH = "switch"


@dataclass
class Node:
    id: str
    type: NodeType


@dataclass
class Edge:
    node_a: str
    node_b: str
