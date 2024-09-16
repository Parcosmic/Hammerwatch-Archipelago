# Item Names
import typing
from . import option_names
from .. import util

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
hammer = "Hammer"
hammer_fragment = "Hammer Fragment"

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

key_bronze_prison_1 = "Prison Floor 1 Master Bronze Key"
key_bronze_prison_2 = "Prison Floor 2 Master Bronze Key"
key_bronze_prison_3 = "Prison Floor 3 Master Bronze Key"
key_bronze_armory_1 = "Armory Floor 4 Master Bronze Key"

key_bonus_prison_master = "Prison Master Bonus Key"
key_bonus_armory_master = "Armory Master Bonus Key"
key_bonus_archives_master = "Archives Master Bonus Key"
key_bonus_chambers_master = "Chambers Master Bonus Key"

key_silver_b1 = "Dune Sharks Arena Silver Key"
key_silver_temple_1 = "Temple Floor 1 Master Silver Key"
key_silver_temple_2 = "Temple Floor 2 Master Silver Key"
key_gold_b1 = "Dune Sharks Arena Gold Key"
key_gold_temple_1 = "Temple Floor 1 Master Gold Key"
key_gold_temple_2 = "Temple Floor 2 Master Gold Key"
key_bonus_pof = "Pyramid of Fear Master Bonus Key"

castle_act_bonus_keys = [
    key_bonus_prison,
    key_bonus_armory,
    key_bonus_archives,
    key_bonus_chambers,
]
castle_master_bonus_keys = [
    key_bonus_prison_master,
    key_bonus_armory_master,
    key_bonus_archives_master,
    key_bonus_chambers_master,
]

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
trap_flies = "Fly Trap"

# Shop item names

shop_paladin_health = "Progressive Paladin Health Pool"
shop_paladin_mana = "Progressive Paladin Mana Pool"
shop_paladin_armor = "Progressive Paladin Armor"
shop_paladin_speed = "Progressive Paladin Move Speed"
shop_paladin_combo = "Paladin Combo"
shop_paladin_combo_timer = "Progressive Paladin Combo Timer"
shop_paladin_combo_nova = "Progressive Paladin Combo Nova"
shop_paladin_combo_healing = "Progressive Paladin Combo Healing"
shop_paladin_combo_mana = "Progressive Paladin Combo Mana"
shop_paladin_dmg = "Progressive Paladin Sword Damage"
shop_paladin_charge_dmg = "Progressive Paladin Charge Damage"
shop_paladin_charge_range = "Progressive Paladin Charge Range"
shop_paladin_healing = "Paladin Healing"
shop_paladin_healing_eff = "Progressive Paladin Healing Efficiency"
shop_paladin_holy_storm = "Paladin Holy Storm"
shop_paladin_holy_storm_dmg = "Progressive Paladin Holy Storm Damage"
shop_paladin_holy_storm_dur = "Progressive Paladin Holy Storm Duration"
shop_paladin_divine_wrath = "Progressive Paladin Divine Wrath"
shop_paladin_arc = "Progressive Paladin Sword Arc"
shop_paladin_shield = "Progressive Paladin Shield"

shop_ranger_health = "Progressive Ranger Health Pool"
shop_ranger_mana = "Progressive Ranger Mana Pool"
shop_ranger_armor = "Progressive Ranger Armor"
shop_ranger_speed = "Progressive Ranger Move Speed"
shop_ranger_combo = "Ranger Combo"
shop_ranger_combo_timer = "Progressive Ranger Combo Timer"
shop_ranger_combo_nova = "Progressive Ranger Combo Nova"
shop_ranger_combo_healing = "Progressive Ranger Combo Healing"
shop_ranger_combo_mana = "Progressive Ranger Combo Mana"
shop_ranger_dmg = "Progressive Ranger Bow Damage"
shop_ranger_penetration = "Progressive Ranger Penetration"
shop_ranger_bomb = "Progressive Ranger Bomb Damage"
shop_ranger_overgrowth = "Ranger Overgrowth"
shop_ranger_overgrowth_dur = "Progressive Ranger Overgrowth Duration"
shop_ranger_overgrowth_range = "Progressive Ranger Overgrowth Range"
shop_ranger_flurry = "Ranger Flurry"
shop_ranger_flurry_waves = "Progressive Ranger Flurry Waves"
shop_ranger_flurry_arrows = "Progressive Ranger Flurry Arrows"
shop_ranger_dodge = "Progressive Ranger Dodge"
shop_ranger_marksmanship = "Progressive Ranger Marksmanship"

shop_wizard_health = "Progressive Wizard Health Pool"
shop_wizard_mana = "Progressive Wizard Mana Pool"
shop_wizard_armor = "Progressive Wizard Armor"
shop_wizard_speed = "Progressive Wizard Move Speed"
shop_wizard_combo = "Wizard Combo"
shop_wizard_combo_timer = "Progressive Wizard Combo Timer"
shop_wizard_combo_nova = "Progressive Wizard Combo Nova"
shop_wizard_combo_healing = "Progressive Wizard Combo Healing"
shop_wizard_combo_mana = "Progressive Wizard Combo Mana"
shop_wizard_fireball_damage = "Progressive Wizard Fireball Damage"
shop_wizard_fireball_range = "Progressive Wizard Fireball Range"
shop_wizard_fire_breath_damage = "Progressive Wizard Fire Breath Damage"
shop_wizard_fire_nova = "Wizard Fire Nova"
shop_wizard_fire_nova_flames = "Progressive Wizard Fire Nova Flames"
shop_wizard_fire_nova_slow = "Progressive Wizard Fire Nova Slow"
shop_wizard_meteor_strike = "Wizard Meteor Strike"
shop_wizard_meteor_strike_damage = "Progressive Wizard Meteor Strike Damage"
shop_wizard_meteor_strike_meteors = "Progressive Wizard Meteor Strike Meteors"
shop_wizard_fire_shield = "Wizard Fire Shield"
shop_wizard_combustion = "Wizard Combustion"
shop_wizard_combustion_damage = "Progressive Wizard Combustion Damage"
shop_wizard_combustion_duration = "Progressive Wizard Combustion Duration"

shop_warlock_health = "Progressive Warlock Health Pool"
shop_warlock_mana = "Progressive Warlock Mana Pool"
shop_warlock_armor = "Progressive Warlock Armor"
shop_warlock_speed = "Progressive Warlock Move Speed"
shop_warlock_combo = "Warlock Combo"
shop_warlock_combo_timer = "Progressive Warlock Combo Timer"
shop_warlock_combo_nova = "Progressive Warlock Combo Nova"
shop_warlock_combo_healing = "Progressive Warlock Combo Healing"
shop_warlock_combo_mana = "Progressive Warlock Combo Mana"
shop_warlock_dagger_damage = "Progressive Warlock Dagger Damage"
shop_warlock_dagger_poison = "Progressive Warlock Dagger Poison"
shop_warlock_lightning_strike_damage = "Progressive Warlock Lightning Strike Damage"
shop_warlock_lightning_strike_targets = "Progressive Warlock Lightning Strike Targets"
shop_warlock_summon_gargoyle = "Warlock Summon Gargoyle"
shop_warlock_gargoyle_damage = "Progressive Warlock Gargoyle Damage"
shop_warlock_gargoyle_duration = "Progressive Warlock Gargoyle Duration"
shop_warlock_electrical_storm = "Warlock Electrical Storm"
shop_warlock_electrical_storm_damage = "Progressive Warlock Electrical Storm Damage"
shop_warlock_electrical_storm_duration = "Progressive Warlock Electrical Storm Duration"
shop_warlock_blood_sacrifice = "Progressive Warlock Blood Sacrifice"
shop_warlock_soul_sacrifice = "Progressive Warlock Soul Sacrifice"

shop_thief_health = "Progressive Thief Health Pool"
shop_thief_mana = "Progressive Thief Mana Pool"
shop_thief_armor = "Progressive Thief Armor"
shop_thief_speed = "Progressive Thief Move Speed"
shop_thief_combo = "Thief Combo"
shop_thief_combo_timer = "Progressive Thief Combo Timer"
shop_thief_combo_nova = "Progressive Thief Combo Nova"
shop_thief_combo_healing = "Progressive Thief Combo Healing"
shop_thief_combo_mana = "Progressive Thief Combo Mana"
shop_thief_knives_damage = "Progressive Thief Knives Damage"
shop_thief_knife_fan_damage = "Progressive Thief Knife Fan Damage"
shop_thief_knife_fan_knives = "Progressive Thief Knife Fan Knives"
shop_thief_grapple_chain = "Thief Grapple Chain"
shop_thief_grapple_chain_length = "Progressive Thief Grapple Chain Length"
shop_thief_grapple_chain_stun = "Progressive Thief Grapple Chain Stun"
shop_thief_smoke_bomb = "Thief Smoke Bomb"
shop_thief_smoke_bomb_range = "Progressive Thief Smoke Bomb Range"
shop_thief_fervor = "Progressive Thief Fervor"
shop_thief_speed_penalty = "Progressive Thief Speed Penalty"
shop_thief_dodge = "Progressive Thief Dodge"

shop_priest_health = "Progressive Priest Health Pool"
shop_priest_mana = "Progressive Priest Mana Pool"
shop_priest_armor = "Progressive Priest Armor"
shop_priest_speed = "Progressive Priest Move Speed"
shop_priest_combo = "Priest Combo"
shop_priest_combo_timer = "Progressive Priest Combo Timer"
shop_priest_combo_nova = "Progressive Priest Combo Nova"
shop_priest_combo_healing = "Progressive Priest Combo Healing"
shop_priest_combo_mana = "Progressive Priest Combo Mana"
shop_priest_smite_damage = "Progressive Priest Smite Damage"
shop_priest_speed_penalty = "Progressive Priest Speed Penalty"
shop_priest_holy_beam_damage = "Progressive Priest Holy Beam Damage"
shop_priest_holy_beam_range = "Progressive Priest Holy Beam Range"
shop_priest_draining_field = "Priest Draining Field"
shop_priest_draining_field_damage = "Progressive Priest Draining Field Damage"
shop_priest_draining_field_number = "Progressive Priest Draining Field Number"
shop_priest_cripple_aura = "Priest Cripple Aura"
shop_priest_cripple_aura_slow = "Progressive Priest Cripple Aura Slow"
shop_priest_cripple_aura_mana_drain = "Priest Cripple Aura Mana Drain"
shop_priest_hp_regen = "Progressive Priest HP Regen"
shop_priest_magic_shield = "Progressive Priest Magic Shield"

shop_sorcerer_health = "Progressive Sorcerer Health Pool"
shop_sorcerer_mana = "Progressive Sorcerer Mana Pool"
shop_sorcerer_armor = "Progressive Sorcerer Armor"
shop_sorcerer_speed = "Progressive Sorcerer Move Speed"
shop_sorcerer_combo = "Sorcerer Combo"
shop_sorcerer_combo_timer = "Progressive Sorcerer Combo Timer"
shop_sorcerer_combo_nova = "Progressive Sorcerer Combo Nova"
shop_sorcerer_combo_healing = "Progressive Sorcerer Combo Healing"
shop_sorcerer_combo_mana = "Progressive Sorcerer Combo Mana"
shop_sorcerer_ice_shard_damage = "Progressive Sorcerer Ice Shard Damage"
shop_sorcerer_ice_shard_bounces = "Progressive Sorcerer Ice Shard Bounces"
shop_sorcerer_comet_damage = "Progressive Sorcerer Comet Damage"
shop_sorcerer_ice_shard_nova = "Sorcerer Ice Shard Nova"
shop_sorcerer_ice_shard_nova_number = "Progressive Sorcerer Ice Shard Nova Number"
shop_sorcerer_ice_shard_nova_mana = "Progressive Sorcerer Ice Shard Nova Mana"
shop_sorcerer_ice_orb = "Sorcerer Ice Orb"
shop_sorcerer_ice_orb_damage = "Progressive Sorcerer Ice Orb Damage"
shop_sorcerer_ice_orb_time = "Progressive Sorcerer Ice Orb Time"
shop_sorcerer_chill = "Sorcerer Chill"
shop_sorcerer_chill_slow = "Progressive Sorcerer Chill Slow"
shop_sorcerer_chill_duration = "Progressive Sorcerer Chill Duration"
shop_sorcerer_frost_shield = "Progressive Sorcerer Frost Shield"

shop_upgrade_prereqs: typing.Dict[str, str] = {
    shop_paladin_combo_timer: shop_paladin_combo,
    shop_paladin_combo_nova: shop_paladin_combo,
    shop_paladin_combo_healing: shop_paladin_combo,
    shop_paladin_combo_mana: shop_paladin_combo,
    shop_paladin_healing_eff: shop_paladin_healing,
    shop_paladin_holy_storm_dmg: shop_paladin_holy_storm,
    shop_paladin_holy_storm_dur: shop_paladin_holy_storm,
    shop_ranger_combo_timer: shop_ranger_combo,
    shop_ranger_combo_nova: shop_ranger_combo,
    shop_ranger_combo_healing: shop_ranger_combo,
    shop_ranger_combo_mana: shop_ranger_combo,
    shop_ranger_overgrowth_dur: shop_ranger_overgrowth,
    shop_ranger_overgrowth_range: shop_ranger_overgrowth,
    shop_ranger_flurry_waves: shop_ranger_flurry,
    shop_ranger_flurry_arrows: shop_ranger_flurry,
    shop_wizard_combo_timer: shop_wizard_combo,
    shop_wizard_combo_nova: shop_wizard_combo,
    shop_wizard_combo_healing: shop_wizard_combo,
    shop_wizard_combo_mana: shop_wizard_combo,
    shop_wizard_fire_nova_flames: shop_wizard_fire_nova,
    shop_wizard_fire_nova_slow: shop_wizard_fire_nova,
    shop_wizard_meteor_strike_damage: shop_wizard_meteor_strike,
    shop_wizard_meteor_strike_meteors: shop_wizard_meteor_strike,
    shop_wizard_combustion_damage: shop_wizard_combustion,
    shop_wizard_combustion_duration: shop_wizard_combustion,
    shop_warlock_combo_timer: shop_warlock_combo,
    shop_warlock_combo_nova: shop_warlock_combo,
    shop_warlock_combo_healing: shop_warlock_combo,
    shop_warlock_combo_mana: shop_warlock_combo,
    shop_warlock_gargoyle_damage: shop_warlock_summon_gargoyle,
    shop_warlock_gargoyle_duration: shop_warlock_summon_gargoyle,
    shop_warlock_electrical_storm_damage: shop_warlock_electrical_storm,
    shop_warlock_electrical_storm_duration: shop_warlock_electrical_storm,
    shop_thief_combo_timer: shop_thief_combo,
    shop_thief_combo_nova: shop_thief_combo,
    shop_thief_combo_healing: shop_thief_combo,
    shop_thief_combo_mana: shop_thief_combo,
    shop_thief_grapple_chain_length: shop_thief_grapple_chain,
    shop_thief_grapple_chain_stun: shop_thief_grapple_chain,
    shop_thief_smoke_bomb_range: shop_thief_smoke_bomb,
    shop_priest_combo_timer: shop_priest_combo,
    shop_priest_combo_nova: shop_priest_combo,
    shop_priest_combo_healing: shop_priest_combo,
    shop_priest_combo_mana: shop_priest_combo,
    shop_priest_draining_field_damage: shop_priest_draining_field,
    shop_priest_draining_field_number: shop_priest_draining_field,
    shop_priest_cripple_aura_slow: shop_priest_cripple_aura,
    shop_priest_cripple_aura_mana_drain: shop_priest_cripple_aura,
    shop_sorcerer_combo_timer: shop_sorcerer_combo,
    shop_sorcerer_combo_nova: shop_sorcerer_combo,
    shop_sorcerer_combo_healing: shop_sorcerer_combo,
    shop_sorcerer_combo_mana: shop_sorcerer_combo,
    shop_sorcerer_ice_shard_nova_number: shop_sorcerer_ice_shard_nova,
    shop_sorcerer_ice_shard_nova_mana: shop_sorcerer_ice_shard_nova,
    shop_sorcerer_ice_orb_damage: shop_sorcerer_ice_orb,
    shop_sorcerer_ice_orb_time: shop_sorcerer_ice_orb,
    shop_sorcerer_chill_slow: shop_sorcerer_chill,
    shop_sorcerer_chill_duration: shop_sorcerer_chill,
}
shop_upgrade_roots: typing.Set[str] = {
    shop_paladin_combo,
    shop_paladin_healing,
    shop_paladin_holy_storm,
    shop_ranger_combo,
    shop_ranger_overgrowth,
    shop_ranger_flurry,
    shop_wizard_combo,
    shop_wizard_fire_nova,
    shop_wizard_meteor_strike,
    shop_wizard_combustion,
    shop_warlock_combo,
    shop_warlock_summon_gargoyle,
    shop_warlock_electrical_storm,
    shop_thief_combo,
    shop_thief_grapple_chain,
    shop_thief_smoke_bomb,
    shop_priest_combo,
    shop_priest_draining_field,
    shop_priest_cripple_aura,
    shop_sorcerer_combo,
    shop_sorcerer_ice_shard_nova,
    shop_sorcerer_ice_orb,
    shop_sorcerer_chill,
}

class_shop_upgrades: typing.Dict[util.PlayerClass, typing.List[str]] = {
    util.PlayerClass.Paladin: [
        shop_paladin_health,
        shop_paladin_mana,
        shop_paladin_armor,
        shop_paladin_speed,
        shop_paladin_combo,
        shop_paladin_combo_timer,
        shop_paladin_combo_nova,
        shop_paladin_combo_healing,
        shop_paladin_combo_mana,
        shop_paladin_dmg,
        shop_paladin_charge_dmg,
        shop_paladin_charge_range,
        shop_paladin_healing,
        shop_paladin_healing_eff,
        shop_paladin_holy_storm,
        shop_paladin_holy_storm_dmg,
        shop_paladin_holy_storm_dur,
        shop_paladin_divine_wrath,
        shop_paladin_arc,
        shop_paladin_shield,
    ],
    util.PlayerClass.Ranger: [
        shop_ranger_health,
        shop_ranger_mana,
        shop_ranger_armor,
        shop_ranger_speed,
        shop_ranger_combo,
        shop_ranger_combo_timer,
        shop_ranger_combo_nova,
        shop_ranger_combo_healing,
        shop_ranger_combo_mana,
        shop_ranger_dmg,
        shop_ranger_penetration,
        shop_ranger_bomb,
        shop_ranger_overgrowth,
        shop_ranger_overgrowth_dur,
        shop_ranger_overgrowth_range,
        shop_ranger_flurry,
        shop_ranger_flurry_waves,
        shop_ranger_flurry_arrows,
        shop_ranger_dodge,
        shop_ranger_marksmanship,
    ],
    util.PlayerClass.Wizard: [
        shop_wizard_health,
        shop_wizard_mana,
        shop_wizard_armor,
        shop_wizard_speed,
        shop_wizard_combo,
        shop_wizard_combo_timer,
        shop_wizard_combo_nova,
        shop_wizard_combo_healing,
        shop_wizard_combo_mana,
        shop_wizard_fireball_damage,
        shop_wizard_fireball_range,
        shop_wizard_fire_breath_damage,
        shop_wizard_fire_nova,
        shop_wizard_fire_nova_flames,
        shop_wizard_fire_nova_slow,
        shop_wizard_meteor_strike,
        shop_wizard_meteor_strike_damage,
        shop_wizard_meteor_strike_meteors,
        shop_wizard_fire_shield,
        shop_wizard_combustion,
        shop_wizard_combustion_damage,
        shop_wizard_combustion_duration,
    ],
    util.PlayerClass.Warlock: [
        shop_warlock_health,
        shop_warlock_mana,
        shop_warlock_armor,
        shop_warlock_speed,
        shop_warlock_combo,
        shop_warlock_combo_timer,
        shop_warlock_combo_nova,
        shop_warlock_combo_healing,
        shop_warlock_combo_mana,
        shop_warlock_dagger_damage,
        shop_warlock_dagger_poison,
        shop_warlock_lightning_strike_damage,
        shop_warlock_lightning_strike_targets,
        shop_warlock_summon_gargoyle,
        shop_warlock_gargoyle_damage,
        shop_warlock_gargoyle_duration,
        shop_warlock_electrical_storm,
        shop_warlock_electrical_storm_damage,
        shop_warlock_electrical_storm_duration,
        shop_warlock_blood_sacrifice,
        shop_warlock_soul_sacrifice,
    ],
    util.PlayerClass.Thief: [
        shop_thief_health,
        shop_thief_mana,
        shop_thief_armor,
        shop_thief_speed,
        shop_thief_combo,
        shop_thief_combo_timer,
        shop_thief_combo_nova,
        shop_thief_combo_healing,
        shop_thief_combo_mana,
        shop_thief_knives_damage,
        shop_thief_knife_fan_damage,
        shop_thief_knife_fan_knives,
        shop_thief_grapple_chain,
        shop_thief_grapple_chain_length,
        shop_thief_grapple_chain_stun,
        shop_thief_smoke_bomb,
        shop_thief_smoke_bomb_range,
        shop_thief_fervor,
        shop_thief_speed_penalty,
        shop_thief_dodge,
    ],
    util.PlayerClass.Priest: [
        shop_priest_health,
        shop_priest_mana,
        shop_priest_armor,
        shop_priest_speed,
        shop_priest_combo,
        shop_priest_combo_timer,
        shop_priest_combo_nova,
        shop_priest_combo_healing,
        shop_priest_combo_mana,
        shop_priest_smite_damage,
        shop_priest_speed_penalty,
        shop_priest_holy_beam_damage,
        shop_priest_holy_beam_range,
        shop_priest_draining_field,
        shop_priest_draining_field_damage,
        shop_priest_draining_field_number,
        shop_priest_cripple_aura,
        shop_priest_cripple_aura_slow,
        shop_priest_cripple_aura_mana_drain,
        shop_priest_hp_regen,
        shop_priest_magic_shield,
    ],
    util.PlayerClass.Sorcerer: [
        shop_sorcerer_health,
        shop_sorcerer_mana,
        shop_sorcerer_armor,
        shop_sorcerer_speed,
        shop_sorcerer_combo,
        shop_sorcerer_combo_timer,
        shop_sorcerer_combo_nova,
        shop_sorcerer_combo_healing,
        shop_sorcerer_combo_mana,
        shop_sorcerer_ice_shard_damage,
        shop_sorcerer_ice_shard_bounces,
        shop_sorcerer_comet_damage,
        shop_sorcerer_ice_shard_nova,
        shop_sorcerer_ice_shard_nova_number,
        shop_sorcerer_ice_shard_nova_mana,
        shop_sorcerer_ice_orb,
        shop_sorcerer_ice_orb_damage,
        shop_sorcerer_ice_orb_time,
        shop_sorcerer_chill,
        shop_sorcerer_chill_slow,
        shop_sorcerer_chill_duration,
        shop_sorcerer_frost_shield,
    ],
}

# Castle button item names
btnc_b1_rune_1 = "Prison Boss Rune y"
btnc_b1_rune_2 = "Prison Boss Rune n"
btnc_b1_rune_3 = "Prison Boss Rune A"
btnc_b2_rune_1 = "Armory Boss Rune y"
btnc_b2_rune_2 = "Armory Boss Rune n"
btnc_b2_rune_3 = "Armory Boss Rune A"
btnc_b3_rune_1 = "Archives Boss Rune y"
btnc_b3_rune_2 = "Archives Boss Rune n"
btnc_b3_rune_3 = "Archives Boss Rune A"
btnc_b4_rune_1 = "Chambers Boss Rune y"
btnc_b4_rune_2 = "Chambers Boss Rune n"
btnc_b4_rune_3 = "Chambers Boss Rune A"
btnc_pstart_puzzle = "Activate PrF1 Puzzle"
btnc_p2_puzzle = "Activate PrF2 Puzzle"
btnc_a1_puzzle = "Activate AmF4 Puzzle"
btnc_a2_puzzle = "Activate AmF5 Puzzle"
btnc_r1_puzzle = "Activate AvF7 Puzzle"
btnc_r2_puzzle = "Activate AvF8 Puzzle"
btnc_c2_puzzle = "Activate ChF11 Puzzle"
btnc_p1_floor = "Open PrF1 Passage"
btnc_p2_spike_puzzle_r = "Enable PrF2 Spike Puzzle East Buttons"
btnc_p2_spike_puzzle_b = "Enable PrF2 Spike Puzzle South Buttons"
btnc_p2_spike_puzzle_t = "Enable PrF2 Spike Puzzle North Buttons"
btnc_p2_red_spikes = "Disable PrF2 Red Spikes"
btnc_p2_open_w_jail = "Open PrF2 West Treasure Room"
btnc_p2_tp_jail = "Teleport PrF2 West Treasure Room Item"
btnc_p2_e_save = "Open PrF2 East Save Room"
btnc_p2_tp_w = "Teleport PrF2 West Rune Puzzle Item"
btnc_p2_rune_sequence = "Activate PrF2 SE Rune Puzzle Reward"
btnc_p2_m_stairs = "Open PrF2 Middle Entrance Room"
btnc_p2_shortcut_n = "Open PrF2 Middle Shortcut Top"
btnc_p2_shortcut_s = "Open PrF2 Middle Shortcut Bottom"
btnc_p3_boss_door = "Open PrF3 Boss Gate"
btnc_p3_sgate_spikes = "Disable PrF3 Entrance Gate Spikes"
btnc_p3_red_spikes = "Disable PrF3 Red Spikes"
btnc_p3_blue_spikes = "Disable PrF3 Blue Spikes"
btnc_p3_e_passage = "Open PrF3 SE Passage"
btnc_p3_s_spikes = "Disable PrF3 South Spikes"
btnc_p3_portal = "Open PrF3 Bonus Portal"
btnc_p3_open_bonus = "Open PrF3 Bonus Room"
btnc_p3_start = "Open PrF3 Entrance Room"
btnc_p3_shop = "Open PrF3 North Secret Shop Room"
btnc_p3_bonus_side = "Open PrF3 Bonus Room Side Hall"
btnc_p3_sw_shortcut = "Open PrF3 SW Shortcut"
btnc_p3_open_n_shortcut = "Open PrF3 North Tower Room Shortcut"
btnc_p3_s_passage = "Open PrF3 South Arrow Hall Passage"
btnc_p3_s_exit_l = "Open PrF3 South Exit Room Left Side"
btnc_p3_s_exit_r = "Open PrF3 South Exit Room Right Side"
btnc_p3_nw_room = "Open PrF3 NW Treasure Room"
btnc_b1_pillars = "Enable Queen Arena Buttons"
btnc_b1_right = "Enable Queen Arena Right Button"
btnc_n1_cache_n = "Open PrB North Treasure Rooms"
btnc_n1_cache_ne = "Open PrB NE Treasure Room"
btnc_n1_hall_top = "Open PrB Top of East Hall"
btnc_n1_hall_bottom = "Open PrB Bottom of East Hall"
btnc_a1_boss_door = "Open AmF4 Boss Gate"
btnc_a1_tp_n = "Teleport AmF4 North Item"
btnc_a1_m_shortcut = "Open AmF4 Middle Shortcut"
btnc_a1_red_spikes = "Disable AmF4 Red Spikes"
btnc_a1_sw_spikes = "Disable AmF4 SW Spikes"
btnc_a1_open_se_cache = "Open AmF4 SE Cache"
btnc_a1_open_m_cache = "Open AmF4 Middle Cache"
btnc_a1_open_ne_cache = "Open AmF4 NE Cache"
btnc_a1_open_se_wall = "Open AmF4 South Wall"
btnc_a1_open_se_rune = "Open AmF4 SE Rune Room"
btnc_a2_pyramid_nw = "Teleport AmF5 NW Pyramid Item"
btnc_a2_bspikes_tp = "Teleport AmF5 Blue Spikes Item"
btnc_a2_open_bonus = "Activate AmF5 Bonus Portal"
btnc_a3_pyramid_ne = "Teleport AmF6 NE Pyramid Item"
btnc_a2_pyramid_sw = "Teleport AmF5 SW Pyramid Item"
btnc_a2_pyramid_se = "Teleport AmF5 SE Pyramid Item"
btnc_a2_tp_ne = "Teleport AmF5 NE Fireball Hall Item"
btnc_a2_tp_sw = "Teleport AmF5 SW Item"
btnc_a2_tp_se = "Teleport AmF5 SE Item"
btnc_a2_tp_ne_gates = "Teleport AmF5 NE Gates Item"
btnc_a2_open_w_exit = "Open AmF5 West Exits Hall"
btnc_a2_open_shortcut = "Open AmF5 Start Shortcut"  # Useful
btnc_a2_open_se_room_l = "Open AmF5 SE Tower Room Left Side"
btnc_a2_open_se_room_t = "Open AmF5 SE Tower Room Top Side"
btnc_a2_blue_spikes = "Disable AmF5 Blue Spikes"
btnc_n2_open_se_room = "Open AmB SE Room"
btnc_n2_open_ne_room = "Open AmB NE Room"
btnc_n2_open_exit = "Open AmB Exit"
btnc_a3_open_knife = "Open AmF6 Spike Turret Reward Rooms"
btnc_a3_tp_m = "Teleport AmF6 Middle Item"
btnc_a3_bgate_tp = "Teleport AmF6 South Pyramid South Bronze Gate Item"
btnc_a3_open_knife_2 = "Open AmF6 Spike Turret 2nd Reward Rooms"
btnc_a3_open_m_stairs = "Open AmF6 Middle Exit"
btnc_a3_open_start_n = "Open AmF6 Start North Wall"
btnc_a3_open_start_e = "Open AmF6 Start East Wall"
btnc_r1_open_w_wall = "Open AvF7 West Wall"
btnc_r1_open_n_wall = "Open AvF7 North Wall"
btnc_r1_open_nw_room = "Open AvF7 NW Secret Room"
btnc_r1_open_m_ledge = "Open AvF7 Middle Ledge"  # Useful, only gives money
btnc_r1_open_l_exit = "Open AvF7 Bottom of Left Exit"
btnc_r1_open_start_room = "Open AvF7 Start Closed Room"
btnc_r1_open_e_wall = "Open AvF7 East Wall"
btnc_r1_open_exits = "Open AvF7 Exits"
btnc_r1_ne_shortcut = "Open AvF7 NE Shortcut"  # Useful
btnc_r1_w_shortcut = "Open AvF7 West Shortcut"  # Useful
btnc_r1_open_se_room = "Open AvF7 SE Closed Room"
btnc_r2_open_bs_l = "Open AvF8 Boss Rune Room Left Side"
btnc_r2_open_bs_r = "Open AvF8 Boss Rune Room Right Side"
btnc_r2_open_fire_t = "Open AvF8 Fire Trap Room Top Side"
btnc_r2_open_exit = "Open AvF8 Left Exit"
btnc_r2_open_s_r = "Open AvF8 South Area Right Side"
btnc_r2_open_fire_b = "Open AvF8 Fire Trap Room Bottom Side"
btnc_r2_open_s_l = "Open AvF8 South Area Left Side"
btnc_r2_open_puzzle = "Open AvF8 Puzzle Room"
btnc_r2_nw_shortcut = "Open AvF8 NW Shortcut"  # Useful
btnc_r2_open_start = "Open AvF8 Middle Entrance"
btnc_r2_open_spikes_t = "Open AvF8 Spike Turret Island Top Shortcut"
btnc_r2_light_bridge = "Activate AvF8 SW Light Bridge"
btnc_r2_open_ne_cache = "Open AvF8 NE Cache"
btnc_r2_open_spikes_l = "Open AvF8 Spike Turret Island Left Shortcut"
btnc_r3_boss_door = "Open AvF9 Boss Gate"
btnc_r3_passage_room_2 = "Open AvF9 Secret Passage North Room"
btnc_r3_tp_nw = "Teleport AvF9 NW Item"
btnc_r3_open_exit = "Open AvF9 Exit"
btnc_r3_open_ne_t = "Open AvF9 NE Room Top Side"
btnc_r3_passage_room_2_spikes = "Disable AvF9 Secret Passage North Room Spikes"
btnc_r3_open_ne_l = "Open AvF9 NE Room Left Side"
btnc_r3_open_s_t = "Open AvF9 South Room Top Side"
btnc_r3_open_s_r = "Open AvF9 South Room Right Side"
btnc_r3_open_bs = "Open AvF9 Boss Rune Room"
btnc_r3_simon = "Activate AvF9 Simon Says Puzzle"
btnc_r3_bonus_bridge = "Activate AvF9 Bonus Return Light Bridge"
btnc_r3_bonus = "Open AvF9 Bonus Portal Passage"
btnc_r3_passage_end = "Open AvF9 Secret Passage End"
btnc_r3_passage_room_1 = "Open AvF9 Secret Passage South Room"
btnc_r3_tp_ne_t = "Teleport AvF9 NE Top Item"
btnc_r3_tp_ne_b = "Teleport AvF9 NE Bottom Item"
btnc_r3_simon_room = "Open AvF9 Simon Says Room"
btnc_r3_sw_room = "Open AvF9 SW Secret Room"
btnc_r3_passage = "Open AvF9 Secret Passage"
btnc_c1_n_spikes = "Disable ChF10 North Spikes"
btnc_c1_red_spikes = "Disable ChF10 Red Spikes"
btnc_c1_red_spike_turrets = "Disable ChF10 Red Spike Turrets"  # Useful
btnc_c1_red_flame_turrets = "Disable ChF10 Red Flame Turret"  # Useful
btnc_c1_s_shortcut = "Open ChF10 South Shortcut"
btnc_c1_sw_exit = "Open ChF10 SW Exit"
btnc_pstart_bridge = "Activate PrF1 SW Light Bridge"
btnc_c2_sw_room = "Open ChF11 SW Secret Room"
btnc_c2_n_shops = "Open ChF11 North Shops Room"
btnc_c2_w_shortcut = "Open ChF11 West Shortcut"
btnc_c2_bonus = "Open ChF11 Bonus Portal"
btnc_c2_tp_spikes = "Teleport ChF11 West Spike Items"
btnc_c2_bonus_room = "Open ChF11 Bonus Room"
btnc_c2_n_room = "Open ChF11 North Exit Closed Room"
btnc_c2_n_red_flame_turret_on = "Activate ChF11 North Red Flame Turret"  # Useful
btnc_c2_blue_spike_turret = "Disable ChF11 Blue Spike Turret"  # Useful
btnc_c2_open_puzzle = "Open ChF11 Chance Puzzle Room"
btnc_c2_e_shop = "Open ChF11 East Shop Shortcut"
btnc_c2_s_red_flame_turret = "Disable ChF11 South Red Flame Turrets"  # Useful
btnc_c2_s_shortcut = "Open ChF11 South Entrance Shortcut"  # Useful
btnc_c3_e_shortcut = "Open ChF12 East Shortcut"
btnc_c3_sw_room = "Open ChF12 SW Hidden Hall"
btnc_c3_red_spikes = "Disable ChF12 Red Spikes"
btnc_c3_blue_fire_turrets_on = "Activate ChF12 Blue Flame Turrets"  # Trap
btnc_c3_tp_m = "Teleport ChF12 Middle Item"
btnc_c3_red_spike_turrets = "Disable ChF12 Red Spike Turrets"  # Useful
btnc_c3_tp_se = "Teleport ChF12 Fire Floor Item"
btnc_c3_open_w_room = "Open ChF12 West Secret Room"
btnc_c3_open_s_hall = "Open ChF12 South Hidden Hall"

# btnc_b1_rune_1_part = "Prison Boss Rune y Progress"
# btnc_b1_rune_2_part = "Prison Boss Rune n Progress"
# btnc_b1_rune_3_part = "Prison Boss Rune A Progress"
# btnc_b2_rune_1_part = "Armory Boss Rune y Progress"
# btnc_b2_rune_2_part = "Armory Boss Rune n Progress"
# btnc_b2_rune_3_part = "Armory Boss Rune A Progress"
# btnc_b3_rune_1_part = "Archives Boss Rune y Progress"
# btnc_b3_rune_2_part = "Archives Boss Rune n Progress"
# btnc_b3_rune_3_part = "Archives Boss Rune A Progress"
# btnc_b4_rune_1_part = "Chambers Boss Rune y Progress"
# btnc_b4_rune_2_part = "Chambers Boss Rune n Progress"
# btnc_b4_rune_3_part = "Chambers Boss Rune A Progress"
# btnc_p2_spike_puzzle_r_part = "Enable PrF2 Spike Puzzle East Buttons Progress"
# btnc_p2_spike_puzzle_b_part = "Enable PrF2 Spike Puzzle South Buttons Progress"
# btnc_p2_spike_puzzle_t_part = "Enable PrF2 Spike Puzzle North Buttons Progress"
# btnc_p2_tp_w_part = "Teleport PrF2 West Rune Puzzle Item Progress"
btnc_p2_rune_sequence_part = "Activate PrF2 SE Rune Puzzle Reward Progress"
# btnc_p3_portal_part = "Open PrF3 Bonus Portal Progress"
# btnc_p3_open_bonus_part = "Open PrF3 Bonus Room Progress"
# btnc_a1_open_se_cache_part = "Open AmF4 SE Cache Progress"
# btnc_a2_tp_ne_gates_part = "Teleport AmF5 NE Gates Item Progress"
# btnc_a3_open_knife_part = "Open AmF6 Spike Turret Reward Rooms Progress"
# btnc_a3_open_knife_2_part = "Open AmF6 Spike Turret 2nd Reward Rooms Progress"
# btnc_r2_open_puzzle_part = "Open AvF8 Puzzle Room Progress"
# btnc_r3_bonus_bridge_part = "Activate AvF9 Bonus Return Light Bridge Progress"
# btnc_r3_bonus_part = "Open AvF9 Bonus Portal Passage Progress"
# btnc_r3_simon_room_part = "Open AvF9 Simon Says Room Progress"
# btnc_pstart_bridge_part = "Activate PrF1 SW Light Bridge Progress"
# btnc_c2_bonus_part = "Open ChF11 Bonus Portal Progress"
# btnc_c2_tp_spikes_part = "Teleport ChF11 West Spike Items Progress"
# btnc_c2_bonus_room_part = "Open ChF11 Bonus Room Progress"
# btnc_c3_sw_room_part = "Open ChF12 SW Hidden Hall Progress"

# Temple button item names
btn_pof = "Elevate PoF Pyramid"
btn_c3_puzzle = "Activate CL3 Puzzle"
btn_c2_puzzle = "Activate CL2 Puzzle"
btn_c1_puzzle_e = "Activate CL1 East Puzzle"
btn_c1_puzzle_w = "Activate CL1 West Puzzle"
btn_p_puzzle = "Activate SP Puzzle"
btn_t1_puzzle_w = "Activate TF1 West Puzzle"
btn_t1_puzzle_e = "Activate TF1 East Puzzle"
btn_t2_puzzle_w = "Activate TF2 West Puzzle"
btn_t2_puzzle_e = "Activate TF2 East Puzzle"
btn_t2_puzzle_n = "Activate TF2 North Puzzle"
btn_t2_puzzle_s = "Activate TF2 South Puzzle"
btn_t3_puzzle = "Activate TF3 Puzzle"
btn_pof_puzzle = "Activate PoF Puzzle"
btn_c3_fall_bridge = "Fix CL3 Fall Bridge"
btn_c3_e_bridge = "Fix CL3 East Bridge"
btn_c2_red = "Fix CL2 Red Bridge"
btn_c2_green = "Fix CL2 Green Bridge"
btn_c2_bridges = "Fix CL2 Double Bridge"
btn_c2_s_bridge = "Fix CL2 Exit Bridge"
btn_c2_pumps = "Activate Water Pumps"
btn_c1_blue = "Fix CL1 Blue Bridge"
btn_c1_red = "Fix CL1 Red Bridge"
btn_c1_green = "Fix CL1 Green Bridge"
btn_c1_tunnel = "Open CL1 Secret Tunnel"
btn_b1_bridge = "Fix Dune Sharks Bridge"
btn_t1_jail_n = "Open TF1 North Jail"
btn_t1_jail_e = "Open TF1 East Jail"
btn_t1_telarian = "Open TF1 Telarian Gate"
btn_t1_guard = "Open TF1 Trapped Guard Gate"
btn_t1_hall = "Open TF1 NE Node Hallway"
btn_t1_runway = "Open TF1 Fireball Runway Passages"
btn_t2_blue = "Disable TF2 Blue Spikes"
btn_t2_light_bridges = "Activate TF2 Light Bridges"
btn_t2_jones_hall_back = "Open TF2 Back of Indiana Jones Hallway"
btn_t2_jones_hall = "Open TF2 Indiana Jones Hallway"
btn_t2_nw_gate = "Open TF2 NW Pillar Gate"
btn_t2_t3_gate_w = "Open TF2 Ornate Room Gate Left Side"
btn_t2_t3_gate_e = "Open TF2 Ornate Room Gate Right Side"
btn_t2_boulder_passage = "Open TF2 Boulder Room Secret Passage"
btn_t2_ice_gate_w = "Open TF2 West Ice Pillar Gate"
btn_t2_ice_gate_e = "Open TF2 East Ice Pillar Gate"
btn_t2_boulder_room = "Open TF2 Boulder Room"
btn_t2_portal = "Open TF2 Portal Room Shortcut"
btn_t2_jail_e = "Open TF2 East Jail"
btn_t2_jail_w = "Open TF2 West Jail"
btn_t2_jail_s = "Open TF2 South Jail"
btn_t2_s_gate_shortcut = "Open TF2 South Gate Shortcut"
btn_t2_s_gate_hall = "Open TF2 South Gate Hall"  # Useless, mark as filler
btn_t2_s_spikes = "Disable TF2 South Spikes"
btn_t2_portal_gate = "Open TF2 SW Portal Gate"
btn_t3_gold_chutes = "Activate TF3 Gold Chutes"
btn_t3_fall_1 = "Open TF3 SE Boss Fall Room"
btn_t3_fall_2 = "Open TF3 NE Boss Fall Room"
btn_t3_fall_3 = "Open TF3 West Boss Fall Room"
btn_t3_pillars = "Disable TF3 North Pillar Walls"
btn_t3_gate_s = "Open TF3 South Gate"
btn_pof_1_walls_s = "Open PoF Level 1 South Walls"
btn_pof_1_exit = "Open PoF Level 1 Exit"
btn_pof_2_puzzle = "Open PoF Level 2 Puzzle Room"
btn_pof_2_exit = "Open PoF Level 2 Exit"
btn_pof_3_start = "Open PoF Level 3 Start Room"

# btn_pof_part = "Elevate PoF Pyramid Progress"
# btn_t2_light_bridges_part = "Activate TF2 Light Bridges Progress"
# btn_t2_portal_part = "Open TF2 Portal Room Shortcut Progress"
# btn_t3_puzzle_room_part = "Open TF3 Puzzle Room Progress"

# Event/Button Names
evc_escaped = "Escaped Castle Hammerwatch"
ev_all_planks = "Get required Strange Planks"

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
ev_solar_node = "Activate Solar Node"
evt_t1_n_mirrors = "Temple Floor 1 North Node North Mirrors"
evt_t1_s_mirror = "Temple Floor 1 North Node South Mirror"
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
group_buttons = "Buttons"

group_b1_boss = "Prison Boss Rune"
group_b2_boss = "Armory Boss Rune"
group_b3_boss = "Archives Boss Rune"
group_b4_boss = "Chambers Boss Rune"

group_shop_items = "Shop Upgrades"
group_shop_paladin = "Paladin Shop Upgrades"
group_shop_ranger = "Ranger Shop Upgrades"
group_shop_wizard = "Wizard Shop Upgrades"
group_shop_warlock = "Warlock Shop Upgrades"
group_shop_thief = "Thief Shop Upgrades"
group_shop_priest = "Priest Shop Upgrades"
group_shop_sorcerer = "Sorcerer Shop Upgrades"

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
        # trap_flies,
    },
    group_buttons: {
        btn_pof,
        btn_c3_puzzle,
        btn_c2_puzzle,
        btn_c1_puzzle_e,
        btn_c1_puzzle_w,
        btn_p_puzzle,
        btn_t1_puzzle_w,
        btn_t1_puzzle_e,
        btn_t2_puzzle_w,
        btn_t2_puzzle_e,
        btn_t2_puzzle_n,
        btn_t2_puzzle_s,
        btn_t3_puzzle,
        btn_pof_puzzle,
        btn_c3_fall_bridge,
        btn_c3_e_bridge,
        btn_c2_red,
        btn_c2_green,
        btn_c2_bridges,
        btn_c2_s_bridge,
        btn_c2_pumps,
        btn_c1_blue,
        btn_c1_red,
        btn_c1_green,
        btn_c1_tunnel,
        btn_b1_bridge,
        btn_t1_jail_n,
        btn_t1_jail_e,
        btn_t1_telarian,
        btn_t1_guard,
        btn_t1_hall,
        btn_t1_runway,
        btn_t2_blue,
        btn_t2_light_bridges,
        btn_t2_jones_hall_back,
        btn_t2_jones_hall,
        btn_t2_nw_gate,
        btn_t2_t3_gate_w,
        btn_t2_t3_gate_e,
        btn_t2_boulder_passage,
        btn_t2_ice_gate_w,
        btn_t2_ice_gate_e,
        btn_t2_boulder_room,
        btn_t2_portal,
        btn_t2_jail_e,
        btn_t2_jail_w,
        btn_t2_jail_s,
        btn_t2_s_gate_shortcut,
        btn_t2_s_gate_hall,
        btn_t2_s_spikes,
        btn_t2_portal_gate,
        btn_t3_gold_chutes,
        btn_t3_fall_1,
        btn_t3_fall_2,
        btn_t3_fall_3,
        btn_t3_pillars,
        btn_t3_gate_s,
        btn_pof_1_walls_s,
        btn_pof_1_exit,
        btn_pof_2_puzzle,
        btn_pof_2_exit,
        btn_pof_3_start,
    },
    group_b1_boss: {
        btnc_b1_rune_1,
        btnc_b1_rune_2,
        btnc_b1_rune_3,
    },
    group_b2_boss: {
        btnc_b2_rune_1,
        btnc_b2_rune_2,
        btnc_b2_rune_3,
    },
    group_b3_boss: {
        btnc_b3_rune_1,
        btnc_b3_rune_2,
        btnc_b3_rune_3,
    },
    group_b4_boss: {
        btnc_b4_rune_1,
        btnc_b4_rune_2,
        btnc_b4_rune_3,
    },
    group_shop_items: {
        *class_shop_upgrades[util.PlayerClass.Paladin],
        *class_shop_upgrades[util.PlayerClass.Wizard],
        *class_shop_upgrades[util.PlayerClass.Ranger],
        *class_shop_upgrades[util.PlayerClass.Warlock],
        *class_shop_upgrades[util.PlayerClass.Thief],
        *class_shop_upgrades[util.PlayerClass.Priest],
        *class_shop_upgrades[util.PlayerClass.Sorcerer],
    },
    group_shop_paladin: {
        *class_shop_upgrades[util.PlayerClass.Paladin]
    },
    group_shop_wizard: {
        *class_shop_upgrades[util.PlayerClass.Wizard]
    },
    group_shop_ranger: {
        *class_shop_upgrades[util.PlayerClass.Ranger]
    },
    group_shop_warlock: {
        *class_shop_upgrades[util.PlayerClass.Warlock]
    },
    group_shop_thief: {
        *class_shop_upgrades[util.PlayerClass.Thief]
    },
    group_shop_priest: {
        *class_shop_upgrades[util.PlayerClass.Priest]
    },
    group_shop_sorcerer: {
        *class_shop_upgrades[util.PlayerClass.Sorcerer]
    },
}
