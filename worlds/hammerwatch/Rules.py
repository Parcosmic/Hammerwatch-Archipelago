import math
import typing

from BaseClasses import MultiWorld, Region, Entrance
from .Names import CastleRegionNames, TempleRegionNames, EntranceNames
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from .Regions import HWEntrance, HWExitData, etr_base_name, connect_from_data
from .Util import *
# from Utils import visualize_regions


def set_rules(multiworld: MultiWorld, player: int, door_counts: typing.Dict[str, int]):
    multiworld.completion_condition[player] = lambda state: state.has(ItemName.ev_victory, player)

    tries = 0
    stop_threshold = 100000
    while not set_connections(multiworld, player):
        # print("------------------------------------------------------------------------------------------------")
        if tries >= stop_threshold:
            break
        tries += 1
    if tries >= stop_threshold:
        raise RuntimeError("Could not generate a valid ER configuration!")
    # print(f"Connecting exits took {tries} tries")

    # test_entrances = multiworld.get_entrances()
    # unconnected = []
    # for entr in test_entrances:
    #     if entr.connected_region is None:
    #         unconnected.append(entr.name)
    # print(unconnected)

    menu_region = multiworld.get_region(CastleRegionNames.menu, player)
    # visualize_regions(menu_region, "_testing.puml", show_locations=False)
    if get_campaign(multiworld, player) == Campaign.Castle:
        second_region_name = CastleRegionNames.p1_start
    else:
        second_region_name = TempleRegionNames.hub_main
    second_region = multiworld.get_region(second_region_name, player)
    loop_entrances = prune_entrances(menu_region, second_region)
    # visualize_regions(second_region, "_testing.puml", show_locations=False)

    set_door_access_rules(multiworld, player, door_counts, loop_entrances)

    # Change the names of all entrances to match where they lead if ER is on
    if get_option(multiworld, OptionNames.exit_randomization, player):
        world = multiworld.worlds[player]
        for exit in world.level_exits:
            exit.name = etr_base_name(exit.parent_region.name, exit.connected_region.name)
            world.exit_spoiler_info.append(exit.name)

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
            entr_name = ""
            if get_option(multiworld, OptionNames.exit_randomization, player):
                for exit in multiworld.get_entrances():
                    if exit.player == player and exit.name.endswith(CastleRegionNames.b4_start):
                        entr_name = exit.name
                        break
            else:
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

        # add_rule(multiworld.get_location(TempleLocationNames.ev_c3_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_c2_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_c1_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_t1_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_t2_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_t3_portal, player), portal_rule)

        # Extra rules for T1 north node blocks locations
        t1_sun_block_entr = etr_base_name(TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_sun_block_hall)
        add_rule(multiworld.get_entrance(t1_sun_block_entr, player),
                 lambda state: state.has_all([ItemName.evt_t1_n_mirrors, ItemName.evt_t1_s_mirror], player))
        add_rule(multiworld.get_entrance(etr_base_name(TempleRegionNames.t1_east, TempleRegionNames.t1_node_2), player),
                 lambda state: state.has(ItemName.evt_t1_n_mirrors, player))


def set_connections(multiworld: MultiWorld, player: int) -> bool:
    world = multiworld.worlds[player]
    level_exits: typing.List[HWEntrance] = world.level_exits.copy()
    if get_option(multiworld, OptionNames.exit_randomization, player):
        act_range = get_option(multiworld, OptionNames.er_act_range, player)
        if get_campaign(multiworld, player) == Campaign.Castle:
            entrance_block_types = c_entrance_block_types
            passage_blocking_codes = c_passage_blocking_codes
        else:
            entrance_block_types = t_entrance_block_types
            passage_blocking_codes = t_passage_blocking_codes
        code_to_exit = {}
        code_to_region = {}
        open_codes = []
        # exit_to_data = {}
        # region_to_exits = {}
        for exit in world.level_exits:
            # exit_name = etr_base_name(exit_data.parent.name, exit_data.target.name)
            # exit_to_data[exit_name] = exit_data
            # if exit_data.parent.name in region_to_exits:
            #     region_to_exits[exit_data.parent.name] = []
            # region_to_exits[exit_data.parent.name].append(exit_data)
            if exit.return_code is not None:
                code_to_exit[exit.return_code] = exit
                code_to_region[exit.return_code] = exit.parent_region
                open_codes.append(exit.return_code)
            else:
                code_to_exit[exit.exit_code] = None
                open_codes.append(exit.exit_code)
                code_to_region[exit.exit_code] = exit.target_region
        start_region = multiworld.get_region(CastleRegionNames.menu, player)
        entrances = start_region.exits.copy()
        traversed_regions: typing.List[str] = [start_region.name]
        needed_regions = []
        open_exits = []
        # connected_exits = []
        # linked_codes = []
        impassable_exits = []

        def disconnect_linked_exit(to_disconnect: HWEntrance):
            to_disconnect.connected_region.entrances.remove(to_disconnect)
            to_disconnect.connected_region = None
            open_codes.append(to_disconnect.return_code)
            # connected_exits.remove(to_disconnect.name)
            to_disconnect.linked = False
        while len(entrances) + len(impassable_exits) > 0:
            # Traverse current section
            while len(entrances) > 0:
                entr = entrances.pop()
                # open_exits.append(entr)  # Technically should be swapped with below but this works so idc
                if not entr.linked:
                    open_exits.append(entr)
                    continue
                if entr.connected_region.name in traversed_regions:
                    continue
                traversed_regions.append(entr.connected_region.name)
                entrances.extend(entr.connected_region.exits)
            # Re-add impassable exits from the previous loop back to entrances, we might be able to traverse them now
            for impassable in impassable_exits:
                if impassable not in open_exits:
                    open_exits.append(impassable)
            impassable_exits.clear()
            needed_regions.clear()
            # If an exit can't be traversed through yet (by not having traversed required regions) remove them for later
            for travel_exit in open_exits:
                if entrance_block_types[travel_exit.exit_code][2] is None:
                    continue
                req_regions = entrance_block_types[travel_exit.exit_code][2]
                for reg in req_regions:
                    if reg not in traversed_regions:
                        if reg not in needed_regions:
                            needed_regions.append(reg)
                        if travel_exit not in impassable_exits:
                            impassable_exits.append(travel_exit)
            for impassable in impassable_exits:
                open_exits.remove(impassable)
            # If we ran out of valid placements we gotta swap a connection
            if (len(impassable_exits) + len(open_codes) > 0) and len(open_exits) == 0:
                # The only things we have to worry about swapping are dead-ends luckily
                exit_needed_regions = {}
                needed_names = []
                have_names = []
                for impassable in impassable_exits:
                    exit_needed_regions[impassable] = []
                    for reg in entrance_block_types[impassable.exit_code][2]:
                        if reg not in traversed_regions:
                            exit_needed_regions[impassable].append(reg)
                            if reg not in needed_names:
                                needed_names.append(reg)
                        elif reg not in have_names:
                            have_names.append(reg)
                blocked_exit = None
                blocked_exit_needed_regions = []
                for b_exit, b_regs in exit_needed_regions.items():
                    if len(b_regs) < len(blocked_exit_needed_regions):
                        blocked_exit = b_exit
                        blocked_exit_needed_regions = b_regs
                blocked_needed_codes = [code_to_exit[code] for code in open_codes
                                        if code_to_region[code].name in blocked_exit_needed_regions]
                # swap goes from dead end to rest of map
                for b in range(len(blocked_exit_needed_regions)):
                    pass
                swap = None
                options = level_exits.copy()
                while len(options) > 0:
                    op = options.pop(world.random.randint(0, len(options) - 1))
                    if op.linked and not op.swapped and op.return_code is not None:
                        op_code = entrance_block_types[op.return_code][1]
                        if op_code == EntranceBlockType.DeadEnd and op.return_code not in passage_blocking_codes.values():
                            swap = op
                            break
                if swap is None:
                    # We don't have any more dead ends to swap with, give up and start over
                    break
                swap2 = None
                for swapp in swap.connected_region.exits:
                    if swapp.connected_region == swap.parent_region:
                        swap2 = swapp
                        break
                # print(f"  Unhooked {swap.name}: {swap.parent_region.name} > {swap.connected_region.name}")
                traversed_regions.remove(swap.parent_region.name)
                disconnect_linked_exit(swap)
                disconnect_linked_exit(swap2)
                swap.swapped = True
                swap2.swapped = True
                open_exits.insert(0, swap2)
            needed_codes = []
            for needed_reg in needed_regions:
                if needed_reg in passage_blocking_codes:
                    needed_codes.append(passage_blocking_codes[needed_reg])
            # print(f"  Needed regions: {needed_codes}")
            # Move one way exits to the front of the list to be filled first
            for i in range(len(open_exits)):
                if open_exits[i].return_code is None:
                    open_exits.insert(0, open_exits.pop(i))
            # For each exit find a valid connection and connect them
            while len(open_exits):
                open_exit = open_exits.pop(world.random.randint(0, len(open_exits)-1))
                if open_exit.linked:
                    # print(f"----Ditched {open_exit}")
                    continue
                # if open_exit.name in connected_exits:
                #     a = 5
                # connected_exits.append(open_exit.name)
                # open_exit = multiworld.get_entrance(open_exit.name, player)
                valid_exits = get_valid_exits(entrance_block_types, open_codes, code_to_region, traversed_regions,
                                              open_exits, open_exit, needed_codes, act_range)
                # print(f"# Exits for {open_exit.parent_region}: {len(valid_exits)}")
                link_code = world.random.choice(valid_exits)
                link_region = code_to_region[link_code]
                # print(f"Linked {open_exit.parent_region} ({open_exit.return_code}) to {link_region} ({link_code})"
                #       + ("    >><<" if open_exit.return_code is not None else ""))

                # Set the reverse exit too if the exit is two-way
                if open_exit.return_code is not None:
                    # code_to_exit.pop(open_exit.return_code)
                    link = multiworld.get_entrance(code_to_exit[link_code].name, player)
                    link.connect(open_exit.parent_region)
                    multiworld.worlds[player].exit_swaps[link.exit_code] = open_exit.return_code
                    link.linked = True
                    open_codes.remove(open_exit.return_code)
                    # if open_exit.return_code in linked_codes:
                    #     print("PANIC")
                    # linked_codes.append(open_exit.return_code)

                open_exit.connect(link_region)
                multiworld.worlds[player].exit_swaps[open_exit.exit_code] = link_code
                # code_to_exit.pop(link_code)
                open_exit.linked = True
                open_codes.remove(link_code)
                # if link_code in linked_codes:
                #     print("PANIC")
                # linked_codes.append(link_code)

                # Find new entrances from new connection
                traversed_regions.append(link_region.name)
                entrances.extend(link_region.exits)
                # Re-add impassable exits back to entrances, we might be able to traverse them now
                # re_verify = []
                # for impassable in impassable_exits:
                #     re_verify.append(impassable)
                # impassable_exits.clear()
                # for l_exit in re_verify:
                #     if not l_exit.linked:
                #         exit_passable = True
                #         req_regions = entrance_block_types[l_exit.exit_code][2]
                #         if req_regions is not None:
                #             for reg in req_regions:
                #                 if reg not in traversed_regions:
                #                     exit_passable = False
                #                     impassable_exits.append(l_exit)
                #                     break
                #         if exit_passable:
                #             open_exits.append(l_exit)
        unconnected = []
        for exit in level_exits:
            # Set exit names
            if not exit.linked:
                unconnected.append(exit)
        if len(unconnected) > 0:
            # print(" !!! Failed to connect entrances properly, trying again...")
            # print(f"Unconnected entrances ({len(unconnected)}): {unconnected}")
            # if len(impassable_exits) > 0:
            #     print(f"Impassable ({len(impassable_exits)}): {impassable_exits}")
            #     test = [t_entrance_block_types[tixe.exit_code][2] for tixe in impassable_exits]
            #     not_in = []
            #     for info in test:
            #         for dat in info:
            #             if dat not in traversed_regions:
            #                 not_in.append(dat)
            #     print(not_in)
            # Give up and disconnect all the entrances
            while len(level_exits) > 0:
                unconnect = level_exits.pop()
                if unconnect.linked:
                    disconnect_linked_exit(unconnect)
            return False
        return True
    else:
        # Create entrances
        for connection in level_exits:
            # connection.parent_region.exits.append(connection)
            connection.connect(connection.target_region)
            # connect_from_data(multiworld, player, connection)
        return True


class EntranceBlockType(Enum):
    Unblocked = 0
    Blocked = 1  # Blocked means you cannot progress without being on the other side, effectively dead end
    DeadEnd = 2
    OneWay = 3


# Required traversed regions is of the exit_code of the original entrance that requires them
c_entrance_block_types = {  # (act, EntranceBlockType, required traversed regions)
    EntranceNames.c_p1_1: (1, EntranceBlockType.DeadEnd, None),  # Technically not a dead end if shortcut portal is enabled
    EntranceNames.c_p1_2: (1, EntranceBlockType.Unblocked, None),  # Leads to 3
    EntranceNames.c_p1_3: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.c_p1_4: (1, EntranceBlockType.DeadEnd, None),
    EntranceNames.c_p1_10: (1, EntranceBlockType.DeadEnd, None),
    EntranceNames.c_p1_20: (1, EntranceBlockType.DeadEnd, None),  # Portal exit, same note as 1 ^
    EntranceNames.c_p2_0: (1, EntranceBlockType.Unblocked, None),  # Leads to 1, 3 (2 is blocked)
    EntranceNames.c_p2_1: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.c_p2_2: (1, EntranceBlockType.Unblocked, None),  # Leads to 0, 1,
    EntranceNames.c_p2_3: (1, EntranceBlockType.Blocked, None),  # Blocked by South spikes
    EntranceNames.c_p3_0: (1, EntranceBlockType.Unblocked, None),  # Is blocked from other exits, but leads to 1, 10, b_ent
    EntranceNames.c_p3_1: (1, EntranceBlockType.Blocked, None),  # Blocked by spikes
    EntranceNames.c_p3_10: (1, EntranceBlockType.Unblocked, None),  # Leads to 100
    EntranceNames.c_p3_b_return: (1, EntranceBlockType.OneWay, None),  # Leads to 10, b_ent, 1
    EntranceNames.c_p3_portal: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.c_p3_b_ent: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.c_p3_boss: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.c_n1_0: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.c_b1_0: (1, EntranceBlockType.Unblocked,
                              [CastleRegionNames.p1_from_p3_n, CastleRegionNames.p2_s, CastleRegionNames.p3_s_gold_gate]),
    EntranceNames.c_b1_1: (1, EntranceBlockType.DeadEnd, None),
    # Technically blocked, but after the wall opens can't move on
    EntranceNames.c_a1_0: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a1_1: (2, EntranceBlockType.DeadEnd, None),
    EntranceNames.c_a1_a2: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a1_a3: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a1_boss: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a2_0: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a2_1: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a2_2: (2, EntranceBlockType.Blocked, None),  # Need to push button to open walls
    EntranceNames.c_a2_3: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a2_10: (2, EntranceBlockType.OneWay, None),
    EntranceNames.c_a2_88: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a3_0: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a3_1: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_a3_2: (2, EntranceBlockType.Blocked, None),  # Need to activate glass bridge
    EntranceNames.c_n2_0: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.c_b2_0: (2, EntranceBlockType.Unblocked,
                              [CastleRegionNames.a1_w, CastleRegionNames.a2_ne, CastleRegionNames.a3_main]),
    EntranceNames.c_b2_1: (2, EntranceBlockType.DeadEnd, None),
    EntranceNames.c_r1_0: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.c_r1_1: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.c_r1_2: (3, EntranceBlockType.Blocked, None),
    EntranceNames.c_r2_0: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.c_r2_1: (3, EntranceBlockType.DeadEnd, None),
    EntranceNames.c_r2_2: (3, EntranceBlockType.Blocked, None),
    EntranceNames.c_r2_200: (3, EntranceBlockType.DeadEnd, None),  # Not a dead end if you aren't a coward :)
    EntranceNames.c_r3_0: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.c_r3_b_return: (3, EntranceBlockType.OneWay, None),
    EntranceNames.c_r3_boss: (3, EntranceBlockType.Blocked, None),  # Need to open wall
    EntranceNames.c_r3_b_ent: (3, EntranceBlockType.Blocked, None),
    EntranceNames.c_r3_250: (3, EntranceBlockType.Blocked, None),
    EntranceNames.c_n3_0: (3, EntranceBlockType.OneWay, None),  # Nothing is blocked so we can make this one way
    EntranceNames.c_n3_12: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.c_n3_80: (3, EntranceBlockType.DeadEnd, None),
    EntranceNames.c_b3_0: (3, EntranceBlockType.Unblocked,
                              [CastleRegionNames.r2_bswitch, CastleRegionNames.r2_n, CastleRegionNames.r3_main]),
    EntranceNames.c_b3_1: (3, EntranceBlockType.DeadEnd, None),
    EntranceNames.c_c1_0: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_c1_75: (4, EntranceBlockType.OneWay, None),
    EntranceNames.c_c1_99: (4, EntranceBlockType.OneWay, None),
    EntranceNames.c_c1_100: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_c1_169: (4, EntranceBlockType.Blocked, None),
    EntranceNames.c_c2_0: (4, EntranceBlockType.Unblocked, None),  # Blocked by spikes from other entrances
    EntranceNames.c_c2_boss: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_c2_45: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_c2_50: (4, EntranceBlockType.OneWay, None),  # One way island
    EntranceNames.c_c2_77: (4, EntranceBlockType.OneWay, None),  # One way wall
    EntranceNames.c_c2_b_ent: (4, EntranceBlockType.Blocked, None),
    EntranceNames.c_c2_105: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_c2_125: (4, EntranceBlockType.OneWay, None),  # Blocked by wall from other entrances
    EntranceNames.c_c3_0: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_c3_54: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_c3_67: (4, EntranceBlockType.OneWay, [CastleRegionNames.c3_nw]),
    EntranceNames.c_c3_156: (4, EntranceBlockType.OneWay, None),  # Blocked by wall from other entrances
    EntranceNames.c_n4_0: (4, EntranceBlockType.Unblocked, None),
    EntranceNames.c_b4_0: (4, EntranceBlockType.DeadEnd,
                              [CastleRegionNames.c2_main, CastleRegionNames.c2_tp_island, CastleRegionNames.c3_nw]),
    # Technically not a dead end, but no entrances beyond are shuffled
    EntranceNames.c_p_return_0: (1, EntranceBlockType.DeadEnd, None),
}

c_passage_blocking_codes = {
    CastleRegionNames.p1_from_p3_n: EntranceNames.c_p1_10,
    CastleRegionNames.p2_s: EntranceNames.c_p2_3,  # Not actually connected, got a gate in the way
    CastleRegionNames.a2_ne: EntranceNames.c_a2_0,
    CastleRegionNames.a3_main: EntranceNames.c_a3_0,
    CastleRegionNames.r2_bswitch: EntranceNames.c_r2_1,
    CastleRegionNames.r2_n: EntranceNames.c_r2_0,
    CastleRegionNames.c2_tp_island: EntranceNames.c_c2_50,
    CastleRegionNames.c3_nw: EntranceNames.c_c3_54,
    CastleRegionNames.b1_defeated: EntranceNames.c_b1_0,
    CastleRegionNames.b2_defeated: EntranceNames.c_b2_0,
    CastleRegionNames.b3_defeated: EntranceNames.c_b3_0,
}

t_entrance_block_types = {  # (act, EntranceBlockType)
    EntranceNames.t_hub_t_ent: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_hub_library: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_hub_t3: (1, EntranceBlockType.Blocked, None),
    # Blocked because you need to talk to Lyron to clear the rocks!
    EntranceNames.t_hub_pof: (1, EntranceBlockType.Unblocked, None),  # Locations to raise pyramids for PoF entrance
    EntranceNames.t_hub_pof_return: (1, EntranceBlockType.OneWay, None),  # This is the bonus completion return
    EntranceNames.t_lib_start: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_lib_lobby_end: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_lib_books: (1, EntranceBlockType.Unblocked, None),
    # EntranceNames.t_lib_end: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_c1_start: (1, EntranceBlockType.OneWay, None),
    EntranceNames.t_c1_end: (1, EntranceBlockType.Unblocked, None),  # Can't get back to the start, but can get to hub portal
    EntranceNames.t_c1_fall_surface: (1, EntranceBlockType.OneWay, [TempleRegionNames.cave_3_main]),
    # Not actually required, to enforce that the right exits in the hub will have items
    EntranceNames.t_c1_portal: (1, EntranceBlockType.DeadEnd, [TempleRegionNames.boss2_defeated]),
    EntranceNames.t_c1_fall_temple: (1, EntranceBlockType.OneWay, None),
    EntranceNames.t_c2_start: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_c2_end: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_c3_start: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_c3_end: (1, EntranceBlockType.Blocked, None),  # Need a switch/switches to cross bridge
    EntranceNames.t_c3_boss: (1, EntranceBlockType.Blocked, None),  # Need green switch
    EntranceNames.t_b1_start: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_b1_end: (1, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_ent_start: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_ent_start_2: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_ent_exit: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_0: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_1: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_2: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_3: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_4: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_end_0: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_end_1: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_end_2: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_end_3: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_mid_end_4: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_end_0: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_end_1: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_end_2: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_p_end_end: (2, EntranceBlockType.Unblocked, None),
    EntranceNames.t_b2: (2, EntranceBlockType.DeadEnd, [TempleRegionNames.cave_2_main]),
    EntranceNames.t_t1_start: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.t_t1_end: (3, EntranceBlockType.Unblocked, None),  # Technically unblocked, but it's kinda hard
    EntranceNames.t_t2_start_1: (3, EntranceBlockType.Blocked, None),
    EntranceNames.t_t2_start_2: (3, EntranceBlockType.Blocked, None),
    EntranceNames.t_t2_w_portal: (3, EntranceBlockType.Unblocked,
                                  [TempleRegionNames.boss2_defeated]),  # Can go through the gate to the main area
    EntranceNames.t_t2_s_light_bridge: (3, EntranceBlockType.Blocked, None),  # Need glass walk
    EntranceNames.t_t2_t3: (3, EntranceBlockType.Blocked, None),  # Need column gate on the other side
    EntranceNames.t_t3_start_1: (3, EntranceBlockType.Unblocked,
                                 [TempleRegionNames.cave_1_main, TempleRegionNames.cave_2_main,
                                  TempleRegionNames.cave_3_main]),
    # Not actually required, to enforce that the right exits in the hub will have items
    EntranceNames.t_t3_start_2: (3, EntranceBlockType.Unblocked,
                                 [TempleRegionNames.cave_1_main, TempleRegionNames.cave_2_main,
                                  TempleRegionNames.cave_3_main]),
    EntranceNames.t_t3_start_3: (3, EntranceBlockType.Unblocked,
                                 [TempleRegionNames.cave_1_main, TempleRegionNames.cave_2_main,
                                  TempleRegionNames.cave_3_main]),
    EntranceNames.t_c3_temple: (3, EntranceBlockType.DeadEnd, [TempleRegionNames.boss2_defeated]),
    EntranceNames.t_t3_t2: (3, EntranceBlockType.Blocked, None),  # Could be blocked, so we assume worst case
    EntranceNames.t_t_ent_hub: (3, EntranceBlockType.Blocked, None),
    EntranceNames.t_t_ent_temple: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.t_t_ent_p: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.t_n1_1_start: (3, EntranceBlockType.Unblocked,
                                 [TempleRegionNames.cave_3_portal, TempleRegionNames.cave_2_pumps,
                                  TempleRegionNames.cave_1_blue_bridge, TempleRegionNames.t1_east,
                                  TempleRegionNames.t2_s_gate, TempleRegionNames.boss2_defeated]),
    EntranceNames.t_n1_1_sw: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.t_n1_1_n: (3, EntranceBlockType.DeadEnd, [TempleRegionNames.pof_1_se_room]),
    EntranceNames.t_n1_2_start: (3, EntranceBlockType.OneWay,
                                 [TempleRegionNames.pof_1_n_room, TempleRegionNames.pof_1_se_room]),
    EntranceNames.t_n1_20: (3, EntranceBlockType.Blocked, None),
    EntranceNames.t_n1_2_nw: (3, EntranceBlockType.Unblocked, None),
    EntranceNames.t_n1_2_n: (3, EntranceBlockType.DeadEnd, None),
    EntranceNames.t_n1_1_ne: (3, EntranceBlockType.Blocked, None),
    EntranceNames.t_n1_1_se: (3, EntranceBlockType.DeadEnd, None),
    EntranceNames.t_n1_100: (3, EntranceBlockType.Blocked, None),
    EntranceNames.t_n1_3_start: (3, EntranceBlockType.OneWay, [TempleRegionNames.pof_2_n]),
}

t_passage_blocking_codes = {
    TempleRegionNames.cave_3_main: EntranceNames.t_c1_start,  # There are more entrances, but use this one for now
    TempleRegionNames.cave_2_main: EntranceNames.t_c2_start,
    TempleRegionNames.cave_2_pumps: EntranceNames.t_c2_start,
    TempleRegionNames.cave_1_main: EntranceNames.t_c3_start,
    TempleRegionNames.cave_1_blue_bridge: EntranceNames.t_c3_start,
    TempleRegionNames.t1_east: EntranceNames.t_t1_end,
    TempleRegionNames.t2_s_gate: EntranceNames.t_t2_w_portal,
    TempleRegionNames.boss2_defeated: EntranceNames.t_b2,
    TempleRegionNames.cave_3_portal: EntranceNames.t_c1_portal,
    TempleRegionNames.pof_1_n_room: EntranceNames.t_n1_1_n,
    TempleRegionNames.pof_2_n: EntranceNames.t_n1_2_n,
    TempleRegionNames.pof_1_se_room: EntranceNames.t_n1_1_se,
}


def get_valid_exits(entrance_block_types, open_codes: typing.List, code_to_region: typing.Dict[str, Region],
                    traversed_regions, open_exits: typing.List[HWEntrance], entrance: HWEntrance,
                    needed_codes: typing.List[str], act_range=4):
    act = entrance_block_types[entrance.return_code if entrance.return_code is not None else entrance.exit_code][0]
    exit_count = len(open_exits)
    open_exit_codes = [exit.return_code for exit in open_exits]
    exits: typing.List[str] = []
    valid_exits: typing.List[str] = []
    type_match_exits: typing.List[str] = []
    # valid_exits = [key for key in unlinked_exit_data.keys()]
    # valid_exits.pop(entrance.return_code)
    # if entrance.return_code in unlinked_exit_data:
    #     print("sdfjs")
    for exit_code in open_codes:
        if exit_code == entrance.return_code:
            continue  # Can't connect an entrance to itself!
        data = entrance_block_types[exit_code]
        if (entrance.return_code is not None) == (data[1] == EntranceBlockType.OneWay):
            continue  # Only shuffle one way transitions together
        type_match_exits.append(exit_code)
        if code_to_region[exit_code].name in traversed_regions:
            continue  # If we can reach the destination then don't consider the transition
        # if exit_count <= 1 and exit_code in open_exit_codes:
        if exit_code in open_exit_codes:
            continue  # If we only have 2 exits don't connect them with each other
        if abs(act - data[0]) > act_range:
            continue  # Only include connections within the act range
        valid_exits.append(exit_code)
        if exit_count == 0 and not (data[1] == EntranceBlockType.Unblocked or data[1] == EntranceBlockType.OneWay):
            continue  # If there is only 1 exit left, we can't block it off
        exits.append(exit_code)
    if len(exits) == 0:
        # if len(valid_exits) == 1:
        #     return valid_exits
        # if len(valid_exits) == 0 and len(type_match_exits) == 1:
        #     return type_match_exits
        if len(valid_exits) == 0:
            return type_match_exits
        else:
            needed_exits = [exit for exit in valid_exits if exit in needed_codes]
            return needed_exits if len(needed_exits) > 0 else valid_exits
    return exits


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
            del_entrance = entrances_to_delete.pop(0)
            # print(f"Deleted {del_entrance.parent_region} -> {del_entrance.connected_region}")
            if del_entrance.exit_code is not None:
                continue
            # delete_entrance(del_entrance)

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

    def copy_entrance_dest(name: str, parent_name: str, entrance: Entrance):
        entr = HWEntrance(player, name, multiworld.get_region(parent_name, player))
        entr.parent_region.exits.append(entr)
        entr.connect(entrance.connected_region)
        return entr

    add_entrances = []
    if get_campaign(multiworld, player) == Campaign.Castle:
        # if not get_option(multiworld, OptionNames.exit_randomization, player):
        # Disconnect level exits and pretend that you need to go through the boss switch areas to the boss
        remove_entrances = [
            multiworld.get_entrance(etr_base_name(CastleRegionNames.p3_sw, CastleRegionNames.b1_start), player),
            multiworld.get_entrance(etr_base_name(CastleRegionNames.a1_start, CastleRegionNames.b2_start), player),
            multiworld.get_entrance(etr_base_name(CastleRegionNames.r3_exit, CastleRegionNames.b3_start), player),
            multiworld.get_entrance(etr_base_name(CastleRegionNames.c2_main, CastleRegionNames.b4_start), player),
        ]
        add_entrances = [
            copy_entrance_dest("P1 Boss Switch", CastleRegionNames.p1_from_p3_n, remove_entrances[0]),
            copy_entrance_dest("P3 Boss Switch", CastleRegionNames.p3_s_gold_gate, remove_entrances[0]),
            copy_entrance_dest("A1 Boss Switch", CastleRegionNames.a1_w, remove_entrances[1]),
            copy_entrance_dest("A2 Boss Switch", CastleRegionNames.a2_ne, remove_entrances[1]),
            copy_entrance_dest("R2 Boss Switch", CastleRegionNames.r2_n, remove_entrances[2]),
            copy_entrance_dest("C1 Boss Switch", CastleRegionNames.c2_tp_island, remove_entrances[3]),
            copy_entrance_dest("C2 Boss Switch", CastleRegionNames.c2_c3_tp, remove_entrances[3]),
            copy_entrance_dest("C3 Boss Switch", CastleRegionNames.c3_rspike_switch, remove_entrances[3]),
            copy_entrance_dest("C3 Portal", CastleRegionNames.c3_nw,
                               multiworld.get_entrance(etr_base_name(CastleRegionNames.c3_sw_hidden,
                                                                     CastleRegionNames.c3_fire_floor), player)),
        ]
    else:
        remove_entrances = [
            # multiworld.get_entrance('Temple Entrance Back__', player),
        ]
        add_entrances = [
            add_entrance("T3 Psuedo Entrance", TempleRegionNames.t3_s_node_blocks_1,
                         TempleRegionNames.t3_s_node_blocks_2)
        ]
    # Don't remove entrances with exit rando because they won't exist
    # if not get_option(multiworld, OptionNames.exit_randomization, player):
    for remove in remove_entrances:
        remove.parent_region.exits.remove(remove)
        remove.connected_region.entrances.remove(remove)

    # Set downstream costs - the keys that are required after a specific entrance
    key_names = get_active_key_names(multiworld, player)
    # seen = [(exit.parent_region) for exit in menu_region.exits]
    start_exits = [exit for exit in menu_region.exits if exit.connected_region.name != CastleRegionNames.get_planks]
    # seen_start = [get_entrance_id(exit) for exit in start_exits]
    # seen_start.remove(get_entrance_id(menu_region.exits[0]))
    # gate_type_counts = {
    #     ItemName.key_bronze: 0,
    #     ItemName.key_silver: 0,
    #     ItemName.key_gold: 0,
    #     ItemName.key_bonus: 0,
    # }
    # for test_entrance in multiworld.get_entrances():
    #     if test_entrance.pass_item in gate_type_counts:
    #         gate_type_counts[test_entrance.pass_item] += 1
    #         if test_entrance.item_count != 1:
    #             print("Panicc")
    for item in key_names:
        # seen = seen_start.copy()
        set_downstream_costs(item, start_exits[0], [])

    # Set the downstream count for loops to be 0
    for loop in loop_entrances:
        for entrance in loop:
            if entrance.items_consumed and entrance.pass_item in key_names:
                entrance.downstream_count = 0

    # Re-add removed entrances and remove added ones
    for add in add_entrances:
        add.parent_region.exits.remove(add)
        add.connected_region.entrances.remove(add)
    # Don't remove entrances with exit rando because they won't exist
    # if not get_option(multiworld, OptionNames.exit_randomization, player):
    for remove in remove_entrances:
        remove.parent_region.exits.append(remove)
        remove.connected_region.entrances.append(remove)

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
    entr_id = get_entrance_id(entrance)
    seen.append(entr_id)
    seen = seen.copy()  # Create a copy so that independent pathways don't lock each other
    door_entrances: typing.Set[str] = set()
    cost_dict: typing.Dict[str] = {}
    cost = 0
    if entrance.parent_region != entrance.connected_region:
        for exit in entrance.connected_region.exits:
            if get_entrance_id(exit) in seen and exit.connected_region.name != exit.parent_region.name:
                continue
            entrances = set_downstream_costs(item, exit, seen)
            cost_dict.update(entrances)
    if entrance.pass_item == item:
        # Just assume the item count is 1, doors should never cost more
        # entrance.downstream_count += entrance.item_count
        door_entrances.add(entr_id)
        if entrance.downstream_count == 0:
            for cost in cost_dict.values():
                entrance.downstream_count += cost
            # entrance.downstream_count = len(door_entrances)
        # else:
        #     new_cost = 0
        #     for cost in cost_dict.values():
        #         new_cost += cost
        #     if entrance.downstream_count > new_cost:
        #         entrance.downstream_count = new_cost
        if entrance.connected_region.name != entrance.parent_region.name:
            cost_dict[entr_id] = entrance.item_count
        else:
            cost_dict[entrance.name] = entrance.item_count
    return cost_dict.copy()


def get_entrance_id(entrance: HWEntrance):
    if entrance.connected_region.name > entrance.parent_region.name:
        return f"{entrance.parent_region.name}, {entrance.connected_region.name}"
    else:
        return f"{entrance.connected_region.name}, {entrance.parent_region.name}"
