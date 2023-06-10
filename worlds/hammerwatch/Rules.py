import math
import typing

from BaseClasses import MultiWorld, Region
from .Names import CastleLocationNames, CastleRegionNames, TempleLocationNames, TempleRegionNames, ItemName
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from .Regions import HWEntrance
from .Util import *


def set_rules(multiworld: MultiWorld, player: int, door_counts: typing.Dict[str, int]):
    multiworld.completion_condition[player] = lambda state: state.has(ItemName.ev_victory, player)

    menu_region = multiworld.get_region(CastleRegionNames.menu, player)
    if get_campaign(multiworld, player) == Campaign.Castle:
        second_region_name = CastleRegionNames.p1_start
    else:
        second_region_name = TempleRegionNames.hub_main
    second_region = multiworld.get_region(second_region_name, player)
    loop_entrances = prune_entrances(menu_region, second_region)

    set_door_access_rules(multiworld, player, door_counts, loop_entrances)

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


def prune_entrances(start_region: Region, next_region: Region):
    # Find loops
    loops = []
    # The purpose of this list to prevent loops from appearing twice
    loop_ending_region_names = []
    loop_entrances = []

    def cycle_search(node: Region, prev_node: Region, visited: typing.List[Region],
                     visited_entrances: typing.List[HWEntrance]):
        visited.append(node)
        for exit in node.exits:
            if exit.connected_region.name == prev_node.name or exit.connected_region.name == node.name\
                    or exit.connected_region.name in loop_ending_region_names:
                continue
            if exit.connected_region in visited:
                index = visited.index(exit.connected_region)
                current_loop = visited[index:]
                reverse_loop_entr = []
                # Traverse the other way to ensure it's actually a loop
                is_loop = True
                for r in reversed(range(len(current_loop))):
                    is_loop = False
                    for entr in current_loop[r].exits:
                        if current_loop[r-1].name == entr.connected_region.name:
                            is_loop = True
                            reverse_loop_entr.append(entr)
                            break
                    if not is_loop:
                        break
                if not is_loop:
                    continue
                if node.name not in loop_ending_region_names:
                    loop_ending_region_names.append(node.name)
                    loops.append(visited[index:])
                    loop_entr = visited_entrances[index:]
                    loop_entr.append(exit)
                    loop_entrances.append(loop_entr)
                continue
            entrances = visited_entrances.copy()
            entrances.append(exit)
            cycle_search(exit.connected_region, node, visited.copy(), entrances)

    cycle_search(next_region, start_region, [], [])

    # Prune backwards entrances
    seen_region_names = [start_region.name]
    next_regions = [start_region]
    entrances_to_delete = []
    while len(next_regions) > 0:
        regions_to_explore = next_regions.copy()
        next_regions.clear()
        for region in regions_to_explore:
            for entrance in region.exits:
                if entrance.connected_region.name in seen_region_names:
                    if entrance.connected_region.name != region.name:
                        entrances_to_delete.append(entrance)
                    continue
                seen_region_names.append(entrance.connected_region.name)
                next_regions.append(entrance.connected_region)

        while len(entrances_to_delete) > 0:
            # print(f"Deleted {entrances_to_delete[0].parent_region} -> {entrances_to_delete[0].connected_region}")
            delete_entrance(entrances_to_delete.pop(0))

    return loop_entrances


def delete_entrance(entrance: HWEntrance):
    # print(entrance)
    entrance.parent_region.exits.remove(entrance)
    entrance.connected_region.entrances.remove(entrance)
    del entrance


def set_door_access_rules(multiworld: MultiWorld, player: int, door_counts: typing.Dict[str, int],
                          loop_entrances: typing.List[typing.List[HWEntrance]]):
    # Set dynamic key/door access rules
    menu_region = multiworld.get_region(CastleRegionNames.menu, player)
    transitions_to_check = menu_region.exits

    # Remove some entrances and add new ones to make the downstream algo not traverse some paths and to consider some
    # doors as blocking
    def add_entrance(name: str, parent_name: str, to_name: str):
        entr = HWEntrance(player, name, multiworld.get_region(parent_name, player))
        entr.parent_region.exits.append(entr)
        entr.connect(multiworld.get_region(to_name, player))
        return entr
    if get_campaign(multiworld, player) == Campaign.Castle:
        remove_entrances = [
            multiworld.get_entrance(CastleRegionNames.b1_start, player),
            multiworld.get_entrance(CastleRegionNames.b2_start, player),
            multiworld.get_entrance(CastleRegionNames.b3_start, player),
            multiworld.get_entrance(CastleRegionNames.b4_start, player),
        ]
        add_entrances = [
            add_entrance("P1 Boss Switch", CastleRegionNames.p1_from_p3_n, CastleRegionNames.b1_start),
            add_entrance("P3 Boss Switch", CastleRegionNames.p3_s_gold_gate, CastleRegionNames.b1_start),
            add_entrance("A1 Boss Switch", CastleRegionNames.a1_w, CastleRegionNames.b2_start),
            add_entrance("A2 Boss Switch", CastleRegionNames.a2_ne, CastleRegionNames.b2_start),
            add_entrance("R2 Boss Switch", CastleRegionNames.r2_n, CastleRegionNames.b3_start),
            add_entrance("C1 Boss Switch", CastleRegionNames.c2_tp_island, CastleRegionNames.b4_start),
            add_entrance("C2 Boss Switch", CastleRegionNames.c2_c3_tp, CastleRegionNames.b4_start),
            add_entrance("C3 Boss Switch", CastleRegionNames.c3_rspike_switch, CastleRegionNames.b4_start),
        ]
    else:
        remove_entrances = [
            # multiworld.get_entrance('Temple Entrance Back__', player),
        ]
        add_entrances = [
            add_entrance("T3 Psuedo Entrance", TempleRegionNames.t3_s_node_blocks_1,
                         TempleRegionNames.t3_s_node_blocks_2)
        ]
    for remove in remove_entrances:
        remove.parent_region.exits.remove(remove)
        remove.connected_region.entrances.remove(remove)

    # Set downstream costs - the keys that are required after a specific entrance
    key_names = get_key_names(multiworld, player)
    # seen = [(exit.parent_region) for exit in menu_region.exits]
    start_exits = [exit for exit in menu_region.exits if exit.connected_region.name != CastleRegionNames.get_planks]
    # seen_start = [get_entrance_id(exit) for exit in start_exits]
    # seen_start.remove(get_entrance_id(menu_region.exits[0]))
    for item in key_names:
        # seen = seen_start.copy()
        set_downstream_costs(item, start_exits[0], [])

    # Set the downstream count for loops to be 0
    for loop in loop_entrances:
        for entrance in loop:
            if entrance.items_consumed and entrance.pass_item in key_names:
                entrance.downstream_count = 0

    # Re-add removed entrances and remove added ones
    for remove in remove_entrances:
        remove.parent_region.exits.append(remove)
        remove.connected_region.entrances.append(remove)
    for add in add_entrances:
        add.parent_region.exits.remove(add)
        add.connected_region.entrances.remove(add)

    transitions = multiworld.get_entrances()
    for exit in transitions:
        if exit.pass_item is None:
            # print(f"{exit.parent_region} -> {exit.connected_region}")
            continue
        # If the items are consumed gotta use the downstream cost logic
        if exit.items_consumed:
            needed_keys = door_counts[exit.pass_item] - exit.downstream_count
            # print(f"{exit.parent_region} -> {exit.connected_region} - {exit.pass_item}: {needed_keys}")
            add_rule(exit, lambda state, this=exit, num=needed_keys: state.has(this.pass_item, player, num), "and")
        else:  # Elsewise just set the item rule normally
            # print(f"{exit.parent_region} -> {exit.connected_region} - {exit.pass_item}: {exit.item_count}")
            add_rule(exit, lambda state, this=exit: state.has(this.pass_item, player, this.item_count), "and")


def set_downstream_costs(item: str, entrance: HWEntrance, seen):
    seen.append(get_entrance_id(entrance))
    seen = seen.copy()  # Create a copy so that independent pathways don't lock each other
    door_entrances: typing.Set[HWEntrance] = set()
    cost_dict: typing.Dict[HWEntrance] = {}
    cost = 0
    if entrance.parent_region != entrance.connected_region:
        for exit in entrance.connected_region.exits:
            if get_entrance_id(exit) in seen and exit.connected_region.name != exit.parent_region.name:
                continue
            for entr, cost in set_downstream_costs(item, exit, seen).items():
                cost_dict[entr] = cost
            # cost_dict.extend(set_downstream_costs(item, exit, seen))
    if entrance.pass_item == item:
        # Just assume the item count is 1, doors should never cost more
        # cost += entrance.item_count
        door_entrances.add(entrance)
        if entrance.downstream_count == 0:
            for cost in cost_dict.values():
                entrance.downstream_count += cost
        cost_dict[entrance] = entrance.item_count
    return cost_dict.copy()


def get_entrance_id(entrance: HWEntrance):
    if entrance.connected_region.name > entrance.parent_region.name:
        return entrance.parent_region.name, entrance.connected_region.name
    else:
        return entrance.connected_region.name, entrance.parent_region.name
