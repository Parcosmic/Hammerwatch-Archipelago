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
