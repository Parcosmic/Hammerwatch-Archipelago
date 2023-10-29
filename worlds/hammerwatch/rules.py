import typing
from enum import Enum
from BaseClasses import MultiWorld, Region, Entrance
from .names import castle_region_names, temple_region_names, entrance_names, item_name, option_names
from worlds.generic.Rules import add_rule
from .regions import HWEntrance, etr_base_name, connect
from .options import ExitRandomization
from .util import GoalType, Campaign, get_goal_type, get_campaign, get_option, get_active_key_names
# from Utils import visualize_regions


def set_rules(multiworld: MultiWorld, player: int, door_counts: typing.Dict[str, int]):
    multiworld.completion_condition[player] = lambda state: state.has(item_name.ev_victory, player)
    world = multiworld.worlds[player]

    if get_campaign(multiworld, player) == Campaign.Castle:
        world.start_exit = entrance_names.c_p1_start
        entrance_block_types = c_entrance_block_types.copy()
        passage_blocking_codes = c_passage_blocking_codes
        # If we aren't randomizing boss entrances, move requirements down to the boss exit
        if get_option(multiworld, player, option_names.exit_randomization) == ExitRandomization.option_no_boss_exits:
            entrance_block_types[entrance_names.c_a1_0] = entrance_block_types[entrance_names.c_b1_0]
            entrance_block_types[entrance_names.c_r1_0] = entrance_block_types[entrance_names.c_b2_0]
            entrance_block_types[entrance_names.c_c1_0] = entrance_block_types[entrance_names.c_b3_0]
    else:
        world.start_exit = entrance_names.t_hub_start
        entrance_block_types = t_entrance_block_types.copy()
        passage_blocking_codes = t_passage_blocking_codes

    code_to_exit = {}
    code_to_region = {}
    open_codes = []
    if get_option(multiworld, player, option_names.exit_randomization) > 0:
        for level_exit in world.level_exits:
            if level_exit.return_code is not None:
                code_to_exit[level_exit.return_code] = level_exit
                code_to_region[level_exit.return_code] = level_exit.parent_region
                open_codes.append(level_exit.return_code)
            else:
                code_to_exit[level_exit.exit_code] = None
                open_codes.append(level_exit.exit_code)
                code_to_region[level_exit.exit_code] = level_exit.target_region

    tries = 0
    stop_threshold = 100000
    while not set_connections(multiworld, player, entrance_block_types, passage_blocking_codes,
                              code_to_exit, code_to_region, open_codes):
        if tries >= stop_threshold:
            break
        tries += 1
    if tries >= stop_threshold:
        raise RuntimeError("Could not generate a valid ER configuration!")
    # print(f"Connecting exits took {tries} tries")

    menu_region = multiworld.get_region(castle_region_names.menu, player)
    # visualize_regions(menu_region, "_testing.puml", show_locations=False)
    if get_campaign(multiworld, player) == Campaign.Castle:
        second_region_name = castle_region_names.p1_start
    else:
        second_region_name = temple_region_names.hub_main
    second_region = multiworld.get_region(second_region_name, player)
    loop_entrances = prune_entrances(menu_region, second_region)

    set_door_access_rules(multiworld, player, door_counts, loop_entrances)

    # Change the names of all entrances to match where they lead if ER is on
    if get_option(multiworld, player, option_names.exit_randomization) > 0:
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
                item_name.evc_beat_boss_1,
                item_name.evc_beat_boss_2,
                item_name.evc_beat_boss_3,
                item_name.evc_beat_boss_4,
            }
            multiworld.completion_condition[player] = lambda state: state.has_all(boss_names, player)
        if get_goal_type(multiworld, player) == GoalType.FullCompletion:
            entr_name = ""
            if get_option(multiworld, player, option_names.exit_randomization) > 0:
                for exit in multiworld.get_entrances():
                    if exit.player == player and exit.name.endswith(castle_region_names.b4_start):
                        entr_name = exit.name
                        break
            else:
                entr_name = etr_base_name(castle_region_names.c2_main, castle_region_names.b4_start)
            add_rule(multiworld.get_entrance(entr_name, player),
                     lambda state: state.has(item_name.plank, player, 12)
                     and state.has(item_name.key_gold, player, 16)
                     and state.has(item_name.key_silver, player, 13)
                     and state.has(item_name.key_bronze, player, 103)
                     and state.has(item_name.key_bonus, player, 18))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_1, player),
            #          lambda state: state.has(item_name.plank, player, 1))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_2, player),
            #          lambda state: state.has(item_name.plank, player, 2))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_3, player),
            #          lambda state: state.has(item_name.plank, player, 3))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_4, player),
            #          lambda state: state.has(item_name.plank, player, 4))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_5, player),
            #          lambda state: state.has(item_name.plank, player, 5))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_6, player),
            #          lambda state: state.has(item_name.plank, player, 6))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_7, player),
            #          lambda state: state.has(item_name.plank, player, 7))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_8, player),
            #          lambda state: state.has(item_name.plank, player, 8))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_9, player),
            #          lambda state: state.has(item_name.plank, player, 9))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_10, player),
            #          lambda state: state.has(item_name.plank, player, 10))
            # add_rule(multiworld.get_location(CastleLocationNames.b4_plank_11, player),
            #          lambda state: state.has(item_name.plank, player, 11))
    else:
        # Overwrite world completion condition if we need to defeat all bosses
        if get_goal_type(multiworld, player) == GoalType.KillBosses:
            boss_names: typing.Set = {
                item_name.evt_beat_boss_1,
                item_name.evt_beat_boss_2,
                item_name.evt_beat_boss_3,
            }
            multiworld.completion_condition[player] = lambda state: state.has_all(boss_names, player)

        # Set access rules for portal activation events
        def portal_rule(state) -> bool:
            return state.has(item_name.key_teleport, player, 6)

        # add_rule(multiworld.get_location(TempleLocationNames.ev_c3_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_c2_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_c1_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_t1_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_t2_portal, player), portal_rule)
        # add_rule(multiworld.get_location(TempleLocationNames.ev_t3_portal, player), portal_rule)

        # Extra rules for T1 north node blocks locations
        t1_sun_block_entr = etr_base_name(temple_region_names.t1_ice_turret, temple_region_names.t1_sun_block_hall)
        add_rule(multiworld.get_entrance(t1_sun_block_entr, player),
                 lambda state: state.has_all([item_name.evt_t1_n_mirrors, item_name.evt_t1_s_mirror], player))
        add_rule(multiworld.get_entrance(etr_base_name(temple_region_names.t1_east, temple_region_names.t1_node_2), player),
                 lambda state: state.has(item_name.evt_t1_n_mirrors, player))

    # visualize_regions(second_region, "_testing.puml", show_locations=False)


def set_connections(multiworld: MultiWorld, player: int, entrance_block_types, passage_blocking_codes,
                    code_to_exit, code_to_region, open_codes) -> bool:
    world = multiworld.worlds[player]
    level_exits: typing.List[HWEntrance] = world.level_exits.copy()
    if get_option(multiworld, player, option_names.exit_randomization) > 0:
        start_entrance = None
        act_range = get_option(multiworld, player, option_names.er_act_range).value
        open_codes = open_codes.copy()

        # Randomly choose a starting exit if the setting is one
        if get_option(multiworld, player, option_names.random_start_exit):
            start_act = get_option(multiworld, player, option_names.random_start_exit_act)
            # Cap the highest act to be 3 in the Temple campaign
            if get_campaign(multiworld, player) == Campaign.Temple and start_act > 3:
                start_act = 3
            available_start_codes = [code for code in open_codes if entrance_block_types[code][0] == start_act]
            start_code = world.random.choice(available_start_codes)
            world.start_exit = start_code
            start_region = code_to_region[start_code]
            start_entrance = connect(multiworld, player, {}, castle_region_names.menu, start_region.name, False)
        else:
            start_region = multiworld.get_region(castle_region_names.menu, player)
        entrances = start_region.exits.copy()
        traversed_regions: typing.List[str] = [start_region.name]
        needed_regions = []
        open_exits = []
        impassable_exits = []

        def disconnect_linked_exit(to_disconnect: HWEntrance):
            to_disconnect.connected_region.entrances.remove(to_disconnect)
            to_disconnect.connected_region = None
            open_codes.append(to_disconnect.return_code)
            to_disconnect.linked = False
        while len(entrances) + len(impassable_exits) > 0:
            # Traverse current section
            while len(entrances) > 0:
                entr: HWEntrance = entrances.pop()
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
                # blocked_exit = None
                # blocked_exit_needed_regions = []
                # for b_exit, b_regs in exit_needed_regions.items():
                #     if len(b_regs) < len(blocked_exit_needed_regions):
                #         blocked_exit = b_exit
                #         blocked_exit_needed_regions = b_regs
                # blocked_needed_codes = [code_to_exit[code] for code in open_codes
                #                         if code_to_region[code].name in blocked_exit_needed_regions]
                # # swap goes from dead end to rest of map
                # for b in range(len(blocked_exit_needed_regions)):
                #     pass
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
                    continue
                valid_exits = get_valid_exits(entrance_block_types, open_codes, code_to_region, traversed_regions,
                                              open_exits, open_exit, needed_codes, act_range)
                # print(f"# Exits for {open_exit.parent_region}: {len(valid_exits)}")
                link_code = world.random.choice(valid_exits)
                link_region = code_to_region[link_code]
                # print(f"Linked {open_exit.parent_region} ({open_exit.return_code}) to {link_region} ({link_code})"
                #       + ("    >><<" if open_exit.return_code is not None else ""))

                # Set the reverse exit too if the exit is two-way
                if open_exit.return_code is not None:
                    link: HWEntrance = multiworld.get_entrance(code_to_exit[link_code].name, player)
                    link.connect(open_exit.parent_region)
                    multiworld.worlds[player].exit_swaps[link.exit_code] = open_exit.return_code
                    link.linked = True
                    open_codes.remove(open_exit.return_code)

                open_exit.connect(link_region)
                multiworld.worlds[player].exit_swaps[open_exit.exit_code] = link_code
                open_exit.linked = True
                open_codes.remove(link_code)

                # Find new entrances from new connection
                traversed_regions.append(link_region.name)
                entrances.extend(link_region.exits)
        unconnected = []
        for exit in level_exits:
            # Set exit names
            if not exit.linked:
                unconnected.append(exit)
        if len(unconnected) > 0:
            # print(" !!! Failed to connect entrances properly, trying again...")
            # Give up and disconnect all the entrances
            while len(level_exits) > 0:
                unconnect = level_exits.pop()
                if unconnect.linked:
                    disconnect_linked_exit(unconnect)
            # If random start exit is on we have to remove the failed entrance
            if get_option(multiworld, player, option_names.random_start_exit):
                start_entrance.parent_region.exits.remove(start_entrance)
                start_entrance.connected_region.entrances.remove(start_entrance)
            return False
        return True
    else:
        # Create entrances
        for connection in level_exits:
            connection.connect(connection.target_region)
        return True


class EntranceBlockType(Enum):
    Unblocked = 0
    Blocked = 1  # Blocked means you cannot progress without being on the other side, effectively dead end
    DeadEnd = 2
    OneWay = 3


# Required traversed regions is of the exit_code of the original entrance that requires them
c_entrance_block_types = {  # (act, EntranceBlockType, required traversed regions)
    entrance_names.c_p1_1: (1, EntranceBlockType.DeadEnd, None),  # Technically not a dead end if shortcut portal is enabled
    entrance_names.c_p1_2: (1, EntranceBlockType.Unblocked, None),  # Leads to 3
    entrance_names.c_p1_3: (1, EntranceBlockType.Unblocked, None),
    entrance_names.c_p1_4: (1, EntranceBlockType.DeadEnd, None),
    entrance_names.c_p1_10: (1, EntranceBlockType.DeadEnd, None),
    entrance_names.c_p1_20: (1, EntranceBlockType.DeadEnd, None),  # Portal exit, same note as 1 ^
    entrance_names.c_p2_0: (1, EntranceBlockType.Unblocked, None),  # Leads to 1, 3 (2 is blocked)
    entrance_names.c_p2_1: (1, EntranceBlockType.Unblocked, None),
    entrance_names.c_p2_2: (1, EntranceBlockType.Unblocked, None),  # Leads to 0, 1,
    entrance_names.c_p2_3: (1, EntranceBlockType.Blocked, None),  # Blocked by South spikes
    entrance_names.c_p3_0: (1, EntranceBlockType.Unblocked, None),  # Is blocked from other exits, but leads to 1, 10, b_ent
    entrance_names.c_p3_1: (1, EntranceBlockType.Blocked, None),  # Blocked by spikes
    entrance_names.c_p3_10: (1, EntranceBlockType.Unblocked, None),  # Leads to 100
    entrance_names.c_p3_b_return: (1, EntranceBlockType.OneWay, None),  # Leads to 10, b_ent, 1
    entrance_names.c_p3_portal: (1, EntranceBlockType.Unblocked, None),
    entrance_names.c_p3_b_ent: (1, EntranceBlockType.Unblocked, None),
    entrance_names.c_p3_boss: (1, EntranceBlockType.Unblocked, None),
    entrance_names.c_n1_0: (1, EntranceBlockType.Unblocked, None),
    entrance_names.c_b1_0: (2, EntranceBlockType.Unblocked,
                           [castle_region_names.p1_from_p3_n, castle_region_names.p2_s, castle_region_names.p3_s_gold_gate]),
    entrance_names.c_b1_1: (2, EntranceBlockType.DeadEnd, None),
    # Technically blocked, but after the wall opens can't move on
    entrance_names.c_a1_0: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a1_1: (2, EntranceBlockType.DeadEnd, None),
    entrance_names.c_a1_a2: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a1_a3: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a1_boss: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a2_0: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a2_1: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a2_2: (2, EntranceBlockType.Blocked, None),  # Need to push button to open walls
    entrance_names.c_a2_3: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a2_10: (2, EntranceBlockType.OneWay, None),
    entrance_names.c_a2_88: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a3_0: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a3_1: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_a3_2: (2, EntranceBlockType.Blocked, None),  # Need to activate glass bridge
    entrance_names.c_n2_0: (2, EntranceBlockType.Unblocked, None),
    entrance_names.c_b2_0: (3, EntranceBlockType.Unblocked,
                           [castle_region_names.a1_w, castle_region_names.a2_ne, castle_region_names.a3_main]),
    entrance_names.c_b2_1: (3, EntranceBlockType.DeadEnd, None),
    entrance_names.c_r1_0: (3, EntranceBlockType.Unblocked, None),
    entrance_names.c_r1_1: (3, EntranceBlockType.Unblocked, None),
    entrance_names.c_r1_2: (3, EntranceBlockType.Blocked, None),
    entrance_names.c_r2_0: (3, EntranceBlockType.Unblocked, None),
    entrance_names.c_r2_1: (3, EntranceBlockType.DeadEnd, None),
    entrance_names.c_r2_2: (3, EntranceBlockType.Blocked, None),
    entrance_names.c_r2_200: (3, EntranceBlockType.DeadEnd, None),  # Not a dead end if you aren't a coward :)
    entrance_names.c_r3_0: (3, EntranceBlockType.Unblocked, None),
    entrance_names.c_r3_b_return: (3, EntranceBlockType.OneWay, None),
    entrance_names.c_r3_boss: (3, EntranceBlockType.Blocked, None),  # Need to open wall
    entrance_names.c_r3_b_ent: (3, EntranceBlockType.Blocked, None),
    entrance_names.c_r3_250: (3, EntranceBlockType.Blocked, None),
    entrance_names.c_n3_0: (3, EntranceBlockType.OneWay, None),  # Nothing is blocked so we can make this one way
    entrance_names.c_n3_12: (3, EntranceBlockType.Unblocked, None),
    entrance_names.c_n3_80: (3, EntranceBlockType.DeadEnd, None),
    entrance_names.c_b3_0: (4, EntranceBlockType.Unblocked,
                              [castle_region_names.r2_bswitch, castle_region_names.r2_n, castle_region_names.r3_main]),
    entrance_names.c_b3_1: (4, EntranceBlockType.DeadEnd, None),
    entrance_names.c_c1_0: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_c1_75: (4, EntranceBlockType.OneWay, None),
    entrance_names.c_c1_99: (4, EntranceBlockType.OneWay, None),
    entrance_names.c_c1_100: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_c1_169: (4, EntranceBlockType.Blocked, None),
    entrance_names.c_c2_0: (4, EntranceBlockType.Unblocked, None),  # Blocked by spikes from other entrances
    entrance_names.c_c2_boss: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_c2_45: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_c2_50: (4, EntranceBlockType.OneWay, None),  # One way island
    entrance_names.c_c2_77: (4, EntranceBlockType.OneWay, None),  # One way wall
    entrance_names.c_c2_b_ent: (4, EntranceBlockType.Blocked, None),
    entrance_names.c_c2_105: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_c2_125: (4, EntranceBlockType.OneWay, None),  # Blocked by wall from other entrances
    entrance_names.c_c3_0: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_c3_54: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_c3_67: (4, EntranceBlockType.OneWay, [castle_region_names.c3_nw]),
    entrance_names.c_c3_156: (4, EntranceBlockType.OneWay, None),  # Blocked by wall from other entrances
    entrance_names.c_n4_0: (4, EntranceBlockType.Unblocked, None),
    entrance_names.c_b4_0: (5, EntranceBlockType.DeadEnd,
                              [castle_region_names.c2_main, castle_region_names.c2_tp_island, castle_region_names.c3_nw]),
    # Technically not a dead end, but no entrances beyond are shuffled
    entrance_names.c_p_return_0: (1, EntranceBlockType.DeadEnd, None),
}

c_passage_blocking_codes = {
    castle_region_names.p1_from_p3_n: entrance_names.c_p1_10,
    castle_region_names.p2_s: entrance_names.c_p2_3,  # Not actually connected, got a gate in the way
    castle_region_names.a2_ne: entrance_names.c_a2_0,
    castle_region_names.a3_main: entrance_names.c_a3_0,
    castle_region_names.r2_bswitch: entrance_names.c_r2_1,
    castle_region_names.r2_n: entrance_names.c_r2_0,
    castle_region_names.c2_tp_island: entrance_names.c_c2_50,
    castle_region_names.c3_nw: entrance_names.c_c3_54,
    castle_region_names.b1_defeated: entrance_names.c_b1_0,
    castle_region_names.b2_defeated: entrance_names.c_b2_0,
    castle_region_names.b3_defeated: entrance_names.c_b3_0,
}

t_entrance_block_types = {  # (act, EntranceBlockType)
    entrance_names.t_hub_t_ent: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_hub_library: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_hub_t3: (1, EntranceBlockType.Blocked, None),
    # Blocked because you need to talk to Lyron to clear the rocks!
    entrance_names.t_hub_pof: (1, EntranceBlockType.Unblocked, None),  # Locations to raise pyramids for PoF entrance
    entrance_names.t_hub_pof_return: (1, EntranceBlockType.OneWay, None),  # This is the bonus completion return
    entrance_names.t_lib_start: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_lib_lobby_end: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_lib_books: (1, EntranceBlockType.Unblocked, None),
    # entrance_names.t_lib_end: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_c1_start: (1, EntranceBlockType.OneWay, None),
    entrance_names.t_c1_end: (1, EntranceBlockType.Unblocked, None),  # Can't get back to the start, but can get to hub portal
    entrance_names.t_c1_fall_surface: (1, EntranceBlockType.OneWay, [temple_region_names.cave_3_main]),
    # Not actually required, to enforce that the right exits in the hub will have items
    entrance_names.t_c1_portal: (1, EntranceBlockType.DeadEnd, [temple_region_names.boss2_defeated]),
    entrance_names.t_c1_fall_temple: (1, EntranceBlockType.OneWay, None),
    entrance_names.t_c2_start: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_c2_end: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_c3_start: (1, EntranceBlockType.Unblocked, None),
    entrance_names.t_c3_end: (1, EntranceBlockType.Blocked, None),  # Need a switch/switches to cross bridge
    entrance_names.t_c3_boss: (1, EntranceBlockType.Blocked, None),  # Need green switch
    entrance_names.t_b1_start: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_b1_end: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_ent_start: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_ent_start_2: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_ent_exit: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_0: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_1: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_2: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_3: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_4: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_end_0: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_end_1: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_end_2: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_end_3: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_mid_end_4: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_end_0: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_end_1: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_end_2: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_p_end_end: (2, EntranceBlockType.Unblocked, None),
    entrance_names.t_b2: (3, EntranceBlockType.DeadEnd, [temple_region_names.cave_2_main]),
    entrance_names.t_t1_start: (3, EntranceBlockType.Unblocked, None),
    entrance_names.t_t1_end: (3, EntranceBlockType.Unblocked, None),  # Technically unblocked, but it's kinda hard
    entrance_names.t_t2_start_1: (3, EntranceBlockType.Blocked, None),
    entrance_names.t_t2_start_2: (3, EntranceBlockType.Blocked, None),
    entrance_names.t_t2_w_portal: (3, EntranceBlockType.Unblocked,
                                  [temple_region_names.boss2_defeated]),  # Can go through the gate to the main area
    entrance_names.t_t2_s_light_bridge: (3, EntranceBlockType.Blocked, None),  # Need glass walk
    entrance_names.t_t2_t3: (3, EntranceBlockType.Blocked, None),  # Need column gate on the other side
    entrance_names.t_t3_start_1: (3, EntranceBlockType.Unblocked,
                                 [temple_region_names.cave_1_main, temple_region_names.cave_2_main,
                                  temple_region_names.cave_3_main]),
    # Not actually required, to enforce that the right exits in the hub will have items
    entrance_names.t_t3_start_2: (3, EntranceBlockType.Unblocked,
                                 [temple_region_names.cave_1_main, temple_region_names.cave_2_main,
                                  temple_region_names.cave_3_main]),
    entrance_names.t_t3_start_3: (3, EntranceBlockType.Unblocked,
                                 [temple_region_names.cave_1_main, temple_region_names.cave_2_main,
                                  temple_region_names.cave_3_main]),
    entrance_names.t_c3_temple: (3, EntranceBlockType.DeadEnd, [temple_region_names.boss2_defeated]),
    entrance_names.t_t3_t2: (3, EntranceBlockType.Blocked, None),  # Could be blocked, so we assume worst case
    entrance_names.t_t_ent_hub: (3, EntranceBlockType.Blocked, None),
    entrance_names.t_t_ent_temple: (3, EntranceBlockType.Unblocked, None),
    entrance_names.t_t_ent_p: (3, EntranceBlockType.Unblocked, None),
    entrance_names.t_n1_1_start: (3, EntranceBlockType.Unblocked,
                                 [temple_region_names.cave_3_portal, temple_region_names.cave_2_pumps,
                                  temple_region_names.cave_1_blue_bridge, temple_region_names.t1_east,
                                  temple_region_names.t2_s_gate, temple_region_names.boss2_defeated]),
    entrance_names.t_n1_1_sw: (3, EntranceBlockType.Unblocked, None),
    entrance_names.t_n1_1_n: (3, EntranceBlockType.DeadEnd, [temple_region_names.pof_1_se_room]),
    entrance_names.t_n1_2_start: (3, EntranceBlockType.OneWay,
                                 [temple_region_names.pof_1_n_room, temple_region_names.pof_1_se_room]),
    entrance_names.t_n1_20: (3, EntranceBlockType.Blocked, None),
    entrance_names.t_n1_2_nw: (3, EntranceBlockType.Unblocked, None),
    entrance_names.t_n1_2_n: (3, EntranceBlockType.DeadEnd, None),
    entrance_names.t_n1_1_ne: (3, EntranceBlockType.Blocked, None),
    entrance_names.t_n1_1_se: (3, EntranceBlockType.DeadEnd, None),
    entrance_names.t_n1_100: (3, EntranceBlockType.Blocked, None),
    entrance_names.t_n1_3_start: (3, EntranceBlockType.OneWay, [temple_region_names.pof_2_n]),
}

t_passage_blocking_codes = {
    temple_region_names.cave_3_main: entrance_names.t_c1_start,  # There are more entrances, but use this one for now
    temple_region_names.cave_2_main: entrance_names.t_c2_start,
    temple_region_names.cave_2_pumps: entrance_names.t_c2_start,
    temple_region_names.cave_1_main: entrance_names.t_c3_start,
    temple_region_names.cave_1_blue_bridge: entrance_names.t_c3_start,
    temple_region_names.t1_east: entrance_names.t_t1_end,
    temple_region_names.t2_s_gate: entrance_names.t_t2_w_portal,
    temple_region_names.boss2_defeated: entrance_names.t_b2,
    temple_region_names.cave_3_portal: entrance_names.t_c1_portal,
    temple_region_names.pof_1_n_room: entrance_names.t_n1_1_n,
    temple_region_names.pof_2_n: entrance_names.t_n1_2_n,
    temple_region_names.pof_1_se_room: entrance_names.t_n1_1_se,
}


def get_valid_exits(entrance_block_types, open_codes: typing.List[str], code_to_region: typing.Dict[str, Region],
                    traversed_regions, open_exits: typing.List[HWEntrance], entrance: HWEntrance,
                    needed_codes: typing.List[str], act_range=4):
    act = entrance_block_types[entrance.return_code if entrance.return_code is not None else entrance.exit_code][0]
    exit_count = len(open_exits)
    open_exit_codes = [exit.return_code for exit in open_exits]
    exits: typing.List[str] = []
    valid_exits: typing.List[str] = []
    # type_match_exits: typing.Dict[int, typing.List[str]] = {}
    # for a in range(5):
    #     type_match_exits[a] = []
    type_match_exits: typing.List[str] = []
    for exit_code in open_codes:
        if exit_code == entrance.return_code:
            continue  # Can't connect an entrance to itself!
        data = entrance_block_types[exit_code]
        if (entrance.return_code is not None) == (data[1] == EntranceBlockType.OneWay):
            continue  # Only shuffle one way transitions together
        act_dist = abs(act - data[0])
        # type_match_exits[act_dist].append(exit_code)
        type_match_exits.append(exit_code)
        if code_to_region[exit_code].name in traversed_regions:
            continue  # If we can reach the destination then don't consider the transition
        # if exit_count <= 1 and exit_code in open_exit_codes:
        if exit_code in open_exit_codes:
            continue  # If we only have 2 exits don't connect them with each other
        # if act_range == 0:  # Special handling for boss levels when act range is 0
        #     if exit_code.startswith("boss"):
        #         if exit_code.endswith("0"):
        #             act_dist -= 1
        #         else:
        #             continue
        if act_dist > act_range:
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
            # for a in range(len(type_match_exits)):
            #     if len(type_match_exits[a]) > 0:
            #         return type_match_exits[a]
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
    entrance.parent_region.exits.remove(entrance)
    entrance.connected_region.entrances.remove(entrance)
    del entrance


def set_door_access_rules(multiworld: MultiWorld, player: int, door_counts: typing.Dict[str, int],
                          loop_entrances: typing.List[typing.List[HWEntrance]]):
    # Set dynamic key/door access rules
    menu_region = multiworld.get_region(castle_region_names.menu, player)

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

    if get_campaign(multiworld, player) == Campaign.Castle:
        # Disconnect level exits and pretend that you need to go through the boss switch areas to the boss
        remove_entrances = [
            multiworld.get_entrance(etr_base_name(castle_region_names.p3_sw, castle_region_names.b1_start), player),
            multiworld.get_entrance(etr_base_name(castle_region_names.a1_start, castle_region_names.b2_start), player),
            multiworld.get_entrance(etr_base_name(castle_region_names.r3_exit, castle_region_names.b3_start), player),
            multiworld.get_entrance(etr_base_name(castle_region_names.c2_main, castle_region_names.b4_start), player),
        ]
        add_entrances = [
            copy_entrance_dest("P1 Boss Switch", castle_region_names.p1_from_p3_n, remove_entrances[0]),
            copy_entrance_dest("P3 Boss Switch", castle_region_names.p3_s_gold_gate, remove_entrances[0]),
            copy_entrance_dest("A1 Boss Switch", castle_region_names.a1_w, remove_entrances[1]),
            copy_entrance_dest("A2 Boss Switch", castle_region_names.a2_ne, remove_entrances[1]),
            copy_entrance_dest("R2 Boss Switch", castle_region_names.r2_n, remove_entrances[2]),
            copy_entrance_dest("C1 Boss Switch", castle_region_names.c2_tp_island, remove_entrances[3]),
            copy_entrance_dest("C2 Boss Switch", castle_region_names.c2_c3_tp, remove_entrances[3]),
            copy_entrance_dest("C3 Boss Switch", castle_region_names.c3_rspike_switch, remove_entrances[3]),
            copy_entrance_dest("C3 Portal", castle_region_names.c3_nw,
                               multiworld.get_entrance(etr_base_name(castle_region_names.c3_sw_hidden,
                                                                     castle_region_names.c3_fire_floor), player)),
        ]
    else:
        remove_entrances = [
            # multiworld.get_entrance('Temple Entrance Back__', player),
        ]
        add_entrances = [
            add_entrance("T3 Psuedo Entrance", temple_region_names.t3_s_node_blocks_1,
                         temple_region_names.t3_s_node_blocks_2)
        ]
    for remove in remove_entrances:
        remove.parent_region.exits.remove(remove)
        remove.connected_region.entrances.remove(remove)

    # Set downstream costs - the keys that are required after a specific entrance
    key_names = get_active_key_names(multiworld, player)
    start_exits = [exit for exit in menu_region.exits if exit.connected_region.name != castle_region_names.get_planks]
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
    for remove in remove_entrances:
        remove.parent_region.exits.append(remove)
        remove.connected_region.entrances.append(remove)

    transitions = multiworld.get_entrances()
    for exit in transitions:
        if exit.player != player:
            continue
        if exit.pass_item is None or exit.parent_region.name == exit.connected_region.name:
            continue
        # If the items are consumed gotta use the downstream cost logic
        if exit.items_consumed and exit.pass_item in door_counts.keys():
            needed_keys = door_counts[exit.pass_item] - exit.downstream_count
            # print(f"{exit.parent_region} -> {exit.connected_region} - {exit.pass_item}: {needed_keys}")
            add_rule(exit, lambda state, this=exit, num=needed_keys: state.has(this.pass_item, player, num), "and")
        else:  # Elsewise just set the item rule normally
            add_rule(exit, lambda state, this=exit: state.has(this.pass_item, player, this.item_count), "and")


def set_downstream_costs(item: str, entrance: HWEntrance, seen):
    entr_id = get_entrance_id(entrance)
    seen.append(entr_id)
    seen = seen.copy()  # Create a copy so that independent pathways don't lock each other
    door_entrances: typing.Set[str] = set()
    cost_dict: typing.Dict[str] = {}
    if entrance.parent_region != entrance.connected_region:
        for exit in entrance.connected_region.exits:
            if get_entrance_id(exit) in seen and exit.connected_region.name != exit.parent_region.name:
                continue
            entrances = set_downstream_costs(item, exit, seen)
            cost_dict.update(entrances)
    if entrance.pass_item == item:
        # Just assume the item count is 1, doors should never cost more
        door_entrances.add(entr_id)
        if entrance.downstream_count == 0:
            for cost in cost_dict.values():
                entrance.downstream_count += cost
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
