import string
from typing import List, Tuple, Dict, Set, NamedTuple, Optional, Iterable, Callable, TYPE_CHECKING
from enum import IntEnum
from collections import namedtuple
from BaseClasses import Region, Entrance, CollectionState, Item
from worlds.generic.Rules import add_rule
from .locations import SWD2Location, LocationData, all_locations, shop_locs
from .names import location_name, region_name, item_name, entrance_name, const
from . import options
from .util import GoalType, get_goal_type, get_random_element, Counter

if TYPE_CHECKING:
    from . import SWD2World


def always_accessible(state: CollectionState, player: int):
    return True


def has_item(item: str, count=1):
    return lambda state, player: state.has(item, player, count)


def has_ignition_axe(state: CollectionState, player: int):
    return state.has(item_name.up_pickaxe_ignition, player)


def has_sprint(state: CollectionState, player: int):
    return state.has(item_name.sprint, player)


def has_lamp(state: CollectionState, player: int):
    return state.has(item_name.lamp, player)


def has_bomb(state: CollectionState, player: int):
    return state.has(item_name.bomb, player)


def has_jackhammer(state: CollectionState, player: int):
    return state.has(item_name.jackhammer, player)


def can_dig_distance(state: CollectionState, player: int):
    return has_bomb(state, player) or can_ramjet(state, player)


def can_break_bricks(state: CollectionState, player: int):
    return state.has(item_name.jackhammer, player)


def has_hookshot(state: CollectionState, player: int):
    return state.has(item_name.hookshot, player)


def has_jet(state: CollectionState, player: int):
    return state.has(item_name.jetengine, player)


def can_ramjet(state: CollectionState, player: int):
    return has_jet(state, player) and state.has(item_name.up_ramjet, player)


def can_high_jump(state: CollectionState, player: int):
    return has_sprint(state, player) or has_hookshot(state, player) or has_jet(state, player)


def has_vertical(state: CollectionState, player: int):
    return has_hookshot(state, player) or has_jet(state, player)


def has_both_vertical(state: CollectionState, player: int):
    return has_hookshot(state, player) and has_jet(state, player)


def has_liquid_res(state: CollectionState, player: int):
    return True  # TODO: add rule for Vidar Boots (Armor Tier 3 upgrade)


def has_full_flight(state: CollectionState, player: int):
    return state.has(item_name.jetengine, player, 1)  # TODO: Change to tier 4 when we add shop logic


def can_cross_ceiling(state: CollectionState, player: int):
    return has_hookshot(state, player) or has_full_flight(state, player)


def has_grenade_or_air_shot(state: CollectionState, player: int):
    return (has_bomb(state, player)
            and (state.has(item_name.up_bomb_grenades, player) or state.has(item_name.up_bomb_air_firing, player)))


def has_artifacts(count: int):
    return lambda s, p: s.has(item_name.artifacts_name, p, count)


# def has_level(level: int):
#     return lambda s, p: s.has(item_name.artifacts_name, p, level)


def has_tank(state: CollectionState, player: int):
    return has_bomb(state, player) or has_jackhammer(state, player)


# Item rules
def is_not_freestanding(item: Item):
    return item.name != item_name.cog and item.name not in item_name.artifacts


class LocData(NamedTuple):
    name: str
    rule: Callable[[CollectionState, int], bool] = always_accessible


class ExitType(IntEnum):
    Internal = 10
    EndCave = 1
    ExitCave = 2
    Level = 3


exit_code_counter = Counter(-1)


class ExitData:
    name: str
    exit_type: ExitType
    rule: Callable[[CollectionState, int], bool]
    exit_id: int

    def __init__(self, name: str, ext_type: ExitType, rule: Callable[[CollectionState, int], bool] = always_accessible):
        self.name = name
        self.exit_type = ext_type
        self.rule = rule
        self.exit_id = exit_code_counter.count()


class DoorData(ExitData):
    door_name: str
    return_door_name: str

    def __init__(self, name: str, door_name: str, return_door_name: str,
                 rule: Callable[[CollectionState, int], bool] = always_accessible,
                 ext_type: ExitType = ExitType.EndCave):
        super().__init__(name, ext_type, rule)
        self.door_name = door_name
        self.return_door_name = return_door_name


class RegionData(NamedTuple):
    locations: Optional[List[LocData]]
    exits: Optional[List[ExitData]] = None


class SWD2Entrance(Entrance):
    target_region: Region

    linked = True
    shuffled = False

    def __init__(self, player: int, name: str = "", parent: Region = None, target: Region = None):
        super().__init__(player, name, parent)
        self.target_region = target


region_data: Dict[str, RegionData] = {
    region_name.menu: RegionData(None, None),
    region_name.west_desert_start: RegionData([
        LocData(location_name.wd_zebulon_yonker,
                lambda state, player: has_jet(state, player) and has_sprint(state, player)),
        # Don't actually need sprint but it prevents sprint from being placed here, you can't go backwards to it
    ], [
        ExitData(region_name.temple_guidance, ExitType.Level)
    ]),
    region_name.temple_guidance: RegionData([
        LocData(location_name.gt_tut_dig_gearbox),
        LocData(location_name.gt_tut_podium),
        LocData(location_name.gt_tut_podium_secret),
    ], [
        ExitData(region_name.temple_guidance_right, ExitType.Internal, has_sprint),
        ExitData(region_name.temple_guidance_cistern, ExitType.Internal,
                 lambda s, p: (has_sprint(s, p) or has_hookshot(s, p)) and has_vertical(s, p)),
    ]),
    region_name.temple_guidance_right: RegionData([
        LocData(location_name.gt_tut_above_hallway, has_vertical),
        LocData(location_name.gt_tut_boss_totem, can_break_bricks),
    ], [
        ExitData(region_name.west_desert_r, ExitType.Level),
        ExitData(region_name.temple_guidance, ExitType.Level, can_break_bricks),
    ]),
    region_name.temple_guidance_cistern: RegionData([
        LocData(location_name.tog_cistern_l, lambda s, p: has_vertical(s, p) and can_dig_distance(s, p)),
        LocData(location_name.tog_cistern_r, has_vertical),
        LocData(location_name.tog_cistern_m, lambda s, p: has_vertical(s, p) and can_break_bricks(s, p)),
    ], [
        ExitData(region_name.temple_guidance, ExitType.Internal, has_vertical),
        ExitData(region_name.yarrow_top_entr, ExitType.Level, has_vertical),
        DoorData(region_name.chamber_of_secrets,
                 entrance_name.door_cavemaze_guidance, entrance_name.door_guidance_cavemaze),
        ExitData(region_name.chamber_of_arrows, ExitType.ExitCave, has_vertical),
        ExitData(region_name.chamber_of_wheels, ExitType.ExitCave, has_vertical),
        DoorData(region_name.device_of_devastation,
                 entrance_name.door_cavegenerator_guidance, entrance_name.door_guidance_cavegenerator,
                 lambda s, p: s.has(item_name.ev_tog_cistern_button, p, 2)),
    ]),
    region_name.chamber_of_secrets: RegionData([
        LocData(location_name.c_cos_podium),
        LocData(location_name.c_cos_wall_l, has_grenade_or_air_shot),
        LocData(location_name.c_cos_end, lambda s, p: has_grenade_or_air_shot(s, p) and has_vertical(s, p)),
    ], None),
    region_name.chamber_of_arrows: RegionData([
        LocData(location_name.c_coa_secret, lambda s, p: has_vertical(s, p) and has_sprint(s, p)),
        LocData(location_name.c_coa_end, lambda s, p: has_vertical(s, p) and has_sprint(s, p)),
    ], [
        ExitData(region_name.temple_guidance_cistern_l, ExitType.ExitCave,
                 lambda s, p: has_vertical(s, p) and has_sprint(s, p)),
    ]),
    region_name.temple_guidance_cistern_l: RegionData([
        LocData(location_name.ev_tog_cistern_button_l),
    ], [
        ExitData(region_name.temple_guidance_cistern, ExitType.Internal)
    ]),
    region_name.chamber_of_wheels: RegionData([
        LocData(location_name.c_cow_secret, lambda s, p: has_vertical(s, p) and has_bomb(s, p)),
        LocData(location_name.c_cow_end, has_vertical),
    ], [
        ExitData(region_name.temple_guidance_cistern_r, ExitType.ExitCave, has_vertical),
    ]),
    region_name.temple_guidance_cistern_r: RegionData([
        LocData(location_name.ev_tog_cistern_button_r),
    ], [
        ExitData(region_name.temple_guidance_cistern, ExitType.Internal)
    ]),
    region_name.device_of_devastation: RegionData([
        LocData(location_name.ev_device_of_devastation),
    ], None),
    region_name.west_desert_r: RegionData([
        LocData(location_name.wd_right, lambda s, p: (has_bomb(s, p) and can_high_jump(s, p) or can_ramjet(s, p))),
    ], [
        # ExitData(region_name.temple_guidance_right, ExitType.Level),
        ExitData(region_name.machino, ExitType.Level),
        ExitData(region_name.west_desert_m, ExitType.Level, lambda s, p: has_bomb(s, p) or has_vertical(s, p)),
    ]),
    region_name.west_desert_m: RegionData([
        LocData(location_name.wd_top),
        LocData(location_name.wd_bottom),
    ], [
        ExitData(region_name.west_desert_start, ExitType.Level),
        DoorData(region_name.tenacious_trollies,
                 entrance_name.door_cavecartpuzzle_wdes, entrance_name.door_wdes_cavecartpuzzle),
    ]),
    region_name.tenacious_trollies: RegionData([
        LocData(location_name.c_tt_breakable_wall, can_dig_distance),
        LocData(location_name.c_tt_end, can_dig_distance),
        LocData(location_name.c_tt_3, can_dig_distance),
    ], None),
    region_name.machino: RegionData([
        LocData(location_name.em_artifact_1, has_artifacts(1)),
        LocData(location_name.em_artifact_3, has_artifacts(3)),
        LocData(location_name.em_artifact_6, has_artifacts(6)),
        LocData(location_name.em_artifact_10, has_artifacts(10)),
        LocData(location_name.em_artifact_15, has_artifacts(15)),
        LocData(location_name.em_artifact_21, has_artifacts(21)),
        LocData(location_name.em_artifact_28, has_artifacts(28)),
        LocData(location_name.em_artifact_42, has_artifacts(42)),
    ], [
        ExitData(region_name.west_desert_r, ExitType.Level, can_high_jump),
        ExitData(region_name.machino_shop, ExitType.Internal),
        ExitData(region_name.machino_uptown, ExitType.Internal, lambda s, p: has_bomb(s, p) or has_vertical(s, p)),
        ExitData(region_name.windy_plains, ExitType.Level, can_high_jump),
        ExitData(region_name.archaea_top, ExitType.Level),
    ]),
    region_name.machino_shop: RegionData([
        LocData(location_name.em_pickaxe_2),
        LocData(location_name.em_backpack_2),
        LocData(location_name.em_lamp_2),
        LocData(location_name.em_tank_2, has_tank),
        LocData(location_name.em_bomb_3, has_bomb),
    ], [
        ExitData(region_name.machino_shop_3, ExitType.Internal, can_high_jump)
    ]),
    region_name.machino_shop_3: RegionData([
        LocData(location_name.em_pickaxe_3),
        LocData(location_name.em_pickaxe_4),
        LocData(location_name.em_backpack_3),
        LocData(location_name.em_backpack_4),
        LocData(location_name.em_backpack_5),
        LocData(location_name.em_lamp_3),
        LocData(location_name.em_lamp_4),
        LocData(location_name.em_armor_2),
        LocData(location_name.em_armor_3),
        LocData(location_name.em_armor_4),
        LocData(location_name.em_tank_3, has_tank),
        # LocData(location_name.em_bomb_1),
        LocData(location_name.em_bomb_2, has_bomb),
        # LocData(location_name.em_hammer_1),
        # LocData(location_name.em_jetpack_1),
    ], [
        ExitData(region_name.machino_shop_6, ExitType.Internal,
                 lambda s, p: s.has(item_name.ev_dampener_destroyed, p, 1))
    ]),
    region_name.machino_shop_6: RegionData([
        LocData(location_name.em_pickaxe_5),
        LocData(location_name.em_pickaxe_6),
        LocData(location_name.em_pickaxe_7),
        LocData(location_name.em_backpack_6),
        LocData(location_name.em_backpack_7),
        LocData(location_name.em_backpack_8),
        LocData(location_name.em_lamp_5),
        LocData(location_name.em_lamp_6),
        LocData(location_name.em_armor_5),
        LocData(location_name.em_armor_6),
        LocData(location_name.em_armor_7),
        LocData(location_name.em_tank_4, has_tank),
        LocData(location_name.em_hammer_2, has_jackhammer),
        LocData(location_name.em_hammer_3, has_jackhammer),
    ], [
        ExitData(region_name.machino_shop_10, ExitType.Internal,
                 lambda s, p: s.has(item_name.ev_dampener_destroyed, p, 2))
    ]),
    region_name.machino_shop_10: RegionData([
        LocData(location_name.em_pickaxe_8),
        LocData(location_name.em_backpack_9),
        LocData(location_name.em_backpack_10),
        LocData(location_name.em_armor_8),
        LocData(location_name.em_hammer_4, has_tank),
        LocData(location_name.em_jetpack_2, has_jet),
    ], [
        ExitData(region_name.machino_shop_14, ExitType.Internal,
                 lambda s, p: s.has(item_name.ev_dampener_destroyed, p, 3))
    ]),
    region_name.machino_shop_14: RegionData([
        LocData(location_name.em_lamp_7),
        LocData(location_name.em_tank_5, has_tank),
        LocData(location_name.em_bomb_4, has_bomb),
        LocData(location_name.em_jetpack_3, has_jet),
    ], None),
    region_name.machino_uptown: RegionData([
        LocData(location_name.em_heisenberg, lambda s, p: s.can_reach_region(region_name.yarrow, p)),
        # LocData(location_name.em_carson_1),  # We can't randomize these for now ;-;
        # LocData(location_name.em_carson_2),
        # LocData(location_name.em_carson_3),
        # LocData(location_name.em_carson_4),
        # LocData(location_name.em_carson_5),
        # LocData(location_name.em_carson_6),
        # LocData(location_name.em_carson_7),
    ], None),
    region_name.windy_plains: RegionData([
        LocData(location_name.wp_cliff),
        LocData(location_name.wp_bottom_l, can_break_bricks),
        LocData(location_name.wp_bottom_r),
    ], [
        ExitData(region_name.machino, ExitType.Level, can_high_jump),
        DoorData(region_name.rock_falls,
                 entrance_name.door_caverunfallblock_edes, entrance_name.door_edes_caverunfallblock, can_dig_distance),
        ExitData(region_name.windy_plains_temple, ExitType.Internal, has_vertical),
    ]),
    region_name.windy_plains_temple: RegionData([
        LocData(location_name.wp_hill_right),
    ], [
        ExitData(region_name.windy_plains, ExitType.Internal),
        ExitData(region_name.temple_destroyer_upper, ExitType.Level),
        ExitData(region_name.temple_destroyer, ExitType.Level),
    ]),
    region_name.rock_falls: RegionData([
        LocData(location_name.c_rf_top_right, can_high_jump),
        LocData(location_name.c_rf_end),
        LocData(location_name.c_rf_3),
    ], None),
    region_name.archaea_top: RegionData(None, [
        ExitData(region_name.archaea, ExitType.Internal),
    ]),
    region_name.archaea: RegionData([
        LocData(location_name.a_top_l_t, can_break_bricks),
        LocData(location_name.a_top_l_b),
        LocData(location_name.a_top_r),
    ], [
        DoorData(region_name.patch_wall_grotto,
                 entrance_name.door_caveunclimbable_arch, entrance_name.door_arch_caveunclimbable),
        DoorData(region_name.bursters_station,
                 entrance_name.door_cavepressurebomb_arch2, entrance_name.door_arch2_cavepressurebomb),
        ExitData(region_name.archaea_below_rrp, ExitType.Internal, has_bomb),
    ]),
    region_name.patch_wall_grotto: RegionData([
        LocData(location_name.c_pwg_ledge),
        LocData(location_name.c_pwg_secret),
    ], None),
    region_name.bursters_station: RegionData([
        LocData(location_name.c_bs_podium),
        LocData(location_name.c_bs_secret_r, can_dig_distance),
        LocData(location_name.c_bs_secret_t, can_dig_distance),
        LocData(location_name.c_bs_podium_ore, can_dig_distance),
    ], None),
    region_name.archaea_cp_entrance: RegionData(None, [
        ExitData(region_name.windy_plains, ExitType.Level),
    ]),
    region_name.archaea_below_rrp: RegionData([
        LocData(location_name.a_rrp_l),
        LocData(location_name.a_rrp_r),
    ], [
        DoorData(region_name.cave_in_catacomb,
                 entrance_name.door_cavesnakestoneblocks_arch1, entrance_name.door_arch1_cavesnakestoneblocks),
        ExitData(region_name.archaea_cactus_plantation, ExitType.Internal),
    ]),
    region_name.cave_in_catacomb: RegionData([
        LocData(location_name.c_cic_end),
        LocData(location_name.c_cic_top_secret, can_high_jump),
    ], None),
    region_name.archaea_cactus_plantation: RegionData([
        LocData(location_name.a_cp_from_wp, lambda s, p: has_bomb(s, p) and can_high_jump(s, p)),
    ], [
        DoorData(region_name.tick_boom_room,
                 entrance_name.door_cavefallblockpuzzle_arch1, entrance_name.door_arch1_cavefallblockpuzzle),
        DoorData(region_name.prickly_panorama,
                 entrance_name.door_cavecactus_arch1, entrance_name.door_arch1_cavecactus),
        ExitData(region_name.archaea_cp_entrance, ExitType.Internal,
                 lambda s, p: can_dig_distance(s, p) and has_vertical(s, p)),
        ExitData(region_name.archaea_wall_above, ExitType.Internal),
    ]),
    region_name.archaea_wall_above: RegionData(None, [
        ExitData(region_name.yarrow, ExitType.Level, has_bomb),
        ExitData(region_name.archaea_wall, ExitType.Internal, can_break_bricks),
    ]),
    region_name.tick_boom_room: RegionData([
        LocData(location_name.c_tbr_reward, can_dig_distance),
    ], None),
    region_name.prickly_panorama: RegionData([
        # Only has a gem location
    ], None),
    region_name.archaea_wall: RegionData([
        LocData(location_name.a_wall),
    ], [
        DoorData(region_name.trilobyte_bluff,
                 entrance_name.door_cavetrilobitepuzzle_arch1, entrance_name.door_arch1_cavetrilobitepuzzle),
    ]),
    region_name.trilobyte_bluff: RegionData([
        LocData(location_name.c_tb_end),
    ], None),
    region_name.yarrow_top_entr: RegionData([
        LocData(location_name.y_up_luke_yonker),
    ], [
        ExitData(region_name.archaea_wall_above, ExitType.Level),
        ExitData(region_name.temple_guidance_cistern, ExitType.Level, has_vertical),
    ]),
    region_name.yarrow: RegionData([
        LocData(location_name.y_up_lake_t),
        LocData(location_name.y_up_lake_r),
    ], [
        ExitData(region_name.yarrow_top_entr, ExitType.Level, has_vertical),
        ExitData(region_name.archaea_below_wall, ExitType.Level),
        ExitData(region_name.yarrow_below_glittering_grove, ExitType.Internal, has_jet),
    ]),
    region_name.yarrow_below_glittering_grove: RegionData(None, [
        DoorData(region_name.swim_swam_sway,
                 entrance_name.door_cavewater_yarr, entrance_name.door_yarr_cavewater),
        ExitData(region_name.sludge_river_bend, ExitType.ExitCave, can_ramjet),
        ExitData(region_name.leaky_lodge, ExitType.ExitCave),
    ]),
    region_name.swim_swam_sway: RegionData([
        LocData(location_name.c_sss_secret_r),
        LocData(location_name.c_sss_secret_l),
        LocData(location_name.c_sss_end),
    ], None),
    region_name.sludge_river_bend: RegionData([
        LocData(location_name.c_srb_r),
        LocData(location_name.c_srb_m, lambda s, p: has_hookshot(s, p) and has_bomb(s, p) and has_liquid_res(s, p)),
    ], [
        ExitData(region_name.oasis, ExitType.Level, has_liquid_res)
    ]),
    region_name.leaky_lodge: RegionData([
        LocData(location_name.c_ll_secret_b),
        LocData(location_name.c_ll_secret_t, lambda s, p: has_vertical(s, p) and has_bomb(s, p)),
        LocData(location_name.c_ll_end, lambda s, p: has_vertical(s, p) and has_bomb(s, p)),
    ], [
        ExitData(region_name.yarrow_below_acid_swamp, ExitType.Internal,
                 lambda s, p: has_vertical(s, p) and has_bomb(s, p)),
    ]),
    region_name.yarrow_below_acid_swamp: RegionData([
        LocData(location_name.y_lower_below_acid_l),
        LocData(location_name.y_lower_bouncy_ceil, has_vertical),
        LocData(location_name.y_lower_above_mm, has_liquid_res),
    ], [
        DoorData(region_name.hodge_podge_hang,
                 entrance_name.door_cavecliffhanger_yarr, entrance_name.door_yarr_cavecliffhanger),
        DoorData(region_name.mushi_mushi_snuggery,
                 entrance_name.door_cavemushimushiroom_yarr, entrance_name.door_yarr_cavemushimushiroom),
        DoorData(region_name.bushwack_beehive, entrance_name.door_cavebats_yarr, entrance_name.door_yarr_cavebats),
        DoorData(region_name.lime_loop, entrance_name.door_caverun_yarr, entrance_name.door_yarr_caverun),
        ExitData(region_name.aeronauts_station, ExitType.ExitCave),
    ]),
    region_name.hodge_podge_hang: RegionData([
        LocData(location_name.c_hph_secret, lambda s, p: s.has(item_name.jetengine, p, 1)),  # TODO: Switch this to 2
        LocData(location_name.c_hph_end, has_vertical),
    ], None),
    region_name.mushi_mushi_snuggery: RegionData([
        LocData(location_name.c_mms_secret, has_vertical),
        LocData(location_name.c_mms_end, has_vertical),
    ], None),
    region_name.bushwack_beehive: RegionData([
        LocData(location_name.c_bb_secret, has_hookshot),
        LocData(location_name.c_bb_end, has_vertical),
    ], None),
    region_name.lime_loop: RegionData([
        LocData(location_name.c_lime_loop_end),
        LocData(location_name.c_lime_loop_secret),
    ], None),
    region_name.aeronauts_station: RegionData([
        LocData(location_name.c_as_podium, has_jet),
        LocData(location_name.c_as_end, can_ramjet),
        LocData(location_name.c_as_secret, can_ramjet),
    ], [
        ExitData(region_name.yarrow_bottom, ExitType.ExitCave, can_ramjet),
    ]),
    region_name.yarrow_bottom: RegionData([
        LocData(location_name.y_lower_mm_l, can_ramjet),
    ], [
        DoorData(region_name.device_of_disaster,
                 entrance_name.door_cavegenerator_yarr2, entrance_name.door_yarr2_cavegenerator),
    ]),
    region_name.device_of_disaster: RegionData([
        LocData(location_name.ev_device_of_disaster),
    ], None),
    region_name.archaea_below_wall: RegionData([
        LocData(location_name.a_bwall_l, can_break_bricks),
        LocData(location_name.a_josh_yonker, can_break_bricks),
    ], [
        DoorData(region_name.masons_station,
                 entrance_name.door_cavejackhammer_arch2, entrance_name.door_arch2_cavejackhammer),
        DoorData(region_name.rupture_rock_hollow,
                 entrance_name.door_cavesnakestone_arch1, entrance_name.door_arch1_cavesnakestone),
        ExitData(region_name.archaea_bricks, ExitType.Internal, can_break_bricks),
    ]),
    region_name.masons_station: RegionData([
        LocData(location_name.c_ms_podium, lambda s, p: can_dig_distance(s, p) or can_break_bricks(s, p)),
        LocData(location_name.c_ms_top, lambda s, p: can_dig_distance(s, p) or can_break_bricks(s, p)),
        LocData(location_name.c_ms_end, can_break_bricks),
    ], None),
    region_name.rupture_rock_hollow: RegionData([
        LocData(location_name.c_rrh_right),
        LocData(location_name.c_rrh_end),
        LocData(location_name.c_rrh_top, has_vertical),
    ], None),
    region_name.archaea_bricks_entrance: RegionData([
        LocData(location_name.a_bwall_entr),
    ], [
        ExitData(region_name.archaea_bricks, ExitType.Internal),
        ExitData(region_name.totd_lava_dripper_hall, ExitType.Level),
    ]),
    region_name.archaea_bricks: RegionData(None, [
        ExitData(region_name.oasis, ExitType.Level),
        ExitData(region_name.archaea_bricks_entrance, ExitType.Internal, has_vertical),
        ExitData(region_name.archaea_lower_mining_outpost, ExitType.Internal),
    ]),
    region_name.oasis: RegionData([
        LocData(location_name.o_top, has_vertical),
    ], [
        ExitData(region_name.machino, ExitType.Level),
        DoorData(region_name.rosies_storage,
                 entrance_name.door_cavegrapplinghook_thehub, entrance_name.door_thehub_cavegrapplinghook),
        ExitData(region_name.archaea_bricks, ExitType.Level),
        # Yeah no let's not randomize the final boss arena lol
        ExitData(region_name.the_reactor, ExitType.Internal, lambda s, p: s.has(item_name.ev_dampener_destroyed, p, 4)),
    ]),
    region_name.rosies_storage: RegionData([
        LocData(location_name.c_rs_podium),
        LocData(location_name.c_rs_secret_r, has_vertical),
        LocData(location_name.c_rs_end, has_vertical),
    ], None),
    region_name.the_reactor: RegionData(None, [
        ExitData(region_name.defeat_rosie, ExitType.Internal),
    ]),
    region_name.defeat_rosie: RegionData([
        LocData(location_name.ev_defeat_rosie),
    ], None),
    region_name.archaea_lower_mining_outpost: RegionData([
        LocData(location_name.a_lmo_ceiling, lambda s, p: can_dig_distance(s, p) and has_vertical(s, p)),
    ], [
        ExitData(region_name.archaea_bottom, ExitType.Internal, can_break_bricks),
    ]),
    region_name.archaea_bottom: RegionData([
        LocData(location_name.a_b_l, has_vertical),
        LocData(location_name.a_b_r),
        LocData(location_name.a_b_m, has_vertical),
    ], [
        DoorData(region_name.mysterious_cave, entrance_name.door_arch_vectron1, entrance_name.door_archaea_vectron1),
        ExitData(region_name.archaea_bottom_jet, ExitType.Internal,
                 lambda s, p: (has_both_vertical(s, p) or has_full_flight(s, p)) and can_break_bricks(s, p)),
    ]),
    region_name.archaea_bottom_jet: RegionData([
        LocData(location_name.a_b_jet_b),
        LocData(location_name.a_b_jet_end),
    ], None),
    region_name.mysterious_cave: RegionData([
        LocData(location_name.c_mc_podium),
        LocData(location_name.c_mc_top, has_vertical),
    ], [
        # ExitData(region_name.vectron, ExitType.Internal),
    ]),
    # region_name.vectron: RegionData(None, None),  # There are unique ores here, but I don't think they're tracked?
    region_name.temple_destroyer_upper: RegionData([
        LocData(location_name.totd_upper_m),
        LocData(location_name.totd_upper_r),
        LocData(location_name.ev_totd_treasure_brazier_top, has_ignition_axe),
    ], [
        ExitData(region_name.windy_plains_temple, ExitType.Level),
    ]),
    region_name.temple_destroyer: RegionData([
        LocData(location_name.totd_entrance_top, can_break_bricks),
    ], [
        ExitData(region_name.windy_plains_temple, ExitType.Level),
        ExitData(region_name.totd_entr_shaft, ExitType.Internal,
                 lambda s, p: can_high_jump(s, p) and can_break_bricks(s, p)),
        ExitData(region_name.demons_crib, ExitType.Internal, has_ignition_axe),
    ]),
    region_name.demons_crib: RegionData([
        LocData(location_name.c_dc_bottom, lambda s, p: can_high_jump(s, p) or has_hookshot(s, p)),
    ], [
        ExitData(region_name.temple_destroyer_upper, ExitType.Internal),
        # Technically an exit cave, but the exit is one-way!
    ]),
    region_name.totd_entr_shaft: RegionData([
        LocData(location_name.totd_es_maze),
    ], [
        DoorData(region_name.the_batcave, entrance_name.door_cavefirebat_fire1, entrance_name.door_fire1_cavefirebat),
        ExitData(region_name.totd_conveyor_maze, ExitType.Internal),
    ]),
    region_name.the_batcave: RegionData([
        LocData(location_name.c_tb_top_r, has_vertical),
        LocData(location_name.c_tb_top_l, has_vertical),
    ], None),
    region_name.totd_conveyor_maze: RegionData([
        LocData(location_name.totd_cm_m, can_break_bricks),
        LocData(location_name.totd_cm_end_t),
        LocData(location_name.totd_cm_end_b),
        LocData(location_name.ev_totd_treasure_brazier_right, has_ignition_axe),
    ], [
        DoorData(region_name.floor_is_lava,
                 entrance_name.door_floor_is_lava_ftemp, entrance_name.door_ftemp_floor_is_lava),
        ExitData(region_name.totd_lava_dripper_hall, ExitType.Internal),
    ]),
    region_name.floor_is_lava: RegionData([
        LocData(location_name.c_fil_end, has_vertical),
        LocData(location_name.c_fil_perfect, has_both_vertical),
    ], None),
    region_name.totd_lava_dripper_hall: RegionData([
        LocData(location_name.totd_ga, lambda s, p: has_vertical(s, p) or s.has(item_name.hookshot, p, 2)),
        LocData(location_name.ev_totd_treasure_brazier_left, has_ignition_axe)
    ], [
        DoorData(region_name.lava_shooters,
                 entrance_name.door_cavelavashooters_ftemp, entrance_name.door_ftemp_cavelavashooters),
        DoorData(region_name.roasted_romp,
                 entrance_name.door_cavecrusher_ftemp, entrance_name.door_ftemp_cavecrusher),
        DoorData(region_name.grim_hollow,
                 entrance_name.door_cavegolem_ftemp, entrance_name.door_ftemp_cavegolem),
        ExitData(region_name.archaea_bricks_entrance, ExitType.Level, has_ignition_axe),
        DoorData(region_name.spikes_conveyors,
                 entrance_name.door_cavespikeconveyor_fire, entrance_name.door_fire_cavespikeconveyor),
        ExitData(region_name.totd_bowels, ExitType.Internal),
    ]),
    region_name.lava_shooters: RegionData([
        LocData(location_name.c_ls_ledge_r, has_vertical),
        LocData(location_name.c_ls_end_secret, has_vertical),
        LocData(location_name.c_ls_end, has_vertical),
    ], None),
    region_name.roasted_romp: RegionData([
        LocData(location_name.c_rr_secret_l),
        LocData(location_name.c_rr_end),
    ], None),
    region_name.grim_hollow: RegionData([
        LocData(location_name.c_gh_secret_left, lambda s, p: has_vertical(s, p) and s.has(item_name.bomb, p, 1)),
        # TODO: change to 2 when we add shop locations
        LocData(location_name.c_gh_end, has_vertical),
    ], None),
    region_name.spikes_conveyors: RegionData([
        LocData(location_name.c_sac_secret_r, has_hookshot),
        LocData(location_name.c_sac_secret_t, has_hookshot),
        LocData(location_name.c_sac_end, has_hookshot),
    ], None),
    region_name.totd_bowels: RegionData([
        LocData(location_name.totd_bowels_l, has_liquid_res),
        LocData(location_name.totd_bowels_m, has_jet),
    ], [
        DoorData(region_name.combusters_station,
                 entrance_name.door_caveflamer_fire1, entrance_name.door_fire1_caveflamer),
        DoorData(region_name.device_of_doom,
                 entrance_name.door_cavegenerator1_fire1, entrance_name.door_fire1_cavegenerator1,
                 lambda s, p: has_ignition_axe(s, p) and can_high_jump(s, p)),
        DoorData(region_name.ronalds_treasure_chamber,
                 entrance_name.door_cavetreasurechamber_fire1, entrance_name.door_fire1_cavetreasurechamber,
                 lambda s, p: has_ignition_axe(s, p) and s.has(item_name.ev_totd_treasure_brazier, p, 3)),
        ExitData(region_name.totd_rivers, ExitType.Internal, has_full_flight),
    ]),
    region_name.combusters_station: RegionData([
        LocData(location_name.c_cs_podium, lambda s, p: has_vertical(s, p) and can_break_bricks(s, p)),
        LocData(location_name.c_cs_secret_l,
                lambda s, p: (has_vertical(s, p) or has_ignition_axe(s, p)) and can_break_bricks(s, p)),
    ], None),
    region_name.device_of_doom: RegionData([
        LocData(location_name.ev_device_of_doom),
    ], None),
    region_name.ronalds_treasure_chamber: RegionData([
        LocData(location_name.c_rtc_podium, has_vertical),
        LocData(location_name.c_rtc_secret_1, has_vertical),
        LocData(location_name.c_rtc_secret_2, has_vertical),
        LocData(location_name.c_rtc_secret_3, has_vertical),
    ], None),
    region_name.totd_rivers: RegionData([
        LocData(location_name.totd_river_t, has_bomb),
        LocData(location_name.totd_river_b_l, can_cross_ceiling),
        LocData(location_name.totd_river_b_b, can_cross_ceiling),
        LocData(location_name.totd_river_b_r, can_cross_ceiling),
        LocData(location_name.totd_river_b_t, can_cross_ceiling),
    ], [
        DoorData(region_name.infernal_crates,
                 entrance_name.door_caveboxes_ftemp, entrance_name.door_ftemp_caveboxes,
                 lambda s, p: can_cross_ceiling(s, p) and can_ramjet(s, p)),
        DoorData(region_name.mine_cart_madness,
                 entrance_name.door_cavehellcarts_fire2, entrance_name.door_fire2_cavehellcarts, can_cross_ceiling),
        DoorData(region_name.the_sun_armory, entrance_name.door_cavearmor_fire2, entrance_name.door_fire2_cavearmor,
                 can_cross_ceiling),
        DoorData(region_name.device_of_destruction,
                 entrance_name.door_cavegenerator2_fire2, entrance_name.door_fire2_cavegenerator2, can_cross_ceiling),
    ]),
    region_name.infernal_crates: RegionData([
        LocData(location_name.c_ic_secret_r, lambda s, p: has_vertical(s, p) and has_bomb(s, p)),
        LocData(location_name.c_ic_end, has_vertical),
    ], None),
    region_name.mine_cart_madness: RegionData([
        LocData(location_name.c_mm_reward_1, lambda s, p: can_dig_distance(s, p) and has_vertical(s, p)),
        LocData(location_name.c_mm_reward_2, lambda s, p: can_dig_distance(s, p) and has_vertical(s, p)),
        LocData(location_name.c_mm_reward_3, lambda s, p: can_dig_distance(s, p) and has_vertical(s, p)),
    ], None),
    region_name.the_sun_armory: RegionData([
        LocData(location_name.c_sa_podium),
    ], None),
    region_name.device_of_destruction: RegionData([
        LocData(location_name.ev_device_of_destruction),
    ], None),
}
REGIONS = list(region_data.keys())


def create_and_connect_regions(world: "SWD2World", active_locations: Set[str], event_locations: Set[set]):
    used_names: Dict[str, int] = {}
    world.swapped_entrances = []
    world.swapped_doors = {}
    # world.swapped_regions = {}

    created_regions = [create_region(world, active_locations, event_locations, reg_name, data.locations)
                       for reg_name, data in region_data.items()]
    world.multiworld.regions.extend(created_regions)

    unconnected_entrances: List[Tuple[SWD2Entrance, DoorData]] = []
    available_exits: List[Tuple[Region, DoorData]] = []
    return_doors = {}
    for reg_name, data in region_data.items():
        if not data.exits:
            continue
        for exit_data in data.exits:
            entrance = connect(world, used_names, reg_name, exit_data.name, exit_data,
                               lambda state, plr=world.player, rule=exit_data.rule: rule(state, plr))
            if not entrance.linked:
                unconnected_entrances.append((entrance, exit_data))
                available_exits.append((entrance.target_region, exit_data))
                return_doors[exit_data.door_name] = exit_data.return_door_name

    # Handle er seed
    random_state = world.random.getstate()
    er_seed = world.options.er_seed.value
    if hasattr(world.multiworld, "re_gen_passthrough"):
        er_seed = world.multiworld.re_gen_passthrough[const.game]["er_seed"]
    if er_seed == "random":
        er_seed = ''.join(world.random.choices(string.ascii_letters, k=16))
        world.options.er_seed.value = er_seed
    world.random.seed(er_seed)

    # Naive shuffle of entrances, make a better algorithm for the higher tiers of shuffle later
    while unconnected_entrances:
        entrance, entrance_data = unconnected_entrances.pop()
        connect_region, connect_data = available_exits.pop(world.random.randint(0, len(available_exits) - 1))
        entrance.connect(connect_region)
        # world.swapped_entrances.append(entrance)
        world.swapped_doors[entrance_data.door_name] = connect_data.door_name
        world.swapped_doors[connect_data.return_door_name] = entrance_data.return_door_name
        world.multiworld.spoiler.set_entrance(entrance.name, entrance.connected_region.name,
                                              "entrance", world.player)
        # world.swapped_regions[entrance_to_connect.target_region] = connect_region

    # Start location
    start_location_regions = {
        options.StartLocation.option_vanilla: region_name.west_desert_start,
        options.StartLocation.option_el_machino: region_name.machino,
        options.StartLocation.option_the_oasis: region_name.oasis,
        options.StartLocation.option_temple_of_the_destroyer: region_name.temple_destroyer,
    }
    connect(world, used_names, region_name.menu, start_location_regions[world.options.start_location], None)

    world.random.setstate(random_state)


def create_region(world: "SWD2World", active_locations: Set[str], event_locations: Set[set], name: str,
                  locations: List[LocData] = None) -> Region:
    region = Region(name, world.player, world.multiworld)
    if locations:
        for loc_data in locations:
            event = loc_data.name in event_locations or loc_data.name not in all_locations.keys()
            if loc_data.name not in active_locations and not event:
                continue
            loc_id = None if event else all_locations[loc_data.name].code
            location = SWD2Location(world.player, loc_data.name, loc_id, region)
            if location.name in shop_locs:
                location.item_rule = is_not_freestanding
            region.locations.append(location)
            add_rule(location, lambda state, plr=world.player, rule=loc_data.rule: rule(state, plr))
    return region


def connect(world: "SWD2World", used: Dict[str, int], source: str, target: str, exit_data: ExitData | None, rule=None):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)
    entrance_name = get_entrance_name(used, source_region.name, target_region.name)

    connection = SWD2Entrance(world.player, entrance_name, source_region, target_region)
    if rule:
        add_rule(connection, rule, "and")

    source_region.exits.append(connection)

    # Don't connect if ER is on
    if exit_data is None or world.options.entrance_rando.value < exit_data.exit_type.value:
        connection.connect(target_region)
    else:
        connection.linked = False
        connection.shuffled = True

    return connection


def get_etr_name(source: str, target: str):
    return source + " > " + target


def get_entrance_name(used_names: Dict[str, int], source: str, target: str):
    base_name = get_etr_name(source, target)
    if base_name not in used_names:
        used_names[base_name] = 1
        name = base_name
    else:
        used_names[base_name] += 1
        name = base_name + ('_' * used_names[base_name])
    return name
