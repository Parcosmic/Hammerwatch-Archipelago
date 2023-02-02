import typing

from BaseClasses import Location, MultiWorld
from .Names import CastleLocationNames, TempleLocationNames, ItemName
from .Options import BonusChestLocationBehavior, Difficulty
from .Util import *
from .Items import castle_item_counts, temple_item_counts, recovery_table, get_item_counts
from enum import Enum


class LocationClassification(Enum):
    Regular = 0
    Recovery = 1
    Secret = 2
    Bonus = 3
    Shop = 4


class LocationData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: LocationClassification = LocationClassification.Regular


class HammerwatchLocation(Location):
    game: str = "Hammerwatch"

    def __init__(self, player: int, name: str = '', code: int = None, parent=None):
        super().__init__(player, name, code, parent)
        self.event = code is None
        self.show_in_spoiler = code is not None


counter = Counter(0x131000)
castle_pickup_locations: typing.Dict[str, LocationData] = {
    CastleLocationNames.p1_p3_n_bridge: LocationData(counter.count(0)),
    CastleLocationNames.p1_bars_2: LocationData(counter.count()),
    CastleLocationNames.p1_entrance_hall_2: LocationData(counter.count(2), LocationClassification.Recovery),
    CastleLocationNames.p1_entrance_hall_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_exit_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_exit_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_nw_bronze_gate: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_m_bronze_gate: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_m_bronze_gate_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_m_bronze_gate_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_m_bronze_gate_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_sw_bronze_gate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_sw_bronze_gate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_e_save_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_e_save_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_entrance_w: LocationData(counter.count()),
    CastleLocationNames.p1_entrance_s: LocationData(counter.count()),
    CastleLocationNames.p1_by_exit_3: LocationData(counter.count()),
    CastleLocationNames.p1_e_bridges_4: LocationData(counter.count()),
    CastleLocationNames.p1_w_of_se_bronze_gate_1: LocationData(counter.count()),
    CastleLocationNames.p1_s_w_bridges_w: LocationData(counter.count()),
    CastleLocationNames.p1_w_of_se_bronze_gate_5: LocationData(counter.count()),
    CastleLocationNames.p1_by_sw_bronze_gate_1: LocationData(counter.count()),
    CastleLocationNames.p1_s_of_e_save_room: LocationData(counter.count()),
    CastleLocationNames.p1_room_by_exit: LocationData(counter.count()),
    CastleLocationNames.p1_ne_arrow_traps: LocationData(counter.count()),
    CastleLocationNames.p1_e_bridges_5: LocationData(counter.count()),
    CastleLocationNames.p1_n_of_se_bridge: LocationData(counter.count()),
    CastleLocationNames.p1_by_sw_bronze_gate_4: LocationData(counter.count()),
    CastleLocationNames.p1_p3_s: LocationData(counter.count()),
    CastleLocationNames.p1_bars_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_entrance_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_entrance_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_entrance_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_entrance_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_w_save: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_e_bridges_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_e_bridges_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_e_bridges_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_m_bronze_gate_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_m_bronze_gate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_by_m_bronze_gate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_center_bridges_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_center_bridges_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_center_bridges_n_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_center_bridges_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_center_bridges_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_center_bridges_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_center_bridges_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_w_of_se_bronze_gate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_w_of_se_bronze_gate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_w_of_se_bronze_gate_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_9: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_10: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_s_lower_hall_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_p2_by_shop: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p1_entrance_secret: LocationData(counter.count()),
    CastleLocationNames.p1_e_secret: LocationData(counter.count()),
    CastleLocationNames.p1_p3_n_across_bridge: LocationData(counter.count()),
    CastleLocationNames.p1_s_secret_2: LocationData(counter.count()),
    CastleLocationNames.p1_hint_room: LocationData(counter.count()),
    CastleLocationNames.p1_se_bridge: LocationData(counter.count()),
    CastleLocationNames.p1_sw_bronze_gate: LocationData(counter.count()),
    CastleLocationNames.p1_s_secret_1: LocationData(counter.count()),

    CastleLocationNames.p2_spike_puzzle_w_1: LocationData(counter.count()),
    CastleLocationNames.p2_big_bridge_3: LocationData(counter.count(2)),
    CastleLocationNames.p2_sequence_puzzle_reward: LocationData(counter.count()),
    CastleLocationNames.p2_spike_puzzle_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_spike_puzzle_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_w_of_silver_gate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_w_of_silver_gate_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_nw_island_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_nw_island_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_by_red_spikes_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_by_red_spikes_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_by_red_spikes_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_entrance_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_big_bridge_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_big_bridge_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_end_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_end_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_save: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_poker_plant_room_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_poker_plant_room_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_s_arrow_traps_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_s_arrow_traps_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_entrance_1: LocationData(counter.count()),
    CastleLocationNames.p2_entrance_2: LocationData(counter.count()),
    CastleLocationNames.p2_entrance_4: LocationData(counter.count()),
    CastleLocationNames.p2_entrance_3: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_4: LocationData(counter.count()),
    CastleLocationNames.p2_w_of_gold_gate: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_5: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_1: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_6: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_2: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_3: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_12: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_13: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_11: LocationData(counter.count()),
    CastleLocationNames.p2_e_of_red_spikes_1: LocationData(counter.count()),
    CastleLocationNames.p2_e_of_red_spikes_2: LocationData(counter.count()),
    CastleLocationNames.p2_e_of_red_spikes_3: LocationData(counter.count()),
    CastleLocationNames.p2_e_of_red_spikes_4: LocationData(counter.count()),
    CastleLocationNames.p2_beetle_boss_room_1: LocationData(counter.count()),
    CastleLocationNames.p2_beetle_boss_room_2: LocationData(counter.count()),
    CastleLocationNames.p2_beetle_boss_room_3: LocationData(counter.count()),
    CastleLocationNames.p2_spike_puzzle_ne_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_spike_puzzle_ne_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_spike_puzzle_ne_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_nw_island_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_nw_island_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_of_ne_save_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_of_ne_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_w_poker_plant_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_w_poker_plant_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_w_poker_plant_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_s_of_w_gold_gate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_s_of_w_gold_gate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_s_of_w_gold_gate_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_poker_plant_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_poker_plant_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_poker_plant_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_gold_gate_room_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_gold_gate_room_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_gold_gate_room_9: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_spike_puzzle_e: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_beetle_boss_room_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_e_gold_gate_room_10: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p2_by_boss_switch: LocationData(counter.count()),
    CastleLocationNames.p2_nw_island_4: LocationData(counter.count()),
    CastleLocationNames.p2_nw_island_3: LocationData(counter.count()),
    CastleLocationNames.p2_nw_island_5: LocationData(counter.count()),
    CastleLocationNames.p2_beetle_boss_hidden_room_1: LocationData(counter.count()),
    CastleLocationNames.p2_toggle_spike_trap_reward_1: LocationData(counter.count()),
    CastleLocationNames.p2_e_poker_plant_room_4: LocationData(counter.count()),
    CastleLocationNames.p2_s_arrow_traps_1: LocationData(counter.count()),
    CastleLocationNames.p2_spike_puzzle_n_2: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_reward_2: LocationData(counter.count()),
    CastleLocationNames.p2_spike_puzzle_n_1: LocationData(counter.count()),
    CastleLocationNames.p2_spike_puzzle_w_2: LocationData(counter.count()),
    CastleLocationNames.p2_beetle_boss_hidden_room_2: LocationData(counter.count()),
    CastleLocationNames.p2_toggle_spike_trap_reward_3: LocationData(counter.count()),
    CastleLocationNames.p2_toggle_spike_trap_reward_2: LocationData(counter.count()),
    CastleLocationNames.p2_e_gold_gate_room_reward_1: LocationData(counter.count()),
    CastleLocationNames.p2_puzzle_1: LocationData(counter.count()),
    CastleLocationNames.p2_puzzle_2: LocationData(counter.count()),
    CastleLocationNames.p2_puzzle_3: LocationData(counter.count()),
    CastleLocationNames.p2_puzzle_4: LocationData(counter.count()),

    CastleLocationNames.p3_bonus_return: LocationData(counter.count()),
    CastleLocationNames.p3_by_w_shop: LocationData(counter.count()),
    CastleLocationNames.p3_red_spike_room: LocationData(counter.count()),
    CastleLocationNames.p3_spike_trap_1: LocationData(counter.count()),
    CastleLocationNames.p3_nw_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_s_bronze_gate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_s_bronze_gate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_s_bronze_gate_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_s_of_poker_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_s_of_poker_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_ne_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_ne_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_ne_of_bridge_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_ne_of_bridge_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_spike_trap_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_spike_trap_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_secret_secret: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_se_cross_hall_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_se_cross_hall_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_w: LocationData(counter.count()),
    CastleLocationNames.p3_entrance_n_1: LocationData(counter.count()),
    CastleLocationNames.p3_entrance_n_of_poker: LocationData(counter.count()),
    CastleLocationNames.p3_entrance_n_2: LocationData(counter.count()),
    CastleLocationNames.p3_entrance_sw: LocationData(counter.count()),
    CastleLocationNames.p3_entrance_m_4: LocationData(counter.count()),
    CastleLocationNames.p3_entrance_s_3: LocationData(counter.count()),
    CastleLocationNames.p3_entrance_s_of_poker_3: LocationData(counter.count()),
    CastleLocationNames.p3_s_of_silver_gate: LocationData(counter.count()),
    CastleLocationNames.p3_arrow_hall_2: LocationData(counter.count()),
    CastleLocationNames.p3_arrow_hall_1: LocationData(counter.count()),
    CastleLocationNames.p3_se_m_2: LocationData(counter.count()),
    CastleLocationNames.p3_se_cross_hall_se: LocationData(counter.count()),
    # CastleLocationNames.p3_skip_boss_switch_2: LocationData(counter.count()),
    CastleLocationNames.p3_w_of_w_poker: LocationData(counter.count(2)),
    CastleLocationNames.p3_nw_of_bridge: LocationData(counter.count()),
    CastleLocationNames.p3_n_of_bridge_5: LocationData(counter.count()),
    CastleLocationNames.p3_s_of_w_poker: LocationData(counter.count()),
    CastleLocationNames.p3_w_of_bridge: LocationData(counter.count()),
    CastleLocationNames.p3_nw_s_bronze_gate_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_n_of_bridge_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_nw_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_nw_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_m_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_m_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_m_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_ne_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_ne_e_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_ne_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_n_bronze_gate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_n_bronze_gate_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_n_bronze_gate_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_entrance_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_e_of_bridge_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_e_of_bridge_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_e_of_bridge_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_se_cross_hall_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_se_cross_hall_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_se_cross_hall_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_se_cross_hall_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_nw_n_bronze_gate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_se_m_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_s_of_boss_door: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.p3_secret_arrow_hall_1: LocationData(counter.count()),
    CastleLocationNames.p3_s_of_e_poker_1: LocationData(counter.count()),
    CastleLocationNames.p3_nw_m: LocationData(counter.count()),
    CastleLocationNames.p3_nw_nw_3: LocationData(counter.count()),
    CastleLocationNames.p3_nw_sw_1: LocationData(counter.count()),
    CastleLocationNames.p3_nw_sw_2: LocationData(counter.count()),
    CastleLocationNames.p3_nw_se: LocationData(counter.count()),
    # CastleLocationNames.p3_skip_boss_switch_6: LocationData(counter.count()),
    # CastleLocationNames.p3_skip_boss_switch_4: LocationData(counter.count()),
    # CastleLocationNames.p3_skip_boss_switch_1: LocationData(counter.count()),
    # CastleLocationNames.p3_skip_boss_switch_3: LocationData(counter.count()),
    # CastleLocationNames.p3_skip_boss_switch_5: LocationData(counter.count()),
    CastleLocationNames.p3_n_of_bridge_4: LocationData(counter.count(6), LocationClassification.Recovery),
    CastleLocationNames.p3_secret_arrow_hall_2: LocationData(counter.count()),
    CastleLocationNames.p3_ne_e_4: LocationData(counter.count()),
    CastleLocationNames.p3_nw_closed_room: LocationData(counter.count()),
    CastleLocationNames.p3_n_of_bridge_2: LocationData(counter.count()),
    CastleLocationNames.p3_se_of_w_shop: LocationData(counter.count()),
    CastleLocationNames.p3_s_of_e_poker_2: LocationData(counter.count()),
    CastleLocationNames.p3_nw_n_bronze_gate_1: LocationData(counter.count()),
    CastleLocationNames.p3_nw_s_bronze_gate_1: LocationData(counter.count()),
    CastleLocationNames.p3_n_of_bridge_1: LocationData(counter.count()),
    CastleLocationNames.p3_sw_of_w_shop: LocationData(counter.count()),
    CastleLocationNames.p3_by_m_shop_1: LocationData(counter.count()),
    CastleLocationNames.p3_by_m_shop_2: LocationData(counter.count()),

    CastleLocationNames.n1_room2_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n1_room2_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n1_room2_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n1_room4_w_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n1_room4_w_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n1_room2_nw_room_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_nw_room_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_nw_room_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_nw_room_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_n_m_room_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_n_m_room_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_n_m_room_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_n_m_room_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_n_m_room_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_n_m_room_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_nw_room_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room2_nw_room_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_15: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_16: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_11: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_10: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_12: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_14: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_13: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_sealed_room_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_sealed_room_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_sealed_room_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_17: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_19: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_20: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room3_w_18: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room4_s_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room4_s_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room4_s_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n1_room1: LocationData(counter.count()),
    CastleLocationNames.n1_room3_sealed_room_1: LocationData(counter.count()),
    CastleLocationNames.n1_room2_small_box: LocationData(counter.count()),
    CastleLocationNames.n1_entrance: LocationData(counter.count()),
    CastleLocationNames.n1_room4_m: LocationData(counter.count()),
    CastleLocationNames.n1_room4_e: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n1_room2_n_secret_room: LocationData(counter.count()),

    CastleLocationNames.b1_reward: LocationData(counter.count()),
    CastleLocationNames.b1_arena_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.b1_arena_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.b1_behind_portal: LocationData(counter.count()),

    CastleLocationNames.a1_m_trellis_secret: LocationData(counter.count()),
    CastleLocationNames.a1_se_cache_3: LocationData(counter.count()),
    CastleLocationNames.a1_nw_left_1: LocationData(counter.count(3), LocationClassification.Recovery),
    CastleLocationNames.a1_nw_right_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_save_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_ne_top_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_ne_top_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_sw_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_sw_n_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_sw_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_cache_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_cache_9: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_red_spikes_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_e_m_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_e_m_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_e_m_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_red_spikes_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_nw_right_4: LocationData(counter.count()),
    CastleLocationNames.a1_nw_right_3: LocationData(counter.count()),
    CastleLocationNames.a1_n_boss_hall: LocationData(counter.count(2)),
    CastleLocationNames.a1_m_ice_tower_1: LocationData(counter.count()),
    CastleLocationNames.a1_e_n_fireball_trap: LocationData(counter.count()),
    CastleLocationNames.a1_e_ne: LocationData(counter.count()),
    CastleLocationNames.a1_ne_3: LocationData(counter.count()),
    CastleLocationNames.a1_e_e_fireball_trap: LocationData(counter.count()),
    CastleLocationNames.a1_e_e: LocationData(counter.count()),
    CastleLocationNames.a1_e_se: LocationData(counter.count()),
    CastleLocationNames.a1_s_save_1: LocationData(counter.count()),
    CastleLocationNames.a1_n_tp: LocationData(counter.count()),
    CastleLocationNames.a1_nw_bgate: LocationData(counter.count()),
    CastleLocationNames.a1_n_cache_1: LocationData(counter.count()),
    CastleLocationNames.a1_from_a2_1: LocationData(counter.count()),
    CastleLocationNames.a1_from_a2_3: LocationData(counter.count()),
    CastleLocationNames.a1_red_spikes_2: LocationData(counter.count()),
    CastleLocationNames.a1_se_cache_4: LocationData(counter.count()),
    CastleLocationNames.a1_se_cache_2: LocationData(counter.count()),
    CastleLocationNames.a1_n_cache_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_cache_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_nw_left_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_nw_left_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_nw_left_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_save_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_save_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_ne_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_ne_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_sw_w_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_sw_w_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_m_ice_tower_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_m_ice_tower_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_m_ice_tower_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_nw_right_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_n_cache_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_e_ne_bgate: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_w_save_1: LocationData(counter.count()),
    CastleLocationNames.a1_ne_top_room_3: LocationData(counter.count()),
    CastleLocationNames.a1_s_save_2: LocationData(counter.count()),
    CastleLocationNames.a1_n_cache_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a1_from_a2_2: LocationData(counter.count()),
    CastleLocationNames.a1_nw_left_5: LocationData(counter.count()),
    CastleLocationNames.a1_w_save_2: LocationData(counter.count()),
    CastleLocationNames.a1_ne_ice_tower_secret: LocationData(counter.count()),
    CastleLocationNames.a1_sw_spikes: LocationData(counter.count()),
    CastleLocationNames.a1_se_cache_1: LocationData(counter.count()),
    CastleLocationNames.a1_n_cache_3: LocationData(counter.count()),
    CastleLocationNames.a1_n_cache_2: LocationData(counter.count()),
    CastleLocationNames.a1_puzzle_1: LocationData(counter.count()),
    CastleLocationNames.a1_puzzle_2: LocationData(counter.count()),
    CastleLocationNames.a1_puzzle_3: LocationData(counter.count()),
    CastleLocationNames.a1_puzzle_4: LocationData(counter.count()),

    CastleLocationNames.a2_bonus_return: LocationData(counter.count()),
    CastleLocationNames.a2_blue_spikes: LocationData(counter.count()),
    CastleLocationNames.a2_ne_l_bgate: LocationData(counter.count(3)),
    CastleLocationNames.a2_pyramid_3: LocationData(counter.count()),
    CastleLocationNames.a2_s_of_n_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_of_n_save_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_nw_ice_tower_across_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_n_of_s_save_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_n_of_s_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_n_of_s_save_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_save_room_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_save_room_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_of_ne_fire_traps_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_fire_trap_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_fire_trap_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_ice_tower_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_of_n_save_1: LocationData(counter.count()),
    CastleLocationNames.a2_ne_ice_tower_9: LocationData(counter.count()),
    CastleLocationNames.a2_ne_ice_tower_4: LocationData(counter.count()),
    CastleLocationNames.a2_e_save_room_1: LocationData(counter.count()),
    CastleLocationNames.a2_n_of_s_save_4: LocationData(counter.count()),
    CastleLocationNames.a2_s_of_ne_fire_traps_1: LocationData(counter.count()),
    CastleLocationNames.a2_e_ice_tower_1: LocationData(counter.count()),
    CastleLocationNames.a2_sw_ice_tower: LocationData(counter.count()),
    CastleLocationNames.a2_s_ice_tower_4: LocationData(counter.count()),
    CastleLocationNames.a2_s_ice_tower_5: LocationData(counter.count()),
    CastleLocationNames.a2_pyramid_4: LocationData(counter.count(2)),
    CastleLocationNames.a2_nw_tp: LocationData(counter.count(2)),
    CastleLocationNames.a2_s_of_e_bgate: LocationData(counter.count()),
    CastleLocationNames.a2_s_bgate: LocationData(counter.count()),
    CastleLocationNames.a2_e_ice_tower_4: LocationData(counter.count()),
    CastleLocationNames.a2_e_ice_tower_5: LocationData(counter.count()),
    CastleLocationNames.a2_nw_ice_tower_across_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_nw_ice_tower_across_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_nw_ice_tower_across_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_ice_tower_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_ice_tower_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_ice_tower_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_ice_tower_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_n_of_ne_fire_traps_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_n_of_ne_fire_traps_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_save_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_save_room_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_save_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_se_of_e_ice_tower_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_se_of_e_ice_tower_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_se_of_e_ice_tower_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_ice_tower_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_ice_tower_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_s_ice_tower_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_of_s_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_of_s_save_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_of_s_save_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_e_of_s_save_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_ice_tower_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_r_bgate_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_r_bgate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_by_w_a1_stair: LocationData(counter.count()),
    CastleLocationNames.a2_e_ice_tower_2: LocationData(counter.count()),
    CastleLocationNames.a2_se_tp: LocationData(counter.count(2)),
    CastleLocationNames.a2_pyramid_1: LocationData(counter.count(2)),
    CastleLocationNames.a2_ne_ice_tower_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a2_ne_tp: LocationData(counter.count(4)),
    CastleLocationNames.a2_nw_ice_tower: LocationData(counter.count()),
    CastleLocationNames.a2_ne_ice_tower_2: LocationData(counter.count()),
    CastleLocationNames.a2_e_bgate: LocationData(counter.count()),
    CastleLocationNames.a2_e_ice_tower_6: LocationData(counter.count(2)),
    CastleLocationNames.a2_sw_ice_tower_tp: LocationData(counter.count()),
    CastleLocationNames.a2_puzzle_1: LocationData(counter.count()),
    CastleLocationNames.a2_puzzle_2: LocationData(counter.count()),
    CastleLocationNames.a2_puzzle_3: LocationData(counter.count()),
    CastleLocationNames.a2_puzzle_4: LocationData(counter.count()),

    CastleLocationNames.n2_m_m_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n2_m_m_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n2_nw_top_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_top_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_12: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_13: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_14: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_10: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_15: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_11: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_w_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_bottom_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_bottom_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_bottom_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_nw_bottom_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_12: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_13: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_14: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_12: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_13: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_14: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_10: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_15: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_n_11: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_11: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_10: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_e_15: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_ne_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_ne_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_ne_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_start_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_start_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_start_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_s_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_m_se_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_m_se_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_m_se_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n2_m_n: LocationData(counter.count()),
    CastleLocationNames.n2_m_m_3: LocationData(counter.count()),
    CastleLocationNames.n2_ne_4: LocationData(counter.count()),
    CastleLocationNames.n2_m_e: LocationData(counter.count()),
    CastleLocationNames.n2_start_1: LocationData(counter.count()),
    CastleLocationNames.n2_m_se_5: LocationData(counter.count()),
    CastleLocationNames.n2_m_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n2_w_1: LocationData(counter.count()),

    CastleLocationNames.a3_s_banner_secret: LocationData(counter.count(2)),
    CastleLocationNames.a3_nw_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_nw_save_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_knife_puzzle_reward_l_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_knife_puzzle_reward_l_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_ne_ice_towers_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_ne_ice_towers_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_ne_ice_towers_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_e_ice_towers_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_e_ice_towers_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_sw_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_15: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_11: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_14: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_nw_save_1: LocationData(counter.count()),
    CastleLocationNames.a3_s_of_knife_puzzle: LocationData(counter.count()),
    CastleLocationNames.a3_fireball_hall_2: LocationData(counter.count()),
    CastleLocationNames.a3_pyramids_s_5: LocationData(counter.count()),
    CastleLocationNames.a3_pyramids_s_4: LocationData(counter.count()),
    CastleLocationNames.a3_e_ice_towers_3: LocationData(counter.count()),
    CastleLocationNames.a3_spike_floor_1: LocationData(counter.count()),
    CastleLocationNames.a3_knife_puzzle_reward_l_5: LocationData(counter.count(2)),
    CastleLocationNames.a3_knife_puzzle_reward_r: LocationData(counter.count()),
    CastleLocationNames.a3_secret_shop: LocationData(counter.count()),
    CastleLocationNames.a3_spike_floor_7: LocationData(counter.count()),
    CastleLocationNames.a3_spike_floor_4: LocationData(counter.count()),
    CastleLocationNames.a3_spike_floor_9: LocationData(counter.count()),
    CastleLocationNames.a3_spike_floor_13: LocationData(counter.count()),
    CastleLocationNames.a3_s_of_n_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_n_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_ne_ice_towers_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_ne_ice_towers_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_ne_ice_towers_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_n_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_n_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_s_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_s_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_sw_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_sw_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_se_boss_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_se_boss_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_se_boss_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_s_of_n_save_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_pyramids_e: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_12: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.a3_spike_floor_2: LocationData(counter.count()),
    CastleLocationNames.a3_pyramid: LocationData(counter.count(2)),
    CastleLocationNames.a3_fireball_hall_1: LocationData(counter.count()),
    CastleLocationNames.a3_e_of_spike_floor: LocationData(counter.count(3)),
    CastleLocationNames.a3_spike_floor_10: LocationData(counter.count()),
    CastleLocationNames.a3_m_tp: LocationData(counter.count()),
    CastleLocationNames.a3_pyramids_s_bgate_tp: LocationData(counter.count()),
    CastleLocationNames.a3_knife_puzzle_reward_l_2: LocationData(counter.count()),
    CastleLocationNames.a3_knife_puzzle_reward_l_3: LocationData(counter.count()),

    CastleLocationNames.b2_boss_reward: LocationData(counter.count()),

    CastleLocationNames.r1_e_fire_floor_1: LocationData(counter.count(3), LocationClassification.Recovery),
    CastleLocationNames.r1_e_fire_floor_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_nw_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_nw_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_nw_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ne_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ne_9: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ne_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ne_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_knife_trap_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_knife_trap_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_knife_trap_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_se_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_se_wall: LocationData(counter.count()),
    CastleLocationNames.r1_e_knife_trap_1: LocationData(counter.count()),
    CastleLocationNames.r1_e_w_1: LocationData(counter.count()),
    CastleLocationNames.r1_e_s: LocationData(counter.count()),
    CastleLocationNames.r1_e_e: LocationData(counter.count()),
    CastleLocationNames.r1_w_knife_trap_1: LocationData(counter.count()),
    CastleLocationNames.r1_w_knife_trap_5: LocationData(counter.count()),
    CastleLocationNames.r1_nw_1: LocationData(counter.count()),
    CastleLocationNames.r1_sw_ne_1: LocationData(counter.count()),
    CastleLocationNames.r1_e_w_2: LocationData(counter.count()),
    CastleLocationNames.r1_se_6: LocationData(counter.count()),
    CastleLocationNames.r1_e_n_1: LocationData(counter.count()),
    CastleLocationNames.r1_nw_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_ne_ggate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_ne_ggate_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_ne_ggate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_ne_ggate_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ne_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ne_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ne_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_knife_trap_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_knife_trap_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_knife_trap_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_w_knife_trap_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_w_knife_trap_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_w_knife_trap_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ggate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_sw_ggate_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_se_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_se_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_nw_hidden_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_e_s_bgate: LocationData(counter.count()),
    CastleLocationNames.r1_w_knife_trap_6: LocationData(counter.count()),
    CastleLocationNames.r1_w_knife_trap_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r1_start_wall: LocationData(counter.count()),
    CastleLocationNames.r1_nw_hidden_1: LocationData(counter.count()),
    CastleLocationNames.r1_e_n_3: LocationData(counter.count()),
    CastleLocationNames.r1_e_fire_floor_3: LocationData(counter.count()),
    CastleLocationNames.r1_sw_ne_2: LocationData(counter.count()),
    CastleLocationNames.r1_e_sgate: LocationData(counter.count()),
    CastleLocationNames.r1_puzzle_1: LocationData(counter.count()),
    CastleLocationNames.r1_puzzle_2: LocationData(counter.count()),
    CastleLocationNames.r1_puzzle_3: LocationData(counter.count()),
    CastleLocationNames.r1_puzzle_4: LocationData(counter.count()),

    CastleLocationNames.r2_ne_knife_trap_wall_3: LocationData(counter.count()),
    CastleLocationNames.r2_n_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_bronze_gates_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_bronze_gates_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_start_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_start_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_hall_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_hall_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_by_sgate_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_by_sgate_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_by_sgate_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_ne_knife_trap_wall_2: LocationData(counter.count()),
    CastleLocationNames.r2_m_spike_trap_2: LocationData(counter.count()),
    CastleLocationNames.r2_s_knife_trap_4: LocationData(counter.count()),
    CastleLocationNames.r2_s_knife_trap_5: LocationData(counter.count()),
    CastleLocationNames.r2_n_bronze_gates_4: LocationData(counter.count()),
    CastleLocationNames.r2_w_boss_3: LocationData(counter.count()),
    CastleLocationNames.r2_n_bronze_gates_1: LocationData(counter.count()),
    CastleLocationNames.r2_start: LocationData(counter.count()),
    CastleLocationNames.r2_m_e_of_spike_trap_3: LocationData(counter.count()),
    CastleLocationNames.r2_by_sgate_1: LocationData(counter.count()),
    CastleLocationNames.r2_m_spike_trap_10: LocationData(counter.count()),
    CastleLocationNames.r2_s_knife_trap_2: LocationData(counter.count()),
    CastleLocationNames.r2_w_island: LocationData(counter.count()),
    CastleLocationNames.r2_nw_spike_trap_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_nw_spike_trap_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_closed_room: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_w_boss_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_by_sgate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_hall_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_hall_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_spike_trap_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_e_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_w_boss_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_w_boss_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_w_boss_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_w_boss_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_e_of_spike_trap_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_e_of_spike_trap_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_e_of_spike_trap_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_8: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_9: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_10: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_11: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_sw_12: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_by_sgate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_by_sgate_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_by_sgate_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_spike_trap_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_spike_trap_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_spike_trap_9: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_spike_trap_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_se_save: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_ne_knife_trap_wall_1: LocationData(counter.count()),
    CastleLocationNames.r2_m_spike_trap_4: LocationData(counter.count()),
    CastleLocationNames.r2_w_boss_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_m_spike_trap_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r2_s_knife_trap_3: LocationData(counter.count()),
    CastleLocationNames.r2_ne_knife_trap_end: LocationData(counter.count()),
    CastleLocationNames.r2_n_1: LocationData(counter.count()),
    CastleLocationNames.r2_w_boss_2: LocationData(counter.count()),
    CastleLocationNames.r2_e_5: LocationData(counter.count()),
    CastleLocationNames.r2_sw_1: LocationData(counter.count()),
    CastleLocationNames.r2_m_spike_trap_1: LocationData(counter.count()),
    CastleLocationNames.r2_s_knife_trap_1: LocationData(counter.count()),
    CastleLocationNames.r2_puzzle_1: LocationData(counter.count()),
    CastleLocationNames.r2_puzzle_2: LocationData(counter.count()),
    CastleLocationNames.r2_puzzle_3: LocationData(counter.count()),
    CastleLocationNames.r2_puzzle_4: LocationData(counter.count()),

    CastleLocationNames.r3_e_secret_tp: LocationData(counter.count(2)),
    CastleLocationNames.r3_e_shops_puzzle_reward: LocationData(counter.count()),
    CastleLocationNames.r3_e_ggate_hallway_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_ggate_hallway_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_ne_knife_trap_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_ne_knife_trap_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_fire_floor_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_fire_floor_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_sw_bgate_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_sw_bgate_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_sw_bgate_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_s_shops_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_s_shops_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_boss_switch_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_bonus_return_1: LocationData(counter.count()),
    CastleLocationNames.r3_bonus_return_2: LocationData(counter.count()),
    CastleLocationNames.r3_w_passage_behind_spikes: LocationData(counter.count()),
    CastleLocationNames.r3_w_passage_s_closed_room: LocationData(counter.count()),
    CastleLocationNames.r3_n_bgate_e: LocationData(counter.count()),
    CastleLocationNames.r3_w_fire_floor_1: LocationData(counter.count()),
    CastleLocationNames.r3_start: LocationData(counter.count()),
    CastleLocationNames.r3_e_miniboss: LocationData(counter.count()),
    CastleLocationNames.r3_e_fire_floor_w: LocationData(counter.count()),
    CastleLocationNames.r3_boss_switch_room_1: LocationData(counter.count()),
    CastleLocationNames.r3_nw_save_2: LocationData(counter.count()),
    CastleLocationNames.r3_e_tp: LocationData(counter.count(2)),
    CastleLocationNames.r3_ne_save_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_ne_save_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_start_nw_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_sw_bgate_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_sw_bgate_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_boss_switch_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_n_miniboss_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_n_miniboss_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_n_miniboss_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_shops_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_shops_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_start_nw_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_start_nw_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_fire_floor_n_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_fire_floor_n_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_fire_floor_n_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_shops_room_e_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_shops_room_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_shops_room_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_ggate_hallway_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_s_of_boss_door_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_w_fire_floor_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_e_fire_floor_e: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_w_ggate_w: LocationData(counter.count()),
    CastleLocationNames.r3_s_save: LocationData(counter.count()),
    CastleLocationNames.r3_nw_save_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.r3_n_miniboss_1: LocationData(counter.count()),
    CastleLocationNames.r3_e_shops_3: LocationData(counter.count(2)),
    CastleLocationNames.r3_s_of_boss_door_1: LocationData(counter.count()),
    CastleLocationNames.r3_e_fire_floor_secret: LocationData(counter.count()),
    CastleLocationNames.r3_shops_room_secret: LocationData(counter.count()),
    CastleLocationNames.r3_nw_tp: LocationData(counter.count()),
    CastleLocationNames.r3_sw_hidden_room_1: LocationData(counter.count()),
    CastleLocationNames.r3_sw_hidden_room_2: LocationData(counter.count()),
    CastleLocationNames.r3_s_shops_room_left_shop: LocationData(counter.count()),

    CastleLocationNames.n3_tp_room: LocationData(counter.count()),
    CastleLocationNames.n3_tp_room_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n3_tp_room_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n3_exit_e_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_e_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_nw_cluster_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_s_cluster_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_se_cluster_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_tp_room_e_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_tp_room_e_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_tp_room_e_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_tp_room_e_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_m_cluster_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_se_cluster_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n3_exit_sw: LocationData(counter.count()),
    CastleLocationNames.n3_m_cluster_5: LocationData(counter.count()),
    CastleLocationNames.n3_se_cluster_5: LocationData(counter.count()),
    CastleLocationNames.n3_exit_s: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.n3_exit_se: LocationData(counter.count()),

    CastleLocationNames.b3_reward: LocationData(counter.count()),

    CastleLocationNames.c1_n_spikes_1: LocationData(counter.count()),
    CastleLocationNames.c1_ledge_1: LocationData(counter.count()),
    CastleLocationNames.c1_prison_stairs: LocationData(counter.count()),
    CastleLocationNames.c1_n_alcove_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c1_n_alcove_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c1_s_ice_towers_4: LocationData(counter.count()),
    CastleLocationNames.c1_s_ice_towers_6: LocationData(counter.count()),
    CastleLocationNames.c1_n_ice_tower_3: LocationData(counter.count()),
    CastleLocationNames.c1_n_ice_tower_1: LocationData(counter.count()),
    CastleLocationNames.c1_n_alcove_1: LocationData(counter.count()),
    CastleLocationNames.c1_ne: LocationData(counter.count()),
    CastleLocationNames.c1_w_1: LocationData(counter.count()),
    CastleLocationNames.c1_w_2: LocationData(counter.count()),
    CastleLocationNames.c1_w_3: LocationData(counter.count()),
    CastleLocationNames.c1_s_ice_towers_1: LocationData(counter.count()),
    CastleLocationNames.c1_s_ice_towers_2: LocationData(counter.count()),
    CastleLocationNames.c1_start: LocationData(counter.count()),
    CastleLocationNames.c1_s_ice_towers_3: LocationData(counter.count()),
    CastleLocationNames.c1_s_ice_towers_5: LocationData(counter.count()),
    CastleLocationNames.c1_se_spikes: LocationData(counter.count()),
    CastleLocationNames.c1_n_ice_tower_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c1_m_knife_traps: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c1_n_alcove_4: LocationData(counter.count()),
    CastleLocationNames.c1_ne_knife_traps_1: LocationData(counter.count()),
    CastleLocationNames.c1_tp_island_2: LocationData(counter.count()),
    CastleLocationNames.c1_n_spikes_2: LocationData(counter.count()),
    CastleLocationNames.c1_ne_knife_traps_2: LocationData(counter.count()),
    CastleLocationNames.c1_tp_island_1: LocationData(counter.count()),
    CastleLocationNames.c1_ledge_2: LocationData(counter.count()),
    CastleLocationNames.c1_sgate: LocationData(counter.count()),

    CastleLocationNames.pstart_puzzle_1: LocationData(counter.count()),
    CastleLocationNames.pstart_puzzle_2: LocationData(counter.count()),
    CastleLocationNames.pstart_puzzle_3: LocationData(counter.count()),
    CastleLocationNames.pstart_puzzle_4: LocationData(counter.count()),

    CastleLocationNames.c2_bonus_return: LocationData(counter.count()),
    CastleLocationNames.c2_ne_platform_5: LocationData(counter.count(2)),
    CastleLocationNames.c2_by_w_shops_2: LocationData(counter.count()),
    CastleLocationNames.c2_e_fire_floor_1: LocationData(counter.count()),
    CastleLocationNames.c2_w_spikes_2: LocationData(counter.count()),
    CastleLocationNames.c2_w_spikes_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_spikes_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_sw_ice_tower_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_sw_ice_tower_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_spikes_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_spikes_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_save: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_alcove_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_alcove_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_by_w_shops_3_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_by_w_shops_3_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_by_e_shops_2_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_by_e_shops_2_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_e_fire_floor_w_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_e_fire_floor_w_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_knife_traps_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_knife_traps_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_start_s_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_start_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_start_s_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_alcove_4: LocationData(counter.count()),
    CastleLocationNames.c2_w_alcove_3: LocationData(counter.count()),
    CastleLocationNames.c2_w_spikes_s_3: LocationData(counter.count()),
    CastleLocationNames.c2_w_spikes_e_3: LocationData(counter.count()),
    CastleLocationNames.c2_ne_platform_n_1: LocationData(counter.count()),
    CastleLocationNames.c2_ne_5: LocationData(counter.count()),
    CastleLocationNames.c2_ne_platform_4: LocationData(counter.count()),
    CastleLocationNames.c2_by_tp_island_1: LocationData(counter.count()),
    CastleLocationNames.c2_w_spikes_s_7: LocationData(counter.count()),
    CastleLocationNames.c2_w_save_wall: LocationData(counter.count()),
    CastleLocationNames.c2_w_knife_traps_2: LocationData(counter.count()),
    CastleLocationNames.c2_by_e_shops_2: LocationData(counter.count()),
    CastleLocationNames.c2_w_knife_traps_4: LocationData(counter.count()),
    CastleLocationNames.c2_s_1: LocationData(counter.count()),
    CastleLocationNames.c2_s_6: LocationData(counter.count()),
    CastleLocationNames.c2_start_s_1: LocationData(counter.count()),
    CastleLocationNames.c2_se_flame_turrets_1: LocationData(counter.count()),
    CastleLocationNames.c2_se_flame_turrets_4: LocationData(counter.count()),
    CastleLocationNames.c2_nw_ledge_4: LocationData(counter.count(2)),
    CastleLocationNames.c2_exit: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_platform_n_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_platform_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_by_tp_island_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_knife_traps_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_s_7: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_se_flame_turrets_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_sw_ice_tower_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_sw_ice_tower_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_sw_ice_tower_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_spikes_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_spikes_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_spikes_s_6: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_platform_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_platform_n_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_e_fire_floor_w_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_e_fire_floor_w_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_e_fire_floor_w_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_start_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_start_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_start_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_ne_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_by_tp_island_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_by_w_shops_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_boss_portal: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_knife_traps_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_se_flame_turrets_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_se_flame_turrets_5: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_e_fire_floor_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_w_spikes_1: LocationData(counter.count(3)),
    CastleLocationNames.c2_w_spikes_4: LocationData(counter.count()),
    CastleLocationNames.c2_ne_platform_1: LocationData(counter.count()),
    CastleLocationNames.c2_w_spikes_e_4: LocationData(counter.count()),
    CastleLocationNames.c2_nw_ledge_1: LocationData(counter.count()),
    CastleLocationNames.c2_nw_ledge_2: LocationData(counter.count()),
    CastleLocationNames.c2_nw_ledge_5: LocationData(counter.count()),
    CastleLocationNames.c2_nw_ledge_6: LocationData(counter.count()),
    CastleLocationNames.c2_nw_ledge_3: LocationData(counter.count()),
    CastleLocationNames.c2_nw_ledge_7: LocationData(counter.count()),
    CastleLocationNames.c2_ne_platform_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c2_n_wall: LocationData(counter.count()),
    CastleLocationNames.c2_sw_ice_tower_6: LocationData(counter.count(2)),
    CastleLocationNames.c2_ne_platform_2: LocationData(counter.count()),
    CastleLocationNames.c2_s_4: LocationData(counter.count()),
    CastleLocationNames.c2_w_spikes_3: LocationData(counter.count()),
    CastleLocationNames.c2_nw_knife_traps_1: LocationData(counter.count()),
    CastleLocationNames.c2_nw_knife_traps_2: LocationData(counter.count()),
    CastleLocationNames.c2_nw_knife_traps_4: LocationData(counter.count()),
    CastleLocationNames.c2_nw_knife_traps_5: LocationData(counter.count()),
    CastleLocationNames.c2_nw_knife_traps_3: LocationData(counter.count()),
    CastleLocationNames.c2_puzzle_1: LocationData(counter.count()),
    CastleLocationNames.c2_puzzle_2: LocationData(counter.count()),
    CastleLocationNames.c2_puzzle_3: LocationData(counter.count()),
    CastleLocationNames.c2_puzzle_4: LocationData(counter.count()),

    CastleLocationNames.n4_e_11: LocationData(counter.count()),
    CastleLocationNames.n4_w_7: LocationData(counter.count()),
    CastleLocationNames.n4_nw_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_10: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_11: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_14: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_15: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_16: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_13: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_nw_12: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_24: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_16: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_7: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_6: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_14: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_15: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_22: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_20: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_19: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_18: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_17: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_10: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_12: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_13: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_5: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_4: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_3: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_2: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_1: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_8: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_10: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_11: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_12: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_13: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_14: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_w_9: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_25: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_26: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_27: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_28: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_29: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_30: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_31: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_e_32: LocationData(counter.count(), LocationClassification.Bonus),
    CastleLocationNames.n4_ne: LocationData(counter.count()),
    CastleLocationNames.n4_by_w_room_1: LocationData(counter.count()),
    CastleLocationNames.n4_by_exit: LocationData(counter.count()),
    CastleLocationNames.n4_by_w_room_2: LocationData(counter.count()),
    CastleLocationNames.n4_e_23: LocationData(counter.count()),
    CastleLocationNames.n4_e_21: LocationData(counter.count()),

    CastleLocationNames.c3_nw_ice_towers_3: LocationData(counter.count()),
    CastleLocationNames.c3_c2_tp: LocationData(counter.count()),
    CastleLocationNames.c3_light_bridge_2: LocationData(counter.count()),
    CastleLocationNames.c3_fire_floor_3: LocationData(counter.count()),
    CastleLocationNames.c3_nw_ice_towers_w: LocationData(counter.count()),
    CastleLocationNames.c3_start_e: LocationData(counter.count()),
    CastleLocationNames.c3_w_ledge_2: LocationData(counter.count()),
    CastleLocationNames.c3_w_ledge_1: LocationData(counter.count()),
    CastleLocationNames.c3_m_wall: LocationData(counter.count()),
    CastleLocationNames.c3_m_ice_towers_1: LocationData(counter.count()),
    CastleLocationNames.c3_m_ice_towers_4: LocationData(counter.count()),
    CastleLocationNames.c3_se_save_1: LocationData(counter.count()),
    CastleLocationNames.c3_e_miniboss: LocationData(counter.count()),
    CastleLocationNames.c3_se_save_2: LocationData(counter.count()),
    CastleLocationNames.c3_sw_save_1: LocationData(counter.count()),
    CastleLocationNames.c3_sw_save_2: LocationData(counter.count()),
    CastleLocationNames.c3_sw_save_3: LocationData(counter.count()),
    CastleLocationNames.c3_fire_floor_w: LocationData(counter.count()),
    CastleLocationNames.c3_s_bgate: LocationData(counter.count()),
    CastleLocationNames.c3_ne_npc_2: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c3_ne_npc_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c3_ne_npc_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c3_fire_floor_1: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c3_easter_egg: LocationData(counter.count()),
    CastleLocationNames.c3_fire_floor_2: LocationData(counter.count()),
    CastleLocationNames.c3_n_spike_floor_1: LocationData(counter.count()),
    CastleLocationNames.c3_boss_switch: LocationData(counter.count()),
    CastleLocationNames.c3_light_bridge_1: LocationData(counter.count()),
    CastleLocationNames.c3_light_bridge_3: LocationData(counter.count()),
    CastleLocationNames.c3_m_ice_towers_3: LocationData(counter.count()),
    CastleLocationNames.c3_sw_hidden: LocationData(counter.count()),
    CastleLocationNames.c3_se_save_3: LocationData(counter.count(), LocationClassification.Recovery),
    CastleLocationNames.c3_nw_ice_towers_2: LocationData(counter.count()),
    CastleLocationNames.c3_nw_ice_towers_1: LocationData(counter.count()),
    CastleLocationNames.c3_n_spike_floor_2: LocationData(counter.count()),
    CastleLocationNames.c3_m_ice_towers_2: LocationData(counter.count(2)),
    CastleLocationNames.c3_m_tp: LocationData(counter.count(2)),
    CastleLocationNames.c3_fire_floor_tp: LocationData(counter.count()),

    CastleLocationNames.b4_e_2: LocationData(counter.count()),
    CastleLocationNames.b4_w_10: LocationData(counter.count()),
    CastleLocationNames.b4_w_2: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_6: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_2: LocationData(counter.count()),
    CastleLocationNames.b4_w_11: LocationData(counter.count()),
    CastleLocationNames.b4_w_1: LocationData(counter.count()),
    CastleLocationNames.b4_w_3: LocationData(counter.count()),
    CastleLocationNames.b4_e_3: LocationData(counter.count()),
    CastleLocationNames.b4_e_4: LocationData(counter.count()),
    CastleLocationNames.b4_e_1: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_9: LocationData(counter.count()),
    CastleLocationNames.b4_plank_1: LocationData(counter.count()),
    CastleLocationNames.b4_plank_2: LocationData(counter.count()),
    CastleLocationNames.b4_plank_3: LocationData(counter.count()),
    CastleLocationNames.b4_plank_4: LocationData(counter.count()),
    CastleLocationNames.b4_plank_5: LocationData(counter.count()),
    CastleLocationNames.b4_plank_6: LocationData(counter.count()),
    CastleLocationNames.b4_plank_7: LocationData(counter.count()),
    CastleLocationNames.b4_plank_8: LocationData(counter.count()),
    CastleLocationNames.b4_plank_9: LocationData(counter.count()),
    CastleLocationNames.b4_plank_10: LocationData(counter.count()),
    CastleLocationNames.b4_plank_11: LocationData(counter.count()),
    CastleLocationNames.b4_w_9: LocationData(counter.count()),
    CastleLocationNames.b4_w_6: LocationData(counter.count()),
    CastleLocationNames.b4_w_4: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_4: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_7: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_11: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_12: LocationData(counter.count()),
    CastleLocationNames.b4_e_8: LocationData(counter.count()),
    CastleLocationNames.b4_w_12: LocationData(counter.count()),
    CastleLocationNames.b4_e_7: LocationData(counter.count()),
    CastleLocationNames.b4_w_5: LocationData(counter.count()),
    CastleLocationNames.b4_w_7: LocationData(counter.count()),
    CastleLocationNames.b4_w_8: LocationData(counter.count()),
    CastleLocationNames.b4_e_6: LocationData(counter.count()),
    CastleLocationNames.b4_e_5: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_10: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_5: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_3: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_8: LocationData(counter.count()),
    CastleLocationNames.b4_dragon_1: LocationData(counter.count()),

    CastleLocationNames.e2_entrance: LocationData(counter.count(4), LocationClassification.Recovery),
    CastleLocationNames.e2_end: LocationData(counter.count(), LocationClassification.Recovery),

    CastleLocationNames.e3_entrance_1: LocationData(counter.count(3), LocationClassification.Recovery),
    CastleLocationNames.e3_entrance_2: LocationData(counter.count(), LocationClassification.Recovery),

    CastleLocationNames.e4_main: LocationData(counter.count(15), LocationClassification.Recovery),
}

castle_shop_locations: typing.Dict[str, LocationData] = {

}

castle_event_locations: typing.Dict[str, LocationData] = {
    CastleLocationNames.ev_p2_gold_gate_room_ne_switch: LocationData(None),
    CastleLocationNames.ev_p2_gold_gate_room_nw_switch: LocationData(None),
    CastleLocationNames.ev_p2_gold_gate_room_se_switch: LocationData(None),
    CastleLocationNames.ev_p2_gold_gate_room_sw_switch: LocationData(None),
    CastleLocationNames.ev_p1_boss_switch: LocationData(None),
    CastleLocationNames.ev_p2_boss_switch: LocationData(None),
    CastleLocationNames.ev_p3_boss_switch: LocationData(None),
    # CastleLocationNames.ev_p3_boss_switch_skip: LocationData(None),
    CastleLocationNames.ev_a1_boss_switch: LocationData(None),
    CastleLocationNames.ev_a2_boss_switch: LocationData(None),
    CastleLocationNames.ev_a3_boss_switch: LocationData(None),
    CastleLocationNames.ev_r1_boss_switch: LocationData(None),
    CastleLocationNames.ev_r2_boss_switch: LocationData(None),
    CastleLocationNames.ev_r3_boss_switch: LocationData(None),
    CastleLocationNames.ev_c2_n_shops_switch: LocationData(None),
    CastleLocationNames.ev_c2_n_tp_button: LocationData(None),
    CastleLocationNames.ev_c1_boss_switch: LocationData(None),
    CastleLocationNames.ev_c2_boss_switch: LocationData(None),
    CastleLocationNames.ev_c3_boss_switch: LocationData(None),
    CastleLocationNames.ev_c3_rspikes_switch: LocationData(None),
    CastleLocationNames.ev_c3_sw_hidden_switch_1: LocationData(None),
    CastleLocationNames.ev_c3_sw_hidden_switch_2: LocationData(None),
    CastleLocationNames.ev_c3_sw_hidden_switch_3: LocationData(None),
    CastleLocationNames.ev_c3_sw_hidden_switch_4: LocationData(None),
    CastleLocationNames.ev_c3_sw_hidden_switch_5: LocationData(None),
    CastleLocationNames.ev_c3_sw_hidden_switch_6: LocationData(None),
}

castle_locations: typing.Dict[str, LocationData] = {
    **castle_pickup_locations,
    **castle_event_locations
}

counter = Counter(0x130000)
temple_pickup_locations: typing.Dict[str, LocationData] = {
    TempleLocationNames.hub_field_nw: LocationData(counter.count(0)),
    TempleLocationNames.hub_on_rock: LocationData(counter.count()),
    TempleLocationNames.hub_pof_reward: LocationData(counter.count()),
    TempleLocationNames.hub_west_pyramid: LocationData(counter.count()),
    TempleLocationNames.hub_rocks_south: LocationData(counter.count()),
    TempleLocationNames.hub_field_north: LocationData(counter.count()),
    TempleLocationNames.hub_behind_temple_entrance: LocationData(counter.count()),
    TempleLocationNames.hub_behind_shops: LocationData(counter.count()),
    TempleLocationNames.hub_front_of_pof: LocationData(counter.count()),
    TempleLocationNames.hub_field_south: LocationData(counter.count()),

    TempleLocationNames.cave3_portal_r: LocationData(counter.count()),
    TempleLocationNames.cave3_n: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave3_outside_guard: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave3_portal_l: LocationData(counter.count()),
    TempleLocationNames.cave3_nw: LocationData(counter.count()),
    TempleLocationNames.cave3_m: LocationData(counter.count()),
    TempleLocationNames.cave3_se: LocationData(counter.count()),
    TempleLocationNames.cave3_fall_se: LocationData(counter.count()),
    TempleLocationNames.cave3_ne: LocationData(counter.count()),
    TempleLocationNames.cave3_captain: LocationData(counter.count()),
    TempleLocationNames.cave3_fall_sw: LocationData(counter.count()),
    TempleLocationNames.cave3_squire: LocationData(counter.count()),
    TempleLocationNames.cave3_captain_dock: LocationData(counter.count()),
    TempleLocationNames.cave3_fall_ne: LocationData(counter.count()),
    TempleLocationNames.cave3_fields_r: LocationData(counter.count()),
    TempleLocationNames.cave3_trapped_guard: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_n: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave3_secret_nw: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave3_secret_s: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave3_secret_6: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_7: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_8: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_5: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_2: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_3: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_4: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_1: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_9: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_10: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_11: LocationData(counter.count()),
    TempleLocationNames.cave3_secret_12: LocationData(counter.count()),
    TempleLocationNames.cave3_fall_nw: LocationData(counter.count()),
    TempleLocationNames.cave3_half_bridge: LocationData(counter.count()),
    TempleLocationNames.cave3_guard: LocationData(counter.count()),
    TempleLocationNames.c3_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.c3_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.c3_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.c3_puzzle_4: LocationData(counter.count()),

    TempleLocationNames.cave2_sw_hidden_room_3: LocationData(counter.count()),
    TempleLocationNames.cave2_pumps_wall_r: LocationData(counter.count()),
    TempleLocationNames.cave2_below_pumps_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_below_pumps_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_double_bridge_l_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_double_bridge_l_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_nw_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_nw_5: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_pumps_wall_l: LocationData(counter.count()),
    TempleLocationNames.cave2_water_n_r_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_water_s: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_nw_2: LocationData(counter.count()),
    TempleLocationNames.cave2_red_bridge_4: LocationData(counter.count()),
    TempleLocationNames.cave2_double_bridge_r: LocationData(counter.count()),
    TempleLocationNames.cave2_w_miniboss_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_w_miniboss_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_w_miniboss_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_red_bridge_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_red_bridge_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_e_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_e_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_guard_n: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave2_red_bridge_2: LocationData(counter.count()),
    TempleLocationNames.cave2_double_bridge_m: LocationData(counter.count()),
    TempleLocationNames.cave2_water_n_r_1: LocationData(counter.count()),
    TempleLocationNames.cave2_green_bridge: LocationData(counter.count()),
    TempleLocationNames.cave2_sw_hidden_room_1: LocationData(counter.count()),
    TempleLocationNames.cave2_guard_s: LocationData(counter.count()),
    TempleLocationNames.cave2_nw_3: LocationData(counter.count()),
    TempleLocationNames.cave2_w_miniboss_4: LocationData(counter.count()),
    TempleLocationNames.cave2_red_bridge_3: LocationData(counter.count()),
    TempleLocationNames.cave2_below_pumps_3: LocationData(counter.count()),
    TempleLocationNames.cave2_secret_ne: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave2_secret_w: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave2_secret_m: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave2_water_n_l: LocationData(counter.count()),
    TempleLocationNames.cave2_nw_1: LocationData(counter.count()),
    TempleLocationNames.cave2_sw: LocationData(counter.count()),
    TempleLocationNames.cave2_double_bridge_secret: LocationData(counter.count()),
    TempleLocationNames.cave2_sw_hidden_room_2: LocationData(counter.count()),
    TempleLocationNames.cave2_pumps_n: LocationData(counter.count()),
    TempleLocationNames.cave2_guard: LocationData(counter.count()),
    TempleLocationNames.cave2_red_bridge_1: LocationData(counter.count()),
    TempleLocationNames.cave2_sw_hidden_room_4: LocationData(counter.count()),
    TempleLocationNames.c2_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.c2_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.c2_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.c2_puzzle_4: LocationData(counter.count()),

    TempleLocationNames.cave1_secret_tunnel_1: LocationData(counter.count()),
    TempleLocationNames.cave1_temple_end_3: LocationData(counter.count()),
    TempleLocationNames.cave1_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_w_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_w_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_ne_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_ne_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_temple_hall_2: LocationData(counter.count()),
    TempleLocationNames.cave1_water_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_water_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_water_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_water_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_water_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_n_bridges_4: LocationData(counter.count()),
    TempleLocationNames.cave1_double_room_l: LocationData(counter.count()),
    TempleLocationNames.cave1_e_3: LocationData(counter.count()),
    TempleLocationNames.cave1_green_bridge_2: LocationData(counter.count()),
    TempleLocationNames.cave1_n_bridges_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_secret_tunnel_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_n_room_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_n_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_n_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_n_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_ne_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_ne_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_ne_5: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_w_by_water_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_double_room_r: LocationData(counter.count()),
    TempleLocationNames.cave1_krilith_ledge_n: LocationData(counter.count()),
    TempleLocationNames.cave1_red_bridge_e: LocationData(counter.count()),
    TempleLocationNames.cave1_ne_hidden_room_3: LocationData(counter.count()),
    TempleLocationNames.cave1_water_s_shore: LocationData(counter.count()),
    TempleLocationNames.cave1_temple_end_2: LocationData(counter.count()),
    TempleLocationNames.cave1_krilith_door: LocationData(counter.count()),
    TempleLocationNames.cave1_temple_end_4: LocationData(counter.count()),
    TempleLocationNames.cave1_ne_grubs: LocationData(counter.count()),
    TempleLocationNames.cave1_w_by_water_2: LocationData(counter.count()),
    TempleLocationNames.cave1_m: LocationData(counter.count()),
    TempleLocationNames.cave1_secret_nw: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave1_secret_n_hidden_room: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave1_secret_ne: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave1_secret_w: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave1_secret_m: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave1_secret_e: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.cave1_temple_hall_1: LocationData(counter.count()),
    TempleLocationNames.cave1_temple_hall_3: LocationData(counter.count()),
    TempleLocationNames.cave1_n_bridges_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_temple_end_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_secret_tunnel_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.cave1_n_3: LocationData(counter.count()),
    TempleLocationNames.cave1_ne_hidden_room_4: LocationData(counter.count()),
    TempleLocationNames.cave1_n_bridges_1: LocationData(counter.count()),
    TempleLocationNames.cave1_krilith_ledge_e: LocationData(counter.count()),
    TempleLocationNames.cave1_green_bridge_1: LocationData(counter.count()),
    TempleLocationNames.cave1_e_2: LocationData(counter.count()),
    TempleLocationNames.cave1_s_3: LocationData(counter.count()),
    TempleLocationNames.cave1_ne_hidden_room_5: LocationData(counter.count()),
    TempleLocationNames.cave1_ne_hidden_room_1: LocationData(counter.count()),
    TempleLocationNames.cave1_ne_hidden_room_2: LocationData(counter.count()),
    TempleLocationNames.cave1_n_bridges_5: LocationData(counter.count()),
    TempleLocationNames.c1_n_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.c1_n_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.c1_n_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.c1_n_puzzle_4: LocationData(counter.count()),
    TempleLocationNames.c1_e_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.c1_e_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.c1_e_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.c1_e_puzzle_4: LocationData(counter.count()),

    TempleLocationNames.boss1_bridge: LocationData(counter.count()),
    TempleLocationNames.boss1_guard_r_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.boss1_guard_r_2: LocationData(counter.count(), LocationClassification.Recovery),
    # TempleLocationNames.boss1_drop_2: LocationData(counter.count()),
    # TempleLocationNames.boss1_drop: LocationData(counter.count()),
    TempleLocationNames.boss1_guard_l: LocationData(counter.count(3), LocationClassification.Recovery),
    TempleLocationNames.boss1_bridge_n: LocationData(counter.count()),
    TempleLocationNames.boss1_secret: LocationData(counter.count(), LocationClassification.Secret),

    TempleLocationNames.p_mid4_2: LocationData(counter.count()),
    TempleLocationNames.p_end3_1: LocationData(counter.count()),
    TempleLocationNames.p_mid4_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.p_mid4_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.p_mid2_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.p_mid2_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.p_mid2_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.p_mid2_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.p_mid4_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.p_mid5_2: LocationData(counter.count()),
    TempleLocationNames.p_end3_2: LocationData(counter.count()),
    TempleLocationNames.p_ent2_secret: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.p_mid3_secret_1: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.p_mid3_secret_2: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.p_mid3_secret_3: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.p_mid3_secret_4: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.p_end1_secret: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.p_mid5_secret: LocationData(counter.count(), LocationClassification.Secret),
    TempleLocationNames.p_mid1_2: LocationData(counter.count()),
    TempleLocationNames.p_mid1_1: LocationData(counter.count()),
    TempleLocationNames.p_mid5_1: LocationData(counter.count()),
    TempleLocationNames.p_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.p_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.p_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.p_puzzle_4: LocationData(counter.count()),

    TempleLocationNames.temple_entrance_l: LocationData(counter.count()),
    TempleLocationNames.temple_entrance_r: LocationData(counter.count()),

    TempleLocationNames.t1_double_gate_behind_block: LocationData(counter.count()),
    TempleLocationNames.t1_sw_hidden_room_3: LocationData(counter.count()),
    TempleLocationNames.t1_telarian_ice: LocationData(counter.count()),
    TempleLocationNames.t1_sun_turret_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_telarian_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_boulder_hallway_by_ice_turret_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_boulder_hallway_by_ice_turret_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_boulder_hallway_by_ice_turret_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_telarian_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_node_2_passage_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_node_2_passage_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_fire_trap_by_sun_turret_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_fire_trap_by_sun_turret_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_e_of_double_gate_room_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_e_of_double_gate_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_sw_sun_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_sw_sun_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_ice_block_chamber_ice: LocationData(counter.count()),
    TempleLocationNames.t1_sun_turret_2: LocationData(counter.count()),
    TempleLocationNames.t1_n_cache_by_ice_turret_5: LocationData(counter.count()),
    TempleLocationNames.t1_s_cache_by_ice_turret_3: LocationData(counter.count()),
    TempleLocationNames.t1_sw_cache_2: LocationData(counter.count()),
    TempleLocationNames.t1_sw_hidden_room_4: LocationData(counter.count()),
    TempleLocationNames.t1_sun_turret_3: LocationData(counter.count()),
    TempleLocationNames.t1_s_bridge_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_s_bridge_5: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_s_bridge_6: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_n_cache_by_ice_turret_1: LocationData(counter.count()),
    TempleLocationNames.t1_n_sunbeam_treasure_2: LocationData(counter.count()),
    TempleLocationNames.t1_s_cache_by_ice_turret_2: LocationData(counter.count()),
    TempleLocationNames.t1_sw_cache_1: LocationData(counter.count()),
    TempleLocationNames.t1_sw_cache_4: LocationData(counter.count()),
    TempleLocationNames.t1_sw_cache_5: LocationData(counter.count()),
    TempleLocationNames.t1_ledge_after_block_trap_2: LocationData(counter.count()),
    TempleLocationNames.t1_ice_block_chamber_3: LocationData(counter.count()),
    TempleLocationNames.t1_ice_block_chamber_2: LocationData(counter.count()),
    TempleLocationNames.t1_double_gate_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_ice_block_chamber_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_sun_block_hall_3: LocationData(counter.count()),
    TempleLocationNames.t1_fire_trap_by_sun_turret_4: LocationData(counter.count()),
    TempleLocationNames.t1_behind_bars_entrance: LocationData(counter.count()),
    TempleLocationNames.t1_mana_drain_fire_trap: LocationData(counter.count()),
    TempleLocationNames.t1_e_gold_beetles: LocationData(counter.count()),
    TempleLocationNames.t1_sun_block_hall_1: LocationData(counter.count()),
    TempleLocationNames.t1_sw_hidden_room_2: LocationData(counter.count()),
    TempleLocationNames.t1_mana_drain_fire_trap_reward_2: LocationData(counter.count()),
    TempleLocationNames.t1_mana_drain_fire_trap_reward_1: LocationData(counter.count()),
    TempleLocationNames.t1_sun_block_hall_4: LocationData(counter.count()),
    TempleLocationNames.t1_fire_trap_by_sun_turret_3: LocationData(counter.count()),
    TempleLocationNames.t1_ledge_after_block_trap_1: LocationData(counter.count()),
    TempleLocationNames.t1_sw_cache_3: LocationData(counter.count()),
    TempleLocationNames.t1_n_sunbeam_treasure_3: LocationData(counter.count()),
    TempleLocationNames.t1_boulder_hallway_by_ice_turret_4: LocationData(counter.count()),
    TempleLocationNames.t1_ice_turret_1: LocationData(counter.count()),
    TempleLocationNames.t1_ice_turret_2: LocationData(counter.count()),
    TempleLocationNames.t1_above_s_bridge: LocationData(counter.count()),
    TempleLocationNames.t1_e_of_double_gate_room_2: LocationData(counter.count()),
    TempleLocationNames.t1_sw_corner_room: LocationData(counter.count()),
    TempleLocationNames.t1_s_bridge_1: LocationData(counter.count()),
    TempleLocationNames.t1_sun_block_hall_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_mana_drain_fire_trap_passage: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t1_n_sunbeam: LocationData(counter.count()),
    TempleLocationNames.t1_n_cache_by_ice_turret_4: LocationData(counter.count()),
    TempleLocationNames.t1_node_2_passage_2: LocationData(counter.count()),
    TempleLocationNames.t1_double_gate_hidden: LocationData(counter.count()),
    TempleLocationNames.t1_ice_turret_boulder_break_block: LocationData(counter.count()),
    TempleLocationNames.t1_e_of_double_gate_room_1: LocationData(counter.count()),
    TempleLocationNames.t1_sw_hidden_room_1: LocationData(counter.count()),
    TempleLocationNames.t1_n_cache_by_ice_turret_2: LocationData(counter.count()),
    TempleLocationNames.t1_n_cache_by_ice_turret_3: LocationData(counter.count()),
    TempleLocationNames.t1_n_sunbeam_treasure_1: LocationData(counter.count()),
    TempleLocationNames.t1_telarian_4: LocationData(counter.count()),
    TempleLocationNames.t1_telarian_1: LocationData(counter.count()),
    TempleLocationNames.t1_node_2_1: LocationData(counter.count()),
    TempleLocationNames.t1_node_2_2: LocationData(counter.count()),
    TempleLocationNames.t1_s_of_sun_turret: LocationData(counter.count()),
    TempleLocationNames.t1_double_gate_2: LocationData(counter.count()),
    TempleLocationNames.t1_double_gate_3: LocationData(counter.count()),
    TempleLocationNames.t1_s_cache_by_ice_turret_1: LocationData(counter.count()),
    TempleLocationNames.t1_s_bridge_2: LocationData(counter.count()),
    TempleLocationNames.t1_s_bridge_3: LocationData(counter.count()),
    TempleLocationNames.t1_telarian_5: LocationData(counter.count()),
    TempleLocationNames.t1_w_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.t1_w_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.t1_w_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.t1_w_puzzle_4: LocationData(counter.count()),
    TempleLocationNames.t1_e_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.t1_e_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.t1_e_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.t1_e_puzzle_4: LocationData(counter.count()),

    TempleLocationNames.boss2_nw: LocationData(counter.count()),
    TempleLocationNames.boss2_se: LocationData(counter.count()),

    TempleLocationNames.t2_nw_puzzle_cache_5: LocationData(counter.count()),
    TempleLocationNames.t2_floor3_cache_3: LocationData(counter.count()),
    TempleLocationNames.t2_fire_trap_maze_2: LocationData(counter.count()),
    TempleLocationNames.t2_sw_gate: LocationData(counter.count()),
    TempleLocationNames.t2_se_light_bridge_2: LocationData(counter.count()),
    TempleLocationNames.t2_boulder_room_block: LocationData(counter.count()),
    TempleLocationNames.t2_nw_ice_turret_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_nw_ice_turret_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_nw_ice_turret_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_w_hall_dead_end_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_w_hall_dead_end_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_w_hall_dead_end_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_e_outside_gold_beetle_cage_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_e_outside_gold_beetle_cage_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_s_node_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_s_node_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_s_node_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_se_banner_chamber_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_se_banner_chamber_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_nw_puzzle_cache_1: LocationData(counter.count()),
    TempleLocationNames.t2_nw_puzzle_cache_2: LocationData(counter.count()),
    TempleLocationNames.t2_nw_gate_2: LocationData(counter.count()),
    TempleLocationNames.t2_floor3_cache_1: LocationData(counter.count()),
    TempleLocationNames.t2_floor3_cache_2: LocationData(counter.count()),
    TempleLocationNames.t2_jones_hallway: LocationData(counter.count()),
    TempleLocationNames.t2_boulder_room_2: LocationData(counter.count()),
    TempleLocationNames.t2_sw_jail_2: LocationData(counter.count()),
    TempleLocationNames.t2_right_of_pof_switch: LocationData(counter.count()),
    TempleLocationNames.t2_w_gold_beetle_room_4: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_nw_gate_3: LocationData(counter.count()),
    TempleLocationNames.t2_nw_under_block: LocationData(counter.count()),
    TempleLocationNames.t2_floor3_cache_6: LocationData(counter.count()),
    TempleLocationNames.t2_w_spike_trap_2: LocationData(counter.count()),
    TempleLocationNames.t2_w_hall_dead_end_4: LocationData(counter.count()),
    TempleLocationNames.t2_fire_trap_maze_3: LocationData(counter.count()),
    TempleLocationNames.t2_boulder_chamber_2: LocationData(counter.count()),
    TempleLocationNames.t2_se_banner_chamber_2: LocationData(counter.count()),
    TempleLocationNames.t2_w_spike_trap_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_boulder_chamber_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_fire_trap_maze_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_s_sunbeam_2: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_nw_gate_1: LocationData(counter.count()),
    TempleLocationNames.t2_w_gold_beetle_room_2: LocationData(counter.count()),
    TempleLocationNames.t2_w_ice_block_gate: LocationData(counter.count()),
    TempleLocationNames.t2_e_ice_block_gate: LocationData(counter.count()),
    TempleLocationNames.t2_nw_puzzle_cache_4: LocationData(counter.count()),
    TempleLocationNames.t2_mana_drain_fire_trap_2: LocationData(counter.count()),
    TempleLocationNames.t2_floor3_cache_4: LocationData(counter.count()),
    TempleLocationNames.t2_portal_gate: LocationData(counter.count()),
    TempleLocationNames.t2_fire_trap_maze_4: LocationData(counter.count()),
    TempleLocationNames.t2_gold_beetle_barricade: LocationData(counter.count()),
    TempleLocationNames.t2_se_light_bridge_1: LocationData(counter.count()),
    TempleLocationNames.t2_teleporter: LocationData(counter.count()),
    TempleLocationNames.t2_mana_drain_fire_trap_1: LocationData(counter.count()),
    TempleLocationNames.t2_floor3_cache_gate: LocationData(counter.count()),
    TempleLocationNames.t2_w_gold_beetle_room_1: LocationData(counter.count()),
    TempleLocationNames.t2_s_light_bridge_1: LocationData(counter.count()),
    TempleLocationNames.t2_nw_ice_turret_4: LocationData(counter.count()),
    TempleLocationNames.t2_s_of_portal: LocationData(counter.count()),
    TempleLocationNames.t2_n_of_sw_gate_2: LocationData(counter.count()),
    TempleLocationNames.t2_boulder_chamber_3: LocationData(counter.count()),
    TempleLocationNames.t2_left_of_pof_switch_2: LocationData(counter.count()),
    TempleLocationNames.t2_s_balcony_2: LocationData(counter.count()),
    TempleLocationNames.t2_se_banner_chamber_5: LocationData(counter.count()),
    TempleLocationNames.t2_n_of_portal: LocationData(counter.count()),
    TempleLocationNames.t2_nw_of_s_ice_turret: LocationData(counter.count()),
    TempleLocationNames.t2_w_hall_dead_end_5: LocationData(counter.count()),
    TempleLocationNames.t2_fire_trap_maze_5: LocationData(counter.count()),
    TempleLocationNames.t2_fire_trap_maze_6: LocationData(counter.count()),
    TempleLocationNames.t2_boulder_chamber_4: LocationData(counter.count()),
    TempleLocationNames.t2_s_balcony_1: LocationData(counter.count()),
    TempleLocationNames.t2_se_banner_chamber_4: LocationData(counter.count()),
    TempleLocationNames.t2_se_fireball_hall: LocationData(counter.count()),
    TempleLocationNames.t2_boulder_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_w_gold_beetle_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    TempleLocationNames.t2_nw_puzzle_cache_3: LocationData(counter.count()),
    TempleLocationNames.t2_floor3_cache_5: LocationData(counter.count()),
    TempleLocationNames.t2_n_of_sw_gate_1: LocationData(counter.count()),
    TempleLocationNames.t2_left_of_pof_switch_1: LocationData(counter.count()),
    TempleLocationNames.t2_s_light_bridge_2: LocationData(counter.count()),
    TempleLocationNames.t2_s_sunbeam_1: LocationData(counter.count()),
    TempleLocationNames.t2_sw_jail_1: LocationData(counter.count()),
    TempleLocationNames.t2_n_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.t2_n_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.t2_n_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.t2_n_puzzle_4: LocationData(counter.count()),
    TempleLocationNames.t2_nw_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.t2_nw_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.t2_nw_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.t2_nw_puzzle_4: LocationData(counter.count()),
    TempleLocationNames.t2_e_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.t2_e_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.t2_e_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.t2_e_puzzle_4: LocationData(counter.count()),
    TempleLocationNames.t2_sw_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.t2_sw_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.t2_sw_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.t2_sw_puzzle_4: LocationData(counter.count()),

    TempleLocationNames.t3_boss_fall_3_2: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_1: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_2: LocationData(counter.count()),
    TempleLocationNames.t3_s_node_cache_2: LocationData(counter.count()),
    TempleLocationNames.t3_n_turret_1: LocationData(counter.count()),
    TempleLocationNames.t3_boulder_block: LocationData(counter.count()),
    TempleLocationNames.t3_e_turret_spikes: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_3: LocationData(counter.count()),
    TempleLocationNames.t3_s_balcony_turret_2: LocationData(counter.count()),
    TempleLocationNames.t3_s_node_cache_1: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_2_2: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_3_4: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_1_3: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_3_1: LocationData(counter.count()),
    TempleLocationNames.t3_n_turret_2: LocationData(counter.count()),
    TempleLocationNames.t3_m_balcony_corridor: LocationData(counter.count()),
    TempleLocationNames.t3_s_node_cache_3: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_3_3: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_2_3: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_1_2: LocationData(counter.count()),
    TempleLocationNames.t3_s_gate: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_blocks_1: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_blocks_2: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_blocks_3: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_blocks_4: LocationData(counter.count()),
    TempleLocationNames.t3_n_node_blocks_5: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_2_1: LocationData(counter.count()),
    TempleLocationNames.t3_boss_fall_1_1: LocationData(counter.count()),
    TempleLocationNames.t3_s_balcony_turret_1: LocationData(counter.count()),
    TempleLocationNames.t3_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.t3_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.t3_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.t3_puzzle_4: LocationData(counter.count()),

    TempleLocationNames.pof_2_ne_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ne_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ne_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ne_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ent_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ent_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ent_6: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ent_5: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ent_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_ent_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_confuse_hall_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_confuse_hall_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_confuse_hall_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_confuse_hall_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_sw_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_sw_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_sw_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_2_sw_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_6: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_7: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_8: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_9: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_confuse_corner_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_confuse_corner_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_confuse_corner_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_confuse_corner_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_end_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_end_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_end_5: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_end_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_10: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_6: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_9: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_7: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_8: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_5: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_13: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_11: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_s_12: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_c_hall_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_c_hall_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_c_hall_5: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_c_hall_6: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_ent_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_ent_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_ent_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_ent_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_c_hall_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_c_hall_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_6: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_5: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_9: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_8: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_10: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_11: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_sw_left_7: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_3_end_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_3_end_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_3_safety_room_2: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_3_safety_room_1: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_3_end_5: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_3_end_4: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_3_safety_room_3: LocationData(counter.count(), LocationClassification.Bonus),
    TempleLocationNames.pof_1_n_5: LocationData(counter.count()),
    TempleLocationNames.pof_1_ent_5: LocationData(counter.count()),
    TempleLocationNames.pof_1_end_1: LocationData(counter.count()),
    TempleLocationNames.pof_3_end_3: LocationData(counter.count()),
    TempleLocationNames.pof_puzzle_1: LocationData(counter.count()),
    TempleLocationNames.pof_puzzle_2: LocationData(counter.count()),
    TempleLocationNames.pof_puzzle_3: LocationData(counter.count()),
    TempleLocationNames.pof_puzzle_4: LocationData(counter.count()),
}

temple_shop_locations: typing.Dict[str, LocationData] = {

}

temple_event_locations: typing.Dict[str, LocationData] = {
    TempleLocationNames.ev_temple_entrance_rock: LocationData(None),
    TempleLocationNames.ev_hub_pof_switch: LocationData(None),
    TempleLocationNames.ev_cave3_pof_switch: LocationData(None),
    TempleLocationNames.ev_cave2_pof_switch: LocationData(None),
    TempleLocationNames.ev_cave1_pof_switch: LocationData(None),
    TempleLocationNames.ev_temple1_pof_switch: LocationData(None),
    TempleLocationNames.ev_temple2_pof_switch: LocationData(None),
    TempleLocationNames.ev_t2_n_bridge_switch: LocationData(None),
    TempleLocationNames.ev_t2_ne_bridge_switch: LocationData(None),
    TempleLocationNames.ev_t2_se_bridge_switch: LocationData(None),
    TempleLocationNames.ev_t2_w_bridge_switch: LocationData(None),
    TempleLocationNames.ev_t2_sw_bridge_switch: LocationData(None),
    TempleLocationNames.ev_t1_n_node: LocationData(None),
    TempleLocationNames.ev_t1_s_node: LocationData(None),
    TempleLocationNames.ev_t2_n_node: LocationData(None),
    TempleLocationNames.ev_t2_s_node: LocationData(None),
    TempleLocationNames.ev_t3_n_node: LocationData(None),
    TempleLocationNames.ev_t3_s_node: LocationData(None),
    TempleLocationNames.ev_pof_1_unlock_exit: LocationData(None),
    TempleLocationNames.ev_pof_2_unlock_exit: LocationData(None),
    TempleLocationNames.ev_pof_end: LocationData(None),
    TempleLocationNames.ev_krilith_defeated: LocationData(None),
}

temple_locations: typing.Dict[str, LocationData] = {
    **temple_pickup_locations
}

common_event_locations: typing.Dict[str, LocationData] = {
    TempleLocationNames.ev_victory: LocationData(None),
}

all_locations: typing.Dict[str, LocationData] = {
    **castle_locations,
    **castle_shop_locations,
    # **castle_event_locations,
    **temple_locations,
    **temple_shop_locations,
    # **temple_event_locations,
    # **common_event_locations
}


def setup_locations(multiworld: MultiWorld, map: Campaign, player: int):
    location_table: typing.Dict[str, LocationData]
    map_locations: typing.Dict[str, LocationData]
    bonus_locations: typing.Dict[str, LocationData] = {}

    location_table = {}
    # Event locations
    if map == Campaign.Castle:
        map_locations = get_castle_locations(multiworld, player, castle_locations)
        location_table.update(castle_event_locations)
    else:  # Need a default case for this else tests will complain
        map_locations = get_temple_locations(multiworld, player, temple_locations)
        location_table.update(temple_event_locations)

    # Add bonus locations if the setting is on, and add bonus locations to a special list for handling below
    for name, data in map_locations.items():
        if data.classification == LocationClassification.Bonus:
            bonus_locations.update({name: data})
            continue
        if data.classification != LocationClassification.Recovery or multiworld.randomize_recovery_items[player]:
            location_table.update({name: data})

    # Random location behavior
    # if multiworld.random_location_behavior[player] == 0:  # Vanilla
    #     if map == Campaign.Castle:  # Castle Hammerwatch
    #         location_table = choose_castle_random_locations(multiworld, player, location_table)
    #     elif map == Campaign.Temple:
    #         location_table = choose_tots_random_locations(multiworld, player, location_table)
    # elif multiworld.random_location_behavior[player] == 1:  # Shuffle, not implemented yet
    #     pass  # Randomly remove some locations, need to determine the number
    # elif multiworld.random_location_behavior[player] == 2:  # All checks
    #     pass  # Do nothing as all locations are already added to the dict

    if map == Campaign.Castle:  # Castle Hammerwatch
        location_table = choose_castle_random_locations(multiworld, player, location_table)
    elif map == Campaign.Temple:
        location_table = choose_tots_random_locations(multiworld, player, location_table)

    item_counts, extra_items = get_item_counts(multiworld, map, player)

    # Bonus level handling
    if multiworld.bonus_behavior[player] == BonusChestLocationBehavior.option_necessary:  # Necessary
        for i in range(extra_items):
            loc = multiworld.random.choice(list(bonus_locations.keys()))
            location_table.update({loc: bonus_locations.pop(loc)})
    elif multiworld.bonus_behavior[player] == BonusChestLocationBehavior.option_all:  # All
        location_table.update(bonus_locations)

    location_table.update(common_event_locations)

    return location_table, item_counts


random_locations: typing.Dict[str, int] = {
}


def get_castle_locations(multiworld, player: int, location_table: typing.Dict[str, LocationData]):
    if get_goal_type(multiworld, player) == GoalType.KillFinalBoss:
        remove_castle_location(location_table, CastleLocationNames.b4_plank_1, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_2, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_3, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_4, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_5, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_6, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_7, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_8, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_9, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_10, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.b4_plank_11, ItemName.diamond_red)
        remove_castle_location(location_table, CastleLocationNames.e2_entrance, ItemName.apple)
        remove_castle_location(location_table, CastleLocationNames.e2_end, ItemName.apple)
        remove_castle_location(location_table, CastleLocationNames.e3_entrance_1, ItemName.apple)
        remove_castle_location(location_table, CastleLocationNames.e3_entrance_2, ItemName.apple)
        remove_castle_location(location_table, CastleLocationNames.e4_main, ItemName.apple)

    return location_table


def get_temple_locations(multiworld, player: int, location_table: typing.Dict[str, LocationData]):
    if get_goal_type(multiworld, player) == GoalType.AltCompletion:
        remove_temple_location(location_table, TempleLocationNames.hub_pof_reward, ItemName.ankh)

    return location_table


def choose_castle_random_locations(multiworld, player: int, location_table: typing.Dict[str, LocationData]):

    def remove_location(location: str, item: str):
        location_table.pop(location)
        castle_item_counts[item] -= 1

    def remove_puzzle_locations(base_name: str, rloc_name: str):
        if random_locations[rloc_name] < 18:
            remove_location(f"{base_name}4", ItemName.chest_purple)
        if random_locations[rloc_name] < 14:
            remove_location(f"{base_name}3", ItemName.stat_upgrade)
        if random_locations[rloc_name] < 10:
            remove_location(f"{base_name}2", ItemName.ankh)
        if random_locations[rloc_name] < 1:
            remove_location(f"{base_name}1", ItemName.potion_rejuvenation)

    # Set puzzle random values
    if multiworld.randomize_puzzles[player]:
        randomize_puzzle(multiworld, CastleLocationNames.crloc_p2_puzzle)
        randomize_puzzle(multiworld, CastleLocationNames.crloc_a1_puzzle)
        randomize_puzzle(multiworld, CastleLocationNames.crloc_a2_puzzle)
        randomize_puzzle(multiworld, CastleLocationNames.crloc_r1_puzzle)
        randomize_puzzle(multiworld, CastleLocationNames.crloc_r2_puzzle)
        randomize_puzzle(multiworld, CastleLocationNames.crloc_ps_puzzle)
        randomize_puzzle(multiworld, CastleLocationNames.crloc_c2_puzzle)
    else:
        random_locations[CastleLocationNames.crloc_p2_puzzle] = -1
        random_locations[CastleLocationNames.crloc_a1_puzzle] = -1
        random_locations[CastleLocationNames.crloc_a2_puzzle] = -1
        random_locations[CastleLocationNames.crloc_r1_puzzle] = -1
        random_locations[CastleLocationNames.crloc_r2_puzzle] = -1
        random_locations[CastleLocationNames.crloc_ps_puzzle] = -1
        random_locations[CastleLocationNames.crloc_c2_puzzle] = -1

    # Prison Floor 1 Locations
    p1_bkey_1_locs: typing.List[str] = [
        CastleLocationNames.p1_entrance_s,
        CastleLocationNames.p1_entrance_w,
    ]
    location_table = keep_one_location(multiworld, location_table, p1_bkey_1_locs, CastleLocationNames.crloc_p1_bronze_key_entrance)
    p1_bkey_2_locs: typing.List[str] = [
        CastleLocationNames.p1_by_sw_bronze_gate_1,
        CastleLocationNames.p1_s_w_bridges_w,
        CastleLocationNames.p1_by_sw_bronze_gate_4,
    ]
    location_table = keep_one_location(multiworld, location_table, p1_bkey_2_locs, CastleLocationNames.crloc_p1_bronze_key_sw)
    p1_bkey_3_locs: typing.List[str] = [
        CastleLocationNames.p1_n_of_se_bridge,
        CastleLocationNames.p1_s_of_e_save_room,
        CastleLocationNames.p1_w_of_se_bronze_gate_5,
        CastleLocationNames.p1_w_of_se_bronze_gate_1,
    ]
    location_table = keep_one_location(multiworld, location_table, p1_bkey_3_locs, CastleLocationNames.crloc_p1_bronze_key_se)
    p1_bkey_4_locs: typing.List[str] = [
        CastleLocationNames.p1_e_bridges_5,
        CastleLocationNames.p1_e_bridges_4,
        CastleLocationNames.p1_ne_arrow_traps,
    ]
    location_table = keep_one_location(multiworld, location_table, p1_bkey_4_locs, CastleLocationNames.crloc_p1_bronze_key_e)
    p1_bkey_5_locs: typing.List[str] = [
        CastleLocationNames.p1_room_by_exit,
        CastleLocationNames.p1_by_exit_3,
    ]
    location_table = keep_one_location(multiworld, location_table, p1_bkey_5_locs, CastleLocationNames.crloc_p1_bronze_key_n)
    # Prison Floor 2
    p2_bkey_1_locs: typing.List[str] = [
        CastleLocationNames.p2_entrance_1,
        CastleLocationNames.p2_entrance_2,
        CastleLocationNames.p2_entrance_4,
        CastleLocationNames.p2_entrance_3,
        CastleLocationNames.p2_w_of_gold_gate,
    ]
    location_table = keep_one_location(multiworld, location_table, p2_bkey_1_locs, CastleLocationNames.crloc_p2_bkey_1)
    p2_bkey_2_locs: typing.List[str] = [
        CastleLocationNames.p2_e_gold_gate_room_3,
        CastleLocationNames.p2_e_gold_gate_room_2,
        CastleLocationNames.p2_e_gold_gate_room_1,
    ]
    location_table = keep_one_location(multiworld, location_table, p2_bkey_2_locs, CastleLocationNames.crloc_p2_bkey_2)
    p2_bkey_3_locs: typing.List[str] = [
        CastleLocationNames.p2_e_gold_gate_room_4,
        CastleLocationNames.p2_e_gold_gate_room_5,
        CastleLocationNames.p2_e_gold_gate_room_6,
    ]
    location_table = keep_one_location(multiworld, location_table, p2_bkey_3_locs, CastleLocationNames.crloc_p2_bkey_3)
    p2_bkey_4_locs: typing.List[str] = [
        CastleLocationNames.p2_e_gold_gate_room_13,
        CastleLocationNames.p2_e_gold_gate_room_12,
        CastleLocationNames.p2_e_gold_gate_room_11,
    ]
    location_table = keep_one_location(multiworld, location_table, p2_bkey_4_locs, CastleLocationNames.crloc_p2_bkey_4)
    p2_skey_locs: typing.List[str] = [
        CastleLocationNames.p2_nw_island_5,
        CastleLocationNames.p2_nw_island_3,
        CastleLocationNames.p2_nw_island_4,
    ]
    location_table = keep_one_location(multiworld, location_table, p2_skey_locs, CastleLocationNames.crloc_p2_skey)
    p2_gkey_1_locs: typing.List[str] = [
        CastleLocationNames.p2_e_of_red_spikes_2,
        CastleLocationNames.p2_e_of_red_spikes_3,
        CastleLocationNames.p2_e_of_red_spikes_4,
        CastleLocationNames.p2_e_of_red_spikes_1,
    ]
    location_table = keep_one_location(multiworld, location_table, p2_gkey_1_locs, CastleLocationNames.crloc_p2_gkey_1)
    p2_gkey_2_locs: typing.List[str] = [
        CastleLocationNames.p2_beetle_boss_room_2,
        CastleLocationNames.p2_beetle_boss_room_1,
        CastleLocationNames.p2_beetle_boss_room_3,
    ]
    location_table = keep_one_location(multiworld, location_table, p2_gkey_2_locs, CastleLocationNames.crloc_p2_gkey_2)
    if multiworld.difficulty[player] == Difficulty.option_easier:
        remove_location(CastleLocationNames.p2_toggle_spike_trap_reward_2, ItemName.chest_wood)
        remove_location(CastleLocationNames.p2_toggle_spike_trap_reward_3, ItemName.chest_wood)
    # Prison Floor 3
    p3_bkey_1_locs: typing.List[str] = [
        CastleLocationNames.p3_entrance_w,
        CastleLocationNames.p3_entrance_n_1,
        CastleLocationNames.p3_entrance_n_2,
        CastleLocationNames.p3_entrance_m_4,
        CastleLocationNames.p3_entrance_n_of_poker,
    ]
    location_table = keep_one_location(multiworld, location_table, p3_bkey_1_locs, CastleLocationNames.crloc_p3_bkey_1)
    p3_bkey_2_locs: typing.List[str] = [
        CastleLocationNames.p3_s_of_silver_gate,
        CastleLocationNames.p3_entrance_sw,
        CastleLocationNames.p3_entrance_s_3,
        CastleLocationNames.p3_entrance_s_of_poker_3,
    ]
    location_table = keep_one_location(multiworld, location_table, p3_bkey_2_locs, CastleLocationNames.crloc_p3_bkey_2)
    p3_bkey_3_locs: typing.List[str] = [
        CastleLocationNames.p3_se_m_2,
        CastleLocationNames.p3_arrow_hall_1,
        CastleLocationNames.p3_arrow_hall_2,
        CastleLocationNames.p3_se_cross_hall_se,
    ]
    location_table = keep_one_location(multiworld, location_table, p3_bkey_3_locs, CastleLocationNames.crloc_p3_bkey_3)
    p3_skey_1_locs: typing.List[str] = [
        CastleLocationNames.p3_nw_se,
        CastleLocationNames.p3_nw_m,
        CastleLocationNames.p3_nw_nw_3,
        CastleLocationNames.p3_nw_sw_1,
        CastleLocationNames.p3_nw_sw_2,
    ]
    location_table = keep_one_location(multiworld, location_table, p3_skey_1_locs, CastleLocationNames.crloc_p3_skey)
    p3_gkey_1_locs: typing.List[str] = [
        CastleLocationNames.p3_w_of_bridge,
        CastleLocationNames.p3_nw_of_bridge,
        CastleLocationNames.p3_s_of_w_poker,
        CastleLocationNames.p3_w_of_w_poker,
        CastleLocationNames.p3_n_of_bridge_5,
    ]
    location_table = keep_one_location(multiworld, location_table, p3_gkey_1_locs, CastleLocationNames.crloc_p3_gkey)
    # Remove puzzles
    remove_puzzle_locations(CastleLocationNames.p2_puzzle_1[:-1], CastleLocationNames.crloc_p2_puzzle)
    remove_puzzle_locations(CastleLocationNames.a1_puzzle_1[:-1], CastleLocationNames.crloc_a1_puzzle)
    remove_puzzle_locations(CastleLocationNames.a2_puzzle_1[:-1], CastleLocationNames.crloc_a2_puzzle)
    remove_puzzle_locations(CastleLocationNames.r1_puzzle_1[:-1], CastleLocationNames.crloc_r1_puzzle)
    remove_puzzle_locations(CastleLocationNames.r2_puzzle_1[:-1], CastleLocationNames.crloc_r2_puzzle)

    return location_table


def choose_tots_random_locations(multiworld, player: int, location_table: typing.Dict[str, LocationData]):

    def remove_location(location: str, item: str):
        if not multiworld.randomize_recovery_items[player] and item in recovery_table.keys():
            return
        location_table.pop(location)
        temple_item_counts[item] -= 1

    def remove_secret(secret_location: str):
        if secret_location in location_table.keys():
            remove_location(secret_location, ItemName.secret)

    def remove_puzzle_locations(base_name: str, rloc_name: str):
        if random_locations[rloc_name] < 18:
            remove_location(f"{base_name}4", ItemName.chest_purple)
        if random_locations[rloc_name] < 14:
            remove_location(f"{base_name}3", ItemName.stat_upgrade)
        if random_locations[rloc_name] < 10:
            remove_location(f"{base_name}2", ItemName.ankh)
        if random_locations[rloc_name] < 1:
            remove_location(f"{base_name}1", ItemName.potion_rejuvenation)

    # Secrets
    if multiworld.randomize_secrets[player]:
        random_locations[TempleLocationNames.rloc_c3_secret_n] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c3_secret_nw] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c3_secret_s] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c2_secret_1] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c2_secret_2] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c2_secret_3] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c1_secret_1] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c1_secret_2] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c1_secret_3] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c1_secret_4] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c1_secret_5] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_c1_secret_6] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_b1_secret] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_p_secret_1] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_p_secret_2] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_p_secret_3] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_p_secret_4] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_p_secret_5] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_p_secret_6] = multiworld.random.randrange(2)
        random_locations[TempleLocationNames.rloc_p_secret_7] = multiworld.random.randrange(2)
    else:
        random_locations[TempleLocationNames.rloc_c3_secret_n] = 0
        random_locations[TempleLocationNames.rloc_c3_secret_nw] = 0
        random_locations[TempleLocationNames.rloc_c3_secret_s] = 0
        random_locations[TempleLocationNames.rloc_c2_secret_1] = 0
        random_locations[TempleLocationNames.rloc_c2_secret_2] = 0
        random_locations[TempleLocationNames.rloc_c2_secret_3] = 0
        random_locations[TempleLocationNames.rloc_c1_secret_1] = 0
        random_locations[TempleLocationNames.rloc_c1_secret_2] = 0
        random_locations[TempleLocationNames.rloc_c1_secret_3] = 0
        random_locations[TempleLocationNames.rloc_c1_secret_4] = 0
        random_locations[TempleLocationNames.rloc_c1_secret_5] = 0
        random_locations[TempleLocationNames.rloc_c1_secret_6] = 0
        random_locations[TempleLocationNames.rloc_b1_secret] = 0
        random_locations[TempleLocationNames.rloc_p_secret_1] = 0
        random_locations[TempleLocationNames.rloc_p_secret_2] = 0
        random_locations[TempleLocationNames.rloc_p_secret_3] = 0
        random_locations[TempleLocationNames.rloc_p_secret_4] = 0
        random_locations[TempleLocationNames.rloc_p_secret_5] = 0
        random_locations[TempleLocationNames.rloc_p_secret_6] = 0
        random_locations[TempleLocationNames.rloc_p_secret_7] = 0
    if random_locations[TempleLocationNames.rloc_c3_secret_n] == 0:
        remove_secret(TempleLocationNames.cave3_secret_n)
    if random_locations[TempleLocationNames.rloc_c3_secret_nw] == 0:
        remove_secret(TempleLocationNames.cave3_secret_nw)
    if random_locations[TempleLocationNames.rloc_c3_secret_s] == 0:
        remove_secret(TempleLocationNames.cave3_secret_s)
    if random_locations[TempleLocationNames.rloc_c2_secret_1] == 0:
        remove_secret(TempleLocationNames.cave2_secret_ne)
    if random_locations[TempleLocationNames.rloc_c2_secret_2] == 0:
        remove_secret(TempleLocationNames.cave2_secret_w)
    if random_locations[TempleLocationNames.rloc_c2_secret_3] == 0:
        remove_secret(TempleLocationNames.cave2_secret_m)
    if random_locations[TempleLocationNames.rloc_c1_secret_1] == 0:
        remove_secret(TempleLocationNames.cave1_secret_nw)
    if random_locations[TempleLocationNames.rloc_c1_secret_2] == 0:
        remove_secret(TempleLocationNames.cave1_secret_n_hidden_room)
    if random_locations[TempleLocationNames.rloc_c1_secret_3] == 0:
        remove_secret(TempleLocationNames.cave1_secret_ne)
    if random_locations[TempleLocationNames.rloc_c1_secret_4] == 0:
        remove_secret(TempleLocationNames.cave1_secret_w)
    if random_locations[TempleLocationNames.rloc_c1_secret_5] == 0:
        remove_secret(TempleLocationNames.cave1_secret_m)
    if random_locations[TempleLocationNames.rloc_c1_secret_6] == 0:
        remove_secret(TempleLocationNames.cave1_secret_e)
    if random_locations[TempleLocationNames.rloc_b1_secret] == 0:
        remove_secret(TempleLocationNames.boss1_secret)
    if random_locations[TempleLocationNames.rloc_p_secret_1] == 0:
        remove_secret(TempleLocationNames.p_ent2_secret)
    if random_locations[TempleLocationNames.rloc_p_secret_2] == 0:
        remove_secret(TempleLocationNames.p_mid3_secret_1)
    if random_locations[TempleLocationNames.rloc_p_secret_3] == 0:
        remove_secret(TempleLocationNames.p_mid3_secret_2)
    if random_locations[TempleLocationNames.rloc_p_secret_4] == 0:
        remove_secret(TempleLocationNames.p_mid3_secret_3)
    if random_locations[TempleLocationNames.rloc_p_secret_5] == 0:
        remove_secret(TempleLocationNames.p_mid3_secret_4)
    if random_locations[TempleLocationNames.rloc_p_secret_6] == 0:
        remove_secret(TempleLocationNames.p_end1_secret)
    if random_locations[TempleLocationNames.rloc_p_secret_7] == 0:
        remove_secret(TempleLocationNames.p_mid5_secret)
    # Set puzzle random values
    if multiworld.randomize_puzzles[player]:
        randomize_puzzle(multiworld, TempleLocationNames.rloc_c3_puzzle)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_c2_puzzle)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_c1_puzzle_n)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_c1_puzzle_e)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_p_puzzle)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_t1_puzzle_w)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_t1_puzzle_e)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_t2_puzzle_n)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_t2_puzzle_nw)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_t2_puzzle_e)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_t2_puzzle_sw)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_t3_puzzle)
        randomize_puzzle(multiworld, TempleLocationNames.rloc_pof_puzzle)
    else:
        random_locations[TempleLocationNames.rloc_c3_puzzle] = -1
        random_locations[TempleLocationNames.rloc_c2_puzzle] = -1
        random_locations[TempleLocationNames.rloc_c1_puzzle_n] = -1
        random_locations[TempleLocationNames.rloc_c1_puzzle_e] = -1
        random_locations[TempleLocationNames.rloc_p_puzzle] = -1
        random_locations[TempleLocationNames.rloc_t1_puzzle_w] = -1
        random_locations[TempleLocationNames.rloc_t1_puzzle_e] = -1
        random_locations[TempleLocationNames.rloc_t2_puzzle_n] = -1
        random_locations[TempleLocationNames.rloc_t2_puzzle_nw] = -1
        random_locations[TempleLocationNames.rloc_t2_puzzle_e] = -1
        random_locations[TempleLocationNames.rloc_t2_puzzle_sw] = -1
        random_locations[TempleLocationNames.rloc_t3_puzzle] = -1
        random_locations[TempleLocationNames.rloc_pof_puzzle] = -1
    # Dunes
    random_locations[TempleLocationNames.rloc_t3_entrance] = multiworld.random.randrange(3)
    # Cave level 3
    random_locations[TempleLocationNames.rloc_squire] = multiworld.random.randrange(6)
    if random_locations[TempleLocationNames.rloc_squire] != 1:
        remove_location(TempleLocationNames.cave3_squire, ItemName.stat_upgrade)
    # Pan location
    pan_locations: typing.List[str] = [
        TempleLocationNames.cave3_nw,
        TempleLocationNames.cave3_m,
        TempleLocationNames.cave3_se,
        TempleLocationNames.cave2_nw_2,
        TempleLocationNames.cave2_red_bridge_4,
        TempleLocationNames.cave2_double_bridge_r,
        TempleLocationNames.cave1_n_bridges_4,
        TempleLocationNames.cave1_double_room_l,
        TempleLocationNames.cave1_e_3,
    ]
    location_table = keep_one_location(multiworld, location_table, pan_locations, TempleLocationNames.rloc_pan)
    # Cave level 2
    c2_keystone_locations: typing.List[str] = [
        TempleLocationNames.cave2_guard_s,
        TempleLocationNames.cave2_nw_3,
        TempleLocationNames.cave2_w_miniboss_4,
        TempleLocationNames.cave2_red_bridge_3,
        TempleLocationNames.cave2_below_pumps_3
    ]
    location_table = keep_one_location(multiworld, location_table, c2_keystone_locations, TempleLocationNames.rloc_c2_keystone)
    random_locations[TempleLocationNames.rloc_c2_portal] = multiworld.random.randrange(3)
    if random_locations[TempleLocationNames.rloc_c2_portal] == 0:
        remove_location(TempleLocationNames.cave2_nw_4, ItemName.apple)
        remove_location(TempleLocationNames.cave2_nw_5, ItemName.apple)
    elif random_locations[TempleLocationNames.rloc_c2_portal] == 1:
        remove_location(TempleLocationNames.cave2_pumps_n, ItemName.vendor_coin)
    random_locations[TempleLocationNames.rloc_c2_hidden_room] = multiworld.random.randrange(4)
    if random_locations[TempleLocationNames.rloc_c2_hidden_room] >= 2:
        remove_location(TempleLocationNames.cave2_sw_hidden_room_1, ItemName.vendor_coin)
        remove_location(TempleLocationNames.cave2_sw_hidden_room_2, ItemName.stat_upgrade)
        remove_location(TempleLocationNames.cave2_sw_hidden_room_3, ItemName.ankh)
        remove_location(TempleLocationNames.cave2_sw_hidden_room_4, ItemName.chest_wood)
    # Cave level 1
    c1_keystone_locations: typing.List[str] = [
        TempleLocationNames.cave1_ne_grubs,
        TempleLocationNames.cave1_w_by_water_2,
        TempleLocationNames.cave1_m
    ]
    location_table = keep_one_location(multiworld, location_table, c1_keystone_locations, TempleLocationNames.rloc_c1_keystone)
    random_locations[TempleLocationNames.rloc_c1_portal] = multiworld.random.randrange(3)
    if random_locations[TempleLocationNames.rloc_c1_portal] == 0:
        remove_location(TempleLocationNames.cave1_n_bridges_5, ItemName.chest_wood)
    random_locations[TempleLocationNames.rloc_c1_hidden_room] = multiworld.random.randrange(4)
    if random_locations[TempleLocationNames.rloc_c1_hidden_room] >= 2:
        remove_location(TempleLocationNames.cave1_ne_hidden_room_1, ItemName.chest_wood)
        remove_location(TempleLocationNames.cave1_ne_hidden_room_2, ItemName.chest_wood)
        remove_location(TempleLocationNames.cave1_ne_hidden_room_3, ItemName.stat_upgrade)
        remove_location(TempleLocationNames.cave1_ne_hidden_room_4, ItemName.vendor_coin)
        remove_location(TempleLocationNames.cave1_ne_hidden_room_5, ItemName.chest_wood)
        remove_secret(TempleLocationNames.cave1_secret_n_hidden_room)
        remove_location(TempleLocationNames.cave1_secret_tunnel_1, ItemName.ankh)
        remove_location(TempleLocationNames.cave1_secret_tunnel_2, ItemName.steak)
        remove_location(TempleLocationNames.cave1_secret_tunnel_3, ItemName.mana_2)
    random_locations[TempleLocationNames.rloc_c1_exit] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_c1_exit] == 0:
        random_locations[TempleLocationNames.rloc_c1_puzzle_e] = -1
    # Passage
    random_locations[TempleLocationNames.rloc_passage_entrance] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_passage_entrance] == 0:
        remove_secret(TempleLocationNames.p_ent2_secret)
    random_locations[TempleLocationNames.rloc_passage_middle] = multiworld.random.randrange(5)
    mid_locations_to_remove: typing.List[str] = [
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
    ]
    temple_item_counts[ItemName.ankh] -= 2
    temple_item_counts[ItemName.apple] -= 2
    temple_item_counts[ItemName.mana_2] -= 1
    temple_item_counts[ItemName.mana_1] -= 3
    temple_item_counts[ItemName.orange] -= 1
    temple_item_counts[ItemName.stat_upgrade] -= 2
    temple_item_counts[ItemName.chest_wood] -= 3
    if random_locations[TempleLocationNames.rloc_passage_middle] == 0:
        mid_locations_to_remove.remove(TempleLocationNames.p_mid1_1)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid1_2)
        temple_item_counts[ItemName.chest_wood] += 2
        random_locations[TempleLocationNames.rloc_p_puzzle] = -1
    elif random_locations[TempleLocationNames.rloc_passage_middle] == 1:
        mid_locations_to_remove.remove(TempleLocationNames.p_mid2_1)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid2_2)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid2_3)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid2_4)
        temple_item_counts[ItemName.mana_2] += 1
        temple_item_counts[ItemName.mana_1] += 3
        random_locations[TempleLocationNames.rloc_p_puzzle] = -1
    elif random_locations[TempleLocationNames.rloc_passage_middle] == 2:
        mid_locations_to_remove.remove(TempleLocationNames.p_mid3_secret_1)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid3_secret_2)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid3_secret_3)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid3_secret_4)
    elif random_locations[TempleLocationNames.rloc_passage_middle] == 3:
        mid_locations_to_remove.remove(TempleLocationNames.p_mid4_1)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid4_2)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid4_3)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid4_4)
        temple_item_counts[ItemName.ankh] += 1
        temple_item_counts[ItemName.orange] += 1
        temple_item_counts[ItemName.apple] += 2
        random_locations[TempleLocationNames.rloc_p_puzzle] = -1
    else:
        mid_locations_to_remove.remove(TempleLocationNames.p_mid5_1)
        mid_locations_to_remove.remove(TempleLocationNames.p_mid5_2)
        temple_item_counts[ItemName.chest_wood] += 1
        temple_item_counts[ItemName.stat_upgrade] += 1
        mid_locations_to_remove.remove(TempleLocationNames.p_mid5_secret)
        random_locations[TempleLocationNames.rloc_p_puzzle] = -1
    for loc in mid_locations_to_remove:
        if temple_locations[loc].classification == LocationClassification.Secret:
            remove_secret(loc)
        elif loc in location_table:
            location_table.pop(loc)
    random_locations[TempleLocationNames.rloc_passage_end] = multiworld.random.randrange(3)
    random_locations[TempleLocationNames.rloc_p_alley] = multiworld.random.randrange(4)
    end_locations_to_remove: typing.List[str] = [
        TempleLocationNames.p_end1_secret,
        TempleLocationNames.p_end3_1,
        TempleLocationNames.p_end3_2,
    ]
    if random_locations[TempleLocationNames.rloc_passage_end] == 0:
        end_locations_to_remove.remove(TempleLocationNames.p_end1_secret)
    elif random_locations[TempleLocationNames.rloc_passage_end] == 2\
            and random_locations[TempleLocationNames.rloc_p_alley] < 2:
        end_locations_to_remove.remove(TempleLocationNames.p_end3_1)
        end_locations_to_remove.remove(TempleLocationNames.p_end3_2)
        temple_item_counts[ItemName.ankh] += 1
        temple_item_counts[ItemName.stat_upgrade] += 1
    for loc in end_locations_to_remove:
        if temple_locations[loc].classification == LocationClassification.Secret:
            remove_secret(loc)
        else:
            location_table.pop(loc)
    # Temple level 1
    # Custom logic for the keystone location, as a diamond spawns in one of the spots if it doesn't appear there
    t1_keystone_locations: typing.List[str] = [
        TempleLocationNames.t1_sun_block_hall_4,
        TempleLocationNames.t1_fire_trap_by_sun_turret_3,
        TempleLocationNames.t1_ledge_after_block_trap_1,
        TempleLocationNames.t1_sw_cache_3
    ]
    random_locations[TempleLocationNames.rloc_t1_keystone] = multiworld.random.randrange(len(t1_keystone_locations))
    t1_keystone_locations.pop(random_locations[TempleLocationNames.rloc_t1_keystone])
    if random_locations[TempleLocationNames.rloc_t1_keystone] == 2:  # Remove the diamond that would spawn there
        temple_item_counts[ItemName.diamond_small] -= 1
    else:
        t1_keystone_locations.remove(TempleLocationNames.t1_ledge_after_block_trap_1)  # Remove the diamond-filled loc
    for loc in t1_keystone_locations:
        location_table.pop(loc)
    random_locations[TempleLocationNames.rloc_t1_portal] = multiworld.random.randrange(3)
    if random_locations[TempleLocationNames.rloc_t1_portal] == 2:
        remove_location(TempleLocationNames.t1_sun_turret_3, ItemName.chest_green)
    t1_silver_key_s_locations: typing.List[str] = [
        TempleLocationNames.t1_s_bridge_1,
        TempleLocationNames.t1_above_s_bridge,
        TempleLocationNames.t1_sw_corner_room,
    ]
    location_table = keep_one_location(multiworld, location_table, t1_silver_key_s_locations,
                                       TempleLocationNames.rloc_t1_silver_key_s)
    t1_silver_key_n_locations: typing.List[str] = [
        TempleLocationNames.t1_n_sunbeam_treasure_3,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_4,
    ]
    location_table = keep_one_location(multiworld, location_table, t1_silver_key_n_locations,
                                       TempleLocationNames.rloc_t1_silver_key_n)
    t1_silver_key_ice_turret_locations: typing.List[str] = [
        TempleLocationNames.t1_ice_turret_1,
        TempleLocationNames.t1_ice_turret_2,
    ]
    location_table = keep_one_location(multiworld, location_table, t1_silver_key_ice_turret_locations,
                                       TempleLocationNames.rloc_t1_silver_key_ice_turret)
    random_locations[TempleLocationNames.rloc_t1_silver_key_funky] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t1_silver_key_funky] == 0:
        location_table.pop(TempleLocationNames.t1_e_of_double_gate_room_2)
        random_locations[TempleLocationNames.rloc_t1_ore_funky] = multiworld.random.randrange(2)
    else:
        random_locations[TempleLocationNames.rloc_t1_ore_funky] = -1
    if random_locations[TempleLocationNames.rloc_t1_ore_funky] != 0:
        location_table.pop(TempleLocationNames.t1_fire_trap_by_sun_turret_4)
    if random_locations[TempleLocationNames.rloc_t1_ore_funky] != 1:
        location_table.pop(TempleLocationNames.t1_mana_drain_fire_trap)
    t1_gold_key_locations: typing.List[str] = [
        TempleLocationNames.t1_n_cache_by_ice_turret_5,
        TempleLocationNames.t1_s_cache_by_ice_turret_3,
    ]
    location_table = keep_one_location(multiworld, location_table, t1_gold_key_locations, TempleLocationNames.rloc_t1_gold_key)
    t1_ore_e_locations: typing.List[str] = [
        TempleLocationNames.t1_sun_block_hall_3,
        TempleLocationNames.t1_e_gold_beetles,
    ]
    location_table = keep_one_location(multiworld, location_table, t1_ore_e_locations, TempleLocationNames.rloc_t1_ore_e)
    t1_mirror_locations: typing.List[str] = [
        TempleLocationNames.t1_ledge_after_block_trap_2,
        TempleLocationNames.t1_ice_block_chamber_3,
        TempleLocationNames.t1_ice_block_chamber_2
    ]
    location_table = keep_one_location(multiworld, location_table, t1_mirror_locations, TempleLocationNames.rloc_t1_mirror)
    # There's a 1/5 chance to potentially open the way to the hidden room
    random_locations[TempleLocationNames.rloc_t1_sw_hidden_room_random_node] = multiworld.random.randrange(5)
    random_locations[TempleLocationNames.rloc_t1_sw_hidden_room] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t1_sw_hidden_room_random_node] != 1\
            or random_locations[TempleLocationNames.rloc_t1_sw_hidden_room] == 1:
        remove_location(TempleLocationNames.t1_sw_hidden_room_1, ItemName.vendor_coin)
        remove_location(TempleLocationNames.t1_sw_hidden_room_2, ItemName.stat_upgrade)
        remove_location(TempleLocationNames.t1_sw_hidden_room_3, ItemName.ankh)
        remove_location(TempleLocationNames.t1_sw_hidden_room_4, ItemName.chest_green)
        random_locations[TempleLocationNames.rloc_t1_sw_hidden_room] = 1
    random_locations[TempleLocationNames.rloc_t1_puzzle_spawn] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t1_puzzle_spawn] == 0:
        random_locations[TempleLocationNames.rloc_t1_puzzle_e] = -1
    else:
        random_locations[TempleLocationNames.rloc_t1_puzzle_w] = -1
    # Temple Level 2
    t2_keystone_locations: typing.List[str] = [
        TempleLocationNames.t2_se_banner_chamber_5,
        TempleLocationNames.t2_s_balcony_2,
        TempleLocationNames.t2_s_of_portal,
        TempleLocationNames.t2_n_of_sw_gate_2,
        TempleLocationNames.t2_nw_ice_turret_4,
        TempleLocationNames.t2_boulder_chamber_3,
        TempleLocationNames.t2_left_of_pof_switch_2,
    ]
    location_table = keep_one_location(multiworld, location_table, t2_keystone_locations, TempleLocationNames.rloc_t2_keystone)
    random_locations[TempleLocationNames.rloc_t2_portal] = multiworld.random.randrange(4)
    if random_locations[TempleLocationNames.rloc_t2_portal] != 2:
        remove_location(TempleLocationNames.t2_teleporter, ItemName.stat_upgrade)
    random_locations[TempleLocationNames.rloc_t2_puzzle_spawn_1] = multiworld.random.randrange(2)
    random_locations[TempleLocationNames.rloc_t2_w_hidden_room] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t2_puzzle_spawn_1] == 0:
        random_locations[TempleLocationNames.rloc_t2_puzzle_e] = -1  # Turn off east puzzle
    else:
        random_locations[TempleLocationNames.rloc_t2_puzzle_nw] = -1
        random_locations[TempleLocationNames.rloc_t2_w_hidden_room] = 1
    if random_locations[TempleLocationNames.rloc_t2_w_hidden_room] != 0:
        # Prevent items from appearing behind the west puzzle in the cache
        remove_location(TempleLocationNames.t2_nw_puzzle_cache_1, ItemName.chest_blue)
        remove_location(TempleLocationNames.t2_nw_puzzle_cache_2, ItemName.chest_blue)
        remove_location(TempleLocationNames.t2_nw_puzzle_cache_3, ItemName.vendor_coin)
        remove_location(TempleLocationNames.t2_nw_puzzle_cache_4, ItemName.stat_upgrade)
        remove_location(TempleLocationNames.t2_nw_puzzle_cache_5, ItemName.ankh)
    random_locations[TempleLocationNames.rloc_t2_puzzle_spawn_2] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t2_puzzle_spawn_2] == 0:
        random_locations[TempleLocationNames.rloc_t2_puzzle_n] = -1
    else:
        random_locations[TempleLocationNames.rloc_t2_puzzle_sw] = -1
    random_locations[TempleLocationNames.rloc_t2_jones_reward] = multiworld.random.randrange(2)
    t2_gold_key_locations: typing.List[str] = [
        TempleLocationNames.t2_right_of_pof_switch,
        TempleLocationNames.t2_sw_jail_2,
        TempleLocationNames.t2_boulder_room_2,
    ]
    if random_locations[TempleLocationNames.rloc_t2_jones_reward] == 0:
        location_table = keep_one_location(multiworld, location_table, t2_gold_key_locations,
                                           TempleLocationNames.rloc_t2_gold_key)
    else:
        temple_item_counts[ItemName.stat_upgrade] -= 1
        for loc in t2_gold_key_locations:
            location_table.pop(loc)
    t2_silver_key_1_locations: typing.List[str] = [
        TempleLocationNames.t2_fire_trap_maze_5,
        TempleLocationNames.t2_fire_trap_maze_6,
        TempleLocationNames.t2_w_hall_dead_end_5,
        TempleLocationNames.t2_nw_of_s_ice_turret,
        TempleLocationNames.t2_n_of_portal,
    ]
    location_table = keep_one_location(multiworld, location_table, t2_silver_key_1_locations,
                                       TempleLocationNames.rloc_t2_silver_key_1)
    t2_silver_key_2_locations: typing.List[str] = [
        TempleLocationNames.t2_se_fireball_hall,
        TempleLocationNames.t2_se_banner_chamber_4,
        TempleLocationNames.t2_s_balcony_1,
        TempleLocationNames.t2_boulder_chamber_4,
    ]
    location_table = keep_one_location(multiworld, location_table, t2_silver_key_2_locations,
                                       TempleLocationNames.rloc_t2_silver_key_2)
    t2_pickaxe_locations: typing.List[str] = [
        TempleLocationNames.t2_w_ice_block_gate,
        TempleLocationNames.t2_e_ice_block_gate
    ]
    location_table = keep_one_location(multiworld, location_table, t2_pickaxe_locations, TempleLocationNames.rloc_t2_pickaxe)
    # Temple Level 3
    random_locations[TempleLocationNames.rloc_t3_s_beam_1] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t3_s_beam_1] == 0:
        remove_location(TempleLocationNames.t3_n_node_blocks_1, ItemName.vendor_coin)
    random_locations[TempleLocationNames.rloc_t3_s_beam_2] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t3_s_beam_2] == 0:
        remove_location(TempleLocationNames.t3_n_node_blocks_2, ItemName.vendor_coin)
    random_locations[TempleLocationNames.rloc_t3_s_beam_3] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t3_s_beam_3] == 0:
        remove_location(TempleLocationNames.t3_n_node_blocks_3, ItemName.vendor_coin)
    random_locations[TempleLocationNames.rloc_t3_s_beam_4] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t3_s_beam_4] == 0:
        remove_location(TempleLocationNames.t3_n_node_blocks_4, ItemName.vendor_coin)
    random_locations[TempleLocationNames.rloc_t3_s_beam_5] = multiworld.random.randrange(2)
    if random_locations[TempleLocationNames.rloc_t3_s_beam_5] == 0:
        remove_location(TempleLocationNames.t3_n_node_blocks_5, ItemName.vendor_coin)
    # Remove puzzle locations
    remove_puzzle_locations(TempleLocationNames.c3_puzzle_1[:-1], TempleLocationNames.rloc_c3_puzzle)
    remove_puzzle_locations(TempleLocationNames.c2_puzzle_1[:-1], TempleLocationNames.rloc_c2_puzzle)
    remove_puzzle_locations(TempleLocationNames.c1_n_puzzle_1[:-1], TempleLocationNames.rloc_c1_puzzle_n)
    remove_puzzle_locations(TempleLocationNames.c1_e_puzzle_1[:-1], TempleLocationNames.rloc_c1_puzzle_e)
    remove_puzzle_locations(TempleLocationNames.p_puzzle_1[:-1], TempleLocationNames.rloc_p_puzzle)
    remove_puzzle_locations(TempleLocationNames.t1_w_puzzle_1[:-1], TempleLocationNames.rloc_t1_puzzle_w)
    remove_puzzle_locations(TempleLocationNames.t1_e_puzzle_1[:-1], TempleLocationNames.rloc_t1_puzzle_e)
    remove_puzzle_locations(TempleLocationNames.t2_n_puzzle_1[:-1], TempleLocationNames.rloc_t2_puzzle_n)
    remove_puzzle_locations(TempleLocationNames.t2_nw_puzzle_1[:-1], TempleLocationNames.rloc_t2_puzzle_nw)
    remove_puzzle_locations(TempleLocationNames.t2_e_puzzle_1[:-1], TempleLocationNames.rloc_t2_puzzle_e)
    remove_puzzle_locations(TempleLocationNames.t2_sw_puzzle_1[:-1], TempleLocationNames.rloc_t2_puzzle_sw)
    remove_puzzle_locations(TempleLocationNames.t3_puzzle_1[:-1], TempleLocationNames.rloc_t3_puzzle)
    remove_puzzle_locations(TempleLocationNames.pof_puzzle_1[:-1], TempleLocationNames.rloc_pof_puzzle)

    return location_table


def remove_castle_location(location_table, location: str, item: str):
    location_table.pop(location)
    castle_item_counts[item] -= 1


def remove_temple_location(location_table, location: str, item: str):
    location_table.pop(location)
    temple_item_counts[item] -= 1


def randomize_puzzle(multiworld: MultiWorld, rloc_name: str):
    pegs = 0
    for p in range(25):
        pegs += multiworld.random.randrange(2)
    random_locations[rloc_name] = pegs


def keep_one_location(multiworld, location_table: typing.Dict[str, LocationData], locations: typing.List[str],
                      rloc_name: str):
    random_locations[rloc_name] = multiworld.random.randrange(len(locations))
    locations.pop(random_locations[rloc_name])
    for loc in locations:
        location_table.pop(loc)
    return location_table


lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in all_locations.items() if
                                            data.code}
