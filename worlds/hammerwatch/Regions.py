import typing
from collections import namedtuple
from random import Random

from BaseClasses import MultiWorld, Region, Entrance
from .Items import HammerwatchItem
from .Locations import HammerwatchLocation, LocationData, LocationClassification
from .Names import CastleLocationNames, TempleLocationNames, ItemName, CastleRegionNames, TempleRegionNames, GateNames,\
    EntranceNames
from .Util import *


class DoorType(Enum):
    Bronze = 0
    Silver = 1
    Gold = 2
    Bonus = 3


HWExitData = namedtuple("HWExitData",
                        ["parent", "target", "return_code", "exit_code", "pass_item", "item_count", "items_consumed"])


class HWEntrance(Entrance):
    visited = False
    target_region: Region
    pass_item: str
    item_count: int
    items_consumed: bool
    return_code: str
    exit_code: str

    linked = True
    downstream_count: int = 0

    def __init__(self, player: int, name: str = "", parent: Region = None, target: Region = None,
                 pass_item: str = None, item_count=0, items_consumed=True,
                 return_code: str = None, exit_code: str = None):
        super().__init__(player, name, parent)
        self.target_region = target
        self.pass_item = pass_item
        self.item_count = item_count
        self.items_consumed = items_consumed
        self.return_code = return_code
        self.exit_code = exit_code


def create_regions(multiworld, map: Campaign, player: int, active_locations: typing.Dict[str, LocationData],
                   random_locations: typing.Dict[str, int]):
    gate_codes = {}
    if map == Campaign.Castle:
        create_castle_regions(multiworld, player, active_locations, random_locations)
        connect_castle_regions(multiworld, player, random_locations, gate_codes)
    else:
        create_tots_regions(multiworld, player, active_locations, random_locations)
        connect_tots_regions(multiworld, player, random_locations, gate_codes)
    return gate_codes


def create_castle_regions(multiworld: MultiWorld, player: int, active_locations: typing.Dict[str, LocationData],
                          random_locations: typing.Dict[str, int]):
    menu_region = create_region(multiworld, player, active_locations, CastleRegionNames.menu, None)
    hub_region = create_region(multiworld, player, active_locations, CastleRegionNames.hub, None)

    p1_start_locations = [
        CastleLocationNames.p1_by_nw_bronze_gate,
        CastleLocationNames.btn_p1_floor,
    ]
    p1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_start,
                                    p1_start_locations)

    p1_nw_locs = [
        CastleLocationNames.p1_entrance_1,
        CastleLocationNames.p1_entrance_2,
        CastleLocationNames.p1_entrance_3,
        CastleLocationNames.p1_entrance_4,
        CastleLocationNames.p1_entrance_hall_1,
        CastleLocationNames.p1_entrance_hall_2,
        CastleLocationNames.p1_entrance_s,
        CastleLocationNames.p1_entrance_w,
        CastleLocationNames.p1_entrance_secret,
    ]
    p1_nw_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_nw, p1_nw_locs)

    p1_s_locations = [
        CastleLocationNames.p1_by_sw_bronze_gate_1,
        CastleLocationNames.p1_by_sw_bronze_gate_2,
        CastleLocationNames.p1_by_sw_bronze_gate_3,
        CastleLocationNames.p1_by_sw_bronze_gate_4,
        CastleLocationNames.p1_s_lower_hall_1,
        CastleLocationNames.p1_s_lower_hall_2,
        CastleLocationNames.p1_s_lower_hall_3,
        CastleLocationNames.p1_s_lower_hall_4,
        CastleLocationNames.p1_s_lower_hall_5,
        CastleLocationNames.p1_s_lower_hall_6,
        CastleLocationNames.p1_s_lower_hall_7,
        CastleLocationNames.p1_s_lower_hall_8,
        CastleLocationNames.p1_s_lower_hall_9,
        CastleLocationNames.p1_s_lower_hall_10,
        CastleLocationNames.p1_e_save_room_1,
        CastleLocationNames.p1_e_save_room_2,
        CastleLocationNames.p1_w_of_se_bronze_gate_1,
        CastleLocationNames.p1_w_of_se_bronze_gate_2,
        CastleLocationNames.p1_w_of_se_bronze_gate_3,
        CastleLocationNames.p1_w_of_se_bronze_gate_4,
        CastleLocationNames.p1_w_of_se_bronze_gate_5,
        CastleLocationNames.p1_s_w_bridges_w,
        CastleLocationNames.p1_s_of_e_save_room,
        CastleLocationNames.p1_n_of_se_bridge,
        CastleLocationNames.p1_w_save,
        CastleLocationNames.p1_center_bridges_n_1,
        CastleLocationNames.p1_center_bridges_n_2,
        CastleLocationNames.p1_center_bridges_n_3,
        CastleLocationNames.p1_center_bridges_s_1,
        CastleLocationNames.p1_center_bridges_s_2,
        CastleLocationNames.p1_center_bridges_s_3,
        CastleLocationNames.p1_center_bridges_s_4,
        CastleLocationNames.p1_e_secret,
        CastleLocationNames.p1_s_secret_1,
        CastleLocationNames.p1_s_secret_2,
        CastleLocationNames.p1_se_bridge,
    ]
    p1_s_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_s, p1_s_locations)

    p1_sw_bronze_gate_locations = [
        CastleLocationNames.p1_sw_bronze_gate,
    ]
    p1_sw_bronze_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_sw_bronze_gate,
                                             p1_sw_bronze_gate_locations)

    p1_e_locations = [
        CastleLocationNames.p1_by_exit_1,
        CastleLocationNames.p1_by_exit_2,
        CastleLocationNames.p1_by_exit_3,
        CastleLocationNames.p1_by_m_bronze_gate_1,
        CastleLocationNames.p1_by_m_bronze_gate_2,
        CastleLocationNames.p1_by_m_bronze_gate_3,
        CastleLocationNames.p1_by_m_bronze_gate_4,
        CastleLocationNames.p1_by_m_bronze_gate_5,
        CastleLocationNames.p1_by_m_bronze_gate_6,
        CastleLocationNames.p1_e_bridges_1,
        CastleLocationNames.p1_e_bridges_2,
        CastleLocationNames.p1_e_bridges_3,
        CastleLocationNames.p1_e_bridges_4,
        CastleLocationNames.p1_e_bridges_5,
        CastleLocationNames.p1_room_by_exit,
        CastleLocationNames.p1_ne_arrow_traps,
        CastleLocationNames.p1_hint_room,
    ]
    p1_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_e, p1_e_locations)

    p1_m_bronze_gate_locations = [
        CastleLocationNames.p1_m_bronze_gate,
    ]
    p1_m_bronze_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_m_bronze_gate,
                                            p1_m_bronze_gate_locations)

    p1_from_p2_locations = [
        CastleLocationNames.p1_bars_1,
        CastleLocationNames.p1_bars_2,
        CastleLocationNames.p1_p2_by_shop,
    ]
    p1_from_p2_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_from_p2,
                                      p1_from_p2_locations)

    p1_from_p3_n_locations = [
        CastleLocationNames.p1_p3_n_bridge,
        CastleLocationNames.p1_p3_n_across_bridge,
        CastleLocationNames.ev_p1_boss_switch
    ]
    p1_from_p3_n_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_from_p3_n,
                                        p1_from_p3_n_locations)

    p1_from_p3_s_locations = [
        CastleLocationNames.p1_p3_s,
    ]
    p1_from_p3_s_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_from_p3_s,
                                        p1_from_p3_s_locations)

    p2_start_locations = []
    p2_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_start,
                                    p2_start_locations)

    p2_m_locations = [
        CastleLocationNames.p2_w_of_silver_gate_1,
        CastleLocationNames.p2_w_of_silver_gate_2,
        CastleLocationNames.p2_nw_island_s_1,
        CastleLocationNames.p2_nw_island_s_2,
        CastleLocationNames.p2_entrance_1,
        CastleLocationNames.p2_entrance_2,
        CastleLocationNames.p2_entrance_3,
        CastleLocationNames.p2_entrance_4,
        CastleLocationNames.p2_entrance_5,
        CastleLocationNames.p2_w_of_gold_gate,
        CastleLocationNames.p2_nw_island_1,
        CastleLocationNames.p2_nw_island_2,
        CastleLocationNames.p2_nw_island_3,
        CastleLocationNames.p2_nw_island_4,
        CastleLocationNames.p2_nw_island_5,
    ]
    p2_m_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_m, p2_m_locations)

    p2_p1_return_locs = [
    ]
    p2_p1_return_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_p1_return,
                                        p2_p1_return_locs)

    p2_n_locations = [
        CastleLocationNames.p2_spike_puzzle_e_1,
        CastleLocationNames.p2_spike_puzzle_e_2,
        CastleLocationNames.p2_spike_puzzle_ne_1,
        CastleLocationNames.p2_spike_puzzle_ne_2,
        CastleLocationNames.p2_spike_puzzle_ne_3,
        CastleLocationNames.p2_spike_puzzle_e,
    ]
    p2_n_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_n, p2_n_locations)

    p2_spike_puzzle_bottom_locs = [
    ]
    p2_spike_puzzle_bottom_region = create_region(multiworld, player, active_locations,
                                                  CastleRegionNames.p2_spike_puzzle_bottom,
                                                  p2_spike_puzzle_bottom_locs)

    p2_spike_puzzle_left_locs = [
        CastleLocationNames.p2_spike_puzzle_w_1,
        CastleLocationNames.p2_spike_puzzle_w_2,
    ]
    p2_spike_puzzle_left_region = create_region(multiworld, player, active_locations,
                                                CastleRegionNames.p2_spike_puzzle_left,
                                                p2_spike_puzzle_left_locs)

    p2_spike_puzzle_top_locs = [
        CastleLocationNames.p2_spike_puzzle_n_1,
        CastleLocationNames.p2_spike_puzzle_n_2,
    ]
    p2_spike_puzzle_top_region = create_region(multiworld, player, active_locations,
                                               CastleRegionNames.p2_spike_puzzle_top,
                                               p2_spike_puzzle_top_locs)

    p2_red_switch_locations = [
        CastleLocationNames.p2_by_red_spikes_1,
        CastleLocationNames.p2_by_red_spikes_2,
        CastleLocationNames.p2_by_red_spikes_3,
        CastleLocationNames.p2_e_poker_plant_room_1,
        CastleLocationNames.p2_e_poker_plant_room_2,
        CastleLocationNames.p2_e_poker_plant_room_3,
        CastleLocationNames.p2_e_poker_plant_room_4,
        CastleLocationNames.p2_e_poker_plant_room_5,
        CastleLocationNames.p2_e_poker_plant_room_6,
        CastleLocationNames.p2_e_of_red_spikes_1,
        CastleLocationNames.p2_e_of_red_spikes_2,
        CastleLocationNames.p2_e_of_red_spikes_3,
        CastleLocationNames.p2_e_of_red_spikes_4,
        CastleLocationNames.p2_e_of_ne_save_1,
        CastleLocationNames.p2_e_of_ne_save_2,
        CastleLocationNames.p2_tower_plant_2,
    ]
    p2_red_switch_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_red_switch,
                                         p2_red_switch_locations)

    p2_puzzle_locs = [
        CastleLocationNames.p2_puzzle_1,
        CastleLocationNames.p2_puzzle_2,
        CastleLocationNames.p2_puzzle_3,
        CastleLocationNames.p2_puzzle_4,
    ]
    p2_puzzle_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_puzzle, p2_puzzle_locs)

    p2_e_bronze_gate_locations = [
        # Offense shop
    ]
    p2_e_bronze_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_e_bronze_gate,
                                            p2_e_bronze_gate_locations)

    p2_e_save_locs = [
        CastleLocationNames.p2_e_save,
    ]
    p2_e_save_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_e_save, p2_e_save_locs)

    p2_s_locations = [
        CastleLocationNames.p2_big_bridge_1,
        CastleLocationNames.p2_big_bridge_2,
        CastleLocationNames.p2_big_bridge_3,
        CastleLocationNames.p2_s_arrow_traps_1,
        CastleLocationNames.p2_s_arrow_traps_2,
        CastleLocationNames.p2_s_arrow_traps_3,
        CastleLocationNames.p2_e_gold_gate_room_1,
        CastleLocationNames.p2_e_gold_gate_room_2,
        CastleLocationNames.p2_e_gold_gate_room_3,
        CastleLocationNames.p2_e_gold_gate_room_4,
        CastleLocationNames.p2_e_gold_gate_room_5,
        CastleLocationNames.p2_e_gold_gate_room_6,
        CastleLocationNames.p2_e_gold_gate_room_7,
        CastleLocationNames.p2_e_gold_gate_room_8,
        CastleLocationNames.p2_e_gold_gate_room_9,
        CastleLocationNames.p2_e_gold_gate_room_10,
        CastleLocationNames.p2_e_gold_gate_room_11,
        CastleLocationNames.p2_e_gold_gate_room_12,
        CastleLocationNames.p2_e_gold_gate_room_13,
        CastleLocationNames.p2_beetle_boss_room_1,
        CastleLocationNames.p2_beetle_boss_room_2,
        CastleLocationNames.p2_beetle_boss_room_3,
        CastleLocationNames.p2_beetle_boss_room_4,
        CastleLocationNames.p2_w_poker_plant_room_1,
        CastleLocationNames.p2_w_poker_plant_room_2,
        CastleLocationNames.p2_w_poker_plant_room_3,
        CastleLocationNames.p2_s_of_w_gold_gate_1,
        CastleLocationNames.p2_s_of_w_gold_gate_2,
        CastleLocationNames.p2_s_of_w_gold_gate_3,
        CastleLocationNames.p2_by_boss_switch,
        CastleLocationNames.p2_toggle_spike_trap_reward_1,
        CastleLocationNames.p2_toggle_spike_trap_reward_2,
        CastleLocationNames.p2_toggle_spike_trap_reward_3,
        CastleLocationNames.p2_miniboss_tick_1,
        CastleLocationNames.p2_miniboss_tick_2,
        CastleLocationNames.p2_tower_plant_1,
        CastleLocationNames.ev_p2_gold_gate_room_sw_switch,
        CastleLocationNames.ev_p2_boss_switch,
    ]
    p2_s_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_s, p2_s_locations)

    p2_e_bronze_gate_2_locations = [
        CastleLocationNames.ev_p2_gold_gate_room_ne_switch
    ]
    p2_e_bronze_gate_2_region = create_region(multiworld, player, active_locations,
                                              CastleRegionNames.p2_e_bronze_gate_2,
                                              p2_e_bronze_gate_2_locations)

    p2_m_bronze_gate_locations = [
        CastleLocationNames.ev_p2_gold_gate_room_nw_switch
    ]
    p2_m_bronze_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_m_bronze_gate,
                                            p2_m_bronze_gate_locations)

    p2_se_bronze_gate_locations = [
        CastleLocationNames.ev_p2_gold_gate_room_se_switch
    ]
    p2_se_bronze_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_se_bronze_gate,
                                             p2_se_bronze_gate_locations)

    p2_gg_room_reward_locations = [
        CastleLocationNames.p2_e_gold_gate_room_reward_1,
        CastleLocationNames.p2_e_gold_gate_room_reward_2,
    ]
    p2_gg_room_reward_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_gg_room_reward,
                                             p2_gg_room_reward_locations)

    p2_w_treasure_locs = [
        CastleLocationNames.p2_beetle_boss_hidden_room_1,
    ]
    p2_w_treasure_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_w_treasure,
                                         p2_w_treasure_locs)

    p2_w_treasure_tp_locs = [
        CastleLocationNames.p2_beetle_boss_hidden_room_2,
    ]
    p2_w_treasure_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_w_treasure_tp,
                                            p2_w_treasure_tp_locs)

    p2_tp_puzzle_locs = [
        CastleLocationNames.p2_sequence_puzzle_reward,
    ]
    p2_tp_puzzle_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_tp_puzzle,
                                        p2_tp_puzzle_locs)

    p2_end_locations = [
        CastleLocationNames.p2_end_1,
        CastleLocationNames.p2_end_2,
    ]
    p2_end_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_end, p2_end_locations)

    p3_start_door_locs = [
    ]
    p3_start_door_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_start_door,
                                         p3_start_door_locs)

    p3_start_locs = [
        CastleLocationNames.p3_entrance_s_of_poker_1,
        CastleLocationNames.p3_entrance_s_of_poker_2,
        CastleLocationNames.p3_entrance_s_of_poker_3,
        CastleLocationNames.p3_entrance_w,
        CastleLocationNames.p3_entrance_n_1,
        CastleLocationNames.p3_entrance_n_2,
        CastleLocationNames.p3_entrance_n_of_poker,
        CastleLocationNames.p3_entrance_sw,
        CastleLocationNames.p3_entrance_m_1,
        CastleLocationNames.p3_entrance_m_2,
        CastleLocationNames.p3_entrance_m_3,
        CastleLocationNames.p3_entrance_m_4,
        CastleLocationNames.p3_entrance_s_1,
        CastleLocationNames.p3_entrance_s_2,
        CastleLocationNames.p3_entrance_s_3,
        CastleLocationNames.p3_nw_n_1,
        CastleLocationNames.p3_nw_n_2,
        CastleLocationNames.p3_nw_nw_1,
        CastleLocationNames.p3_nw_nw_2,
        CastleLocationNames.p3_nw_nw_3,
        CastleLocationNames.p3_nw_m,
        CastleLocationNames.p3_nw_sw_1,
        CastleLocationNames.p3_nw_sw_2,
        CastleLocationNames.p3_nw_se,
        CastleLocationNames.p3_nw_closed_room,
        CastleLocationNames.p3_tower_plant_1,
    ]
    p3_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_start, p3_start_locs)

    p3_nw_closed_room_locs = [
    ]
    p3_nw_closed_room_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_nw_closed_room,
                                             p3_nw_closed_room_locs)

    p3_nw_n_bronze_gate_locs = [
        CastleLocationNames.p3_nw_n_bronze_gate_1,
        CastleLocationNames.p3_nw_n_bronze_gate_2,
        CastleLocationNames.p3_nw_n_bronze_gate_3,
        CastleLocationNames.p3_nw_n_bronze_gate_4,
        CastleLocationNames.p3_nw_n_bronze_gate_5,
    ]
    p3_nw_n_bronze_gate_region = create_region(multiworld, player, active_locations,
                                               CastleRegionNames.p3_nw_n_bronze_gate, p3_nw_n_bronze_gate_locs)

    p3_nw_s_bronze_gate_locs = [
        CastleLocationNames.p3_nw_s_bronze_gate_1,
        CastleLocationNames.p3_nw_s_bronze_gate_2,
        CastleLocationNames.p3_nw_s_bronze_gate_3,
        CastleLocationNames.p3_nw_s_bronze_gate_4,
        CastleLocationNames.p3_nw_s_bronze_gate_5,
    ]
    p3_nw_s_bronze_gate_region = create_region(multiworld, player, active_locations,
                                               CastleRegionNames.p3_nw_s_bronze_gate, p3_nw_s_bronze_gate_locs)

    p3_s_bronze_gate_locs = [
    ]
    p3_s_bronze_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_s_bronze_gate,
                                            p3_s_bronze_gate_locs)

    p3_silver_gate_locs = [
        CastleLocationNames.p3_s_of_silver_gate,
    ]
    p3_silver_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_silver_gate,
                                          p3_silver_gate_locs)

    p3_n_gold_gate_locs = [
        CastleLocationNames.p3_by_w_shop,
        CastleLocationNames.p3_ne_se_1,
        CastleLocationNames.p3_ne_se_2,
        CastleLocationNames.p3_se_cross_hall_e_1,
        CastleLocationNames.p3_se_cross_hall_e_2,
        CastleLocationNames.p3_se_cross_hall_s_1,
        CastleLocationNames.p3_se_cross_hall_s_2,
        CastleLocationNames.p3_se_cross_hall_s_3,
        CastleLocationNames.p3_se_cross_hall_s_4,
        CastleLocationNames.p3_se_cross_hall_se,
        CastleLocationNames.p3_arrow_hall_1,
        CastleLocationNames.p3_arrow_hall_2,
        CastleLocationNames.p3_se_m_1,
        CastleLocationNames.p3_se_m_2,
        CastleLocationNames.p3_ne_e_1,
        CastleLocationNames.p3_ne_e_2,
        CastleLocationNames.p3_ne_e_3,
        CastleLocationNames.p3_ne_e_4,
        CastleLocationNames.p3_s_of_e_poker_1,
        CastleLocationNames.p3_s_of_e_poker_2,
        CastleLocationNames.p3_se_of_w_shop,
        CastleLocationNames.p3_sw_of_w_shop,
        CastleLocationNames.p3_miniboss_tick_1,
        CastleLocationNames.p3_miniboss_tick_2,
        CastleLocationNames.p3_tower_plant_2,
        CastleLocationNames.p3_tower_plant_5,
        CastleLocationNames.p3_tower_plant_6,
        CastleLocationNames.p3_tower_plant_7,
    ]
    p3_n_gold_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_n_gold_gate,
                                          p3_n_gold_gate_locs)

    p3_rspikes_locs = [
        CastleLocationNames.p3_red_spike_room,
    ]
    p3_rspikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_rspikes,
                                      p3_rspikes_locs)

    p3_rspikes_room_locs = [
        CastleLocationNames.p3_tower_plant_4,
    ]
    p3_rspikes_room_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_rspikes_room,
                                           p3_rspikes_room_locs)

    p3_bonus_locs = [
    ]
    p3_bonus_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_bonus, p3_bonus_locs)

    p3_arrow_hall_secret_locs = [
        CastleLocationNames.btnc_p3_arrow_hall_wall,
    ]
    p3_arrow_hall_secret_region = create_region(multiworld, player, active_locations,
                                                CastleRegionNames.p3_arrow_hall_secret, p3_arrow_hall_secret_locs)

    p3_spikes_s_locs = [
        CastleLocationNames.p3_spike_trap_1,
        CastleLocationNames.p3_spike_trap_2,
        CastleLocationNames.p3_spike_trap_3,
        CastleLocationNames.p3_by_m_shop_1,
        CastleLocationNames.p3_by_m_shop_2,
    ]
    p3_spikes_s_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_spikes_s,
                                       p3_spikes_s_locs)

    p3_sw_locs = [
        CastleLocationNames.p3_ne_of_bridge_1,
        CastleLocationNames.p3_ne_of_bridge_2,
        CastleLocationNames.p3_w_of_w_poker,
        CastleLocationNames.p3_s_of_w_poker,
        CastleLocationNames.p3_nw_of_bridge,
        CastleLocationNames.p3_n_of_bridge_1,
        CastleLocationNames.p3_n_of_bridge_2,
        CastleLocationNames.p3_n_of_bridge_3,
        CastleLocationNames.p3_n_of_bridge_4,
        CastleLocationNames.p3_n_of_bridge_5,
        CastleLocationNames.p3_w_of_bridge,
        CastleLocationNames.p3_e_of_bridge_1,
        CastleLocationNames.p3_e_of_bridge_2,
        CastleLocationNames.p3_e_of_bridge_3,
        CastleLocationNames.p3_s_of_boss_door,
        CastleLocationNames.p3_tower_plant_3,
        CastleLocationNames.p3_tower_plant_8,
        CastleLocationNames.btnc_p3_sw,
    ]
    p3_sw_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_sw, p3_sw_locs)

    p3_exit_s_locs = [
    ]
    p3_exit_s_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_exit_s, p3_exit_s_locs)

    p3_hidden_arrow_hall_locs = [
        CastleLocationNames.p3_secret_secret,
        CastleLocationNames.p3_secret_arrow_hall_1,
        CastleLocationNames.p3_secret_arrow_hall_2,
    ]
    p3_hidden_arrow_hall_region = create_region(multiworld, player, active_locations,
                                                CastleRegionNames.p3_hidden_arrow_hall, p3_hidden_arrow_hall_locs)

    p3_s_gold_gate_locs = [
        CastleLocationNames.ev_p3_boss_switch
    ]
    p3_s_gold_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_s_gold_gate,
                                          p3_s_gold_gate_locs)

    p3_bonus_return_locs = [
        CastleLocationNames.p3_bonus_return,
    ]
    p3_bonus_return_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_bonus_return,
                                           p3_bonus_return_locs)

    if multiworld.shortcut_teleporter[player]:
        p3_portal_from_p1_locs = [
            CastleLocationNames.p3_skip_boss_switch_1,
            CastleLocationNames.p3_skip_boss_switch_2,
            CastleLocationNames.p3_skip_boss_switch_3,
            CastleLocationNames.p3_skip_boss_switch_4,
            CastleLocationNames.p3_skip_boss_switch_5,
            CastleLocationNames.p3_skip_boss_switch_6,
        ]
        p3_portal_from_p1_region = create_region(multiworld, player, active_locations,
                                                 CastleRegionNames.p3_portal_from_p1, p3_portal_from_p1_locs)
        multiworld.regions.append(p3_portal_from_p1_region)

    n1_start_locs = [
        CastleLocationNames.n1_entrance
    ]
    n1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_start, n1_start_locs)

    n1_room1_locs = [
        CastleLocationNames.n1_room1
    ]
    n1_room1_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room1, n1_room1_locs)

    n1_room2_locs = [
        CastleLocationNames.n1_room2_s_1,
        CastleLocationNames.n1_room2_s_2,
        CastleLocationNames.n1_room2_s_3,
        CastleLocationNames.n1_room2_n_secret_room,
    ]
    n1_room2_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room2, n1_room2_locs)

    n1_room2_unlock_locs = [
        CastleLocationNames.n1_room2_small_box,
        CastleLocationNames.n1_room2_nw_room_1,
        CastleLocationNames.n1_room2_nw_room_2,
        CastleLocationNames.n1_room2_nw_room_3,
        CastleLocationNames.n1_room2_nw_room_4,
        CastleLocationNames.n1_room2_nw_room_5,
        CastleLocationNames.n1_room2_nw_room_6,
        CastleLocationNames.n1_room2_n_m_room_1,
        CastleLocationNames.n1_room2_n_m_room_2,
        CastleLocationNames.n1_room2_n_m_room_3,
        CastleLocationNames.n1_room2_n_m_room_4,
        CastleLocationNames.n1_room2_n_m_room_5,
        CastleLocationNames.n1_room2_n_m_room_6,
    ]
    n1_room2_unlock_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room2_unlock,
                                           n1_room2_unlock_locs)

    n1_room3_locs = [
        CastleLocationNames.n1_room3_w_1,
        CastleLocationNames.n1_room3_w_2,
        CastleLocationNames.n1_room3_w_3,
        CastleLocationNames.n1_room3_w_4,
        CastleLocationNames.n1_room3_w_5,
        CastleLocationNames.n1_room3_w_6,
        CastleLocationNames.n1_room3_w_7,
        CastleLocationNames.n1_room3_w_8,
        CastleLocationNames.n1_room3_w_9,
        CastleLocationNames.n1_room3_w_10,
        CastleLocationNames.n1_room3_w_11,
        CastleLocationNames.n1_room3_w_12,
        CastleLocationNames.n1_room3_w_13,
        CastleLocationNames.n1_room3_w_14,
        CastleLocationNames.n1_room3_w_15,
        CastleLocationNames.n1_room3_w_16,
        CastleLocationNames.n1_room3_w_17,
        CastleLocationNames.n1_room3_w_18,
        CastleLocationNames.n1_room3_w_19,
        CastleLocationNames.n1_room3_w_20,
    ]
    n1_room3_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room3, n1_room3_locs)

    n1_room3_unlock_locs = [
        CastleLocationNames.n1_room3_sealed_room_1,
        CastleLocationNames.n1_room3_sealed_room_2,
        CastleLocationNames.n1_room3_sealed_room_3,
        CastleLocationNames.n1_room3_sealed_room_4,
    ]
    n1_room3_unlock_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room3_unlock,
                                           n1_room3_unlock_locs)

    n1_room3_hall_locs = [
    ]
    n1_room3_hall_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room3_hall,
                                         n1_room3_hall_locs)

    n1_room4_locs = [
        CastleLocationNames.n1_room4_e,
        CastleLocationNames.n1_room4_m,
        CastleLocationNames.n1_room4_w_1,
        CastleLocationNames.n1_room4_w_2,
        CastleLocationNames.n1_room4_s_1,
        CastleLocationNames.n1_room4_s_2,
        CastleLocationNames.n1_room4_s_3,
    ]
    n1_room4_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room4, n1_room4_locs)

    b1_start_locs = [
        CastleLocationNames.b1_behind_portal
    ]
    b1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.b1_start, b1_start_locs)

    b1_arena_locs = [
        CastleLocationNames.b1_arena_1,
        CastleLocationNames.b1_arena_2
    ]
    b1_arena_region = create_region(multiworld, player, active_locations, CastleRegionNames.b1_arena, b1_arena_locs)

    b1_defeated_locs = [
        CastleLocationNames.b1_reward,
        CastleLocationNames.ev_beat_boss_1,
    ]
    b1_defeated_region = create_region(multiworld, player, active_locations, CastleRegionNames.b1_defeated,
                                       b1_defeated_locs)

    b1_exit_locs = [
    ]
    b1_exit_region = create_region(multiworld, player, active_locations, CastleRegionNames.b1_exit, b1_exit_locs)

    a1_start_locs = [
    ]
    a1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_start, a1_start_locs)

    a1_start_shop_w_locs = []  # Start bronze gate shop
    a1_start_shop_w_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_start_shop_w,
                                           a1_start_shop_w_locs)

    a1_start_shop_m_locs = []  # Start top gold gate shop
    a1_start_shop_m_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_start_shop_m,
                                           a1_start_shop_m_locs)

    a1_start_shop_e_locs = []  # Start bottom gold gate shop
    a1_start_shop_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_start_shop_e,
                                           a1_start_shop_e_locs)

    a1_se_locs = [
        CastleLocationNames.a1_s_save_1,
        CastleLocationNames.a1_s_save_2,
    ]
    a1_se_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_se, a1_se_locs)

    a1_e_locs = [
        CastleLocationNames.a1_m_trellis_secret,
        CastleLocationNames.a1_n_save_1,
        CastleLocationNames.a1_n_save_2,
        CastleLocationNames.a1_n_save_3,
        CastleLocationNames.a1_n_save_4,
        CastleLocationNames.a1_ne_top_room_1,
        CastleLocationNames.a1_ne_top_room_2,
        CastleLocationNames.a1_ne_top_room_3,
        CastleLocationNames.a1_e_m_1,
        CastleLocationNames.a1_e_m_2,
        CastleLocationNames.a1_e_m_3,
        CastleLocationNames.a1_n_boss_hall,
        CastleLocationNames.a1_m_ice_tower_1,
        CastleLocationNames.a1_m_ice_tower_2,
        CastleLocationNames.a1_m_ice_tower_3,
        CastleLocationNames.a1_m_ice_tower_4,
        CastleLocationNames.a1_e_n_fireball_trap,
        CastleLocationNames.a1_e_e_fireball_trap,
        CastleLocationNames.a1_e_ne,
        CastleLocationNames.a1_ne_1,
        CastleLocationNames.a1_ne_2,
        CastleLocationNames.a1_ne_3,
        CastleLocationNames.a1_e_e,
        CastleLocationNames.a1_e_se,
        CastleLocationNames.a1_ne_ice_tower_secret,
        CastleLocationNames.a1_miniboss_skeleton_1,
        CastleLocationNames.a1_miniboss_skeleton_2,
        CastleLocationNames.a1_tower_ice_3,
        CastleLocationNames.a1_tower_ice_4,
    ]
    a1_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_e, a1_e_locs)

    a1_e_sw_bgate_locs = []
    a1_e_sw_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_e_sw_bgate,
                                         a1_e_sw_bgate_locs)

    a1_e_s_bgate_locs = []
    a1_e_s_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_e_s_bgate,
                                        a1_e_s_bgate_locs)

    a1_e_se_bgate_locs = []
    a1_e_se_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_e_se_bgate,
                                         a1_e_se_bgate_locs)

    a1_e_e_bgate_locs = []
    a1_e_e_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_e_e_bgate,
                                        a1_e_e_bgate_locs)

    a1_rune_room_locs = [

    ]
    a1_rune_room_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_rune_room,
                                        a1_rune_room_locs)

    a1_se_cache_locs = [
        CastleLocationNames.a1_se_cache_1,
        CastleLocationNames.a1_se_cache_2,
        CastleLocationNames.a1_se_cache_3,
        CastleLocationNames.a1_se_cache_4,
    ]
    a1_se_cache_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_se_cache,
                                       a1_se_cache_locs)

    a1_e_ne_bgate_locs = [
        CastleLocationNames.a1_e_ne_bgate,
    ]
    a1_e_ne_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_e_ne_bgate,
                                         a1_e_ne_bgate_locs)

    a1_red_spikes_locs = [
        CastleLocationNames.a1_red_spikes_1,
        CastleLocationNames.a1_red_spikes_2,
        CastleLocationNames.a1_red_spikes_3,
    ]
    a1_red_spikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_red_spikes,
                                         a1_red_spikes_locs)

    a1_n_bgate_locs = [
        CastleLocationNames.a1_n_cache_1,
        CastleLocationNames.a1_n_cache_2,
        CastleLocationNames.a1_n_cache_3,
        CastleLocationNames.a1_n_cache_4,
        CastleLocationNames.a1_n_cache_5,
        CastleLocationNames.a1_n_cache_6,
        CastleLocationNames.a1_n_cache_7,
        CastleLocationNames.a1_n_cache_8,
        CastleLocationNames.a1_n_cache_9,
    ]
    a1_n_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_n_bgate,
                                      a1_n_bgate_locs)

    a1_tp_n_locs = [
        CastleLocationNames.a1_n_tp,
    ]
    a1_tp_n_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_tp_n, a1_tp_n_locs)

    a1_w_locs = [
        CastleLocationNames.a1_nw_left_1,
        CastleLocationNames.a1_nw_left_2,
        CastleLocationNames.a1_nw_left_3,
        CastleLocationNames.a1_nw_left_4,
        CastleLocationNames.a1_nw_left_5,
        CastleLocationNames.a1_nw_right_1,
        CastleLocationNames.a1_nw_right_2,
        CastleLocationNames.a1_nw_right_3,
        CastleLocationNames.a1_nw_right_4,
        CastleLocationNames.a1_sw_n_1,
        CastleLocationNames.a1_sw_n_2,
        CastleLocationNames.a1_sw_n_3,
        CastleLocationNames.a1_sw_w_1,
        CastleLocationNames.a1_sw_w_2,
        CastleLocationNames.a1_w_save_1,
        CastleLocationNames.a1_w_save_2,
        CastleLocationNames.a1_tower_ice_1,
        CastleLocationNames.a1_tower_ice_2,
        CastleLocationNames.ev_a1_boss_switch,
    ]
    a1_w_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_w, a1_w_locs)

    a1_puzzle_locs = [
        CastleLocationNames.a1_puzzle_1,
        CastleLocationNames.a1_puzzle_2,
        CastleLocationNames.a1_puzzle_3,
        CastleLocationNames.a1_puzzle_4,
    ]
    a1_puzzle_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_puzzle, a1_puzzle_locs)

    a1_w_ne_bgate_locs = []
    a1_w_ne_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_w_ne_bgate,
                                         a1_w_ne_bgate_locs)

    a1_nw_bgate_locs = [
        CastleLocationNames.a1_nw_bgate
    ]
    a1_nw_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_nw_bgate,
                                       a1_nw_bgate_locs)

    a1_w_se_bgate_locs = []
    a1_w_se_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_w_se_bgate,
                                         a1_w_se_bgate_locs)

    a1_w_sw_bgate_locs = []
    a1_w_sw_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_w_sw_bgate,
                                         a1_w_sw_bgate_locs)

    a1_w_sw_bgate_1_locs = []
    a1_w_sw_bgate_1_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_w_sw_bgate_1,
                                           a1_w_sw_bgate_1_locs)

    a1_sw_spikes_locs = [
        CastleLocationNames.a1_sw_spikes
    ]
    a1_sw_spikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_sw_spikes,
                                        a1_sw_spikes_locs)

    a1_from_a2_locs = [
        CastleLocationNames.a1_from_a2_1,
        CastleLocationNames.a1_from_a2_2,
        CastleLocationNames.a1_from_a2_3,
    ]
    a1_from_a2_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_from_a2,
                                      a1_from_a2_locs)

    a2_start_locs = [
        CastleLocationNames.a2_n_of_s_save_1,
        CastleLocationNames.a2_n_of_s_save_2,
        CastleLocationNames.a2_n_of_s_save_3,
        CastleLocationNames.a2_n_of_s_save_4,
        CastleLocationNames.a2_s_fire_trap_1,
        CastleLocationNames.a2_s_fire_trap_2,
        CastleLocationNames.a2_sw_ice_tower,
        CastleLocationNames.a2_s_ice_tower_1,
        CastleLocationNames.a2_s_ice_tower_2,
        CastleLocationNames.a2_s_ice_tower_3,
        CastleLocationNames.a2_s_ice_tower_4,
        CastleLocationNames.a2_s_ice_tower_5,
        CastleLocationNames.a2_e_of_s_save_1,
        CastleLocationNames.a2_e_of_s_save_2,
        CastleLocationNames.a2_e_of_s_save_3,
        CastleLocationNames.a2_e_of_s_save_4,
        CastleLocationNames.a2_tower_ice_3,
        CastleLocationNames.a2_tower_ice_5,
    ]
    a2_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_start, a2_start_locs)

    a2_puzzle_locs = [
        CastleLocationNames.a2_puzzle_1,
        CastleLocationNames.a2_puzzle_2,
        CastleLocationNames.a2_puzzle_3,
        CastleLocationNames.a2_puzzle_4,
    ]
    a2_puzzle_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_puzzle, a2_puzzle_locs)

    a2_tp_sw_locs = [
        CastleLocationNames.a2_sw_ice_tower_tp,
    ]
    a2_tp_sw_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_tp_sw, a2_tp_sw_locs)

    a2_tp_se_locs = [
        CastleLocationNames.a2_se_tp,
    ]
    a2_tp_se_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_tp_se, a2_tp_se_locs)

    a2_sw_bgate_locs = []
    a2_sw_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_sw_bgate,
                                       a2_sw_bgate_locs)

    a2_s_bgate_locs = [
        CastleLocationNames.a2_s_bgate,
    ]
    a2_s_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_s_bgate,
                                      a2_s_bgate_locs)

    a2_se_bgate_locs = []
    a2_se_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_se_bgate,
                                       a2_se_bgate_locs)

    a2_s_save_bgate_locs = []
    a2_s_save_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_s_save_bgate,
                                           a2_s_save_bgate_locs)

    a2_ne_locs = [
        CastleLocationNames.a2_s_of_n_save_1,
        CastleLocationNames.a2_s_of_n_save_2,
        CastleLocationNames.a2_s_of_n_save_3,
        CastleLocationNames.a2_nw_ice_tower_across_1,
        CastleLocationNames.a2_nw_ice_tower_across_2,
        CastleLocationNames.a2_nw_ice_tower_across_3,
        CastleLocationNames.a2_nw_ice_tower_across_4,
        CastleLocationNames.a2_e_save_room_1,
        CastleLocationNames.a2_e_save_room_2,
        CastleLocationNames.a2_e_save_room_3,
        CastleLocationNames.a2_e_save_room_4,
        CastleLocationNames.a2_e_save_room_5,
        CastleLocationNames.a2_e_save_room_6,
        CastleLocationNames.a2_n_of_ne_fire_traps_1,
        CastleLocationNames.a2_n_of_ne_fire_traps_2,
        CastleLocationNames.a2_s_of_ne_fire_traps_1,
        CastleLocationNames.a2_s_of_ne_fire_traps_2,
        CastleLocationNames.a2_ne_ice_tower_1,
        CastleLocationNames.a2_ne_ice_tower_2,
        CastleLocationNames.a2_ne_ice_tower_3,
        CastleLocationNames.a2_ne_ice_tower_4,
        CastleLocationNames.a2_ne_ice_tower_5,
        CastleLocationNames.a2_ne_ice_tower_6,
        CastleLocationNames.a2_ne_ice_tower_7,
        CastleLocationNames.a2_ne_ice_tower_8,
        CastleLocationNames.a2_ne_ice_tower_9,
        CastleLocationNames.a2_se_of_e_ice_tower_1,
        CastleLocationNames.a2_se_of_e_ice_tower_2,
        CastleLocationNames.a2_se_of_e_ice_tower_3,
        CastleLocationNames.a2_miniboss_skeleton_1,
        CastleLocationNames.a2_miniboss_skeleton_2,
        CastleLocationNames.a2_tower_ice_2,
        CastleLocationNames.a2_tower_ice_4,
        CastleLocationNames.ev_a2_boss_switch,
        CastleLocationNames.btnc_a2_bspikes_tp,
    ]
    a2_ne_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_ne, a2_ne_locs)

    a2_ne_m_bgate_locs = []
    a2_ne_m_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_ne_m_bgate,
                                         a2_ne_m_bgate_locs)

    a2_ne_l_bgate_locs = [
        CastleLocationNames.a2_ne_l_bgate,
    ]
    a2_ne_l_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_ne_l_bgate,
                                         a2_ne_l_bgate_locs)

    a2_ne_r_bgate_locs = [
        CastleLocationNames.a2_ne_r_bgate_1,
        CastleLocationNames.a2_ne_r_bgate_2,
    ]
    a2_ne_r_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_ne_r_bgate,
                                         a2_ne_r_bgate_locs)

    a2_ne_b_bgate_locs = []
    a2_ne_b_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_ne_b_bgate,
                                         a2_ne_b_bgate_locs)

    a2_ne_save_bgate_locs = []
    a2_ne_save_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_ne_save_bgate,
                                            a2_ne_save_bgate_locs)

    a2_tp_ne_locs = [
        CastleLocationNames.a2_ne_tp,
    ]
    a2_tp_ne_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_tp_ne, a2_tp_ne_locs)

    a2_e_locs = [
        CastleLocationNames.a2_e_ice_tower_1,
        CastleLocationNames.a2_e_ice_tower_2,
        CastleLocationNames.a2_e_ice_tower_3,
        CastleLocationNames.a2_e_ice_tower_4,
        CastleLocationNames.a2_e_ice_tower_5,
        CastleLocationNames.a2_e_ice_tower_6,
        CastleLocationNames.a2_s_of_e_bgate,
        CastleLocationNames.a2_tower_ice_6,
    ]
    a2_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_e, a2_e_locs)

    a2_e_bgate_locs = [
        CastleLocationNames.a2_e_bgate,
    ]
    a2_e_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_e_bgate,
                                      a2_e_bgate_locs)

    a2_nw_locs = [
        CastleLocationNames.a2_pyramid_1,
        CastleLocationNames.a2_pyramid_3,
        CastleLocationNames.a2_pyramid_4,
        CastleLocationNames.a2_nw_ice_tower,
        CastleLocationNames.a2_by_w_a1_stair,
        CastleLocationNames.a2_tower_ice_1,
    ]
    a2_nw_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_nw, a2_nw_locs)

    a2_bonus_return_locs = [
        CastleLocationNames.a2_bonus_return,
    ]
    a2_bonus_return_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_bonus_return,
                                           a2_bonus_return_locs)

    a2_blue_spikes_locs = [
        CastleLocationNames.a2_blue_spikes,
    ]
    a2_blue_spikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_blue_spikes,
                                          a2_blue_spikes_locs)

    a2_blue_spikes_tp_locs = [
        CastleLocationNames.a2_nw_tp,
    ]
    a2_blue_spikes_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_blue_spikes_tp,
                                             a2_blue_spikes_tp_locs)

    a2_to_a3_locs = []
    a2_to_a3_region = create_region(multiworld, player, active_locations, CastleRegionNames.a2_to_a3, a2_to_a3_locs)

    n2_start_locs = [
        CastleLocationNames.n2_start_1,
        CastleLocationNames.n2_start_2,
        CastleLocationNames.n2_start_3,
        CastleLocationNames.n2_start_4,
    ]
    n2_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_start, n2_start_locs)

    n2_m_locs = [
        CastleLocationNames.n2_m_m_1,
        CastleLocationNames.n2_m_m_2,
        CastleLocationNames.n2_m_m_3,
        CastleLocationNames.n2_m_n,
        CastleLocationNames.n2_m_e,
        CastleLocationNames.n2_m_se_1,
        CastleLocationNames.n2_m_se_2,
        CastleLocationNames.n2_m_se_3,
        CastleLocationNames.n2_m_se_4,
        CastleLocationNames.n2_m_se_5,
    ]
    n2_m_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_m, n2_m_locs)

    n2_nw_locs = [
        CastleLocationNames.n2_nw_top_1,
        CastleLocationNames.n2_nw_top_2,
        CastleLocationNames.n2_nw_top_3,
        CastleLocationNames.n2_nw_top_4,
        CastleLocationNames.n2_nw_top_5,
        CastleLocationNames.n2_nw_top_6,
        CastleLocationNames.n2_nw_top_7,
        CastleLocationNames.n2_nw_top_8,
        CastleLocationNames.n2_nw_top_9,
        CastleLocationNames.n2_nw_bottom_1,
        CastleLocationNames.n2_nw_bottom_2,
        CastleLocationNames.n2_nw_bottom_3,
        CastleLocationNames.n2_nw_bottom_4,
        CastleLocationNames.btnc_n2_blue_spikes,
    ]
    n2_nw_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_nw, n2_nw_locs)

    n2_w_locs = [
        CastleLocationNames.n2_w_1,
        CastleLocationNames.n2_w_2,
        CastleLocationNames.n2_w_3,
        CastleLocationNames.n2_w_4,
        CastleLocationNames.n2_w_5,
        CastleLocationNames.n2_w_6,
        CastleLocationNames.n2_w_7,
        CastleLocationNames.n2_w_8,
        CastleLocationNames.n2_w_9,
        CastleLocationNames.n2_w_10,
        CastleLocationNames.n2_w_11,
        CastleLocationNames.n2_w_12,
        CastleLocationNames.n2_w_13,
        CastleLocationNames.n2_w_14,
        CastleLocationNames.n2_w_15,
    ]
    n2_w_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_w, n2_w_locs)

    n2_e_locs = [
        CastleLocationNames.n2_e_1,
        CastleLocationNames.n2_e_2,
        CastleLocationNames.n2_e_3,
        CastleLocationNames.n2_e_4,
        CastleLocationNames.n2_e_5,
        CastleLocationNames.n2_e_6,
        CastleLocationNames.n2_e_7,
        CastleLocationNames.n2_e_8,
        CastleLocationNames.n2_e_9,
        CastleLocationNames.n2_e_10,
        CastleLocationNames.n2_e_11,
        CastleLocationNames.n2_e_12,
        CastleLocationNames.n2_e_13,
        CastleLocationNames.n2_e_14,
        CastleLocationNames.n2_e_15,
    ]
    n2_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_e, n2_e_locs)

    n2_n_locs = [
        CastleLocationNames.n2_n_1,
        CastleLocationNames.n2_n_2,
        CastleLocationNames.n2_n_3,
        CastleLocationNames.n2_n_4,
        CastleLocationNames.n2_n_5,
        CastleLocationNames.n2_n_6,
        CastleLocationNames.n2_n_7,
        CastleLocationNames.n2_n_8,
        CastleLocationNames.n2_n_9,
        CastleLocationNames.n2_n_10,
        CastleLocationNames.n2_n_11,
        CastleLocationNames.n2_n_12,
        CastleLocationNames.n2_n_13,
        CastleLocationNames.n2_n_14,
        CastleLocationNames.n2_n_15,
    ]
    n2_n_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_n, n2_n_locs)

    n2_s_locs = [
        CastleLocationNames.n2_s_1,
        CastleLocationNames.n2_s_2,
        CastleLocationNames.n2_s_3,
        CastleLocationNames.n2_s_4,
        CastleLocationNames.n2_s_5,
        CastleLocationNames.n2_s_6,
        CastleLocationNames.n2_s_7,
        CastleLocationNames.n2_s_8,
        CastleLocationNames.n2_s_9,
    ]
    n2_s_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_s, n2_s_locs)

    n2_ne_locs = [
        CastleLocationNames.n2_ne_1,
        CastleLocationNames.n2_ne_2,
        CastleLocationNames.n2_ne_3,
        CastleLocationNames.n2_ne_4,
    ]
    n2_ne_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_ne, n2_ne_locs)

    n2_se_locs = [
    ]
    n2_se_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_se, n2_se_locs)

    n2_exit_locs = [
    ]
    n2_exit_region = create_region(multiworld, player, active_locations, CastleRegionNames.n2_exit, n2_exit_locs)

    a3_start_locs = [
        CastleLocationNames.a3_sw_1,
        CastleLocationNames.a3_sw_2,
        CastleLocationNames.a3_sw_3,
    ]
    a3_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_start, a3_start_locs)

    a3_main_locs = [
        CastleLocationNames.a3_s_banner_secret,
        CastleLocationNames.a3_nw_save_2,
        CastleLocationNames.a3_nw_save_3,
        CastleLocationNames.a3_ne_ice_towers_1,
        CastleLocationNames.a3_ne_ice_towers_2,
        CastleLocationNames.a3_ne_ice_towers_3,
        CastleLocationNames.a3_pyramids_s_1,
        CastleLocationNames.a3_pyramids_s_2,
        CastleLocationNames.a3_pyramids_s_3,
        CastleLocationNames.a3_e_ice_towers_1,
        CastleLocationNames.a3_e_ice_towers_2,
        CastleLocationNames.a3_spike_floor_8,
        CastleLocationNames.a3_spike_floor_15,
        CastleLocationNames.a3_spike_floor_11,
        CastleLocationNames.a3_spike_floor_14,
        CastleLocationNames.a3_nw_save_1,
        CastleLocationNames.a3_s_of_knife_puzzle,
        CastleLocationNames.a3_fireball_hall_2,
        CastleLocationNames.a3_pyramids_s_5,
        CastleLocationNames.a3_pyramids_s_4,
        CastleLocationNames.a3_e_ice_towers_3,
        CastleLocationNames.a3_spike_floor_1,
        CastleLocationNames.a3_secret_shop,
        CastleLocationNames.a3_spike_floor_7,
        CastleLocationNames.a3_spike_floor_4,
        CastleLocationNames.a3_spike_floor_9,
        CastleLocationNames.a3_spike_floor_13,
        CastleLocationNames.a3_s_of_n_save_2,
        CastleLocationNames.a3_pyramids_n_3,
        CastleLocationNames.a3_pyramids_n_2,
        CastleLocationNames.a3_pyramids_n_1,
        CastleLocationNames.a3_ne_ice_towers_6,
        CastleLocationNames.a3_ne_ice_towers_5,
        CastleLocationNames.a3_ne_ice_towers_4,
        CastleLocationNames.a3_pyramids_n_5,
        CastleLocationNames.a3_pyramids_n_4,
        CastleLocationNames.a3_pyramids_s_6,
        CastleLocationNames.a3_pyramids_s_7,
        CastleLocationNames.a3_se_boss_room_1,
        CastleLocationNames.a3_se_boss_room_2,
        CastleLocationNames.a3_spike_floor_6,
        CastleLocationNames.a3_spike_floor_5,
        CastleLocationNames.a3_se_boss_room_3,
        CastleLocationNames.a3_s_of_n_save_1,
        CastleLocationNames.a3_pyramids_e,
        CastleLocationNames.a3_spike_floor_3,
        CastleLocationNames.a3_spike_floor_12,
        CastleLocationNames.a3_spike_floor_2,
        CastleLocationNames.a3_pyramid,
        CastleLocationNames.a3_fireball_hall_1,
        CastleLocationNames.a3_e_of_spike_floor,
        CastleLocationNames.a3_spike_floor_10,
        CastleLocationNames.a3_miniboss_skeleton_1,
        CastleLocationNames.a3_miniboss_skeleton_2,
        CastleLocationNames.a3_tower_ice_1,
        CastleLocationNames.a3_tower_ice_2,
        CastleLocationNames.a3_tower_ice_3,
        CastleLocationNames.a3_tower_ice_4,
        CastleLocationNames.a3_tower_ice_5,
        CastleLocationNames.a3_tower_ice_6,
        CastleLocationNames.a3_tower_ice_7,
        CastleLocationNames.a3_tower_ice_8,
        CastleLocationNames.a3_tower_ice_9,
        CastleLocationNames.ev_a3_boss_switch,
    ]
    a3_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_main, a3_main_locs)

    a3_tp_locs = [
        CastleLocationNames.a3_m_tp,
    ]
    a3_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_tp, a3_tp_locs)

    a3_from_a2_locs = [
        # Bgate teleport button
    ]
    a3_from_a2_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_from_a2,
                                      a3_from_a2_locs)

    a3_knife_puzzle_reward_locs = [
        CastleLocationNames.a3_knife_puzzle_reward_l_5,
        CastleLocationNames.a3_knife_puzzle_reward_r,
    ]
    a3_knife_puzzle_reward_region = create_region(multiworld, player, active_locations,
                                                  CastleRegionNames.a3_knife_puzzle_reward, a3_knife_puzzle_reward_locs)

    a3_knife_reward_2_locs = [
        CastleLocationNames.a3_knife_puzzle_reward_l_1,
        CastleLocationNames.a3_knife_puzzle_reward_l_2,
        CastleLocationNames.a3_knife_puzzle_reward_l_3,
        CastleLocationNames.a3_knife_puzzle_reward_l_4,
    ]
    a3_knife_reward_2_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_knife_reward_2,
                                             a3_knife_reward_2_locs)

    a3_w_b_bgate_locs = [
        CastleLocationNames.a3_pyramids_s_bgate_tp
    ]
    a3_w_b_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_w_b_bgate,
                                        a3_w_b_bgate_locs)

    a3_w_t_bgate_locs = []
    a3_w_t_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_w_t_bgate,
                                        a3_w_t_bgate_locs)

    a3_w_r_bgate_locs = []
    a3_w_r_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_w_r_bgate,
                                        a3_w_r_bgate_locs)

    a3_n_l_bgate_locs = []
    a3_n_l_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_n_l_bgate,
                                        a3_n_l_bgate_locs)

    a3_n_r_bgate_locs = []
    a3_n_r_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_n_r_bgate,
                                        a3_n_r_bgate_locs)

    a3_e_l_bgate_locs = []
    a3_e_l_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_e_l_bgate,
                                        a3_e_l_bgate_locs)

    a3_e_r_bgate_locs = []
    a3_e_r_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.a3_e_r_bgate,
                                        a3_e_r_bgate_locs)

    b2_start_locs = [
    ]
    b2_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.b2_start, b2_start_locs)

    b2_arena_locs = [
    ]
    b2_arena_region = create_region(multiworld, player, active_locations, CastleRegionNames.b2_arena, b2_arena_locs)

    b2_defeated_locs = [
        CastleLocationNames.b2_boss,
        CastleLocationNames.b2_boss_reward,
        CastleLocationNames.ev_beat_boss_2,
    ]
    b2_defeated_region = create_region(multiworld, player, active_locations, CastleRegionNames.b2_defeated,
                                       b2_defeated_locs)

    b2_exit_locs = [
    ]
    b2_exit_region = create_region(multiworld, player, active_locations, CastleRegionNames.b2_exit, b2_exit_locs)

    r1_start_locs = [
        CastleLocationNames.r1_se_1,
        CastleLocationNames.r1_se_2,
        CastleLocationNames.r1_se_3,
        CastleLocationNames.r1_se_4,
        CastleLocationNames.r1_se_5,
        CastleLocationNames.r1_se_6,
    ]
    r1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_start, r1_start_locs)

    r1_se_ggate_locs = []
    r1_se_ggate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_se_ggate,
                                       r1_se_ggate_locs)

    r1_start_wall_locs = [
        CastleLocationNames.r1_start_wall
    ]
    r1_start_wall_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_start_wall,
                                         r1_start_wall_locs)

    r1_e_locs = [
        CastleLocationNames.r1_e_knife_trap_1,
        CastleLocationNames.r1_e_knife_trap_2,
        CastleLocationNames.r1_e_knife_trap_3,
        CastleLocationNames.r1_e_knife_trap_4,
        CastleLocationNames.r1_e_knife_trap_5,
        CastleLocationNames.r1_e_knife_trap_6,
        CastleLocationNames.r1_e_knife_trap_7,
        CastleLocationNames.r1_e_s,
    ]
    r1_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_e, r1_e_locs)

    r1_e_s_bgate_locs = [
        CastleLocationNames.r1_e_s_bgate
    ]
    r1_e_s_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_e_s_bgate,
                                        r1_e_s_bgate_locs)

    r1_e_n_bgate_locs = [
        CastleLocationNames.r1_e_fire_floor_1,
        CastleLocationNames.r1_e_fire_floor_2,
        CastleLocationNames.r1_e_fire_floor_3,
        CastleLocationNames.r1_e_w_1,
        CastleLocationNames.r1_e_w_2,
        CastleLocationNames.r1_e_e,
        CastleLocationNames.r1_e_n_1,
        CastleLocationNames.r1_e_n_2,
        CastleLocationNames.r1_e_n_3,
        CastleLocationNames.r1_tower_plant_2,
    ]
    r1_e_n_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_e_n_bgate,
                                        r1_e_n_bgate_locs)

    r1_e_sgate_locs = [
        CastleLocationNames.r1_e_sgate
    ]
    r1_e_sgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_e_sgate,
                                      r1_e_sgate_locs)

    r1_se_wall_locs = [
        CastleLocationNames.r1_se_wall
    ]
    r1_se_wall_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_se_wall,
                                      r1_se_wall_locs)

    r1_ne_ggate_locs = [
        CastleLocationNames.r1_ne_ggate_1,
        CastleLocationNames.r1_ne_ggate_2,
        CastleLocationNames.r1_ne_ggate_3,
        CastleLocationNames.r1_ne_ggate_4,
    ]
    r1_ne_ggate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_ne_ggate,
                                       r1_ne_ggate_locs)

    r1_nw_locs = [
        CastleLocationNames.r1_nw_1,
        CastleLocationNames.r1_nw_2,
        CastleLocationNames.r1_puzzle_1,
        CastleLocationNames.r1_puzzle_2,
        CastleLocationNames.r1_puzzle_3,
        CastleLocationNames.r1_puzzle_4,
        CastleLocationNames.r1_tower_plant_1,
    ]
    r1_nw_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_nw, r1_nw_locs)

    r1_nw_hidden_locs = [
        CastleLocationNames.r1_nw_hidden_1,
        CastleLocationNames.r1_nw_hidden_2,
    ]
    r1_nw_hidden_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_nw_hidden,
                                        r1_nw_hidden_locs)

    r1_nw_ggate_locs = []
    r1_nw_ggate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_nw_ggate,
                                       r1_nw_ggate_locs)

    r1_sw_locs = [
        CastleLocationNames.r1_sw_nw_1,
        CastleLocationNames.r1_sw_nw_2,
        CastleLocationNames.r1_sw_nw_3,
        CastleLocationNames.r1_sw_ne_1,
        CastleLocationNames.r1_sw_ne_2,
        CastleLocationNames.r1_sw_ne_3,
        CastleLocationNames.r1_sw_ne_4,
        CastleLocationNames.r1_sw_ne_5,
        CastleLocationNames.r1_sw_ne_6,
        CastleLocationNames.r1_sw_ne_7,
        CastleLocationNames.r1_sw_ne_8,
        CastleLocationNames.r1_sw_ne_9,
        CastleLocationNames.r1_w_knife_trap_1,
        CastleLocationNames.r1_w_knife_trap_2,
        CastleLocationNames.r1_w_knife_trap_3,
        CastleLocationNames.r1_w_knife_trap_4,
        CastleLocationNames.r1_w_knife_trap_5,
        CastleLocationNames.r1_w_knife_trap_6,
        CastleLocationNames.r1_w_knife_trap_7,
        CastleLocationNames.r1_sw_ggate_1,
        CastleLocationNames.r1_sw_ggate_2,
        CastleLocationNames.r1_tower_plant_3,
        CastleLocationNames.r1_tower_plant_4,
    ]
    r1_sw_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_sw, r1_sw_locs)

    r1_w_sgate_locs = [  # Shop region
    ]
    r1_w_sgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_w_sgate,
                                      r1_w_sgate_locs)

    r1_sw_ggate_locs = []
    r1_sw_ggate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_sw_ggate,
                                       r1_sw_ggate_locs)

    r1_exit_l_locs = []
    r1_exit_l_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_exit_l, r1_exit_l_locs)

    r1_exit_r_locs = []
    r1_exit_r_region = create_region(multiworld, player, active_locations, CastleRegionNames.r1_exit_r, r1_exit_r_locs)

    r2_start_locs = [
        CastleLocationNames.r2_start
    ]
    r2_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_start, r2_start_locs)

    r2_bswitch_locs = [
        CastleLocationNames.ev_r1_boss_switch
    ]
    r2_bswitch_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_bswitch,
                                      r2_bswitch_locs)

    r2_m_locs = [
        CastleLocationNames.r2_n_3,
        CastleLocationNames.r2_n_4,
        CastleLocationNames.r2_n_bronze_gates_3,
        CastleLocationNames.r2_n_bronze_gates_2,
        CastleLocationNames.r2_m_start_1,
        CastleLocationNames.r2_m_start_2,
        CastleLocationNames.r2_e_hall_2,
        CastleLocationNames.r2_e_hall_1,
        CastleLocationNames.r2_by_sgate_8,
        CastleLocationNames.r2_by_sgate_7,
        CastleLocationNames.r2_by_sgate_6,
        CastleLocationNames.r2_m_spike_trap_2,
        CastleLocationNames.r2_n_bronze_gates_4,
        CastleLocationNames.r2_w_boss_3,
        CastleLocationNames.r2_n_bronze_gates_1,
        CastleLocationNames.r2_m_e_of_spike_trap_3,
        CastleLocationNames.r2_by_sgate_1,
        CastleLocationNames.r2_m_spike_trap_10,
        CastleLocationNames.r2_w_boss_6,
        CastleLocationNames.r2_by_sgate_2,
        CastleLocationNames.r2_e_hall_4,
        CastleLocationNames.r2_e_hall_3,
        CastleLocationNames.r2_m_spike_trap_8,
        CastleLocationNames.r2_n_5,
        CastleLocationNames.r2_n_6,
        CastleLocationNames.r2_n_7,
        CastleLocationNames.r2_w_boss_8,
        CastleLocationNames.r2_w_boss_7,
        CastleLocationNames.r2_w_boss_5,
        CastleLocationNames.r2_w_boss_4,
        CastleLocationNames.r2_m_e_of_spike_trap_4,
        CastleLocationNames.r2_m_e_of_spike_trap_1,
        CastleLocationNames.r2_m_e_of_spike_trap_2,
        CastleLocationNames.r2_by_sgate_3,
        CastleLocationNames.r2_by_sgate_5,
        CastleLocationNames.r2_by_sgate_4,
        CastleLocationNames.r2_m_spike_trap_5,
        CastleLocationNames.r2_m_spike_trap_6,
        CastleLocationNames.r2_m_spike_trap_9,
        CastleLocationNames.r2_m_spike_trap_7,
        CastleLocationNames.r2_n_2,
        CastleLocationNames.r2_se_save,
        CastleLocationNames.r2_m_spike_trap_4,
        CastleLocationNames.r2_w_boss_1,
        CastleLocationNames.r2_m_spike_trap_3,
        CastleLocationNames.r2_n_1,
        CastleLocationNames.r2_w_boss_2,
        CastleLocationNames.r2_m_spike_trap_1,
        CastleLocationNames.r2_miniboss_eye_e_1,
        CastleLocationNames.r2_miniboss_eye_e_2,
        CastleLocationNames.r2_miniboss_eye_w_1,
        CastleLocationNames.r2_miniboss_eye_w_2,
        CastleLocationNames.r2_tower_plant_2,
        CastleLocationNames.r2_tower_plant_3,
        CastleLocationNames.r2_tower_plant_4,
    ]
    r2_m_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_m, r2_m_locs)

    r2_nw_locs = [
        CastleLocationNames.r2_nw_spike_trap_1,
        CastleLocationNames.r2_nw_spike_trap_2,
        CastleLocationNames.r2_tower_plant_1,
    ]
    r2_nw_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_nw, r2_nw_locs)

    r2_n_locs = [
        CastleLocationNames.r2_n_closed_room,
        CastleLocationNames.ev_r2_boss_switch,
    ]
    r2_n_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_n, r2_n_locs)

    r2_e_locs = [
        CastleLocationNames.r2_e_1,
        CastleLocationNames.r2_e_2,
        CastleLocationNames.r2_e_3,
        CastleLocationNames.r2_e_4,
        CastleLocationNames.r2_e_5,
    ]
    r2_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_e, r2_e_locs)

    r2_w_bgate_locs = []
    r2_w_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_w_bgate,
                                      r2_w_bgate_locs)

    r2_sgate_locs = []
    r2_sgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_sgate, r2_sgate_locs)

    r2_s_locs = [
        CastleLocationNames.r2_sw_1,
        CastleLocationNames.r2_sw_2,
        CastleLocationNames.r2_sw_3,
        CastleLocationNames.r2_sw_4,
        CastleLocationNames.r2_sw_5,
        CastleLocationNames.r2_sw_6,
        CastleLocationNames.r2_sw_7,
        CastleLocationNames.r2_sw_8,
        CastleLocationNames.r2_sw_9,
        CastleLocationNames.r2_sw_10,
        CastleLocationNames.r2_sw_11,
        CastleLocationNames.r2_sw_12,
        CastleLocationNames.r2_tower_plant_5,
    ]
    r2_s_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_s, r2_s_locs)

    r2_spike_island_locs = [
        CastleLocationNames.r2_s_knife_trap_1,
        CastleLocationNames.r2_s_knife_trap_2,
        CastleLocationNames.r2_s_knife_trap_3,
        CastleLocationNames.r2_s_knife_trap_4,
        CastleLocationNames.r2_s_knife_trap_5,
    ]
    r2_spike_island_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_spike_island,
                                           r2_spike_island_locs)

    r2_sw_bridge_locs = []
    r2_sw_bridge_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_sw_bridge,
                                        r2_sw_bridge_locs)

    r2_puzzle_locs = [
        CastleLocationNames.r2_puzzle_1,
        CastleLocationNames.r2_puzzle_2,
        CastleLocationNames.r2_puzzle_3,
        CastleLocationNames.r2_puzzle_4,
    ]
    r2_puzzle_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_puzzle, r2_puzzle_locs)

    r2_w_locs = [
        CastleLocationNames.r2_w_island,
    ]
    r2_w_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_w, r2_w_locs)

    r2_from_r3_locs = [
        CastleLocationNames.r2_ne_knife_trap_end,
    ]
    r2_from_r3_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_from_r3,
                                      r2_from_r3_locs)

    r2_ne_cache_locs = [
        CastleLocationNames.r2_ne_knife_trap_wall_1,
        CastleLocationNames.r2_ne_knife_trap_wall_2,
        CastleLocationNames.r2_ne_knife_trap_wall_3,
    ]
    r2_ne_cache_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_ne_cache,
                                       r2_ne_cache_locs)

    r2_ggate_locs = []
    r2_ggate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r2_ggate, r2_ggate_locs)

    r3_main_locs = [
        CastleLocationNames.r3_ne_knife_trap_1,
        CastleLocationNames.r3_ne_knife_trap_2,
        CastleLocationNames.r3_e_fire_floor_n_1,
        CastleLocationNames.r3_e_fire_floor_n_2,
        CastleLocationNames.r3_sw_bgate_3,
        CastleLocationNames.r3_sw_bgate_4,
        CastleLocationNames.r3_sw_bgate_5,
        CastleLocationNames.r3_n_bgate_e,
        CastleLocationNames.r3_w_fire_floor_1,
        CastleLocationNames.r3_start,
        CastleLocationNames.r3_e_miniboss,
        CastleLocationNames.r3_e_fire_floor_w,
        CastleLocationNames.r3_nw_save_2,
        CastleLocationNames.r3_ne_save_1,
        CastleLocationNames.r3_ne_save_2,
        CastleLocationNames.r3_start_nw_3,
        CastleLocationNames.r3_sw_bgate_2,
        CastleLocationNames.r3_sw_bgate_1,
        CastleLocationNames.r3_n_miniboss_4,
        CastleLocationNames.r3_n_miniboss_3,
        CastleLocationNames.r3_n_miniboss_2,
        CastleLocationNames.r3_e_shops_4,
        CastleLocationNames.r3_e_shops_5,
        CastleLocationNames.r3_start_nw_2,
        CastleLocationNames.r3_start_nw_1,
        CastleLocationNames.r3_e_fire_floor_n_5,
        CastleLocationNames.r3_e_fire_floor_n_4,
        CastleLocationNames.r3_e_fire_floor_n_3,
        CastleLocationNames.r3_shops_room_e_3,
        CastleLocationNames.r3_shops_room_e_2,
        CastleLocationNames.r3_shops_room_e_1,
        CastleLocationNames.r3_w_fire_floor_2,
        CastleLocationNames.r3_e_fire_floor_e,
        CastleLocationNames.r3_w_ggate_w,
        CastleLocationNames.r3_s_save,
        CastleLocationNames.r3_nw_save_1,
        CastleLocationNames.r3_n_miniboss_1,
        CastleLocationNames.r3_e_shops_3,
        CastleLocationNames.r3_shops_room_secret,
        CastleLocationNames.r3_miniboss_eye_e_1,
        CastleLocationNames.r3_miniboss_eye_e_2,
        CastleLocationNames.r3_miniboss_eye_n_1,
        CastleLocationNames.r3_miniboss_eye_n_2,
        CastleLocationNames.r3_miniboss_eye_s_1,
        CastleLocationNames.r3_miniboss_eye_s_2,
        CastleLocationNames.r3_tower_plant_1,
        CastleLocationNames.r3_tower_plant_2,
        CastleLocationNames.r3_tower_plant_4,
        CastleLocationNames.r3_tower_plant_6,
        CastleLocationNames.r3_tower_plant_7,
        CastleLocationNames.r3_tower_plant_8,
        CastleLocationNames.r3_tower_plant_9,
        CastleLocationNames.r3_tower_plant_10,
        CastleLocationNames.ev_r3_boss_switch,
    ]
    r3_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_main, r3_main_locs)

    r3_ne_room_locs = [
        CastleLocationNames.r3_e_secret_tp,
        CastleLocationNames.r3_e_tp,
    ]
    r3_ne_room_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_ne_room,
                                      r3_ne_room_locs)

    r3_s_room_locs = [
        CastleLocationNames.r3_s_shops_room_1,
        CastleLocationNames.r3_s_shops_room_2,
    ]
    r3_s_room_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_s_room, r3_s_room_locs)

    r3_w_ggate_locs = [
        CastleLocationNames.r3_s_of_boss_door_1,
        CastleLocationNames.r3_s_of_boss_door_2,
        CastleLocationNames.r3_tower_plant_5,
    ]
    r3_w_ggate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_w_ggate,
                                      r3_w_ggate_locs)

    r3_e_ggate_locs = [
        CastleLocationNames.r3_e_ggate_hallway_1,
        CastleLocationNames.r3_e_ggate_hallway_2,
        CastleLocationNames.r3_e_ggate_hallway_3,
        CastleLocationNames.r3_tower_plant_3,
    ]
    r3_e_ggate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_e_ggate,
                                      r3_e_ggate_locs)

    r3_sw_bgate_locs = [
    ]
    r3_sw_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_sw_bgate,
                                       r3_sw_bgate_locs)

    r3_sw_wall_r_locs = [
        CastleLocationNames.r3_sw_hidden_room_1,
        CastleLocationNames.r3_sw_hidden_room_2,
    ]
    r3_sw_wall_r_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_sw_wall_r,
                                        r3_sw_wall_r_locs)

    r3_sw_wall_l_locs = [
        CastleLocationNames.r3_w_passage_behind_spikes,
        CastleLocationNames.r3_w_passage_s_closed_room,
    ]
    r3_sw_wall_l_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_sw_wall_l,
                                        r3_sw_wall_l_locs)

    r3_nw_tp_locs = [
        CastleLocationNames.r3_nw_tp,
    ]
    r3_nw_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_nw_tp, r3_nw_tp_locs)

    r3_se_cache_locs = [
        CastleLocationNames.r3_e_fire_floor_secret,
    ]
    r3_se_cache_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_se_cache,
                                       r3_se_cache_locs)

    r3_boss_switch_locs = [
        CastleLocationNames.r3_boss_switch_room_1,
        CastleLocationNames.r3_boss_switch_room_2,
        CastleLocationNames.r3_boss_switch_room_3,
    ]
    r3_boss_switch_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_boss_switch,
                                          r3_boss_switch_locs)

    r3_rune_room_locs = []
    r3_rune_room_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_rune_room,
                                        r3_rune_room_locs)

    r3_bonus_locs = []
    r3_bonus_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_bonus, r3_bonus_locs)

    r3_l_shop_sgate_locs = [
        CastleLocationNames.r3_s_shops_room_left_shop,
    ]
    r3_l_shop_sgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_l_shop_sgate,
                                           r3_l_shop_sgate_locs)

    r3_r_shop_sgate_locs = []
    r3_r_shop_sgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_r_shop_sgate,
                                           r3_r_shop_sgate_locs)

    r3_bonus_return_locs = [
        CastleLocationNames.r3_bonus_return_1,
        CastleLocationNames.r3_bonus_return_2,
    ]
    r3_bonus_return_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_bonus_return,
                                           r3_bonus_return_locs)

    r3_bonus_return_bridge_locs = [
        CastleLocationNames.r3_e_shops_puzzle_reward,
    ]
    r3_bonus_return_bridge_region = create_region(multiworld, player, active_locations,
                                                  CastleRegionNames.r3_bonus_return_bridge, r3_bonus_return_bridge_locs)

    r3_exit_locs = []
    r3_exit_region = create_region(multiworld, player, active_locations, CastleRegionNames.r3_exit, r3_exit_locs)

    n3_main_locs = [
        CastleLocationNames.n3_tp_room_n_1,
        CastleLocationNames.n3_tp_room_n_2,
        CastleLocationNames.n3_exit_e_1,
        CastleLocationNames.n3_exit_e_2,
        CastleLocationNames.n3_exit_e_3,
        CastleLocationNames.n3_exit_e_6,
        CastleLocationNames.n3_exit_e_4,
        CastleLocationNames.n3_exit_e_5,
        CastleLocationNames.n3_exit_e_7,
        CastleLocationNames.n3_exit_e_8,
        CastleLocationNames.n3_exit_e_9,
        CastleLocationNames.n3_nw_cluster_1,
        CastleLocationNames.n3_nw_cluster_2,
        CastleLocationNames.n3_nw_cluster_3,
        CastleLocationNames.n3_nw_cluster_6,
        CastleLocationNames.n3_nw_cluster_5,
        CastleLocationNames.n3_nw_cluster_4,
        CastleLocationNames.n3_nw_cluster_7,
        CastleLocationNames.n3_nw_cluster_8,
        CastleLocationNames.n3_nw_cluster_9,
        CastleLocationNames.n3_exit_s_cluster_7,
        CastleLocationNames.n3_exit_s_cluster_9,
        CastleLocationNames.n3_exit_s_cluster_8,
        CastleLocationNames.n3_exit_s_cluster_4,
        CastleLocationNames.n3_exit_s_cluster_6,
        CastleLocationNames.n3_exit_s_cluster_5,
        CastleLocationNames.n3_exit_s_cluster_1,
        CastleLocationNames.n3_exit_s_cluster_3,
        CastleLocationNames.n3_exit_s_cluster_2,
        CastleLocationNames.n3_exit_se_cluster_7,
        CastleLocationNames.n3_exit_se_cluster_9,
        CastleLocationNames.n3_exit_se_cluster_8,
        CastleLocationNames.n3_exit_se_cluster_4,
        CastleLocationNames.n3_exit_se_cluster_6,
        CastleLocationNames.n3_exit_se_cluster_5,
        CastleLocationNames.n3_exit_se_cluster_1,
        CastleLocationNames.n3_exit_se_cluster_3,
        CastleLocationNames.n3_exit_se_cluster_2,
        CastleLocationNames.n3_tp_room_e_4,
        CastleLocationNames.n3_tp_room_e_3,
        CastleLocationNames.n3_tp_room_e_2,
        CastleLocationNames.n3_tp_room_e_1,
        CastleLocationNames.n3_m_cluster_7,
        CastleLocationNames.n3_m_cluster_8,
        CastleLocationNames.n3_m_cluster_9,
        CastleLocationNames.n3_m_cluster_6,
        CastleLocationNames.n3_m_cluster_4,
        CastleLocationNames.n3_m_cluster_1,
        CastleLocationNames.n3_m_cluster_3,
        CastleLocationNames.n3_m_cluster_2,
        CastleLocationNames.n3_se_cluster_1,
        CastleLocationNames.n3_se_cluster_2,
        CastleLocationNames.n3_se_cluster_3,
        CastleLocationNames.n3_se_cluster_6,
        CastleLocationNames.n3_se_cluster_4,
        CastleLocationNames.n3_se_cluster_7,
        CastleLocationNames.n3_se_cluster_8,
        CastleLocationNames.n3_se_cluster_9,
        CastleLocationNames.n3_exit_sw,
        CastleLocationNames.n3_m_cluster_5,
        CastleLocationNames.n3_se_cluster_5,
        CastleLocationNames.n3_exit_s,
        CastleLocationNames.n3_exit_se,
    ]
    n3_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.n3_main, n3_main_locs)

    n3_tp_room_locs = [
        CastleLocationNames.n3_tp_room,
    ]
    n3_tp_room_region = create_region(multiworld, player, active_locations, CastleRegionNames.n3_tp_room,
                                      n3_tp_room_locs)

    b3_start_locs = [
    ]
    b3_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.b3_start, b3_start_locs)

    b3_arena_locs = [
    ]
    b3_arena_region = create_region(multiworld, player, active_locations, CastleRegionNames.b3_arena, b3_arena_locs)

    b3_defeated_locs = [
        CastleLocationNames.b3_boss,
        CastleLocationNames.b3_reward,
        CastleLocationNames.ev_beat_boss_3,
    ]
    b3_defeated_region = create_region(multiworld, player, active_locations, CastleRegionNames.b3_defeated,
                                       b3_defeated_locs)

    b3_exit_locs = [
    ]
    b3_exit_region = create_region(multiworld, player, active_locations, CastleRegionNames.b3_exit, b3_exit_locs)

    c1_start_locs = [
        CastleLocationNames.c1_n_alcove_2,
        CastleLocationNames.c1_n_alcove_3,
        CastleLocationNames.c1_s_ice_towers_4,
        CastleLocationNames.c1_s_ice_towers_6,
        CastleLocationNames.c1_n_ice_tower_3,
        CastleLocationNames.c1_n_ice_tower_1,
        CastleLocationNames.c1_n_alcove_1,
        CastleLocationNames.c1_ne,
        CastleLocationNames.c1_s_ice_towers_1,
        CastleLocationNames.c1_s_ice_towers_2,
        CastleLocationNames.c1_start,
        CastleLocationNames.c1_s_ice_towers_3,
        CastleLocationNames.c1_s_ice_towers_5,
        CastleLocationNames.c1_n_ice_tower_2,
        CastleLocationNames.c1_m_knife_traps,
        CastleLocationNames.c1_n_alcove_4,
        CastleLocationNames.c1_ne_knife_traps_1,
        CastleLocationNames.c1_ne_knife_traps_2,
        CastleLocationNames.c1_tower_plant_1,
        CastleLocationNames.c1_tower_ice_1,
        CastleLocationNames.c1_tower_ice_2,
        CastleLocationNames.c1_tower_ice_3,
    ]
    c1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_start, c1_start_locs)

    c1_se_spikes_locs = [
        CastleLocationNames.c1_se_spikes
    ]
    c1_se_spikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_se_spikes,
                                        c1_se_spikes_locs)

    c1_n_spikes_locs = [
        CastleLocationNames.c1_n_spikes_1,
        CastleLocationNames.c1_n_spikes_2,
    ]
    c1_n_spikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_n_spikes,
                                       c1_n_spikes_locs)
    # Obviously a shop region
    c1_shop_locs = [
    ]
    c1_shop_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_shop, c1_shop_locs)

    c1_w_locs = [
        CastleLocationNames.c1_w_1,
        CastleLocationNames.c1_w_2,
        CastleLocationNames.c1_w_3,
        CastleLocationNames.c1_miniboss_lich_1,
        CastleLocationNames.c1_miniboss_lich_2,
        CastleLocationNames.c1_tower_plant_2,
    ]
    c1_w_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_w, c1_w_locs)

    c1_sgate_locs = [
        CastleLocationNames.c1_sgate
    ]
    c1_sgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_sgate, c1_sgate_locs)

    c1_prison_stairs_locs = [
        CastleLocationNames.c1_prison_stairs
    ]
    c1_prison_stairs_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_prison_stairs,
                                            c1_prison_stairs_locs)
    # Symbolic region containing the button to open the shortcut to the east area
    c1_s_bgate_locs = [
    ]
    c1_s_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_s_bgate,
                                      c1_s_bgate_locs)

    c1_ledge_locs = [
        CastleLocationNames.c1_ledge_1,
        CastleLocationNames.c1_ledge_2,
    ]
    c1_ledge_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_ledge, c1_ledge_locs)

    c1_tp_island_locs = [
        CastleLocationNames.c1_tp_island_1,
        CastleLocationNames.c1_tp_island_2,
    ]
    c1_tp_island_region = create_region(multiworld, player, active_locations, CastleRegionNames.c1_tp_island,
                                        c1_tp_island_locs)

    pstart_start_locs = [
    ]
    pstart_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.pstart_start,
                                        pstart_start_locs)

    pstart_puzzle_locs = [
        CastleLocationNames.pstart_puzzle_1,
        CastleLocationNames.pstart_puzzle_2,
        CastleLocationNames.pstart_puzzle_3,
        CastleLocationNames.pstart_puzzle_4,
    ]
    pstart_puzzle_region = create_region(multiworld, player, active_locations, CastleRegionNames.pstart_puzzle,
                                         pstart_puzzle_locs)

    c2_main_locs = [
        CastleLocationNames.c2_ne_platform_5,
        CastleLocationNames.c2_e_fire_floor_1,
        CastleLocationNames.c2_w_spikes_s_2,
        CastleLocationNames.c2_w_spikes_s_1,
        CastleLocationNames.c2_sw_ice_tower_5,
        CastleLocationNames.c2_sw_ice_tower_4,
        CastleLocationNames.c2_w_spikes_e_2,
        CastleLocationNames.c2_w_spikes_e_1,
        CastleLocationNames.c2_w_save,
        CastleLocationNames.c2_w_alcove_2,
        CastleLocationNames.c2_w_alcove_1,
        CastleLocationNames.c2_e_fire_floor_w_2,
        CastleLocationNames.c2_e_fire_floor_w_1,
        CastleLocationNames.c2_w_knife_traps_6,
        CastleLocationNames.c2_w_knife_traps_5,
        CastleLocationNames.c2_s_3,
        CastleLocationNames.c2_s_2,
        CastleLocationNames.c2_start_s_6,
        CastleLocationNames.c2_start_s_5,
        CastleLocationNames.c2_start_s_7,
        CastleLocationNames.c2_ne_2,
        CastleLocationNames.c2_ne_4,
        CastleLocationNames.c2_ne_3,
        CastleLocationNames.c2_ne_6,
        CastleLocationNames.c2_w_alcove_4,
        CastleLocationNames.c2_w_alcove_3,
        CastleLocationNames.c2_w_spikes_s_3,
        CastleLocationNames.c2_w_spikes_e_3,
        CastleLocationNames.c2_ne_platform_n_1,
        CastleLocationNames.c2_ne_5,
        CastleLocationNames.c2_ne_platform_4,
        CastleLocationNames.c2_by_tp_island_1,
        CastleLocationNames.c2_w_spikes_s_7,
        CastleLocationNames.c2_w_knife_traps_2,
        CastleLocationNames.c2_w_knife_traps_4,
        CastleLocationNames.c2_s_1,
        CastleLocationNames.c2_s_6,
        CastleLocationNames.c2_start_s_1,
        CastleLocationNames.c2_se_flame_turrets_1,
        CastleLocationNames.c2_se_flame_turrets_4,
        CastleLocationNames.c2_exit,
        CastleLocationNames.c2_ne_platform_n_3,
        CastleLocationNames.c2_ne_platform_6,
        CastleLocationNames.c2_by_tp_island_3,
        CastleLocationNames.c2_w_knife_traps_1,
        CastleLocationNames.c2_s_7,
        CastleLocationNames.c2_se_flame_turrets_2,
        CastleLocationNames.c2_sw_ice_tower_1,
        CastleLocationNames.c2_sw_ice_tower_2,
        CastleLocationNames.c2_sw_ice_tower_3,
        CastleLocationNames.c2_w_spikes_s_4,
        CastleLocationNames.c2_w_spikes_s_5,
        CastleLocationNames.c2_w_spikes_s_6,
        CastleLocationNames.c2_ne_platform_n_2,
        CastleLocationNames.c2_ne_platform_n_4,
        CastleLocationNames.c2_e_fire_floor_w_3,
        CastleLocationNames.c2_e_fire_floor_w_4,
        CastleLocationNames.c2_e_fire_floor_w_5,
        CastleLocationNames.c2_start_s_2,
        CastleLocationNames.c2_start_s_3,
        CastleLocationNames.c2_start_s_4,
        CastleLocationNames.c2_ne_1,
        CastleLocationNames.c2_by_tp_island_2,
        CastleLocationNames.c2_boss_portal,
        CastleLocationNames.c2_w_knife_traps_3,
        CastleLocationNames.c2_s_5,
        CastleLocationNames.c2_se_flame_turrets_3,
        CastleLocationNames.c2_se_flame_turrets_5,
        CastleLocationNames.c2_e_fire_floor_2,
        CastleLocationNames.c2_ne_platform_1,
        CastleLocationNames.c2_w_spikes_e_4,
        CastleLocationNames.c2_ne_platform_3,
        CastleLocationNames.c2_ne_platform_2,
        CastleLocationNames.c2_s_4,
        CastleLocationNames.c2_miniboss_lich_ne_1,
        CastleLocationNames.c2_miniboss_lich_ne_2,
        CastleLocationNames.c2_miniboss_lich_m_1,
        CastleLocationNames.c2_miniboss_lich_m_2,
        CastleLocationNames.c2_tower_plant_2,
        CastleLocationNames.c2_tower_plant_3,
        CastleLocationNames.c2_tower_plant_4,
        CastleLocationNames.c2_tower_plant_5,
        CastleLocationNames.c2_tower_plant_6,
        CastleLocationNames.c2_tower_plant_7,
        CastleLocationNames.c2_tower_plant_8,
        CastleLocationNames.c2_tower_ice_1,
        CastleLocationNames.c2_tower_ice_2,
        CastleLocationNames.c2_tower_ice_3,
        CastleLocationNames.c2_tower_ice_4,
        CastleLocationNames.c2_tower_ice_5,
        CastleLocationNames.c2_tower_ice_9,
        CastleLocationNames.c2_tower_ice_10,
        CastleLocationNames.c2_tower_ice_11,
        CastleLocationNames.c2_by_e_shops_2_1,
        CastleLocationNames.c2_by_e_shops_2_2,
        CastleLocationNames.ev_c2_boss_switch
    ]
    c2_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_main, c2_main_locs)

    c2_exit_bgate_locs = [
        CastleLocationNames.btnc_c2_n_open_wall,
    ]
    c2_exit_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_exit_bgate,
                                         c2_exit_bgate_locs)

    c2_sw_wall_locs = [
        CastleLocationNames.c2_sw_ice_tower_6,
    ]
    c2_sw_wall_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_sw_wall,
                                      c2_sw_wall_locs)

    c2_w_wall_locs = [
        CastleLocationNames.c2_w_save_wall,
    ]
    c2_w_wall_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_w_wall, c2_w_wall_locs)

    c2_e_wall_locs = [
        CastleLocationNames.c2_by_e_shops_2,
    ]
    c2_e_wall_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_e_wall, c2_e_wall_locs)

    c2_w_spikes_locs = [
        CastleLocationNames.c2_w_spikes_1,
        CastleLocationNames.c2_w_spikes_2,
        CastleLocationNames.c2_w_spikes_3,
        CastleLocationNames.c2_w_spikes_4,
    ]
    c2_w_spikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_w_spikes,
                                       c2_w_spikes_locs)

    c2_w_shops_1_locs = [
        CastleLocationNames.c2_by_w_shops_1
    ]
    c2_w_shops_1_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_w_shops_1,
                                        c2_w_shops_1_locs)

    c2_w_shops_2_locs = [
        CastleLocationNames.c2_by_w_shops_2
    ]
    c2_w_shops_2_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_w_shops_2,
                                        c2_w_shops_2_locs)

    c2_w_shops_3_locs = [
        CastleLocationNames.c2_by_w_shops_3_1,
        CastleLocationNames.c2_by_w_shops_3_2,
    ]
    c2_w_shops_3_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_w_shops_3,
                                        c2_w_shops_3_locs)

    c2_e_shops_1_locs = []
    c2_e_shops_1_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_e_shops_1,
                                        c2_e_shops_1_locs)

    c2_e_shops_2_locs = []
    c2_e_shops_2_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_e_shops_2,
                                        c2_e_shops_2_locs)

    c2_puzzle_locs = [
        CastleLocationNames.c2_puzzle_1,
        CastleLocationNames.c2_puzzle_2,
        CastleLocationNames.c2_puzzle_3,
        CastleLocationNames.c2_puzzle_4,
    ]
    c2_puzzle_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_puzzle, c2_puzzle_locs)

    c2_n_locs = [
        CastleLocationNames.c2_nw_ledge_1,
        CastleLocationNames.c2_nw_ledge_2,
        CastleLocationNames.c2_nw_ledge_3,
        CastleLocationNames.c2_nw_ledge_4,
        CastleLocationNames.c2_nw_ledge_5,
        CastleLocationNames.c2_nw_ledge_6,
        CastleLocationNames.c2_nw_ledge_7,
        CastleLocationNames.c2_nw_knife_traps_1,
        CastleLocationNames.c2_nw_knife_traps_2,
        CastleLocationNames.c2_nw_knife_traps_3,
        CastleLocationNames.c2_nw_knife_traps_4,
        CastleLocationNames.c2_nw_knife_traps_5,
        CastleLocationNames.c2_miniboss_lich_n_1,
        CastleLocationNames.c2_miniboss_lich_n_2,
        CastleLocationNames.c2_tower_plant_1,
        CastleLocationNames.c2_tower_ice_6,
        CastleLocationNames.c2_tower_ice_7,
        CastleLocationNames.c2_tower_ice_8,
    ]
    c2_n_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_n, c2_n_locs)

    c2_n_wall_locs = [
        CastleLocationNames.c2_n_wall
    ]
    c2_n_wall_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_n_wall, c2_n_wall_locs)

    c2_bonus_locs = []
    c2_bonus_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_bonus, c2_bonus_locs)

    c2_bonus_return_locs = [
        CastleLocationNames.c2_bonus_return
    ]
    c2_bonus_return_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_bonus_return,
                                           c2_bonus_return_locs)

    c2_tp_island_locs = [
        CastleLocationNames.ev_c1_boss_switch
    ]
    c2_tp_island_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_tp_island,
                                        c2_tp_island_locs)

    c2_c3_tp_locs = [
        CastleLocationNames.ev_c2_n_shops_switch
    ]
    c2_c3_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_c3_tp, c2_c3_tp_locs)

    c2_n_shops_locs = [
    ]
    c2_n_shops_region = create_region(multiworld, player, active_locations, CastleRegionNames.c2_n_shops,
                                      c2_n_shops_locs)

    n4_main_locs = [
        CastleLocationNames.n4_ne,
        CastleLocationNames.n4_by_w_room_1,
        CastleLocationNames.n4_by_exit,
        CastleLocationNames.n4_by_w_room_2,
    ]
    n4_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.n4_main, n4_main_locs)

    n4_nw_locs = [
        CastleLocationNames.n4_nw_1,
        CastleLocationNames.n4_nw_2,
        CastleLocationNames.n4_nw_3,
        CastleLocationNames.n4_nw_5,
        CastleLocationNames.n4_nw_4,
        CastleLocationNames.n4_nw_6,
        CastleLocationNames.n4_nw_7,
        CastleLocationNames.n4_nw_8,
        CastleLocationNames.n4_nw_9,
        CastleLocationNames.n4_nw_10,
        CastleLocationNames.n4_nw_11,
        CastleLocationNames.n4_nw_14,
        CastleLocationNames.n4_nw_15,
        CastleLocationNames.n4_nw_16,
        CastleLocationNames.n4_nw_13,
        CastleLocationNames.n4_nw_12,
    ]
    n4_nw_region = create_region(multiworld, player, active_locations, CastleRegionNames.n4_nw, n4_nw_locs)

    n4_w_locs = [
        CastleLocationNames.n4_w_7,
        CastleLocationNames.n4_w_4,
        CastleLocationNames.n4_w_3,
        CastleLocationNames.n4_w_2,
        CastleLocationNames.n4_w_1,
        CastleLocationNames.n4_w_6,
        CastleLocationNames.n4_w_5,
        CastleLocationNames.n4_w_8,
        CastleLocationNames.n4_w_10,
        CastleLocationNames.n4_w_11,
        CastleLocationNames.n4_w_12,
        CastleLocationNames.n4_w_13,
        CastleLocationNames.n4_w_14,
        CastleLocationNames.n4_w_9,
    ]
    n4_w_region = create_region(multiworld, player, active_locations, CastleRegionNames.n4_w, n4_w_locs)

    n4_e_locs = [
        CastleLocationNames.n4_e_11,
        CastleLocationNames.n4_e_24,
        CastleLocationNames.n4_e_16,
        CastleLocationNames.n4_e_8,
        CastleLocationNames.n4_e_7,
        CastleLocationNames.n4_e_6,
        CastleLocationNames.n4_e_14,
        CastleLocationNames.n4_e_15,
        CastleLocationNames.n4_e_22,
        CastleLocationNames.n4_e_20,
        CastleLocationNames.n4_e_19,
        CastleLocationNames.n4_e_18,
        CastleLocationNames.n4_e_17,
        CastleLocationNames.n4_e_9,
        CastleLocationNames.n4_e_10,
        CastleLocationNames.n4_e_12,
        CastleLocationNames.n4_e_13,
        CastleLocationNames.n4_e_5,
        CastleLocationNames.n4_e_4,
        CastleLocationNames.n4_e_3,
        CastleLocationNames.n4_e_2,
        CastleLocationNames.n4_e_1,
        CastleLocationNames.n4_e_25,
        CastleLocationNames.n4_e_26,
        CastleLocationNames.n4_e_27,
        CastleLocationNames.n4_e_28,
        CastleLocationNames.n4_e_29,
        CastleLocationNames.n4_e_30,
        CastleLocationNames.n4_e_31,
        CastleLocationNames.n4_e_32,
        CastleLocationNames.n4_e_23,
        CastleLocationNames.n4_e_21,
    ]
    n4_e_region = create_region(multiworld, player, active_locations, CastleRegionNames.n4_e, n4_e_locs)

    c3_main_locs = [
        CastleLocationNames.c3_start_e
    ]
    c3_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_start, c3_main_locs)

    c3_rspike_switch_locs = [
        CastleLocationNames.ev_c3_rspikes_switch
    ]
    c3_rspike_switch_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_rspike_switch,
                                            c3_rspike_switch_locs)

    c3_rspikes_locs = [
        CastleLocationNames.c3_w_ledge_1,
        CastleLocationNames.c3_w_ledge_2,
        CastleLocationNames.c3_m_ice_towers_1,
        CastleLocationNames.c3_m_ice_towers_2,
        CastleLocationNames.c3_m_ice_towers_3,
        CastleLocationNames.c3_m_ice_towers_4,
        CastleLocationNames.c3_se_save_1,
        CastleLocationNames.c3_se_save_2,
        CastleLocationNames.c3_se_save_3,
        CastleLocationNames.c3_sw_save_1,
        CastleLocationNames.c3_sw_save_2,
        CastleLocationNames.c3_sw_save_3,
        CastleLocationNames.c3_fire_floor_w,
        CastleLocationNames.c3_ne_npc_1,
        CastleLocationNames.c3_ne_npc_2,
        CastleLocationNames.c3_ne_npc_3,
        CastleLocationNames.c3_miniboss_lich_sw_1,
        CastleLocationNames.c3_miniboss_lich_sw_2,
        CastleLocationNames.c3_tower_plant_3,
        CastleLocationNames.c3_tower_plant_4,
        CastleLocationNames.c3_tower_plant_5,
        CastleLocationNames.c3_tower_plant_6,
        CastleLocationNames.c3_tower_ice_5,
        CastleLocationNames.c3_tower_ice_7,
        CastleLocationNames.c3_tower_ice_8,
        CastleLocationNames.c3_tower_ice_9,
        CastleLocationNames.c3_tower_ice_10,
        CastleLocationNames.ev_c3_sw_hidden_switch_3,
        CastleLocationNames.ev_c3_sw_hidden_switch_4,
        CastleLocationNames.ev_c3_sw_hidden_switch_5,
        CastleLocationNames.ev_c3_sw_hidden_switch_6,
    ]
    c3_rspikes_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_rspikes,
                                      c3_rspikes_locs)

    c3_m_wall_locs = [
        CastleLocationNames.c3_m_wall
    ]
    c3_m_wall_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_m_wall, c3_m_wall_locs)

    c3_m_shop_locs = []
    c3_m_shop_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_m_shop, c3_m_shop_locs)

    c3_m_tp_locs = [
        CastleLocationNames.c3_m_tp
    ]
    c3_m_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_m_tp, c3_m_tp_locs)

    c3_s_bgate_locs = [
        CastleLocationNames.c3_s_bgate
    ]
    c3_s_bgate_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_s_bgate,
                                      c3_s_bgate_locs)

    c3_nw_locs = [
        CastleLocationNames.c3_nw_ice_towers_1,
        CastleLocationNames.c3_nw_ice_towers_2,
        CastleLocationNames.c3_nw_ice_towers_3,
        CastleLocationNames.c3_nw_ice_towers_w,
        CastleLocationNames.c3_e_miniboss,
        CastleLocationNames.c3_n_spike_floor_1,
        CastleLocationNames.c3_n_spike_floor_2,
        CastleLocationNames.c3_boss_switch,
        CastleLocationNames.c3_miniboss_lich_e_1,
        CastleLocationNames.c3_miniboss_lich_e_2,
        CastleLocationNames.c3_tower_plant_1,
        CastleLocationNames.c3_tower_plant_2,
        CastleLocationNames.c3_tower_ice_1,
        CastleLocationNames.c3_tower_ice_2,
        CastleLocationNames.c3_tower_ice_3,
        CastleLocationNames.c3_tower_ice_4,
        CastleLocationNames.c3_tower_ice_6,
        CastleLocationNames.ev_c3_sw_hidden_switch_1,
        CastleLocationNames.ev_c3_sw_hidden_switch_2,
        CastleLocationNames.ev_c3_boss_switch
    ]
    c3_nw_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_nw, c3_nw_locs)

    c3_sw_hidden_locs = [
        CastleLocationNames.c3_sw_hidden
    ]
    c3_sw_hidden_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_sw_hidden,
                                        c3_sw_hidden_locs)

    c3_se_hidden_locs = []
    c3_se_hidden_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_se_hidden,
                                        c3_se_hidden_locs)

    c3_light_bridge_locs = [
        CastleLocationNames.c3_light_bridge_1,
        CastleLocationNames.c3_light_bridge_2,
        CastleLocationNames.c3_light_bridge_3,
        CastleLocationNames.c3_easter_egg,
    ]
    c3_light_bridge_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_light_bridge,
                                           c3_light_bridge_locs)

    c3_fire_floor_locs = [
        CastleLocationNames.c3_fire_floor_1,
        CastleLocationNames.c3_fire_floor_2,
        CastleLocationNames.c3_fire_floor_3,
    ]
    c3_fire_floor_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_fire_floor,
                                         c3_fire_floor_locs)

    c3_fire_floor_tp_locs = [
        CastleLocationNames.c3_fire_floor_tp
    ]
    c3_fire_floor_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_fire_floor_tp,
                                            c3_fire_floor_tp_locs)

    c3_c2_tp_locs = [
        CastleLocationNames.c3_c2_tp
    ]
    c3_c2_tp_region = create_region(multiworld, player, active_locations, CastleRegionNames.c3_c2_tp, c3_c2_tp_locs)

    b4_start_locs = [
        CastleLocationNames.b4_e_2,
        CastleLocationNames.b4_w_10,
        CastleLocationNames.b4_w_2,
        CastleLocationNames.b4_dragon_6,
        CastleLocationNames.b4_dragon_2,
        CastleLocationNames.b4_w_11,
        CastleLocationNames.b4_w_1,
        CastleLocationNames.b4_w_3,
        CastleLocationNames.b4_e_3,
        CastleLocationNames.b4_e_4,
        CastleLocationNames.b4_e_1,
        CastleLocationNames.b4_dragon_9,
        CastleLocationNames.b4_w_9,
        CastleLocationNames.b4_w_6,
        CastleLocationNames.b4_w_4,
        CastleLocationNames.b4_dragon_4,
        CastleLocationNames.b4_dragon_7,
        CastleLocationNames.b4_dragon_11,
        CastleLocationNames.b4_dragon_12,
        CastleLocationNames.b4_e_8,
        CastleLocationNames.b4_w_12,
        CastleLocationNames.b4_e_7,
        CastleLocationNames.b4_w_5,
        CastleLocationNames.b4_w_7,
        CastleLocationNames.b4_w_8,
        CastleLocationNames.b4_e_6,
        CastleLocationNames.b4_e_5,
        CastleLocationNames.b4_dragon_10,
        CastleLocationNames.b4_dragon_5,
        CastleLocationNames.b4_dragon_3,
        CastleLocationNames.b4_dragon_8,
        CastleLocationNames.b4_dragon_1,
        CastleLocationNames.b4_miniboss_lich_1,
        CastleLocationNames.b4_miniboss_lich_2,
    ]
    b4_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.b4_start, b4_start_locs)

    b4_defeated_locations = [
        CastleLocationNames.b4_plank_1,
        CastleLocationNames.b4_plank_2,
        CastleLocationNames.b4_plank_3,
        CastleLocationNames.b4_plank_4,
        CastleLocationNames.b4_plank_5,
        CastleLocationNames.b4_plank_6,
        CastleLocationNames.b4_plank_7,
        CastleLocationNames.b4_plank_8,
        CastleLocationNames.b4_plank_9,
        CastleLocationNames.b4_plank_10,
        CastleLocationNames.b4_plank_11,
        CastleLocationNames.ev_beat_boss_4,
    ]
    if get_goal_type(multiworld, player) == GoalType.KillBosses:
        b4_defeated_locations.append(CastleLocationNames.ev_victory)
    b4_defeated_region = create_region(multiworld, player, active_locations, CastleRegionNames.b4_defeated,
                                       b4_defeated_locations)

    get_planks_locations = []
    if get_goal_type(multiworld, player) == GoalType.PlankHunt:
        get_planks_locations.append(CastleLocationNames.ev_victory)
    get_planks_region = create_region(multiworld, player, active_locations, CastleRegionNames.get_planks,
                                      get_planks_locations)

    e1_main_locations = []
    e1_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.e1_main, e1_main_locations)

    e2_main_locations = [
        CastleLocationNames.e2_entrance,
        CastleLocationNames.e2_end,
    ]
    e2_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.e2_main, e2_main_locations)

    e3_main_locations = [
        CastleLocationNames.e3_entrance_1,
        CastleLocationNames.e3_entrance_2,
    ]
    e3_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.e3_main, e3_main_locations)

    e4_main_locations = [
        CastleLocationNames.e4_main
    ]
    e4_main_region = create_region(multiworld, player, active_locations, CastleRegionNames.e4_main, e4_main_locations)

    escaped_locations = []
    if get_goal_type(multiworld, player) == GoalType.FullCompletion:
        escaped_locations.append(CastleLocationNames.ev_victory)
    escaped_region = create_region(multiworld, player, active_locations, CastleRegionNames.escaped, escaped_locations)

    multiworld.regions += [
        menu_region,
        hub_region,
        p1_start_region,
        p1_nw_region,
        p1_s_region,
        p1_sw_bronze_gate_region,
        p1_e_region,
        p1_m_bronze_gate_region,
        p1_from_p2_region,
        p1_from_p3_n_region,
        p1_from_p3_s_region,
        p2_start_region,
        p2_m_region,
        p2_p1_return_region,
        p2_n_region,
        p2_spike_puzzle_bottom_region,
        p2_spike_puzzle_left_region,
        p2_spike_puzzle_top_region,
        p2_red_switch_region,
        p2_puzzle_region,
        p2_e_bronze_gate_region,
        p2_e_save_region,
        p2_s_region,
        p2_e_bronze_gate_2_region,
        p2_m_bronze_gate_region,
        p2_se_bronze_gate_region,
        p2_gg_room_reward_region,
        p2_w_treasure_region,
        p2_w_treasure_tp_region,
        p2_tp_puzzle_region,
        p2_end_region,
        p3_start_door_region,
        p3_start_region,
        p3_nw_closed_room_region,
        p3_nw_n_bronze_gate_region,
        p3_nw_s_bronze_gate_region,
        p3_s_bronze_gate_region,
        p3_silver_gate_region,
        p3_n_gold_gate_region,
        p3_rspikes_region,
        p3_rspikes_room_region,
        p3_bonus_region,
        p3_arrow_hall_secret_region,
        p3_spikes_s_region,
        p3_sw_region,
        p3_exit_s_region,
        p3_hidden_arrow_hall_region,
        p3_s_gold_gate_region,
        p3_bonus_return_region,
        n1_start_region,
        n1_room1_region,
        n1_room2_region,
        n1_room2_unlock_region,
        n1_room3_region,
        n1_room3_unlock_region,
        n1_room3_hall_region,
        n1_room4_region,
        b1_start_region,
        b1_arena_region,
        b1_defeated_region,
        b1_exit_region,
        a1_start_region,
        a1_start_shop_w_region,
        a1_start_shop_m_region,
        a1_start_shop_e_region,
        a1_se_region,
        a1_e_region,
        a1_e_sw_bgate_region,
        a1_e_s_bgate_region,
        a1_e_se_bgate_region,
        a1_e_e_bgate_region,
        a1_rune_room_region,
        a1_se_cache_region,
        a1_e_ne_bgate_region,
        a1_red_spikes_region,
        a1_n_bgate_region,
        a1_tp_n_region,
        a1_w_region,
        a1_puzzle_region,
        a1_w_ne_bgate_region,
        a1_nw_bgate_region,
        a1_w_se_bgate_region,
        a1_w_sw_bgate_region,
        a1_w_sw_bgate_1_region,
        a1_sw_spikes_region,
        a1_from_a2_region,
        a2_start_region,
        a2_puzzle_region,
        a2_tp_sw_region,
        a2_tp_se_region,
        a2_sw_bgate_region,
        a2_s_bgate_region,
        a2_se_bgate_region,
        a2_s_save_bgate_region,
        a2_ne_region,
        a2_ne_m_bgate_region,
        a2_ne_l_bgate_region,
        a2_ne_r_bgate_region,
        a2_ne_b_bgate_region,
        a2_ne_save_bgate_region,
        a2_tp_ne_region,
        a2_e_region,
        a2_e_bgate_region,
        a2_nw_region,
        a2_bonus_return_region,
        a2_blue_spikes_region,
        a2_blue_spikes_tp_region,
        a2_to_a3_region,
        n2_start_region,
        n2_m_region,
        n2_nw_region,
        n2_n_region,
        n2_e_region,
        n2_s_region,
        n2_w_region,
        n2_ne_region,
        n2_se_region,
        n2_exit_region,
        a3_start_region,
        a3_main_region,
        a3_tp_region,
        a3_from_a2_region,
        a3_knife_puzzle_reward_region,
        a3_knife_reward_2_region,
        a3_w_t_bgate_region,
        a3_w_r_bgate_region,
        a3_w_b_bgate_region,
        a3_n_l_bgate_region,
        a3_n_r_bgate_region,
        a3_e_l_bgate_region,
        a3_e_r_bgate_region,
        b2_start_region,
        b2_arena_region,
        b2_defeated_region,
        b2_exit_region,
        r1_start_region,
        r1_se_ggate_region,
        r1_e_region,
        r1_start_wall_region,
        r1_e_n_bgate_region,
        r1_e_s_bgate_region,
        r1_e_sgate_region,
        r1_w_sgate_region,
        r1_se_wall_region,
        r1_ne_ggate_region,
        r1_nw_region,
        r1_nw_hidden_region,
        r1_nw_ggate_region,
        r1_sw_region,
        r1_sw_ggate_region,
        r1_exit_l_region,
        r1_exit_r_region,
        r2_start_region,
        r2_bswitch_region,
        r2_m_region,
        r2_w_bgate_region,
        r2_nw_region,
        r2_n_region,
        r2_e_region,
        r2_sgate_region,
        r2_s_region,
        r2_spike_island_region,
        r2_sw_bridge_region,
        r2_puzzle_region,
        r2_w_region,
        r2_from_r3_region,
        r2_ne_cache_region,
        r2_ggate_region,
        r3_main_region,
        r3_ne_room_region,
        r3_s_room_region,
        r3_w_ggate_region,
        r3_e_ggate_region,
        r3_sw_bgate_region,
        r3_sw_wall_r_region,
        r3_sw_wall_l_region,
        r3_nw_tp_region,
        r3_se_cache_region,
        r3_boss_switch_region,
        r3_rune_room_region,
        r3_bonus_region,
        r3_l_shop_sgate_region,
        r3_r_shop_sgate_region,
        r3_bonus_return_region,
        r3_bonus_return_bridge_region,
        r3_exit_region,
        n3_main_region,
        n3_tp_room_region,
        b3_start_region,
        b3_arena_region,
        b3_defeated_region,
        b3_exit_region,
        c1_start_region,
        c1_n_spikes_region,
        c1_se_spikes_region,
        c1_shop_region,
        c1_w_region,
        c1_sgate_region,
        c1_prison_stairs_region,
        c1_s_bgate_region,
        c1_ledge_region,
        c1_tp_island_region,
        pstart_start_region,
        pstart_puzzle_region,
        c2_main_region,
        c2_sw_wall_region,
        c2_w_wall_region,
        c2_e_wall_region,
        c2_w_spikes_region,
        c2_w_shops_1_region,
        c2_w_shops_2_region,
        c2_w_shops_3_region,
        c2_e_shops_1_region,
        c2_e_shops_2_region,
        c2_puzzle_region,
        c2_exit_bgate_region,
        c2_n_region,
        c2_n_wall_region,
        c2_bonus_region,
        c2_bonus_return_region,
        c2_tp_island_region,
        c2_c3_tp_region,
        c2_n_shops_region,
        n4_main_region,
        n4_nw_region,
        n4_w_region,
        n4_e_region,
        c3_main_region,
        c3_rspike_switch_region,
        c3_rspikes_region,
        c3_m_shop_region,
        c3_m_wall_region,
        c3_m_tp_region,
        c3_s_bgate_region,
        c3_nw_region,
        c3_sw_hidden_region,
        c3_se_hidden_region,
        c3_light_bridge_region,
        c3_fire_floor_region,
        c3_fire_floor_tp_region,
        c3_c2_tp_region,
        b4_start_region,
        b4_defeated_region,
        e1_main_region,
        e2_main_region,
        e3_main_region,
        e4_main_region,
        escaped_region,
        get_planks_region
    ]


def connect_castle_regions(multiworld: MultiWorld, player: int, random_locations: typing.Dict[str, int],
                           gate_codes: typing.Dict[str, str]):
    used_names: typing.Dict[str, int] = {}
    gate_counts: typing.Dict[str, int] = {
        ItemName.key_bronze: 0,
        ItemName.key_silver: 0,
        ItemName.key_gold: 0,
    }
    prison_gate_items: typing.Dict[str, int] = {
        ItemName.key_bronze_prison: 0,
        ItemName.key_silver_prison: 0,
        ItemName.key_gold_prison: 0,
    }
    armory_gate_items: typing.Dict[str, int] = {
        ItemName.key_bronze_armory: 0,
        ItemName.key_silver_armory: 0,
        ItemName.key_gold_armory: 0,
    }
    archives_gate_items: typing.Dict[str, int] = {
        ItemName.key_bronze_archives: 0,
        ItemName.key_silver_archives: 0,
        ItemName.key_gold_archives: 0,
    }
    chambers_gate_items: typing.Dict[str, int] = {
        ItemName.key_bronze_chambers: 0,
        ItemName.key_silver_chambers: 0,
        ItemName.key_gold_chambers: 0,
    }

    if multiworld.act_specific_keys[player]:
        key_bronze_prison = ItemName.key_bronze_prison
        key_silver_prison = ItemName.key_silver_prison
        key_gold_prison = ItemName.key_gold_prison
        key_bonus_prison = ItemName.key_bonus_prison

        key_bronze_armory = ItemName.key_bronze_armory
        key_silver_armory = ItemName.key_silver_armory
        key_gold_armory = ItemName.key_gold_armory
        key_bonus_armory = ItemName.key_bonus_armory

        key_bronze_archives = ItemName.key_bronze_archives
        key_silver_archives = ItemName.key_silver_archives
        key_gold_archives = ItemName.key_gold_archives
        key_bonus_archives = ItemName.key_bonus_archives

        key_bronze_chambers = ItemName.key_bronze_chambers
        key_silver_chambers = ItemName.key_silver_chambers
        key_gold_chambers = ItemName.key_gold_chambers
        key_bonus_chambers = ItemName.key_bonus_chambers

        if not multiworld.randomize_bonus_keys[player]:
            key_bonus_prison = ItemName.key_bonus
            key_bonus_armory = ItemName.key_bonus
            key_bonus_archives = ItemName.key_bonus
            key_bonus_chambers = ItemName.key_bonus
    else:
        key_bronze_prison = ItemName.key_bronze
        key_silver_prison = ItemName.key_silver
        key_gold_prison = ItemName.key_gold
        key_bonus_prison = ItemName.key_bonus

        key_bronze_armory = ItemName.key_bronze
        key_silver_armory = ItemName.key_silver
        key_gold_armory = ItemName.key_gold
        key_bonus_armory = ItemName.key_bonus

        key_bronze_archives = ItemName.key_bronze
        key_silver_archives = ItemName.key_silver
        key_gold_archives = ItemName.key_gold
        key_bonus_archives = ItemName.key_bonus

        key_bronze_chambers = ItemName.key_bronze
        key_silver_chambers = ItemName.key_silver
        key_gold_chambers = ItemName.key_gold
        key_bonus_chambers = ItemName.key_bonus

        prison_gate_items = gate_counts
        armory_gate_items = gate_counts
        archives_gate_items = gate_counts
        chambers_gate_items = gate_counts

    prison_gate_items[key_bronze_prison] += 12
    armory_gate_items[key_bronze_armory] += 29
    archives_gate_items[key_bronze_archives] += 20
    chambers_gate_items[key_bronze_chambers] += 42
    prison_gate_items[key_silver_prison] += 2
    armory_gate_items[key_silver_armory] += 3
    archives_gate_items[key_silver_archives] += 5
    chambers_gate_items[key_silver_chambers] += 3
    prison_gate_items[key_gold_prison] += 4
    armory_gate_items[key_gold_armory] += 2
    archives_gate_items[key_gold_archives] += 7
    chambers_gate_items[key_gold_chambers] += 3

    connect(multiworld, player, used_names, CastleRegionNames.menu, CastleRegionNames.p1_start, False)
    connect(multiworld, player, used_names, CastleRegionNames.p1_start, CastleRegionNames.hub, True)

    if multiworld.open_castle[player]:
        connect(multiworld, player, used_names, CastleRegionNames.hub, CastleRegionNames.a1_start, True)
        connect(multiworld, player, used_names, CastleRegionNames.hub, CastleRegionNames.r1_start, True)
        connect(multiworld, player, used_names, CastleRegionNames.hub, CastleRegionNames.c1_start, True)

    connect(multiworld, player, used_names, CastleRegionNames.p1_start, CastleRegionNames.p1_nw,
            True, ItemName.btnc_p1_floor, 1, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p1_nw, CastleRegionNames.p1_s,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p1_0, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p1_s, CastleRegionNames.p1_sw_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p1_3, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p1_s, CastleRegionNames.p1_e,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p1_2, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p1_e, CastleRegionNames.p1_m_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p1_1, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.p1_e, CastleRegionNames.p2_start,
                 EntranceNames.c_p2_0, EntranceNames.c_p1_1)
    if multiworld.shortcut_teleporter[player]:
        connect_exit(multiworld, player, used_names, CastleRegionNames.p1_nw, CastleRegionNames.p3_portal_from_p1,
                     EntranceNames.c_p3_portal, EntranceNames.c_p1_20)
        connect(multiworld, player, used_names, CastleRegionNames.p3_portal_from_p1, CastleRegionNames.p3_n_gold_gate,
                True)

    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_start, CastleRegionNames.p2_m,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p2_0, True)
    connect_exit(multiworld, player, used_names, CastleRegionNames.p2_m, CastleRegionNames.p1_from_p2,
                 EntranceNames.c_p1_2, EntranceNames.c_p2_1)
    connect_exit(multiworld, player, used_names, CastleRegionNames.p1_from_p2, CastleRegionNames.p2_p1_return,
                 EntranceNames.c_p2_2, EntranceNames.c_p1_3)
    # connect_generic(multiworld, player, used_names, CastleRegionNames.p2_p1_return, CastleRegionNames.p2_m)
    # Requires return wall button
    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_m, CastleRegionNames.p2_n,
                 key_silver_prison, gate_codes, prison_gate_items, GateNames.c_p2_5, True)
    connect(multiworld, player, used_names, CastleRegionNames.p2_n, CastleRegionNames.p2_spike_puzzle_bottom, False)
    # Requires spike button 5
    connect(multiworld, player, used_names, CastleRegionNames.p2_n, CastleRegionNames.p2_spike_puzzle_top, False)
    # Requires spike buttons (4, 5, 9) or (5, 7, 6)
    connect(multiworld, player, used_names, CastleRegionNames.p2_n, CastleRegionNames.p2_spike_puzzle_left, False)
    # Requires spike buttons (4, 5, 9) or (5, 7, 6, 1 ,9)
    connect(multiworld, player, used_names, CastleRegionNames.p2_n, CastleRegionNames.p2_red_switch, False)
    # Requires red spike button, also two-way
    connect(multiworld, player, used_names, CastleRegionNames.p2_red_switch, CastleRegionNames.p2_puzzle, False)
    # Requires puzzle button
    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_red_switch, CastleRegionNames.p2_e_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p2_1, False)
    connect(multiworld, player, used_names, CastleRegionNames.p2_red_switch, CastleRegionNames.p2_e_save, False)
    # Requires east save button, also two-way
    # connect_generic(multiworld, player, used_names, CastleRegionNames.p2_m, CastleRegionNames.p2_e_save)
    # Requires east save button
    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_m, CastleRegionNames.p2_s,
                 key_gold_prison, gate_codes, prison_gate_items, GateNames.c_p2_4, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_e_bronze_gate_2,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p2_7, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_m_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p2_6, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_se_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p2_2, False)
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_gg_room_reward,
            False, ItemName.ev_castle_p2_switch, 4, False)
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_w_treasure, False)
    # Requires treasure west wall button
    connect(multiworld, player, used_names, CastleRegionNames.p2_w_treasure, CastleRegionNames.p2_w_treasure_tp, False)
    # Requires treasure east wall button
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_tp_puzzle, False)
    # Requires tp puzzle buttons
    connect_gate(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_end,
                 key_gold_prison, gate_codes, prison_gate_items, GateNames.c_p2_3, True)
    connect_exit(multiworld, player, used_names, CastleRegionNames.p2_end, CastleRegionNames.p3_start_door,
                 EntranceNames.c_p3_0, EntranceNames.c_p2_3)

    connect(multiworld, player, used_names, CastleRegionNames.p3_start_door, CastleRegionNames.p3_start, False)
    # Actually *not* two-way! The button prevents backtracking for now
    # Requires entrance button
    connect(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_nw_closed_room, False)
    # Requires room open button
    connect_gate(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_nw_n_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p3_1, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_nw_s_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p3_0, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_silver_gate,
                 key_silver_prison, gate_codes, prison_gate_items, GateNames.c_p3_3, True)
    # Requires start spike switch
    connect_exit(multiworld, player, used_names, CastleRegionNames.p3_silver_gate, CastleRegionNames.p1_from_p3_s,
                 EntranceNames.c_p1_4, EntranceNames.c_p3_1)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_n_gold_gate,
                 key_gold_prison, gate_codes, prison_gate_items, GateNames.c_p3_4, True)
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p3_rspikes, False)
    # Requires red spikes button, two-way
    connect(multiworld, player, used_names, CastleRegionNames.p3_rspikes, CastleRegionNames.p3_rspikes_room, False)
    # Requires middle room unlock button, from p3_n_gold_gate, two-way. This also connects p3_start to p3_n_gold_gate!
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p3_bonus, False)
    # Requires 5 bonus switches
    connect_exit(multiworld, player, used_names, CastleRegionNames.p3_bonus, CastleRegionNames.n1_start,
                 EntranceNames.c_n1_0, EntranceNames.c_p3_b_ent)
    # Requires 9 bonus buttons
    connect_gate(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p3_s_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, GateNames.c_p3_2, False)
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p3_spikes_s, False)
    # Requires spike switch
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p3_sw, False)
    # Requires spike switch, also two-way
    connect(multiworld, player, used_names, CastleRegionNames.p3_sw, CastleRegionNames.p3_exit_s, False)
    # Requires exit button, two-way
    connect_exit(multiworld, player, used_names, CastleRegionNames.p3_exit_s, CastleRegionNames.p1_from_p3_n,
                 EntranceNames.c_p1_10, EntranceNames.c_p3_10)
    connect(multiworld, player, used_names, CastleRegionNames.p3_exit_s, CastleRegionNames.p3_n_gold_gate, False)
    # Requires exit shortcut button, two-way
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p3_arrow_hall_secret,
            False, ItemName.btnc_p3_e_passage, 1, False)
    connect(multiworld, player, used_names, CastleRegionNames.p3_sw, CastleRegionNames.p3_hidden_arrow_hall, False,
            ItemName.btnc_p3_s_passage, 1, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.p3_sw, CastleRegionNames.p3_s_gold_gate,
                 key_gold_prison, gate_codes, prison_gate_items, GateNames.c_p3_5, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.p3_sw, CastleRegionNames.b1_start,
                 EntranceNames.c_b1_0, EntranceNames.c_p3_boss, ItemName.ev_castle_b1_boss_switch, 3, False)

    # if multiworld.randomize_bonus_keys[player]:
    connect(multiworld, player, used_names, CastleRegionNames.n1_start, CastleRegionNames.n1_room1,
            False, key_bonus_prison)
    connect(multiworld, player, used_names, CastleRegionNames.n1_room1, CastleRegionNames.n1_room2,
            False, key_bonus_prison)
    connect(multiworld, player, used_names, CastleRegionNames.n1_room2, CastleRegionNames.n1_room2_unlock, False)
    # Requires room 2 panel
    connect(multiworld, player, used_names, CastleRegionNames.n1_room2, CastleRegionNames.n1_room3,
            False, key_bonus_prison)
    connect(multiworld, player, used_names, CastleRegionNames.n1_room3, CastleRegionNames.n1_room3_unlock, False)
    # Requires room 3 west panel
    connect(multiworld, player, used_names, CastleRegionNames.n1_room3, CastleRegionNames.n1_room3_hall, False)
    # Requires room 3 east panel or room 3 hall panel
    connect(multiworld, player, used_names, CastleRegionNames.n1_room3_hall, CastleRegionNames.n1_room4,
            False, key_bonus_prison)
    connect_exit(multiworld, player, used_names, CastleRegionNames.n1_room4, CastleRegionNames.p3_bonus_return,
                 EntranceNames.c_p3_b_return, None, key_bonus_prison)
    # else:
    #     connect_generic(multiworld, player, used_names, CastleRegionNames.n1_start, CastleRegionNames.n1_room1)
    #     connect_generic(multiworld, player, used_names, CastleRegionNames.n1_room1, CastleRegionNames.n1_room2)
    #     connect_generic(multiworld, player, used_names, CastleRegionNames.n1_room2, CastleRegionNames.n1_room3)
    #     connect_generic(multiworld, player, used_names, CastleRegionNames.n1_room3, CastleRegionNames.n1_room4)
    #     connect_generic(multiworld, player, used_names, CastleRegionNames.n1_room4, CastleRegionNames.p3_bonus_return,
    #                     True)

    connect(multiworld, player, used_names, CastleRegionNames.b1_start, CastleRegionNames.b1_arena, False)
    connect(multiworld, player, used_names, CastleRegionNames.b1_arena, CastleRegionNames.b1_defeated, False)
    connect(multiworld, player, used_names, CastleRegionNames.b1_defeated, CastleRegionNames.b1_exit, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.b1_exit, CastleRegionNames.a1_start,
                 EntranceNames.c_a1_0, EntranceNames.c_b1_1)

    connect(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.a1_se, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.a1_start_shop_w,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_3, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.a1_start_shop_m,
                 key_gold_armory, gate_codes, armory_gate_items, GateNames.c_a1_7, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.a1_start_shop_e,
                 key_gold_armory, gate_codes, armory_gate_items, GateNames.c_a1_8, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.a2_start,
                 EntranceNames.c_a2_0, EntranceNames.c_a1_a2)
    connect_exit(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.a3_main,
                 EntranceNames.c_a3_0, EntranceNames.c_a1_a3)
    # Requires start wall switch
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_se, CastleRegionNames.a1_e,
                 key_silver_armory, gate_codes, armory_gate_items, GateNames.c_a1_6, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_e_sw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_12, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_e_s_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_4, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_e_se_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_5, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_e_e_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_14, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_e_ne_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_13, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_n_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_10, False)
    connect(multiworld, player, used_names, CastleRegionNames.a1_e_se_bgate, CastleRegionNames.a1_rune_room, False)
    # Requires se gate wall switch
    connect(multiworld, player, used_names, CastleRegionNames.a1_rune_room, CastleRegionNames.a1_se_cache, False)
    # Requires 4 rune switches
    connect(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_red_spikes, False)
    # Requires red spike switch
    connect(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_tp_n, False)
    # Requires tp switch
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_e, CastleRegionNames.a1_w,
                 key_silver_armory, gate_codes, armory_gate_items, GateNames.c_a1_15, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_w, CastleRegionNames.a1_nw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_0, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_w, CastleRegionNames.a1_w_ne_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_9, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_w, CastleRegionNames.a1_w_se_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_2, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_w, CastleRegionNames.a1_w_sw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_1, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a1_w, CastleRegionNames.a1_w_sw_bgate_1,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a1_11, False)
    connect(multiworld, player, used_names, CastleRegionNames.a1_w, CastleRegionNames.a1_puzzle, False)
    connect(multiworld, player, used_names, CastleRegionNames.a1_w, CastleRegionNames.a1_sw_spikes, False)
    # Requires spike switch, can also reach from a1_start

    connect(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_tp_sw, False)
    # Requires floor 5 sw teleport switch
    connect(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_tp_se, False)
    # Requires floor 5 se teleport switch
    connect(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_puzzle, False)
    # Requires floor 5 puzzle switch
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_sw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_3, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_s_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_4, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_se_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_5, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_s_save_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_10, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_start, CastleRegionNames.a2_ne,
                 key_silver_armory, gate_codes, armory_gate_items, GateNames.c_a2_6, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_ne, CastleRegionNames.a2_ne_m_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_7, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_ne, CastleRegionNames.a2_ne_l_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_1, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_ne, CastleRegionNames.a2_ne_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_0, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_ne, CastleRegionNames.a2_ne_b_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_8, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_ne, CastleRegionNames.a2_ne_save_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_9, False)
    connect(multiworld, player, used_names, CastleRegionNames.a2_ne, CastleRegionNames.a2_tp_ne, False)
    # Requires floor 5 ne teleport switch
    connect(multiworld, player, used_names, CastleRegionNames.a2_ne, CastleRegionNames.a2_e, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a2_e, CastleRegionNames.a2_e_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a2_2, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.a2_nw, CastleRegionNames.n2_start,
                 EntranceNames.c_n2_0, EntranceNames.c_a2_88)
    # Requires bonus portal switch
    connect_exit(multiworld, player, used_names, CastleRegionNames.a2_nw, CastleRegionNames.a1_from_a2,
                 EntranceNames.c_a1_1, EntranceNames.c_a2_1)
    connect(multiworld, player, used_names, CastleRegionNames.a2_nw, CastleRegionNames.a2_blue_spikes,
            False, ItemName.btnc_a2_blue_spikes, 1, False)
    connect(multiworld, player, used_names, CastleRegionNames.a2_blue_spikes, CastleRegionNames.a2_blue_spikes_tp,
            False, ItemName.btnc_a2_bspikes_tp, 1, False)
    # Requires floor 5 blue spikes teleport switch
    connect(multiworld, player, used_names, CastleRegionNames.a2_nw, CastleRegionNames.a2_to_a3, False)
    # Requires floor 6 passage open switch
    connect_exit(multiworld, player, used_names, CastleRegionNames.a2_to_a3, CastleRegionNames.a3_from_a2,
                 EntranceNames.c_a3_1, EntranceNames.c_a2_2)

    connect(multiworld, player, used_names, CastleRegionNames.n2_start, CastleRegionNames.n2_m,
            False, key_bonus_armory)
    connect(multiworld, player, used_names, CastleRegionNames.n2_m, CastleRegionNames.n2_nw,
            False, key_bonus_armory)
    connect(multiworld, player, used_names, CastleRegionNames.n2_m, CastleRegionNames.n2_n,
            False, key_bonus_armory)
    connect(multiworld, player, used_names, CastleRegionNames.n2_m, CastleRegionNames.n2_e,
            False, key_bonus_armory)
    connect(multiworld, player, used_names, CastleRegionNames.n2_m, CastleRegionNames.n2_s,
            False, key_bonus_armory)
    connect(multiworld, player, used_names, CastleRegionNames.n2_m, CastleRegionNames.n2_w,
            False, key_bonus_armory)
    connect(multiworld, player, used_names, CastleRegionNames.n2_m, CastleRegionNames.n2_se, False)
    # Requires bonus 2 open se room panel
    connect(multiworld, player, used_names, CastleRegionNames.n2_m, CastleRegionNames.n2_ne, False)
    # Requires bonus 2 open ne room panel
    connect(multiworld, player, used_names, CastleRegionNames.n2_ne, CastleRegionNames.n2_exit, False)
    # Requires bonus 2 open exit panel
    connect_exit(multiworld, player, used_names, CastleRegionNames.n2_exit, CastleRegionNames.a2_bonus_return,
                 EntranceNames.c_a2_10, None)

    connect(multiworld, player, used_names, CastleRegionNames.a3_start, CastleRegionNames.a3_main, True)
    # Requires open start top wall switch or open start right wall switch
    connect(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_knife_puzzle_reward, False)
    # Requires 5 spike puzzle switches
    connect(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_knife_reward_2, False)
    # Requires 2 spike puzzle switches
    connect_exit(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a2_nw,
                 EntranceNames.c_a2_3, EntranceNames.c_a3_2)
    connect(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_tp, False)
    # Requires floor 6 teleport switch
    # connect_generic(multiworld, player, used_names, CastleRegionNames.a3_from_a2, CastleRegionNames.a3_main)
    # Requires floor 6 from floor 5 open passage switch
    connect_gate(multiworld, player, used_names, CastleRegionNames.a3_from_a2, CastleRegionNames.a3_w_b_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a3_5, False)
    # Don't forget to add extra thing in rules requiring the teleport button for the item inside
    connect_gate(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_w_t_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a3_2, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_w_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a3_4, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_n_l_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a3_1, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_n_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a3_0, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_e_l_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a3_3, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.a3_main, CastleRegionNames.a3_e_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, GateNames.c_a3_6, False)

    connect_exit(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.b2_start,
                 EntranceNames.c_b2_0, EntranceNames.c_a1_boss, ItemName.ev_castle_b2_boss_switch, 3, False)
    connect(multiworld, player, used_names, CastleRegionNames.b2_start, CastleRegionNames.b2_arena, False)
    connect(multiworld, player, used_names, CastleRegionNames.b2_arena, CastleRegionNames.b2_defeated, False)
    connect(multiworld, player, used_names, CastleRegionNames.b2_defeated, CastleRegionNames.b2_exit, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.b2_exit, CastleRegionNames.r1_start,
                 EntranceNames.c_r1_0, EntranceNames.c_b2_1)

    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_start, CastleRegionNames.r1_se_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, GateNames.c_r1_2, False)
    connect(multiworld, player, used_names, CastleRegionNames.r1_se_ggate, CastleRegionNames.r1_e, False)
    # Requires floor 7 open east passage
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_e, CastleRegionNames.r1_e_s_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r1_5, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_e, CastleRegionNames.r1_e_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, GateNames.c_r1_7, False)
    connect(multiworld, player, used_names, CastleRegionNames.r1_e_sgate, CastleRegionNames.r1_se_wall, False)
    # Requires floor 7 open right wall
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_e, CastleRegionNames.r1_e_n_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r1_4, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_e, CastleRegionNames.r1_e_n_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r1_6, True)
    # connect_generic(multiworld, player, used_names, CastleRegionNames.r1_e, CastleRegionNames.r1_e,
    #                 False, False, key_bronze_archives)
    # Internal gate
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_e_n_bgate, CastleRegionNames.r1_e_n_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r1_3, False)
    # connect_gate(multiworld, player, used_names, CastleRegionNames.r1_e_n_bgate, CastleRegionNames.r1_e_n_bgate,
    #              key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r1_)
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_e_n_bgate, CastleRegionNames.r1_ne_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, GateNames.c_r1_1, False)
    connect(multiworld, player, used_names, CastleRegionNames.r1_ne_ggate, CastleRegionNames.r1_nw, False)
    # Requires floor 7 open North passage
    connect(multiworld, player, used_names, CastleRegionNames.r1_nw, CastleRegionNames.r1_nw_hidden, False)
    # Requires floor 7 open hidden room
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_nw_hidden, CastleRegionNames.r1_nw_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, GateNames.c_r1_0, False)
    connect(multiworld, player, used_names, CastleRegionNames.r1_nw_ggate, CastleRegionNames.r1_sw, False)
    # Requires floor 7 open west passage
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_sw, CastleRegionNames.r1_w_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, GateNames.c_r1_10, False)
    connect(multiworld, player, used_names, CastleRegionNames.r1_w_sgate, CastleRegionNames.r1_start_wall, False)
    # Requires floor 7 open start wall
    connect_gate(multiworld, player, used_names, CastleRegionNames.r1_sw, CastleRegionNames.r1_sw_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, GateNames.c_r1_11, False)
    connect(multiworld, player, used_names, CastleRegionNames.r1_sw_ggate, CastleRegionNames.r1_exit_l, False)
    # From sw requires floor 7 open left exit
    # Internal bronze gate
    r1_internals = [
        GateNames.c_r1_8,
        GateNames.c_r1_9,
    ]
    for gate in r1_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.r1_sw, CastleRegionNames.r1_sw,
                     key_bronze_archives, gate_codes, archives_gate_items, gate, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.r1_exit_l, CastleRegionNames.r2_start,
                 EntranceNames.c_r2_0, EntranceNames.c_r1_1)
    connect(multiworld, player, used_names, CastleRegionNames.r1_exit_l, CastleRegionNames.r1_exit_r, False)
    # From start requires floor 7 open right exit
    connect_exit(multiworld, player, used_names, CastleRegionNames.r1_exit_r, CastleRegionNames.r2_bswitch,
                 EntranceNames.c_r2_1, EntranceNames.c_r1_2)

    connect(multiworld, player, used_names, CastleRegionNames.r2_start, CastleRegionNames.r2_m, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.r2_m, CastleRegionNames.r2_w_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r2_0, False)
    # Internal bronze gates
    r2_internals = [
        GateNames.c_r2_6,
        GateNames.c_r2_1,
        GateNames.c_r2_2,
        GateNames.c_r2_8,
        GateNames.c_r2_3,
    ]
    for gate in r2_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.r2_m, CastleRegionNames.r2_m,
                     key_bronze_archives, gate_codes, archives_gate_items, gate, False)
    connect(multiworld, player, used_names, CastleRegionNames.r2_m, CastleRegionNames.r2_e, False)
    # Requires open east passage top or open east passage bottom
    connect_gate(multiworld, player, used_names, CastleRegionNames.r2_m, CastleRegionNames.r2_nw,
                 key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r2_7, False)  # True for button rando
    connect(multiworld, player, used_names, CastleRegionNames.r2_nw, CastleRegionNames.r2_n, False)  # True
    # Requires open north room left
    # Or requires open north room right from r2_m
    connect_gate(multiworld, player, used_names, CastleRegionNames.r2_m, CastleRegionNames.r2_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, GateNames.c_r2_5, False)
    connect(multiworld, player, used_names, CastleRegionNames.r2_sgate, CastleRegionNames.r2_s, False)
    # Requires silver gate floor button
    connect(multiworld, player, used_names, CastleRegionNames.r2_s, CastleRegionNames.r2_spike_island, False)
    # Requires open spike island passage
    connect(multiworld, player, used_names, CastleRegionNames.r2_spike_island, CastleRegionNames.r2_sw_bridge, False)
    # Requires open sw bridge from r2_s
    connect(multiworld, player, used_names, CastleRegionNames.r2_sw_bridge, CastleRegionNames.r2_puzzle, False)
    # Requires open puzzle room
    connect(multiworld, player, used_names, CastleRegionNames.r2_s, CastleRegionNames.r2_w, False)
    # Requires open west passage
    connect(multiworld, player, used_names, CastleRegionNames.r2_from_r3, CastleRegionNames.r2_ne_cache, False)
    # Requires open cache passage
    connect_gate(multiworld, player, used_names, CastleRegionNames.r2_m, CastleRegionNames.r2_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, GateNames.c_r2_4, False)  # True
    # Can also access with open exit button, it removes the wall
    connect_exit(multiworld, player, used_names, CastleRegionNames.r2_ggate, CastleRegionNames.r3_main,
                 EntranceNames.c_r3_0, EntranceNames.c_r2_2)
    # Requires open exit button

    connect(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_ne_room, False)
    # Requires open ne room
    connect(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_s_room, False)
    # Requires open south room
    connect_gate(multiworld, player, used_names, CastleRegionNames.r3_s_room, CastleRegionNames.r3_l_shop_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, GateNames.c_r3_5, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.r3_s_room, CastleRegionNames.r3_r_shop_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, GateNames.c_r3_4, False)
    connect(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_se_cache, False)
    # Requires open se cache room
    connect(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_boss_switch, False)
    # Requires open boss switch room
    connect(multiworld, player, used_names, CastleRegionNames.r3_boss_switch, CastleRegionNames.r3_rune_room, False)
    # Requires 5 open simon says room switch
    connect(multiworld, player, used_names, CastleRegionNames.r3_rune_room, CastleRegionNames.r3_bonus, False)
    # Requires 6 simon says switch
    connect_exit(multiworld, player, used_names, CastleRegionNames.r3_bonus, CastleRegionNames.n3_main,
                 EntranceNames.c_n3_0, EntranceNames.c_r3_b_ent)
    # Requires open bonus entrance passage
    connect_gate(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_sw_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, GateNames.c_r3_1, False)
    # Internal bronze gates
    r3_internals = [
        GateNames.c_r3_0,
        GateNames.c_r3_7,
        GateNames.c_r3_9,
        GateNames.c_r3_2,
        GateNames.c_r3_10,
        GateNames.c_r3_8,
    ]
    for gate in r3_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_main,
                     key_bronze_archives, gate_codes, archives_gate_items, gate, False)
    connect(multiworld, player, used_names, CastleRegionNames.r3_sw_bgate, CastleRegionNames.r3_sw_wall_l, False)
    # Requires left sw button
    connect(multiworld, player, used_names, CastleRegionNames.r3_sw_bgate, CastleRegionNames.r3_sw_wall_r, False)
    # Requires right sw button
    connect(multiworld, player, used_names, CastleRegionNames.r3_sw_wall_l, CastleRegionNames.r3_nw_tp, False)
    # Requires nw tp button
    connect(multiworld, player, used_names, CastleRegionNames.r3_bonus_return, CastleRegionNames.r3_bonus_return_bridge,
            False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.r3_bonus_return, CastleRegionNames.r2_from_r3,
                 EntranceNames.c_r2_200, EntranceNames.c_r3_250)
    connect_gate(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_e_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, GateNames.c_r3_6, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.r3_main, CastleRegionNames.r3_w_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, GateNames.c_r3_3, True)
    connect(multiworld, player, used_names, CastleRegionNames.r3_w_ggate, CastleRegionNames.r3_exit, False)
    # Requires open boss switch room
    connect_exit(multiworld, player, used_names, CastleRegionNames.r3_exit, CastleRegionNames.b3_start,
                 EntranceNames.c_b3_0, EntranceNames.c_r3_boss, ItemName.ev_castle_b3_boss_switch, 3, False)

    connect_exit(multiworld, player, used_names, CastleRegionNames.n3_main, CastleRegionNames.n3_tp_room,
                 EntranceNames.c_n3_80, EntranceNames.c_n3_12)
    connect_exit(multiworld, player, used_names, CastleRegionNames.n3_main, CastleRegionNames.r3_bonus_return,
                 EntranceNames.c_r3_b_return, None)
    # Internal bronze gates
    for i in range(3):
        connect(multiworld, player, used_names, CastleRegionNames.n3_main, CastleRegionNames.n3_main,
                False, key_bonus_archives)

    connect(multiworld, player, used_names, CastleRegionNames.b3_start, CastleRegionNames.b3_arena, False)
    connect(multiworld, player, used_names, CastleRegionNames.b3_arena, CastleRegionNames.b3_defeated, False)
    connect(multiworld, player, used_names, CastleRegionNames.b3_defeated, CastleRegionNames.b3_exit, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.b3_exit, CastleRegionNames.c1_start,
                 EntranceNames.c_c1_0, EntranceNames.c_b3_1)

    connect(multiworld, player, used_names, CastleRegionNames.c1_start, CastleRegionNames.c1_n_spikes, False)
    # Requires n spikes switch
    connect(multiworld, player, used_names, CastleRegionNames.c1_start, CastleRegionNames.c1_se_spikes, False)
    # Requires se spikes switch
    connect_gate(multiworld, player, used_names, CastleRegionNames.c1_start, CastleRegionNames.c1_shop,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c1_3, False)
    # Bronze gates with no checks
    c1_s_internals = [
        GateNames.c_c1_7,
        GateNames.c_c1_2,
        GateNames.c_c1_9,
        GateNames.c_c1_10,
        GateNames.c_c1_11,
    ]
    for gate in c1_s_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.c1_start, CastleRegionNames.c1_start,
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c1_start, CastleRegionNames.c1_w,
                 key_gold_chambers, gate_codes, chambers_gate_items, GateNames.c_c1_12, True)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c1_w, CastleRegionNames.c1_sgate,
                 key_silver_chambers, gate_codes, chambers_gate_items, GateNames.c_c1_13, True)
    connect(multiworld, player, used_names, CastleRegionNames.c1_sgate, CastleRegionNames.c1_prison_stairs, False)
    # Requires open prison door passage from c1_start
    connect_exit(multiworld, player, used_names, CastleRegionNames.c1_sgate, CastleRegionNames.c2_tp_island,
                 EntranceNames.c_c2_50, None)
    connect_exit(multiworld, player, used_names, CastleRegionNames.c1_tp_island, CastleRegionNames.c1_sgate,
                 EntranceNames.c_c1_75, None)
    connect_exit(multiworld, player, used_names, CastleRegionNames.c1_prison_stairs, CastleRegionNames.pstart_start,
                 EntranceNames.c_p_return_0, EntranceNames.c_c1_169)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c1_w, CastleRegionNames.c1_s_bgate,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c1_6, False)
    connect(multiworld, player, used_names, CastleRegionNames.c1_s_bgate, CastleRegionNames.c1_start, False)
    # Requires s shortcut button
    connect_gate(multiworld, player, used_names, CastleRegionNames.c1_s_bgate, CastleRegionNames.c1_ledge,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c1_5, False)
    # Bronze gates with no checks
    c1_s_internals = [
        GateNames.c_c1_0,
        GateNames.c_c1_1,
        GateNames.c_c1_8,
        GateNames.c_c1_4,
    ]
    for gate in c1_s_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.c1_w, CastleRegionNames.c1_w,
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.c1_w, CastleRegionNames.c2_main,
                 EntranceNames.c_c2_0, EntranceNames.c_c1_100)

    connect(multiworld, player, used_names, CastleRegionNames.pstart_start, CastleRegionNames.pstart_puzzle, False)
    # Requires 4 prison return rune switches and prison return puzzle switch

    connect(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_sw_wall, False)
    # Requires open sw wall
    connect(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_w_wall, False)
    # Requires open west wall
    connect(multiworld, player, used_names, CastleRegionNames.c2_w_shops_2, CastleRegionNames.c2_e_wall, False)
    # Requires open east wall
    connect(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_w_spikes, False)
    # Requires 4 spike floor rune switches
    connect_gate(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_w_shops_1,
                 key_silver_chambers, gate_codes, chambers_gate_items, GateNames.c_c2_11, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c2_w_shops_3, CastleRegionNames.c2_w_shops_2,
                 key_silver_chambers, gate_codes, chambers_gate_items, GateNames.c_c2_10, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_w_shops_3,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c2_3, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_e_shops_1,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c2_2, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_e_shops_2,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c2_16, False)
    # Can also access from main through open east wall
    connect(multiworld, player, used_names, CastleRegionNames.c2_e_shops_1, CastleRegionNames.c2_puzzle, False)
    # Requires open puzzle room and puzzle switch
    connect_gate(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_exit_bgate,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c2_12, False)
    # Bronze gates with no checks
    c2_internals = [
        GateNames.c_c2_5,
        GateNames.c_c2_7,
        GateNames.c_c2_18,
        GateNames.c_c2_8,
        GateNames.c_c2_15,
        GateNames.c_c2_6,
        GateNames.c_c2_13,
        GateNames.c_c2_4,
        GateNames.c_c2_17,
        GateNames.c_c2_1,
        GateNames.c_c2_0,
        GateNames.c_c2_14,
    ]
    for gate in c2_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_main,
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_n,
                 key_gold_chambers, gate_codes, chambers_gate_items, GateNames.c_c2_9, True)
    connect(multiworld, player, used_names, CastleRegionNames.c2_n, CastleRegionNames.c2_bonus, True)
    # Require 5 open bonus entrance wall switches
    connect_exit(multiworld, player, used_names, CastleRegionNames.c2_bonus, CastleRegionNames.n4_main,
                 EntranceNames.c_n4_0, EntranceNames.c_c2_b_ent)
    connect(multiworld, player, used_names, CastleRegionNames.c2_n, CastleRegionNames.c2_n_wall,
            False, ItemName.btnc_c2_n_wall, 1, False)
    connect(multiworld, player, used_names, CastleRegionNames.c2_n, CastleRegionNames.c2_n_shops,
            False, ItemName.ev_castle_c2_n_shops_switch, 1, False)
    connect(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c2_n_shops,
            False, ItemName.ev_castle_c2_n_shops_switch, 1, False)
    # Presently to open the north shops you need access to c3_nw, change to two-way for button rando
    connect_exit(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.c3_start,
                 EntranceNames.c_c3_0, EntranceNames.c_c2_45)
    connect_exit(multiworld, player, used_names, CastleRegionNames.c2_n, CastleRegionNames.c3_nw,
                 EntranceNames.c_c3_54, EntranceNames.c_c2_105)
    connect_exit(multiworld, player, used_names, CastleRegionNames.c2_tp_island, CastleRegionNames.c1_tp_island,
                 EntranceNames.c_c1_99, None)

    connect(multiworld, player, used_names, CastleRegionNames.n4_main, CastleRegionNames.n4_nw,
            False, key_bonus_chambers)
    connect(multiworld, player, used_names, CastleRegionNames.n4_main, CastleRegionNames.n4_w,
            False, key_bonus_chambers)
    connect(multiworld, player, used_names, CastleRegionNames.n4_main, CastleRegionNames.n4_e,
            False, key_bonus_chambers)
    connect_exit(multiworld, player, used_names, CastleRegionNames.n4_main, CastleRegionNames.c2_bonus_return,
                 EntranceNames.c_c2_125, None, key_bonus_chambers)

    connect_gate(multiworld, player, used_names, CastleRegionNames.c3_start, CastleRegionNames.c3_rspike_switch,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c3_1, False)
    # Can also get there if you have red spike switch
    connect(multiworld, player, used_names, CastleRegionNames.c3_rspike_switch, CastleRegionNames.c3_rspikes,
            False, ItemName.ev_castle_c3_rspikes_switch, 1, False)
    # From c3_start technically, but route through gate so that we require it
    connect_gate(multiworld, player, used_names, CastleRegionNames.c3_rspikes, CastleRegionNames.c3_s_bgate,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c3_8, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c3_rspikes, CastleRegionNames.c3_m_shop,
                 key_bronze_chambers, gate_codes, chambers_gate_items, GateNames.c_c3_5, False)
    connect(multiworld, player, used_names, CastleRegionNames.c3_rspikes, CastleRegionNames.c3_m_wall, False)
    # Requires open middle passage
    connect(multiworld, player, used_names, CastleRegionNames.c3_rspikes, CastleRegionNames.c3_m_tp, False)
    # Requires teleport middle item
    # Bronze gates with no checks
    c3_s_internals = [
        GateNames.c_c3_6,
        GateNames.c_c3_12,
        GateNames.c_c3_11,
        GateNames.c_c3_3,
        GateNames.c_c3_4,
        GateNames.c_c3_13,
        GateNames.c_c3_7,
        GateNames.c_c3_14,
    ]
    for gate in c3_s_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.c3_rspikes, CastleRegionNames.c3_rspikes,
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_gate(multiworld, player, used_names, CastleRegionNames.c3_rspikes, CastleRegionNames.c3_nw,
                 key_gold_chambers, gate_codes, chambers_gate_items, GateNames.c_c3_9, True)
    # Bronze gates with no checks
    c3_n_internals = [
        GateNames.c_c3_2,
        GateNames.c_c3_0,
        GateNames.c_c3_10,
    ]
    for gate in c3_n_internals:
        connect_gate(multiworld, player, used_names, CastleRegionNames.c3_nw, CastleRegionNames.c3_nw,
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect(multiworld, player, used_names, CastleRegionNames.c3_rspikes, CastleRegionNames.c3_sw_hidden,
            False, ItemName.ev_castle_c3_sw_hidden_switch, 6, False)
    connect(multiworld, player, used_names, CastleRegionNames.c3_sw_hidden, CastleRegionNames.c3_se_hidden, False)
    # Requires open se hidden wall switch
    connect(multiworld, player, used_names, CastleRegionNames.c3_se_hidden, CastleRegionNames.c3_light_bridge, False)
    # Requires activate light bridge switch
    connect_exit(multiworld, player, used_names, CastleRegionNames.c3_sw_hidden, CastleRegionNames.c3_fire_floor,
                 EntranceNames.c_c3_67, None)
    connect(multiworld, player, used_names, CastleRegionNames.c3_fire_floor, CastleRegionNames.c3_fire_floor_tp, False)
    connect_exit(multiworld, player, used_names, CastleRegionNames.c3_fire_floor, CastleRegionNames.c2_c3_tp,
                 EntranceNames.c_c2_77, None)
    connect_exit(multiworld, player, used_names, CastleRegionNames.c2_c3_tp, CastleRegionNames.c3_c2_tp,
                 EntranceNames.c_c3_156, None)

    # Old connect method to ensure no keys will in the final boss room
    connect_exit(multiworld, player, used_names, CastleRegionNames.c2_main, CastleRegionNames.b4_start,
                 EntranceNames.c_b4_0, EntranceNames.c_c2_boss, ItemName.ev_castle_b4_boss_switch, 3, False)
    connect(multiworld, player, used_names, CastleRegionNames.b4_start, CastleRegionNames.b4_defeated, False)

    # The escape sequence rooms aren't randomized, it makes the escape goal too easy!
    planks_to_win = multiworld.planks_required_count[player]
    connect(multiworld, player, used_names, CastleRegionNames.b4_defeated, CastleRegionNames.e1_main,
            False, ItemName.plank, 12, False)
    # Technically planks are consumed, but nothing else does so this is faster
    connect(multiworld, player, used_names, CastleRegionNames.e1_main, CastleRegionNames.e2_main, False)
    connect(multiworld, player, used_names, CastleRegionNames.e2_main, CastleRegionNames.e3_main, False)
    connect(multiworld, player, used_names, CastleRegionNames.e3_main, CastleRegionNames.e4_main, False)
    connect(multiworld, player, used_names, CastleRegionNames.e4_main, CastleRegionNames.escaped, False)

    connect(multiworld, player, used_names, CastleRegionNames.menu, CastleRegionNames.get_planks,
            False, ItemName.plank, planks_to_win, False)


def create_tots_regions(multiworld, player: int, active_locations: typing.Dict[str, LocationData],
                        random_locations: typing.Dict[str, int]):
    menu_region = create_region(multiworld, player, active_locations, TempleRegionNames.menu, None)

    get_planks_locations = []
    if get_goal_type(multiworld, player) == GoalType.PlankHunt:
        get_planks_locations.append(TempleLocationNames.ev_victory)
    get_planks_region = create_region(multiworld, player, active_locations, TempleRegionNames.get_planks,
                                      get_planks_locations)

    hub_main_locations = [
        TempleLocationNames.hub_front_of_pof,
        TempleLocationNames.hub_behind_temple_entrance
    ]
    dunes_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.hub_main,
                                      hub_main_locations)

    dunes_rocks_locations = [
        TempleLocationNames.hub_behind_shops,
        TempleLocationNames.hub_on_rock,
        TempleLocationNames.hub_west_pyramid,
        TempleLocationNames.hub_rocks_south,
        TempleLocationNames.hub_field_south,
        TempleLocationNames.hub_field_nw,
        TempleLocationNames.hub_field_north,
        TempleLocationNames.ev_hub_pof_switch
    ]
    dunes_rocks_region = create_region(multiworld, player, active_locations, TempleRegionNames.hub_rocks,
                                       dunes_rocks_locations)

    dunes_pyramid_locations = [
        TempleLocationNames.hub_pof_reward
    ]
    dunes_pyramid_region = create_region(multiworld, player, active_locations, TempleRegionNames.hub_pyramid_of_fear,
                                         dunes_pyramid_locations)

    library_region = create_region(multiworld, player, active_locations, TempleRegionNames.library, [])
    library_lobby_region = create_region(multiworld, player, active_locations, TempleRegionNames.library_lobby, [])

    cave3_main_locations = [
        TempleLocationNames.cave3_squire,
        TempleLocationNames.cave3_guard,
        TempleLocationNames.cave3_ne,
        TempleLocationNames.cave3_nw,
        TempleLocationNames.cave3_m,
        TempleLocationNames.cave3_half_bridge,
        TempleLocationNames.cave3_n,
        TempleLocationNames.cave3_secret_n,
        TempleLocationNames.cave3_secret_nw,
        TempleLocationNames.cave3_secret_s,
        TempleLocationNames.c3_miniboss_tick_1,
        TempleLocationNames.c3_miniboss_tick_2,
        TempleLocationNames.c3_tower_plant_small_1,
        TempleLocationNames.c3_tower_plant_small_2,
        TempleLocationNames.c3_tower_plant_small_3,
        TempleLocationNames.c3_tower_plant_small_4,
        TempleLocationNames.c3_tower_plant_small_5,
        TempleLocationNames.c3_tower_plant_small_6,
    ]
    cave3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_main,
                                      cave3_main_locations)

    c3_puzzle_locs = [
        TempleLocationNames.c3_puzzle_1,
        TempleLocationNames.c3_puzzle_2,
        TempleLocationNames.c3_puzzle_3,
        TempleLocationNames.c3_puzzle_4,
    ]
    c3_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.c3_puzzle, c3_puzzle_locs)

    c3_e_locs = [
        TempleLocationNames.cave3_outside_guard,
        TempleLocationNames.cave3_se,
        TempleLocationNames.cave3_trapped_guard,
        TempleLocationNames.c3_tower_plant,
        TempleLocationNames.c3_tower_plant_small_7,
        TempleLocationNames.c3_tower_plant_small_8,
        TempleLocationNames.ev_c3_portal,
    ]
    c3_e_region = create_region(multiworld, player, active_locations, TempleRegionNames.c3_e, c3_e_locs)

    cave3_fall_locations = [
        TempleLocationNames.cave3_fall_nw,
        TempleLocationNames.cave3_fall_ne,
        TempleLocationNames.cave3_fall_sw,
        TempleLocationNames.cave3_fall_se
    ]
    cave3_fall_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_fall,
                                      cave3_fall_locations)

    cave3_fields_locations = [
        TempleLocationNames.cave3_captain,
        TempleLocationNames.cave3_captain_dock,
    ]
    cave3_fields_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_fields,
                                        cave3_fields_locations)

    c3_e_water_locs = [
        TempleLocationNames.cave3_fields_r,
    ]
    c3_e_water_region = create_region(multiworld, player, active_locations, TempleRegionNames.c3_e_water,
                                      c3_e_water_locs)

    cave3_portal_locations = [
        TempleLocationNames.cave3_portal_l,
        TempleLocationNames.cave3_portal_r,
        TempleLocationNames.ev_cave3_pof_switch
    ]
    cave3_portal_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_portal,
                                        cave3_portal_locations)

    cave3_secret_locations = [
        TempleLocationNames.cave3_secret_1,
        TempleLocationNames.cave3_secret_2,
        TempleLocationNames.cave3_secret_3,
        TempleLocationNames.cave3_secret_4,
        TempleLocationNames.cave3_secret_5,
        TempleLocationNames.cave3_secret_6,
        TempleLocationNames.cave3_secret_7,
        TempleLocationNames.cave3_secret_8,
        TempleLocationNames.cave3_secret_9,
        TempleLocationNames.cave3_secret_10,
        TempleLocationNames.cave3_secret_11,
        TempleLocationNames.cave3_secret_12,
    ]
    cave3_secret_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_secret,
                                        cave3_secret_locations)

    cave2_main_locations = [
        TempleLocationNames.cave2_nw_2,
        TempleLocationNames.cave2_double_bridge_r,
        TempleLocationNames.cave2_guard_s,
        TempleLocationNames.cave2_nw_3,
        TempleLocationNames.cave2_w_miniboss_4,
        TempleLocationNames.cave2_below_pumps_3,
        TempleLocationNames.cave2_nw_1,
        TempleLocationNames.cave2_pumps_n,
        TempleLocationNames.cave2_guard,
        TempleLocationNames.cave2_below_pumps_1,
        TempleLocationNames.cave2_below_pumps_2,
        TempleLocationNames.cave2_e_1,
        TempleLocationNames.cave2_e_2,
        TempleLocationNames.cave2_nw_4,
        TempleLocationNames.cave2_nw_5,
        TempleLocationNames.cave2_w_miniboss_3,
        TempleLocationNames.cave2_w_miniboss_2,
        TempleLocationNames.cave2_w_miniboss_1,
        TempleLocationNames.cave2_red_bridge_se_1,
        TempleLocationNames.cave2_red_bridge_se_2,
        TempleLocationNames.cave2_e_3,
        TempleLocationNames.cave2_e_4,
        TempleLocationNames.cave2_guard_n,
        TempleLocationNames.cave2_secret_ne,
        TempleLocationNames.cave2_secret_m,
        TempleLocationNames.c2_miniboss_maggot_w_1,
        TempleLocationNames.c2_miniboss_maggot_w_2,
        TempleLocationNames.c2_miniboss_tick_1,
        TempleLocationNames.c2_miniboss_tick_2,
        TempleLocationNames.c2_tower_plant_1,
        TempleLocationNames.c2_tower_plant_3,
        TempleLocationNames.c2_tower_plant_small_1,
        TempleLocationNames.c2_tower_plant_small_2,
        TempleLocationNames.c2_tower_plant_small_3,
        TempleLocationNames.c2_tower_plant_small_4,
        TempleLocationNames.c2_tower_plant_small_5,
        TempleLocationNames.c2_tower_plant_small_6,
        TempleLocationNames.c2_tower_plant_small_7,
        TempleLocationNames.c2_tower_plant_small_8,
        TempleLocationNames.c2_tower_plant_small_9,
        TempleLocationNames.c2_tower_plant_small_11,
        TempleLocationNames.c2_tower_plant_small_12,
        TempleLocationNames.c2_tower_plant_small_13,
        TempleLocationNames.c2_tower_plant_small_14,
        TempleLocationNames.c2_tower_plant_small_15,
        TempleLocationNames.c2_tower_plant_small_17,
        TempleLocationNames.c2_tower_plant_small_18,
        TempleLocationNames.c2_tower_plant_small_20,
        TempleLocationNames.c2_tower_plant_small_21,
        TempleLocationNames.c2_tower_plant_small_23,
        TempleLocationNames.ev_c2_portal,
    ]
    cave2_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_2_main,
                                      cave2_main_locations)

    cave2_pumps_locations = [
        TempleLocationNames.cave2_pumps_wall_r,
        TempleLocationNames.cave2_pumps_wall_l,
        TempleLocationNames.cave2_water_n_r_1,
        TempleLocationNames.cave2_water_n_l,
        TempleLocationNames.ev_cave2_pof_switch,
        TempleLocationNames.cave2_water_n_r_2,
        TempleLocationNames.cave2_water_s,
    ]
    cave2_pumps_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_2_pumps,
                                       cave2_pumps_locations)

    cave_2_red_bridge_locations = [
        TempleLocationNames.cave2_red_bridge_1,
        TempleLocationNames.cave2_red_bridge_2,
        TempleLocationNames.cave2_red_bridge_3,
        TempleLocationNames.cave2_red_bridge_4,
    ]
    cave2_red_bridge_region = create_region(multiworld, player, active_locations, TempleRegionNames.c2_red_bridge,
                                            cave_2_red_bridge_locations)

    cave_2_green_bridge_locations = [
        TempleLocationNames.cave2_green_bridge,
    ]
    cave2_green_bridge_region = create_region(multiworld, player, active_locations, TempleRegionNames.c2_green_bridge,
                                              cave_2_green_bridge_locations)

    c2_double_bridge_locs = [
        TempleLocationNames.cave2_double_bridge_m,
    ]
    c2_double_bridge_region = create_region(multiworld, player, active_locations, TempleRegionNames.c2_double_bridge,
                                            c2_double_bridge_locs)

    c2_sw_locs = [
        TempleLocationNames.cave2_sw_hidden_room_1,
        TempleLocationNames.cave2_sw_hidden_room_2,
        TempleLocationNames.cave2_sw_hidden_room_3,
        TempleLocationNames.cave2_sw_hidden_room_4,
        TempleLocationNames.cave2_double_bridge_l_1,
        TempleLocationNames.cave2_double_bridge_l_2,
        TempleLocationNames.cave2_sw,
        TempleLocationNames.cave2_double_bridge_secret,
        TempleLocationNames.cave2_secret_w,
        TempleLocationNames.c2_miniboss_maggot_s_1,
        TempleLocationNames.c2_miniboss_maggot_s_2,
        TempleLocationNames.c2_tower_plant_2,
        TempleLocationNames.c2_tower_plant_small_10,
        TempleLocationNames.c2_tower_plant_small_16,
        TempleLocationNames.c2_tower_plant_small_19,
        TempleLocationNames.c2_tower_plant_small_22,
    ]
    c2_sw_region = create_region(multiworld, player, active_locations, TempleRegionNames.c2_sw, c2_sw_locs)

    c2_puzzle_locs = [
        TempleLocationNames.c2_puzzle_1,
        TempleLocationNames.c2_puzzle_2,
        TempleLocationNames.c2_puzzle_3,
        TempleLocationNames.c2_puzzle_4,
    ]
    c2_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.c2_puzzle, c2_puzzle_locs)

    cave1_main_locations = [
        TempleLocationNames.cave1_n_3,
        TempleLocationNames.cave1_w_by_water_2,
        TempleLocationNames.cave1_s_3,
        TempleLocationNames.cave1_m,
        TempleLocationNames.cave1_double_room_l,
        TempleLocationNames.cave1_double_room_r,
        TempleLocationNames.cave1_n_1,
        TempleLocationNames.cave1_n_2,
        TempleLocationNames.cave1_w_1,
        TempleLocationNames.cave1_w_2,
        TempleLocationNames.cave1_s_4,
        TempleLocationNames.cave1_s_5,
        TempleLocationNames.cave1_n_room_1,
        TempleLocationNames.cave1_n_room_2,
        TempleLocationNames.cave1_n_room_3,
        TempleLocationNames.cave1_n_room_4,
        TempleLocationNames.cave1_s_1,
        TempleLocationNames.cave1_s_2,
        TempleLocationNames.cave1_w_by_water_1,
        TempleLocationNames.cave1_secret_nw,
        TempleLocationNames.cave1_secret_w,
        TempleLocationNames.cave1_secret_m,
        TempleLocationNames.c1_miniboss_maggot_s_1,
        TempleLocationNames.c1_miniboss_maggot_s_2,
        TempleLocationNames.c1_miniboss_tick_1,
        TempleLocationNames.c1_miniboss_tick_2,
        TempleLocationNames.c1_tower_plant_1,
        TempleLocationNames.c1_tower_plant_3,
        TempleLocationNames.c1_tower_plant_small_5,
        TempleLocationNames.c1_tower_plant_small_6,
        TempleLocationNames.c1_tower_plant_small_7,
        TempleLocationNames.c1_tower_plant_small_8,
        TempleLocationNames.c1_tower_plant_small_11,
        TempleLocationNames.c1_tower_plant_small_12,
    ]
    cave1_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_main,
                                      cave1_main_locations)

    c1_n_puzzle_locs = [
        TempleLocationNames.c1_n_puzzle_1,
        TempleLocationNames.c1_n_puzzle_2,
        TempleLocationNames.c1_n_puzzle_3,
        TempleLocationNames.c1_n_puzzle_4,
    ]
    c1_n_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.c1_n_puzzle,
                                       c1_n_puzzle_locs)

    cave1_blue_bridge_locations = [
        TempleLocationNames.cave1_ne_hidden_room_1,
        TempleLocationNames.cave1_ne_hidden_room_2,
        TempleLocationNames.cave1_ne_hidden_room_3,
        TempleLocationNames.cave1_ne_hidden_room_4,
        TempleLocationNames.cave1_ne_hidden_room_5,
        TempleLocationNames.cave1_ne_grubs,
        TempleLocationNames.cave1_n_bridges_1,
        TempleLocationNames.cave1_n_bridges_4,
        TempleLocationNames.cave1_n_bridges_5,
        TempleLocationNames.cave1_secret_n_hidden_room,
        TempleLocationNames.cave1_ne_1,
        TempleLocationNames.cave1_ne_2,
        TempleLocationNames.cave1_ne_3,
        TempleLocationNames.cave1_ne_4,
        TempleLocationNames.cave1_ne_5,
        TempleLocationNames.cave1_n_bridges_2,
        TempleLocationNames.cave1_n_bridges_3,
        TempleLocationNames.cave1_secret_ne,
        TempleLocationNames.c1_miniboss_maggot_ne_1,
        TempleLocationNames.c1_miniboss_maggot_ne_2,
        TempleLocationNames.c1_tower_plant_2,
        TempleLocationNames.c1_tower_plant_4,
        TempleLocationNames.c1_tower_plant_small_1,
        TempleLocationNames.c1_tower_plant_small_2,
        TempleLocationNames.c1_tower_plant_small_3,
        TempleLocationNames.c1_tower_plant_small_4,
        TempleLocationNames.c1_tower_plant_small_9,
        TempleLocationNames.c1_tower_plant_small_10,
        TempleLocationNames.c1_tower_plant_small_13,
        TempleLocationNames.c1_tower_plant_small_14,
        TempleLocationNames.ev_cave1_pof_switch,
    ]
    cave1_blue_bridge_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_blue_bridge,
                                             cave1_blue_bridge_locations)

    c1_secret_hall_locs = [
        TempleLocationNames.cave1_secret_tunnel_1,
        TempleLocationNames.cave1_secret_tunnel_2,
        TempleLocationNames.cave1_secret_tunnel_3,
    ]
    c1_secret_hall_region = create_region(multiworld, player, active_locations, TempleRegionNames.c1_secret_hall,
                                          c1_secret_hall_locs)

    cave1_red_bridge_locations = [
        TempleLocationNames.cave1_e_2,
        TempleLocationNames.cave1_e_3,
        TempleLocationNames.cave1_red_bridge_e,
        TempleLocationNames.cave1_se_1,
        TempleLocationNames.cave1_se_2,
        TempleLocationNames.cave1_e_1,
        TempleLocationNames.cave1_secret_e,
    ]
    cave1_red_bridge_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_red_bridge,
                                            cave1_red_bridge_locations)

    c1_e_puzzle_locs = [
        TempleLocationNames.c1_e_puzzle_1,
        TempleLocationNames.c1_e_puzzle_2,
        TempleLocationNames.c1_e_puzzle_3,
        TempleLocationNames.c1_e_puzzle_4,
    ]
    c1_e_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.c1_e_puzzle,
                                       c1_e_puzzle_locs)

    cave1_green_bridge_locations = [
        TempleLocationNames.cave1_green_bridge_1,
        TempleLocationNames.cave1_green_bridge_2,
    ]
    cave1_green_bridge_region = create_region(multiworld, player, active_locations,
                                              TempleRegionNames.cave_1_green_bridge,
                                              cave1_green_bridge_locations)

    c1_storage_locs = [
        TempleLocationNames.cave1_krilith_ledge_n,
        TempleLocationNames.cave1_krilith_ledge_e,
        TempleLocationNames.cave1_krilith_door,
    ]
    c1_storage_island_region = create_region(multiworld, player, active_locations, TempleRegionNames.c1_storage_island,
                                             c1_storage_locs)

    cave1_pumps_locations = [
        TempleLocationNames.cave1_water_s_shore,
        TempleLocationNames.cave1_water_s_1,
        TempleLocationNames.cave1_water_s_2,
        TempleLocationNames.cave1_water_s_3,
        TempleLocationNames.cave1_water_s_4,
        TempleLocationNames.cave1_water_s_5,
    ]
    cave1_pumps_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_pumps,
                                       cave1_pumps_locations)

    cave1_temple_locations = [
        TempleLocationNames.cave1_temple_hall_1,
        TempleLocationNames.cave1_temple_hall_2,
        TempleLocationNames.cave1_temple_hall_3,
        TempleLocationNames.cave1_temple_end_2,
        TempleLocationNames.cave1_temple_end_3,
        TempleLocationNames.cave1_temple_end_4,
        TempleLocationNames.cave1_temple_end_1,
    ]
    cave1_temple_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_temple,
                                        cave1_temple_locations)
    # Dynamically place portal event location
    c1_portal_loc = HammerwatchLocation(player, TempleLocationNames.ev_c1_portal)
    if random_locations[TempleLocationNames.rloc_c1_portal] == 1:
        cave1_main_region.locations.append(c1_portal_loc)
        c1_portal_loc.parent_region = cave1_main_region
    else:
        cave1_blue_bridge_region.locations.append(c1_portal_loc)
        c1_portal_loc.parent_region = cave1_blue_bridge_region

    boss1_entrance_locations = [
        TempleLocationNames.boss1_guard_l,
        TempleLocationNames.boss1_guard_r_1,
        TempleLocationNames.boss1_guard_r_2,
    ]
    boss1_entrance_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss_1_entrance,
                                          boss1_entrance_locations)

    boss1_arena_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss_1_arena, [])

    boss1_defeated_locations = [
        TempleLocationNames.b1_boss_worm_1_1,
        TempleLocationNames.b1_boss_worm_1_2,
        TempleLocationNames.b1_boss_worm_2_1,
        TempleLocationNames.b1_boss_worm_2_2,
        TempleLocationNames.b1_boss_worm_3_1,
        TempleLocationNames.b1_boss_worm_3_2,
        TempleLocationNames.b1_boss_worm_4_1,
        TempleLocationNames.b1_boss_worm_4_2,
        TempleLocationNames.b1_boss_worm_key,
        TempleLocationNames.ev_beat_boss_1,
    ]
    boss1_defeated_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss_1_defeated,
                                          boss1_defeated_locations)

    b1_back_locs = [
        TempleLocationNames.boss1_bridge,
        TempleLocationNames.boss1_bridge_n,
        TempleLocationNames.boss1_secret,
    ]
    b1_back_region = create_region(multiworld, player, active_locations, TempleRegionNames.b1_back, b1_back_locs)

    passage_entrance_locations = [
        TempleLocationNames.p_ent2_secret
    ]
    passage_entrance_region = create_region(multiworld, player, active_locations, TempleRegionNames.passage_entrance,
                                            passage_entrance_locations)

    passage_mid_locations = [
        TempleLocationNames.p_mid1_1,
        TempleLocationNames.p_mid1_2,
        TempleLocationNames.p_mid2_1,
        TempleLocationNames.p_mid2_2,
        TempleLocationNames.p_mid2_3,
        TempleLocationNames.p_mid2_4,
        TempleLocationNames.p_mid3_secret_1,
        TempleLocationNames.p_mid3_secret_2,
        TempleLocationNames.p_mid3_secret_3,
        TempleLocationNames.p_mid3_secret_4,
        TempleLocationNames.p_mid4_1,
        TempleLocationNames.p_mid4_2,
        TempleLocationNames.p_mid4_3,
        TempleLocationNames.p_mid4_4,
        TempleLocationNames.p_mid5_1,
        TempleLocationNames.p_mid5_2,
        TempleLocationNames.p_mid5_secret,
        TempleLocationNames.p_tower_plant_small_1,
        TempleLocationNames.p_tower_plant_small_2,
        TempleLocationNames.p_tower_plant_small_3,
        TempleLocationNames.p_tower_plant_small_4,
        TempleLocationNames.p_tower_plant_small_5,
        TempleLocationNames.p_tower_plant_small_6,
    ]
    passage_mid_region = create_region(multiworld, player, active_locations, TempleRegionNames.passage_mid,
                                       passage_mid_locations)

    passage_puzzle_locations = [
        TempleLocationNames.p_puzzle_1,
        TempleLocationNames.p_puzzle_2,
        TempleLocationNames.p_puzzle_3,
        TempleLocationNames.p_puzzle_4,
    ]
    passage_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.passage_puzzle,
                                          passage_puzzle_locations)

    passage_end_locations = [
        TempleLocationNames.p_end1_secret,
        TempleLocationNames.p_end3_1,
        TempleLocationNames.p_end3_2,
    ]
    passage_end_region = create_region(multiworld, player, active_locations, TempleRegionNames.passage_end,
                                       passage_end_locations)

    temple_entrance_region = create_region(multiworld, player, active_locations, TempleRegionNames.temple_entrance, [])

    temple_entrance_back_locations = [
        TempleLocationNames.temple_entrance_l,
        TempleLocationNames.temple_entrance_r,
        TempleLocationNames.ev_temple_entrance_rock,
    ]
    temple_entrance_back_region = create_region(multiworld, player, active_locations,
                                                TempleRegionNames.temple_entrance_back,
                                                temple_entrance_back_locations)

    t1_main_locations = [
        TempleLocationNames.t1_above_s_bridge,
        TempleLocationNames.t1_s_bridge_1,
        TempleLocationNames.t1_s_bridge_2,
        TempleLocationNames.t1_s_bridge_3,
        TempleLocationNames.t1_s_bridge_4,
        TempleLocationNames.t1_s_bridge_5,
        TempleLocationNames.t1_s_bridge_6,
        TempleLocationNames.t1_sw_sun_room_1,
        TempleLocationNames.t1_sw_sun_room_2,
        TempleLocationNames.t1_sw_corner_room,
        TempleLocationNames.t1_sw_hidden_room_1,
        TempleLocationNames.t1_sw_hidden_room_2,
        TempleLocationNames.t1_sw_hidden_room_3,
        TempleLocationNames.t1_sw_hidden_room_4,
    ]
    t1_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_main, t1_main_locations)

    t1_w_puzzle_locs = [
        TempleLocationNames.t1_w_puzzle_1,
        TempleLocationNames.t1_w_puzzle_2,
        TempleLocationNames.t1_w_puzzle_3,
        TempleLocationNames.t1_w_puzzle_4,
    ]
    t1_w_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_w_puzzle,
                                       t1_w_puzzle_locs)

    t1_sw_sdoor_locations = [
        TempleLocationNames.t1_sw_sdoor_1,
        TempleLocationNames.t1_sw_sdoor_2,
        TempleLocationNames.t1_sw_sdoor_3,
        TempleLocationNames.t1_sw_sdoor_4,
        TempleLocationNames.t1_sw_sdoor_5,
    ]
    t1_sw_cache_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_sw_sdoor,
                                       t1_sw_sdoor_locations)

    t1_node_1_locations = [
        TempleLocationNames.ev_t1_s_node
    ]
    t1_node_1_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_node_1,
                                     t1_node_1_locations)

    t1_w_locations = [
        TempleLocationNames.t1_double_gate_1,
        TempleLocationNames.t1_double_gate_2,
        TempleLocationNames.t1_double_gate_3,
        TempleLocationNames.t1_double_gate_hidden,
        TempleLocationNames.t1_behind_bars_entrance,
        TempleLocationNames.t1_e_of_double_gate_room_1,
        TempleLocationNames.t1_e_of_double_gate_room_2,
        TempleLocationNames.t1_e_of_double_gate_room_3,
        TempleLocationNames.t1_e_of_double_gate_room_4,
        TempleLocationNames.t1_mana_drain_fire_trap,
        TempleLocationNames.t1_mana_drain_fire_trap_reward_1,
        TempleLocationNames.t1_mana_drain_fire_trap_reward_2,
        TempleLocationNames.t1_mana_drain_fire_trap_passage,
    ]
    t1_w_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_w, t1_w_locations)

    t1_sun_turret_locations = [
        TempleLocationNames.t1_double_gate_behind_block,
        TempleLocationNames.t1_s_of_sun_turret,
        TempleLocationNames.t1_sun_turret_1,
        TempleLocationNames.t1_sun_turret_2,
        TempleLocationNames.t1_sun_turret_3,
        TempleLocationNames.t1_fire_trap_by_sun_turret_1,
        TempleLocationNames.t1_fire_trap_by_sun_turret_2,
        TempleLocationNames.t1_fire_trap_by_sun_turret_3,
        TempleLocationNames.t1_fire_trap_by_sun_turret_4,
        TempleLocationNames.t1_tower_fire,
    ]
    t1_sun_turret_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_sun_turret,
                                         t1_sun_turret_locations)

    t1_ice_turret_locations = [
        TempleLocationNames.t1_ice_turret_1,
        TempleLocationNames.t1_ice_turret_2,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_1,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_2,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_3,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_4,
        TempleLocationNames.t1_ice_turret_boulder_break_block,
        TempleLocationNames.t1_n_sunbeam,
        TempleLocationNames.t1_n_sunbeam_treasure_1,
        TempleLocationNames.t1_n_sunbeam_treasure_2,
        TempleLocationNames.t1_n_sunbeam_treasure_3,
        TempleLocationNames.t1_tower_ice,
        TempleLocationNames.ev_t1_n_node_n_mirrors,
    ]
    t1_ice_turret_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_ice_turret,
                                         t1_ice_turret_locations)

    t1_telarian_locs = [
        TempleLocationNames.t1_telarian_1,
        TempleLocationNames.t1_telarian_2,
        TempleLocationNames.t1_telarian_3,
        TempleLocationNames.t1_telarian_4,
        TempleLocationNames.t1_telarian_5,
    ]
    t1_telarian_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_telarian,
                                       t1_telarian_locs)

    t1_n_of_ice_turret_locations = [
        TempleLocationNames.t1_n_cache_by_ice_turret_1,
        TempleLocationNames.t1_n_cache_by_ice_turret_2,
        TempleLocationNames.t1_n_cache_by_ice_turret_3,
        TempleLocationNames.t1_n_cache_by_ice_turret_4,
        TempleLocationNames.t1_n_cache_by_ice_turret_5,
    ]
    t1_n_of_ice_turret_region = create_region(multiworld, player, active_locations,
                                              TempleRegionNames.t1_n_of_ice_turret,
                                              t1_n_of_ice_turret_locations)

    t1_s_of_ice_turret_locations = [
        TempleLocationNames.t1_s_cache_by_ice_turret_1,
        TempleLocationNames.t1_s_cache_by_ice_turret_2,
        TempleLocationNames.t1_s_cache_by_ice_turret_3,
    ]
    t1_s_of_ice_turret_region = create_region(multiworld, player, active_locations,
                                              TempleRegionNames.t1_s_of_ice_turret,
                                              t1_s_of_ice_turret_locations)

    t1_east_locations = [
        TempleLocationNames.t1_ledge_after_block_trap_1,
        TempleLocationNames.t1_ledge_after_block_trap_2,
        TempleLocationNames.t1_ice_block_chamber_1,
        TempleLocationNames.t1_ice_block_chamber_2,
        TempleLocationNames.t1_ice_block_chamber_3,
        TempleLocationNames.t1_node_2_1,
        TempleLocationNames.t1_node_2_2,
        TempleLocationNames.t1_node_2_passage_1,
        TempleLocationNames.t1_node_2_passage_2,
        TempleLocationNames.t1_node_2_passage_3,
        TempleLocationNames.ev_temple1_pof_switch,
        TempleLocationNames.t1_miniboss_mummy,
        TempleLocationNames.ev_t1_n_node_s_mirror,
    ]
    t1_east_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_east, t1_east_locations)

    t1_e_puzzle_locs = [
        TempleLocationNames.t1_e_puzzle_1,
        TempleLocationNames.t1_e_puzzle_2,
        TempleLocationNames.t1_e_puzzle_3,
        TempleLocationNames.t1_e_puzzle_4,
    ]
    t1_e_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_e_puzzle,
                                       t1_e_puzzle_locs)

    t1_jail_e_locs = [
        TempleLocationNames.t1_e_gold_beetles,
    ]
    t1_jail_e_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_jail_e, t1_jail_e_locs)

    t1_sun_block_hall_locations = [
        TempleLocationNames.t1_sun_block_hall_1,
        TempleLocationNames.t1_sun_block_hall_2,
        TempleLocationNames.t1_sun_block_hall_3,
        TempleLocationNames.t1_sun_block_hall_4,
    ]
    t1_sun_block_hall_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_sun_block_hall,
                                             t1_sun_block_hall_locations)

    t1_node_2_locations = [
        TempleLocationNames.ev_t1_n_node
    ]
    t1_node_2_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_node_2,
                                     t1_node_2_locations)

    t1_telarian_melt_ice_locations = [
        TempleLocationNames.t1_telarian_ice
    ]
    t1_telarian_melt_ice_region = create_region(multiworld, player, active_locations,
                                                TempleRegionNames.t1_telarian_melt_ice,
                                                t1_telarian_melt_ice_locations)

    t1_ice_chamber_melt_ice_locations = [
        TempleLocationNames.t1_ice_block_chamber_ice
    ]
    t1_ice_chamber_melt_ice_region = create_region(multiworld, player, active_locations,
                                                   TempleRegionNames.t1_ice_chamber_melt_ice,
                                                   t1_ice_chamber_melt_ice_locations)
    # Dynamically place portal event location
    t1_portal_loc = HammerwatchLocation(player, TempleLocationNames.ev_t1_portal)
    if random_locations[TempleLocationNames.rloc_t1_portal] == 0:
        t1_east_region.locations.append(t1_portal_loc)
        t1_portal_loc.parent_region = t1_east_region
    elif random_locations[TempleLocationNames.rloc_t1_portal] == 1:
        t1_ice_turret_region.locations.append(t1_portal_loc)
        t1_portal_loc.parent_region = t1_ice_turret_region
    else:
        t1_sun_turret_region.locations.append(t1_portal_loc)
        t1_portal_loc.parent_region = t1_sun_turret_region

    boss2_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss2_main, [])

    boss2_defeated_locations = [
        TempleLocationNames.boss2_nw,
        TempleLocationNames.boss2_se,
        TempleLocationNames.ev_beat_boss_2
    ]
    boss2_defeated_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss2_defeated,
                                          boss2_defeated_locations)

    t2_main_locations = [
        TempleLocationNames.t2_n_of_portal,
        TempleLocationNames.t2_s_of_portal,
        TempleLocationNames.t2_w_spike_trap_1,
        TempleLocationNames.t2_w_spike_trap_2,
        TempleLocationNames.t2_nw_puzzle_cache_1,
        TempleLocationNames.t2_nw_puzzle_cache_2,
        TempleLocationNames.t2_nw_puzzle_cache_3,
        TempleLocationNames.t2_nw_puzzle_cache_4,
        TempleLocationNames.t2_nw_puzzle_cache_5,
        TempleLocationNames.t2_nw_of_s_ice_turret,
        TempleLocationNames.t2_w_hall_dead_end_1,
        TempleLocationNames.t2_w_hall_dead_end_2,
        TempleLocationNames.t2_w_hall_dead_end_3,
        TempleLocationNames.t2_w_hall_dead_end_4,
        TempleLocationNames.t2_w_hall_dead_end_5,
        TempleLocationNames.t2_n_of_sw_gate_1,
        TempleLocationNames.t2_n_of_sw_gate_2,
        TempleLocationNames.t2_fire_trap_maze_1,
        TempleLocationNames.t2_fire_trap_maze_2,
        TempleLocationNames.t2_fire_trap_maze_3,
        TempleLocationNames.t2_fire_trap_maze_4,
        TempleLocationNames.t2_fire_trap_maze_5,
        TempleLocationNames.t2_fire_trap_maze_6,
        TempleLocationNames.t2_teleporter,
        TempleLocationNames.t2_e_outside_gold_beetle_cage_1,
        TempleLocationNames.t2_e_outside_gold_beetle_cage_2,
        TempleLocationNames.t2_boulder_chamber_1,
        TempleLocationNames.t2_boulder_chamber_2,
        TempleLocationNames.t2_boulder_chamber_3,
        TempleLocationNames.t2_boulder_chamber_4,
        TempleLocationNames.t2_s_balcony_1,
        TempleLocationNames.t2_s_balcony_2,
        TempleLocationNames.t2_se_banner_chamber_1,
        TempleLocationNames.t2_se_banner_chamber_2,
        TempleLocationNames.t2_se_banner_chamber_3,
        TempleLocationNames.t2_se_banner_chamber_4,
        TempleLocationNames.t2_se_banner_chamber_5,
        TempleLocationNames.t2_se_fireball_hall,
        TempleLocationNames.btn_t2_rune_e,
        TempleLocationNames.btn_t2_rune_se,
        TempleLocationNames.t2_miniboss_mummy_e,
        TempleLocationNames.t2_miniboss_mummy_w,
        TempleLocationNames.t2_tower_fire,
        TempleLocationNames.t2_tower_ice_3,
        TempleLocationNames.t2_tower_mana_1,
        TempleLocationNames.t2_tower_mana_2,
    ]
    t2_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_main, t2_main_locations)

    t2_nw_puzzle_locs = [
        TempleLocationNames.t2_nw_puzzle_1,
        TempleLocationNames.t2_nw_puzzle_2,
        TempleLocationNames.t2_nw_puzzle_3,
        TempleLocationNames.t2_nw_puzzle_4,
    ]
    t2_nw_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_nw_puzzle,
                                        t2_nw_puzzle_locs)

    t2_e_puzzle_locs = [
        TempleLocationNames.t2_e_puzzle_1,
        TempleLocationNames.t2_e_puzzle_2,
        TempleLocationNames.t2_e_puzzle_3,
        TempleLocationNames.t2_e_puzzle_4,
    ]
    t2_e_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_e_puzzle,
                                       t2_e_puzzle_locs)

    t2_melt_ice_locations = [
    ]
    t2_melt_ice_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_melt_ice,
                                       t2_melt_ice_locations)

    t2_w_ice_gate_locs = [
        TempleLocationNames.t2_w_ice_block_gate,
    ]
    t2_w_ice_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_w_ice_gate,
                                         t2_w_ice_gate_locs)

    t2_e_ice_gate_locs = [
        TempleLocationNames.t2_e_ice_block_gate,
    ]
    t2_e_ice_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_e_ice_gate,
                                         t2_e_ice_gate_locs)

    t2_n_gate_locations = [
        TempleLocationNames.t2_nw_ice_turret_1,
        TempleLocationNames.t2_nw_ice_turret_2,
        TempleLocationNames.t2_nw_ice_turret_3,
        TempleLocationNames.t2_nw_ice_turret_4,
        TempleLocationNames.t2_nw_under_block,
        TempleLocationNames.t2_nw_gate_3,
        TempleLocationNames.t2_tower_ice_1,
        TempleLocationNames.t2_tower_ice_2,
    ]
    t2_n_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_n_gate,
                                     t2_n_gate_locations)

    t2_n_puzzle_locs = [
        TempleLocationNames.t2_n_puzzle_1,
        TempleLocationNames.t2_n_puzzle_2,
        TempleLocationNames.t2_n_puzzle_3,
        TempleLocationNames.t2_n_puzzle_4,
    ]
    t2_n_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_n_puzzle,
                                       t2_n_puzzle_locs)

    t2_nw_button_gate_locs = [
        TempleLocationNames.t2_nw_gate_1,
        TempleLocationNames.t2_nw_gate_2,
    ]
    t2_nw_button_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_nw_button_gate,
                                             t2_nw_button_gate_locs)

    t2_s_gate_locations = [
        TempleLocationNames.t2_s_node_room_1,
        TempleLocationNames.t2_s_node_room_2,
        TempleLocationNames.t2_s_node_room_3,
        TempleLocationNames.t2_s_sunbeam_1,
        TempleLocationNames.t2_s_sunbeam_2,
        TempleLocationNames.t2_sw_jail_1,
        TempleLocationNames.t2_sw_jail_2,
        TempleLocationNames.btn_t2_rune_sw,
        TempleLocationNames.ev_temple2_pof_switch,
        TempleLocationNames.t2_tower_mana_3,
        TempleLocationNames.btn_t2_floor_blue,
    ]
    t2_s_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_s_gate,
                                     t2_s_gate_locations)

    t2_sw_puzzle_locs = [
        TempleLocationNames.t2_sw_puzzle_1,
        TempleLocationNames.t2_sw_puzzle_2,
        TempleLocationNames.t2_sw_puzzle_3,
        TempleLocationNames.t2_sw_puzzle_4,
    ]
    t2_sw_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_sw_puzzle,
                                        t2_sw_puzzle_locs)

    t2_n_node_locations = [
        TempleLocationNames.ev_t2_n_node,
    ]
    t2_n_node_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_n_node,
                                     t2_n_node_locations)

    t2_boulder_room_locs = [
        TempleLocationNames.t2_boulder_room_1,
        TempleLocationNames.t2_boulder_room_2,
        TempleLocationNames.t2_boulder_room_block,
        TempleLocationNames.btn_t2_rune_w
    ]
    t2_boulder_room_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_boulder_room,
                                           t2_boulder_room_locs)

    t2_n_hidden_hall_locs = [
        TempleLocationNames.t2_mana_drain_fire_trap_1,
        TempleLocationNames.t2_mana_drain_fire_trap_2,
    ]
    t2_n_hidden_hall_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_n_hidden_hall,
                                            t2_n_hidden_hall_locs)

    t2_jones_hall_locs = [
        TempleLocationNames.t2_jones_hallway,
    ]
    t2_jones_hall_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_jones_hall,
                                         t2_jones_hall_locs)

    t2_s_node_locations = [
        TempleLocationNames.ev_t2_s_node
    ]
    t2_s_node_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_s_node,
                                     t2_s_node_locations)

    t2_jail_sw_locs = [
        TempleLocationNames.t2_gold_beetle_barricade,
        TempleLocationNames.t2_w_gold_beetle_room_1,
        TempleLocationNames.t2_w_gold_beetle_room_2,
        TempleLocationNames.t2_w_gold_beetle_room_3,
        TempleLocationNames.t2_w_gold_beetle_room_4,
    ]
    t2_jail_sw_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_jail_sw,
                                      t2_jail_sw_locs)

    t2_sdoor_gate_locs = [
        TempleLocationNames.t2_sw_gate,
    ]
    t2_sdoor_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_sdoor_gate,
                                         t2_sdoor_gate_locs)

    t2_pof_locs = [
        TempleLocationNames.t2_left_of_pof_switch_1,
        TempleLocationNames.t2_left_of_pof_switch_2,
    ]
    t2_pof_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_pof, t2_pof_locs)

    t2_pof_spikes_locs = [
        TempleLocationNames.t2_right_of_pof_switch
    ]
    t2_pof_spikes_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_pof_spikes,
                                         t2_pof_spikes_locs)

    t2_jail_s_locs = [
    ]
    t2_jail_s_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_jail_s, t2_jail_s_locs)

    t2_ornate_locations = [
        TempleLocationNames.btn_t2_rune_n
    ]
    t2_ornate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_ornate,
                                     t2_ornate_locations)

    t2_light_bridge_w_locations = [
    ]
    t2_light_bridge_w_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_light_bridge_w,
                                             t2_light_bridge_w_locations)

    t2_light_bridges_se_locations = [
        TempleLocationNames.t2_se_light_bridge_1,
        TempleLocationNames.t2_se_light_bridge_2,
    ]
    t2_light_bridges_se_region = create_region(multiworld, player, active_locations,
                                               TempleRegionNames.t2_light_bridges_se, t2_light_bridges_se_locations)

    t2_light_bridges_s_locations = [
        TempleLocationNames.t2_s_light_bridge_1,
        TempleLocationNames.t2_s_light_bridge_2,
    ]
    t2_light_bridges_s_region = create_region(multiworld, player, active_locations,
                                              TempleRegionNames.t2_light_bridges_s, t2_light_bridges_s_locations)

    t2_portal_gate_locs = [
        TempleLocationNames.t2_portal_gate,
    ]
    t2_portal_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_portal_gate,
                                          t2_portal_gate_locs)

    t2_ornate_t3_locations = [
        TempleLocationNames.t2_floor3_cache_1,
        TempleLocationNames.t2_floor3_cache_2,
        TempleLocationNames.t2_floor3_cache_3,
        TempleLocationNames.t2_floor3_cache_4,
        TempleLocationNames.t2_floor3_cache_5,
        TempleLocationNames.t2_floor3_cache_6,
    ]
    t2_ornate_t3_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_ornate_t3,
                                        t2_ornate_t3_locations)

    t2_ornate_gate_locs = [
        TempleLocationNames.t2_floor3_cache_gate,
    ]
    t2_ornate_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_ornate_gate,
                                          t2_ornate_gate_locs)

    # Dynamically place portal event location
    t2_portal_loc = HammerwatchLocation(player, TempleLocationNames.ev_t2_portal)
    if random_locations[TempleLocationNames.rloc_t2_portal] == 0:
        t2_main_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_main_region
    elif random_locations[TempleLocationNames.rloc_t2_portal] == 1:
        t2_s_gate_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_s_gate_region
    elif random_locations[TempleLocationNames.rloc_t2_portal] == 2:
        t2_main_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_main_region
    else:
        t2_n_gate_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_n_gate_region

    t3_main_locations = [
        TempleLocationNames.t3_s_balcony_turret_1,
        TempleLocationNames.t3_s_balcony_turret_2,
        TempleLocationNames.t3_n_turret_1,
        TempleLocationNames.t3_n_turret_2,
        TempleLocationNames.t3_boulder_block,
        TempleLocationNames.t3_e_turret_spikes,
        TempleLocationNames.t3_tower_fire_1,
        TempleLocationNames.t3_tower_fire_2,
        TempleLocationNames.t3_tower_ice_1,
        TempleLocationNames.t3_tower_mana_1,
        TempleLocationNames.t3_tower_mana_2,
        TempleLocationNames.ev_t3_portal,
    ]
    t3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_main, t3_main_locations)

    t3_blockade_s_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_blockade_s, [])

    t3_s_gate_locs = [
        TempleLocationNames.t3_s_gate,
    ]
    t3_s_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_s_gate, t3_s_gate_locs)

    t3_n_node_blocks_locations = [
        TempleLocationNames.t3_n_node_blocks_1,
        TempleLocationNames.t3_n_node_blocks_2,
        TempleLocationNames.t3_n_node_blocks_3,
        TempleLocationNames.t3_n_node_blocks_4,
        TempleLocationNames.t3_n_node_blocks_5,
    ]
    t3_n_node_blocks_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_n_node_blocks,
                                            t3_n_node_blocks_locations)

    t3_gates_locs = [
        TempleLocationNames.t3_tower_ice_2,
        TempleLocationNames.t3_tower_ice_3,
    ]
    t3_gates_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_gates, t3_gates_locs)

    t3_puzzle_locs = [
        TempleLocationNames.t3_puzzle_1,
        TempleLocationNames.t3_puzzle_2,
        TempleLocationNames.t3_puzzle_3,
        TempleLocationNames.t3_puzzle_4,
    ]
    t3_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_puzzle, t3_puzzle_locs)

    t3_n_node_locations = [
        TempleLocationNames.ev_t3_n_node
    ]
    t3_n_node_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_n_node,
                                     t3_n_node_locations)

    t3_s_node_blocks_1_locations = [
        TempleLocationNames.t3_s_node_cache_1,
        TempleLocationNames.t3_s_node_cache_2,
        TempleLocationNames.t3_s_node_cache_3,
    ]
    t3_s_node_blocks_1_region = create_region(multiworld, player, active_locations,
                                              TempleRegionNames.t3_s_node_blocks_1,
                                              t3_s_node_blocks_1_locations)

    t3_s_node_blocks_2_locations = [
        TempleLocationNames.t3_m_balcony_corridor,
    ]
    t3_s_node_blocks_2_region = create_region(multiworld, player, active_locations,
                                              TempleRegionNames.t3_s_node_blocks_2,
                                              t3_s_node_blocks_2_locations)

    t3_s_node_locations = [
        TempleLocationNames.t3_n_node_1,
        TempleLocationNames.t3_n_node_2,
        TempleLocationNames.t3_n_node_3,
        TempleLocationNames.ev_t3_s_node,
    ]
    t3_s_node_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_s_node,
                                     t3_s_node_locations)

    t3_boss_fall_1_locations = [
        TempleLocationNames.t3_boss_fall_1_1,
        TempleLocationNames.t3_boss_fall_1_2,
        TempleLocationNames.t3_boss_fall_1_3,
    ]
    t3_boss_fall_1_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_boss_fall_1,
                                          t3_boss_fall_1_locations)

    t3_boss_fall_2_locations = [
        TempleLocationNames.t3_boss_fall_2_1,
        TempleLocationNames.t3_boss_fall_2_2,
        TempleLocationNames.t3_boss_fall_2_3,
    ]
    t3_boss_fall_2_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_boss_fall_2,
                                          t3_boss_fall_2_locations)

    t3_boss_fall_3_locations = [
        TempleLocationNames.t3_boss_fall_3_1,
        TempleLocationNames.t3_boss_fall_3_2,
        TempleLocationNames.t3_boss_fall_3_3,
        TempleLocationNames.t3_boss_fall_3_4,
    ]
    t3_boss_fall_3_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_boss_fall_3,
                                          t3_boss_fall_3_locations)

    pof_1_main_locations = [
        TempleLocationNames.pof_1_ent_1,
        TempleLocationNames.pof_1_ent_2,
        TempleLocationNames.pof_1_ent_3,
        TempleLocationNames.pof_1_ent_4,
        TempleLocationNames.pof_1_ent_5,
        TempleLocationNames.pof_1_sw_left_1,
        TempleLocationNames.pof_1_sw_left_2,
        TempleLocationNames.pof_1_sw_left_3,
        TempleLocationNames.pof_1_sw_left_4,
        TempleLocationNames.pof_1_sw_left_5,
        TempleLocationNames.pof_1_sw_left_6,
        TempleLocationNames.pof_1_sw_left_7,
        TempleLocationNames.pof_1_sw_left_8,
        TempleLocationNames.pof_1_sw_left_9,
        TempleLocationNames.pof_1_sw_left_10,
        TempleLocationNames.pof_1_sw_left_11,
    ]
    pof_1_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_main,
                                      pof_1_main_locations)

    pof_1_se_room_locations = [
        TempleLocationNames.ev_pof_1_se_room_panel,
    ]
    pof_1_se_room_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_se_room,
                                         pof_1_se_room_locations)

    pof_1_se_room_top_locs = [
        TempleLocationNames.pof_1_s_1,
        TempleLocationNames.pof_1_s_2,
        TempleLocationNames.pof_1_s_3,
        TempleLocationNames.pof_1_s_4,
        TempleLocationNames.pof_1_s_5,
        TempleLocationNames.pof_1_s_6,
        TempleLocationNames.pof_1_s_7,
        TempleLocationNames.pof_1_s_8,
        TempleLocationNames.pof_1_s_9,
        TempleLocationNames.pof_1_s_10,
        TempleLocationNames.pof_1_s_11,
        TempleLocationNames.pof_1_s_12,
        TempleLocationNames.pof_1_s_13,
    ]
    pof_1_se_room_top_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_se_room_top,
                                             pof_1_se_room_top_locs)

    pof_1_sw_gate_locs = [
    ]
    pof_1_sw_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_sw_gate,
                                         pof_1_sw_gate_locs)

    pof_1_nw_locs = [
        TempleLocationNames.pof_1_confuse_corner_1,
        TempleLocationNames.pof_1_confuse_corner_2,
        TempleLocationNames.pof_1_confuse_corner_3,
        TempleLocationNames.pof_1_confuse_corner_4,
    ]
    pof_1_nw_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_nw, pof_1_nw_locs)

    pof_1_n_room_locations = [
        TempleLocationNames.pof_1_n_1,
        TempleLocationNames.pof_1_n_2,
        TempleLocationNames.pof_1_n_3,
        TempleLocationNames.pof_1_n_4,
        TempleLocationNames.pof_1_n_5,
        TempleLocationNames.pof_1_n_6,
        TempleLocationNames.pof_1_n_7,
        TempleLocationNames.pof_1_n_8,
        TempleLocationNames.pof_1_n_9,
        TempleLocationNames.ev_pof_1_unlock_exit
    ]
    pof_1_n_room_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_n_room,
                                        pof_1_n_room_locations)

    pof_1_exit_hall_locs = [
        TempleLocationNames.pof_1_c_hall_1,
        TempleLocationNames.pof_1_c_hall_2,
        TempleLocationNames.pof_1_c_hall_3,
        TempleLocationNames.pof_1_c_hall_4,
        TempleLocationNames.pof_1_c_hall_5,
        TempleLocationNames.pof_1_c_hall_6,
    ]
    pof_1_exit_hall_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_exit_hall,
                                           pof_1_exit_hall_locs)

    pof_1_gate_2_locations = [
        TempleLocationNames.pof_1_end_1,
        TempleLocationNames.pof_1_end_2,
        TempleLocationNames.pof_1_end_3,
        TempleLocationNames.pof_1_end_4,
        TempleLocationNames.pof_1_end_5,
    ]
    pof_1_gate_2_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_gate_2,
                                        pof_1_gate_2_locations)

    pof_2_main_locations = [
        TempleLocationNames.pof_2_ent_1,
        TempleLocationNames.pof_2_ent_2,
        TempleLocationNames.pof_2_ent_3,
        TempleLocationNames.pof_2_ent_4,
        TempleLocationNames.pof_2_ent_5,
        TempleLocationNames.pof_2_ent_6,
        TempleLocationNames.pof_2_confuse_hall_1,
        TempleLocationNames.pof_2_confuse_hall_2,
        TempleLocationNames.pof_2_confuse_hall_3,
        TempleLocationNames.pof_2_confuse_hall_4,
        TempleLocationNames.pof_2_sw_1,
        TempleLocationNames.pof_2_sw_2,
        TempleLocationNames.pof_2_sw_3,
        TempleLocationNames.pof_2_sw_4,
    ]
    pof_2_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_2_main,
                                      pof_2_main_locations)

    pof_2_n_locations = [
        TempleLocationNames.pof_2_ne_1,
        TempleLocationNames.pof_2_ne_2,
        TempleLocationNames.pof_2_ne_3,
        TempleLocationNames.pof_2_ne_4,
    ]
    pof_2_n_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_2_n, pof_2_n_locations)

    pof_2_puzzle_locs = [
        TempleLocationNames.ev_pof_2_unlock_exit
    ]
    pof_2_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_2_puzzle,
                                        pof_2_puzzle_locs)

    pof_puzzle_locs = [
        TempleLocationNames.pof_puzzle_1,
        TempleLocationNames.pof_puzzle_2,
        TempleLocationNames.pof_puzzle_3,
        TempleLocationNames.pof_puzzle_4,
    ]
    pof_puzzle_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_puzzle,
                                      pof_puzzle_locs)

    pof_2_exit_locations = [
    ]
    pof_2_exit_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_2_exit,
                                      pof_2_exit_locations)

    pof_3_start_locs = [
        TempleLocationNames.pof_3_safety_room_1,
        TempleLocationNames.pof_3_safety_room_2,
        TempleLocationNames.pof_3_safety_room_3,
    ]
    pof_3_start_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_3_start,
                                       pof_3_start_locs)

    pof_3_main_locations = [
        TempleLocationNames.pof_3_end_1,
        TempleLocationNames.pof_3_end_2,
        TempleLocationNames.pof_3_end_3,
        TempleLocationNames.pof_3_end_4,
        TempleLocationNames.pof_3_end_5,
        TempleLocationNames.ev_pof_end
    ]
    if get_goal_type(multiworld, player) == GoalType.AltCompletion:
        pof_3_main_locations.append(TempleLocationNames.ev_victory)
    pof_3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_3_main,
                                      pof_3_main_locations)

    b3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_main, [])
    b3_platform_1_locs = [
        TempleLocationNames.b3_tower_fire_2,
    ]
    b3_platform_1_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_platform_1,
                                         b3_platform_1_locs)
    b3_platform_2_locs = [
        TempleLocationNames.b3_tower_fire_1,
    ]
    b3_platform_2_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_platform_2,
                                         b3_platform_2_locs)
    b3_platform_3_locs = [
        TempleLocationNames.b3_tower_fire_3,
    ]
    b3_platform_3_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_platform_3,
                                         b3_platform_3_locs)

    b3_defeated_locations = [
        TempleLocationNames.ev_beat_boss_3,
    ]
    if get_goal_type(multiworld, player) == GoalType.KillBosses:
        b3_defeated_locations.append(TempleLocationNames.ev_victory)
    b3_defeated_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_defeated,
                                       b3_defeated_locations)

    multiworld.regions += [
        menu_region,
        dunes_main_region,
        dunes_rocks_region,
        dunes_pyramid_region,
        library_region,
        library_lobby_region,
        cave3_main_region,
        c3_puzzle_region,
        c3_e_region,
        cave3_fall_region,
        cave3_fields_region,
        c3_e_water_region,
        cave3_portal_region,
        cave3_secret_region,
        cave2_main_region,
        cave2_red_bridge_region,
        cave2_green_bridge_region,
        c2_double_bridge_region,
        c2_sw_region,
        c2_puzzle_region,
        cave2_pumps_region,
        cave1_main_region,
        c1_n_puzzle_region,
        cave1_blue_bridge_region,
        c1_secret_hall_region,
        cave1_red_bridge_region,
        c1_e_puzzle_region,
        cave1_green_bridge_region,
        c1_storage_island_region,
        cave1_pumps_region,
        cave1_temple_region,
        boss1_entrance_region,
        boss1_arena_region,
        b1_back_region,
        boss1_defeated_region,
        passage_entrance_region,
        passage_mid_region,
        passage_puzzle_region,
        passage_end_region,
        temple_entrance_region,
        temple_entrance_back_region,
        t1_main_region,
        t1_w_puzzle_region,
        t1_sw_cache_region,
        t1_w_region,
        t1_node_1_region,
        t1_node_2_region,
        t1_sun_turret_region,
        t1_ice_turret_region,
        t1_telarian_region,
        t1_n_of_ice_turret_region,
        t1_s_of_ice_turret_region,
        t1_east_region,
        t1_e_puzzle_region,
        t1_jail_e_region,
        t1_sun_block_hall_region,
        t1_telarian_melt_ice_region,
        t1_ice_chamber_melt_ice_region,
        boss2_main_region,
        boss2_defeated_region,
        t2_main_region,
        t2_nw_puzzle_region,
        t2_e_puzzle_region,
        t2_melt_ice_region,
        t2_w_ice_gate_region,
        t2_e_ice_gate_region,
        t2_n_gate_region,
        t2_n_puzzle_region,
        t2_nw_button_gate_region,
        t2_s_gate_region,
        t2_sw_puzzle_region,
        t2_n_node_region,
        t2_boulder_room_region,
        t2_n_hidden_hall_region,
        t2_jones_hall_region,
        t2_s_node_region,
        t2_jail_sw_region,
        t2_sdoor_gate_region,
        t2_pof_region,
        t2_pof_spikes_region,
        t2_jail_s_region,
        t2_ornate_region,
        t2_light_bridge_w_region,
        t2_light_bridges_se_region,
        t2_light_bridges_s_region,
        t2_portal_gate_region,
        t2_ornate_t3_region,
        t2_ornate_gate_region,
        t3_main_region,
        t3_blockade_s_region,
        t3_s_gate_region,
        t3_n_node_blocks_region,
        t3_gates_region,
        t3_puzzle_region,
        t3_n_node_region,
        t3_s_node_blocks_1_region,
        t3_s_node_blocks_2_region,
        t3_s_node_region,
        t3_boss_fall_1_region,
        t3_boss_fall_2_region,
        t3_boss_fall_3_region,
        pof_1_main_region,
        pof_1_se_room_region,
        pof_1_se_room_top_region,
        pof_1_sw_gate_region,
        pof_1_nw_region,
        pof_1_n_room_region,
        pof_1_exit_hall_region,
        pof_1_gate_2_region,
        pof_2_main_region,
        pof_2_n_region,
        pof_2_puzzle_region,
        pof_puzzle_region,
        pof_2_exit_region,
        pof_3_start_region,
        pof_3_main_region,
        b3_main_region,
        b3_platform_1_region,
        b3_platform_2_region,
        b3_platform_3_region,
        b3_defeated_region,
        get_planks_region
    ]


def connect_tots_regions(multiworld, player: int, random_locations: typing.Dict[str, int],
                         gate_codes: typing.Dict[str, str]):
    used_names: typing.Dict[str, int] = {}

    gate_counts: typing.Dict[str, int] = {
        ItemName.key_silver: 6,
        ItemName.key_gold: 4,
    }

    pan_item = ItemName.pan
    lever_item = ItemName.lever
    pickaxe_item = ItemName.pickaxe
    pan_item_count = multiworld.pan_fragments[player]
    lever_item_count = multiworld.lever_fragments[player]
    pickaxe_item_count = multiworld.pickaxe_fragments[player]
    if pan_item_count > 1:
        pan_item = ItemName.pan_fragment
    if lever_item_count > 1:
        lever_item = ItemName.lever_fragment
    if pickaxe_item_count > 1:
        pickaxe_item = ItemName.pickaxe_fragment

    connect(multiworld, player, used_names, TempleRegionNames.menu, TempleRegionNames.hub_main, False)

    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.hub_rocks,
            True, pickaxe_item, pickaxe_item_count, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.hub_rocks, TempleRegionNames.cave_3_fall,
                 EntranceNames.t_c1_fall_surface, None)
    # For the temple entrances in the hub
    t3_entrance = TempleRegionNames.t3_main
    if random_locations[TempleLocationNames.rloc_t3_entrance] == 2:
        t3_entrance = TempleRegionNames.t3_blockade_s
    t3_entrance_code = f"t3|{random_locations[TempleLocationNames.rloc_t3_entrance]}"
    connect_exit(multiworld, player, used_names, TempleRegionNames.hub_rocks, t3_entrance,
                 t3_entrance_code, EntranceNames.t_hub_t3)  # , ItemName.key_teleport, 1, True)
    connect_exit(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.temple_entrance,
                 EntranceNames.t_t_ent_hub, EntranceNames.t_hub_t_ent)
    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.hub_pyramid_of_fear,
            False, ItemName.ev_pof_complete, 1, False)

    connect_exit(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.library_lobby,
                 EntranceNames.t_lib_start, EntranceNames.t_hub_library)
    connect_exit(multiworld, player, used_names, TempleRegionNames.library_lobby, TempleRegionNames.library,
                 EntranceNames.t_lib_books, EntranceNames.t_lib_lobby_end)
    connect_exit(multiworld, player, used_names, TempleRegionNames.library, TempleRegionNames.cave_3_main,
                 EntranceNames.t_c1_start, EntranceNames.t_lib_end)
    connect(multiworld, player, used_names, TempleRegionNames.cave_3_main, TempleRegionNames.cave_3_fields,
            False, lever_item, lever_item_count, False)
    connect(multiworld, player, used_names, TempleRegionNames.c3_e, TempleRegionNames.c3_e_water,
            False, lever_item, lever_item_count, False)

    connect(multiworld, player, used_names, TempleRegionNames.cave_3_main, TempleRegionNames.c3_puzzle, False)
    connect(multiworld, player, used_names, TempleRegionNames.cave_3_main, TempleRegionNames.c3_e, True)
    connect(multiworld, player, used_names, TempleRegionNames.cave_3_fall, TempleRegionNames.cave_3_main, False)
    connect(multiworld, player, used_names, TempleRegionNames.cave_3_secret, TempleRegionNames.cave_3_main, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.c3_e, TempleRegionNames.cave_2_main,
                 EntranceNames.t_c2_start, EntranceNames.t_c1_end)  # , ItemName.key_teleport, 1, True)

    connect(multiworld, player, used_names, TempleRegionNames.cave_2_main, TempleRegionNames.cave_2_pumps,
            False, lever_item, lever_item_count, False)
    connect(multiworld, player, used_names, TempleRegionNames.cave_2_main, TempleRegionNames.c2_red_bridge, False)
    # Requires red switch
    connect(multiworld, player, used_names, TempleRegionNames.cave_2_main, TempleRegionNames.c2_green_bridge, False)
    connect(multiworld, player, used_names, TempleRegionNames.cave_2_main, TempleRegionNames.c2_sw, True)
    # Both require green switch
    connect(multiworld, player, used_names, TempleRegionNames.c2_sw, TempleRegionNames.c2_puzzle, False)
    connect(multiworld, player, used_names, TempleRegionNames.c2_sw, TempleRegionNames.c2_double_bridge, False)
    # Two-way
    # connect_generic(multiworld, player, used_names, TempleRegionNames.c2_double_bridge, TempleRegionNames.cave_2_main)
    # Both require double bridge switch
    # connect(multiworld, player, used_names, TempleRegionNames.c2_sw, TempleRegionNames.cave_2_main, False)
    # Requires lower bridge switch
    connect_exit(multiworld, player, used_names, TempleRegionNames.c2_sw, TempleRegionNames.cave_1_main,
                 EntranceNames.t_c3_start, EntranceNames.t_c2_end)  # , ItemName.key_teleport, 1, True)

    connect(multiworld, player, used_names, TempleRegionNames.cave_1_main, TempleRegionNames.c1_n_puzzle, False)
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_main, TempleRegionNames.cave_1_blue_bridge, False)
    # Requires blue switch, two-way
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_blue_bridge, TempleRegionNames.cave_1_red_bridge,
            False)
    # Requires red switch, two-way
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_blue_bridge,
            TempleRegionNames.c1_secret_hall, False)
    # Requires wall switch
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_main, TempleRegionNames.cave_1_pumps,
            True, lever_item, lever_item_count, False)
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_pumps, TempleRegionNames.cave_1_green_bridge,
            False)
    # Symbolic connection, requires green switch which is underwater
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_pumps, TempleRegionNames.c1_storage_island, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.c1_storage_island, TempleRegionNames.boss2_main,
                 EntranceNames.t_b2, EntranceNames.t_c3_boss)
    # Technically a level exit, but we need to be able to go to the defeated room from anywhere rip
    connect(multiworld, player, used_names, TempleRegionNames.boss2_main, TempleRegionNames.boss2_defeated,
            False)

    connect(multiworld, player, used_names, TempleRegionNames.cave_1_red_bridge, TempleRegionNames.c1_e_puzzle, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.cave_1_red_bridge,
                 TempleRegionNames.boss_1_entrance, EntranceNames.t_b1_start, EntranceNames.t_c3_end)  # ,
                 # ItemName.key_teleport, 1, True)

    connect(multiworld, player, used_names, TempleRegionNames.boss_1_entrance, TempleRegionNames.boss_1_arena,
            True)  # We shouldn't include boss teleporters in ER, it's kinda mean lol
    connect(multiworld, player, used_names, TempleRegionNames.boss_1_arena, TempleRegionNames.boss_1_defeated, False)
    connect_gate(multiworld, player, used_names, TempleRegionNames.boss_1_arena, TempleRegionNames.b1_back,
                 ItemName.key_gold, gate_codes, gate_counts, GateNames.t_b1_0, True)
    # connect_generic(multiworld, player, used_names, TempleRegionNames.b1_back, TempleRegionNames.boss_1_entrance)
    # Requires boss 1 bridge switch

    passage_entrance = EntranceNames.t_p_ent_start if random_locations[TempleLocationNames.rloc_passage_entrance] == 0\
        else EntranceNames.t_p_ent_start_2
    connect_exit(multiworld, player, used_names, TempleRegionNames.b1_back, TempleRegionNames.passage_entrance,
                 passage_entrance, EntranceNames.t_b1_end)
    passage_mid = f"passage|{random_locations[TempleLocationNames.rloc_passage_middle] + 1}0"
    connect_exit(multiworld, player, used_names, TempleRegionNames.passage_entrance, TempleRegionNames.passage_mid,
                 passage_mid, EntranceNames.t_p_ent_exit)
    connect(multiworld, player, used_names, TempleRegionNames.passage_mid, TempleRegionNames.passage_puzzle, False)
    passage_end = f"passage|1{random_locations[TempleLocationNames.rloc_passage_end] + 1}0"
    connect_exit(multiworld, player, used_names, TempleRegionNames.passage_mid, TempleRegionNames.passage_end,
                 passage_end, f"passage|{random_locations[TempleLocationNames.rloc_passage_middle] + 1}1")

    connect_exit(multiworld, player, used_names, TempleRegionNames.passage_end, TempleRegionNames.temple_entrance_back,
                 EntranceNames.t_t_ent_p, EntranceNames.t_p_end_end)
    connect(multiworld, player, used_names, TempleRegionNames.temple_entrance_back, TempleRegionNames.temple_entrance,
            False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.temple_entrance_back, TempleRegionNames.t1_main,
                 EntranceNames.t_t1_start, EntranceNames.t_t_ent_temple)

    connect(multiworld, player, used_names, TempleRegionNames.t1_main, TempleRegionNames.t1_w_puzzle, False)
    connect_gate(multiworld, player, used_names, TempleRegionNames.t1_main, TempleRegionNames.t1_sw_sdoor,
                 ItemName.key_silver, gate_codes, gate_counts, GateNames.t_t1_3, False)
    connect(multiworld, player, used_names, TempleRegionNames.t1_main, TempleRegionNames.t1_node_1,
            False, ItemName.mirror, 3)
    connect(multiworld, player, used_names, TempleRegionNames.t1_node_1, TempleRegionNames.t1_w, False)
    connect(multiworld, player, used_names, TempleRegionNames.t1_w, TempleRegionNames.t1_main, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.t1_w, TempleRegionNames.cave_3_secret,
                 EntranceNames.t_c1_fall_temple, None)
    connect_gate(multiworld, player, used_names, TempleRegionNames.t1_w, TempleRegionNames.t1_sun_turret,
                 ItemName.key_silver, gate_codes, gate_counts, GateNames.t_t1_1, False)
    connect_gate(multiworld, player, used_names, TempleRegionNames.t1_w, TempleRegionNames.t1_ice_turret,
                 ItemName.key_gold, gate_codes, gate_counts, GateNames.t_t1_4, True)
    connect(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_telarian, False)
    # Requires telarian button
    connect(multiworld, player, used_names, TempleRegionNames.t1_ice_turret,
            TempleRegionNames.t1_telarian_melt_ice, False, ItemName.evt_beat_boss_2, 1, False)
    connect_gate(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_n_of_ice_turret,
                 ItemName.key_silver, gate_codes, gate_counts, GateNames.t_t1_0, False)
    connect_gate(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_s_of_ice_turret,
                 ItemName.key_silver, gate_codes, gate_counts, GateNames.t_t1_2, False)
    connect_gate(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_east,
                 ItemName.key_gold, gate_codes, gate_counts, GateNames.t_t1_5, True)
    connect(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_sun_block_hall,
            False, ItemName.mirror, 3)
    connect(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t1_node_2,
            False, ItemName.mirror, 1)  # For future reference both these have extra stuff set in Rules.py
    connect(multiworld, player, used_names, TempleRegionNames.t1_east,
            TempleRegionNames.t1_ice_chamber_melt_ice, False, ItemName.evt_beat_boss_2, 1, False)
    connect(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t1_jail_e, False)
    # Requires east jail button
    connect(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t1_e_puzzle, False)

    connect_exit(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t2_main,
                 f"t2|{random_locations[TempleLocationNames.rloc_t2_entrance]}", EntranceNames.t_t1_end)  # ,
                 # ItemName.key_teleport, 1, True)
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_nw_puzzle,
            False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_e_puzzle,
            False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_melt_ice,
            True, ItemName.evt_beat_boss_2, 1, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_melt_ice, TempleRegionNames.t2_w_ice_gate, False)
    # Requires west ice gate button
    connect(multiworld, player, used_names, TempleRegionNames.t2_melt_ice, TempleRegionNames.t2_e_ice_gate, False)
    # Requires east ice gate button
    connect_gate(multiworld, player, used_names, TempleRegionNames.t2_melt_ice, TempleRegionNames.t2_n_gate,
                 ItemName.key_silver, gate_codes, gate_counts, GateNames.t_t2_0, False)
    connect_gate(multiworld, player, used_names, TempleRegionNames.t2_melt_ice, TempleRegionNames.t2_s_gate,
                 ItemName.key_silver, gate_codes, gate_counts, GateNames.t_t2_1, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_s_gate, TempleRegionNames.t2_sdoor_gate, False)
    # Requires south door gate button
    connect_gate(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_ornate,
                 ItemName.key_gold, gate_codes, gate_counts, GateNames.t_t2_2, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_ornate, TempleRegionNames.t2_ornate_gate, False)
    # Requires east ornate wall button. Note we make this one-way because you have to access the other side to cross
    connect(multiworld, player, used_names, TempleRegionNames.t2_ornate_t3, TempleRegionNames.t2_ornate_gate, False)
    # Requires west ornate wall button. Note we make this one-way because you have to access the other side to cross
    connect(multiworld, player, used_names, TempleRegionNames.t2_n_gate, TempleRegionNames.t2_n_puzzle, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_n_gate, TempleRegionNames.t2_n_node,
            False, ItemName.mirror, 3)
    connect(multiworld, player, used_names, TempleRegionNames.t2_n_gate, TempleRegionNames.t2_nw_button_gate, False)
    # Requires nw gate button
    connect(multiworld, player, used_names, TempleRegionNames.t2_n_node, TempleRegionNames.t2_boulder_room, False)
    # From north gate, requires north node button
    connect(multiworld, player, used_names, TempleRegionNames.t2_boulder_room, TempleRegionNames.t2_jail_sw,
            False, ItemName.btn_t2_blue_spikes, 1, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_boulder_room, TempleRegionNames.t2_n_hidden_hall,
            False)
    # Requires hidden hall button
    connect(multiworld, player, used_names, TempleRegionNames.t2_n_hidden_hall, TempleRegionNames.t2_jones_hall, False)
    # Requires jones hall button
    connect(multiworld, player, used_names, TempleRegionNames.t2_s_gate, TempleRegionNames.t2_sw_puzzle, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_s_gate, TempleRegionNames.t2_s_node,
            False,  ItemName.mirror, 4)
    connect(multiworld, player, used_names, TempleRegionNames.t2_s_node, TempleRegionNames.t2_pof, False)
    # Technically you only need 3 mirrors to get here, but this is safer logic
    connect(multiworld, player, used_names, TempleRegionNames.t2_pof, TempleRegionNames.t2_jail_s, False)
    # Requires pof wall button
    connect(multiworld, player, used_names, TempleRegionNames.t2_jail_s, TempleRegionNames.t2_pof_spikes, False)
    # Requires pof south jail wall button
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_light_bridges_se,
            False, ItemName.ev_t2_rune_switch, 5, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_light_bridges_s,
            False, ItemName.ev_t2_rune_switch, 5, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_light_bridge_w,
            False, ItemName.ev_t2_rune_switch, 5, False)
    connect(multiworld, player, used_names, TempleRegionNames.t2_light_bridge_w, TempleRegionNames.t2_portal_gate, False)
    # Requires portal floor switch
    connect(multiworld, player, used_names, TempleRegionNames.t2_portal_gate, TempleRegionNames.t2_main, False)
    # Requires portal floor switch
    connect_exit(multiworld, player, used_names, TempleRegionNames.t2_light_bridge_w, TempleRegionNames.cave_3_portal,
                 EntranceNames.t_c1_portal, EntranceNames.t_t2_w_portal)
    connect_exit(multiworld, player, used_names, TempleRegionNames.t2_light_bridges_s, TempleRegionNames.cave_1_temple,
                 EntranceNames.t_c3_temple, EntranceNames.t_t2_s_light_bridge)

    connect(multiworld, player, used_names, TempleRegionNames.t3_blockade_s, TempleRegionNames.t3_s_gate, False)
    # Requires south gate button
    connect(multiworld, player, used_names, TempleRegionNames.t3_s_gate, TempleRegionNames.t3_main, False)
    # One-way because we need to hit the button first!
    connect_exit(multiworld, player, used_names, TempleRegionNames.t3_main, TempleRegionNames.t2_ornate_t3,
                 EntranceNames.t_t2_t3, EntranceNames.t_t3_t2)  # , ItemName.key_teleport, 1, True)
    connect(multiworld, player, used_names, TempleRegionNames.t3_main, TempleRegionNames.t3_main,
            False, ItemName.mirror, 2)
    # Wonky logic, we treat this like a dead end as players could waste their mirrors on this with no benefit
    connect(multiworld, player, used_names, TempleRegionNames.t3_s_node_blocks_2,
            TempleRegionNames.t3_n_node_blocks, False, ItemName.mirror, 1)
    # After wasting mirrors everywhere else only this one will turn on the beam to break the blockade
    connect(multiworld, player, used_names, TempleRegionNames.t3_n_node_blocks, TempleRegionNames.t3_blockade_s, False)
    connect(multiworld, player, used_names, TempleRegionNames.t3_n_node_blocks, TempleRegionNames.t3_gates, False)
    # Requires gates button
    connect(multiworld, player, used_names, TempleRegionNames.t3_gates, TempleRegionNames.t3_puzzle, False)
    connect(multiworld, player, used_names, TempleRegionNames.t3_n_node_blocks, TempleRegionNames.t3_n_node, False)
    connect(multiworld, player, used_names, TempleRegionNames.t3_main, TempleRegionNames.t3_s_node_blocks_1,
            False, ItemName.mirror, 2)
    connect(multiworld, player, used_names, TempleRegionNames.t3_main, TempleRegionNames.t3_s_node_blocks_2,
            False, ItemName.mirror, 1)
    # More wonky logic, I hope everything works out!
    connect(multiworld, player, used_names, TempleRegionNames.t3_s_node_blocks_2, TempleRegionNames.t3_s_node, False)

    connect_exit(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.pof_1_main,
                 EntranceNames.t_n1_1_start, EntranceNames.t_hub_pof, ItemName.ev_pof_switch, 6, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.pof_1_main, TempleRegionNames.pof_1_se_room,
                 EntranceNames.t_n1_1_se, EntranceNames.t_n1_1_sw)
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_se_room, TempleRegionNames.pof_1_se_room_top, False,
            ItemName.ev_pof_1_s_walls, 1, False)
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_main, TempleRegionNames.pof_1_sw_gate, False,
            ItemName.ev_pof_1_s_walls, 1, False)
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_sw_gate, TempleRegionNames.pof_1_nw,
            False, ItemName.key_bonus)
    connect_exit(multiworld, player, used_names, TempleRegionNames.pof_1_nw, TempleRegionNames.pof_1_n_room,
                 EntranceNames.t_n1_1_n, EntranceNames.t_n1_1_ne)
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_nw, TempleRegionNames.pof_1_exit_hall,
            True, ItemName.ev_pof_1_unlock_exit, 1, False)
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_exit_hall, TempleRegionNames.pof_1_gate_2,
            True, ItemName.key_bonus)
    connect_exit(multiworld, player, used_names, TempleRegionNames.pof_1_gate_2, TempleRegionNames.pof_2_main,
                 EntranceNames.t_n1_2_start, None)  # EntranceNames.t_n1_20)
    connect_exit(multiworld, player, used_names, TempleRegionNames.pof_2_main, TempleRegionNames.pof_2_n,
                 EntranceNames.t_n1_2_n, EntranceNames.t_n1_2_nw)
    connect(multiworld, player, used_names, TempleRegionNames.pof_2_n, TempleRegionNames.pof_2_puzzle, False)
    connect(multiworld, player, used_names, TempleRegionNames.pof_2_puzzle, TempleRegionNames.pof_puzzle, False)
    # Requires bonus panel
    connect(multiworld, player, used_names, TempleRegionNames.pof_2_main, TempleRegionNames.pof_2_exit,
            False, ItemName.ev_pof_2_unlock_exit, 1, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.pof_2_exit, TempleRegionNames.pof_3_start,
                 EntranceNames.t_n1_3_start, None)  # EntranceNames.t_n1_100)
    connect(multiworld, player, used_names, TempleRegionNames.pof_3_start, TempleRegionNames.pof_3_main, False)
    connect_exit(multiworld, player, used_names, TempleRegionNames.pof_3_main, TempleRegionNames.hub_main,
                 EntranceNames.t_hub_pof_return, None)

    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.b3_main,
            True, ItemName.ev_solar_node, 6, False)  # Ignoring for ER, kinda dumb
    connect(multiworld, player, used_names, TempleRegionNames.b3_main, TempleRegionNames.b3_platform_1, False)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_1, TempleRegionNames.b3_platform_2, False)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_2, TempleRegionNames.b3_platform_3, False)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_3, TempleRegionNames.b3_defeated, False)

    # These are also ignored 
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_1, TempleRegionNames.t3_boss_fall_1, False)
    # connect(multiworld, player, used_names, TempleRegionNames.t3_boss_fall_1, TempleRegionNames.t3_main, False)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_2, TempleRegionNames.t3_boss_fall_2, False)
    # connect(multiworld, player, used_names, TempleRegionNames.t3_boss_fall_2, TempleRegionNames.t3_main, False)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_3, TempleRegionNames.t3_boss_fall_3, False)
    # connect(multiworld, player, used_names, TempleRegionNames.t3_boss_fall_3, TempleRegionNames.t3_main, False)

    planks_to_win = multiworld.planks_required_count[player]
    connect(multiworld, player, used_names, TempleRegionNames.menu, TempleRegionNames.get_planks,
            False, ItemName.plank, planks_to_win, False)


def create_region(multiworld: MultiWorld, player: int, active_locations: typing.Dict[str, LocationData], name: str,
                  locations: typing.List[str]) -> Region:
    region = Region(name, player, multiworld)
    if locations:
        for location in locations:
            if location not in active_locations.keys():
                continue
            region.locations.append(HammerwatchLocation(player, location, active_locations[location].code, region))
    return region


def connect(multiworld: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
            two_way: bool, pass_item: str = None, item_count=1, items_consumed=True):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)

    entrance_name = get_entrance_name(used_names, source, target)

    connection = HWEntrance(player, entrance_name, source_region, target_region,
                            pass_item, item_count, items_consumed, None)

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect(multiworld, player, used_names, target, source, False, pass_item, item_count,
                items_consumed)


def connect_gate(multiworld: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
                 key_type: str, gate_codes: typing.Dict[str, str], gate_items: typing.Dict[str, int], gate_code: str,
                 two_way: bool):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)

    entrance_name = get_entrance_name(used_names, source, target)

    key_item_name = key_type
    if multiworld.gate_shuffle[player]:
        key_item_name = get_random_element(multiworld, gate_items)
        gate_items[key_item_name] -= 1
        if gate_items[key_item_name] == 0:
            gate_items.pop(key_item_name)
        gate_codes[gate_code] = key_item_name.split(" ")[-2].lower()

    connection = HWEntrance(player, entrance_name, source_region, target_region, key_item_name, 1, True, None)

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect(multiworld, player, used_names, target, source, False, key_item_name, 1, True)


def connect_exit(multiworld: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
                 exit_code: str, return_code: str, pass_item: str = None, item_count=1, items_consumed=True,
                 two_way=True):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)

    entrance_name = get_entrance_name(used_names, source, target)

    connection = HWEntrance(player, entrance_name, source_region, target_region,
                            pass_item, item_count, items_consumed, return_code, exit_code)
    source_region.exits.append(connection)
    # if return_code is None:
    #     connection.connect(target_region)
    #     return
    connection.linked = False
    multiworld.worlds[player].level_exits.append(connection)
    # multiworld.worlds[player].level_exits.append(
    #     HWExitData(source_region, target_region, return_code, exit_code, pass_item, item_count, items_consumed))

    if two_way and return_code is not None:
        connect_exit(multiworld, player, used_names, target, source, return_code, exit_code, pass_item, item_count,
                     items_consumed, False)


def connect_from_data(multiworld: MultiWorld, player: int, data: HWExitData):
    connect(multiworld, player, {}, data.parent, data.target, False,
            data.pass_item, data.item_count, data.items_consumed)


def etr_base_name(source: str, target: str):
    return source + " > " + target


def get_entrance_name(used_names: typing.Dict[str, int], source: str, target: str):
    base_name = etr_base_name(source, target)
    if base_name not in used_names:
        used_names[base_name] = 1
        name = base_name
    else:
        used_names[base_name] += 1
        name = base_name + ('_' * used_names[base_name])
    return name
