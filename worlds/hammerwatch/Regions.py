import typing

from BaseClasses import MultiWorld, Region, RegionType, Entrance
from .Items import HammerwatchItem
from .Locations import HammerwatchLocation, location_table
from .Names import LocationName, ItemName, RegionName


def create_regions(world, player: int, active_locations):
    if world.map[player] == 0:
        pass
    else:
        create_tots_regions(world, player, active_locations)


def create_tots_regions(world, player: int, active_locations):
    used_names: typing.Dict[str, int] = {}

    menu_region = create_region(world, player, active_locations, RegionName.menu, None)

    hub_main_locations = [
        LocationName.hub_front_of_pof,
        LocationName.hub_behind_temple_entrance
    ]
    dunes_main_region = create_region(world, player, active_locations, RegionName.hub_main, hub_main_locations)

    dunes_rocks_locations = [
        LocationName.hub_behind_shops,
        # LocationName.hub_on_rock,
        # LocationName.hub_west_pyramid,
        LocationName.hub_rocks_south,
        LocationName.hub_field_south,
        LocationName.hub_field_nw,
        LocationName.hub_field_north,
        LocationName.victory
    ]
    dunes_rocks_region = create_region(world, player, active_locations, RegionName.hub_rocks,
                                       dunes_rocks_locations)

    dunes_pyramid_locations = [
        # LocationName.hub_pof_reward
    ]
    dunes_pyramid_region = create_region(world, player, active_locations, RegionName.hub_pyramid_of_pain,
                                         dunes_pyramid_locations)

    world.regions += [
        menu_region,
        dunes_main_region,
        dunes_rocks_region,
        # dunes_pyramid_locations
    ]

    # Connections
    connect(world, player, used_names, RegionName.menu, RegionName.hub_main)
    connect(world, player, used_names, RegionName.hub_main, RegionName.hub_rocks,
            lambda state: (state.has(ItemName.pickaxe, player, 1)))


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
