# Most of the patches in this file are inspired by the standalone rando:
# https://github.com/clementgallet/SWD2Randomizer

import os
import shutil
import random
from typing import Callable, Tuple, Optional, Iterable
from copy import deepcopy
from NetUtils import NetworkItem
from zipfile import ZipFile, ZIP_DEFLATED
from CommonClient import logger, CommonContext
from BaseClasses import ItemClassification
import xml.etree.ElementTree as et

from .game_data import (in_game_item_data, ap_item_to_in_game_name, door_source_regions, cave_doors,
                        COG_COSTS, EXTRA_COG_COSTS, shop_item_data, cog_item, ore_entity, gem_entity)
from .names import option_name, item_name, location_name, entrance_name
from . import options
from .items import item_table, lookup_id_to_name, ItemType
from .regions import REGIONS
from .client_util import *

import zlib


def patch_files(ctx: ClientContextData):
    bundle_dir = os.path.join(ctx.game_dir, "Bundle")
    data_dir = os.path.join(bundle_dir, "data01")

    non_data_files: List[str] = extract_game_files(ctx.game_dir)

    # Convenience patches
    patch_quests(data_dir)
    patch_damage_types(data_dir)
    patch_levels(data_dir)
    patch_resources(data_dir, ctx)
    language_lines_to_add, offworld_item_names = patch_blueprints(data_dir, ctx)
    patch_entities(data_dir, offworld_item_names)

    patch_start_location_and_inventory(data_dir, ctx)

    # Patches for items
    patch_patchsets(bundle_dir, ctx)

    patch_lang_file(bundle_dir, language_lines_to_add)

    pack_game_files(ctx.game_dir, non_data_files)


non_data_files_that_need_patching = [
    os.path.join("Patchsets", "TempleOfGuidance", "temple_of_guidance.le.z"),
    os.path.join("Language", "en.csv.z"),
]


def extract_game_files(game_dir: str):
    bundle_dir = os.path.join(game_dir, "Bundle")
    data_dir = os.path.join(bundle_dir, "data01")
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)

    impak_file = os.path.join(bundle_dir, "data01.impak")

    original_data_file = impak_file + ".orig"
    if not os.path.exists(original_data_file):
        # Back up the vanilla data file
        shutil.copy(impak_file, original_data_file)
    else:
        # Restore the vanilla data file. TODO: don't restore if the randomized game is being resumed
        # shutil.copy(original_data_file, impak_file)
        # os.remove(impak_file)
        pass

    data_zip_path = impak_file + ".zip"
    shutil.copy(original_data_file, data_zip_path)
    with open(data_zip_path, "rb") as data_zip_stream:
        with ZipFile(data_zip_stream, "r", compression=ZIP_DEFLATED) as data_zip:
            for member in data_zip.infolist():
                data_zip.extract(member, path=data_dir)

    non_data_files: List[str] = []
    for non_data_file in non_data_files_that_need_patching:
        file_path = os.path.join(bundle_dir, non_data_file)
        non_data_files.append(extract_file(file_path))
    return non_data_files


def pack_game_files(game_dir: str, non_data_files: List[str]):
    bundle_dir = os.path.join(game_dir, "Bundle")
    data_dir = os.path.join(bundle_dir, "data01")
    impak_file = os.path.join(bundle_dir, "data01.impak")
    if os.path.exists(impak_file):
        os.remove(impak_file)
    shutil.make_archive(impak_file, "zip", data_dir)
    shutil.move(impak_file + ".zip", impak_file)

    for non_data_info in non_data_files:
        compress_file(non_data_info)


def patch_lang_file(bundle_dir: str, language_lines_to_add: Iterable[tuple[str, str]]):
    language_dir = os.path.join(bundle_dir, "Language")
    decomp_language_file = os.path.join(language_dir, "en.csv")

    lines_to_add = [
        ("apitem", "Archipelago Item"),
        ("upgrade_cog_desc", "Used to enable Cog Mods."),
        ("upgrade_cog_flavor", "\"\"\"Upgrades, people, upgrades!\"\"\""),
        *language_lines_to_add
    ]

    with open(decomp_language_file, "a") as csv_writer:
        for line in lines_to_add:
            csv_writer.write(f"{line[0]}\t{line[1]}\n")


def patch_start_location_and_inventory(data_dir: str, ctx_data: ClientContextData):
    slot_data: Dict[str, Any] = ctx_data.slot_data
    items_received: list[NetworkItem] = ctx_data.items_received

    outsets_file = os.path.join(data_dir, "Definitions", "outsets.xml")
    outsets_doc = et.parse(outsets_file)
    outsets_root = outsets_doc.getroot()

    start_location: int = slot_data[option_name.start_location]
    start_location_data = {
        options.StartLocation.option_vanilla: "west_desert",
        options.StartLocation.option_el_machino: "el_machino",
        options.StartLocation.option_the_oasis: "the_hub",
        options.StartLocation.option_temple_of_the_destroyer: "fire_temple",
    }

    start_inventory: list[int] = [item.item for item in items_received if item.location == -2]
    # Add default items to the dict
    start_items: Dict[str, int] = {
        item_name.lamp: 2,
        item_name.armor: 1,
        item_name.pickaxe: 1,
        item_name.backpack: 1,
        item_name.tank: 1,
        "fate": 1,
        "buddy": 1,
        "minimap": 1,
        "minimap.quest_pointer": 1,
        # "ap_upgrades": 1,
    }
    for item_id in start_inventory:
        if item_id not in start_items:
            start_items[lookup_id_to_name[item_id]] = 0
        start_items[lookup_id_to_name[item_id]] += 1
    # Hack testing full mobility, remove for release
    start_items.update({
        # item_name.armor: 6,
        item_name.sprint: 1,
        item_name.bomb: 1,
        item_name.jackhammer: 1,
        item_name.jetengine: 1,
        item_name.hookshot: 1,
        item_name.up_lamp_secret_sight: 1,
    })
    cogs = start_inventory.count(item_table[item_name.cog].code)
    money: int = slot_data[option_name.starting_money]
    level: int = slot_data[option_name.starting_level]

    new_game_outset = outsets_root.find(".//Outset[@Name='new_game']")
    new_game_outset.find(".//Level").text = start_location_data[start_location]
    # new_game_outset.find(".//Level").text = "yarrow_cave_run"
    # new_game_outset.find(".//Level").text = "west_desert"
    # new_game_outset.find(".//Level").text = "temple_of_guidance"
    # new_game_outset.find(".//Level").text = "archaea_cave_cactus"
    # entrance_node = et.Element("Entrance")
    # entrance_node.text = "outside_temple_spawnpoint"
    # new_game_outset.append(entrance_node)
    # Handle start-inventory
    new_game_outset.find(".//Money").text = str(money)
    new_game_outset.find(".//Cogs").text = str(cogs)
    # Remove starting upgrades
    for upgrade in list(new_game_outset.findall(".//Upgrade")):
        new_game_outset.remove(upgrade)

    start_resources = {}
    for start_item_name, start_count in start_items.items():
        # If the item is an in-game name, we just add it as-is
        if start_item_name not in item_table:
            start_upgrade_node = et.Element("Upgrade")
            start_upgrade_node.attrib["Name"] = start_item_name
            start_upgrade_node.attrib["Tier"] = str(start_count)
            new_game_outset.append(start_upgrade_node)
            continue
        start_item_id = item_table[start_item_name].code
        item_type = item_table[start_item_name].item_type
        if item_type == ItemType.Upgrade or item_type == ItemType.Blueprint or item_type == ItemType.ShopUpgrade:
            start_upgrade_node = et.Element("Upgrade")
            start_upgrade_node.attrib["Name"] = ap_item_to_in_game_name[start_item_id]
            start_upgrade_node.attrib["Tier"] = str(start_count)
            new_game_outset.append(start_upgrade_node)
        elif item_type == ItemType.Artifact:
            start_collectible_node = et.Element("Collectible")
            start_collectible_node.text = ap_item_to_in_game_name[start_item_id]
            new_game_outset.append(start_collectible_node)
        elif item_type == ItemType.Resource:
            # Add ores and gems to inventory, orbs do nothing
            resource_name = None
            if start_item_name == item_name.ore_pack:
                resource_name = "resource_gold"
            elif start_item_name == item_name.gem_pack:
                resource_name = "resource_diamond"
            if resource_name is None:
                continue
            # if resource_name not in start_resources:
            #     start_resources[resource_name] = 0
            start_resources[resource_name] = start_count

    if level > 1:
        start_level_node = et.Element("ExperienceLevel")
        start_level_node.text = str(level)
        new_game_outset.append(start_level_node)
    if len(start_resources):
        for res_name, res_count in start_resources.items():
            resource_node = et.Element("Resource")
            resource_node.attrib["Name"] = res_name
            resource_node.attrib["Amount"] = str(res_count)
            new_game_outset.append(resource_node)

    quest_states = [
        ("quest_earthquake", "in_progress"),
        ("quest_lit_the_lamp", "completed"),
        ("quest_enter_temple", "completed"),
        # ("guard_quest_pathfinder_deactivate", "completed"),
        ("quest_tutorial_indicators", "completed"),
        ("quest_find_the_hub", "in_progress"),
        ("quest_workbench_cog_conversation", "completed"),  # For convenience
    ]

    for quest_data in quest_states:
        quest_node = et.Element("Quest")
        quest_node.attrib["State"] = quest_data[1]
        quest_node.text = quest_data[0]
        new_game_outset.append(quest_node)

    # conversations = [
    #     "guard_open_hatch"
    # ]
    # conversations_node = et.Element("Conversations")
    # for conversation in conversations:
    #     conversation_node = et.Element("Conversation")
    #     conversation_node.text = conversation
    #     conversations_node.append(conversation_node)
    # new_game_outset.append(conversations_node)

    outsets_doc.write(outsets_file)


def get_location_from_vanilla_item(vanilla_item: str, locations: Dict[int, NetworkItem]):
    if vanilla_item not in in_game_item_data:
        return None
    loc_id = in_game_item_data[vanilla_item].ap_loc_id
    if loc_id not in locations:
        return None
    return loc_id


def get_randomized_item(vanilla_item: str, locations: Dict[int, NetworkItem]):
    loc_id = get_location_from_vanilla_item(vanilla_item, locations)
    if loc_id is None:
        return None
    network_item = locations[loc_id]
    return ap_item_to_in_game_name[network_item.item] if network_item.item in ap_item_to_in_game_name else f"ap_{loc_id}"


def get_randomized_shop_item(tool_name: str, tier_index: int, locations: Dict[int, NetworkItem]):
    if tier_index >= len(shop_item_data[tool_name]):
        return None
    loc_data = shop_item_data[tool_name][tier_index]
    if loc_data is None:
        return None
    loc_id = loc_data.ap_loc_id
    if loc_id not in locations:
        return None
    network_item = locations[loc_id]
    randomized_item = ap_item_to_in_game_name[network_item.item] if network_item.item in ap_item_to_in_game_name else None
    if randomized_item == cog_item:
        return None
    return randomized_item


def get_randomized_item_at_location(loc_id: int, locations: Dict[int, NetworkItem]):
    if loc_id not in locations:
        return None
    network_item = locations[loc_id]
    return network_item
    # return ap_item_to_in_game_name[network_item.item] if network_item.item in ap_item_to_in_game_name else None


def is_item_upgrade(name: str):
    return name != cog_item and "collectible" not in name and name != ore_entity and name != gem_entity


def patch_patchsets(bundle_dir: str, ctx_data: ClientContextData):
    slot_data: Dict[str, Any] = ctx_data.slot_data
    locations: Dict[int, NetworkItem] = ctx_data.locations_info

    data_dir = os.path.join(bundle_dir, "data01")
    patchsets_dir = os.path.join(data_dir, "Patchsets")
    walk_results = [(dirpath, dirnames, files) for (dirpath, dirnames, files) in os.walk(patchsets_dir)]
    patchset_files: list[str] = []
    for walk in walk_results:
        for file in walk[2]:
            patchset_files.append(os.path.join(walk[0], file))

    # Files that aren't in the data folder that we need to patch
    patchset_files.append(os.path.join(bundle_dir, "Patchsets", "TempleOfGuidance", "temple_of_guidance.le"))

    # These files are going to be custom patched to include various convenience patches from the base rando
    custom_patches: Dict[str, Callable[[et.Element], None]] = {
        os.path.join(patchsets_dir, "WestDesert", "west_desert_intro.le"): patch_intro,
        os.path.join(patchsets_dir, "Archaea", "archaea_patch_entrance.le"): patch_archaea_entrance,
        os.path.join(patchsets_dir, "TheHub", "the_hub_patch_main.le"): patch_oasis,
        os.path.join(patchsets_dir, "Archaea", "archaea_cave_vectron_entrance.le"): patch_vectron,
    }
    return_tubes: List[Tuple[str, int, int]] = [
        ("temple_of_guidance.le", -240, 0),
        ("archaea_cave_pressurebomb.le", -240, 0),
        ("archaea_cave_jackhammer.le", 240, 0),
        ("the_hub_cave_grapplinghook.le", -240, 0),
        ("archaea_cave_vectron_entrance.le", 240, 0),
        ("temple_of_guidance_2_cave_maze.le", -240, 0),
        ("firetemple_cave_flamer.le", 240, 0),
        ("yarrow_cave_steampack_slayer.le", 240, 0),
    ]

    entrance_swaps: Dict[str, int] = slot_data["Entrance Swaps"]
    randomize_cogs: Dict[str, int] = slot_data["randomize_cogs"]
    randomize_artifacts: Dict[str, int] = slot_data["randomize_artifacts"]
    randomize_ores: Dict[str, int] = slot_data["randomize_ores"]
    for patchset_file in patchset_files:
        patchset_doc = et.parse(patchset_file)
        patchset_root = patchset_doc.getroot()

        if patchset_file in custom_patches:
            custom_patches[patchset_file](patchset_root)

        foreground_node = patchset_root.find(".//TileLayer[Name='Foreground']")
        entity_parent_node = foreground_node.find("Entities")

        sand_tiles_to_add = []  # For randomizing ore/gem blocks
        air_tiles_to_add = []

        # Patch randomized locations
        upgrade_nodes = []
        upgrade_podium_nodes: List[et.Element] = [
            *patchset_root.findall(".//CustomEntity[Definition='upgrade_podium']"),
        ]
        upgrade_nodes.extend(upgrade_podium_nodes)
        upgrade_nodes.extend(patchset_root.findall(".//ScriptEntity[Definition='GiveBlueprint']"))
        for upgrade_node in upgrade_nodes:
            upgrade_value_node = upgrade_node.find(".//Property/Value")
            if upgrade_value_node is None:
                continue
            loc_vanilla_item = upgrade_value_node.text
            # if loc_vanilla_item == "run_boots":  # For testing
            #     # property_name_node = upgrade_node.find(".//Property/Name")
            #     # property_name_node.text = "EditorPickup"
            #     # upgrade_node.find(".//Definition").text = "upgrade_podium_artifact"
            #     randomized_item = cog_item
            # else:
            randomized_item = get_randomized_item(loc_vanilla_item, locations)
            if randomized_item is None:
                logger.error(f"""Could not find a randomized item for vanilla item {loc_vanilla_item}""")
            else:
                if not is_item_upgrade(randomized_item):
                    loc_id = get_location_from_vanilla_item(loc_vanilla_item, locations)
                    # entity_node_name = upgrade_node.find("./Name").text + "_item"
                    entity_node_name = str(loc_id)
                    position = upgrade_node.find("./Position").text
                    if loc_id in { 32579550, 32588814, 32592305 }:  # Make the object spawn normally for the yonker bros
                        new_pos = position
                    else:
                        new_pos = edit_position(position, 0, -60)
                    if randomized_item == cog_item:
                        entity_node = create_custom_entity_node(loc_id * 10, entity_node_name,
                                                                new_pos,
                                                                True,
                                                                "Sprites/General/UpgradeCogContainer/all.png",
                                                                "0, 0, 0.5, 0.5",
                                                                "120, 120",
                                                                "upgrade_cog_container")
                    elif randomized_item == ore_entity or randomized_item == gem_entity:
                        entity_node = create_custom_entity_node(loc_id * 10, entity_node_name,
                                                                new_pos,
                                                                True,
                                                                "Editor/Textures/placeholder_ore.png",
                                                                "0, 0, 0.5, 0.5",
                                                                "120, 120",
                                                                randomized_item)
                        sand_tiles_to_add.append(new_pos)
                    else:  # Artifact
                        entity_node = create_custom_entity_node(loc_id * 10, entity_node_name,
                                                                new_pos,
                                                                True,
                                                                "Editor/Textures/collectible.png",
                                                                "0, 0, 0.5, 0.5",
                                                                "86, 83",
                                                                "pickup_collectible")
                        entity_node.append(create_property_node("EditorPickup", "String", randomized_item))
                    entity_parent_node.append(entity_node)
                    randomized_item = ""
                upgrade_value_node.text = randomized_item

        # Patch freestanding items and ore blocks
        freestanding_nodes = []
        if randomize_cogs:
            freestanding_nodes.extend(patchset_root.findall(".//CustomEntity[Definition='upgrade_cog_container']"))
        if randomize_artifacts:
            freestanding_nodes.extend(patchset_root.findall(".//CustomEntity[Definition='pickup_collectible']"))
        if randomize_ores:
            freestanding_nodes.extend(patchset_root.findall(".//CustomEntity[Definition='placeholder_ore']"))
            freestanding_nodes.extend(patchset_root.findall(".//CustomEntity[Definition='placeholder_gem']"))

        for freestanding_node in freestanding_nodes:
            position_node = freestanding_node.find(".//Position")
            property_node = freestanding_node.find(".//Property")
            asset_name_node = freestanding_node.find(".//AssetName")  # Likely not needed to be set
            size_node = freestanding_node.find(".//Size")
            definition_node = freestanding_node.find(".//Definition")
            has_property_node = property_node is not None
            property_value_node = None
            if has_property_node:
                property_value_node = freestanding_node.find(".//Property/Value")
            was_ore = definition_node.text.startswith("placeholder_")
            # Get item from entity id
            node_id = freestanding_node.find(".//Id").text
            node_loc_id = int(node_id)
            if was_ore:  # This is a hack but all ore locations are prepended with a 1 to avoid collisions
                node_loc_id = int("1" + node_id)
            # Set the name so that the mod knows what location this is
            freestanding_node.find(".//Name").text = str(node_loc_id)
            randomized_item = get_randomized_item_at_location(node_loc_id, locations)
            if randomized_item is None:
                continue
            if randomized_item.item in ap_item_to_in_game_name:
                randomized_item_pickup_name = ap_item_to_in_game_name[randomized_item.item]
            else:
                randomized_item_pickup_name = f"ap_{randomized_item.location}"
            if randomized_item_pickup_name == cog_item:
                asset_name_node.text = "Sprites/General/UpgradeCogContainer/all.png"
                size_node.text = "120, 120"
                definition_node.text = "pickup_upgrade_cog" if was_ore else "upgrade_cog_container"
                if has_property_node:
                    freestanding_node.remove(property_node)
            elif randomized_item_pickup_name == ore_entity or randomized_item_pickup_name == gem_entity:
                asset_name_node.text = "Editor/Textures/placeholder_gem.png"
                size_node.text = "64, 64"
                definition_node.text = randomized_item_pickup_name
                if has_property_node:
                    freestanding_node.remove(property_node)
                if was_ore:
                    was_ore = False
                else:
                    sand_tiles_to_add.append(position_node.text)
            else:
                if "collectible" in randomized_item_pickup_name:
                    asset_name = "Editor/Textures/collectible.png"
                    definition_name = "pickup_collectible"
                elif randomized_item_pickup_name.startswith("ap_"):
                    asset_name = "Editor/Textures/pickup_blueprint.png"
                    definition_name = "ap_item_offworld"
                else:
                    asset_name = "Editor/Textures/pickup_blueprint.png"
                    definition_name = "pickup_blueprint"
                asset_name_node.text = asset_name
                size_node.text = "86, 83"
                definition_node.text = definition_name
                if not has_property_node:
                    property_node = create_property_node()
                    property_value_node = property_node.find(".//Value")
                    freestanding_node.append(property_node)
                property_value_node.text = randomized_item_pickup_name
            if was_ore:
                air_tiles_to_add.append(position_node.text)

        # Change tilemap if ore blocks need to be created/destroyed
        foreground_tilelayer_tile_size = [int(s) for s in foreground_node.find("TileSize").text.split(", ")]
        foreground_tilelayer_offset = [int(s) for s in foreground_node.find("TileOffset").text.split(", ")]
        foreground_tile_mapping_node = foreground_node.find("TileMappings")
        foreground_tiles_node = foreground_node.find("Tiles")
        if len(sand_tiles_to_add) > 0:
            sand_node = foreground_tile_mapping_node.find(".//Mapping[@Name=\"sand\"]")
            if sand_node is not None:
                sand_node_index = list(foreground_tile_mapping_node).index(sand_node)
            else:
                sand_node = et.Element("Mapping", attrib={
                    "Name": "sand",
                    "FlipX": "False",
                    "FlipY": "False",
                    "Rotation": "0",
                })
                sand_node_index = len(foreground_tile_mapping_node)
                foreground_tile_mapping_node.append(sand_node)
            for entity_pos in sand_tiles_to_add:
                tile_pos: list[int] = [int(p) for p in entity_pos.split(", ")]
                tile_pos_x = int(tile_pos[0] / foreground_tilelayer_tile_size[0]) - foreground_tilelayer_offset[0]
                tile_pos_y = int(tile_pos[1] / foreground_tilelayer_tile_size[1]) - foreground_tilelayer_offset[1]
                row_node = foreground_tiles_node[tile_pos_y]
                row_indices = row_node.text.split(" ")
                row_indices[tile_pos_x] = str(sand_node_index)
                row_node.text = " ".join(row_indices)
        if len(air_tiles_to_add) > 0:  # I think air is always index 0 so crossing fingers this works
            for entity_pos in air_tiles_to_add:
                tile_pos: list[int] = [int(p) for p in entity_pos.split(", ")]
                tile_pos_x = int(tile_pos[0] / foreground_tilelayer_tile_size[0] - 0.5) - foreground_tilelayer_offset[0]
                tile_pos_y = int(tile_pos[1] / foreground_tilelayer_tile_size[1] - 0.5) - foreground_tilelayer_offset[1]
                row_node = foreground_tiles_node[tile_pos_y]
                row_indices = row_node.text.split(" ")
                row_indices[tile_pos_x] = "0"
                row_node.text = " ".join(row_indices)

        # Patch entrances
        door_nodes = patchset_root.findall(".//CustomEntity[Definition='door']")
        for door_node in door_nodes:
            dest_entitiy_value_node = door_node.find(".//Property[Name='DestinationEntity']/Value")
            if dest_entitiy_value_node.text not in entrance_name.DOORS:
                continue
            door_index_str = str(entrance_name.DOORS.index(dest_entitiy_value_node.text))
            if door_index_str not in entrance_swaps:
                continue
            dest_level_value_node = door_node.find(".//Property[Name='DestinationLevel']/Value")

            new_door_index = entrance_swaps[door_index_str]
            new_door = entrance_name.DOORS[new_door_index]

            dest_level_value_node.text = entrance_name.door_levels[new_door]
            dest_entitiy_value_node.text = new_door

        # Hack in tubes in upgrade caves to prevent softlocks
        for return_tube_data in return_tubes:
            if patchset_file.endswith(return_tube_data[0]):
                if len(upgrade_podium_nodes):
                    podium_node = upgrade_podium_nodes[0]
                    podium_position = podium_node.find("Position").text
                else:
                    logger.error("Could not find podiums for patchset " + return_tube_data[0])
                    continue
                podium_x_str, podium_y_str = podium_position.split(", ")
                position_str = f"{float(podium_x_str)+return_tube_data[1]}, {float(podium_y_str)+return_tube_data[2]}"
                tube_entity = create_custom_entity_node(999999999, "town_teleporter", position_str, True,
                                                        "Editor/Textures/pneumatic_chamber.png", "0, 0, 0.5, 1",
                                                        "142, 196", "teleporter_ap")
                tube_entity.append(create_property_node("DisableMapPing", "Boolean", "True"))
                entity_parent_node.append(tube_entity)

        patchset_doc.write(patchset_file)

    # Patch artifact blueprints
    collectors_file = os.path.join(bundle_dir, "data01", "Definitions", "collectors.xml")
    collectors_doc = et.parse(collectors_file)
    collectors_root = collectors_doc.getroot()

    reward_nodes = collectors_root.findall(".//Rewards/Reward")
    for reward_node in reward_nodes:
        loc_vanilla_item = reward_node.attrib["Blueprint"]
        randomized_item = get_randomized_item(loc_vanilla_item, locations)
        if randomized_item is None:
            logger.error(f"""Could not find a randomized item for vanilla location {loc_vanilla_item},
                          ap item: {locations[in_game_item_data[loc_vanilla_item].ap_loc_id].item}""")
        else:
            reward_node.attrib["Blueprint"] = randomized_item

    collectors_doc.write(collectors_file)


def patch_quests(data_dir: str):
    # Edit initial quests, might not be needed now that we can manipulate quests from the outsets file?
    quests_file = os.path.join(data_dir, "Definitions", "quests.xml")
    quests_doc = et.parse(quests_file)
    quests_root = quests_doc.getroot()

    SIDE_QUEST = "SIDE_QUEST"

    q_earthquake = quests_root.find(".//Quest[@Name='quest_earthquake']")
    q_earthquake.attrib["Template"] = SIDE_QUEST

    q_temple = quests_root.find(".//Quest[@Name='quest_enter_temple']")
    q_temple.remove(q_temple.find("UnlockedBy"))

    q_fen = quests_root.find(".//Quest[@Name='quest_find_fen']")
    q_fen.attrib["Template"] = SIDE_QUEST
    q_fen.remove(q_fen.find("UnlockedBy"))

    q_release_fen = quests_root.find(".//Quest[@Name='quest_release_fen']")
    q_release_fen.attrib["Template"] = SIDE_QUEST

    q_exit_temple = quests_root.find(".//Quest[@Name='quest_exit_temple']")
    q_exit_temple.find("UnlockedBy").text = "quest_get_run_boots"

    # Remove blockade in the Oasis
    quests_root.remove(quests_root.find(".//Quest[@Name='quest_hub_teleport_blocked']"))
    quests_root.remove(quests_root.find(".//Quest[@Name='quest_see_blockade']"))

    quest_final_node = quests_root.find(".//Quest[@Name='quest_confront_rosie']/UnlockedBy")
    quest_final_node.text = "quest_destroy_all_generators"

    # I hate Vectron so I love the idea of skipping it
    # Also you can't revisit it anyway so even if there were items in it that would cause issues
    quest_vectron_node = quests_root.find(".//Quest[@Name='quest_vectron_helper']")
    child_nodes = [child for child in quest_vectron_node]
    for child in child_nodes:
        if child.tag == "Objective" and child.attrib["Name"] != "obj_outro_conv":
            quest_vectron_node.remove(child)

    quests_doc.write(quests_file)


def patch_damage_types(data_dir: str):
    # Make the ignition axe actually do damage against the priest boss, only does 5% damage for some reason
    damage_types_file = os.path.join(data_dir, "Definitions", "damage_types.xml")
    damage_types_doc = et.parse(damage_types_file)
    damage_types_root = damage_types_doc.getroot()

    priest_dmg_node = damage_types_root.find(".//DamageType[@Name='fire']/Multiplier[@AgainstArmor='priest_glorious']")
    priest_dmg_node.attrib["Value"] = "1"

    damage_types_doc.write(damage_types_file)


def patch_levels(data_dir: str):
    # Open the gate into the Oasis in the beginning
    level_defs_file = os.path.join(data_dir, "Definitions", "levels.xml")
    level_defs_doc = et.parse(level_defs_file)
    level_defs_root = level_defs_doc.getroot()

    filter_intro_node = level_defs_root.find(".//Level[@Name='the_hub']/LayerFilters/Filter[@Layer='filter_intro']")
    filter_intro_node.remove(filter_intro_node[0])
    filter_intro_node.remove(filter_intro_node[0])
    disable_node = et.Element("Disable")
    filter_intro_node.append(disable_node)

    filter_post_node = level_defs_root.find(".//Level[@Name='the_hub']/LayerFilters/Filter[@Layer='filter_post_intro']")
    filter_post_node.remove(filter_post_node[0])
    filter_post_node.remove(filter_post_node[0])
    enable_node = et.Element("Enable")
    filter_post_node.append(enable_node)

    level_defs_doc.write(level_defs_file)


def patch_resources(data_dir: str, ctx: ClientContextData):
    slot_data: Dict[str, Any] = ctx.slot_data
    if slot_data[option_name.shuffle_resources] == 0:
        return
    resources_file = os.path.join(data_dir, "Definitions", "resource_table.xml")
    resources_doc = et.parse(resources_file)
    resources_root = resources_doc.getroot()

    ore_list = []
    gem_list = []

    resource_table = resources_root.find(".//ResourceTable[@Name='default']")
    ore_group = resource_table.find(".//ResourceGroup[@Name='ore']")
    gem_group = resource_table.find(".//ResourceGroup[@Name='gem']")
    for ore_entry in ore_group:
        ore_list.append(ore_entry.attrib["Name"])
    for gem_entry in gem_group:
        gem_list.append(gem_entry.attrib["Name"])

    random.shuffle(ore_list)
    random.shuffle(gem_list)

    for ore_entry in ore_group:
        ore_entry.attrib["Name"] = ore_list.pop()
    for gem_entry in gem_group:
        gem_entry.attrib["Name"] = gem_list.pop()

    resources_doc.write(resources_file)


def patch_intro(intro_patch_root: et.Element):
    # Intro patch

    # Bypass quest_earthquake CheckQuestState and the once node to always make the ground crumble
    earthquake_onenter_node = intro_patch_root.find(".//ScriptEntity[Id='32564401']")
    earthquake_onenter_node.find(".//Connection[TargetId='32564402']/TargetId").text = "32564404"

    # Remove nodes connecting to the intro cutscene
    intro_checkpoint_node = intro_patch_root.find(".//ScriptEntity[Id='32564404']")
    intro_checkpoint_node.find("./Connections").clear()

    # Revove SpecialInteractiveEvent whatever that is
    music_connections_node = intro_patch_root.find(".//ScriptEntity[Id='32586922']/Connections")
    music_connections_node.remove(music_connections_node.find(".//Connection[TargetId='32586789']"))

    # Replace earthquake CheckQuestState node with one that awards the minimap
    # earthquake_quest_check_node = intro_patch_root.find(".//ScriptEntity[Id='32564402']")
    # earthquake_quest_check_node.clear()
    # earthquake_quest_check_node.extend(et.fromstring("""
    # <Node>
    #     <Id>32564402</Id>
    #     <Name>SetUpgrade2</Name>
    #     <Position>1664, 2035</Position>
    #     <Definition>SetUpgrade</Definition>
    #     <Area>1562, 2003, 203, 63</Area>
    #     <Connections>
    #         <Connection>
    #             <SourceContact>out</SourceContact>
    #             <TargetContact>in</TargetContact>
    #         <TargetId>32564403</TargetId>
    #         </Connection>
    #     </Connections>
    #     <Property>
    #         <Name>UpgradeId</Name>
    #         <Type>String</Type>
    #         <Value>minimap</Value>
    #     </Property>
    #     <Property>
    #         <Name>Tier</Name>
    #         <Type>Int32</Type>
    #         <Value>1</Value>
    #     </Property>
    #     <Property>
    #         <Name>HideNewMarker</Name>
    #         <Type>Boolean</Type>
    #         <Value>True</Value>
    #     </Property>
    # </Node>
    # """).findall("*"))

    # Replace the next node (what's a Once node?) with one that completes the light the lamp quest
    # once_node = intro_patch_root.find(".//ScriptEntity[Id='32564403']")
    # once_node.clear()
    # once_node.extend(et.fromstring("""
    # <Node>
    #     <Id>32564403</Id>
    #     <Name>ProgressQuest4</Name>
    #     <Position>1839, 2035</Position>
    #     <Definition>ProgressQuest</Definition>
    #     <Area>1807, 2003, 63, 63</Area>
    #     <Connections>
    #         <Connection>
    #             <SourceContact>out</SourceContact>
    #             <TargetContact>in</TargetContact>
    #             <TargetId>32564404</TargetId>
    #         </Connection>
    #     </Connections>
    #     <Property>
    #         <Name>QuestName</Name>
    #         <Type>String</Type>
    #         <Value>quest_lit_the_lamp</Value>
    #     </Property>
    #     <Property>
    #         <Name>ObjectiveName</Name>
    #         <Type>String</Type>
    #         <Value>obj_lit_the_lamp</Value>
    #     </Property>
    #     <Property>
    #         <Name>Increase</Name>
    #         <Type>Int32</Type>
    #         <Value>1</Value>
    #     </Property>
    # </Node>
    # """).findall("*"))

    # The base rando hacks in a node to automatically complete the arrow trap in the Chamber of Arrows
    # I personally disagree with this but I'll leave a note here in case I want to revert to the base behavior

    # Replace a node with one that sets that you found the hub
    # set_position_node = intro_patch_root.find(".//ScriptEntity[Id='32581848']")
    # set_position_node.clear()
    # set_position_node.extend(et.fromstring("""
    # <Node>
    #     <Id>32581848</Id>
    #     <Name>ProgressQuest5</Name>
    #     <Position>2168, 2036</Position>
    #     <Definition>ProgressQuest</Definition>
    #     <Area>2101, 2004, 132, 63</Area>
    #     <Connections>
    #         <Connection>
    #             <SourceContact>out</SourceContact>
    #             <TargetContact>in</TargetContact>
    #             <TargetId>32566045</TargetId>
    #         </Connection>
    #     </Connections>
    #     <Property>
    #         <Name>QuestName</Name>
    #         <Type>String</Type>
    #         <Value>quest_find_the_hub</Value>
    #     </Property>
    #     <Property>
    #         <Name>ObjectiveName</Name>
    #         <Type>String</Type>
    #         <Value>obj_find_the_hub</Value>
    #     </Property>
    #     <Property>
    #         <Name>Increase</Name>
    #         <Type>Int32</Type>
    #         <Value>1</Value>
    #     </Property>
    # </Node>
    # """).findall("*"))

    # Remove intro cutscene
    # freeze_input_node = intro_patch_root.find(".//ScriptEntity[Id='32566045']")
    # freeze_input_node.clear()
    # freeze_input_node.extend(et.fromstring("""
    # <Node>
    #     <Id>32566045</Id>
    #     <Name>ProgressQuest6</Name>
    #     <Position>2389, 2036</Position>
    #     <Definition>ProgressQuest</Definition>
    #     <Area>2280, 2004, 216, 63</Area>
    #     <Connections/>
    #     <Property>
    #         <Name>QuestName</Name>
    #         <Type>String</Type>
    #         <Value>quest_enter_temple</Value>
    #     </Property>
    #     <Property>
    #         <Name>ObjectiveName</Name>
    #         <Type>String</Type>
    #         <Value>obj_enter_temple</Value>
    #     </Property>
    #     <Property>
    #         <Name>Increase</Name>
    #         <Type>Int32</Type>
    #         <Value>1</Value>
    #     </Property>
    # </Node>
    # """).findall("*"))


def patch_archaea_entrance(archaea_entrance_root: et.Element):
    # Hack the gates to be open by default
    gate_node_ids = [
        "32577658",
        "32577657",
    ]
    for gate_node_id in gate_node_ids:
        archaea_entrance_root.find(f".//CustomEntity[Id='{gate_node_id}']/Property/Value").text = "True"


def patch_oasis(oasis_patch_root: et.Element):
    # Ensure the upper gate to the hookshot room is always open
    gate_node = oasis_patch_root.find(".//CustomEntity[Name='gate_hub_small']")
    gate_node.find(".//Property/Value").text = "True"

    gate_connection_node = oasis_patch_root.find(".//Connection[TargetId='32586635']/..")
    gate_connection_node.remove(gate_connection_node.find(".//Connection[TargetId='32586635']"))

    # Make it so the door to the final boss only opens after destroying all 4 generators
    door_quest_node = oasis_patch_root.find(".//Property[Value='quest_destroy_the_last_generators']")
    door_quest_node.text = "quest_destroy_all_generators"


def patch_vectron(cave_patch_root: et.Element):
    # Create vertical snake tiles so you can access the bottom of the room with the upgrade
    tiles_node = cave_patch_root.find(".//TileLayer[Id='32565491']")
    snake_tile_node = et.Element("Mapping")
    snake_tile_node.attrib["Name"] = "snake_vertical_01"
    snake_tile_node.attrib["FlipX"] = "False"
    snake_tile_node.attrib["FlipY"] = "False"
    snake_tile_node.attrib["Rotation"] = "False"
    tiles_node.find(".//TileMappings").append(snake_tile_node)
    tiles_node.find(".//Tiles")[33].text = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 1 0 0 0 0 0 0 1 17 2 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1"


def get_ap_item_upgrade_name(item: NetworkItem):
    return f"ap_item_{item.item}_{item.player}_{item.flags}"


def get_ap_item_desc_and_flavor(item: NetworkItem, ap_item_player):
    ap_item_desc = ""
    ap_item_flavor = "\"\"\""
    if item.flags & ItemClassification.progression:
        if item.flags & ItemClassification.skip_balancing:
            ap_item_desc += f"A somewhat important item for {ap_item_player}"
            ap_item_flavor += "Probably just a Power Star..."
        elif item.flags & ItemClassification.useful:
            ap_item_desc += f"A very important item for {ap_item_player}"
            ap_item_flavor += "This'll get me out of BK!"
        else:
            ap_item_desc += f"An important item for {ap_item_player}"
            ap_item_flavor += "Gotta have it!"
        if item.flags & ItemClassification.trap:
            ap_item_desc += f", with risky consequences."
            ap_item_flavor = "\"\"\"How important is this, really?"
        else:
            ap_item_desc += f"."
    elif item.flags & ItemClassification.useful:
        if item.flags & ItemClassification.trap:
            ap_item_desc += f"A useful item for {ap_item_player}, with risky consequences."
            ap_item_flavor += "How useful is this, really?"
        else:
            ap_item_desc += f"A useful item for {ap_item_player}."
            ap_item_flavor += "This might be helpful!"
    elif item.flags & ItemClassification.trap:
        ap_item_desc += f"A suspicious item for {ap_item_player}."
        ap_item_flavor += "Do I hear... bees?"
    else:
        ap_item_desc += f"An item for {ap_item_player}."
        ap_item_flavor += "It looks strange, like it's from another world."
    ap_item_flavor += "\"\"\""

    return ap_item_desc, ap_item_flavor


def patch_blueprints(data_dir: str, ctx_data: ClientContextData) -> Tuple[Iterable[Tuple[str, str]], List[str]]:
    slot: int = ctx_data.slot
    slot_data: Dict[str, Any] = ctx_data.slot_data
    locations: Dict[int, NetworkItem] = ctx_data.locations_info
    item_names: CommonContext.NameLookupDict = ctx_data.item_names
    player_names: Dict[int, str] = ctx_data.player_names

    shop_cost_min: int = slot_data[option_name.shop_cost_min]
    shop_cost_max: int = slot_data[option_name.shop_cost_max]

    def modify_cost(cost: int):
        cost_mod = random.randint(shop_cost_min, shop_cost_max)
        return int(int(cost)*cost_mod/100)

    # Reduce the cost to buy the triple grenade blueprint
    prices_file = os.path.join(data_dir, "Definitions", "pricelists.xml")
    prices_doc = et.parse(prices_file)
    prices_root = prices_doc.getroot()

    # Randomize Carson's cog costs
    # carson_costs_node = prices_root.find(".//PriceList[@Name='carson_cogs']/Prices")
    # cost_strings = carson_costs_node.text.split(", ")
    # new_cost_string = ""
    # for cost_string in cost_strings:
    #     new_cost = modify_cost(int(cost_string))
    #     new_cost_string += str(new_cost) + ", "
    # carson_costs_node.text = new_cost_string[:-2]

    # Reduce cost of the triple grenade blueprint
    triple_blueprint_node = prices_root.find(".//PriceList[@Name='blueprint_vendor_02']/Prices")
    triple_blueprint_node.text = "200"

    prices_doc.write(prices_file)

    # Add categories to blueprints so their names show up properly when receiving them from an upgrade podium
    upgrades_file = os.path.join(data_dir, "Definitions", "upgrades.xml")
    upgrades_doc = et.parse(upgrades_file)
    upgrades_root = upgrades_doc.getroot()
    category_strings = {
        "fate.bloodquest": "upgrade_fate_bloodquest",
        "fate.xpx2": "upgrade_fate_xpx2",
        "fate.explosions": "upgrade_fate_explosions",
        "pressurebomb.launcher_triple": "upgrade_pressurebomb_launcher_triple",

        "minimap.hp_bar": "upgrade_minimap_hp_bar",
        "fate.resource_exploder": "upgrade_minimap_hp_bar",
        "armor.rainbow_orbs": "upgrade_armor_rainbow_orbs",
        "backpack.extra_ore": "upgrade_backpack_extra_ore_01",
        "minimap.mineral_detector": "upgrade_minimap_mineral_detector",
        "pickaxe.enemy_damage_01": "upgrade_pickaxe_enemy_damage_01",
        "watertank.health_regen": "upgrade_watertank_regeneration",
        "fate.hell_cave_sigil": "upgrade_fate_hell_cave_sigil",
    }
    for blueprint, cat_string in category_strings.items():
        node = upgrades_root.find(f".//Upgrade[@Name='{blueprint}']")
        cat_node = et.Element("CategoryStringId")
        cat_node.text = cat_string
        node.append(cat_node)

    # Shop cost rando
    money_cost_nodes = upgrades_root.findall(".//Upgrade/Tier/MoneyCost")
    for money_cost_node in money_cost_nodes:
        money_cost_node.text = str(modify_cost(int(money_cost_node.text)))

    # Cog upgrade shuffle
    use_unused: int = slot_data[option_name.add_unused_cog_upgrades]
    randomize_shops: int = slot_data[option_name.randomize_shops]
    if randomize_shops:
        # (upgrade, [exclude list], [include list])
        items_to_randomize: List[Tuple[str, Optional[List[str]], Optional[List[str]]]] = [
            ("pickaxe", ["pickaxe.fire"], None),
            ("backpack", None, None),
            ("lamp", None, ["lamp.damaging_light"] if use_unused else None),
            ("armor", ["armor.damage_reduction"], None),
            ("watertank", None, ["watertank.water_pickup"] if use_unused else None),
            ("pressurebomb", ["pressurebomb.launcher", "pressurebomb.launcher_triple"],
             ["pressurebomb.increased_radius", "pressurebomb.improved_water"] if use_unused else None),
            ("jackhammer", None, ["jackhammer.shockwave", "jackhammer.improved_water"] if use_unused else None),
            ("steampack", ["steampack.slayer"], None),
        ]
        upgrade_subupgrades: Dict[et.Element, List[str]] = {}
        used_subupgrades = set()
        for upgrade_data in items_to_randomize:
            upgrades = []
            upgrade_node = upgrades_root.find(f".//Upgrade[@Name='{upgrade_data[0]}']")
            upgrade_subupgrades[upgrade_node] = []
            # We're randomizing locked upgrades as actual items, don't remove and add to the available upgrade pool
            # locked_upgrades_node = upgrade_node.find("./LockedUpgrades")
            # if locked_upgrades_node is not None:
            #     for locked_upgrade in [upg for upg in locked_upgrades_node]:
            #         # Skip the upgrade if it's in the exclude list
            #         if upgrade_data[1] is not None and locked_upgrade.attrib["Id"] in upgrade_data[1]:
            #             continue
            #         upgrades.append(locked_upgrade.attrib["Id"])
            #         locked_upgrades_node.remove(locked_upgrade)
            upgrade_tier_nodes = upgrade_node.findall("./Tier")
            available_upgrade_tier_nodes = []
            for upgrade_tier_node in upgrade_tier_nodes:
                # money_cost_node = upgrade_tier_node.find("./MoneyCost")
                sub_upgrade_node = upgrade_tier_node.find("./SubUpgrade")
                # Skip the first tier, only buying a new tier will grant an upgrade
                # if (money_cost_node is None or money_cost_node.text == 0) and sub_upgrade_node is None:
                    # if len(upgrades) != 0:
                    # continue
                available_upgrade_tier_nodes.append(upgrade_tier_node)
                if sub_upgrade_node is None:
                    upgrades.append(None)
                else:
                    upgrades.append(sub_upgrade_node.attrib["Id"])
                    upgrade_subupgrades[upgrade_node].append(sub_upgrade_node.attrib["Id"])
                    upgrade_tier_node.remove(sub_upgrade_node)
            if randomize_shops == 1:  # Shuffle
                # Add upgrades to the list, replacing None's if they exist
                if upgrade_data[2] is not None:
                    for add_upgrade in upgrade_data[2]:
                        for u in range(len(upgrades)):
                            if upgrades[u] is None:
                                upgrades[u] = add_upgrade
                                add_upgrade = None
                                break
                        if add_upgrade is not None:
                            upgrades.append(add_upgrade)
                random.shuffle(upgrades)
                for upgrade_tier_node in available_upgrade_tier_nodes:
                    upgrade = upgrades.pop()
                    if upgrade is not None:
                        sub_node = et.Element("SubUpgrade")
                        sub_node.attrib["Id"] = upgrade
                        upgrade_tier_node.append(sub_node)
            elif randomize_shops == 2:  # Randomize
                for t in range(len(upgrade_tier_nodes)):
                    randomized_item = get_randomized_shop_item(upgrade_data[0], t, locations)
                    if randomized_item is not None:
                        used_subupgrades.add(randomized_item)
                        sub_node = et.Element("SubUpgrade")
                        sub_node.attrib["Id"] = randomized_item
                        upgrade_tier_nodes[t].append(sub_node)
                        if randomized_item in upgrades:
                            upgrades.remove(randomized_item)
        # for upgrade_node, subupgrades in upgrade_subupgrades.items():
        #     # Add remaining items to locked upgrades so they appear when they're unlocked
        #     locked_upgrades_node = upgrade_node.find(".//LockedUpgrades")
        #     if locked_upgrades_node is None:
        #         locked_upgrades_node = et.Element("LockedUpgrades")
        #         upgrade_node.append(locked_upgrades_node)
        #     else:
        #         # Probably remove the locked upgrade nodes, we'll recreate them down below if we need them
        #         # Actually add them to subupgrades?
        #         for locked_upgrade in locked_upgrades_node:
        #             locked_upgrade_id = locked_upgrade.attrib["Id"]
        #             if locked_upgrade_id not in used_subupgrades:
        #                 used_subupgrades.add(locked_upgrade_id)
        #     for subupgrade in subupgrades:
        #         if subupgrade in used_subupgrades:
        #             continue
        #         locked_upgrade_node = et.Element("LockedUpgrade")
        #         locked_upgrade_node.attrib["Id"] = subupgrade
        #         locked_upgrade_node.attrib["AfterTier"] = "100"
        #         locked_upgrades_node.append(locked_upgrade_node)

    # Cog cost randomization
    total_cog_costs = slot_data[option_name.randomize_cog_costs]
    if total_cog_costs != -1:
        cog_costs = dict(COG_COSTS)
        if use_unused:
            cog_costs.update(EXTRA_COG_COSTS)
        new_cog_costs = {cog_upgrade: 0 for cog_upgrade in cog_costs.keys()}
        # Shuffle
        if total_cog_costs == -2:
            cog_cost_values = list(cog_costs.values())
            # print(sum(cog_cost_values))
            random.shuffle(cog_cost_values)
            for cog_upgrade in new_cog_costs.keys():
                new_cog_costs[cog_upgrade] = cog_cost_values.pop()
        else:  # Set max cost
            available_upgrades_to_increase_cost = list(cog_costs.keys())
            while total_cog_costs > 0:
                upgrade_index = random.randint(0, len(available_upgrades_to_increase_cost) - 1)
                new_cog_costs[available_upgrades_to_increase_cost[upgrade_index]] += 1
                if new_cog_costs[available_upgrades_to_increase_cost[upgrade_index]] >= 5:
                    available_upgrades_to_increase_cost.pop(upgrade_index)
                total_cog_costs -= 1
        # Set costs on nodes
        for upgrade_node in upgrades_root:
            cost_node = upgrade_node.find(".//Tier/CogCost")
            if cost_node is None or upgrade_node.attrib["Name"] not in new_cog_costs:
                continue
            cost_node.text = str(new_cog_costs[upgrade_node.attrib["Name"]])

    # Create upgrades for collectibles
    collectibles_file = os.path.join(data_dir, "Definitions", "collectibles.xml")
    collectibles_doc = et.parse(collectibles_file)
    collectibles_root = collectibles_doc.getroot()
    collectibles_nodes = collectibles_root.findall(".//Collectible")
    for collectible_node in collectibles_nodes:
        upgrade_node = create_upgrade_node(collectible_node.attrib["Name"],
                                           collectible_node.find("./NameStringId").text,
                                           collectible_node.find("./DescStringId").text,
                                           collectible_node.find("./FlavorStringId").text,
                                           collectible_node.find("./Icon").text)
        upgrades_root.append(upgrade_node)
    upgrades_root.append(create_upgrade_node(cog_item, "upgrade_cog",
                                             "upgrade_cog_desc",
                                             "upgrade_cog_flavor",
                                             "Icons/Currency/cogs_big"))

    # Create upgrades for other people's items
    # test_root_upgrade = create_upgrade_node("ap_upgrades", "upgrade_cog",
    #                                         "upgrade_cog_desc",
    #                                         "upgrade_cog_flavor",
    #                                         "Icons/Currency/cogs_big", True)
    # upgrades_root.append(test_root_upgrade)
    lang_lines_to_add = []
    name_data_created_items = set()
    offworld_item_names = []
    for _, item in locations.items():
        if item.player != slot:
            name = f"ap_{item.location}"
            offworld_item_names.append(name)
            offworld_item_name = get_ap_item_upgrade_name(item)
            desc = offworld_item_name + "_desc"
            flavor = offworld_item_name + "_flavor"
            offworld_upgrade_node = create_upgrade_node(name,
                                                        offworld_item_name,
                                                        desc,
                                                        flavor,
                                                        "Icons/Currency/cogs_big")
            upgrades_root.append(offworld_upgrade_node)
            if offworld_item_name in name_data_created_items:
                continue
            ap_item_name = item_names.lookup_in_slot(item.item, item.player)
            ap_item_player = player_names[item.player]
            ap_item_display_name = f"{ap_item_player}'s {ap_item_name}"
            ap_item_desc, ap_item_flavor = get_ap_item_desc_and_flavor(item, ap_item_player)
            lang_lines_to_add.extend([
                (offworld_item_name, ap_item_display_name),
                (desc, ap_item_desc),
                (flavor, ap_item_flavor),
            ])
            name_data_created_items.add(offworld_item_name)
    # ap_locked_upgrades_node = et.Element("LockedUpgrades")
    # for ap_upgrade in offworld_item_names:
    #     ap_locked_upgrades_node.append(create_node_with_attributes("LockedUpgrade", {"Id": ap_upgrade}))
    # test_root_upgrade.append(ap_locked_upgrades_node)

    upgrades_doc.write(upgrades_file)

    return lang_lines_to_add, offworld_item_names


def patch_entities(data_dir: str, offworld_item_names: List[str]):
    pickups_file = os.path.join(data_dir, "Definitions", "entities.pickups.xml")
    pickups_doc = et.parse(pickups_file)
    pickups_root = pickups_doc.getroot()

    # Edit sprite of freestanding blueprints
    pickup_blueprint_node = pickups_root.find(".//Entity[@Name='pickup_blueprint']")
    blueprint_rigid_character_node = pickup_blueprint_node.find("./RigidCharacter/File")
    # blueprint_rigid_character_node.text = "Sprites/Pickups/ResourceBloodstone/resource_bloodstone.irc2"  # Default
    # blueprint_rigid_character_node.text = "Sprites/Pickups/ResourceSodium/resource_sodium.irc2"  # Off center, vertic.
    # blueprint_rigid_character_node.text = "Sprites/Archaea/Dummy/SteamEngine_RustyCog.irc2"  # Too large but looks ok
    # blueprint_rigid_character_node.text = "Sprites/ElMachino/cog_01.irc2"  # Also too large, a lighter color
    blueprint_rigid_character_node.text = "Sprites/ElMachino/cog_03.irc2"  # Not a bad size, lightish color
    # blueprint_rigid_character_node.text = "Icons/Symbols/upgrade_arrow"
    # blueprint_rigid_character_node.text = "Icons/Symbols/upgrade_arrow_frozen"
    # blueprint_rigid_character_node.text = "$sym_215"  # In game_menus

    # Add custom archipelago pickups when we get around to making them
    ap_offworld_item_node = deepcopy(pickup_blueprint_node)
    ap_offworld_item_node.attrib["Name"] = "ap_item_offworld"
    ap_rigid_character_node = ap_offworld_item_node.find("./RigidCharacter/File")
    ap_rigid_character_node.text = "Sprites/FireTemple/cog_03.irc2"
    ap_offworld_item_node.find("./LightComponent/Color").text = "1.0, 1.0, 1.0"
    pickups_root.append(ap_offworld_item_node)

    pickups_doc.write(pickups_file)

    editor_pickups_file = os.path.join(data_dir, "Definitions", "editor_pickups.xml")
    editor_pickups_doc = et.parse(editor_pickups_file)
    editor_pickups_root = editor_pickups_doc.getroot()

    editor_pickup_entries_to_add = [
        *in_game_item_data.keys(),
        *offworld_item_names,
    ]
    # Add custom blueprint pickup items
    for editor_string in editor_pickup_entries_to_add:
        if "collectible" in editor_string:
            continue
        editor_pickup_node = et.Element("EditorPickup")
        editor_pickup_node.attrib["Name"] = editor_string
        value_node = et.Element("Value")
        value_node.text = editor_string
        editor_pickup_node.append(value_node)
        editor_pickups_root.append(editor_pickup_node)

    editor_pickups_doc.write(editor_pickups_file)

    objects_file = os.path.join(data_dir, "Definitions", "entities.objects.xml")
    objects_doc = et.parse(objects_file)
    objects_root = objects_doc.getroot()

    teleporter_ap_object = deepcopy(objects_root.find("./Entity[@Name='teleporter']"))
    teleporter_ap_object.attrib["Name"] = "teleporter_ap"
    teleporter_blocker_info = teleporter_ap_object.find("./Blocker")
    teleporter_blocker_info.find("./ThemedBlockerEntities").clear()
    # teleporter_blocker_info.find("./UnblockBanner").attrib["IsTeleporter"] = "false"
    # teleporter_ap_object.remove(teleporter_blocker_info)
    objects_root.append(teleporter_ap_object)

    objects_doc.write(objects_file)


def extract_file(file_path: str):
    output_file = file_path[:-2]
    backup_file = file_path + ".orig"
    if os.path.exists(backup_file):
        file_path = backup_file
    with open(file_path, "rb") as lang_file_stream:
        lang_file_stream.read(4)
        lang_bytes = lang_file_stream.read()
        output_bytes = zlib.decompress(lang_bytes)
        with open(output_file, "wb") as test:
            test.write(output_bytes)
    return output_file


def compress_file(file_path: str):
    # Backup original zip file
    target_file = file_path + ".z"
    backup_file = target_file + ".orig"
    if not os.path.exists(backup_file):
        shutil.copy(target_file, backup_file)

    with open(file_path, "rb") as lang_file_stream:
        file_bytes = lang_file_stream.read()
        prefix_bytes = len(file_bytes).to_bytes(4, "little", signed=False)
        compress_bytes = prefix_bytes + zlib.compress(file_bytes, 9)
        with open(target_file, "wb") as zip_writer:
            zip_writer.write(compress_bytes)
