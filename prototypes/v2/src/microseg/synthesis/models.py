from collections import defaultdict


class SegmentationResult:
    def __init__(self):
        self.node_to_vlans = defaultdict(set)
        self.vlan_to_nodes = defaultdict(list)

    # -------------------------
    # Assign VLAN to node
    # -------------------------
    def assign(self, node: str, vlan: int):
        self.node_to_vlans[node].add(vlan)

    # -------------------------
    # Get VLANs of a node
    # -------------------------
    def get_vlans(self, node: str):
        return self.node_to_vlans.get(node, set())

    # -------------------------
    # Build reverse mapping
    # -------------------------
    def finalize(self):
        self.vlan_to_nodes.clear()

        for node, vlans in self.node_to_vlans.items():
            for vlan in vlans:
                self.vlan_to_nodes[vlan].append(node)

    # -------------------------
    # Optional helper
    # -------------------------
    def get_nodes_in_vlan(self, vlan: int):
        return self.vlan_to_nodes.get(vlan, [])

    # -------------------------
    # Pretty print
    # -------------------------
    def __str__(self):
        output = []

        for vlan in sorted(self.vlan_to_nodes.keys()):
            nodes = sorted(self.vlan_to_nodes[vlan])
            output.append(f"VLAN {vlan}: {nodes}")

        return "\n".join(output)
