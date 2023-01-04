import typing
from random import Random

from BaseClasses import MultiWorld, Region, RegionType, Entrance
from .Items import HammerwatchItem
from .Locations import HammerwatchLocation, LocationData, LocationClassification, random_locations
from .Names import CastleLocationNames, TempleLocationNames, ItemName, CastleRegionNames, TempleRegionNames
from .Util import Counter, Campaign


def create_regions(multiworld, map: Campaign, player: int, active_locations: typing.Dict[str, LocationData]):
    if map == Campaign.Castle:
        create_castle_regions(multiworld, player, active_locations)
    else:
        create_tots_regions(multiworld, player, active_locations)


def create_castle_regions(multiworld, player: int, active_locations: typing.Dict[str, LocationData]):
    menu_region = create_region(multiworld, player, active_locations, CastleRegionNames.menu, None)

    p1_start_locations = [
        CastleLocationNames.p1_entrance_1,
        CastleLocationNames.p1_entrance_2,
        CastleLocationNames.p1_entrance_3,
        CastleLocationNames.p1_entrance_4,
        CastleLocationNames.p1_entrance_hall_1,
        CastleLocationNames.p1_entrance_hall_2,
        CastleLocationNames.p1_entrance_s,
        CastleLocationNames.p1_entrance_w,
        CastleLocationNames.p1_by_nw_bronze_gate,
        CastleLocationNames.p1_entrance_secret,
    ]
    p1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.p1_start,
                                    p1_start_locations)

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

    p2_n_locations = [
        CastleLocationNames.p2_spike_puzzle_w_1,
        CastleLocationNames.p2_spike_puzzle_w_2,
        CastleLocationNames.p2_spike_puzzle_e_1,
        CastleLocationNames.p2_spike_puzzle_e_2,
        CastleLocationNames.p2_spike_puzzle_ne_1,
        CastleLocationNames.p2_spike_puzzle_ne_2,
        CastleLocationNames.p2_spike_puzzle_ne_3,
        CastleLocationNames.p2_spike_puzzle_e,
        CastleLocationNames.p2_spike_puzzle_n_1,
        CastleLocationNames.p2_spike_puzzle_n_2,
    ]
    p2_n_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_n, p2_n_locations)

    p2_red_switch_locations = [
        CastleLocationNames.p2_by_red_spikes_1,
        CastleLocationNames.p2_by_red_spikes_2,
        CastleLocationNames.p2_by_red_spikes_3,
        CastleLocationNames.p2_e_save,
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
        CastleLocationNames.p2_puzzle_1,
        CastleLocationNames.p2_puzzle_2,
        CastleLocationNames.p2_puzzle_3,
        CastleLocationNames.p2_puzzle_4,
    ]
    p2_red_switch_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_red_switch,
                                         p2_red_switch_locations)

    p2_e_bronze_gate_locations = [
        # Offense shop
    ]
    p2_e_bronze_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_e_bronze_gate,
                                            p2_e_bronze_gate_locations)

    p2_s_locations = [
        CastleLocationNames.p2_big_bridge_1,
        CastleLocationNames.p2_big_bridge_2,
        CastleLocationNames.p2_big_bridge_3,
        CastleLocationNames.p2_sequence_puzzle_reward,
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
        CastleLocationNames.p2_beetle_boss_hidden_room_1,
        CastleLocationNames.p2_beetle_boss_hidden_room_2,
        CastleLocationNames.p2_toggle_spike_trap_reward_1,
        CastleLocationNames.p2_toggle_spike_trap_reward_2,
        CastleLocationNames.p2_toggle_spike_trap_reward_3,
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

    p2_end_locations = [
        CastleLocationNames.p2_end_1,
        CastleLocationNames.p2_end_2,
    ]
    p2_end_region = create_region(multiworld, player, active_locations, CastleRegionNames.p2_end, p2_end_locations)

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
    ]
    p3_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_start, p3_start_locs)

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
        CastleLocationNames.p3_red_spike_room,
        CastleLocationNames.p3_spike_trap_1,
        CastleLocationNames.p3_spike_trap_2,
        CastleLocationNames.p3_spike_trap_3,
        CastleLocationNames.p3_ne_se_1,
        CastleLocationNames.p3_ne_se_2,
        CastleLocationNames.p3_ne_of_bridge_1,
        CastleLocationNames.p3_ne_of_bridge_2,
        CastleLocationNames.p3_secret_secret,
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
        CastleLocationNames.p3_w_of_w_poker,
        CastleLocationNames.p3_s_of_w_poker,
        CastleLocationNames.p3_nw_of_bridge,
        CastleLocationNames.p3_n_of_bridge_1,
        CastleLocationNames.p3_n_of_bridge_2,
        CastleLocationNames.p3_n_of_bridge_3,
        CastleLocationNames.p3_n_of_bridge_4,
        CastleLocationNames.p3_n_of_bridge_5,
        CastleLocationNames.p3_w_of_bridge,
        CastleLocationNames.p3_ne_e_1,
        CastleLocationNames.p3_ne_e_2,
        CastleLocationNames.p3_ne_e_3,
        CastleLocationNames.p3_ne_e_4,
        CastleLocationNames.p3_e_of_bridge_1,
        CastleLocationNames.p3_e_of_bridge_2,
        CastleLocationNames.p3_e_of_bridge_3,
        CastleLocationNames.p3_s_of_boss_door,
        CastleLocationNames.p3_secret_arrow_hall_1,
        CastleLocationNames.p3_secret_arrow_hall_2,
        CastleLocationNames.p3_s_of_e_poker_1,
        CastleLocationNames.p3_s_of_e_poker_2,
        CastleLocationNames.p3_se_of_w_shop,
        CastleLocationNames.p3_sw_of_w_shop,
        CastleLocationNames.p3_by_m_shop_1,
        CastleLocationNames.p3_by_m_shop_2,
    ]
    p3_n_gold_gate_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_n_gold_gate,
                                          p3_n_gold_gate_locs)

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

    p3_portal_from_p1_locs = [
        CastleLocationNames.p3_skip_boss_switch_1,
        CastleLocationNames.p3_skip_boss_switch_2,
        CastleLocationNames.p3_skip_boss_switch_3,
        CastleLocationNames.p3_skip_boss_switch_4,
        CastleLocationNames.p3_skip_boss_switch_5,
        CastleLocationNames.p3_skip_boss_switch_6,
        CastleLocationNames.ev_p3_boss_switch_skip,
    ]
    p3_portal_from_p1_region = create_region(multiworld, player, active_locations, CastleRegionNames.p3_portal_from_p1,
                                             p3_portal_from_p1_locs)
    # Don't add this region yet until I can figure out a good way to deal with this

    n1_start_locs = [
        CastleLocationNames.n1_entrance
    ]
    n1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_start, n1_start_locs)

    n1_room1_locs = [
        CastleLocationNames.n1_room1
    ]
    n1_room1_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room1, n1_room1_locs)

    n1_room2_locs = [
        CastleLocationNames.n1_room2_small_box,
        CastleLocationNames.n1_room2_s_1,
        CastleLocationNames.n1_room2_s_2,
        CastleLocationNames.n1_room2_s_3,
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
        CastleLocationNames.n1_room2_n_secret_room,
    ]
    n1_room2_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room2, n1_room2_locs)

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
        CastleLocationNames.n1_room3_sealed_room_1,
        CastleLocationNames.n1_room3_sealed_room_2,
        CastleLocationNames.n1_room3_sealed_room_3,
        CastleLocationNames.n1_room3_sealed_room_4,
    ]
    n1_room3_region = create_region(multiworld, player, active_locations, CastleRegionNames.n1_room3, n1_room3_locs)

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
        CastleLocationNames.b1_reward
    ]
    b1_defeated_region = create_region(multiworld, player, active_locations, CastleRegionNames.b1_defeated,
                                       b1_defeated_locs)

    a1_start_locs = [
    ]
    a1_start_region = create_region(multiworld, player, active_locations, CastleRegionNames.a1_start, a1_start_locs)

    b4_defeated_locations = []
    if multiworld.goal[player].value == 0:
        b4_defeated_locations.append(CastleLocationNames.ev_victory)
    b4_defeated_region = create_region(multiworld, player, active_locations, CastleRegionNames.b4_defeated,
                                       b4_defeated_locations)

    get_planks_locations = []
    if multiworld.goal[player].value == 1:
        get_planks_locations.append(CastleLocationNames.ev_victory)
    get_planks_region = create_region(multiworld, player, active_locations, CastleRegionNames.get_planks,
                                      get_planks_locations)

    escaped_locations = []
    if multiworld.goal[player].value == 2:
        escaped_locations.append(CastleLocationNames.ev_victory)
    escaped_region = create_region(multiworld, player, active_locations, CastleRegionNames.escaped, escaped_locations)

    multiworld.regions += [
        menu_region,
        p1_start_region,
        p1_s_region,
        p1_sw_bronze_gate_region,
        p1_e_region,
        p1_m_bronze_gate_region,
        p1_from_p2_region,
        p1_from_p3_n_region,
        p1_from_p3_s_region,
        p2_start_region,
        p2_m_region,
        p2_n_region,
        p2_red_switch_region,
        p2_e_bronze_gate_region,
        p2_s_region,
        p2_e_bronze_gate_2_region,
        p2_m_bronze_gate_region,
        p2_se_bronze_gate_region,
        p2_gg_room_reward_region,
        p2_end_region,
        p3_start_region,
        p3_nw_n_bronze_gate_region,
        p3_nw_s_bronze_gate_region,
        p3_s_bronze_gate_region,
        p3_silver_gate_region,
        p3_n_gold_gate_region,
        p3_s_gold_gate_region,
        p3_bonus_return_region,
        n1_start_region,
        n1_room1_region,
        n1_room2_region,
        n1_room3_region,
        n1_room4_region,
        b1_start_region,
        b1_arena_region,
        b1_defeated_region,
        a1_start_region,
        b4_defeated_region,
        escaped_region,
        get_planks_region
    ]

    connect_castle_regions(multiworld, player, active_locations)

    check_region_locations(multiworld, player, active_locations)


def connect_castle_regions(multiworld, player: int, active_locations):
    used_names: typing.Dict[str, int] = {}

    connect(multiworld, player, used_names, CastleRegionNames.menu, CastleRegionNames.p1_start)
    connect(multiworld, player, used_names, CastleRegionNames.p1_start, CastleRegionNames.p1_s,
            lambda state: (state.has(ItemName.key_bronze, player, 1)))
    connect(multiworld, player, used_names, CastleRegionNames.p1_s, CastleRegionNames.p1_sw_bronze_gate,
            lambda state: (state.has(ItemName.key_bronze, player, 2)))
    connect(multiworld, player, used_names, CastleRegionNames.p1_s, CastleRegionNames.p1_e,
            lambda state: (state.has(ItemName.key_bronze, player, 3)))
    connect(multiworld, player, used_names, CastleRegionNames.p1_e, CastleRegionNames.p1_m_bronze_gate,
            lambda state: (state.has(ItemName.key_bronze, player, 4)))
    connect(multiworld, player, used_names, CastleRegionNames.p1_e, CastleRegionNames.p2_start)

    connect(multiworld, player, used_names, CastleRegionNames.p2_start, CastleRegionNames.p2_m,
            lambda state: (state.has(ItemName.key_bronze, player, 5)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_m, CastleRegionNames.p1_from_p2)
    connect(multiworld, player, used_names, CastleRegionNames.p2_m, CastleRegionNames.p2_n,
            lambda state: (state.has(ItemName.key_silver, player, 1) and state.has(ItemName.key_bronze, player, 5)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_n, CastleRegionNames.p2_red_switch)
    connect(multiworld, player, used_names, CastleRegionNames.p2_red_switch, CastleRegionNames.p2_e_bronze_gate,
            lambda state: (state.has(ItemName.key_bronze, player, 6)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_m, CastleRegionNames.p2_s,
            lambda state: (state.has(ItemName.key_gold, player, 1) and state.has(ItemName.key_bronze, player, 6)
                           and state.has(ItemName.key_silver, player, 1)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_e_bronze_gate_2,
            lambda state: (state.has(ItemName.key_bronze, player, 7)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_m_bronze_gate,
            lambda state: (state.has(ItemName.key_bronze, player, 8)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_se_bronze_gate,
            lambda state: (state.has(ItemName.key_bronze, player, 9)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_gg_room_reward,
            lambda state: (state.has(ItemName.ev_castle_p2_switch, player, 4)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_s, CastleRegionNames.p2_end,
            lambda state: (state.has(ItemName.key_gold, player, 2) and state.has(ItemName.key_bronze, player, 9)))
    connect(multiworld, player, used_names, CastleRegionNames.p2_end, CastleRegionNames.p3_start)

    connect(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_nw_n_bronze_gate,
            lambda state: (state.has(ItemName.key_bronze, player, 12)))
    connect(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_nw_s_bronze_gate,
            lambda state: (state.has(ItemName.key_bronze, player, 12)))
    connect(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_silver_gate,
            lambda state: (state.has(ItemName.key_silver, player, 2) and state.has(ItemName.key_bronze, player, 12)))
    connect(multiworld, player, used_names, CastleRegionNames.p3_silver_gate, CastleRegionNames.p1_from_p3_s)
    connect(multiworld, player, used_names, CastleRegionNames.p3_start, CastleRegionNames.p3_n_gold_gate,
            lambda state: (state.has(ItemName.key_gold, player, 3) and state.has(ItemName.key_silver, player, 2)
                           and state.has(ItemName.key_bronze, player, 12)))
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.n1_start)
    connect(multiworld, player, used_names, CastleRegionNames.p3_bonus_return, CastleRegionNames.p3_n_gold_gate)
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p1_from_p3_n)
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.p3_s_gold_gate,
            lambda state: (state.has(ItemName.key_gold, player, 4)))
    connect(multiworld, player, used_names, CastleRegionNames.p3_n_gold_gate, CastleRegionNames.b1_start,
            lambda state: (state.has(ItemName.ev_castle_b1_boss_switch, player, 3)
                           and state.has(ItemName.key_gold, player, 4)))

    # Technically a bonus key is needed to traverse to the next room, but we aren't randomizing them for now
    connect(multiworld, player, used_names, CastleRegionNames.n1_start, CastleRegionNames.n1_room1)
    connect(multiworld, player, used_names, CastleRegionNames.n1_room1, CastleRegionNames.n1_room2)
    connect(multiworld, player, used_names, CastleRegionNames.n1_room2, CastleRegionNames.n1_room3)
    connect(multiworld, player, used_names, CastleRegionNames.n1_room3, CastleRegionNames.n1_room4)
    connect(multiworld, player, used_names, CastleRegionNames.n1_room4, CastleRegionNames.p3_bonus_return)

    connect(multiworld, player, used_names, CastleRegionNames.b1_start, CastleRegionNames.b1_arena)
    connect(multiworld, player, used_names, CastleRegionNames.b1_arena, CastleRegionNames.b1_defeated)
    connect(multiworld, player, used_names, CastleRegionNames.b1_defeated, CastleRegionNames.a1_start)

    connect(multiworld, player, used_names, CastleRegionNames.a1_start, CastleRegionNames.b4_defeated)

    planks_to_win = multiworld.planks_required_count[player]
    connect(multiworld, player, used_names, CastleRegionNames.b4_defeated, CastleRegionNames.escaped,
            lambda state: (state.has(ItemName.plank, player, 12)))

    connect(multiworld, player, used_names, CastleRegionNames.menu, CastleRegionNames.get_planks,
            lambda state: (state.has(ItemName.plank, player, planks_to_win)))


def create_tots_regions(multiworld, player: int, active_locations: typing.Dict[str, LocationData]):
    menu_region = create_region(multiworld, player, active_locations, TempleRegionNames.menu, None)

    get_planks_locations = []
    if multiworld.goal[player].value % 10 == 1:
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

    cave3_main_locations = [
        TempleLocationNames.cave3_squire,
        TempleLocationNames.cave3_guard,
        TempleLocationNames.cave3_ne,
        TempleLocationNames.cave3_nw,
        TempleLocationNames.cave3_m,
        TempleLocationNames.cave3_se,
        TempleLocationNames.cave3_half_bridge,
        TempleLocationNames.cave3_trapped_guard,
        TempleLocationNames.cave3_n,
        TempleLocationNames.cave3_outside_guard,
        TempleLocationNames.cave3_secret_n,
        TempleLocationNames.cave3_secret_nw,
        TempleLocationNames.cave3_secret_s,
        TempleLocationNames.c3_puzzle_1,
        TempleLocationNames.c3_puzzle_2,
        TempleLocationNames.c3_puzzle_3,
        TempleLocationNames.c3_puzzle_4,
    ]
    cave3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_main,
                                      cave3_main_locations)

    cave3_fall_locations = [
        TempleLocationNames.cave3_fall_nw,
        TempleLocationNames.cave3_fall_ne,
        TempleLocationNames.cave3_fall_sw,
        TempleLocationNames.cave3_fall_se
    ]
    cave3_fall_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_fall,
                                      cave3_fall_locations)

    cave3_fields_locations = [
        TempleLocationNames.cave3_fields_r,
        TempleLocationNames.cave3_captain,
        TempleLocationNames.cave3_captain_dock,
    ]
    cave3_fields_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_3_fields,
                                        cave3_fields_locations)

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
        TempleLocationNames.cave2_sw_hidden_room_3,
        TempleLocationNames.cave2_red_bridge_2,
        TempleLocationNames.cave2_double_bridge_m,
        TempleLocationNames.cave2_nw_2,
        TempleLocationNames.cave2_red_bridge_4,
        TempleLocationNames.cave2_double_bridge_r,
        TempleLocationNames.cave2_green_bridge,
        TempleLocationNames.cave2_sw_hidden_room_1,
        TempleLocationNames.cave2_guard_s,
        TempleLocationNames.cave2_nw_3,
        TempleLocationNames.cave2_w_miniboss_4,
        TempleLocationNames.cave2_red_bridge_3,
        TempleLocationNames.cave2_below_pumps_3,
        TempleLocationNames.cave2_nw_1,
        TempleLocationNames.cave2_sw,
        TempleLocationNames.cave2_double_bridge_secret,
        TempleLocationNames.cave2_sw_hidden_room_2,
        TempleLocationNames.cave2_pumps_n,
        TempleLocationNames.cave2_guard,
        TempleLocationNames.cave2_red_bridge_1,
        TempleLocationNames.cave2_sw_hidden_room_4,
        TempleLocationNames.cave2_below_pumps_1,
        TempleLocationNames.cave2_below_pumps_2,
        TempleLocationNames.cave2_double_bridge_l_1,
        TempleLocationNames.cave2_double_bridge_l_2,
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
        TempleLocationNames.cave2_secret_w,
        TempleLocationNames.cave2_secret_m,
        TempleLocationNames.c2_puzzle_1,
        TempleLocationNames.c2_puzzle_2,
        TempleLocationNames.c2_puzzle_3,
        TempleLocationNames.c2_puzzle_4,
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
        TempleLocationNames.c1_n_puzzle_1,
        TempleLocationNames.c1_n_puzzle_2,
        TempleLocationNames.c1_n_puzzle_3,
        TempleLocationNames.c1_n_puzzle_4,
    ]
    cave1_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_main,
                                      cave1_main_locations)

    cave1_blue_bridge_locations = [
        TempleLocationNames.cave1_ne_hidden_room_1,
        TempleLocationNames.cave1_ne_hidden_room_2,
        TempleLocationNames.cave1_ne_hidden_room_3,
        TempleLocationNames.cave1_ne_hidden_room_4,
        TempleLocationNames.cave1_ne_hidden_room_5,
        TempleLocationNames.cave1_ne_grubs,
        TempleLocationNames.cave1_secret_tunnel_1,
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
        TempleLocationNames.cave1_secret_tunnel_2,
        TempleLocationNames.cave1_secret_tunnel_3,
        TempleLocationNames.cave1_secret_ne,
        TempleLocationNames.ev_cave1_pof_switch,
    ]
    cave1_blue_bridge_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_blue_bridge,
                                             cave1_blue_bridge_locations)

    cave1_red_bridge_locations = [
        TempleLocationNames.cave1_e_2,
        TempleLocationNames.cave1_e_3,
        TempleLocationNames.cave1_red_bridge_e,
        TempleLocationNames.cave1_se_1,
        TempleLocationNames.cave1_se_2,
        TempleLocationNames.cave1_e_1,
        TempleLocationNames.cave1_secret_e,
        TempleLocationNames.c1_e_puzzle_1,
        TempleLocationNames.c1_e_puzzle_2,
        TempleLocationNames.c1_e_puzzle_3,
        TempleLocationNames.c1_e_puzzle_4,
    ]
    cave1_red_bridge_region = create_region(multiworld, player, active_locations, TempleRegionNames.cave_1_red_bridge,
                                            cave1_red_bridge_locations)

    cave1_green_bridge_locations = [
        TempleLocationNames.cave1_green_bridge_1,
        TempleLocationNames.cave1_green_bridge_2,
        TempleLocationNames.cave1_krilith_ledge_n,
        TempleLocationNames.cave1_krilith_ledge_e,
        TempleLocationNames.cave1_krilith_door,
    ]
    cave1_green_bridge_region = create_region(multiworld, player, active_locations,
                                              TempleRegionNames.cave_1_green_bridge,
                                              cave1_green_bridge_locations)

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

    boss1_main_locations = [
        TempleLocationNames.boss1_guard_l,
        TempleLocationNames.boss1_guard_r_1,
        TempleLocationNames.boss1_guard_r_2,
    ]
    boss1_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss_1_main,
                                      boss1_main_locations)

    boss1_defeated_locations = [
        TempleLocationNames.boss1_bridge,
        TempleLocationNames.boss1_bridge_n,
        TempleLocationNames.boss1_drop,
        # TempleLocationNames.boss1_drop_2,
        TempleLocationNames.boss1_secret,
        TempleLocationNames.ev_temple_entrance_rock,
    ]
    boss1_defeated_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss_1_defeated,
                                          boss1_defeated_locations)

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
        TempleLocationNames.p_puzzle_1,
        TempleLocationNames.p_puzzle_2,
        TempleLocationNames.p_puzzle_3,
        TempleLocationNames.p_puzzle_4,
    ]
    passage_mid_region = create_region(multiworld, player, active_locations, TempleRegionNames.passage_mid,
                                       passage_mid_locations)

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
        TempleLocationNames.t1_w_puzzle_1,
        TempleLocationNames.t1_w_puzzle_2,
        TempleLocationNames.t1_w_puzzle_3,
        TempleLocationNames.t1_w_puzzle_4,
    ]
    t1_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_main, t1_main_locations)

    t1_sw_sdoor_locations = [
        TempleLocationNames.t1_sw_cache_1,
        TempleLocationNames.t1_sw_cache_2,
        TempleLocationNames.t1_sw_cache_3,
        TempleLocationNames.t1_sw_cache_4,
        TempleLocationNames.t1_sw_cache_5,
    ]
    t1_sw_cache_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_sw_sdoor,
                                       t1_sw_sdoor_locations)

    t1_node_1_locations = [
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
        TempleLocationNames.ev_t1_s_node
    ]
    t1_node_1_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_node_1,
                                     t1_node_1_locations)

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
    ]
    t1_sun_turret_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_sun_turret,
                                         t1_sun_turret_locations)

    t1_ice_turret_locations = [
        TempleLocationNames.t1_ice_turret_1,
        TempleLocationNames.t1_ice_turret_2,
        TempleLocationNames.t1_telarian_1,
        TempleLocationNames.t1_telarian_2,
        TempleLocationNames.t1_telarian_3,
        TempleLocationNames.t1_telarian_4,
        TempleLocationNames.t1_telarian_5,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_1,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_2,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_3,
        TempleLocationNames.t1_boulder_hallway_by_ice_turret_4,
        TempleLocationNames.t1_ice_turret_boulder_break_block,
        TempleLocationNames.t1_n_sunbeam,
        TempleLocationNames.t1_n_sunbeam_treasure_1,
        TempleLocationNames.t1_n_sunbeam_treasure_2,
        TempleLocationNames.t1_n_sunbeam_treasure_3,
    ]
    t1_ice_turret_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_ice_turret,
                                         t1_ice_turret_locations)

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
        TempleLocationNames.t1_e_gold_beetles,
        TempleLocationNames.ev_temple1_pof_switch,
        TempleLocationNames.t1_e_puzzle_1,
        TempleLocationNames.t1_e_puzzle_2,
        TempleLocationNames.t1_e_puzzle_3,
        TempleLocationNames.t1_e_puzzle_4,
    ]
    t1_east_region = create_region(multiworld, player, active_locations, TempleRegionNames.t1_east, t1_east_locations)

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

    boss2_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.boss2_main, [])

    boss2_defeated_locations = [
        TempleLocationNames.boss2_nw,
        TempleLocationNames.boss2_se,
        TempleLocationNames.ev_krilith_defeated
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
        TempleLocationNames.ev_t2_ne_bridge_switch,
        TempleLocationNames.ev_t2_se_bridge_switch,
        TempleLocationNames.t2_nw_puzzle_1,
        TempleLocationNames.t2_nw_puzzle_2,
        TempleLocationNames.t2_nw_puzzle_3,
        TempleLocationNames.t2_nw_puzzle_4,
        TempleLocationNames.t2_e_puzzle_1,
        TempleLocationNames.t2_e_puzzle_2,
        TempleLocationNames.t2_e_puzzle_3,
        TempleLocationNames.t2_e_puzzle_4,
    ]
    t2_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_main, t2_main_locations)

    t2_melt_ice_locations = [
        TempleLocationNames.t2_w_ice_block_gate,
        TempleLocationNames.t2_e_ice_block_gate,
    ]
    t2_melt_ice_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_melt_ice,
                                       t2_melt_ice_locations)

    t2_n_gate_locations = [
        TempleLocationNames.t2_nw_ice_turret_1,
        TempleLocationNames.t2_nw_ice_turret_2,
        TempleLocationNames.t2_nw_ice_turret_3,
        TempleLocationNames.t2_nw_ice_turret_4,
        TempleLocationNames.t2_nw_under_block,
        TempleLocationNames.t2_nw_gate_1,
        TempleLocationNames.t2_nw_gate_2,
        TempleLocationNames.t2_nw_gate_3,
        TempleLocationNames.t2_n_puzzle_1,
        TempleLocationNames.t2_n_puzzle_2,
        TempleLocationNames.t2_n_puzzle_3,
        TempleLocationNames.t2_n_puzzle_4,
    ]
    t2_n_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_n_gate,
                                     t2_n_gate_locations)

    t2_s_gate_locations = [
        TempleLocationNames.t2_sw_gate,
        TempleLocationNames.t2_s_node_room_1,
        TempleLocationNames.t2_s_node_room_2,
        TempleLocationNames.t2_s_node_room_3,
        TempleLocationNames.t2_s_sunbeam_1,
        TempleLocationNames.t2_s_sunbeam_2,
        TempleLocationNames.t2_sw_jail_1,
        TempleLocationNames.t2_sw_jail_2,
        TempleLocationNames.t2_left_of_pof_switch_1,
        TempleLocationNames.t2_left_of_pof_switch_2,
        TempleLocationNames.t2_right_of_pof_switch,
        TempleLocationNames.ev_t2_sw_bridge_switch,
        TempleLocationNames.ev_temple2_pof_switch,
        TempleLocationNames.t2_sw_puzzle_1,
        TempleLocationNames.t2_sw_puzzle_2,
        TempleLocationNames.t2_sw_puzzle_3,
        TempleLocationNames.t2_sw_puzzle_4,
    ]
    t2_s_gate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_s_gate,
                                     t2_s_gate_locations)

    t2_n_node_locations = [
        TempleLocationNames.t2_boulder_room_1,
        TempleLocationNames.t2_boulder_room_2,
        TempleLocationNames.t2_boulder_room_block,
        TempleLocationNames.t2_mana_drain_fire_trap_1,
        TempleLocationNames.t2_mana_drain_fire_trap_2,
        TempleLocationNames.t2_jones_hallway,
        TempleLocationNames.t2_gold_beetle_barricade,
        TempleLocationNames.t2_w_gold_beetle_room_1,
        TempleLocationNames.t2_w_gold_beetle_room_2,
        TempleLocationNames.t2_w_gold_beetle_room_3,
        TempleLocationNames.t2_w_gold_beetle_room_4,
        TempleLocationNames.ev_t2_n_node,
        TempleLocationNames.ev_t2_w_bridge_switch
    ]
    t2_n_node_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_n_node,
                                     t2_n_node_locations)

    t2_s_node_locations = [
        TempleLocationNames.ev_t2_s_node
    ]
    t2_s_node_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_s_node,
                                     t2_s_node_locations)

    t2_ornate_locations = [
        TempleLocationNames.ev_t2_n_bridge_switch
    ]
    t2_ornate_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_ornate,
                                     t2_ornate_locations)

    t2_light_bridges_locations = [
        TempleLocationNames.t2_se_light_bridge_1,
        TempleLocationNames.t2_se_light_bridge_2,
        TempleLocationNames.t2_s_light_bridge_1,
        TempleLocationNames.t2_s_light_bridge_2,
        TempleLocationNames.t2_portal_gate,
    ]
    t2_light_bridges_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_light_bridges,
                                            t2_light_bridges_locations)

    t2_ornate_t3_locations = [
        TempleLocationNames.t2_floor3_cache_1,
        TempleLocationNames.t2_floor3_cache_2,
        TempleLocationNames.t2_floor3_cache_3,
        TempleLocationNames.t2_floor3_cache_4,
        TempleLocationNames.t2_floor3_cache_5,
        TempleLocationNames.t2_floor3_cache_6,
        TempleLocationNames.t2_floor3_cache_gate,
    ]
    t2_ornate_t3_region = create_region(multiworld, player, active_locations, TempleRegionNames.t2_ornate_t3,
                                        t2_ornate_t3_locations)

    t3_main_locations = [
        TempleLocationNames.t3_s_balcony_turret_1,
        TempleLocationNames.t3_s_balcony_turret_2,
        TempleLocationNames.t3_n_turret_1,
        TempleLocationNames.t3_n_turret_2,
        TempleLocationNames.t3_boulder_block,
        TempleLocationNames.t3_e_turret_spikes,
        TempleLocationNames.t3_puzzle_1,
        TempleLocationNames.t3_puzzle_2,
        TempleLocationNames.t3_puzzle_3,
        TempleLocationNames.t3_puzzle_4,
    ]
    t3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_main, t3_main_locations)

    t3_n_node_blocks_locations = [
        TempleLocationNames.t3_s_gate,
        TempleLocationNames.t3_n_node_blocks_1,
        TempleLocationNames.t3_n_node_blocks_2,
        TempleLocationNames.t3_n_node_blocks_3,
        TempleLocationNames.t3_n_node_blocks_4,
        TempleLocationNames.t3_n_node_blocks_5,
    ]
    t3_n_node_blocks_region = create_region(multiworld, player, active_locations, TempleRegionNames.t3_n_node_blocks,
                                            t3_n_node_blocks_locations)

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
    pof_1_se_room_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_se_room,
                                         pof_1_se_room_locations)

    pof_gate_1_locations = [
        TempleLocationNames.pof_1_confuse_corner_1,
        TempleLocationNames.pof_1_confuse_corner_2,
        TempleLocationNames.pof_1_confuse_corner_3,
        TempleLocationNames.pof_1_confuse_corner_4,
        TempleLocationNames.pof_1_c_hall_1,
        TempleLocationNames.pof_1_c_hall_2,
        TempleLocationNames.pof_1_c_hall_3,
        TempleLocationNames.pof_1_c_hall_4,
        TempleLocationNames.pof_1_c_hall_5,
        TempleLocationNames.pof_1_c_hall_6,
    ]
    pof_gate_1_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_gate_1,
                                      pof_gate_1_locations)

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
    ]
    pof_1_n_room_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_1_n_room,
                                        pof_1_n_room_locations)

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
        TempleLocationNames.pof_puzzle_1,
        TempleLocationNames.pof_puzzle_2,
        TempleLocationNames.pof_puzzle_3,
        TempleLocationNames.pof_puzzle_4,
    ]
    pof_2_n_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_2_n, pof_2_n_locations)

    pof_3_main_locations = [
        TempleLocationNames.pof_3_safety_room_1,
        TempleLocationNames.pof_3_safety_room_2,
        TempleLocationNames.pof_3_safety_room_3,
        TempleLocationNames.pof_3_end_1,
        TempleLocationNames.pof_3_end_2,
        TempleLocationNames.pof_3_end_3,
        TempleLocationNames.pof_3_end_4,
        TempleLocationNames.pof_3_end_5,
        TempleLocationNames.ev_pof_end
    ]
    if multiworld.goal[player].value == 13:
        pof_3_main_locations.append(TempleLocationNames.ev_victory)
    pof_3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.pof_3_main,
                                      pof_3_main_locations)

    b3_main_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_main, [])
    b3_platform_1_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_platform_1, [])
    b3_platform_2_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_platform_2, [])
    b3_platform_3_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_platform_3, [])

    b3_defeated_locations = []
    if multiworld.goal[player].value == 10:
        b3_defeated_locations.append(TempleLocationNames.ev_victory)
    b3_defeated_region = create_region(multiworld, player, active_locations, TempleRegionNames.b3_defeated,
                                       b3_defeated_locations)

    multiworld.regions += [
        menu_region,
        dunes_main_region,
        dunes_rocks_region,
        dunes_pyramid_region,
        library_region,
        cave3_main_region,
        cave3_fall_region,
        cave3_fields_region,
        cave3_portal_region,
        cave3_secret_region,
        cave2_main_region,
        cave2_pumps_region,
        cave1_main_region,
        cave1_blue_bridge_region,
        cave1_red_bridge_region,
        cave1_green_bridge_region,
        cave1_pumps_region,
        cave1_temple_region,
        boss1_main_region,
        boss1_defeated_region,
        passage_entrance_region,
        passage_mid_region,
        passage_end_region,
        temple_entrance_region,
        temple_entrance_back_region,
        t1_main_region,
        t1_sw_cache_region,
        t1_node_1_region,
        t1_node_2_region,
        t1_sun_turret_region,
        t1_ice_turret_region,
        t1_n_of_ice_turret_region,
        t1_s_of_ice_turret_region,
        t1_east_region,
        t1_sun_block_hall_region,
        t1_telarian_melt_ice_region,
        t1_ice_chamber_melt_ice_region,
        boss2_main_region,
        boss2_defeated_region,
        t2_main_region,
        t2_melt_ice_region,
        t2_n_gate_region,
        t2_s_gate_region,
        t2_n_node_region,
        t2_s_node_region,
        t2_ornate_region,
        t2_light_bridges_region,
        t2_ornate_t3_region,
        t3_main_region,
        t3_n_node_blocks_region,
        t3_n_node_region,
        t3_s_node_blocks_1_region,
        t3_s_node_blocks_2_region,
        t3_s_node_region,
        t3_boss_fall_1_region,
        t3_boss_fall_2_region,
        t3_boss_fall_3_region,
        pof_1_main_region,
        pof_1_se_room_region,
        pof_gate_1_region,
        pof_1_n_room_region,
        pof_1_gate_2_region,
        pof_2_main_region,
        pof_2_n_region,
        pof_3_main_region,
        b3_main_region,
        b3_platform_1_region,
        b3_platform_2_region,
        b3_platform_3_region,
        b3_defeated_region,
        get_planks_region
    ]

    connect_tots_regions(multiworld, player, active_locations)

    check_region_locations(multiworld, player, active_locations)


def connect_tots_regions(multiworld, player: int, active_locations):
    used_names: typing.Dict[str, int] = {}

    def has_pan(state):
        return state.has(ItemName.pan, player) \
               or state.has(ItemName.pan_fragment, player, multiworld.pan_fragments[player].value)

    def has_lever(state):
        return state.has(ItemName.lever, player) \
               or state.has(ItemName.lever_fragment, player, multiworld.lever_fragments[player].value)

    def has_pickaxe(state):
        return state.has(ItemName.pickaxe, player) \
               or state.has(ItemName.pickaxe_fragment, player, multiworld.pickaxe_fragments[player].value)

    connect(multiworld, player, used_names, TempleRegionNames.menu, TempleRegionNames.hub_main)

    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.hub_rocks, has_pickaxe)
    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.cave_3_fall, has_pickaxe)
    # For the temple entrances in the hub
    connect(multiworld, player, used_names, TempleRegionNames.hub_rocks, TempleRegionNames.t3_main)
    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.temple_entrance)

    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.library)
    connect(multiworld, player, used_names, TempleRegionNames.library, TempleRegionNames.cave_3_main)
    connect(multiworld, player, used_names, TempleRegionNames.cave_3_main, TempleRegionNames.cave_3_fields, has_lever)

    connect(multiworld, player, used_names, TempleRegionNames.cave_3_main, TempleRegionNames.cave_2_main)
    connect(multiworld, player, used_names, TempleRegionNames.cave_2_main, TempleRegionNames.cave_2_pumps, has_lever)

    connect(multiworld, player, used_names, TempleRegionNames.cave_2_main, TempleRegionNames.cave_1_main)
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_main, TempleRegionNames.cave_1_blue_bridge)
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_blue_bridge, TempleRegionNames.cave_1_red_bridge)
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_main, TempleRegionNames.cave_1_pumps, has_lever)
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_pumps, TempleRegionNames.cave_1_green_bridge)
    connect(multiworld, player, used_names, TempleRegionNames.cave_1_green_bridge, TempleRegionNames.boss2_main)
    connect(multiworld, player, used_names, TempleRegionNames.boss2_main, TempleRegionNames.boss2_defeated)

    connect(multiworld, player, used_names, TempleRegionNames.cave_1_red_bridge, TempleRegionNames.boss_1_main)
    connect(multiworld, player, used_names, TempleRegionNames.boss_1_main, TempleRegionNames.boss_1_defeated,
            lambda state: (state.has(ItemName.key_gold, player, 1)))

    connect(multiworld, player, used_names, TempleRegionNames.boss_1_defeated, TempleRegionNames.passage_entrance)
    connect(multiworld, player, used_names, TempleRegionNames.passage_entrance, TempleRegionNames.passage_mid)
    connect(multiworld, player, used_names, TempleRegionNames.passage_mid, TempleRegionNames.passage_end)

    connect(multiworld, player, used_names, TempleRegionNames.passage_end, TempleRegionNames.temple_entrance_back)
    connect(multiworld, player, used_names, TempleRegionNames.temple_entrance_back, TempleRegionNames.temple_entrance,
            lambda state: (state.has(ItemName.ev_open_temple_entrance_shortcut, player)))
    connect(multiworld, player, used_names, TempleRegionNames.temple_entrance_back, TempleRegionNames.t1_main)

    connect(multiworld, player, used_names, TempleRegionNames.t1_main, TempleRegionNames.t1_sw_sdoor,
            lambda state: (state.has(ItemName.key_silver, player, 1)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_main, TempleRegionNames.t1_node_1,
            lambda state: (state.has(ItemName.mirror, player, 3)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_node_1, TempleRegionNames.cave_3_secret)
    connect(multiworld, player, used_names, TempleRegionNames.t1_node_1, TempleRegionNames.t1_sun_turret,
            lambda state: (state.has(ItemName.key_silver, player, 2)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_node_1, TempleRegionNames.t1_ice_turret,
            lambda state: (state.has(ItemName.key_gold, player, 2) and state.has(ItemName.key_silver, player, 2)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_telarian_melt_ice,
            lambda state: (state.has(ItemName.ev_krilith_defeated, player)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_n_of_ice_turret,
            lambda state: (state.has(ItemName.key_silver, player, 4)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_s_of_ice_turret,
            lambda state: (state.has(ItemName.key_silver, player, 4)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_ice_turret, TempleRegionNames.t1_east,
            lambda state: (state.has(ItemName.key_gold, player, 3) and state.has(ItemName.key_silver, player, 4)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t1_sun_block_hall,
            lambda state: (state.has(ItemName.mirror, player, 6)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t1_node_2,
            lambda state: (state.has(ItemName.mirror, player, 7)))
    connect(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t1_ice_chamber_melt_ice,
            lambda state: (state.has(ItemName.ev_krilith_defeated, player)))

    connect(multiworld, player, used_names, TempleRegionNames.t1_east, TempleRegionNames.t2_main)
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_melt_ice,
            lambda state: (state.has(ItemName.ev_krilith_defeated, player)))
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_n_gate,
            lambda state: (state.has(ItemName.key_silver, player, 6)
                           and state.has(ItemName.ev_krilith_defeated, player)))
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_s_gate,
            lambda state: (state.has(ItemName.key_silver, player, 6)
                           and state.has(ItemName.ev_krilith_defeated, player)))
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_ornate,
            lambda state: (state.has(ItemName.key_gold, player, 4)))
    connect(multiworld, player, used_names, TempleRegionNames.t2_n_gate, TempleRegionNames.t2_n_node,
            lambda state: (state.has(ItemName.mirror, player, 10)))
    connect(multiworld, player, used_names, TempleRegionNames.t2_s_gate, TempleRegionNames.t2_s_node,
            lambda state: (state.has(ItemName.mirror, player, 14)))
    connect(multiworld, player, used_names, TempleRegionNames.t2_main, TempleRegionNames.t2_light_bridges,
            lambda state: (state.has(ItemName.ev_t2_bridge_switch, player, 5)))
    connect(multiworld, player, used_names, TempleRegionNames.t2_light_bridges, TempleRegionNames.cave_3_portal)
    connect(multiworld, player, used_names, TempleRegionNames.t2_light_bridges, TempleRegionNames.cave_1_temple)

    connect(multiworld, player, used_names, TempleRegionNames.t3_main, TempleRegionNames.t2_ornate_t3)
    connect(multiworld, player, used_names, TempleRegionNames.t3_main, TempleRegionNames.t3_n_node_blocks,
            lambda state: (state.has(ItemName.mirror, player, 19)))
    connect(multiworld, player, used_names, TempleRegionNames.t3_n_node_blocks, TempleRegionNames.t3_n_node,
            lambda state: (state.has(ItemName.mirror, player, 20)))
    connect(multiworld, player, used_names, TempleRegionNames.t3_main, TempleRegionNames.t3_s_node_blocks_1,
            lambda state: (state.has(ItemName.mirror, player, 18)))
    connect(multiworld, player, used_names, TempleRegionNames.t3_s_node_blocks_1, TempleRegionNames.t3_s_node_blocks_2,
            lambda state: (state.has(ItemName.mirror, player, 19)))
    connect(multiworld, player, used_names, TempleRegionNames.t3_s_node_blocks_2, TempleRegionNames.t3_s_node,
            lambda state: (state.has(ItemName.mirror, player, 20)))

    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.pof_1_main,
            lambda state: (state.has(ItemName.ev_pof_switch, player, 6)))
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_main, TempleRegionNames.pof_1_se_room)
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_se_room, TempleRegionNames.pof_1_gate_1)
            # lambda state: (state.has(ItemName.bonus_key, player, 1)))
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_gate_1, TempleRegionNames.pof_1_n_room)
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_n_room, TempleRegionNames.pof_1_gate_2)
            # lambda state: (state.has(ItemName.bonus_key, player, 2)))
    connect(multiworld, player, used_names, TempleRegionNames.pof_1_gate_2, TempleRegionNames.pof_2_main)
    connect(multiworld, player, used_names, TempleRegionNames.pof_2_main, TempleRegionNames.pof_2_n)
    connect(multiworld, player, used_names, TempleRegionNames.pof_2_n, TempleRegionNames.pof_3_main)
    connect(multiworld, player, used_names, TempleRegionNames.pof_3_main, TempleRegionNames.hub_pyramid_of_fear,
            lambda state: (state.has(ItemName.ev_pof_complete, player)))

    connect(multiworld, player, used_names, TempleRegionNames.hub_main, TempleRegionNames.b3_main,
            lambda state: (state.has(ItemName.ev_solar_node, player, 6)))
    connect(multiworld, player, used_names, TempleRegionNames.b3_main, TempleRegionNames.b3_platform_1)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_1, TempleRegionNames.b3_platform_2)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_2, TempleRegionNames.b3_platform_3)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_3, TempleRegionNames.b3_defeated)

    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_1, TempleRegionNames.t3_boss_fall_1)
    connect(multiworld, player, used_names, TempleRegionNames.t3_boss_fall_1, TempleRegionNames.t3_main)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_2, TempleRegionNames.t3_boss_fall_2)
    connect(multiworld, player, used_names, TempleRegionNames.t3_boss_fall_2, TempleRegionNames.t3_main)
    connect(multiworld, player, used_names, TempleRegionNames.b3_platform_3, TempleRegionNames.t3_boss_fall_3)
    connect(multiworld, player, used_names, TempleRegionNames.t3_boss_fall_3, TempleRegionNames.t3_main)

    planks_to_win = multiworld.planks_required_count[player]
    connect(multiworld, player, used_names, TempleRegionNames.menu, TempleRegionNames.get_planks,
            lambda state: (state.has(ItemName.plank, player, planks_to_win)))


def create_region(multiworld: MultiWorld, player: int, active_locations: typing.Dict[str, LocationData], name: str,
                  locations: typing.List[str]) -> Region:
    region = Region(name, RegionType.Generic, name, player, multiworld)
    if locations:
        for location in locations:
            if location not in active_locations.keys():
                continue
            region.locations.append(HammerwatchLocation(player, location, active_locations[location].code, region))
    return region


def connect(multiworld: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def check_region_locations(multiworld: MultiWorld, player: int, active_locations: typing.Dict[str, LocationData]):
    # Duplicate location testing because I sometimes add stuff late at night and forget to check it >:|
    name_list = []
    remaining_locs = active_locations.copy()
    test = 0
    for region in multiworld.regions:
        if region.player != player:
            continue
        test += len(region.locations)
        for loc in region.locations:
            if loc.name in name_list:
                print(f"Duplicate location found!!! {loc.name}")
            name_list.append(loc.name)
            if loc.name not in remaining_locs:
                print(f"Location found not in active locations!!! {loc.name}")
            remaining_locs.pop(loc.name)
    for loc_name, data in remaining_locs.items():
        print(f"Missing location in regions!!! {loc_name} {data.code}")
