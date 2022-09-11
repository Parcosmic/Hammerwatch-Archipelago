import typing

from BaseClasses import Location
from .Names import LocationName
from .Util import Counter
from random import Random


class HammerwatchLocation(Location):
    game: str = "Hammerwatch"

    def __init__(self, player: int, name: str = '', code: int = None, parent=None):
        super().__init__(player, name, code, parent)
        self.event = code is None


castle_pickup_locations: typing.Dict[str, int] = {

}

castle_recovery_location_names: typing.List[str] = [
]

castle_shop_locations: typing.Dict[str, int] = {

}

castle_event_locations: typing.Dict[str, None] = {

}

castle_locations: typing.Dict[str, int] = {
    **castle_pickup_locations,
    **castle_event_locations
}

counter = Counter(0x130000)
temple_pickup_locations: typing.Dict[str, int] = {
    LocationName.hub_field_nw: counter.count(),
    LocationName.hub_on_rock: counter.count(),
    LocationName.hub_pof_reward: counter.count(),
    LocationName.hub_west_pyramid: counter.count(),
    LocationName.hub_rocks_south: counter.count(),
    LocationName.hub_field_north: counter.count(),
    LocationName.hub_behind_temple_entrance: counter.count(),
    LocationName.hub_behind_shops: counter.count(),
    LocationName.hub_front_of_pof: counter.count(),
    LocationName.hub_field_south: counter.count(),

    LocationName.cave3_portal_r: counter.count(),
    LocationName.cave3_n: counter.count(),
    LocationName.cave3_outside_guard: counter.count(),
    LocationName.cave3_portal_l: counter.count(),
    LocationName.cave3_fall_se: counter.count(),
    LocationName.cave3_ne: counter.count(),
    LocationName.cave3_nw: counter.count(),
    LocationName.cave3_m: counter.count(),
    LocationName.cave3_se: counter.count(),
    LocationName.cave3_captain: counter.count(),
    LocationName.cave3_fall_sw: counter.count(),
    LocationName.cave3_squire: counter.count(),
    LocationName.cave3_captain_dock: counter.count(),
    LocationName.cave3_fall_ne: counter.count(),
    LocationName.cave3_fields_r: counter.count(),
    LocationName.cave3_trapped_guard: counter.count(),
    LocationName.cave3_secret_n: counter.count(),
    LocationName.cave3_secret_nw: counter.count(),
    LocationName.cave3_secret_s: counter.count(),
    LocationName.cave3_secret_6: counter.count(),
    LocationName.cave3_secret_7: counter.count(),
    LocationName.cave3_secret_8: counter.count(),
    LocationName.cave3_secret_5: counter.count(),
    LocationName.cave3_secret_2: counter.count(),
    LocationName.cave3_secret_3: counter.count(),
    LocationName.cave3_secret_4: counter.count(),
    LocationName.cave3_secret_1: counter.count(),
    LocationName.cave3_secret_9: counter.count(),
    LocationName.cave3_secret_10: counter.count(),
    LocationName.cave3_secret_11: counter.count(),
    LocationName.cave3_secret_12: counter.count(),
    LocationName.cave3_fall_nw: counter.count(),
    LocationName.cave3_half_bridge: counter.count(),
    LocationName.cave3_guard: counter.count(),

    LocationName.cave2_sw_room_3: counter.count(),
    LocationName.cave2_pumps_wall_r: counter.count(),
    LocationName.cave2_below_pumps_1: counter.count(),
    LocationName.cave2_below_pumps_2: counter.count(),
    LocationName.cave2_double_bridge_l_1: counter.count(),
    LocationName.cave2_double_bridge_l_2: counter.count(),
    LocationName.cave2_e_1: counter.count(),
    LocationName.cave2_e_2: counter.count(),
    LocationName.cave2_nw_4: counter.count(),
    LocationName.cave2_nw_5: counter.count(),
    LocationName.cave2_pumps_wall_l: counter.count(),
    LocationName.cave2_water_n_r_2: counter.count(),
    LocationName.cave2_water_s: counter.count(),
    LocationName.cave2_w_miniboss_3: counter.count(),
    LocationName.cave2_w_miniboss_2: counter.count(),
    LocationName.cave2_w_miniboss_1: counter.count(),
    LocationName.cave2_red_bridge_se_1: counter.count(),
    LocationName.cave2_red_bridge_se_2: counter.count(),
    LocationName.cave2_e_3: counter.count(),
    LocationName.cave2_e_4: counter.count(),
    LocationName.cave2_guard_n: counter.count(),
    LocationName.cave2_red_bridge_2: counter.count(),
    LocationName.cave2_double_bridge_m: counter.count(),
    LocationName.cave2_nw_2: counter.count(),
    LocationName.cave2_red_bridge_4: counter.count(),
    LocationName.cave2_double_bridge_r: counter.count(),
    LocationName.cave2_water_n_r_1: counter.count(),
    LocationName.cave2_green_bridge: counter.count(),
    LocationName.cave2_sw_room_1: counter.count(),
    LocationName.cave2_guard_s: counter.count(),
    LocationName.cave2_nw_3: counter.count(),
    LocationName.cave2_w_miniboss_4: counter.count(),
    LocationName.cave2_red_bridge_3: counter.count(),
    LocationName.cave2_below_pumps_3: counter.count(),
    LocationName.cave2_secret_ne: counter.count(),
    LocationName.cave2_secret_w: counter.count(),
    LocationName.cave2_secret_m: counter.count(),
    LocationName.cave2_water_n_l: counter.count(),
    LocationName.cave2_nw_1: counter.count(),
    LocationName.cave2_sw: counter.count(),
    LocationName.cave2_double_bridge_secret: counter.count(),
    LocationName.cave2_sw_room_2: counter.count(),
    LocationName.cave2_pumps_n: counter.count(),
    LocationName.cave2_guard: counter.count(),
    LocationName.cave2_red_bridge_1: counter.count(),
    LocationName.cave2_sw_room_4: counter.count(),
}

temple_recovery_location_names: typing.List[str] = [
    LocationName.cave3_n,
    LocationName.cave3_outside_guard
]

temple_shop_locations: typing.Dict[str, int] = {

}

temple_event_locations: typing.Dict[str, None] = {
    # LocationName.visit_temple_entrance: None,
    # LocationName.pof_switch_hub: None
}

temple_locations: typing.Dict[str, int] = {
    **temple_pickup_locations,
    **temple_event_locations
}

common_event_locations: typing.Dict[str, None] = {
    LocationName.victory: None,
}

all_locations: typing.Dict[str, int] = {
    **castle_locations,
    **castle_shop_locations,
    **temple_locations,
    **temple_shop_locations,
    **common_event_locations
}


def setup_locations(world, player: int):
    location_table: typing.Dict[str, int]

    if world.map[player] == 0:  # Castle Hammerwatch
        location_table = {**castle_locations}
        if world.random_location_behavior[player] == 1:
            location_table = choose_castle_random_locations(world, player, location_table)
        if not world.randomize_recovery_items[player].value:
            for name in castle_recovery_location_names:
                location_table.pop(name)
        if world.randomize_shops[player].value:
            location_table.update({**castle_shop_locations})
        location_table.update(castle_event_locations)
    else:  # Temple of the Sun
        location_table = {**temple_locations}
        if world.random_location_behavior[player] == 1:
            # location_table = choose_tots_random_locations(world, player, location_table)
            pass
        if not world.randomize_recovery_items[player].value:
            for name in temple_recovery_location_names:
                location_table.pop(name)
        if world.randomize_shops[player].value:
            location_table.update({**temple_shop_locations})
        location_table.update(temple_event_locations)

    location_table.update(common_event_locations)

    return location_table


def choose_castle_random_locations(world, player: int, location_table: typing.Dict[str, int]):

    return location_table


def choose_tots_random_locations(world, player: int, location_table: typing.Dict[str, int]):
    if world.random_location_behavior[player].value == 1:
        random = Random()
        random.seed(random, world.seed)
        # Squire location
        if Random.randrange(random, 6) != 0:
            location_table.pop(LocationName.cave3_squire)
        # Remove all pan locations until there is only one left
        locs = 2
        for l in range(locs):
            location = random.choice(pan_locations)
            location_table.pop(location)
    return location_table


pan_locations: typing.List = [
    LocationName.cave3_nw,
    LocationName.cave3_m,
    LocationName.cave3_se,
    LocationName.cave2_nw_2,
    LocationName.cave2_red_bridge_3,
    LocationName.cave2_double_bridge_r,
]


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
