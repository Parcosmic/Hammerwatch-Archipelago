import typing

from BaseClasses import Location
from Names import LocationName
from Util import Counter


class LocationData(typing.NamedTuple):
    code: typing.Optional[int]
    hwid: int


class HammerwatchLocation(Location):
    game: str = "Hammerwatch"

    def __init__(self, player: int, name: str = '', code: int = None, parent=None):
        super().__init__(player, name, code, parent)
        self.event = code is None


castle_pickup_locations: typing.Dict[str, int] = {

}

castle_recovery_locations: typing.Dict[str, int] = {

}

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
    LocationName.hub_front_of_pof: counter.count(),
    LocationName.hub_behind_temple_entrance: counter.count(),

    LocationName.hub_behind_shops: counter.count(),
    LocationName.hub_on_rock: counter.count(),
    LocationName.hub_west_pyramid: counter.count(),
    LocationName.hub_rocks_south: counter.count(),
    LocationName.hub_field_south: counter.count(),
    LocationName.hub_field_nw: counter.count(),
    LocationName.hub_field_north: counter.count(),

    LocationName.hub_pof_reward: counter.count(),

    LocationName.cave3_squire: counter.count(),
    LocationName.cave3_guard: counter.count(),
    LocationName.cave3_ne: counter.count(),
    LocationName.cave3_nw: counter.count(),
    LocationName.cave3_m: counter.count(),
    LocationName.cave3_se: counter.count(),
    LocationName.cave3_half_bridge: counter.count(),
    LocationName.cave3_trapped_guard: counter.count(),

    LocationName.cave3_fall_ne: counter.count(),
    LocationName.cave3_fall_nw: counter.count(),
    LocationName.cave3_fall_se: counter.count(),
    LocationName.cave3_fall_sw: counter.count(),

    LocationName.cave3_fields_r: counter.count(),
    LocationName.cave3_captain: counter.count(),
    LocationName.cave3_captain_dock: counter.count(),

    LocationName.cave3_secret_1: counter.count(),
    LocationName.cave3_secret_2: counter.count(),
    LocationName.cave3_secret_3: counter.count(),
    LocationName.cave3_secret_4: counter.count(),
    LocationName.cave3_secret_5: counter.count(),
    LocationName.cave3_secret_6: counter.count(),
    LocationName.cave3_secret_7: counter.count(),
    LocationName.cave3_secret_8: counter.count(),
    LocationName.cave3_secret_9: counter.count(),
    LocationName.cave3_secret_10: counter.count(),
    LocationName.cave3_secret_11: counter.count(),
    LocationName.cave3_secret_12: counter.count(),

    LocationName.cave3_portal_l: counter.count(),
    LocationName.cave3_portal_r: counter.count(),
    # LocationName.cave3_portal_puzzle: counter.count(),
}

temple_recovery_locations: typing.Dict[str, int] = {
    LocationName.cave3_n: counter.count(),
    LocationName.cave3_outside_guard: counter.count(),
}

temple_shop_locations: typing.Dict[str, int] = {

}

temple_event_locations: typing.Dict[str, None] = {
    LocationName.visit_temple_entrance: None,
    LocationName.pof_switch_hub: None
}

temple_locations: typing.Dict[str, int] = {
    **temple_pickup_locations,
    **temple_event_locations
}

common_event_locations: typing.Dict[str, None] = {
    LocationName.victory: None,
}

all_locations: typing.Dict[str, int] = {
    **castle_pickup_locations,
    **castle_recovery_locations,
    **castle_shop_locations,
    **temple_pickup_locations,
    **temple_recovery_locations,
    **temple_shop_locations,
    **common_event_locations
}

location_table: typing.Dict[str, int] = {

}


def setup_locations(world, player: int):
    location_table: typing.Dict[str, int]

    if world.map[player] == 0:  # Castle Hammerwatch
        location_table = {**castle_locations}
        if world.randomize_recovery_items[player].value:
            location_table.update({**castle_recovery_locations})
        if world.randomize_shops[player].value:
            location_table.update({**castle_shop_locations})
        location_table.update(castle_event_locations)
    else:  # Temple of the Sun
        location_table = {**temple_locations}
        if world.randomize_recovery_items[player].value:
            location_table.update({**temple_recovery_locations})
        if world.randomize_shops[player].value:
            location_table.update({**temple_shop_locations})
        location_table.update(temple_event_locations)

    location_table.update(common_event_locations)

    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
