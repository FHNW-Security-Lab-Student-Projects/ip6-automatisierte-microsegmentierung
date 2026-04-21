from collections import defaultdict


class SegmentationResult:
    def __init__(self):
        """
        Store bidirectional mappings: node→VLANs and VLAN→nodes.
        Uses defaultdicts for convenient incremental updates.
        """

        self.node_to_vlans = defaultdict(set)
        self.vlan_to_nodes = defaultdict(list)

    def assign(self, node: str, vlan: int):
        """
        Assign a VLAN to a node (adds to node→VLAN mapping).
        Reverse mapping is built later via finalize().
        """

        self.node_to_vlans[node].add(vlan)

    def get_vlans(self, node: str):
        """
        Return VLANs assigned to a node; empty set if none.
        """

        return self.node_to_vlans.get(node, set())

    def finalize(self):
        """
        Build VLAN→nodes mapping from node→VLANs.
        Should be called after all assignments are complete.
        """

        self.vlan_to_nodes.clear()

        for node, vlans in self.node_to_vlans.items():
            for vlan in vlans:
                self.vlan_to_nodes[vlan].append(node)

    def get_nodes_in_vlan(self, vlan: int):
        """
        Return list of nodes in a VLAN; empty list if none.
        """

        return self.vlan_to_nodes.get(vlan, [])

    def __str__(self):
        """
        Return a readable string of VLANs and their sorted node lists.
        """

        output = []

        for vlan in sorted(self.vlan_to_nodes.keys()):
            nodes = sorted(self.vlan_to_nodes[vlan])
            output.append(f"VLAN {vlan}: {nodes}")

        return "\n".join(output)
