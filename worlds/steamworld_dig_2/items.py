from typing import List, Tuple, Dict, NamedTuple, Optional, TYPE_CHECKING
from enum import IntEnum
from BaseClasses import Item, ItemClassification
from .names import item_name, const
from .options import RandomizeShopUpgrades
from .util import Counter

if TYPE_CHECKING:
    from . import SWD2World


class ItemType(IntEnum):
    Normal = 0,
    Upgrade = 1,
    Blueprint = 2,
    Cog = 3,
    Artifact = 4,
    Resource = 5,
    ShopUpgrade = 6
    ShopBlueprint = 7


class ItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    item_type: ItemType = ItemType.Normal


class SWD2Item(Item):
    game: str = const.game


id_start = 0xfe5000

counter = Counter(id_start - 1)
item_table: Dict[str, ItemData] = {
    item_name.cog: ItemData(counter.count(), ItemClassification.filler, ItemType.Cog),
    item_name.pickaxe: ItemData(counter.count(), ItemClassification.progression, ItemType.ShopUpgrade),
    item_name.backpack: ItemData(counter.count(), ItemClassification.progression, ItemType.ShopUpgrade),
    item_name.lamp: ItemData(counter.count(), ItemClassification.progression, ItemType.ShopUpgrade),
    item_name.armor: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopUpgrade),
    item_name.tank: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopUpgrade),
    item_name.bomb: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.jackhammer: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.jetengine: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.hookshot: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.up_hookshot_range: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.sprint: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.up_pickaxe_ignition: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.up_bomb_grenades: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.up_bomb_more_grenades: ItemData(counter.count(), ItemClassification.useful, ItemType.Upgrade),
    item_name.up_ramjet: ItemData(counter.count(), ItemClassification.progression, ItemType.Upgrade),
    item_name.up_armor_defense: ItemData(counter.count(), ItemClassification.useful, ItemType.Upgrade),
    item_name.up_fate_blood_quest: ItemData(counter.count(), ItemClassification.trap, ItemType.Blueprint),
    item_name.up_fate_thrillseekers_tale: ItemData(counter.count(), ItemClassification.trap, ItemType.Blueprint),
    item_name.up_fate_deathplosions: ItemData(counter.count(), ItemClassification.trap, ItemType.Blueprint),
    item_name.ore: ItemData(counter.count(), ItemClassification.filler, ItemType.Resource),
    item_name.gem: ItemData(counter.count(), ItemClassification.filler, ItemType.Resource),
    item_name.omni_orbs: ItemData(counter.count(), ItemClassification.filler, ItemType.Resource),
    item_name.up_pickaxe_xp: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_pickaxe_resource_dmg: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_pickaxe_gold_kills: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_pickaxe_recoil: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_pickaxe_heal_orb: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_pickaxe_projectile_reflect: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_pickaxe_swing_speed: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_pickaxe_damage: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_bag_resource_loss: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_discard_gold: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_storage_gem: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_portal: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_resource_dupe: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_magnet: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_cheap_res_gold: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_discard_heal: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_sell_gold: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bag_storage_ore: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_lamp_radius: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_lamp_pickup_light: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_lamp_hazard_dodge: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_lamp_enemy_light: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_lamp_light_min: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_lamp_secret_sight: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_armor_fall_damage: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_armor_thorns: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_armor_liquid_res: ItemData(counter.count(), ItemClassification.progression, ItemType.ShopBlueprint),
    item_name.up_armor_reflect: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_armor_second_life: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_armor_orbs: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_tank_fill_speed: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_tank_water_orb_convert: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_tank_water_regen: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_tank_water_healing: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_bomb_no_friendly_fire: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bomb_extra_bomb: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bomb_strength: ItemData(counter.count(), ItemClassification.progression, ItemType.ShopBlueprint),
    item_name.up_bomb_air_firing: ItemData(counter.count(), ItemClassification.progression, ItemType.ShopBlueprint),
    item_name.up_hammer_windup: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_hammer_winddown: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_hammer_forward_pull: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_hammer_speed: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_jetpack_coast: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_jetpack_speed: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_jetpack_air_cooling: ItemData(counter.count(), ItemClassification.progression, ItemType.ShopBlueprint),
    item_name.up_map_markers: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_map_resources: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_map_health: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_fate_dmg_aoe: ItemData(counter.count(), ItemClassification.useful, ItemType.Blueprint),
    item_name.up_lamp_damage: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_tank_water_pickup: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bomb_radius: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_bomb_water_usage: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_hammer_shockwave: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.up_hammer_water_usage: ItemData(counter.count(), ItemClassification.useful, ItemType.ShopBlueprint),
    item_name.a_building_plans: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_straw_doll: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_book_groda: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_banana_peels: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_action_figure: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_inflatable_friend: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_black_box: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_fertilizer: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_amulet: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_dead_rat: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_diary: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_wrapped_gift: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_fifty: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_lost_penguin: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_glowing_goo: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_six_pack: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_dumbells: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_monster_plushy: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_stone_tablet: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_shark_tooth: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_theremin: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_red_cloth: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_weird_stone: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_fossil: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_cult_list: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_chainsaw: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_holy_toast: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_cake: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_manual: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_rubber_chickens: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_pills: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_old_invitations: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_toy_rocket: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_wagon_wheel: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_sacred_documentation: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_birdie_seeds: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_amiigo: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_orchid: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_scented_candle: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_cereal: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_painting: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_lime_snowman: ItemData(counter.count(), ItemClassification.progression_skip_balancing, ItemType.Artifact),
    item_name.a_completion_proof: ItemData(counter.count(), ItemClassification.useful, ItemType.Artifact),
    item_name.up_fate_sigil: ItemData(counter.count(), ItemClassification.progression, ItemType.Blueprint),
    item_name.vectron_ore_1: ItemData(counter.count(), ItemClassification.useful, ItemType.Resource),
    item_name.vectron_ore_2: ItemData(counter.count(), ItemClassification.useful, ItemType.Resource),
    item_name.vectron_ore_3: ItemData(counter.count(), ItemClassification.useful, ItemType.Resource),
    item_name.vectron_ore_4: ItemData(counter.count(), ItemClassification.useful, ItemType.Resource),
    item_name.vectron_ore_5: ItemData(counter.count(), ItemClassification.useful, ItemType.Resource),
}

item_counts: Dict[str, int] = {
    item_name.ore: 94,
    item_name.gem: 60,
    item_name.omni_orbs: 130,

    item_name.vectron_ore_1: 1,
    item_name.vectron_ore_2: 1,
    item_name.vectron_ore_3: 1,
    item_name.vectron_ore_4: 1,
    item_name.vectron_ore_5: 1,

    item_name.cog: 77,  # 84
    # item_name.lamp: 1,
    item_name.bomb: 1,
    item_name.jackhammer: 1,
    item_name.jetengine: 1,
    item_name.hookshot: 1,
    item_name.up_hookshot_range: 1,
    item_name.sprint: 1,
    item_name.up_pickaxe_ignition: 1,
    item_name.up_bomb_grenades: 1,
    item_name.up_ramjet: 1,
    item_name.up_armor_defense: 1,

    item_name.up_bomb_more_grenades: 1,
    item_name.up_map_health: 1,
    item_name.up_fate_dmg_aoe: 1,
    item_name.up_armor_orbs: 1,
    item_name.up_bag_storage_ore: 1,
    item_name.up_map_resources: 1,
    item_name.up_pickaxe_damage: 1,
    item_name.up_tank_water_healing: 1,
    item_name.up_fate_sigil: 1,

    item_name.up_fate_blood_quest: 1,
    item_name.up_fate_deathplosions: 1,
    item_name.up_fate_thrillseekers_tale: 1,
}

active_filler_items: List[str] = [
    item_name.ore,
    item_name.gem,
    item_name.omni_orbs,
]


def get_item_counts(world: "SWD2World") -> Tuple[Dict[str, int], int]:
    item_counts_dict = {**item_counts}
    extra_items = 0

    if not world.options.randomize_cogs:
        item_counts_dict[item_name.cog] = 0
    if not world.options.randomize_ores:
        item_counts_dict[item_name.ore] = 0
        item_counts_dict[item_name.gem] = 0
    if world.options.skip_vectron or not world.options.randomize_ores:
        item_counts_dict[item_name.vectron_ore_1] = 0
        item_counts_dict[item_name.vectron_ore_2] = 0
        item_counts_dict[item_name.vectron_ore_3] = 0
        item_counts_dict[item_name.vectron_ore_4] = 0
        item_counts_dict[item_name.vectron_ore_5] = 0
    if not world.options.randomize_orbs:
        item_counts_dict[item_name.omni_orbs] = 0

    if world.options.randomize_artifacts:
        for artifact in item_name.artifacts:
            item_counts_dict[artifact] = 1
        if not world.options.randomize_trials_reward:
            item_counts_dict.pop(item_name.a_completion_proof)
    if world.options.randomize_shops == RandomizeShopUpgrades.option_randomize:
        for item, data in item_table.items():
            if data.item_type == ItemType.ShopBlueprint:
                if item in item_name.unused_items and not world.options.add_unused_cog_upgrades:
                    continue
                item_counts_dict[item] = 1

    return item_counts_dict, extra_items


filler_items: List[str] = [item_name for item_name, data in item_table.items()
                           if data.classification == ItemClassification.filler]
trap_items: List[str] = [item_name for item_name, data in item_table.items()
                         if data.classification & ItemClassification.trap]
lookup_id_to_name: Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
