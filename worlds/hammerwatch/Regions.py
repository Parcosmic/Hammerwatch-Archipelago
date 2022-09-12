import typing

from BaseClasses import MultiWorld, Region, RegionType, Entrance
from .Items import HammerwatchItem
from .Locations import HammerwatchLocation, LocationData, LocationClassification
from .Names import LocationName, ItemName, RegionName


def create_regions(world, player: int, active_locations: typing.Dict[str, LocationData]):
    if world.map[player] == 0:
        pass
    else:
        create_tots_regions(world, player, active_locations)


def create_tots_regions(world, player: int, active_locations: typing.Dict[str, LocationData]):
    menu_region = create_region(world, player, active_locations, RegionName.menu, None)

    hub_main_locations = [
        LocationName.hub_front_of_pof,
        LocationName.hub_behind_temple_entrance
    ]
    dunes_main_region = create_region(world, player, active_locations, RegionName.hub_main, hub_main_locations)

    dunes_rocks_locations = [
        LocationName.hub_behind_shops,
        LocationName.hub_on_rock,
        LocationName.hub_west_pyramid,
        LocationName.hub_rocks_south,
        LocationName.hub_field_south,
        LocationName.hub_field_nw,
        LocationName.hub_field_north,
        LocationName.hub_pof_switch
    ]
    dunes_rocks_region = create_region(world, player, active_locations, RegionName.hub_rocks,
                                       dunes_rocks_locations)

    dunes_pyramid_locations = [
        LocationName.hub_pof_reward
    ]
    dunes_pyramid_region = create_region(world, player, active_locations, RegionName.hub_pyramid_of_fear,
                                         dunes_pyramid_locations)

    pof_1_locations = [

    ]
    pof_1_region = create_region(world, player, active_locations, RegionName.pof_1, pof_1_locations)

    pof_2_locations = [

    ]
    pof_2_region = create_region(world, player, active_locations, RegionName.pof_2, pof_2_locations)

    pof_3_locations = [
        LocationName.pof_end
    ]
    pof_3_region = create_region(world, player, active_locations, RegionName.pof_3, pof_3_locations)

    library_region = create_region(world, player, active_locations, RegionName.library, [])

    cave3_main_locations = [
        LocationName.cave3_squire,
        LocationName.cave3_guard,
        LocationName.cave3_ne,
        LocationName.cave3_nw,
        LocationName.cave3_m,
        LocationName.cave3_se,
        LocationName.cave3_half_bridge,
        LocationName.cave3_trapped_guard,
        LocationName.cave3_n,
        LocationName.cave3_outside_guard,
        LocationName.cave3_secret_n,
        LocationName.cave3_secret_nw,
        LocationName.cave3_secret_s,
    ]
    cave3_main_region = create_region(world, player, active_locations, RegionName.cave_3_main, cave3_main_locations)

    cave3_fall_locations = [
        LocationName.cave3_fall_nw,
        LocationName.cave3_fall_ne,
        LocationName.cave3_fall_sw,
        LocationName.cave3_fall_se
    ]
    cave3_fall_region = create_region(world, player, active_locations, RegionName.cave_3_fall, cave3_fall_locations)

    cave3_fields_locations = [
        LocationName.cave3_fields_r,
        LocationName.cave3_captain,
        LocationName.cave3_captain_dock,
    ]
    cave3_fields_region = create_region(world, player, active_locations, RegionName.cave_3_fields,
                                        cave3_fields_locations)

    cave3_portal_locations = [
        LocationName.cave3_portal_l,
        LocationName.cave3_portal_r,
        LocationName.cave3_pof_switch
    ]
    cave3_portal_region = create_region(world, player, active_locations, RegionName.cave_3_portal,
                                        cave3_portal_locations)

    cave3_secret_locations = [
        LocationName.cave3_secret_1,
        LocationName.cave3_secret_2,
        LocationName.cave3_secret_3,
        LocationName.cave3_secret_4,
        LocationName.cave3_secret_5,
        LocationName.cave3_secret_6,
        LocationName.cave3_secret_7,
        LocationName.cave3_secret_8,
        LocationName.cave3_secret_9,
        LocationName.cave3_secret_10,
        LocationName.cave3_secret_11,
        LocationName.cave3_secret_12,
    ]
    cave3_secret_region = create_region(world, player, active_locations, RegionName.cave_3_secret,
                                        cave3_secret_locations)

    cave2_main_locations = [
        LocationName.cave2_sw_room_3,
        LocationName.cave2_red_bridge_2,
        LocationName.cave2_double_bridge_m,
        LocationName.cave2_nw_2,
        LocationName.cave2_red_bridge_4,
        LocationName.cave2_double_bridge_r,
        LocationName.cave2_green_bridge,
        LocationName.cave2_sw_room_1,
        LocationName.cave2_guard_s,
        LocationName.cave2_nw_3,
        LocationName.cave2_w_miniboss_4,
        LocationName.cave2_red_bridge_3,
        LocationName.cave2_below_pumps_3,
        LocationName.cave2_nw_1,
        LocationName.cave2_sw,
        LocationName.cave2_double_bridge_secret,
        LocationName.cave2_sw_room_2,
        LocationName.cave2_pumps_n,
        LocationName.cave2_guard,
        LocationName.cave2_red_bridge_1,
        LocationName.cave2_sw_room_4,
        LocationName.cave2_below_pumps_1,
        LocationName.cave2_below_pumps_2,
        LocationName.cave2_double_bridge_l_1,
        LocationName.cave2_double_bridge_l_2,
        LocationName.cave2_e_1,
        LocationName.cave2_e_2,
        LocationName.cave2_nw_4,
        LocationName.cave2_nw_5,
        LocationName.cave2_w_miniboss_3,
        LocationName.cave2_w_miniboss_2,
        LocationName.cave2_w_miniboss_1,
        LocationName.cave2_red_bridge_se_1,
        LocationName.cave2_red_bridge_se_2,
        LocationName.cave2_e_3,
        LocationName.cave2_e_4,
        LocationName.cave2_guard_n,
        LocationName.cave2_secret_ne,
        LocationName.cave2_secret_w,
        LocationName.cave2_secret_m,
    ]
    cave2_main_region = create_region(world, player, active_locations, RegionName.cave_2_main, cave2_main_locations)

    cave2_pumps_locations = [
        LocationName.cave2_pumps_wall_r,
        LocationName.cave2_pumps_wall_l,
        LocationName.cave2_water_n_r_1,
        LocationName.cave2_water_n_l,
        LocationName.cave2_pof_switch,
        LocationName.cave2_water_n_r_2,
        LocationName.cave2_water_s,
    ]
    cave2_pumps_region = create_region(world, player, active_locations, RegionName.cave_2_pumps, cave2_pumps_locations)

    cave1_main_locations = [
        LocationName.cave1_n_3,
        LocationName.cave1_w_by_water_2,
        LocationName.cave1_s_3,
        LocationName.cave1_m,
        LocationName.cave1_double_room_l,
        LocationName.cave1_double_room_r,
        LocationName.cave1_n_1,
        LocationName.cave1_n_2,
        LocationName.cave1_w_1,
        LocationName.cave1_w_2,
        LocationName.cave1_s_4,
        LocationName.cave1_s_5,
        LocationName.cave1_n_room_1,
        LocationName.cave1_n_room_2,
        LocationName.cave1_n_room_3,
        LocationName.cave1_n_room_4,
        LocationName.cave1_s_1,
        LocationName.cave1_s_2,
        LocationName.cave1_w_by_water_1,
        LocationName.cave1_secret_nw,
        LocationName.cave1_secret_w,
        LocationName.cave1_secret_m,
    ]
    cave1_main_region = create_region(world, player, active_locations, RegionName.cave_1_main, cave1_main_locations)

    cave1_blue_bridge_locations = [
        LocationName.cave1_ne_room_1,
        LocationName.cave1_ne_room_2,
        LocationName.cave1_ne_room_3,
        LocationName.cave1_ne_room_4,
        LocationName.cave1_ne_room_5,
        LocationName.cave1_ne_grubs,
        LocationName.cave1_secret_tunnel_1,
        LocationName.cave1_n_bridges_1,
        LocationName.cave1_n_bridges_4,
        LocationName.cave1_n_bridges_5,
        LocationName.cave1_secret_n_room,
        LocationName.cave1_pof_switch,
        LocationName.cave1_ne_1,
        LocationName.cave1_ne_2,
        LocationName.cave1_ne_3,
        LocationName.cave1_ne_4,
        LocationName.cave1_ne_5,
        LocationName.cave1_n_bridges_2,
        LocationName.cave1_n_bridges_3,
        LocationName.cave1_secret_tunnel_2,
        LocationName.cave1_secret_tunnel_3,
        LocationName.cave1_secret_ne,
    ]
    cave1_blue_bridge_region = create_region(world, player, active_locations, RegionName.cave_1_blue_bridge,
                                             cave1_blue_bridge_locations)

    cave1_red_bridge_locations = [
        LocationName.cave1_e_2,
        LocationName.cave1_e_3,
        LocationName.cave1_red_bridge_e,
        LocationName.cave1_se_1,
        LocationName.cave1_se_2,
        LocationName.cave1_e_1,
        LocationName.cave1_secret_e,
    ]
    cave1_red_bridge_region = create_region(world, player, active_locations, RegionName.cave_1_red_bridge,
                                            cave1_red_bridge_locations)

    cave1_green_bridge_locations = [
        LocationName.cave1_green_bridge_1,
        LocationName.cave1_green_bridge_2,
        LocationName.cave1_krilith_ledge_n,
        LocationName.cave1_krilith_ledge_e,
        LocationName.cave1_krilith_door,
    ]
    cave1_green_bridge_region = create_region(world, player, active_locations, RegionName.cave_1_green_bridge,
                                              cave1_green_bridge_locations)

    cave1_pumps_locations = [
        LocationName.cave1_water_s_shore,
        LocationName.cave1_water_s_1,
        LocationName.cave1_water_s_2,
        LocationName.cave1_water_s_3,
        LocationName.cave1_water_s_4,
        LocationName.cave1_water_s_5,
    ]
    cave1_pumps_region = create_region(world, player, active_locations, RegionName.cave_1_pumps,
                                       cave1_pumps_locations)

    cave1_temple_locations = [
        LocationName.cave1_temple_hall_1,
        LocationName.cave1_temple_hall_2,
        LocationName.cave1_temple_hall_3,
        LocationName.cave1_temple_end_2,
        LocationName.cave1_temple_end_3,
        LocationName.cave1_temple_end_4,
        LocationName.cave1_temple_end_1,
    ]
    cave1_temple_region = create_region(world, player, active_locations, RegionName.cave_1_temple,
                                        cave1_temple_locations)

    boss1_main_locations = [
        LocationName.boss1_guard_l,
        LocationName.boss1_guard_r_1,
        LocationName.boss1_guard_r_2,
    ]
    boss1_main_region = create_region(world, player, active_locations, RegionName.boss_1_main,
                                      boss1_main_locations)

    boss1_defeated_locations = [
        LocationName.boss1_bridge,
        LocationName.boss1_bridge_n,
        # LocationName.boss1_drop,
        # LocationName.boss1_drop_2,
        LocationName.boss1_secret,
    ]
    boss1_defeated_region = create_region(world, player, active_locations, RegionName.boss_1_defeated,
                                          boss1_defeated_locations)

    # TODO: Add logic for randomizing passage and discarding impossible to reach checks
    passage_entrance_locations = [

    ]
    passage_entrance_region = create_region(world, player, active_locations, RegionName.passage_entrance,
                                            passage_entrance_locations)
    passage_mid_locations = [

    ]
    passage_mid_region = create_region(world, player, active_locations, RegionName.passage_mid, passage_mid_locations)
    passage_end_locations = [

    ]
    passage_end_region = create_region(world, player, active_locations, RegionName.passage_end, passage_end_locations)

    temple_entrance_region = create_region(world, player, active_locations, RegionName.temple_entrance, [])

    temple_entrance_back_locations = [
        LocationName.temple_entrance_l,
        LocationName.temple_entrance_r,
        LocationName.temple_entrance_rock,
        LocationName.victory
    ]
    temple_entrance_back_region = create_region(world, player, active_locations, RegionName.temple_entrance_back,
                                                temple_entrance_back_locations)

    world.regions += [
        menu_region,
        dunes_main_region,
        dunes_rocks_region,
        dunes_pyramid_region,
        pof_1_region,
        pof_2_region,
        pof_3_region,
        library_region,
        cave3_main_region,
        cave3_fall_region,
        cave3_fields_region,
        cave3_portal_region,
        cave3_secret_region,
        cave2_main_region,
        cave2_pumps_region,
        cave1_main_region,
        cave1_blue_bridge_region,
        cave1_red_bridge_region,
        cave1_green_bridge_region,
        cave1_pumps_region,
        cave1_temple_region,
        boss1_main_region,
        boss1_defeated_region,
        passage_entrance_region,
        passage_mid_region,
        passage_end_region,
        temple_entrance_region,
        temple_entrance_back_region,
    ]

    connect_tots_regions(world, player, active_locations)


def connect_tots_regions(world, player: int, active_locations):
    used_names: typing.Dict[str, int] = {}

    connect(world, player, used_names, RegionName.menu, RegionName.hub_main)
    connect(world, player, used_names, RegionName.hub_main, RegionName.hub_rocks,
            lambda state: (state.has(ItemName.pickaxe, player, 1)))
    connect(world, player, used_names, RegionName.hub_main, RegionName.cave_3_fall,
            lambda state: (state.has(ItemName.pickaxe, player, 1)))
    # For the temple entrances in the hub
    # connect(world, player, used_names, RegionName.hub_main, RegionName.temple_3_main,
    # lambda state: (state.has(ItemName.pickaxe, player, 1)))
    connect(world, player, used_names, RegionName.hub_main, RegionName.temple_entrance)
    connect(world, player, used_names, RegionName.hub_main, RegionName.pof_1,
            lambda state: (state.has(ItemName.pof_switch, player, 4)))  # TODO: Don't forget to change this to 6 later!

    connect(world, player, used_names, RegionName.pof_1, RegionName.pof_2)
    connect(world, player, used_names, RegionName.pof_2, RegionName.pof_3)
    connect(world, player, used_names, RegionName.pof_3, RegionName.hub_pyramid_of_fear,
            lambda state: (state.has(ItemName.pof_complete, player, 1)))

    connect(world, player, used_names, RegionName.hub_main, RegionName.library)
    connect(world, player, used_names, RegionName.library, RegionName.cave_3_main)
    connect(world, player, used_names, RegionName.cave_3_main, RegionName.cave_3_fields,
            lambda state: (state.has(ItemName.lever, player, 1)))

    connect(world, player, used_names, RegionName.cave_3_main, RegionName.cave_2_main)
    connect(world, player, used_names, RegionName.cave_2_main, RegionName.cave_2_pumps,
            lambda state: (state.has(ItemName.lever, player, 1)))

    connect(world, player, used_names, RegionName.cave_2_main, RegionName.cave_1_main)
    connect(world, player, used_names, RegionName.cave_1_main, RegionName.cave_1_blue_bridge)
    connect(world, player, used_names, RegionName.cave_1_main, RegionName.cave_1_red_bridge)
    connect(world, player, used_names, RegionName.cave_1_main, RegionName.cave_1_pumps)
    connect(world, player, used_names, RegionName.cave_1_pumps, RegionName.cave_1_green_bridge)
    # connect(world, player, used_names, RegionName.temple_2_main, RegionName.cave_1_temple)

    connect(world, player, used_names, RegionName.cave_1_red_bridge, RegionName.boss_1_main)
    connect(world, player, used_names, RegionName.boss_1_main, RegionName.boss_1_defeated,
            lambda state: (state.has(ItemName.key_gold, player, 1)))

    connect(world, player, used_names, RegionName.boss_1_defeated, RegionName.passage_entrance)
    connect(world, player, used_names, RegionName.passage_entrance, RegionName.passage_mid)
    connect(world, player, used_names, RegionName.passage_mid, RegionName.passage_end)

    connect(world, player, used_names, RegionName.passage_end, RegionName.temple_entrance_back)
    connect(world, player, used_names, RegionName.temple_entrance_back, RegionName.temple_entrance,
            lambda state: (state.has(ItemName.open_temple_entrance_shortcut, player, 1)))

    # TODO: Remove this when we add Temple Level 2
    connect(world, player, used_names, RegionName.temple_entrance_back, RegionName.cave_3_portal)


def create_region(world: MultiWorld, player: int, active_locations: typing.Dict[str, LocationData], name: str,
                  locations: typing.List[str]) -> Region:
    ret = Region(name, RegionType.Generic, name, player, world)
    if locations:
        for location in locations:
            if world.randomize_recovery_items[player].value \
                    and active_locations[location].classification == LocationClassification.Recovery:
                continue
            ret.locations.append(HammerwatchLocation(player, location, active_locations[location].code, ret))
    # if exits:
    #     for exit in exits:
    #         ret.exits.append(Entrance(player, exit, ret))

    return ret


def connect(world: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)
