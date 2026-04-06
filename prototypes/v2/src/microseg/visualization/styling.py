import random


def generate_vlan_colors(vlans):
    """
    Assign a distinct color to each VLAN.
    """
    random.seed(42)

    colors = {}
    for vlan in sorted(vlans):
        colors[vlan] = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    return colors


def get_node_color(node_id, node_data, segmentation, vlan_colors):
    node_type = node_data.get("type")

    # Switch = always white
    if node_type == "switch":
        return "#ffffff"

    vlans = segmentation.get_vlans(node_id)

    if not vlans:
        return "#cccccc"  # fallback

    # take first VLAN (hosts should only have one)
    vlan = sorted(vlans)[0]

    return vlan_colors.get(vlan, "#cccccc")