from typing import TYPE_CHECKING

from . import options
from .util import Campaign

if TYPE_CHECKING:
    from . import HammerwatchWorld

def set_options_from_slot_data(world: "HammerwatchWorld"):
    if world.is_using_ut and hasattr(world.multiworld, "re_gen_passthrough") and "Hammerwatch" in world.multiworld.re_gen_passthrough:
        world.ut_re_gen_passthrough = world.multiworld.re_gen_passthrough["Hammerwatch"]
        for option in options.client_required_options:
            getattr(world.options, option).value = world.ut_re_gen_passthrough[option]

def get_tracker_world(world: "HammerwatchWorld"):
    tracker_world = default_tracker_world.copy()
    # Castle maps are already in the default tracker world
    if world.campaign == Campaign.Temple:
        world.tracker_world["map_page_maps"] = "maps/maps_temple.json"
        world.tracker_world["map_page_locations"] = "locations/temple_locations.json"
        world.tracker_world["map_page_index"] = get_map_page_index_temple
    return tracker_world

def get_map_page_index_castle(level_id: str) -> int:
    return map_page_indices_castle[level_id] if level_id in map_page_indices_castle else 0

def get_map_page_index_temple(level_id: str) -> int:
    return map_page_indices_temple[level_id] if level_id in map_page_indices_temple else 0

map_page_indices_castle = {
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "10": 9,
    "10b": 0,
    "11": 10,
    "12": 11,
    "bonus_1": 12,
    "bonus_2": 13,
    "bonus_3": 14,
    "bonus_4": 15,
    "boss_1": 16,
    "boss_2": 17,
    "boss_3": 18,
    "boss_4": 19,
    "shop": 20,
}

map_page_indices_temple = {
    "hub": 0,
    "library": 0,
    "c1": 1,
    "c2": 2,
    "c3": 3,
    "passage": 4,
    "t_entrance": 5,
    "t1": 6,
    "t2": 7,
    "t3": 8,
    "boss_1": 9,
    "boss_2": 10,
    "boss_2_special": 10,
    "boss_3": 11,
    "bonus_5": 12,
    "shop": 13,
}

default_tracker_world = {
    "map_page_folder": "HammerwatchTrackerPack",
    "map_page_setting_key": "{team}:{player}:CurrentRegion",
    "map_page_index": get_map_page_index_castle,
    "map_page_maps": ["maps/maps.json"],
    "map_page_locations": ["locations/castle_locations.json"]
}
