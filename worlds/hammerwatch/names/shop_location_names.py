# Shop location names
import typing
from . import option_names
from .. import util

vitality_shop_location_count = [2, 2, 3, 3, 3]
combo_shop_location_count = [5, 4, 4, 4, 4]

shop_class_base_location_names: typing.Dict[util.PlayerClass, typing.Dict[util.ShopType, typing.List[int]]] = {
    util.PlayerClass.Paladin: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 5, 6, 4],
            util.ShopType.Defense: [3, 4, 4, 2, 2],
        },
    util.PlayerClass.Ranger: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 5, 6, 5],
            util.ShopType.Defense: [2, 3, 3, 4, 3],
        },
    util.PlayerClass.Wizard: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 7, 7, 7],
            util.ShopType.Defense: [2, 2, 3, 3, 2],
        },
    util.PlayerClass.Warlock: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 5, 6, 7, 6],
            util.ShopType.Defense: [2, 3, 4, 4, 2],
        },
    util.PlayerClass.Thief: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 5, 5, 5, 1],
            util.ShopType.Defense: [2, 4, 5, 4, 3],
        },
    util.PlayerClass.Priest: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 5, 6, 6, 5],
            util.ShopType.Defense: [3, 3, 5, 4, 4],
        },
    util.PlayerClass.Sorcerer: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 7, 7, 7],
            util.ShopType.Defense: [2, 3, 4, 3, 2],
        },
}
shop_class_location_names: typing.Dict[util.PlayerClass, typing.Dict[util.ShopType, typing.List[typing.List[str]]]] = {}
for _player_class, shop_type_locs in shop_class_base_location_names.items():
    shop_class_location_names[_player_class] = {}
    for shop_type, shop_counts in shop_type_locs.items():
        shop_class_location_names[_player_class][shop_type] = []
        for level, shop_level_count in enumerate(shop_counts, start=1):
            shop_class_location_names[_player_class][shop_type].append([
                f"{_player_class.name} {shop_type.name} {level} Shop Item {i}" for i in range(1, shop_level_count+1)
            ])
# for player_class, shop_types in shop_class_base_location_names.items():
#     total_shops = 0
#     for shop_type in shop_types:
#         total_shops += sum(shop_types[shop_type])
#     print(f"{player_class.name} {total_shops}")

# Get rid of all the rest of this
shop_health_1 = "Health Pool 1"
shop_health_2 = "Health Pool 2"
shop_health_3 = "Health Pool 3"
shop_health_4 = "Health Pool 4"
shop_health_5 = "Health Pool 5"
shop_mana_1 = "Mana Pool 1"
shop_mana_2 = "Mana Pool 2"
shop_mana_3 = "Mana Pool 3"
shop_mana_4 = "Mana Pool 4"
shop_mana_5 = "Mana Pool 5"
shop_armor_1 = "Armor 1"
shop_armor_2 = "Armor 2"
shop_armor_3 = "Armor 3"
shop_armor_4 = "Armor 4"
shop_armor_5 = "Armor 5"
shop_speed_1 = "Move Speed 1"
shop_speed_2 = "Move Speed 2"
shop_speed_3 = "Move Speed 3"
shop_combo = "Combo"
shop_combo_timer_1 = "Combo Timer 1"
shop_combo_timer_2 = "Combo Timer 2"
shop_combo_timer_3 = "Combo Timer 3"
shop_combo_timer_4 = "Combo Timer 4"
shop_combo_timer_5 = "Combo Timer 5"
shop_combo_nova_1 = "Combo Nova 1"
shop_combo_nova_2 = "Combo Nova 2"
shop_combo_nova_3 = "Combo Nova 3"
shop_combo_nova_4 = "Combo Nova 4"
shop_combo_nova_5 = "Combo Nova 5"
shop_combo_healing_1 = "Combo Healing 1"
shop_combo_healing_2 = "Combo Healing 2"
shop_combo_healing_3 = "Combo Healing 3"
shop_combo_healing_4 = "Combo Healing 4"
shop_combo_healing_5 = "Combo Healing 5"
shop_combo_mana_1 = "Combo Mana 1"
shop_combo_mana_2 = "Combo Mana 2"
shop_combo_mana_3 = "Combo Mana 3"
shop_combo_mana_4 = "Combo Mana 4"
shop_combo_mana_5 = "Combo Mana 5"

shop_paladin_health_1 = f"Paladin {shop_health_1}"
shop_paladin_health_2 = f"Paladin {shop_health_2}"
shop_paladin_health_3 = f"Paladin {shop_health_3}"
shop_paladin_health_4 = f"Paladin {shop_health_4}"
shop_paladin_health_5 = f"Paladin {shop_health_5}"
shop_paladin_mana_1 = f"Paladin {shop_mana_1}"
shop_paladin_mana_2 = f"Paladin {shop_mana_2}"
shop_paladin_mana_3 = f"Paladin {shop_mana_3}"
shop_paladin_mana_4 = f"Paladin {shop_mana_4}"
shop_paladin_mana_5 = f"Paladin {shop_mana_5}"
shop_paladin_armor_1 = f"Paladin {shop_armor_1}"
shop_paladin_armor_2 = f"Paladin {shop_armor_2}"
shop_paladin_armor_3 = f"Paladin {shop_armor_3}"
shop_paladin_armor_4 = f"Paladin {shop_armor_4}"
shop_paladin_armor_5 = f"Paladin {shop_armor_5}"
shop_paladin_speed_1 = f"Paladin {shop_speed_1}"
shop_paladin_speed_2 = f"Paladin {shop_speed_2}"
shop_paladin_speed_3 = f"Paladin {shop_speed_3}"
shop_paladin_combo = f"Paladin {shop_combo}"
shop_paladin_combo_timer_1 = f"Paladin {shop_combo_timer_1}"
shop_paladin_combo_timer_2 = f"Paladin {shop_combo_timer_2}"
shop_paladin_combo_timer_3 = f"Paladin {shop_combo_timer_3}"
shop_paladin_combo_timer_4 = f"Paladin {shop_combo_timer_4}"
shop_paladin_combo_timer_5 = f"Paladin {shop_combo_timer_5}"
shop_paladin_combo_nova_1 = f"Paladin {shop_combo_nova_1}"
shop_paladin_combo_nova_2 = f"Paladin {shop_combo_nova_2}"
shop_paladin_combo_nova_3 = f"Paladin {shop_combo_nova_3}"
shop_paladin_combo_nova_4 = f"Paladin {shop_combo_nova_4}"
shop_paladin_combo_nova_5 = f"Paladin {shop_combo_nova_5}"
shop_paladin_combo_healing_1 = f"Paladin {shop_combo_healing_1}"
shop_paladin_combo_healing_2 = f"Paladin {shop_combo_healing_2}"
shop_paladin_combo_healing_3 = f"Paladin {shop_combo_healing_3}"
shop_paladin_combo_healing_4 = f"Paladin {shop_combo_healing_4}"
shop_paladin_combo_healing_5 = f"Paladin {shop_combo_healing_5}"
shop_paladin_combo_mana_1 = f"Paladin {shop_combo_mana_1}"
shop_paladin_combo_mana_2 = f"Paladin {shop_combo_mana_2}"
shop_paladin_combo_mana_3 = f"Paladin {shop_combo_mana_3}"
shop_paladin_combo_mana_4 = f"Paladin {shop_combo_mana_4}"
shop_paladin_combo_mana_5 = f"Paladin {shop_combo_mana_5}"

shop_paladin_damage_1 = "Paladin Sword Damage 1"
shop_paladin_damage_2 = "Paladin Sword Damage 2"
shop_paladin_damage_3 = "Paladin Sword Damage 3"
shop_paladin_damage_4 = "Paladin Sword Damage 4"
shop_paladin_damage_5 = "Paladin Sword Damage 5"
shop_paladin_charge_damage_1 = "Paladin Charge Damage 1"
shop_paladin_charge_damage_2 = "Paladin Charge Damage 2"
shop_paladin_charge_damage_3 = "Paladin Charge Damage 3"
shop_paladin_charge_range_1 = "Paladin Charge Range 1"
shop_paladin_charge_range_2 = "Paladin Charge Range 2"
shop_paladin_charge_range_3 = "Paladin Charge Range 3"
shop_paladin_healing = "Paladin Healing"
shop_paladin_healing_efficiency_1 = "Paladin Healing Efficiency 1"
shop_paladin_healing_efficiency_2 = "Paladin Healing Efficiency 2"
shop_paladin_healing_efficiency_3 = "Paladin Healing Efficiency 3"
shop_paladin_holy_storm = "Paladin Holy Storm"
shop_paladin_holy_storm_damage_1 = "Paladin Holy Storm Damage 1"
shop_paladin_holy_storm_damage_2 = "Paladin Holy Storm Damage 2"
shop_paladin_holy_storm_duration_1 = "Paladin Holy Storm Duration 1"
shop_paladin_holy_storm_duration_2 = "Paladin Holy Storm Duration 2"
shop_paladin_divine_wrath_1 = "Paladin Divine Wrath 1"
shop_paladin_divine_wrath_2 = "Paladin Divine Wrath 2"
shop_paladin_divine_wrath_3 = "Paladin Divine Wrath 3"
shop_paladin_sword_arc_1 = "Paladin Sword Arc 1"
shop_paladin_sword_arc_2 = "Paladin Sword Arc 2"
shop_paladin_sword_arc_3 = "Paladin Sword Arc 3"
shop_paladin_sword_arc_4 = "Paladin Sword Arc 4"
shop_paladin_sword_arc_5 = "Paladin Sword Arc 5"
shop_paladin_shield_1 = "Paladin Shield 1"
shop_paladin_shield_2 = "Paladin Shield 2"
shop_paladin_shield_3 = "Paladin Shield 3"

shop_ranger_health_1 = f"Ranger {shop_health_1}"
shop_ranger_health_2 = f"Ranger {shop_health_2}"
shop_ranger_health_3 = f"Ranger {shop_health_3}"
shop_ranger_health_4 = f"Ranger {shop_health_4}"
shop_ranger_health_5 = f"Ranger {shop_health_5}"
shop_ranger_mana_1 = f"Ranger {shop_mana_1}"
shop_ranger_mana_2 = f"Ranger {shop_mana_2}"
shop_ranger_mana_3 = f"Ranger {shop_mana_3}"
shop_ranger_mana_4 = f"Ranger {shop_mana_4}"
shop_ranger_mana_5 = f"Ranger {shop_mana_5}"
shop_ranger_armor_1 = f"Ranger {shop_armor_1}"
shop_ranger_armor_2 = f"Ranger {shop_armor_2}"
shop_ranger_armor_3 = f"Ranger {shop_armor_3}"
shop_ranger_armor_4 = f"Ranger {shop_armor_4}"
shop_ranger_armor_5 = f"Ranger {shop_armor_5}"
shop_ranger_speed_1 = f"Ranger {shop_speed_1}"
shop_ranger_speed_2 = f"Ranger {shop_speed_2}"
shop_ranger_speed_3 = f"Ranger {shop_speed_3}"
shop_ranger_combo = f"Ranger {shop_combo}"
shop_ranger_combo_timer_1 = f"Ranger {shop_combo_timer_1}"
shop_ranger_combo_timer_2 = f"Ranger {shop_combo_timer_2}"
shop_ranger_combo_timer_3 = f"Ranger {shop_combo_timer_3}"
shop_ranger_combo_timer_4 = f"Ranger {shop_combo_timer_4}"
shop_ranger_combo_timer_5 = f"Ranger {shop_combo_timer_5}"
shop_ranger_combo_nova_1 = f"Ranger {shop_combo_nova_1}"
shop_ranger_combo_nova_2 = f"Ranger {shop_combo_nova_2}"
shop_ranger_combo_nova_3 = f"Ranger {shop_combo_nova_3}"
shop_ranger_combo_nova_4 = f"Ranger {shop_combo_nova_4}"
shop_ranger_combo_nova_5 = f"Ranger {shop_combo_nova_5}"
shop_ranger_combo_healing_1 = f"Ranger {shop_combo_healing_1}"
shop_ranger_combo_healing_2 = f"Ranger {shop_combo_healing_2}"
shop_ranger_combo_healing_3 = f"Ranger {shop_combo_healing_3}"
shop_ranger_combo_healing_4 = f"Ranger {shop_combo_healing_4}"
shop_ranger_combo_healing_5 = f"Ranger {shop_combo_healing_5}"
shop_ranger_combo_mana_1 = f"Ranger {shop_combo_mana_1}"
shop_ranger_combo_mana_2 = f"Ranger {shop_combo_mana_2}"
shop_ranger_combo_mana_3 = f"Ranger {shop_combo_mana_3}"
shop_ranger_combo_mana_4 = f"Ranger {shop_combo_mana_4}"
shop_ranger_combo_mana_5 = f"Ranger {shop_combo_mana_5}"

shop_ranger_bow_damage_1 = "Ranger Bow Damage 1"
shop_ranger_bow_damage_2 = "Ranger Bow Damage 2"
shop_ranger_bow_damage_3 = "Ranger Bow Damage 3"
shop_ranger_bow_damage_4 = "Ranger Bow Damage 4"
shop_ranger_bow_damage_5 = "Ranger Bow Damage 5"
shop_ranger_penetration_1 = "Ranger Penetration 1"
shop_ranger_penetration_2 = "Ranger Penetration 2"
shop_ranger_penetration_3 = "Ranger Penetration 3"
shop_ranger_penetration_4 = "Ranger Penetration 4"
shop_ranger_penetration_5 = "Ranger Penetration 5"
shop_ranger_bomb_damage_1 = "Ranger Bomb Damage 1"
shop_ranger_bomb_damage_2 = "Ranger Bomb Damage 2"
shop_ranger_bomb_damage_3 = "Ranger Bomb Damage 3"
shop_ranger_overgrowth = "Ranger Overgrowth"
shop_ranger_overgrowth_duration_1 = "Ranger Overgrowth Duration 1"
shop_ranger_overgrowth_duration_2 = "Ranger Overgrowth Duration 2"
shop_ranger_overgrowth_range_1 = "Ranger Overgrowth Range 1"
shop_ranger_overgrowth_range_2 = "Ranger Overgrowth Range 2"
shop_ranger_flurry = "Ranger Flurry"
shop_ranger_flurry_waves_1 = "Ranger Flurry Waves 1"
shop_ranger_flurry_waves_2 = "Ranger Flurry Waves 2"
shop_ranger_flurry_arrows_1 = "Ranger Flurry Arrows 1"
shop_ranger_flurry_arrows_2 = "Ranger Flurry Arrows 2"
shop_ranger_dodge_1 = "Ranger Dodge 1"
shop_ranger_dodge_2 = "Ranger Dodge 2"
shop_ranger_dodge_3 = "Ranger Dodge 3"
shop_ranger_dodge_4 = "Ranger Dodge 4"
shop_ranger_dodge_5 = "Ranger Dodge 5"
shop_ranger_marksmanship_1 = "Ranger Marksmanship 1"
shop_ranger_marksmanship_2 = "Ranger Marksmanship 2"
shop_ranger_marksmanship_3 = "Ranger Marksmanship 3"
shop_ranger_marksmanship_4 = "Ranger Marksmanship 4"

shop_wizard_health_1 = f"Wizard {shop_health_1}"
shop_wizard_health_2 = f"Wizard {shop_health_2}"
shop_wizard_health_3 = f"Wizard {shop_health_3}"
shop_wizard_health_4 = f"Wizard {shop_health_4}"
shop_wizard_health_5 = f"Wizard {shop_health_5}"
shop_wizard_mana_1 = f"Wizard {shop_mana_1}"
shop_wizard_mana_2 = f"Wizard {shop_mana_2}"
shop_wizard_mana_3 = f"Wizard {shop_mana_3}"
shop_wizard_mana_4 = f"Wizard {shop_mana_4}"
shop_wizard_mana_5 = f"Wizard {shop_mana_5}"
shop_wizard_armor_1 = f"Wizard {shop_armor_1}"
shop_wizard_armor_2 = f"Wizard {shop_armor_2}"
shop_wizard_armor_3 = f"Wizard {shop_armor_3}"
shop_wizard_armor_4 = f"Wizard {shop_armor_4}"
shop_wizard_speed_1 = f"Wizard {shop_speed_1}"
shop_wizard_speed_2 = f"Wizard {shop_speed_2}"
shop_wizard_speed_3 = f"Wizard {shop_speed_3}"
shop_wizard_combo = f"Wizard {shop_combo}"
shop_wizard_combo_timer_1 = f"Wizard {shop_combo_timer_1}"
shop_wizard_combo_timer_2 = f"Wizard {shop_combo_timer_2}"
shop_wizard_combo_timer_3 = f"Wizard {shop_combo_timer_3}"
shop_wizard_combo_timer_4 = f"Wizard {shop_combo_timer_4}"
shop_wizard_combo_timer_5 = f"Wizard {shop_combo_timer_5}"
shop_wizard_combo_nova_1 = f"Wizard {shop_combo_nova_1}"
shop_wizard_combo_nova_2 = f"Wizard {shop_combo_nova_2}"
shop_wizard_combo_nova_3 = f"Wizard {shop_combo_nova_3}"
shop_wizard_combo_nova_4 = f"Wizard {shop_combo_nova_4}"
shop_wizard_combo_nova_5 = f"Wizard {shop_combo_nova_5}"
shop_wizard_combo_healing_1 = f"Wizard {shop_combo_healing_1}"
shop_wizard_combo_healing_2 = f"Wizard {shop_combo_healing_2}"
shop_wizard_combo_healing_3 = f"Wizard {shop_combo_healing_3}"
shop_wizard_combo_healing_4 = f"Wizard {shop_combo_healing_4}"
shop_wizard_combo_healing_5 = f"Wizard {shop_combo_healing_5}"
shop_wizard_combo_mana_1 = f"Wizard {shop_combo_mana_1}"
shop_wizard_combo_mana_2 = f"Wizard {shop_combo_mana_2}"
shop_wizard_combo_mana_3 = f"Wizard {shop_combo_mana_3}"
shop_wizard_combo_mana_4 = f"Wizard {shop_combo_mana_4}"
shop_wizard_combo_mana_5 = f"Wizard {shop_combo_mana_5}"

shop_wizard_fireball_damage_1 = "Wizard Fireball Damage 1"
shop_wizard_fireball_damage_2 = "Wizard Fireball Damage 2"
shop_wizard_fireball_damage_3 = "Wizard Fireball Damage 3"
shop_wizard_fireball_damage_4 = "Wizard Fireball Damage 4"
shop_wizard_fireball_damage_5 = "Wizard Fireball Damage 5"
shop_wizard_fireball_range_1 = "Wizard Fireball Range 1"
shop_wizard_fireball_range_2 = "Wizard Fireball Range 2"
shop_wizard_fireball_range_3 = "Wizard Fireball Range 3"
shop_wizard_fireball_range_4 = "Wizard Fireball Range 4"
shop_wizard_fireball_range_5 = "Wizard Fireball Range 5"
shop_wizard_fire_breath_damage_1 = "Wizard Fire Breath Damage 1"
shop_wizard_fire_breath_damage_2 = "Wizard Fire Breath Damage 2"
shop_wizard_fire_breath_damage_3 = "Wizard Fire Breath Damage 3"
shop_wizard_fire_breath_damage_4 = "Wizard Fire Breath Damage 4"
shop_wizard_fire_nova = "Wizard Fire Nova"
shop_wizard_fire_nova_flames_1 = "Wizard Fire Nova Flames 1"
shop_wizard_fire_nova_flames_2 = "Wizard Fire Nova Flames 2"
shop_wizard_fire_nova_flames_3 = "Wizard Fire Nova Flames 3"
shop_wizard_fire_nova_slow_1 = "Wizard Fire Nova Slow 1"
shop_wizard_fire_nova_slow_2 = "Wizard Fire Nova Slow 2"
shop_wizard_fire_nova_slow_3 = "Wizard Fire Nova Slow 3"
shop_wizard_meteor_strike = "Wizard Meteor Strike"
shop_wizard_meteor_strike_damage_1 = "Wizard Meteor Strike Damage 1"
shop_wizard_meteor_strike_damage_2 = "Wizard Meteor Strike Damage 2"
shop_wizard_meteor_strike_meteors_1 = "Wizard Meteor Strike Meteors 1"
shop_wizard_meteor_strike_meteors_2 = "Wizard Meteor Strike Meteors 2"
shop_wizard_meteor_strike_meteors_3 = "Wizard Meteor Strike Meteors 3"
shop_wizard_fire_shield = "Wizard Fire Shield"
shop_wizard_combustion = "Wizard Combustion"
shop_wizard_combustion_damage_1 = "Wizard Combustion Damage 1"
shop_wizard_combustion_damage_2 = "Wizard Combustion Damage 2"
shop_wizard_combustion_damage_3 = "Wizard Combustion Damage 3"
shop_wizard_combustion_duration_1 = "Wizard Combustion Duration 1"
shop_wizard_combustion_duration_2 = "Wizard Combustion Duration 2"
shop_wizard_combustion_duration_3 = "Wizard Combustion Duration 3"

shop_warlock_health_1 = f"Warlock {shop_health_1}"
shop_warlock_health_2 = f"Warlock {shop_health_2}"
shop_warlock_health_3 = f"Warlock {shop_health_3}"
shop_warlock_health_4 = f"Warlock {shop_health_4}"
shop_warlock_health_5 = f"Warlock {shop_health_5}"
shop_warlock_mana_1 = f"Warlock {shop_mana_1}"
shop_warlock_mana_2 = f"Warlock {shop_mana_2}"
shop_warlock_mana_3 = f"Warlock {shop_mana_3}"
shop_warlock_mana_4 = f"Warlock {shop_mana_4}"
shop_warlock_mana_5 = f"Warlock {shop_mana_5}"
shop_warlock_armor_1 = f"Warlock {shop_armor_1}"
shop_warlock_armor_2 = f"Warlock {shop_armor_2}"
shop_warlock_armor_3 = f"Warlock {shop_armor_3}"
shop_warlock_armor_4 = f"Warlock {shop_armor_4}"
shop_warlock_armor_5 = f"Warlock {shop_armor_5}"
shop_warlock_speed_1 = f"Warlock {shop_speed_1}"
shop_warlock_speed_2 = f"Warlock {shop_speed_2}"
shop_warlock_speed_3 = f"Warlock {shop_speed_3}"
shop_warlock_combo = f"Warlock {shop_combo}"
shop_warlock_combo_timer_1 = f"Warlock {shop_combo_timer_1}"
shop_warlock_combo_timer_2 = f"Warlock {shop_combo_timer_2}"
shop_warlock_combo_timer_3 = f"Warlock {shop_combo_timer_3}"
shop_warlock_combo_timer_4 = f"Warlock {shop_combo_timer_4}"
shop_warlock_combo_timer_5 = f"Warlock {shop_combo_timer_5}"
shop_warlock_combo_nova_1 = f"Warlock {shop_combo_nova_1}"
shop_warlock_combo_nova_2 = f"Warlock {shop_combo_nova_2}"
shop_warlock_combo_nova_3 = f"Warlock {shop_combo_nova_3}"
shop_warlock_combo_nova_4 = f"Warlock {shop_combo_nova_4}"
shop_warlock_combo_nova_5 = f"Warlock {shop_combo_nova_5}"
shop_warlock_combo_healing_1 = f"Warlock {shop_combo_healing_1}"
shop_warlock_combo_healing_2 = f"Warlock {shop_combo_healing_2}"
shop_warlock_combo_healing_3 = f"Warlock {shop_combo_healing_3}"
shop_warlock_combo_healing_4 = f"Warlock {shop_combo_healing_4}"
shop_warlock_combo_healing_5 = f"Warlock {shop_combo_healing_5}"
shop_warlock_combo_mana_1 = f"Warlock {shop_combo_mana_1}"
shop_warlock_combo_mana_2 = f"Warlock {shop_combo_mana_2}"
shop_warlock_combo_mana_3 = f"Warlock {shop_combo_mana_3}"
shop_warlock_combo_mana_4 = f"Warlock {shop_combo_mana_4}"
shop_warlock_combo_mana_5 = f"Warlock {shop_combo_mana_5}"

shop_warlock_dagger_damage_1 = "Warlock Dagger Damage 1"
shop_warlock_dagger_damage_2 = "Warlock Dagger Damage 2"
shop_warlock_dagger_damage_3 = "Warlock Dagger Damage 3"
shop_warlock_dagger_damage_4 = "Warlock Dagger Damage 4"
shop_warlock_dagger_damage_5 = "Warlock Dagger Damage 5"
shop_warlock_dagger_poison_1 = "Warlock Dagger Poison 1"
shop_warlock_dagger_poison_2 = "Warlock Dagger Poison 2"
shop_warlock_dagger_poison_3 = "Warlock Dagger Poison 3"
shop_warlock_dagger_poison_4 = "Warlock Dagger Poison 4"
shop_warlock_dagger_poison_5 = "Warlock Dagger Poison 5"
shop_warlock_lightning_strike_damage_1 = "Warlock Lightning Strike Damage 1"
shop_warlock_lightning_strike_damage_2 = "Warlock Lightning Strike Damage 2"
shop_warlock_lightning_strike_damage_3 = "Warlock Lightning Strike Damage 3"
shop_warlock_lightning_strike_damage_4 = "Warlock Lightning Strike Damage 4"
shop_warlock_lightning_strike_targets_1 = "Warlock Lightning Strike Targets 1"
shop_warlock_lightning_strike_targets_2 = "Warlock Lightning Strike Targets 2"
shop_warlock_lightning_strike_targets_3 = "Warlock Lightning Strike Targets 3"
shop_warlock_lightning_strike_targets_4 = "Warlock Lightning Strike Targets 4"
shop_warlock_summon_gargoyle = "Warlock Summon Gargoyle"
shop_warlock_gargoyle_damage_1 = "Warlock Gargoyle Damage 1"
shop_warlock_gargoyle_damage_2 = "Warlock Gargoyle Damage 2"
shop_warlock_gargoyle_duration_1 = "Warlock Gargoyle Duration 1"
shop_warlock_gargoyle_duration_2 = "Warlock Gargoyle Duration 2"
shop_warlock_electrical_storm = "Warlock Electrical Storm"
shop_warlock_electrical_storm_damage_1 = "Warlock Electrical Storm Damage 1"
shop_warlock_electrical_storm_damage_2 = "Warlock Electrical Storm Damage 2"
shop_warlock_electrical_storm_duration_1 = "Warlock Electrical Storm Duration 1"
shop_warlock_electrical_storm_duration_2 = "Warlock Electrical Storm Duration 2"
shop_warlock_blood_sacrifice_1 = "Warlock Blood Sacrifice 1"
shop_warlock_blood_sacrifice_2 = "Warlock Blood Sacrifice 2"
shop_warlock_blood_sacrifice_3 = "Warlock Blood Sacrifice 3"
shop_warlock_blood_sacrifice_4 = "Warlock Blood Sacrifice 4"
shop_warlock_blood_sacrifice_5 = "Warlock Blood Sacrifice 5"
shop_warlock_soul_sacrifice_1 = "Warlock Soul Sacrifice 1"
shop_warlock_soul_sacrifice_2 = "Warlock Soul Sacrifice 2"
shop_warlock_soul_sacrifice_3 = "Warlock Soul Sacrifice 3"

shop_thief_health_1 = f"Thief {shop_health_1}"
shop_thief_health_2 = f"Thief {shop_health_2}"
shop_thief_health_3 = f"Thief {shop_health_3}"
shop_thief_health_4 = f"Thief {shop_health_4}"
shop_thief_health_5 = f"Thief {shop_health_5}"
shop_thief_mana_1 = f"Thief {shop_mana_1}"
shop_thief_mana_2 = f"Thief {shop_mana_2}"
shop_thief_mana_3 = f"Thief {shop_mana_3}"
shop_thief_mana_4 = f"Thief {shop_mana_4}"
shop_thief_mana_5 = f"Thief {shop_mana_5}"
shop_thief_armor_1 = f"Thief {shop_armor_1}"
shop_thief_armor_2 = f"Thief {shop_armor_2}"
shop_thief_armor_3 = f"Thief {shop_armor_3}"
shop_thief_armor_4 = f"Thief {shop_armor_4}"
shop_thief_armor_5 = f"Thief {shop_armor_5}"
shop_thief_speed_1 = f"Thief {shop_speed_1}"
shop_thief_speed_2 = f"Thief {shop_speed_2}"
shop_thief_speed_3 = f"Thief {shop_speed_3}"
shop_thief_combo = f"Thief {shop_combo}"
shop_thief_combo_timer_1 = f"Thief {shop_combo_timer_1}"
shop_thief_combo_timer_2 = f"Thief {shop_combo_timer_2}"
shop_thief_combo_timer_3 = f"Thief {shop_combo_timer_3}"
shop_thief_combo_timer_4 = f"Thief {shop_combo_timer_4}"
shop_thief_combo_timer_5 = f"Thief {shop_combo_timer_5}"
shop_thief_combo_nova_1 = f"Thief {shop_combo_nova_1}"
shop_thief_combo_nova_2 = f"Thief {shop_combo_nova_2}"
shop_thief_combo_nova_3 = f"Thief {shop_combo_nova_3}"
shop_thief_combo_nova_4 = f"Thief {shop_combo_nova_4}"
shop_thief_combo_nova_5 = f"Thief {shop_combo_nova_5}"
shop_thief_combo_healing_1 = f"Thief {shop_combo_healing_1}"
shop_thief_combo_healing_2 = f"Thief {shop_combo_healing_2}"
shop_thief_combo_healing_3 = f"Thief {shop_combo_healing_3}"
shop_thief_combo_healing_4 = f"Thief {shop_combo_healing_4}"
shop_thief_combo_healing_5 = f"Thief {shop_combo_healing_5}"
shop_thief_combo_mana_1 = f"Thief {shop_combo_mana_1}"
shop_thief_combo_mana_2 = f"Thief {shop_combo_mana_2}"
shop_thief_combo_mana_3 = f"Thief {shop_combo_mana_3}"
shop_thief_combo_mana_4 = f"Thief {shop_combo_mana_4}"
shop_thief_combo_mana_5 = f"Thief {shop_combo_mana_5}"

shop_thief_knives_damage_1 = "Thief Knives Damage 1"
shop_thief_knives_damage_2 = "Thief Knives Damage 2"
shop_thief_knives_damage_3 = "Thief Knives Damage 3"
shop_thief_knives_damage_4 = "Thief Knives Damage 4"
shop_thief_knives_damage_5 = "Thief Knives Damage 5"
shop_thief_knife_fan_damage_1 = "Thief Knife Fan Damage 1"
shop_thief_knife_fan_damage_2 = "Thief Knife Fan Damage 2"
shop_thief_knife_fan_damage_3 = "Thief Knife Fan Damage 3"
shop_thief_knife_fan_knives_1 = "Thief Knife Fan Knives 1"
shop_thief_knife_fan_knives_2 = "Thief Knife Fan Knives 2"
shop_thief_knife_fan_knives_3 = "Thief Knife Fan Knives 3"
shop_thief_grapple_chain = "Thief Grapple Chain"
shop_thief_grapple_chain_length_1 = "Thief Grapple Chain Length 1"
shop_thief_grapple_chain_length_2 = "Thief Grapple Chain Length 2"
shop_thief_grapple_chain_stun_1 = "Thief Grapple Chain Stun 1"
shop_thief_grapple_chain_stun_2 = "Thief Grapple Chain Stun 2"
shop_thief_smoke_bomb = "Thief Smoke Bomb"
shop_thief_smoke_bomb_range_1 = "Thief Smoke Bomb Range 1"
shop_thief_smoke_bomb_range_2 = "Thief Smoke Bomb Range 2"
shop_thief_fervor_1 = "Thief Fervor 1"
shop_thief_fervor_2 = "Thief Fervor 2"
shop_thief_fervor_3 = "Thief Fervor 3"
shop_thief_speed_penalty_1 = "Thief Speed Penalty 1"
shop_thief_speed_penalty_2 = "Thief Speed Penalty 2"
shop_thief_speed_penalty_3 = "Thief Speed Penalty 3"
shop_thief_speed_penalty_4 = "Thief Speed Penalty 4"
shop_thief_dodge_1 = "Thief Dodge 1"
shop_thief_dodge_2 = "Thief Dodge 2"
shop_thief_dodge_3 = "Thief Dodge 3"
shop_thief_dodge_4 = "Thief Dodge 4"
shop_thief_dodge_5 = "Thief Dodge 5"

shop_priest_health_1 = f"Priest {shop_health_1}"
shop_priest_health_2 = f"Priest {shop_health_2}"
shop_priest_health_3 = f"Priest {shop_health_3}"
shop_priest_health_4 = f"Priest {shop_health_4}"
shop_priest_health_5 = f"Priest {shop_health_5}"
shop_priest_mana_1 = f"Priest {shop_mana_1}"
shop_priest_mana_2 = f"Priest {shop_mana_2}"
shop_priest_mana_3 = f"Priest {shop_mana_3}"
shop_priest_mana_4 = f"Priest {shop_mana_4}"
shop_priest_mana_5 = f"Priest {shop_mana_5}"
shop_priest_armor_1 = f"Priest {shop_armor_1}"
shop_priest_armor_2 = f"Priest {shop_armor_2}"
shop_priest_armor_3 = f"Priest {shop_armor_3}"
shop_priest_armor_4 = f"Priest {shop_armor_4}"
shop_priest_armor_5 = f"Priest {shop_armor_5}"
shop_priest_speed_1 = f"Priest {shop_speed_1}"
shop_priest_speed_2 = f"Priest {shop_speed_2}"
shop_priest_speed_3 = f"Priest {shop_speed_3}"
shop_priest_combo = f"Priest {shop_combo}"
shop_priest_combo_timer_1 = f"Priest {shop_combo_timer_1}"
shop_priest_combo_timer_2 = f"Priest {shop_combo_timer_2}"
shop_priest_combo_timer_3 = f"Priest {shop_combo_timer_3}"
shop_priest_combo_timer_4 = f"Priest {shop_combo_timer_4}"
shop_priest_combo_timer_5 = f"Priest {shop_combo_timer_5}"
shop_priest_combo_nova_1 = f"Priest {shop_combo_nova_1}"
shop_priest_combo_nova_2 = f"Priest {shop_combo_nova_2}"
shop_priest_combo_nova_3 = f"Priest {shop_combo_nova_3}"
shop_priest_combo_nova_4 = f"Priest {shop_combo_nova_4}"
shop_priest_combo_nova_5 = f"Priest {shop_combo_nova_5}"
shop_priest_combo_healing_1 = f"Priest {shop_combo_healing_1}"
shop_priest_combo_healing_2 = f"Priest {shop_combo_healing_2}"
shop_priest_combo_healing_3 = f"Priest {shop_combo_healing_3}"
shop_priest_combo_healing_4 = f"Priest {shop_combo_healing_4}"
shop_priest_combo_healing_5 = f"Priest {shop_combo_healing_5}"
shop_priest_combo_mana_1 = f"Priest {shop_combo_mana_1}"
shop_priest_combo_mana_2 = f"Priest {shop_combo_mana_2}"
shop_priest_combo_mana_3 = f"Priest {shop_combo_mana_3}"
shop_priest_combo_mana_4 = f"Priest {shop_combo_mana_4}"
shop_priest_combo_mana_5 = f"Priest {shop_combo_mana_5}"

shop_priest_smite_damage_1 = "Priest Smite Damage 1"
shop_priest_smite_damage_2 = "Priest Smite Damage 2"
shop_priest_smite_damage_3 = "Priest Smite Damage 3"
shop_priest_smite_damage_4 = "Priest Smite Damage 4"
shop_priest_smite_damage_5 = "Priest Smite Damage 5"
shop_priest_speed_penalty_1 = "Priest Speed Penalty 1"
shop_priest_speed_penalty_2 = "Priest Speed Penalty 2"
shop_priest_speed_penalty_3 = "Priest Speed Penalty 3"
shop_priest_speed_penalty_4 = "Priest Speed Penalty 4"
shop_priest_speed_penalty_5 = "Priest Speed Penalty 5"
shop_priest_holy_beam_damage_1 = "Priest Holy Beam Damage 1"
shop_priest_holy_beam_damage_2 = "Priest Holy Beam Damage 2"
shop_priest_holy_beam_damage_3 = "Priest Holy Beam Damage 3"
shop_priest_holy_beam_damage_4 = "Priest Holy Beam Damage 4"
shop_priest_holy_beam_range_1 = "Priest Holy Beam Range 1"
shop_priest_holy_beam_range_2 = "Priest Holy Beam Range 2"
shop_priest_holy_beam_range_3 = "Priest Holy Beam Range 3"
shop_priest_holy_beam_range_4 = "Priest Holy Beam Range 4"
shop_priest_draining_field = "Priest Draining Field"
shop_priest_draining_field_damage_1 = "Priest Draining Field Damage 1"
shop_priest_draining_field_damage_2 = "Priest Draining Field Damage 2"
shop_priest_draining_field_damage_3 = "Priest Draining Field Damage 3"
shop_priest_draining_field_number_1 = "Priest Draining Field Number 1"
shop_priest_draining_field_number_2 = "Priest Draining Field Number 2"
shop_priest_cripple_aura = "Priest Cripple Aura"
shop_priest_cripple_aura_slow_1 = "Priest Cripple Aura Slow 1"
shop_priest_cripple_aura_slow_2 = "Priest Cripple Aura Slow 2"
shop_priest_cripple_aura_mana_drain = "Priest Cripple Aura Mana Drain"
shop_priest_hp_regen_1 = "Priest HP Regen 1"
shop_priest_hp_regen_2 = "Priest HP Regen 2"
shop_priest_hp_regen_3 = "Priest HP Regen 3"
shop_priest_hp_regen_4 = "Priest HP Regen 4"
shop_priest_hp_regen_5 = "Priest HP Regen 5"
shop_priest_magic_shield_1 = "Priest Magic Shield 1"
shop_priest_magic_shield_2 = "Priest Magic Shield 2"
shop_priest_magic_shield_3 = "Priest Magic Shield 3"
shop_priest_magic_shield_4 = "Priest Magic Shield 4"
shop_priest_magic_shield_5 = "Priest Magic Shield 5"

shop_sorcerer_health_1 = f"Sorcerer {shop_health_1}"
shop_sorcerer_health_2 = f"Sorcerer {shop_health_2}"
shop_sorcerer_health_3 = f"Sorcerer {shop_health_3}"
shop_sorcerer_health_4 = f"Sorcerer {shop_health_4}"
shop_sorcerer_health_5 = f"Sorcerer {shop_health_5}"
shop_sorcerer_mana_1 = f"Sorcerer {shop_mana_1}"
shop_sorcerer_mana_2 = f"Sorcerer {shop_mana_2}"
shop_sorcerer_mana_3 = f"Sorcerer {shop_mana_3}"
shop_sorcerer_mana_4 = f"Sorcerer {shop_mana_4}"
shop_sorcerer_mana_5 = f"Sorcerer {shop_mana_5}"
shop_sorcerer_armor_1 = f"Sorcerer {shop_armor_1}"
shop_sorcerer_armor_2 = f"Sorcerer {shop_armor_2}"
shop_sorcerer_armor_3 = f"Sorcerer {shop_armor_3}"
shop_sorcerer_armor_4 = f"Sorcerer {shop_armor_4}"
shop_sorcerer_speed_1 = f"Sorcerer {shop_speed_1}"
shop_sorcerer_speed_2 = f"Sorcerer {shop_speed_2}"
shop_sorcerer_speed_3 = f"Sorcerer {shop_speed_3}"
shop_sorcerer_combo = f"Sorcerer {shop_combo}"
shop_sorcerer_combo_timer_1 = f"Sorcerer {shop_combo_timer_1}"
shop_sorcerer_combo_timer_2 = f"Sorcerer {shop_combo_timer_2}"
shop_sorcerer_combo_timer_3 = f"Sorcerer {shop_combo_timer_3}"
shop_sorcerer_combo_timer_4 = f"Sorcerer {shop_combo_timer_4}"
shop_sorcerer_combo_timer_5 = f"Sorcerer {shop_combo_timer_5}"
shop_sorcerer_combo_nova_1 = f"Sorcerer {shop_combo_nova_1}"
shop_sorcerer_combo_nova_2 = f"Sorcerer {shop_combo_nova_2}"
shop_sorcerer_combo_nova_3 = f"Sorcerer {shop_combo_nova_3}"
shop_sorcerer_combo_nova_4 = f"Sorcerer {shop_combo_nova_4}"
shop_sorcerer_combo_nova_5 = f"Sorcerer {shop_combo_nova_5}"
shop_sorcerer_combo_healing_1 = f"Sorcerer {shop_combo_healing_1}"
shop_sorcerer_combo_healing_2 = f"Sorcerer {shop_combo_healing_2}"
shop_sorcerer_combo_healing_3 = f"Sorcerer {shop_combo_healing_3}"
shop_sorcerer_combo_healing_4 = f"Sorcerer {shop_combo_healing_4}"
shop_sorcerer_combo_healing_5 = f"Sorcerer {shop_combo_healing_5}"
shop_sorcerer_combo_mana_1 = f"Sorcerer {shop_combo_mana_1}"
shop_sorcerer_combo_mana_2 = f"Sorcerer {shop_combo_mana_2}"
shop_sorcerer_combo_mana_3 = f"Sorcerer {shop_combo_mana_3}"
shop_sorcerer_combo_mana_4 = f"Sorcerer {shop_combo_mana_4}"
shop_sorcerer_combo_mana_5 = f"Sorcerer {shop_combo_mana_5}"

shop_sorcerer_ice_shard_damage_1 = "Sorcerer Ice Shard Damage 1"
shop_sorcerer_ice_shard_damage_2 = "Sorcerer Ice Shard Damage 2"
shop_sorcerer_ice_shard_damage_3 = "Sorcerer Ice Shard Damage 3"
shop_sorcerer_ice_shard_damage_4 = "Sorcerer Ice Shard Damage 4"
shop_sorcerer_ice_shard_damage_5 = "Sorcerer Ice Shard Damage 5"
shop_sorcerer_ice_shard_bounces_1 = "Sorcerer Ice Shard Bounces 1"
shop_sorcerer_ice_shard_bounces_2 = "Sorcerer Ice Shard Bounces 2"
shop_sorcerer_ice_shard_bounces_3 = "Sorcerer Ice Shard Bounces 3"
shop_sorcerer_ice_shard_bounces_4 = "Sorcerer Ice Shard Bounces 4"
shop_sorcerer_ice_shard_bounces_5 = "Sorcerer Ice Shard Bounces 5"
shop_sorcerer_comet_damage_1 = "Sorcerer Comet Damage 1"
shop_sorcerer_comet_damage_2 = "Sorcerer Comet Damage 2"
shop_sorcerer_comet_damage_3 = "Sorcerer Comet Damage 3"
shop_sorcerer_comet_damage_4 = "Sorcerer Comet Damage 4"
shop_sorcerer_ice_shard_nova = "Sorcerer Ice Shard Nova"
shop_sorcerer_ice_shard_nova_number_1 = "Sorcerer Ice Shard Nova Number 1"
shop_sorcerer_ice_shard_nova_number_2 = "Sorcerer Ice Shard Nova Number 2"
shop_sorcerer_ice_shard_nova_mana_1 = "Sorcerer Ice Shard Nova Mana 1"
shop_sorcerer_ice_shard_nova_mana_2 = "Sorcerer Ice Shard Nova Mana 2"
shop_sorcerer_ice_orb = "Sorcerer Ice Orb"
shop_sorcerer_ice_orb_damage_1 = "Sorcerer Ice Orb Damage 1"
shop_sorcerer_ice_orb_damage_2 = "Sorcerer Ice Orb Damage 2"
shop_sorcerer_ice_orb_time_1 = "Sorcerer Ice Orb Time 1"
shop_sorcerer_ice_orb_time_2 = "Sorcerer Ice Orb Time 2"
shop_sorcerer_ice_orb_time_3 = "Sorcerer Ice Orb Time 3"
shop_sorcerer_chill = "Sorcerer Chill"
shop_sorcerer_chill_slow_1 = "Sorcerer Chill Slow 1"
shop_sorcerer_chill_slow_2 = "Sorcerer Chill Slow 2"
shop_sorcerer_chill_slow_3 = "Sorcerer Chill Slow 3"
shop_sorcerer_chill_duration_1 = "Sorcerer Chill Duration 1"
shop_sorcerer_chill_duration_2 = "Sorcerer Chill Duration 2"
shop_sorcerer_chill_duration_3 = "Sorcerer Chill Duration 3"
shop_sorcerer_frost_shield_1 = "Sorcerer Frost Shield 1"
shop_sorcerer_frost_shield_2 = "Sorcerer Frost Shield 2"
shop_sorcerer_frost_shield_3 = "Sorcerer Frost Shield 3"
shop_sorcerer_frost_shield_4 = "Sorcerer Frost Shield 4"
shop_sorcerer_frost_shield_5 = "Sorcerer Frost Shield 5"

class_shop_locations: typing.Dict[util.PlayerClass, typing.List[str]] = {
    util.PlayerClass.Paladin: [
        shop_paladin_damage_1,
        shop_paladin_damage_2,
        shop_paladin_damage_3,
        shop_paladin_damage_4,
        shop_paladin_damage_5,
        shop_paladin_charge_damage_1,
        shop_paladin_charge_damage_2,
        shop_paladin_charge_damage_3,
        shop_paladin_charge_range_1,
        shop_paladin_charge_range_2,
        shop_paladin_charge_range_3,
        shop_paladin_healing,
        shop_paladin_healing_efficiency_1,
        shop_paladin_healing_efficiency_2,
        shop_paladin_healing_efficiency_3,
        shop_paladin_holy_storm,
        shop_paladin_holy_storm_damage_1,
        shop_paladin_holy_storm_damage_2,
        shop_paladin_holy_storm_duration_1,
        shop_paladin_holy_storm_duration_2,
        shop_paladin_divine_wrath_1,
        shop_paladin_divine_wrath_2,
        shop_paladin_divine_wrath_3,
        shop_paladin_sword_arc_1,
        shop_paladin_sword_arc_2,
        shop_paladin_sword_arc_3,
        shop_paladin_sword_arc_4,
        shop_paladin_sword_arc_5,
        shop_paladin_shield_1,
        shop_paladin_shield_2,
        shop_paladin_shield_3,
    ],
    util.PlayerClass.Ranger: [
        shop_ranger_bow_damage_1,
        shop_ranger_bow_damage_2,
        shop_ranger_bow_damage_3,
        shop_ranger_bow_damage_4,
        shop_ranger_bow_damage_5,
        shop_ranger_penetration_1,
        shop_ranger_penetration_2,
        shop_ranger_penetration_3,
        shop_ranger_penetration_4,
        shop_ranger_penetration_5,
        shop_ranger_bomb_damage_1,
        shop_ranger_bomb_damage_2,
        shop_ranger_bomb_damage_3,
        shop_ranger_overgrowth,
        shop_ranger_overgrowth_duration_1,
        shop_ranger_overgrowth_duration_2,
        shop_ranger_overgrowth_range_1,
        shop_ranger_overgrowth_range_2,
        shop_ranger_flurry,
        shop_ranger_flurry_waves_1,
        shop_ranger_flurry_waves_2,
        shop_ranger_flurry_arrows_1,
        shop_ranger_flurry_arrows_2,
        shop_ranger_dodge_1,
        shop_ranger_dodge_2,
        shop_ranger_dodge_3,
        shop_ranger_dodge_4,
        shop_ranger_dodge_5,
        shop_ranger_marksmanship_1,
        shop_ranger_marksmanship_2,
        shop_ranger_marksmanship_3,
        shop_ranger_marksmanship_4,
    ],
    util.PlayerClass.Wizard: [
        shop_wizard_fireball_damage_1,
        shop_wizard_fireball_damage_2,
        shop_wizard_fireball_damage_3,
        shop_wizard_fireball_damage_4,
        shop_wizard_fireball_damage_5,
        shop_wizard_fireball_range_1,
        shop_wizard_fireball_range_2,
        shop_wizard_fireball_range_3,
        shop_wizard_fireball_range_4,
        shop_wizard_fireball_range_5,
        shop_wizard_fire_breath_damage_1,
        shop_wizard_fire_breath_damage_2,
        shop_wizard_fire_breath_damage_3,
        shop_wizard_fire_breath_damage_4,
        shop_wizard_fire_nova,
        shop_wizard_fire_nova_flames_1,
        shop_wizard_fire_nova_flames_2,
        shop_wizard_fire_nova_flames_3,
        shop_wizard_fire_nova_slow_1,
        shop_wizard_fire_nova_slow_2,
        shop_wizard_fire_nova_slow_3,
        shop_wizard_meteor_strike,
        shop_wizard_meteor_strike_damage_1,
        shop_wizard_meteor_strike_damage_2,
        shop_wizard_meteor_strike_meteors_1,
        shop_wizard_meteor_strike_meteors_2,
        shop_wizard_meteor_strike_meteors_3,
        shop_wizard_fire_shield,
        shop_wizard_combustion,
        shop_wizard_combustion_damage_1,
        shop_wizard_combustion_damage_2,
        shop_wizard_combustion_damage_3,
        shop_wizard_combustion_duration_1,
        shop_wizard_combustion_duration_2,
        shop_wizard_combustion_duration_3,
    ],
    util.PlayerClass.Warlock: [
        shop_warlock_dagger_damage_1,
        shop_warlock_dagger_damage_2,
        shop_warlock_dagger_damage_3,
        shop_warlock_dagger_damage_4,
        shop_warlock_dagger_damage_5,
        shop_warlock_dagger_poison_1,
        shop_warlock_dagger_poison_2,
        shop_warlock_dagger_poison_3,
        shop_warlock_dagger_poison_4,
        shop_warlock_dagger_poison_5,
        shop_warlock_lightning_strike_damage_1,
        shop_warlock_lightning_strike_damage_2,
        shop_warlock_lightning_strike_damage_3,
        shop_warlock_lightning_strike_damage_4,
        shop_warlock_lightning_strike_targets_1,
        shop_warlock_lightning_strike_targets_2,
        shop_warlock_lightning_strike_targets_3,
        shop_warlock_lightning_strike_targets_4,
        shop_warlock_summon_gargoyle,
        shop_warlock_gargoyle_damage_1,
        shop_warlock_gargoyle_damage_2,
        shop_warlock_gargoyle_duration_1,
        shop_warlock_gargoyle_duration_2,
        shop_warlock_electrical_storm,
        shop_warlock_electrical_storm_damage_1,
        shop_warlock_electrical_storm_damage_2,
        shop_warlock_electrical_storm_duration_1,
        shop_warlock_electrical_storm_duration_2,
        shop_warlock_blood_sacrifice_1,
        shop_warlock_blood_sacrifice_2,
        shop_warlock_blood_sacrifice_3,
        shop_warlock_blood_sacrifice_4,
        shop_warlock_blood_sacrifice_5,
        shop_warlock_soul_sacrifice_1,
        shop_warlock_soul_sacrifice_2,
        shop_warlock_soul_sacrifice_3,
    ],
    util.PlayerClass.Thief: [
        shop_thief_knives_damage_1,
        shop_thief_knives_damage_2,
        shop_thief_knives_damage_3,
        shop_thief_knives_damage_4,
        shop_thief_knives_damage_5,
        shop_thief_knife_fan_damage_1,
        shop_thief_knife_fan_damage_2,
        shop_thief_knife_fan_damage_3,
        shop_thief_knife_fan_knives_1,
        shop_thief_knife_fan_knives_2,
        shop_thief_knife_fan_knives_3,
        shop_thief_grapple_chain,
        shop_thief_grapple_chain_length_1,
        shop_thief_grapple_chain_length_2,
        shop_thief_grapple_chain_stun_1,
        shop_thief_grapple_chain_stun_2,
        shop_thief_smoke_bomb,
        shop_thief_smoke_bomb_range_1,
        shop_thief_smoke_bomb_range_2,
        shop_thief_fervor_1,
        shop_thief_fervor_2,
        shop_thief_fervor_3,
        shop_thief_speed_penalty_1,
        shop_thief_speed_penalty_2,
        shop_thief_speed_penalty_3,
        shop_thief_speed_penalty_4,
        shop_thief_dodge_1,
        shop_thief_dodge_2,
        shop_thief_dodge_3,
        shop_thief_dodge_4,
        shop_thief_dodge_5,
    ],
    util.PlayerClass.Priest: [
        shop_priest_smite_damage_1,
        shop_priest_smite_damage_2,
        shop_priest_smite_damage_3,
        shop_priest_smite_damage_4,
        shop_priest_smite_damage_5,
        shop_priest_speed_penalty_1,
        shop_priest_speed_penalty_2,
        shop_priest_speed_penalty_3,
        shop_priest_speed_penalty_4,
        shop_priest_speed_penalty_5,
        shop_priest_holy_beam_damage_1,
        shop_priest_holy_beam_damage_2,
        shop_priest_holy_beam_damage_3,
        shop_priest_holy_beam_damage_4,
        shop_priest_holy_beam_range_1,
        shop_priest_holy_beam_range_2,
        shop_priest_holy_beam_range_3,
        shop_priest_holy_beam_range_4,
        shop_priest_draining_field,
        shop_priest_draining_field_damage_1,
        shop_priest_draining_field_damage_2,
        shop_priest_draining_field_damage_3,
        shop_priest_draining_field_number_1,
        shop_priest_draining_field_number_2,
        shop_priest_cripple_aura,
        shop_priest_cripple_aura_slow_1,
        shop_priest_cripple_aura_slow_2,
        shop_priest_cripple_aura_mana_drain,
        shop_priest_hp_regen_1,
        shop_priest_hp_regen_2,
        shop_priest_hp_regen_3,
        shop_priest_hp_regen_4,
        shop_priest_hp_regen_5,
        shop_priest_magic_shield_1,
        shop_priest_magic_shield_2,
        shop_priest_magic_shield_3,
        shop_priest_magic_shield_4,
        shop_priest_magic_shield_5,
    ],
    util.PlayerClass.Sorcerer: [
        shop_sorcerer_ice_shard_damage_1,
        shop_sorcerer_ice_shard_damage_2,
        shop_sorcerer_ice_shard_damage_3,
        shop_sorcerer_ice_shard_damage_4,
        shop_sorcerer_ice_shard_damage_5,
        shop_sorcerer_ice_shard_bounces_1,
        shop_sorcerer_ice_shard_bounces_2,
        shop_sorcerer_ice_shard_bounces_3,
        shop_sorcerer_ice_shard_bounces_4,
        shop_sorcerer_ice_shard_bounces_5,
        shop_sorcerer_comet_damage_1,
        shop_sorcerer_comet_damage_2,
        shop_sorcerer_comet_damage_3,
        shop_sorcerer_comet_damage_4,
        shop_sorcerer_ice_shard_nova,
        shop_sorcerer_ice_shard_nova_number_1,
        shop_sorcerer_ice_shard_nova_number_2,
        shop_sorcerer_ice_shard_nova_mana_1,
        shop_sorcerer_ice_shard_nova_mana_2,
        shop_sorcerer_ice_orb,
        shop_sorcerer_ice_orb_damage_1,
        shop_sorcerer_ice_orb_damage_2,
        shop_sorcerer_ice_orb_time_1,
        shop_sorcerer_ice_orb_time_2,
        shop_sorcerer_ice_orb_time_3,
        shop_sorcerer_chill,
        shop_sorcerer_chill_slow_1,
        shop_sorcerer_chill_slow_2,
        shop_sorcerer_chill_slow_3,
        shop_sorcerer_chill_duration_1,
        shop_sorcerer_chill_duration_2,
        shop_sorcerer_chill_duration_3,
        shop_sorcerer_frost_shield_1,
        shop_sorcerer_frost_shield_2,
        shop_sorcerer_frost_shield_3,
        shop_sorcerer_frost_shield_4,
        shop_sorcerer_frost_shield_5,
    ],
}
#
