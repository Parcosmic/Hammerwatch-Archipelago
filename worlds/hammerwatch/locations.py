import typing

from BaseClasses import Location
from .names import castle_location_names, temple_location_names, item_name, option_names, shop_location_names
from .util import (Counter, GoalType, Campaign, get_goal_type, get_buttonsanity_insanity, get_shopsanity_classes,
                   is_using_universal_tracker)
from .items import castle_item_counts, temple_item_counts, recovery_table, get_item_counts, id_start
from enum import IntFlag

if typing.TYPE_CHECKING:
    from . import HammerwatchWorld


class LocType(IntFlag):
    Normal = 0
    Recovery = 1
    Puzzle = 2
    Secret = 4
    Bonus = 8
    Shop = 16
    EnemyLoot = 32
    Button = 64
    Buttoninsanity = 128 | Button


class LocationData(typing.NamedTuple):
    code: typing.Optional[int]
    loc_type: LocType = LocType.Normal


class HammerwatchLocation(Location):
    game: str = "Hammerwatch"

    def __init__(self, player: int, name: str = '', code: int = None, parent=None):
        super().__init__(player, name, code, parent)
        self.event = code is None
        self.show_in_spoiler = code is not None


counter = Counter(id_start + 0x1000)
castle_pickup_locations: typing.Dict[str, LocationData] = {
    castle_location_names.p1_p3_n_bridge: LocationData(counter.count(0)),
    castle_location_names.p1_bars_2: LocationData(counter.count()),
    castle_location_names.p1_entrance_hall_2: LocationData(counter.count(2), LocType.Recovery),
    castle_location_names.p1_entrance_hall_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_exit_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_exit_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_nw_bronze_gate: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_m_bronze_gate: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_m_bronze_gate_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_m_bronze_gate_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_m_bronze_gate_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_sw_bronze_gate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_sw_bronze_gate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_e_save_room_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_e_save_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_entrance_w: LocationData(counter.count()),
    castle_location_names.p1_entrance_s: LocationData(counter.count()),
    castle_location_names.p1_by_exit_3: LocationData(counter.count()),
    castle_location_names.p1_e_bridges_4: LocationData(counter.count()),
    castle_location_names.p1_w_of_se_bronze_gate_1: LocationData(counter.count()),
    castle_location_names.p1_s_w_bridges_w: LocationData(counter.count()),
    castle_location_names.p1_w_of_se_bronze_gate_5: LocationData(counter.count()),
    castle_location_names.p1_by_sw_bronze_gate_1: LocationData(counter.count()),
    castle_location_names.p1_s_of_e_save_room: LocationData(counter.count()),
    castle_location_names.p1_room_by_exit: LocationData(counter.count()),
    castle_location_names.p1_ne_arrow_traps: LocationData(counter.count()),
    castle_location_names.p1_e_bridges_5: LocationData(counter.count()),
    castle_location_names.p1_n_of_se_bridge: LocationData(counter.count()),
    castle_location_names.p1_by_sw_bronze_gate_4: LocationData(counter.count()),
    castle_location_names.p1_p3_s: LocationData(counter.count()),
    castle_location_names.p1_bars_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_entrance_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_entrance_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_entrance_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_entrance_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_w_save: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_e_bridges_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_e_bridges_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_e_bridges_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_m_bronze_gate_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_m_bronze_gate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_by_m_bronze_gate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_center_bridges_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_center_bridges_n_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_center_bridges_n_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_center_bridges_s_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_center_bridges_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_center_bridges_s_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_center_bridges_s_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_w_of_se_bronze_gate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_w_of_se_bronze_gate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_w_of_se_bronze_gate_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_9: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_10: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_s_lower_hall_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_p2_by_shop: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p1_entrance_secret: LocationData(counter.count()),
    castle_location_names.p1_e_secret: LocationData(counter.count()),
    castle_location_names.p1_p3_n_across_bridge: LocationData(counter.count()),
    castle_location_names.p1_s_secret_2: LocationData(counter.count()),
    castle_location_names.p1_hint_room: LocationData(counter.count()),
    castle_location_names.p1_se_bridge: LocationData(counter.count()),
    castle_location_names.p1_sw_bronze_gate: LocationData(counter.count()),
    castle_location_names.p1_s_secret_1: LocationData(counter.count()),

    castle_location_names.p2_spike_puzzle_w_1: LocationData(counter.count()),
    castle_location_names.p2_big_bridge_3: LocationData(counter.count(2)),
    castle_location_names.p2_sequence_puzzle_reward: LocationData(counter.count()),
    castle_location_names.p2_spike_puzzle_e_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_spike_puzzle_e_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_w_of_silver_gate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_w_of_silver_gate_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_nw_island_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_nw_island_s_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_by_red_spikes_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_by_red_spikes_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_by_red_spikes_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_entrance_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_big_bridge_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_big_bridge_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_end_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_end_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_save: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_poker_plant_room_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_poker_plant_room_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_s_arrow_traps_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_s_arrow_traps_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_entrance_1: LocationData(counter.count()),
    castle_location_names.p2_entrance_2: LocationData(counter.count()),
    castle_location_names.p2_entrance_4: LocationData(counter.count()),
    castle_location_names.p2_entrance_3: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_4: LocationData(counter.count()),
    castle_location_names.p2_w_of_gold_gate: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_5: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_1: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_6: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_2: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_3: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_12: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_13: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_11: LocationData(counter.count()),
    castle_location_names.p2_e_of_red_spikes_1: LocationData(counter.count()),
    castle_location_names.p2_e_of_red_spikes_2: LocationData(counter.count()),
    castle_location_names.p2_e_of_red_spikes_3: LocationData(counter.count()),
    castle_location_names.p2_e_of_red_spikes_4: LocationData(counter.count()),
    castle_location_names.p2_beetle_boss_room_1: LocationData(counter.count()),
    castle_location_names.p2_beetle_boss_room_2: LocationData(counter.count()),
    castle_location_names.p2_beetle_boss_room_3: LocationData(counter.count()),
    castle_location_names.p2_spike_puzzle_ne_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_spike_puzzle_ne_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_spike_puzzle_ne_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_nw_island_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_nw_island_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_of_ne_save_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_of_ne_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_w_poker_plant_room_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_w_poker_plant_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_w_poker_plant_room_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_s_of_w_gold_gate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_s_of_w_gold_gate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_s_of_w_gold_gate_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_poker_plant_room_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_poker_plant_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_poker_plant_room_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_gold_gate_room_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_gold_gate_room_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_gold_gate_room_9: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_spike_puzzle_e: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_beetle_boss_room_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_e_gold_gate_room_10: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p2_by_boss_switch: LocationData(counter.count()),
    castle_location_names.p2_nw_island_4: LocationData(counter.count()),
    castle_location_names.p2_nw_island_3: LocationData(counter.count()),
    castle_location_names.p2_nw_island_5: LocationData(counter.count()),
    castle_location_names.p2_beetle_boss_hidden_room_1: LocationData(counter.count()),
    castle_location_names.p2_toggle_spike_trap_reward_1: LocationData(counter.count()),
    castle_location_names.p2_e_poker_plant_room_4: LocationData(counter.count()),
    castle_location_names.p2_s_arrow_traps_1: LocationData(counter.count()),
    castle_location_names.p2_spike_puzzle_n_2: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_reward_2: LocationData(counter.count()),
    castle_location_names.p2_spike_puzzle_n_1: LocationData(counter.count()),
    castle_location_names.p2_spike_puzzle_w_2: LocationData(counter.count()),
    castle_location_names.p2_beetle_boss_hidden_room_2: LocationData(counter.count()),
    castle_location_names.p2_toggle_spike_trap_reward_3: LocationData(counter.count()),
    castle_location_names.p2_toggle_spike_trap_reward_2: LocationData(counter.count()),
    castle_location_names.p2_e_gold_gate_room_reward_1: LocationData(counter.count()),
    castle_location_names.p2_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.p2_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.p2_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.p2_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    castle_location_names.p3_bonus_return: LocationData(counter.count()),
    castle_location_names.p3_by_w_shop: LocationData(counter.count()),
    castle_location_names.p3_red_spike_room: LocationData(counter.count()),
    castle_location_names.p3_spike_trap_1: LocationData(counter.count()),
    castle_location_names.p3_nw_n_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_s_bronze_gate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_s_bronze_gate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_s_bronze_gate_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_s_of_poker_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_s_of_poker_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_ne_se_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_ne_se_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_ne_of_bridge_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_ne_of_bridge_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_spike_trap_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_spike_trap_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_secret_secret: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_se_cross_hall_e_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_se_cross_hall_e_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_w: LocationData(counter.count()),
    castle_location_names.p3_entrance_n_1: LocationData(counter.count()),
    castle_location_names.p3_entrance_n_of_poker: LocationData(counter.count()),
    castle_location_names.p3_entrance_n_2: LocationData(counter.count()),
    castle_location_names.p3_entrance_sw: LocationData(counter.count()),
    castle_location_names.p3_entrance_m_4: LocationData(counter.count()),
    castle_location_names.p3_entrance_s_3: LocationData(counter.count()),
    castle_location_names.p3_entrance_s_of_poker_3: LocationData(counter.count()),
    castle_location_names.p3_s_of_silver_gate: LocationData(counter.count()),
    castle_location_names.p3_arrow_hall_2: LocationData(counter.count()),
    castle_location_names.p3_arrow_hall_1: LocationData(counter.count()),
    castle_location_names.p3_se_m_2: LocationData(counter.count()),
    castle_location_names.p3_se_cross_hall_se: LocationData(counter.count()),
    castle_location_names.p3_skip_boss_switch_2: LocationData(counter.count()),
    castle_location_names.p3_w_of_w_poker: LocationData(counter.count()),
    castle_location_names.p3_nw_of_bridge: LocationData(counter.count()),
    castle_location_names.p3_n_of_bridge_5: LocationData(counter.count()),
    castle_location_names.p3_s_of_w_poker: LocationData(counter.count()),
    castle_location_names.p3_w_of_bridge: LocationData(counter.count()),
    castle_location_names.p3_nw_s_bronze_gate_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_n_of_bridge_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_nw_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_nw_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_m_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_m_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_m_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_ne_e_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_ne_e_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_ne_e_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_n_bronze_gate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_n_bronze_gate_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_n_bronze_gate_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_s_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_entrance_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_e_of_bridge_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_e_of_bridge_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_e_of_bridge_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_se_cross_hall_s_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_se_cross_hall_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_se_cross_hall_s_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_se_cross_hall_s_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_nw_n_bronze_gate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_se_m_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_s_of_boss_door: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_secret_arrow_hall_1: LocationData(counter.count()),
    castle_location_names.p3_s_of_e_poker_1: LocationData(counter.count()),
    castle_location_names.p3_nw_m: LocationData(counter.count()),
    castle_location_names.p3_nw_nw_3: LocationData(counter.count()),
    castle_location_names.p3_nw_sw_1: LocationData(counter.count()),
    castle_location_names.p3_nw_sw_2: LocationData(counter.count()),
    castle_location_names.p3_nw_se: LocationData(counter.count()),
    castle_location_names.p3_skip_boss_switch_6: LocationData(counter.count()),
    castle_location_names.p3_skip_boss_switch_4: LocationData(counter.count()),
    castle_location_names.p3_skip_boss_switch_1: LocationData(counter.count()),
    castle_location_names.p3_skip_boss_switch_3: LocationData(counter.count()),
    castle_location_names.p3_skip_boss_switch_5: LocationData(counter.count()),
    castle_location_names.p3_n_of_bridge_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.p3_secret_arrow_hall_2: LocationData(counter.count()),
    castle_location_names.p3_ne_e_4: LocationData(counter.count()),
    castle_location_names.p3_nw_closed_room: LocationData(counter.count()),
    castle_location_names.p3_n_of_bridge_2: LocationData(counter.count()),
    castle_location_names.p3_se_of_w_shop: LocationData(counter.count()),
    castle_location_names.p3_s_of_e_poker_2: LocationData(counter.count()),
    castle_location_names.p3_nw_n_bronze_gate_1: LocationData(counter.count()),
    castle_location_names.p3_nw_s_bronze_gate_1: LocationData(counter.count()),
    castle_location_names.p3_n_of_bridge_1: LocationData(counter.count()),
    castle_location_names.p3_sw_of_w_shop: LocationData(counter.count()),
    castle_location_names.p3_by_m_shop_1: LocationData(counter.count()),
    castle_location_names.p3_by_m_shop_2: LocationData(counter.count()),

    castle_location_names.n1_room2_s_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n1_room2_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n1_room2_s_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n1_room4_w_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n1_room4_w_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n1_room2_nw_room_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_nw_room_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_nw_room_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_nw_room_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_n_m_room_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_n_m_room_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_n_m_room_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_n_m_room_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_n_m_room_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_n_m_room_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_nw_room_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room2_nw_room_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_15: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_16: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_11: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_10: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_12: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_14: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_13: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_sealed_room_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_sealed_room_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_sealed_room_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_17: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_19: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_20: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room3_w_18: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room4_s_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room4_s_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room4_s_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n1_room1: LocationData(counter.count()),
    castle_location_names.n1_room3_sealed_room_1: LocationData(counter.count()),
    castle_location_names.n1_room2_small_box: LocationData(counter.count()),
    castle_location_names.n1_entrance: LocationData(counter.count()),
    castle_location_names.n1_room4_m: LocationData(counter.count()),
    castle_location_names.n1_room4_e: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n1_room2_n_secret_room: LocationData(counter.count()),

    castle_location_names.b1_reward: LocationData(counter.count()),
    castle_location_names.b1_arena_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.b1_arena_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.b1_behind_portal: LocationData(counter.count()),

    castle_location_names.a1_m_trellis_secret: LocationData(counter.count()),
    castle_location_names.a1_se_cache_3: LocationData(counter.count()),
    castle_location_names.a1_nw_left_1: LocationData(counter.count(3), LocType.Recovery),
    castle_location_names.a1_nw_right_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_save_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_ne_top_room_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_ne_top_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_sw_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_sw_n_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_sw_n_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_cache_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_cache_9: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_red_spikes_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_e_m_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_e_m_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_e_m_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_red_spikes_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_nw_right_4: LocationData(counter.count()),
    castle_location_names.a1_nw_right_3: LocationData(counter.count()),
    castle_location_names.a1_n_boss_hall: LocationData(counter.count(2)),
    castle_location_names.a1_m_ice_tower_1: LocationData(counter.count()),
    castle_location_names.a1_e_n_fireball_trap: LocationData(counter.count()),
    castle_location_names.a1_e_ne: LocationData(counter.count()),
    castle_location_names.a1_ne_3: LocationData(counter.count()),
    castle_location_names.a1_e_e_fireball_trap: LocationData(counter.count()),
    castle_location_names.a1_e_e: LocationData(counter.count()),
    castle_location_names.a1_e_se: LocationData(counter.count()),
    castle_location_names.a1_s_save_1: LocationData(counter.count()),
    castle_location_names.a1_n_tp: LocationData(counter.count()),
    castle_location_names.a1_nw_bgate: LocationData(counter.count()),
    castle_location_names.a1_n_cache_1: LocationData(counter.count()),
    castle_location_names.a1_from_a2_1: LocationData(counter.count()),
    castle_location_names.a1_from_a2_3: LocationData(counter.count()),
    castle_location_names.a1_red_spikes_2: LocationData(counter.count()),
    castle_location_names.a1_se_cache_4: LocationData(counter.count()),
    castle_location_names.a1_se_cache_2: LocationData(counter.count()),
    castle_location_names.a1_n_cache_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_cache_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_nw_left_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_nw_left_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_nw_left_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_save_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_save_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_ne_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_ne_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_sw_w_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_sw_w_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_m_ice_tower_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_m_ice_tower_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_m_ice_tower_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_nw_right_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_n_cache_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_e_ne_bgate: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_w_save_1: LocationData(counter.count()),
    castle_location_names.a1_ne_top_room_3: LocationData(counter.count()),
    castle_location_names.a1_s_save_2: LocationData(counter.count()),
    castle_location_names.a1_n_cache_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a1_from_a2_2: LocationData(counter.count()),
    castle_location_names.a1_nw_left_5: LocationData(counter.count()),
    castle_location_names.a1_w_save_2: LocationData(counter.count()),
    castle_location_names.a1_ne_ice_tower_secret: LocationData(counter.count()),
    castle_location_names.a1_sw_spikes: LocationData(counter.count()),
    castle_location_names.a1_se_cache_1: LocationData(counter.count()),
    castle_location_names.a1_n_cache_3: LocationData(counter.count()),
    castle_location_names.a1_n_cache_2: LocationData(counter.count()),
    castle_location_names.a1_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.a1_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.a1_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.a1_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    castle_location_names.a2_bonus_return: LocationData(counter.count()),
    castle_location_names.a2_blue_spikes: LocationData(counter.count()),
    castle_location_names.a2_ne_l_bgate: LocationData(counter.count(3)),
    castle_location_names.a2_pyramid_3: LocationData(counter.count()),
    castle_location_names.a2_s_of_n_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_of_n_save_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_nw_ice_tower_across_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_n_of_s_save_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_n_of_s_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_n_of_s_save_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_save_room_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_save_room_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_of_ne_fire_traps_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_fire_trap_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_fire_trap_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_ice_tower_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_of_n_save_1: LocationData(counter.count()),
    castle_location_names.a2_ne_ice_tower_9: LocationData(counter.count()),
    castle_location_names.a2_ne_ice_tower_4: LocationData(counter.count()),
    castle_location_names.a2_e_save_room_1: LocationData(counter.count()),
    castle_location_names.a2_n_of_s_save_4: LocationData(counter.count()),
    castle_location_names.a2_s_of_ne_fire_traps_1: LocationData(counter.count()),
    castle_location_names.a2_e_ice_tower_1: LocationData(counter.count()),
    castle_location_names.a2_sw_ice_tower: LocationData(counter.count()),
    castle_location_names.a2_s_ice_tower_4: LocationData(counter.count()),
    castle_location_names.a2_s_ice_tower_5: LocationData(counter.count()),
    castle_location_names.a2_pyramid_4: LocationData(counter.count(2)),
    castle_location_names.a2_nw_tp: LocationData(counter.count(2)),
    castle_location_names.a2_s_of_e_bgate: LocationData(counter.count()),
    castle_location_names.a2_s_bgate: LocationData(counter.count()),
    castle_location_names.a2_e_ice_tower_4: LocationData(counter.count()),
    castle_location_names.a2_e_ice_tower_5: LocationData(counter.count()),
    castle_location_names.a2_nw_ice_tower_across_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_nw_ice_tower_across_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_nw_ice_tower_across_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_ice_tower_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_ice_tower_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_ice_tower_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_ice_tower_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_n_of_ne_fire_traps_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_n_of_ne_fire_traps_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_save_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_save_room_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_save_room_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_se_of_e_ice_tower_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_se_of_e_ice_tower_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_se_of_e_ice_tower_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_ice_tower_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_ice_tower_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_s_ice_tower_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_of_s_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_of_s_save_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_of_s_save_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_e_of_s_save_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_ice_tower_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_r_bgate_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_r_bgate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_by_w_a1_stair: LocationData(counter.count()),
    castle_location_names.a2_e_ice_tower_2: LocationData(counter.count()),
    castle_location_names.a2_se_tp: LocationData(counter.count(2)),
    castle_location_names.a2_pyramid_1: LocationData(counter.count(2)),
    castle_location_names.a2_ne_ice_tower_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a2_ne_tp: LocationData(counter.count(4)),
    castle_location_names.a2_nw_ice_tower: LocationData(counter.count()),
    castle_location_names.a2_ne_ice_tower_2: LocationData(counter.count()),
    castle_location_names.a2_e_bgate: LocationData(counter.count()),
    castle_location_names.a2_e_ice_tower_6: LocationData(counter.count(2)),
    castle_location_names.a2_sw_ice_tower_tp: LocationData(counter.count()),
    castle_location_names.a2_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.a2_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.a2_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.a2_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    castle_location_names.n2_m_m_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n2_m_m_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n2_nw_top_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_top_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_12: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_13: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_14: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_10: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_15: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_11: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_w_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_bottom_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_bottom_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_bottom_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_nw_bottom_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_12: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_13: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_14: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_12: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_13: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_14: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_10: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_15: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_n_11: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_11: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_10: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_e_15: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_ne_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_ne_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_ne_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_start_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_start_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_start_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_s_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_m_se_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_m_se_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_m_se_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n2_m_n: LocationData(counter.count()),
    castle_location_names.n2_m_m_3: LocationData(counter.count()),
    castle_location_names.n2_ne_4: LocationData(counter.count()),
    castle_location_names.n2_m_e: LocationData(counter.count()),
    castle_location_names.n2_start_1: LocationData(counter.count()),
    castle_location_names.n2_m_se_5: LocationData(counter.count()),
    castle_location_names.n2_m_se_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n2_w_1: LocationData(counter.count()),

    castle_location_names.a3_s_banner_secret: LocationData(counter.count(2)),
    castle_location_names.a3_nw_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_nw_save_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_knife_puzzle_reward_l_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_knife_puzzle_reward_l_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_ne_ice_towers_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_ne_ice_towers_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_ne_ice_towers_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_s_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_s_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_e_ice_towers_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_e_ice_towers_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_sw_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_15: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_11: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_14: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_nw_save_1: LocationData(counter.count()),
    castle_location_names.a3_s_of_knife_puzzle: LocationData(counter.count()),
    castle_location_names.a3_fireball_hall_2: LocationData(counter.count()),
    castle_location_names.a3_pyramids_s_5: LocationData(counter.count()),
    castle_location_names.a3_pyramids_s_4: LocationData(counter.count()),
    castle_location_names.a3_e_ice_towers_3: LocationData(counter.count()),
    castle_location_names.a3_spike_floor_1: LocationData(counter.count()),
    castle_location_names.a3_knife_puzzle_reward_l_5: LocationData(counter.count(2)),
    castle_location_names.a3_knife_puzzle_reward_r: LocationData(counter.count()),
    castle_location_names.a3_secret_shop: LocationData(counter.count()),
    castle_location_names.a3_spike_floor_7: LocationData(counter.count()),
    castle_location_names.a3_spike_floor_4: LocationData(counter.count()),
    castle_location_names.a3_spike_floor_9: LocationData(counter.count()),
    castle_location_names.a3_spike_floor_13: LocationData(counter.count()),
    castle_location_names.a3_s_of_n_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_n_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_n_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_ne_ice_towers_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_ne_ice_towers_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_ne_ice_towers_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_n_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_n_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_s_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_s_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_sw_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_sw_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_se_boss_room_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_se_boss_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_se_boss_room_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_s_of_n_save_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_pyramids_e: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_12: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.a3_spike_floor_2: LocationData(counter.count()),
    castle_location_names.a3_pyramid: LocationData(counter.count(2)),
    castle_location_names.a3_fireball_hall_1: LocationData(counter.count()),
    castle_location_names.a3_e_of_spike_floor: LocationData(counter.count(3)),
    castle_location_names.a3_spike_floor_10: LocationData(counter.count()),
    castle_location_names.a3_m_tp: LocationData(counter.count()),
    castle_location_names.a3_pyramids_s_bgate_tp: LocationData(counter.count()),
    castle_location_names.a3_knife_puzzle_reward_l_2: LocationData(counter.count()),
    castle_location_names.a3_knife_puzzle_reward_l_3: LocationData(counter.count()),

    castle_location_names.b2_boss_reward: LocationData(counter.count()),

    castle_location_names.r1_e_fire_floor_1: LocationData(counter.count(3), LocType.Recovery),
    castle_location_names.r1_e_fire_floor_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_nw_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_nw_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_nw_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ne_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ne_9: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ne_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ne_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_knife_trap_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_knife_trap_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_knife_trap_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_se_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_se_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_se_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_se_wall: LocationData(counter.count()),
    castle_location_names.r1_e_knife_trap_1: LocationData(counter.count()),
    castle_location_names.r1_e_w_1: LocationData(counter.count()),
    castle_location_names.r1_e_s: LocationData(counter.count()),
    castle_location_names.r1_e_e: LocationData(counter.count()),
    castle_location_names.r1_w_knife_trap_1: LocationData(counter.count()),
    castle_location_names.r1_w_knife_trap_5: LocationData(counter.count()),
    castle_location_names.r1_nw_1: LocationData(counter.count()),
    castle_location_names.r1_sw_ne_1: LocationData(counter.count()),
    castle_location_names.r1_e_w_2: LocationData(counter.count()),
    castle_location_names.r1_se_6: LocationData(counter.count()),
    castle_location_names.r1_e_n_1: LocationData(counter.count()),
    castle_location_names.r1_nw_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_ne_ggate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_ne_ggate_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_ne_ggate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_ne_ggate_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ne_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ne_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ne_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_knife_trap_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_knife_trap_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_knife_trap_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_w_knife_trap_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_w_knife_trap_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_w_knife_trap_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ggate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_sw_ggate_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_se_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_se_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_nw_hidden_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_e_s_bgate: LocationData(counter.count()),
    castle_location_names.r1_w_knife_trap_6: LocationData(counter.count()),
    castle_location_names.r1_w_knife_trap_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r1_start_wall: LocationData(counter.count()),
    castle_location_names.r1_nw_hidden_1: LocationData(counter.count()),
    castle_location_names.r1_e_n_3: LocationData(counter.count()),
    castle_location_names.r1_e_fire_floor_3: LocationData(counter.count()),
    castle_location_names.r1_sw_ne_2: LocationData(counter.count()),
    castle_location_names.r1_e_sgate: LocationData(counter.count()),
    castle_location_names.r1_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.r1_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.r1_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.r1_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    castle_location_names.r2_ne_knife_trap_wall_3: LocationData(counter.count()),
    castle_location_names.r2_n_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_bronze_gates_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_bronze_gates_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_start_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_start_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_hall_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_hall_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_by_sgate_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_by_sgate_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_by_sgate_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_ne_knife_trap_wall_2: LocationData(counter.count()),
    castle_location_names.r2_m_spike_trap_2: LocationData(counter.count()),
    castle_location_names.r2_s_knife_trap_4: LocationData(counter.count()),
    castle_location_names.r2_s_knife_trap_5: LocationData(counter.count()),
    castle_location_names.r2_n_bronze_gates_4: LocationData(counter.count()),
    castle_location_names.r2_w_boss_3: LocationData(counter.count()),
    castle_location_names.r2_n_bronze_gates_1: LocationData(counter.count()),
    castle_location_names.r2_start: LocationData(counter.count()),
    castle_location_names.r2_m_e_of_spike_trap_3: LocationData(counter.count()),
    castle_location_names.r2_by_sgate_1: LocationData(counter.count()),
    castle_location_names.r2_m_spike_trap_10: LocationData(counter.count()),
    castle_location_names.r2_s_knife_trap_2: LocationData(counter.count()),
    castle_location_names.r2_w_island: LocationData(counter.count()),
    castle_location_names.r2_nw_spike_trap_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_nw_spike_trap_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_closed_room: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_w_boss_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_by_sgate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_hall_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_hall_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_spike_trap_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_e_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_w_boss_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_w_boss_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_w_boss_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_w_boss_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_e_of_spike_trap_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_e_of_spike_trap_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_e_of_spike_trap_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_8: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_9: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_10: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_11: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_sw_12: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_by_sgate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_by_sgate_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_by_sgate_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_spike_trap_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_spike_trap_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_spike_trap_9: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_spike_trap_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_se_save: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_ne_knife_trap_wall_1: LocationData(counter.count()),
    castle_location_names.r2_m_spike_trap_4: LocationData(counter.count()),
    castle_location_names.r2_w_boss_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_m_spike_trap_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r2_s_knife_trap_3: LocationData(counter.count()),
    castle_location_names.r2_ne_knife_trap_end: LocationData(counter.count()),
    castle_location_names.r2_n_1: LocationData(counter.count()),
    castle_location_names.r2_w_boss_2: LocationData(counter.count()),
    castle_location_names.r2_e_5: LocationData(counter.count()),
    castle_location_names.r2_sw_1: LocationData(counter.count()),
    castle_location_names.r2_m_spike_trap_1: LocationData(counter.count()),
    castle_location_names.r2_s_knife_trap_1: LocationData(counter.count()),
    castle_location_names.r2_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.r2_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.r2_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.r2_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    castle_location_names.r3_e_secret_tp: LocationData(counter.count(2)),
    castle_location_names.r3_e_shops_puzzle_reward: LocationData(counter.count()),
    castle_location_names.r3_e_ggate_hallway_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_ggate_hallway_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_ne_knife_trap_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_ne_knife_trap_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_fire_floor_n_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_fire_floor_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_sw_bgate_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_sw_bgate_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_sw_bgate_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_s_shops_room_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_s_shops_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_boss_switch_room_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_bonus_return_1: LocationData(counter.count()),
    castle_location_names.r3_bonus_return_2: LocationData(counter.count()),
    castle_location_names.r3_w_passage_behind_spikes: LocationData(counter.count()),
    castle_location_names.r3_w_passage_s_closed_room: LocationData(counter.count()),
    castle_location_names.r3_n_bgate_e: LocationData(counter.count()),
    castle_location_names.r3_w_fire_floor_1: LocationData(counter.count()),
    castle_location_names.r3_start: LocationData(counter.count()),
    castle_location_names.r3_e_miniboss: LocationData(counter.count()),
    castle_location_names.r3_e_fire_floor_w: LocationData(counter.count()),
    castle_location_names.r3_boss_switch_room_1: LocationData(counter.count()),
    castle_location_names.r3_nw_save_2: LocationData(counter.count()),
    castle_location_names.r3_e_tp: LocationData(counter.count(2)),
    castle_location_names.r3_ne_save_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_ne_save_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_start_nw_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_sw_bgate_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_sw_bgate_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_boss_switch_room_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_n_miniboss_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_n_miniboss_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_n_miniboss_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_shops_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_shops_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_start_nw_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_start_nw_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_fire_floor_n_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_fire_floor_n_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_fire_floor_n_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_shops_room_e_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_shops_room_e_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_shops_room_e_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_ggate_hallway_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_s_of_boss_door_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_w_fire_floor_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_e_fire_floor_e: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_w_ggate_w: LocationData(counter.count()),
    castle_location_names.r3_s_save: LocationData(counter.count()),
    castle_location_names.r3_nw_save_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.r3_n_miniboss_1: LocationData(counter.count()),
    castle_location_names.r3_e_shops_3: LocationData(counter.count(2)),
    castle_location_names.r3_s_of_boss_door_1: LocationData(counter.count()),
    castle_location_names.r3_e_fire_floor_secret: LocationData(counter.count()),
    castle_location_names.r3_shops_room_secret: LocationData(counter.count()),
    castle_location_names.r3_nw_tp: LocationData(counter.count()),
    castle_location_names.r3_sw_hidden_room_1: LocationData(counter.count()),
    castle_location_names.r3_sw_hidden_room_2: LocationData(counter.count()),
    castle_location_names.r3_s_shops_room_left_shop: LocationData(counter.count()),

    castle_location_names.n3_tp_room: LocationData(counter.count()),
    castle_location_names.n3_tp_room_n_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n3_tp_room_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n3_exit_e_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_e_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_nw_cluster_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_s_cluster_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_se_cluster_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_tp_room_e_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_tp_room_e_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_tp_room_e_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_tp_room_e_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_m_cluster_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_se_cluster_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n3_exit_sw: LocationData(counter.count()),
    castle_location_names.n3_m_cluster_5: LocationData(counter.count()),
    castle_location_names.n3_se_cluster_5: LocationData(counter.count()),
    castle_location_names.n3_exit_s: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.n3_exit_se: LocationData(counter.count()),

    castle_location_names.b3_reward: LocationData(counter.count()),

    castle_location_names.c1_n_spikes_1: LocationData(counter.count()),
    castle_location_names.c1_ledge_1: LocationData(counter.count()),
    castle_location_names.c1_prison_stairs: LocationData(counter.count()),
    castle_location_names.c1_n_alcove_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c1_n_alcove_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c1_s_ice_towers_4: LocationData(counter.count()),
    castle_location_names.c1_s_ice_towers_6: LocationData(counter.count()),
    castle_location_names.c1_n_ice_tower_3: LocationData(counter.count()),
    castle_location_names.c1_n_ice_tower_1: LocationData(counter.count()),
    castle_location_names.c1_n_alcove_1: LocationData(counter.count()),
    castle_location_names.c1_ne: LocationData(counter.count()),
    castle_location_names.c1_w_1: LocationData(counter.count()),
    castle_location_names.c1_w_2: LocationData(counter.count()),
    castle_location_names.c1_w_3: LocationData(counter.count()),
    castle_location_names.c1_s_ice_towers_1: LocationData(counter.count()),
    castle_location_names.c1_s_ice_towers_2: LocationData(counter.count()),
    castle_location_names.c1_start: LocationData(counter.count()),
    castle_location_names.c1_s_ice_towers_3: LocationData(counter.count()),
    castle_location_names.c1_s_ice_towers_5: LocationData(counter.count()),
    castle_location_names.c1_se_spikes: LocationData(counter.count()),
    castle_location_names.c1_n_ice_tower_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c1_m_knife_traps: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c1_n_alcove_4: LocationData(counter.count()),
    castle_location_names.c1_ne_knife_traps_1: LocationData(counter.count()),
    castle_location_names.c1_tp_island_2: LocationData(counter.count()),
    castle_location_names.c1_n_spikes_2: LocationData(counter.count()),
    castle_location_names.c1_ne_knife_traps_2: LocationData(counter.count()),
    castle_location_names.c1_tp_island_1: LocationData(counter.count()),
    castle_location_names.c1_ledge_2: LocationData(counter.count()),
    castle_location_names.c1_sgate: LocationData(counter.count()),

    castle_location_names.pstart_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.pstart_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.pstart_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.pstart_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    castle_location_names.c2_bonus_return: LocationData(counter.count()),
    castle_location_names.c2_ne_platform_5: LocationData(counter.count(2)),
    castle_location_names.c2_by_w_shops_2: LocationData(counter.count()),
    castle_location_names.c2_e_fire_floor_1: LocationData(counter.count()),
    castle_location_names.c2_w_spikes_2: LocationData(counter.count()),
    castle_location_names.c2_w_spikes_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_spikes_s_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_sw_ice_tower_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_sw_ice_tower_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_spikes_e_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_spikes_e_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_save: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_alcove_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_alcove_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_by_w_shops_3_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_by_w_shops_3_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_by_e_shops_2_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_by_e_shops_2_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_e_fire_floor_w_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_e_fire_floor_w_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_knife_traps_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_knife_traps_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_s_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_start_s_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_start_s_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_start_s_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_alcove_4: LocationData(counter.count()),
    castle_location_names.c2_w_alcove_3: LocationData(counter.count()),
    castle_location_names.c2_w_spikes_s_3: LocationData(counter.count()),
    castle_location_names.c2_w_spikes_e_3: LocationData(counter.count()),
    castle_location_names.c2_ne_platform_n_1: LocationData(counter.count()),
    castle_location_names.c2_ne_5: LocationData(counter.count()),
    castle_location_names.c2_ne_platform_4: LocationData(counter.count()),
    castle_location_names.c2_by_tp_island_1: LocationData(counter.count()),
    castle_location_names.c2_w_spikes_s_7: LocationData(counter.count()),
    castle_location_names.c2_w_save_wall: LocationData(counter.count()),
    castle_location_names.c2_w_knife_traps_2: LocationData(counter.count()),
    castle_location_names.c2_by_e_shops_2: LocationData(counter.count()),
    castle_location_names.c2_w_knife_traps_4: LocationData(counter.count()),
    castle_location_names.c2_s_1: LocationData(counter.count()),
    castle_location_names.c2_s_6: LocationData(counter.count()),
    castle_location_names.c2_start_s_1: LocationData(counter.count()),
    castle_location_names.c2_se_flame_turrets_1: LocationData(counter.count()),
    castle_location_names.c2_se_flame_turrets_4: LocationData(counter.count()),
    castle_location_names.c2_nw_ledge_4: LocationData(counter.count(2)),
    castle_location_names.c2_exit: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_platform_n_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_platform_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_by_tp_island_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_knife_traps_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_s_7: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_se_flame_turrets_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_sw_ice_tower_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_sw_ice_tower_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_sw_ice_tower_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_spikes_s_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_spikes_s_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_spikes_s_6: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_platform_n_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_platform_n_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_e_fire_floor_w_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_e_fire_floor_w_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_e_fire_floor_w_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_start_s_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_start_s_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_start_s_4: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_ne_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_by_tp_island_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_by_w_shops_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_boss_portal: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_knife_traps_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_s_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_se_flame_turrets_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_se_flame_turrets_5: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_e_fire_floor_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_w_spikes_1: LocationData(counter.count(3)),
    castle_location_names.c2_w_spikes_4: LocationData(counter.count()),
    castle_location_names.c2_ne_platform_1: LocationData(counter.count()),
    castle_location_names.c2_w_spikes_e_4: LocationData(counter.count()),
    castle_location_names.c2_nw_ledge_1: LocationData(counter.count()),
    castle_location_names.c2_nw_ledge_2: LocationData(counter.count()),
    castle_location_names.c2_nw_ledge_5: LocationData(counter.count()),
    castle_location_names.c2_nw_ledge_6: LocationData(counter.count()),
    castle_location_names.c2_nw_ledge_3: LocationData(counter.count()),
    castle_location_names.c2_nw_ledge_7: LocationData(counter.count()),
    castle_location_names.c2_ne_platform_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c2_n_wall: LocationData(counter.count()),
    castle_location_names.c2_sw_ice_tower_6: LocationData(counter.count(2)),
    castle_location_names.c2_ne_platform_2: LocationData(counter.count()),
    castle_location_names.c2_s_4: LocationData(counter.count()),
    castle_location_names.c2_w_spikes_3: LocationData(counter.count()),
    castle_location_names.c2_nw_knife_traps_1: LocationData(counter.count()),
    castle_location_names.c2_nw_knife_traps_2: LocationData(counter.count()),
    castle_location_names.c2_nw_knife_traps_4: LocationData(counter.count()),
    castle_location_names.c2_nw_knife_traps_5: LocationData(counter.count()),
    castle_location_names.c2_nw_knife_traps_3: LocationData(counter.count()),
    castle_location_names.c2_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.c2_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.c2_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    castle_location_names.c2_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    castle_location_names.n4_e_11: LocationData(counter.count()),
    castle_location_names.n4_w_7: LocationData(counter.count()),
    castle_location_names.n4_nw_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_10: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_11: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_14: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_15: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_16: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_13: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_nw_12: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_24: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_16: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_7: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_6: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_14: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_15: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_22: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_20: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_19: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_18: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_17: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_10: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_12: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_13: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_5: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_4: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_3: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_2: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_1: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_8: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_10: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_11: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_12: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_13: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_14: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_w_9: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_25: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_26: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_27: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_28: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_29: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_30: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_31: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_e_32: LocationData(counter.count(), LocType.Bonus),
    castle_location_names.n4_ne: LocationData(counter.count()),
    castle_location_names.n4_by_w_room_1: LocationData(counter.count()),
    castle_location_names.n4_by_exit: LocationData(counter.count()),
    castle_location_names.n4_by_w_room_2: LocationData(counter.count()),
    castle_location_names.n4_e_23: LocationData(counter.count()),
    castle_location_names.n4_e_21: LocationData(counter.count()),

    castle_location_names.c3_nw_ice_towers_3: LocationData(counter.count()),
    castle_location_names.c3_c2_tp: LocationData(counter.count()),
    castle_location_names.c3_light_bridge_2: LocationData(counter.count()),
    castle_location_names.c3_fire_floor_3: LocationData(counter.count()),
    castle_location_names.c3_nw_ice_towers_w: LocationData(counter.count()),
    castle_location_names.c3_start_e: LocationData(counter.count()),
    castle_location_names.c3_w_ledge_2: LocationData(counter.count()),
    castle_location_names.c3_w_ledge_1: LocationData(counter.count()),
    castle_location_names.c3_m_wall: LocationData(counter.count()),
    castle_location_names.c3_m_ice_towers_1: LocationData(counter.count()),
    castle_location_names.c3_m_ice_towers_4: LocationData(counter.count()),
    castle_location_names.c3_se_save_1: LocationData(counter.count()),
    castle_location_names.c3_e_miniboss: LocationData(counter.count()),
    castle_location_names.c3_se_save_2: LocationData(counter.count()),
    castle_location_names.c3_sw_save_1: LocationData(counter.count()),
    castle_location_names.c3_sw_save_2: LocationData(counter.count()),
    castle_location_names.c3_sw_save_3: LocationData(counter.count()),
    castle_location_names.c3_fire_floor_w: LocationData(counter.count()),
    castle_location_names.c3_s_bgate: LocationData(counter.count()),
    castle_location_names.c3_ne_npc_2: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c3_ne_npc_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c3_ne_npc_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c3_fire_floor_1: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c3_easter_egg: LocationData(counter.count()),
    castle_location_names.c3_fire_floor_2: LocationData(counter.count()),
    castle_location_names.c3_n_spike_floor_1: LocationData(counter.count()),
    castle_location_names.c3_boss_switch: LocationData(counter.count()),
    castle_location_names.c3_light_bridge_1: LocationData(counter.count()),
    castle_location_names.c3_light_bridge_3: LocationData(counter.count()),
    castle_location_names.c3_m_ice_towers_3: LocationData(counter.count()),
    castle_location_names.c3_sw_hidden: LocationData(counter.count()),
    castle_location_names.c3_se_save_3: LocationData(counter.count(), LocType.Recovery),
    castle_location_names.c3_nw_ice_towers_2: LocationData(counter.count()),
    castle_location_names.c3_nw_ice_towers_1: LocationData(counter.count()),
    castle_location_names.c3_n_spike_floor_2: LocationData(counter.count()),
    castle_location_names.c3_m_ice_towers_2: LocationData(counter.count(2)),
    castle_location_names.c3_m_tp: LocationData(counter.count(2)),
    castle_location_names.c3_fire_floor_tp: LocationData(counter.count()),

    castle_location_names.b4_e_2: LocationData(counter.count()),
    castle_location_names.b4_w_10: LocationData(counter.count()),
    castle_location_names.b4_w_2: LocationData(counter.count()),
    castle_location_names.b4_dragon_6: LocationData(counter.count()),
    castle_location_names.b4_dragon_2: LocationData(counter.count()),
    castle_location_names.b4_w_11: LocationData(counter.count()),
    castle_location_names.b4_w_1: LocationData(counter.count()),
    castle_location_names.b4_w_3: LocationData(counter.count()),
    castle_location_names.b4_e_3: LocationData(counter.count()),
    castle_location_names.b4_e_4: LocationData(counter.count()),
    castle_location_names.b4_e_1: LocationData(counter.count()),
    castle_location_names.b4_dragon_9: LocationData(counter.count()),
    castle_location_names.b4_plank_1: LocationData(counter.count()),
    castle_location_names.b4_plank_2: LocationData(counter.count()),
    castle_location_names.b4_plank_3: LocationData(counter.count()),
    castle_location_names.b4_plank_4: LocationData(counter.count()),
    castle_location_names.b4_plank_5: LocationData(counter.count()),
    castle_location_names.b4_plank_6: LocationData(counter.count()),
    castle_location_names.b4_plank_7: LocationData(counter.count()),
    castle_location_names.b4_plank_8: LocationData(counter.count()),
    castle_location_names.b4_plank_9: LocationData(counter.count()),
    castle_location_names.b4_plank_10: LocationData(counter.count()),
    castle_location_names.b4_plank_11: LocationData(counter.count()),
    castle_location_names.b4_w_9: LocationData(counter.count()),
    castle_location_names.b4_w_6: LocationData(counter.count()),
    castle_location_names.b4_w_4: LocationData(counter.count()),
    castle_location_names.b4_dragon_4: LocationData(counter.count()),
    castle_location_names.b4_dragon_7: LocationData(counter.count()),
    castle_location_names.b4_dragon_11: LocationData(counter.count()),
    castle_location_names.b4_dragon_12: LocationData(counter.count()),
    castle_location_names.b4_e_8: LocationData(counter.count()),
    castle_location_names.b4_w_12: LocationData(counter.count()),
    castle_location_names.b4_e_7: LocationData(counter.count()),
    castle_location_names.b4_w_5: LocationData(counter.count()),
    castle_location_names.b4_w_7: LocationData(counter.count()),
    castle_location_names.b4_w_8: LocationData(counter.count()),
    castle_location_names.b4_e_6: LocationData(counter.count()),
    castle_location_names.b4_e_5: LocationData(counter.count()),
    castle_location_names.b4_dragon_10: LocationData(counter.count()),
    castle_location_names.b4_dragon_5: LocationData(counter.count()),
    castle_location_names.b4_dragon_3: LocationData(counter.count()),
    castle_location_names.b4_dragon_8: LocationData(counter.count()),
    castle_location_names.b4_dragon_1: LocationData(counter.count()),

    castle_location_names.e2_entrance: LocationData(counter.count(4), LocType.Recovery),
    castle_location_names.e2_end: LocationData(counter.count(), LocType.Recovery),

    castle_location_names.e3_entrance_1: LocationData(counter.count(3), LocType.Recovery),
    castle_location_names.e3_entrance_2: LocationData(counter.count(), LocType.Recovery),

    castle_location_names.e4_main: LocationData(counter.count(15), LocType.Recovery),
}

castle_enemy_loot_locations: typing.Dict[str, LocationData] = {
    castle_location_names.p2_miniboss_tick_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p2_miniboss_tick_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p2_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p2_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_miniboss_tick_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_miniboss_tick_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_7: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.p3_tower_plant_8: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a1_miniboss_skeleton_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a1_miniboss_skeleton_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a1_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a1_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a1_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a1_tower_ice_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_miniboss_skeleton_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_miniboss_skeleton_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_tower_ice_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_tower_ice_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a2_tower_ice_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_miniboss_skeleton_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_miniboss_skeleton_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_7: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_8: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.a3_tower_ice_9: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r1_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r1_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r1_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r1_tower_plant_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_miniboss_eye_w_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_miniboss_eye_w_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_miniboss_eye_e_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_miniboss_eye_e_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_tower_plant_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r2_tower_plant_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_miniboss_eye_n_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_miniboss_eye_n_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_miniboss_eye_e_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_miniboss_eye_e_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_miniboss_eye_s_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_miniboss_eye_s_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_7: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_8: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_9: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.r3_tower_plant_10: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c1_miniboss_lich_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c1_miniboss_lich_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c1_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c1_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c1_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c1_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c1_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_miniboss_lich_ne_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_miniboss_lich_ne_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_miniboss_lich_n_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_miniboss_lich_n_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_miniboss_lich_m_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_miniboss_lich_m_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_7: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_plant_8: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_7: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_8: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_9: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_10: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c2_tower_ice_11: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_miniboss_lich_e_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_miniboss_lich_e_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_miniboss_lich_sw_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_miniboss_lich_sw_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_plant_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_plant_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_plant_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_4: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_5: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_6: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_7: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_8: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_9: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.c3_tower_ice_10: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.b2_boss: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.b3_boss: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.b4_miniboss_lich_1: LocationData(counter.count(), LocType.EnemyLoot),
    castle_location_names.b4_miniboss_lich_2: LocationData(counter.count(), LocType.EnemyLoot),
}

castle_button_locations: typing.Dict[str, LocationData] = {
    castle_location_names.btn_p1_boss: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p1_boss_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p1_boss_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p1_boss_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p1_boss_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p1_floor: LocationData(counter.count(2), LocType.Button),
    castle_location_names.btn_p2_boss: LocationData(counter.count(6), LocType.Button),
    castle_location_names.btn_p2_boss_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_boss_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_boss_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_boss_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_floor_spike_puzzle_e_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_n_3: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_n_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_e_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_n_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_e_3: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_s_3: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_s_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_spike_puzzle_s_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_red: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_tp_item_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_tp_item_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_floor_e_save: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    castle_location_names.btn_p2_rune_puzzle: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_rune_puzzle_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_rune_sequence: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_rune_sequence_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_rune_puzzle_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_rune_sequence_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_rune_puzzle_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_rune_sequence_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_rune_puzzle_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_rune_sequence_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p2_wall_from_p1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_wall_shortcut_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p2_wall_shortcut_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_boss_door: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_boss_s: LocationData(counter.count(2), LocType.Button),
    castle_location_names.btn_p3_boss_s_3: LocationData(counter.count(5), LocType.Buttoninsanity),
    castle_location_names.btn_p3_boss_s_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_boss_s_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_boss_s_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_floor: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_floor_red: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_floor_blue: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_floor_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_floor_arrow_hall: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_rune_bonus_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_6: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_5: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_7: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_8: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_rune_bonus_9: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_wall_bonus_nw: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_wall_start: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_start_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_bonus: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_bonus_ne: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_wall_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_bonus_w_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_wall_bonus_w_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_bonus_s: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_wall_bonus_se: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_p3_wall_secret_arrow_hall: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_boss_door: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_to_p1_s: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_b1_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_b1_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_boss_door: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_boss: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_boss_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_boss_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_boss_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_boss_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_floor_tp_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_floor_shortcut: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_floor_red: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_floor_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    castle_location_names.btn_a1_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_rune_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_rune_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_rune_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_rune_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a1_wall_m_cache: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_wall_red_spikes: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_wall_start: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a1_wall_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_boss: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_boss_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_boss_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_boss_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_boss_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_floor_pyramid_nw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_tp_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_pyramid_ne: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_pyramid_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_pyramid_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_pyramid_m: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_secret_e: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_floor_tp_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    castle_location_names.btn_a2_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_rune_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_rune_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_rune_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_rune_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a2_wall_nw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_wall_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_wall_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a2_wall_e: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n2_floor_blue: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_boss: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_boss_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_boss_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_boss_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_boss_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_floor_knife_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_floor_knife_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_floor_knife_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_floor_knife_5: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_floor_knife_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_floor_tp_m: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_floor_stairs_in_wall: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_wall_knife_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_wall_knife_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_a3_wall_from_a2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_wall_start: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_wall_end: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_nw_hidden: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_ne: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_nw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_e: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_w_s: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_w_shop: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_floor_exit: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    castle_location_names.btn_r1_wall_ne: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_wall_w: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r1_wall_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_boss_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_boss_e: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_boss_n_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_boss_n_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_boss_n_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_boss_n_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_boss_e_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_boss_e_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_boss_e_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_boss_e_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_floor_nw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_floor_boss_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_floor_ne: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_floor_gate_w: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_floor_gate_s: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_floor_e: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_floor_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    castle_location_names.btn_r2_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_rune_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_rune_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_rune_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_rune_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r2_wall_nw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_wall_start: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_wall_spike_island_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_wall_spike_island_s: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_wall_ne: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_boss_door: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_boss: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_boss_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_boss_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_boss_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_boss_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_floor_passage: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_passage_end: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_gate_nw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_ne: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_passage_room_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_ne_room: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_s_room: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_s: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_simon: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_rune_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_simon: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_simon_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_rune_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_simon_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_rune_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_simon_5: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_rune_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_simon_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_simon_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_simon_6: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_wall_passage_room_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_wall_passage_room_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_wall_ne_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_wall_ne_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_wall_seq_n: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_wall_seq_ne: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_wall_sw_gate: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_wall_seq_w: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_wall_seq_m: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_r3_wall_seq_se: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c1_floor_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c1_floor_red: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c1_wall_red: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c1_wall_ledge: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c1_wall_s_gate: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_pstart_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    castle_location_names.btn_pstart_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_pstart_rune_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_pstart_rune_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_pstart_rune_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_pstart_rune_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_w: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_boss_e: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_boss_w_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_w_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_w_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_w_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_e_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_e_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_e_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_boss_e_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_floor_sw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_floor_t_hall: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_floor_w: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    castle_location_names.btn_c2_rune_bonus: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_rune_bonus_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_rune_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_bonus_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_bonus_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_bonus_8: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_bonus_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_bonus_6: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_bonus_7: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_rune_bonus_5: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_wall_seq_nw: LocationData(counter.count(10), LocType.Buttoninsanity),
    castle_location_names.btn_c2_wall_seq_ne: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_wall_n_exit_gate: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_wall_seq_w: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_wall_seq_s: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_wall_seq_e: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c2_wall_red_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_wall_blue: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_wall_portal_shop: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_wall_e_shop: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_wall_red_s: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_wall_s_save: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_boss: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_boss_1: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_boss_3: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_boss_2: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_boss_4: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_floor: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_rune: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_rune_s: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_rune_se: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_rune_w: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_rune_e: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_rune_n: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_rune_ne: LocationData(counter.count(), LocType.Buttoninsanity),
    castle_location_names.btn_c3_wall_red: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_wall_blue: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_wall_w: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_wall_shop: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_wall_fire_floor: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_wall_se_hidden: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n1_panel_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n1_panel_e_1: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n1_panel_e_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n1_panel_s: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n2_panel_n: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n2_panel_se: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_n2_panel_ne: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_wall_start_nw: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_rune_bonus: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r2_floor_sw_hidden: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_floor_sw_gate: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c1_wall_portal: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c3_wall_sw_hidden: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_p3_seq_bonus: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_seq_knife: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_a3_seq_knife_2: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_r3_seq_simon_room: LocationData(counter.count(), LocType.Button),
    castle_location_names.btn_c2_seq_bonus: LocationData(counter.count(), LocType.Button),
}

castle_combo_button_locations: typing.List[str] = [
    castle_location_names.btn_p1_boss,
    castle_location_names.btn_p2_boss,
    castle_location_names.btn_p3_boss_s,
    castle_location_names.btn_a1_boss,
    castle_location_names.btn_a2_boss,
    castle_location_names.btn_a3_boss,
    castle_location_names.btn_r2_boss_e,
    castle_location_names.btn_r2_boss_n,
    castle_location_names.btn_r3_boss,
    castle_location_names.btn_c2_boss_e,
    castle_location_names.btn_c2_boss_w,
    castle_location_names.btn_c3_boss,
    castle_location_names.btn_p2_rune_puzzle,
    castle_location_names.btn_p2_rune_sequence,
    castle_location_names.btn_p3_rune_bonus,
    castle_location_names.btn_a1_rune,
    castle_location_names.btn_a2_rune,
    castle_location_names.btn_r2_rune,
    castle_location_names.btn_r3_rune,
    castle_location_names.btn_r3_simon,
    castle_location_names.btn_pstart_rune,
    castle_location_names.btn_c2_rune,
    castle_location_names.btn_c2_rune_bonus,
    castle_location_names.btn_p3_seq_bonus,
    castle_location_names.btn_a3_seq_knife,
    castle_location_names.btn_a3_seq_knife_2,
    castle_location_names.btn_r3_seq_simon_room,
    castle_location_names.btn_c2_seq_bonus,
]

castle_event_buttons: typing.Dict[str, str] = {
    castle_location_names.btn_p1_floor: item_name.btnc_p1_floor,
    castle_location_names.btn_p2_rune_sequence_2: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p2_rune_sequence_1: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p2_rune_sequence_4: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p2_rune_sequence_3: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p3_floor_sw: item_name.btnc_p3_e_passage,
    castle_location_names.btn_p3_wall_secret_arrow_hall: item_name.btnc_p3_s_passage,
    castle_location_names.btn_n2_floor_blue: item_name.btnc_a2_blue_spikes,
    castle_location_names.btn_a2_floor_tp_n: item_name.btnc_a2_bspikes_tp,
    castle_location_names.btn_a3_floor_stairs_in_wall: item_name.btnc_a3_bgate_tp,
    castle_location_names.btn_c2_wall_n_exit_gate: item_name.btnc_c2_n_room,
    castle_location_names.btn_c2_floor_t_hall: item_name.btnc_c2_n_shops,
    castle_location_names.btn_c3_wall_red: item_name.btnc_c3_red_spikes,
    castle_location_names.btn_c3_rune_n: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_ne: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_e: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_se: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_w: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_s: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_wall_fire_floor: item_name.btnc_c3_tp_se,

    castle_location_names.btn_p1_boss: item_name.btnc_b1_rune_1,
    castle_location_names.btn_p2_boss: item_name.btnc_b1_rune_2,
    castle_location_names.btn_p3_boss_s: item_name.btnc_b1_rune_3,
    castle_location_names.btn_a1_boss: item_name.btnc_b2_rune_1,
    castle_location_names.btn_a2_boss: item_name.btnc_b2_rune_2,
    castle_location_names.btn_a3_boss: item_name.btnc_b2_rune_3,
    castle_location_names.btn_r2_boss_e: item_name.btnc_b3_rune_1,
    castle_location_names.btn_r2_boss_n: item_name.btnc_b3_rune_2,
    castle_location_names.btn_r3_boss: item_name.btnc_b3_rune_3,
    castle_location_names.btn_c2_boss_e: item_name.btnc_b4_rune_1,
    castle_location_names.btn_c2_boss_w: item_name.btnc_b4_rune_2,
    castle_location_names.btn_c3_boss: item_name.btnc_b4_rune_3,
}


castle_locations: typing.Dict[str, LocationData] = {
    **castle_pickup_locations,
    **castle_enemy_loot_locations,
    **castle_button_locations,
}
castle_button_items: typing.Dict[str, str] = {
    castle_location_names.btn_p1_boss: item_name.btnc_b1_rune_1,
    castle_location_names.btn_p1_boss_1: item_name.btnc_b1_rune_1_part,
    castle_location_names.btn_p1_boss_2: item_name.btnc_b1_rune_1_part,
    castle_location_names.btn_p1_boss_3: item_name.btnc_b1_rune_1_part,
    castle_location_names.btn_p1_boss_4: item_name.btnc_b1_rune_1_part,
    castle_location_names.btn_p1_floor: item_name.btnc_p1_floor,
    castle_location_names.btn_p2_boss: item_name.btnc_b1_rune_2,
    castle_location_names.btn_p2_boss_2: item_name.btnc_b1_rune_2_part,
    castle_location_names.btn_p2_boss_4: item_name.btnc_b1_rune_2_part,
    castle_location_names.btn_p2_boss_1: item_name.btnc_b1_rune_2_part,
    castle_location_names.btn_p2_boss_3: item_name.btnc_b1_rune_2_part,
    castle_location_names.btn_p2_floor_spike_puzzle_e_1: item_name.btnc_p2_spike_puzzle_r_part,
    castle_location_names.btn_p2_floor_spike_puzzle_e_2: item_name.btnc_p2_spike_puzzle_r_part,
    castle_location_names.btn_p2_floor_spike_puzzle_e_3: item_name.btnc_p2_spike_puzzle_r_part,
    castle_location_names.btn_p2_floor_spike_puzzle_n_3: item_name.btnc_p2_spike_puzzle_t_part,
    castle_location_names.btn_p2_floor_spike_puzzle_n_2: item_name.btnc_p2_spike_puzzle_t_part,
    castle_location_names.btn_p2_floor_spike_puzzle_n_1: item_name.btnc_p2_spike_puzzle_t_part,
    castle_location_names.btn_p2_floor_spike_puzzle_s_3: item_name.btnc_p2_spike_puzzle_b_part,
    castle_location_names.btn_p2_floor_spike_puzzle_s_2: item_name.btnc_p2_spike_puzzle_b_part,
    castle_location_names.btn_p2_floor_spike_puzzle_s_1: item_name.btnc_p2_spike_puzzle_b_part,
    castle_location_names.btn_p2_floor_red: item_name.btnc_p2_red_spikes,
    castle_location_names.btn_p2_floor_tp_item_2: item_name.btnc_p2_tp_jail,
    castle_location_names.btn_p2_floor_tp_item_1: item_name.btnc_p2_open_w_jail,
    castle_location_names.btn_p2_floor_e_save: item_name.btnc_p2_e_save,
    castle_location_names.btn_p2_puzzle: item_name.btnc_p2_puzzle,
    castle_location_names.btn_p2_rune_puzzle: item_name.btnc_p2_tp_w,
    castle_location_names.btn_p2_rune_puzzle_1: item_name.btnc_p2_tp_w_part,
    castle_location_names.btn_p2_rune_puzzle_2: item_name.btnc_p2_tp_w_part,
    castle_location_names.btn_p2_rune_puzzle_3: item_name.btnc_p2_tp_w_part,
    castle_location_names.btn_p2_rune_puzzle_4: item_name.btnc_p2_tp_w_part,
    castle_location_names.btn_p2_rune_sequence: item_name.btnc_p2_rune_sequence,
    castle_location_names.btn_p2_rune_sequence_1: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p2_rune_sequence_2: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p2_rune_sequence_4: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p2_rune_sequence_3: item_name.btnc_p2_rune_sequence_part,
    castle_location_names.btn_p2_wall_from_p1: item_name.btnc_p2_m_stairs,
    castle_location_names.btn_p2_wall_shortcut_1: item_name.btnc_p2_shortcut_n,
    castle_location_names.btn_p2_wall_shortcut_2: item_name.btnc_p2_shortcut_s,
    castle_location_names.btn_p3_boss_door: item_name.btnc_p3_boss_door,
    castle_location_names.btn_p3_boss_s: item_name.btnc_b1_rune_3,
    castle_location_names.btn_p3_boss_s_3: item_name.btnc_b1_rune_3_part,
    castle_location_names.btn_p3_boss_s_4: item_name.btnc_b1_rune_3_part,
    castle_location_names.btn_p3_boss_s_1: item_name.btnc_b1_rune_3_part,
    castle_location_names.btn_p3_boss_s_2: item_name.btnc_b1_rune_3_part,
    castle_location_names.btn_p3_floor: item_name.btnc_p3_sgate_spikes,
    castle_location_names.btn_p3_floor_red: item_name.btnc_p3_red_spikes,
    castle_location_names.btn_p3_floor_blue: item_name.btnc_p3_blue_spikes,
    castle_location_names.btn_p3_floor_sw: item_name.btnc_p3_e_passage,
    castle_location_names.btn_p3_floor_arrow_hall: item_name.btnc_p3_s_spikes,
    castle_location_names.btn_p3_rune_bonus_1: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_4: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_2: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_6: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_3: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_5: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_7: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_8: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_rune_bonus_9: item_name.btnc_p3_portal_part,
    castle_location_names.btn_p3_wall_bonus_nw: item_name.btnc_p3_open_bonus_part,
    castle_location_names.btn_p3_wall_start: item_name.btnc_p3_start,
    castle_location_names.btn_p3_wall_start_n: item_name.btnc_p3_shop,
    castle_location_names.btn_p3_wall_bonus: item_name.btnc_p3_bonus_side,
    castle_location_names.btn_p3_wall_bonus_ne: item_name.btnc_p3_open_bonus_part,
    castle_location_names.btn_p3_wall_sw: item_name.btnc_p3_sw_shortcut,
    castle_location_names.btn_p3_wall_bonus_w_1: item_name.btnc_p3_open_bonus_part,
    castle_location_names.btn_p3_wall_bonus_w_2: item_name.btnc_p3_open_n_shortcut,
    castle_location_names.btn_p3_wall_bonus_s: item_name.btnc_p3_open_bonus_part,
    castle_location_names.btn_p3_wall_bonus_se: item_name.btnc_p3_open_bonus_part,
    castle_location_names.btn_p3_wall_secret_arrow_hall: item_name.btnc_p3_s_passage,
    castle_location_names.btn_p3_wall_boss_door: item_name.btnc_p3_s_exit_l,
    castle_location_names.btn_p3_wall_to_p1_s: item_name.btnc_p3_s_exit_r,
    castle_location_names.btn_b1_1: item_name.btnc_b1_pillars,
    # castle_location_names.btn_b1_2: item_name.btnc_b1_right,
    castle_location_names.btn_a1_boss_door: item_name.btnc_a1_boss_door,
    castle_location_names.btn_a1_boss: item_name.btnc_b2_rune_1,
    castle_location_names.btn_a1_boss_2: item_name.btnc_b2_rune_1_part,
    castle_location_names.btn_a1_boss_1: item_name.btnc_b2_rune_1_part,
    castle_location_names.btn_a1_boss_3: item_name.btnc_b2_rune_1_part,
    castle_location_names.btn_a1_boss_4: item_name.btnc_b2_rune_1_part,
    castle_location_names.btn_a1_floor_tp_n: item_name.btnc_a1_tp_n,
    castle_location_names.btn_a1_floor_shortcut: item_name.btnc_a1_m_shortcut,
    castle_location_names.btn_a1_floor_red: item_name.btnc_a1_red_spikes,
    castle_location_names.btn_a1_floor_sw: item_name.btnc_a1_sw_spikes,
    castle_location_names.btn_a1_puzzle: item_name.btnc_a1_puzzle,
    castle_location_names.btn_a1_rune: item_name.btnc_a1_open_se_cache,
    castle_location_names.btn_a1_rune_1: item_name.btnc_a1_open_se_cache_part,
    castle_location_names.btn_a1_rune_2: item_name.btnc_a1_open_se_cache_part,
    castle_location_names.btn_a1_rune_3: item_name.btnc_a1_open_se_cache_part,
    castle_location_names.btn_a1_rune_4: item_name.btnc_a1_open_se_cache_part,
    castle_location_names.btn_a1_wall_m_cache: item_name.btnc_a1_open_m_cache,
    castle_location_names.btn_a1_wall_red_spikes: item_name.btnc_a1_open_ne_cache,
    castle_location_names.btn_a1_wall_start: item_name.btnc_a1_open_se_wall,
    castle_location_names.btn_a1_wall_se: item_name.btnc_a1_open_se_rune,
    castle_location_names.btn_a2_boss: item_name.btnc_b2_rune_2,
    castle_location_names.btn_a2_boss_2: item_name.btnc_b2_rune_2_part,
    castle_location_names.btn_a2_boss_1: item_name.btnc_b2_rune_2_part,
    castle_location_names.btn_a2_boss_3: item_name.btnc_b2_rune_2_part,
    castle_location_names.btn_a2_boss_4: item_name.btnc_b2_rune_2_part,
    castle_location_names.btn_a2_floor_pyramid_nw: item_name.btnc_a2_pyramid_nw,
    castle_location_names.btn_a2_floor_tp_n: item_name.btnc_a2_bspikes_tp,
    castle_location_names.btn_a2_floor_pyramid_ne: item_name.btnc_a2_open_bonus,
    castle_location_names.btn_a2_floor_pyramid_sw: item_name.btnc_a2_pyramid_sw,
    castle_location_names.btn_a2_floor_pyramid_se: item_name.btnc_a2_pyramid_se,
    castle_location_names.btn_a2_floor_pyramid_m: item_name.btnc_a3_pyramid_ne,
    castle_location_names.btn_a2_floor_secret_e: item_name.btnc_a2_tp_ne,
    castle_location_names.btn_a2_floor_sw: item_name.btnc_a2_tp_sw,
    castle_location_names.btn_a2_floor_tp_se: item_name.btnc_a2_tp_se,
    castle_location_names.btn_a2_puzzle: item_name.btnc_a2_puzzle,
    castle_location_names.btn_a2_rune: item_name.btnc_a2_tp_ne_gates,
    castle_location_names.btn_a2_rune_2: item_name.btnc_a2_tp_ne_gates_part,
    castle_location_names.btn_a2_rune_1: item_name.btnc_a2_tp_ne_gates_part,
    castle_location_names.btn_a2_rune_4: item_name.btnc_a2_tp_ne_gates_part,
    castle_location_names.btn_a2_rune_3: item_name.btnc_a2_tp_ne_gates_part,
    castle_location_names.btn_a2_wall_nw: item_name.btnc_a2_open_w_exit,
    castle_location_names.btn_a2_wall_sw: item_name.btnc_a2_open_shortcut,
    castle_location_names.btn_a2_wall_se: item_name.btnc_a2_open_se_room_l,
    castle_location_names.btn_a2_wall_e: item_name.btnc_a2_open_se_room_t,
    castle_location_names.btn_n2_floor_blue: item_name.btnc_a2_blue_spikes,
    castle_location_names.btn_a3_boss: item_name.btnc_b2_rune_3,
    castle_location_names.btn_a3_boss_1: item_name.btnc_b2_rune_3_part,
    castle_location_names.btn_a3_boss_3: item_name.btnc_b2_rune_3_part,
    castle_location_names.btn_a3_boss_2: item_name.btnc_b2_rune_3_part,
    castle_location_names.btn_a3_boss_4: item_name.btnc_b2_rune_3_part,
    castle_location_names.btn_a3_floor_knife_1: item_name.btnc_a3_open_knife_part,
    castle_location_names.btn_a3_floor_knife_3: item_name.btnc_a3_open_knife_part,
    castle_location_names.btn_a3_floor_knife_4: item_name.btnc_a3_open_knife_part,
    castle_location_names.btn_a3_floor_knife_5: item_name.btnc_a3_open_knife_part,
    castle_location_names.btn_a3_floor_knife_2: item_name.btnc_a3_open_knife_part,
    castle_location_names.btn_a3_floor_tp_m: item_name.btnc_a3_tp_m,
    castle_location_names.btn_a3_floor_stairs_in_wall: item_name.btnc_a3_bgate_tp,
    castle_location_names.btn_a3_wall_knife_1: item_name.btnc_a3_open_knife_2_part,
    castle_location_names.btn_a3_wall_knife_2: item_name.btnc_a3_open_knife_2_part,
    castle_location_names.btn_a3_wall_from_a2: item_name.btnc_a3_open_m_stairs,
    castle_location_names.btn_a3_wall_start: item_name.btnc_a3_open_start_n,
    castle_location_names.btn_a3_wall_end: item_name.btnc_a3_open_start_e,
    castle_location_names.btn_r1_floor_nw_hidden: item_name.btnc_r1_open_w_wall,
    castle_location_names.btn_r1_floor_ne: item_name.btnc_r1_open_n_wall,
    castle_location_names.btn_r1_floor_nw: item_name.btnc_r1_open_nw_room,
    castle_location_names.btn_r1_floor_e: item_name.btnc_r1_open_m_ledge,
    castle_location_names.btn_r1_floor_w_s: item_name.btnc_r1_open_l_exit,
    castle_location_names.btn_r1_floor_w_shop: item_name.btnc_r1_open_start_room,
    castle_location_names.btn_r1_floor_se: item_name.btnc_r1_open_e_wall,
    castle_location_names.btn_r1_floor_exit: item_name.btnc_r1_open_exits,
    castle_location_names.btn_r1_puzzle: item_name.btnc_r1_puzzle,
    castle_location_names.btn_r1_wall_ne: item_name.btnc_r1_ne_shortcut,
    castle_location_names.btn_r1_wall_w: item_name.btnc_r1_w_shortcut,
    castle_location_names.btn_r1_wall_se: item_name.btnc_r1_open_se_room,
    castle_location_names.btn_r2_boss_n: item_name.btnc_b3_rune_2,
    castle_location_names.btn_r2_boss_e: item_name.btnc_b3_rune_1,
    castle_location_names.btn_r2_boss_n_2: item_name.btnc_b3_rune_2_part,
    castle_location_names.btn_r2_boss_n_1: item_name.btnc_b3_rune_2_part,
    castle_location_names.btn_r2_boss_n_4: item_name.btnc_b3_rune_2_part,
    castle_location_names.btn_r2_boss_n_3: item_name.btnc_b3_rune_2_part,
    castle_location_names.btn_r2_boss_e_2: item_name.btnc_b3_rune_1_part,
    castle_location_names.btn_r2_boss_e_1: item_name.btnc_b3_rune_1_part,
    castle_location_names.btn_r2_boss_e_3: item_name.btnc_b3_rune_1_part,
    castle_location_names.btn_r2_boss_e_4: item_name.btnc_b3_rune_1_part,
    castle_location_names.btn_r2_floor_nw: item_name.btnc_r2_open_bs_l,
    castle_location_names.btn_r2_floor_boss_rune: item_name.btnc_r2_open_bs_r,
    castle_location_names.btn_r2_floor_ne: item_name.btnc_r2_open_fire_t,
    castle_location_names.btn_r2_floor_gate_w: item_name.btnc_r2_open_exit,
    castle_location_names.btn_r2_floor_gate_s: item_name.btnc_r2_open_s_r,
    castle_location_names.btn_r2_floor_e: item_name.btnc_r2_open_fire_b,
    castle_location_names.btn_r2_floor_sw: item_name.btnc_r2_open_s_l,
    castle_location_names.btn_r2_puzzle: item_name.btnc_r2_puzzle,
    castle_location_names.btn_r2_rune: item_name.btnc_r2_open_puzzle,
    castle_location_names.btn_r2_rune_1: item_name.btnc_r2_open_puzzle_part,
    castle_location_names.btn_r2_rune_2: item_name.btnc_r2_open_puzzle_part,
    castle_location_names.btn_r2_rune_3: item_name.btnc_r2_open_puzzle_part,
    castle_location_names.btn_r2_rune_4: item_name.btnc_r2_open_puzzle_part,
    castle_location_names.btn_r2_wall_nw: item_name.btnc_r2_nw_shortcut,
    castle_location_names.btn_r2_wall_start: item_name.btnc_r2_open_start,
    castle_location_names.btn_r2_wall_spike_island_n: item_name.btnc_r2_open_spikes_t,
    castle_location_names.btn_r2_wall_spike_island_s: item_name.btnc_r2_light_bridge,
    castle_location_names.btn_r2_wall_ne: item_name.btnc_r2_open_ne_cache,
    castle_location_names.btn_r3_boss_door: item_name.btnc_r3_boss_door,
    castle_location_names.btn_r3_boss: item_name.btnc_b3_rune_3,
    castle_location_names.btn_r3_boss_3: item_name.btnc_b3_rune_3_part,
    castle_location_names.btn_r3_boss_4: item_name.btnc_b3_rune_3_part,
    castle_location_names.btn_r3_boss_1: item_name.btnc_b3_rune_3_part,
    castle_location_names.btn_r3_boss_2: item_name.btnc_b3_rune_3_part,
    castle_location_names.btn_r3_floor_passage: item_name.btnc_r3_passage_room_2,
    castle_location_names.btn_r3_floor_passage_end: item_name.btnc_r3_tp_nw,
    castle_location_names.btn_r3_floor_gate_nw: item_name.btnc_r3_open_exit,
    castle_location_names.btn_r3_floor_ne: item_name.btnc_r3_open_ne_t,
    castle_location_names.btn_r3_floor_passage_room_2: item_name.btnc_r3_passage_room_2_spikes,
    castle_location_names.btn_r3_floor_ne_room: item_name.btnc_r3_open_ne_l,
    castle_location_names.btn_r3_floor_s_room: item_name.btnc_r3_open_s_t,
    castle_location_names.btn_r3_floor_s: item_name.btnc_r3_open_s_r,
    castle_location_names.btn_r3_floor_se: item_name.btnc_r3_open_bs,
    castle_location_names.btn_r3_floor_simon: item_name.btnc_r3_simon,
    castle_location_names.btn_r3_rune: item_name.btnc_r3_bonus_bridge,
    castle_location_names.btn_r3_rune_4: item_name.btnc_r3_bonus_bridge_part,
    castle_location_names.btn_r3_simon: item_name.btnc_r3_bonus,
    castle_location_names.btn_r3_simon_4: item_name.btnc_r3_bonus_part,
    castle_location_names.btn_r3_rune_3: item_name.btnc_r3_bonus_bridge_part,
    castle_location_names.btn_r3_simon_1: item_name.btnc_r3_bonus_part,
    castle_location_names.btn_r3_rune_2: item_name.btnc_r3_bonus_bridge_part,
    castle_location_names.btn_r3_simon_5: item_name.btnc_r3_bonus_part,
    castle_location_names.btn_r3_rune_1: item_name.btnc_r3_bonus_bridge_part,
    castle_location_names.btn_r3_simon_2: item_name.btnc_r3_bonus_part,
    castle_location_names.btn_r3_simon_3: item_name.btnc_r3_bonus_part,
    castle_location_names.btn_r3_simon_6: item_name.btnc_r3_bonus_part,
    castle_location_names.btn_r3_wall_passage_room_2: item_name.btnc_r3_passage_end,
    castle_location_names.btn_r3_wall_passage_room_1: item_name.btnc_r3_passage_room_1,
    castle_location_names.btn_r3_wall_ne_2: item_name.btnc_r3_tp_ne_t,
    castle_location_names.btn_r3_wall_ne_1: item_name.btnc_r3_tp_ne_b,
    castle_location_names.btn_r3_wall_seq_n: item_name.btnc_r3_simon_room_part,
    castle_location_names.btn_r3_wall_seq_ne: item_name.btnc_r3_simon_room_part,
    castle_location_names.btn_r3_wall_sw_gate: item_name.btnc_r3_sw_room,
    castle_location_names.btn_r3_wall_seq_w: item_name.btnc_r3_simon_room_part,
    castle_location_names.btn_r3_wall_seq_m: item_name.btnc_r3_simon_room_part,
    castle_location_names.btn_r3_wall_seq_se: item_name.btnc_r3_simon_room_part,
    castle_location_names.btn_c1_floor_n: item_name.btnc_c1_n_spikes,
    castle_location_names.btn_c1_floor_red: item_name.btnc_c1_red_spikes,
    castle_location_names.btn_c1_wall_red: item_name.btnc_c1_red_spike_turrets,
    castle_location_names.btn_c1_wall_ledge: item_name.btnc_c1_red_flame_turrets,
    castle_location_names.btn_c1_wall_s_gate: item_name.btnc_c1_s_shortcut,
    castle_location_names.btn_pstart_puzzle: item_name.btnc_pstart_puzzle,
    castle_location_names.btn_pstart_rune: item_name.btnc_pstart_bridge,
    castle_location_names.btn_pstart_rune_4: item_name.btnc_pstart_bridge_part,
    castle_location_names.btn_pstart_rune_3: item_name.btnc_pstart_bridge_part,
    castle_location_names.btn_pstart_rune_2: item_name.btnc_pstart_bridge_part,
    castle_location_names.btn_pstart_rune_1: item_name.btnc_pstart_bridge_part,
    castle_location_names.btn_c2_boss_w: item_name.btnc_b4_rune_2,
    castle_location_names.btn_c2_boss_e: item_name.btnc_b4_rune_1,
    castle_location_names.btn_c2_boss_w_1: item_name.btnc_b4_rune_2_part,
    castle_location_names.btn_c2_boss_w_3: item_name.btnc_b4_rune_2_part,
    castle_location_names.btn_c2_boss_w_2: item_name.btnc_b4_rune_2_part,
    castle_location_names.btn_c2_boss_w_4: item_name.btnc_b4_rune_2_part,
    castle_location_names.btn_c2_boss_e_2: item_name.btnc_b4_rune_1_part,
    castle_location_names.btn_c2_boss_e_1: item_name.btnc_b4_rune_1_part,
    castle_location_names.btn_c2_boss_e_3: item_name.btnc_b4_rune_1_part,
    castle_location_names.btn_c2_boss_e_4: item_name.btnc_b4_rune_1_part,
    castle_location_names.btn_c2_floor_sw: item_name.btnc_c2_sw_room,
    castle_location_names.btn_c2_floor_t_hall: item_name.btnc_c2_n_shops,
    castle_location_names.btn_c2_floor_w: item_name.btnc_c2_w_shortcut,
    castle_location_names.btn_c2_puzzle: item_name.btnc_c2_puzzle,
    castle_location_names.btn_c2_rune_bonus: item_name.btnc_c2_bonus,
    castle_location_names.btn_c2_rune_bonus_1: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_rune: item_name.btnc_c2_tp_spikes,
    castle_location_names.btn_c2_rune_1: item_name.btnc_c2_tp_spikes_part,
    castle_location_names.btn_c2_rune_bonus_2: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_rune_2: item_name.btnc_c2_tp_spikes_part,
    castle_location_names.btn_c2_rune_bonus_3: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_rune_3: item_name.btnc_c2_tp_spikes_part,
    castle_location_names.btn_c2_rune_bonus_8: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_rune_4: item_name.btnc_c2_tp_spikes_part,
    castle_location_names.btn_c2_rune_bonus_4: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_rune_bonus_6: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_rune_bonus_7: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_rune_bonus_5: item_name.btnc_c2_bonus_part,
    castle_location_names.btn_c2_wall_seq_nw: item_name.btnc_c2_bonus_room_part,
    castle_location_names.btn_c2_wall_seq_ne: item_name.btnc_c2_bonus_room_part,
    castle_location_names.btn_c2_wall_n_exit_gate: item_name.btnc_c2_n_room,
    castle_location_names.btn_c2_wall_seq_w: item_name.btnc_c2_bonus_room_part,
    castle_location_names.btn_c2_wall_seq_s: item_name.btnc_c2_bonus_room_part,
    castle_location_names.btn_c2_wall_seq_e: item_name.btnc_c2_bonus_room_part,
    castle_location_names.btn_c2_wall_red_n: item_name.btnc_c2_n_red_flame_turret_on,
    castle_location_names.btn_c2_wall_blue: item_name.btnc_c2_blue_spike_turret,
    castle_location_names.btn_c2_wall_portal_shop: item_name.btnc_c2_open_puzzle,
    castle_location_names.btn_c2_wall_e_shop: item_name.btnc_c2_e_shop,
    castle_location_names.btn_c2_wall_red_s: item_name.btnc_c2_s_red_flame_turret,
    castle_location_names.btn_c2_wall_s_save: item_name.btnc_c2_s_shortcut,
    castle_location_names.btn_c3_boss: item_name.btnc_b4_rune_3,
    castle_location_names.btn_c3_boss_1: item_name.btnc_b4_rune_3_part,
    castle_location_names.btn_c3_boss_3: item_name.btnc_b4_rune_3_part,
    castle_location_names.btn_c3_boss_2: item_name.btnc_b4_rune_3_part,
    castle_location_names.btn_c3_boss_4: item_name.btnc_b4_rune_3_part,
    castle_location_names.btn_c3_floor: item_name.btnc_c3_e_shortcut,
    castle_location_names.btn_c3_rune: item_name.btnc_c3_sw_room,
    castle_location_names.btn_c3_rune_s: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_se: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_w: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_e: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_n: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_rune_ne: item_name.btnc_c3_sw_room_part,
    castle_location_names.btn_c3_wall_red: item_name.btnc_c3_red_spikes,
    castle_location_names.btn_c3_wall_blue: item_name.btnc_c3_blue_fire_turrets_on,
    castle_location_names.btn_c3_wall_w: item_name.btnc_c3_tp_m,
    castle_location_names.btn_c3_wall_shop: item_name.btnc_c3_red_spike_turrets,
    castle_location_names.btn_c3_wall_fire_floor: item_name.btnc_c3_tp_se,
    castle_location_names.btn_c3_wall_se_hidden: item_name.btnc_c3_open_w_room,
    castle_location_names.btn_n1_panel_n: item_name.btnc_n1_cache_n,
    castle_location_names.btn_n1_panel_e_1: item_name.btnc_n1_cache_ne,
    castle_location_names.btn_n1_panel_e_2: item_name.btnc_n1_hall_top,
    castle_location_names.btn_n1_panel_s: item_name.btnc_n1_hall_bottom,
    castle_location_names.btn_n2_panel_n: item_name.btnc_n2_open_se_room,
    castle_location_names.btn_n2_panel_se: item_name.btnc_n2_open_ne_room,
    castle_location_names.btn_n2_panel_ne: item_name.btnc_n2_open_exit,
    castle_location_names.btn_p3_wall_start_nw: item_name.btnc_p3_nw_room,
    castle_location_names.btn_p3_rune_bonus: item_name.btnc_p3_portal,
    castle_location_names.btn_r2_floor_sw_hidden: item_name.btnc_r2_open_spikes_l,
    castle_location_names.btn_r3_floor_sw_gate: item_name.btnc_r3_passage,
    castle_location_names.btn_c1_wall_portal: item_name.btnc_c1_sw_exit,
    castle_location_names.btn_c3_wall_sw_hidden: item_name.btnc_c3_open_s_hall,
    castle_location_names.btn_p3_seq_bonus: item_name.btnc_p3_open_bonus,
    castle_location_names.btn_a3_seq_knife: item_name.btnc_a3_open_knife,
    castle_location_names.btn_a3_seq_knife_2: item_name.btnc_a3_open_knife_2,
    castle_location_names.btn_r3_seq_simon_room: item_name.btnc_r3_simon_room,
    castle_location_names.btn_c2_seq_bonus: item_name.btnc_c2_bonus_room,
}

counter = Counter(id_start)
temple_pickup_locations: typing.Dict[str, LocationData] = {
    temple_location_names.hub_field_nw: LocationData(counter.count(0)),
    temple_location_names.hub_on_rock: LocationData(counter.count()),
    temple_location_names.hub_pof_reward: LocationData(counter.count()),
    temple_location_names.hub_west_pyramid: LocationData(counter.count()),
    temple_location_names.hub_rocks_south: LocationData(counter.count()),
    temple_location_names.hub_field_north: LocationData(counter.count()),
    temple_location_names.hub_behind_temple_entrance: LocationData(counter.count()),
    temple_location_names.hub_behind_shops: LocationData(counter.count()),
    temple_location_names.hub_front_of_pof: LocationData(counter.count()),
    temple_location_names.hub_field_south: LocationData(counter.count()),

    temple_location_names.cave3_portal_r: LocationData(counter.count()),
    temple_location_names.cave3_n: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave3_outside_guard: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave3_portal_l: LocationData(counter.count()),
    temple_location_names.cave3_nw: LocationData(counter.count()),
    temple_location_names.cave3_m: LocationData(counter.count()),
    temple_location_names.cave3_se: LocationData(counter.count()),
    temple_location_names.cave3_fall_se: LocationData(counter.count()),
    temple_location_names.cave3_ne: LocationData(counter.count()),
    temple_location_names.cave3_captain: LocationData(counter.count()),
    temple_location_names.cave3_fall_sw: LocationData(counter.count()),
    temple_location_names.cave3_squire: LocationData(counter.count()),
    temple_location_names.cave3_captain_dock: LocationData(counter.count()),
    temple_location_names.cave3_fall_ne: LocationData(counter.count()),
    temple_location_names.cave3_fields_r: LocationData(counter.count()),
    temple_location_names.cave3_trapped_guard: LocationData(counter.count()),
    temple_location_names.cave3_secret_n: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave3_secret_nw: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave3_secret_s: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave3_secret_6: LocationData(counter.count()),
    temple_location_names.cave3_secret_7: LocationData(counter.count()),
    temple_location_names.cave3_secret_8: LocationData(counter.count()),
    temple_location_names.cave3_secret_5: LocationData(counter.count()),
    temple_location_names.cave3_secret_2: LocationData(counter.count()),
    temple_location_names.cave3_secret_3: LocationData(counter.count()),
    temple_location_names.cave3_secret_4: LocationData(counter.count()),
    temple_location_names.cave3_secret_1: LocationData(counter.count()),
    temple_location_names.cave3_secret_9: LocationData(counter.count()),
    temple_location_names.cave3_secret_10: LocationData(counter.count()),
    temple_location_names.cave3_secret_11: LocationData(counter.count()),
    temple_location_names.cave3_secret_12: LocationData(counter.count()),
    temple_location_names.cave3_fall_nw: LocationData(counter.count()),
    temple_location_names.cave3_half_bridge: LocationData(counter.count()),
    temple_location_names.cave3_guard: LocationData(counter.count()),
    temple_location_names.c3_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c3_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c3_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c3_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    temple_location_names.cave2_sw_hidden_room_3: LocationData(counter.count()),
    temple_location_names.cave2_pumps_wall_r: LocationData(counter.count()),
    temple_location_names.cave2_below_pumps_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_below_pumps_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_double_bridge_l_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_double_bridge_l_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_e_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_e_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_nw_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_nw_5: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_pumps_wall_l: LocationData(counter.count()),
    temple_location_names.cave2_water_n_r_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_water_s: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_nw_2: LocationData(counter.count()),
    temple_location_names.cave2_red_bridge_4: LocationData(counter.count()),
    temple_location_names.cave2_double_bridge_r: LocationData(counter.count()),
    temple_location_names.cave2_w_miniboss_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_w_miniboss_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_w_miniboss_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_red_bridge_se_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_red_bridge_se_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_e_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_e_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_guard_n: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave2_red_bridge_2: LocationData(counter.count()),
    temple_location_names.cave2_double_bridge_m: LocationData(counter.count()),
    temple_location_names.cave2_water_n_r_1: LocationData(counter.count()),
    temple_location_names.cave2_green_bridge: LocationData(counter.count()),
    temple_location_names.cave2_sw_hidden_room_1: LocationData(counter.count()),
    temple_location_names.cave2_guard_s: LocationData(counter.count()),
    temple_location_names.cave2_nw_3: LocationData(counter.count()),
    temple_location_names.cave2_w_miniboss_4: LocationData(counter.count()),
    temple_location_names.cave2_red_bridge_3: LocationData(counter.count()),
    temple_location_names.cave2_below_pumps_3: LocationData(counter.count()),
    temple_location_names.cave2_secret_ne: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave2_secret_w: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave2_secret_m: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave2_water_n_l: LocationData(counter.count()),
    temple_location_names.cave2_nw_1: LocationData(counter.count()),
    temple_location_names.cave2_sw: LocationData(counter.count()),
    temple_location_names.cave2_double_bridge_secret: LocationData(counter.count()),
    temple_location_names.cave2_sw_hidden_room_2: LocationData(counter.count()),
    temple_location_names.cave2_pumps_n: LocationData(counter.count()),
    temple_location_names.cave2_guard: LocationData(counter.count()),
    temple_location_names.cave2_red_bridge_1: LocationData(counter.count()),
    temple_location_names.cave2_sw_hidden_room_4: LocationData(counter.count()),
    temple_location_names.c2_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c2_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c2_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c2_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    temple_location_names.cave1_secret_tunnel_1: LocationData(counter.count()),
    temple_location_names.cave1_temple_end_3: LocationData(counter.count()),
    temple_location_names.cave1_n_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_n_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_w_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_w_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_s_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_s_5: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_ne_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_ne_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_temple_hall_2: LocationData(counter.count()),
    temple_location_names.cave1_water_s_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_water_s_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_water_s_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_water_s_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_water_s_5: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_n_bridges_4: LocationData(counter.count()),
    temple_location_names.cave1_double_room_l: LocationData(counter.count()),
    temple_location_names.cave1_e_3: LocationData(counter.count()),
    temple_location_names.cave1_green_bridge_2: LocationData(counter.count()),
    temple_location_names.cave1_n_bridges_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_secret_tunnel_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_n_room_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_n_room_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_n_room_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_n_room_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_se_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_se_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_s_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_s_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_ne_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_ne_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_ne_5: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_w_by_water_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_e_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_double_room_r: LocationData(counter.count()),
    temple_location_names.cave1_krilith_ledge_n: LocationData(counter.count()),
    temple_location_names.cave1_red_bridge_e: LocationData(counter.count()),
    temple_location_names.cave1_ne_hidden_room_3: LocationData(counter.count()),
    temple_location_names.cave1_water_s_shore: LocationData(counter.count()),
    temple_location_names.cave1_temple_end_2: LocationData(counter.count()),
    temple_location_names.cave1_krilith_door: LocationData(counter.count()),
    temple_location_names.cave1_temple_end_4: LocationData(counter.count()),
    temple_location_names.cave1_ne_grubs: LocationData(counter.count()),
    temple_location_names.cave1_w_by_water_2: LocationData(counter.count()),
    temple_location_names.cave1_m: LocationData(counter.count()),
    temple_location_names.cave1_secret_nw: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave1_secret_n_hidden_room: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave1_secret_ne: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave1_secret_w: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave1_secret_m: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave1_secret_e: LocationData(counter.count(), LocType.Secret),
    temple_location_names.cave1_temple_hall_1: LocationData(counter.count()),
    temple_location_names.cave1_temple_hall_3: LocationData(counter.count()),
    temple_location_names.cave1_n_bridges_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_temple_end_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_secret_tunnel_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.cave1_n_3: LocationData(counter.count()),
    temple_location_names.cave1_ne_hidden_room_4: LocationData(counter.count()),
    temple_location_names.cave1_n_bridges_1: LocationData(counter.count()),
    temple_location_names.cave1_krilith_ledge_e: LocationData(counter.count()),
    temple_location_names.cave1_green_bridge_1: LocationData(counter.count()),
    temple_location_names.cave1_e_2: LocationData(counter.count()),
    temple_location_names.cave1_s_3: LocationData(counter.count()),
    temple_location_names.cave1_ne_hidden_room_5: LocationData(counter.count()),
    temple_location_names.cave1_ne_hidden_room_1: LocationData(counter.count()),
    temple_location_names.cave1_ne_hidden_room_2: LocationData(counter.count()),
    temple_location_names.cave1_n_bridges_5: LocationData(counter.count()),
    temple_location_names.c1_n_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c1_n_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c1_n_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c1_n_puzzle_4: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c1_e_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c1_e_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c1_e_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.c1_e_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    temple_location_names.boss1_bridge: LocationData(counter.count()),
    temple_location_names.boss1_guard_r_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.boss1_guard_r_2: LocationData(counter.count(), LocType.Recovery),
    # temple_location_names.boss1_drop_2: LocationData(counter.count()),
    # temple_location_names.boss1_drop: LocationData(counter.count()),
    temple_location_names.boss1_guard_l: LocationData(counter.count(3), LocType.Recovery),
    temple_location_names.boss1_bridge_n: LocationData(counter.count()),
    temple_location_names.boss1_secret: LocationData(counter.count(), LocType.Secret),

    temple_location_names.p_mid4_2: LocationData(counter.count()),
    temple_location_names.p_end3_1: LocationData(counter.count()),
    temple_location_names.p_mid4_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.p_mid4_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.p_mid2_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.p_mid2_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.p_mid2_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.p_mid2_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.p_mid4_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.p_mid5_2: LocationData(counter.count()),
    temple_location_names.p_end3_2: LocationData(counter.count()),
    temple_location_names.p_ent2_secret: LocationData(counter.count(), LocType.Secret),
    temple_location_names.p_mid3_secret_1: LocationData(counter.count(), LocType.Secret),
    temple_location_names.p_mid3_secret_2: LocationData(counter.count(), LocType.Secret),
    temple_location_names.p_mid3_secret_3: LocationData(counter.count(), LocType.Secret),
    temple_location_names.p_mid3_secret_4: LocationData(counter.count(), LocType.Secret),
    temple_location_names.p_end1_secret: LocationData(counter.count(), LocType.Secret),
    temple_location_names.p_mid5_secret: LocationData(counter.count(), LocType.Secret),
    temple_location_names.p_mid1_2: LocationData(counter.count()),
    temple_location_names.p_mid1_1: LocationData(counter.count()),
    temple_location_names.p_mid5_1: LocationData(counter.count()),
    temple_location_names.p_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.p_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.p_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.p_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    temple_location_names.temple_entrance_l: LocationData(counter.count()),
    temple_location_names.temple_entrance_r: LocationData(counter.count()),

    temple_location_names.t1_double_gate_behind_block: LocationData(counter.count()),
    temple_location_names.t1_sw_hidden_room_3: LocationData(counter.count()),
    temple_location_names.t1_telarian_ice: LocationData(counter.count()),
    temple_location_names.t1_sun_turret_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_telarian_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_boulder_hallway_by_ice_turret_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_boulder_hallway_by_ice_turret_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_boulder_hallway_by_ice_turret_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_telarian_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_node_2_passage_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_node_2_passage_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_fire_trap_by_sun_turret_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_fire_trap_by_sun_turret_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_e_of_double_gate_room_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_e_of_double_gate_room_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_sw_sun_room_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_sw_sun_room_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_ice_block_chamber_ice: LocationData(counter.count()),
    temple_location_names.t1_sun_turret_2: LocationData(counter.count()),
    temple_location_names.t1_n_cache_by_ice_turret_5: LocationData(counter.count()),
    temple_location_names.t1_s_cache_by_ice_turret_3: LocationData(counter.count()),
    temple_location_names.t1_sw_sdoor_2: LocationData(counter.count()),
    temple_location_names.t1_sw_hidden_room_4: LocationData(counter.count()),
    temple_location_names.t1_sun_turret_3: LocationData(counter.count()),
    temple_location_names.t1_s_bridge_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_s_bridge_5: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_s_bridge_6: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_n_cache_by_ice_turret_1: LocationData(counter.count()),
    temple_location_names.t1_n_sunbeam_treasure_2: LocationData(counter.count()),
    temple_location_names.t1_s_cache_by_ice_turret_2: LocationData(counter.count()),
    temple_location_names.t1_sw_sdoor_1: LocationData(counter.count()),
    temple_location_names.t1_sw_sdoor_4: LocationData(counter.count()),
    temple_location_names.t1_sw_sdoor_5: LocationData(counter.count()),
    temple_location_names.t1_ledge_after_block_trap_2: LocationData(counter.count()),
    temple_location_names.t1_ice_block_chamber_3: LocationData(counter.count()),
    temple_location_names.t1_ice_block_chamber_2: LocationData(counter.count()),
    temple_location_names.t1_double_gate_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_ice_block_chamber_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_sun_block_hall_3: LocationData(counter.count()),
    temple_location_names.t1_fire_trap_by_sun_turret_4: LocationData(counter.count()),
    temple_location_names.t1_behind_bars_entrance: LocationData(counter.count()),
    temple_location_names.t1_mana_drain_fire_trap: LocationData(counter.count()),
    temple_location_names.t1_e_gold_beetles: LocationData(counter.count()),
    temple_location_names.t1_sun_block_hall_1: LocationData(counter.count()),
    temple_location_names.t1_sw_hidden_room_2: LocationData(counter.count()),
    temple_location_names.t1_mana_drain_fire_trap_reward_2: LocationData(counter.count()),
    temple_location_names.t1_mana_drain_fire_trap_reward_1: LocationData(counter.count()),
    temple_location_names.t1_sun_block_hall_4: LocationData(counter.count()),
    temple_location_names.t1_fire_trap_by_sun_turret_3: LocationData(counter.count()),
    temple_location_names.t1_ledge_after_block_trap_1: LocationData(counter.count()),
    temple_location_names.t1_sw_sdoor_3: LocationData(counter.count()),
    temple_location_names.t1_n_sunbeam_treasure_3: LocationData(counter.count()),
    temple_location_names.t1_boulder_hallway_by_ice_turret_4: LocationData(counter.count()),
    temple_location_names.t1_ice_turret_1: LocationData(counter.count()),
    temple_location_names.t1_ice_turret_2: LocationData(counter.count()),
    temple_location_names.t1_above_s_bridge: LocationData(counter.count()),
    temple_location_names.t1_e_of_double_gate_room_2: LocationData(counter.count()),
    temple_location_names.t1_sw_corner_room: LocationData(counter.count()),
    temple_location_names.t1_s_bridge_1: LocationData(counter.count()),
    temple_location_names.t1_sun_block_hall_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_mana_drain_fire_trap_passage: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t1_n_sunbeam: LocationData(counter.count()),
    temple_location_names.t1_n_cache_by_ice_turret_4: LocationData(counter.count()),
    temple_location_names.t1_node_2_passage_2: LocationData(counter.count()),
    temple_location_names.t1_double_gate_hidden: LocationData(counter.count()),
    temple_location_names.t1_ice_turret_boulder_break_block: LocationData(counter.count()),
    temple_location_names.t1_e_of_double_gate_room_1: LocationData(counter.count()),
    temple_location_names.t1_sw_hidden_room_1: LocationData(counter.count()),
    temple_location_names.t1_n_cache_by_ice_turret_2: LocationData(counter.count()),
    temple_location_names.t1_n_cache_by_ice_turret_3: LocationData(counter.count()),
    temple_location_names.t1_n_sunbeam_treasure_1: LocationData(counter.count()),
    temple_location_names.t1_telarian_4: LocationData(counter.count()),
    temple_location_names.t1_telarian_1: LocationData(counter.count()),
    temple_location_names.t1_node_2_1: LocationData(counter.count()),
    temple_location_names.t1_node_2_2: LocationData(counter.count()),
    temple_location_names.t1_s_of_sun_turret: LocationData(counter.count()),
    temple_location_names.t1_double_gate_2: LocationData(counter.count()),
    temple_location_names.t1_double_gate_3: LocationData(counter.count()),
    temple_location_names.t1_s_cache_by_ice_turret_1: LocationData(counter.count()),
    temple_location_names.t1_s_bridge_2: LocationData(counter.count()),
    temple_location_names.t1_s_bridge_3: LocationData(counter.count()),
    temple_location_names.t1_telarian_5: LocationData(counter.count()),
    temple_location_names.t1_w_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t1_w_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t1_w_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t1_w_puzzle_4: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t1_e_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t1_e_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t1_e_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t1_e_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    temple_location_names.boss2_nw: LocationData(counter.count()),
    temple_location_names.boss2_se: LocationData(counter.count()),

    temple_location_names.t2_nw_puzzle_cache_5: LocationData(counter.count()),
    temple_location_names.t2_floor3_cache_3: LocationData(counter.count()),
    temple_location_names.t2_fire_trap_maze_2: LocationData(counter.count()),
    temple_location_names.t2_sw_gate: LocationData(counter.count()),
    temple_location_names.t2_se_light_bridge_2: LocationData(counter.count()),
    temple_location_names.t2_boulder_room_block: LocationData(counter.count()),
    temple_location_names.t2_nw_ice_turret_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_nw_ice_turret_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_nw_ice_turret_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_w_hall_dead_end_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_w_hall_dead_end_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_w_hall_dead_end_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_e_outside_gold_beetle_cage_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_e_outside_gold_beetle_cage_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_s_node_room_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_s_node_room_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_s_node_room_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_se_banner_chamber_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_se_banner_chamber_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_nw_puzzle_cache_1: LocationData(counter.count()),
    temple_location_names.t2_nw_puzzle_cache_2: LocationData(counter.count()),
    temple_location_names.t2_nw_gate_2: LocationData(counter.count()),
    temple_location_names.t2_floor3_cache_1: LocationData(counter.count()),
    temple_location_names.t2_floor3_cache_2: LocationData(counter.count()),
    temple_location_names.t2_jones_hallway: LocationData(counter.count()),
    temple_location_names.t2_boulder_room_2: LocationData(counter.count()),
    temple_location_names.t2_sw_jail_2: LocationData(counter.count()),
    temple_location_names.t2_right_of_pof_switch: LocationData(counter.count()),
    temple_location_names.t2_w_gold_beetle_room_4: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_nw_gate_3: LocationData(counter.count()),
    temple_location_names.t2_nw_under_block: LocationData(counter.count()),
    temple_location_names.t2_floor3_cache_6: LocationData(counter.count()),
    temple_location_names.t2_w_spike_trap_2: LocationData(counter.count()),
    temple_location_names.t2_w_hall_dead_end_4: LocationData(counter.count()),
    temple_location_names.t2_fire_trap_maze_3: LocationData(counter.count()),
    temple_location_names.t2_boulder_chamber_2: LocationData(counter.count()),
    temple_location_names.t2_se_banner_chamber_2: LocationData(counter.count()),
    temple_location_names.t2_w_spike_trap_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_boulder_chamber_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_fire_trap_maze_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_s_sunbeam_2: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_nw_gate_1: LocationData(counter.count()),
    temple_location_names.t2_w_gold_beetle_room_2: LocationData(counter.count()),
    temple_location_names.t2_w_ice_block_gate: LocationData(counter.count()),
    temple_location_names.t2_e_ice_block_gate: LocationData(counter.count()),
    temple_location_names.t2_nw_puzzle_cache_4: LocationData(counter.count()),
    temple_location_names.t2_mana_drain_fire_trap_2: LocationData(counter.count()),
    temple_location_names.t2_floor3_cache_4: LocationData(counter.count()),
    temple_location_names.t2_portal_gate: LocationData(counter.count()),
    temple_location_names.t2_fire_trap_maze_4: LocationData(counter.count()),
    temple_location_names.t2_gold_beetle_barricade: LocationData(counter.count()),
    temple_location_names.t2_se_light_bridge_1: LocationData(counter.count()),
    temple_location_names.t2_teleporter: LocationData(counter.count()),
    temple_location_names.t2_mana_drain_fire_trap_1: LocationData(counter.count()),
    temple_location_names.t2_floor3_cache_gate: LocationData(counter.count()),
    temple_location_names.t2_w_gold_beetle_room_1: LocationData(counter.count()),
    temple_location_names.t2_s_light_bridge_1: LocationData(counter.count()),
    temple_location_names.t2_nw_ice_turret_4: LocationData(counter.count()),
    temple_location_names.t2_s_of_portal: LocationData(counter.count()),
    temple_location_names.t2_n_of_sw_gate_2: LocationData(counter.count()),
    temple_location_names.t2_boulder_chamber_3: LocationData(counter.count()),
    temple_location_names.t2_left_of_pof_switch_2: LocationData(counter.count()),
    temple_location_names.t2_s_balcony_2: LocationData(counter.count()),
    temple_location_names.t2_se_banner_chamber_5: LocationData(counter.count()),
    temple_location_names.t2_n_of_portal: LocationData(counter.count()),
    temple_location_names.t2_nw_of_s_ice_turret: LocationData(counter.count()),
    temple_location_names.t2_w_hall_dead_end_5: LocationData(counter.count()),
    temple_location_names.t2_fire_trap_maze_5: LocationData(counter.count()),
    temple_location_names.t2_fire_trap_maze_6: LocationData(counter.count()),
    temple_location_names.t2_boulder_chamber_4: LocationData(counter.count()),
    temple_location_names.t2_s_balcony_1: LocationData(counter.count()),
    temple_location_names.t2_se_banner_chamber_4: LocationData(counter.count()),
    temple_location_names.t2_se_fireball_hall: LocationData(counter.count()),
    temple_location_names.t2_boulder_room_1: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_w_gold_beetle_room_3: LocationData(counter.count(), LocType.Recovery),
    temple_location_names.t2_nw_puzzle_cache_3: LocationData(counter.count()),
    temple_location_names.t2_floor3_cache_5: LocationData(counter.count()),
    temple_location_names.t2_n_of_sw_gate_1: LocationData(counter.count()),
    temple_location_names.t2_left_of_pof_switch_1: LocationData(counter.count()),
    temple_location_names.t2_s_light_bridge_2: LocationData(counter.count()),
    temple_location_names.t2_s_sunbeam_1: LocationData(counter.count()),
    temple_location_names.t2_sw_jail_1: LocationData(counter.count()),
    temple_location_names.t2_n_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_n_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_n_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_n_puzzle_4: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_nw_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_nw_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_nw_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_nw_puzzle_4: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_e_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_e_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_e_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_e_puzzle_4: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_sw_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_sw_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_sw_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t2_sw_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    temple_location_names.t3_boss_fall_3_2: LocationData(counter.count()),
    temple_location_names.t3_n_node_1: LocationData(counter.count()),
    temple_location_names.t3_n_node_2: LocationData(counter.count()),
    temple_location_names.t3_s_node_cache_2: LocationData(counter.count()),
    temple_location_names.t3_n_turret_1: LocationData(counter.count()),
    temple_location_names.t3_boulder_block: LocationData(counter.count()),
    temple_location_names.t3_e_turret_spikes: LocationData(counter.count()),
    temple_location_names.t3_n_node_3: LocationData(counter.count()),
    temple_location_names.t3_s_balcony_turret_2: LocationData(counter.count()),
    temple_location_names.t3_s_node_cache_1: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_2_2: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_3_4: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_1_3: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_3_1: LocationData(counter.count()),
    temple_location_names.t3_n_turret_2: LocationData(counter.count()),
    temple_location_names.t3_m_balcony_corridor: LocationData(counter.count()),
    temple_location_names.t3_s_node_cache_3: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_3_3: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_2_3: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_1_2: LocationData(counter.count()),
    temple_location_names.t3_s_gate: LocationData(counter.count()),
    temple_location_names.t3_n_node_blocks_1: LocationData(counter.count()),
    temple_location_names.t3_n_node_blocks_2: LocationData(counter.count()),
    temple_location_names.t3_n_node_blocks_3: LocationData(counter.count()),
    temple_location_names.t3_n_node_blocks_4: LocationData(counter.count()),
    temple_location_names.t3_n_node_blocks_5: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_2_1: LocationData(counter.count()),
    temple_location_names.t3_boss_fall_1_1: LocationData(counter.count()),
    temple_location_names.t3_s_balcony_turret_1: LocationData(counter.count()),
    temple_location_names.t3_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t3_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t3_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.t3_puzzle_4: LocationData(counter.count(), LocType.Puzzle),

    temple_location_names.pof_2_ne_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ne_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ne_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ne_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ent_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ent_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ent_6: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ent_5: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ent_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_ent_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_confuse_hall_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_confuse_hall_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_confuse_hall_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_confuse_hall_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_sw_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_sw_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_sw_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_2_sw_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_6: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_7: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_8: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_9: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_confuse_corner_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_confuse_corner_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_confuse_corner_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_confuse_corner_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_end_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_end_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_end_5: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_end_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_10: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_6: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_9: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_7: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_8: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_5: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_13: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_11: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_s_12: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_c_hall_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_c_hall_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_c_hall_5: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_c_hall_6: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_ent_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_ent_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_ent_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_ent_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_c_hall_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_c_hall_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_6: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_5: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_9: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_8: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_10: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_11: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_sw_left_7: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_3_end_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_3_end_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_3_safety_room_2: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_3_safety_room_1: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_3_end_5: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_3_end_4: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_3_safety_room_3: LocationData(counter.count(), LocType.Bonus),
    temple_location_names.pof_1_n_5: LocationData(counter.count()),
    temple_location_names.pof_1_ent_5: LocationData(counter.count()),
    temple_location_names.pof_1_end_1: LocationData(counter.count()),
    temple_location_names.pof_3_end_3: LocationData(counter.count()),
    temple_location_names.pof_puzzle_1: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.pof_puzzle_2: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.pof_puzzle_3: LocationData(counter.count(), LocType.Puzzle),
    temple_location_names.pof_puzzle_4: LocationData(counter.count(), LocType.Puzzle),
}

temple_enemy_loot_locations: typing.Dict[str, LocationData] = {
    temple_location_names.c3_miniboss_tick_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_miniboss_tick_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_4: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_5: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_6: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_7: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c3_tower_plant_small_8: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_miniboss_maggot_w_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_miniboss_maggot_w_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_miniboss_maggot_s_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_miniboss_maggot_s_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_miniboss_tick_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_miniboss_tick_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_4: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_5: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_6: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_7: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_8: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_9: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_10: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_11: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_12: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_13: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_14: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_15: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_16: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_17: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_18: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_19: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_20: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_21: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_22: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c2_tower_plant_small_23: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_miniboss_maggot_s_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_miniboss_maggot_s_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_miniboss_maggot_ne_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_miniboss_maggot_ne_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_miniboss_tick_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_miniboss_tick_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_4: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_4: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_5: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_6: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_7: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_8: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_9: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_10: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_11: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_12: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_13: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.c1_tower_plant_small_14: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_1_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_1_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_2_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_2_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_3_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_3_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_4_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_4_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b1_boss_worm_key: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.p_tower_plant_small_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.p_tower_plant_small_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.p_tower_plant_small_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.p_tower_plant_small_4: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.p_tower_plant_small_5: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.p_tower_plant_small_6: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t1_miniboss_mummy_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t1_miniboss_mummy_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t1_tower_fire: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t1_tower_ice: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_miniboss_mummy_w_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_miniboss_mummy_w_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_miniboss_mummy_e_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_miniboss_mummy_e_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_tower_fire: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_tower_mana_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_tower_mana_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t2_tower_mana_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t3_tower_fire_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t3_tower_fire_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t3_tower_ice_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t3_tower_ice_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t3_tower_ice_3: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t3_tower_mana_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.t3_tower_mana_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b3_tower_fire_1: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b3_tower_fire_2: LocationData(counter.count(), LocType.EnemyLoot),
    temple_location_names.b3_tower_fire_3: LocationData(counter.count(), LocType.EnemyLoot),
}

temple_button_locations: typing.Dict[str, LocationData] = {
    temple_location_names.btn_hub_pof: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_hub_pof_1: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_hub_pof_2: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_hub_pof_3: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_hub_pof_4: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c3_floor_fall: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c3_bridge: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c3_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_c3_pof: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c3_pof_1: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c3_pof_2: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c3_pof_3: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c3_pof_4: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c2_red: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c2_green: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c2_bridges: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c2_s_bridge: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c2_pumps: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c2_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_c2_pof: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c2_pof_1: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c2_pof_2: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c2_pof_3: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c2_pof_4: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c1_blue: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c1_red: LocationData(counter.count(2), LocType.Button),
    temple_location_names.btn_c1_green: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c1_puzzle_w: LocationData(counter.count(2), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_c1_puzzle_e: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_c1_pof: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_c1_pof_1: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c1_pof_2: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c1_pof_3: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c1_pof_4: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_c1_wall: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_b1_bridge: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_p_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t1_puzzle_w: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t1_puzzle_e: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t1_pof: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t1_pof_1: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t1_pof_2: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t1_pof_3: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t1_pof_4: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t1_wall_n_jail: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t1_wall_telarian: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t1_wall_n_hall: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t1_wall_guard: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t1_wall_runway: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t1_wall_e_jail: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_floor_blue: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_puzzle_n: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t2_puzzle_w: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t2_puzzle_e: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t2_puzzle_s: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t2_pof: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_pof_1: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_pof_2: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_pof_3: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_pof_4: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_rune_n: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_rune_se: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_rune_sw: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_rune_w: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_rune_e: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_wall_n_hidden_hall: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_nw_gate: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_jones_hall: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_t3_gate_w: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_t3_gate_e: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_boulder_room: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_w_ice_gate: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_n_node: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_portal_w: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_wall_portal_e: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t2_wall_jail_e: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_jail_w: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_s_gate_shortcut: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_s_gate_hall: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_e_ice_gate: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_pof: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_wall_jail_s: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t3_lever_2: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t3_lever_1: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t3_lever_3: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t3_lever_4: LocationData(counter.count(), LocType.Buttoninsanity),
    temple_location_names.btn_t3_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_t3_wall_fall_2: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t3_wall_fall_3: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t3_wall_blockade: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t3_wall_fall_1: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t3_wall_gate_s: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_pof_puzzle: LocationData(counter.count(), LocType.Button | LocType.Puzzle),
    temple_location_names.btn_pof_1_panel_se: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_pof_1_panel_n: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_pof_2_panel_e: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_pof_2_panel_w: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_pof_3_panel: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_floor_portal: LocationData(counter.count(), LocType.Button),

    temple_location_names.btn_t2_runes: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t2_portal: LocationData(counter.count(), LocType.Button),
    temple_location_names.btn_t3_levers: LocationData(counter.count(), LocType.Button),
}

temple_combo_button_locations: typing.List[str] = [
    temple_location_names.btn_hub_pof,
    temple_location_names.btn_c3_pof,
    temple_location_names.btn_c2_pof,
    temple_location_names.btn_c1_pof,
    temple_location_names.btn_t1_pof,
    temple_location_names.btn_t2_pof,
    # temple_location_names.btn_t2_runes,  # This location always needs to exist
    # temple_location_names.btn_t2_portal,
    # temple_location_names.btn_t3_levers,
]

# These locked items correspond to buttons that require logic even with buttonsanity off
temple_event_buttons = {
    temple_location_names.btn_c3_bridge: item_name.btn_c3_e_bridge,
    temple_location_names.btn_c2_pumps: item_name.btn_c2_pumps,
    temple_location_names.btn_hub_pof: item_name.btn_pof,
    temple_location_names.btn_c1_pof: item_name.btn_pof,
    temple_location_names.btn_c2_pof: item_name.btn_pof,
    temple_location_names.btn_c3_pof: item_name.btn_pof,
    temple_location_names.btn_t1_pof: item_name.btn_pof,
    temple_location_names.btn_t2_pof: item_name.btn_pof,
    temple_location_names.btn_pof_1_panel_se: item_name.btn_pof_1_walls_s,
    temple_location_names.btn_pof_1_panel_n: item_name.btn_pof_1_exit,
    temple_location_names.btn_pof_2_panel_w: item_name.btn_pof_2_exit,
    temple_location_names.btn_t2_floor_blue: item_name.btn_t2_blue,
    temple_location_names.btn_t2_runes: item_name.btn_t2_light_bridges,
    temple_location_names.btn_t2_rune_n: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_w: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_e: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_se: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_sw: item_name.btn_t2_light_bridges_part,
}

temple_button_items: typing.Dict[str, str] = {
    temple_location_names.btn_hub_pof_1: item_name.btn_pof_part,
    temple_location_names.btn_hub_pof_2: item_name.btn_pof_part,
    temple_location_names.btn_hub_pof_3: item_name.btn_pof_part,
    temple_location_names.btn_hub_pof_4: item_name.btn_pof_part,
    temple_location_names.btn_c3_pof_1: item_name.btn_pof_part,
    temple_location_names.btn_c3_pof_2: item_name.btn_pof_part,
    temple_location_names.btn_c3_pof_3: item_name.btn_pof_part,
    temple_location_names.btn_c3_pof_4: item_name.btn_pof_part,
    temple_location_names.btn_c2_pof_1: item_name.btn_pof_part,
    temple_location_names.btn_c2_pof_2: item_name.btn_pof_part,
    temple_location_names.btn_c2_pof_3: item_name.btn_pof_part,
    temple_location_names.btn_c2_pof_4: item_name.btn_pof_part,
    temple_location_names.btn_c1_pof_1: item_name.btn_pof_part,
    temple_location_names.btn_c1_pof_2: item_name.btn_pof_part,
    temple_location_names.btn_c1_pof_3: item_name.btn_pof_part,
    temple_location_names.btn_c1_pof_4: item_name.btn_pof_part,
    temple_location_names.btn_t1_pof_1: item_name.btn_pof_part,
    temple_location_names.btn_t1_pof_2: item_name.btn_pof_part,
    temple_location_names.btn_t1_pof_3: item_name.btn_pof_part,
    temple_location_names.btn_t1_pof_4: item_name.btn_pof_part,
    temple_location_names.btn_t2_pof_1: item_name.btn_pof_part,
    temple_location_names.btn_t2_pof_2: item_name.btn_pof_part,
    temple_location_names.btn_t2_pof_3: item_name.btn_pof_part,
    temple_location_names.btn_t2_pof_4: item_name.btn_pof_part,
    temple_location_names.btn_c3_floor_fall: item_name.btn_c3_fall_bridge,
    temple_location_names.btn_c3_bridge: item_name.btn_c3_e_bridge,
    temple_location_names.btn_c3_puzzle: item_name.btn_c3_puzzle,
    temple_location_names.btn_c2_red: item_name.btn_c2_red,
    temple_location_names.btn_c2_green: item_name.btn_c2_green,
    temple_location_names.btn_c2_bridges: item_name.btn_c2_bridges,
    temple_location_names.btn_c2_s_bridge: item_name.btn_c2_s_bridge,
    temple_location_names.btn_c2_pumps: item_name.btn_c2_pumps,
    temple_location_names.btn_c2_puzzle: item_name.btn_c2_puzzle,
    temple_location_names.btn_c1_blue: item_name.btn_c1_blue,
    temple_location_names.btn_c1_red: item_name.btn_c1_red,
    temple_location_names.btn_c1_green: item_name.btn_c1_green,
    temple_location_names.btn_c1_puzzle_e: item_name.btn_c1_puzzle_e,
    temple_location_names.btn_c1_puzzle_w: item_name.btn_c1_puzzle_w,
    temple_location_names.btn_c1_wall: item_name.btn_c1_tunnel,
    temple_location_names.btn_b1_bridge: item_name.btn_b1_bridge,
    temple_location_names.btn_p_puzzle: item_name.btn_p_puzzle,
    temple_location_names.btn_t1_puzzle_e: item_name.btn_t1_puzzle_e,
    temple_location_names.btn_t1_puzzle_w: item_name.btn_t1_puzzle_w,
    temple_location_names.btn_t1_wall_n_jail: item_name.btn_t1_jail_n,
    temple_location_names.btn_t1_wall_e_jail: item_name.btn_t1_jail_e,
    temple_location_names.btn_t1_wall_telarian: item_name.btn_t1_telarian,
    temple_location_names.btn_t1_wall_guard: item_name.btn_t1_guard,
    temple_location_names.btn_t1_wall_n_hall: item_name.btn_t1_hall,
    temple_location_names.btn_t1_wall_runway: item_name.btn_t1_runway,
    temple_location_names.btn_t2_floor_blue: item_name.btn_t2_blue,
    temple_location_names.btn_t2_puzzle_n: item_name.btn_t2_puzzle_n,
    temple_location_names.btn_t2_puzzle_e: item_name.btn_t2_puzzle_e,
    temple_location_names.btn_t2_puzzle_s: item_name.btn_t2_puzzle_s,
    temple_location_names.btn_t2_puzzle_w: item_name.btn_t2_puzzle_w,
    temple_location_names.btn_t2_rune_n: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_e: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_w: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_se: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_rune_sw: item_name.btn_t2_light_bridges_part,
    temple_location_names.btn_t2_wall_n_hidden_hall: item_name.btn_t2_jones_hall_back,
    temple_location_names.btn_t2_wall_nw_gate: item_name.btn_t2_nw_gate,
    temple_location_names.btn_t2_wall_jones_hall: item_name.btn_t2_jones_hall,
    temple_location_names.btn_t2_wall_t3_gate_e: item_name.btn_t2_t3_gate_e,
    temple_location_names.btn_t2_wall_t3_gate_w: item_name.btn_t2_t3_gate_w,
    temple_location_names.btn_t2_wall_boulder_room: item_name.btn_t2_boulder_passage,
    temple_location_names.btn_t2_wall_w_ice_gate: item_name.btn_t2_ice_gate_w,
    temple_location_names.btn_t2_wall_e_ice_gate: item_name.btn_t2_ice_gate_e,
    temple_location_names.btn_t2_wall_n_node: item_name.btn_t2_boulder_room,
    temple_location_names.btn_t2_wall_portal_w: item_name.btn_t2_portal_part,
    temple_location_names.btn_t2_wall_portal_e: item_name.btn_t2_portal_part,
    temple_location_names.btn_t2_wall_jail_w: item_name.btn_t2_jail_w,
    temple_location_names.btn_t2_wall_jail_e: item_name.btn_t2_jail_e,
    temple_location_names.btn_t2_wall_jail_s: item_name.btn_t2_s_spikes,
    temple_location_names.btn_t2_wall_s_gate_shortcut: item_name.btn_t2_s_gate_shortcut,
    temple_location_names.btn_t2_wall_s_gate_hall: item_name.btn_t2_s_gate_hall,
    temple_location_names.btn_t2_wall_pof: item_name.btn_t2_jail_s,
    temple_location_names.btn_t2_floor_portal: item_name.btn_t2_portal_gate,
    temple_location_names.btn_t3_lever_1: item_name.btn_t3_puzzle_room_part,
    temple_location_names.btn_t3_lever_2: item_name.btn_t3_puzzle_room_part,
    temple_location_names.btn_t3_lever_3: item_name.btn_t3_puzzle_room_part,
    temple_location_names.btn_t3_lever_4: item_name.btn_t3_puzzle_room_part,
    temple_location_names.btn_t3_puzzle: item_name.btn_t3_puzzle,
    temple_location_names.btn_t3_wall_fall_1: item_name.btn_t3_fall_1,
    temple_location_names.btn_t3_wall_fall_2: item_name.btn_t3_fall_2,
    temple_location_names.btn_t3_wall_fall_3: item_name.btn_t3_fall_3,
    temple_location_names.btn_t3_wall_blockade: item_name.btn_t3_pillars,
    temple_location_names.btn_t3_wall_gate_s: item_name.btn_t3_gate_s,
    temple_location_names.btn_pof_puzzle: item_name.btn_pof_puzzle,
    temple_location_names.btn_pof_1_panel_se: item_name.btn_pof_1_walls_s,
    temple_location_names.btn_pof_1_panel_n: item_name.btn_pof_1_exit,
    temple_location_names.btn_pof_2_panel_e: item_name.btn_pof_2_puzzle,
    temple_location_names.btn_pof_2_panel_w: item_name.btn_pof_2_exit,
    temple_location_names.btn_pof_3_panel: item_name.btn_pof_3_start,

    temple_location_names.btn_hub_pof: item_name.btn_pof,
    temple_location_names.btn_c3_pof: item_name.btn_pof,
    temple_location_names.btn_c2_pof: item_name.btn_pof,
    temple_location_names.btn_c1_pof: item_name.btn_pof,
    temple_location_names.btn_t1_pof: item_name.btn_pof,
    temple_location_names.btn_t2_pof: item_name.btn_pof,
    temple_location_names.btn_t2_runes: item_name.btn_t2_light_bridges,
    temple_location_names.btn_t2_portal: item_name.btn_t2_portal,
    temple_location_names.btn_t3_levers: item_name.btn_t3_puzzle_room,
}

temple_part_items: typing.Set[str] = {
    item_name.btn_pof_part,
    item_name.btn_t2_light_bridges_part,
    item_name.btn_t2_portal_part,
    item_name.btn_t3_puzzle_room_part,
}

temple_locations: typing.Dict[str, LocationData] = {
    **temple_pickup_locations,
    **temple_enemy_loot_locations,
    **temple_button_locations,
}

base_count = id_start + 0x10000 - 1
counter = Counter(base_count)
class_shop_table: typing.Dict[str, LocationData] = {}
for _player_class, shop_type_locs in shop_location_names.shop_class_location_names.items():
    for shop_tier_names in shop_type_locs.values():
        for shop_tier in shop_tier_names:
            class_shop_table.update(
                {shop_loc_name: LocationData(counter.count(), LocType.Shop) for shop_loc_name in shop_tier})
    base_count += 100
    counter = Counter(base_count)

shop_locations: typing.Dict[str, LocationData] = {
    **class_shop_table,
}
# for name, item_data in shop_locations.items():
#     print(f"{name}:{item_data.code}")

all_locations: typing.Dict[str, LocationData] = {
    **castle_locations,
    **temple_locations,
    **shop_locations,
}


def setup_locations(world: "HammerwatchWorld", hw_map: Campaign):
    location_table: typing.Dict[str, LocationData]
    hw_map_locations: typing.Dict[str, LocationData]
    item_counts: typing.Dict[str, int] = {}
    bonus_locations: typing.Dict[str, LocationData] = {}
    random_locations: typing.Dict[str, int] = {}
    button_items = {}
    map_button_items: typing.Dict[str, str]
    event_buttons: typing.Dict[str, str]
    combo_button_locs: typing.List[str]
    pickup_locs: typing.Dict[str, LocationData]
    enemy_loot_locs: typing.Dict[str, LocationData]

    location_table = {}
    if hw_map == Campaign.Castle:
        item_counts.update(castle_item_counts)
        map_button_items = castle_button_items
        button_locations = castle_button_locations
        combo_button_locs = castle_combo_button_locations
        hw_map_locations = get_base_locations(world, castle_pickup_locations, castle_enemy_loot_locations,
                                              button_locations, castle_event_buttons, combo_button_locs)
    else:  # Need a default case for this else tests will complain
        item_counts.update(temple_item_counts)
        map_button_items = temple_button_items
        button_locations = temple_button_locations
        combo_button_locs = temple_combo_button_locations
        hw_map_locations = get_base_locations(world, temple_pickup_locations, temple_enemy_loot_locations,
                                              button_locations, temple_event_buttons, combo_button_locs)

    if world.options.buttonsanity > 0:
        for loc, itm in map_button_items.items():
            if (button_locations[loc].loc_type & LocType.Buttoninsanity) == LocType.Buttoninsanity:
                continue
            if itm not in button_items:
                button_items[itm] = 0
            button_items[itm] += 1
        if hw_map == Campaign.Castle:
            # Special override as the spike puzzle locations exist for both buttonsanity options
            button_items.pop(item_name.btnc_p2_spike_puzzle_r_part)
            button_items.pop(item_name.btnc_p2_spike_puzzle_b_part)
            button_items.pop(item_name.btnc_p2_spike_puzzle_t_part)
            button_items[item_name.btnc_p2_spike_puzzle_r] = 1
            button_items[item_name.btnc_p2_spike_puzzle_b] = 1
            button_items[item_name.btnc_p2_spike_puzzle_t] = 1
    item_counts.update(button_items)

    # Add bonus locations if the setting is on, and add bonus locations to a special list for handling below
    for name, data in hw_map_locations.items():
        if data.loc_type & LocType.Bonus:
            bonus_locations[name] = data
            continue
        if data.loc_type & LocType.Recovery and not world.options.randomize_recovery_items:
            continue
        if data.loc_type & LocType.Puzzle and not world.options.randomize_puzzles:
            if name in map_button_items:
                item_counts[map_button_items[name]] -= 1
            continue
        location_table[name] = data

    # Shop locations
    classes = get_shopsanity_classes(world)
    for player_class in classes:
        for shop_type, shop_tier_counts in shop_location_names.shop_class_location_names[player_class].items():
            for loc_names in shop_tier_counts:
                location_table.update({loc_name: shop_locations[loc_name] for loc_name in loc_names})

    if hw_map == Campaign.Castle:  # Castle Hammerwatch
        location_table, item_counts, random_locations = set_castle_random_locations(world, location_table, item_counts)
    elif hw_map == Campaign.Temple:
        location_table, item_counts, random_locations = set_tots_random_locations(world, location_table, item_counts)

    item_counts, extra_items = get_item_counts(world, hw_map, item_counts)

    # Bonus level handling
    bonus_behavior = world.options.bonus_behavior.value
    if bonus_behavior == world.options.bonus_behavior.option_necessary:  # Necessary
        for i in range(min(extra_items, len(bonus_locations))):
            loc = world.random.choice(list(bonus_locations.keys()))
            location_table.update({loc: bonus_locations.pop(loc)})
    elif bonus_behavior == world.options.bonus_behavior.option_all:  # All
        location_table.update(bonus_locations)

    return location_table, item_counts, random_locations


def get_base_locations(world: "HammerwatchWorld", pickup_locs: typing.Dict[str, LocationData],
                       enemy_loot_locs: typing.Dict[str, LocationData], button_locs: typing.Dict[str, LocationData],
                       event_buttons: typing.Dict[str, str], combo_button_locs: typing.List[str]):
    location_table: typing.Dict[str, LocationData] = {}
    location_table.update(pickup_locs)
    if world.options.randomize_enemy_loot.value:
        location_table.update(enemy_loot_locs)

    button_locations: typing.Dict[str, LocationData] = {}
    if world.options.buttonsanity == world.options.buttonsanity.option_off:
        # Only add buttons that need locked items for logic
        button_locations.update({loc: button_locs[loc] for loc in event_buttons.keys()})
    elif get_buttonsanity_insanity(world):
        button_locations.update({loc: data for loc, data in button_locs.items()
                                 if loc not in combo_button_locs})
    else:
        # Add non-insanity buttons and the combo function buttons
        button_locations = {loc: data for loc, data in button_locs.items()
                            if (data.loc_type & LocType.Buttoninsanity) != LocType.Buttoninsanity}
        button_locations.update({loc: button_locs[loc] for loc in combo_button_locs})
    location_table.update(button_locations)

    return location_table


def set_castle_random_locations(world: "HammerwatchWorld", location_table: typing.Dict[str, LocationData],
                                item_counts: typing.Dict[str, int]):
    random_locations: typing.Dict[str, int] = {}

    if hasattr(world.multiworld, "re_gen_passthrough"):
        random_locations = world.multiworld.re_gen_passthrough["Hammerwatch"]["Random Locations"]
    if is_using_universal_tracker(world):
        item_counts.pop(item_name.loot_tower)
        item_counts.pop(item_name.loot_flower)
        return location_table, item_counts, random_locations

    def remove_location(location: str, loc_item: str):
        if location in location_table:
            location_table.pop(location)
        item_counts[loc_item] -= 1

    def remove_puzzle_locations(base_name: str, rloc_name: str):
        if random_locations[rloc_name] < 18:
            remove_location(f"{base_name}4", item_name.chest_purple)
        if random_locations[rloc_name] < 14:
            remove_location(f"{base_name}3", item_name.stat_upgrade)
        if random_locations[rloc_name] < 10:
            remove_location(f"{base_name}2", item_name.ankh)
        if random_locations[rloc_name] < 1:
            remove_location(f"{base_name}1", item_name.potion_rejuvenation)

    def keep_one_location(locations: typing.List[str], rloc_name: str):
        random_locations[rloc_name] = world.random.randrange(len(locations))
        locations.pop(random_locations[rloc_name])
        for location in locations:
            location_table.pop(location)
        return location_table

    def randomize_puzzle(rloc_name: str):
        pegs = 0
        for p in range(25):
            pegs += world.random.randrange(2)
        random_locations[rloc_name] = pegs

    puzzle_locs = {
        castle_location_names.crloc_p2_puzzle: castle_location_names.p2_puzzle_1,
        castle_location_names.crloc_a1_puzzle: castle_location_names.a1_puzzle_1,
        castle_location_names.crloc_a2_puzzle: castle_location_names.a2_puzzle_1,
        castle_location_names.crloc_r1_puzzle: castle_location_names.r1_puzzle_1,
        castle_location_names.crloc_r2_puzzle: castle_location_names.r2_puzzle_1,
        castle_location_names.crloc_ps_puzzle: castle_location_names.pstart_puzzle_1,
        castle_location_names.crloc_c2_puzzle: castle_location_names.c2_puzzle_1,
    }

    # Set puzzle random values
    if world.options.randomize_puzzles.value:
        for rloc in puzzle_locs.keys():
            randomize_puzzle(rloc)
    else:
        for rloc in puzzle_locs.keys():
            random_locations[rloc] = -1

    # Goal stuff
    if get_goal_type(world) != GoalType.FullCompletion:
        remove_location(castle_location_names.b4_plank_1, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_2, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_3, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_4, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_5, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_6, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_7, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_8, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_9, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_10, item_name.diamond_red)
        remove_location(castle_location_names.b4_plank_11, item_name.diamond_red)
        if world.options.randomize_recovery_items.value:
            remove_location(castle_location_names.e2_entrance, item_name.apple)
            remove_location(castle_location_names.e2_end, item_name.apple)
            remove_location(castle_location_names.e3_entrance_1, item_name.apple)
            remove_location(castle_location_names.e3_entrance_2, item_name.apple)
            remove_location(castle_location_names.e4_main, item_name.apple)

    # Shortcut teleporter
    if world.options.shortcut_teleporter.value:
        remove_location(castle_location_names.p2_by_boss_switch, item_name.potion_rejuvenation)
    else:
        remove_location(castle_location_names.p3_skip_boss_switch_1, item_name.diamond_small)
        remove_location(castle_location_names.p3_skip_boss_switch_2, item_name.diamond)
        remove_location(castle_location_names.p3_skip_boss_switch_3, item_name.diamond_small)
        remove_location(castle_location_names.p3_skip_boss_switch_4, item_name.diamond_small)
        remove_location(castle_location_names.p3_skip_boss_switch_5, item_name.diamond_small_red)
        remove_location(castle_location_names.p3_skip_boss_switch_6, item_name.diamond_small)

    # Prison Floor 1 Locations
    p1_bkey_1_locs: typing.List[str] = [
        castle_location_names.p1_entrance_s,
        castle_location_names.p1_entrance_w,
    ]
    location_table = keep_one_location(p1_bkey_1_locs, castle_location_names.crloc_p1_bronze_key_entrance)
    p1_bkey_2_locs: typing.List[str] = [
        castle_location_names.p1_by_sw_bronze_gate_1,
        castle_location_names.p1_s_w_bridges_w,
        castle_location_names.p1_by_sw_bronze_gate_4,
    ]
    location_table = keep_one_location(p1_bkey_2_locs, castle_location_names.crloc_p1_bronze_key_sw)
    p1_bkey_3_locs: typing.List[str] = [
        castle_location_names.p1_n_of_se_bridge,
        castle_location_names.p1_s_of_e_save_room,
        castle_location_names.p1_w_of_se_bronze_gate_5,
        castle_location_names.p1_w_of_se_bronze_gate_1,
    ]
    location_table = keep_one_location(p1_bkey_3_locs, castle_location_names.crloc_p1_bronze_key_se)
    p1_bkey_4_locs: typing.List[str] = [
        castle_location_names.p1_e_bridges_5,
        castle_location_names.p1_e_bridges_4,
        castle_location_names.p1_ne_arrow_traps,
    ]
    location_table = keep_one_location(p1_bkey_4_locs, castle_location_names.crloc_p1_bronze_key_e)
    p1_bkey_5_locs: typing.List[str] = [
        castle_location_names.p1_room_by_exit,
        castle_location_names.p1_by_exit_3,
    ]
    location_table = keep_one_location(p1_bkey_5_locs, castle_location_names.crloc_p1_bronze_key_n)
    # Prison Floor 2
    p2_bkey_1_locs: typing.List[str] = [
        castle_location_names.p2_entrance_1,
        castle_location_names.p2_entrance_2,
        castle_location_names.p2_entrance_3,
        castle_location_names.p2_entrance_4,
        castle_location_names.p2_w_of_gold_gate,
    ]
    location_table = keep_one_location(p2_bkey_1_locs, castle_location_names.crloc_p2_bkey_1)
    p2_bkey_2_locs: typing.List[str] = [
        castle_location_names.p2_e_gold_gate_room_3,
        castle_location_names.p2_e_gold_gate_room_2,
        castle_location_names.p2_e_gold_gate_room_1,
    ]
    location_table = keep_one_location(p2_bkey_2_locs, castle_location_names.crloc_p2_bkey_2)
    p2_bkey_3_locs: typing.List[str] = [
        castle_location_names.p2_e_gold_gate_room_4,
        castle_location_names.p2_e_gold_gate_room_5,
        castle_location_names.p2_e_gold_gate_room_6,
    ]
    location_table = keep_one_location(p2_bkey_3_locs, castle_location_names.crloc_p2_bkey_3)
    p2_bkey_4_locs: typing.List[str] = [
        castle_location_names.p2_e_gold_gate_room_13,
        castle_location_names.p2_e_gold_gate_room_12,
        castle_location_names.p2_e_gold_gate_room_11,
    ]
    location_table = keep_one_location(p2_bkey_4_locs, castle_location_names.crloc_p2_bkey_4)
    p2_skey_locs: typing.List[str] = [
        castle_location_names.p2_nw_island_5,
        castle_location_names.p2_nw_island_3,
        castle_location_names.p2_nw_island_4,
    ]
    location_table = keep_one_location(p2_skey_locs, castle_location_names.crloc_p2_skey)
    p2_gkey_1_locs: typing.List[str] = [
        castle_location_names.p2_e_of_red_spikes_2,
        castle_location_names.p2_e_of_red_spikes_3,
        castle_location_names.p2_e_of_red_spikes_4,
        castle_location_names.p2_e_of_red_spikes_1,
    ]
    location_table = keep_one_location(p2_gkey_1_locs, castle_location_names.crloc_p2_gkey_1)
    p2_gkey_2_locs: typing.List[str] = [
        castle_location_names.p2_beetle_boss_room_2,
        castle_location_names.p2_beetle_boss_room_1,
        castle_location_names.p2_beetle_boss_room_3,
    ]
    location_table = keep_one_location(p2_gkey_2_locs, castle_location_names.crloc_p2_gkey_2)
    if world.options.difficulty.value == world.options.difficulty.option_easier:
        remove_location(castle_location_names.p2_toggle_spike_trap_reward_2, item_name.chest_wood)
        remove_location(castle_location_names.p2_toggle_spike_trap_reward_3, item_name.chest_wood)
    # Prison Floor 3
    p3_bkey_1_locs: typing.List[str] = [
        castle_location_names.p3_entrance_w,
        castle_location_names.p3_entrance_n_1,
        castle_location_names.p3_entrance_n_2,
        castle_location_names.p3_entrance_m_4,
        castle_location_names.p3_entrance_n_of_poker,
    ]
    location_table = keep_one_location(p3_bkey_1_locs, castle_location_names.crloc_p3_bkey_1)
    p3_bkey_2_locs: typing.List[str] = [
        castle_location_names.p3_s_of_silver_gate,
        castle_location_names.p3_entrance_sw,
        castle_location_names.p3_entrance_s_3,
        castle_location_names.p3_entrance_s_of_poker_3,
    ]
    location_table = keep_one_location(p3_bkey_2_locs, castle_location_names.crloc_p3_bkey_2)
    p3_bkey_3_locs: typing.List[str] = [
        castle_location_names.p3_se_m_2,
        castle_location_names.p3_arrow_hall_1,
        castle_location_names.p3_arrow_hall_2,
        castle_location_names.p3_se_cross_hall_se,
    ]
    location_table = keep_one_location(p3_bkey_3_locs, castle_location_names.crloc_p3_bkey_3)
    p3_skey_1_locs: typing.List[str] = [
        castle_location_names.p3_nw_se,
        castle_location_names.p3_nw_m,
        castle_location_names.p3_nw_nw_3,
        castle_location_names.p3_nw_sw_1,
        castle_location_names.p3_nw_sw_2,
    ]
    location_table = keep_one_location(p3_skey_1_locs, castle_location_names.crloc_p3_skey)
    p3_gkey_1_locs: typing.List[str] = [
        castle_location_names.p3_w_of_bridge,
        castle_location_names.p3_nw_of_bridge,
        castle_location_names.p3_s_of_w_poker,
        castle_location_names.p3_w_of_w_poker,
        castle_location_names.p3_n_of_bridge_5,
    ]
    location_table = keep_one_location(p3_gkey_1_locs, castle_location_names.crloc_p3_gkey)
    # Remove puzzles
    if world.options.randomize_puzzles:
        for rloc, loc in puzzle_locs.items():
            remove_puzzle_locations(loc[:-1], rloc)
    # Enemy loot locations
    if world.options.randomize_enemy_loot.value:
        flower_locs = [
            castle_location_names.p2_tower_plant_1,
            castle_location_names.p2_tower_plant_2,
            castle_location_names.p3_tower_plant_1,
            castle_location_names.p3_tower_plant_2,
            castle_location_names.p3_tower_plant_3,
            castle_location_names.p3_tower_plant_4,
            castle_location_names.p3_tower_plant_5,
            castle_location_names.p3_tower_plant_6,
            castle_location_names.p3_tower_plant_7,
            castle_location_names.p3_tower_plant_8,
        ]
        flower_loot_chances = [
            (0.01, item_name.vendor_coin),
            (0.20, item_name.stat_upgrade)
        ]
        for loc in flower_locs:
            item = roll_for_item(world, flower_loot_chances)
            if item is None:
                remove_location(loc, item_name.loot_flower)
            else:
                item_counts[item] += 1
        tower_locs = [
            castle_location_names.a1_tower_ice_1,
            castle_location_names.a1_tower_ice_2,
            castle_location_names.a1_tower_ice_3,
            castle_location_names.a1_tower_ice_4,
            castle_location_names.a2_tower_ice_1,
            castle_location_names.a2_tower_ice_2,
            castle_location_names.a2_tower_ice_3,
            castle_location_names.a2_tower_ice_4,
            castle_location_names.a2_tower_ice_5,
            castle_location_names.a2_tower_ice_6,
            castle_location_names.a3_tower_ice_1,
            castle_location_names.a3_tower_ice_2,
            castle_location_names.a3_tower_ice_3,
            castle_location_names.a3_tower_ice_4,
            castle_location_names.a3_tower_ice_5,
            castle_location_names.a3_tower_ice_6,
            castle_location_names.a3_tower_ice_7,
            castle_location_names.a3_tower_ice_8,
            castle_location_names.a3_tower_ice_9,
            castle_location_names.r1_tower_plant_1,
            castle_location_names.r1_tower_plant_2,
            castle_location_names.r1_tower_plant_3,
            castle_location_names.r1_tower_plant_4,
            castle_location_names.r2_tower_plant_1,
            castle_location_names.r2_tower_plant_2,
            castle_location_names.r2_tower_plant_3,
            castle_location_names.r2_tower_plant_4,
            castle_location_names.r2_tower_plant_5,
            castle_location_names.r3_tower_plant_1,
            castle_location_names.r3_tower_plant_2,
            castle_location_names.r3_tower_plant_3,
            castle_location_names.r3_tower_plant_4,
            castle_location_names.r3_tower_plant_5,
            castle_location_names.r3_tower_plant_6,
            castle_location_names.r3_tower_plant_7,
            castle_location_names.r3_tower_plant_8,
            castle_location_names.r3_tower_plant_9,
            castle_location_names.r3_tower_plant_10,
            castle_location_names.c1_tower_plant_1,
            castle_location_names.c1_tower_plant_2,
            castle_location_names.c2_tower_plant_1,
            castle_location_names.c2_tower_plant_2,
            castle_location_names.c2_tower_plant_3,
            castle_location_names.c2_tower_plant_4,
            castle_location_names.c2_tower_plant_5,
            castle_location_names.c2_tower_plant_6,
            castle_location_names.c2_tower_plant_7,
            castle_location_names.c2_tower_plant_8,
            castle_location_names.c3_tower_plant_1,
            castle_location_names.c3_tower_plant_2,
            castle_location_names.c3_tower_plant_3,
            castle_location_names.c3_tower_plant_4,
            castle_location_names.c3_tower_plant_5,
            castle_location_names.c3_tower_plant_6,
            castle_location_names.c1_tower_ice_1,
            castle_location_names.c1_tower_ice_2,
            castle_location_names.c1_tower_ice_3,
            castle_location_names.c2_tower_ice_1,
            castle_location_names.c2_tower_ice_2,
            castle_location_names.c2_tower_ice_3,
            castle_location_names.c2_tower_ice_4,
            castle_location_names.c2_tower_ice_5,
            castle_location_names.c2_tower_ice_6,
            castle_location_names.c2_tower_ice_7,
            castle_location_names.c2_tower_ice_8,
            castle_location_names.c2_tower_ice_9,
            castle_location_names.c2_tower_ice_10,
            castle_location_names.c2_tower_ice_11,
            castle_location_names.c3_tower_ice_1,
            castle_location_names.c3_tower_ice_2,
            castle_location_names.c3_tower_ice_3,
            castle_location_names.c3_tower_ice_4,
            castle_location_names.c3_tower_ice_5,
            castle_location_names.c3_tower_ice_6,
            castle_location_names.c3_tower_ice_7,
            castle_location_names.c3_tower_ice_8,
            castle_location_names.c3_tower_ice_9,
            castle_location_names.c3_tower_ice_10,
        ]
        tower_loot_chances = [
            (0.05, item_name.vendor_coin),
            (0.20, item_name.stat_upgrade)
        ]
        for loc in tower_locs:
            item = roll_for_item(world, tower_loot_chances)
            if item is None:
                remove_location(loc, item_name.loot_tower)
            else:
                item_counts[item] += 1
    else:
        item_counts[item_name.vendor_coin] -= 17
        item_counts.pop(item_name.miniboss_stat_upgrade)
    item_counts.pop(item_name.loot_tower)
    item_counts.pop(item_name.loot_flower)

    return location_table, item_counts, random_locations


def set_tots_random_locations(world: "HammerwatchWorld", location_table: typing.Dict[str, LocationData],
                              item_counts: typing.Dict[str, int]):
    random_locations: typing.Dict[str, int] = {}

    if hasattr(world.multiworld, "re_gen_passthrough"):
        random_locations = world.multiworld.re_gen_passthrough["Hammerwatch"]["Random Locations"]
        item_counts.pop(item_name.loot_tower)
        item_counts.pop(item_name.loot_flower)
        item_counts.pop(item_name.loot_mini_flower)
        item_counts.pop(item_name.miniboss_stat_upgrade)
        return location_table, item_counts, random_locations

    buttonsanity = world.options.buttonsanity.value > 0

    def remove_location(location: str, loc_item: str):
        if not world.options.randomize_recovery_items.value and loc_item in recovery_table.keys():
            return
        location_table.pop(location)
        item_counts[loc_item] -= 1

    def remove_button(location: str):
        location_table.pop(location)
        button_item = temple_button_items[location]
        if button_item in item_counts:
            item_counts[button_item] -= 1

    def remove_puzzle_button(location: str):
        if buttonsanity and world.options.randomize_puzzles:
            remove_button(location)

    def remove_secret(secret_location: str):
        if secret_location in location_table.keys():
            remove_location(secret_location, item_name.secret)

    def remove_puzzle_locations(base_name: str, rloc_name: str):
        if random_locations[rloc_name] < 18:
            remove_location(f"{base_name}4", item_name.chest_purple)
        if random_locations[rloc_name] < 14:
            remove_location(f"{base_name}3", item_name.stat_upgrade)
        if random_locations[rloc_name] < 10:
            remove_location(f"{base_name}2", item_name.ankh)
        if random_locations[rloc_name] < 1:
            remove_location(f"{base_name}1", item_name.potion_rejuvenation)

    def keep_one_location(locations: typing.List[str], rloc_name: str):
        random_locations[rloc_name] = world.random.randrange(len(locations))
        locations.pop(random_locations[rloc_name])
        for location in locations:
            location_table.pop(location)
        return location_table

    def randomize_puzzle(rloc_name: str):
        pegs = 0
        for p in range(25):
            pegs += world.random.randrange(2)
        random_locations[rloc_name] = pegs

    # Secrets
    secret_locs = {
        temple_location_names.rloc_c3_secret_n: temple_location_names.cave3_secret_n,
        temple_location_names.rloc_c3_secret_nw: temple_location_names.cave3_secret_nw,
        temple_location_names.rloc_c3_secret_s: temple_location_names.cave3_secret_s,
        temple_location_names.rloc_c2_secret_1: temple_location_names.cave2_secret_ne,
        temple_location_names.rloc_c2_secret_2: temple_location_names.cave2_secret_w,
        temple_location_names.rloc_c2_secret_3: temple_location_names.cave2_secret_m,
        temple_location_names.rloc_c1_secret_1: temple_location_names.cave1_secret_nw,
        temple_location_names.rloc_c1_secret_2: temple_location_names.cave1_secret_n_hidden_room,
        temple_location_names.rloc_c1_secret_3: temple_location_names.cave1_secret_ne,
        temple_location_names.rloc_c1_secret_4: temple_location_names.cave1_secret_w,
        temple_location_names.rloc_c1_secret_5: temple_location_names.cave1_secret_m,
        temple_location_names.rloc_c1_secret_6: temple_location_names.cave1_secret_e,
        temple_location_names.rloc_b1_secret: temple_location_names.boss1_secret,
        temple_location_names.rloc_p_secret_1: temple_location_names.p_ent2_secret,
        temple_location_names.rloc_p_secret_2: temple_location_names.p_mid3_secret_1,
        temple_location_names.rloc_p_secret_3: temple_location_names.p_mid3_secret_2,
        temple_location_names.rloc_p_secret_4: temple_location_names.p_mid3_secret_3,
        temple_location_names.rloc_p_secret_5: temple_location_names.p_mid3_secret_4,
        temple_location_names.rloc_p_secret_6: temple_location_names.p_end1_secret,
        temple_location_names.rloc_p_secret_7: temple_location_names.p_mid5_secret,
    }
    if world.options.randomize_secrets.value:
        for secret_key in secret_locs.keys():
            random_locations[secret_key] = world.random.randrange(2)
    else:
        for secret_key in secret_locs.keys():
            random_locations[secret_key] = 0
    for rloc_, loc_ in secret_locs.items():
        if random_locations[rloc_] == 0:
            remove_secret(loc_)

    # Set puzzle random values
    puzzle_locs = {
        temple_location_names.rloc_c3_puzzle: temple_location_names.c3_puzzle_1,
        temple_location_names.rloc_c2_puzzle: temple_location_names.c2_puzzle_1,
        temple_location_names.rloc_c1_puzzle_n: temple_location_names.c1_n_puzzle_1,
        temple_location_names.rloc_c1_puzzle_e: temple_location_names.c1_e_puzzle_1,
        temple_location_names.rloc_p_puzzle: temple_location_names.p_puzzle_1,
        temple_location_names.rloc_t1_puzzle_w: temple_location_names.t1_w_puzzle_1,
        temple_location_names.rloc_t1_puzzle_e: temple_location_names.t1_e_puzzle_1,
        temple_location_names.rloc_t2_puzzle_n: temple_location_names.t2_n_puzzle_1,
        temple_location_names.rloc_t2_puzzle_nw: temple_location_names.t2_nw_puzzle_1,
        temple_location_names.rloc_t2_puzzle_e: temple_location_names.t2_e_puzzle_1,
        temple_location_names.rloc_t2_puzzle_sw: temple_location_names.t2_sw_puzzle_1,
        temple_location_names.rloc_t3_puzzle: temple_location_names.t3_puzzle_1,
        temple_location_names.rloc_pof_puzzle: temple_location_names.pof_puzzle_1,
    }
    if world.options.randomize_puzzles.value:
        for puzzle_loc in puzzle_locs.keys():
            randomize_puzzle(puzzle_loc)
    else:
        for puzzle_loc in puzzle_locs.keys():
            random_locations[puzzle_loc] = -1

    # Goal stuff
    if get_goal_type(world) == GoalType.AltCompletion:
        remove_location(temple_location_names.hub_pof_reward, item_name.ankh)
    # Dunes
    random_locations[temple_location_names.rloc_t3_entrance] = world.random.randrange(3)
    # Cave level 3
    random_locations[temple_location_names.rloc_squire] = world.random.randrange(6)
    if random_locations[temple_location_names.rloc_squire] != 1:
        remove_location(temple_location_names.cave3_squire, item_name.stat_upgrade)
    # Pan location
    pan_locations: typing.List[str] = [
        temple_location_names.cave3_nw,
        temple_location_names.cave3_m,
        temple_location_names.cave3_se,
        temple_location_names.cave2_nw_2,
        temple_location_names.cave2_red_bridge_4,
        temple_location_names.cave2_double_bridge_r,
        temple_location_names.cave1_n_bridges_4,
        temple_location_names.cave1_double_room_l,
        temple_location_names.cave1_e_3,
    ]
    location_table = keep_one_location(pan_locations, temple_location_names.rloc_pan)
    # Cave level 2
    c2_keystone_locations: typing.List[str] = [
        temple_location_names.cave2_guard_s,
        temple_location_names.cave2_nw_3,
        temple_location_names.cave2_w_miniboss_4,
        temple_location_names.cave2_red_bridge_3,
        temple_location_names.cave2_below_pumps_3
    ]
    location_table = keep_one_location(c2_keystone_locations, temple_location_names.rloc_c2_keystone)
    random_locations[temple_location_names.rloc_c2_portal] = world.random.randrange(3)
    if random_locations[temple_location_names.rloc_c2_portal] == 0:
        remove_location(temple_location_names.cave2_nw_4, item_name.apple)
        remove_location(temple_location_names.cave2_nw_5, item_name.apple)
    elif random_locations[temple_location_names.rloc_c2_portal] == 1:
        remove_location(temple_location_names.cave2_pumps_n, item_name.vendor_coin)
    random_locations[temple_location_names.rloc_c2_hidden_room] = world.random.randrange(4)
    if random_locations[temple_location_names.rloc_c2_hidden_room] >= 2:
        remove_location(temple_location_names.cave2_sw_hidden_room_1, item_name.vendor_coin)
        remove_location(temple_location_names.cave2_sw_hidden_room_2, item_name.stat_upgrade)
        remove_location(temple_location_names.cave2_sw_hidden_room_3, item_name.ankh)
        remove_location(temple_location_names.cave2_sw_hidden_room_4, item_name.chest_wood)
    # Cave level 1
    c1_keystone_locations: typing.List[str] = [
        temple_location_names.cave1_ne_grubs,
        temple_location_names.cave1_w_by_water_2,
        temple_location_names.cave1_m
    ]
    location_table = keep_one_location(c1_keystone_locations, temple_location_names.rloc_c1_keystone)
    random_locations[temple_location_names.rloc_c1_portal] = world.random.randrange(3)
    if random_locations[temple_location_names.rloc_c1_portal] == 0:
        remove_location(temple_location_names.cave1_n_bridges_5, item_name.chest_wood)
    random_locations[temple_location_names.rloc_c1_hidden_room] = world.random.randrange(4)
    if random_locations[temple_location_names.rloc_c1_hidden_room] >= 2:
        remove_location(temple_location_names.cave1_ne_hidden_room_1, item_name.chest_wood)
        remove_location(temple_location_names.cave1_ne_hidden_room_2, item_name.chest_wood)
        remove_location(temple_location_names.cave1_ne_hidden_room_3, item_name.stat_upgrade)
        remove_location(temple_location_names.cave1_ne_hidden_room_4, item_name.vendor_coin)
        remove_location(temple_location_names.cave1_ne_hidden_room_5, item_name.chest_wood)
        remove_secret(temple_location_names.cave1_secret_n_hidden_room)
        remove_location(temple_location_names.cave1_secret_tunnel_1, item_name.ankh)
        remove_location(temple_location_names.cave1_secret_tunnel_2, item_name.steak)
        remove_location(temple_location_names.cave1_secret_tunnel_3, item_name.mana_2)
        if buttonsanity:
            remove_button(temple_location_names.btn_c1_wall)
    random_locations[temple_location_names.rloc_c1_hall_e] = world.random.randrange(4)
    random_locations[temple_location_names.rloc_c1_exit] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_c1_exit] == 0:
        random_locations[temple_location_names.rloc_c1_puzzle_e] = -1
        remove_puzzle_button(temple_location_names.btn_c1_puzzle_e)
    # Passage
    random_locations[temple_location_names.rloc_passage_entrance] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_passage_entrance] == 0:
        remove_secret(temple_location_names.p_ent2_secret)
    random_locations[temple_location_names.rloc_passage_middle] = world.random.randrange(5)
    mid_locations_to_remove: typing.List[str] = [
        temple_location_names.p_mid1_1,
        temple_location_names.p_mid1_2,
        temple_location_names.p_mid2_1,
        temple_location_names.p_mid2_2,
        temple_location_names.p_mid2_3,
        temple_location_names.p_mid2_4,
        temple_location_names.p_mid3_secret_1,
        temple_location_names.p_mid3_secret_2,
        temple_location_names.p_mid3_secret_3,
        temple_location_names.p_mid3_secret_4,
        temple_location_names.p_mid4_1,
        temple_location_names.p_mid4_2,
        temple_location_names.p_mid4_3,
        temple_location_names.p_mid4_4,
        temple_location_names.p_mid5_1,
        temple_location_names.p_mid5_2,
        temple_location_names.p_mid5_secret,
        temple_location_names.p_tower_plant_small_1,
        temple_location_names.p_tower_plant_small_2,
        temple_location_names.p_tower_plant_small_3,
        temple_location_names.p_tower_plant_small_4,
        temple_location_names.p_tower_plant_small_5,
        temple_location_names.p_tower_plant_small_6,
    ]
    item_counts[item_name.ankh] -= 2
    item_counts[item_name.apple] -= 2
    item_counts[item_name.mana_2] -= 1
    item_counts[item_name.mana_1] -= 3
    item_counts[item_name.orange] -= 1
    item_counts[item_name.stat_upgrade] -= 2
    item_counts[item_name.chest_wood] -= 3
    if random_locations[temple_location_names.rloc_passage_middle] == 0:
        mid_locations_to_remove.remove(temple_location_names.p_mid1_1)
        mid_locations_to_remove.remove(temple_location_names.p_mid1_2)
        item_counts[item_name.chest_wood] += 2
    elif random_locations[temple_location_names.rloc_passage_middle] == 1:
        mid_locations_to_remove.remove(temple_location_names.p_mid2_1)
        mid_locations_to_remove.remove(temple_location_names.p_mid2_2)
        mid_locations_to_remove.remove(temple_location_names.p_mid2_3)
        mid_locations_to_remove.remove(temple_location_names.p_mid2_4)
        item_counts[item_name.mana_2] += 1
        item_counts[item_name.mana_1] += 3
    elif random_locations[temple_location_names.rloc_passage_middle] == 2:
        mid_locations_to_remove.remove(temple_location_names.p_mid3_secret_1)
        mid_locations_to_remove.remove(temple_location_names.p_mid3_secret_2)
        mid_locations_to_remove.remove(temple_location_names.p_mid3_secret_3)
        mid_locations_to_remove.remove(temple_location_names.p_mid3_secret_4)
    elif random_locations[temple_location_names.rloc_passage_middle] == 3:
        mid_locations_to_remove.remove(temple_location_names.p_mid4_1)
        mid_locations_to_remove.remove(temple_location_names.p_mid4_2)
        mid_locations_to_remove.remove(temple_location_names.p_mid4_3)
        mid_locations_to_remove.remove(temple_location_names.p_mid4_4)
        mid_locations_to_remove.remove(temple_location_names.p_tower_plant_small_1)
        mid_locations_to_remove.remove(temple_location_names.p_tower_plant_small_2)
        mid_locations_to_remove.remove(temple_location_names.p_tower_plant_small_3)
        mid_locations_to_remove.remove(temple_location_names.p_tower_plant_small_4)
        mid_locations_to_remove.remove(temple_location_names.p_tower_plant_small_5)
        mid_locations_to_remove.remove(temple_location_names.p_tower_plant_small_6)
        item_counts[item_name.ankh] += 1
        item_counts[item_name.orange] += 1
        item_counts[item_name.apple] += 2
    else:
        mid_locations_to_remove.remove(temple_location_names.p_mid5_1)
        mid_locations_to_remove.remove(temple_location_names.p_mid5_2)
        item_counts[item_name.chest_wood] += 1
        item_counts[item_name.stat_upgrade] += 1
        mid_locations_to_remove.remove(temple_location_names.p_mid5_secret)
    # Remove puzzle locations
    if random_locations[temple_location_names.rloc_passage_middle] != 2:
        random_locations[temple_location_names.rloc_p_puzzle] = -1
        remove_puzzle_button(temple_location_names.btn_p_puzzle)
    for loc in mid_locations_to_remove:
        if temple_locations[loc].loc_type == LocType.Secret:
            remove_secret(loc)
        elif loc in location_table:
            location_table.pop(loc)
    random_locations[temple_location_names.rloc_passage_end] = world.random.randrange(3)
    random_locations[temple_location_names.rloc_p_alley] = world.random.randrange(4)
    end_locations_to_remove: typing.List[str] = [
        temple_location_names.p_end1_secret,
        temple_location_names.p_end3_1,
        temple_location_names.p_end3_2,
    ]
    if random_locations[temple_location_names.rloc_passage_end] == 0:
        end_locations_to_remove.remove(temple_location_names.p_end1_secret)
    elif random_locations[temple_location_names.rloc_passage_end] == 2\
            and random_locations[temple_location_names.rloc_p_alley] < 2:
        end_locations_to_remove.remove(temple_location_names.p_end3_1)
        end_locations_to_remove.remove(temple_location_names.p_end3_2)
        item_counts[item_name.ankh] += 1
        item_counts[item_name.stat_upgrade] += 1
    for loc in end_locations_to_remove:
        if temple_locations[loc].loc_type == LocType.Secret:
            remove_secret(loc)
        else:
            location_table.pop(loc)
    # Temple level 1
    # Custom logic for the keystone location, as a diamond spawns in one of the spots if it doesn't appear there
    t1_keystone_locations: typing.List[str] = [
        temple_location_names.t1_sun_block_hall_4,
        temple_location_names.t1_fire_trap_by_sun_turret_3,
        temple_location_names.t1_ledge_after_block_trap_1,
        temple_location_names.t1_sw_sdoor_3
    ]
    random_locations[temple_location_names.rloc_t1_keystone] = world.random.randrange(len(t1_keystone_locations))
    t1_keystone_locations.pop(random_locations[temple_location_names.rloc_t1_keystone])
    if random_locations[temple_location_names.rloc_t1_keystone] == 2:  # Remove the diamond that would spawn there
        item_counts[item_name.diamond_small] -= 1
    else:
        t1_keystone_locations.remove(temple_location_names.t1_ledge_after_block_trap_1)  # Remove the diamond-filled loc
    for loc in t1_keystone_locations:
        location_table.pop(loc)
    random_locations[temple_location_names.rloc_t1_portal] = world.random.randrange(3)
    if random_locations[temple_location_names.rloc_t1_portal] == 2:
        remove_location(temple_location_names.t1_sun_turret_3, item_name.chest_green)
    t1_silver_key_s_locations: typing.List[str] = [
        temple_location_names.t1_s_bridge_1,
        temple_location_names.t1_above_s_bridge,
        temple_location_names.t1_sw_corner_room,
    ]
    location_table = keep_one_location(t1_silver_key_s_locations,
                                       temple_location_names.rloc_t1_silver_key_s)
    t1_silver_key_n_locations: typing.List[str] = [
        temple_location_names.t1_n_sunbeam_treasure_3,
        temple_location_names.t1_boulder_hallway_by_ice_turret_4,
    ]
    location_table = keep_one_location(t1_silver_key_n_locations,
                                       temple_location_names.rloc_t1_silver_key_n)
    t1_silver_key_ice_turret_locations: typing.List[str] = [
        temple_location_names.t1_ice_turret_1,
        temple_location_names.t1_ice_turret_2,
    ]
    location_table = keep_one_location(t1_silver_key_ice_turret_locations,
                                       temple_location_names.rloc_t1_silver_key_ice_turret)
    random_locations[temple_location_names.rloc_t1_silver_key_funky] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t1_silver_key_funky] == 0:
        location_table.pop(temple_location_names.t1_e_of_double_gate_room_2)
        random_locations[temple_location_names.rloc_t1_ore_funky] = world.random.randrange(2)
    else:
        random_locations[temple_location_names.rloc_t1_ore_funky] = -1
    if random_locations[temple_location_names.rloc_t1_ore_funky] != 0:
        location_table.pop(temple_location_names.t1_fire_trap_by_sun_turret_4)
    if random_locations[temple_location_names.rloc_t1_ore_funky] != 1:
        location_table.pop(temple_location_names.t1_mana_drain_fire_trap)
    t1_gold_key_locations: typing.List[str] = [
        temple_location_names.t1_n_cache_by_ice_turret_5,
        temple_location_names.t1_s_cache_by_ice_turret_3,
    ]
    location_table = keep_one_location(t1_gold_key_locations, temple_location_names.rloc_t1_gold_key)
    t1_ore_e_locations: typing.List[str] = [
        temple_location_names.t1_sun_block_hall_3,
        temple_location_names.t1_e_gold_beetles,
    ]
    location_table = keep_one_location(t1_ore_e_locations, temple_location_names.rloc_t1_ore_e)
    t1_mirror_locations: typing.List[str] = [
        temple_location_names.t1_ledge_after_block_trap_2,
        temple_location_names.t1_ice_block_chamber_3,
        temple_location_names.t1_ice_block_chamber_2
    ]
    location_table = keep_one_location(t1_mirror_locations, temple_location_names.rloc_t1_mirror)
    # There's a 1/5 chance to potentially open the way to the hidden room
    random_locations[temple_location_names.rloc_t1_sw_hidden_room_random_node] = world.random.randrange(5)
    random_locations[temple_location_names.rloc_t1_sw_hidden_room] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t1_sw_hidden_room_random_node] != 1\
            or random_locations[temple_location_names.rloc_t1_sw_hidden_room] == 1:
        remove_location(temple_location_names.t1_sw_hidden_room_1, item_name.vendor_coin)
        remove_location(temple_location_names.t1_sw_hidden_room_2, item_name.stat_upgrade)
        remove_location(temple_location_names.t1_sw_hidden_room_3, item_name.ankh)
        remove_location(temple_location_names.t1_sw_hidden_room_4, item_name.chest_green)
        random_locations[temple_location_names.rloc_t1_sw_hidden_room] = 1
    random_locations[temple_location_names.rloc_t1_puzzle_spawn] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t1_puzzle_spawn] == 0:
        random_locations[temple_location_names.rloc_t1_puzzle_e] = -1
        remove_puzzle_button(temple_location_names.btn_t1_puzzle_e)
    else:
        random_locations[temple_location_names.rloc_t1_puzzle_w] = -1
        remove_puzzle_button(temple_location_names.btn_t1_puzzle_w)
    # Temple Level 2
    t2_keystone_locations: typing.List[str] = [
        temple_location_names.t2_se_banner_chamber_5,
        temple_location_names.t2_s_balcony_2,
        temple_location_names.t2_s_of_portal,
        temple_location_names.t2_n_of_sw_gate_2,
        temple_location_names.t2_nw_ice_turret_4,
        temple_location_names.t2_boulder_chamber_3,
        temple_location_names.t2_left_of_pof_switch_2,
    ]
    location_table = keep_one_location(t2_keystone_locations, temple_location_names.rloc_t2_keystone)
    random_locations[temple_location_names.rloc_t2_entrance] = world.random.randrange(2)
    random_locations[temple_location_names.rloc_t2_portal] = world.random.randrange(4)
    if random_locations[temple_location_names.rloc_t2_portal] != 2:
        remove_location(temple_location_names.t2_teleporter, item_name.stat_upgrade)
        if world.options.buttonsanity.value == world.options.buttonsanity.option_insanity:
            remove_button(temple_location_names.btn_t2_wall_portal_w)
            remove_button(temple_location_names.btn_t2_wall_portal_e)
        elif world.options.buttonsanity.value > 0:
            remove_button(temple_location_names.btn_t2_portal)
    random_locations[temple_location_names.rloc_t2_puzzle_spawn_1] = world.random.randrange(2)
    random_locations[temple_location_names.rloc_t2_w_hidden_room] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t2_puzzle_spawn_1] == 0:
        random_locations[temple_location_names.rloc_t2_puzzle_e] = -1  # Turn off east puzzle
        remove_puzzle_button(temple_location_names.btn_t2_puzzle_e)
    else:
        random_locations[temple_location_names.rloc_t2_puzzle_nw] = -1
        remove_puzzle_button(temple_location_names.btn_t2_puzzle_w)
        random_locations[temple_location_names.rloc_t2_w_hidden_room] = 1
    if random_locations[temple_location_names.rloc_t2_w_hidden_room] != 0:
        # Prevent items from appearing behind the west puzzle in the cache
        remove_location(temple_location_names.t2_nw_puzzle_cache_1, item_name.chest_blue)
        remove_location(temple_location_names.t2_nw_puzzle_cache_2, item_name.chest_blue)
        remove_location(temple_location_names.t2_nw_puzzle_cache_3, item_name.vendor_coin)
        remove_location(temple_location_names.t2_nw_puzzle_cache_4, item_name.stat_upgrade)
        remove_location(temple_location_names.t2_nw_puzzle_cache_5, item_name.ankh)
    random_locations[temple_location_names.rloc_t2_puzzle_spawn_2] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t2_puzzle_spawn_2] == 0:
        random_locations[temple_location_names.rloc_t2_puzzle_n] = -1
        remove_puzzle_button(temple_location_names.btn_t2_puzzle_n)
    else:
        random_locations[temple_location_names.rloc_t2_puzzle_sw] = -1
        remove_puzzle_button(temple_location_names.btn_t2_puzzle_s)
    random_locations[temple_location_names.rloc_t2_jones_reward] = world.random.randrange(2)
    t2_gold_key_locations: typing.List[str] = [
        temple_location_names.t2_right_of_pof_switch,
        temple_location_names.t2_sw_jail_2,
        temple_location_names.t2_boulder_room_2,
    ]
    if random_locations[temple_location_names.rloc_t2_jones_reward] == 0:
        location_table = keep_one_location(t2_gold_key_locations, temple_location_names.rloc_t2_gold_key)
    else:
        item_counts[item_name.stat_upgrade] -= 1
        for loc in t2_gold_key_locations:
            location_table.pop(loc)
    t2_silver_key_1_locations: typing.List[str] = [
        temple_location_names.t2_fire_trap_maze_5,
        temple_location_names.t2_fire_trap_maze_6,
        temple_location_names.t2_w_hall_dead_end_5,
        temple_location_names.t2_nw_of_s_ice_turret,
        temple_location_names.t2_n_of_portal,
    ]
    location_table = keep_one_location(t2_silver_key_1_locations,
                                       temple_location_names.rloc_t2_silver_key_1)
    t2_silver_key_2_locations: typing.List[str] = [
        temple_location_names.t2_se_fireball_hall,
        temple_location_names.t2_se_banner_chamber_4,
        temple_location_names.t2_s_balcony_1,
        temple_location_names.t2_boulder_chamber_4,
    ]
    location_table = keep_one_location(t2_silver_key_2_locations,
                                       temple_location_names.rloc_t2_silver_key_2)
    t2_pickaxe_locations: typing.List[str] = [
        temple_location_names.t2_w_ice_block_gate,
        temple_location_names.t2_e_ice_block_gate
    ]
    location_table = keep_one_location(t2_pickaxe_locations, temple_location_names.rloc_t2_pickaxe)
    if buttonsanity:
        if random_locations[temple_location_names.rloc_t2_pickaxe] == 0:
            remove_button(temple_location_names.btn_t2_wall_e_ice_gate)
        else:
            remove_button(temple_location_names.btn_t2_wall_w_ice_gate)
    # Temple Level 3
    random_locations[temple_location_names.rloc_t3_s_beam_1] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t3_s_beam_1] == 0:
        remove_location(temple_location_names.t3_n_node_blocks_1, item_name.vendor_coin)
    random_locations[temple_location_names.rloc_t3_s_beam_2] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t3_s_beam_2] == 0:
        remove_location(temple_location_names.t3_n_node_blocks_2, item_name.vendor_coin)
    random_locations[temple_location_names.rloc_t3_s_beam_3] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t3_s_beam_3] == 0:
        remove_location(temple_location_names.t3_n_node_blocks_3, item_name.vendor_coin)
    random_locations[temple_location_names.rloc_t3_s_beam_4] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t3_s_beam_4] == 0:
        remove_location(temple_location_names.t3_n_node_blocks_4, item_name.vendor_coin)
    random_locations[temple_location_names.rloc_t3_s_beam_5] = world.random.randrange(2)
    if random_locations[temple_location_names.rloc_t3_s_beam_5] == 0:
        remove_location(temple_location_names.t3_n_node_blocks_5, item_name.vendor_coin)

    # Remove puzzle locations
    if world.options.randomize_puzzles:
        for rloc, loc in puzzle_locs.items():
            remove_puzzle_locations(loc[:-1], rloc)
    else:
        item_counts[item_name.chest_purple] -= len(puzzle_locs)
        item_counts[item_name.stat_upgrade] -= len(puzzle_locs)
        item_counts[item_name.ankh] -= len(puzzle_locs)
        item_counts[item_name.potion_rejuvenation] -= len(puzzle_locs)

    # Enemy loot locations
    if world.options.randomize_enemy_loot.value:
        flower_locs = [
            temple_location_names.c3_tower_plant,
            temple_location_names.c2_tower_plant_1,
            temple_location_names.c2_tower_plant_2,
            temple_location_names.c2_tower_plant_3,
            temple_location_names.c1_tower_plant_1,
            temple_location_names.c1_tower_plant_2,
            temple_location_names.c1_tower_plant_3,
            temple_location_names.c1_tower_plant_4,
        ]
        flower_loot_chances = [
            (0.01, item_name.vendor_coin),
            (0.20, item_name.stat_upgrade)
        ]
        for loc in flower_locs:
            item = roll_for_item(world, flower_loot_chances)
            if item is None:
                remove_location(loc, item_name.loot_flower)
            else:
                item_counts[item] += 1
        mini_flower_locs = [
            temple_location_names.c3_tower_plant_small_1,
            temple_location_names.c3_tower_plant_small_2,
            temple_location_names.c3_tower_plant_small_3,
            temple_location_names.c3_tower_plant_small_4,
            temple_location_names.c3_tower_plant_small_5,
            temple_location_names.c3_tower_plant_small_6,
            temple_location_names.c3_tower_plant_small_7,
            temple_location_names.c3_tower_plant_small_8,
            temple_location_names.c2_tower_plant_small_1,
            temple_location_names.c2_tower_plant_small_2,
            temple_location_names.c2_tower_plant_small_3,
            temple_location_names.c2_tower_plant_small_4,
            temple_location_names.c2_tower_plant_small_5,
            temple_location_names.c2_tower_plant_small_6,
            temple_location_names.c2_tower_plant_small_7,
            temple_location_names.c2_tower_plant_small_8,
            temple_location_names.c2_tower_plant_small_9,
            temple_location_names.c2_tower_plant_small_10,
            temple_location_names.c2_tower_plant_small_11,
            temple_location_names.c2_tower_plant_small_12,
            temple_location_names.c2_tower_plant_small_13,
            temple_location_names.c2_tower_plant_small_14,
            temple_location_names.c2_tower_plant_small_15,
            temple_location_names.c2_tower_plant_small_16,
            temple_location_names.c2_tower_plant_small_17,
            temple_location_names.c2_tower_plant_small_18,
            temple_location_names.c2_tower_plant_small_19,
            temple_location_names.c2_tower_plant_small_20,
            temple_location_names.c2_tower_plant_small_21,
            temple_location_names.c2_tower_plant_small_22,
            temple_location_names.c2_tower_plant_small_23,
            temple_location_names.c1_tower_plant_small_1,
            temple_location_names.c1_tower_plant_small_2,
            temple_location_names.c1_tower_plant_small_3,
            temple_location_names.c1_tower_plant_small_4,
            temple_location_names.c1_tower_plant_small_5,
            temple_location_names.c1_tower_plant_small_6,
            temple_location_names.c1_tower_plant_small_7,
            temple_location_names.c1_tower_plant_small_8,
            temple_location_names.c1_tower_plant_small_9,
            temple_location_names.c1_tower_plant_small_10,
            temple_location_names.c1_tower_plant_small_11,
            temple_location_names.c1_tower_plant_small_12,
            temple_location_names.c1_tower_plant_small_13,
            temple_location_names.c1_tower_plant_small_14,
            temple_location_names.p_tower_plant_small_1,
            temple_location_names.p_tower_plant_small_2,
            temple_location_names.p_tower_plant_small_3,
            temple_location_names.p_tower_plant_small_4,
            temple_location_names.p_tower_plant_small_5,
            temple_location_names.p_tower_plant_small_6,
        ]
        mini_flower_loot_chances = [
            (0.05, item_name.vendor_coin),
            (0.25, item_name.valuable_6)
        ]
        for loc in mini_flower_locs:
            item = roll_for_item(world, mini_flower_loot_chances)
            if item is None:
                if loc in location_table.keys():
                    remove_location(loc, item_name.loot_mini_flower)
            else:
                item_counts[item] += 1
        tower_locs = [
            temple_location_names.t1_tower_fire,
            temple_location_names.t1_tower_ice,
            temple_location_names.t2_tower_fire,
            temple_location_names.t2_tower_ice_1,
            temple_location_names.t2_tower_ice_2,
            temple_location_names.t2_tower_ice_3,
            temple_location_names.t2_tower_mana_1,
            temple_location_names.t2_tower_mana_2,
            temple_location_names.t2_tower_mana_3,
            temple_location_names.t3_tower_fire_1,
            temple_location_names.t3_tower_fire_2,
            temple_location_names.t3_tower_ice_1,
            temple_location_names.t3_tower_ice_2,
            temple_location_names.t3_tower_ice_3,
            temple_location_names.t3_tower_mana_1,
            temple_location_names.t3_tower_mana_2,
            temple_location_names.b3_tower_fire_1,
            temple_location_names.b3_tower_fire_2,
            temple_location_names.b3_tower_fire_3,
        ]
        tower_loot_chances = [
            (0.05, item_name.vendor_coin),
            (0.20, item_name.stat_upgrade)
        ]
        for loc in tower_locs:
            item = roll_for_item(world, tower_loot_chances)
            if item is None:
                remove_location(loc, item_name.loot_tower)
            else:
                item_counts[item] += 1
        # Dune shark locations
        dune_shark_upgrade_locs = [
            temple_location_names.b1_boss_worm_1_1,
            temple_location_names.b1_boss_worm_2_1,
            temple_location_names.b1_boss_worm_3_1,
            temple_location_names.b1_boss_worm_4_1,
        ]
        for loc in dune_shark_upgrade_locs:
            if world.random.random() >= 0.1:
                location_table.pop(loc)
            else:
                item_counts[item_name.stat_upgrade] += 1
        dune_shark_steak_locs = [
            temple_location_names.b1_boss_worm_1_2,
            temple_location_names.b1_boss_worm_2_2,
            temple_location_names.b1_boss_worm_3_2,
            temple_location_names.b1_boss_worm_4_2,
        ]
        for loc in dune_shark_steak_locs:
            if world.random.random() >= 0.05:
                location_table.pop(loc)
            else:
                item_counts[item_name.steak] += 1
    else:
        item_counts[item_name.vendor_coin] -= item_counts[item_name.miniboss_stat_upgrade]
        item_counts.pop(item_name.miniboss_stat_upgrade)
        # Hack to force the dune sharks key location to always exist
        if world.options.key_mode.value == world.options.key_mode.option_floor_master:
            key_loc_name = temple_location_names.b1_boss_worm_key
            location_table[key_loc_name] = temple_enemy_loot_locations[key_loc_name]
    item_counts.pop(item_name.loot_tower)
    item_counts.pop(item_name.loot_flower)
    item_counts.pop(item_name.loot_mini_flower)

    return location_table, item_counts, random_locations


def remove_location_with_item(location_table, location: str, item: str, item_counts: typing.Dict[str, int]):
    location_table.pop(location)
    item_counts[item] -= 1


def roll_for_item(world, loot_chances: typing.List[typing.Tuple[float, str]]):
    rnd = world.random.random()
    for item in loot_chances:
        rnd -= item[0]
        if rnd < 0:
            return item[1]
    return None


lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in all_locations.items() if
                                            data.code}
