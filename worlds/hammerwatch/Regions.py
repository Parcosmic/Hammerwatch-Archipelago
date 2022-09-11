import typing

from BaseClasses import MultiWorld, Region, RegionType, Entrance
from .Items import HammerwatchItem
from .Locations import HammerwatchLocation
from .Names import LocationName, ItemName, RegionName


def create_regions(world, player: int, active_locations):
    if world.map[player] == 0:
        pass
    else:
        create_tots_regions(world, player, active_locations)


def create_tots_regions(world, player: int, active_locations):
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
    ]
    dunes_rocks_region = create_region(world, player, active_locations, RegionName.hub_rocks,
                                       dunes_rocks_locations)

    dunes_pyramid_locations = [
        LocationName.hub_pof_reward
    ]
    dunes_pyramid_region = create_region(world, player, active_locations, RegionName.hub_pyramid_of_pain,
                                         dunes_pyramid_locations)

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
    ]
    if world.randomize_recovery_items[player].value:
        cave3_main_locations += [
            LocationName.cave3_n,
            LocationName.cave3_outside_guard,
        ]
    cave3_main_locations += [
        LocationName.cave3_secret_n,
        LocationName.cave3_secret_nw,
        LocationName.cave3_secret_s,
    ]
    cave3_main_region = create_region(world, player, active_locations, RegionName.cave_3_main, cave3_main_locations)

    cave3_fall_locations = [
        LocationName.cave3_fall_nw,
        LocationName.cave3_fall_ne,
        LocationName.cave3_fall_sw,
        LocationName.cave3_fall_se,
        LocationName.victory
    ]
    cave3_fall_region = create_region(world, player, active_locations, RegionName.cave_3_fall, cave3_fall_locations)

    cave3_fields_locations = [
        LocationName.cave3_fields_r,
        LocationName.cave3_captain,
        LocationName.cave3_captain_dock,
    ]
    cave3_fields_region = create_region(world, player, active_locations, RegionName.cave_3_fields, cave3_fields_locations)

    cave3_portal_locations = [
        LocationName.cave3_portal_l,
        LocationName.cave3_portal_r,
        # LocationName.cave3_portal_puzzle
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
        LocationName.cave2_secret_ne,
        LocationName.cave2_secret_w,
        LocationName.cave2_secret_m,
        LocationName.cave2_nw_1,
        LocationName.cave2_sw,
        LocationName.cave2_double_bridge_secret,
        LocationName.cave2_sw_room_2,
        LocationName.cave2_pumps_n,
        LocationName.cave2_guard,
        LocationName.cave2_red_bridge_1,
        LocationName.cave2_sw_room_4
    ]
    cave2_main_region = create_region(world, player, active_locations, RegionName.cave_2_main,
                                        cave2_main_locations)

    cave2_pumps_locations = [
        LocationName.cave2_pumps_wall_r,
        LocationName.cave2_pumps_wall_l,
        LocationName.cave2_water_n_r_2,
        LocationName.cave2_water_s,
        LocationName.cave2_water_n_r_1,
        LocationName.cave2_water_n_l,
    ]
    cave2_pumps_region = create_region(world, player, active_locations, RegionName.cave_2_pumps,
                                      cave2_pumps_locations)

    world.regions += [
        menu_region,
        dunes_main_region,
        dunes_rocks_region,
        dunes_pyramid_region,
        library_region,
        cave3_main_region,
        cave3_fall_region,
        cave3_fields_region,
        cave3_portal_region,
        cave3_secret_region,
        cave2_main_region,
        cave2_pumps_region
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
    # connect(world, player, used_names, RegionName.hub_main, RegionName.temple_entrance,
    # lambda state: (state.has(ItemName.visit_temple_entrance, player, 1)))
    connect(world, player, used_names, RegionName.hub_main, RegionName.library)
    connect(world, player, used_names, RegionName.library, RegionName.cave_3_main)
    connect(world, player, used_names, RegionName.cave_3_main, RegionName.cave_3_fields,
            lambda state: (state.has(ItemName.lever, player, 1)))

    connect(world, player, used_names, RegionName.cave_3_main, RegionName.cave_2_main)
    connect(world, player, used_names, RegionName.cave_2_main, RegionName.cave_2_pumps,
            lambda state: (state.has(ItemName.lever, player, 1)))


def create_region(world: MultiWorld, player: int, active_locations: typing.Dict[str, int], name: str,
                  locations: typing.List[str]) -> Region:
    ret = Region(name, RegionType.Generic, name, player, world)
    if locations:
        for location in locations:
            ret.locations.append(HammerwatchLocation(player, location, active_locations[location], ret))
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
