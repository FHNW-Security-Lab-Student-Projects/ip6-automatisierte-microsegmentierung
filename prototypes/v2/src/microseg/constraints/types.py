from enum import Enum


class ConstraintType(str, Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    LOCATED_AT = "LOCATED_AT"
    CONNECTED = "CONNECTED"