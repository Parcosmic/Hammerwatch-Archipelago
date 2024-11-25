from typing import List, Tuple, Dict, Set, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import Region, Entrance
from .names import region_name, location_name, item_name
from worlds.generic.Rules import add_rule
from .regions import SWD2Entrance, get_etr_name
from .util import GoalType, get_goal_type, add_loc_item_rule

if TYPE_CHECKING:
    from . import SWD2World


def set_rules(world: "SWD2World"):
    goal = get_goal_type(world)

    if goal == GoalType.FinalBoss:
        world.multiworld.completion_condition[world.player] =\
            lambda state: state.has(item_name.ev_blastoff, world.player)


def get_entrance_id(entrance: SWD2Entrance):
    if entrance.connected_region.name > entrance.parent_region.name:
        return f"{entrance.parent_region.name}, {entrance.connected_region.name}"
    else:
        return f"{entrance.connected_region.name}, {entrance.parent_region.name}"


def get_unique_entrance_id(entrance: SWD2Entrance):
    if entrance.connected_region == entrance.parent_region:
        return entrance.name
    return get_entrance_id(entrance)


def get_entrance(world: "SWD2World", start_region: str, end_region: str) -> SWD2Entrance:
    return world.multiworld.get_entrance(get_etr_name(start_region, end_region), world.player)
