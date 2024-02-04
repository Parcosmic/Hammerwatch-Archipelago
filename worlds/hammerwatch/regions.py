import typing
from enum import Enum
from collections import namedtuple
from BaseClasses import Region, Entrance
from worlds.generic.Rules import add_rule
from .locations import HammerwatchLocation, LocationData, all_locations
from .names import castle_location_names, temple_location_names, castle_region_names, temple_region_names, item_name, \
    gate_names, entrance_names
from .util import GoalType, Campaign, get_goal_type, get_random_element

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


def create_regions(world: "HammerwatchWorld", campaign: Campaign, active_locations: typing.Dict[str, LocationData],
                   random_locations: typing.Dict[str, int]):
    gate_codes = {}
    if campaign == Campaign.Castle:
        create_castle_regions(world, active_locations, random_locations)
        connect_castle_regions(world, random_locations, gate_codes)
    else:
        create_tots_regions(world, active_locations, random_locations)
        connect_tots_regions(world, random_locations, gate_codes)
    return gate_codes


def create_castle_regions(world: "HammerwatchWorld", active_locations: typing.Dict[str, LocationData],
                          random_locations: typing.Dict[str, int]):
    goal = get_goal_type(world)

    menu_region = create_region(world, active_locations, castle_region_names.menu)
    hub_region = create_region(world, active_locations, castle_region_names.hub)

    p1_start_locations = [
        castle_location_names.p1_by_nw_bronze_gate,
        castle_location_names.btn_p1_floor,
    ]
    p1_start_region = create_region(world, active_locations, castle_region_names.p1_start,
                                    p1_start_locations)

    p1_nw_locs = [
        castle_location_names.p1_entrance_1,
        castle_location_names.p1_entrance_2,
        castle_location_names.p1_entrance_3,
        castle_location_names.p1_entrance_4,
        castle_location_names.p1_entrance_hall_1,
        castle_location_names.p1_entrance_hall_2,
        castle_location_names.p1_entrance_secret,
    ]
    p1_nw_region = create_region(world, active_locations, castle_region_names.p1_nw, p1_nw_locs)

    p1_nw_left_locs = [
        castle_location_names.p1_entrance_s,
        castle_location_names.p1_entrance_w,
    ]
    p1_nw_left_region = create_region(world, active_locations, castle_region_names.p1_nw_left,
                                      p1_nw_left_locs)

    p1_s_locations = [
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
    ]
    p1_s_region = create_region(world, active_locations, castle_region_names.p1_s, p1_s_locations)

    p1_sw_bronze_gate_locations = [
        castle_location_names.p1_sw_bronze_gate,
    ]
    p1_sw_bronze_gate_region = create_region(world, active_locations, castle_region_names.p1_sw_bronze_gate,
                                             p1_sw_bronze_gate_locations)

    p1_e_locations = [
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
    ]
    p1_e_region = create_region(world, active_locations, castle_region_names.p1_e, p1_e_locations)

    p1_m_bronze_gate_locations = [
        castle_location_names.p1_m_bronze_gate,
    ]
    p1_m_bronze_gate_region = create_region(world, active_locations, castle_region_names.p1_m_bronze_gate,
                                            p1_m_bronze_gate_locations)

    p1_from_p2_locations = [
        castle_location_names.p1_bars_1,
        castle_location_names.p1_bars_2,
        castle_location_names.p1_p2_by_shop,
    ]
    p1_from_p2_region = create_region(world, active_locations, castle_region_names.p1_from_p2,
                                      p1_from_p2_locations)

    p1_from_p3_n_locations = [
        castle_location_names.p1_p3_n_bridge,
        castle_location_names.p1_p3_n_across_bridge,
        castle_location_names.ev_p1_boss_switch
    ]
    p1_from_p3_n_region = create_region(world, active_locations, castle_region_names.p1_from_p3_n,
                                        p1_from_p3_n_locations)

    p1_from_p3_s_locations = [
        castle_location_names.p1_p3_s,
    ]
    p1_from_p3_s_region = create_region(world, active_locations, castle_region_names.p1_from_p3_s,
                                        p1_from_p3_s_locations)

    p2_start_locations = []
    p2_start_region = create_region(world, active_locations, castle_region_names.p2_start,
                                    p2_start_locations)

    p2_m_locations = [
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
    ]
    p2_m_region = create_region(world, active_locations, castle_region_names.p2_m, p2_m_locations)

    p2_p1_return_locs = [
    ]
    p2_p1_return_region = create_region(world, active_locations, castle_region_names.p2_p1_return,
                                        p2_p1_return_locs)

    p2_n_locations = [
        castle_location_names.p2_spike_puzzle_e_1,
        castle_location_names.p2_spike_puzzle_e_2,
        castle_location_names.p2_spike_puzzle_ne_1,
        castle_location_names.p2_spike_puzzle_ne_2,
        castle_location_names.p2_spike_puzzle_ne_3,
        castle_location_names.p2_spike_puzzle_e,
    ]
    p2_n_region = create_region(world, active_locations, castle_region_names.p2_n, p2_n_locations)

    p2_spike_puzzle_bottom_locs = [
    ]
    p2_spike_puzzle_bottom_region = create_region(world, active_locations,
                                                  castle_region_names.p2_spike_puzzle_bottom,
                                                  p2_spike_puzzle_bottom_locs)

    p2_spike_puzzle_left_locs = [
        castle_location_names.p2_spike_puzzle_w_1,
        castle_location_names.p2_spike_puzzle_w_2,
    ]
    p2_spike_puzzle_left_region = create_region(world, active_locations,
                                                castle_region_names.p2_spike_puzzle_left,
                                                p2_spike_puzzle_left_locs)

    p2_spike_puzzle_top_locs = [
        castle_location_names.p2_spike_puzzle_n_1,
        castle_location_names.p2_spike_puzzle_n_2,
    ]
    p2_spike_puzzle_top_region = create_region(world, active_locations,
                                               castle_region_names.p2_spike_puzzle_top,
                                               p2_spike_puzzle_top_locs)

    p2_red_switch_locations = [
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
    ]
    p2_red_switch_region = create_region(world, active_locations, castle_region_names.p2_red_switch,
                                         p2_red_switch_locations)

    p2_puzzle_locs = [
        castle_location_names.p2_puzzle_1,
        castle_location_names.p2_puzzle_2,
        castle_location_names.p2_puzzle_3,
        castle_location_names.p2_puzzle_4,
    ]
    p2_puzzle_region = create_region(world, active_locations, castle_region_names.p2_puzzle, p2_puzzle_locs)

    p2_e_bronze_gate_locations = [
        # Offense shop
    ]
    p2_e_bronze_gate_region = create_region(world, active_locations, castle_region_names.p2_e_bronze_gate,
                                            p2_e_bronze_gate_locations)

    p2_e_save_locs = [
        castle_location_names.p2_e_save,
    ]
    p2_e_save_region = create_region(world, active_locations, castle_region_names.p2_e_save, p2_e_save_locs)

    p2_s_locations = [
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
        castle_location_names.ev_p2_gold_gate_room_sw_switch,
        castle_location_names.ev_p2_boss_switch,
    ]
    p2_s_region = create_region(world, active_locations, castle_region_names.p2_s, p2_s_locations)

    p2_e_bronze_gate_2_locations = [
        castle_location_names.ev_p2_gold_gate_room_ne_switch
    ]
    p2_e_bronze_gate_2_region = create_region(world, active_locations,
                                              castle_region_names.p2_e_bronze_gate_2,
                                              p2_e_bronze_gate_2_locations)

    p2_m_bronze_gate_locations = [
        castle_location_names.ev_p2_gold_gate_room_nw_switch
    ]
    p2_m_bronze_gate_region = create_region(world, active_locations, castle_region_names.p2_m_bronze_gate,
                                            p2_m_bronze_gate_locations)

    p2_se_bronze_gate_locations = [
        castle_location_names.ev_p2_gold_gate_room_se_switch
    ]
    p2_se_bronze_gate_region = create_region(world, active_locations, castle_region_names.p2_se_bronze_gate,
                                             p2_se_bronze_gate_locations)

    p2_gg_room_reward_locations = [
        castle_location_names.p2_e_gold_gate_room_reward_1,
        castle_location_names.p2_e_gold_gate_room_reward_2,
    ]
    p2_gg_room_reward_region = create_region(world, active_locations, castle_region_names.p2_gg_room_reward,
                                             p2_gg_room_reward_locations)

    p2_w_treasure_locs = [
        castle_location_names.p2_beetle_boss_hidden_room_1,
    ]
    p2_w_treasure_region = create_region(world, active_locations, castle_region_names.p2_w_treasure,
                                         p2_w_treasure_locs)

    p2_w_treasure_tp_locs = [
        castle_location_names.p2_beetle_boss_hidden_room_2,
    ]
    p2_w_treasure_tp_region = create_region(world, active_locations, castle_region_names.p2_w_treasure_tp,
                                            p2_w_treasure_tp_locs)

    p2_tp_puzzle_locs = [
        castle_location_names.p2_sequence_puzzle_reward,
    ]
    p2_tp_puzzle_region = create_region(world, active_locations, castle_region_names.p2_tp_puzzle,
                                        p2_tp_puzzle_locs)

    p2_end_locations = [
        castle_location_names.p2_end_1,
        castle_location_names.p2_end_2,
    ]
    p2_end_region = create_region(world, active_locations, castle_region_names.p2_end, p2_end_locations)

    p3_start_door_locs = [
    ]
    p3_start_door_region = create_region(world, active_locations, castle_region_names.p3_start_door,
                                         p3_start_door_locs)

    p3_start_locs = [
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
        castle_location_names.p3_nw_closed_room,
        castle_location_names.p3_tower_plant_1,
    ]
    p3_start_region = create_region(world, active_locations, castle_region_names.p3_start, p3_start_locs)

    p3_nw_closed_room_locs = [
    ]
    p3_nw_closed_room_region = create_region(world, active_locations, castle_region_names.p3_nw_closed_room,
                                             p3_nw_closed_room_locs)

    p3_nw_n_bronze_gate_locs = [
        castle_location_names.p3_nw_n_bronze_gate_1,
        castle_location_names.p3_nw_n_bronze_gate_2,
        castle_location_names.p3_nw_n_bronze_gate_3,
        castle_location_names.p3_nw_n_bronze_gate_4,
        castle_location_names.p3_nw_n_bronze_gate_5,
    ]
    p3_nw_n_bronze_gate_region = create_region(world, active_locations,
                                               castle_region_names.p3_nw_n_bronze_gate, p3_nw_n_bronze_gate_locs)

    p3_nw_s_bronze_gate_locs = [
        castle_location_names.p3_nw_s_bronze_gate_1,
        castle_location_names.p3_nw_s_bronze_gate_2,
        castle_location_names.p3_nw_s_bronze_gate_3,
        castle_location_names.p3_nw_s_bronze_gate_4,
        castle_location_names.p3_nw_s_bronze_gate_5,
    ]
    p3_nw_s_bronze_gate_region = create_region(world, active_locations,
                                               castle_region_names.p3_nw_s_bronze_gate, p3_nw_s_bronze_gate_locs)

    p3_s_bronze_gate_locs = [
    ]
    p3_s_bronze_gate_region = create_region(world, active_locations, castle_region_names.p3_s_bronze_gate,
                                            p3_s_bronze_gate_locs)

    p3_silver_gate_locs = [
        castle_location_names.p3_s_of_silver_gate,
    ]
    p3_silver_gate_region = create_region(world, active_locations, castle_region_names.p3_silver_gate,
                                          p3_silver_gate_locs)

    p3_n_gold_gate_locs = [
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
    ]
    p3_n_gold_gate_region = create_region(world, active_locations, castle_region_names.p3_n_gold_gate,
                                          p3_n_gold_gate_locs)

    p3_rspikes_locs = [
        castle_location_names.p3_red_spike_room,
    ]
    p3_rspikes_region = create_region(world, active_locations, castle_region_names.p3_rspikes,
                                      p3_rspikes_locs)

    p3_rspikes_room_locs = [
        castle_location_names.p3_tower_plant_4,
    ]
    p3_rspikes_room_region = create_region(world, active_locations, castle_region_names.p3_rspikes_room,
                                           p3_rspikes_room_locs)

    p3_bonus_locs = [
    ]
    p3_bonus_region = create_region(world, active_locations, castle_region_names.p3_bonus, p3_bonus_locs)

    p3_arrow_hall_secret_locs = [
        castle_location_names.btnc_p3_arrow_hall_wall,
    ]
    p3_arrow_hall_secret_region = create_region(world, active_locations,
                                                castle_region_names.p3_arrow_hall_secret, p3_arrow_hall_secret_locs)

    p3_spikes_s_locs = [
        castle_location_names.p3_spike_trap_1,
        castle_location_names.p3_spike_trap_2,
        castle_location_names.p3_spike_trap_3,
        castle_location_names.p3_by_m_shop_1,
        castle_location_names.p3_by_m_shop_2,
    ]
    p3_spikes_s_region = create_region(world, active_locations, castle_region_names.p3_spikes_s,
                                       p3_spikes_s_locs)

    p3_sw_locs = [
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
        castle_location_names.btnc_p3_sw,
    ]
    p3_sw_region = create_region(world, active_locations, castle_region_names.p3_sw, p3_sw_locs)

    p3_exit_s_locs = [
    ]
    p3_exit_s_region = create_region(world, active_locations, castle_region_names.p3_exit_s, p3_exit_s_locs)

    p3_hidden_arrow_hall_locs = [
        castle_location_names.p3_secret_secret,
        castle_location_names.p3_secret_arrow_hall_1,
        castle_location_names.p3_secret_arrow_hall_2,
    ]
    p3_hidden_arrow_hall_region = create_region(world, active_locations,
                                                castle_region_names.p3_hidden_arrow_hall, p3_hidden_arrow_hall_locs)

    p3_s_gold_gate_locs = [
        castle_location_names.ev_p3_boss_switch
    ]
    p3_s_gold_gate_region = create_region(world, active_locations, castle_region_names.p3_s_gold_gate,
                                          p3_s_gold_gate_locs)

    p3_bonus_return_locs = [
        castle_location_names.p3_bonus_return,
    ]
    p3_bonus_return_region = create_region(world, active_locations, castle_region_names.p3_bonus_return,
                                           p3_bonus_return_locs)

    if world.options.shortcut_teleporter.value:
        p3_portal_from_p1_locs = [
            castle_location_names.p3_skip_boss_switch_1,
            castle_location_names.p3_skip_boss_switch_2,
            castle_location_names.p3_skip_boss_switch_3,
            castle_location_names.p3_skip_boss_switch_4,
            castle_location_names.p3_skip_boss_switch_5,
            castle_location_names.p3_skip_boss_switch_6,
        ]
        p3_portal_from_p1_region = create_region(world, active_locations,
                                                 castle_region_names.p3_portal_from_p1, p3_portal_from_p1_locs)
        world.multiworld.regions.append(p3_portal_from_p1_region)

    n1_start_locs = [
        castle_location_names.n1_entrance
    ]
    n1_start_region = create_region(world, active_locations, castle_region_names.n1_start, n1_start_locs)

    n1_room1_locs = [
        castle_location_names.n1_room1
    ]
    n1_room1_region = create_region(world, active_locations, castle_region_names.n1_room1, n1_room1_locs)

    n1_room2_locs = [
        castle_location_names.n1_room2_s_1,
        castle_location_names.n1_room2_s_2,
        castle_location_names.n1_room2_s_3,
        castle_location_names.n1_room2_n_secret_room,
    ]
    n1_room2_region = create_region(world, active_locations, castle_region_names.n1_room2, n1_room2_locs)

    n1_room2_unlock_locs = [
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
    ]
    n1_room2_unlock_region = create_region(world, active_locations, castle_region_names.n1_room2_unlock,
                                           n1_room2_unlock_locs)

    n1_room3_locs = [
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
    ]
    n1_room3_region = create_region(world, active_locations, castle_region_names.n1_room3, n1_room3_locs)

    n1_room3_unlock_locs = [
        castle_location_names.n1_room3_sealed_room_1,
        castle_location_names.n1_room3_sealed_room_2,
        castle_location_names.n1_room3_sealed_room_3,
        castle_location_names.n1_room3_sealed_room_4,
    ]
    n1_room3_unlock_region = create_region(world, active_locations, castle_region_names.n1_room3_unlock,
                                           n1_room3_unlock_locs)

    n1_room3_hall_locs = [
    ]
    n1_room3_hall_region = create_region(world, active_locations, castle_region_names.n1_room3_hall,
                                         n1_room3_hall_locs)

    n1_room4_locs = [
        castle_location_names.n1_room4_e,
        castle_location_names.n1_room4_m,
        castle_location_names.n1_room4_w_1,
        castle_location_names.n1_room4_w_2,
        castle_location_names.n1_room4_s_1,
        castle_location_names.n1_room4_s_2,
        castle_location_names.n1_room4_s_3,
    ]
    n1_room4_region = create_region(world, active_locations, castle_region_names.n1_room4, n1_room4_locs)

    b1_start_locs = [
        castle_location_names.b1_behind_portal
    ]
    b1_start_region = create_region(world, active_locations, castle_region_names.b1_start, b1_start_locs)

    b1_arena_locs = [
        castle_location_names.b1_arena_1,
        castle_location_names.b1_arena_2
    ]
    b1_arena_region = create_region(world, active_locations, castle_region_names.b1_arena, b1_arena_locs)

    b1_defeated_locs = [
        castle_location_names.b1_reward,
        castle_location_names.ev_beat_boss_1,
    ]
    b1_defeated_region = create_region(world, active_locations, castle_region_names.b1_defeated,
                                       b1_defeated_locs)

    b1_exit_locs = [
    ]
    b1_exit_region = create_region(world, active_locations, castle_region_names.b1_exit, b1_exit_locs)

    a1_start_locs = [
    ]
    a1_start_region = create_region(world, active_locations, castle_region_names.a1_start, a1_start_locs)

    a1_start_shop_w_locs = []  # Start bronze gate shop
    a1_start_shop_w_region = create_region(world, active_locations, castle_region_names.a1_start_shop_w,
                                           a1_start_shop_w_locs)

    a1_start_shop_m_locs = []  # Start top gold gate shop
    a1_start_shop_m_region = create_region(world, active_locations, castle_region_names.a1_start_shop_m,
                                           a1_start_shop_m_locs)

    a1_start_shop_e_locs = []  # Start bottom gold gate shop
    a1_start_shop_e_region = create_region(world, active_locations, castle_region_names.a1_start_shop_e,
                                           a1_start_shop_e_locs)

    a1_se_locs = [
        castle_location_names.a1_s_save_1,
        castle_location_names.a1_s_save_2,
    ]
    a1_se_region = create_region(world, active_locations, castle_region_names.a1_se, a1_se_locs)

    a1_e_locs = [
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
        castle_location_names.a1_ne_ice_tower_secret,
        castle_location_names.a1_miniboss_skeleton_1,
        castle_location_names.a1_miniboss_skeleton_2,
        castle_location_names.a1_tower_ice_3,
        castle_location_names.a1_tower_ice_4,
    ]
    a1_e_region = create_region(world, active_locations, castle_region_names.a1_e, a1_e_locs)

    a1_e_sw_bgate_locs = []
    a1_e_sw_bgate_region = create_region(world, active_locations, castle_region_names.a1_e_sw_bgate,
                                         a1_e_sw_bgate_locs)

    a1_e_s_bgate_locs = []
    a1_e_s_bgate_region = create_region(world, active_locations, castle_region_names.a1_e_s_bgate,
                                        a1_e_s_bgate_locs)

    a1_e_se_bgate_locs = []
    a1_e_se_bgate_region = create_region(world, active_locations, castle_region_names.a1_e_se_bgate,
                                         a1_e_se_bgate_locs)

    a1_e_e_bgate_locs = []
    a1_e_e_bgate_region = create_region(world, active_locations, castle_region_names.a1_e_e_bgate,
                                        a1_e_e_bgate_locs)

    a1_rune_room_locs = [

    ]
    a1_rune_room_region = create_region(world, active_locations, castle_region_names.a1_rune_room,
                                        a1_rune_room_locs)

    a1_se_cache_locs = [
        castle_location_names.a1_se_cache_1,
        castle_location_names.a1_se_cache_2,
        castle_location_names.a1_se_cache_3,
        castle_location_names.a1_se_cache_4,
    ]
    a1_se_cache_region = create_region(world, active_locations, castle_region_names.a1_se_cache,
                                       a1_se_cache_locs)

    a1_e_ne_bgate_locs = [
        castle_location_names.a1_e_ne_bgate,
    ]
    a1_e_ne_bgate_region = create_region(world, active_locations, castle_region_names.a1_e_ne_bgate,
                                         a1_e_ne_bgate_locs)

    a1_red_spikes_locs = [
        castle_location_names.a1_red_spikes_1,
        castle_location_names.a1_red_spikes_2,
        castle_location_names.a1_red_spikes_3,
    ]
    a1_red_spikes_region = create_region(world, active_locations, castle_region_names.a1_red_spikes,
                                         a1_red_spikes_locs)

    a1_n_bgate_locs = [
        castle_location_names.a1_n_cache_1,
        castle_location_names.a1_n_cache_2,
        castle_location_names.a1_n_cache_3,
        castle_location_names.a1_n_cache_4,
        castle_location_names.a1_n_cache_5,
        castle_location_names.a1_n_cache_6,
        castle_location_names.a1_n_cache_7,
        castle_location_names.a1_n_cache_8,
        castle_location_names.a1_n_cache_9,
    ]
    a1_n_bgate_region = create_region(world, active_locations, castle_region_names.a1_n_bgate,
                                      a1_n_bgate_locs)

    a1_tp_n_locs = [
        castle_location_names.a1_n_tp,
    ]
    a1_tp_n_region = create_region(world, active_locations, castle_region_names.a1_tp_n, a1_tp_n_locs)

    a1_w_locs = [
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
        castle_location_names.ev_a1_boss_switch,
    ]
    a1_w_region = create_region(world, active_locations, castle_region_names.a1_w, a1_w_locs)

    a1_puzzle_locs = [
        castle_location_names.a1_puzzle_1,
        castle_location_names.a1_puzzle_2,
        castle_location_names.a1_puzzle_3,
        castle_location_names.a1_puzzle_4,
    ]
    a1_puzzle_region = create_region(world, active_locations, castle_region_names.a1_puzzle, a1_puzzle_locs)

    a1_w_ne_bgate_locs = []
    a1_w_ne_bgate_region = create_region(world, active_locations, castle_region_names.a1_w_ne_bgate,
                                         a1_w_ne_bgate_locs)

    a1_nw_bgate_locs = [
        castle_location_names.a1_nw_bgate
    ]
    a1_nw_bgate_region = create_region(world, active_locations, castle_region_names.a1_nw_bgate,
                                       a1_nw_bgate_locs)

    a1_w_se_bgate_locs = []
    a1_w_se_bgate_region = create_region(world, active_locations, castle_region_names.a1_w_se_bgate,
                                         a1_w_se_bgate_locs)

    a1_w_sw_bgate_locs = []
    a1_w_sw_bgate_region = create_region(world, active_locations, castle_region_names.a1_w_sw_bgate,
                                         a1_w_sw_bgate_locs)

    a1_w_sw_bgate_1_locs = []
    a1_w_sw_bgate_1_region = create_region(world, active_locations, castle_region_names.a1_w_sw_bgate_1,
                                           a1_w_sw_bgate_1_locs)

    a1_sw_spikes_locs = [
        castle_location_names.a1_sw_spikes
    ]
    a1_sw_spikes_region = create_region(world, active_locations, castle_region_names.a1_sw_spikes,
                                        a1_sw_spikes_locs)

    a1_from_a2_locs = [
        castle_location_names.a1_from_a2_1,
        castle_location_names.a1_from_a2_2,
        castle_location_names.a1_from_a2_3,
    ]
    a1_from_a2_region = create_region(world, active_locations, castle_region_names.a1_from_a2,
                                      a1_from_a2_locs)

    a2_start_locs = [
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
    ]
    a2_start_region = create_region(world, active_locations, castle_region_names.a2_start, a2_start_locs)

    a2_puzzle_locs = [
        castle_location_names.a2_puzzle_1,
        castle_location_names.a2_puzzle_2,
        castle_location_names.a2_puzzle_3,
        castle_location_names.a2_puzzle_4,
    ]
    a2_puzzle_region = create_region(world, active_locations, castle_region_names.a2_puzzle, a2_puzzle_locs)

    a2_tp_sw_locs = [
        castle_location_names.a2_sw_ice_tower_tp,
    ]
    a2_tp_sw_region = create_region(world, active_locations, castle_region_names.a2_tp_sw, a2_tp_sw_locs)

    a2_tp_se_locs = [
        castle_location_names.a2_se_tp,
    ]
    a2_tp_se_region = create_region(world, active_locations, castle_region_names.a2_tp_se, a2_tp_se_locs)

    a2_sw_bgate_locs = []
    a2_sw_bgate_region = create_region(world, active_locations, castle_region_names.a2_sw_bgate,
                                       a2_sw_bgate_locs)

    a2_s_bgate_locs = [
        castle_location_names.a2_s_bgate,
    ]
    a2_s_bgate_region = create_region(world, active_locations, castle_region_names.a2_s_bgate,
                                      a2_s_bgate_locs)

    a2_se_bgate_locs = []
    a2_se_bgate_region = create_region(world, active_locations, castle_region_names.a2_se_bgate,
                                       a2_se_bgate_locs)

    a2_s_save_bgate_locs = []
    a2_s_save_bgate_region = create_region(world, active_locations, castle_region_names.a2_s_save_bgate,
                                           a2_s_save_bgate_locs)

    a2_ne_locs = [
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
        castle_location_names.ev_a2_boss_switch,
        castle_location_names.btnc_a2_bspikes_tp,
    ]
    a2_ne_region = create_region(world, active_locations, castle_region_names.a2_ne, a2_ne_locs)

    a2_ne_m_bgate_locs = []
    a2_ne_m_bgate_region = create_region(world, active_locations, castle_region_names.a2_ne_m_bgate,
                                         a2_ne_m_bgate_locs)

    a2_ne_l_bgate_locs = [
        castle_location_names.a2_ne_l_bgate,
    ]
    a2_ne_l_bgate_region = create_region(world, active_locations, castle_region_names.a2_ne_l_bgate,
                                         a2_ne_l_bgate_locs)

    a2_ne_r_bgate_locs = [
        castle_location_names.a2_ne_r_bgate_1,
        castle_location_names.a2_ne_r_bgate_2,
    ]
    a2_ne_r_bgate_region = create_region(world, active_locations, castle_region_names.a2_ne_r_bgate,
                                         a2_ne_r_bgate_locs)

    a2_ne_b_bgate_locs = []
    a2_ne_b_bgate_region = create_region(world, active_locations, castle_region_names.a2_ne_b_bgate,
                                         a2_ne_b_bgate_locs)

    a2_ne_save_bgate_locs = []
    a2_ne_save_bgate_region = create_region(world, active_locations, castle_region_names.a2_ne_save_bgate,
                                            a2_ne_save_bgate_locs)

    a2_tp_ne_locs = [
        castle_location_names.a2_ne_tp,
    ]
    a2_tp_ne_region = create_region(world, active_locations, castle_region_names.a2_tp_ne, a2_tp_ne_locs)

    a2_e_locs = [
        castle_location_names.a2_e_ice_tower_1,
        castle_location_names.a2_e_ice_tower_2,
        castle_location_names.a2_e_ice_tower_3,
        castle_location_names.a2_e_ice_tower_4,
        castle_location_names.a2_e_ice_tower_5,
        castle_location_names.a2_e_ice_tower_6,
        castle_location_names.a2_s_of_e_bgate,
        castle_location_names.a2_tower_ice_6,
    ]
    a2_e_region = create_region(world, active_locations, castle_region_names.a2_e, a2_e_locs)

    a2_e_bgate_locs = [
        castle_location_names.a2_e_bgate,
    ]
    a2_e_bgate_region = create_region(world, active_locations, castle_region_names.a2_e_bgate,
                                      a2_e_bgate_locs)

    a2_nw_locs = [
        castle_location_names.a2_pyramid_1,
        castle_location_names.a2_pyramid_3,
        castle_location_names.a2_pyramid_4,
        castle_location_names.a2_nw_ice_tower,
        castle_location_names.a2_by_w_a1_stair,
        castle_location_names.a2_tower_ice_1,
    ]
    a2_nw_region = create_region(world, active_locations, castle_region_names.a2_nw, a2_nw_locs)

    a2_bonus_return_locs = [
        castle_location_names.a2_bonus_return,
    ]
    a2_bonus_return_region = create_region(world, active_locations, castle_region_names.a2_bonus_return,
                                           a2_bonus_return_locs)

    a2_blue_spikes_locs = [
        castle_location_names.a2_blue_spikes,
    ]
    a2_blue_spikes_region = create_region(world, active_locations, castle_region_names.a2_blue_spikes,
                                          a2_blue_spikes_locs)

    a2_blue_spikes_tp_locs = [
        castle_location_names.a2_nw_tp,
    ]
    a2_blue_spikes_tp_region = create_region(world, active_locations, castle_region_names.a2_blue_spikes_tp,
                                             a2_blue_spikes_tp_locs)

    a2_to_a3_locs = []
    a2_to_a3_region = create_region(world, active_locations, castle_region_names.a2_to_a3, a2_to_a3_locs)

    n2_start_locs = [
        castle_location_names.n2_start_1,
        castle_location_names.n2_start_2,
        castle_location_names.n2_start_3,
        castle_location_names.n2_start_4,
    ]
    n2_start_region = create_region(world, active_locations, castle_region_names.n2_start, n2_start_locs)

    n2_m_locs = [
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
    ]
    n2_m_region = create_region(world, active_locations, castle_region_names.n2_m, n2_m_locs)

    n2_nw_locs = [
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
        castle_location_names.btnc_n2_blue_spikes,
    ]
    n2_nw_region = create_region(world, active_locations, castle_region_names.n2_nw, n2_nw_locs)

    n2_w_locs = [
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
    ]
    n2_w_region = create_region(world, active_locations, castle_region_names.n2_w, n2_w_locs)

    n2_e_locs = [
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
    ]
    n2_e_region = create_region(world, active_locations, castle_region_names.n2_e, n2_e_locs)

    n2_n_locs = [
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
    ]
    n2_n_region = create_region(world, active_locations, castle_region_names.n2_n, n2_n_locs)

    n2_s_locs = [
        castle_location_names.n2_s_1,
        castle_location_names.n2_s_2,
        castle_location_names.n2_s_3,
        castle_location_names.n2_s_4,
        castle_location_names.n2_s_5,
        castle_location_names.n2_s_6,
        castle_location_names.n2_s_7,
        castle_location_names.n2_s_8,
        castle_location_names.n2_s_9,
    ]
    n2_s_region = create_region(world, active_locations, castle_region_names.n2_s, n2_s_locs)

    n2_ne_locs = [
        castle_location_names.n2_ne_1,
        castle_location_names.n2_ne_2,
        castle_location_names.n2_ne_3,
        castle_location_names.n2_ne_4,
    ]
    n2_ne_region = create_region(world, active_locations, castle_region_names.n2_ne, n2_ne_locs)

    n2_se_locs = [
    ]
    n2_se_region = create_region(world, active_locations, castle_region_names.n2_se, n2_se_locs)

    n2_exit_locs = [
    ]
    n2_exit_region = create_region(world, active_locations, castle_region_names.n2_exit, n2_exit_locs)

    a3_start_locs = [
        castle_location_names.a3_sw_1,
        castle_location_names.a3_sw_2,
        castle_location_names.a3_sw_3,
    ]
    a3_start_region = create_region(world, active_locations, castle_region_names.a3_start, a3_start_locs)

    a3_main_locs = [
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
        castle_location_names.a3_secret_shop,
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
        castle_location_names.ev_a3_boss_switch,
    ]
    a3_main_region = create_region(world, active_locations, castle_region_names.a3_main, a3_main_locs)

    a3_tp_locs = [
        castle_location_names.a3_m_tp,
    ]
    a3_tp_region = create_region(world, active_locations, castle_region_names.a3_tp, a3_tp_locs)

    a3_from_a2_locs = [
        # Bgate teleport button
    ]
    a3_from_a2_region = create_region(world, active_locations, castle_region_names.a3_from_a2,
                                      a3_from_a2_locs)

    a3_knife_puzzle_reward_locs = [
        castle_location_names.a3_knife_puzzle_reward_l_5,
        castle_location_names.a3_knife_puzzle_reward_r,
    ]
    a3_knife_puzzle_reward_region = create_region(world, active_locations,
                                                  castle_region_names.a3_knife_puzzle_reward, a3_knife_puzzle_reward_locs)

    a3_knife_reward_2_locs = [
        castle_location_names.a3_knife_puzzle_reward_l_1,
        castle_location_names.a3_knife_puzzle_reward_l_2,
        castle_location_names.a3_knife_puzzle_reward_l_3,
        castle_location_names.a3_knife_puzzle_reward_l_4,
    ]
    a3_knife_reward_2_region = create_region(world, active_locations, castle_region_names.a3_knife_reward_2,
                                             a3_knife_reward_2_locs)

    a3_nw_stairs_region = create_region(world, active_locations, castle_region_names.a3_nw_stairs, [])

    a3_w_b_bgate_locs = [
        castle_location_names.a3_pyramids_s_bgate_tp
    ]
    a3_w_b_bgate_region = create_region(world, active_locations, castle_region_names.a3_w_b_bgate,
                                        a3_w_b_bgate_locs)

    a3_w_t_bgate_locs = []
    a3_w_t_bgate_region = create_region(world, active_locations, castle_region_names.a3_w_t_bgate,
                                        a3_w_t_bgate_locs)

    a3_w_r_bgate_locs = []
    a3_w_r_bgate_region = create_region(world, active_locations, castle_region_names.a3_w_r_bgate,
                                        a3_w_r_bgate_locs)

    a3_n_l_bgate_locs = []
    a3_n_l_bgate_region = create_region(world, active_locations, castle_region_names.a3_n_l_bgate,
                                        a3_n_l_bgate_locs)

    a3_n_r_bgate_locs = []
    a3_n_r_bgate_region = create_region(world, active_locations, castle_region_names.a3_n_r_bgate,
                                        a3_n_r_bgate_locs)

    a3_e_l_bgate_locs = []
    a3_e_l_bgate_region = create_region(world, active_locations, castle_region_names.a3_e_l_bgate,
                                        a3_e_l_bgate_locs)

    a3_e_r_bgate_locs = []
    a3_e_r_bgate_region = create_region(world, active_locations, castle_region_names.a3_e_r_bgate,
                                        a3_e_r_bgate_locs)

    b2_start_locs = [
    ]
    b2_start_region = create_region(world, active_locations, castle_region_names.b2_start, b2_start_locs)

    b2_arena_locs = [
    ]
    b2_arena_region = create_region(world, active_locations, castle_region_names.b2_arena, b2_arena_locs)

    b2_defeated_locs = [
        castle_location_names.b2_boss,
        castle_location_names.b2_boss_reward,
        castle_location_names.ev_beat_boss_2,
    ]
    b2_defeated_region = create_region(world, active_locations, castle_region_names.b2_defeated,
                                       b2_defeated_locs)

    b2_exit_locs = [
    ]
    b2_exit_region = create_region(world, active_locations, castle_region_names.b2_exit, b2_exit_locs)

    r1_start_locs = [
        castle_location_names.r1_se_1,
        castle_location_names.r1_se_2,
        castle_location_names.r1_se_3,
        castle_location_names.r1_se_4,
        castle_location_names.r1_se_5,
        castle_location_names.r1_se_6,
    ]
    r1_start_region = create_region(world, active_locations, castle_region_names.r1_start, r1_start_locs)

    r1_se_ggate_locs = []
    r1_se_ggate_region = create_region(world, active_locations, castle_region_names.r1_se_ggate,
                                       r1_se_ggate_locs)

    r1_start_wall_locs = [
        castle_location_names.r1_start_wall
    ]
    r1_start_wall_region = create_region(world, active_locations, castle_region_names.r1_start_wall,
                                         r1_start_wall_locs)

    r1_e_locs = [
        castle_location_names.r1_e_knife_trap_1,
        castle_location_names.r1_e_knife_trap_2,
        castle_location_names.r1_e_knife_trap_3,
        castle_location_names.r1_e_knife_trap_4,
        castle_location_names.r1_e_knife_trap_5,
        castle_location_names.r1_e_knife_trap_6,
        castle_location_names.r1_e_knife_trap_7,
        castle_location_names.r1_e_s,
    ]
    r1_e_region = create_region(world, active_locations, castle_region_names.r1_e, r1_e_locs)

    r1_e_s_bgate_locs = [
        castle_location_names.r1_e_s_bgate
    ]
    r1_e_s_bgate_region = create_region(world, active_locations, castle_region_names.r1_e_s_bgate,
                                        r1_e_s_bgate_locs)

    r1_e_n_bgate_locs = [
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
    ]
    r1_e_n_bgate_region = create_region(world, active_locations, castle_region_names.r1_e_n_bgate,
                                        r1_e_n_bgate_locs)

    r1_e_sgate_locs = [
        castle_location_names.r1_e_sgate
    ]
    r1_e_sgate_region = create_region(world, active_locations, castle_region_names.r1_e_sgate,
                                      r1_e_sgate_locs)

    r1_se_wall_locs = [
        castle_location_names.r1_se_wall
    ]
    r1_se_wall_region = create_region(world, active_locations, castle_region_names.r1_se_wall,
                                      r1_se_wall_locs)

    r1_ne_ggate_locs = [
        castle_location_names.r1_ne_ggate_1,
        castle_location_names.r1_ne_ggate_2,
        castle_location_names.r1_ne_ggate_3,
        castle_location_names.r1_ne_ggate_4,
    ]
    r1_ne_ggate_region = create_region(world, active_locations, castle_region_names.r1_ne_ggate,
                                       r1_ne_ggate_locs)

    r1_nw_locs = [
        castle_location_names.r1_nw_1,
        castle_location_names.r1_nw_2,
        castle_location_names.r1_puzzle_1,
        castle_location_names.r1_puzzle_2,
        castle_location_names.r1_puzzle_3,
        castle_location_names.r1_puzzle_4,
        castle_location_names.r1_tower_plant_1,
    ]
    r1_nw_region = create_region(world, active_locations, castle_region_names.r1_nw, r1_nw_locs)

    r1_nw_hidden_locs = [
        castle_location_names.r1_nw_hidden_1,
        castle_location_names.r1_nw_hidden_2,
    ]
    r1_nw_hidden_region = create_region(world, active_locations, castle_region_names.r1_nw_hidden,
                                        r1_nw_hidden_locs)

    r1_nw_ggate_locs = []
    r1_nw_ggate_region = create_region(world, active_locations, castle_region_names.r1_nw_ggate,
                                       r1_nw_ggate_locs)

    r1_sw_locs = [
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
    ]
    r1_sw_region = create_region(world, active_locations, castle_region_names.r1_sw, r1_sw_locs)

    r1_w_sgate_locs = [  # Shop region
    ]
    r1_w_sgate_region = create_region(world, active_locations, castle_region_names.r1_w_sgate,
                                      r1_w_sgate_locs)

    r1_sw_ggate_locs = []
    r1_sw_ggate_region = create_region(world, active_locations, castle_region_names.r1_sw_ggate,
                                       r1_sw_ggate_locs)

    r1_exit_l_locs = []
    r1_exit_l_region = create_region(world, active_locations, castle_region_names.r1_exit_l, r1_exit_l_locs)

    r1_exit_r_locs = []
    r1_exit_r_region = create_region(world, active_locations, castle_region_names.r1_exit_r, r1_exit_r_locs)

    r2_start_locs = [
        castle_location_names.r2_start
    ]
    r2_start_region = create_region(world, active_locations, castle_region_names.r2_start, r2_start_locs)

    r2_bswitch_locs = [
        castle_location_names.ev_r1_boss_switch
    ]
    r2_bswitch_region = create_region(world, active_locations, castle_region_names.r2_bswitch,
                                      r2_bswitch_locs)

    r2_m_locs = [
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
    ]
    r2_m_region = create_region(world, active_locations, castle_region_names.r2_m, r2_m_locs)

    r2_nw_locs = [
        castle_location_names.r2_nw_spike_trap_1,
        castle_location_names.r2_nw_spike_trap_2,
        castle_location_names.r2_tower_plant_1,
    ]
    r2_nw_region = create_region(world, active_locations, castle_region_names.r2_nw, r2_nw_locs)

    r2_n_locs = [
        castle_location_names.r2_n_closed_room,
        castle_location_names.ev_r2_boss_switch,
    ]
    r2_n_region = create_region(world, active_locations, castle_region_names.r2_n, r2_n_locs)

    r2_e_locs = [
        castle_location_names.r2_e_1,
        castle_location_names.r2_e_2,
        castle_location_names.r2_e_3,
        castle_location_names.r2_e_4,
        castle_location_names.r2_e_5,
    ]
    r2_e_region = create_region(world, active_locations, castle_region_names.r2_e, r2_e_locs)

    r2_w_bgate_locs = []
    r2_w_bgate_region = create_region(world, active_locations, castle_region_names.r2_w_bgate,
                                      r2_w_bgate_locs)

    r2_sgate_locs = []
    r2_sgate_region = create_region(world, active_locations, castle_region_names.r2_sgate, r2_sgate_locs)

    r2_s_locs = [
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
    ]
    r2_s_region = create_region(world, active_locations, castle_region_names.r2_s, r2_s_locs)

    r2_spike_island_locs = [
        castle_location_names.r2_s_knife_trap_1,
        castle_location_names.r2_s_knife_trap_2,
        castle_location_names.r2_s_knife_trap_3,
        castle_location_names.r2_s_knife_trap_4,
        castle_location_names.r2_s_knife_trap_5,
    ]
    r2_spike_island_region = create_region(world, active_locations, castle_region_names.r2_spike_island,
                                           r2_spike_island_locs)

    r2_sw_bridge_locs = []
    r2_sw_bridge_region = create_region(world, active_locations, castle_region_names.r2_sw_bridge,
                                        r2_sw_bridge_locs)

    r2_puzzle_locs = [
        castle_location_names.r2_puzzle_1,
        castle_location_names.r2_puzzle_2,
        castle_location_names.r2_puzzle_3,
        castle_location_names.r2_puzzle_4,
    ]
    r2_puzzle_region = create_region(world, active_locations, castle_region_names.r2_puzzle, r2_puzzle_locs)

    r2_w_locs = [
        castle_location_names.r2_w_island,
    ]
    r2_w_region = create_region(world, active_locations, castle_region_names.r2_w, r2_w_locs)

    r2_from_r3_locs = [
        castle_location_names.r2_ne_knife_trap_end,
    ]
    r2_from_r3_region = create_region(world, active_locations, castle_region_names.r2_from_r3,
                                      r2_from_r3_locs)

    r2_ne_cache_locs = [
        castle_location_names.r2_ne_knife_trap_wall_1,
        castle_location_names.r2_ne_knife_trap_wall_2,
        castle_location_names.r2_ne_knife_trap_wall_3,
    ]
    r2_ne_cache_region = create_region(world, active_locations, castle_region_names.r2_ne_cache,
                                       r2_ne_cache_locs)

    r2_ggate_locs = []
    r2_ggate_region = create_region(world, active_locations, castle_region_names.r2_ggate, r2_ggate_locs)

    r3_main_locs = [
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
        castle_location_names.ev_r3_boss_switch,
    ]
    r3_main_region = create_region(world, active_locations, castle_region_names.r3_main, r3_main_locs)

    r3_ne_room_locs = [
        castle_location_names.r3_e_secret_tp,
        castle_location_names.r3_e_tp,
    ]
    r3_ne_room_region = create_region(world, active_locations, castle_region_names.r3_ne_room,
                                      r3_ne_room_locs)

    r3_s_room_locs = [
        castle_location_names.r3_s_shops_room_1,
        castle_location_names.r3_s_shops_room_2,
    ]
    r3_s_room_region = create_region(world, active_locations, castle_region_names.r3_s_room, r3_s_room_locs)

    r3_w_ggate_locs = [
        castle_location_names.r3_s_of_boss_door_1,
        castle_location_names.r3_s_of_boss_door_2,
        castle_location_names.r3_tower_plant_5,
    ]
    r3_w_ggate_region = create_region(world, active_locations, castle_region_names.r3_w_ggate,
                                      r3_w_ggate_locs)

    r3_e_ggate_locs = [
        castle_location_names.r3_e_ggate_hallway_1,
        castle_location_names.r3_e_ggate_hallway_2,
        castle_location_names.r3_e_ggate_hallway_3,
        castle_location_names.r3_tower_plant_3,
    ]
    r3_e_ggate_region = create_region(world, active_locations, castle_region_names.r3_e_ggate,
                                      r3_e_ggate_locs)

    r3_sw_bgate_locs = [
    ]
    r3_sw_bgate_region = create_region(world, active_locations, castle_region_names.r3_sw_bgate,
                                       r3_sw_bgate_locs)

    r3_sw_wall_r_locs = [
        castle_location_names.r3_sw_hidden_room_1,
        castle_location_names.r3_sw_hidden_room_2,
    ]
    r3_sw_wall_r_region = create_region(world, active_locations, castle_region_names.r3_sw_wall_r,
                                        r3_sw_wall_r_locs)

    r3_sw_wall_l_locs = [
        castle_location_names.r3_w_passage_behind_spikes,
        castle_location_names.r3_w_passage_s_closed_room,
    ]
    r3_sw_wall_l_region = create_region(world, active_locations, castle_region_names.r3_sw_wall_l,
                                        r3_sw_wall_l_locs)

    r3_nw_tp_locs = [
        castle_location_names.r3_nw_tp,
    ]
    r3_nw_tp_region = create_region(world, active_locations, castle_region_names.r3_nw_tp, r3_nw_tp_locs)

    r3_se_cache_locs = [
        castle_location_names.r3_e_fire_floor_secret,
    ]
    r3_se_cache_region = create_region(world, active_locations, castle_region_names.r3_se_cache,
                                       r3_se_cache_locs)

    r3_boss_switch_locs = [
        castle_location_names.r3_boss_switch_room_1,
        castle_location_names.r3_boss_switch_room_2,
        castle_location_names.r3_boss_switch_room_3,
    ]
    r3_boss_switch_region = create_region(world, active_locations, castle_region_names.r3_boss_switch,
                                          r3_boss_switch_locs)

    r3_rune_room_locs = []
    r3_rune_room_region = create_region(world, active_locations, castle_region_names.r3_rune_room,
                                        r3_rune_room_locs)

    r3_bonus_locs = []
    r3_bonus_region = create_region(world, active_locations, castle_region_names.r3_bonus, r3_bonus_locs)

    r3_l_shop_sgate_locs = [
        castle_location_names.r3_s_shops_room_left_shop,
    ]
    r3_l_shop_sgate_region = create_region(world, active_locations, castle_region_names.r3_l_shop_sgate,
                                           r3_l_shop_sgate_locs)

    r3_r_shop_sgate_locs = []
    r3_r_shop_sgate_region = create_region(world, active_locations, castle_region_names.r3_r_shop_sgate,
                                           r3_r_shop_sgate_locs)

    r3_bonus_return_locs = [
        castle_location_names.r3_bonus_return_1,
        castle_location_names.r3_bonus_return_2,
    ]
    r3_bonus_return_region = create_region(world, active_locations, castle_region_names.r3_bonus_return,
                                           r3_bonus_return_locs)

    r3_bonus_return_bridge_locs = [
        castle_location_names.r3_e_shops_puzzle_reward,
    ]
    r3_bonus_return_bridge_region = create_region(world, active_locations,
                                                  castle_region_names.r3_bonus_return_bridge, r3_bonus_return_bridge_locs)

    r3_exit_locs = []
    r3_exit_region = create_region(world, active_locations, castle_region_names.r3_exit, r3_exit_locs)

    n3_main_locs = [
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
    ]
    n3_main_region = create_region(world, active_locations, castle_region_names.n3_main, n3_main_locs)

    n3_tp_room_locs = [
        castle_location_names.n3_tp_room,
    ]
    n3_tp_room_region = create_region(world, active_locations, castle_region_names.n3_tp_room,
                                      n3_tp_room_locs)

    b3_start_locs = [
    ]
    b3_start_region = create_region(world, active_locations, castle_region_names.b3_start, b3_start_locs)

    b3_arena_locs = [
    ]
    b3_arena_region = create_region(world, active_locations, castle_region_names.b3_arena, b3_arena_locs)

    b3_defeated_locs = [
        castle_location_names.b3_boss,
        castle_location_names.b3_reward,
        castle_location_names.ev_beat_boss_3,
    ]
    b3_defeated_region = create_region(world, active_locations, castle_region_names.b3_defeated,
                                       b3_defeated_locs)

    b3_exit_locs = [
    ]
    b3_exit_region = create_region(world, active_locations, castle_region_names.b3_exit, b3_exit_locs)

    c1_start_locs = [
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
        castle_location_names.c1_tower_ice_1,
        castle_location_names.c1_tower_ice_2,
        castle_location_names.c1_tower_ice_3,
    ]
    c1_start_region = create_region(world, active_locations, castle_region_names.c1_start, c1_start_locs)

    c1_se_spikes_locs = [
        castle_location_names.c1_se_spikes
    ]
    c1_se_spikes_region = create_region(world, active_locations, castle_region_names.c1_se_spikes,
                                        c1_se_spikes_locs)

    c1_n_spikes_locs = [
        castle_location_names.c1_n_spikes_1,
        castle_location_names.c1_n_spikes_2,
    ]
    c1_n_spikes_region = create_region(world, active_locations, castle_region_names.c1_n_spikes,
                                       c1_n_spikes_locs)
    # Obviously a shop region
    c1_shop_locs = [
    ]
    c1_shop_region = create_region(world, active_locations, castle_region_names.c1_shop, c1_shop_locs)

    c1_w_locs = [
        castle_location_names.c1_w_1,
        castle_location_names.c1_w_2,
        castle_location_names.c1_w_3,
        castle_location_names.c1_miniboss_lich_1,
        castle_location_names.c1_miniboss_lich_2,
        castle_location_names.c1_tower_plant_2,
    ]
    c1_w_region = create_region(world, active_locations, castle_region_names.c1_w, c1_w_locs)

    c1_sgate_locs = [
        castle_location_names.c1_sgate
    ]
    c1_sgate_region = create_region(world, active_locations, castle_region_names.c1_sgate, c1_sgate_locs)

    c1_prison_stairs_locs = [
        castle_location_names.c1_prison_stairs
    ]
    c1_prison_stairs_region = create_region(world, active_locations, castle_region_names.c1_prison_stairs,
                                            c1_prison_stairs_locs)
    # Symbolic region containing the button to open the shortcut to the east area
    c1_s_bgate_locs = [
    ]
    c1_s_bgate_region = create_region(world, active_locations, castle_region_names.c1_s_bgate,
                                      c1_s_bgate_locs)

    c1_ledge_locs = [
        castle_location_names.c1_ledge_1,
        castle_location_names.c1_ledge_2,
    ]
    c1_ledge_region = create_region(world, active_locations, castle_region_names.c1_ledge, c1_ledge_locs)

    c1_tp_island_locs = [
        castle_location_names.c1_tp_island_1,
        castle_location_names.c1_tp_island_2,
    ]
    c1_tp_island_region = create_region(world, active_locations, castle_region_names.c1_tp_island,
                                        c1_tp_island_locs)

    pstart_start_locs = [
    ]
    pstart_start_region = create_region(world, active_locations, castle_region_names.pstart_start,
                                        pstart_start_locs)

    pstart_puzzle_locs = [
        castle_location_names.pstart_puzzle_1,
        castle_location_names.pstart_puzzle_2,
        castle_location_names.pstart_puzzle_3,
        castle_location_names.pstart_puzzle_4,
    ]
    pstart_puzzle_region = create_region(world, active_locations, castle_region_names.pstart_puzzle,
                                         pstart_puzzle_locs)

    c2_main_locs = [
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
        castle_location_names.ev_c2_boss_switch
    ]
    c2_main_region = create_region(world, active_locations, castle_region_names.c2_main, c2_main_locs)

    c2_exit_bgate_locs = [
        castle_location_names.btnc_c2_n_open_wall,
    ]
    c2_exit_bgate_region = create_region(world, active_locations, castle_region_names.c2_exit_bgate,
                                         c2_exit_bgate_locs)

    c2_sw_wall_locs = [
        castle_location_names.c2_sw_ice_tower_6,
    ]
    c2_sw_wall_region = create_region(world, active_locations, castle_region_names.c2_sw_wall,
                                      c2_sw_wall_locs)

    c2_w_wall_locs = [
        castle_location_names.c2_w_save_wall,
    ]
    c2_w_wall_region = create_region(world, active_locations, castle_region_names.c2_w_wall, c2_w_wall_locs)

    c2_e_wall_locs = [
        castle_location_names.c2_by_e_shops_2,
    ]
    c2_e_wall_region = create_region(world, active_locations, castle_region_names.c2_e_wall, c2_e_wall_locs)

    c2_w_spikes_locs = [
        castle_location_names.c2_w_spikes_1,
        castle_location_names.c2_w_spikes_2,
        castle_location_names.c2_w_spikes_3,
        castle_location_names.c2_w_spikes_4,
    ]
    c2_w_spikes_region = create_region(world, active_locations, castle_region_names.c2_w_spikes,
                                       c2_w_spikes_locs)

    c2_w_shops_1_locs = [
        castle_location_names.c2_by_w_shops_1
    ]
    c2_w_shops_1_region = create_region(world, active_locations, castle_region_names.c2_w_shops_1,
                                        c2_w_shops_1_locs)

    c2_w_shops_2_locs = [
        castle_location_names.c2_by_w_shops_2
    ]
    c2_w_shops_2_region = create_region(world, active_locations, castle_region_names.c2_w_shops_2,
                                        c2_w_shops_2_locs)

    c2_w_shops_3_locs = [
        castle_location_names.c2_by_w_shops_3_1,
        castle_location_names.c2_by_w_shops_3_2,
    ]
    c2_w_shops_3_region = create_region(world, active_locations, castle_region_names.c2_w_shops_3,
                                        c2_w_shops_3_locs)

    c2_e_shops_1_locs = []
    c2_e_shops_1_region = create_region(world, active_locations, castle_region_names.c2_e_shops_1,
                                        c2_e_shops_1_locs)

    c2_e_shops_2_locs = []
    c2_e_shops_2_region = create_region(world, active_locations, castle_region_names.c2_e_shops_2,
                                        c2_e_shops_2_locs)

    c2_puzzle_locs = [
        castle_location_names.c2_puzzle_1,
        castle_location_names.c2_puzzle_2,
        castle_location_names.c2_puzzle_3,
        castle_location_names.c2_puzzle_4,
    ]
    c2_puzzle_region = create_region(world, active_locations, castle_region_names.c2_puzzle, c2_puzzle_locs)

    c2_n_locs = [
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
    ]
    c2_n_region = create_region(world, active_locations, castle_region_names.c2_n, c2_n_locs)

    c2_n_wall_locs = [
        castle_location_names.c2_n_wall
    ]
    c2_n_wall_region = create_region(world, active_locations, castle_region_names.c2_n_wall, c2_n_wall_locs)

    c2_bonus_locs = []
    c2_bonus_region = create_region(world, active_locations, castle_region_names.c2_bonus, c2_bonus_locs)

    c2_bonus_return_locs = [
        castle_location_names.c2_bonus_return
    ]
    c2_bonus_return_region = create_region(world, active_locations, castle_region_names.c2_bonus_return,
                                           c2_bonus_return_locs)

    c2_tp_island_locs = [
        castle_location_names.ev_c1_boss_switch
    ]
    c2_tp_island_region = create_region(world, active_locations, castle_region_names.c2_tp_island,
                                        c2_tp_island_locs)

    c2_c3_tp_locs = [
        castle_location_names.ev_c2_n_shops_switch
    ]
    c2_c3_tp_region = create_region(world, active_locations, castle_region_names.c2_c3_tp, c2_c3_tp_locs)

    c2_n_shops_locs = [
    ]
    c2_n_shops_region = create_region(world, active_locations, castle_region_names.c2_n_shops,
                                      c2_n_shops_locs)

    n4_main_locs = [
        castle_location_names.n4_ne,
        castle_location_names.n4_by_w_room_1,
        castle_location_names.n4_by_exit,
        castle_location_names.n4_by_w_room_2,
    ]
    n4_main_region = create_region(world, active_locations, castle_region_names.n4_main, n4_main_locs)

    n4_nw_locs = [
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
    ]
    n4_nw_region = create_region(world, active_locations, castle_region_names.n4_nw, n4_nw_locs)

    n4_w_locs = [
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
    ]
    n4_w_region = create_region(world, active_locations, castle_region_names.n4_w, n4_w_locs)

    n4_e_locs = [
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
    ]
    n4_e_region = create_region(world, active_locations, castle_region_names.n4_e, n4_e_locs)

    c3_main_locs = [
        castle_location_names.c3_start_e
    ]
    c3_main_region = create_region(world, active_locations, castle_region_names.c3_start, c3_main_locs)

    c3_rspike_switch_locs = [
        castle_location_names.ev_c3_rspikes_switch
    ]
    c3_rspike_switch_region = create_region(world, active_locations, castle_region_names.c3_rspike_switch,
                                            c3_rspike_switch_locs)

    c3_rspikes_locs = [
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
        castle_location_names.ev_c3_sw_hidden_switch_3,
        castle_location_names.ev_c3_sw_hidden_switch_4,
        castle_location_names.ev_c3_sw_hidden_switch_5,
        castle_location_names.ev_c3_sw_hidden_switch_6,
    ]
    c3_rspikes_region = create_region(world, active_locations, castle_region_names.c3_rspikes,
                                      c3_rspikes_locs)

    c3_m_wall_locs = [
        castle_location_names.c3_m_wall
    ]
    c3_m_wall_region = create_region(world, active_locations, castle_region_names.c3_m_wall, c3_m_wall_locs)

    c3_m_shop_locs = []
    c3_m_shop_region = create_region(world, active_locations, castle_region_names.c3_m_shop, c3_m_shop_locs)

    c3_m_tp_locs = [
        castle_location_names.c3_m_tp
    ]
    c3_m_tp_region = create_region(world, active_locations, castle_region_names.c3_m_tp, c3_m_tp_locs)

    c3_s_bgate_locs = [
        castle_location_names.c3_s_bgate
    ]
    c3_s_bgate_region = create_region(world, active_locations, castle_region_names.c3_s_bgate,
                                      c3_s_bgate_locs)

    c3_nw_locs = [
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
        castle_location_names.ev_c3_sw_hidden_switch_1,
        castle_location_names.ev_c3_sw_hidden_switch_2,
        castle_location_names.ev_c3_boss_switch
    ]
    c3_nw_region = create_region(world, active_locations, castle_region_names.c3_nw, c3_nw_locs)

    c3_sw_hidden_locs = [
        castle_location_names.c3_sw_hidden
    ]
    c3_sw_hidden_region = create_region(world, active_locations, castle_region_names.c3_sw_hidden,
                                        c3_sw_hidden_locs)

    c3_se_hidden_locs = []
    c3_se_hidden_region = create_region(world, active_locations, castle_region_names.c3_se_hidden,
                                        c3_se_hidden_locs)

    c3_light_bridge_locs = [
        castle_location_names.c3_light_bridge_1,
        castle_location_names.c3_light_bridge_2,
        castle_location_names.c3_light_bridge_3,
        castle_location_names.c3_easter_egg,
    ]
    c3_light_bridge_region = create_region(world, active_locations, castle_region_names.c3_light_bridge,
                                           c3_light_bridge_locs)

    c3_fire_floor_locs = [
        castle_location_names.c3_fire_floor_1,
        castle_location_names.c3_fire_floor_2,
        castle_location_names.c3_fire_floor_3,
    ]
    c3_fire_floor_region = create_region(world, active_locations, castle_region_names.c3_fire_floor,
                                         c3_fire_floor_locs)

    c3_fire_floor_tp_locs = [
        castle_location_names.c3_fire_floor_tp
    ]
    c3_fire_floor_tp_region = create_region(world, active_locations, castle_region_names.c3_fire_floor_tp,
                                            c3_fire_floor_tp_locs)

    c3_c2_tp_locs = [
        castle_location_names.c3_c2_tp
    ]
    c3_c2_tp_region = create_region(world, active_locations, castle_region_names.c3_c2_tp, c3_c2_tp_locs)

    b4_start_locs = [
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
    ]
    b4_start_region = create_region(world, active_locations, castle_region_names.b4_start, b4_start_locs)

    b4_defeated_locations = [
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
    ]
    b4_defeated_region = create_region(world, active_locations, castle_region_names.b4_defeated,
                                       b4_defeated_locations)

    e1_main_locations = []
    e1_main_region = create_region(world, active_locations, castle_region_names.e1_main, e1_main_locations)

    e2_main_locations = [
        castle_location_names.e2_entrance,
        castle_location_names.e2_end,
    ]
    e2_main_region = create_region(world, active_locations, castle_region_names.e2_main, e2_main_locations)

    e3_main_locations = [
        castle_location_names.e3_entrance_1,
        castle_location_names.e3_entrance_2,
    ]
    e3_main_region = create_region(world, active_locations, castle_region_names.e3_main, e3_main_locations)

    e4_main_locations = [
        castle_location_names.e4_main,
    ]
    e4_main_region = create_region(world, active_locations, castle_region_names.e4_main, e4_main_locations)

    escaped_locations = [
        castle_location_names.ev_escape,
    ]
    escaped_region = create_region(world, active_locations, castle_region_names.escaped, escaped_locations)

    world.multiworld.regions += [
        menu_region,
        hub_region,
        p1_start_region,
        p1_nw_region,
        p1_nw_left_region,
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
        a3_nw_stairs_region,
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
    ]


def connect_castle_regions(world: "HammerwatchWorld", random_locations: typing.Dict[str, int],
                           gate_codes: typing.Dict[str, str]):
    used_names: typing.Dict[str, int] = {}
    gate_counts: typing.Dict[str, int] = {
        item_name.key_bronze: 0,
        item_name.key_silver: 0,
        item_name.key_gold: 0,
    }
    prison_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_prison: 0,
        item_name.key_silver_prison: 0,
        item_name.key_gold_prison: 0,
    }
    armory_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_armory: 0,
        item_name.key_silver_armory: 0,
        item_name.key_gold_armory: 0,
    }
    archives_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_archives: 0,
        item_name.key_silver_archives: 0,
        item_name.key_gold_archives: 0,
    }
    chambers_gate_items: typing.Dict[str, int] = {
        item_name.key_bronze_chambers: 0,
        item_name.key_silver_chambers: 0,
        item_name.key_gold_chambers: 0,
    }

    if world.options.act_specific_keys.value:
        key_bronze_prison = item_name.key_bronze_prison
        key_silver_prison = item_name.key_silver_prison
        key_gold_prison = item_name.key_gold_prison
        key_bonus_prison = item_name.key_bonus_prison

        key_bronze_armory = item_name.key_bronze_armory
        key_silver_armory = item_name.key_silver_armory
        key_gold_armory = item_name.key_gold_armory
        key_bonus_armory = item_name.key_bonus_armory

        key_bronze_archives = item_name.key_bronze_archives
        key_silver_archives = item_name.key_silver_archives
        key_gold_archives = item_name.key_gold_archives
        key_bonus_archives = item_name.key_bonus_archives

        key_bronze_chambers = item_name.key_bronze_chambers
        key_silver_chambers = item_name.key_silver_chambers
        key_gold_chambers = item_name.key_gold_chambers
        key_bonus_chambers = item_name.key_bonus_chambers

        if not world.options.randomize_bonus_keys.value:
            key_bonus_prison = item_name.key_bonus
            key_bonus_armory = item_name.key_bonus
            key_bonus_archives = item_name.key_bonus
            key_bonus_chambers = item_name.key_bonus
    else:
        key_bronze_prison = item_name.key_bronze
        key_silver_prison = item_name.key_silver
        key_gold_prison = item_name.key_gold
        key_bonus_prison = item_name.key_bonus

        key_bronze_armory = item_name.key_bronze
        key_silver_armory = item_name.key_silver
        key_gold_armory = item_name.key_gold
        key_bonus_armory = item_name.key_bonus

        key_bronze_archives = item_name.key_bronze
        key_silver_archives = item_name.key_silver
        key_gold_archives = item_name.key_gold
        key_bonus_archives = item_name.key_bonus

        key_bronze_chambers = item_name.key_bronze
        key_silver_chambers = item_name.key_silver
        key_gold_chambers = item_name.key_gold
        key_bonus_chambers = item_name.key_bonus

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

    # If not doing entrance randomization or randomizing the start we start in the normal spot
    if not world.options.exit_randomization.value or not world.options.random_start_exit.value:
        connect(world, used_names, castle_region_names.menu, castle_region_names.p1_start, False)
    connect(world, used_names, castle_region_names.p1_start, castle_region_names.hub, True)

    if world.options.open_castle.value:
        connect(world, used_names, castle_region_names.hub, castle_region_names.a1_start, True)
        connect(world, used_names, castle_region_names.hub, castle_region_names.r1_start, True)
        connect(world, used_names, castle_region_names.hub, castle_region_names.c1_start, True)

    connect(world, used_names, castle_region_names.p1_start, castle_region_names.p1_nw,
            True, item_name.btnc_p1_floor, 1, False)
    connect(world, used_names, castle_region_names.p1_nw, castle_region_names.p1_nw_left, False)
    connect_gate(world, used_names, castle_region_names.p1_start, castle_region_names.p1_s,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p1_0, True)
    connect_gate(world, used_names, castle_region_names.p1_s, castle_region_names.p1_sw_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p1_3, False)
    connect_gate(world, used_names, castle_region_names.p1_s, castle_region_names.p1_e,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p1_2, True)
    connect_gate(world, used_names, castle_region_names.p1_e, castle_region_names.p1_m_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p1_1, False)
    connect_exit(world, used_names, castle_region_names.p1_e, castle_region_names.p2_start,
                 entrance_names.c_p2_0, entrance_names.c_p1_1)
    if world.options.shortcut_teleporter.value:
        connect_exit(world, used_names, castle_region_names.p1_nw_left, castle_region_names.p3_portal_from_p1,
                     entrance_names.c_p3_portal, entrance_names.c_p1_20)
        connect(world, used_names, castle_region_names.p3_portal_from_p1, castle_region_names.p3_n_gold_gate,
                False)

    connect_gate(world, used_names, castle_region_names.p2_start, castle_region_names.p2_m,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p2_0, True)
    connect_exit(world, used_names, castle_region_names.p2_m, castle_region_names.p1_from_p2,
                 entrance_names.c_p1_2, entrance_names.c_p2_1)
    connect_exit(world, used_names, castle_region_names.p1_from_p2, castle_region_names.p2_p1_return,
                 entrance_names.c_p2_2, entrance_names.c_p1_3)
    # connect_generic(multiworld, player, used_names, castle_region_names.p2_p1_return, castle_region_names.p2_m)
    # Requires return wall button
    connect_gate(world, used_names, castle_region_names.p2_m, castle_region_names.p2_n,
                 key_silver_prison, gate_codes, prison_gate_items, gate_names.c_p2_5, True)
    connect(world, used_names, castle_region_names.p2_n, castle_region_names.p2_spike_puzzle_bottom, False)
    # Requires spike button 5
    connect(world, used_names, castle_region_names.p2_n, castle_region_names.p2_spike_puzzle_top, False)
    # Requires spike buttons (4, 5, 9) or (5, 7, 6)
    connect(world, used_names, castle_region_names.p2_n, castle_region_names.p2_spike_puzzle_left, False)
    # Requires spike buttons (4, 5, 9) or (5, 7, 6, 1 ,9)
    connect(world, used_names, castle_region_names.p2_n, castle_region_names.p2_red_switch, False)
    # Requires red spike button, also two-way
    connect(world, used_names, castle_region_names.p2_red_switch, castle_region_names.p2_puzzle, False)
    # Requires puzzle button
    connect_gate(world, used_names, castle_region_names.p2_red_switch, castle_region_names.p2_e_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p2_1, False)
    connect(world, used_names, castle_region_names.p2_red_switch, castle_region_names.p2_e_save, False)
    # Requires east save button, also two-way
    # connect_generic(multiworld, player, used_names, castle_region_names.p2_m, castle_region_names.p2_e_save)
    # Requires east save button
    connect_gate(world, used_names, castle_region_names.p2_m, castle_region_names.p2_s,
                 key_gold_prison, gate_codes, prison_gate_items, gate_names.c_p2_4, True)
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_e_bronze_gate_2,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p2_7, False)
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_m_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p2_6, False)
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_se_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p2_2, False)
    connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_gg_room_reward,
            False, item_name.ev_castle_p2_switch, 4, False)
    connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_w_treasure, False)
    # Requires treasure west wall button
    connect(world, used_names, castle_region_names.p2_w_treasure, castle_region_names.p2_w_treasure_tp, False)
    # Requires treasure east wall button
    connect(world, used_names, castle_region_names.p2_s, castle_region_names.p2_tp_puzzle, False)
    # Requires tp puzzle buttons
    connect_gate(world, used_names, castle_region_names.p2_s, castle_region_names.p2_end,
                 key_gold_prison, gate_codes, prison_gate_items, gate_names.c_p2_3, True)
    connect_exit(world, used_names, castle_region_names.p2_end, castle_region_names.p3_start_door,
                 entrance_names.c_p3_0, entrance_names.c_p2_3)

    connect(world, used_names, castle_region_names.p3_start_door, castle_region_names.p3_start, False)
    # Actually *not* two-way! The button prevents backtracking for now
    # Requires entrance button
    connect(world, used_names, castle_region_names.p3_start, castle_region_names.p3_nw_closed_room, False)
    # Requires room open button
    connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_nw_n_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p3_1, False)
    connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_nw_s_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p3_0, False)
    connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_silver_gate,
                 key_silver_prison, gate_codes, prison_gate_items, gate_names.c_p3_3, True)
    # Requires start spike switch
    connect_exit(world, used_names, castle_region_names.p3_silver_gate, castle_region_names.p1_from_p3_s,
                 entrance_names.c_p1_4, entrance_names.c_p3_1)
    connect_gate(world, used_names, castle_region_names.p3_start, castle_region_names.p3_n_gold_gate,
                 key_gold_prison, gate_codes, prison_gate_items, gate_names.c_p3_4, True)
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_rspikes, False)
    # Requires red spikes button, two-way
    connect(world, used_names, castle_region_names.p3_rspikes, castle_region_names.p3_rspikes_room, False)
    # Requires middle room unlock button, from p3_n_gold_gate, two-way. This also connects p3_start to p3_n_gold_gate!
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_bonus, False)
    # Requires 5 bonus switches
    connect_exit(world, used_names, castle_region_names.p3_bonus, castle_region_names.n1_start,
                 entrance_names.c_n1_0, entrance_names.c_p3_b_ent)
    # Requires 9 bonus buttons
    connect_gate(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_s_bronze_gate,
                 key_bronze_prison, gate_codes, prison_gate_items, gate_names.c_p3_2, False)
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_spikes_s, False)
    # Requires spike switch
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_sw, False)
    # Requires spike switch, also two-way
    connect(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_exit_s, False)
    # Requires exit button, two-way
    connect_exit(world, used_names, castle_region_names.p3_exit_s, castle_region_names.p1_from_p3_n,
                 entrance_names.c_p1_10, entrance_names.c_p3_10)
    connect(world, used_names, castle_region_names.p3_exit_s, castle_region_names.p3_n_gold_gate, False)
    # Requires exit shortcut button, two-way
    connect(world, used_names, castle_region_names.p3_n_gold_gate, castle_region_names.p3_arrow_hall_secret,
            False, item_name.btnc_p3_e_passage, 1, False)
    connect(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_hidden_arrow_hall, False,
            item_name.btnc_p3_s_passage, 1, False)
    connect_gate(world, used_names, castle_region_names.p3_sw, castle_region_names.p3_s_gold_gate,
                 key_gold_prison, gate_codes, prison_gate_items, gate_names.c_p3_5, False)
    connect_exit(world, used_names, castle_region_names.p3_sw, castle_region_names.b1_start,
                 entrance_names.c_b1_0, entrance_names.c_p3_boss, item_name.ev_castle_b1_boss_switch, 3, False)

    # if multiworld.randomize_bonus_keys[player]:
    connect(world, used_names, castle_region_names.n1_start, castle_region_names.n1_room1,
            False, key_bonus_prison)
    connect(world, used_names, castle_region_names.n1_room1, castle_region_names.n1_room2,
            False, key_bonus_prison)
    connect(world, used_names, castle_region_names.n1_room2, castle_region_names.n1_room2_unlock, False)
    # Requires room 2 panel
    connect(world, used_names, castle_region_names.n1_room2, castle_region_names.n1_room3,
            False, key_bonus_prison)
    connect(world, used_names, castle_region_names.n1_room3, castle_region_names.n1_room3_unlock, False)
    # Requires room 3 west panel
    connect(world, used_names, castle_region_names.n1_room3, castle_region_names.n1_room3_hall, False)
    # Requires room 3 east panel or room 3 hall panel
    connect(world, used_names, castle_region_names.n1_room3_hall, castle_region_names.n1_room4,
            False, key_bonus_prison)
    connect_exit(world, used_names, castle_region_names.n1_room4, castle_region_names.p3_bonus_return,
                 entrance_names.c_p3_b_return, None, key_bonus_prison)
    connect(world, used_names, castle_region_names.p3_bonus_return, castle_region_names.p3_bonus, False)
    # else:
    #     connect_generic(multiworld, player, used_names, castle_region_names.n1_start, castle_region_names.n1_room1)
    #     connect_generic(multiworld, player, used_names, castle_region_names.n1_room1, castle_region_names.n1_room2)
    #     connect_generic(multiworld, player, used_names, castle_region_names.n1_room2, castle_region_names.n1_room3)
    #     connect_generic(multiworld, player, used_names, castle_region_names.n1_room3, castle_region_names.n1_room4)
    #     connect_generic(multiworld, player, used_names, castle_region_names.n1_room4, castle_region_names.p3_bonus_return,
    #                     True)

    connect(world, used_names, castle_region_names.b1_start, castle_region_names.b1_arena, False)
    connect(world, used_names, castle_region_names.b1_arena, castle_region_names.b1_defeated, False)
    connect(world, used_names, castle_region_names.b1_defeated, castle_region_names.b1_exit, False)
    connect_exit(world, used_names, castle_region_names.b1_exit, castle_region_names.a1_start,
                 entrance_names.c_a1_0, entrance_names.c_b1_1)

    connect(world, used_names, castle_region_names.a1_start, castle_region_names.a1_se, False)
    connect_gate(world, used_names, castle_region_names.a1_start, castle_region_names.a1_start_shop_w,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_3, False)
    connect_gate(world, used_names, castle_region_names.a1_start, castle_region_names.a1_start_shop_m,
                 key_gold_armory, gate_codes, armory_gate_items, gate_names.c_a1_7, False)
    connect_gate(world, used_names, castle_region_names.a1_start, castle_region_names.a1_start_shop_e,
                 key_gold_armory, gate_codes, armory_gate_items, gate_names.c_a1_8, False)
    connect_exit(world, used_names, castle_region_names.a1_start, castle_region_names.a2_start,
                 entrance_names.c_a2_0, entrance_names.c_a1_a2)
    connect_exit(world, used_names, castle_region_names.a1_start, castle_region_names.a3_main,
                 entrance_names.c_a3_0, entrance_names.c_a1_a3)
    # Requires start wall switch
    connect_gate(world, used_names, castle_region_names.a1_se, castle_region_names.a1_e,
                 key_silver_armory, gate_codes, armory_gate_items, gate_names.c_a1_6, True)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_sw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_12, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_s_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_4, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_se_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_5, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_e_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_14, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_e_ne_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_13, False)
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_n_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_10, False)
    connect(world, used_names, castle_region_names.a1_e_se_bgate, castle_region_names.a1_rune_room, False)
    # Requires se gate wall switch
    connect(world, used_names, castle_region_names.a1_rune_room, castle_region_names.a1_se_cache, False)
    # Requires 4 rune switches
    connect(world, used_names, castle_region_names.a1_e, castle_region_names.a1_red_spikes, False)
    # Requires red spike switch
    connect(world, used_names, castle_region_names.a1_e, castle_region_names.a1_tp_n, False)
    # Requires tp switch
    connect_gate(world, used_names, castle_region_names.a1_e, castle_region_names.a1_w,
                 key_silver_armory, gate_codes, armory_gate_items, gate_names.c_a1_15, True)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_nw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_0, True)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_ne_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_9, False)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_se_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_2, False)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_sw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_1, False)
    connect_gate(world, used_names, castle_region_names.a1_w, castle_region_names.a1_w_sw_bgate_1,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a1_11, False)
    connect(world, used_names, castle_region_names.a1_w, castle_region_names.a1_puzzle, False)
    connect(world, used_names, castle_region_names.a1_w, castle_region_names.a1_sw_spikes, False)
    # Requires spike switch, can also reach from a1_start

    connect(world, used_names, castle_region_names.a2_start, castle_region_names.a2_tp_sw, False)
    # Requires floor 5 sw teleport switch
    connect(world, used_names, castle_region_names.a2_start, castle_region_names.a2_tp_se, False)
    # Requires floor 5 se teleport switch
    connect(world, used_names, castle_region_names.a2_start, castle_region_names.a2_puzzle, False)
    # Requires floor 5 puzzle switch
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_sw_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_3, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_s_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_4, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_se_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_5, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_s_save_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_10, False)
    connect_gate(world, used_names, castle_region_names.a2_start, castle_region_names.a2_ne,
                 key_silver_armory, gate_codes, armory_gate_items, gate_names.c_a2_6, True)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_m_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_7, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_l_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_1, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_0, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_b_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_8, False)
    connect_gate(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_ne_save_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_9, False)
    connect(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_tp_ne, False)
    # Requires floor 5 ne teleport switch
    connect(world, used_names, castle_region_names.a2_ne, castle_region_names.a2_e, False)
    connect_gate(world, used_names, castle_region_names.a2_e, castle_region_names.a2_e_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a2_2, False)
    connect_exit(world, used_names, castle_region_names.a2_nw, castle_region_names.n2_start,
                 entrance_names.c_n2_0, entrance_names.c_a2_88)
    # Requires bonus portal switch
    connect_exit(world, used_names, castle_region_names.a2_nw, castle_region_names.a1_from_a2,
                 entrance_names.c_a1_1, entrance_names.c_a2_1)
    connect(world, used_names, castle_region_names.a2_nw, castle_region_names.a2_blue_spikes,
            False, item_name.btnc_a2_blue_spikes, 1, False)
    connect(world, used_names, castle_region_names.a2_blue_spikes, castle_region_names.a2_blue_spikes_tp,
            False, item_name.btnc_a2_bspikes_tp, 1, False)
    # Requires floor 5 blue spikes teleport switch
    connect(world, used_names, castle_region_names.a2_nw, castle_region_names.a2_to_a3, False)
    # Requires floor 6 passage open switch
    connect_exit(world, used_names, castle_region_names.a2_to_a3, castle_region_names.a3_from_a2,
                 entrance_names.c_a3_1, entrance_names.c_a2_2)

    connect(world, used_names, castle_region_names.n2_start, castle_region_names.n2_m,
            False, key_bonus_armory)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_nw,
            False, key_bonus_armory)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_n,
            False, key_bonus_armory)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_e,
            False, key_bonus_armory)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_s,
            False, key_bonus_armory)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_w,
            False, key_bonus_armory)
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_se, False)
    # Requires bonus 2 open se room panel
    connect(world, used_names, castle_region_names.n2_m, castle_region_names.n2_ne, False)
    # Requires bonus 2 open ne room panel
    connect(world, used_names, castle_region_names.n2_ne, castle_region_names.n2_exit, False)
    # Requires bonus 2 open exit panel
    connect_exit(world, used_names, castle_region_names.n2_exit, castle_region_names.a2_bonus_return,
                 entrance_names.c_a2_10, None)

    connect(world, used_names, castle_region_names.a3_start, castle_region_names.a3_main, True)
    # Requires open start top wall switch or open start right wall switch
    connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_knife_puzzle_reward, False)
    # Requires 5 spike puzzle switches
    connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_knife_reward_2, False)
    # Requires 2 spike puzzle switches
    connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_nw_stairs, False)
    # Requires 2 spike puzzle switches
    connect_exit(world, used_names, castle_region_names.a3_nw_stairs, castle_region_names.a2_nw,
                 entrance_names.c_a2_3, entrance_names.c_a3_2)
    connect(world, used_names, castle_region_names.a3_main, castle_region_names.a3_tp, False)
    # Requires floor 6 teleport switch
    # connect_generic(multiworld, player, used_names, castle_region_names.a3_from_a2, castle_region_names.a3_main)
    # Requires floor 6 from floor 5 open passage switch
    connect_gate(world, used_names, castle_region_names.a3_from_a2, castle_region_names.a3_w_b_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a3_5, False)
    # Don't forget to add extra thing in rules requiring the teleport button for the item inside
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_w_t_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a3_2, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_w_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a3_4, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_n_l_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a3_1, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_n_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a3_0, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_e_l_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a3_3, False)
    connect_gate(world, used_names, castle_region_names.a3_main, castle_region_names.a3_e_r_bgate,
                 key_bronze_armory, gate_codes, armory_gate_items, gate_names.c_a3_6, False)

    connect_exit(world, used_names, castle_region_names.a1_start, castle_region_names.b2_start,
                 entrance_names.c_b2_0, entrance_names.c_a1_boss, item_name.ev_castle_b2_boss_switch, 3, False)
    connect(world, used_names, castle_region_names.b2_start, castle_region_names.b2_arena, False)
    connect(world, used_names, castle_region_names.b2_arena, castle_region_names.b2_defeated, False)
    connect(world, used_names, castle_region_names.b2_defeated, castle_region_names.b2_exit, False)
    connect_exit(world, used_names, castle_region_names.b2_exit, castle_region_names.r1_start,
                 entrance_names.c_r1_0, entrance_names.c_b2_1)

    connect_gate(world, used_names, castle_region_names.r1_start, castle_region_names.r1_se_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, gate_names.c_r1_2, False)
    connect(world, used_names, castle_region_names.r1_se_ggate, castle_region_names.r1_e, False)
    # Requires floor 7 open east passage
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e_s_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, gate_names.c_r1_5, False)
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, gate_names.c_r1_7, False)
    connect(world, used_names, castle_region_names.r1_e_sgate, castle_region_names.r1_se_wall, False)
    # Requires floor 7 open right wall
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e,
                 key_bronze_archives, gate_codes, archives_gate_items, gate_names.c_r1_4, False)
    # Technically this also leads to e_n_bgate, but doing this should logically be equivalent (hopefully)
    connect_gate(world, used_names, castle_region_names.r1_e, castle_region_names.r1_e_n_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, gate_names.c_r1_6, True)
    # Internal gate
    connect_gate(world, used_names, castle_region_names.r1_e_n_bgate, castle_region_names.r1_e_n_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, gate_names.c_r1_3, False)
    connect_gate(world, used_names, castle_region_names.r1_e_n_bgate, castle_region_names.r1_ne_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, gate_names.c_r1_1, False)
    connect(world, used_names, castle_region_names.r1_ne_ggate, castle_region_names.r1_nw, False)
    # Requires floor 7 open North passage
    connect(world, used_names, castle_region_names.r1_nw, castle_region_names.r1_nw_hidden, False)
    # Requires floor 7 open hidden room
    connect_gate(world, used_names, castle_region_names.r1_nw_hidden, castle_region_names.r1_nw_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, gate_names.c_r1_0, False)
    connect(world, used_names, castle_region_names.r1_nw_ggate, castle_region_names.r1_sw, False)
    # Requires floor 7 open west passage
    connect_gate(world, used_names, castle_region_names.r1_sw, castle_region_names.r1_w_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, gate_names.c_r1_10, False)
    connect(world, used_names, castle_region_names.r1_w_sgate, castle_region_names.r1_start_wall, False)
    # Requires floor 7 open start wall
    connect_gate(world, used_names, castle_region_names.r1_sw, castle_region_names.r1_sw_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, gate_names.c_r1_11, False)
    connect(world, used_names, castle_region_names.r1_sw_ggate, castle_region_names.r1_exit_l, False)
    # From sw requires floor 7 open left exit
    # Internal bronze gate
    r1_internals = [
        gate_names.c_r1_8,
        gate_names.c_r1_9,
    ]
    for gate in r1_internals:
        connect_gate(world, used_names, castle_region_names.r1_sw, castle_region_names.r1_sw,
                     key_bronze_archives, gate_codes, archives_gate_items, gate, False)
    connect_exit(world, used_names, castle_region_names.r1_exit_l, castle_region_names.r2_start,
                 entrance_names.c_r2_0, entrance_names.c_r1_1)
    connect(world, used_names, castle_region_names.r1_exit_l, castle_region_names.r1_exit_r, False)
    # From start requires floor 7 open right exit
    connect_exit(world, used_names, castle_region_names.r1_exit_r, castle_region_names.r2_bswitch,
                 entrance_names.c_r2_1, entrance_names.c_r1_2)

    connect(world, used_names, castle_region_names.r2_start, castle_region_names.r2_m, False)
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_w_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, gate_names.c_r2_0, False)
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
                     key_bronze_archives, gate_codes, archives_gate_items, gate, False)
    connect(world, used_names, castle_region_names.r2_m, castle_region_names.r2_e, False)
    # Requires open east passage top or open east passage bottom
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_nw,
                 key_bronze_archives, gate_codes, archives_gate_items, gate_names.c_r2_7, False)  # True for button rando
    connect(world, used_names, castle_region_names.r2_nw, castle_region_names.r2_n, False)  # True
    # Requires open north room left
    # Or requires open north room right from r2_m
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, gate_names.c_r2_5, False)
    connect(world, used_names, castle_region_names.r2_sgate, castle_region_names.r2_s, False)
    # Requires silver gate floor button
    connect(world, used_names, castle_region_names.r2_s, castle_region_names.r2_spike_island, False)
    # Requires open spike island passage
    connect(world, used_names, castle_region_names.r2_spike_island, castle_region_names.r2_sw_bridge, False)
    # Requires open sw bridge from r2_s
    connect(world, used_names, castle_region_names.r2_sw_bridge, castle_region_names.r2_puzzle, False)
    # Requires open puzzle room
    connect(world, used_names, castle_region_names.r2_s, castle_region_names.r2_w, False)
    # Requires open west passage
    connect(world, used_names, castle_region_names.r2_from_r3, castle_region_names.r2_ne_cache, False)
    # Requires open cache passage
    connect_gate(world, used_names, castle_region_names.r2_m, castle_region_names.r2_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, gate_names.c_r2_4, False)  # True
    # Can also access with open exit button, it removes the wall
    connect_exit(world, used_names, castle_region_names.r2_ggate, castle_region_names.r3_main,
                 entrance_names.c_r3_0, entrance_names.c_r2_2)
    # Requires open exit button

    connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_ne_room, False)
    # Requires open ne room
    connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_s_room, False)
    # Requires open south room
    connect_gate(world, used_names, castle_region_names.r3_s_room, castle_region_names.r3_l_shop_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, gate_names.c_r3_5, False)
    connect_gate(world, used_names, castle_region_names.r3_s_room, castle_region_names.r3_r_shop_sgate,
                 key_silver_archives, gate_codes, archives_gate_items, gate_names.c_r3_4, False)
    connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_se_cache, False)
    # Requires open se cache room
    connect(world, used_names, castle_region_names.r3_main, castle_region_names.r3_boss_switch, False)
    # Requires open boss switch room
    connect(world, used_names, castle_region_names.r3_boss_switch, castle_region_names.r3_rune_room, False)
    # Requires 5 open simon says room switch
    connect(world, used_names, castle_region_names.r3_rune_room, castle_region_names.r3_bonus, False)
    # Requires 6 simon says switch
    connect_exit(world, used_names, castle_region_names.r3_bonus, castle_region_names.n3_main,
                 entrance_names.c_n3_0, None)  # entrance_names.c_r3_b_ent)
    # Requires open bonus entrance passage  # We can make this one-way because we can't get locked here
    connect_gate(world, used_names, castle_region_names.r3_main, castle_region_names.r3_sw_bgate,
                 key_bronze_archives, gate_codes, archives_gate_items, gate_names.c_r3_1, False)
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
                     key_bronze_archives, gate_codes, archives_gate_items, gate, False)
    connect(world, used_names, castle_region_names.r3_sw_bgate, castle_region_names.r3_sw_wall_l, False)
    # Requires left sw button
    connect(world, used_names, castle_region_names.r3_sw_bgate, castle_region_names.r3_sw_wall_r, False)
    # Requires right sw button
    connect(world, used_names, castle_region_names.r3_sw_wall_l, castle_region_names.r3_nw_tp, False)
    # Requires nw tp button
    connect(world, used_names, castle_region_names.r3_bonus_return, castle_region_names.r3_bonus_return_bridge,
            False)
    connect_exit(world, used_names, castle_region_names.r3_bonus_return, castle_region_names.r2_from_r3,
                 entrance_names.c_r2_200, entrance_names.c_r3_250)
    connect_gate(world, used_names, castle_region_names.r3_main, castle_region_names.r3_e_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, gate_names.c_r3_6, False)
    connect_gate(world, used_names, castle_region_names.r3_main, castle_region_names.r3_w_ggate,
                 key_gold_archives, gate_codes, archives_gate_items, gate_names.c_r3_3, True)
    connect(world, used_names, castle_region_names.r3_w_ggate, castle_region_names.r3_exit, False)
    # Requires open boss switch room
    connect_exit(world, used_names, castle_region_names.r3_exit, castle_region_names.b3_start,
                 entrance_names.c_b3_0, entrance_names.c_r3_boss, item_name.ev_castle_b3_boss_switch, 3, False)

    connect_exit(world, used_names, castle_region_names.n3_main, castle_region_names.n3_tp_room,
                 entrance_names.c_n3_80, entrance_names.c_n3_12)
    connect_exit(world, used_names, castle_region_names.n3_main, castle_region_names.r3_bonus_return,
                 entrance_names.c_r3_b_return, None)
    # Internal bronze gates
    for i in range(3):
        connect(world, used_names, castle_region_names.n3_main, castle_region_names.n3_main,
                False, key_bonus_archives)

    connect(world, used_names, castle_region_names.b3_start, castle_region_names.b3_arena, False)
    connect(world, used_names, castle_region_names.b3_arena, castle_region_names.b3_defeated, False)
    connect(world, used_names, castle_region_names.b3_defeated, castle_region_names.b3_exit, False)
    connect_exit(world, used_names, castle_region_names.b3_exit, castle_region_names.c1_start,
                 entrance_names.c_c1_0, entrance_names.c_b3_1)

    connect(world, used_names, castle_region_names.c1_start, castle_region_names.c1_n_spikes, False)
    # Requires n spikes switch
    connect(world, used_names, castle_region_names.c1_start, castle_region_names.c1_se_spikes, False)
    # Requires se spikes switch
    connect_gate(world, used_names, castle_region_names.c1_start, castle_region_names.c1_shop,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c1_3, False)
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
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_gate(world, used_names, castle_region_names.c1_start, castle_region_names.c1_w,
                 key_gold_chambers, gate_codes, chambers_gate_items, gate_names.c_c1_12, True)
    connect_gate(world, used_names, castle_region_names.c1_w, castle_region_names.c1_sgate,
                 key_silver_chambers, gate_codes, chambers_gate_items, gate_names.c_c1_13, True)
    connect(world, used_names, castle_region_names.c1_sgate, castle_region_names.c1_prison_stairs, False)
    # Requires open prison door passage from c1_start
    connect_exit(world, used_names, castle_region_names.c1_sgate, castle_region_names.c2_tp_island,
                 entrance_names.c_c2_50, None)
    connect_exit(world, used_names, castle_region_names.c1_tp_island, castle_region_names.c1_sgate,
                 entrance_names.c_c1_75, None)
    connect_exit(world, used_names, castle_region_names.c1_prison_stairs, castle_region_names.pstart_start,
                 entrance_names.c_p_return_0, entrance_names.c_c1_169)
    connect_gate(world, used_names, castle_region_names.c1_w, castle_region_names.c1_s_bgate,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c1_6, False)
    connect(world, used_names, castle_region_names.c1_s_bgate, castle_region_names.c1_start, False)
    # Requires s shortcut button
    connect_gate(world, used_names, castle_region_names.c1_s_bgate, castle_region_names.c1_ledge,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c1_5, False)
    # Bronze gates with no checks
    c1_s_internals = [
        gate_names.c_c1_0,
        gate_names.c_c1_1,
        gate_names.c_c1_8,
        gate_names.c_c1_4,
    ]
    for gate in c1_s_internals:
        connect_gate(world, used_names, castle_region_names.c1_w, castle_region_names.c1_w,
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_exit(world, used_names, castle_region_names.c1_w, castle_region_names.c2_main,
                 entrance_names.c_c2_0, entrance_names.c_c1_100)

    connect(world, used_names, castle_region_names.pstart_start, castle_region_names.pstart_puzzle, False)
    # Requires 4 prison return rune switches and prison return puzzle switch

    connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_sw_wall, False)
    # Requires open sw wall
    connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_wall, False)
    # Requires open west wall
    connect(world, used_names, castle_region_names.c2_w_shops_2, castle_region_names.c2_e_wall, False)
    # Requires open east wall
    connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_spikes, False)
    # Requires 4 spike floor rune switches
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_shops_1,
                 key_silver_chambers, gate_codes, chambers_gate_items, gate_names.c_c2_11, False)
    connect_gate(world, used_names, castle_region_names.c2_w_shops_3, castle_region_names.c2_w_shops_2,
                 key_silver_chambers, gate_codes, chambers_gate_items, gate_names.c_c2_10, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_w_shops_3,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c2_3, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_e_shops_1,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c2_2, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_e_shops_2,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c2_16, False)
    # Can also access from main through open east wall
    connect(world, used_names, castle_region_names.c2_e_shops_1, castle_region_names.c2_puzzle, False)
    # Requires open puzzle room and puzzle switch
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_exit_bgate,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c2_12, False)
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
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_gate(world, used_names, castle_region_names.c2_main, castle_region_names.c2_n,
                 key_gold_chambers, gate_codes, chambers_gate_items, gate_names.c_c2_9, True)
    connect(world, used_names, castle_region_names.c2_n, castle_region_names.c2_bonus, True)
    # Require 5 open bonus entrance wall switches
    connect_exit(world, used_names, castle_region_names.c2_bonus, castle_region_names.n4_main,
                 entrance_names.c_n4_0, entrance_names.c_c2_b_ent)
    connect(world, used_names, castle_region_names.c2_n, castle_region_names.c2_n_wall,
            False, item_name.btnc_c2_n_wall, 1, False)
    connect(world, used_names, castle_region_names.c2_n, castle_region_names.c2_n_shops,
            False, item_name.ev_castle_c2_n_shops_switch, 1, False)
    connect(world, used_names, castle_region_names.c2_main, castle_region_names.c2_n_shops,
            False, item_name.ev_castle_c2_n_shops_switch, 1, False)
    # Presently to open the north shops you need access to c3_nw, change to two-way for button rando
    connect_exit(world, used_names, castle_region_names.c2_main, castle_region_names.c3_start,
                 entrance_names.c_c3_0, entrance_names.c_c2_45)
    connect_exit(world, used_names, castle_region_names.c2_n, castle_region_names.c3_nw,
                 entrance_names.c_c3_54, entrance_names.c_c2_105)
    connect_exit(world, used_names, castle_region_names.c2_tp_island, castle_region_names.c1_tp_island,
                 entrance_names.c_c1_99, None)

    connect(world, used_names, castle_region_names.n4_main, castle_region_names.n4_nw,
            False, key_bonus_chambers)
    connect(world, used_names, castle_region_names.n4_main, castle_region_names.n4_w,
            False, key_bonus_chambers)
    connect(world, used_names, castle_region_names.n4_main, castle_region_names.n4_e,
            False, key_bonus_chambers)
    connect_exit(world, used_names, castle_region_names.n4_main, castle_region_names.c2_bonus_return,
                 entrance_names.c_c2_125, None, key_bonus_chambers)

    connect_gate(world, used_names, castle_region_names.c3_start, castle_region_names.c3_rspike_switch,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c3_1, False)
    # Can also get there if you have red spike switch
    connect(world, used_names, castle_region_names.c3_rspike_switch, castle_region_names.c3_rspikes,
            False, item_name.ev_castle_c3_rspikes_switch, 1, False)
    # From c3_start technically, but route through gate so that we require it
    connect_gate(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_s_bgate,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c3_8, False)
    connect_gate(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_m_shop,
                 key_bronze_chambers, gate_codes, chambers_gate_items, gate_names.c_c3_5, False)
    connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_m_wall, False)
    # Requires open middle passage
    connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_m_tp, False)
    # Requires teleport middle item
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
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect_gate(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_nw,
                 key_gold_chambers, gate_codes, chambers_gate_items, gate_names.c_c3_9, True)
    # Bronze gates with no checks
    c3_n_internals = [
        gate_names.c_c3_2,
        gate_names.c_c3_0,
        gate_names.c_c3_10,
    ]
    for gate in c3_n_internals:
        connect_gate(world, used_names, castle_region_names.c3_nw, castle_region_names.c3_nw,
                     key_bronze_chambers, gate_codes, chambers_gate_items, gate, False)
    connect(world, used_names, castle_region_names.c3_rspikes, castle_region_names.c3_sw_hidden,
            False, item_name.ev_castle_c3_sw_hidden_switch, 6, False)
    connect(world, used_names, castle_region_names.c3_sw_hidden, castle_region_names.c3_se_hidden, False)
    # Requires open se hidden wall switch
    connect(world, used_names, castle_region_names.c3_se_hidden, castle_region_names.c3_light_bridge, False)
    # Requires activate light bridge switch
    connect_exit(world, used_names, castle_region_names.c3_sw_hidden, castle_region_names.c3_fire_floor,
                 entrance_names.c_c3_67, None)
    connect(world, used_names, castle_region_names.c3_fire_floor, castle_region_names.c3_fire_floor_tp, False)
    connect_exit(world, used_names, castle_region_names.c3_fire_floor, castle_region_names.c2_c3_tp,
                 entrance_names.c_c2_77, None)
    connect_exit(world, used_names, castle_region_names.c2_c3_tp, castle_region_names.c3_c2_tp,
                 entrance_names.c_c3_156, None)
    connect(world, used_names, castle_region_names.c3_c2_tp, castle_region_names.c3_nw, False)

    # Old connect method to ensure no keys will in the final boss room
    connect_exit(world, used_names, castle_region_names.c2_main, castle_region_names.b4_start,
                 entrance_names.c_b4_0, entrance_names.c_c2_boss, item_name.ev_castle_b4_boss_switch, 3, False)
    connect(world, used_names, castle_region_names.b4_start, castle_region_names.b4_defeated, False)

    # The escape sequence rooms aren't randomized, it makes the escape goal too easy!
    connect(world, used_names, castle_region_names.b4_defeated, castle_region_names.e1_main,
            False, item_name.plank, 12, False)
    # Technically planks are consumed, but nothing else does so this is faster
    connect(world, used_names, castle_region_names.e1_main, castle_region_names.e2_main, False)
    connect(world, used_names, castle_region_names.e2_main, castle_region_names.e3_main, False)
    connect(world, used_names, castle_region_names.e3_main, castle_region_names.e4_main, False)
    connect(world, used_names, castle_region_names.e4_main, castle_region_names.escaped, False)


def create_tots_regions(world: "HammerwatchWorld", active_locations: typing.Dict[str, LocationData],
                        random_locations: typing.Dict[str, int]):
    menu_region = create_region(world, active_locations, temple_region_names.menu, None)

    hub_main_locations = [
        temple_location_names.hub_front_of_pof,
        temple_location_names.hub_behind_temple_entrance
    ]
    dunes_main_region = create_region(world, active_locations, temple_region_names.hub_main, hub_main_locations)

    dunes_rocks_locations = [
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
    ]
    dunes_rocks_region = create_region(world, active_locations, temple_region_names.hub_rocks, dunes_rocks_locations)

    dunes_pyramid_locations = [
        temple_location_names.hub_pof_reward
    ]
    dunes_pyramid_region = create_region(world, active_locations, temple_region_names.hub_pyramid_of_fear,
                                         dunes_pyramid_locations)

    library_region = create_region(world, active_locations, temple_region_names.library, [])
    library_lobby_region = create_region(world, active_locations, temple_region_names.library_lobby, [])

    cave3_main_locations = [
        temple_location_names.cave3_squire,
        temple_location_names.cave3_guard,
        temple_location_names.cave3_ne,
        temple_location_names.cave3_nw,
        temple_location_names.cave3_m,
        temple_location_names.cave3_half_bridge,
        temple_location_names.cave3_n,
        temple_location_names.cave3_secret_n,
        temple_location_names.cave3_secret_nw,
        temple_location_names.cave3_secret_s,
        temple_location_names.c3_miniboss_tick_1,
        temple_location_names.c3_miniboss_tick_2,
        temple_location_names.c3_tower_plant_small_1,
        temple_location_names.c3_tower_plant_small_2,
        temple_location_names.c3_tower_plant_small_3,
        temple_location_names.c3_tower_plant_small_4,
        temple_location_names.c3_tower_plant_small_5,
        temple_location_names.c3_tower_plant_small_6,
        temple_location_names.btn_c3_puzzle,
        temple_location_names.btn_c3_bridge,
    ]
    cave3_main_region = create_region(world, active_locations, temple_region_names.cave_3_main, cave3_main_locations)

    c3_puzzle_locs = [
        temple_location_names.c3_puzzle_1,
        temple_location_names.c3_puzzle_2,
        temple_location_names.c3_puzzle_3,
        temple_location_names.c3_puzzle_4,
    ]
    c3_puzzle_region = create_region(world, active_locations, temple_region_names.c3_puzzle, c3_puzzle_locs)

    c3_e_locs = [
        temple_location_names.cave3_outside_guard,
        temple_location_names.cave3_se,
        temple_location_names.cave3_trapped_guard,
        temple_location_names.c3_tower_plant,
        temple_location_names.c3_tower_plant_small_7,
        temple_location_names.c3_tower_plant_small_8,
        temple_location_names.ev_c3_portal,
    ]
    c3_e_region = create_region(world, active_locations, temple_region_names.c3_e, c3_e_locs)

    cave3_fall_locations = [
        temple_location_names.cave3_fall_nw,
        temple_location_names.cave3_fall_ne,
        temple_location_names.cave3_fall_sw,
        temple_location_names.cave3_fall_se,
        temple_location_names.btn_c3_floor_fall,
    ]
    cave3_fall_region = create_region(world, active_locations, temple_region_names.cave_3_fall, cave3_fall_locations)

    cave3_fields_locations = [
        temple_location_names.cave3_captain,
        temple_location_names.cave3_captain_dock,
    ]
    cave3_fields_region = create_region(world, active_locations, temple_region_names.cave_3_fields,
                                        cave3_fields_locations)

    c3_e_water_locs = [
        temple_location_names.cave3_fields_r,
    ]
    c3_e_water_region = create_region(world, active_locations, temple_region_names.c3_e_water, c3_e_water_locs)

    cave3_portal_locations = [
        temple_location_names.cave3_portal_l,
        temple_location_names.cave3_portal_r,
        temple_location_names.btn_c3_pof_1,
        temple_location_names.btn_c3_pof_2,
        temple_location_names.btn_c3_pof_3,
        temple_location_names.btn_c3_pof_4,
        temple_location_names.btn_c3_pof,
    ]
    cave3_portal_region = create_region(world, active_locations, temple_region_names.cave_3_portal,
                                        cave3_portal_locations)

    cave3_secret_locations = [
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
    ]
    cave3_secret_region = create_region(world, active_locations, temple_region_names.cave_3_secret,
                                        cave3_secret_locations)

    cave2_main_locations = [
        temple_location_names.cave2_nw_2,
        temple_location_names.cave2_double_bridge_r,
        temple_location_names.cave2_guard_s,
        temple_location_names.cave2_nw_3,
        temple_location_names.cave2_w_miniboss_4,
        temple_location_names.cave2_below_pumps_3,
        temple_location_names.cave2_nw_1,
        temple_location_names.cave2_pumps_n,
        temple_location_names.cave2_guard,
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
        temple_location_names.cave2_secret_ne,
        temple_location_names.cave2_secret_m,
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
    ]
    cave2_main_region = create_region(world, active_locations, temple_region_names.cave_2_main, cave2_main_locations)

    cave2_pumps_locations = [
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
    ]
    cave2_pumps_region = create_region(world, active_locations, temple_region_names.cave_2_pumps, cave2_pumps_locations)

    cave_2_red_bridge_locations = [
        temple_location_names.cave2_red_bridge_1,
        temple_location_names.cave2_red_bridge_2,
        temple_location_names.cave2_red_bridge_3,
        temple_location_names.cave2_red_bridge_4,
    ]
    cave2_red_bridge_region = create_region(world, active_locations, temple_region_names.c2_red_bridge,
                                            cave_2_red_bridge_locations)

    cave_2_green_bridge_locations = [
        temple_location_names.cave2_green_bridge,
    ]
    cave2_green_bridge_region = create_region(world, active_locations, temple_region_names.c2_green_bridge,
                                              cave_2_green_bridge_locations)

    c2_double_bridge_locs = [
        temple_location_names.cave2_double_bridge_m,
    ]
    c2_double_bridge_region = create_region(world, active_locations, temple_region_names.c2_double_bridge,
                                            c2_double_bridge_locs)

    c2_sw_locs = [
        temple_location_names.cave2_sw_hidden_room_1,
        temple_location_names.cave2_sw_hidden_room_2,
        temple_location_names.cave2_sw_hidden_room_3,
        temple_location_names.cave2_sw_hidden_room_4,
        temple_location_names.cave2_double_bridge_l_1,
        temple_location_names.cave2_double_bridge_l_2,
        temple_location_names.cave2_sw,
        temple_location_names.cave2_double_bridge_secret,
        temple_location_names.cave2_secret_w,
        temple_location_names.c2_miniboss_maggot_s_1,
        temple_location_names.c2_miniboss_maggot_s_2,
        temple_location_names.c2_tower_plant_2,
        temple_location_names.c2_tower_plant_small_10,
        temple_location_names.c2_tower_plant_small_16,
        temple_location_names.c2_tower_plant_small_19,
        temple_location_names.c2_tower_plant_small_22,
        temple_location_names.btn_c2_bridges,
        temple_location_names.btn_c2_s_bridge,
        temple_location_names.btn_c2_puzzle,
    ]
    c2_sw_region = create_region(world, active_locations, temple_region_names.c2_sw, c2_sw_locs)

    c2_puzzle_locs = [
        temple_location_names.c2_puzzle_1,
        temple_location_names.c2_puzzle_2,
        temple_location_names.c2_puzzle_3,
        temple_location_names.c2_puzzle_4,
    ]
    c2_puzzle_region = create_region(world, active_locations, temple_region_names.c2_puzzle, c2_puzzle_locs)

    cave1_main_locations = [
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
        temple_location_names.cave1_secret_nw,
        temple_location_names.cave1_secret_w,
        temple_location_names.cave1_secret_m,
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
        temple_location_names.btn_c1_puzzle_w
    ]
    cave1_main_region = create_region(world, active_locations, temple_region_names.cave_1_main, cave1_main_locations)

    c1_n_puzzle_locs = [
        temple_location_names.c1_n_puzzle_1,
        temple_location_names.c1_n_puzzle_2,
        temple_location_names.c1_n_puzzle_3,
        temple_location_names.c1_n_puzzle_4,
    ]
    c1_n_puzzle_region = create_region(world, active_locations, temple_region_names.c1_n_puzzle, c1_n_puzzle_locs)

    cave1_blue_bridge_locations = [
        temple_location_names.cave1_ne_hidden_room_1,
        temple_location_names.cave1_ne_hidden_room_2,
        temple_location_names.cave1_ne_hidden_room_3,
        temple_location_names.cave1_ne_hidden_room_4,
        temple_location_names.cave1_ne_hidden_room_5,
        temple_location_names.cave1_ne_grubs,
        temple_location_names.cave1_n_bridges_1,
        temple_location_names.cave1_n_bridges_4,
        temple_location_names.cave1_n_bridges_5,
        temple_location_names.cave1_secret_n_hidden_room,
        temple_location_names.cave1_ne_1,
        temple_location_names.cave1_ne_2,
        temple_location_names.cave1_ne_3,
        temple_location_names.cave1_ne_4,
        temple_location_names.cave1_ne_5,
        temple_location_names.cave1_n_bridges_2,
        temple_location_names.cave1_n_bridges_3,
        temple_location_names.cave1_secret_ne,
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
    ]
    cave1_blue_bridge_region = create_region(world, active_locations, temple_region_names.cave_1_blue_bridge,
                                             cave1_blue_bridge_locations)

    c1_secret_hall_locs = [
        temple_location_names.cave1_secret_tunnel_1,
        temple_location_names.cave1_secret_tunnel_2,
        temple_location_names.cave1_secret_tunnel_3,
    ]
    c1_secret_hall_region = create_region(world, active_locations, temple_region_names.c1_secret_hall,
                                          c1_secret_hall_locs)

    cave1_red_bridge_locations = [
        temple_location_names.cave1_e_2,
        temple_location_names.cave1_e_3,
        temple_location_names.cave1_red_bridge_e,
        temple_location_names.cave1_se_1,
        temple_location_names.cave1_se_2,
        temple_location_names.cave1_e_1,
        temple_location_names.cave1_secret_e,
        temple_location_names.btn_c1_puzzle_e,
    ]
    cave1_red_bridge_region = create_region(world, active_locations, temple_region_names.cave_1_red_bridge,
                                            cave1_red_bridge_locations)

    c1_e_puzzle_locs = [
        temple_location_names.c1_e_puzzle_1,
        temple_location_names.c1_e_puzzle_2,
        temple_location_names.c1_e_puzzle_3,
        temple_location_names.c1_e_puzzle_4,
    ]
    c1_e_puzzle_region = create_region(world, active_locations, temple_region_names.c1_e_puzzle, c1_e_puzzle_locs)

    cave1_green_bridge_locations = [
        temple_location_names.cave1_green_bridge_1,
        temple_location_names.cave1_green_bridge_2,
    ]
    cave1_green_bridge_region = create_region(world, active_locations, temple_region_names.cave_1_green_bridge,
                                              cave1_green_bridge_locations)

    c1_storage_locs = [
        temple_location_names.cave1_krilith_ledge_n,
        temple_location_names.cave1_krilith_ledge_e,
        temple_location_names.cave1_krilith_door,
    ]
    c1_storage_island_region = create_region(world, active_locations, temple_region_names.c1_storage_island,
                                             c1_storage_locs)

    cave1_pumps_locations = [
        temple_location_names.cave1_water_s_shore,
        temple_location_names.cave1_water_s_1,
        temple_location_names.cave1_water_s_2,
        temple_location_names.cave1_water_s_3,
        temple_location_names.cave1_water_s_4,
        temple_location_names.cave1_water_s_5,
        temple_location_names.btn_c1_green,
    ]
    cave1_pumps_region = create_region(world, active_locations, temple_region_names.cave_1_pumps, cave1_pumps_locations)

    cave1_temple_locations = [
        temple_location_names.cave1_temple_hall_1,
        temple_location_names.cave1_temple_hall_2,
        temple_location_names.cave1_temple_hall_3,
        temple_location_names.cave1_temple_end_2,
        temple_location_names.cave1_temple_end_3,
        temple_location_names.cave1_temple_end_4,
        temple_location_names.cave1_temple_end_1,
    ]
    cave1_temple_region = create_region(world, active_locations, temple_region_names.cave_1_temple,
                                        cave1_temple_locations)
    # Dynamically place portal event location
    c1_portal_loc = HammerwatchLocation(world.player, temple_location_names.ev_c1_portal)
    if random_locations[temple_location_names.rloc_c1_portal] == 1:
        cave1_main_region.locations.append(c1_portal_loc)
        c1_portal_loc.parent_region = cave1_main_region
    else:
        cave1_blue_bridge_region.locations.append(c1_portal_loc)
        c1_portal_loc.parent_region = cave1_blue_bridge_region

    boss1_entrance_locations = [
        temple_location_names.boss1_guard_l,
        temple_location_names.boss1_guard_r_1,
        temple_location_names.boss1_guard_r_2,
    ]
    boss1_entrance_region = create_region(world, active_locations, temple_region_names.boss_1_entrance,
                                          boss1_entrance_locations)

    boss1_arena_region = create_region(world, active_locations, temple_region_names.boss_1_arena, [])

    boss1_defeated_locations = [
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
    ]
    boss1_defeated_region = create_region(world, active_locations, temple_region_names.boss_1_defeated,
                                          boss1_defeated_locations)

    b1_back_locs = [
        temple_location_names.boss1_bridge,
        temple_location_names.boss1_bridge_n,
        temple_location_names.boss1_secret,
        temple_location_names.btn_b1_bridge,
    ]
    b1_back_region = create_region(world, active_locations, temple_region_names.b1_back, b1_back_locs)

    passage_entrance_locations = [
        temple_location_names.p_ent2_secret
    ]
    passage_entrance_region = create_region(world, active_locations, temple_region_names.passage_entrance,
                                            passage_entrance_locations)

    passage_mid_locations = [
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
        temple_location_names.btn_p_puzzle,
    ]
    passage_mid_region = create_region(world, active_locations, temple_region_names.passage_mid, passage_mid_locations)

    passage_puzzle_locations = [
        temple_location_names.p_puzzle_1,
        temple_location_names.p_puzzle_2,
        temple_location_names.p_puzzle_3,
        temple_location_names.p_puzzle_4,
    ]
    passage_puzzle_region = create_region(world, active_locations, temple_region_names.passage_puzzle,
                                          passage_puzzle_locations)

    passage_end_locations = [
        temple_location_names.p_end1_secret,
        temple_location_names.p_end3_1,
        temple_location_names.p_end3_2,
    ]
    passage_end_region = create_region(world, active_locations, temple_region_names.passage_end, passage_end_locations)

    temple_entrance_region = create_region(world, active_locations, temple_region_names.temple_entrance, [])

    temple_entrance_back_locations = [
        temple_location_names.temple_entrance_l,
        temple_location_names.temple_entrance_r,
        temple_location_names.ev_temple_entrance_rock,
    ]
    temple_entrance_back_region = create_region(world, active_locations, temple_region_names.temple_entrance_back,
                                                temple_entrance_back_locations)

    t1_main_locations = [
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
        temple_location_names.btn_t1_puzzle_w,
        temple_location_names.btn_t1_wall_guard,
    ]
    t1_main_region = create_region(world, active_locations, temple_region_names.t1_main, t1_main_locations)

    t1_w_puzzle_locs = [
        temple_location_names.t1_w_puzzle_1,
        temple_location_names.t1_w_puzzle_2,
        temple_location_names.t1_w_puzzle_3,
        temple_location_names.t1_w_puzzle_4,
    ]
    t1_w_puzzle_region = create_region(world, active_locations, temple_region_names.t1_w_puzzle, t1_w_puzzle_locs)

    t1_sw_sdoor_locations = [
        temple_location_names.t1_sw_sdoor_1,
        temple_location_names.t1_sw_sdoor_2,
        temple_location_names.t1_sw_sdoor_3,
        temple_location_names.t1_sw_sdoor_4,
        temple_location_names.t1_sw_sdoor_5,
    ]
    t1_sw_cache_region = create_region(world, active_locations, temple_region_names.t1_sw_sdoor, t1_sw_sdoor_locations)

    t1_node_1_locations = [
        temple_location_names.ev_t1_s_node
    ]
    t1_node_1_region = create_region(world, active_locations, temple_region_names.t1_node_1, t1_node_1_locations)

    t1_w_locations = [
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
    ]
    t1_w_region = create_region(world, active_locations, temple_region_names.t1_w, t1_w_locations)

    t1_runway_halls_locations = [
        temple_location_names.t1_mana_drain_fire_trap_passage,
    ]
    t1_runway_halls_region = create_region(world, active_locations, temple_region_names.t1_runway_halls,
                                           t1_runway_halls_locations)

    t1_sun_turret_locations = [
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
    ]
    t1_sun_turret_region = create_region(world, active_locations, temple_region_names.t1_sun_turret,
                                         t1_sun_turret_locations)

    t1_ice_turret_locations = [
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
    ]
    t1_ice_turret_region = create_region(world, active_locations, temple_region_names.t1_ice_turret,
                                         t1_ice_turret_locations)

    t1_telarian_locs = [
        temple_location_names.t1_telarian_1,
        temple_location_names.t1_telarian_2,
        temple_location_names.t1_telarian_3,
        temple_location_names.t1_telarian_4,
        temple_location_names.t1_telarian_5,
        temple_location_names.btn_t1_wall_telarian,
    ]
    t1_telarian_region = create_region(world, active_locations, temple_region_names.t1_telarian, t1_telarian_locs)

    t1_n_of_ice_turret_locations = [
        temple_location_names.t1_n_cache_by_ice_turret_1,
        temple_location_names.t1_n_cache_by_ice_turret_2,
        temple_location_names.t1_n_cache_by_ice_turret_3,
        temple_location_names.t1_n_cache_by_ice_turret_4,
        temple_location_names.t1_n_cache_by_ice_turret_5,
        temple_location_names.btn_t1_wall_n_jail,
    ]
    t1_n_of_ice_turret_region = create_region(world, active_locations, temple_region_names.t1_n_of_ice_turret,
                                              t1_n_of_ice_turret_locations)

    t1_s_of_ice_turret_locations = [
        temple_location_names.t1_s_cache_by_ice_turret_1,
        temple_location_names.t1_s_cache_by_ice_turret_2,
        temple_location_names.t1_s_cache_by_ice_turret_3,
    ]
    t1_s_of_ice_turret_region = create_region(world, active_locations, temple_region_names.t1_s_of_ice_turret,
                                              t1_s_of_ice_turret_locations)

    t1_east_locations = [
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
        temple_location_names.btn_t1_puzzle_e,
        temple_location_names.btn_t1_wall_n_hall,
        temple_location_names.btn_t1_wall_e_jail,
        temple_location_names.ev_t1_n_node_s_mirror,
    ]
    t1_east_region = create_region(world, active_locations, temple_region_names.t1_east, t1_east_locations)

    t1_ne_hall_locations = [
        temple_location_names.t1_node_2_passage_1,
        temple_location_names.t1_node_2_passage_2,
        temple_location_names.t1_node_2_passage_3,
    ]
    t1_ne_hall_region = create_region(world, active_locations, temple_region_names.t1_ne_hall, t1_ne_hall_locations)

    t1_e_puzzle_locs = [
        temple_location_names.t1_e_puzzle_1,
        temple_location_names.t1_e_puzzle_2,
        temple_location_names.t1_e_puzzle_3,
        temple_location_names.t1_e_puzzle_4,
    ]
    t1_e_puzzle_region = create_region(world, active_locations, temple_region_names.t1_e_puzzle, t1_e_puzzle_locs)

    t1_jail_e_locs = [
        temple_location_names.t1_e_gold_beetles,
    ]
    t1_jail_e_region = create_region(world, active_locations, temple_region_names.t1_jail_e, t1_jail_e_locs)

    t1_sun_block_hall_locations = [
        temple_location_names.t1_sun_block_hall_1,
        temple_location_names.t1_sun_block_hall_2,
        temple_location_names.t1_sun_block_hall_3,
        temple_location_names.t1_sun_block_hall_4,
    ]
    t1_sun_block_hall_region = create_region(world, active_locations, temple_region_names.t1_sun_block_hall,
                                             t1_sun_block_hall_locations)

    t1_node_2_locations = [
        temple_location_names.ev_t1_n_node
    ]
    t1_node_2_region = create_region(world, active_locations, temple_region_names.t1_node_2, t1_node_2_locations)

    t1_telarian_melt_ice_locations = [
        temple_location_names.t1_telarian_ice
    ]
    t1_telarian_melt_ice_region = create_region(world, active_locations, temple_region_names.t1_telarian_melt_ice,
                                                t1_telarian_melt_ice_locations)

    t1_ice_chamber_melt_ice_locations = [
        temple_location_names.t1_ice_block_chamber_ice
    ]
    t1_ice_chamber_melt_ice_region = create_region(world, active_locations, temple_region_names.t1_ice_chamber_melt_ice,
                                                   t1_ice_chamber_melt_ice_locations)
    # Dynamically place portal event location
    t1_portal_loc = HammerwatchLocation(world.player, temple_location_names.ev_t1_portal)
    if random_locations[temple_location_names.rloc_t1_portal] == 0:
        t1_east_region.locations.append(t1_portal_loc)
        t1_portal_loc.parent_region = t1_east_region
    elif random_locations[temple_location_names.rloc_t1_portal] == 1:
        t1_ice_turret_region.locations.append(t1_portal_loc)
        t1_portal_loc.parent_region = t1_ice_turret_region
    else:
        t1_sun_turret_region.locations.append(t1_portal_loc)
        t1_portal_loc.parent_region = t1_sun_turret_region

    boss2_main_region = create_region(world, active_locations, temple_region_names.boss2_main, [])

    boss2_defeated_locations = [
        temple_location_names.boss2_nw,
        temple_location_names.boss2_se,
        temple_location_names.ev_beat_boss_2
    ]
    boss2_defeated_region = create_region(world, active_locations, temple_region_names.boss2_defeated,
                                          boss2_defeated_locations)

    t2_main_locations = [
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
        temple_location_names.btn_t2_puzzle_w,
        temple_location_names.btn_t2_puzzle_e,
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
    ]
    t2_main_region = create_region(world, active_locations, temple_region_names.t2_main, t2_main_locations)

    t2_nw_puzzle_locs = [
        temple_location_names.t2_nw_puzzle_1,
        temple_location_names.t2_nw_puzzle_2,
        temple_location_names.t2_nw_puzzle_3,
        temple_location_names.t2_nw_puzzle_4,
    ]
    t2_nw_puzzle_region = create_region(world, active_locations, temple_region_names.t2_nw_puzzle, t2_nw_puzzle_locs)

    t2_e_puzzle_locs = [
        temple_location_names.t2_e_puzzle_1,
        temple_location_names.t2_e_puzzle_2,
        temple_location_names.t2_e_puzzle_3,
        temple_location_names.t2_e_puzzle_4,
    ]
    t2_e_puzzle_region = create_region(world, active_locations, temple_region_names.t2_e_puzzle, t2_e_puzzle_locs)

    t2_melt_ice_locations = [
    ]
    t2_melt_ice_region = create_region(world, active_locations, temple_region_names.t2_melt_ice, t2_melt_ice_locations)

    t2_w_ice_gate_locs = [
        temple_location_names.t2_w_ice_block_gate,
    ]
    t2_w_ice_gate_region = create_region(world, active_locations, temple_region_names.t2_w_ice_gate, t2_w_ice_gate_locs)

    t2_e_ice_gate_locs = [
        temple_location_names.t2_e_ice_block_gate,
    ]
    t2_e_ice_gate_region = create_region(world, active_locations, temple_region_names.t2_e_ice_gate, t2_e_ice_gate_locs)

    t2_n_gate_locations = [
        temple_location_names.t2_nw_ice_turret_1,
        temple_location_names.t2_nw_ice_turret_2,
        temple_location_names.t2_nw_ice_turret_3,
        temple_location_names.t2_nw_ice_turret_4,
        temple_location_names.t2_nw_under_block,
        temple_location_names.t2_nw_gate_3,
        temple_location_names.t2_tower_ice_1,
        temple_location_names.t2_tower_ice_2,
        temple_location_names.btn_t2_puzzle_n,
        temple_location_names.btn_t2_wall_nw_gate,
        temple_location_names.btn_t2_wall_jones_hall,
    ]
    t2_n_gate_region = create_region(world, active_locations, temple_region_names.t2_n_gate, t2_n_gate_locations)

    t2_n_puzzle_locs = [
        temple_location_names.t2_n_puzzle_1,
        temple_location_names.t2_n_puzzle_2,
        temple_location_names.t2_n_puzzle_3,
        temple_location_names.t2_n_puzzle_4,
    ]
    t2_n_puzzle_region = create_region(world, active_locations, temple_region_names.t2_n_puzzle, t2_n_puzzle_locs)

    t2_nw_button_gate_locs = [
        temple_location_names.t2_nw_gate_1,
        temple_location_names.t2_nw_gate_2,
    ]
    t2_nw_button_gate_region = create_region(world, active_locations, temple_region_names.t2_nw_button_gate,
                                             t2_nw_button_gate_locs)

    t2_s_gate_locations = [
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
        temple_location_names.btn_t2_puzzle_s,
        temple_location_names.btn_t2_wall_s_gate_shortcut,
        temple_location_names.btn_t2_wall_s_gate_hall,
    ]
    t2_s_gate_region = create_region(world, active_locations, temple_region_names.t2_s_gate, t2_s_gate_locations)

    t2_sw_puzzle_locs = [
        temple_location_names.t2_sw_puzzle_1,
        temple_location_names.t2_sw_puzzle_2,
        temple_location_names.t2_sw_puzzle_3,
        temple_location_names.t2_sw_puzzle_4,
    ]
    t2_sw_puzzle_region = create_region(world, active_locations, temple_region_names.t2_sw_puzzle, t2_sw_puzzle_locs)

    t2_n_node_locations = [
        temple_location_names.btn_t2_wall_n_node,
        temple_location_names.ev_t2_n_node,
    ]
    t2_n_node_region = create_region(world, active_locations, temple_region_names.t2_n_node, t2_n_node_locations)

    t2_boulder_room_locs = [
        temple_location_names.t2_boulder_room_1,
        temple_location_names.t2_boulder_room_2,
        temple_location_names.t2_boulder_room_block,
        temple_location_names.btn_t2_rune_w,
        temple_location_names.btn_t2_wall_boulder_room,
    ]
    t2_boulder_room_region = create_region(world, active_locations, temple_region_names.t2_boulder_room,
                                           t2_boulder_room_locs)

    t2_n_hidden_hall_locs = [
        temple_location_names.t2_mana_drain_fire_trap_1,
        temple_location_names.t2_mana_drain_fire_trap_2,
        temple_location_names.btn_t2_wall_n_hidden_hall,
    ]
    t2_n_hidden_hall_region = create_region(world, active_locations, temple_region_names.t2_n_hidden_hall,
                                            t2_n_hidden_hall_locs)

    t2_jones_hall_locs = [
        temple_location_names.t2_jones_hallway,
    ]
    t2_jones_hall_region = create_region(world, active_locations, temple_region_names.t2_jones_hall, t2_jones_hall_locs)

    t2_s_node_locations = [
        temple_location_names.ev_t2_s_node
    ]
    t2_s_node_region = create_region(world, active_locations, temple_region_names.t2_s_node, t2_s_node_locations)

    t2_jail_sw_locs = [
        temple_location_names.t2_gold_beetle_barricade,
        temple_location_names.t2_w_gold_beetle_room_1,
        temple_location_names.t2_w_gold_beetle_room_2,
        temple_location_names.t2_w_gold_beetle_room_3,
        temple_location_names.t2_w_gold_beetle_room_4,
        temple_location_names.btn_t2_wall_jail_w,
    ]
    t2_jail_sw_region = create_region(world, active_locations, temple_region_names.t2_jail_sw, t2_jail_sw_locs)

    t2_sdoor_gate_locs = [
        temple_location_names.t2_sw_gate,
    ]
    t2_sdoor_gate_region = create_region(world, active_locations, temple_region_names.t2_sdoor_gate, t2_sdoor_gate_locs)

    t2_pof_locs = [
        temple_location_names.t2_left_of_pof_switch_1,
        temple_location_names.t2_left_of_pof_switch_2,
        temple_location_names.btn_t2_pof_1,
        temple_location_names.btn_t2_pof_2,
        temple_location_names.btn_t2_pof_3,
        temple_location_names.btn_t2_pof_4,
        temple_location_names.btn_t2_wall_pof,
        temple_location_names.btn_t2_pof,
    ]
    t2_pof_region = create_region(world, active_locations, temple_region_names.t2_pof, t2_pof_locs)

    t2_pof_spikes_locs = [
        temple_location_names.t2_right_of_pof_switch
    ]
    t2_pof_spikes_region = create_region(world, active_locations, temple_region_names.t2_pof_spikes, t2_pof_spikes_locs)

    t2_jail_s_locs = [
        temple_location_names.btn_t2_wall_jail_s,
    ]
    t2_jail_s_region = create_region(world, active_locations, temple_region_names.t2_jail_s, t2_jail_s_locs)

    t2_ornate_locations = [
        temple_location_names.btn_t2_rune_n,
        temple_location_names.btn_t2_wall_t3_gate_e,
    ]
    t2_ornate_region = create_region(world, active_locations, temple_region_names.t2_ornate, t2_ornate_locations)

    t2_light_bridge_w_locations = [
        temple_location_names.btn_t2_floor_portal,
    ]
    t2_light_bridge_w_region = create_region(world, active_locations, temple_region_names.t2_light_bridge_w,
                                             t2_light_bridge_w_locations)

    t2_light_bridges_se_locations = [
        temple_location_names.t2_se_light_bridge_1,
        temple_location_names.t2_se_light_bridge_2,
    ]
    t2_light_bridges_se_region = create_region(world, active_locations, temple_region_names.t2_light_bridges_se,
                                               t2_light_bridges_se_locations)

    t2_light_bridges_s_locations = [
        temple_location_names.t2_s_light_bridge_1,
        temple_location_names.t2_s_light_bridge_2,
    ]
    t2_light_bridges_s_region = create_region(world, active_locations, temple_region_names.t2_light_bridges_s,
                                              t2_light_bridges_s_locations)

    t2_portal_gate_locs = [
        temple_location_names.t2_portal_gate,
    ]
    t2_portal_gate_region = create_region(world, active_locations, temple_region_names.t2_portal_gate,
                                          t2_portal_gate_locs)

    t2_ornate_t3_locations = [
        temple_location_names.t2_floor3_cache_1,
        temple_location_names.t2_floor3_cache_2,
        temple_location_names.t2_floor3_cache_3,
        temple_location_names.t2_floor3_cache_4,
        temple_location_names.t2_floor3_cache_5,
        temple_location_names.t2_floor3_cache_6,
        temple_location_names.btn_t2_wall_t3_gate_w,
    ]
    t2_ornate_t3_region = create_region(world, active_locations, temple_region_names.t2_ornate_t3,
                                        t2_ornate_t3_locations)

    t2_ornate_gate_locs = [
        temple_location_names.t2_floor3_cache_gate,
    ]
    t2_ornate_gate_region = create_region(world, active_locations, temple_region_names.t2_ornate_gate,
                                          t2_ornate_gate_locs)

    # Dynamically place portal event location
    t2_portal_loc = HammerwatchLocation(world.player, temple_location_names.ev_t2_portal)
    if random_locations[temple_location_names.rloc_t2_portal] == 0:
        t2_main_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_main_region
    elif random_locations[temple_location_names.rloc_t2_portal] == 1:
        t2_s_gate_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_s_gate_region
    elif random_locations[temple_location_names.rloc_t2_portal] == 2:
        t2_main_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_main_region
    else:
        t2_n_gate_region.locations.append(t2_portal_loc)
        t2_portal_loc.parent_region = t2_n_gate_region

    t3_main_locations = [
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
    ]
    t3_main_region = create_region(world, active_locations, temple_region_names.t3_main, t3_main_locations)

    t3_blockade_s_locs = [
        temple_location_names.btn_t3_wall_gate_s,
    ]
    t3_blockade_s_region = create_region(world, active_locations, temple_region_names.t3_blockade_s, t3_blockade_s_locs)

    t3_s_gate_locs = [
        temple_location_names.t3_s_gate,
    ]
    t3_s_gate_region = create_region(world, active_locations, temple_region_names.t3_s_gate, t3_s_gate_locs)

    t3_n_node_blocks_locations = [
        temple_location_names.t3_n_node_blocks_1,
        temple_location_names.t3_n_node_blocks_2,
        temple_location_names.t3_n_node_blocks_3,
        temple_location_names.t3_n_node_blocks_4,
        temple_location_names.t3_n_node_blocks_5,
        temple_location_names.btn_t3_wall_blockade,
    ]
    t3_n_node_blocks_region = create_region(world, active_locations, temple_region_names.t3_n_node_blocks,
                                            t3_n_node_blocks_locations)

    t3_gates_locs = [
        temple_location_names.t3_tower_ice_2,
        temple_location_names.t3_tower_ice_3,
        temple_location_names.btn_t3_levers,
        temple_location_names.btn_t3_lever_1,
        temple_location_names.btn_t3_lever_2,
        temple_location_names.btn_t3_lever_3,
        temple_location_names.btn_t3_lever_4,
    ]
    t3_gates_region = create_region(world, active_locations, temple_region_names.t3_gates, t3_gates_locs)

    t3_puzzle_room_locs = [
        temple_location_names.btn_t3_puzzle,
    ]
    t3_puzzle_room_region = create_region(world, active_locations, temple_region_names.t3_puzzle_room,
                                          t3_puzzle_room_locs)

    t3_puzzle_locs = [
        temple_location_names.t3_puzzle_1,
        temple_location_names.t3_puzzle_2,
        temple_location_names.t3_puzzle_3,
        temple_location_names.t3_puzzle_4,
    ]
    t3_puzzle_region = create_region(world, active_locations, temple_region_names.t3_puzzle, t3_puzzle_locs)

    t3_n_node_locations = [
        temple_location_names.ev_t3_n_node
    ]
    t3_n_node_region = create_region(world, active_locations, temple_region_names.t3_n_node, t3_n_node_locations)

    t3_s_node_blocks_1_locations = [
        temple_location_names.t3_s_node_cache_1,
        temple_location_names.t3_s_node_cache_2,
        temple_location_names.t3_s_node_cache_3,
    ]
    t3_s_node_blocks_1_region = create_region(world, active_locations, temple_region_names.t3_s_node_blocks_1,
                                              t3_s_node_blocks_1_locations)

    t3_s_node_blocks_2_locations = [
        temple_location_names.t3_m_balcony_corridor,
    ]
    t3_s_node_blocks_2_region = create_region(world, active_locations, temple_region_names.t3_s_node_blocks_2,
                                              t3_s_node_blocks_2_locations)

    t3_s_node_locations = [
        temple_location_names.t3_n_node_1,
        temple_location_names.t3_n_node_2,
        temple_location_names.t3_n_node_3,
        temple_location_names.ev_t3_s_node,
    ]
    t3_s_node_region = create_region(world, active_locations, temple_region_names.t3_s_node, t3_s_node_locations)

    t3_boss_fall_1_locations = [
        temple_location_names.t3_boss_fall_1_1,
        temple_location_names.t3_boss_fall_1_2,
        temple_location_names.t3_boss_fall_1_3,
        temple_location_names.btn_t3_wall_fall_1,
    ]
    t3_boss_fall_1_region = create_region(world, active_locations, temple_region_names.t3_boss_fall_1,
                                          t3_boss_fall_1_locations)

    t3_boss_fall_2_locations = [
        temple_location_names.t3_boss_fall_2_1,
        temple_location_names.t3_boss_fall_2_2,
        temple_location_names.t3_boss_fall_2_3,
        temple_location_names.btn_t3_wall_fall_2,
    ]
    t3_boss_fall_2_region = create_region(world, active_locations, temple_region_names.t3_boss_fall_2,
                                          t3_boss_fall_2_locations)

    t3_boss_fall_3_locations = [
        temple_location_names.t3_boss_fall_3_1,
        temple_location_names.t3_boss_fall_3_2,
        temple_location_names.t3_boss_fall_3_3,
        temple_location_names.t3_boss_fall_3_4,
        temple_location_names.btn_t3_wall_fall_3,
    ]
    t3_boss_fall_3_region = create_region(world, active_locations, temple_region_names.t3_boss_fall_3,
                                          t3_boss_fall_3_locations)

    pof_1_main_locations = [
        temple_location_names.pof_1_ent_1,
        temple_location_names.pof_1_ent_2,
        temple_location_names.pof_1_ent_3,
        temple_location_names.pof_1_ent_4,
        temple_location_names.pof_1_ent_5,
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
    ]
    pof_1_main_region = create_region(world, active_locations, temple_region_names.pof_1_main, pof_1_main_locations)

    pof_1_se_room_locations = [
        temple_location_names.btn_pof_1_panel_se,
    ]
    pof_1_se_room_region = create_region(world, active_locations, temple_region_names.pof_1_se_room,
                                         pof_1_se_room_locations)

    pof_1_se_room_top_locs = [
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
    ]
    pof_1_se_room_top_region = create_region(world, active_locations, temple_region_names.pof_1_se_room_top,
                                             pof_1_se_room_top_locs)

    pof_1_sw_gate_locs = [
    ]
    pof_1_sw_gate_region = create_region(world, active_locations, temple_region_names.pof_1_sw_gate, pof_1_sw_gate_locs)

    pof_1_nw_locs = [
        temple_location_names.pof_1_confuse_corner_1,
        temple_location_names.pof_1_confuse_corner_2,
        temple_location_names.pof_1_confuse_corner_3,
        temple_location_names.pof_1_confuse_corner_4,
    ]
    pof_1_nw_region = create_region(world, active_locations, temple_region_names.pof_1_nw, pof_1_nw_locs)

    pof_1_n_room_locations = [
        temple_location_names.pof_1_n_1,
        temple_location_names.pof_1_n_2,
        temple_location_names.pof_1_n_3,
        temple_location_names.pof_1_n_4,
        temple_location_names.pof_1_n_5,
        temple_location_names.pof_1_n_6,
        temple_location_names.pof_1_n_7,
        temple_location_names.pof_1_n_8,
        temple_location_names.pof_1_n_9,
        temple_location_names.btn_pof_1_panel_n
    ]
    pof_1_n_room_region = create_region(world, active_locations, temple_region_names.pof_1_n_room,
                                        pof_1_n_room_locations)

    pof_1_exit_hall_locs = [
        temple_location_names.pof_1_c_hall_1,
        temple_location_names.pof_1_c_hall_2,
        temple_location_names.pof_1_c_hall_3,
        temple_location_names.pof_1_c_hall_4,
        temple_location_names.pof_1_c_hall_5,
        temple_location_names.pof_1_c_hall_6,
    ]
    pof_1_exit_hall_region = create_region(world, active_locations, temple_region_names.pof_1_exit_hall,
                                           pof_1_exit_hall_locs)

    pof_1_gate_2_locations = [
        temple_location_names.pof_1_end_1,
        temple_location_names.pof_1_end_2,
        temple_location_names.pof_1_end_3,
        temple_location_names.pof_1_end_4,
        temple_location_names.pof_1_end_5,
    ]
    pof_1_gate_2_region = create_region(world, active_locations, temple_region_names.pof_1_gate_2,
                                        pof_1_gate_2_locations)

    pof_2_main_locations = [
        temple_location_names.pof_2_ent_1,
        temple_location_names.pof_2_ent_2,
        temple_location_names.pof_2_ent_3,
        temple_location_names.pof_2_ent_4,
        temple_location_names.pof_2_ent_5,
        temple_location_names.pof_2_ent_6,
        temple_location_names.pof_2_confuse_hall_1,
        temple_location_names.pof_2_confuse_hall_2,
        temple_location_names.pof_2_confuse_hall_3,
        temple_location_names.pof_2_confuse_hall_4,
        temple_location_names.pof_2_sw_1,
        temple_location_names.pof_2_sw_2,
        temple_location_names.pof_2_sw_3,
        temple_location_names.pof_2_sw_4,
    ]
    pof_2_main_region = create_region(world, active_locations, temple_region_names.pof_2_main, pof_2_main_locations)

    pof_2_n_locations = [
        temple_location_names.pof_2_ne_1,
        temple_location_names.pof_2_ne_2,
        temple_location_names.pof_2_ne_3,
        temple_location_names.pof_2_ne_4,
        temple_location_names.btn_pof_2_panel_e,
    ]
    pof_2_n_region = create_region(world, active_locations, temple_region_names.pof_2_n, pof_2_n_locations)

    pof_2_puzzle_locs = [
        temple_location_names.btn_pof_2_panel_w,
        temple_location_names.btn_pof_puzzle,
    ]
    pof_2_puzzle_region = create_region(world, active_locations, temple_region_names.pof_2_puzzle, pof_2_puzzle_locs)

    pof_puzzle_locs = [
        temple_location_names.pof_puzzle_1,
        temple_location_names.pof_puzzle_2,
        temple_location_names.pof_puzzle_3,
        temple_location_names.pof_puzzle_4,
    ]
    pof_puzzle_region = create_region(world, active_locations, temple_region_names.pof_puzzle, pof_puzzle_locs)

    pof_2_exit_locations = [
    ]
    pof_2_exit_region = create_region(world, active_locations, temple_region_names.pof_2_exit, pof_2_exit_locations)

    pof_3_start_locs = [
        temple_location_names.pof_3_safety_room_1,
        temple_location_names.pof_3_safety_room_2,
        temple_location_names.pof_3_safety_room_3,
        temple_location_names.btn_pof_3_panel,
    ]
    pof_3_start_region = create_region(world, active_locations, temple_region_names.pof_3_start, pof_3_start_locs)

    pof_3_main_locations = [
        temple_location_names.pof_3_end_1,
        temple_location_names.pof_3_end_2,
        temple_location_names.pof_3_end_3,
        temple_location_names.pof_3_end_4,
        temple_location_names.pof_3_end_5,
        temple_location_names.ev_pof_end,
    ]
    pof_3_main_region = create_region(world, active_locations, temple_region_names.pof_3_main, pof_3_main_locations)

    b3_main_region = create_region(world, active_locations, temple_region_names.b3_main, [])
    b3_platform_1_locs = [
        temple_location_names.b3_tower_fire_2,
    ]
    b3_platform_1_region = create_region(world, active_locations, temple_region_names.b3_platform_1, b3_platform_1_locs)
    b3_platform_2_locs = [
        temple_location_names.b3_tower_fire_1,
    ]
    b3_platform_2_region = create_region(world, active_locations, temple_region_names.b3_platform_2, b3_platform_2_locs)
    b3_platform_3_locs = [
        temple_location_names.b3_tower_fire_3,
    ]
    b3_platform_3_region = create_region(world, active_locations, temple_region_names.b3_platform_3, b3_platform_3_locs)

    b3_defeated_locations = [
        temple_location_names.ev_beat_boss_3,
    ]
    b3_defeated_region = create_region(world, active_locations, temple_region_names.b3_defeated, b3_defeated_locations)

    world.multiworld.regions += [
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
        t1_runway_halls_region,
        t1_node_1_region,
        t1_node_2_region,
        t1_sun_turret_region,
        t1_ice_turret_region,
        t1_telarian_region,
        t1_n_of_ice_turret_region,
        t1_s_of_ice_turret_region,
        t1_east_region,
        t1_ne_hall_region,
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
        t3_puzzle_room_region,
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
    ]


def connect_tots_regions(world: "HammerwatchWorld", random_locations: typing.Dict[str, int],
                         gate_codes: typing.Dict[str, str]):
    used_names: typing.Dict[str, int] = {}

    gate_counts: typing.Dict[str, int] = {
        item_name.key_silver: 6,
        item_name.key_gold: 4,
    }

    pan_item = item_name.pan
    # lever_item = item_name.lever
    pickaxe_item = item_name.pickaxe
    pan_item_count = world.options.pan_fragments.value
    # lever_item_count = world.options.lever_fragments.value
    pickaxe_item_count = world.options.pickaxe_fragments.value
    if pan_item_count > 1:
        pan_item = item_name.pan_fragment
    # if lever_item_count > 1:
    #     lever_item = item_name.lever_fragment
    if pickaxe_item_count > 1:
        pickaxe_item = item_name.pickaxe_fragment

    # If not doing entrance randomization or randomizing the start we start in the normal spot
    if not (world.options.exit_randomization.value and world.options.random_start_exit.value):
        connect(world, used_names, temple_region_names.menu, temple_region_names.hub_main, False)

    buttonsanity = world.options.buttonsanity.value > 0

    connect(world, used_names, temple_region_names.hub_main, temple_region_names.hub_rocks,
            False, pickaxe_item, pickaxe_item_count, False)
    # Actually one-way because you need to talk to Lyron to clear the rocks, and he's on the shop side
    connect_exit(world, used_names, temple_region_names.hub_rocks, temple_region_names.cave_3_fall,
                 entrance_names.t_c1_fall_surface, None)
    # For the temple entrances in the hub
    t3_entrance = temple_region_names.t3_main
    if random_locations[temple_location_names.rloc_t3_entrance] == 2:
        t3_entrance = temple_region_names.t3_blockade_s
    t3_entrance_code = f"t3|{random_locations[temple_location_names.rloc_t3_entrance]}"
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
    connect(world, used_names, temple_region_names.cave_3_main, temple_region_names.c3_puzzle, False,
            item_name.btn_c3_puzzle, 1, False, buttonsanity)
    connect_or(world, used_names, temple_region_names.cave_3_main, temple_region_names.c3_e, True,
              [item_name.btn_c3_e_bridge, item_name.btn_c2_pumps])
    connect(world, used_names, temple_region_names.cave_3_fall, temple_region_names.cave_3_main, False,
            item_name.btn_c3_fall_bridge, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_3_secret, temple_region_names.cave_3_main, False)
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

    connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.cave_2_pumps,
            False, item_name.btn_c2_pumps, 1, False)
    connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_red_bridge, False,
            item_name.btn_c2_red, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_green_bridge, False,
            item_name.btn_c2_green, 1, False, buttonsanity)
    if buttonsanity:
        connect_or(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_sw, False,
                   [item_name.btn_c2_green, item_name.btn_c2_s_bridge])
        connect(world, used_names, temple_region_names.c2_sw, temple_region_names.cave_2_main, False)
        # Can go through the breakable wall
        connect(world, used_names, temple_region_names.c2_sw, temple_region_names.c2_double_bridge, True,
                item_name.btn_c2_bridges, 1, False)
        connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_double_bridge, True,
                item_name.btn_c2_bridges, 1, False)
    else:
        connect(world, used_names, temple_region_names.cave_2_main, temple_region_names.c2_sw, True)
        connect(world, used_names, temple_region_names.c2_sw, temple_region_names.c2_double_bridge, False)
    # Both require green switch
    connect(world, used_names, temple_region_names.c2_sw, temple_region_names.c2_puzzle, False,
            item_name.btn_c2_puzzle, 1, False, buttonsanity)
    # Two-way
    # connect_generic(multiworld, player, used_names, temple_region_names.c2_double_bridge, temple_region_names.cave_2_main)
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

    connect(world, used_names, temple_region_names.cave_1_main, temple_region_names.c1_n_puzzle, False,
            item_name.btn_c1_puzzle_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.cave_1_main, temple_region_names.cave_1_blue_bridge, buttonsanity,
            item_name.btn_c1_blue, 1, False, buttonsanity)
    c1_no_e_shortcut = random_locations[temple_location_names.rloc_c1_hall_e] >= 2
    connect(world, used_names, temple_region_names.cave_1_blue_bridge, temple_region_names.cave_1_red_bridge, buttonsanity,
            item_name.btn_c1_red, 1, False, c1_no_e_shortcut and buttonsanity)
    if buttonsanity:
        connect(world, used_names, temple_region_names.cave_1_blue_bridge, temple_region_names.cave_1_green_bridge, True,
                item_name.btn_c1_green, 1, False)
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
                 entrance_names.t_b2, entrance_names.t_c3_boss)
    # Technically a level exit, but we need to be able to go to the defeated room from anywhere rip
    connect(world, used_names, temple_region_names.boss2_main, temple_region_names.boss2_defeated, False)

    connect(world, used_names, temple_region_names.cave_1_red_bridge, temple_region_names.c1_e_puzzle, False,
            item_name.btn_c1_puzzle_e, 1, False, buttonsanity)
    if world.options.exit_randomization.value:
        if world.options.portal_accessibility.value:
            connect_exit(world, used_names, temple_region_names.cave_1_red_bridge,
                         temple_region_names.boss_1_entrance, entrance_names.t_b1_start, entrance_names.t_c3_end)
        else:
            connect_exit(world, used_names, temple_region_names.cave_1_red_bridge,
                         temple_region_names.boss_1_entrance, entrance_names.t_b1_start, entrance_names.t_c3_end,
                         item_name.key_teleport, 1, True)
    else:
        connect_exit(world, used_names, temple_region_names.cave_1_red_bridge,
                     temple_region_names.boss_1_entrance, entrance_names.t_b1_start, entrance_names.t_c3_end,
                     item_name.key_teleport, 3, False)

    connect(world, used_names, temple_region_names.boss_1_entrance, temple_region_names.boss_1_arena,
            True)  # We shouldn't include boss teleporters in ER, it's kinda mean lol
    connect(world, used_names, temple_region_names.boss_1_arena, temple_region_names.boss_1_defeated, False)
    connect_gate(world, used_names, temple_region_names.boss_1_arena, temple_region_names.b1_back,
                 item_name.key_gold, gate_codes, gate_counts, gate_names.t_b1_0, True)
    connect(world, used_names, temple_region_names.b1_back, temple_region_names.boss_1_entrance, buttonsanity,
            item_name.btn_b1_bridge, 1, False, buttonsanity)

    passage_entrance = entrance_names.t_p_ent_start if random_locations[temple_location_names.rloc_passage_entrance] == 0\
        else entrance_names.t_p_ent_start_2
    connect_exit(world, used_names, temple_region_names.b1_back, temple_region_names.passage_entrance,
                 passage_entrance, entrance_names.t_b1_end)
    passage_mid = f"passage|{random_locations[temple_location_names.rloc_passage_middle] + 1}0"
    connect_exit(world, used_names, temple_region_names.passage_entrance, temple_region_names.passage_mid,
                 passage_mid, entrance_names.t_p_ent_exit)
    connect(world, used_names, temple_region_names.passage_mid, temple_region_names.passage_puzzle, False,
            item_name.btn_p_puzzle, 1, False, buttonsanity)
    passage_end = f"passage|1{random_locations[temple_location_names.rloc_passage_end] + 1}0"
    connect_exit(world, used_names, temple_region_names.passage_mid, temple_region_names.passage_end,
                 passage_end, f"passage|{random_locations[temple_location_names.rloc_passage_middle] + 1}1")

    connect_exit(world, used_names, temple_region_names.passage_end, temple_region_names.temple_entrance_back,
                 entrance_names.t_t_ent_p, entrance_names.t_p_end_end)
    connect(world, used_names, temple_region_names.temple_entrance_back, temple_region_names.temple_entrance,
            False)
    connect_exit(world, used_names, temple_region_names.temple_entrance_back, temple_region_names.t1_main,
                 entrance_names.t_t1_start, entrance_names.t_t_ent_temple)

    connect(world, used_names, temple_region_names.t1_main, temple_region_names.t1_w_puzzle, False,
            item_name.btn_t1_puzzle_w, 1, False, buttonsanity)
    connect_gate(world, used_names, temple_region_names.t1_main, temple_region_names.t1_sw_sdoor,
                 item_name.key_silver, gate_codes, gate_counts, gate_names.t_t1_3, False)
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
                 item_name.key_silver, gate_codes, gate_counts, gate_names.t_t1_1, False)
    connect_gate(world, used_names, temple_region_names.t1_w, temple_region_names.t1_ice_turret,
                 item_name.key_gold, gate_codes, gate_counts, gate_names.t_t1_4, True)
    connect(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_telarian, False,
            item_name.btn_t1_telarian, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_telarian_melt_ice, False,
            item_name.evt_beat_boss_2, 1, False)
    connect_gate(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_n_of_ice_turret,
                 item_name.key_silver, gate_codes, gate_counts, gate_names.t_t1_0, False)
    connect_gate(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_s_of_ice_turret,
                 item_name.key_silver, gate_codes, gate_counts, gate_names.t_t1_2, False)
    connect_gate(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_east,
                 item_name.key_gold, gate_codes, gate_counts, gate_names.t_t1_5, True)
    connect(world, used_names, temple_region_names.t1_ice_turret, temple_region_names.t1_sun_block_hall,
            False, item_name.mirror, 3)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_node_2,
            False, item_name.mirror, 1)  # For future reference both these have extra stuff set in Rules.py
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_ice_chamber_melt_ice, False,
            item_name.evt_beat_boss_2, 1, False)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_jail_e, False,
            item_name.btn_t1_jail_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_e_puzzle, False,
            item_name.btn_t1_puzzle_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t1_east, temple_region_names.t1_ne_hall, False,
            item_name.btn_t1_hall, 1, False, buttonsanity)

    if world.options.exit_randomization.value:
        if world.options.portal_accessibility.value:
            connect_exit(world, used_names, temple_region_names.t1_east, temple_region_names.t2_main,
                         f"t2|{random_locations[temple_location_names.rloc_t2_entrance]}", entrance_names.t_t1_end)
            connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_main, False)
        else:
            connect_exit(world, used_names, temple_region_names.t1_east, temple_region_names.t2_main,
                         f"t2|{random_locations[temple_location_names.rloc_t2_entrance]}", entrance_names.t_t1_end,
                         item_name.key_teleport, 1, True)
            connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_main, False,
                    item_name.key_teleport, 1, True)
    else:
        connect_exit(world, used_names, temple_region_names.t1_east, temple_region_names.t2_main,
                     f"t2|{random_locations[temple_location_names.rloc_t2_entrance]}", entrance_names.t_t1_end,
                     item_name.key_teleport, 4, False)

    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_nw_puzzle, False,
            item_name.btn_t2_puzzle_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_e_puzzle, False,
            item_name.btn_t2_puzzle_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_main, temple_region_names.t2_melt_ice,
            True, item_name.evt_beat_boss_2, 1, False)
    connect(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_w_ice_gate, False,
            item_name.btn_t2_ice_gate_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_e_ice_gate, False,
            item_name.btn_t2_ice_gate_e, 1, False, buttonsanity)
    connect_gate(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_n_gate,
                 item_name.key_silver, gate_codes, gate_counts, gate_names.t_t2_0, False)
    connect_gate(world, used_names, temple_region_names.t2_melt_ice, temple_region_names.t2_s_gate,
                 item_name.key_silver, gate_codes, gate_counts, gate_names.t_t2_1, False)
    connect(world, used_names, temple_region_names.t2_s_gate, temple_region_names.t2_sdoor_gate, False,
            item_name.btn_t2_s_gate_shortcut, 1, False, buttonsanity)
    # Technically should be two-way, but you have to have been to t2_main before getting here so it's not needed
    connect_gate(world, used_names, temple_region_names.t2_main, temple_region_names.t2_ornate,
                 item_name.key_gold, gate_codes, gate_counts, gate_names.t_t2_2, False)
    connect(world, used_names, temple_region_names.t2_ornate, temple_region_names.t2_ornate_gate, buttonsanity,
            item_name.btn_t2_t3_gate_e, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_ornate_t3, temple_region_names.t2_ornate_gate, buttonsanity,
            item_name.btn_t2_t3_gate_w, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_n_gate, temple_region_names.t2_n_puzzle, False,
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
    connect(world, used_names, temple_region_names.t2_boulder_room, temple_region_names.t2_n_hidden_hall,False,
            item_name.btn_t2_s_gate_hall, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_n_hidden_hall, temple_region_names.t2_jones_hall, False,
            item_name.btn_t2_jones_hall_back, 1, False, buttonsanity)
    connect(world, used_names, temple_region_names.t2_s_gate, temple_region_names.t2_sw_puzzle, False,
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

    if world.options.buttonsanity != world.options.buttonsanity.option_insanity:
        connect_exit(world, used_names, temple_region_names.hub_main, temple_region_names.pof_1_main,
                     entrance_names.t_n1_1_start, entrance_names.t_hub_pof,
                     item_name.btn_pof, 6, False, False)
    else:
        connect_exit(world, used_names, temple_region_names.hub_main, temple_region_names.pof_1_main,
                     entrance_names.t_n1_1_start, entrance_names.t_hub_pof,
                     item_name.btn_pof_part, 24, False, False)
    connect_exit(world, used_names, temple_region_names.pof_1_main, temple_region_names.hub_main,
                 entrance_names.t_hub_pof, entrance_names.t_n1_1_start, None, 1, False, False)
    # Going back to the hub has no entrance requirements
    connect_exit(world, used_names, temple_region_names.pof_1_main, temple_region_names.pof_1_se_room,
                 entrance_names.t_n1_1_se, entrance_names.t_n1_1_sw)
    connect(world, used_names, temple_region_names.pof_1_se_room, temple_region_names.pof_1_se_room_top, False,
            item_name.btn_pof_1_walls_s, 1, False)
    connect(world, used_names, temple_region_names.pof_1_main, temple_region_names.pof_1_sw_gate, False,
            item_name.btn_pof_1_walls_s, 1, False)
    connect(world, used_names, temple_region_names.pof_1_sw_gate, temple_region_names.pof_1_nw, False,
            item_name.key_bonus)
    connect_exit(world, used_names, temple_region_names.pof_1_nw, temple_region_names.pof_1_n_room,
                 entrance_names.t_n1_1_n, entrance_names.t_n1_1_ne)
    connect(world, used_names, temple_region_names.pof_1_nw, temple_region_names.pof_1_exit_hall, True,
            item_name.btn_pof_1_exit, 1, False)
    connect(world, used_names, temple_region_names.pof_1_exit_hall, temple_region_names.pof_1_gate_2, True,
            item_name.key_bonus)
    connect_exit(world, used_names, temple_region_names.pof_1_gate_2, temple_region_names.pof_2_main,
                 entrance_names.t_n1_2_start, None)  # entrance_names.t_n1_20)
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

    connect(world, used_names, temple_region_names.hub_main, temple_region_names.b3_main,
            True, item_name.ev_solar_node, 6, False)  # Ignoring for ER, kinda dumb
    connect(world, used_names, temple_region_names.b3_main, temple_region_names.b3_platform_1, False)
    connect(world, used_names, temple_region_names.b3_platform_1, temple_region_names.b3_platform_2, False)
    connect(world, used_names, temple_region_names.b3_platform_2, temple_region_names.b3_platform_3, False)
    connect(world, used_names, temple_region_names.b3_platform_3, temple_region_names.b3_defeated, False)

    # For the kill final boss goal and ER it's kinda silly to randomize the fall exits, but I feel it's good for others
    if get_goal_type(world) == GoalType.KillBosses:
        connect(world, used_names, temple_region_names.b3_platform_1, temple_region_names.t3_boss_fall_1, False)
        connect(world, used_names, temple_region_names.b3_platform_2, temple_region_names.t3_boss_fall_2, False)
        connect(world, used_names, temple_region_names.b3_platform_3, temple_region_names.t3_boss_fall_3, False)
    else:
        connect_exit(world, used_names, temple_region_names.b3_platform_1, temple_region_names.t3_boss_fall_1,
                     entrance_names.t_t3_fall_1, None, None, 1, False)
        connect_exit(world, used_names, temple_region_names.b3_platform_2, temple_region_names.t3_boss_fall_2,
                     entrance_names.t_t3_fall_2, None, None, 1, False)
        connect_exit(world, used_names, temple_region_names.b3_platform_3, temple_region_names.t3_boss_fall_3,
                     entrance_names.t_t3_fall_3, None, None, 1, False)


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

    entrance_name = get_entrance_name(used_names, source, target)

    if not use_pass_item:
        pass_item = None

    rule_item = None
    if pass_item and not items_consumed:
        rule_item = pass_item
        # pass_item = None

    connection = HWEntrance(world.player, entrance_name, source_region, target_region,
                            pass_item, item_count, items_consumed, None)
    # if rule_item and use_pass_item:
    #     add_rule(connection, lambda state: state.has(rule_item, world.player, item_count), "and")

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect(world, used_names, target, source, False, pass_item, item_count, items_consumed, use_pass_item)

    return connection


def connect_or(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str, two_way: bool,
               pass_items: typing.List[str]):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    entrance_name = get_entrance_name(used_names, source, target)

    connection = HWEntrance(world.player, entrance_name, source_region, target_region,
                            None, 1, False, None)
    add_rule(connection, lambda state: state.has_any(pass_items, world.player), "and")

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect_or(world, used_names, target, source, False, pass_items)

    return connection


def connect_gate(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str, key_type: str,
                 gate_codes: typing.Dict[str, str], gate_items: typing.Dict[str, int], gate_code: str, two_way: bool):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    entrance_name = get_entrance_name(used_names, source, target)

    key_item_name = key_type
    if world.options.gate_shuffle.value:
        key_item_name = get_random_element(world, gate_items)
        gate_items[key_item_name] -= 1
        if gate_items[key_item_name] == 0:
            gate_items.pop(key_item_name)
        gate_codes[gate_code] = key_item_name.split(" ")[-2].lower()

    connection = HWEntrance(world.player, entrance_name, source_region, target_region, key_item_name, 1, True, None)

    source_region.exits.append(connection)
    connection.connect(target_region)

    if two_way:
        connect(world, used_names, target, source, False, key_item_name, 1, True)


def connect_exit(world: "HammerwatchWorld", used_names: typing.Dict[str, int], source: str, target: str,
                 exit_code: str, return_code: str = None, pass_item: str = None, item_count=1, items_consumed=True,
                 two_way=True):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    entrance_name = get_entrance_name(used_names, source, target)

    connection = HWEntrance(world.player, entrance_name, source_region, target_region,
                            pass_item, item_count, items_consumed, return_code, exit_code)
    source_region.exits.append(connection)
    if world.options.exit_randomization.value == 0 or (world.options.exit_randomization.value == 1 and
            (exit_code.startswith("boss") or (return_code is not None and return_code.startswith("boss")))):
        connection.connect(target_region)
    else:
        connection.linked = False
        world.level_exits.append(connection)

    if two_way and return_code is not None:
        connect_exit(world, used_names, target, source, return_code, exit_code, pass_item, item_count,
                     items_consumed, False)


def connect_from_data(world: "HammerwatchWorld", data: HWExitData):
    connect(world, {}, data.parent, data.target, False,
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
