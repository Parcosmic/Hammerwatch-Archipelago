import typing

from BaseClasses import Item, ItemClassification, MultiWorld
from .Names import ItemName
from .Util import Counter, Campaign
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
    ItemName.key_teleport: ItemData(counter.count(), ItemClassification.progression),
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

trap_table: typing.Dict[str, ItemData] = {
    ItemName.trap_bomb: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_mana: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_poison: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_frost: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_fire: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_confuse: ItemData(counter.count(), ItemClassification.trap),
}

event_table: typing.Dict[str, ItemData] = {
    ItemName.ev_victory: ItemData(None, ItemClassification.progression),
    ItemName.ev_castle_p2_switch: ItemData(None, ItemClassification.progression),
    ItemName.ev_pof_switch: ItemData(None, ItemClassification.progression),
    ItemName.ev_pof_complete: ItemData(None, ItemClassification.progression),
    ItemName.ev_open_temple_entrance_shortcut: ItemData(None, ItemClassification.progression),
}

item_table: typing.Dict[str, ItemData] = {
    **collectable_table,
    **recovery_table,
    **tool_table,
    **special_table,
    **trap_table
}

stat_upgrade_items: typing.List[str] = [
    ItemName.stat_upgrade_damage,
    ItemName.stat_upgrade_defense,
    ItemName.stat_upgrade_health,
    ItemName.stat_upgrade_mana,
]

junk_items: typing.List[str] = [
    ItemName.apple,
    ItemName.mana_1,
    ItemName.diamond_small
]

trap_items: typing.List[str] = [
    ItemName.trap_bomb,
    ItemName.trap_mana,
    ItemName.trap_poison,
    ItemName.trap_frost,
    ItemName.trap_fire,
    ItemName.trap_confuse,
]

castle_item_counts: typing.Dict[str, int] = {
    ItemName.bonus_chest: 0,
    ItemName.bonus_key: 0,
    ItemName.chest_blue: 0,
    ItemName.chest_green: 0,
    ItemName.chest_purple: 1,
    ItemName.chest_red: 0,
    ItemName.chest_wood: 7,
    ItemName.vendor_coin: 10,
    ItemName.plank: 2,
    ItemName.key_bronze: 9,
    ItemName.key_silver: 1,
    ItemName.key_gold: 3,
    ItemName.ankh: 6,
    ItemName.ankh_5up: 0,
    ItemName.potion_damage: 0,
    ItemName.potion_rejuvenation: 3,
    ItemName.potion_invulnerability: 0,
    ItemName.stat_upgrade_damage: 0,
    ItemName.stat_upgrade_defense: 0,
    ItemName.stat_upgrade_health: 0,
    ItemName.stat_upgrade_mana: 0,
    ItemName.apple: 35,
    ItemName.orange: 4,
    ItemName.steak: 0,
    ItemName.fish: 0,
    ItemName.mana_1: 47,
    ItemName.mana_2: 1,
    ItemName.diamond: 0,
    ItemName.diamond_red: 0,
    ItemName.diamond_small: 0,
    ItemName.diamond_small_red: 0,
    ItemName.stat_upgrade: 1,
    ItemName.secret: 0,
    ItemName.puzzle: 1
}

temple_item_counts: typing.Dict[str, int] = {
    ItemName.bonus_chest: 75,
    ItemName.bonus_key: 2,
    ItemName.chest_blue: 10,
    ItemName.chest_green: 5,
    ItemName.chest_purple: 13,
    ItemName.chest_red: 11,
    ItemName.chest_wood: 29,
    ItemName.vendor_coin: 43,
    ItemName.plank: 0,
    ItemName.key_silver: 6,
    ItemName.key_gold: 4,
    ItemName.mirror: 20,
    ItemName.ore: 11,
    ItemName.key_teleport: 6,
    ItemName.ankh: 31,
    ItemName.ankh_5up: 4,
    ItemName.potion_rejuvenation: 13,
    ItemName.sonic_ring: 12,
    ItemName.serious_health: 1,
    ItemName.diamond: 0,
    ItemName.diamond_red: 0,
    ItemName.diamond_small: 3,
    ItemName.diamond_small_red: 0,
    ItemName.stat_upgrade_damage: 1,
    ItemName.stat_upgrade_defense: 1,
    ItemName.stat_upgrade_health: 0,
    ItemName.stat_upgrade_mana: 0,
    ItemName.apple: 48,
    ItemName.orange: 11,
    ItemName.steak: 7,
    ItemName.fish: 7,
    ItemName.mana_1: 24,
    ItemName.mana_2: 4,
    ItemName.pan: 1,
    ItemName.lever: 1,
    ItemName.pickaxe: 1,
    ItemName.stat_upgrade: 43,
    ItemName.secret: 20,
    ItemName.puzzle: 10
}


def get_item_counts(multiworld: MultiWorld, campaign: Campaign, player: int):
    item_counts_table: typing.Dict[str, int]
    extra_items: int = 0

    if campaign == Campaign.Castle:  # Castle Hammerwatch
        item_counts_table = {**castle_item_counts}
    elif campaign == Campaign.Temple:  # Temple of the Sun
        item_counts_table = {**temple_item_counts}

    secrets: int = item_counts_table.pop(ItemName.secret)
    puzzles: int = item_counts_table.pop(ItemName.puzzle)

    # Strange planks
    if multiworld.goal[player].value % 10 == 1 or multiworld.goal[player].value % 10 == 2:
        minimum_planks = 12
        if multiworld.goal[player].value % 10 == 1:  # Plank hunt
            minimum_planks = multiworld.planks_required_count[player].value
        planks_needed = max(multiworld.plank_count[player].value, minimum_planks)
        extra_items = planks_needed - item_counts_table[ItemName.plank]
        item_counts_table[ItemName.plank] = planks_needed
    else:  # Remove planks from the pool, they're not needed
        extra_items -= item_counts_table[ItemName.plank]
        item_counts_table.pop(ItemName.plank)

    # Bonus check behavior - None
    if multiworld.bonus_behavior[player].value == 0 or multiworld.bonus_behavior[player].value == 1:
        item_counts_table.pop(ItemName.bonus_chest)

    if campaign == Campaign.Temple:
        # If using fragments switch the whole item out for fragments
        if multiworld.pan_fragments[player].value > 1:
            item_counts_table.pop(ItemName.pan)
            item_counts_table.update({ItemName.pan_fragment: multiworld.pan_fragments[player].value})
            extra_items += multiworld.pan_fragments[player].value - 1
        if multiworld.lever_fragments[player].value > 1:
            item_counts_table.pop(ItemName.lever)
            item_counts_table.update({ItemName.lever_fragment: multiworld.lever_fragments[player].value})
            extra_items += multiworld.lever_fragments[player].value - 1
        if multiworld.pickaxe_fragments[player].value > 1:
            item_counts_table.pop(ItemName.pickaxe)
            item_counts_table.update({ItemName.pickaxe_fragment: multiworld.pickaxe_fragments[player].value})
            extra_items += multiworld.pickaxe_fragments[player].value - 1

        # If Portal Accessibility is on then remove Rune Keys from the pool, they're placed elsewhere
        if multiworld.portal_accessibility[player].value > 0:
            item_counts_table.pop(ItemName.key_teleport)

        # Add secret items from TotS
        if multiworld.randomize_secrets[player].value:
            for s in range(secrets):
                item = multiworld.random.randint(0, 12)
                if item < 8:
                    item_counts_table[ItemName.chest_wood] += 1
                elif item < 12:
                    item_counts_table[ItemName.ankh] += 1
                else:
                    item_counts_table[ItemName.stat_upgrade] += 1

    # If the player has selected not to randomize recovery items, set all their counts to zero
    if not multiworld.randomize_recovery_items[player].value:
        for recovery in recovery_table.keys():
            item_counts_table[recovery] = 0

    # Add puzzle items
    # if multiworld.randomize_puzzles[player].value:
    # item_counts_table[ItemName.chest_purple] += puzzles
    # item_counts_table[ItemName.stat_upgrade] += puzzles
    # item_counts_table[ItemName.ankh] += puzzles
    # item_counts_table[ItemName.potion_rejuvenation] += puzzles

    # Determine stat upgrades and add them to the pool
    stat_upgrades: int = item_counts_table.pop(ItemName.stat_upgrade)
    for u in range(stat_upgrades):
        upgrade = multiworld.random.randrange(4)
        item_counts_table[stat_upgrade_items[upgrade]] += 1

    # Build filler items list
    filler_item_names: typing.List[str] = []
    filler_items: int = 0
    for item in item_counts_table.keys():
        if item_table[item].classification == ItemClassification.filler and item_counts_table[item] > 0:
            filler_item_names.append(item)
            filler_items += item_counts_table[item]

    # Trap items
    if multiworld.trap_item_percent[player].value > 0:
        for trap_item in trap_items:
            item_counts_table[trap_item] = 0
        trap_item_count = int((filler_items - extra_items) * multiworld.trap_item_percent[player].value / 100)
        extra_items += trap_item_count
        for t in range(trap_item_count):
            item = trap_items[multiworld.random.randrange(len(trap_items))]
            item_counts_table[item] += 1

    # For each extra item remove a filler item, or add extra items if we need more
    for t in range(extra_items):
        filler_item = filler_item_names[multiworld.random.randrange(len(filler_item_names))]
        if extra_items > 1:
            item_counts_table[filler_item] -= 1
            if item_counts_table[filler_item] == 0:
                filler_item_names.remove(filler_item)
        else:
            item_counts_table[filler_item] += 1

    return item_counts_table


filler_items: typing.List[str] = [item_name for item_name, data in item_table.items() if data.classification.filler]
lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
