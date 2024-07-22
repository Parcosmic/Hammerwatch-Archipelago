import typing
from enum import Enum
from collections import namedtuple
from BaseClasses import Region, Entrance, CollectionState
from worlds.generic.Rules import add_rule
from .locations import HammerwatchLocation, LocationData, all_locations
from .names import castle_location_names, temple_location_names, castle_region_names, temple_region_names, item_name, \
    gate_names, entrance_names, shop_location_names, shop_region_names
from .util import (GoalType, Campaign, get_goal_type, get_random_element, castle_act_names, get_buttonsanity_insanity,
                   get_key_code, ShopType, ShopInfo)

if typing.TYPE_CHECKING:
    from . import HammerwatchWorld


class DoorType(Enum):
    Bronze = 0
    Silver = 1
    Gold = 2
    Bonus = 3


HWExitData = namedtuple("HWExitData",
                        ["parent", "target", "return_code", "exit_code", "pass_item", "item_count", "items_consumed"])


class HWEntrance(Entrance):
    target_region: Region
    pass_item: str
    item_count: int
    items_consumed: bool
    return_code: str
    exit_code: str
    swapped: bool

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
        self.swapped = False


def create_regions(world: "HammerwatchWorld", campaign: Campaign, active_locations: typing.Dict[str, LocationData]):
    gate_codes = {}
    if campaign == Campaign.Castle:
        create_castle_regions(world, active_locations)
        connect_castle_regions(world, gate_codes)
    else:
        create_tots_regions(world, active_locations)
        connect_tots_regions(world, gate_codes)
        create_temple_shop_regions(world, active_locations)
    return gate_codes


castle_regions: typing.Dict[str, typing.Optional[typing.List[str]]] = {
    castle_region_names.menu: None,
    castle_region_names.hub: None,
    castle_region_names.p1_start: [
        castle_location_names.p1_by_nw_bronze_gate,
        castle_location_names.btn_p1_floor,
        castle_location_names.ev_entrance_bridge,
    ],
    castle_region_names.p1_nw: [
        castle_location_names.p1_entrance_1,
        castle_location_names.p1_entrance_2,
        castle_location_names.p1_entrance_3,
        castle_location_names.p1_entrance_4,
        castle_location_names.p1_entrance_hall_1,
        castle_location_names.p1_entrance_hall_2,
    ],
    castle_region_names.p1_secret: [
        castle_location_names.p1_entrance_secret,
    ],
    castle_region_names.p1_nw_left: [
        castle_location_names.p1_entrance_s,
        castle_location_names.p1_entrance_w,
    ],
    castle_region_names.p1_s: [
        castle_location_names.p1_by_sw_bronze_gate_1,
        castle_location_names.p1_by_sw_bronze_gate_2,
        castle_location_names.p1_by_sw_bronze_gate_3,
        castle_location_names.p1_by_sw_bronze_gate_4,
        castle_location_names.p1_s_lower_hall_1,
        castle_location_names.p1_s_lower_hall_2,
        castle_location_names.p1_s_lower_hall_3,
        castle_location_names.p1_s_lower_hall_4,
        castle_location_names.p1_s_lower_hall_5,
        castle_location_names.p1_s_lower_hall_6,
        castle_location_names.p1_s_lower_hall_7,
        castle_location_names.p1_s_lower_hall_8,
        castle_location_names.p1_s_lower_hall_9,
        castle_location_names.p1_s_lower_hall_10,
        castle_location_names.p1_e_save_room_1,
        castle_location_names.p1_e_save_room_2,
        castle_location_names.p1_w_of_se_bronze_gate_1,
        castle_location_names.p1_w_of_se_bronze_gate_2,
        castle_location_names.p1_w_of_se_bronze_gate_3,
        castle_location_names.p1_w_of_se_bronze_gate_4,
        castle_location_names.p1_w_of_se_bronze_gate_5,
        castle_location_names.p1_s_w_bridges_w,
        castle_location_names.p1_s_of_e_save_room,
        castle_location_names.p1_n_of_se_bridge,
        castle_location_names.p1_w_save,
        castle_location_names.p1_center_bridges_n_1,
        castle_location_names.p1_center_bridges_n_2,
        castle_location_names.p1_center_bridges_n_3,
        castle_location_names.p1_center_bridges_s_1,
        castle_location_names.p1_center_bridges_s_2,
        castle_location_names.p1_center_bridges_s_3,
        castle_location_names.p1_center_bridges_s_4,
        castle_location_names.p1_e_secret,
        castle_location_names.p1_s_secret_1,
        castle_location_names.p1_s_secret_2,
        castle_location_names.p1_se_bridge,
    ],
    castle_region_names.p1_sw_bronze_gate: [
        castle_location_names.p1_sw_bronze_gate,
    ],
    castle_region_names.p1_e: [
        castle_location_names.p1_by_exit_1,
        castle_location_names.p1_by_exit_2,
        castle_location_names.p1_by_exit_3,
        castle_location_names.p1_by_m_bronze_gate_1,
        castle_location_names.p1_by_m_bronze_gate_2,
        castle_location_names.p1_by_m_bronze_gate_3,
        castle_location_names.p1_by_m_bronze_gate_4,
        castle_location_names.p1_by_m_bronze_gate_5,
        castle_location_names.p1_by_m_bronze_gate_6,
        castle_location_names.p1_e_bridges_1,
        castle_location_names.p1_e_bridges_2,
        castle_location_names.p1_e_bridges_3,
        castle_location_names.p1_e_bridges_4,
        castle_location_names.p1_e_bridges_5,
        castle_location_names.p1_room_by_exit,
        castle_location_names.p1_ne_arrow_traps,
        castle_location_names.p1_hint_room,
    ],
    castle_region_names.p1_m_bronze_gate: [
        castle_location_names.p1_m_bronze_gate,
    ],
    castle_region_names.p1_from_p2: [
        castle_location_names.p1_bars_1,
        castle_location_names.p1_bars_2,
        castle_location_names.p1_p2_by_shop,
    ],
    castle_region_names.p1_from_p3_n: [
        castle_location_names.p1_p3_n_bridge,
        castle_location_names.p1_p3_n_across_bridge,
        castle_location_names.btn_p1_boss,
        castle_location_names.btn_p1_boss_1,
        castle_location_names.btn_p1_boss_2,
        castle_location_names.btn_p1_boss_3,
        castle_location_names.btn_p1_boss_4,
    ],
    castle_region_names.p1_from_p3_s: [
        castle_location_names.p1_p3_s,
    ],
    castle_region_names.p2_start: None,
    castle_region_names.p2_m: [
        castle_location_names.p2_w_of_silver_gate_1,
        castle_location_names.p2_w_of_silver_gate_2,
        castle_location_names.p2_nw_island_s_1,
        castle_location_names.p2_nw_island_s_2,
        castle_location_names.p2_entrance_1,
        castle_location_names.p2_entrance_2,
        castle_location_names.p2_entrance_3,
        castle_location_names.p2_entrance_4,
        castle_location_names.p2_entrance_5,
        castle_location_names.p2_w_of_gold_gate,
        castle_location_names.p2_nw_island_1,
        castle_location_names.p2_nw_island_2,
        castle_location_names.p2_nw_island_3,
        castle_location_names.p2_nw_island_4,
        castle_location_names.p2_nw_island_5,
        castle_location_names.btn_p2_wall_shortcut_1,
    ],
    castle_region_names.p2_p1_return: [
        castle_location_names.btn_p2_wall_from_p1,
    ],
    castle_region_names.p2_n: [
        castle_location_names.p2_spike_puzzle_e_1,
        castle_location_names.p2_spike_puzzle_e_2,
        castle_location_names.p2_spike_puzzle_ne_1,
        castle_location_names.p2_spike_puzzle_ne_2,
        castle_location_names.p2_spike_puzzle_ne_3,
        castle_location_names.p2_spike_puzzle_e,
        castle_location_names.btn_p2_floor_red,
        castle_location_names.btn_p2_floor_spike_puzzle_e_1,
        castle_location_names.btn_p2_floor_spike_puzzle_e_2,
        castle_location_names.btn_p2_floor_spike_puzzle_e_3,
    ],
    castle_region_names.p2_spike_puzzle_bottom: [
        castle_location_names.btn_p2_floor_spike_puzzle_s_1,
        castle_location_names.btn_p2_floor_spike_puzzle_s_2,
        castle_location_names.btn_p2_floor_spike_puzzle_s_3,
    ],
    castle_region_names.p2_spike_puzzle_left: [
        castle_location_names.p2_spike_puzzle_w_1,
        castle_location_names.p2_spike_puzzle_w_2,
    ],
    castle_region_names.p2_spike_puzzle_top: [
        castle_location_names.p2_spike_puzzle_n_1,
        castle_location_names.p2_spike_puzzle_n_2,
        castle_location_names.btn_p2_floor_spike_puzzle_n_1,
        castle_location_names.btn_p2_floor_spike_puzzle_n_2,
        castle_location_names.btn_p2_floor_spike_puzzle_n_3,
    ],
    castle_region_names.p2_red_switch: [
        castle_location_names.p2_by_red_spikes_1,
        castle_location_names.p2_by_red_spikes_2,
        castle_location_names.p2_by_red_spikes_3,
        castle_location_names.p2_e_poker_plant_room_1,
        castle_location_names.p2_e_poker_plant_room_2,
        castle_location_names.p2_e_poker_plant_room_3,
        castle_location_names.p2_e_poker_plant_room_4,
        castle_location_names.p2_e_poker_plant_room_5,
        castle_location_names.p2_e_poker_plant_room_6,
        castle_location_names.p2_e_of_red_spikes_1,
        castle_location_names.p2_e_of_red_spikes_2,
        castle_location_names.p2_e_of_red_spikes_3,
        castle_location_names.p2_e_of_red_spikes_4,
        castle_location_names.p2_e_of_ne_save_1,
        castle_location_names.p2_e_of_ne_save_2,
        castle_location_names.p2_tower_plant_2,
        castle_location_names.btn_p2_floor_e_save,
    ],
    castle_region_names.p2_ne_secret: [
        castle_location_names.btn_p2_puzzle,
    ],
    castle_region_names.p2_puzzle: [
        castle_location_names.p2_puzzle_1,
        castle_location_names.p2_puzzle_2,
        castle_location_names.p2_puzzle_3,
        castle_location_names.p2_puzzle_4,
    ],
    castle_region_names.p2_e_bronze_gate: [
        # Offense shop
    ],
    castle_region_names.p2_e_save: [
        castle_location_names.p2_e_save,
    ],
    castle_region_names.p2_s: [
        castle_location_names.p2_big_bridge_1,
        castle_location_names.p2_big_bridge_2,
        castle_location_names.p2_big_bridge_3,
        castle_location_names.p2_s_arrow_traps_1,
        castle_location_names.p2_s_arrow_traps_2,
        castle_location_names.p2_s_arrow_traps_3,
        castle_location_names.p2_e_gold_gate_room_1,
        castle_location_names.p2_e_gold_gate_room_2,
        castle_location_names.p2_e_gold_gate_room_3,
        castle_location_names.p2_e_gold_gate_room_4,
        castle_location_names.p2_e_gold_gate_room_5,
        castle_location_names.p2_e_gold_gate_room_6,
        castle_location_names.p2_e_gold_gate_room_7,
        castle_location_names.p2_e_gold_gate_room_8,
        castle_location_names.p2_e_gold_gate_room_9,
        castle_location_names.p2_e_gold_gate_room_10,
        castle_location_names.p2_e_gold_gate_room_11,
        castle_location_names.p2_e_gold_gate_room_12,
        castle_location_names.p2_e_gold_gate_room_13,
        castle_location_names.p2_beetle_boss_room_1,
        castle_location_names.p2_beetle_boss_room_2,
        castle_location_names.p2_beetle_boss_room_3,
        castle_location_names.p2_beetle_boss_room_4,
        castle_location_names.p2_w_poker_plant_room_1,
        castle_location_names.p2_w_poker_plant_room_2,
        castle_location_names.p2_w_poker_plant_room_3,
        castle_location_names.p2_s_of_w_gold_gate_1,
        castle_location_names.p2_s_of_w_gold_gate_2,
        castle_location_names.p2_s_of_w_gold_gate_3,
        castle_location_names.p2_by_boss_switch,
        castle_location_names.p2_toggle_spike_trap_reward_1,
        castle_location_names.p2_toggle_spike_trap_reward_2,
        castle_location_names.p2_toggle_spike_trap_reward_3,
        castle_location_names.p2_miniboss_tick_1,
        castle_location_names.p2_miniboss_tick_2,
        castle_location_names.p2_tower_plant_1,
        castle_location_names.btn_p2_rune_sequence,
        castle_location_names.btn_p2_rune_sequence_3,
        castle_location_names.btn_p2_wall_shortcut_2,
        castle_location_names.btn_p2_boss,
        castle_location_names.btn_p2_boss_1,
        castle_location_names.btn_p2_boss_2,
        castle_location_names.btn_p2_boss_3,
        castle_location_names.btn_p2_boss_4,
    ],
    castle_region_names.p2_e_bronze_gate_2: [
        castle_location_names.btn_p2_rune_sequence_2
    ],
    castle_region_names.p2_m_bronze_gate: [
        castle_location_names.btn_p2_rune_sequence_1
    ],
    castle_region_names.p2_se_bronze_gate: [
        castle_location_names.btn_p2_rune_sequence_4
    ],
    castle_region_names.p2_gg_room_reward: [
        castle_location_names.p2_e_gold_gate_room_reward_1,
        castle_location_names.p2_e_gold_gate_room_reward_2,
    ],
    castle_region_names.p2_w_secrets: [
        castle_location_names.btn_p2_floor_tp_item_1,
        castle_location_names.btn_p2_floor_tp_item_2,
        castle_location_names.btn_p2_rune_puzzle,
        castle_location_names.btn_p2_rune_puzzle_1,
        castle_location_names.btn_p2_rune_puzzle_2,
        castle_location_names.btn_p2_rune_puzzle_3,
        castle_location_names.btn_p2_rune_puzzle_4,
    ],
    castle_region_names.p2_w_treasure: [
        castle_location_names.p2_beetle_boss_hidden_room_1,
    ],
    castle_region_names.p2_w_treasure_tp: [
        castle_location_names.p2_beetle_boss_hidden_room_2,
    ],
    castle_region_names.p2_tp_puzzle: [
        castle_location_names.p2_sequence_puzzle_reward,
    ],
    castle_region_names.p2_end: [
        castle_location_names.p2_end_1,
        castle_location_names.p2_end_2,
    ],
    castle_region_names.p3_start_door: [
        castle_location_names.btn_p3_wall_start,
    ],
    castle_region_names.p3_start: [
        castle_location_names.p3_entrance_s_of_poker_1,
        castle_location_names.p3_entrance_s_of_poker_2,
        castle_location_names.p3_entrance_s_of_poker_3,
        castle_location_names.p3_entrance_w,
        castle_location_names.p3_entrance_n_1,
        castle_location_names.p3_entrance_n_2,
        castle_location_names.p3_entrance_n_of_poker,
        castle_location_names.p3_entrance_sw,
        castle_location_names.p3_entrance_m_1,
        castle_location_names.p3_entrance_m_2,
        castle_location_names.p3_entrance_m_3,
        castle_location_names.p3_entrance_m_4,
        castle_location_names.p3_entrance_s_1,
        castle_location_names.p3_entrance_s_2,
        castle_location_names.p3_entrance_s_3,
        castle_location_names.p3_nw_n_1,
        castle_location_names.p3_nw_n_2,
        castle_location_names.p3_nw_nw_1,
        castle_location_names.p3_nw_nw_2,
        castle_location_names.p3_nw_nw_3,
        castle_location_names.p3_nw_m,
        castle_location_names.p3_nw_sw_1,
        castle_location_names.p3_nw_sw_2,
        castle_location_names.p3_nw_se,
        castle_location_names.p3_tower_plant_1,
        castle_location_names.btn_p3_floor,
        castle_location_names.btn_p3_wall_start_n,
    ],
    castle_region_names.p3_start_shop: [
        # Shop
    ],
    castle_region_names.p3_start_secret: [
        castle_location_names.btn_p3_wall_start_nw,
    ],
    castle_region_names.p3_nw_closed_room: [
        castle_location_names.p3_nw_closed_room,
    ],
    castle_region_names.p3_nw_n_bronze_gate: [
        castle_location_names.p3_nw_n_bronze_gate_1,
        castle_location_names.p3_nw_n_bronze_gate_2,
        castle_location_names.p3_nw_n_bronze_gate_3,
        castle_location_names.p3_nw_n_bronze_gate_4,
        castle_location_names.p3_nw_n_bronze_gate_5,
    ],
    castle_region_names.p3_nw_s_bronze_gate: [
        castle_location_names.p3_nw_s_bronze_gate_1,
        castle_location_names.p3_nw_s_bronze_gate_2,
        castle_location_names.p3_nw_s_bronze_gate_3,
        castle_location_names.p3_nw_s_bronze_gate_4,
        castle_location_names.p3_nw_s_bronze_gate_5,
    ],
    castle_region_names.p3_s_bronze_gate: None,
    castle_region_names.p3_silver_gate: [
        castle_location_names.p3_s_of_silver_gate,
    ],
    castle_region_names.p3_n_gold_gate: [
        castle_location_names.p3_by_w_shop,
        castle_location_names.p3_ne_se_1,
        castle_location_names.p3_ne_se_2,
        castle_location_names.p3_se_cross_hall_e_1,
        castle_location_names.p3_se_cross_hall_e_2,
        castle_location_names.p3_se_cross_hall_s_1,
        castle_location_names.p3_se_cross_hall_s_2,
        castle_location_names.p3_se_cross_hall_s_3,
        castle_location_names.p3_se_cross_hall_s_4,
        castle_location_names.p3_se_cross_hall_se,
        castle_location_names.p3_arrow_hall_1,
        castle_location_names.p3_arrow_hall_2,
        castle_location_names.p3_se_m_1,
        castle_location_names.p3_se_m_2,
        castle_location_names.p3_ne_e_1,
        castle_location_names.p3_ne_e_2,
        castle_location_names.p3_ne_e_3,
        castle_location_names.p3_ne_e_4,
        castle_location_names.p3_s_of_e_poker_1,
        castle_location_names.p3_s_of_e_poker_2,
        castle_location_names.p3_se_of_w_shop,
        castle_location_names.p3_sw_of_w_shop,
        castle_location_names.p3_miniboss_tick_1,
        castle_location_names.p3_miniboss_tick_2,
        castle_location_names.p3_tower_plant_2,
        castle_location_names.p3_tower_plant_5,
        castle_location_names.p3_tower_plant_6,
        castle_location_names.p3_tower_plant_7,
        castle_location_names.btn_p3_floor_red,
        castle_location_names.btn_p3_floor_blue,
        castle_location_names.btn_p3_floor_arrow_hall,
        castle_location_names.btn_p3_wall_bonus_nw,
        castle_location_names.btn_p3_wall_bonus_ne,
        castle_location_names.btn_p3_wall_bonus_s,
        castle_location_names.btn_p3_wall_bonus_se,
    ],
    castle_region_names.p3_rspikes: [
        castle_location_names.p3_red_spike_room,
        castle_location_names.btn_p3_wall_bonus_w_2,
    ],
    castle_region_names.p3_rspikes_room: [
        castle_location_names.p3_tower_plant_4,
        castle_location_names.btn_p3_wall_bonus_w_1,
        castle_location_names.btn_p3_seq_bonus,
    ],
    castle_region_names.p3_bspikes: [
        # Shop location
    ],
    castle_region_names.p3_bonus: [
        castle_location_names.btn_p3_wall_bonus,
        castle_location_names.btn_p3_rune_bonus,
        castle_location_names.btn_p3_rune_bonus_1,
        castle_location_names.btn_p3_rune_bonus_2,
        castle_location_names.btn_p3_rune_bonus_3,
        castle_location_names.btn_p3_rune_bonus_4,
        castle_location_names.btn_p3_rune_bonus_5,
        castle_location_names.btn_p3_rune_bonus_6,
        castle_location_names.btn_p3_rune_bonus_7,
        castle_location_names.btn_p3_rune_bonus_8,
        castle_location_names.btn_p3_rune_bonus_9,
    ],
    castle_region_names.p3_se_secret: [
        # Shop region
    ],
    castle_region_names.p3_arrow_hall_secret: [
        castle_location_names.btn_p3_wall_secret_arrow_hall,
    ],
    castle_region_names.p3_spikes_s: [
        castle_location_names.p3_spike_trap_1,
        castle_location_names.p3_spike_trap_2,
        castle_location_names.p3_spike_trap_3,
    ],
    castle_region_names.p3_m_secret: [
        castle_location_names.p3_by_m_shop_1,
        castle_location_names.p3_by_m_shop_2,
        # Shop region
    ],
    castle_region_names.p3_sw: [
        castle_location_names.p3_ne_of_bridge_1,
        castle_location_names.p3_ne_of_bridge_2,
        castle_location_names.p3_w_of_w_poker,
        castle_location_names.p3_s_of_w_poker,
        castle_location_names.p3_nw_of_bridge,
        castle_location_names.p3_n_of_bridge_1,
        castle_location_names.p3_n_of_bridge_2,
        castle_location_names.p3_n_of_bridge_3,
        castle_location_names.p3_n_of_bridge_4,
        castle_location_names.p3_n_of_bridge_5,
        castle_location_names.p3_w_of_bridge,
        castle_location_names.p3_e_of_bridge_1,
        castle_location_names.p3_e_of_bridge_2,
        castle_location_names.p3_e_of_bridge_3,
        castle_location_names.p3_s_of_boss_door,
        castle_location_names.p3_tower_plant_3,
        castle_location_names.p3_tower_plant_8,
        castle_location_names.btn_p3_boss_door,
        castle_location_names.btn_p3_floor_sw,
        castle_location_names.btn_p3_wall_sw,
        castle_location_names.btn_p3_wall_boss_door,
    ],
    castle_region_names.p3_boss: None,
    castle_region_names.p3_exit_s: [
        castle_location_names.btn_p3_wall_to_p1_s,
    ],
    castle_region_names.p3_hidden_arrow_hall: [
        castle_location_names.p3_secret_arrow_hall_1,
        castle_location_names.p3_secret_arrow_hall_2,
    ],
    castle_region_names.p3_hidden_s_hall_secret: [
        castle_location_names.p3_secret_secret,
    ],
    castle_region_names.p3_s_gold_gate: [
        castle_location_names.btn_p3_boss_s,
        castle_location_names.btn_p3_boss_s_1,
        castle_location_names.btn_p3_boss_s_2,
        castle_location_names.btn_p3_boss_s_3,
        castle_location_names.btn_p3_boss_s_4,
    ],
    castle_region_names.p3_bonus_return: [
        castle_location_names.p3_bonus_return,
    ],
    castle_region_names.n1_start: [
        castle_location_names.n1_entrance
    ],
    castle_region_names.n1_room1: [
        castle_location_names.n1_room1
    ],
    castle_region_names.n1_room2: [
        castle_location_names.n1_room2_s_1,
        castle_location_names.n1_room2_s_2,
        castle_location_names.n1_room2_s_3,
        castle_location_names.btn_n1_panel_n,
    ],
    castle_region_names.n1_room2_secret: [
        castle_location_names.n1_room2_n_secret_room,
    ],
    castle_region_names.n1_room2_unlock: [
        castle_location_names.n1_room2_small_box,
        castle_location_names.n1_room2_nw_room_1,
        castle_location_names.n1_room2_nw_room_2,
        castle_location_names.n1_room2_nw_room_3,
        castle_location_names.n1_room2_nw_room_4,
        castle_location_names.n1_room2_nw_room_5,
        castle_location_names.n1_room2_nw_room_6,
        castle_location_names.n1_room2_n_m_room_1,
        castle_location_names.n1_room2_n_m_room_2,
        castle_location_names.n1_room2_n_m_room_3,
        castle_location_names.n1_room2_n_m_room_4,
        castle_location_names.n1_room2_n_m_room_5,
        castle_location_names.n1_room2_n_m_room_6,
    ],
    castle_region_names.n1_room3: [
        castle_location_names.n1_room3_w_1,
        castle_location_names.n1_room3_w_2,
        castle_location_names.n1_room3_w_3,
        castle_location_names.n1_room3_w_4,
        castle_location_names.n1_room3_w_5,
        castle_location_names.n1_room3_w_6,
        castle_location_names.n1_room3_w_7,
        castle_location_names.n1_room3_w_8,
        castle_location_names.n1_room3_w_9,
        castle_location_names.n1_room3_w_10,
        castle_location_names.n1_room3_w_11,
        castle_location_names.n1_room3_w_12,
        castle_location_names.n1_room3_w_13,
        castle_location_names.n1_room3_w_14,
        castle_location_names.n1_room3_w_15,
        castle_location_names.n1_room3_w_16,
        castle_location_names.n1_room3_w_17,
        castle_location_names.n1_room3_w_18,
        castle_location_names.n1_room3_w_19,
        castle_location_names.n1_room3_w_20,
        castle_location_names.btn_n1_panel_e_1,
        castle_location_names.btn_n1_panel_e_2,
    ],
    castle_region_names.n1_room3_unlock: [
        castle_location_names.n1_room3_sealed_room_1,
        castle_location_names.n1_room3_sealed_room_2,
        castle_location_names.n1_room3_sealed_room_3,
        castle_location_names.n1_room3_sealed_room_4,
    ],
    castle_region_names.n1_room3_hall: [
        castle_location_names.btn_n1_panel_s,
    ],
    castle_region_names.n1_room4: [
        castle_location_names.n1_room4_e,
        castle_location_names.n1_room4_m,
        castle_location_names.n1_room4_w_1,
        castle_location_names.n1_room4_w_2,
        castle_location_names.n1_room4_s_1,
        castle_location_names.n1_room4_s_2,
        castle_location_names.n1_room4_s_3,
    ],
    castle_region_names.n1_exit: None,
    castle_region_names.b1_start: [
        castle_location_names.b1_behind_portal,
    ],
    castle_region_names.b1_arena: [
        castle_location_names.b1_arena_1,
        castle_location_names.b1_arena_2,
        castle_location_names.btn_b1_1,
        castle_location_names.btn_b1_2,
    ],
    castle_region_names.b1_defeated: [
        castle_location_names.b1_reward,
        castle_location_names.ev_beat_boss_1,
    ],
    castle_region_names.b1_exit: None,
    castle_region_names.a1_start: [
        castle_location_names.btn_a1_wall_start,
        castle_location_names.btn_a1_boss_door,
    ],
    castle_region_names.a1_boss: None,
    castle_region_names.a1_start_shop_w: [
        # Start bronze gate shop
    ],
    castle_region_names.a1_start_shop_m: [
        # Start top gold gate shop
    ],
    castle_region_names.a1_start_shop_e: [
        # Start bottom gold gate shop
    ],
    castle_region_names.a1_se: [
        castle_location_names.a1_s_save_1,
        castle_location_names.a1_s_save_2,
    ],
    castle_region_names.a1_e: [
        castle_location_names.a1_m_trellis_secret,
        castle_location_names.a1_n_save_1,
        castle_location_names.a1_n_save_2,
        castle_location_names.a1_n_save_3,
        castle_location_names.a1_n_save_4,
        castle_location_names.a1_ne_top_room_1,
        castle_location_names.a1_ne_top_room_2,
        castle_location_names.a1_ne_top_room_3,
        castle_location_names.a1_e_m_1,
        castle_location_names.a1_e_m_2,
        castle_location_names.a1_e_m_3,
        castle_location_names.a1_n_boss_hall,
        castle_location_names.a1_m_ice_tower_1,
        castle_location_names.a1_m_ice_tower_2,
        castle_location_names.a1_m_ice_tower_3,
        castle_location_names.a1_m_ice_tower_4,
        castle_location_names.a1_e_n_fireball_trap,
        castle_location_names.a1_e_e_fireball_trap,
        castle_location_names.a1_e_ne,
        castle_location_names.a1_ne_1,
        castle_location_names.a1_ne_2,
        castle_location_names.a1_ne_3,
        castle_location_names.a1_e_e,
        castle_location_names.a1_e_se,
        castle_location_names.a1_miniboss_skeleton_1,
        castle_location_names.a1_miniboss_skeleton_2,
        castle_location_names.a1_tower_ice_3,
        castle_location_names.a1_tower_ice_4,
        castle_location_names.btn_a1_floor_tp_n,
        castle_location_names.btn_a1_floor_red,
        castle_location_names.btn_a1_wall_red_spikes,
    ],
    castle_region_names.a1_ne_cache: [
        castle_location_names.a1_ne_ice_tower_secret,
    ],
    castle_region_names.a1_e_sw_bgate: None,
    castle_region_names.a1_e_s_bgate: None,
    castle_region_names.a1_e_se_bgate: [
        castle_location_names.btn_a1_wall_se,
    ],
    castle_region_names.a1_e_e_bgate: None,
    castle_region_names.a1_rune_room: [
        castle_location_names.btn_a1_rune,
        castle_location_names.btn_a1_rune_1,
        castle_location_names.btn_a1_rune_2,
        castle_location_names.btn_a1_rune_3,
        castle_location_names.btn_a1_rune_4,
    ],
    castle_region_names.a1_se_cache: [
        castle_location_names.a1_se_cache_1,
        castle_location_names.a1_se_cache_2,
        castle_location_names.a1_se_cache_3,
        castle_location_names.a1_se_cache_4,
    ],
    castle_region_names.a1_e_ne_bgate: [
        castle_location_names.a1_e_ne_bgate,
    ],
    castle_region_names.a1_red_spikes: [
        castle_location_names.a1_red_spikes_1,
        castle_location_names.a1_red_spikes_2,
        castle_location_names.a1_red_spikes_3,
    ],
    castle_region_names.a1_n_bgate: [
        castle_location_names.a1_n_cache_1,
        castle_location_names.a1_n_cache_2,
        castle_location_names.a1_n_cache_3,
        castle_location_names.a1_n_cache_4,
        castle_location_names.a1_n_cache_5,
        castle_location_names.a1_n_cache_6,
        castle_location_names.a1_n_cache_7,
        castle_location_names.a1_n_cache_8,
        castle_location_names.a1_n_cache_9,
    ],
    castle_region_names.a1_tp_n: [
        castle_location_names.a1_n_tp,
    ],
    castle_region_names.a1_w: [
        castle_location_names.a1_nw_left_1,
        castle_location_names.a1_nw_left_2,
        castle_location_names.a1_nw_left_3,
        castle_location_names.a1_nw_left_4,
        castle_location_names.a1_nw_left_5,
        castle_location_names.a1_nw_right_1,
        castle_location_names.a1_nw_right_2,
        castle_location_names.a1_nw_right_3,
        castle_location_names.a1_nw_right_4,
        castle_location_names.a1_sw_n_1,
        castle_location_names.a1_sw_n_2,
        castle_location_names.a1_sw_n_3,
        castle_location_names.a1_sw_w_1,
        castle_location_names.a1_sw_w_2,
        castle_location_names.a1_w_save_1,
        castle_location_names.a1_w_save_2,
        castle_location_names.a1_tower_ice_1,
        castle_location_names.a1_tower_ice_2,
        castle_location_names.btn_a1_boss,
        castle_location_names.btn_a1_boss_1,
        castle_location_names.btn_a1_boss_2,
        castle_location_names.btn_a1_boss_3,
        castle_location_names.btn_a1_boss_4,
        castle_location_names.btn_a1_floor_shortcut,
        castle_location_names.btn_a1_floor_sw,
        castle_location_names.btn_a1_wall_m_cache,
    ],
    castle_region_names.a1_n_secret: [
        castle_location_names.btn_a1_puzzle,
    ],
    castle_region_names.a1_puzzle: [
        castle_location_names.a1_puzzle_1,
        castle_location_names.a1_puzzle_2,
        castle_location_names.a1_puzzle_3,
        castle_location_names.a1_puzzle_4,
    ],
    castle_region_names.a1_w_ne_bgate: None,
    castle_region_names.a1_nw_bgate: [
        castle_location_names.a1_nw_bgate
    ],
    castle_region_names.a1_w_se_bgate: None,
    castle_region_names.a1_w_sw_bgate: None,
    castle_region_names.a1_w_sw_bgate_1: None,
    castle_region_names.a1_sw_spikes: [
        castle_location_names.a1_sw_spikes
    ],
    castle_region_names.a1_from_a2: [
        castle_location_names.a1_from_a2_1,
        castle_location_names.a1_from_a2_2,
        castle_location_names.a1_from_a2_3,
    ],
    # castle_region_names.a1_from_a2_secret: [
    #     # Just an Easter egg and a bunch of money (164 gold)
    # ],
    castle_region_names.a2_start: [
        castle_location_names.a2_n_of_s_save_1,
        castle_location_names.a2_n_of_s_save_2,
        castle_location_names.a2_n_of_s_save_3,
        castle_location_names.a2_n_of_s_save_4,
        castle_location_names.a2_s_fire_trap_1,
        castle_location_names.a2_s_fire_trap_2,
        castle_location_names.a2_sw_ice_tower,
        castle_location_names.a2_s_ice_tower_1,
        castle_location_names.a2_s_ice_tower_2,
        castle_location_names.a2_s_ice_tower_3,
        castle_location_names.a2_s_ice_tower_4,
        castle_location_names.a2_s_ice_tower_5,
        castle_location_names.a2_e_of_s_save_1,
        castle_location_names.a2_e_of_s_save_2,
        castle_location_names.a2_e_of_s_save_3,
        castle_location_names.a2_e_of_s_save_4,
        castle_location_names.a2_tower_ice_3,
        castle_location_names.a2_tower_ice_5,
        castle_location_names.btn_a2_floor_sw,
        castle_location_names.btn_a2_floor_tp_se,
        castle_location_names.btn_a2_wall_sw,
    ],
    castle_region_names.a2_s_secret: [
        castle_location_names.btn_a2_puzzle,
    ],
    castle_region_names.a2_puzzle: [
        castle_location_names.a2_puzzle_1,
        castle_location_names.a2_puzzle_2,
        castle_location_names.a2_puzzle_3,
        castle_location_names.a2_puzzle_4,
    ],
    castle_region_names.a2_tp_sw: [
        castle_location_names.a2_sw_ice_tower_tp,
    ],
    castle_region_names.a2_tp_se: [
        castle_location_names.a2_se_tp,
    ],
    castle_region_names.a2_sw_bgate: None,
    castle_region_names.a2_s_bgate: [
        castle_location_names.a2_s_bgate,
    ],
    castle_region_names.a2_se_bgate: None,
    castle_region_names.a2_s_save_bgate: None,
    castle_region_names.a2_ne: [
        castle_location_names.a2_s_of_n_save_1,
        castle_location_names.a2_s_of_n_save_2,
        castle_location_names.a2_s_of_n_save_3,
        castle_location_names.a2_nw_ice_tower_across_1,
        castle_location_names.a2_nw_ice_tower_across_2,
        castle_location_names.a2_nw_ice_tower_across_3,
        castle_location_names.a2_nw_ice_tower_across_4,
        castle_location_names.a2_e_save_room_1,
        castle_location_names.a2_e_save_room_2,
        castle_location_names.a2_e_save_room_3,
        castle_location_names.a2_e_save_room_4,
        castle_location_names.a2_e_save_room_5,
        castle_location_names.a2_e_save_room_6,
        castle_location_names.a2_n_of_ne_fire_traps_1,
        castle_location_names.a2_n_of_ne_fire_traps_2,
        castle_location_names.a2_s_of_ne_fire_traps_1,
        castle_location_names.a2_s_of_ne_fire_traps_2,
        castle_location_names.a2_ne_ice_tower_1,
        castle_location_names.a2_ne_ice_tower_2,
        castle_location_names.a2_ne_ice_tower_3,
        castle_location_names.a2_ne_ice_tower_4,
        castle_location_names.a2_ne_ice_tower_5,
        castle_location_names.a2_ne_ice_tower_6,
        castle_location_names.a2_ne_ice_tower_7,
        castle_location_names.a2_ne_ice_tower_8,
        castle_location_names.a2_ne_ice_tower_9,
        castle_location_names.a2_se_of_e_ice_tower_1,
        castle_location_names.a2_se_of_e_ice_tower_2,
        castle_location_names.a2_se_of_e_ice_tower_3,
        castle_location_names.a2_miniboss_skeleton_1,
        castle_location_names.a2_miniboss_skeleton_2,
        castle_location_names.a2_tower_ice_2,
        castle_location_names.a2_tower_ice_4,
        castle_location_names.btn_a2_boss,
        castle_location_names.btn_a2_boss_1,
        castle_location_names.btn_a2_boss_2,
        castle_location_names.btn_a2_boss_3,
        castle_location_names.btn_a2_boss_4,
        castle_location_names.btn_a2_floor_tp_n,
        castle_location_names.btn_a2_wall_e,
    ],
    castle_region_names.a2_ne_m_bgate: None,
    castle_region_names.a2_ne_l_bgate: [
        castle_location_names.a2_ne_l_bgate,
    ],
    castle_region_names.a2_ne_r_bgate: [
        castle_location_names.a2_ne_r_bgate_1,
        castle_location_names.a2_ne_r_bgate_2,
        castle_location_names.btn_a2_rune,
        castle_location_names.btn_a2_rune_1,
        castle_location_names.btn_a2_rune_2,
        castle_location_names.btn_a2_rune_3,
        castle_location_names.btn_a2_rune_4,
    ],
    castle_region_names.a2_ne_b_bgate: None,
    castle_region_names.a2_ne_save_bgate: None,
    castle_region_names.a2_tp_ne: [
        castle_location_names.a2_ne_tp,
    ],
    castle_region_names.a2_ne_secret: [
        castle_location_names.btn_a2_floor_secret_e,
    ],
    castle_region_names.a2_e: [
        castle_location_names.a2_e_ice_tower_1,
        castle_location_names.a2_e_ice_tower_2,
        castle_location_names.a2_e_ice_tower_3,
        castle_location_names.a2_e_ice_tower_4,
        castle_location_names.a2_e_ice_tower_5,
        castle_location_names.a2_e_ice_tower_6,
        castle_location_names.a2_s_of_e_bgate,
        castle_location_names.a2_tower_ice_6,
        castle_location_names.btn_a2_wall_se,
    ],
    castle_region_names.a2_e_bgate: [
        castle_location_names.a2_e_bgate,
    ],
    castle_region_names.a2_nw: [
        castle_location_names.a2_pyramid_1,
        castle_location_names.a2_pyramid_3,
        castle_location_names.a2_pyramid_4,
        castle_location_names.a2_nw_ice_tower,
        castle_location_names.a2_by_w_a1_stair,
        castle_location_names.a2_tower_ice_1,
        castle_location_names.btn_a2_floor_pyramid_nw,
        castle_location_names.btn_a2_floor_pyramid_ne,
        castle_location_names.btn_a2_floor_pyramid_sw,
        castle_location_names.btn_a2_floor_pyramid_se,
        castle_location_names.btn_a2_floor_pyramid_m,
        castle_location_names.btn_a2_wall_nw,
    ],
    castle_region_names.a2_bonus_return: [
        castle_location_names.a2_bonus_return,
    ],
    castle_region_names.a2_blue_spikes: [
        castle_location_names.a2_blue_spikes,
    ],
    castle_region_names.a2_blue_spikes_tp: [
        castle_location_names.a2_nw_tp,
    ],
    castle_region_names.a2_to_a3: None,
    castle_region_names.n2_start: [
        castle_location_names.n2_start_1,
        castle_location_names.n2_start_2,
        castle_location_names.n2_start_3,
        castle_location_names.n2_start_4,
    ],
    castle_region_names.n2_m: [
        castle_location_names.n2_m_m_1,
        castle_location_names.n2_m_m_2,
        castle_location_names.n2_m_m_3,
        castle_location_names.n2_m_n,
        castle_location_names.n2_m_e,
        castle_location_names.n2_m_se_1,
        castle_location_names.n2_m_se_2,
        castle_location_names.n2_m_se_3,
        castle_location_names.n2_m_se_4,
        castle_location_names.n2_m_se_5,
        castle_location_names.btn_n2_panel_n,
    ],
    castle_region_names.n2_nw: [
        castle_location_names.n2_nw_top_1,
        castle_location_names.n2_nw_top_2,
        castle_location_names.n2_nw_top_3,
        castle_location_names.n2_nw_top_4,
        castle_location_names.n2_nw_top_5,
        castle_location_names.n2_nw_top_6,
        castle_location_names.n2_nw_top_7,
        castle_location_names.n2_nw_top_8,
        castle_location_names.n2_nw_top_9,
        castle_location_names.n2_nw_bottom_1,
        castle_location_names.n2_nw_bottom_2,
        castle_location_names.n2_nw_bottom_3,
        castle_location_names.n2_nw_bottom_4,
        castle_location_names.btn_n2_floor_blue,
    ],
    castle_region_names.n2_w: [
        castle_location_names.n2_w_1,
        castle_location_names.n2_w_2,
        castle_location_names.n2_w_3,
        castle_location_names.n2_w_4,
        castle_location_names.n2_w_5,
        castle_location_names.n2_w_6,
        castle_location_names.n2_w_7,
        castle_location_names.n2_w_8,
        castle_location_names.n2_w_9,
        castle_location_names.n2_w_10,
        castle_location_names.n2_w_11,
        castle_location_names.n2_w_12,
        castle_location_names.n2_w_13,
        castle_location_names.n2_w_14,
        castle_location_names.n2_w_15,
    ],
    castle_region_names.n2_e: [
        castle_location_names.n2_e_1,
        castle_location_names.n2_e_2,
        castle_location_names.n2_e_3,
        castle_location_names.n2_e_4,
        castle_location_names.n2_e_5,
        castle_location_names.n2_e_6,
        castle_location_names.n2_e_7,
        castle_location_names.n2_e_8,
        castle_location_names.n2_e_9,
        castle_location_names.n2_e_10,
        castle_location_names.n2_e_11,
        castle_location_names.n2_e_12,
        castle_location_names.n2_e_13,
        castle_location_names.n2_e_14,
        castle_location_names.n2_e_15,
    ],
    castle_region_names.n2_n: [
        castle_location_names.n2_n_1,
        castle_location_names.n2_n_2,
        castle_location_names.n2_n_3,
        castle_location_names.n2_n_4,
        castle_location_names.n2_n_5,
        castle_location_names.n2_n_6,
        castle_location_names.n2_n_7,
        castle_location_names.n2_n_8,
        castle_location_names.n2_n_9,
        castle_location_names.n2_n_10,
        castle_location_names.n2_n_11,
        castle_location_names.n2_n_12,
        castle_location_names.n2_n_13,
        castle_location_names.n2_n_14,
        castle_location_names.n2_n_15,
    ],
    castle_region_names.n2_s: [
        castle_location_names.n2_s_1,
        castle_location_names.n2_s_2,
        castle_location_names.n2_s_3,
        castle_location_names.n2_s_4,
        castle_location_names.n2_s_5,
        castle_location_names.n2_s_6,
        castle_location_names.n2_s_7,
        castle_location_names.n2_s_8,
        castle_location_names.n2_s_9,
    ],
    castle_region_names.n2_ne: [
        castle_location_names.n2_ne_1,
        castle_location_names.n2_ne_2,
        castle_location_names.n2_ne_3,
        castle_location_names.n2_ne_4,
        castle_location_names.btn_n2_panel_ne,
    ],
    castle_region_names.n2_se: [
        castle_location_names.btn_n2_panel_se,
    ],
    castle_region_names.n2_exit: None,
    castle_region_names.a3_start: [
        castle_location_names.a3_sw_1,
        castle_location_names.a3_sw_2,
        castle_location_names.a3_sw_3,
        castle_location_names.btn_a3_wall_start,
    ],
    castle_region_names.a3_main: [
        castle_location_names.a3_s_banner_secret,
        castle_location_names.a3_nw_save_2,
        castle_location_names.a3_nw_save_3,
        castle_location_names.a3_ne_ice_towers_1,
        castle_location_names.a3_ne_ice_towers_2,
        castle_location_names.a3_ne_ice_towers_3,
        castle_location_names.a3_pyramids_s_1,
        castle_location_names.a3_pyramids_s_2,
        castle_location_names.a3_pyramids_s_3,
        castle_location_names.a3_e_ice_towers_1,
        castle_location_names.a3_e_ice_towers_2,
        castle_location_names.a3_spike_floor_8,
        castle_location_names.a3_spike_floor_15,
        castle_location_names.a3_spike_floor_11,
        castle_location_names.a3_spike_floor_14,
        castle_location_names.a3_nw_save_1,
        castle_location_names.a3_s_of_knife_puzzle,
        castle_location_names.a3_fireball_hall_2,
        castle_location_names.a3_pyramids_s_5,
        castle_location_names.a3_pyramids_s_4,
        castle_location_names.a3_e_ice_towers_3,
        castle_location_names.a3_spike_floor_1,
        castle_location_names.a3_spike_floor_7,
        castle_location_names.a3_spike_floor_4,
        castle_location_names.a3_spike_floor_9,
        castle_location_names.a3_spike_floor_13,
        castle_location_names.a3_s_of_n_save_2,
        castle_location_names.a3_pyramids_n_3,
        castle_location_names.a3_pyramids_n_2,
        castle_location_names.a3_pyramids_n_1,
        castle_location_names.a3_ne_ice_towers_6,
        castle_location_names.a3_ne_ice_towers_5,
        castle_location_names.a3_ne_ice_towers_4,
        castle_location_names.a3_pyramids_n_5,
        castle_location_names.a3_pyramids_n_4,
        castle_location_names.a3_pyramids_s_6,
        castle_location_names.a3_pyramids_s_7,
        castle_location_names.a3_se_boss_room_1,
        castle_location_names.a3_se_boss_room_2,
        castle_location_names.a3_spike_floor_6,
        castle_location_names.a3_spike_floor_5,
        castle_location_names.a3_se_boss_room_3,
        castle_location_names.a3_s_of_n_save_1,
        castle_location_names.a3_pyramids_e,
        castle_location_names.a3_spike_floor_3,
        castle_location_names.a3_spike_floor_12,
        castle_location_names.a3_spike_floor_2,
        castle_location_names.a3_pyramid,
        castle_location_names.a3_fireball_hall_1,
        castle_location_names.a3_e_of_spike_floor,
        castle_location_names.a3_spike_floor_10,
        castle_location_names.a3_miniboss_skeleton_1,
        castle_location_names.a3_miniboss_skeleton_2,
        castle_location_names.a3_tower_ice_1,
        castle_location_names.a3_tower_ice_2,
        castle_location_names.a3_tower_ice_3,
        castle_location_names.a3_tower_ice_4,
        castle_location_names.a3_tower_ice_5,
        castle_location_names.a3_tower_ice_6,
        castle_location_names.a3_tower_ice_7,
        castle_location_names.a3_tower_ice_8,
        castle_location_names.a3_tower_ice_9,
        castle_location_names.btn_a3_boss,
        castle_location_names.btn_a3_boss_1,
        castle_location_names.btn_a3_boss_2,
        castle_location_names.btn_a3_boss_3,
        castle_location_names.btn_a3_boss_4,
        castle_location_names.btn_a3_floor_knife_1,
        castle_location_names.btn_a3_floor_knife_2,
        castle_location_names.btn_a3_floor_knife_3,
        castle_location_names.btn_a3_floor_knife_4,
        castle_location_names.btn_a3_floor_knife_5,
        castle_location_names.btn_a3_floor_tp_m,
        castle_location_names.btn_a3_wall_end,
        castle_location_names.btn_a3_seq_knife,
    ],
    castle_region_names.a3_tp: [
        castle_location_names.a3_m_tp,
    ],
    castle_region_names.a3_from_a2: [
        castle_location_names.btn_a3_wall_from_a2,
    ],
    castle_region_names.a3_from_a2_wall: [
        castle_location_names.btn_a3_floor_stairs_in_wall,
    ],
    castle_region_names.a3_knife_puzzle_reward: [
        castle_location_names.a3_knife_puzzle_reward_l_5,
        castle_location_names.a3_knife_puzzle_reward_r,
        castle_location_names.btn_a3_wall_knife_1,
        castle_location_names.btn_a3_wall_knife_2,
        castle_location_names.btn_a3_seq_knife_2,
    ],
    castle_region_names.a3_knife_reward_2: [
        castle_location_names.a3_knife_puzzle_reward_l_1,
        castle_location_names.a3_knife_puzzle_reward_l_2,
        castle_location_names.a3_knife_puzzle_reward_l_3,
        castle_location_names.a3_knife_puzzle_reward_l_4,
    ],
    castle_region_names.a3_secret: [
        castle_location_names.a3_secret_shop,
        # Shop region
    ],
    castle_region_names.a3_nw_stairs: None,
    castle_region_names.a3_w_b_bgate: None,
    castle_region_names.a3_w_b_bgate_tp: [
        castle_location_names.a3_pyramids_s_bgate_tp
    ],
    castle_region_names.a3_w_t_bgate: None,
    castle_region_names.a3_w_r_bgate: None,
    castle_region_names.a3_n_l_bgate: None,
    castle_region_names.a3_n_r_bgate: None,
    castle_region_names.a3_e_l_bgate: None,
    castle_region_names.a3_e_r_bgate: None,
    castle_region_names.b2_start: None,
    castle_region_names.b2_arena: None,
    castle_region_names.b2_defeated: [
        castle_location_names.b2_boss,
        castle_location_names.b2_boss_reward,
        castle_location_names.ev_beat_boss_2,
    ],
    castle_region_names.b2_exit: None,
    castle_region_names.r1_start: [
        castle_location_names.r1_se_1,
        castle_location_names.r1_se_2,
        castle_location_names.r1_se_3,
        castle_location_names.r1_se_4,
        castle_location_names.r1_se_5,
        castle_location_names.r1_se_6,
    ],
    castle_region_names.r1_se_ggate: [
        castle_location_names.btn_r1_floor_se,
    ],
    castle_region_names.r1_start_wall: [
        castle_location_names.r1_start_wall
    ],
    castle_region_names.r1_e: [
        castle_location_names.r1_e_knife_trap_1,
        castle_location_names.r1_e_knife_trap_2,
        castle_location_names.r1_e_knife_trap_3,
        castle_location_names.r1_e_knife_trap_4,
        castle_location_names.r1_e_knife_trap_5,
        castle_location_names.r1_e_knife_trap_6,
        castle_location_names.r1_e_knife_trap_7,
        castle_location_names.r1_e_s,
        castle_location_names.btn_r1_floor_e,
    ],
    castle_region_names.r1_e_s_bgate: [
        castle_location_names.r1_e_s_bgate
    ],
    castle_region_names.r1_e_n_bgate: [
        castle_location_names.r1_e_fire_floor_1,
        castle_location_names.r1_e_fire_floor_2,
        castle_location_names.r1_e_fire_floor_3,
        castle_location_names.r1_e_w_1,
        castle_location_names.r1_e_w_2,
        castle_location_names.r1_e_e,
        castle_location_names.r1_e_n_1,
        castle_location_names.r1_e_n_2,
        castle_location_names.r1_e_n_3,
        castle_location_names.r1_tower_plant_2,
        castle_location_names.btn_r1_wall_ne,
    ],
    castle_region_names.r1_e_sgate: [
        castle_location_names.r1_e_sgate,
        castle_location_names.btn_r1_wall_se,
    ],
    castle_region_names.r1_se_wall: [
        castle_location_names.r1_se_wall
    ],
    castle_region_names.r1_ne_ggate: [
        castle_location_names.r1_ne_ggate_1,
        castle_location_names.r1_ne_ggate_2,
        castle_location_names.r1_ne_ggate_3,
        castle_location_names.r1_ne_ggate_4,
        castle_location_names.btn_r1_floor_ne,
    ],
    castle_region_names.r1_nw: [
        castle_location_names.r1_nw_1,
        castle_location_names.r1_nw_2,
        castle_location_names.r1_tower_plant_1,
        castle_location_names.btn_r1_floor_nw,
        castle_location_names.btn_r1_puzzle,
    ],
    castle_region_names.r1_puzzle: [
        castle_location_names.r1_puzzle_1,
        castle_location_names.r1_puzzle_2,
        castle_location_names.r1_puzzle_3,
        castle_location_names.r1_puzzle_4,
    ],
    castle_region_names.r1_nw_hidden: [
        castle_location_names.r1_nw_hidden_1,
        castle_location_names.r1_nw_hidden_2,
    ],
    castle_region_names.r1_nw_ggate: [
        castle_location_names.btn_r1_floor_nw_hidden,
    ],
    castle_region_names.r1_sw: [
        castle_location_names.r1_sw_nw_1,
        castle_location_names.r1_sw_nw_2,
        castle_location_names.r1_sw_nw_3,
        castle_location_names.r1_sw_ne_1,
        castle_location_names.r1_sw_ne_2,
        castle_location_names.r1_sw_ne_3,
        castle_location_names.r1_sw_ne_4,
        castle_location_names.r1_sw_ne_5,
        castle_location_names.r1_sw_ne_6,
        castle_location_names.r1_sw_ne_7,
        castle_location_names.r1_sw_ne_8,
        castle_location_names.r1_sw_ne_9,
        castle_location_names.r1_w_knife_trap_1,
        castle_location_names.r1_w_knife_trap_2,
        castle_location_names.r1_w_knife_trap_3,
        castle_location_names.r1_w_knife_trap_4,
        castle_location_names.r1_w_knife_trap_5,
        castle_location_names.r1_w_knife_trap_6,
        castle_location_names.r1_w_knife_trap_7,
        castle_location_names.r1_sw_ggate_1,
        castle_location_names.r1_sw_ggate_2,
        castle_location_names.r1_tower_plant_3,
        castle_location_names.r1_tower_plant_4,
        castle_location_names.btn_r1_wall_w,
    ],
    castle_region_names.r1_w_sgate: [
        castle_location_names.btn_r1_floor_w_shop,
        # Shop region
    ],
    castle_region_names.r1_sw_ggate: [
        castle_location_names.btn_r1_floor_w_s,
    ],
    castle_region_names.r1_exit_l: [
        castle_location_names.btn_r1_floor_exit,
    ],
    castle_region_names.r1_exit_r: None,
    castle_region_names.r2_start: [
        castle_location_names.r2_start,
        castle_location_names.btn_r2_wall_start,
    ],
    castle_region_names.r2_bswitch: [
        castle_location_names.btn_r2_boss_e,
        castle_location_names.btn_r2_boss_e_1,
        castle_location_names.btn_r2_boss_e_2,
        castle_location_names.btn_r2_boss_e_3,
        castle_location_names.btn_r2_boss_e_4,
    ],
    castle_region_names.r2_m: [
        castle_location_names.r2_n_3,
        castle_location_names.r2_n_4,
        castle_location_names.r2_n_bronze_gates_3,
        castle_location_names.r2_n_bronze_gates_2,
        castle_location_names.r2_m_start_1,
        castle_location_names.r2_m_start_2,
        castle_location_names.r2_e_hall_2,
        castle_location_names.r2_e_hall_1,
        castle_location_names.r2_by_sgate_8,
        castle_location_names.r2_by_sgate_7,
        castle_location_names.r2_by_sgate_6,
        castle_location_names.r2_m_spike_trap_2,
        castle_location_names.r2_n_bronze_gates_4,
        castle_location_names.r2_w_boss_3,
        castle_location_names.r2_n_bronze_gates_1,
        castle_location_names.r2_m_e_of_spike_trap_3,
        castle_location_names.r2_by_sgate_1,
        castle_location_names.r2_m_spike_trap_10,
        castle_location_names.r2_w_boss_6,
        castle_location_names.r2_by_sgate_2,
        castle_location_names.r2_e_hall_4,
        castle_location_names.r2_e_hall_3,
        castle_location_names.r2_m_spike_trap_8,
        castle_location_names.r2_n_5,
        castle_location_names.r2_n_6,
        castle_location_names.r2_n_7,
        castle_location_names.r2_w_boss_8,
        castle_location_names.r2_w_boss_7,
        castle_location_names.r2_w_boss_5,
        castle_location_names.r2_w_boss_4,
        castle_location_names.r2_m_e_of_spike_trap_4,
        castle_location_names.r2_m_e_of_spike_trap_1,
        castle_location_names.r2_m_e_of_spike_trap_2,
        castle_location_names.r2_by_sgate_3,
        castle_location_names.r2_by_sgate_5,
        castle_location_names.r2_by_sgate_4,
        castle_location_names.r2_m_spike_trap_5,
        castle_location_names.r2_m_spike_trap_6,
        castle_location_names.r2_m_spike_trap_9,
        castle_location_names.r2_m_spike_trap_7,
        castle_location_names.r2_n_2,
        castle_location_names.r2_se_save,
        castle_location_names.r2_m_spike_trap_4,
        castle_location_names.r2_w_boss_1,
        castle_location_names.r2_m_spike_trap_3,
        castle_location_names.r2_n_1,
        castle_location_names.r2_w_boss_2,
        castle_location_names.r2_m_spike_trap_1,
        castle_location_names.r2_miniboss_eye_e_1,
        castle_location_names.r2_miniboss_eye_e_2,
        castle_location_names.r2_miniboss_eye_w_1,
        castle_location_names.r2_miniboss_eye_w_2,
        castle_location_names.r2_tower_plant_2,
        castle_location_names.r2_tower_plant_3,
        castle_location_names.r2_tower_plant_4,
        castle_location_names.btn_r2_floor_ne,
        castle_location_names.btn_r2_wall_nw,
    ],
    castle_region_names.r2_nw: [
        castle_location_names.r2_nw_spike_trap_1,
        castle_location_names.r2_nw_spike_trap_2,
        castle_location_names.r2_tower_plant_1,
        castle_location_names.btn_r2_floor_nw,
    ],
    castle_region_names.r2_n: [
        castle_location_names.r2_n_closed_room,
        castle_location_names.btn_r2_boss_n,
        castle_location_names.btn_r2_boss_n_1,
        castle_location_names.btn_r2_boss_n_2,
        castle_location_names.btn_r2_boss_n_3,
        castle_location_names.btn_r2_boss_n_4,
        castle_location_names.btn_r2_floor_boss_rune,
    ],
    castle_region_names.r2_e: [
        castle_location_names.r2_e_1,
        castle_location_names.r2_e_2,
        castle_location_names.r2_e_3,
        castle_location_names.r2_e_4,
        castle_location_names.r2_e_5,
        castle_location_names.btn_r2_floor_e,
    ],
    castle_region_names.r2_w_bgate: None,
    castle_region_names.r2_sgate: [
        castle_location_names.btn_r2_floor_gate_s,
    ],
    castle_region_names.r2_s: [
        castle_location_names.r2_sw_1,
        castle_location_names.r2_sw_2,
        castle_location_names.r2_sw_3,
        castle_location_names.r2_sw_4,
        castle_location_names.r2_sw_5,
        castle_location_names.r2_sw_6,
        castle_location_names.r2_sw_7,
        castle_location_names.r2_sw_8,
        castle_location_names.r2_sw_9,
        castle_location_names.r2_sw_10,
        castle_location_names.r2_sw_11,
        castle_location_names.r2_sw_12,
        castle_location_names.r2_tower_plant_5,
        castle_location_names.btn_r2_floor_sw_hidden,
        castle_location_names.btn_r2_floor_sw,
    ],
    castle_region_names.r2_spike_island: [
        castle_location_names.r2_s_knife_trap_1,
        castle_location_names.r2_s_knife_trap_2,
        castle_location_names.r2_s_knife_trap_3,
        castle_location_names.r2_s_knife_trap_4,
        castle_location_names.r2_s_knife_trap_5,
        castle_location_names.btn_r2_wall_spike_island_n,
        castle_location_names.btn_r2_wall_spike_island_s,
    ],
    castle_region_names.r2_sw_bridge: [
    ],
    castle_region_names.r2_sw_secret: [
        castle_location_names.btn_r2_rune,
        castle_location_names.btn_r2_rune_1,
        castle_location_names.btn_r2_rune_2,
        castle_location_names.btn_r2_rune_3,
        castle_location_names.btn_r2_rune_4,
    ],
    castle_region_names.r2_puzzle_room: [
        castle_location_names.btn_r2_puzzle,
    ],
    castle_region_names.r2_puzzle: [
        castle_location_names.r2_puzzle_1,
        castle_location_names.r2_puzzle_2,
        castle_location_names.r2_puzzle_3,
        castle_location_names.r2_puzzle_4,
    ],
    castle_region_names.r2_w: [
        castle_location_names.r2_w_island,
    ],
    castle_region_names.r2_from_r3: [
        castle_location_names.r2_ne_knife_trap_end,
        castle_location_names.btn_r2_wall_ne,
    ],
    castle_region_names.r2_ne_cache: [
        castle_location_names.r2_ne_knife_trap_wall_1,
        castle_location_names.r2_ne_knife_trap_wall_2,
        castle_location_names.r2_ne_knife_trap_wall_3,
    ],
    # castle_region_names.r2_ne_secret: [
    #     # The act 3 Easter egg and a lot more money
    # ],
    castle_region_names.r2_ggate: [
        castle_location_names.btn_r2_floor_gate_w,
    ],
    castle_region_names.r2_exit: None,
    castle_region_names.r3_main: [
        castle_location_names.r3_ne_knife_trap_1,
        castle_location_names.r3_ne_knife_trap_2,
        castle_location_names.r3_e_fire_floor_n_1,
        castle_location_names.r3_e_fire_floor_n_2,
        castle_location_names.r3_sw_bgate_3,
        castle_location_names.r3_sw_bgate_4,
        castle_location_names.r3_sw_bgate_5,
        castle_location_names.r3_n_bgate_e,
        castle_location_names.r3_w_fire_floor_1,
        castle_location_names.r3_start,
        castle_location_names.r3_e_miniboss,
        castle_location_names.r3_e_fire_floor_w,
        castle_location_names.r3_nw_save_2,
        castle_location_names.r3_ne_save_1,
        castle_location_names.r3_ne_save_2,
        castle_location_names.r3_start_nw_3,
        castle_location_names.r3_sw_bgate_2,
        castle_location_names.r3_sw_bgate_1,
        castle_location_names.r3_n_miniboss_4,
        castle_location_names.r3_n_miniboss_3,
        castle_location_names.r3_n_miniboss_2,
        castle_location_names.r3_e_shops_4,
        castle_location_names.r3_e_shops_5,
        castle_location_names.r3_start_nw_2,
        castle_location_names.r3_start_nw_1,
        castle_location_names.r3_e_fire_floor_n_5,
        castle_location_names.r3_e_fire_floor_n_4,
        castle_location_names.r3_e_fire_floor_n_3,
        castle_location_names.r3_shops_room_e_3,
        castle_location_names.r3_shops_room_e_2,
        castle_location_names.r3_shops_room_e_1,
        castle_location_names.r3_w_fire_floor_2,
        castle_location_names.r3_e_fire_floor_e,
        castle_location_names.r3_w_ggate_w,
        castle_location_names.r3_s_save,
        castle_location_names.r3_nw_save_1,
        castle_location_names.r3_n_miniboss_1,
        castle_location_names.r3_e_shops_3,
        castle_location_names.r3_shops_room_secret,
        castle_location_names.r3_miniboss_eye_e_1,
        castle_location_names.r3_miniboss_eye_e_2,
        castle_location_names.r3_miniboss_eye_n_1,
        castle_location_names.r3_miniboss_eye_n_2,
        castle_location_names.r3_miniboss_eye_s_1,
        castle_location_names.r3_miniboss_eye_s_2,
        castle_location_names.r3_tower_plant_1,
        castle_location_names.r3_tower_plant_2,
        castle_location_names.r3_tower_plant_4,
        castle_location_names.r3_tower_plant_6,
        castle_location_names.r3_tower_plant_7,
        castle_location_names.r3_tower_plant_8,
        castle_location_names.r3_tower_plant_9,
        castle_location_names.r3_tower_plant_10,
        castle_location_names.btn_r3_floor_ne,
        castle_location_names.btn_r3_floor_s,
        castle_location_names.btn_r3_floor_se,
        castle_location_names.btn_r3_wall_ne_1,
        castle_location_names.btn_r3_wall_ne_2,
        castle_location_names.btn_r3_wall_seq_n,
        castle_location_names.btn_r3_wall_seq_w,
        castle_location_names.btn_r3_wall_seq_m,
    ],
    castle_region_names.r3_ne_room: [
        castle_location_names.r3_e_secret_tp,
        castle_location_names.r3_e_tp,
        castle_location_names.btn_r3_floor_ne_room,
    ],
    castle_region_names.r3_s_room: [
        castle_location_names.r3_s_shops_room_1,
        castle_location_names.r3_s_shops_room_2,
        castle_location_names.btn_r3_floor_s_room,
    ],
    castle_region_names.r3_w_ggate: [
        castle_location_names.r3_s_of_boss_door_1,
        castle_location_names.r3_s_of_boss_door_2,
        castle_location_names.r3_tower_plant_5,
    ],
    castle_region_names.r3_e_ggate: [
        castle_location_names.r3_e_ggate_hallway_1,
        castle_location_names.r3_e_ggate_hallway_2,
        castle_location_names.r3_e_ggate_hallway_3,
        castle_location_names.r3_tower_plant_3,
        castle_location_names.btn_r3_floor_gate_nw,
    ],
    castle_region_names.r3_sw_bgate: [
        castle_location_names.btn_r3_wall_sw_gate,
    ],
    castle_region_names.r3_sw_bgate_secret: [
        castle_location_names.btn_r3_floor_sw_gate,
    ],
    castle_region_names.r3_sw_wall_r: [
        castle_location_names.r3_sw_hidden_room_1,
        castle_location_names.r3_sw_hidden_room_2,
    ],
    castle_region_names.r3_passage_start: [
        # A bit of money
    ],
    castle_region_names.r3_passage: [
        # Nothing really here
    ],
    castle_region_names.r3_passage_mid: [
        castle_location_names.btn_r3_floor_passage,
    ],
    castle_region_names.r3_passage_room_1: [
        castle_location_names.r3_w_passage_s_closed_room,
        castle_location_names.btn_r3_wall_passage_room_1,
    ],
    castle_region_names.r3_passage_room_2: [
        castle_location_names.r3_w_passage_behind_spikes,
        castle_location_names.btn_r3_floor_passage_room_2,
    ],
    castle_region_names.r3_passage_spikes: [
        castle_location_names.btn_r3_wall_passage_room_2,
    ],
    castle_region_names.r3_passage_end: [
        castle_location_names.btn_r3_floor_passage_end,
    ],
    castle_region_names.r3_nw_tp: [
        castle_location_names.r3_nw_tp,
    ],
    castle_region_names.r3_se_secret: [
        castle_location_names.r3_e_fire_floor_secret,
        castle_location_names.btn_r3_wall_seq_ne,
    ],
    castle_region_names.r3_boss_switch: [
        castle_location_names.r3_boss_switch_room_1,
        castle_location_names.r3_boss_switch_room_2,
        castle_location_names.r3_boss_switch_room_3,
        castle_location_names.btn_r3_boss,
        castle_location_names.btn_r3_boss_1,
        castle_location_names.btn_r3_boss_2,
        castle_location_names.btn_r3_boss_3,
        castle_location_names.btn_r3_boss_4,
        castle_location_names.btn_r3_wall_seq_se,
        castle_location_names.btn_r3_seq_simon_room,
    ],
    castle_region_names.r3_rune_room: [
        castle_location_names.btn_r3_floor_simon,
    ],
    castle_region_names.r3_simon_says: [
        castle_location_names.btn_r3_simon,
        castle_location_names.btn_r3_simon_1,
        castle_location_names.btn_r3_simon_2,
        castle_location_names.btn_r3_simon_3,
        castle_location_names.btn_r3_simon_4,
        castle_location_names.btn_r3_simon_5,
        castle_location_names.btn_r3_simon_6,
    ],
    castle_region_names.r3_bonus: None,
    castle_region_names.r3_l_shop_sgate: [
        castle_location_names.r3_s_shops_room_left_shop,
        # Shop region
    ],
    castle_region_names.r3_r_shop_sgate: [
        # Shop region
    ],
    castle_region_names.r3_bonus_return: [
        castle_location_names.r3_bonus_return_1,
        castle_location_names.r3_bonus_return_2,
        castle_location_names.btn_r3_rune,
        castle_location_names.btn_r3_rune_1,
        castle_location_names.btn_r3_rune_2,
        castle_location_names.btn_r3_rune_3,
        castle_location_names.btn_r3_rune_4,
    ],
    castle_region_names.r3_bonus_return_bridge: [
        castle_location_names.r3_e_shops_puzzle_reward,
    ],
    castle_region_names.r3_exit: [
        castle_location_names.btn_r3_boss_door,
    ],
    castle_region_names.r3_boss: None,
    castle_region_names.n3_main: [
        castle_location_names.n3_tp_room_n_1,
        castle_location_names.n3_tp_room_n_2,
        castle_location_names.n3_exit_e_1,
        castle_location_names.n3_exit_e_2,
        castle_location_names.n3_exit_e_3,
        castle_location_names.n3_exit_e_6,
        castle_location_names.n3_exit_e_4,
        castle_location_names.n3_exit_e_5,
        castle_location_names.n3_exit_e_7,
        castle_location_names.n3_exit_e_8,
        castle_location_names.n3_exit_e_9,
        castle_location_names.n3_nw_cluster_1,
        castle_location_names.n3_nw_cluster_2,
        castle_location_names.n3_nw_cluster_3,
        castle_location_names.n3_nw_cluster_6,
        castle_location_names.n3_nw_cluster_5,
        castle_location_names.n3_nw_cluster_4,
        castle_location_names.n3_nw_cluster_7,
        castle_location_names.n3_nw_cluster_8,
        castle_location_names.n3_nw_cluster_9,
        castle_location_names.n3_exit_s_cluster_7,
        castle_location_names.n3_exit_s_cluster_9,
        castle_location_names.n3_exit_s_cluster_8,
        castle_location_names.n3_exit_s_cluster_4,
        castle_location_names.n3_exit_s_cluster_6,
        castle_location_names.n3_exit_s_cluster_5,
        castle_location_names.n3_exit_s_cluster_1,
        castle_location_names.n3_exit_s_cluster_3,
        castle_location_names.n3_exit_s_cluster_2,
        castle_location_names.n3_exit_se_cluster_7,
        castle_location_names.n3_exit_se_cluster_9,
        castle_location_names.n3_exit_se_cluster_8,
        castle_location_names.n3_exit_se_cluster_4,
        castle_location_names.n3_exit_se_cluster_6,
        castle_location_names.n3_exit_se_cluster_5,
        castle_location_names.n3_exit_se_cluster_1,
        castle_location_names.n3_exit_se_cluster_3,
        castle_location_names.n3_exit_se_cluster_2,
        castle_location_names.n3_tp_room_e_4,
        castle_location_names.n3_tp_room_e_3,
        castle_location_names.n3_tp_room_e_2,
        castle_location_names.n3_tp_room_e_1,
        castle_location_names.n3_m_cluster_7,
        castle_location_names.n3_m_cluster_8,
        castle_location_names.n3_m_cluster_9,
        castle_location_names.n3_m_cluster_6,
        castle_location_names.n3_m_cluster_4,
        castle_location_names.n3_m_cluster_1,
        castle_location_names.n3_m_cluster_3,
        castle_location_names.n3_m_cluster_2,
        castle_location_names.n3_se_cluster_1,
        castle_location_names.n3_se_cluster_2,
        castle_location_names.n3_se_cluster_3,
        castle_location_names.n3_se_cluster_6,
        castle_location_names.n3_se_cluster_4,
        castle_location_names.n3_se_cluster_7,
        castle_location_names.n3_se_cluster_8,
        castle_location_names.n3_se_cluster_9,
        castle_location_names.n3_exit_sw,
        castle_location_names.n3_m_cluster_5,
        castle_location_names.n3_se_cluster_5,
        castle_location_names.n3_exit_s,
        castle_location_names.n3_exit_se,
    ],
    castle_region_names.n3_tp_room: [
        castle_location_names.n3_tp_room,
    ],
    castle_region_names.b3_start: None,
    castle_region_names.b3_arena: None,
    castle_region_names.b3_defeated: [
        castle_location_names.b3_boss,
        castle_location_names.b3_reward,
        castle_location_names.ev_beat_boss_3,
    ],
    castle_region_names.b3_exit: None,
    castle_region_names.c1_start: [
        castle_location_names.c1_n_alcove_2,
        castle_location_names.c1_n_alcove_3,
        castle_location_names.c1_s_ice_towers_4,
        castle_location_names.c1_s_ice_towers_6,
        castle_location_names.c1_n_ice_tower_3,
        castle_location_names.c1_n_ice_tower_1,
        castle_location_names.c1_n_alcove_1,
        castle_location_names.c1_ne,
        castle_location_names.c1_s_ice_towers_1,
        castle_location_names.c1_s_ice_towers_2,
        castle_location_names.c1_start,
        castle_location_names.c1_s_ice_towers_3,
        castle_location_names.c1_s_ice_towers_5,
        castle_location_names.c1_n_ice_tower_2,
        castle_location_names.c1_m_knife_traps,
        castle_location_names.c1_n_alcove_4,
        castle_location_names.c1_ne_knife_traps_1,
        castle_location_names.c1_ne_knife_traps_2,
        castle_location_names.c1_tower_plant_1,
        castle_location_names.c1_tower_ice_2,
        castle_location_names.c1_tower_ice_3,
        castle_location_names.btn_c1_floor_n,
        castle_location_names.btn_c1_floor_red,
        castle_location_names.btn_c1_wall_red,
    ],
    castle_region_names.c1_se_spikes: [
        castle_location_names.c1_se_spikes
    ],
    castle_region_names.c1_n_spikes: [
        castle_location_names.c1_n_spikes_1,
        castle_location_names.c1_n_spikes_2,
        castle_location_names.c1_tower_ice_1,
    ],
    castle_region_names.c1_shop: [
        # Shop region
    ],
    castle_region_names.c1_w: [
        castle_location_names.c1_w_1,
        castle_location_names.c1_w_2,
        castle_location_names.c1_w_3,
        castle_location_names.c1_miniboss_lich_1,
        castle_location_names.c1_miniboss_lich_2,
        castle_location_names.c1_tower_plant_2,
    ],
    castle_region_names.c1_sgate: [
        castle_location_names.c1_sgate,
        castle_location_names.btn_c1_wall_portal,
    ],
    castle_region_names.c1_prison_stairs: [
        castle_location_names.c1_prison_stairs
    ],
    castle_region_names.c1_s_bgate: [
        castle_location_names.btn_c1_wall_s_gate,
    ],
    castle_region_names.c1_ledge: [
        castle_location_names.c1_ledge_1,
        castle_location_names.c1_ledge_2,
        castle_location_names.btn_c1_wall_ledge,
    ],
    castle_region_names.c1_tp_island: [
        castle_location_names.c1_tp_island_1,
        castle_location_names.c1_tp_island_2,
    ],
    castle_region_names.pstart_start: [
        castle_location_names.btn_pstart_rune,
        castle_location_names.btn_pstart_rune_1,
        castle_location_names.btn_pstart_rune_2,
        castle_location_names.btn_pstart_rune_3,
        castle_location_names.btn_pstart_rune_4,
    ],
    castle_region_names.pstart_puzzle_island: [
        castle_location_names.btn_pstart_puzzle,
    ],
    castle_region_names.pstart_puzzle: [
        castle_location_names.pstart_puzzle_1,
        castle_location_names.pstart_puzzle_2,
        castle_location_names.pstart_puzzle_3,
        castle_location_names.pstart_puzzle_4,
    ],
    castle_region_names.c2_main: [
        castle_location_names.c2_ne_platform_5,
        castle_location_names.c2_e_fire_floor_1,
        castle_location_names.c2_w_spikes_s_2,
        castle_location_names.c2_w_spikes_s_1,
        castle_location_names.c2_sw_ice_tower_5,
        castle_location_names.c2_sw_ice_tower_4,
        castle_location_names.c2_w_spikes_e_2,
        castle_location_names.c2_w_spikes_e_1,
        castle_location_names.c2_w_save,
        castle_location_names.c2_w_alcove_2,
        castle_location_names.c2_w_alcove_1,
        castle_location_names.c2_e_fire_floor_w_2,
        castle_location_names.c2_e_fire_floor_w_1,
        castle_location_names.c2_w_knife_traps_6,
        castle_location_names.c2_w_knife_traps_5,
        castle_location_names.c2_s_3,
        castle_location_names.c2_s_2,
        castle_location_names.c2_start_s_6,
        castle_location_names.c2_start_s_5,
        castle_location_names.c2_start_s_7,
        castle_location_names.c2_ne_2,
        castle_location_names.c2_ne_4,
        castle_location_names.c2_ne_3,
        castle_location_names.c2_ne_6,
        castle_location_names.c2_w_alcove_4,
        castle_location_names.c2_w_alcove_3,
        castle_location_names.c2_w_spikes_s_3,
        castle_location_names.c2_w_spikes_e_3,
        castle_location_names.c2_ne_platform_n_1,
        castle_location_names.c2_ne_5,
        castle_location_names.c2_ne_platform_4,
        castle_location_names.c2_by_tp_island_1,
        castle_location_names.c2_w_spikes_s_7,
        castle_location_names.c2_w_knife_traps_2,
        castle_location_names.c2_w_knife_traps_4,
        castle_location_names.c2_s_1,
        castle_location_names.c2_s_6,
        castle_location_names.c2_start_s_1,
        castle_location_names.c2_se_flame_turrets_1,
        castle_location_names.c2_se_flame_turrets_4,
        castle_location_names.c2_exit,
        castle_location_names.c2_ne_platform_n_3,
        castle_location_names.c2_ne_platform_6,
        castle_location_names.c2_by_tp_island_3,
        castle_location_names.c2_w_knife_traps_1,
        castle_location_names.c2_s_7,
        castle_location_names.c2_se_flame_turrets_2,
        castle_location_names.c2_sw_ice_tower_1,
        castle_location_names.c2_sw_ice_tower_2,
        castle_location_names.c2_sw_ice_tower_3,
        castle_location_names.c2_w_spikes_s_4,
        castle_location_names.c2_w_spikes_s_5,
        castle_location_names.c2_w_spikes_s_6,
        castle_location_names.c2_ne_platform_n_2,
        castle_location_names.c2_ne_platform_n_4,
        castle_location_names.c2_e_fire_floor_w_3,
        castle_location_names.c2_e_fire_floor_w_4,
        castle_location_names.c2_e_fire_floor_w_5,
        castle_location_names.c2_start_s_2,
        castle_location_names.c2_start_s_3,
        castle_location_names.c2_start_s_4,
        castle_location_names.c2_ne_1,
        castle_location_names.c2_by_tp_island_2,
        castle_location_names.c2_boss_portal,
        castle_location_names.c2_w_knife_traps_3,
        castle_location_names.c2_s_5,
        castle_location_names.c2_se_flame_turrets_3,
        castle_location_names.c2_se_flame_turrets_5,
        castle_location_names.c2_e_fire_floor_2,
        castle_location_names.c2_ne_platform_1,
        castle_location_names.c2_w_spikes_e_4,
        castle_location_names.c2_ne_platform_3,
        castle_location_names.c2_ne_platform_2,
        castle_location_names.c2_s_4,
        castle_location_names.c2_miniboss_lich_ne_1,
        castle_location_names.c2_miniboss_lich_ne_2,
        castle_location_names.c2_miniboss_lich_m_1,
        castle_location_names.c2_miniboss_lich_m_2,
        castle_location_names.c2_tower_plant_2,
        castle_location_names.c2_tower_plant_3,
        castle_location_names.c2_tower_plant_4,
        castle_location_names.c2_tower_plant_5,
        castle_location_names.c2_tower_plant_6,
        castle_location_names.c2_tower_plant_7,
        castle_location_names.c2_tower_plant_8,
        castle_location_names.c2_tower_ice_1,
        castle_location_names.c2_tower_ice_2,
        castle_location_names.c2_tower_ice_3,
        castle_location_names.c2_tower_ice_4,
        castle_location_names.c2_tower_ice_5,
        castle_location_names.c2_tower_ice_9,
        castle_location_names.c2_tower_ice_10,
        castle_location_names.c2_tower_ice_11,
        castle_location_names.c2_by_e_shops_2_1,
        castle_location_names.c2_by_e_shops_2_2,
        castle_location_names.btn_c2_boss_w,
        castle_location_names.btn_c2_boss_w_1,
        castle_location_names.btn_c2_boss_w_2,
        castle_location_names.btn_c2_boss_w_3,
        castle_location_names.btn_c2_boss_w_4,
        castle_location_names.btn_c2_floor_sw,
        castle_location_names.btn_c2_floor_w,
        castle_location_names.btn_c2_rune,
        castle_location_names.btn_c2_rune_1,
        castle_location_names.btn_c2_rune_2,
        castle_location_names.btn_c2_rune_3,
        castle_location_names.btn_c2_rune_4,
        castle_location_names.btn_c2_wall_red_n,
        castle_location_names.btn_c2_wall_blue,
        castle_location_names.btn_c2_wall_red_s,
        castle_location_names.btn_c2_wall_s_save,
    ],
    castle_region_names.c2_boss: None,
    castle_region_names.c2_exit_bgate: [
        castle_location_names.btn_c2_wall_n_exit_gate,
    ],
    castle_region_names.c2_sw_wall: [
        castle_location_names.c2_sw_ice_tower_6,
    ],
    castle_region_names.c2_w_wall: [
        castle_location_names.c2_w_save_wall,
    ],
    castle_region_names.c2_e_wall: [
        castle_location_names.c2_by_e_shops_2,
    ],
    castle_region_names.c2_w_spikes: [
        castle_location_names.c2_w_spikes_1,
        castle_location_names.c2_w_spikes_2,
        castle_location_names.c2_w_spikes_3,
        castle_location_names.c2_w_spikes_4,
    ],
    castle_region_names.c2_w_shops_1: [
        castle_location_names.c2_by_w_shops_1,
        # Shop region
    ],
    castle_region_names.c2_w_shops_2: [
        castle_location_names.c2_by_w_shops_2,
        # Shop region
    ],
    castle_region_names.c2_w_shops_3: [
        castle_location_names.c2_by_w_shops_3_1,
        castle_location_names.c2_by_w_shops_3_2,
        # Shop region
    ],
    castle_region_names.c2_e_shops_1: [
        castle_location_names.btn_c2_wall_portal_shop,
        # Shop region
    ],
    castle_region_names.c2_e_shops_2: [
        castle_location_names.btn_c2_wall_e_shop,
        # Shop region
    ],
    castle_region_names.c2_puzzle_room: [
        castle_location_names.btn_c2_puzzle,
    ],
    castle_region_names.c2_puzzle: [
        castle_location_names.c2_puzzle_1,
        castle_location_names.c2_puzzle_2,
        castle_location_names.c2_puzzle_3,
        castle_location_names.c2_puzzle_4,
    ],
    castle_region_names.c2_n: [
        castle_location_names.c2_nw_ledge_1,
        castle_location_names.c2_nw_ledge_2,
        castle_location_names.c2_nw_ledge_3,
        castle_location_names.c2_nw_ledge_4,
        castle_location_names.c2_nw_ledge_5,
        castle_location_names.c2_nw_ledge_6,
        castle_location_names.c2_nw_ledge_7,
        castle_location_names.c2_nw_knife_traps_1,
        castle_location_names.c2_nw_knife_traps_2,
        castle_location_names.c2_nw_knife_traps_3,
        castle_location_names.c2_nw_knife_traps_4,
        castle_location_names.c2_nw_knife_traps_5,
        castle_location_names.c2_miniboss_lich_n_1,
        castle_location_names.c2_miniboss_lich_n_2,
        castle_location_names.c2_tower_plant_1,
        castle_location_names.c2_tower_ice_6,
        castle_location_names.c2_tower_ice_7,
        castle_location_names.c2_tower_ice_8,
        castle_location_names.btn_c2_wall_seq_nw,
        castle_location_names.btn_c2_wall_seq_ne,
        castle_location_names.btn_c2_wall_seq_w,
        castle_location_names.btn_c2_wall_seq_s,
        castle_location_names.btn_c2_wall_seq_e,
        castle_location_names.btn_c2_seq_bonus,
    ],
    castle_region_names.c2_n_wall: [
        castle_location_names.c2_n_wall
    ],
    castle_region_names.c2_bonus: [
        castle_location_names.btn_c2_rune_bonus,
        castle_location_names.btn_c2_rune_bonus_1,
        castle_location_names.btn_c2_rune_bonus_2,
        castle_location_names.btn_c2_rune_bonus_3,
        castle_location_names.btn_c2_rune_bonus_4,
        castle_location_names.btn_c2_rune_bonus_5,
        castle_location_names.btn_c2_rune_bonus_6,
        castle_location_names.btn_c2_rune_bonus_7,
        castle_location_names.btn_c2_rune_bonus_8,
    ],
    castle_region_names.c2_bonus_return: [
        castle_location_names.c2_bonus_return
    ],
    castle_region_names.c2_tp_island: [
        castle_location_names.btn_c2_boss_e,
        castle_location_names.btn_c2_boss_e_1,
        castle_location_names.btn_c2_boss_e_2,
        castle_location_names.btn_c2_boss_e_3,
        castle_location_names.btn_c2_boss_e_4,
    ],
    castle_region_names.c2_c3_tp: [
        castle_location_names.btn_c2_floor_t_hall,
    ],
    castle_region_names.c2_n_shops: [
        # Shop region #1
        # Shop region #2
    ],
    castle_region_names.n4_main: [
        castle_location_names.n4_ne,
        castle_location_names.n4_by_w_room_1,
        castle_location_names.n4_by_exit,
        castle_location_names.n4_by_w_room_2,
    ],
    castle_region_names.n4_nw: [
        castle_location_names.n4_nw_1,
        castle_location_names.n4_nw_2,
        castle_location_names.n4_nw_3,
        castle_location_names.n4_nw_5,
        castle_location_names.n4_nw_4,
        castle_location_names.n4_nw_6,
        castle_location_names.n4_nw_7,
        castle_location_names.n4_nw_8,
        castle_location_names.n4_nw_9,
        castle_location_names.n4_nw_10,
        castle_location_names.n4_nw_11,
        castle_location_names.n4_nw_14,
        castle_location_names.n4_nw_15,
        castle_location_names.n4_nw_16,
        castle_location_names.n4_nw_13,
        castle_location_names.n4_nw_12,
    ],
    castle_region_names.n4_w: [
        castle_location_names.n4_w_7,
        castle_location_names.n4_w_4,
        castle_location_names.n4_w_3,
        castle_location_names.n4_w_2,
        castle_location_names.n4_w_1,
        castle_location_names.n4_w_6,
        castle_location_names.n4_w_5,
        castle_location_names.n4_w_8,
        castle_location_names.n4_w_10,
        castle_location_names.n4_w_11,
        castle_location_names.n4_w_12,
        castle_location_names.n4_w_13,
        castle_location_names.n4_w_14,
        castle_location_names.n4_w_9,
    ],
    castle_region_names.n4_e: [
        castle_location_names.n4_e_11,
        castle_location_names.n4_e_24,
        castle_location_names.n4_e_16,
        castle_location_names.n4_e_8,
        castle_location_names.n4_e_7,
        castle_location_names.n4_e_6,
        castle_location_names.n4_e_14,
        castle_location_names.n4_e_15,
        castle_location_names.n4_e_22,
        castle_location_names.n4_e_20,
        castle_location_names.n4_e_19,
        castle_location_names.n4_e_18,
        castle_location_names.n4_e_17,
        castle_location_names.n4_e_9,
        castle_location_names.n4_e_10,
        castle_location_names.n4_e_12,
        castle_location_names.n4_e_13,
        castle_location_names.n4_e_5,
        castle_location_names.n4_e_4,
        castle_location_names.n4_e_3,
        castle_location_names.n4_e_2,
        castle_location_names.n4_e_1,
        castle_location_names.n4_e_25,
        castle_location_names.n4_e_26,
        castle_location_names.n4_e_27,
        castle_location_names.n4_e_28,
        castle_location_names.n4_e_29,
        castle_location_names.n4_e_30,
        castle_location_names.n4_e_31,
        castle_location_names.n4_e_32,
        castle_location_names.n4_e_23,
        castle_location_names.n4_e_21,
    ],
    castle_region_names.n4_exit: None,
    castle_region_names.c3_start: [
        castle_location_names.c3_start_e
    ],
    castle_region_names.c3_rspike_switch: [
        castle_location_names.btn_c3_wall_red
    ],
    castle_region_names.c3_rspikes: [
        castle_location_names.c3_w_ledge_1,
        castle_location_names.c3_w_ledge_2,
        castle_location_names.c3_m_ice_towers_1,
        castle_location_names.c3_m_ice_towers_2,
        castle_location_names.c3_m_ice_towers_3,
        castle_location_names.c3_m_ice_towers_4,
        castle_location_names.c3_se_save_1,
        castle_location_names.c3_se_save_2,
        castle_location_names.c3_se_save_3,
        castle_location_names.c3_sw_save_1,
        castle_location_names.c3_sw_save_2,
        castle_location_names.c3_sw_save_3,
        castle_location_names.c3_fire_floor_w,
        castle_location_names.c3_ne_npc_1,
        castle_location_names.c3_ne_npc_2,
        castle_location_names.c3_ne_npc_3,
        castle_location_names.c3_miniboss_lich_sw_1,
        castle_location_names.c3_miniboss_lich_sw_2,
        castle_location_names.c3_tower_plant_3,
        castle_location_names.c3_tower_plant_4,
        castle_location_names.c3_tower_plant_5,
        castle_location_names.c3_tower_plant_6,
        castle_location_names.c3_tower_ice_5,
        castle_location_names.c3_tower_ice_7,
        castle_location_names.c3_tower_ice_8,
        castle_location_names.c3_tower_ice_9,
        castle_location_names.c3_tower_ice_10,
        castle_location_names.btn_c3_rune,
        castle_location_names.btn_c3_rune_e,
        castle_location_names.btn_c3_rune_se,
        castle_location_names.btn_c3_rune_w,
        castle_location_names.btn_c3_rune_s,
        castle_location_names.btn_c3_floor,
        castle_location_names.btn_c3_wall_blue,
        castle_location_names.btn_c3_wall_w,
    ],
    castle_region_names.c3_m_wall: [
        castle_location_names.c3_m_wall
    ],
    castle_region_names.c3_m_shop: [
        castle_location_names.btn_c3_wall_shop,
        # Shop region
    ],
    castle_region_names.c3_m_tp: [
        castle_location_names.c3_m_tp
    ],
    castle_region_names.c3_s_bgate: [
        castle_location_names.c3_s_bgate
    ],
    castle_region_names.c3_nw: [
        castle_location_names.c3_nw_ice_towers_1,
        castle_location_names.c3_nw_ice_towers_2,
        castle_location_names.c3_nw_ice_towers_3,
        castle_location_names.c3_nw_ice_towers_w,
        castle_location_names.c3_e_miniboss,
        castle_location_names.c3_n_spike_floor_1,
        castle_location_names.c3_n_spike_floor_2,
        castle_location_names.c3_boss_switch,
        castle_location_names.c3_miniboss_lich_e_1,
        castle_location_names.c3_miniboss_lich_e_2,
        castle_location_names.c3_tower_plant_1,
        castle_location_names.c3_tower_plant_2,
        castle_location_names.c3_tower_ice_1,
        castle_location_names.c3_tower_ice_2,
        castle_location_names.c3_tower_ice_3,
        castle_location_names.c3_tower_ice_4,
        castle_location_names.c3_tower_ice_6,
        castle_location_names.btn_c3_rune_n,
        castle_location_names.btn_c3_rune_ne,
        castle_location_names.btn_c3_boss,
        castle_location_names.btn_c3_boss_1,
        castle_location_names.btn_c3_boss_2,
        castle_location_names.btn_c3_boss_3,
        castle_location_names.btn_c3_boss_4,
    ],
    castle_region_names.c3_sw_hidden: [
        castle_location_names.c3_sw_hidden,
        castle_location_names.btn_c3_wall_sw_hidden,
    ],
    castle_region_names.c3_se_hidden: [
        castle_location_names.btn_c3_wall_se_hidden,
    ],
    castle_region_names.c3_light_bridge: [
        castle_location_names.c3_light_bridge_1,
        castle_location_names.c3_light_bridge_2,
        castle_location_names.c3_light_bridge_3,
    ],
    castle_region_names.c3_easter_egg: [
        castle_location_names.c3_easter_egg,
    ],
    castle_region_names.c3_fire_floor: [
        castle_location_names.c3_fire_floor_1,
        castle_location_names.c3_fire_floor_2,
        castle_location_names.c3_fire_floor_3,
        castle_location_names.btn_c3_wall_fire_floor,
    ],
    castle_region_names.c3_fire_floor_tp: [
        castle_location_names.c3_fire_floor_tp
    ],
    castle_region_names.c3_c2_tp: [
        castle_location_names.c3_c2_tp
    ],
    castle_region_names.b4_start: [
        castle_location_names.b4_w_1,
        castle_location_names.b4_w_2,
        castle_location_names.b4_w_3,
        castle_location_names.b4_w_4,
        castle_location_names.b4_w_5,
        castle_location_names.b4_w_6,
        castle_location_names.b4_w_7,
        castle_location_names.b4_w_8,
        castle_location_names.b4_w_9,
        castle_location_names.b4_w_10,
        castle_location_names.b4_w_11,
        castle_location_names.b4_w_12,
        castle_location_names.b4_e_1,
        castle_location_names.b4_e_2,
        castle_location_names.b4_e_3,
        castle_location_names.b4_e_4,
        castle_location_names.b4_e_5,
        castle_location_names.b4_e_6,
        castle_location_names.b4_e_7,
        castle_location_names.b4_e_8,
        castle_location_names.b4_dragon_12,
        castle_location_names.b4_miniboss_lich_1,
        castle_location_names.b4_miniboss_lich_2,
    ],
    castle_region_names.b4_defeated: [
        castle_location_names.b4_dragon_1,
        castle_location_names.b4_dragon_2,
        castle_location_names.b4_dragon_3,
        castle_location_names.b4_dragon_4,
        castle_location_names.b4_dragon_5,
        castle_location_names.b4_dragon_6,
        castle_location_names.b4_dragon_7,
        castle_location_names.b4_dragon_8,
        castle_location_names.b4_dragon_9,
        castle_location_names.b4_dragon_10,
        castle_location_names.b4_dragon_11,
        castle_location_names.b4_plank_1,
        castle_location_names.b4_plank_2,
        castle_location_names.b4_plank_3,
        castle_location_names.b4_plank_4,
        castle_location_names.b4_plank_5,
        castle_location_names.b4_plank_6,
        castle_location_names.b4_plank_7,
        castle_location_names.b4_plank_8,
        castle_location_names.b4_plank_9,
        castle_location_names.b4_plank_10,
        castle_location_names.b4_plank_11,
        castle_location_names.ev_beat_boss_4,
    ],
    castle_region_names.e1_main: None,
    castle_region_names.e2_main: [
        castle_location_names.e2_entrance,
        castle_location_names.e2_end,
    ],
    castle_region_names.e3_main: [
        castle_location_names.e3_entrance_1,
        castle_location_names.e3_entrance_2,
    ],
    castle_region_names.e4_main: [
        castle_location_names.e4_main,
    ],
    castle_region_names.escaped: [
        castle_location_names.ev_escape
    ],
}
p3_portal_boss_rune_room_regions = {
    castle_region_names.p3_portal_from_p1: [
        castle_location_names.p3_skip_boss_switch_1,
        castle_location_names.p3_skip_boss_switch_2,
        castle_location_names.p3_skip_boss_switch_3,
        castle_location_names.p3_skip_boss_switch_4,
        castle_location_names.p3_skip_boss_switch_5,
        castle_location_names.p3_skip_boss_switch_6,
    ]
}


def create_castle_regions(world: "HammerwatchWorld", active_locations: typing.Dict[str, LocationData]):

    castle_created_regions = [create_region(world, active_locations, region_name, locations)
                              for region_name, locations in castle_regions.items()]

    if world.options.shortcut_teleporter.value == world.options.shortcut_teleporter.option_true:
        castle_created_regions.extend([create_region(world, active_locations, region_name, locations)
                                       for region_name, locations in p3_portal_boss_rune_room_regions.items()])

    world.multiworld.regions.extend(castle_created_regions)


def create_temple_shop_regions(world: "HammerwatchWorld", active_locations: typing.Dict[str, LocationData]):
    created_shop_regions = []
    shop_regions: typing.Dict[ShopType, typing.List[Region]] = {}

    for shop_type, shop_names in shop_region_names.shop_regions.items():
        shop_regions[shop_type] = []
        for t, shop_name in enumerate(shop_names):
            region_location_names = []
            for player_class, shop_type_locs in shop_location_names.shop_class_location_names.items():
                region_location_names.extend(shop_type_locs[shop_type][t])
            shop_region = create_region(world, active_locations, shop_name, region_location_names)
            shop_regions[shop_type].append(shop_region)
            created_shop_regions.append(shop_region)

    world.multiworld.regions.extend(created_shop_regions)


def connect_castle_regions(world: "HammerwatchWorld", gate_codes: typing.Dict[str, str]):
    used_names: typing.Dict[str, int] = {}
    gate_counts: typing.List[typing.Dict[str, int]]
    all_gate_counts: typing.Dict[str, int] = {
        item_name.key_bronze: 103,
        item_name.key_silver: 13,
        item_name.key_gold: 16,
    }
    prison_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_prison: 12,
        item_name.key_silver_prison: 2,
        item_name.key_gold_prison: 4,
    }
    armory_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_armory: 29,
        item_name.key_silver_armory: 3,
        item_name.key_gold_armory: 2,
    }
    archives_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_archives: 20,
        item_name.key_silver_archives: 5,
        item_name.key_gold_archives: 7,
    }
    chambers_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_chambers: 42,
        item_name.key_silver_chambers: 3,
        item_name.key_gold_chambers: 3,
    }

    if world.options.key_mode.value == world.options.key_mode.option_floor_master:
        key_bronze = [f"{castle_act_names[i//3]} Floor {i+1} Master Bronze Key" for i in range(12)]
        key_silver = [f"{castle_act_names[i//3]} Floor {i+1} Master Silver Key" for i in range(12)]
        key_gold = [f"{castle_act_names[i//3]} Floor {i+1} Master Gold Key" for i in range(12)]
        if world.options.randomize_bonus_keys == world.options.randomize_bonus_keys.option_true:
            key_bonus = [f"{castle_act_names[b]} Master Bonus Key" for b in range(4)]
        else:
            key_bonus = [f"{castle_act_names[b]} Bonus Key" for b in range(4)]
        gate_counts = [{key_bronze[i]: 999999999, key_silver[i]: 999999999, key_gold[i]: 999999999} for i in range(12)]
    elif world.options.key_mode.value == world.options.key_mode.option_act_specific:
        key_bronze = [f"{castle_act_names[i//3]} Bronze Key" for i in range(12)]
        key_silver = [f"{castle_act_names[i//3]} Silver Key" for i in range(12)]
        key_gold = [f"{castle_act_names[i//3]} Gold Key" for i in range(12)]
        key_bonus = [f"{castle_act_names[b]} Bonus Key" for b in range(4)]
        gate_counts = [
            prison_gate_items,
            prison_gate_items,
            prison_gate_items,
            armory_gate_items,
            armory_gate_items,
            armory_gate_items,
            archives_gate_items,
            archives_gate_items,
            archives_gate_items,
            chambers_gate_items,
            chambers_gate_items,
            chambers_gate_items,
        ]
    else:
        key_bronze = [item_name.key_bronze for _ in range(12)]
        key_silver = [item_name.key_silver for _ in range(12)]
        key_gold = [item_name.key_gold for _ in range(12)]
        key_bonus = [item_name.key_bonus for _ in range(4)]

        gate_counts = [all_gate_counts for _ in range(12)]

    buttonsanity = world.options.buttonsanity.value > 0
    buttonsanity_insanity = get_buttonsanity_insanity(world)
    rando_all_exits = world.options.exit_randomization.value == world.options.exit_randomization.option_all

    hammer_item = item_name.hammer
    hammer_item_count = world.options.hammer_fragments.value
    if hammer_item_count > 1:
        hammer_item = item_name.hammer_fragment

    # If not doing entrance randomization or randomizing the start we start in the normal spot
    if not world.options.exit_randomization.value or not world.options.random_start_exit.value:
        connect(world, used_names, castle_region_names.menu, castle_region_names.p1_start, False)
    connect(world, used_names, castle_region_names.p1_start, castle_region_names.hub, True)

    if world.options.open_castle.value:
        connect(world, used_names, castle_region_names.hub, castle_region_names.a1_start, True)
        connect(world, used_names, castle_region_names.hub, castle_region_names.r1_start, True)
        connect(world, used_names, castle_region_names.hub, castle_region_names.c1_start, True)

    # Prison Floor 1
    connect(world, used_names, castle_region_names.p1_start, castle_region_names.p1_nw,
            True, item_name.btnc_p1_floor, 1, False)
    connect(world, used_names, castle_region_names.p1_nw, castle_region_names.p1_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.p1_nw, castle_region_names.p1_nw_left, False)
    connect_gate(world, used_names, castle_region_names.p1_start, castle_region_names.p1_s,
                 key_bronze[0], gate_codes, gate_counts[0], gate_names.c_p1_0, True)
    connect_gate(world, used_names, castle_region_names.p1_s, castle_region_names.p1_sw_bronze_gate,
                 key_bronze[0], gate_codes, gate_counts[0], gate_names.c_p1_3, False)
    connect_gate(world, used_names, castle_region_names.p1_s, castle_region_names.p1_e,
                 key_bronze[0], gate_codes, gate_counts[0], gate_names.c_p1_2, True)
    connect_gate(world, used_names, castle_region_names.p1_e, castle_region_names.p1_m_bronze_gate,
                 key_bronze[0], gate_codes, gate_counts[0], gate_names.c_p1_1, False)
    connect_exit(world, used_names, castle_region_names.p1_e, castle_region_names.p2_start,
                 entrance_names.c_p2_0, entrance_names.c_p1_1)
    if world.options.shortcut_teleporter.value:
        connect_exit(world, used_names, castle_region_names.p1_nw_left, castle_region_names.p3_portal_from_p1,
                     entrance_names.c_p3_portal, entrance_names.c_p1_20)
        connect(world, used_names, castle_region_names.p3_portal_from_p1, castle_region_names.p3_n_gold_gate,
                False)

    # Prison Floor 2
    connect_gate(world, used_names, castle_region_names.p2_start, castle_region_names.p2_m,
                 key_bronze[1], gate_codes, gate_counts[1], gate_names.c_p2_0, True)
    connect_exit(world, used_names, castle_region_names.p2_m, castle_region_names.p1_from_p2,
                 entrance_names.c_p1_2, entrance_names.c_p2_1)
    connect_exit(world, used_names, castle_region_names.p1_from_p2, castle_region_names.p2_p1_return,
                 entrance_names.c_p2_2, entrance_names.c_p1_3)
    connect(world, used_names, castle_region_names.p2_p1_return, castle_region_names.p2_m, buttonsanity,
            item_name.btnc_p2_m_stairs, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.p2_m, castle_region_names.p2_n,
                 key_silver[1], gate_codes, gate_counts[1], gate_names.c_p2_5, True)
    if buttonsanity:
        p2_shortcut = connect(world, used_names, castle_region_names.p2_m, castle_region_names.p2_n, True)
        p2_shortcut_items = [
            item_name.btnc_p2_shortcut_n,
            item_name.btnc_p2_shortcut_s,
        ]
        add_rule(p2_shortcut, lambda state: state.has_all(p2_shortcut_items, world.player))
    if buttonsanity_insanity:
        connect(world, used_names, castle_region_names.p2_n, castle_region_names.p2_spike_puzzle_bottom, False,
                item_name.btnc_p2_spike_puzzle_r_part, 3, False, buttonsanity)
        connect(world, used_names, castle_region_names.p2_spike_puzzle_bottom, castle_region_names.p2_spike_puzzle_left,
                False, item_name.btnc_p2_spike_puzzle_b_part, 3, False, buttonsanity)
    else:
        connect(world, used_names, castle_region_names.p2_n, castle_region_names.p2_spike_puzzle_bottom, False,
                item_name.btnc_p2_spike_puzzle_r, 1, False, buttonsanity)
        connect(world, used_names, castle_region_names.p2_spike_puzzle_bottom, castle_region_names.p2_spike_puzzle_left,
                False, item_name.btnc_p2_spike_puzzle_b, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.p2_spike_puzzle_left, castle_region_names.p2_spike_puzzle_top, False)
    # The spike puzzle is passable, also the top buttons are technically useless
    connect(world, used_names, castle_region_names.p2_n, castle_region_names.p2_red_switch, True,
            item_name.btnc_p2_red_spikes, 1, False, buttonsanity)
    # Spikes passable
    connect(world, used_names, castle_region_names.p2_red_switch, castle_region_names.p2_ne_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.p2_ne_secret, castle_region_names.p2_puzzle, False,
            item_name.btnc_p2_puzzle, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.p2_red_switch, castle_region_names.p2_e_bronze_gate,
                 key_bronze[1], gate_codes, gate_counts[1], gate_names.c_p2_1, False)
    connect(world, used_names, castle_region_names.p2_red_switch, castle_region_names.p2_e_save, True,
            item_name.btnc_p2_e_save, 1, False, buttonsanity)
    if buttonsanity:
        connect(world, used_names, castle_region_names.p2_e_save, castle_region_names.p2_m, True,
                item_name.btnc_p2_e_save, 1, False)
    connect_gate(world, used_names, castle_region_names.p2_m, castle_region_names.p2_s,
                 key_gold[1], gate_codes, gate_counts[1], gate_names.c_p2_4, True)
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_e_bronze_gate_2,
                 key_bronze[1], gate_codes, gate_counts[1], gate_names.c_p2_7, False)
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_m_bronze_gate,
                 key_bronze[1], gate_codes, gate_counts[1], gate_names.c_p2_6, False)
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_se_bronze_gate,
                 key_bronze[1], gate_codes, gate_counts[1], gate_names.c_p2_2, False)
    if world.options.buttonsanity.value == world.options.buttonsanity.option_normal:
        connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_gg_room_reward,
                False, item_name.btnc_p2_rune_sequence, 1, False)
    else:
        connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_gg_room_reward,
                False, item_name.btnc_p2_rune_sequence_part, 4, False)
    connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_w_treasure, False,
            item_name.btnc_p2_open_w_jail, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_w_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.p2_w_treasure, castle_region_names.p2_w_treasure_tp, False,
            item_name.btnc_p2_tp_jail, 1, False, buttonsanity)
    if get_buttonsanity_insanity(world):
        connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_tp_puzzle, False,
                item_name.btnc_p2_tp_w_part, 4, False)
    else:
        connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_tp_puzzle, False,
                item_name.btnc_p2_tp_w, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_end,
                 key_gold[1], gate_codes, gate_counts[1], gate_names.c_p2_3, True)
    connect_exit(world, used_names, castle_region_names.p2_end, castle_region_names.p3_start_door,
                 entrance_names.c_p3_0, entrance_names.c_p2_3)

    # Prison Floor 3
    connect(world, used_names, castle_region_names.p3_start_door, castle_region_names.p3_start, buttonsanity,
            item_name.btnc_p3_start, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.p3_start, castle_region_names.p3_start_shop, False,
            item_name.btnc_p3_shop, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.p3_start, castle_region_names.p3_start_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.p3_start, castle_region_names.p3_nw_closed_room, False,
            item_name.btnc_p3_nw_room, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_nw_n_bronze_gate,
                 key_bronze[2], gate_codes, gate_counts[2], gate_names.c_p3_1, False)
    connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_nw_s_bronze_gate,
                 key_bronze[2], gate_codes, gate_counts[2], gate_names.c_p3_0, False)
    p3_sgate_entrs = connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_silver_gate,
                                  key_silver[2], gate_codes, gate_counts[2], gate_names.c_p3_3, True)
    if buttonsanity:
        for entr in p3_sgate_entrs:
            add_rule(entr, lambda state: state.has(item_name.btnc_p3_sgate_spikes, world.player), "and")
        connect(world, used_names, castle_region_names.p3_start, castle_region_names.p3_rspikes, True,
                item_name.btnc_p3_red_spikes, 1, False)
        connect(world, used_names, castle_region_names.p3_rspikes_room, castle_region_names.p3_start, True,
                item_name.btnc_p3_open_n_shortcut, 1, False)
    # Both sets of spikes passable
    connect_exit(world, used_names, castle_region_names.p3_silver_gate, castle_region_names.p1_from_p3_s,
                 entrance_names.c_p1_4, entrance_names.c_p3_1)
    connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_n_gold_gate,
                 key_gold[2], gate_codes, gate_counts[2], gate_names.c_p3_4, True)
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_rspikes, buttonsanity,
            item_name.btnc_p3_red_spikes, 1, False, buttonsanity)
    # Spikes passable
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_rspikes_room, buttonsanity,
            item_name.btnc_p3_open_n_shortcut, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_bspikes, buttonsanity,
            item_name.btnc_p3_blue_spikes, 1, False, buttonsanity)
    # Spikes passable
    if buttonsanity_insanity:
        connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_bonus, True,
                item_name.btnc_p3_open_bonus_part, 5, False)
        connect_exit(world, used_names, castle_region_names.p3_bonus, castle_region_names.n1_start,
                     entrance_names.c_n1_0, entrance_names.c_p3_b_ent,
                     item_name.btnc_p3_portal_part, 9, False)
    else:
        connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_bonus, buttonsanity,
                item_name.btnc_p3_open_bonus, 1, False, buttonsanity)
        if buttonsanity:
            connect_exit(world, used_names, castle_region_names.p3_bonus, castle_region_names.n1_start,
                         entrance_names.c_n1_0, entrance_names.c_p3_b_ent,
                         item_name.btnc_p3_portal, 1, False)
        else:
            connect_exit(world, used_names, castle_region_names.p3_bonus, castle_region_names.n1_start,
                         entrance_names.c_n1_0, entrance_names.c_p3_b_ent)
    if buttonsanity:
        connect(world, used_names, castle_region_names.p3_bonus, castle_region_names.p3_bspikes, True,
                item_name.btnc_p3_bonus_side, 1, False)
    connect_gate(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_s_bronze_gate,
                 key_bronze[2], gate_codes, gate_counts[2], gate_names.c_p3_2, False)
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_se_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_spikes_s, buttonsanity,
            item_name.btnc_p3_s_spikes, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.p3_spikes_s, castle_region_names.p3_m_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.p3_spikes_s, castle_region_names.p3_sw, buttonsanity,
            item_name.btnc_p3_s_spikes, 1, False, buttonsanity)
    # All three connections have spikes that can be passed
    connect(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_exit_s, buttonsanity,
            item_name.btnc_p3_s_exit_l, 1, False, buttonsanity)
    connect_exit(world, used_names, castle_region_names.p3_exit_s, castle_region_names.p1_from_p3_n,
                 entrance_names.c_p1_10, entrance_names.c_p3_10)
    connect(world, used_names, castle_region_names.p3_exit_s, castle_region_names.p3_n_gold_gate, buttonsanity,
            item_name.btnc_p3_s_exit_r, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_arrow_hall_secret,
            False, item_name.btnc_p3_e_passage, 1, False)
    connect(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_hidden_arrow_hall, False,
            item_name.btnc_p3_s_passage, 1, False)
    connect(world, used_names, castle_region_names.p3_hidden_arrow_hall, castle_region_names.p3_hidden_s_hall_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect_gate(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_s_gold_gate,
                 key_gold[2], gate_codes, gate_counts[2], gate_names.c_p3_5, False)
    if buttonsanity:
        connect(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_n_gold_gate, True,
                item_name.btnc_p3_sw_shortcut, 1, False)
        connect(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_boss, True,
                item_name.btnc_p3_boss_door, 1, False)
    else:
        connect_all(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_boss, True,
                    [item_name.btnc_b1_rune_1, item_name.btnc_b1_rune_2, item_name.btnc_b1_rune_3],
                    True)
    connect_exit(world, used_names, castle_region_names.p3_boss, castle_region_names.b1_start,
                 entrance_names.c_b1_0, entrance_names.c_p3_boss, None, 0, False,
                 rando_all_exits, True)

    # Prison Bonus
    connect_gate(world, used_names, castle_region_names.n1_start, castle_region_names.n1_room1, key_bonus[0])
    connect_gate(world, used_names, castle_region_names.n1_room1, castle_region_names.n1_room2, key_bonus[0])
    connect(world, used_names, castle_region_names.n1_room2, castle_region_names.n1_room2_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.n1_room2, castle_region_names.n1_room2_unlock, False,
            item_name.btnc_n1_cache_n, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.n1_room2, castle_region_names.n1_room3, key_bonus[0])
    connect(world, used_names, castle_region_names.n1_room3, castle_region_names.n1_room3_unlock, False,
            item_name.btnc_n1_cache_ne, 1, False, buttonsanity)
    connect_or(world, used_names, castle_region_names.n1_room3, castle_region_names.n1_room3_hall, False,
               [item_name.btnc_n1_hall_top, item_name.btnc_n1_hall_bottom], buttonsanity)
    connect_gate(world, used_names, castle_region_names.n1_room3_hall, castle_region_names.n1_room4, key_bonus[0])
    connect_gate(world, used_names, castle_region_names.n1_room4, castle_region_names.n1_exit, key_bonus[0])
    connect_exit(world, used_names, castle_region_names.n1_exit, castle_region_names.p3_bonus_return,
                 entrance_names.c_p3_b_return, None)
    connect(world, used_names, castle_region_names.p3_bonus_return, castle_region_names.p3_bonus, False)

    # Boss 1
    connect(world, used_names, castle_region_names.b1_start, castle_region_names.b1_arena, False,
            item_name.btnc_b1_pillars, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.b1_arena, castle_region_names.b1_defeated, False)
    # Technically only need 1 button functional for the fight to not be super terrible
    connect(world, used_names, castle_region_names.b1_defeated, castle_region_names.b1_exit, False)
    connect_exit(world, used_names, castle_region_names.b1_exit, castle_region_names.a1_start,
                 entrance_names.c_a1_0, entrance_names.c_b1_1)

    # Armory Floor 4
    connect(world, used_names, castle_region_names.a1_start, castle_region_names.a1_se, buttonsanity,
            item_name.btnc_a1_open_se_wall, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.a1_start, castle_region_names.a1_start_shop_w,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_3, False)
    connect_gate(world, used_names, castle_region_names.a1_start, castle_region_names.a1_start_shop_m,
                 key_gold[3], gate_codes, gate_counts[3], gate_names.c_a1_7, False)
    connect_gate(world, used_names, castle_region_names.a1_start, castle_region_names.a1_start_shop_e,
                 key_gold[3], gate_codes, gate_counts[3], gate_names.c_a1_8, False)
    connect_exit(world, used_names, castle_region_names.a1_start, castle_region_names.a2_start,
                 entrance_names.c_a2_0, entrance_names.c_a1_a2)
    connect_exit(world, used_names, castle_region_names.a1_start, castle_region_names.a3_start,
                 entrance_names.c_a3_0, entrance_names.c_a1_a3)
    if buttonsanity:
        connect(world, used_names, castle_region_names.a1_start, castle_region_names.a1_boss, True,
                item_name.btnc_a1_boss_door, 1, False)
    else:
        connect_all(world, used_names, castle_region_names.a1_start, castle_region_names.a1_boss, True,
                    [item_name.btnc_b2_rune_1, item_name.btnc_b2_rune_2, item_name.btnc_b2_rune_3],
                    True)
    connect_exit(world, used_names, castle_region_names.a1_boss, castle_region_names.b2_start,
                 entrance_names.c_b2_0, entrance_names.c_a1_boss, None, 0, False,
                 rando_all_exits, True)
    connect_gate(world, used_names, castle_region_names.a1_se, castle_region_names.a1_e,
                 key_silver[3], gate_codes, gate_counts[3], gate_names.c_a1_6, True)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_sw_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_12, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_s_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_4, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_se_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_5, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_e_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_14, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_ne_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_13, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_n_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_10, False)
    if buttonsanity:
        connect(world, used_names, castle_region_names.a1_e, castle_region_names.a1_rune_room, False,
                item_name.btnc_a1_open_se_rune, 1, False)
        if buttonsanity_insanity:
            connect(world, used_names, castle_region_names.a1_e_se_bgate, castle_region_names.a1_se_cache, False,
                    item_name.btnc_a1_open_se_cache_part, 4, False)
        else:
            connect(world, used_names, castle_region_names.a1_e_se_bgate, castle_region_names.a1_se_cache, False,
                    item_name.btnc_a1_open_se_cache, 1, False)
    else:
        connect(world, used_names, castle_region_names.a1_e_se_bgate, castle_region_names.a1_rune_room, False)
        connect(world, used_names, castle_region_names.a1_rune_room, castle_region_names.a1_se_cache, False)
    connect(world, used_names, castle_region_names.a1_e, castle_region_names.a1_red_spikes, False,
            item_name.btnc_a1_red_spikes, 1, False, buttonsanity)
    # Spikes passable
    connect(world, used_names, castle_region_names.a1_e, castle_region_names.a1_ne_cache, False,
            item_name.btnc_a1_open_ne_cache, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a1_e, castle_region_names.a1_tp_n, False,
            item_name.btnc_a1_tp_n, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_w,
                 key_silver[3], gate_codes, gate_counts[3], gate_names.c_a1_15, True)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_nw_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_0, True)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_ne_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_9, False)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_se_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_2, False)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_sw_bgate,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_1, False)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_sw_bgate_1,
                 key_bronze[3], gate_codes, gate_counts[3], gate_names.c_a1_11, False)
    connect(world, used_names, castle_region_names.a1_w, castle_region_names.a1_n_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.a1_n_secret, castle_region_names.a1_puzzle, False,
            item_name.btnc_a1_puzzle, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a1_w, castle_region_names.a1_n_bgate, buttonsanity,
            item_name.btnc_a1_open_m_cache, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a1_w, castle_region_names.a1_sw_spikes, buttonsanity,
            item_name.btnc_a1_sw_spikes, 1, False, buttonsanity)
    # Spikes passable
    if buttonsanity:
        connect(world, used_names, castle_region_names.a1_w, castle_region_names.a1_e, True,
                item_name.btnc_a1_m_shortcut, 1, False)
        connect(world, used_names, castle_region_names.a1_start, castle_region_names.a1_sw_spikes, False,
                item_name.btnc_a1_sw_spikes, 1, False)
        # Spikes passable

    # Armory Floor 5
    connect(world, used_names, castle_region_names.a2_start, castle_region_names.a2_tp_sw, False,
            item_name.btnc_a2_tp_sw, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a2_start, castle_region_names.a2_tp_se, False,
            item_name.btnc_a2_tp_se, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a2_start, castle_region_names.a2_s_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.a2_s_secret, castle_region_names.a2_puzzle, False,
            item_name.btnc_a2_puzzle, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_sw_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_3, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_s_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_4, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_se_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_5, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_s_save_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_10, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_ne,
                 key_silver[4], gate_codes, gate_counts[4], gate_names.c_a2_6, True)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_m_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_7, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_l_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_1, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_r_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_0, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_b_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_8, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_save_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_9, False)
    connect(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_tp_ne, False,
            item_name.btnc_a2_tp_ne, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_e, buttonsanity,
            item_name.btnc_a2_open_se_room_t, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_e, buttonsanity,
            item_name.btnc_a2_open_se_room_t, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.a2_e, castle_region_names.a2_e_bgate,
                 key_bronze[4], gate_codes, gate_counts[4], gate_names.c_a2_2, False)
    if buttonsanity:
        connect_exit(world, used_names, castle_region_names.a2_nw, castle_region_names.n2_start,
                     entrance_names.c_n2_0, entrance_names.c_a2_88,
                     item_name.btnc_a2_open_bonus, 1, False)
        connect(world, used_names, castle_region_names.a2_start, castle_region_names.a2_e, False,
                item_name.btnc_a2_open_se_room_l, 1, False)
    else:
        connect_exit(world, used_names, castle_region_names.a2_nw, castle_region_names.n2_start,
                     entrance_names.c_n2_0, entrance_names.c_a2_88)
    connect_exit(world, used_names, castle_region_names.a2_nw, castle_region_names.a1_from_a2,
                 entrance_names.c_a1_1, entrance_names.c_a2_1)
    connect(world, used_names, castle_region_names.a2_nw, castle_region_names.a2_blue_spikes, False,
            item_name.btnc_a2_blue_spikes, 1, False)
    # Spikes passable
    connect(world, used_names, castle_region_names.a2_blue_spikes, castle_region_names.a2_blue_spikes_tp, False,
            item_name.btnc_a2_bspikes_tp, 1, False)
    connect(world, used_names, castle_region_names.a2_nw, castle_region_names.a2_to_a3, True,
            item_name.btnc_a2_open_w_exit, 1, False, buttonsanity)
    connect_exit(world, used_names, castle_region_names.a2_to_a3, castle_region_names.a3_from_a2,
                 entrance_names.c_a3_1, entrance_names.c_a2_2)

    # Armory Bonus
    connect_gate(world, used_names, castle_region_names.n2_start, castle_region_names.n2_m, key_bonus[1])
    connect_gate(world, used_names, castle_region_names.n2_m, castle_region_names.n2_nw, key_bonus[1])
    connect_gate(world, used_names, castle_region_names.n2_m, castle_region_names.n2_n, key_bonus[1])
    connect_gate(world, used_names, castle_region_names.n2_m, castle_region_names.n2_e, key_bonus[1])
    connect_gate(world, used_names, castle_region_names.n2_m, castle_region_names.n2_s, key_bonus[1])
    connect_gate(world, used_names, castle_region_names.n2_m, castle_region_names.n2_w, key_bonus[1])
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_se, False,
            item_name.btnc_n2_open_se_room, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_ne, False,
            item_name.btnc_n2_open_ne_room, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_exit, False,
            item_name.btnc_n2_open_exit, 1, False, buttonsanity)
    connect_exit(world, used_names, castle_region_names.n2_exit, castle_region_names.a2_bonus_return,
                 entrance_names.c_a2_10, None)

    # Armory Floor 6
    connect_or(world, used_names, castle_region_names.a3_start, castle_region_names.a3_main, True,
               [item_name.btnc_a3_open_start_n, item_name.btnc_a3_open_start_e], buttonsanity)
    if buttonsanity_insanity:
        connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_knife_puzzle_reward, False,
                item_name.btnc_a3_open_knife_part, 5, False)
        connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_knife_reward_2, False,
                item_name.btnc_a3_open_knife_2_part, 2, False)
        connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_nw_stairs, True,
                item_name.btnc_a3_open_knife_2_part, 2, False)
    else:
        connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_knife_puzzle_reward, False,
                item_name.btnc_a3_open_knife, 1, False, buttonsanity)
        connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_knife_reward_2, False,
                item_name.btnc_a3_open_knife_2, 1, False, buttonsanity)
        connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_nw_stairs, buttonsanity,
                item_name.btnc_a3_open_knife_2, 1, False, buttonsanity)
    connect_exit(world, used_names, castle_region_names.a3_nw_stairs, castle_region_names.a2_nw,
                 entrance_names.c_a2_3, entrance_names.c_a3_2)
    connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_tp, False,
            item_name.btnc_a3_tp_m, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a3_from_a2, castle_region_names.a3_from_a2_wall, buttonsanity,
            item_name.btnc_a3_open_m_stairs, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.a3_from_a2_wall, castle_region_names.a3_main, buttonsanity,
            item_name.btnc_a3_open_m_stairs, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_w_b_bgate,
                 key_bronze[5], gate_codes, gate_counts[5], gate_names.c_a3_5, False)
    connect(world, used_names, castle_region_names.a3_w_b_bgate, castle_region_names.a3_w_b_bgate_tp, False,
            item_name.btnc_a3_bgate_tp, 1, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_w_t_bgate,
                 key_bronze[5], gate_codes, gate_counts[5], gate_names.c_a3_2, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_w_r_bgate,
                 key_bronze[5], gate_codes, gate_counts[5], gate_names.c_a3_4, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_n_l_bgate,
                 key_bronze[5], gate_codes, gate_counts[5], gate_names.c_a3_1, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_n_r_bgate,
                 key_bronze[5], gate_codes, gate_counts[5], gate_names.c_a3_0, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_e_l_bgate,
                 key_bronze[5], gate_codes, gate_counts[5], gate_names.c_a3_3, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_e_r_bgate,
                 key_bronze[5], gate_codes, gate_counts[5], gate_names.c_a3_6, False)

    # Boss 2
    connect(world, used_names, castle_region_names.b2_start, castle_region_names.b2_arena, False)
    connect(world, used_names, castle_region_names.b2_arena, castle_region_names.b2_defeated, False)
    connect(world, used_names, castle_region_names.b2_defeated, castle_region_names.b2_exit, False)
    connect_exit(world, used_names, castle_region_names.b2_exit, castle_region_names.r1_start,
                 entrance_names.c_r1_0, entrance_names.c_b2_1)

    # Archives Floor 7
    connect_gate(world, used_names, castle_region_names.r1_start, castle_region_names.r1_se_ggate,
                 key_gold[6], gate_codes, gate_counts[6], gate_names.c_r1_2, False)
    if buttonsanity:
        connect(world, used_names, castle_region_names.r1_start, castle_region_names.r1_e, True,
                item_name.btnc_r1_open_e_wall, 1, False)
        connect(world, used_names, castle_region_names.r1_start, castle_region_names.r1_se_wall, False,
                item_name.btnc_r1_open_se_room, 1, False)
        connect(world, used_names, castle_region_names.r1_e_n_bgate, castle_region_names.r1_nw, True,
                item_name.btnc_r1_open_n_wall, 1, False)
        connect(world, used_names, castle_region_names.r1_nw, castle_region_names.r1_sw, True,
                item_name.btnc_r1_open_w_wall, 1, False)
        connect(world, used_names, castle_region_names.r1_w_sgate, castle_region_names.r1_start_wall, False,
                item_name.btnc_r1_open_start_room, 1, False)
        connect(world, used_names, castle_region_names.r1_sw, castle_region_names.r1_exit_l, True,
                item_name.btnc_r1_open_l_exit, 1, False)
        connect(world, used_names, castle_region_names.r1_start, castle_region_names.r1_exit_l, True,
                item_name.btnc_r1_open_exits, 1, False)
        connect(world, used_names, castle_region_names.r1_start, castle_region_names.r1_exit_r, True,
                item_name.btnc_r1_open_exits, 1, False)
    else:
        connect(world, used_names, castle_region_names.r1_se_ggate, castle_region_names.r1_e, False)
        connect(world, used_names, castle_region_names.r1_e_sgate, castle_region_names.r1_se_wall, False)
        connect(world, used_names, castle_region_names.r1_ne_ggate, castle_region_names.r1_nw, False)
        connect(world, used_names, castle_region_names.r1_nw_ggate, castle_region_names.r1_sw, False)
        connect(world, used_names, castle_region_names.r1_w_sgate, castle_region_names.r1_start_wall, False)
        connect(world, used_names, castle_region_names.r1_sw_ggate, castle_region_names.r1_exit_l, False)
        connect(world, used_names, castle_region_names.r1_exit_l, castle_region_names.r1_exit_r, False)
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e_s_bgate,
                 key_bronze[6], gate_codes, gate_counts[6], gate_names.c_r1_5, False)
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e_sgate,
                 key_silver[6], gate_codes, gate_counts[6], gate_names.c_r1_7, False)
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e,
                 key_bronze[6], gate_codes, gate_counts[6], gate_names.c_r1_4, False)
    # Technically this also leads to e_n_bgate, but doing this should logically be equivalent (hopefully)
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e_n_bgate,
                 key_bronze[6], gate_codes, gate_counts[6], gate_names.c_r1_6, True)
    # Internal gate
    connect_gate(world, used_names, castle_region_names.r1_e_n_bgate, castle_region_names.r1_e_n_bgate,
                 key_bronze[6], gate_codes, gate_counts[6], gate_names.c_r1_3, False)
    connect_gate(world, used_names, castle_region_names.r1_e_n_bgate, castle_region_names.r1_ne_ggate,
                 key_gold[6], gate_codes, gate_counts[6], gate_names.c_r1_1, False)
    connect(world, used_names, castle_region_names.r1_nw, castle_region_names.r1_puzzle, False,
            item_name.btnc_r1_puzzle, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.r1_nw, castle_region_names.r1_nw_hidden, False,
            item_name.btnc_r1_open_nw_room, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.r1_nw_hidden, castle_region_names.r1_nw_ggate,
                 key_gold[6], gate_codes, gate_counts[6], gate_names.c_r1_0, False)
    connect_gate(world, used_names, castle_region_names.r1_sw, castle_region_names.r1_w_sgate,
                 key_silver[6], gate_codes, gate_counts[6], gate_names.c_r1_10, False)
    connect_gate(world, used_names, castle_region_names.r1_sw, castle_region_names.r1_sw_ggate,
                 key_gold[6], gate_codes, gate_counts[6], gate_names.c_r1_11, False)
    # Internal bronze gate
    r1_internals = [
        gate_names.c_r1_8,
        gate_names.c_r1_9,
    ]
    for gate in r1_internals:
        connect_gate(world, used_names, castle_region_names.r1_sw, castle_region_names.r1_sw,
                     key_bronze[6], gate_codes, gate_counts[6], gate, False)
    connect_exit(world, used_names, castle_region_names.r1_exit_l, castle_region_names.r2_start,
                 entrance_names.c_r2_0, entrance_names.c_r1_1)
    connect_exit(world, used_names, castle_region_names.r1_exit_r, castle_region_names.r2_bswitch,
                 entrance_names.c_r2_1, entrance_names.c_r1_2)

    # Archives Floor 8
    connect(world, used_names, castle_region_names.r2_start, castle_region_names.r2_m, buttonsanity,
            item_name.btnc_r2_open_start, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_w_bgate,
                 key_bronze[7], gate_codes, gate_counts[7], gate_names.c_r2_0, False)
    # Internal bronze gates
    r2_internals = [
        gate_names.c_r2_6,
        gate_names.c_r2_1,
        gate_names.c_r2_2,
        gate_names.c_r2_8,
        gate_names.c_r2_3,
    ]
    for gate in r2_internals:
        connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_m,
                     key_bronze[7], gate_codes, gate_counts[7], gate, False)
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_ggate,
                 key_gold[7], gate_codes, gate_counts[7], gate_names.c_r2_4, False)
    if buttonsanity:
        connect_or(world, used_names, castle_region_names.r2_m, castle_region_names.r2_e, False,
                   [item_name.btnc_r2_open_fire_t, item_name.btnc_r2_open_fire_b], True)
        connect(world, used_names, castle_region_names.r2_m, castle_region_names.r2_n, False,
                item_name.btnc_r2_open_bs_r, 1, False)
        connect(world, used_names, castle_region_names.r2_m, castle_region_names.r2_spike_island, True,
                item_name.btnc_r2_open_spikes_t, 1, False)
        connect_or(world, used_names, castle_region_names.r2_m, castle_region_names.r2_s, False,
                   [item_name.btnc_r2_open_s_r, item_name.btnc_r2_open_s_l], True)
        connect(world, used_names, castle_region_names.r2_s, castle_region_names.r2_sw_bridge, False,
                item_name.btnc_r2_light_bridge, 1, False)
        if buttonsanity_insanity:
            r2_puzzle_item = item_name.btnc_r2_open_puzzle_part
        else:
            r2_puzzle_item = item_name.btnc_r2_open_puzzle
        connect(world, used_names, castle_region_names.r2_s, castle_region_names.r2_puzzle_room, False,
                r2_puzzle_item, 1, False)
        connect(world, used_names, castle_region_names.r2_m, castle_region_names.r2_ggate, False,
                item_name.btnc_r2_open_exit, 1, False)
        connect(world, used_names, castle_region_names.r2_m, castle_region_names.r2_exit, False,
                item_name.btnc_r2_open_exit, 1, False)
    else:
        connect(world, used_names, castle_region_names.r2_m, castle_region_names.r2_e, False)
        connect(world, used_names, castle_region_names.r2_sgate, castle_region_names.r2_s, False)
        connect(world, used_names, castle_region_names.r2_spike_island, castle_region_names.r2_sw_bridge, False)
        connect(world, used_names, castle_region_names.r2_sw_secret, castle_region_names.r2_puzzle_room, False)
        connect(world, used_names, castle_region_names.r2_ggate, castle_region_names.r2_exit, False)
    connect(world, used_names, castle_region_names.r2_sw_bridge, castle_region_names.r2_sw_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_nw,
                 key_bronze[7], gate_codes, gate_counts[7], gate_names.c_r2_7, False)
    connect(world, used_names, castle_region_names.r2_nw, castle_region_names.r2_n, buttonsanity,
            item_name.btnc_r2_open_bs_l, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_sgate,
                 key_silver[7], gate_codes, gate_counts[7], gate_names.c_r2_5, False)
    connect(world, used_names, castle_region_names.r2_s, castle_region_names.r2_spike_island, buttonsanity,
            item_name.btnc_r2_open_spikes_l, 1, False, buttonsanity)
    # Spike turrets passable
    connect(world, used_names, castle_region_names.r2_puzzle_room, castle_region_names.r2_puzzle, False)
    connect(world, used_names, castle_region_names.r2_s, castle_region_names.r2_w, False,
            item_name.btnc_r2_open_s_l, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.r2_from_r3, castle_region_names.r2_ne_cache, False,
            item_name.btnc_r2_open_ne_cache, 1, False, buttonsanity)
    connect_exit(world, used_names, castle_region_names.r2_exit, castle_region_names.r3_main,
                 entrance_names.c_r3_0, entrance_names.c_r2_2)

    # Archives Floor 9
    connect_or(world, used_names, castle_region_names.r3_main, castle_region_names.r3_ne_room, False,
               [item_name.btnc_r3_open_ne_l, item_name.btnc_r3_open_ne_t], buttonsanity)
    connect_or(world, used_names, castle_region_names.r3_main, castle_region_names.r3_s_room, False,
               [item_name.btnc_r3_open_s_r, item_name.btnc_r3_open_s_t], buttonsanity)
    connect_gate(world, used_names, castle_region_names.r3_s_room, castle_region_names.r3_l_shop_sgate,
                 key_silver[8], gate_codes, gate_counts[8], gate_names.c_r3_5, False)
    connect_gate(world, used_names, castle_region_names.r3_s_room, castle_region_names.r3_r_shop_sgate,
                 key_silver[8], gate_codes, gate_counts[8], gate_names.c_r3_4, False)
    connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_se_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_boss_switch, False,
            item_name.btnc_r3_open_bs, 1, False, buttonsanity)
    if buttonsanity_insanity:
        connect(world, used_names, castle_region_names.r3_boss_switch, castle_region_names.r3_rune_room, False,
                item_name.btnc_r3_simon_room_part, 5, False, True)
        connect(world, used_names, castle_region_names.r3_boss_switch, castle_region_names.r3_bonus, False,
                item_name.btnc_r3_bonus_part, 6, False, True)
    else:
        connect(world, used_names, castle_region_names.r3_boss_switch, castle_region_names.r3_rune_room, False,
                item_name.btnc_r3_simon_room, 1, False, buttonsanity)
        if buttonsanity:
            connect(world, used_names, castle_region_names.r3_boss_switch, castle_region_names.r3_bonus, False,
                    item_name.btnc_r3_bonus, 1, False)
        else:
            connect(world, used_names, castle_region_names.r3_simon_says, castle_region_names.r3_bonus, False)
            # Symbolic entrance representing completing the Simon Says puzzle
    connect(world, used_names, castle_region_names.r3_rune_room, castle_region_names.r3_simon_says, False,
            item_name.btnc_r3_simon, 1, False, buttonsanity)
    connect_exit(world, used_names, castle_region_names.r3_bonus, castle_region_names.n3_main,
                 entrance_names.c_n3_0, None)  # entrance_names.c_r3_b_ent)
    # We can make this one-way because we can't get locked here
    connect_gate(world, used_names, castle_region_names.r3_main, castle_region_names.r3_sw_bgate,
                 key_bronze[8], gate_codes, gate_counts[8], gate_names.c_r3_1, False)
    connect(world, used_names, castle_region_names.r3_sw_bgate, castle_region_names.r3_sw_bgate_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    # Internal bronze gates
    r3_internals = [
        gate_names.c_r3_0,
        gate_names.c_r3_7,
        gate_names.c_r3_9,
        gate_names.c_r3_2,
        gate_names.c_r3_10,
        gate_names.c_r3_8,
    ]
    for gate in r3_internals:
        connect_gate(world, used_names, castle_region_names.r3_main, castle_region_names.r3_main,
                     key_bronze[8], gate_codes, gate_counts[8], gate, False)
    if buttonsanity:
        connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_passage_start, False,
                item_name.btnc_r3_passage, 1, False)
        connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_sw_wall_r, False,
                item_name.btnc_r3_sw_room, 1, False)
        connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_passage_room_1, False,
                item_name.btnc_r3_passage_room_1, 1, False)
        connect(world, used_names, castle_region_names.r3_passage_room_2, castle_region_names.r3_passage_spikes, True,
                item_name.btnc_r3_passage_room_2_spikes, 1, False)
        connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_passage_spikes, False,
                item_name.btnc_r3_passage_room_2_spikes, 1, False)
        # Spikes passable
        connect(world, used_names, castle_region_names.r3_passage_mid, castle_region_names.r3_passage_end, False,
                item_name.btnc_r3_passage_end, 1, False)
        connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_nw_tp, False,
                item_name.btnc_r3_tp_nw, 1, False)
        if buttonsanity_insanity:
            connect(world, used_names, castle_region_names.r3_bonus_return, castle_region_names.r3_bonus_return_bridge,
                    False, item_name.btnc_r3_bonus_bridge_part, 4, False)
        else:
            connect(world, used_names, castle_region_names.r3_bonus_return, castle_region_names.r3_bonus_return_bridge,
                    False, item_name.btnc_r3_bonus_bridge, 1, False)
    else:
        connect(world, used_names, castle_region_names.r3_sw_bgate_secret, castle_region_names.r3_passage_start, False)
        connect(world, used_names, castle_region_names.r3_sw_bgate, castle_region_names.r3_sw_wall_r, False)
        connect(world, used_names, castle_region_names.r3_passage_room_2, castle_region_names.r3_passage_spikes, False)
        # Spikes passable from main
        connect(world, used_names, castle_region_names.r3_passage_room_2, castle_region_names.r3_passage_end, False)
        connect(world, used_names, castle_region_names.r3_passage_end, castle_region_names.r3_nw_tp, False)
        connect(world, used_names, castle_region_names.r3_bonus_return, castle_region_names.r3_bonus_return_bridge,
                False)
    connect(world, used_names, castle_region_names.r3_passage_start, castle_region_names.r3_passage,
            buttonsanity, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.r3_passage, castle_region_names.r3_passage_mid,
            buttonsanity, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, castle_region_names.r3_passage, castle_region_names.r3_passage_room_1, False)
    connect(world, used_names, castle_region_names.r3_passage_mid, castle_region_names.r3_passage_room_2, buttonsanity,
            item_name.btnc_r3_passage_room_2, 1, False, buttonsanity)
    connect_exit(world, used_names, castle_region_names.r3_bonus_return, castle_region_names.r2_from_r3,
                 entrance_names.c_r2_200, entrance_names.c_r3_250)
    connect_gate(world, used_names, castle_region_names.r3_main, castle_region_names.r3_e_ggate,
                 key_gold[8], gate_codes, gate_counts[8], gate_names.c_r3_6, False)
    connect_gate(world, used_names, castle_region_names.r3_main, castle_region_names.r3_w_ggate,
                 key_gold[8], gate_codes, gate_counts[8], gate_names.c_r3_3, True)
    connect(world, used_names, castle_region_names.r3_w_ggate, castle_region_names.r3_exit, False,
            item_name.btnc_r3_open_exit, 1, False, buttonsanity)
    if buttonsanity:
        connect(world, used_names, castle_region_names.r3_exit, castle_region_names.r3_boss, True,
                item_name.btnc_r3_boss_door, 1, False)
    else:
        connect_all(world, used_names, castle_region_names.r3_exit, castle_region_names.r3_boss, True,
                    [item_name.btnc_b3_rune_1, item_name.btnc_b3_rune_2, item_name.btnc_b3_rune_3],
                    True)
    connect_exit(world, used_names, castle_region_names.r3_boss, castle_region_names.b3_start,
                 entrance_names.c_b3_0, entrance_names.c_r3_boss, None, 0, False,
                 rando_all_exits, True)

    # Archives Bonus
    connect_exit(world, used_names, castle_region_names.n3_main, castle_region_names.n3_tp_room,
                 entrance_names.c_n3_80, entrance_names.c_n3_12)
    connect_exit(world, used_names, castle_region_names.n3_main, castle_region_names.r3_bonus_return,
                 entrance_names.c_r3_b_return, None)
    # Internal bronze gates
    for i in range(3):
        connect_gate(world, used_names, castle_region_names.n3_main, castle_region_names.n3_main, key_bonus[2],
                     None, None, None, False)

    # Boss 3
    connect(world, used_names, castle_region_names.b3_start, castle_region_names.b3_arena, False)
    connect(world, used_names, castle_region_names.b3_arena, castle_region_names.b3_defeated, False)
    connect(world, used_names, castle_region_names.b3_defeated, castle_region_names.b3_exit, False)
    connect_exit(world, used_names, castle_region_names.b3_exit, castle_region_names.c1_start,
                 entrance_names.c_c1_0, entrance_names.c_b3_1)

    # Chambers Floor 10
    connect(world, used_names, castle_region_names.c1_start, castle_region_names.c1_n_spikes, False,
            item_name.btnc_c1_n_spikes, 1, False, buttonsanity)
    # Spikes passable
    connect(world, used_names, castle_region_names.c1_start, castle_region_names.c1_se_spikes, False,
            item_name.btnc_c1_red_spikes, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.c1_start, castle_region_names.c1_shop,
                 key_bronze[9], gate_codes, gate_counts[9], gate_names.c_c1_3, False)
    # Bronze gates with no checks
    c1_s_internals = [
        gate_names.c_c1_7,
        gate_names.c_c1_2,
        gate_names.c_c1_9,
        gate_names.c_c1_10,
        gate_names.c_c1_11,
    ]
    for gate in c1_s_internals:
        connect_gate(world, used_names, castle_region_names.c1_start, castle_region_names.c1_start,
                     key_bronze[9], gate_codes, gate_counts[9], gate, False)
    connect_gate(world, used_names, castle_region_names.c1_start, castle_region_names.c1_w,
                 key_gold[9], gate_codes, gate_counts[9], gate_names.c_c1_12, True)
    connect_gate(world, used_names, castle_region_names.c1_w, castle_region_names.c1_sgate,
                 key_silver[9], gate_codes, gate_counts[9], gate_names.c_c1_13, True)
    if buttonsanity:
        connect(world, used_names, castle_region_names.c1_w, castle_region_names.c1_prison_stairs, True,
                item_name.btnc_c1_sw_exit, 1, False)
    else:
        connect(world, used_names, castle_region_names.c1_sgate, castle_region_names.c1_prison_stairs, False)
    connect_exit(world, used_names, castle_region_names.c1_sgate, castle_region_names.c2_tp_island,
                 entrance_names.c_c2_50, None)
    connect_exit(world, used_names, castle_region_names.c1_tp_island, castle_region_names.c1_sgate,
                 entrance_names.c_c1_75, None)
    connect_exit(world, used_names, castle_region_names.c1_prison_stairs, castle_region_names.pstart_start,
                 entrance_names.c_p_return_0, entrance_names.c_c1_169)
    connect_gate(world, used_names, castle_region_names.c1_w, castle_region_names.c1_s_bgate,
                 key_bronze[9], gate_codes, gate_counts[9], gate_names.c_c1_6, buttonsanity)
    connect(world, used_names, castle_region_names.c1_s_bgate, castle_region_names.c1_start, buttonsanity,
            item_name.btnc_c1_s_shortcut, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.c1_s_bgate, castle_region_names.c1_ledge,
                 key_bronze[9], gate_codes, gate_counts[9], gate_names.c_c1_5, False)
    # Bronze gates with no checks
    c1_s_internals = [
        gate_names.c_c1_0,
        gate_names.c_c1_1,
        gate_names.c_c1_8,
        gate_names.c_c1_4,
    ]
    for gate in c1_s_internals:
        connect_gate(world, used_names, castle_region_names.c1_w, castle_region_names.c1_w,
                     key_bronze[9], gate_codes, gate_counts[9], gate, False)
    connect_exit(world, used_names, castle_region_names.c1_w, castle_region_names.c2_main,
                 entrance_names.c_c2_0, entrance_names.c_c1_100)

    # Prison Return
    if buttonsanity_insanity:
        connect(world, used_names, castle_region_names.pstart_start, castle_region_names.pstart_puzzle_island, False,
                item_name.btnc_pstart_bridge_part, 4, False)
    else:
        connect(world, used_names, castle_region_names.pstart_start, castle_region_names.pstart_puzzle_island, False,
                item_name.btnc_pstart_bridge, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.pstart_puzzle_island, castle_region_names.pstart_puzzle, False,
            item_name.btnc_pstart_puzzle, 1, False, buttonsanity)

    # Chambers Floor 11
    connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_sw_wall, False,
            item_name.btnc_c2_sw_room, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_wall, False,
            item_name.btnc_c2_w_shortcut, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.c2_w_shops_2, castle_region_names.c2_e_wall, buttonsanity,
            item_name.btnc_c2_e_shop, 1, False, buttonsanity)
    if buttonsanity_insanity:
        connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_spikes, False,
                item_name.btnc_c2_tp_spikes_part, 4, False)
        connect(world, used_names, castle_region_names.c2_n, castle_region_names.c2_bonus, True,
                item_name.btnc_c2_bonus_room_part, 5, False)
        connect_exit(world, used_names, castle_region_names.c2_bonus, castle_region_names.n4_main,
                     entrance_names.c_n4_0, entrance_names.c_c2_b_ent,
                     item_name.btnc_c2_bonus_part, 8, False)
    else:
        connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_spikes, False,
                item_name.btnc_c2_tp_spikes, 1, False, buttonsanity)
        connect(world, used_names, castle_region_names.c2_n, castle_region_names.c2_bonus, buttonsanity,
                item_name.btnc_c2_bonus_room, 1, False, buttonsanity)
        if buttonsanity:
            connect_exit(world, used_names, castle_region_names.c2_bonus, castle_region_names.n4_main,
                         entrance_names.c_n4_0, entrance_names.c_c2_b_ent,
                         item_name.btnc_c2_bonus, 1, False)
        else:
            connect_exit(world, used_names, castle_region_names.c2_bonus, castle_region_names.n4_main,
                         entrance_names.c_n4_0, entrance_names.c_c2_b_ent)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_shops_1,
                 key_silver[10], gate_codes, gate_counts[10], gate_names.c_c2_11, False)
    connect_gate(world, used_names, castle_region_names.c2_w_shops_3, castle_region_names.c2_w_shops_2,
                 key_silver[10], gate_codes, gate_counts[10], gate_names.c_c2_10, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_shops_3,
                 key_bronze[10], gate_codes, gate_counts[10], gate_names.c_c2_3, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_e_shops_1,
                 key_bronze[10], gate_codes, gate_counts[10], gate_names.c_c2_2, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_e_shops_2,
                 key_bronze[10], gate_codes, gate_counts[10], gate_names.c_c2_16, False)
    if buttonsanity:
        connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_e_wall, False,
                item_name.btnc_c2_e_shop, 1, False)
        connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_puzzle_room, False,
                item_name.btnc_c2_open_puzzle, 1, False)
    else:
        connect(world, used_names, castle_region_names.c2_e_shops_1, castle_region_names.c2_puzzle_room, False)
    connect(world, used_names, castle_region_names.c2_puzzle_room, castle_region_names.c2_puzzle, False,
            item_name.btnc_c2_puzzle, 1, False, buttonsanity)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_exit_bgate,
                 key_bronze[10], gate_codes, gate_counts[10], gate_names.c_c2_12, False)
    # Bronze gates with no checks
    c2_internals = [
        gate_names.c_c2_5,
        gate_names.c_c2_7,
        gate_names.c_c2_18,
        gate_names.c_c2_8,
        gate_names.c_c2_15,
        gate_names.c_c2_6,
        gate_names.c_c2_13,
        gate_names.c_c2_4,
        gate_names.c_c2_17,
        gate_names.c_c2_1,
        gate_names.c_c2_0,
        gate_names.c_c2_14,
    ]
    for gate in c2_internals:
        connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_main,
                     key_bronze[10], gate_codes, gate_counts[10], gate, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_n,
                 key_gold[10], gate_codes, gate_counts[10], gate_names.c_c2_9, True)
    connect(world, used_names, castle_region_names.c2_n, castle_region_names.c2_n_wall, False,
            item_name.btnc_c2_n_room, 1, False)
    connect(world, used_names, castle_region_names.c2_n, castle_region_names.c2_n_shops, True,
            item_name.btnc_c2_n_shops, 1, False)
    connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_n_shops, True,
            item_name.btnc_c2_n_shops, 1, False)
    connect_exit(world, used_names, castle_region_names.c2_main, castle_region_names.c3_start,
                 entrance_names.c_c3_0, entrance_names.c_c2_45)
    connect_exit(world, used_names, castle_region_names.c2_n, castle_region_names.c3_nw,
                 entrance_names.c_c3_54, entrance_names.c_c2_105)
    connect_exit(world, used_names, castle_region_names.c2_tp_island, castle_region_names.c1_tp_island,
                 entrance_names.c_c1_99, None)

    # Chambers Bonus
    connect_gate(world, used_names, castle_region_names.n4_main, castle_region_names.n4_nw, key_bonus[3])
    connect_gate(world, used_names, castle_region_names.n4_main, castle_region_names.n4_w, key_bonus[3])
    connect_gate(world, used_names, castle_region_names.n4_main, castle_region_names.n4_e, key_bonus[3])
    connect_gate(world, used_names, castle_region_names.n4_main, castle_region_names.n4_exit, key_bonus[3])
    connect_exit(world, used_names, castle_region_names.n4_exit, castle_region_names.c2_bonus_return,
                 entrance_names.c_c2_125, None)

    # Chambers Floor 12
    connect_gate(world, used_names, castle_region_names.c3_start, castle_region_names.c3_rspike_switch,
                 key_bronze[11], gate_codes, gate_counts[11], gate_names.c_c3_1, False)
    if buttonsanity:
        connect(world, used_names, castle_region_names.c3_start, castle_region_names.c3_rspikes, True,
                item_name.btnc_c3_red_spikes, 1, False)
    connect(world, used_names, castle_region_names.c3_rspike_switch, castle_region_names.c3_rspikes, buttonsanity,
            item_name.btnc_c3_red_spikes, 1, False, buttonsanity)
    # Spikes passable
    connect_gate(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_s_bgate,
                 key_bronze[11], gate_codes, gate_counts[11], gate_names.c_c3_8, False)
    connect_gate(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_m_shop,
                 key_bronze[11], gate_codes, gate_counts[11], gate_names.c_c3_5, False)
    connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_m_wall, False,
            item_name.btnc_c3_e_shortcut, 1, False, buttonsanity)
    connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_m_tp, False,
            item_name.btnc_c3_tp_m, 1, False, buttonsanity)
    # Bronze gates with no checks
    c3_s_internals = [
        gate_names.c_c3_6,
        gate_names.c_c3_12,
        gate_names.c_c3_11,
        gate_names.c_c3_3,
        gate_names.c_c3_4,
        gate_names.c_c3_13,
        gate_names.c_c3_7,
        gate_names.c_c3_14,
    ]
    for gate in c3_s_internals:
        connect_gate(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_rspikes,
                     key_bronze[11], gate_codes, gate_counts[11], gate, False)
    connect_gate(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_nw,
                 key_gold[11], gate_codes, gate_counts[11], gate_names.c_c3_9, True)
    # Bronze gates with no checks
    c3_n_internals = [
        gate_names.c_c3_2,
        gate_names.c_c3_0,
        gate_names.c_c3_10,
    ]
    for gate in c3_n_internals:
        connect_gate(world, used_names, castle_region_names.c3_nw, castle_region_names.c3_nw,
                     key_bronze[11], gate_codes, gate_counts[11], gate, False)
    if world.options.buttonsanity.value == world.options.buttonsanity.option_normal:
        connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_sw_hidden, buttonsanity,
                item_name.btnc_c3_sw_room, 1, False)
    else:
        connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_sw_hidden, buttonsanity,
                item_name.btnc_c3_sw_room_part, 6, False)
    if buttonsanity:
        connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_se_hidden, False,
                item_name.btnc_c3_open_s_hall, 1, False)
        connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_light_bridge, False,
                item_name.btnc_c3_open_w_room, 1, False)
    else:
        connect(world, used_names, castle_region_names.c3_sw_hidden, castle_region_names.c3_se_hidden, False)
        connect(world, used_names, castle_region_names.c3_se_hidden, castle_region_names.c3_light_bridge, False)
    connect_exit(world, used_names, castle_region_names.c3_sw_hidden, castle_region_names.c3_fire_floor,
                 entrance_names.c_c3_67, None)
    connect(world, used_names, castle_region_names.c3_fire_floor, castle_region_names.c3_fire_floor_tp, False,
            item_name.btnc_c3_tp_se, 1, False)
    connect_exit(world, used_names, castle_region_names.c3_fire_floor, castle_region_names.c2_c3_tp,
                 entrance_names.c_c2_77, None)
    connect_exit(world, used_names, castle_region_names.c2_c3_tp, castle_region_names.c3_c2_tp,
                 entrance_names.c_c3_156, None)
    connect(world, used_names, castle_region_names.c3_c2_tp, castle_region_names.c3_nw, False)
    connect(world, used_names, castle_region_names.c3_light_bridge, castle_region_names.c3_easter_egg,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)

    if buttonsanity_insanity:
        b4_runes_entr = connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_boss, False)
        b4_runes_entr_inv = connect(world, used_names, castle_region_names.c2_boss, castle_region_names.c2_main, False)
        rune_items = [
            item_name.btnc_b4_rune_1_part,
            item_name.btnc_b4_rune_2_part,
            item_name.btnc_b4_rune_3_part,
        ]
        add_rule(b4_runes_entr, lambda state: all(state.has(rune, world.player, 4) for rune in rune_items))
        add_rule(b4_runes_entr_inv, lambda state: all(state.has(rune, world.player, 4) for rune in rune_items))
    else:
        connect_all(world, used_names, castle_region_names.c2_main, castle_region_names.c2_boss, rando_all_exits,
                    [item_name.btnc_b4_rune_1, item_name.btnc_b4_rune_2, item_name.btnc_b4_rune_3],
                    True)

    # Boss 4
    connect_exit(world, used_names, castle_region_names.c2_boss, castle_region_names.b4_start,
                 entrance_names.c_b4_0, entrance_names.c_c2_boss,
                 None, 0, False, rando_all_exits, True)
    connect(world, used_names, castle_region_names.b4_start, castle_region_names.b4_defeated, False)

    # The escape sequence rooms aren't randomized, it makes the escape goal too easy!
    connect(world, used_names, castle_region_names.b4_defeated, castle_region_names.e1_main,
            False, item_name.plank, 12, False,
            get_goal_type(world) != GoalType.KillBosses)
    # Technically planks are consumed, but nothing else does so this is faster
    connect(world, used_names, castle_region_names.e1_main, castle_region_names.e2_main, False)
    connect(world, used_names, castle_region_names.e2_main, castle_region_names.e3_main, False)
    connect(world, used_names, castle_region_names.e3_main, castle_region_names.e4_main, False)
    connect(world, used_names, castle_region_names.e4_main, castle_region_names.escaped,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)


temple_regions: typing.Dict[str, typing.Optional[typing.List[str]]] = {
    temple_region_names.menu: None,
    temple_region_names.hub_main: [
        temple_location_names.hub_front_of_pof,
        temple_location_names.hub_behind_temple_entrance,
        temple_location_names.ev_planks,
    ],
    temple_region_names.hub_rocks: [
        temple_location_names.hub_behind_shops,
        temple_location_names.hub_on_rock,
        temple_location_names.hub_west_pyramid,
        temple_location_names.hub_rocks_south,
        temple_location_names.hub_field_south,
        temple_location_names.hub_field_nw,
        temple_location_names.hub_field_north,
        temple_location_names.btn_hub_pof_1,
        temple_location_names.btn_hub_pof_2,
        temple_location_names.btn_hub_pof_3,
        temple_location_names.btn_hub_pof_4,
        temple_location_names.btn_hub_pof,
    ],
    temple_region_names.hub_pyramid_of_fear: [
        temple_location_names.hub_pof_reward
    ],
    temple_region_names.library: None,
    temple_region_names.library_lobby: None,
    temple_region_names.cave_3_main: [
        temple_location_names.cave3_squire,
        temple_location_names.cave3_ne,
        temple_location_names.cave3_nw,
        temple_location_names.cave3_m,
        temple_location_names.cave3_half_bridge,
        temple_location_names.cave3_n,
        temple_location_names.c3_miniboss_tick_1,
        temple_location_names.c3_miniboss_tick_2,
        temple_location_names.c3_tower_plant_small_1,
        temple_location_names.c3_tower_plant_small_2,
        temple_location_names.c3_tower_plant_small_3,
        temple_location_names.c3_tower_plant_small_4,
        temple_location_names.c3_tower_plant_small_5,
        temple_location_names.c3_tower_plant_small_6,
        temple_location_names.btn_c3_bridge,
    ],
    temple_region_names.c3_main_secrets: [
        temple_location_names.cave3_guard,
        temple_location_names.cave3_secret_n,
        temple_location_names.cave3_secret_nw,
        temple_location_names.cave3_secret_s,
        temple_location_names.btn_c3_puzzle,
    ],
    temple_region_names.c3_puzzle: [
        temple_location_names.c3_puzzle_1,
        temple_location_names.c3_puzzle_2,
        temple_location_names.c3_puzzle_3,
        temple_location_names.c3_puzzle_4,
    ],
    temple_region_names.c3_e: [
        temple_location_names.cave3_outside_guard,
        temple_location_names.cave3_se,
        temple_location_names.c3_tower_plant,
        temple_location_names.c3_tower_plant_small_7,
        temple_location_names.c3_tower_plant_small_8,
        temple_location_names.ev_c3_portal,
    ],
    temple_region_names.c3_e_guard_secret: [
        temple_location_names.cave3_trapped_guard,
    ],
    temple_region_names.cave_3_fall: [
        temple_location_names.cave3_fall_nw,
        temple_location_names.cave3_fall_ne,
        temple_location_names.cave3_fall_sw,
        temple_location_names.cave3_fall_se,
        temple_location_names.btn_c3_floor_fall,
    ],
    temple_region_names.cave_3_fields: [
        temple_location_names.cave3_captain,
        temple_location_names.cave3_captain_dock,
    ],
    temple_region_names.c3_e_water: [
        temple_location_names.cave3_fields_r,
    ],
    temple_region_names.cave_3_portal: [
        temple_location_names.cave3_portal_l,
        temple_location_names.cave3_portal_r,
        temple_location_names.btn_c3_pof_1,
        temple_location_names.btn_c3_pof_2,
        temple_location_names.btn_c3_pof_3,
        temple_location_names.btn_c3_pof_4,
        temple_location_names.btn_c3_pof,
    ],
    temple_region_names.cave_3_secret: [
        temple_location_names.cave3_secret_1,
        temple_location_names.cave3_secret_2,
        temple_location_names.cave3_secret_3,
        temple_location_names.cave3_secret_4,
        temple_location_names.cave3_secret_5,
        temple_location_names.cave3_secret_6,
        temple_location_names.cave3_secret_7,
        temple_location_names.cave3_secret_8,
        temple_location_names.cave3_secret_9,
        temple_location_names.cave3_secret_10,
        temple_location_names.cave3_secret_11,
        temple_location_names.cave3_secret_12,
    ],
    temple_region_names.cave_2_main: [
        temple_location_names.cave2_nw_2,
        temple_location_names.cave2_double_bridge_r,
        temple_location_names.cave2_guard_s,
        temple_location_names.cave2_nw_3,
        temple_location_names.cave2_w_miniboss_4,
        temple_location_names.cave2_below_pumps_3,
        temple_location_names.cave2_nw_1,
        temple_location_names.cave2_pumps_n,
        temple_location_names.cave2_below_pumps_1,
        temple_location_names.cave2_below_pumps_2,
        temple_location_names.cave2_e_1,
        temple_location_names.cave2_e_2,
        temple_location_names.cave2_nw_4,
        temple_location_names.cave2_nw_5,
        temple_location_names.cave2_w_miniboss_3,
        temple_location_names.cave2_w_miniboss_2,
        temple_location_names.cave2_w_miniboss_1,
        temple_location_names.cave2_red_bridge_se_1,
        temple_location_names.cave2_red_bridge_se_2,
        temple_location_names.cave2_e_3,
        temple_location_names.cave2_e_4,
        temple_location_names.cave2_guard_n,
        temple_location_names.c2_miniboss_maggot_w_1,
        temple_location_names.c2_miniboss_maggot_w_2,
        temple_location_names.c2_miniboss_tick_1,
        temple_location_names.c2_miniboss_tick_2,
        temple_location_names.c2_tower_plant_1,
        temple_location_names.c2_tower_plant_3,
        temple_location_names.c2_tower_plant_small_1,
        temple_location_names.c2_tower_plant_small_2,
        temple_location_names.c2_tower_plant_small_3,
        temple_location_names.c2_tower_plant_small_4,
        temple_location_names.c2_tower_plant_small_5,
        temple_location_names.c2_tower_plant_small_6,
        temple_location_names.c2_tower_plant_small_7,
        temple_location_names.c2_tower_plant_small_8,
        temple_location_names.c2_tower_plant_small_9,
        temple_location_names.c2_tower_plant_small_11,
        temple_location_names.c2_tower_plant_small_12,
        temple_location_names.c2_tower_plant_small_13,
        temple_location_names.c2_tower_plant_small_14,
        temple_location_names.c2_tower_plant_small_15,
        temple_location_names.c2_tower_plant_small_17,
        temple_location_names.c2_tower_plant_small_18,
        temple_location_names.c2_tower_plant_small_20,
        temple_location_names.c2_tower_plant_small_21,
        temple_location_names.c2_tower_plant_small_23,
        temple_location_names.btn_c2_red,
        temple_location_names.btn_c2_green,
        temple_location_names.btn_c2_pumps,
        temple_location_names.ev_c2_portal,
    ],
    temple_region_names.c2_main_secrets: [
        temple_location_names.cave2_secret_ne,
        temple_location_names.cave2_secret_m,
        temple_location_names.cave2_guard,
    ],
    temple_region_names.cave_2_pumps: [
        temple_location_names.cave2_pumps_wall_r,
        temple_location_names.cave2_pumps_wall_l,
        temple_location_names.cave2_water_n_r_1,
        temple_location_names.cave2_water_n_l,
        temple_location_names.btn_c2_pof,
        temple_location_names.cave2_water_n_r_2,
        temple_location_names.cave2_water_s,
        temple_location_names.btn_c2_pof_1,
        temple_location_names.btn_c2_pof_2,
        temple_location_names.btn_c2_pof_3,
        temple_location_names.btn_c2_pof_4,
    ],
    temple_region_names.c2_red_bridge: [
        temple_location_names.cave2_red_bridge_1,
        temple_location_names.cave2_red_bridge_2,
        temple_location_names.cave2_red_bridge_3,
        temple_location_names.cave2_red_bridge_4,
    ],
    temple_region_names.c2_green_bridge: [
        temple_location_names.cave2_green_bridge,
    ],
    temple_region_names.c2_double_bridge: [
        temple_location_names.cave2_double_bridge_m,
    ],
    temple_region_names.c2_sw: [
        temple_location_names.cave2_sw_hidden_room_1,
        temple_location_names.cave2_sw_hidden_room_2,
        temple_location_names.cave2_sw_hidden_room_3,
        temple_location_names.cave2_sw_hidden_room_4,
        temple_location_names.cave2_double_bridge_l_1,
        temple_location_names.cave2_double_bridge_l_2,
        temple_location_names.cave2_sw,
        temple_location_names.c2_miniboss_maggot_s_1,
        temple_location_names.c2_miniboss_maggot_s_2,
        temple_location_names.c2_tower_plant_2,
        temple_location_names.c2_tower_plant_small_10,
        temple_location_names.c2_tower_plant_small_16,
        temple_location_names.c2_tower_plant_small_19,
        temple_location_names.c2_tower_plant_small_22,
        temple_location_names.btn_c2_s_bridge,
    ],
    temple_region_names.c2_sw_secrets: [
        temple_location_names.cave2_secret_w,
        temple_location_names.cave2_double_bridge_secret,
        temple_location_names.btn_c2_puzzle,
        temple_location_names.btn_c2_bridges,
    ],
    temple_region_names.c2_puzzle: [
        temple_location_names.c2_puzzle_1,
        temple_location_names.c2_puzzle_2,
        temple_location_names.c2_puzzle_3,
        temple_location_names.c2_puzzle_4,
    ],
    temple_region_names.cave_1_main: [
        temple_location_names.cave1_n_3,
        temple_location_names.cave1_w_by_water_2,
        temple_location_names.cave1_s_3,
        temple_location_names.cave1_m,
        temple_location_names.cave1_double_room_l,
        temple_location_names.cave1_double_room_r,
        temple_location_names.cave1_n_1,
        temple_location_names.cave1_n_2,
        temple_location_names.cave1_w_1,
        temple_location_names.cave1_w_2,
        temple_location_names.cave1_s_4,
        temple_location_names.cave1_s_5,
        temple_location_names.cave1_n_room_1,
        temple_location_names.cave1_n_room_2,
        temple_location_names.cave1_n_room_3,
        temple_location_names.cave1_n_room_4,
        temple_location_names.cave1_s_1,
        temple_location_names.cave1_s_2,
        temple_location_names.cave1_w_by_water_1,
        temple_location_names.c1_miniboss_maggot_s_1,
        temple_location_names.c1_miniboss_maggot_s_2,
        temple_location_names.c1_miniboss_tick_1,
        temple_location_names.c1_miniboss_tick_2,
        temple_location_names.c1_tower_plant_1,
        temple_location_names.c1_tower_plant_3,
        temple_location_names.c1_tower_plant_small_5,
        temple_location_names.c1_tower_plant_small_6,
        temple_location_names.c1_tower_plant_small_7,
        temple_location_names.c1_tower_plant_small_8,
        temple_location_names.c1_tower_plant_small_11,
        temple_location_names.c1_tower_plant_small_12,
        temple_location_names.btn_c1_blue,
    ],
    temple_region_names.c1_main_secrets: [
        temple_location_names.cave1_secret_nw,
        temple_location_names.cave1_secret_w,
        temple_location_names.cave1_secret_m,
        temple_location_names.btn_c1_puzzle_w,
    ],
    temple_region_names.c1_n_puzzle: [
        temple_location_names.c1_n_puzzle_1,
        temple_location_names.c1_n_puzzle_2,
        temple_location_names.c1_n_puzzle_3,
        temple_location_names.c1_n_puzzle_4,
    ],
    temple_region_names.cave_1_blue_bridge: [
        temple_location_names.cave1_ne_hidden_room_1,
        temple_location_names.cave1_ne_hidden_room_2,
        temple_location_names.cave1_ne_hidden_room_3,
        temple_location_names.cave1_ne_hidden_room_4,
        temple_location_names.cave1_ne_hidden_room_5,
        temple_location_names.cave1_ne_grubs,
        temple_location_names.cave1_n_bridges_1,
        temple_location_names.cave1_n_bridges_4,
        temple_location_names.cave1_n_bridges_5,
        temple_location_names.cave1_ne_1,
        temple_location_names.cave1_ne_2,
        temple_location_names.cave1_ne_3,
        temple_location_names.cave1_ne_4,
        temple_location_names.cave1_ne_5,
        temple_location_names.cave1_n_bridges_2,
        temple_location_names.cave1_n_bridges_3,
        temple_location_names.c1_miniboss_maggot_ne_1,
        temple_location_names.c1_miniboss_maggot_ne_2,
        temple_location_names.c1_tower_plant_2,
        temple_location_names.c1_tower_plant_4,
        temple_location_names.c1_tower_plant_small_1,
        temple_location_names.c1_tower_plant_small_2,
        temple_location_names.c1_tower_plant_small_3,
        temple_location_names.c1_tower_plant_small_4,
        temple_location_names.c1_tower_plant_small_9,
        temple_location_names.c1_tower_plant_small_10,
        temple_location_names.c1_tower_plant_small_13,
        temple_location_names.c1_tower_plant_small_14,
        temple_location_names.btn_c1_red,
        temple_location_names.btn_c1_pof_1,
        temple_location_names.btn_c1_pof_2,
        temple_location_names.btn_c1_pof_3,
        temple_location_names.btn_c1_pof_4,
        temple_location_names.btn_c1_wall,
        temple_location_names.btn_c1_pof,
    ],
    temple_region_names.c1_blue_bridge_secrets: [
        temple_location_names.cave1_secret_n_hidden_room,
        temple_location_names.cave1_secret_ne,
    ],
    temple_region_names.c1_secret_hall: [
        temple_location_names.cave1_secret_tunnel_1,
        temple_location_names.cave1_secret_tunnel_2,
        temple_location_names.cave1_secret_tunnel_3,
    ],
    temple_region_names.cave_1_red_bridge: [
        temple_location_names.cave1_e_2,
        temple_location_names.cave1_e_3,
        temple_location_names.cave1_red_bridge_e,
        temple_location_names.cave1_se_1,
        temple_location_names.cave1_se_2,
        temple_location_names.cave1_e_1,
    ],
    temple_region_names.c1_red_bridge_secrets: [
        temple_location_names.cave1_secret_e,
        temple_location_names.btn_c1_puzzle_e,
    ],
    temple_region_names.c1_e_puzzle: [
        temple_location_names.c1_e_puzzle_1,
        temple_location_names.c1_e_puzzle_2,
        temple_location_names.c1_e_puzzle_3,
        temple_location_names.c1_e_puzzle_4,
    ],
    temple_region_names.cave_1_green_bridge: [
        temple_location_names.cave1_green_bridge_1,
        temple_location_names.cave1_green_bridge_2,
    ],
    temple_region_names.c1_storage_island: [
        temple_location_names.cave1_krilith_ledge_n,
        temple_location_names.cave1_krilith_ledge_e,
        temple_location_names.cave1_krilith_door,
    ],
    temple_region_names.cave_1_pumps: [
        temple_location_names.cave1_water_s_shore,
        temple_location_names.cave1_water_s_1,
        temple_location_names.cave1_water_s_2,
        temple_location_names.cave1_water_s_3,
        temple_location_names.cave1_water_s_4,
        temple_location_names.cave1_water_s_5,
        temple_location_names.btn_c1_green,
    ],
    temple_region_names.cave_1_temple: [
        temple_location_names.cave1_temple_hall_1,
        temple_location_names.cave1_temple_hall_2,
        temple_location_names.cave1_temple_hall_3,
        temple_location_names.cave1_temple_end_2,
        temple_location_names.cave1_temple_end_3,
        temple_location_names.cave1_temple_end_4,
        temple_location_names.cave1_temple_end_1,
    ],
    temple_region_names.boss_1_entrance: [
        temple_location_names.boss1_guard_l,
        temple_location_names.boss1_guard_r_1,
        temple_location_names.boss1_guard_r_2,
    ],
    temple_region_names.boss_1_arena: None,
    temple_region_names.boss_1_defeated: [
        temple_location_names.b1_boss_worm_1_1,
        temple_location_names.b1_boss_worm_1_2,
        temple_location_names.b1_boss_worm_2_1,
        temple_location_names.b1_boss_worm_2_2,
        temple_location_names.b1_boss_worm_3_1,
        temple_location_names.b1_boss_worm_3_2,
        temple_location_names.b1_boss_worm_4_1,
        temple_location_names.b1_boss_worm_4_2,
        temple_location_names.b1_boss_worm_key,
        temple_location_names.ev_beat_boss_1,
    ],
    temple_region_names.b1_back: [
        temple_location_names.boss1_bridge,
        temple_location_names.boss1_bridge_n,
        temple_location_names.btn_b1_bridge,
    ],
    temple_region_names.b1_back_secret: [
        temple_location_names.boss1_secret,
    ],
    temple_region_names.passage_entrance: None,
    temple_region_names.passage_entrance_secret: [
        temple_location_names.p_ent2_secret,
    ],
    temple_region_names.passage_mid: [
        temple_location_names.p_mid1_1,
        temple_location_names.p_mid1_2,
        temple_location_names.p_mid2_1,
        temple_location_names.p_mid2_2,
        temple_location_names.p_mid2_3,
        temple_location_names.p_mid2_4,
        temple_location_names.p_mid4_1,
        temple_location_names.p_mid4_2,
        temple_location_names.p_mid4_3,
        temple_location_names.p_mid4_4,
        temple_location_names.p_mid5_1,
        temple_location_names.p_mid5_2,
        temple_location_names.p_tower_plant_small_1,
        temple_location_names.p_tower_plant_small_2,
        temple_location_names.p_tower_plant_small_3,
        temple_location_names.p_tower_plant_small_4,
        temple_location_names.p_tower_plant_small_5,
        temple_location_names.p_tower_plant_small_6,
    ],
    temple_region_names.passage_mid_secrets: [
        temple_location_names.p_mid3_secret_1,
        temple_location_names.p_mid3_secret_2,
        temple_location_names.p_mid3_secret_3,
        temple_location_names.p_mid3_secret_4,
        temple_location_names.p_mid5_secret,
        temple_location_names.btn_p_puzzle,
    ],
    temple_region_names.passage_puzzle: [
        temple_location_names.p_puzzle_1,
        temple_location_names.p_puzzle_2,
        temple_location_names.p_puzzle_3,
        temple_location_names.p_puzzle_4,
    ],
    temple_region_names.passage_end: [
        temple_location_names.p_end3_1,
        temple_location_names.p_end3_2,
    ],
    temple_region_names.passage_end_secret: [
        temple_location_names.p_end1_secret,
    ],
    temple_region_names.temple_entrance: None,
    temple_region_names.temple_entrance_back: [
        temple_location_names.temple_entrance_l,
        temple_location_names.temple_entrance_r,
        temple_location_names.ev_temple_entrance_rock,
    ],
    temple_region_names.t1_main: [
        temple_location_names.t1_above_s_bridge,
        temple_location_names.t1_s_bridge_1,
        temple_location_names.t1_s_bridge_2,
        temple_location_names.t1_s_bridge_3,
        temple_location_names.t1_s_bridge_4,
        temple_location_names.t1_s_bridge_5,
        temple_location_names.t1_s_bridge_6,
        temple_location_names.t1_sw_sun_room_1,
        temple_location_names.t1_sw_sun_room_2,
        temple_location_names.t1_sw_corner_room,
        temple_location_names.t1_sw_hidden_room_1,
        temple_location_names.t1_sw_hidden_room_2,
        temple_location_names.t1_sw_hidden_room_3,
        temple_location_names.t1_sw_hidden_room_4,
        temple_location_names.btn_t1_wall_guard,
    ],
    temple_region_names.t1_main_secret: [
        temple_location_names.btn_t1_puzzle_w,
    ],
    temple_region_names.t1_w_puzzle: [
        temple_location_names.t1_w_puzzle_1,
        temple_location_names.t1_w_puzzle_2,
        temple_location_names.t1_w_puzzle_3,
        temple_location_names.t1_w_puzzle_4,
    ],
    temple_region_names.t1_sw_sdoor: [
        temple_location_names.t1_sw_sdoor_1,
        temple_location_names.t1_sw_sdoor_2,
        temple_location_names.t1_sw_sdoor_3,
        temple_location_names.t1_sw_sdoor_4,
        temple_location_names.t1_sw_sdoor_5,
    ],
    temple_region_names.t1_node_1: [
        temple_location_names.ev_t1_s_node,
    ],
    temple_region_names.t1_w: [
        temple_location_names.t1_double_gate_1,
        temple_location_names.t1_double_gate_2,
        temple_location_names.t1_double_gate_3,
        temple_location_names.t1_double_gate_hidden,
        temple_location_names.t1_behind_bars_entrance,
        temple_location_names.t1_e_of_double_gate_room_1,
        temple_location_names.t1_e_of_double_gate_room_2,
        temple_location_names.t1_e_of_double_gate_room_3,
        temple_location_names.t1_e_of_double_gate_room_4,
        temple_location_names.t1_mana_drain_fire_trap,
        temple_location_names.t1_mana_drain_fire_trap_reward_1,
        temple_location_names.t1_mana_drain_fire_trap_reward_2,
        temple_location_names.btn_t1_wall_runway,
    ],
    temple_region_names.t1_runway_halls: [
        temple_location_names.t1_mana_drain_fire_trap_passage,
    ],
    temple_region_names.t1_sun_turret: [
        temple_location_names.t1_double_gate_behind_block,
        temple_location_names.t1_s_of_sun_turret,
        temple_location_names.t1_sun_turret_1,
        temple_location_names.t1_sun_turret_2,
        temple_location_names.t1_sun_turret_3,
        temple_location_names.t1_fire_trap_by_sun_turret_1,
        temple_location_names.t1_fire_trap_by_sun_turret_2,
        temple_location_names.t1_fire_trap_by_sun_turret_3,
        temple_location_names.t1_fire_trap_by_sun_turret_4,
        temple_location_names.t1_tower_fire,
    ],
    temple_region_names.t1_ice_turret: [
        temple_location_names.t1_ice_turret_1,
        temple_location_names.t1_ice_turret_2,
        temple_location_names.t1_boulder_hallway_by_ice_turret_1,
        temple_location_names.t1_boulder_hallway_by_ice_turret_2,
        temple_location_names.t1_boulder_hallway_by_ice_turret_3,
        temple_location_names.t1_boulder_hallway_by_ice_turret_4,
        temple_location_names.t1_ice_turret_boulder_break_block,
        temple_location_names.t1_n_sunbeam,
        temple_location_names.t1_n_sunbeam_treasure_1,
        temple_location_names.t1_n_sunbeam_treasure_2,
        temple_location_names.t1_n_sunbeam_treasure_3,
        temple_location_names.t1_tower_ice,
        temple_location_names.ev_t1_n_node_n_mirrors,
    ],
    temple_region_names.t1_telarian: [
        temple_location_names.t1_telarian_1,
        temple_location_names.t1_telarian_2,
        temple_location_names.t1_telarian_3,
        temple_location_names.t1_telarian_4,
        temple_location_names.t1_telarian_5,
        temple_location_names.btn_t1_wall_telarian,
    ],
    temple_region_names.t1_n_of_ice_turret: [
        temple_location_names.t1_n_cache_by_ice_turret_1,
        temple_location_names.t1_n_cache_by_ice_turret_2,
        temple_location_names.t1_n_cache_by_ice_turret_3,
        temple_location_names.t1_n_cache_by_ice_turret_4,
        temple_location_names.t1_n_cache_by_ice_turret_5,
        temple_location_names.btn_t1_wall_n_jail,
    ],
    temple_region_names.t1_s_of_ice_turret: [
        temple_location_names.t1_s_cache_by_ice_turret_1,
        temple_location_names.t1_s_cache_by_ice_turret_2,
        temple_location_names.t1_s_cache_by_ice_turret_3,
    ],
    temple_region_names.t1_east: [
        temple_location_names.t1_ledge_after_block_trap_1,
        temple_location_names.t1_ledge_after_block_trap_2,
        temple_location_names.t1_ice_block_chamber_1,
        temple_location_names.t1_ice_block_chamber_2,
        temple_location_names.t1_ice_block_chamber_3,
        temple_location_names.t1_node_2_1,
        temple_location_names.t1_node_2_2,
        temple_location_names.btn_t1_pof,
        temple_location_names.t1_miniboss_mummy_1,
        temple_location_names.t1_miniboss_mummy_2,
        temple_location_names.btn_t1_pof_1,
        temple_location_names.btn_t1_pof_2,
        temple_location_names.btn_t1_pof_3,
        temple_location_names.btn_t1_pof_4,
        temple_location_names.btn_t1_wall_n_hall,
        temple_location_names.btn_t1_wall_e_jail,
        temple_location_names.ev_t1_n_node_s_mirror,
    ],
    temple_region_names.t1_e_secret: [
        temple_location_names.btn_t1_puzzle_e,
    ],
    temple_region_names.t1_ne_hall: [
        temple_location_names.t1_node_2_passage_1,
        temple_location_names.t1_node_2_passage_2,
        temple_location_names.t1_node_2_passage_3,
    ],
    temple_region_names.t1_e_puzzle: [
        temple_location_names.t1_e_puzzle_1,
        temple_location_names.t1_e_puzzle_2,
        temple_location_names.t1_e_puzzle_3,
        temple_location_names.t1_e_puzzle_4,
    ],
    temple_region_names.t1_jail_e: [
        temple_location_names.t1_e_gold_beetles,
    ],
    temple_region_names.t1_sun_block_hall: [
        temple_location_names.t1_sun_block_hall_1,
        temple_location_names.t1_sun_block_hall_2,
        temple_location_names.t1_sun_block_hall_3,
        temple_location_names.t1_sun_block_hall_4,
    ],
    temple_region_names.t1_node_2: [
        temple_location_names.ev_t1_n_node,
    ],
    temple_region_names.t1_telarian_melt_ice: [
        temple_location_names.t1_telarian_ice,
    ],
    temple_region_names.t1_ice_chamber_melt_ice: [
        temple_location_names.t1_ice_block_chamber_ice,
    ],
    temple_region_names.boss2_main: None,
    temple_region_names.boss2_defeated: [
        temple_location_names.boss2_nw,
        temple_location_names.boss2_se,
        temple_location_names.ev_beat_boss_2,
    ],
    temple_region_names.t2_main: [
        temple_location_names.t2_n_of_portal,
        temple_location_names.t2_s_of_portal,
        temple_location_names.t2_w_spike_trap_1,
        temple_location_names.t2_w_spike_trap_2,
        temple_location_names.t2_nw_puzzle_cache_1,
        temple_location_names.t2_nw_puzzle_cache_2,
        temple_location_names.t2_nw_puzzle_cache_3,
        temple_location_names.t2_nw_puzzle_cache_4,
        temple_location_names.t2_nw_puzzle_cache_5,
        temple_location_names.t2_nw_of_s_ice_turret,
        temple_location_names.t2_w_hall_dead_end_1,
        temple_location_names.t2_w_hall_dead_end_2,
        temple_location_names.t2_w_hall_dead_end_3,
        temple_location_names.t2_w_hall_dead_end_4,
        temple_location_names.t2_w_hall_dead_end_5,
        temple_location_names.t2_n_of_sw_gate_1,
        temple_location_names.t2_n_of_sw_gate_2,
        temple_location_names.t2_fire_trap_maze_1,
        temple_location_names.t2_fire_trap_maze_2,
        temple_location_names.t2_fire_trap_maze_3,
        temple_location_names.t2_fire_trap_maze_4,
        temple_location_names.t2_fire_trap_maze_5,
        temple_location_names.t2_fire_trap_maze_6,
        temple_location_names.t2_teleporter,
        temple_location_names.t2_e_outside_gold_beetle_cage_1,
        temple_location_names.t2_e_outside_gold_beetle_cage_2,
        temple_location_names.t2_boulder_chamber_1,
        temple_location_names.t2_boulder_chamber_2,
        temple_location_names.t2_boulder_chamber_3,
        temple_location_names.t2_boulder_chamber_4,
        temple_location_names.t2_s_balcony_1,
        temple_location_names.t2_s_balcony_2,
        temple_location_names.t2_se_banner_chamber_1,
        temple_location_names.t2_se_banner_chamber_2,
        temple_location_names.t2_se_banner_chamber_3,
        temple_location_names.t2_se_banner_chamber_4,
        temple_location_names.t2_se_banner_chamber_5,
        temple_location_names.t2_se_fireball_hall,
        temple_location_names.btn_t2_runes,
        temple_location_names.btn_t2_rune_e,
        temple_location_names.btn_t2_rune_se,
        temple_location_names.btn_t2_wall_w_ice_gate,
        temple_location_names.btn_t2_wall_e_ice_gate,
        temple_location_names.btn_t2_wall_jail_e,
        temple_location_names.btn_t2_portal,
        temple_location_names.btn_t2_wall_portal_w,
        temple_location_names.btn_t2_wall_portal_e,
        temple_location_names.t2_miniboss_mummy_e_1,
        temple_location_names.t2_miniboss_mummy_e_2,
        temple_location_names.t2_miniboss_mummy_w_1,
        temple_location_names.t2_miniboss_mummy_w_2,
        temple_location_names.t2_tower_fire,
        temple_location_names.t2_tower_ice_3,
        temple_location_names.t2_tower_mana_1,
        temple_location_names.t2_tower_mana_2,
    ],
    temple_region_names.t2_main_secrets: [
        temple_location_names.btn_t2_puzzle_w,
        temple_location_names.btn_t2_puzzle_e,
    ],
    temple_region_names.t2_nw_puzzle: [
        temple_location_names.t2_nw_puzzle_1,
        temple_location_names.t2_nw_puzzle_2,
        temple_location_names.t2_nw_puzzle_3,
        temple_location_names.t2_nw_puzzle_4,
    ],
    temple_region_names.t2_e_puzzle: [
        temple_location_names.t2_e_puzzle_1,
        temple_location_names.t2_e_puzzle_2,
        temple_location_names.t2_e_puzzle_3,
        temple_location_names.t2_e_puzzle_4,
    ],
    temple_region_names.t2_melt_ice: None,
    temple_region_names.t2_w_ice_gate: [
        temple_location_names.t2_w_ice_block_gate,
    ],
    temple_region_names.t2_e_ice_gate: [
        temple_location_names.t2_e_ice_block_gate,
    ],
    temple_region_names.t2_n_gate: [
        temple_location_names.t2_nw_ice_turret_1,
        temple_location_names.t2_nw_ice_turret_2,
        temple_location_names.t2_nw_ice_turret_3,
        temple_location_names.t2_nw_ice_turret_4,
        temple_location_names.t2_nw_under_block,
        temple_location_names.t2_nw_gate_3,
        temple_location_names.t2_tower_ice_1,
        temple_location_names.t2_tower_ice_2,
        temple_location_names.btn_t2_wall_nw_gate,
        temple_location_names.btn_t2_wall_jones_hall,
    ],
    temple_region_names.t2_n_gate_secret: [
        temple_location_names.btn_t2_puzzle_n,
    ],
    temple_region_names.t2_n_puzzle: [
        temple_location_names.t2_n_puzzle_1,
        temple_location_names.t2_n_puzzle_2,
        temple_location_names.t2_n_puzzle_3,
        temple_location_names.t2_n_puzzle_4,
    ],
    temple_region_names.t2_nw_button_gate: [
        temple_location_names.t2_nw_gate_1,
        temple_location_names.t2_nw_gate_2,
    ],
    temple_region_names.t2_s_gate: [
        temple_location_names.t2_s_node_room_1,
        temple_location_names.t2_s_node_room_2,
        temple_location_names.t2_s_node_room_3,
        temple_location_names.t2_s_sunbeam_1,
        temple_location_names.t2_s_sunbeam_2,
        temple_location_names.t2_sw_jail_1,
        temple_location_names.t2_sw_jail_2,
        temple_location_names.t2_tower_mana_3,
        temple_location_names.btn_t2_rune_sw,
        temple_location_names.btn_t2_floor_blue,
        temple_location_names.btn_t2_wall_s_gate_shortcut,
        temple_location_names.btn_t2_wall_s_gate_hall,
    ],
    temple_region_names.t2_s_gate_secret: [
        temple_location_names.btn_t2_puzzle_s,
    ],
    temple_region_names.t2_sw_puzzle: [
        temple_location_names.t2_sw_puzzle_1,
        temple_location_names.t2_sw_puzzle_2,
        temple_location_names.t2_sw_puzzle_3,
        temple_location_names.t2_sw_puzzle_4,
    ],
    temple_region_names.t2_n_node: [
        temple_location_names.btn_t2_wall_n_node,
        temple_location_names.ev_t2_n_node,
    ],
    temple_region_names.t2_boulder_room: [
        temple_location_names.t2_boulder_room_1,
        temple_location_names.t2_boulder_room_2,
        temple_location_names.t2_boulder_room_block,
        temple_location_names.btn_t2_rune_w,
        temple_location_names.btn_t2_wall_boulder_room,
    ],
    temple_region_names.t2_n_hidden_hall: [
        temple_location_names.t2_mana_drain_fire_trap_1,
        temple_location_names.t2_mana_drain_fire_trap_2,
        temple_location_names.btn_t2_wall_n_hidden_hall,
    ],
    temple_region_names.t2_jones_hall: [
        temple_location_names.t2_jones_hallway,
    ],
    temple_region_names.t2_s_node: [
        temple_location_names.ev_t2_s_node,
    ],
    temple_region_names.t2_jail_sw: [
        temple_location_names.t2_gold_beetle_barricade,
        temple_location_names.t2_w_gold_beetle_room_1,
        temple_location_names.t2_w_gold_beetle_room_2,
        temple_location_names.t2_w_gold_beetle_room_3,
        temple_location_names.t2_w_gold_beetle_room_4,
        temple_location_names.btn_t2_wall_jail_w,
    ],
    temple_region_names.t2_sdoor_gate: [
        temple_location_names.t2_sw_gate,
    ],
    temple_region_names.t2_pof: [
        temple_location_names.t2_left_of_pof_switch_1,
        temple_location_names.t2_left_of_pof_switch_2,
        temple_location_names.btn_t2_pof_1,
        temple_location_names.btn_t2_pof_2,
        temple_location_names.btn_t2_pof_3,
        temple_location_names.btn_t2_pof_4,
        temple_location_names.btn_t2_wall_pof,
        temple_location_names.btn_t2_pof,
    ],
    temple_region_names.t2_pof_spikes: [
        temple_location_names.t2_right_of_pof_switch,
    ],
    temple_region_names.t2_jail_s: [
        temple_location_names.btn_t2_wall_jail_s,
    ],
    temple_region_names.t2_ornate: [
        temple_location_names.btn_t2_rune_n,
        temple_location_names.btn_t2_wall_t3_gate_e,
    ],
    temple_region_names.t2_light_bridge_w: [
        temple_location_names.btn_t2_floor_portal,
    ],
    temple_region_names.t2_light_bridges_se: [
        temple_location_names.t2_se_light_bridge_1,
        temple_location_names.t2_se_light_bridge_2,
    ],
    temple_region_names.t2_light_bridges_s: [
        temple_location_names.t2_s_light_bridge_1,
        temple_location_names.t2_s_light_bridge_2,
    ],
    temple_region_names.t2_portal_gate: [
        temple_location_names.t2_portal_gate,
    ],
    temple_region_names.t2_ornate_t3: [
        temple_location_names.t2_floor3_cache_1,
        temple_location_names.t2_floor3_cache_2,
        temple_location_names.t2_floor3_cache_3,
        temple_location_names.t2_floor3_cache_4,
        temple_location_names.t2_floor3_cache_5,
        temple_location_names.t2_floor3_cache_6,
        temple_location_names.btn_t2_wall_t3_gate_w,
    ],
    temple_region_names.t2_ornate_gate: [
        temple_location_names.t2_floor3_cache_gate,
    ],
    temple_region_names.t3_main: [
        temple_location_names.t3_s_balcony_turret_1,
        temple_location_names.t3_s_balcony_turret_2,
        temple_location_names.t3_n_turret_1,
        temple_location_names.t3_n_turret_2,
        temple_location_names.t3_boulder_block,
        temple_location_names.t3_e_turret_spikes,
        temple_location_names.t3_tower_fire_1,
        temple_location_names.t3_tower_fire_2,
        temple_location_names.t3_tower_ice_1,
        temple_location_names.t3_tower_mana_1,
        temple_location_names.t3_tower_mana_2,
        temple_location_names.ev_t3_portal,
    ],
    temple_region_names.t3_blockade_s: [
        temple_location_names.btn_t3_wall_gate_s,
    ],
    temple_region_names.t3_s_gate: [
        temple_location_names.t3_s_gate,
    ],
    temple_region_names.t3_n_node_blocks: [
        temple_location_names.t3_n_node_blocks_1,
        temple_location_names.t3_n_node_blocks_2,
        temple_location_names.t3_n_node_blocks_3,
        temple_location_names.t3_n_node_blocks_4,
        temple_location_names.t3_n_node_blocks_5,
        temple_location_names.btn_t3_wall_blockade,
    ],
    temple_region_names.t3_gates: [
        temple_location_names.t3_tower_ice_2,
        temple_location_names.t3_tower_ice_3,
        temple_location_names.btn_t3_levers,
        temple_location_names.btn_t3_lever_1,
        temple_location_names.btn_t3_lever_2,
        temple_location_names.btn_t3_lever_3,
        temple_location_names.btn_t3_lever_4,
    ],
    temple_region_names.t3_puzzle_room: [
        temple_location_names.btn_t3_puzzle,
    ],
    temple_region_names.t3_puzzle: [
        temple_location_names.t3_puzzle_1,
        temple_location_names.t3_puzzle_2,
        temple_location_names.t3_puzzle_3,
        temple_location_names.t3_puzzle_4,
    ],
    temple_region_names.t3_n_node: [
        temple_location_names.ev_t3_n_node,
    ],
    temple_region_names.t3_s_node_blocks_1: [
        temple_location_names.t3_s_node_cache_1,
        temple_location_names.t3_s_node_cache_2,
        temple_location_names.t3_s_node_cache_3,
    ],
    temple_region_names.t3_s_node_blocks_2: [
        temple_location_names.t3_m_balcony_corridor,
    ],
    temple_region_names.t3_s_node: [
        temple_location_names.t3_n_node_1,
        temple_location_names.t3_n_node_2,
        temple_location_names.t3_n_node_3,
        temple_location_names.ev_t3_s_node,
    ],
    temple_region_names.t3_boss_fall_1: [
        temple_location_names.t3_boss_fall_1_1,
        temple_location_names.t3_boss_fall_1_2,
        temple_location_names.t3_boss_fall_1_3,
        temple_location_names.btn_t3_wall_fall_1,
    ],
    temple_region_names.t3_boss_fall_2: [
        temple_location_names.t3_boss_fall_2_1,
        temple_location_names.t3_boss_fall_2_2,
        temple_location_names.t3_boss_fall_2_3,
        temple_location_names.btn_t3_wall_fall_2,
    ],
    temple_region_names.t3_boss_fall_3: [
        temple_location_names.t3_boss_fall_3_1,
        temple_location_names.t3_boss_fall_3_2,
        temple_location_names.t3_boss_fall_3_3,
        temple_location_names.t3_boss_fall_3_4,
        temple_location_names.btn_t3_wall_fall_3,
    ],
    temple_region_names.pof_1_main: [
        temple_location_names.pof_1_ent_1,
        temple_location_names.pof_1_ent_2,
        temple_location_names.pof_1_ent_3,
        temple_location_names.pof_1_ent_4,
        temple_location_names.pof_1_ent_5,
    ],
    temple_region_names.pof_1_s_halls: None,
    temple_region_names.pof_1_sw_room: [
        temple_location_names.pof_1_sw_left_1,
        temple_location_names.pof_1_sw_left_2,
        temple_location_names.pof_1_sw_left_3,
        temple_location_names.pof_1_sw_left_4,
        temple_location_names.pof_1_sw_left_5,
        temple_location_names.pof_1_sw_left_6,
        temple_location_names.pof_1_sw_left_7,
        temple_location_names.pof_1_sw_left_8,
        temple_location_names.pof_1_sw_left_9,
        temple_location_names.pof_1_sw_left_10,
        temple_location_names.pof_1_sw_left_11,
    ],
    temple_region_names.pof_1_se_room: [
        temple_location_names.btn_pof_1_panel_se,
    ],
    temple_region_names.pof_1_se_room_top: [
        temple_location_names.pof_1_s_1,
        temple_location_names.pof_1_s_2,
        temple_location_names.pof_1_s_3,
        temple_location_names.pof_1_s_4,
        temple_location_names.pof_1_s_5,
        temple_location_names.pof_1_s_6,
        temple_location_names.pof_1_s_7,
        temple_location_names.pof_1_s_8,
        temple_location_names.pof_1_s_9,
        temple_location_names.pof_1_s_10,
        temple_location_names.pof_1_s_11,
        temple_location_names.pof_1_s_12,
        temple_location_names.pof_1_s_13,
    ],
    temple_region_names.pof_1_sw_gate: None,
    temple_region_names.pof_1_center: None,
    temple_region_names.pof_1_nw: [
        temple_location_names.pof_1_confuse_corner_1,
        temple_location_names.pof_1_confuse_corner_2,
        temple_location_names.pof_1_confuse_corner_3,
        temple_location_names.pof_1_confuse_corner_4,
    ],
    temple_region_names.pof_1_n_room: [
        temple_location_names.pof_1_n_1,
        temple_location_names.pof_1_n_2,
        temple_location_names.pof_1_n_3,
        temple_location_names.pof_1_n_4,
        temple_location_names.pof_1_n_5,
        temple_location_names.pof_1_n_6,
        temple_location_names.pof_1_n_7,
        temple_location_names.pof_1_n_8,
        temple_location_names.pof_1_n_9,
        temple_location_names.btn_pof_1_panel_n,
    ],
    temple_region_names.pof_1_exit_hall: [
        temple_location_names.pof_1_c_hall_1,
        temple_location_names.pof_1_c_hall_2,
        temple_location_names.pof_1_c_hall_3,
        temple_location_names.pof_1_c_hall_4,
        temple_location_names.pof_1_c_hall_5,
        temple_location_names.pof_1_c_hall_6,
    ],
    temple_region_names.pof_1_gate_2: [
        temple_location_names.pof_1_end_1,
        temple_location_names.pof_1_end_2,
        temple_location_names.pof_1_end_3,
        temple_location_names.pof_1_end_4,
        temple_location_names.pof_1_end_5,
    ],
    temple_region_names.pof_2_entrance: None,
    temple_region_names.pof_2_entrance_blocks: [
        temple_location_names.pof_2_ent_1,
        temple_location_names.pof_2_ent_2,
        temple_location_names.pof_2_ent_3,
        temple_location_names.pof_2_ent_4,
        temple_location_names.pof_2_ent_5,
        temple_location_names.pof_2_ent_6,
    ],
    temple_region_names.pof_2_main: [
        temple_location_names.pof_2_confuse_hall_1,
        temple_location_names.pof_2_confuse_hall_2,
        temple_location_names.pof_2_confuse_hall_3,
        temple_location_names.pof_2_confuse_hall_4,
        temple_location_names.pof_2_sw_1,
        temple_location_names.pof_2_sw_2,
        temple_location_names.pof_2_sw_3,
        temple_location_names.pof_2_sw_4,
    ],
    temple_region_names.pof_2_n: [
        temple_location_names.pof_2_ne_1,
        temple_location_names.pof_2_ne_2,
        temple_location_names.pof_2_ne_3,
        temple_location_names.pof_2_ne_4,
        temple_location_names.btn_pof_2_panel_e,
    ],
    temple_region_names.pof_2_puzzle: [
        temple_location_names.btn_pof_2_panel_w,
        temple_location_names.btn_pof_puzzle,
    ],
    temple_region_names.pof_puzzle: [
        temple_location_names.pof_puzzle_1,
        temple_location_names.pof_puzzle_2,
        temple_location_names.pof_puzzle_3,
        temple_location_names.pof_puzzle_4,
    ],
    temple_region_names.pof_2_exit: None,
    temple_region_names.pof_3_start: [
        temple_location_names.pof_3_safety_room_1,
        temple_location_names.pof_3_safety_room_2,
        temple_location_names.pof_3_safety_room_3,
        temple_location_names.btn_pof_3_panel,
    ],
    temple_region_names.pof_3_main: [
        temple_location_names.pof_3_end_1,
        temple_location_names.pof_3_end_2,
        temple_location_names.pof_3_end_3,
        temple_location_names.pof_3_end_4,
        temple_location_names.pof_3_end_5,
        temple_location_names.ev_pof_end,
    ],
    temple_region_names.b3_main: None,
    temple_region_names.b3_platform_1: [
        temple_location_names.b3_tower_fire_2,
    ],
    temple_region_names.b3_platform_2: [
        temple_location_names.b3_tower_fire_1,
    ],
    temple_region_names.b3_platform_3: [
        temple_location_names.b3_tower_fire_3,
    ],
    temple_region_names.b3_defeated: [
        temple_location_names.ev_beat_boss_3,
    ],
}


def create_tots_regions(world: "HammerwatchWorld", active_locations: typing.Dict[str, LocationData]):

    temple_created_regions = [create_region(world, active_locations, region_name, locations)
                              for region_name, locations in temple_regions.items()]

    world.multiworld.regions.extend(temple_created_regions)

    # Dynamically place portal event locations
    dynamic_loc_regions = {}
    if world.get_random_location(temple_location_names.rloc_c1_portal) == 1:
        dynamic_loc_regions[temple_location_names.ev_c1_portal] = temple_region_names.cave_1_main
    else:
        dynamic_loc_regions[temple_location_names.ev_c1_portal] = temple_region_names.cave_1_blue_bridge

    t1_portal_rloc = world.get_random_location(temple_location_names.rloc_t1_portal)
    if t1_portal_rloc == 0:
        dynamic_loc_regions[temple_location_names.ev_t1_portal] = temple_region_names.t1_east
    elif t1_portal_rloc == 1:
        dynamic_loc_regions[temple_location_names.ev_t1_portal] = temple_region_names.t1_ice_turret
    else:
        dynamic_loc_regions[temple_location_names.ev_t1_portal] = temple_region_names.t1_sun_turret

    t2_portal_rloc = world.get_random_location(temple_location_names.rloc_t2_portal)
    if t2_portal_rloc == 0 or t2_portal_rloc == 2:
        dynamic_loc_regions[temple_location_names.ev_t2_portal] = temple_region_names.t2_main
    elif t2_portal_rloc == 1:
        dynamic_loc_regions[temple_location_names.ev_t2_portal] = temple_region_names.t2_s_gate
    else:
        dynamic_loc_regions[temple_location_names.ev_t2_portal] = temple_region_names.t2_n_gate

    for loc_name, region_name in dynamic_loc_regions.items():
        region = world.multiworld.get_region(region_name, world.player)
        region.locations.append(HammerwatchLocation(world.player, loc_name, None, region))


def connect_tots_regions(world: "HammerwatchWorld", gate_codes: typing.Dict[str, str]):
    used_names: typing.Dict[str, int] = {}

    gate_counts: typing.List[typing.Dict[str, int]]
    all_gate_counts: typing.Dict[str, int] = {
        item_name.key_silver: 6,
        item_name.key_gold: 4,
    }
    if world.options.key_mode.value == world.options.key_mode.option_floor_master:
        key_silver = [f"Temple Floor {i+1} Master Silver Key" for i in range(2)]
        key_silver.append(item_name.key_gold_b1)
        key_gold = [f"Temple Floor {i+1} Master Gold Key" for i in range(2)]
        key_gold.append(item_name.key_gold_b1)
        gate_counts = [{key_silver[i]: 999999999, key_gold[i]: 999999999} for i in range(3)]
    else:
        key_silver = [item_name.key_silver for _ in range(3)]
        key_gold = [item_name.key_gold for _ in range(3)]

        gate_counts = [all_gate_counts for _ in range(3)]

    # pan_item = item_name.pan
    # lever_item = item_name.lever
    pickaxe_item = item_name.pickaxe
    # pan_item_count = world.options.pan_fragments.value
    # lever_item_count = world.options.lever_fragments.value
    pickaxe_item_count = world.options.pickaxe_fragments.value
    # if pan_item_count > 1:
    #     pan_item = item_name.pan_fragment
    # if lever_item_count > 1:
    #     lever_item = item_name.lever_fragment
    if pickaxe_item_count > 1:
        pickaxe_item = item_name.pickaxe_fragment
    hammer_item = item_name.hammer
    hammer_item_count = world.options.hammer_fragments.value
    if hammer_item_count > 1:
        hammer_item = item_name.hammer_fragment

    rando_all_exits = world.options.exit_randomization.value == world.options.exit_randomization.option_all

    # If not doing entrance randomization or randomizing the start we start in the normal spot
    if not (world.options.exit_randomization.value and world.options.random_start_exit.value):
        connect(world, used_names, temple_region_names.menu, temple_region_names.hub_main, False)

    buttonsanity = world.options.buttonsanity.value > 0
    buttonsanity_insanity = get_buttonsanity_insanity(world)

    connect(world, used_names, temple_region_names.hub_main, temple_region_names.hub_rocks,
            False, pickaxe_item, pickaxe_item_count, False)
    # Actually one-way because you need to talk to Lyron to clear the rocks, and he's on the shop side
    connect_exit(world, used_names, temple_region_names.hub_rocks, temple_region_names.cave_3_fall,
                 entrance_names.t_c1_fall_surface, None)
    # For the temple entrances in the hub
    t3_entrance = temple_region_names.t3_main
    t3_entrance_rloc = world.get_random_location(temple_location_names.rloc_t3_entrance)
    if t3_entrance_rloc == 2:
        t3_entrance = temple_region_names.t3_blockade_s
    t3_entrance_code = f"t3|{t3_entrance_rloc}"
    connect_exit(world, used_names, temple_region_names.hub_rocks, t3_entrance,
                 t3_entrance_code, entrance_names.t_hub_t3)  # , item_name.key_teleport, 1, True)
    connect_exit(world, used_names, temple_region_names.hub_main, temple_region_names.temple_entrance,
                 entrance_names.t_t_ent_hub, entrance_names.t_hub_t_ent)
    connect(world, used_names, temple_region_names.hub_main, temple_region_names.hub_pyramid_of_fear,
            False, item_name.ev_pof_complete, 1, False)

    connect_exit(world, used_names, temple_region_names.hub_main, temple_region_names.library_lobby,
                 entrance_names.t_lib_start, entrance_names.t_hub_library)
    connect_exit(world, used_names, temple_region_names.library_lobby, temple_region_names.library,
                 entrance_names.t_lib_books, entrance_names.t_lib_lobby_end)
    connect_exit(world, used_names, temple_region_names.library, temple_region_names.cave_3_main,
                 entrance_names.t_c1_start, None)
    connect(world, used_names, temple_region_names.cave_3_main, temple_region_names.cave_3_fields,
            False, item_name.btn_c2_pumps, 1, False)
    connect(world, used_names, temple_region_names.c3_e, temple_region_names.c3_e_water,
            False, item_name.btn_c2_pumps, 1, False)
    connect(world, used_names, temple_region_names.c3_e_water, temple_region_names.cave_3_main, False)
    connect(world, used_names, temple_region_names.cave_3_main, temple_region_names.c3_main_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.c3_main_secrets, temple_region_names.c3_puzzle, False,
            item_name.btn_c3_puzzle, 1, False, buttonsanity)
    connect_or(world, used_names, temple_region_names.cave_3_main, temple_region_names.c3_e, True,
               [item_name.btn_c3_e_bridge, item_name.btn_c2_pumps], True)
    connect(world, used_names, temple_region_names.c3_e, temple_region_names.c3_e_guard_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.cave_3_fall, temple_region_names.cave_3_main, False,
            item_name.btn_c3_fall_bridge, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_3_secret, temple_region_names.c3_e,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    # If ER is on, use consume logic if Rune Keys are placed normally. If we're placing them don't use logic as we
    # can't predict how we'll collect them. If ER is off use hardcoded logic so we have reasonable spheres
    if world.options.exit_randomization.value:
        if world.options.portal_accessibility.value:
            connect_exit(world, used_names, temple_region_names.c3_e, temple_region_names.cave_2_main,
                         entrance_names.t_c2_start, entrance_names.t_c1_end)
        else:
            connect_exit(world, used_names, temple_region_names.c3_e, temple_region_names.cave_2_main,
                         entrance_names.t_c2_start, entrance_names.t_c1_end, item_name.key_teleport, 1, True)
    else:
        connect_exit(world, used_names, temple_region_names.c3_e, temple_region_names.cave_2_main,
                     entrance_names.t_c2_start, entrance_names.t_c1_end, item_name.key_teleport, 1, False)

    connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_main_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.cave_2_pumps,
            False, item_name.btn_c2_pumps, 1, False)
    connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_red_bridge, False,
            item_name.btn_c2_red, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_green_bridge, False,
            item_name.btn_c2_green, 1, False, buttonsanity)
    if buttonsanity:
        connect_or(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_sw, False,
                   [item_name.btn_c2_green, item_name.btn_c2_s_bridge], True)
        connect(world, used_names, temple_region_names.c2_sw, temple_region_names.cave_2_main,
                False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
        connect(world, used_names, temple_region_names.c2_sw, temple_region_names.c2_double_bridge, True,
                item_name.btn_c2_bridges, 1, False)
        connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_double_bridge, True,
                item_name.btn_c2_bridges, 1, False)
    else:
        connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_sw, True)
        connect(world, used_names, temple_region_names.c2_sw_secrets, temple_region_names.c2_double_bridge, False)
    # Both require green switch
    connect(world, used_names, temple_region_names.c2_sw, temple_region_names.c2_sw_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.c2_sw_secrets, temple_region_names.c2_puzzle, False,
            item_name.btn_c2_puzzle, 1, False, buttonsanity)
    # Two-way
    # connect_generic(multiworld, player, used_names, temple_region_names.c2_double_bridge,
    #                 temple_region_names.cave_2_main)
    # Both require double bridge switch
    # connect(world, used_names, temple_region_names.c2_sw, temple_region_names.cave_2_main, False)
    # Requires lower bridge switch
    if world.options.exit_randomization.value:
        if world.options.portal_accessibility.value:
            connect_exit(world, used_names, temple_region_names.c2_sw, temple_region_names.cave_1_main,
                         entrance_names.t_c3_start, entrance_names.t_c2_end)
        else:
            connect_exit(world, used_names, temple_region_names.c2_sw, temple_region_names.cave_1_main,
                         entrance_names.t_c3_start, entrance_names.t_c2_end, item_name.key_teleport, 1, True)
    else:
        connect_exit(world, used_names, temple_region_names.c2_sw, temple_region_names.cave_1_main,
                     entrance_names.t_c3_start, entrance_names.t_c2_end, item_name.key_teleport, 2, False)

    connect(world, used_names, temple_region_names.cave_1_main, temple_region_names.c1_main_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.c1_main_secrets, temple_region_names.c1_n_puzzle, False,
            item_name.btn_c1_puzzle_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_1_main, temple_region_names.cave_1_blue_bridge, buttonsanity,
            item_name.btn_c1_blue, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_1_blue_bridge, temple_region_names.c1_blue_bridge_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    c1_no_e_shortcut = world.get_random_location(temple_location_names.rloc_c1_hall_e) >= 2
    connect(world, used_names, temple_region_names.cave_1_blue_bridge, temple_region_names.cave_1_red_bridge,
            buttonsanity, item_name.btn_c1_red, 1, False, c1_no_e_shortcut and buttonsanity)
    connect(world, used_names, temple_region_names.cave_1_red_bridge, temple_region_names.c1_red_bridge_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.c1_red_bridge_secrets, temple_region_names.c1_e_puzzle, False,
            item_name.btn_c1_puzzle_e, 1, False, buttonsanity)
    if buttonsanity:
        connect(world, used_names, temple_region_names.cave_1_blue_bridge, temple_region_names.cave_1_green_bridge,
                True, item_name.btn_c1_green, 1, False)
        connect(world, used_names, temple_region_names.cave_1_green_bridge, temple_region_names.c1_storage_island, True,
                item_name.btn_c1_green, 1, False)
    else:
        connect(world, used_names, temple_region_names.cave_1_pumps, temple_region_names.cave_1_green_bridge, False)
    connect(world, used_names, temple_region_names.cave_1_blue_bridge, temple_region_names.c1_secret_hall, False,
            item_name.btn_c1_tunnel, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_1_main, temple_region_names.cave_1_pumps,
            True, item_name.btn_c2_pumps, 1, False)
    connect(world, used_names, temple_region_names.cave_1_pumps, temple_region_names.c1_storage_island, False)
    connect_exit(world, used_names, temple_region_names.c1_storage_island, temple_region_names.boss2_main,
                 entrance_names.t_b2, entrance_names.t_c3_boss, None, 1, False,
                 rando_all_exits, True)
    # Technically a level exit, but we need to be able to go to the defeated room from anywhere rip
    connect(world, used_names, temple_region_names.boss2_main, temple_region_names.boss2_defeated, False)

    if world.options.exit_randomization.value:
        if world.options.portal_accessibility.value:
            connect_exit(world, used_names, temple_region_names.cave_1_red_bridge,
                         temple_region_names.boss_1_entrance, entrance_names.t_b1_start, entrance_names.t_c3_end,
                         None, 1, False, True, True)
        else:
            connect_exit(world, used_names, temple_region_names.cave_1_red_bridge,
                         temple_region_names.boss_1_entrance, entrance_names.t_b1_start, entrance_names.t_c3_end,
                         item_name.key_teleport, 1, True, True, True)
    else:
        connect_exit(world, used_names, temple_region_names.cave_1_red_bridge,
                     temple_region_names.boss_1_entrance, entrance_names.t_b1_start, entrance_names.t_c3_end,
                     item_name.key_teleport, 3, False, True, True)

    connect(world, used_names, temple_region_names.boss_1_entrance, temple_region_names.boss_1_arena,
            True)  # We shouldn't include boss teleporters in ER, it's kinda mean lol
    connect(world, used_names, temple_region_names.boss_1_arena, temple_region_names.boss_1_defeated, False)
    connect_gate(world, used_names, temple_region_names.boss_1_arena, temple_region_names.b1_back,
                 key_gold[2], gate_codes, gate_counts[2], gate_names.t_b1_0, True)
    connect(world, used_names, temple_region_names.b1_back, temple_region_names.b1_back_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.b1_back, temple_region_names.boss_1_entrance, buttonsanity,
            item_name.btn_b1_bridge, 1, False, buttonsanity)

    p_entr_rloc = world.get_random_location(temple_location_names.rloc_passage_entrance)
    p_mid_rloc = world.get_random_location(temple_location_names.rloc_passage_middle)
    p_end_rloc = world.get_random_location(temple_location_names.rloc_passage_end)
    passage_entrance = entrance_names.t_p_ent_start if p_entr_rloc == 0\
        else entrance_names.t_p_ent_start_2
    connect_exit(world, used_names, temple_region_names.b1_back, temple_region_names.passage_entrance,
                 passage_entrance, entrance_names.t_b1_end)
    connect(world, used_names, temple_region_names.passage_entrance, temple_region_names.passage_entrance_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    passage_mid = f"passage|{p_mid_rloc + 1}0"
    connect_exit(world, used_names, temple_region_names.passage_entrance, temple_region_names.passage_mid,
                 passage_mid, entrance_names.t_p_ent_exit)
    connect(world, used_names, temple_region_names.passage_mid, temple_region_names.passage_mid_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.passage_mid_secrets, temple_region_names.passage_puzzle, False,
            item_name.btn_p_puzzle, 1, False, buttonsanity)
    passage_end = f"passage|1{p_end_rloc + 1}0"
    connect_exit(world, used_names, temple_region_names.passage_mid, temple_region_names.passage_end,
                 passage_end, f"passage|{p_mid_rloc + 1}1")
    connect(world, used_names, temple_region_names.passage_end, temple_region_names.passage_end_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)

    connect_exit(world, used_names, temple_region_names.passage_end, temple_region_names.temple_entrance_back,
                 entrance_names.t_t_ent_p, entrance_names.t_p_end_end)
    connect(world, used_names, temple_region_names.temple_entrance_back, temple_region_names.temple_entrance,
            False)
    connect_exit(world, used_names, temple_region_names.temple_entrance_back, temple_region_names.t1_main,
                 entrance_names.t_t1_start, entrance_names.t_t_ent_temple)

    connect(world, used_names, temple_region_names.t1_main, temple_region_names.t1_main_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.t1_main_secret, temple_region_names.t1_w_puzzle, False,
            item_name.btn_t1_puzzle_w, 1, False, buttonsanity)
    connect_gate(world, used_names, temple_region_names.t1_main, temple_region_names.t1_sw_sdoor,
                 key_silver[0], gate_codes, gate_counts[0], gate_names.t_t1_3, False)
    connect(world, used_names, temple_region_names.t1_main, temple_region_names.t1_node_1,
            False, item_name.mirror, 3)
    connect(world, used_names, temple_region_names.t1_node_1, temple_region_names.t1_w, False)
    connect(world, used_names, temple_region_names.t1_w, temple_region_names.t1_runway_halls, buttonsanity,
            item_name.btn_t1_runway, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t1_runway_halls, temple_region_names.t1_main, buttonsanity,
            item_name.btn_t1_runway, 1, False, buttonsanity)
    connect_exit(world, used_names, temple_region_names.t1_runway_halls, temple_region_names.cave_3_secret,
                 entrance_names.t_c1_fall_temple, None)
    connect_gate(world, used_names, temple_region_names.t1_w, temple_region_names.t1_sun_turret,
                 key_silver[0], gate_codes, gate_counts[0], gate_names.t_t1_1, False)
    connect_gate(world, used_names, temple_region_names.t1_w, temple_region_names.t1_ice_turret,
                 key_gold[0], gate_codes, gate_counts[0], gate_names.t_t1_4, True)
    connect(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_telarian, False,
            item_name.btn_t1_telarian, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_telarian_melt_ice, False,
            item_name.evt_beat_boss_2, 1, False)
    connect_gate(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_n_of_ice_turret,
                 key_silver[0], gate_codes, gate_counts[0], gate_names.t_t1_0, False)
    connect_gate(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_s_of_ice_turret,
                 key_silver[0], gate_codes, gate_counts[0], gate_names.t_t1_2, False)
    connect_gate(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_east,
                 key_gold[0], gate_codes, gate_counts[0], gate_names.t_t1_5, True)
    connect(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_sun_block_hall,
            False, item_name.mirror, 3)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_node_2,
            False, item_name.mirror, 1)  # For future reference both these have extra stuff set in Rules.py
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_ice_chamber_melt_ice, False,
            item_name.evt_beat_boss_2, 1, False)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_jail_e, False,
            item_name.btn_t1_jail_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_e_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.t1_e_secret, temple_region_names.t1_e_puzzle, False,
            item_name.btn_t1_puzzle_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_ne_hall, False,
            item_name.btn_t1_hall, 1, False, buttonsanity)

    t2_entr_rloc = world.get_random_location(temple_location_names.rloc_t2_entrance)
    if world.options.exit_randomization.value:
        if world.options.portal_accessibility.value:
            connect_exit(world, used_names, temple_region_names.t1_east, temple_region_names.t2_main,
                         f"t2|{t2_entr_rloc}", entrance_names.t_t1_end)
            connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_main, False)
        else:
            connect_exit(world, used_names, temple_region_names.t1_east, temple_region_names.t2_main,
                         f"t2|{t2_entr_rloc}", entrance_names.t_t1_end,
                         item_name.key_teleport, 1, True)
            connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_main, False,
                    item_name.key_teleport, 1, True)
    else:
        connect_exit(world, used_names, temple_region_names.t1_east, temple_region_names.t2_main,
                     f"t2|{t2_entr_rloc}", entrance_names.t_t1_end,
                     item_name.key_teleport, 4, False)

    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_main_secrets,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.t2_main_secrets, temple_region_names.t2_nw_puzzle, False,
            item_name.btn_t2_puzzle_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_main_secrets, temple_region_names.t2_e_puzzle, False,
            item_name.btn_t2_puzzle_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_melt_ice,
            True, item_name.evt_beat_boss_2, 1, False)
    connect(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_w_ice_gate, False,
            item_name.btn_t2_ice_gate_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_e_ice_gate, False,
            item_name.btn_t2_ice_gate_e, 1, False, buttonsanity)
    connect_gate(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_n_gate,
                 key_silver[1], gate_codes, gate_counts[1], gate_names.t_t2_0, False)
    connect_gate(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_s_gate,
                 key_silver[1], gate_codes, gate_counts[1], gate_names.t_t2_1, False)
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_sdoor_gate, False,
            item_name.btn_t2_s_gate_shortcut, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_sdoor_gate, temple_region_names.t2_s_gate, False,
            item_name.btn_t2_s_gate_shortcut, 1, False, buttonsanity)
    # Technically should be two-way, but you have to have been to t2_main before getting here so it's not needed
    connect_gate(world, used_names, temple_region_names.t2_main, temple_region_names.t2_ornate,
                 key_gold[1], gate_codes, gate_counts[1], gate_names.t_t2_2, buttonsanity)
    connect(world, used_names, temple_region_names.t2_ornate, temple_region_names.t2_ornate_gate, buttonsanity,
            item_name.btn_t2_t3_gate_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_ornate_t3, temple_region_names.t2_ornate_gate, buttonsanity,
            item_name.btn_t2_t3_gate_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_n_gate, temple_region_names.t2_n_gate_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.t2_n_gate_secret, temple_region_names.t2_n_puzzle, False,
            item_name.btn_t2_puzzle_n, 1, False, buttonsanity)
    # connect(world, used_names, temple_region_names.t2_n_gate, temple_region_names.t2_jones_hall, False,
    #         item_name.btn_t2_jones_hall, 1, False, buttonsanity)
    #  Technically possible, but you'll likely need to play as Paladin to escape with your life
    connect(world, used_names, temple_region_names.t2_n_gate, temple_region_names.t2_n_node, False,
            item_name.mirror, 3)
    connect(world, used_names, temple_region_names.t2_n_gate, temple_region_names.t2_nw_button_gate, False,
            item_name.btn_t2_nw_gate, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_n_node, temple_region_names.t2_boulder_room, False,
            item_name.btn_t2_boulder_room, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_boulder_room, temple_region_names.t2_jail_sw, False,
            item_name.btn_t2_blue, 1, False)
    connect(world, used_names, temple_region_names.t2_jail_sw, temple_region_names.t2_s_gate, buttonsanity,
            item_name.btn_t2_jail_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_boulder_room, temple_region_names.t2_n_hidden_hall, False,
            item_name.btn_t2_s_gate_hall, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_n_hidden_hall, temple_region_names.t2_jones_hall, False,
            item_name.btn_t2_jones_hall_back, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_s_gate, temple_region_names.t2_s_gate_secret,
            False, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.t2_s_gate_secret, temple_region_names.t2_sw_puzzle, False,
            item_name.btn_t2_puzzle_s, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_s_gate, temple_region_names.t2_s_node, False,
            item_name.mirror, 4)
    connect(world, used_names, temple_region_names.t2_s_node, temple_region_names.t2_pof, False)
    # Technically you only need 3 mirrors to get here, but this is safer logic
    connect(world, used_names, temple_region_names.t2_pof, temple_region_names.t2_jail_s, False,
            item_name.btn_t2_jail_s, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_pof_spikes, False,
            item_name.btn_t2_s_spikes, 1, False, buttonsanity)
    # Same reasoning making this from main as the south gate shortcut
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_light_bridges_se, False,
            item_name.btn_t2_light_bridges, 1, False)
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_light_bridges_s, False,
            item_name.btn_t2_light_bridges, 1, False)
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_light_bridge_w, False,
            item_name.btn_t2_light_bridges, 1, False)
    connect(world, used_names, temple_region_names.t2_light_bridge_w, temple_region_names.t2_portal_gate, buttonsanity,
            item_name.btn_t2_portal_gate, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_portal_gate, temple_region_names.t2_main, buttonsanity,
            item_name.btn_t2_portal_gate, 1, False, buttonsanity)
    connect_exit(world, used_names, temple_region_names.t2_light_bridge_w, temple_region_names.cave_3_portal,
                 entrance_names.t_c1_portal, entrance_names.t_t2_w_portal)
    connect_exit(world, used_names, temple_region_names.t2_light_bridges_s, temple_region_names.cave_1_temple,
                 entrance_names.t_c3_temple, entrance_names.t_t2_s_light_bridge)

    connect(world, used_names, temple_region_names.t3_blockade_s, temple_region_names.t3_s_gate, buttonsanity,
            item_name.btn_t3_gate_s, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t3_s_gate, temple_region_names.t3_main, buttonsanity,
            item_name.btn_t3_gate_s, 1, False, buttonsanity)
    if world.options.exit_randomization.value:
        if world.options.portal_accessibility.value:
            connect_exit(world, used_names, temple_region_names.t3_main, temple_region_names.t2_ornate_t3,
                         entrance_names.t_t2_t3, entrance_names.t_t3_t2)
        else:
            connect_exit(world, used_names, temple_region_names.t3_main, temple_region_names.t2_ornate_t3,
                         entrance_names.t_t2_t3, entrance_names.t_t3_t2, item_name.key_teleport, 1, True)
    else:
        connect_exit(world, used_names, temple_region_names.t3_main, temple_region_names.t2_ornate_t3,
                     entrance_names.t_t2_t3, entrance_names.t_t3_t2, item_name.key_teleport, 6, False)
    connect(world, used_names, temple_region_names.t3_main, temple_region_names.t3_main,
            False, item_name.mirror, 2)
    # Wonky logic, we treat this like a dead end as players could waste their mirrors on this with no benefit
    connect(world, used_names, temple_region_names.t3_s_node_blocks_2, temple_region_names.t3_n_node_blocks, False,
            item_name.mirror, 1)
    # After wasting mirrors everywhere else only this one will turn on the beam to break the blockade
    connect(world, used_names, temple_region_names.t3_n_node_blocks, temple_region_names.t3_blockade_s, False)
    if buttonsanity:
        connect(world, used_names, temple_region_names.t3_main, temple_region_names.t3_gates, False,
                item_name.btn_t3_pillars, 1, False)
        connect(world, used_names, temple_region_names.t3_main, temple_region_names.t3_puzzle_room, False,
                item_name.btn_t3_puzzle_room, 1, False)
    else:
        connect(world, used_names, temple_region_names.t3_n_node_blocks, temple_region_names.t3_gates, False)
        connect(world, used_names, temple_region_names.t3_gates, temple_region_names.t3_puzzle_room, False)
    connect(world, used_names, temple_region_names.t3_puzzle_room, temple_region_names.t3_puzzle, False,
            item_name.btn_t3_puzzle, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t3_n_node_blocks, temple_region_names.t3_n_node, False)
    connect(world, used_names, temple_region_names.t3_main, temple_region_names.t3_s_node_blocks_1,
            False, item_name.mirror, 2)
    connect(world, used_names, temple_region_names.t3_main, temple_region_names.t3_s_node_blocks_2,
            False, item_name.mirror, 1)
    # More wonky logic, I hope everything works out!
    connect(world, used_names, temple_region_names.t3_s_node_blocks_2, temple_region_names.t3_s_node, False)
    connect(world, used_names, temple_region_names.t3_boss_fall_1, temple_region_names.t3_main, buttonsanity,
            item_name.btn_t3_fall_1, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t3_boss_fall_2, temple_region_names.t3_main, buttonsanity,
            item_name.btn_t3_fall_2, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t3_boss_fall_3, temple_region_names.t3_main, buttonsanity,
            item_name.btn_t3_fall_3, 1, False, buttonsanity)

    if buttonsanity_insanity:
        connect_exit(world, used_names, temple_region_names.hub_main, temple_region_names.pof_1_main,
                     entrance_names.t_n1_1_start, entrance_names.t_hub_pof,
                     item_name.btn_pof_part, 24, False, False)
    else:
        connect_exit(world, used_names, temple_region_names.hub_main, temple_region_names.pof_1_main,
                     entrance_names.t_n1_1_start, entrance_names.t_hub_pof,
                     item_name.btn_pof, 6, False, False)
    connect_exit(world, used_names, temple_region_names.pof_1_main, temple_region_names.hub_main,
                 entrance_names.t_hub_pof, entrance_names.t_n1_1_start, None, 1, False, False)
    # Going back to the hub has no entrance requirements
    connect(world, used_names, temple_region_names.pof_1_main, temple_region_names.pof_1_s_halls,
            True, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.pof_1_s_halls, temple_region_names.pof_1_sw_room,
            True, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect_exit(world, used_names, temple_region_names.pof_1_sw_room, temple_region_names.pof_1_se_room,
                 entrance_names.t_n1_1_se, entrance_names.t_n1_1_sw)
    connect(world, used_names, temple_region_names.pof_1_se_room, temple_region_names.pof_1_se_room_top, False,
            item_name.btn_pof_1_walls_s, 1, False)
    connect(world, used_names, temple_region_names.pof_1_s_halls, temple_region_names.pof_1_sw_gate, True,
            item_name.btn_pof_1_walls_s, 1, False)
    connect_gate(world, used_names, temple_region_names.pof_1_sw_gate, temple_region_names.pof_1_center,
                 item_name.key_bonus, None, None, None, True)
    connect(world, used_names, temple_region_names.pof_1_center, temple_region_names.pof_1_nw,
            True, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect_exit(world, used_names, temple_region_names.pof_1_nw, temple_region_names.pof_1_n_room,
                 entrance_names.t_n1_1_n, entrance_names.t_n1_1_ne)
    connect(world, used_names, temple_region_names.pof_1_nw, temple_region_names.pof_1_exit_hall, True,
            item_name.btn_pof_1_exit, 1, False)
    connect_gate(world, used_names, temple_region_names.pof_1_exit_hall, temple_region_names.pof_1_gate_2,
                 item_name.key_bonus, None, None, None, True)
    connect_exit(world, used_names, temple_region_names.pof_1_gate_2, temple_region_names.pof_2_entrance,
                 entrance_names.t_n1_2_start, None)  # entrance_names.t_n1_20)
    connect(world, used_names, temple_region_names.pof_2_entrance, temple_region_names.pof_2_entrance_blocks,
            True, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect(world, used_names, temple_region_names.pof_2_entrance_blocks, temple_region_names.pof_2_main,
            True, hammer_item, hammer_item_count, False, hammer_item_count > 0)
    connect_exit(world, used_names, temple_region_names.pof_2_main, temple_region_names.pof_2_n,
                 entrance_names.t_n1_2_n, entrance_names.t_n1_2_nw)
    connect(world, used_names, temple_region_names.pof_2_n, temple_region_names.pof_2_puzzle, False,
            item_name.btn_pof_2_puzzle, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.pof_2_puzzle, temple_region_names.pof_puzzle, False,
            item_name.btn_pof_puzzle, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.pof_2_main, temple_region_names.pof_2_exit, False,
            item_name.btn_pof_2_exit, 1, False)
    connect_exit(world, used_names, temple_region_names.pof_2_exit, temple_region_names.pof_3_start,
                 entrance_names.t_n1_3_start, None)  # entrance_names.t_n1_100)
    connect(world, used_names, temple_region_names.pof_3_start, temple_region_names.pof_3_main, False,
            item_name.btn_pof_3_start, 1, False, buttonsanity)
    connect_exit(world, used_names, temple_region_names.pof_3_main, temple_region_names.hub_main,
                 entrance_names.t_hub_pof_return, None)

    connect_exit(world, used_names, temple_region_names.hub_main, temple_region_names.b3_main,
                 entrance_names.t_b3, entrance_names.t_hub_b3,
                 item_name.ev_solar_node, 6, False, rando_all_exits, True)
    connect(world, used_names, temple_region_names.b3_main, temple_region_names.b3_platform_1, False)
    connect(world, used_names, temple_region_names.b3_platform_1, temple_region_names.b3_platform_2, False)
    connect(world, used_names, temple_region_names.b3_platform_2, temple_region_names.b3_platform_3, False)
    connect(world, used_names, temple_region_names.b3_platform_3, temple_region_names.b3_defeated, False)

    connect_exit(world, used_names, temple_region_names.b3_platform_1, temple_region_names.t3_boss_fall_1,
                 entrance_names.t_t3_fall_1, None, None, 1, False, False)
    connect_exit(world, used_names, temple_region_names.b3_platform_2, temple_region_names.t3_boss_fall_2,
                 entrance_names.t_t3_fall_2, None, None, 1, False, False)
    connect_exit(world, used_names, temple_region_names.b3_platform_3, temple_region_names.t3_boss_fall_3,
                 entrance_names.t_t3_fall_3, None, None, 1, False, False)


def connect_shops(world: "HammerwatchWorld"):
    used_names = {}
    # Shop shuffle
    world.shop_locations = {}
    if world.campaign == Campaign.Castle:
        shop_counts = {
            ShopType.Combo: [1, 2, 2, 3, 4, 4, 5],
            ShopType.Offense: [1, 1, 2, 3, 3, 4, 5],
            ShopType.Defense: [1, 2, 3, 4, 5],
            ShopType.Vitality: [1, 2, 3, 4, 4, 5],
            ShopType.Powerup: [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        }
        world.shop_locations = {
            castle_location_names.shop_p1_combo: ShopInfo(ShopType.Combo, 1),
            castle_location_names.shop_p1_misc: ShopInfo(ShopType.Vitality, 1),
            castle_location_names.shop_p2_off: ShopInfo(ShopType.Offense, 1),
            castle_location_names.shop_p2_combo: ShopInfo(ShopType.Combo, 2),
            castle_location_names.shop_p3_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_p3_off: ShopInfo(ShopType.Offense, 1),
            castle_location_names.shop_p3_def: ShopInfo(ShopType.Defense, 1),
            castle_location_names.shop_p3_combo: ShopInfo(ShopType.Combo, 2),
            castle_location_names.shop_p3_misc: ShopInfo(ShopType.Vitality, 2),
            castle_location_names.shop_b1_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_a1_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_a1_combo: ShopInfo(ShopType.Combo, 3),
            castle_location_names.shop_a1_misc: ShopInfo(ShopType.Vitality, 3),
            castle_location_names.shop_a1_off: ShopInfo(ShopType.Offense, 2),
            castle_location_names.shop_a1_def: ShopInfo(ShopType.Defense, 2),
            castle_location_names.shop_a3_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_b2_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_r1_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_r1_misc: ShopInfo(ShopType.Vitality, 4),
            castle_location_names.shop_r2_combo: ShopInfo(ShopType.Combo, 4),
            castle_location_names.shop_r2_off: ShopInfo(ShopType.Offense, 3),
            castle_location_names.shop_r3_misc: ShopInfo(ShopType.Vitality, 4),
            castle_location_names.shop_r3_def: ShopInfo(ShopType.Defense, 3),
            castle_location_names.shop_r3_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_r3_off: ShopInfo(ShopType.Offense, 3),
            castle_location_names.shop_r3_combo: ShopInfo(ShopType.Combo, 4),
            castle_location_names.shop_b3_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_c1_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_c2_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_c2_combo: ShopInfo(ShopType.Combo, 5),
            castle_location_names.shop_c2_off: ShopInfo(ShopType.Offense, 4),
            castle_location_names.shop_c2_def: ShopInfo(ShopType.Defense, 4),
            castle_location_names.shop_c2_misc: ShopInfo(ShopType.Vitality, 5),
            castle_location_names.shop_c3_power: ShopInfo(ShopType.Powerup, 0),
            castle_location_names.shop_c2_off_2: ShopInfo(ShopType.Offense, 5),
            castle_location_names.shop_c2_def_2: ShopInfo(ShopType.Defense, 5),
        }

        if world.options.shop_shuffle.value:
            for loc in world.shop_locations.keys():
                shop_type = world.random.choice(list(shop_counts.keys()))
                tier = shop_counts[shop_type].pop(0)
                if len(shop_counts[shop_type]) == 0:
                    shop_counts.pop(shop_type)
                world.shop_locations[loc] = ShopInfo(shop_type, tier)
                # if tier > 0:
                #     world.shop_locations[loc] = f"{shop_type} Level {tier}"
                # else:
                #     world.shop_locations[loc] = f"{shop_type}"
    else:
        shop_counts = {
            ShopType.Combo: 1,
            ShopType.Offense: 1,
            ShopType.Defense: 1,
            ShopType.Vitality: 1,
        }
        world.shop_locations = {
            temple_location_names.shop_combo: ShopInfo(ShopType.Combo, 1),
            temple_location_names.shop_misc: ShopInfo(ShopType.Vitality, 2),
            temple_location_names.shop_off: ShopInfo(ShopType.Offense, 0),
            temple_location_names.shop_def: ShopInfo(ShopType.Defense, 0),
        }

        if world.options.shop_shuffle.value:
            remaining_shops = []
            for shop_type in shop_counts.keys():
                remaining_shops.append(shop_type)

            for loc in world.shop_locations.keys():
                shop_loc_type_index = world.random.randint(0, len(remaining_shops) - 1)
                world.shop_locations[loc].shop_type = remaining_shops.pop(shop_loc_type_index)

        combo_regions = shop_region_names.shop_regions[world.shop_locations[temple_location_names.shop_combo].shop_type]
        misc_regions = shop_region_names.shop_regions[world.shop_locations[temple_location_names.shop_misc].shop_type]
        off_regions = shop_region_names.shop_regions[world.shop_locations[temple_location_names.shop_off].shop_type]
        def_regions = shop_region_names.shop_regions[world.shop_locations[temple_location_names.shop_def].shop_type]

        connect(world, used_names, temple_region_names.menu, combo_regions[0], False)
        connect(world, used_names, temple_region_names.menu, misc_regions[0], False)
        connect(world, used_names, misc_regions[0], misc_regions[1], False)
        # Can spend 12 ore on all other shops before this and we need 1 more to access the first level
        connect(world, used_names, temple_region_names.menu, off_regions[0], False,
                item_name.ore, 13, False)
        connect(world, used_names, temple_region_names.menu, def_regions[0], False,
                item_name.ore, 13, False)

        # 3 Ore locked behind the first level of the combo shop
        for r in range(len(combo_regions)-1):
            connect(world, used_names, combo_regions[r], combo_regions[r+1], False,
                    item_name.ore, 14 + r, False)
        # 2 Ore locked behind the second level of the vitality shop
        for r in range(1, len(misc_regions)-1):
            connect(world, used_names, misc_regions[r], misc_regions[r+1], False,
                    item_name.ore, 14 + r, False)
        # 4 Ore locked behind the first level of the offense shop
        for r in range(len(off_regions)-1):
            connect(world, used_names, off_regions[r], off_regions[r+1], False,
                    item_name.ore, 14 + r, False)
        # 4 Ore locked behind the first level of the defense shop
        for r in range(len(def_regions)-1):
            connect(world, used_names, def_regions[r], def_regions[r+1], False,
                    item_name.ore, 14 + r, False)


def create_region(world: "HammerwatchWorld", active_locations: typing.Dict[str, LocationData], name: str,
                  locations: typing.List[str] = None) -> Region:
    region = Region(name, world.player, world.multiworld)
    if locations:
        for location in locations:
            event = location not in all_locations.keys()
            if location not in active_locations.keys() and not event:
                continue
            loc_id = None if event else active_locations[location].code
            region.locations.append(HammerwatchLocation(world.player, location, loc_id, region))
    return region


def connect(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str,
            two_way: bool, pass_item: str = None, item_count=1, items_consumed=True, use_pass_item=True):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    return connect_region(world, used_names, source_region, target_region, two_way, pass_item, item_count,
                          items_consumed, use_pass_item)


def connect_region(world: "HammerwatchWorld", used_names: typing.Dict[str, int],
                   source_region: Region, target_region: Region,
                   two_way: bool, pass_item: str = None, item_count=1, items_consumed=True, use_pass_item=True):
    entrance_name = get_entrance_name(used_names, source_region.name, target_region.name)

    if not use_pass_item:
        pass_item = None

    connection = HWEntrance(world.player, entrance_name, source_region, target_region,
                            pass_item, item_count, items_consumed, None)

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect_region(world, used_names, target_region, source_region, False, pass_item, item_count,
                       items_consumed, use_pass_item)

    return connection


def connect_all(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str, two_way: bool,
                pass_items: typing.List[str], use_rule: bool):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    entrance_name = get_entrance_name(used_names, source, target)

    connection = HWEntrance(world.player, entrance_name, source_region, target_region,
                            None, 1, False, None)
    if use_rule:
        add_rule(connection, lambda state: state.has_all(pass_items, world.player), "and")

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect_or(world, used_names, target, source, False, pass_items, use_rule)

    return connection


def connect_or(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str, two_way: bool,
               pass_items: typing.List[str], use_rule: bool):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    entrance_name = get_entrance_name(used_names, source, target)

    connection = HWEntrance(world.player, entrance_name, source_region, target_region,
                            None, 1, False, None)
    if use_rule:
        add_rule(connection, lambda state: state.has_any(pass_items, world.player), "and")

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect_or(world, used_names, target, source, False, pass_items, use_rule)

    return connection


def connect_gate(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str, key_type: str,
                 gate_codes: typing.Dict[str, str] = None, gate_items: typing.Dict[str, int] = None,
                 gate_code: str = None, two_way=True):
    entrances = []

    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    entrance_name = get_entrance_name(used_names, source, target)

    key_item_name = key_type
    # Override the key item if gate shuffle is on
    if world.options.gate_shuffle.value and gate_code is not None:
        # Special handling for Universal Tracker
        if hasattr(world.multiworld, "re_gen_passthrough"):
            key_item_name = \
                (world.multiworld.re_gen_passthrough["Hammerwatch"]["Gate Types"][gate_code].capitalize() + " Key")
            if world.options.key_mode.value == world.options.key_mode.option_act_specific:
                key_item_name = " ".join(key_type.split()[:-2]) + " " + key_item_name
            elif world.options.key_mode.value == world.options.key_mode.option_floor_master:
                key_item_name = " ".join(key_type.split()[:-2]) + " " + key_item_name
        else:
            key_item_name = get_random_element(world, gate_items)
        gate_items[key_item_name] -= 1
        if gate_items[key_item_name] == 0:
            gate_items.pop(key_item_name)
        gate_codes[gate_code] = get_key_code(key_item_name.split(" ")[-2].lower())

    consumed = True
    if world.options.key_mode.value == world.options.key_mode.option_floor_master:
        consumed = False

    if key_item_name not in world.key_item_counts:
        world.key_item_counts[key_item_name] = 0
    if consumed:
        world.key_item_counts[key_item_name] += 1
    else:
        if world.key_item_counts[key_item_name] > 1:
            print("Something is consumed and also not consumed")
        world.key_item_counts[key_item_name] = 1

    connection = HWEntrance(world.player, entrance_name, source_region, target_region, key_item_name, 1, consumed, None)
    entrances.append(connection)

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        entrances.append(connect(world, used_names, target, source, False, key_item_name, 1, consumed))

    return entrances


def connect_exit(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str,
                 exit_code: str, return_code: str = None, pass_item: str = None, item_count=1, items_consumed=True,
                 two_way=True, boss_exit=False):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    entrance_name = get_entrance_name(used_names, source, target)

    connection = HWEntrance(world.player, entrance_name, source_region, target_region,
                            pass_item, item_count, items_consumed, return_code, exit_code)
    source_region.exits.append(connection)

    connect_regions = False
    if world.options.exit_randomization.value == world.options.exit_randomization.option_off:
        connect_regions = True
    elif world.options.exit_randomization.value == world.options.exit_randomization.option_no_boss_exits and boss_exit:
        two_way = False  # We don't need the return entrance as the boss rooms are always one-way
        connect_regions = True

    if connect_regions:
        connection.connect(target_region)
    else:
        connection.linked = False
        world.level_exits.append(connection)

    if two_way and return_code is not None:
        connect_exit(world, used_names, target, source, return_code, exit_code, pass_item, item_count,
                     items_consumed, False, boss_exit)


def connect_from_data(world: "HammerwatchWorld", data: HWExitData):
    connect(world, {}, data.parent, data.target, False,
            data.pass_item, data.item_count, data.items_consumed)


def get_etr_name(source: str, target: str):
    return source + " > " + target


def get_entrance_name(used_names: typing.Dict[str, int], source: str, target: str):
    base_name = get_etr_name(source, target)
    if base_name not in used_names:
        used_names[base_name] = 1
        name = base_name
    else:
        used_names[base_name] += 1
        name = base_name + ('_' * used_names[base_name])
    return name
