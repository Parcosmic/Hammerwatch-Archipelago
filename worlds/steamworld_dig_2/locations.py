from typing import List, Tuple, Dict, Set, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import Location
from .names import item_name, location_name, option_name, const
from .util import Counter, GoalType, get_goal_type, is_using_universal_tracker
from .items import id_start, get_item_counts
from enum import IntEnum

if TYPE_CHECKING:
    from . import SWD2World


class LocType(IntEnum):
    Normal = 0,
    Upgrade = 1,
    Podium = 2,
    Cog = 3,
    Artifact = 4,
    Resource = 5,
    Shop = 6,


class LocationData(NamedTuple):
    code: Optional[int]
    loc_type: LocType = LocType.Normal


class SWD2Location(Location):
    game: str = const.game

    def __init__(self, player: int, name: str = '', code: int = None, parent=None):
        super().__init__(player, name, code, parent)
        self.event = code is None
        self.show_in_spoiler = code is not None


counter = Counter(id_start - 1)
default_locs: Dict[str, LocationData] = {
    location_name.wd_zebulon_yonker: LocationData(32579550, LocType.Upgrade),
    location_name.gt_tut_dig_gearbox: LocationData(32569640, LocType.Cog),
    location_name.gt_tut_podium: LocationData(32569721, LocType.Podium),
    location_name.gt_tut_podium_secret: LocationData(32580827, LocType.Artifact),
    location_name.gt_tut_above_hallway: LocationData(32580825, LocType.Cog),
    location_name.gt_tut_boss_totem: LocationData(32602808, LocType.Artifact),
    location_name.wd_right: LocationData(32564509, LocType.Cog),
    location_name.wd_top: LocationData(1042420, LocType.Cog),
    location_name.wd_bottom: LocationData(32569045, LocType.Artifact),
    location_name.c_tt_breakable_wall: LocationData(32587494, LocType.Artifact),
    location_name.c_tt_end: LocationData(32583882, LocType.Cog),
    location_name.wp_cliff: LocationData(32568549, LocType.Artifact),
    location_name.wp_bottom_l: LocationData(32577986, LocType.Cog),
    location_name.wp_bottom_r: LocationData(32569078, LocType.Cog),
    location_name.wp_hill_right: LocationData(32569055, LocType.Artifact),
    location_name.c_rf_top_right: LocationData(32569075, LocType.Artifact),
    location_name.c_rf_end: LocationData(32569033, LocType.Cog),
    location_name.a_top_l_t: LocationData(32592322, LocType.Artifact),
    location_name.a_top_l_b: LocationData(32587043, LocType.Cog),
    location_name.a_top_r: LocationData(32566126, LocType.Cog),
    location_name.c_pwg_ledge: LocationData(32587525, LocType.Cog),
    location_name.c_pwg_secret: LocationData(32587511, LocType.Artifact),
    location_name.c_bs_podium: LocationData(1043571, LocType.Podium),
    location_name.c_bs_secret_r: LocationData(32567992, LocType.Artifact),
    location_name.c_bs_secret_t: LocationData(32579724, LocType.Cog),
    location_name.a_rrp_l: LocationData(32568029, LocType.Cog),
    location_name.a_rrp_r: LocationData(32568201, LocType.Cog),
    location_name.c_cic_end: LocationData(32577629, LocType.Cog),
    location_name.c_cic_top_secret: LocationData(32579771, LocType.Artifact),
    location_name.a_cp_from_wp: LocationData(32568172, LocType.Artifact),
    location_name.c_tbr_reward: LocationData(32569676, LocType.Cog),
    location_name.y_up_lake_t: LocationData(32589038, LocType.Artifact),
    location_name.y_up_lake_r: LocationData(32589008, LocType.Cog),
    location_name.y_up_luke_yonker: LocationData(32588814, LocType.Upgrade),
    location_name.a_wall: LocationData(32566248, LocType.Cog),
    location_name.a_bwall_entr: LocationData(32592321, LocType.Cog),
    location_name.a_bwall_l: LocationData(32575375, LocType.Cog),
    location_name.a_josh_yonker: LocationData(32592305, LocType.Upgrade),
    location_name.c_tb_end: LocationData(32577477, LocType.Cog),
    location_name.c_ms_podium: LocationData(32579374, LocType.Podium),
    location_name.c_ms_top: LocationData(32579539, LocType.Artifact),
    location_name.c_ms_end: LocationData(32579537, LocType.Cog),
    location_name.c_rrh_end: LocationData(32569704, LocType.Cog),
    location_name.c_rrh_top: LocationData(32588914, LocType.Cog),
    location_name.c_rrh_right: LocationData(32575335, LocType.Artifact),
    location_name.o_top: LocationData(32591507, LocType.Artifact),
    location_name.c_rs_podium: LocationData(32566920, LocType.Podium),
    location_name.c_rs_secret_r: LocationData(32587334, LocType.Artifact),
    location_name.c_rs_end: LocationData(32586924, LocType.Cog),
    location_name.a_lmo_ceiling: LocationData(32568333, LocType.Cog),
    location_name.a_b_l: LocationData(32581716, LocType.Cog),
    location_name.a_b_r: LocationData(32581714, LocType.Artifact),
    location_name.a_b_m: LocationData(32581715, LocType.Cog),
    location_name.a_b_jet_b: LocationData(32581136, LocType.Cog),
    location_name.a_b_jet_end: LocationData(32589845, LocType.Cog),
    location_name.c_mc_podium: LocationData(32569115, LocType.Podium),
    location_name.c_mc_top: LocationData(32586900, LocType.Cog),
    location_name.totd_upper_m: LocationData(32588558, LocType.Cog),
    location_name.totd_upper_r: LocationData(32588447, LocType.Cog),
    location_name.totd_entrance_top: LocationData(32581026, LocType.Cog),
    location_name.c_dc_bottom: LocationData(32586013, LocType.Artifact),
    location_name.totd_es_maze: LocationData(32578060, LocType.Cog),
    location_name.c_tb_top_r: LocationData(32577739, LocType.Cog),
    location_name.c_tb_top_l: LocationData(32577792, LocType.Artifact),
    location_name.totd_cm_m: LocationData(32583402, LocType.Cog),
    location_name.totd_cm_end_t: LocationData(32583157, LocType.Cog),
    location_name.totd_cm_end_b: LocationData(32587497, LocType.Artifact),
    location_name.c_fil_end: LocationData(32603123, LocType.Cog),
    location_name.c_fil_perfect: LocationData(32603159, LocType.Artifact),
    location_name.totd_ga: LocationData(32585973, LocType.Artifact),
    location_name.c_ls_ledge_r: LocationData(32585999, LocType.Cog),
    location_name.c_ls_end_secret: LocationData(32587498, LocType.Artifact),
    location_name.c_ls_end: LocationData(32585844, LocType.Cog),
    location_name.c_rr_secret_l: LocationData(32607900, LocType.Cog),
    location_name.c_rr_end: LocationData(32608097, LocType.Cog),
    location_name.c_gh_secret_left: LocationData(32588357, LocType.Artifact),
    location_name.c_gh_end: LocationData(32588269, LocType.Cog),
    location_name.c_sac_secret_r: LocationData(32588005, LocType.Cog),
    location_name.c_sac_secret_t: LocationData(32587613, LocType.Artifact),
    location_name.c_sac_end: LocationData(32587611, LocType.Cog),
    location_name.totd_bowels_l: LocationData(32581157, LocType.Cog),
    location_name.totd_bowels_m: LocationData(32588778, LocType.Cog),
    location_name.c_cs_podium: LocationData(32575326, LocType.Podium),
    location_name.c_cs_secret_l: LocationData(32587113, LocType.Cog),
    location_name.c_rtc_podium: LocationData(32588107, LocType.Podium),
    location_name.c_rtc_secret_1: LocationData(32588108, LocType.Cog),
    location_name.c_rtc_secret_2: LocationData(32588109, LocType.Cog),
    location_name.c_rtc_secret_3: LocationData(32588110, LocType.Cog),
    location_name.totd_river_t: LocationData(32584270, LocType.Cog),
    location_name.c_ic_secret_r: LocationData(32597482, LocType.Artifact),
    location_name.c_ic_end: LocationData(32592847, LocType.Cog),
    location_name.totd_river_b_l: LocationData(32586334, LocType.Cog),
    location_name.totd_river_b_b: LocationData(32586044, LocType.Artifact),
    location_name.totd_river_b_r: LocationData(32586872, LocType.Cog),
    location_name.totd_river_b_t: LocationData(32591410, LocType.Artifact),
    location_name.c_mm_reward_1: LocationData(32587482, LocType.Cog),
    location_name.c_mm_reward_2: LocationData(32592316, LocType.Cog),
    location_name.c_mm_reward_3: LocationData(32587481, LocType.Artifact),
    location_name.c_sa_podium: LocationData(32592366, LocType.Podium),
    location_name.tog_cistern_l: LocationData(32589310, LocType.Cog),
    location_name.tog_cistern_r: LocationData(32592319, LocType.Artifact),
    location_name.tog_cistern_m: LocationData(32582465, LocType.Cog),
    location_name.c_cos_podium: LocationData(32581915, LocType.Podium),
    location_name.c_cos_wall_l: LocationData(32581912, LocType.Artifact),
    location_name.c_cos_end: LocationData(32587946, LocType.Cog),
    location_name.c_coa_secret: LocationData(32584808, LocType.Artifact),
    location_name.c_coa_end: LocationData(32586196, LocType.Cog),
    location_name.c_cow_secret: LocationData(32582093, LocType.Artifact),
    location_name.c_cow_end: LocationData(32582090, LocType.Cog),
    location_name.y_lower_below_acid_l: LocationData(32592346, LocType.Artifact),
    location_name.y_lower_bouncy_ceil: LocationData(32592481, LocType.Cog),
    location_name.y_lower_above_mm: LocationData(32587526, LocType.Cog),
    location_name.y_lower_mm_l: LocationData(32592328, LocType.Artifact),
    location_name.c_sss_secret_r: LocationData(32595773, LocType.Artifact),
    location_name.c_sss_secret_l: LocationData(32595874, LocType.Cog),
    location_name.c_sss_end: LocationData(32595711, LocType.Cog),
    location_name.c_srb_r: LocationData(32587619, LocType.Cog),
    location_name.c_srb_m: LocationData(32587589, LocType.Cog),
    location_name.c_ll_secret_b: LocationData(32603614, LocType.Artifact),
    location_name.c_ll_end: LocationData(32603664, LocType.Cog),
    location_name.c_ll_secret_t: LocationData(32603645, LocType.Cog),
    location_name.c_hph_secret: LocationData(32596502, LocType.Artifact),
    location_name.c_hph_end: LocationData(32596938, LocType.Cog),
    location_name.c_mms_secret: LocationData(32598464, LocType.Artifact),
    location_name.c_mms_end: LocationData(32598353, LocType.Cog),
    location_name.c_bb_secret: LocationData(32597381, LocType.Artifact),
    location_name.c_bb_end: LocationData(32597333, LocType.Cog),
    location_name.c_lime_loop_end: LocationData(32596725, LocType.Cog),
    location_name.c_lime_loop_secret: LocationData(32596733, LocType.Artifact),
    location_name.c_as_podium: LocationData(32587938, LocType.Podium),
    location_name.c_as_end: LocationData(32588510, LocType.Cog),
    location_name.c_as_secret: LocationData(32588423, LocType.Cog),
    location_name.c_hell_end: LocationData(32596828, LocType.Artifact),

    location_name.wd_start_cliff_ore: LocationData(counter.count(), LocType.Resource),
    location_name.gt_tut_podium_water_ore: LocationData(counter.count(), LocType.Resource),
    location_name.c_tt_3: LocationData(counter.count(), LocType.Resource),
    location_name.c_rf_3: LocationData(counter.count(), LocType.Resource),
    location_name.c_bs_podium_ore: LocationData(counter.count(), LocType.Resource),
}

counter = Counter(id_start + 0x100 - 1)
shop_locs: Dict[str, LocationData] = {
    location_name.em_heisenberg: LocationData(counter.count(), LocType.Upgrade),
    # location_name.em_carson_1: LocationData(counter.count(), LocType.Cog),
    # location_name.em_carson_2: LocationData(counter.count(), LocType.Cog),
    # location_name.em_carson_3: LocationData(counter.count(), LocType.Cog),
    # location_name.em_carson_4: LocationData(counter.count(), LocType.Cog),
    # location_name.em_carson_5: LocationData(counter.count(), LocType.Cog),
    # location_name.em_carson_6: LocationData(counter.count(), LocType.Cog),
    # location_name.em_carson_7: LocationData(counter.count(), LocType.Cog),
    location_name.em_artifact_1: LocationData(counter.count(8), LocType.Upgrade),
    location_name.em_artifact_3: LocationData(counter.count(), LocType.Upgrade),
    location_name.em_artifact_6: LocationData(counter.count(), LocType.Upgrade),
    location_name.em_artifact_10: LocationData(counter.count(), LocType.Upgrade),
    location_name.em_artifact_15: LocationData(counter.count(), LocType.Upgrade),
    location_name.em_artifact_21: LocationData(counter.count(), LocType.Upgrade),
    location_name.em_artifact_28: LocationData(counter.count(), LocType.Upgrade),
    location_name.em_artifact_42: LocationData(counter.count(), LocType.Upgrade),
    location_name.em_pickaxe_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_pickaxe_3: LocationData(counter.count(), LocType.Shop),
    location_name.em_pickaxe_4: LocationData(counter.count(), LocType.Shop),
    location_name.em_pickaxe_5: LocationData(counter.count(), LocType.Shop),
    location_name.em_pickaxe_6: LocationData(counter.count(), LocType.Shop),
    location_name.em_pickaxe_7: LocationData(counter.count(), LocType.Shop),
    location_name.em_pickaxe_8: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_3: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_4: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_5: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_6: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_7: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_8: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_9: LocationData(counter.count(), LocType.Shop),
    location_name.em_backpack_10: LocationData(counter.count(), LocType.Shop),
    location_name.em_lamp_1: LocationData(counter.count(), LocType.Shop),
    location_name.em_lamp_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_lamp_3: LocationData(counter.count(), LocType.Shop),
    location_name.em_lamp_4: LocationData(counter.count(), LocType.Shop),
    location_name.em_lamp_5: LocationData(counter.count(), LocType.Shop),
    location_name.em_lamp_6: LocationData(counter.count(), LocType.Shop),
    location_name.em_lamp_7: LocationData(counter.count(), LocType.Shop),
    location_name.em_armor_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_armor_3: LocationData(counter.count(), LocType.Shop),
    location_name.em_armor_4: LocationData(counter.count(), LocType.Shop),
    location_name.em_armor_5: LocationData(counter.count(), LocType.Shop),
    location_name.em_armor_6: LocationData(counter.count(), LocType.Shop),
    location_name.em_armor_7: LocationData(counter.count(), LocType.Shop),
    location_name.em_armor_8: LocationData(counter.count(), LocType.Shop),
    location_name.em_tank_1: LocationData(counter.count(), LocType.Shop),
    location_name.em_tank_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_tank_3: LocationData(counter.count(), LocType.Shop),
    location_name.em_tank_4: LocationData(counter.count(), LocType.Shop),
    location_name.em_tank_5: LocationData(counter.count(), LocType.Shop),
    location_name.em_bomb_1: LocationData(counter.count(), LocType.Shop),
    location_name.em_bomb_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_bomb_3: LocationData(counter.count(), LocType.Shop),
    location_name.em_bomb_4: LocationData(counter.count(), LocType.Shop),
    location_name.em_hammer_1: LocationData(counter.count(), LocType.Shop),
    location_name.em_hammer_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_hammer_3: LocationData(counter.count(), LocType.Shop),
    location_name.em_hammer_4: LocationData(counter.count(), LocType.Shop),
    location_name.em_jetpack_1: LocationData(counter.count(), LocType.Shop),
    location_name.em_jetpack_2: LocationData(counter.count(), LocType.Shop),
    location_name.em_jetpack_3: LocationData(counter.count(), LocType.Shop),
}


all_locations: Dict[str, LocationData] = {
    **default_locs,
    **shop_locs,
}

artifact_locations = [loc for loc, data in all_locations.items() if data.loc_type == LocType.Artifact]


def setup_locations(world: "SWD2World"):
    active_locations: Set[str] = set()
    event_locations: Set[str] = set()
    item_counts: Dict[str, int]

    item_counts, extra_items = get_item_counts(world)

    disallowed_types = [
        LocType.Resource,
    ]

    if not world.options.randomize_cogs:
        disallowed_types.append(LocType.Cog)
    if not world.options.randomize_artifacts:
        disallowed_types.append(LocType.Artifact)
    if world.options.randomize_shops != world.options.randomize_shops.option_randomize:
        disallowed_types.append(LocType.Shop)

    for loc, data in all_locations.items():
        if data.loc_type in disallowed_types:
            if data.loc_type == LocType.Artifact:
                event_locations.add(loc)
            continue
        active_locations.add(loc)

    # Remove unimplemented locations
    # active_locations.remove(location_name.em_carson_1)
    # active_locations.remove(location_name.em_carson_2)
    # active_locations.remove(location_name.em_carson_3)
    # active_locations.remove(location_name.em_carson_4)
    # active_locations.remove(location_name.em_carson_5)
    # active_locations.remove(location_name.em_carson_6)
    # active_locations.remove(location_name.em_carson_7)
    if world.options.randomize_shops == world.options.randomize_shops.option_randomize:
        active_locations.remove(location_name.em_lamp_1)
        active_locations.remove(location_name.em_tank_1)
        active_locations.remove(location_name.em_bomb_1)
        active_locations.remove(location_name.em_hammer_1)
        active_locations.remove(location_name.em_jetpack_1)
    if world.options.randomize_artifacts and not world.options.randomize_trials_reward:
        active_locations.remove(location_name.c_hell_end)

    return active_locations, event_locations, item_counts


lookup_id_to_name: Dict[int, str] = {data.code: item_name for item_name, data in all_locations.items() if data.code}
