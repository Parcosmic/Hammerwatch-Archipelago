import math

from BaseClasses import MultiWorld
from .Names import CastleLocationNames, CastleRegionNames, TempleLocationNames, TempleRegionNames, ItemName
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from .Util import *


def set_rules(multiworld: MultiWorld, player: int):
    multiworld.completion_condition[player] = lambda state: state.has(ItemName.ev_victory, player)

    if get_campaign(multiworld, player) == Campaign.Castle \
            and get_goal_type(multiworld, player) == GoalType.FullCompletion:
        add_rule(multiworld.get_entrance(CastleRegionNames.b4_start, player),
                 lambda state: state.has(ItemName.plank, player, 12))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_1, player),
        #          lambda state: state.has(ItemName.plank, player, 1))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_2, player),
        #          lambda state: state.has(ItemName.plank, player, 2))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_3, player),
        #          lambda state: state.has(ItemName.plank, player, 3))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_4, player),
        #          lambda state: state.has(ItemName.plank, player, 4))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_5, player),
        #          lambda state: state.has(ItemName.plank, player, 5))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_6, player),
        #          lambda state: state.has(ItemName.plank, player, 6))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_7, player),
        #          lambda state: state.has(ItemName.plank, player, 7))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_8, player),
        #          lambda state: state.has(ItemName.plank, player, 8))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_9, player),
        #          lambda state: state.has(ItemName.plank, player, 9))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_10, player),
        #          lambda state: state.has(ItemName.plank, player, 10))
        # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_11, player),
        #          lambda state: state.has(ItemName.plank, player, 11))

