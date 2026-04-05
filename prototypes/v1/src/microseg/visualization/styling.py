ROLE_COLOR_MAP = {
    "user": "lightblue",
    "application": "lightgreen",
    "database": "orange",
    "dns": "violet",
    "identity": "violet",
    "fileserver": "violet",
    "mail": "violet",
    "monitoring": "grey",
    "logging": "grey",
    "backup": "grey",
    "firewall": "red",
    "vpn": "red",
}


def get_role_color(role: str) -> str:
    return ROLE_COLOR_MAP.get(role, "white")


def scale_weight(weight: float, *, factor: float = 100.0, min_width: float = 0.0) -> float:
    return max(min_width, weight / factor)