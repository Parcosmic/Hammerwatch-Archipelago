from typing import Any
import xml.etree.ElementTree as et
from NetUtils import NetworkItem
from CommonClient import CommonContext


class ClientContextData:
    game_dir: str
    slot: int
    slot_data: dict[str, Any]
    items_received: list[NetworkItem]
    locations_info: dict[int, NetworkItem]
    item_names: CommonContext.NameLookupDict
    location_names: CommonContext.NameLookupDict
    player_names: dict[int, str]

    def __init__(self, game_dir: str, slot: int, slot_data: dict[str, Any], items_received: list[NetworkItem],
                 locations_info: dict[int, NetworkItem], item_names: CommonContext.NameLookupDict,
                 location_names: CommonContext.NameLookupDict, player_names: dict[int, str]):
        self.game_dir = game_dir
        self.slot = slot
        self.slot_data = slot_data
        self.items_received = items_received
        self.locations_info = locations_info
        self.item_names = item_names
        self.location_names = location_names
        self.player_names = player_names


def create_node(node_name: str, name: str = None, text: str = None):
    node = et.Element(node_name)
    if name is not None:
        node.attrib["Name"] = name
    if text is not None:
        node.text = text
    return node


def create_node_with_attributes(node_name: str, attributes: dict[str, str]):
    node = et.Element(node_name)
    for attrib, value in attributes.items():
        node.attrib[attrib] = value
    return node


def create_property_node(name: str = "EditorPickup", type_string: str = "String", value: str = "collectible_01"):
    property_node = et.Element("Property")
    property_node.append(create_node("Name", None, name))
    property_node.append(create_node("Type", None, type_string))
    property_node.append(create_node("Value", None, value))
    return property_node


def create_connection_node(source_contact: str, target_contact: str, target_id: str):
    property_node = et.Element("Connection")
    property_node.append(create_node("SourceContact", None, source_contact))
    property_node.append(create_node("TargetContact", None, target_contact))
    property_node.append(create_node("TargetId", None, target_id))
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


def create_ap_spawner_node(entity_id: int, name: str, position: str, entity: str):
    ap_spawner_node = create_custom_entity_node(entity_id, name, position, True,
                                                "Editor/Textures/generic_spawner.png", "0, 0, 0.5, 0.5",
                                                "150, 150", "spawner_ap")
    ap_spawner_node.append(create_property_node("Entity", "String", entity))
    return ap_spawner_node


def create_script_entity_node_base(entity_id: int, name: str, position: str, definition: str, area: str):
    script_node = et.Element("ScriptEntity")
    script_node.append(create_node("Id", None, str(entity_id)))
    script_node.append(create_node("Name", None, name))
    script_node.append(create_node("Position", None, position))
    script_node.append(create_node("Definition", None, definition))
    script_node.append(create_node("Area", None, area))
    return script_node


def create_shape_entity_node(entity_id: int, name: str, position: str, shape: str, origin: str = "0, 0, 0, 0"):
    script_node = et.Element("ShapeEntity")
    script_node.append(create_node("Id", None, str(entity_id)))
    script_node.append(create_node("Name", None, name))
    script_node.append(create_node("Position", None, position))
    script_node.append(create_node("Shape", None, shape))  # Point
    script_node.append(create_node("Origin", None, origin))
    script_node.append(create_node("Color", None, "255, 0, 0, 255"))
    return script_node


def create_give_valuables_node(entity_id: int, position: str, area: str, health: float = 0, money: int = 0, cogs: int = 0,
                               light: float = 0, water: float = 0, diesel: float = 0, silent: bool = False):
    script_node = create_script_entity_node_base(entity_id, "GiveValuables", position, "GiveValuables", area)
    script_node.append(create_node("Connections"))
    script_node.append(create_property_node("Health", "Single", str(health)))
    script_node.append(create_property_node("Money", "Int32", str(money)))
    script_node.append(create_property_node("Cogs", "Int32", str(cogs)))
    script_node.append(create_property_node("Light", "Single", str(light)))
    script_node.append(create_property_node("Water", "Single", str(water)))
    script_node.append(create_property_node("Diesel", "Single", str(diesel)))
    script_node.append(create_property_node("Silent", "Boolean", str(silent)))
    return script_node


def create_give_blueprint_node(entity_id: int, position: str, area: str, upgrade_id: str):
    script_node = create_script_entity_node_base(entity_id, "GiveBlueprint", position, "GiveBlueprint", area)
    script_node.append(create_node("Connections"))
    script_node.append(create_property_node("UpgradeId", "String", upgrade_id))
    return script_node


def create_give_upgrade_node(entity_id: int, position: str, area: str, upgrade_id: str, require_payment: bool = False):
    script_node = create_script_entity_node_base(entity_id, "GiveUpgrade", position, "GiveUpgrade", area)
    script_node.append(create_node("Connections"))
    script_node.append(create_property_node("UpgradeId", "String", upgrade_id))
    script_node.append(create_property_node("RequirePayment", "Boolean", str(require_payment)))
    return script_node


def create_on_activated_node(entity_id: int, position: str, area: str, source_id: int, out_ids: list[int]):
    script_node = create_script_entity_node_base(entity_id, "OnActivated", position, "OnActivated", area)
    connections_node = create_node("Connections")
    connections_node.append(create_connection_node("entity", "", str(source_id)))
    for out_id in out_ids:
        connections_node.append(create_connection_node("out", "in", str(out_id)))
    script_node.append(connections_node)
    return script_node


def create_on_destroyed_node(entity_id: int, position: str, area: str, source_id: int, out_ids: list[int]):
    script_node = create_script_entity_node_base(entity_id, "OnDestroyed", position, "OnDestroyed", area)
    connections_node = create_node("Connections")
    connections_node.append(create_connection_node("entity", "", str(source_id)))
    for out_id in out_ids:
        connections_node.append(create_connection_node("out", "in", str(out_id)))
    script_node.append(connections_node)
    return script_node


def create_delay_node(entity_id: int, position: str, area: str, delay: float, out_ids: list[int]):
    script_node = create_script_entity_node_base(entity_id, "Delay", position, "Delay", area)
    connections_node = create_node("Connections")
    for out_id in out_ids:
        connections_node.append(create_connection_node("out", "in", str(out_id)))
    script_node.append(connections_node)
    script_node.append(create_property_node("Delay", "Single", str(delay)))
    return script_node


def create_toggle_node(entity_id: int, position: str, area: str, target_id: int, out_ids: list[int]):
    script_node = create_script_entity_node_base(entity_id, "ToggleEntity", position, "ToggleEntity", area)
    connections_node = create_node("Connections")
    connections_node.append(create_connection_node("entity", "", str(target_id)))
    for out_id in out_ids:
        connections_node.append(create_connection_node("out", "in", str(out_id)))
    script_node.append(connections_node)
    return script_node


def create_on_tile_destroyed_node(entity_id: int, position: str, area: str, shape_id: int, out_ids: list[int]):
    script_node = create_script_entity_node_base(entity_id, "OnTileDestroyed", position, "OnTileDestroyed", area)
    connections_node = create_node("Connections")
    connections_node.append(create_connection_node("shape", "", str(shape_id)))
    for out_id in out_ids:
        connections_node.append(create_connection_node("out", "in", str(out_id)))
    script_node.append(connections_node)
    return script_node


def edit_position(position: str, adjust_x: float, adjust_y: float):
    pos_splits = position.split(", ")
    pos_x = float(pos_splits[0])
    pos_y = float(pos_splits[1])
    return f"{pos_x + adjust_x}, {pos_y + adjust_y}"
