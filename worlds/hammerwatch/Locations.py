import typing

from BaseClasses import Location
from .Names import LocationName
from .Util import Counter
from random import Random
from enum import Enum


class LocationClassification(Enum):
    Regular = 0
    Recovery = 1
    Secret = 2
    Bonus = 3
    Shop = 4


class LocationData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: LocationClassification = LocationClassification.Regular


class HammerwatchLocation(Location):
    game: str = "Hammerwatch"

    def __init__(self, player: int, name: str = '', code: int = None, parent=None):
        super().__init__(player, name, code, parent)
        self.event = code is None


castle_pickup_locations: typing.Dict[str, LocationData] = {

}

castle_shop_locations: typing.Dict[str, LocationData] = {

}

castle_event_locations: typing.Dict[str, LocationData] = {

}

castle_locations: typing.Dict[str, LocationData] = {
    **castle_pickup_locations,
    **castle_event_locations
}

counter = Counter(0x130000)
temple_pickup_locations: typing.Dict[str, LocationData] = {
    LocationName.hub_field_nw: LocationData(counter.count()),
    LocationName.hub_on_rock: LocationData(counter.count()),
    LocationName.hub_pof_reward: LocationData(counter.count()),
    LocationName.hub_west_pyramid: LocationData(counter.count()),
    LocationName.hub_rocks_south: LocationData(counter.count()),
    LocationName.hub_field_north: LocationData(counter.count()),
    LocationName.hub_behind_temple_entrance: LocationData(counter.count()),
    LocationName.hub_behind_shops: LocationData(counter.count()),
    LocationName.hub_front_of_pof: LocationData(counter.count()),
    LocationName.hub_field_south: LocationData(counter.count()),

    LocationName.cave3_portal_r: LocationData(counter.count()),
    LocationName.cave3_n: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave3_outside_guard: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave3_portal_l: LocationData(counter.count()),
    LocationName.cave3_fall_se: LocationData(counter.count()),
    LocationName.cave3_ne: LocationData(counter.count()),
    LocationName.cave3_nw: LocationData(counter.count()),
    LocationName.cave3_m: LocationData(counter.count()),
    LocationName.cave3_se: LocationData(counter.count()),
    LocationName.cave3_captain: LocationData(counter.count()),
    LocationName.cave3_fall_sw: LocationData(counter.count()),
    LocationName.cave3_squire: LocationData(counter.count()),
    LocationName.cave3_captain_dock: LocationData(counter.count()),
    LocationName.cave3_fall_ne: LocationData(counter.count()),
    LocationName.cave3_fields_r: LocationData(counter.count()),
    LocationName.cave3_trapped_guard: LocationData(counter.count()),
    LocationName.cave3_secret_n: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave3_secret_nw: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave3_secret_s: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave3_secret_6: LocationData(counter.count()),
    LocationName.cave3_secret_7: LocationData(counter.count()),
    LocationName.cave3_secret_8: LocationData(counter.count()),
    LocationName.cave3_secret_5: LocationData(counter.count()),
    LocationName.cave3_secret_2: LocationData(counter.count()),
    LocationName.cave3_secret_3: LocationData(counter.count()),
    LocationName.cave3_secret_4: LocationData(counter.count()),
    LocationName.cave3_secret_1: LocationData(counter.count()),
    LocationName.cave3_secret_9: LocationData(counter.count()),
    LocationName.cave3_secret_10: LocationData(counter.count()),
    LocationName.cave3_secret_11: LocationData(counter.count()),
    LocationName.cave3_secret_12: LocationData(counter.count()),
    LocationName.cave3_fall_nw: LocationData(counter.count()),
    LocationName.cave3_half_bridge: LocationData(counter.count()),
    LocationName.cave3_guard: LocationData(counter.count()),

    LocationName.cave2_sw_room_3: LocationData(counter.count()),
    LocationName.cave2_pumps_wall_r: LocationData(counter.count()),
    LocationName.cave2_below_pumps_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_below_pumps_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_double_bridge_l_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_double_bridge_l_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_nw_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_nw_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_pumps_wall_l: LocationData(counter.count()),
    LocationName.cave2_water_n_r_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_water_s: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_w_miniboss_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_w_miniboss_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_w_miniboss_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_red_bridge_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_red_bridge_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_guard_n: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_red_bridge_2: LocationData(counter.count()),
    LocationName.cave2_double_bridge_m: LocationData(counter.count()),
    LocationName.cave2_nw_2: LocationData(counter.count()),
    LocationName.cave2_red_bridge_4: LocationData(counter.count()),
    LocationName.cave2_double_bridge_r: LocationData(counter.count()),
    LocationName.cave2_water_n_r_1: LocationData(counter.count()),
    LocationName.cave2_green_bridge: LocationData(counter.count()),
    LocationName.cave2_sw_room_1: LocationData(counter.count()),
    LocationName.cave2_guard_s: LocationData(counter.count()),
    LocationName.cave2_nw_3: LocationData(counter.count()),
    LocationName.cave2_w_miniboss_4: LocationData(counter.count()),
    LocationName.cave2_red_bridge_3: LocationData(counter.count()),
    LocationName.cave2_below_pumps_3: LocationData(counter.count()),
    LocationName.cave2_secret_ne: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave2_secret_w: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave2_secret_m: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave2_water_n_l: LocationData(counter.count()),
    LocationName.cave2_nw_1: LocationData(counter.count()),
    LocationName.cave2_sw: LocationData(counter.count()),
    LocationName.cave2_double_bridge_secret: LocationData(counter.count()),
    LocationName.cave2_sw_room_2: LocationData(counter.count()),
    LocationName.cave2_pumps_n: LocationData(counter.count()),
    LocationName.cave2_guard: LocationData(counter.count()),
    LocationName.cave2_red_bridge_1: LocationData(counter.count()),
    LocationName.cave2_sw_room_4: LocationData(counter.count()),

    LocationName.cave1_secret_tunnel_1: LocationData(counter.count()),
    LocationName.cave1_temple_end_3: LocationData(counter.count()),
    LocationName.cave1_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_w_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_w_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_temple_hall_2: LocationData(counter.count()),
    LocationName.cave1_water_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_bridges_4: LocationData(counter.count()),
    LocationName.cave1_double_room_l: LocationData(counter.count()),
    LocationName.cave1_e_3: LocationData(counter.count()),
    LocationName.cave1_green_bridge_2: LocationData(counter.count()),
    LocationName.cave1_n_bridges_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_secret_tunnel_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_w_by_water_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_double_room_r: LocationData(counter.count()),
    LocationName.cave1_krilith_ledge_n: LocationData(counter.count()),
    LocationName.cave1_red_bridge_e: LocationData(counter.count()),
    LocationName.cave1_ne_room_3: LocationData(counter.count()),
    LocationName.cave1_water_s_shore: LocationData(counter.count()),
    LocationName.cave1_temple_end_2: LocationData(counter.count()),
    LocationName.cave1_krilith_door: LocationData(counter.count()),
    LocationName.cave1_temple_end_4: LocationData(counter.count()),
    LocationName.cave1_ne_grubs: LocationData(counter.count()),
    LocationName.cave1_w_by_water_2: LocationData(counter.count()),
    LocationName.cave1_m: LocationData(counter.count()),
    LocationName.cave1_secret_nw: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_n_room: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_ne: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_w: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_m: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_e: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_temple_hall_1: LocationData(counter.count()),
    LocationName.cave1_temple_hall_3: LocationData(counter.count()),
    LocationName.cave1_n_bridges_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_temple_end_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_secret_tunnel_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_3: LocationData(counter.count()),
    LocationName.cave1_ne_room_4: LocationData(counter.count()),
    LocationName.cave1_n_bridges_1: LocationData(counter.count()),
    LocationName.cave1_krilith_ledge_e: LocationData(counter.count()),
    LocationName.cave1_green_bridge_1: LocationData(counter.count()),
    LocationName.cave1_e_2: LocationData(counter.count()),
    LocationName.cave1_s_3: LocationData(counter.count()),
    LocationName.cave1_ne_room_5: LocationData(counter.count()),
    LocationName.cave1_ne_room_1: LocationData(counter.count()),
    LocationName.cave1_ne_room_2: LocationData(counter.count()),
    LocationName.cave1_n_bridges_5: LocationData(counter.count()),

    LocationName.boss1_bridge: LocationData(counter.count()),
    LocationName.boss1_guard_r_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.boss1_guard_r_2: LocationData(counter.count(3), LocationClassification.Recovery),
    # LocationName.boss1_drop_2: LocationData(counter.count()),
    # LocationName.boss1_drop: LocationData(counter.count()),
    LocationName.boss1_guard_l: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.boss1_bridge_n: LocationData(counter.count()),
    LocationName.boss1_secret: LocationData(counter.count(), LocationClassification.Secret),

    # Passage locations

    LocationName.temple_entrance_l: LocationData(counter.count()),
    LocationName.temple_entrance_r: LocationData(counter.count()),
}

temple_shop_locations: typing.Dict[str, LocationData] = {

}

temple_event_locations: typing.Dict[str, LocationData] = {
    LocationName.temple_entrance_rock: LocationData(None),
    LocationName.hub_pof_switch: LocationData(None),
    LocationName.cave3_pof_switch: LocationData(None),
    LocationName.cave2_pof_switch: LocationData(None),
    LocationName.cave1_pof_switch: LocationData(None),
    LocationName.pof_end: LocationData(None),
    # LocationName.pof_switch: LocationData(None)
}

temple_locations: typing.Dict[str, LocationData] = {
    **temple_pickup_locations,
    **temple_event_locations
}

common_event_locations: typing.Dict[str, LocationData] = {
    LocationName.victory: LocationData(None),
}

all_locations: typing.Dict[str, LocationData] = {
    **castle_locations,
    **castle_shop_locations,
    **castle_event_locations,
    **temple_locations,
    **temple_shop_locations,
    **temple_event_locations,
    **common_event_locations
}


def setup_locations(world, player: int):
    location_table: typing.Dict[str, LocationData]

    if world.map[player] == 0:  # Castle Hammerwatch
        location_table = {}
        for name, data in castle_locations.items():
            if data.classification != LocationClassification.Recovery or world.randomize_recovery_items[player].value:
                location_table.update({name: data})
        if world.random_location_behavior[player] == 1:
            # location_table = choose_castle_random_locations(world, player, location_table)
            pass
        if world.randomize_shops[player].value:
            location_table.update({**castle_shop_locations})
        location_table.update(castle_event_locations)
    else:  # Temple of the Sun
        location_table = {}
        for name, data in temple_locations.items():
            if data.classification != LocationClassification.Recovery or world.randomize_recovery_items[player].value == 1:
                location_table.update({name: data})
        if world.random_location_behavior[player] == 1:
            # location_table = choose_tots_random_locations(world, player, location_table)
            pass
        if world.randomize_shops[player].value:
            location_table.update({**temple_shop_locations})
        location_table.update(temple_event_locations)

    location_table.update(common_event_locations)

    return location_table


def choose_castle_random_locations(world, player: int, location_table: typing.Dict[str, LocationData]):

    return location_table


def choose_tots_random_locations(world, player: int, location_table: typing.Dict[str, LocationData]):
    if world.random_location_behavior[player].value == 1:
        random = Random()
        random.seed(random, world.seed)
        # Squire location
        if Random.randrange(random, 6) != 0:
            location_table.pop(LocationName.cave3_squire)
        # Remove all pan locations until there is only one left
        locs = 8
        for l in range(len(pan_locations)-1):
            location = random.choice(pan_locations)
            pan_locations.pop(location)
            location_table.pop(location)
    return location_table


pan_locations: typing.List = [
    LocationName.cave3_nw,
    LocationName.cave3_m,
    LocationName.cave3_se,
    LocationName.cave2_nw_2,
    LocationName.cave2_red_bridge_3,
    LocationName.cave2_double_bridge_r,
    LocationName.cave1_n_bridges_4,
    LocationName.cave1_double_room_l,
    LocationName.cave1_e_3,
]


lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in all_locations.items() if data.code}
