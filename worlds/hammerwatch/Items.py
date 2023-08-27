from BaseClasses import Item, ItemClassification, MultiWorld
from . import Options
from .Names import ItemName
from .Options import BonusChestLocationBehavior
from .Util import *


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification


class HammerwatchItem(Item):
    game: str = "Hammerwatch"


id_start = 0x110000

counter = Counter(id_start - 1)
collectable_table: typing.Dict[str, ItemData] = {
    ItemName.bonus_chest: ItemData(counter.count(), ItemClassification.filler),
    ItemName.key_bonus: ItemData(counter.count(), ItemClassification.progression),
    ItemName.chest_blue: ItemData(counter.count(), ItemClassification.filler),
    ItemName.chest_green: ItemData(counter.count(), ItemClassification.filler),
    ItemName.chest_purple: ItemData(counter.count(), ItemClassification.useful),
    ItemName.chest_red: ItemData(counter.count(), ItemClassification.filler),
    ItemName.chest_wood: ItemData(counter.count(), ItemClassification.filler),
    ItemName.vendor_coin: ItemData(counter.count(), ItemClassification.filler),
    ItemName.plank: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
    ItemName.key_silver: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_gold: ItemData(counter.count(), ItemClassification.progression),
    ItemName.mirror: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
    ItemName.ore: ItemData(counter.count(), ItemClassification.useful),
    ItemName.key_teleport: ItemData(counter.count(), ItemClassification.useful),
    ItemName.ankh: ItemData(counter.count(), ItemClassification.filler),
    ItemName.ankh_5up: ItemData(counter.count(), ItemClassification.filler),
    ItemName.ankh_7up: ItemData(counter.count(), ItemClassification.filler),
    ItemName.potion_damage: ItemData(counter.count(), ItemClassification.filler),
    ItemName.potion_rejuvenation: ItemData(counter.count(), ItemClassification.filler),
    ItemName.potion_invulnerability: ItemData(counter.count(), ItemClassification.filler),
    ItemName.diamond: ItemData(counter.count(), ItemClassification.filler),
    ItemName.diamond_red: ItemData(counter.count(), ItemClassification.filler),
    ItemName.diamond_small: ItemData(counter.count(), ItemClassification.filler),
    ItemName.diamond_small_red: ItemData(counter.count(), ItemClassification.filler),
    ItemName.stat_upgrade: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_damage: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_defense: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_health: ItemData(counter.count(), ItemClassification.useful),
    ItemName.stat_upgrade_mana: ItemData(counter.count(), ItemClassification.useful),
    ItemName.valuable_1: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_2: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_3: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_4: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_5: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_6: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_7: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_8: ItemData(counter.count(), ItemClassification.filler),
    ItemName.valuable_9: ItemData(counter.count(), ItemClassification.filler),
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

counter = Counter(id_start + 0x100 - 1)
trap_table: typing.Dict[str, ItemData] = {
    ItemName.trap_bomb: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_mana: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_poison: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_frost: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_fire: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_confuse: ItemData(counter.count(), ItemClassification.trap),
    ItemName.trap_banner: ItemData(counter.count(), ItemClassification.trap),
}

counter = Counter(id_start + 0x200 - 1)
custom_table: typing.Dict[str, ItemData] = {
    ItemName.key_bronze_big: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_prison: ItemData(counter.count(4), ItemClassification.progression),
    ItemName.key_silver_prison: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_gold_prison: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bonus_prison: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_armory: ItemData(counter.count(4), ItemClassification.progression),
    ItemName.key_silver_armory: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_gold_armory: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bonus_armory: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_archives: ItemData(counter.count(4), ItemClassification.progression),
    ItemName.key_silver_archives: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_gold_archives: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bonus_archives: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_chambers: ItemData(counter.count(4), ItemClassification.progression),
    ItemName.key_silver_chambers: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_gold_chambers: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bonus_chambers: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_big_prison: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_big_armory: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_big_archives: ItemData(counter.count(), ItemClassification.progression),
    ItemName.key_bronze_big_chambers: ItemData(counter.count(), ItemClassification.progression),
}

item_table: typing.Dict[str, ItemData] = {
    **collectable_table,
    **recovery_table,
    **tool_table,
    **special_table,
    **custom_table,
    **trap_table
}

stat_upgrade_items: typing.List[str] = [
    ItemName.stat_upgrade_damage,
    ItemName.stat_upgrade_defense,
    ItemName.stat_upgrade_health,
    ItemName.stat_upgrade_mana,
]

trap_items: typing.List[str] = [
    ItemName.trap_bomb,
    ItemName.trap_mana,
    ItemName.trap_poison,
    ItemName.trap_frost,
    ItemName.trap_fire,
    ItemName.trap_confuse,
    ItemName.trap_banner,
]

big_key_amount = 3
key_table: typing.Dict[str, typing.Tuple[str, int]] = {
    # ItemName.key_bronze: (ItemName.key_bronze, 1),
    # ItemName.key_silver: (ItemName.key_silver, 1),
    # ItemName.key_gold: (ItemName.key_gold, 1),
    # ItemName.key_bonus: (ItemName.key_bonus, 1),

    ItemName.key_bronze_big: (ItemName.key_bronze, 3),

    ItemName.key_bronze_big_prison: (ItemName.key_bronze_prison, 3),
    ItemName.key_bronze_big_armory: (ItemName.key_bronze_armory, 3),
    ItemName.key_bronze_big_archives: (ItemName.key_bronze_archives, 3),
    ItemName.key_bronze_big_chambers: (ItemName.key_bronze_chambers, 3),

    ItemName.key_bronze_prison: (ItemName.key_bronze, 1),
    ItemName.key_bronze_armory: (ItemName.key_bronze, 1),
    ItemName.key_bronze_archives: (ItemName.key_bronze, 1),
    ItemName.key_bronze_chambers: (ItemName.key_bronze, 1),

    ItemName.key_silver_prison: (ItemName.key_silver, 1),
    ItemName.key_silver_armory: (ItemName.key_silver, 1),
    ItemName.key_silver_archives: (ItemName.key_silver, 1),
    ItemName.key_silver_chambers: (ItemName.key_silver, 1),

    ItemName.key_gold_prison: (ItemName.key_gold, 1),
    ItemName.key_gold_armory: (ItemName.key_gold, 1),
    ItemName.key_gold_archives: (ItemName.key_gold, 1),
    ItemName.key_gold_chambers: (ItemName.key_gold, 1),

    ItemName.key_bonus_prison: (ItemName.key_bonus, 1),
    ItemName.key_bonus_armory: (ItemName.key_bonus, 1),
    ItemName.key_bonus_archives: (ItemName.key_bonus, 1),
    ItemName.key_bonus_chambers: (ItemName.key_bonus, 1),

    # ItemName.key_teleport: (ItemName.key_teleport, 1),
}

castle_item_counts: typing.Dict[str, int] = {
    ItemName.bonus_chest: 227,
    ItemName.key_bonus: 18,
    ItemName.chest_blue: 15,
    ItemName.chest_green: 18,
    ItemName.chest_purple: 7,
    ItemName.chest_red: 14,
    ItemName.chest_wood: 25,
    ItemName.vendor_coin: 80,
    ItemName.plank: 12,
    ItemName.key_bronze: 103,
    ItemName.key_silver: 13,
    ItemName.key_gold: 16,
    ItemName.ankh: 38,
    ItemName.ankh_5up: 6,
    ItemName.potion_damage: 0,
    ItemName.potion_rejuvenation: 17,
    ItemName.potion_invulnerability: 0,
    ItemName.diamond: 5,
    ItemName.diamond_red: 12,
    ItemName.diamond_small: 14,
    ItemName.diamond_small_red: 18,
    ItemName.stat_upgrade_damage: 1,
    ItemName.stat_upgrade_defense: 0,
    ItemName.stat_upgrade_health: 0,
    ItemName.stat_upgrade_mana: 0,
    ItemName.apple: 177,
    ItemName.orange: 40,
    ItemName.steak: 9,
    ItemName.mana_1: 196,
    ItemName.mana_2: 30,
    ItemName.stat_upgrade: 14,
    ItemName.secret: 0,  # Future me please don't remove this it'll break item gen code
    # ItemName.puzzle: 7,
    ItemName.miniboss_stat_upgrade: 17,
    ItemName.loot_tower: 45,
    ItemName.loot_flower: 43,
    ItemName.key_bronze_prison: 12,
    ItemName.key_silver_prison: 2,
    ItemName.key_gold_prison: 4,
    ItemName.key_bonus_prison: 5,
    ItemName.key_bronze_armory: 29,
    ItemName.key_silver_armory: 3,
    ItemName.key_gold_armory: 2,
    ItemName.key_bonus_armory: 6,
    ItemName.key_bronze_archives: 20,
    ItemName.key_silver_archives: 5,
    ItemName.key_gold_archives: 7,
    ItemName.key_bonus_archives: 3,
    ItemName.key_bronze_chambers: 42,
    ItemName.key_silver_chambers: 3,
    ItemName.key_gold_chambers: 3,
    ItemName.key_bonus_chambers: 4,
}

temple_item_counts: typing.Dict[str, int] = {
    ItemName.bonus_chest: 75,
    ItemName.key_bonus: 2,
    ItemName.chest_blue: 10,
    ItemName.chest_green: 5,
    ItemName.chest_purple: 13,
    ItemName.chest_red: 11,
    ItemName.chest_wood: 29,
    ItemName.vendor_coin: 50,
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
    ItemName.valuable_6: 0,
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
    # ItemName.puzzle: 10
    ItemName.miniboss_stat_upgrade: 10,
    ItemName.loot_tower: 19,
    ItemName.loot_flower: 8,
    ItemName.loot_mini_flower: 51,
}


def get_item_counts(multiworld: MultiWorld, campaign: Campaign, player: int, item_counts_table: typing.Dict[str, int]):
    extra_items: int = 0

    secrets: int = item_counts_table.pop(ItemName.secret)

    # Remove bonus keys from the item counts as they are placed elsewhere
    if multiworld.randomize_bonus_keys[player] == 0:
        item_counts_table.pop(ItemName.key_bonus)

    # Strange planks
    if get_goal_type(multiworld, player) == GoalType.PlankHunt \
            or get_goal_type(multiworld, player) == GoalType.FullCompletion:
        planks_to_win = 12
        if get_goal_type(multiworld, player) == GoalType.PlankHunt:  # Plank hunt
            planks_to_win = multiworld.planks_required_count[player]
        total_planks = planks_to_win + int(planks_to_win * multiworld.extra_plank_percent[player] / 100)
        extra_items = total_planks - item_counts_table[ItemName.plank]
        item_counts_table[ItemName.plank] = total_planks
    else:  # Remove planks from the pool, they're not needed
        extra_items -= item_counts_table.pop(ItemName.plank)

    # Extra keys
    all_key_names = {
        ItemName.key_bronze,
        ItemName.key_silver,
        ItemName.key_gold,
        ItemName.key_bonus,
        ItemName.mirror,
        ItemName.key_bronze_prison,
        ItemName.key_bronze_armory,
        ItemName.key_bronze_archives,
        ItemName.key_bronze_chambers,
        ItemName.key_silver_prison,
        ItemName.key_silver_armory,
        ItemName.key_silver_archives,
        ItemName.key_silver_chambers,
        ItemName.key_gold_prison,
        ItemName.key_gold_armory,
        ItemName.key_gold_archives,
        ItemName.key_gold_chambers,
        ItemName.key_bonus_prison,
        ItemName.key_bonus_armory,
        ItemName.key_bonus_archives,
        ItemName.key_bonus_chambers,
    }
    active_keys = get_active_key_names(multiworld, player)
    for key in all_key_names:
        if key in item_counts_table.keys() and key not in active_keys:
            item_counts_table.pop(key)
    # Get the active keys, and don't add bronze keys or bonus keys those don't get extra for now
    key_names = set()
    for key_name in active_keys:
        if "Bronze" not in key_name and "Bonus" not in key_name:
            key_names.add(key_name)
    for key in key_names:
        extra_keys = int(item_counts_table[key] * multiworld.extra_keys_percent[player] / 100)
        item_counts_table[key] += extra_keys
        extra_items += extra_keys
    if get_campaign(multiworld, player) == Campaign.Temple:
        extra_mirrors = int(item_counts_table[ItemName.mirror] * multiworld.extra_keys_percent[player] / 100)
        item_counts_table[ItemName.mirror] += extra_mirrors
        extra_items += extra_mirrors

    # Bonus check behavior - None
    if multiworld.bonus_behavior[player] == BonusChestLocationBehavior.option_none:
        item_counts_table[ItemName.bonus_chest] = 0

    # Consolidate bronze keys
    if campaign == Campaign.Castle and multiworld.big_bronze_key_percent[player] > 0:
        bronze_key_names = [key for key in get_active_key_names(multiworld, player) if "Bronze" in key]
        for bronze_key in bronze_key_names:
            big_name = "Big " + bronze_key
            big_keys = int(item_counts_table[bronze_key] * multiworld.big_bronze_key_percent[player] / 100
                           / key_table[big_name][1])
            if big_keys > 0:
                item_counts_table[big_name] = big_keys
                item_counts_table[bronze_key] -= big_keys * key_table[big_name][1]
                extra_items -= big_keys * key_table[big_name][1] - big_keys

    if campaign == Campaign.Temple:
        # If using fragments switch the whole item out for fragments
        if multiworld.pan_fragments[player] > 1:
            item_counts_table.pop(ItemName.pan)
            item_counts_table.update({ItemName.pan_fragment: multiworld.pan_fragments[player]})
            extra_items += multiworld.pan_fragments[player] - 1
        if multiworld.lever_fragments[player] > 1:
            item_counts_table.pop(ItemName.lever)
            item_counts_table.update({ItemName.lever_fragment: multiworld.lever_fragments[player]})
            extra_items += multiworld.lever_fragments[player] - 1
        if multiworld.pickaxe_fragments[player] > 1:
            item_counts_table.pop(ItemName.pickaxe)
            item_counts_table.update({ItemName.pickaxe_fragment: multiworld.pickaxe_fragments[player]})
            extra_items += multiworld.pickaxe_fragments[player] - 1

        # If Portal Accessibility is on then remove Rune Keys from the pool, they're placed elsewhere
        if multiworld.portal_accessibility[player]:
            item_counts_table.pop(ItemName.key_teleport)

        # Add secret items from TotS
        if multiworld.randomize_secrets[player]:
            for s in range(secrets):
                item = multiworld.random.randint(0, 12)
                if item < 8:
                    item_counts_table[ItemName.chest_wood] += 1
                elif item < 12:
                    item_counts_table[ItemName.ankh] += 1
                else:
                    item_counts_table[ItemName.stat_upgrade] += 1

    # Remove extra lives if the option was selected
    if multiworld.remove_lives[player]:
        extra_items -= item_counts_table.pop(ItemName.ankh)
        extra_items -= item_counts_table.pop(ItemName.ankh_5up)
        extra_items -= item_counts_table.pop(ItemName.ankh_7up)  # No maps have 7-ups in them, but here for future stuff

    # If the player has selected not to randomize recovery items, set all their counts to zero
    if not multiworld.randomize_recovery_items[player]:
        for recovery in recovery_table.keys():
            item_counts_table[recovery] = 0

    # Enemy loot
    if multiworld.randomize_enemy_loot[player]:
        miniboss_stat_upgrade_chances = [
            (0.3, ItemName.stat_upgrade_health),
            (0.3, ItemName.stat_upgrade_mana),
            (0.3, ItemName.stat_upgrade_damage),
            (0.1, ItemName.stat_upgrade_defense),
        ]
        miniboss_upgrades = item_counts_table.pop(ItemName.miniboss_stat_upgrade)
        for i in range(miniboss_upgrades):
            item = roll_for_item(multiworld, miniboss_stat_upgrade_chances)
            item_counts_table[item] += 1

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
    if multiworld.trap_item_percent[player] > 0:
        for trap_item in trap_items:
            item_counts_table[trap_item] = 0
        trap_item_count = int((filler_items - extra_items) * multiworld.trap_item_percent[player] / 100)
        extra_items += trap_item_count
        for t in range(trap_item_count):
            item = trap_items[multiworld.random.randrange(len(trap_items))]
            item_counts_table[item] += 1

    # For Necessary we set the number of bonus chests equal to each extra item
    if multiworld.bonus_behavior[player] == BonusChestLocationBehavior.option_necessary:
        item_counts_table[ItemName.bonus_chest] = max(extra_items, 0)

    return item_counts_table, extra_items


def roll_for_item(multiworld, loot_chances: typing.List[typing.Tuple[float, str]]):
    rnd = multiworld.random.random()
    for item in loot_chances:
        rnd -= item[0]
        if rnd < 0:
            return item[1]
    return None


filler_items: typing.List[str] = [item_name for item_name, data in item_table.items() if data.classification.filler]
lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
