import typing

from BaseClasses import Item, ItemClassification
from .Names import ItemName
from .Util import Counter
from random import Random


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification


class HammerwatchItem(Item):
    game: str = "Hammerwatch"


counter = Counter(0x130000 - 1)
collectable_table: typing.Dict[str, ItemData] = {
    ItemName.bonus_chest: ItemData(counter.count(), ItemClassification.filler),
    ItemName.bonus_key: ItemData(counter.count(), ItemClassification.progression),
    ItemName.chest_blue: ItemData(counter.count(), ItemClassification.filler),
    ItemName.chest_green: ItemData(counter.count(), ItemClassification.filler),
    ItemName.chest_purple: ItemData(counter.count(), ItemClassification.filler),
    ItemName.chest_red: ItemData(counter.count(), ItemClassification.filler),
    ItemName.chest_wood: ItemData(counter.count(), ItemClassification.filler),
    ItemName.vendor_coin: ItemData(counter.count(), ItemClassification.filler),
    ItemName.plank: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_silver: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_gold: ItemData(counter.count(), ItemClassification.progression),
    ItemName.mirror: ItemData(counter.count(), ItemClassification.progression),
    ItemName.ore: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_teleport: ItemData(counter.count(), ItemClassification.useful),
    ItemName.ankh: ItemData(counter.count(), ItemClassification.filler),
    ItemName.ankh_5up: ItemData(counter.count(), ItemClassification.filler),
    ItemName.ankh_7up: ItemData(counter.count(), ItemClassification.filler),
    ItemName.potion_damage: ItemData(counter.count(), ItemClassification.useful),
    ItemName.potion_rejuvenation: ItemData(counter.count(), ItemClassification.useful),
    ItemName.potion_invulnerability: ItemData(counter.count(), ItemClassification.useful),
    ItemName.diamond: ItemData(counter.count(), ItemClassification.filler),
    ItemName.diamond_red: ItemData(counter.count(), ItemClassification.filler),
    ItemName.diamond_small: ItemData(counter.count(), ItemClassification.filler),
    ItemName.diamond_small_red: ItemData(counter.count(), ItemClassification.filler),
    ItemName.stat_upgrade: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_damage: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_defense: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_health: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_mana: ItemData(counter.count(), ItemClassification.useful),
}

recovery_table: typing.Dict[str, ItemData] = {
    ItemName.apple: ItemData(counter.count(), ItemClassification.filler),
    ItemName.orange: ItemData(counter.count(), ItemClassification.filler),
    ItemName.steak: ItemData(counter.count(), ItemClassification.filler),
    ItemName.fish: ItemData(counter.count(), ItemClassification.filler),
    ItemName.mana_1: ItemData(counter.count(), ItemClassification.filler),
    ItemName.mana_2: ItemData(counter.count(), ItemClassification.filler),
}

tool_table: typing.Dict[str, ItemData] = {
    ItemName.pan: ItemData(counter.count(), ItemClassification.progression),
    ItemName.lever: ItemData(counter.count(), ItemClassification.progression),
    ItemName.pickaxe: ItemData(counter.count(), ItemClassification.progression),
    ItemName.pan_fragment: ItemData(counter.count(), ItemClassification.progression),
    ItemName.lever_fragment: ItemData(counter.count(), ItemClassification.progression),
    ItemName.pickaxe_fragment: ItemData(counter.count(), ItemClassification.progression),
}

special_table: typing.Dict[str, ItemData] = {
    ItemName.sonic_ring: ItemData(counter.count(), ItemClassification.filler),
    ItemName.serious_health: ItemData(counter.count(), ItemClassification.filler)
}

event_table: typing.Dict[str, ItemData] = {
    ItemName.victory: ItemData(None, ItemClassification.progression),
    ItemName.pof_switch: ItemData(None, ItemClassification.progression),
    ItemName.pof_complete: ItemData(None, ItemClassification.progression),
    ItemName.open_temple_entrance_shortcut: ItemData(None, ItemClassification.progression),
}

item_table: typing.Dict[str, ItemData] = {
    **collectable_table,
    **recovery_table,
    **tool_table,
    **special_table,
    # **event_table
}

junk_items: typing.List[str] = [
    ItemName.apple,
    ItemName.mana_1,
    ItemName.diamond_small
]

trap_items: typing.List[str] = [

]

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
    ItemName.stat_upgrade: 0,
    ItemName.secret: 20,
    ItemName.puzzle: 0
}

temple_item_counts: typing.Dict[str, int] = {
    ItemName.bonus_chest: 0,  # 75
    ItemName.bonus_key: 0,  # 2
    ItemName.chest_blue: 8,
    ItemName.chest_green: 4,
    ItemName.chest_purple: 0,
    ItemName.chest_red: 10,
    ItemName.chest_wood: 26,
    ItemName.vendor_coin: 32,
    ItemName.key_silver: 6,
    ItemName.key_gold: 4,
    ItemName.mirror: 15,
    ItemName.ore: 11,
    ItemName.key_teleport: 5,
    ItemName.ankh: 18,
    ItemName.ankh_5up: 3,
    ItemName.ankh_7up: 0,
    ItemName.potion_damage: 0,
    ItemName.potion_rejuvenation: 0,
    ItemName.potion_invulnerability: 0,
    ItemName.sonic_ring: 12,
    ItemName.serious_health: 1,
    ItemName.diamond: 0,
    ItemName.diamond_red: 0,
    ItemName.diamond_small: 3,
    ItemName.diamond_small_red: 0,
    ItemName.stat_upgrade: 23,
    ItemName.stat_upgrade_damage: 1,
    ItemName.stat_upgrade_defense: 1,
    ItemName.apple: 48,
    ItemName.orange: 11,
    ItemName.steak: 7,
    ItemName.fish: 7,
    ItemName.mana_1: 24,
    ItemName.mana_2: 4,
    ItemName.pan: 1,
    ItemName.lever: 1,
    ItemName.pickaxe: 1,
    ItemName.secret: 20,
    ItemName.puzzle: 0
}


def get_item_counts(world, player: int):
    item_counts_table: typing.Dict[str, int]
    secrets: int

    if world.map[player] == 0:  # Castle Hammerwatch
        item_counts_table = {**castle_item_counts}
    else:  # Temple of the Sun
        item_counts_table = {**temple_item_counts}

    secrets = item_counts_table[ItemName.secret]

    # If using fragments switch the whole item out for fragments
    if world.pan_fragments[player] > 0:
        item_counts_table.pop(ItemName.pan)
        item_counts_table.update({ItemName.pan_fragment: world.pan_fragments[player]})
    if world.lever_fragments[player] > 0:
        item_counts_table.pop(ItemName.lever)
        item_counts_table.update({ItemName.lever_fragment: world.lever_fragments[player]})
    if world.pickaxe_fragments[player] > 0:
        item_counts_table.pop(ItemName.pickaxe)
        item_counts_table.update({ItemName.pickaxe_fragment: world.pickaxe_fragments[player]})

    # If the player has selected not to randomize recovery items, set all their counts to zero
    if not world.randomize_recovery_items[player].value:
        for recovery in recovery_table.keys():
            item_counts_table[recovery] = 0

    # Add secret items
    random = Random()
    random.seed(random, world.seed)
    for s in range(secrets):
        item = random.randint(0, 12)
        if item < 8:
            item_counts_table[ItemName.chest_wood] += 1
        elif item < 12:
            item_counts_table[ItemName.ankh] += 1
        else:
            item_counts_table[ItemName.stat_upgrade] += 1

    return item_counts_table


lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
