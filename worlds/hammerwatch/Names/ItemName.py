# Item Names
import typing

empty = "Empty"
bonus_chest = "Bonus Chest"
key_bonus = "Bonus Key"
chest_blue = "Blue Chest"
chest_green = "Green Chest"
chest_purple = "Purple Chest"
chest_red = "Red Chest"
chest_wood = "Wood Chest"
vendor_coin = "Vendor Coin"
plank = "Strange Plank"
apple = "Apple"
orange = "Orange"
steak = "Steak"
fish = "Fish"
mana_1 = "Mana Shard"
mana_2 = "Mana Orb"
key_bronze = "Bronze Key"
key_silver = "Silver Key"
key_gold = "Gold Key"
mirror = "Mirror"
ore = "Ore"
key_teleport = "Rune Key"
ankh = "1-Up Ankh"
ankh_5up = "5-Up Ankh"
ankh_7up = "7-Up Ankh"
powerup_7up = "7-Up Ankh"
potion_damage = "Damage Potion"
potion_rejuvenation = "Rejuvenation Potion"
potion_invulnerability = "Invulnerability Potion"
stat_upgrade_damage = "Damage Upgrade"
stat_upgrade_defense = "Defense Upgrade"
stat_upgrade_health = "Health Upgrade"
stat_upgrade_mana = "Mana Upgrade"
stat_upgrade = "Random Stat Upgrade"
diamond = "Diamond"
diamond_red = "Red Diamond"
diamond_small = "Small Diamond"
diamond_small_red = "Small Red Diamond"
valuable_1 = "Copper Coin"
valuable_2 = "Copper Coins"
valuable_3 = "Copper Coin Pile"
valuable_4 = "Silver Coin"
valuable_5 = "Silver Coins"
valuable_6 = "Silver Coin Pile"
valuable_7 = "Gold Coin"
valuable_8 = "Gold Coins"
valuable_9 = "Gold Coin Pile"

# Quest Item Names
pan = "Frying Pan"
lever = "Pumps Lever"
pickaxe = "Pickaxe"

pan_fragment = "Frying Pan Fragment"
lever_fragment = "Pumps Lever Fragment"
pickaxe_fragment = "Pickaxe Fragment"

# Special Item Names
sonic_ring = "Gold Ring"
serious_health = "Serious Health Upgrade"

# Custom Item Names
key_bronze_big = "Big Bronze Key"

key_bronze_prison = "Prison Bronze Key"
key_silver_prison = "Prison Silver Key"
key_gold_prison = "Prison Gold Key"
key_bonus_prison = "Prison Bonus Key"
key_bronze_armory = "Armory Bronze Key"
key_silver_armory = "Armory Silver Key"
key_gold_armory = "Armory Gold Key"
key_bonus_armory = "Armory Bonus Key"
key_bronze_archives = "Archives Bronze Key"
key_silver_archives = "Archives Silver Key"
key_gold_archives = "Archives Gold Key"
key_bonus_archives = "Archives Bonus Key"
key_bronze_chambers = "Chambers Bronze Key"
key_silver_chambers = "Chambers Silver Key"
key_gold_chambers = "Chambers Gold Key"
key_bonus_chambers = "Chambers Bonus Key"
key_bronze_big_prison = "Big Prison Bronze Key"
key_bronze_big_armory = "Big Armory Bronze Key"
key_bronze_big_archives = "Big Archives Bronze Key"
key_bronze_big_chambers = "Big Chambers Bronze Key"

# Special Generation stuff
secret = "Secret"
puzzle = "Puzzle"
miniboss_stat_upgrade = "Miniboss Stat Upgrade"
loot_tower = "Tower Loot"
loot_flower = "Flower Loot"
loot_mini_flower = "Mini Flower Loot"

# Trap Items
trap_bomb = "Bomb Trap"
trap_confuse = "Confuse Trap"
trap_mana = "Mana Drain Trap"
trap_poison = "Poison Trap"
trap_frost = "Frost Trap"
trap_fire = "Fire Trap"
trap_banner = "Banner Trap"

# Event/Button Names
ev_victory = "Victory"

btnc_p1_floor = "Prison Floor 1 Open Passage"
ev_castle_p2_switch = "Prison Floor 2 Switch"
btnc_n1_cache_n = "Bonus 1 Open North Treasure Rooms"
btnc_n1_cache_ne = "Bonus 1 Open NE Treasure Room"
btnc_n1_hall_top = "Bonus 1 Open Top of East Hall"
btnc_n1_hall_bottom = "Bonus 1 Open Bottom of East Hall"
btnc_a2_blue_spikes = "Armory Floor 5 Deactivate Blue Spikes"
ev_castle_c2_n_shops_switch = "Chambers Floor 11 Open North Shops Area"
btnc_c2_n_wall = "Chambers Floor 11 Open North Wall"
ev_castle_c3_rspikes_switch = "Chambers Floor 12 Deactivate Red Spikes"
ev_castle_c3_sw_hidden_switch = "Chambers Floor 12 Open SW Hidden Hall"
ev_castle_b1_boss_switch = "Prison Boss Switch"
ev_castle_b2_boss_switch = "Armory Boss Switch"
ev_castle_b3_boss_switch = "Archives Boss Switch"
ev_castle_b4_boss_switch = "Chambers Boss Switch"

evc_beat_boss_1 = "Defeat Queen"
evc_beat_boss_2 = "Defeat Knight"
evc_beat_boss_3 = "Defeat Lich"
evc_beat_boss_4 = "Defeat Dragon"

# Temple
ev_c1_portal = "Cave Level 1 Activate Portal"
ev_c2_portal = "Cave Level 2 Activate Portal"
ev_c3_portal = "Cave Level 3 Activate Portal"
ev_t1_portal = "Temple Floor 1 Activate Portal"
ev_t2_portal = "Temple Floor 2 Activate Portal"
ev_t3_portal = "Temple Floor 3 Activate Portal"
ev_open_temple_entrance_shortcut = "Open Temple Entrance Shortcut"
ev_pof_switch = "Activate PoF Switch"
ev_solar_node = "Activate Solar Node"
evt_t1_n_mirrors = "Temple Floor 1 North Node North Mirrors"
evt_t1_s_mirror = "Temple Floor 1 North Node South Mirror"
btn_t2_blue_spikes = "Temple Floor 2 Deactivate Blue Spikes"
ev_t2_rune_switch = "Temple Floor 2 Light Bridge Rune Button"
ev_pof_1_unlock_exit = "PoF Level 1 Unlock Exit"
ev_pof_2_unlock_exit = "PoF Level 2 Unlock Exit"
ev_pof_complete = "PoF Complete"

evt_beat_boss_1 = "Defeat Dune Sharks"
evt_beat_boss_2 = "Defeat Krilith"
evt_beat_boss_3 = "Defeat Sha'Rand"

# group names
group_chests = "Chests"
group_keys = "Keys"
group_ankhs = "Ankhs"
group_potions = "Potions"
group_diamonds = "Diamonds"
group_upgrades = "Stat Upgrades"
group_coins = "Coins"
group_recovery = "Recovery Items"
group_tools = "Tools"
group_traps = "Traps"

item_groups: typing.Dict[str, typing.Set[str]] = {
    group_chests: {
        bonus_chest,
        chest_blue,
        chest_green,
        chest_purple,
        chest_red,
        chest_wood,
    },
    group_keys: {
        key_bonus,
        key_bronze,
        key_silver,
        key_gold,
        key_bronze_big,
        key_bonus_prison,
        key_bonus_armory,
        key_bonus_archives,
        key_bonus_chambers,
        key_bronze_prison,
        key_bronze_armory,
        key_bronze_archives,
        key_bronze_chambers,
        key_silver_prison,
        key_silver_armory,
        key_silver_archives,
        key_silver_chambers,
        key_gold_prison,
        key_gold_armory,
        key_gold_archives,
        key_gold_chambers,
        key_bronze_big_prison,
        key_bronze_big_armory,
        key_bronze_big_archives,
        key_bronze_big_chambers,
    },
    group_ankhs: {
        ankh,
        ankh_5up,
        ankh_7up,
    },
    group_potions: {
        potion_damage,
        potion_rejuvenation,
        potion_invulnerability,
    },
    group_diamonds: {
        diamond,
        diamond_red,
        diamond_small,
        diamond_small_red,
    },
    group_upgrades: {
        stat_upgrade,
        stat_upgrade_damage,
        stat_upgrade_defense,
        stat_upgrade_health,
        stat_upgrade_mana,
    },
    group_coins: {
        valuable_1,
        valuable_2,
        valuable_3,
        valuable_4,
        valuable_5,
        valuable_6,
        valuable_7,
        valuable_8,
        valuable_9,
    },
    group_recovery: {
        apple,
        orange,
        steak,
        fish,
        mana_1,
        mana_2,
    },
    group_tools: {
        pan,
        lever,
        pickaxe,
        pan_fragment,
        lever_fragment,
        pickaxe_fragment,
    },
    group_traps: {
        trap_bomb,
        trap_mana,
        trap_poison,
        trap_frost,
        trap_fire,
        trap_confuse,
        trap_banner,
    },
}
