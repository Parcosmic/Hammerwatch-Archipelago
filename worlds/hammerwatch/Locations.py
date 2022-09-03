import typing

from BaseClasses import Location
from .Names import LocationName


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

castle_shop_locations: typing.Dict[str, int] = {

}

castle_locations: typing.Dict[str, int] = {
    **castle_pickup_locations
}

temple_pickup_locations: typing.Dict[str, int] = {
    LocationName.hub_front_of_pof: 0x130000+138376,
    LocationName.hub_behind_temple_entrance: 0x130001+137867,

    LocationName.hub_behind_shops: 0x130002+110993,
    # LocationName.hub_on_rock: 0x130003,
    # LocationName.hub_west_pyramid: 0x130004,
    LocationName.hub_rocks_south: 0x130005,
    LocationName.hub_field_south: 0x130006+154738,
    LocationName.hub_field_nw: 0x130007+154737,
    LocationName.hub_field_north: 0x130008+154850,

    # LocationName.hub_pof_reward: 0x130009
}

temple_shop_locations: typing.Dict[str, int] = {

}

temple_locations: typing.Dict[str, int] = {
    **temple_pickup_locations
}

common_locations: typing.Dict[str, int] = {
    LocationName.victory: None,
}

all_locations: typing.Dict[str, int] = {
    **castle_pickup_locations,
    **castle_shop_locations,
    **temple_pickup_locations,
    **temple_shop_locations,
    **common_locations
}

location_table: typing.Dict[str, int] = {

}


def setup_locations(world, player: int):
    location_table: typing.Dict[str, int]

    if world.map[player] == 0:
        location_table = {**castle_locations}
    else:
        location_table = {**temple_locations}

    if False:#world.include_shops[player].value
        location_table.update({**temple_shop_locations})

    location_table.update(common_locations)

    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
