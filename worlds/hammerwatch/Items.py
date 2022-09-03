import typing

from BaseClasses import Item
from .Names import ItemName


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    event: bool = False


class HammerwatchItem(Item):
    game: str = "Hammerwatch"


collectible_table: typing.Dict[str, ItemData] = {
    ItemName.bonus_chest: ItemData(0x130001, False),
    ItemName.bonus_key: ItemData(0x130002, False),
    ItemName.chest_blue: ItemData(0x130003, False),
    ItemName.chest_green: ItemData(0x130004, False),
    ItemName.chest_red: ItemData(0x130005, False),
    ItemName.chest_wood: ItemData(0x130006, False),
    ItemName.vendor_coin: ItemData(0x130007, False),
    ItemName.plank: ItemData(0x130008, True),
    ItemName.key_bronze: ItemData(0x130009, True),
    ItemName.key_silver: ItemData(0x130010, True),
    ItemName.key_gold: ItemData(0x130011, True),
    ItemName.mirror: ItemData(0x130012, True),
    ItemName.ore: ItemData(0x130013, False),
    ItemName.key_teleport: ItemData(0x130014, False),
    ItemName.ankh: ItemData(0x130015, False),
    ItemName.ankh_5up: ItemData(0x130016, False),
    ItemName.potion_damage: ItemData(0x130017, False),
    ItemName.potion_rejuvenation: ItemData(0x130018, False),
    ItemName.potion_invulnerability: ItemData(0x130019, False),
    ItemName.stat_upgrade_damage: ItemData(0x130020, False),
    ItemName.pickaxe: ItemData(0x130021, True),
    ItemName.diamond: ItemData(0x130022, False),
    ItemName.diamond_red: ItemData(0x130023, False),
    ItemName.diamond_small: ItemData(0x130024, False),
    ItemName.diamond_small_red: ItemData(0x130025, False),
    ItemName.stat_upgrade: ItemData(0x130026, False)
}

special_table: typing.Dict[str, ItemData] = {
    ItemName.sonic_ring: ItemData(0x130027, False),
    ItemName.serious_health: ItemData(0x130028, False)
}

event_table: typing.Dict[str, ItemData] = {
    ItemName.victory: ItemData(None, True)
}

item_table: typing.Dict[str, ItemData] = {
    **collectible_table,
    **special_table,
    **event_table
}

junk_table: typing.Dict[str, ItemData] = {
    ItemName.ankh: item_table[ItemName.ankh],
    ItemName.diamond_small: item_table[ItemName.diamond_small],
}

castle_item_counts: typing.Dict[str, int] = {
    ItemName.bonus_chest: 227,
    ItemName.bonus_key: 18,
    ItemName.chest_blue: 17,
    ItemName.chest_green: 18,
    ItemName.chest_red: 14,
    ItemName.chest_wood: 21,
    ItemName.vendor_coin: 61,
    ItemName.plank: 13,
    ItemName.key_bronze: 94,
    ItemName.key_silver: 15,
    ItemName.key_gold: 11,
    ItemName.mirror: 0,
    ItemName.ore: 0,
    ItemName.key_teleport: 0,
    ItemName.ankh: 32,
    ItemName.ankh_5up: 6,
    ItemName.potion_damage: 0,
    ItemName.potion_rejuvenation: 9,
    ItemName.potion_invulnerability: 0,
    ItemName.stat_upgrade_damage: 2,
    ItemName.sonic_ring: 0,
    ItemName.serious_health: 0,
    ItemName.pickaxe: 0,
    ItemName.diamond: 4,
    ItemName.diamond_red: 1,
    ItemName.diamond_small: 10,
    ItemName.diamond_small_red: 18,
    ItemName.stat_upgrade: -1
}

temple_item_counts: typing.Dict[str, int] = {
    ItemName.bonus_chest: 0,
    ItemName.bonus_key: 0,
    ItemName.chest_blue: 0,
    ItemName.chest_green: 0,
    ItemName.chest_red: 0,
    ItemName.chest_wood: 0,
    ItemName.vendor_coin: 2,
    ItemName.plank: 0,
    ItemName.key_bronze: 0,
    ItemName.key_silver: 0,
    ItemName.key_gold: 0,
    ItemName.mirror: 0,
    ItemName.ore: 0,
    ItemName.key_teleport: 0,
    ItemName.ankh: 0,
    ItemName.ankh_5up: 0,
    ItemName.potion_damage: 0,
    ItemName.potion_rejuvenation: 1,
    ItemName.potion_invulnerability: 0,
    ItemName.stat_upgrade_damage: 0,
    ItemName.sonic_ring: 0,
    ItemName.serious_health: 0,
    ItemName.pickaxe: 1,
    ItemName.diamond: 0,
    ItemName.diamond_red: 0,
    ItemName.diamond_small: 0,
    ItemName.diamond_small_red: 0,
    ItemName.stat_upgrade: 0
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
