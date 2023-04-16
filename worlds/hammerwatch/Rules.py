import math
import typing

from BaseClasses import MultiWorld
from .Names import CastleLocationNames, CastleRegionNames, TempleLocationNames, TempleRegionNames, ItemName
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from .Regions import HWEntrance
from .Util import *


def set_rules(multiworld: MultiWorld, player: int, item_counts: typing.Dict[str, int]):
    multiworld.completion_condition[player] = lambda state: state.has(ItemName.ev_victory, player)

    set_door_access_rules(multiworld, player, item_counts)

    # It's kinda mean to make players get their last planks during the final boss, or even after when they're not sure
    # if they can beat their game
    if get_campaign(multiworld, player) == Campaign.Castle:
        if get_goal_type(multiworld, player) == GoalType.FullCompletion:
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
    else:
        # Set access rules for portal activation events
        def portal_rule(state) -> bool:
            return state.has(ItemName.key_teleport, player, 6)

        add_rule(multiworld.get_location(TempleLocationNames.ev_c3_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_c2_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_c1_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_t1_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_t2_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_t3_portal, player), portal_rule)


def set_door_access_rules(multiworld: MultiWorld, player: int, item_counts: typing.Dict[str, int]):
    # Set dynamic key/door access rules
    item_names = [
        ItemName.key_bronze,
        ItemName.key_silver,
        ItemName.key_gold,
        ItemName.bonus_key,
        ItemName.mirror,
    ]

    menu_region = multiworld.get_region(CastleRegionNames.menu, player)
    transitions_to_check = menu_region.exits

    # Set downstream costs - the keys that are required after a specific entrance
    for item in item_names:
        set_downstream_costs(item, menu_region.exits[0])

    while len(transitions_to_check) > 0:
        transitions = transitions_to_check.copy()
        transitions_to_check = []
        for exit in transitions:
            if exit.pass_item is None:
                continue
            # If the items are consumed gotta use the downstream cost logic
            if exit.items_consumed:
                needed_keys = item_counts[exit.pass_item] - exit.item_count + 1
                exit.access_rule = lambda state, num=needed_keys: state.has(exit.pass_item, player, num)
            else:  # Elsewise just set the item rule normally
                exit.access_rule = lambda state: state.has(exit.pass_item, player, exit.item_count)
            transitions.extend(exit.connected_region.exits)


def set_downstream_costs(item: str, entrance: HWEntrance, seen=None):
    if seen is None:
        seen = []
    cost = 0
    for exit in entrance.connected_region.exits:
        if exit in seen:
            continue
        seen.append(exit)
        cost += set_downstream_costs(item, exit, seen)
    if entrance.pass_item == item:
        cost += entrance.item_count
        entrance.downstream_count = cost
    return cost
