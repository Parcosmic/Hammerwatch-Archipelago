from typing import List, Dict
import xml.etree.ElementTree as et


def create_node(node_name: str, name: str = None, text: str = None):
    node = et.Element(node_name)
    if name is not None:
        node.attrib["Name"] = name
    if text is not None:
        node.text = text
    return node


def create_node_with_attributes(node_name: str, attributes: Dict[str, str]):
    node = et.Element(node_name)
    for attrib, value in attributes.items():
        node.attrib[attrib] = value
    return node


def create_property_node(name: str = "EditorPickup", value: str = "collectible_01"):
    property_node = et.Element("Property")
    property_node.append(create_node("Name", None, name))
    property_node.append(create_node("Type", None, "String"))
    property_node.append(create_node("Value", None, value))
    return property_node


def create_upgrade_node(upgrade_name: str, name_id: str, desc_id: str, flavor_id: str, icon: str):
    upgrade_node = et.Element("Upgrade")
    upgrade_node.attrib["Name"] = upgrade_name
    upgrade_node.append(create_node("CategoryStringId", None, name_id))
    upgrade_node.append(create_node("DescStringId", None, desc_id))
    tier_node = et.Element("Tier")
    tier_node.append(create_node("Icon", None, icon))
    tier_node.append(create_node("NameStringId", None, name_id))
    tier_node.append(create_node("DescStringId", None, flavor_id))
    upgrade_node.append(tier_node)
    return upgrade_node


def create_custom_entity_node(entity_id: int, name: str, position: str, snap_to_tile: bool, asset_name: str,
                              origin: str, size: str, definition: str):
    custom_entity_node = et.Element("CustomEntity")
    custom_entity_node.append(create_node("Id", None, str(entity_id)))
    custom_entity_node.append(create_node("Name", None, name))
    custom_entity_node.append(create_node("Position", None, position))
    custom_entity_node.append(create_node("SnapToTile", None, str(snap_to_tile)))
    custom_entity_node.append(create_node("AssetName", None, asset_name))
    custom_entity_node.append(create_node("Origin", None, origin))
    custom_entity_node.append(create_node("Size", None, size))
    custom_entity_node.append(create_node("Definition", None, definition))
    return custom_entity_node


def edit_position(position: str, adjust_x: float, adjust_y: float):
    pos_splits = position.split(", ")
    pos_x = float(pos_splits[0])
    pos_y = float(pos_splits[1])
    return f"{pos_x + adjust_x}, {pos_y + adjust_y}"
