import typing
from BaseClasses import Item, ItemClassification
from .names import item_name
from .options import BonusChestLocationBehavior
from .util import Counter, Campaign, GoalType, get_campaign, get_goal_type, get_active_key_names

if typing.TYPE_CHECKING:
    from . import HammerwatchWorld


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification


class HammerwatchItem(Item):
    game: str = "Hammerwatch"


id_start = 0x110000

counter = Counter(id_start - 1)
collectable_table: typing.Dict[str, ItemData] = {
    item_name.bonus_chest: ItemData(counter.count(), ItemClassification.filler),
    item_name.key_bonus: ItemData(counter.count(), ItemClassification.progression),
    item_name.chest_blue: ItemData(counter.count(), ItemClassification.filler),
    item_name.chest_green: ItemData(counter.count(), ItemClassification.filler),
    item_name.chest_purple: ItemData(counter.count(), ItemClassification.useful),
    item_name.chest_red: ItemData(counter.count(), ItemClassification.filler),
    item_name.chest_wood: ItemData(counter.count(), ItemClassification.filler),
    item_name.vendor_coin: ItemData(counter.count(), ItemClassification.filler),
    item_name.plank: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
    item_name.key_silver: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_gold: ItemData(counter.count(), ItemClassification.progression),
    item_name.mirror: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
    item_name.ore: ItemData(counter.count(), ItemClassification.useful),
    item_name.key_teleport: ItemData(counter.count(), ItemClassification.progression),
    item_name.ankh: ItemData(counter.count(), ItemClassification.filler),
    item_name.ankh_5up: ItemData(counter.count(), ItemClassification.filler),
    item_name.ankh_7up: ItemData(counter.count(), ItemClassification.filler),
    item_name.potion_damage: ItemData(counter.count(), ItemClassification.filler),
    item_name.potion_rejuvenation: ItemData(counter.count(), ItemClassification.filler),
    item_name.potion_invulnerability: ItemData(counter.count(), ItemClassification.filler),
    item_name.diamond: ItemData(counter.count(), ItemClassification.filler),
    item_name.diamond_red: ItemData(counter.count(), ItemClassification.filler),
    item_name.diamond_small: ItemData(counter.count(), ItemClassification.filler),
    item_name.diamond_small_red: ItemData(counter.count(), ItemClassification.filler),
    item_name.stat_upgrade: ItemData(counter.count(), ItemClassification.useful),
    item_name.stat_upgrade_damage: ItemData(counter.count(), ItemClassification.useful),
    item_name.stat_upgrade_defense: ItemData(counter.count(), ItemClassification.useful),
    item_name.stat_upgrade_health: ItemData(counter.count(), ItemClassification.useful),
    item_name.stat_upgrade_mana: ItemData(counter.count(), ItemClassification.useful),
    item_name.valuable_1: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_2: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_3: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_4: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_5: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_6: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_7: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_8: ItemData(counter.count(), ItemClassification.filler),
    item_name.valuable_9: ItemData(counter.count(), ItemClassification.filler),
}

recovery_table: typing.Dict[str, ItemData] = {
    item_name.apple: ItemData(counter.count(), ItemClassification.filler),
    item_name.orange: ItemData(counter.count(), ItemClassification.filler),
    item_name.steak: ItemData(counter.count(), ItemClassification.filler),
    item_name.fish: ItemData(counter.count(), ItemClassification.filler),
    item_name.mana_1: ItemData(counter.count(), ItemClassification.filler),
    item_name.mana_2: ItemData(counter.count(), ItemClassification.filler),
}

tool_table: typing.Dict[str, ItemData] = {
    item_name.pan: ItemData(counter.count(), ItemClassification.progression),
    item_name.lever: ItemData(counter.count(), ItemClassification.progression),
    item_name.pickaxe: ItemData(counter.count(), ItemClassification.progression),
    item_name.pan_fragment: ItemData(counter.count(), ItemClassification.progression),
    item_name.lever_fragment: ItemData(counter.count(), ItemClassification.progression),
    item_name.pickaxe_fragment: ItemData(counter.count(), ItemClassification.progression),
}

special_table: typing.Dict[str, ItemData] = {
    item_name.sonic_ring: ItemData(counter.count(), ItemClassification.filler),
    item_name.serious_health: ItemData(counter.count(), ItemClassification.useful)
}

counter = Counter(id_start + 0x100 - 1)
trap_table: typing.Dict[str, ItemData] = {
    item_name.trap_bomb: ItemData(counter.count(), ItemClassification.trap),
    item_name.trap_mana: ItemData(counter.count(), ItemClassification.trap),
    item_name.trap_poison: ItemData(counter.count(), ItemClassification.trap),
    item_name.trap_frost: ItemData(counter.count(), ItemClassification.trap),
    item_name.trap_fire: ItemData(counter.count(), ItemClassification.trap),
    item_name.trap_confuse: ItemData(counter.count(), ItemClassification.trap),
    item_name.trap_banner: ItemData(counter.count(), ItemClassification.trap),
}

counter = Counter(id_start + 0x200 - 1)
custom_table: typing.Dict[str, ItemData] = {
    item_name.key_bronze_big: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_prison: ItemData(counter.count(4), ItemClassification.progression),
    item_name.key_silver_prison: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_gold_prison: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bonus_prison: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_armory: ItemData(counter.count(4), ItemClassification.progression),
    item_name.key_silver_armory: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_gold_armory: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bonus_armory: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_archives: ItemData(counter.count(4), ItemClassification.progression),
    item_name.key_silver_archives: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_gold_archives: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bonus_archives: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_chambers: ItemData(counter.count(4), ItemClassification.progression),
    item_name.key_silver_chambers: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_gold_chambers: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bonus_chambers: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_big_prison: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_big_armory: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_big_archives: ItemData(counter.count(), ItemClassification.progression),
    item_name.key_bronze_big_chambers: ItemData(counter.count(), ItemClassification.progression),
}

counter = Counter(id_start + 0x300 - 1)
castle_button_table: typing.Dict[str, ItemData] = {

}

counter = Counter(id_start + 0x400 - 1)
temple_button_table: typing.Dict[str, ItemData] = {
    item_name.btn_pof: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c3_puzzle: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c2_puzzle: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c1_puzzle_e: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c1_puzzle_w: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_p_puzzle: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_puzzle_w: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_puzzle_e: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_puzzle_w: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_puzzle_e: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_puzzle_n: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_puzzle_s: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t3_puzzle: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_pof_puzzle: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c3_fall_bridge: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c3_e_bridge: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c2_red: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c2_green: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c2_bridges: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c2_s_bridge: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c2_pumps: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c1_blue: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c1_red: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c1_green: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_c1_tunnel: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_b1_bridge: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_jail_n: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_jail_e: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_telarian: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_guard: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_hall: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t1_runway: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_blue: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_light_bridges: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_jones_hall_back: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_jones_hall: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_nw_gate: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_t3_gate_w: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_t3_gate_e: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_boulder_passage: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_ice_gate_w: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_ice_gate_e: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_boulder_room: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_portal: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_jail_e: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_jail_w: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_jail_s: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_s_gate_shortcut: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_s_gate_hall: ItemData(counter.count(), ItemClassification.useful),
    item_name.btn_t2_s_spikes: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t2_portal_gate: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t3_puzzle_room: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t3_fall_1: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t3_fall_2: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t3_fall_3: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t3_pillars: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_t3_gate_s: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_pof_1_walls_s: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_pof_1_exit: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_pof_2_puzzle: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_pof_2_exit: ItemData(counter.count(), ItemClassification.progression),
    item_name.btn_pof_3_start: ItemData(counter.count(), ItemClassification.progression),

    item_name.btn_pof_part: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
    item_name.btn_t2_light_bridges_part: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
    item_name.btn_t2_portal_part: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
    item_name.btn_t3_puzzle_room_part: ItemData(counter.count(), ItemClassification.progression_skip_balancing),
}
# for itm, data in temple_button_table.items():
#     print(f"{itm}:{data.code}")

button_table = {
    **castle_button_table,
    **temple_button_table,
}

item_table: typing.Dict[str, ItemData] = {
    **collectable_table,
    **recovery_table,
    **tool_table,
    **special_table,
    **custom_table,
    **trap_table,
    **button_table,
}

stat_upgrade_items: typing.List[str] = [
    item_name.stat_upgrade_damage,
    item_name.stat_upgrade_defense,
    item_name.stat_upgrade_health,
    item_name.stat_upgrade_mana,
]

trap_items: typing.List[str] = [
    item_name.trap_bomb,
    item_name.trap_mana,
    item_name.trap_poison,
    item_name.trap_frost,
    item_name.trap_fire,
    item_name.trap_confuse,
    item_name.trap_banner,
]

big_key_amount = 3
key_table: typing.Dict[str, typing.Tuple[str, int]] = {
    # item_name.key_bronze: (item_name.key_bronze, 1),
    # item_name.key_silver: (item_name.key_silver, 1),
    # item_name.key_gold: (item_name.key_gold, 1),
    # item_name.key_bonus: (item_name.key_bonus, 1),

    item_name.key_bronze_big: (item_name.key_bronze, 3),

    item_name.key_bronze_big_prison: (item_name.key_bronze_prison, 3),
    item_name.key_bronze_big_armory: (item_name.key_bronze_armory, 3),
    item_name.key_bronze_big_archives: (item_name.key_bronze_archives, 3),
    item_name.key_bronze_big_chambers: (item_name.key_bronze_chambers, 3),

    item_name.key_bronze_prison: (item_name.key_bronze, 1),
    item_name.key_bronze_armory: (item_name.key_bronze, 1),
    item_name.key_bronze_archives: (item_name.key_bronze, 1),
    item_name.key_bronze_chambers: (item_name.key_bronze, 1),

    item_name.key_silver_prison: (item_name.key_silver, 1),
    item_name.key_silver_armory: (item_name.key_silver, 1),
    item_name.key_silver_archives: (item_name.key_silver, 1),
    item_name.key_silver_chambers: (item_name.key_silver, 1),

    item_name.key_gold_prison: (item_name.key_gold, 1),
    item_name.key_gold_armory: (item_name.key_gold, 1),
    item_name.key_gold_archives: (item_name.key_gold, 1),
    item_name.key_gold_chambers: (item_name.key_gold, 1),

    item_name.key_bonus_prison: (item_name.key_bonus, 1),
    item_name.key_bonus_armory: (item_name.key_bonus, 1),
    item_name.key_bonus_archives: (item_name.key_bonus, 1),
    item_name.key_bonus_chambers: (item_name.key_bonus, 1),

    # item_name.key_teleport: (item_name.key_teleport, 1),
}

castle_item_counts: typing.Dict[str, int] = {
    item_name.bonus_chest: 227,
    item_name.key_bonus: 18,
    item_name.chest_blue: 15,
    item_name.chest_green: 18,
    item_name.chest_purple: 7,
    item_name.chest_red: 14,
    item_name.chest_wood: 25,
    item_name.vendor_coin: 80,
    item_name.plank: 12,
    item_name.key_bronze: 103,
    item_name.key_silver: 13,
    item_name.key_gold: 16,
    item_name.ankh: 38,
    item_name.ankh_5up: 6,
    item_name.potion_damage: 0,
    item_name.potion_rejuvenation: 17,
    item_name.potion_invulnerability: 0,
    item_name.diamond: 5,
    item_name.diamond_red: 12,
    item_name.diamond_small: 14,
    item_name.diamond_small_red: 18,
    item_name.stat_upgrade_damage: 1,
    item_name.stat_upgrade_defense: 0,
    item_name.stat_upgrade_health: 0,
    item_name.stat_upgrade_mana: 0,
    item_name.apple: 177,
    item_name.orange: 40,
    item_name.steak: 9,
    item_name.mana_1: 196,
    item_name.mana_2: 30,
    item_name.stat_upgrade: 14,
    item_name.secret: 0,  # Future me please don't remove this it'll break item gen code
    # item_name.puzzle: 7,
    item_name.miniboss_stat_upgrade: 17,
    item_name.loot_tower: 45,
    item_name.loot_flower: 43,
    item_name.key_bronze_prison: 12,
    item_name.key_silver_prison: 2,
    item_name.key_gold_prison: 4,
    item_name.key_bonus_prison: 5,
    item_name.key_bronze_armory: 29,
    item_name.key_silver_armory: 3,
    item_name.key_gold_armory: 2,
    item_name.key_bonus_armory: 6,
    item_name.key_bronze_archives: 20,
    item_name.key_silver_archives: 5,
    item_name.key_gold_archives: 7,
    item_name.key_bonus_archives: 3,
    item_name.key_bronze_chambers: 42,
    item_name.key_silver_chambers: 3,
    item_name.key_gold_chambers: 3,
    item_name.key_bonus_chambers: 4,
}

castle_button_counts: typing.Dict[str, int] = {
}

temple_item_counts: typing.Dict[str, int] = {
    item_name.bonus_chest: 75,
    item_name.key_bonus: 2,
    item_name.chest_blue: 10,
    item_name.chest_green: 5,
    item_name.chest_purple: 13,
    item_name.chest_red: 11,
    item_name.chest_wood: 29,
    item_name.vendor_coin: 53,
    item_name.plank: 0,
    item_name.key_silver: 6,
    item_name.key_gold: 4,
    item_name.mirror: 20,
    item_name.ore: 11,
    item_name.key_teleport: 6,
    item_name.ankh: 31,
    item_name.ankh_5up: 4,
    item_name.potion_rejuvenation: 13,
    item_name.sonic_ring: 12,
    item_name.serious_health: 1,
    item_name.diamond: 0,
    item_name.diamond_red: 0,
    item_name.diamond_small: 3,
    item_name.diamond_small_red: 0,
    item_name.stat_upgrade_damage: 1,
    item_name.stat_upgrade_defense: 1,
    item_name.stat_upgrade_health: 0,
    item_name.stat_upgrade_mana: 0,
    item_name.valuable_6: 0,
    item_name.apple: 48,
    item_name.orange: 11,
    item_name.steak: 7,
    item_name.fish: 7,
    item_name.mana_1: 24,
    item_name.mana_2: 4,
    item_name.pan: 1,
    item_name.lever: 1,
    item_name.pickaxe: 1,
    item_name.stat_upgrade: 43,
    item_name.secret: 20,
    # item_name.puzzle: 10
    item_name.miniboss_stat_upgrade: 10,
    item_name.loot_tower: 19,
    item_name.loot_flower: 8,
    item_name.loot_mini_flower: 51,
}

temple_button_counts: typing.Dict[str, int] = {
    item_name.btn_pof_part: 24,
    item_name.btn_t2_light_bridges_part: 5,
    item_name.btn_t2_portal_part: 2,
    item_name.btn_t3_puzzle_room_part: 4,
}


def get_item_counts(world: "HammerwatchWorld", campaign: Campaign, item_counts_table: typing.Dict[str, int]):
    extra_items: int = 0

    secrets: int = item_counts_table.pop(item_name.secret)

    # Remove bonus keys from the item counts as they are placed elsewhere
    if world.options.randomize_bonus_keys.value == 0:
        item_counts_table.pop(item_name.key_bonus)

    # Strange planks
    goal = get_goal_type(world)
    if goal == GoalType.PlankHunt or goal == GoalType.FullCompletion:
        planks_to_win = 12
        if goal == GoalType.PlankHunt:  # Plank hunt
            planks_to_win = world.options.planks_required_count.value
        total_planks =\
            planks_to_win + int(planks_to_win * world.options.extra_plank_percent.value / 100)
        extra_items = total_planks - item_counts_table[item_name.plank]
        item_counts_table[item_name.plank] = total_planks
    else:  # Remove planks from the pool, they're not needed
        extra_items -= item_counts_table.pop(item_name.plank)

    # Extra keys
    all_key_names = {
        item_name.key_bronze,
        item_name.key_silver,
        item_name.key_gold,
        item_name.key_bonus,
        item_name.mirror,
        item_name.key_bronze_prison,
        item_name.key_bronze_armory,
        item_name.key_bronze_archives,
        item_name.key_bronze_chambers,
        item_name.key_silver_prison,
        item_name.key_silver_armory,
        item_name.key_silver_archives,
        item_name.key_silver_chambers,
        item_name.key_gold_prison,
        item_name.key_gold_armory,
        item_name.key_gold_archives,
        item_name.key_gold_chambers,
        item_name.key_bonus_prison,
        item_name.key_bonus_armory,
        item_name.key_bonus_archives,
        item_name.key_bonus_chambers,
    }
    active_keys = get_active_key_names(world)
    for key in all_key_names:
        if key in item_counts_table.keys() and key not in active_keys:
            item_counts_table.pop(key)
    # Get the active keys, and don't add bronze keys or bonus keys those don't get extra for now
    key_names = set()
    for key_name in active_keys:
        # Exclude bronze keys and rune keys from getting extra items added to the pool
        if "Bronze" not in key_name and "Rune" not in key_name:
            key_names.add(key_name)
    extra_key_percent = world.options.extra_keys_percent.value / 100
    for key in key_names:
        extra_keys = int(item_counts_table[key] * extra_key_percent)
        item_counts_table[key] += extra_keys
        extra_items += extra_keys
    if get_campaign(world) == Campaign.Temple:
        extra_mirrors = int(item_counts_table[item_name.mirror] * extra_key_percent)
        item_counts_table[item_name.mirror] += extra_mirrors
        extra_items += extra_mirrors

    # Bonus check behavior - None
    if world.options.bonus_behavior.value == BonusChestLocationBehavior.option_none:
        item_counts_table[item_name.bonus_chest] = 0

    # Consolidate bronze keys
    big_bronze_key_percent = world.options.big_bronze_key_percent.value / 100
    if campaign == Campaign.Castle and big_bronze_key_percent > 0:
        bronze_key_names = [key for key in get_active_key_names(world) if "Bronze" in key]
        for bronze_key in bronze_key_names:
            big_name = "Big " + bronze_key
            big_keys = int(item_counts_table[bronze_key] * big_bronze_key_percent / key_table[big_name][1])
            if big_keys > 0:
                item_counts_table[big_name] = big_keys
                item_counts_table[bronze_key] -= big_keys * key_table[big_name][1]
                extra_items -= big_keys * key_table[big_name][1] - big_keys

    if campaign == Campaign.Temple:
        # If using fragments switch the whole item out for fragments
        pan_fragments = world.options.pan_fragments.value
        if pan_fragments > 1:
            item_counts_table.pop(item_name.pan)
            item_counts_table.update({item_name.pan_fragment: pan_fragments})
            extra_items += pan_fragments - 1
        lever_fragments = world.options.lever_fragments.value
        if lever_fragments > 1:
            item_counts_table.pop(item_name.lever)
            item_counts_table.update({item_name.lever_fragment: lever_fragments})
            extra_items += lever_fragments - 1
        pickaxe_fragments = world.options.pickaxe_fragments.value
        if pickaxe_fragments > 1:
            item_counts_table.pop(item_name.pickaxe)
            item_counts_table.update({item_name.pickaxe_fragment: pickaxe_fragments})
            extra_items += pickaxe_fragments - 1

        # If Portal Accessibility is on then remove Rune Keys from the pool, they're placed elsewhere
        if world.options.portal_accessibility.value:
            item_counts_table.pop(item_name.key_teleport)

        # Add secret items from TotS
        if world.options.randomize_secrets.value:
            for s in range(secrets):
                item = world.random.randint(0, 12)
                if item < 8:
                    item_counts_table[item_name.chest_wood] += 1
                elif item < 12:
                    item_counts_table[item_name.ankh] += 1
                else:
                    item_counts_table[item_name.stat_upgrade] += 1

    # Remove extra lives if the option was selected
    if world.options.remove_lives.value:
        extra_items -= item_counts_table.pop(item_name.ankh)
        extra_items -= item_counts_table.pop(item_name.ankh_5up)

    # If the player has selected not to randomize recovery items, set all their counts to zero
    if not world.options.randomize_recovery_items.value:
        for recovery in recovery_table.keys():
            item_counts_table[recovery] = 0

    # Enemy loot
    if world.options.randomize_enemy_loot.value:
        miniboss_stat_upgrade_chances = [
            (0.3, item_name.stat_upgrade_health),
            (0.3, item_name.stat_upgrade_mana),
            (0.3, item_name.stat_upgrade_damage),
            (0.1, item_name.stat_upgrade_defense),
        ]
        miniboss_upgrades = item_counts_table.pop(item_name.miniboss_stat_upgrade)
        for i in range(miniboss_upgrades):
            item = roll_for_item(world, miniboss_stat_upgrade_chances)
            item_counts_table[item] += 1

    # Determine stat upgrades and add them to the pool
    stat_upgrades: int = item_counts_table.pop(item_name.stat_upgrade)
    for u in range(stat_upgrades):
        upgrade = world.random.randrange(4)
        item_counts_table[stat_upgrade_items[upgrade]] += 1

    # Build filler items list
    filler_item_names: typing.List[str] = []
    filler_item_count: int = 0
    for item in item_counts_table.keys():
        if item_table[item].classification == ItemClassification.filler and item_counts_table[item] > 0:
            filler_item_names.append(item)
            filler_item_count += item_counts_table[item]

    # Trap items
    trap_item_percent = world.options.trap_item_percent.value / 100
    if trap_item_percent > 0:
        for trap_item in trap_items:
            item_counts_table[trap_item] = 0
        trap_item_count = int((filler_item_count - extra_items) * trap_item_percent)
        extra_items += trap_item_count
        for t in range(trap_item_count):
            item = trap_items[world.random.randrange(len(trap_items))]
            item_counts_table[item] += 1

    # For Necessary we set the number of bonus chests equal to each extra item
    if world.options.bonus_behavior.value == BonusChestLocationBehavior.option_necessary:
        item_counts_table[item_name.bonus_chest] = max(item_counts_table[item_name.bonus_chest], extra_items, 0)

    return item_counts_table, extra_items


def roll_for_item(world, loot_chances: typing.List[typing.Tuple[float, str]]):
    rnd = world.random.random()
    for item in loot_chances:
        rnd -= item[0]
        if rnd < 0:
            return item[1]
    return None


filler_items: typing.List[str] = [item_name for item_name, data in item_table.items()
                                  if data.classification == ItemClassification.filler]
lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
