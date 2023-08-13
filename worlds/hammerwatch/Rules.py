import math
import typing

from BaseClasses import MultiWorld, Region
from .Names import CastleLocationNames, CastleRegionNames, TempleLocationNames, TempleRegionNames, EntranceNames
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from .Regions import HWEntrance, etr_base_name
from .Util import *


def set_rules(multiworld: MultiWorld, player: int, door_counts: typing.Dict[str, int]):
    multiworld.completion_condition[player] = lambda state: state.has(ItemName.ev_victory, player)

    set_connections(multiworld, player)

    menu_region = multiworld.get_region(CastleRegionNames.menu, player)
    if get_campaign(multiworld, player) == Campaign.Castle:
        second_region_name = CastleRegionNames.p1_start
    else:
        second_region_name = TempleRegionNames.hub_main
    second_region = multiworld.get_region(second_region_name, player)
    loop_entrances = prune_entrances(menu_region, second_region)

    set_door_access_rules(multiworld, player, door_counts, loop_entrances)

    # It's kinda mean to make players get their last planks or keys during the final boss,
    # or even after when they're not sure if they can beat their game
    if get_campaign(multiworld, player) == Campaign.Castle:
        # Overwrite world completion condition if we need to defeat all bosses
        if get_goal_type(multiworld, player) == GoalType.KillBosses:
            boss_names: typing.Set = {
                ItemName.evc_beat_boss_1,
                ItemName.evc_beat_boss_2,
                ItemName.evc_beat_boss_3,
                ItemName.evc_beat_boss_4,
            }
            multiworld.completion_condition[player] = lambda state: state.has_all(boss_names, player)
        if get_goal_type(multiworld, player) == GoalType.FullCompletion:
            entr_name = etr_base_name(CastleRegionNames.c2_main, CastleRegionNames.b4_start)
            add_rule(multiworld.get_entrance(entr_name, player),
                     lambda state: state.has(ItemName.plank, player, 12)
                                   and state.has(ItemName.key_gold, player, 16)
                                   and state.has(ItemName.key_silver, player, 13)
                                   and state.has(ItemName.key_bronze, player, 103)
                                   and state.has(ItemName.key_bonus, player, 18))
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
        # Overwrite world completion condition if we need to defeat all bosses
        if get_goal_type(multiworld, player) == GoalType.KillBosses:
            boss_names: typing.Set = {
                ItemName.evt_beat_boss_1,
                ItemName.evt_beat_boss_2,
                ItemName.evt_beat_boss_3,
            }
            multiworld.completion_condition[player] = lambda state: state.has_all(boss_names, player)

        # Set access rules for portal activation events
        def portal_rule(state) -> bool:
            return state.has(ItemName.key_teleport, player, 6)

        add_rule(multiworld.get_location(TempleLocationNames.ev_c3_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_c2_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_c1_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_t1_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_t2_portal, player), portal_rule)
        add_rule(multiworld.get_location(TempleLocationNames.ev_t3_portal, player), portal_rule)

        # Extra rules for T1 north node blocks locations
        t1_sun_block_entr = etr_base_name(TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_sun_block_hall)
        add_rule(multiworld.get_entrance(t1_sun_block_entr, player),
                 lambda state: state.has_all([ItemName.evt_t1_n_mirrors, ItemName.evt_t1_s_mirror], player))
        add_rule(multiworld.get_entrance(etr_base_name(TempleRegionNames.t1_east, TempleRegionNames.t1_node_2), player),
                 lambda state: state.has(ItemName.evt_t1_n_mirrors, player))


def set_connections(multiworld, player):
    pass


class EntranceBlockType(Enum):
    Unblocked = 0
    Blocked = 1  # Blocked means you cannot progress without being on the other side, effectively dead end
    DeadEnd = 2


entrance_block_types: typing.Dict[str, EntranceBlockType] = {
    EntranceNames.c_p1_1: EntranceBlockType.DeadEnd,  # Technically not a dead end if shortcut portal is enabled
    EntranceNames.c_p1_2: EntranceBlockType.Unblocked,  # Leads to 3
    EntranceNames.c_p1_3: EntranceBlockType.Unblocked,
    EntranceNames.c_p1_4: EntranceBlockType.DeadEnd,
    EntranceNames.c_p1_10: EntranceBlockType.DeadEnd,
    EntranceNames.c_p1_20: EntranceBlockType.DeadEnd,  # Portal exit, same note as 1 ^
    EntranceNames.c_p2_0: EntranceBlockType.Unblocked,  # Leads to 1, 3 (2 is blocked)
    EntranceNames.c_p2_1: EntranceBlockType.Unblocked,
    EntranceNames.c_p2_2: EntranceBlockType.Unblocked,  # Leads to 0, 1,
    EntranceNames.c_p2_3: EntranceBlockType.Blocked,  # Blocked by South spikes
    EntranceNames.c_p3_0: EntranceBlockType.Unblocked,  # Is blocked from other exits, but leads to 1, 10, b_ent
    EntranceNames.c_p3_1: EntranceBlockType.Blocked,  # Blocked by spikes
    EntranceNames.c_p3_10: EntranceBlockType.Unblocked,  # Leads to 100
    EntranceNames.c_p3_b_return: EntranceBlockType.Unblocked,  # Leads to 10, b_ent, 1
    EntranceNames.c_p3_portal: EntranceBlockType.Unblocked,
    EntranceNames.c_p3_b_ent: EntranceBlockType.Unblocked,
    EntranceNames.c_p3_boss: EntranceBlockType.Unblocked,
    EntranceNames.c_n1_0: EntranceBlockType.Unblocked,
    EntranceNames.c_b1_0: EntranceBlockType.Unblocked,  # Gotta beat the boss though
    EntranceNames.c_b1_1: EntranceBlockType.DeadEnd,  # Technically blocked, but after the wall opens can't move on
    EntranceNames.c_a1_0: EntranceBlockType.Unblocked,
    EntranceNames.c_a1_1: EntranceBlockType.DeadEnd,
    EntranceNames.c_a1_a2: EntranceBlockType.Unblocked,
    EntranceNames.c_a1_a3: EntranceBlockType.Unblocked,
    EntranceNames.c_a1_boss: EntranceBlockType.Unblocked,
    EntranceNames.c_a2_0: EntranceBlockType.Unblocked,
    EntranceNames.c_a2_1: EntranceBlockType.Unblocked,
    EntranceNames.c_a2_2: EntranceBlockType.Blocked,  # Need to push button to open walls
    EntranceNames.c_a2_3: EntranceBlockType.Unblocked,
    EntranceNames.c_a2_10: EntranceBlockType.Unblocked,
    EntranceNames.c_a2_88: EntranceBlockType.Unblocked,
    EntranceNames.c_a3_0: EntranceBlockType.Unblocked,
    EntranceNames.c_a3_1: EntranceBlockType.Unblocked,
    EntranceNames.c_a3_2: EntranceBlockType.Blocked,  # Need to activate glass bridge
    EntranceNames.c_n2_0: EntranceBlockType.Unblocked,
    EntranceNames.c_b2_0: EntranceBlockType.Unblocked,
    EntranceNames.c_b2_1: EntranceBlockType.DeadEnd,
    EntranceNames.c_r1_0: EntranceBlockType.Unblocked,
    EntranceNames.c_r1_1: EntranceBlockType.Unblocked,  # Funnily enough you appear on the floor switch to open the wall
    EntranceNames.c_r1_2: EntranceBlockType.Blocked,
    EntranceNames.c_r2_0: EntranceBlockType.Unblocked,
    EntranceNames.c_r2_1: EntranceBlockType.DeadEnd,
    EntranceNames.c_r2_2: EntranceBlockType.Blocked,
    EntranceNames.c_r2_200: EntranceBlockType.DeadEnd,  # Not a dead end if you aren't a coward :)
    EntranceNames.c_r3_0: EntranceBlockType.Unblocked,
    EntranceNames.c_r3_b_return: EntranceBlockType.Unblocked,
    EntranceNames.c_r3_boss: EntranceBlockType.Blocked,  # Need to open wall
    EntranceNames.c_r3_b_ent: EntranceBlockType.Blocked,
    EntranceNames.c_r3_250: EntranceBlockType.Blocked,
    EntranceNames.c_n3_0: EntranceBlockType.Unblocked,
    EntranceNames.c_n3_12: EntranceBlockType.Unblocked,
    EntranceNames.c_n3_80: EntranceBlockType.DeadEnd,
    EntranceNames.c_b3_0: EntranceBlockType.Unblocked,
    EntranceNames.c_b3_1: EntranceBlockType.DeadEnd,
    EntranceNames.c_c1_0: EntranceBlockType.Unblocked,
    EntranceNames.c_c1_75: EntranceBlockType.Unblocked,
    EntranceNames.c_c1_99: EntranceBlockType.Unblocked,
    EntranceNames.c_c1_100: EntranceBlockType.Unblocked,
    EntranceNames.c_c1_169: EntranceBlockType.Blocked,
    EntranceNames.c_c2_0: EntranceBlockType.Unblocked,  # Blocked by spikes from other entrances
    EntranceNames.c_c2_boss: EntranceBlockType.Unblocked,
    EntranceNames.c_c2_45: EntranceBlockType.Unblocked,
    EntranceNames.c_c2_50: EntranceBlockType.Unblocked,  # One way island
    EntranceNames.c_c2_77: EntranceBlockType.Unblocked,  # One way wall
    EntranceNames.c_c2_b_ent: EntranceBlockType.Blocked,
    EntranceNames.c_c2_105: EntranceBlockType.Unblocked,
    EntranceNames.c_c2_125: EntranceBlockType.Unblocked,  # Blocked by wall from other entrances
    EntranceNames.c_c3_0: EntranceBlockType.Unblocked,
    EntranceNames.c_c3_54: EntranceBlockType.Unblocked,
    EntranceNames.c_c3_67: EntranceBlockType.Unblocked,
    EntranceNames.c_c3_156: EntranceBlockType.Unblocked,  # Blocked by wall from other entrances
    EntranceNames.c_n4_0: EntranceBlockType.Unblocked,
    EntranceNames.c_b4_0: EntranceBlockType.DeadEnd,  # Technically not a dead end, but no entrances beyond are shuffled
    EntranceNames.c_p_return_0: EntranceBlockType.DeadEnd,
    
    EntranceNames.t_hub_1: EntranceBlockType.Unblocked,
    EntranceNames.t_hub_50: EntranceBlockType.Unblocked,
    EntranceNames.t_hub_56: EntranceBlockType.Blocked,  # Blocked because you need to talk to Lyron to clear the rocks!
    EntranceNames.t_hub_111: EntranceBlockType.Unblocked,
    EntranceNames.t_library_0: EntranceBlockType.Unblocked,
    EntranceNames.t_library_1: EntranceBlockType.Unblocked,
    EntranceNames.t_library_3: EntranceBlockType.Unblocked,
    EntranceNames.t_library_5: EntranceBlockType.Unblocked,
    EntranceNames.t_c1_0: EntranceBlockType.Unblocked,
    EntranceNames.t_c1_1: EntranceBlockType.Unblocked,  # Can't get back to the start, but can get to hub portal
    EntranceNames.t_c1_111: EntranceBlockType.Unblocked,
    EntranceNames.t_c1_123: EntranceBlockType.DeadEnd,
    EntranceNames.t_c1_197: EntranceBlockType.Unblocked,
    EntranceNames.t_c2_0: EntranceBlockType.Unblocked,
    EntranceNames.t_c2_1: EntranceBlockType.Unblocked,
    EntranceNames.t_c3_0: EntranceBlockType.Unblocked,
    EntranceNames.t_c3_49: EntranceBlockType.Blocked,  # Need a switch/switches to cross bridge
    EntranceNames.t_c3_123: EntranceBlockType.Blocked,  # Need green switch
    EntranceNames.t_b1_0: EntranceBlockType.Unblocked,
    EntranceNames.t_b1_2: EntranceBlockType.Unblocked,
    EntranceNames.t_p_ent_0: EntranceBlockType.Unblocked,
    EntranceNames.t_p_ent_1: EntranceBlockType.Unblocked,
    EntranceNames.t_p_ent_exit: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_0: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_1: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_2: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_3: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_4: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_end_0: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_end_1: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_end_2: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_end_3: EntranceBlockType.Unblocked,
    EntranceNames.t_p_mid_end_4: EntranceBlockType.Unblocked,
    EntranceNames.t_p_end_0: EntranceBlockType.Unblocked,
    EntranceNames.t_p_end_1: EntranceBlockType.Unblocked,
    EntranceNames.t_p_end_2: EntranceBlockType.Unblocked,
    EntranceNames.t_p_end_end: EntranceBlockType.Unblocked,
    EntranceNames.t_b2_0: EntranceBlockType.DeadEnd,
    EntranceNames.t_t1_0: EntranceBlockType.Unblocked,
    EntranceNames.t_t1_1: EntranceBlockType.Unblocked,  # Technically unblocked, but it's kinda hard
    EntranceNames.t_t2_0: EntranceBlockType.Unblocked,
    EntranceNames.t_t2_1: EntranceBlockType.Unblocked,
    EntranceNames.t_t2_78: EntranceBlockType.Unblocked,  # Can go to an exit to level 1
    EntranceNames.t_t2_97: EntranceBlockType.Blocked,  # Need glass walk
    EntranceNames.t_t2_123: EntranceBlockType.Blocked,  # Need column gate on the other side
    EntranceNames.t_t3_0: EntranceBlockType.Unblocked,
    EntranceNames.t_t3_1: EntranceBlockType.Unblocked,
    EntranceNames.t_t3_2: EntranceBlockType.Unblocked,
    EntranceNames.t_c3_97: EntranceBlockType.DeadEnd,
    EntranceNames.t_t3_123: EntranceBlockType.Blocked,  # Could potentially be blocked, so we assume worst case
    EntranceNames.t_t_ent_hub: EntranceBlockType.Blocked,
    EntranceNames.t_t_ent_temple: EntranceBlockType.Unblocked,
    EntranceNames.t_t_ent_p: EntranceBlockType.Unblocked,
    EntranceNames.t_n1_0: EntranceBlockType.Unblocked,
    EntranceNames.t_n1_12: EntranceBlockType.Unblocked,
    EntranceNames.t_n1_15: EntranceBlockType.DeadEnd,
    EntranceNames.t_n1_18: EntranceBlockType.Unblocked,
    EntranceNames.t_n1_25: EntranceBlockType.Unblocked,
    EntranceNames.t_n1_35: EntranceBlockType.DeadEnd,
    EntranceNames.t_n1_75: EntranceBlockType.Blocked,
    EntranceNames.t_n1_80: EntranceBlockType.DeadEnd,
    EntranceNames.t_n1_160: EntranceBlockType.Unblocked,
}


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
    # print("Prune entrance: " + entrance.name)
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
            multiworld.get_entrance(etr_base_name(CastleRegionNames.p3_sw, CastleRegionNames.b1_start), player),
            multiworld.get_entrance(etr_base_name(CastleRegionNames.a1_start, CastleRegionNames.b2_start), player),
            multiworld.get_entrance(etr_base_name(CastleRegionNames.r3_exit, CastleRegionNames.b3_start), player),
            multiworld.get_entrance(etr_base_name(CastleRegionNames.c2_main, CastleRegionNames.b4_start), player),
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
    key_names = get_active_key_names(multiworld, player)
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
        if exit.player != player:
            continue
        if exit.pass_item is None or exit.parent_region.name == exit.connected_region.name:
            # print(f"{exit.parent_region} -> {exit.connected_region}")
            continue
        # If the items are consumed gotta use the downstream cost logic
        if exit.items_consumed and exit.pass_item in door_counts.keys():
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
