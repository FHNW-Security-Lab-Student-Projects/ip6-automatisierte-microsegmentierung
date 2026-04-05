import csv
from pathlib import Path
from typing import List, Dict


# ---------------------------
# Helper
# ---------------------------

def _validate_file(path: str) -> Path:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if not p.is_file():
        raise ValueError(f"Not a file: {path}")
    return p


def _safe_int(value: str, field: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid integer in field '{field}': {value}")


# ---------------------------
# Public API
# ---------------------------

def load_nodes(path: str) -> List[Dict]:
    """
    Load nodes.csv

    Expected columns:
    - node_id
    - node_type
    - role
    """

    file_path = _validate_file(path)

    nodes = []

    with file_path.open(mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required_fields = {"node_id", "node_type", "role"}
        if not required_fields.issubset(reader.fieldnames):
            raise ValueError(
                f"Missing required columns in nodes.csv. "
                f"Expected: {required_fields}, got: {reader.fieldnames}"
            )

        for i, row in enumerate(reader, start=1):
            node_id = row["node_id"].strip()

            if not node_id:
                raise ValueError(f"Empty node_id at line {i}")

            node = {
                "node_id": node_id,
                "node_type": row["node_type"].strip(),
                "role": row["role"].strip(),
            }

            nodes.append(node)

    return nodes


def load_traffic(path: str) -> List[Dict]:
    """
    Load traffic.csv

    Expected columns:
    - source
    - destination
    - protocol
    - port
    - connections
    """

    file_path = _validate_file(path)

    traffic = []

    with file_path.open(mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required_fields = {
            "source",
            "destination",
            "protocol",
            "port",
            "connections",
        }

        if not required_fields.issubset(reader.fieldnames):
            raise ValueError(
                f"Missing required columns in traffic.csv. "
                f"Expected: {required_fields}, got: {reader.fieldnames}"
            )

        for i, row in enumerate(reader, start=1):
            source = row["source"].strip()
            destination = row["destination"].strip()

            if not source or not destination:
                raise ValueError(f"Invalid edge at line {i}: empty source/destination")

            entry = {
                "source": source,
                "destination": destination,
                "protocol": row["protocol"].strip().upper(),
                "port": _safe_int(row["port"], "port"),
                "connections": _safe_int(row["connections"], "connections"),
            }

            traffic.append(entry)

    return traffic