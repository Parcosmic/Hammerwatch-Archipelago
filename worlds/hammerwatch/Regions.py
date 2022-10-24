import typing
from random import Random

from BaseClasses import MultiWorld, Region, RegionType, Entrance
from .Items import HammerwatchItem
from .Locations import HammerwatchLocation, LocationData, LocationClassification, random_locations
from .Names import LocationName, ItemName, RegionName
from .Util import Counter


def create_regions(world, player: int, active_locations: typing.Dict[str, LocationData]):
    if world.map[player] == 0:
        pass
    else:
        create_tots_regions(world, player, active_locations)


def create_tots_regions(world, player: int, active_locations: typing.Dict[str, LocationData]):
    menu_region = create_region(world, player, active_locations, RegionName.menu, None)

    hub_main_locations = [
        LocationName.hub_front_of_pof,
        LocationName.hub_behind_temple_entrance
    ]
    dunes_main_region = create_region(world, player, active_locations, RegionName.hub_main, hub_main_locations)

    dunes_rocks_locations = [
        LocationName.hub_behind_shops,
        LocationName.hub_on_rock,
        LocationName.hub_west_pyramid,
        LocationName.hub_rocks_south,
        LocationName.hub_field_south,
        LocationName.hub_field_nw,
        LocationName.hub_field_north,
        LocationName.ev_hub_pof_switch
    ]
    dunes_rocks_region = create_region(world, player, active_locations, RegionName.hub_rocks,
                                       dunes_rocks_locations)

    dunes_pyramid_locations = [
        LocationName.hub_pof_reward
    ]
    dunes_pyramid_region = create_region(world, player, active_locations, RegionName.hub_pyramid_of_fear,
                                         dunes_pyramid_locations)

    library_region = create_region(world, player, active_locations, RegionName.library, [])

    cave3_main_locations = [
        LocationName.cave3_squire,
        LocationName.cave3_guard,
        LocationName.cave3_ne,
        LocationName.cave3_nw,
        LocationName.cave3_m,
        LocationName.cave3_se,
        LocationName.cave3_half_bridge,
        LocationName.cave3_trapped_guard,
        LocationName.cave3_n,
        LocationName.cave3_outside_guard,
        LocationName.cave3_secret_n,
        LocationName.cave3_secret_nw,
        LocationName.cave3_secret_s,
    ]
    cave3_main_region = create_region(world, player, active_locations, RegionName.cave_3_main, cave3_main_locations)

    cave3_fall_locations = [
        LocationName.cave3_fall_nw,
        LocationName.cave3_fall_ne,
        LocationName.cave3_fall_sw,
        LocationName.cave3_fall_se
    ]
    cave3_fall_region = create_region(world, player, active_locations, RegionName.cave_3_fall, cave3_fall_locations)

    cave3_fields_locations = [
        LocationName.cave3_fields_r,
        LocationName.cave3_captain,
        LocationName.cave3_captain_dock,
    ]
    cave3_fields_region = create_region(world, player, active_locations, RegionName.cave_3_fields,
                                        cave3_fields_locations)

    cave3_portal_locations = [
        LocationName.cave3_portal_l,
        LocationName.cave3_portal_r,
        LocationName.ev_cave3_pof_switch
    ]
    cave3_portal_region = create_region(world, player, active_locations, RegionName.cave_3_portal,
                                        cave3_portal_locations)

    cave3_secret_locations = [
        LocationName.cave3_secret_1,
        LocationName.cave3_secret_2,
        LocationName.cave3_secret_3,
        LocationName.cave3_secret_4,
        LocationName.cave3_secret_5,
        LocationName.cave3_secret_6,
        LocationName.cave3_secret_7,
        LocationName.cave3_secret_8,
        LocationName.cave3_secret_9,
        LocationName.cave3_secret_10,
        LocationName.cave3_secret_11,
        LocationName.cave3_secret_12,
    ]
    cave3_secret_region = create_region(world, player, active_locations, RegionName.cave_3_secret,
                                        cave3_secret_locations)

    cave2_main_locations = [
        LocationName.cave2_sw_hidden_room_3,
        LocationName.cave2_red_bridge_2,
        LocationName.cave2_double_bridge_m,
        LocationName.cave2_nw_2,
        LocationName.cave2_red_bridge_4,
        LocationName.cave2_double_bridge_r,
        LocationName.cave2_green_bridge,
        LocationName.cave2_sw_hidden_room_1,
        LocationName.cave2_guard_s,
        LocationName.cave2_nw_3,
        LocationName.cave2_w_miniboss_4,
        LocationName.cave2_red_bridge_3,
        LocationName.cave2_below_pumps_3,
        LocationName.cave2_nw_1,
        LocationName.cave2_sw,
        LocationName.cave2_double_bridge_secret,
        LocationName.cave2_sw_hidden_room_2,
        LocationName.cave2_pumps_n,
        LocationName.cave2_guard,
        LocationName.cave2_red_bridge_1,
        LocationName.cave2_sw_hidden_room_4,
        LocationName.cave2_below_pumps_1,
        LocationName.cave2_below_pumps_2,
        LocationName.cave2_double_bridge_l_1,
        LocationName.cave2_double_bridge_l_2,
        LocationName.cave2_e_1,
        LocationName.cave2_e_2,
        LocationName.cave2_nw_4,
        LocationName.cave2_nw_5,
        LocationName.cave2_w_miniboss_3,
        LocationName.cave2_w_miniboss_2,
        LocationName.cave2_w_miniboss_1,
        LocationName.cave2_red_bridge_se_1,
        LocationName.cave2_red_bridge_se_2,
        LocationName.cave2_e_3,
        LocationName.cave2_e_4,
        LocationName.cave2_guard_n,
        LocationName.cave2_secret_ne,
        LocationName.cave2_secret_w,
        LocationName.cave2_secret_m,
    ]
    cave2_main_region = create_region(world, player, active_locations, RegionName.cave_2_main, cave2_main_locations)

    cave2_pumps_locations = [
        LocationName.cave2_pumps_wall_r,
        LocationName.cave2_pumps_wall_l,
        LocationName.cave2_water_n_r_1,
        LocationName.cave2_water_n_l,
        LocationName.ev_cave2_pof_switch,
        LocationName.cave2_water_n_r_2,
        LocationName.cave2_water_s,
    ]
    cave2_pumps_region = create_region(world, player, active_locations, RegionName.cave_2_pumps, cave2_pumps_locations)

    cave1_main_locations = [
        LocationName.cave1_n_3,
        LocationName.cave1_w_by_water_2,
        LocationName.cave1_s_3,
        LocationName.cave1_m,
        LocationName.cave1_double_room_l,
        LocationName.cave1_double_room_r,
        LocationName.cave1_n_1,
        LocationName.cave1_n_2,
        LocationName.cave1_w_1,
        LocationName.cave1_w_2,
        LocationName.cave1_s_4,
        LocationName.cave1_s_5,
        LocationName.cave1_n_room_1,
        LocationName.cave1_n_room_2,
        LocationName.cave1_n_room_3,
        LocationName.cave1_n_room_4,
        LocationName.cave1_s_1,
        LocationName.cave1_s_2,
        LocationName.cave1_w_by_water_1,
        LocationName.cave1_secret_nw,
        LocationName.cave1_secret_w,
        LocationName.cave1_secret_m,
    ]
    cave1_main_region = create_region(world, player, active_locations, RegionName.cave_1_main, cave1_main_locations)

    cave1_blue_bridge_locations = [
        LocationName.cave1_ne_hidden_room_1,
        LocationName.cave1_ne_hidden_room_2,
        LocationName.cave1_ne_hidden_room_3,
        LocationName.cave1_ne_hidden_room_4,
        LocationName.cave1_ne_hidden_room_5,
        LocationName.cave1_ne_grubs,
        LocationName.cave1_secret_tunnel_1,
        LocationName.cave1_n_bridges_1,
        LocationName.cave1_n_bridges_4,
        LocationName.cave1_n_bridges_5,
        LocationName.cave1_secret_n_hidden_room,
        LocationName.cave1_ne_1,
        LocationName.cave1_ne_2,
        LocationName.cave1_ne_3,
        LocationName.cave1_ne_4,
        LocationName.cave1_ne_5,
        LocationName.cave1_n_bridges_2,
        LocationName.cave1_n_bridges_3,
        LocationName.cave1_secret_tunnel_2,
        LocationName.cave1_secret_tunnel_3,
        LocationName.cave1_secret_ne,
        LocationName.ev_cave1_pof_switch,
    ]
    cave1_blue_bridge_region = create_region(world, player, active_locations, RegionName.cave_1_blue_bridge,
                                             cave1_blue_bridge_locations)

    cave1_red_bridge_locations = [
        LocationName.cave1_e_2,
        LocationName.cave1_e_3,
        LocationName.cave1_red_bridge_e,
        LocationName.cave1_se_1,
        LocationName.cave1_se_2,
        LocationName.cave1_e_1,
        LocationName.cave1_secret_e,
    ]
    cave1_red_bridge_region = create_region(world, player, active_locations, RegionName.cave_1_red_bridge,
                                            cave1_red_bridge_locations)

    cave1_green_bridge_locations = [
        LocationName.cave1_green_bridge_1,
        LocationName.cave1_green_bridge_2,
        LocationName.cave1_krilith_ledge_n,
        LocationName.cave1_krilith_ledge_e,
        LocationName.cave1_krilith_door,
    ]
    cave1_green_bridge_region = create_region(world, player, active_locations, RegionName.cave_1_green_bridge,
                                              cave1_green_bridge_locations)

    cave1_pumps_locations = [
        LocationName.cave1_water_s_shore,
        LocationName.cave1_water_s_1,
        LocationName.cave1_water_s_2,
        LocationName.cave1_water_s_3,
        LocationName.cave1_water_s_4,
        LocationName.cave1_water_s_5,
    ]
    cave1_pumps_region = create_region(world, player, active_locations, RegionName.cave_1_pumps,
                                       cave1_pumps_locations)

    cave1_temple_locations = [
        LocationName.cave1_temple_hall_1,
        LocationName.cave1_temple_hall_2,
        LocationName.cave1_temple_hall_3,
        LocationName.cave1_temple_end_2,
        LocationName.cave1_temple_end_3,
        LocationName.cave1_temple_end_4,
        LocationName.cave1_temple_end_1,
    ]
    cave1_temple_region = create_region(world, player, active_locations, RegionName.cave_1_temple,
                                        cave1_temple_locations)

    boss1_main_locations = [
        LocationName.boss1_guard_l,
        LocationName.boss1_guard_r_1,
        LocationName.boss1_guard_r_2,
    ]
    boss1_main_region = create_region(world, player, active_locations, RegionName.boss_1_main,
                                      boss1_main_locations)

    boss1_defeated_locations = [
        LocationName.boss1_bridge,
        LocationName.boss1_bridge_n,
        LocationName.boss1_drop,
        # LocationName.boss1_drop_2,
        LocationName.boss1_secret,
        LocationName.ev_temple_entrance_rock,
    ]
    boss1_defeated_region = create_region(world, player, active_locations, RegionName.boss_1_defeated,
                                          boss1_defeated_locations)

    passage_entrance_locations = [
        LocationName.p_ent2_secret
    ]
    passage_entrance_region = create_region(world, player, active_locations, RegionName.passage_entrance,
                                            passage_entrance_locations)

    passage_mid_locations = [
        LocationName.p_mid1_1,
        LocationName.p_mid1_2,
        LocationName.p_mid2_1,
        LocationName.p_mid2_2,
        LocationName.p_mid2_3,
        LocationName.p_mid2_4,
        LocationName.p_mid3_secret_1,
        LocationName.p_mid3_secret_2,
        LocationName.p_mid3_secret_3,
        LocationName.p_mid3_secret_4,
        LocationName.p_mid4_1,
        LocationName.p_mid4_2,
        LocationName.p_mid4_3,
        LocationName.p_mid4_4,
        LocationName.p_mid5_1,
        LocationName.p_mid5_2,
        LocationName.p_mid5_secret,
    ]
    passage_mid_region = create_region(world, player, active_locations, RegionName.passage_mid, passage_mid_locations)

    passage_end_locations = [
        LocationName.p_end1_secret,
        LocationName.p_end3_1,
        LocationName.p_end3_2,
    ]
    passage_end_region = create_region(world, player, active_locations, RegionName.passage_end, passage_end_locations)

    temple_entrance_region = create_region(world, player, active_locations, RegionName.temple_entrance, [])

    temple_entrance_back_locations = [
        LocationName.temple_entrance_l,
        LocationName.temple_entrance_r,
    ]
    temple_entrance_back_region = create_region(world, player, active_locations, RegionName.temple_entrance_back,
                                                temple_entrance_back_locations)

    t1_main_locations = [
        LocationName.t1_above_s_bridge,
        LocationName.t1_s_bridge_1,
        LocationName.t1_s_bridge_2,
        LocationName.t1_s_bridge_3,
        LocationName.t1_s_bridge_4,
        LocationName.t1_s_bridge_5,
        LocationName.t1_s_bridge_6,
        LocationName.t1_sw_sun_room_1,
        LocationName.t1_sw_sun_room_2,
        LocationName.t1_sw_corner_room,
        LocationName.t1_sw_hidden_room_1,
        LocationName.t1_sw_hidden_room_2,
        LocationName.t1_sw_hidden_room_3,
        LocationName.t1_sw_hidden_room_4,
    ]
    t1_main_region = create_region(world, player, active_locations, RegionName.t1_main, t1_main_locations)

    t1_sw_cache_locations = [
        LocationName.t1_sw_cache_1,
        LocationName.t1_sw_cache_2,
        LocationName.t1_sw_cache_3,
        LocationName.t1_sw_cache_4,
        LocationName.t1_sw_cache_5,
    ]
    t1_sw_cache_region = create_region(world, player, active_locations, RegionName.t1_sw_cache, t1_sw_cache_locations)

    t1_node_1_locations = [
        LocationName.t1_double_gate_1,
        LocationName.t1_double_gate_2,
        LocationName.t1_double_gate_3,
        LocationName.t1_double_gate_hidden,
        LocationName.t1_behind_bars_entrance,
        LocationName.t1_e_of_double_gate_room_1,
        LocationName.t1_e_of_double_gate_room_2,
        LocationName.t1_e_of_double_gate_room_3,
        LocationName.t1_e_of_double_gate_room_4,
        LocationName.t1_mana_drain_fire_trap,
        LocationName.t1_mana_drain_fire_trap_reward_1,
        LocationName.t1_mana_drain_fire_trap_reward_2,
        LocationName.t1_mana_drain_fire_trap_passage,
        LocationName.ev_t1_s_node
    ]
    t1_node_1_region = create_region(world, player, active_locations, RegionName.t1_node_1, t1_node_1_locations)

    t1_sun_turret_locations = [
        LocationName.t1_double_gate_behind_block,
        LocationName.t1_s_of_sun_turret,
        LocationName.t1_sun_turret_1,
        LocationName.t1_sun_turret_2,
        LocationName.t1_sun_turret_3,
        LocationName.t1_fire_trap_by_sun_turret_1,
        LocationName.t1_fire_trap_by_sun_turret_2,
        LocationName.t1_fire_trap_by_sun_turret_3,
        LocationName.t1_fire_trap_by_sun_turret_4,
    ]
    t1_sun_turret_region = create_region(world, player, active_locations, RegionName.t1_sun_turret,
                                         t1_sun_turret_locations)

    t1_ice_turret_locations = [
        LocationName.t1_ice_turret_1,
        LocationName.t1_ice_turret_2,
        LocationName.t1_telariana_1,
        LocationName.t1_telariana_2,
        LocationName.t1_telariana_3,
        LocationName.t1_telariana_4,
        LocationName.t1_telariana_5,
        LocationName.t1_boulder_hallway_by_ice_turret_1,
        LocationName.t1_boulder_hallway_by_ice_turret_2,
        LocationName.t1_boulder_hallway_by_ice_turret_3,
        LocationName.t1_boulder_hallway_by_ice_turret_4,
        LocationName.t1_ice_turret_boulder_break_block,
        LocationName.t1_n_sunbeam,
        LocationName.t1_n_sunbeam_treasure_1,
        LocationName.t1_n_sunbeam_treasure_2,
        LocationName.t1_n_sunbeam_treasure_3,
    ]
    t1_ice_turret_region = create_region(world, player, active_locations, RegionName.t1_ice_turret,
                                         t1_ice_turret_locations)

    t1_n_of_ice_turret_locations = [
        LocationName.t1_n_cache_by_ice_turret_1,
        LocationName.t1_n_cache_by_ice_turret_2,
        LocationName.t1_n_cache_by_ice_turret_3,
        LocationName.t1_n_cache_by_ice_turret_4,
        LocationName.t1_n_cache_by_ice_turret_5,
    ]
    t1_n_of_ice_turret_region = create_region(world, player, active_locations, RegionName.t1_n_of_ice_turret,
                                              t1_n_of_ice_turret_locations)

    t1_s_of_ice_turret_locations = [
        LocationName.t1_s_cache_by_ice_turret_1,
        LocationName.t1_s_cache_by_ice_turret_2,
        LocationName.t1_s_cache_by_ice_turret_3,
    ]
    t1_s_of_ice_turret_region = create_region(world, player, active_locations, RegionName.t1_s_of_ice_turret,
                                              t1_s_of_ice_turret_locations)

    t1_east_locations = [
        LocationName.t1_ledge_after_block_trap_1,
        LocationName.t1_ledge_after_block_trap_2,
        LocationName.t1_ice_block_chamber_1,
        LocationName.t1_ice_block_chamber_2,
        LocationName.t1_ice_block_chamber_3,
        LocationName.t1_node_2_1,
        LocationName.t1_node_2_2,
        LocationName.t1_node_2_passage_1,
        LocationName.t1_node_2_passage_2,
        LocationName.t1_node_2_passage_3,
        LocationName.t1_e_gold_beetles,
        LocationName.ev_temple1_pof_switch
    ]
    t1_east_region = create_region(world, player, active_locations, RegionName.t1_east, t1_east_locations)

    t1_sun_block_hall_locations = [
        LocationName.t1_sun_block_hall_1,
        LocationName.t1_sun_block_hall_2,
        LocationName.t1_sun_block_hall_3,
        LocationName.t1_sun_block_hall_4,
    ]
    t1_sun_block_hall_region = create_region(world, player, active_locations, RegionName.t1_sun_block_hall,
                                             t1_sun_block_hall_locations)

    t1_node_2_locations = [
        LocationName.ev_t1_n_node
    ]
    t1_node_2_region = create_region(world, player, active_locations, RegionName.t1_node_2, t1_node_2_locations)

    t1_telariana_melt_ice_locations = [
        LocationName.t1_telariana_ice
    ]
    t1_telariana_melt_ice_region = create_region(world, player, active_locations, RegionName.t1_telariana_melt_ice,
                                                 t1_telariana_melt_ice_locations)

    t1_ice_chamber_melt_ice_locations = [
        LocationName.t1_telariana_ice,
        LocationName.t1_ice_block_chamber_ice
    ]
    t1_ice_chamber_melt_ice_region = create_region(world, player, active_locations, RegionName.t1_ice_chamber_melt_ice,
                                                   t1_ice_chamber_melt_ice_locations)

    boss2_main_region = create_region(world, player, active_locations, RegionName.boss2_main, [])

    boss2_defeated_locations = [
        LocationName.boss2_nw,
        LocationName.boss2_se,
        LocationName.ev_krilith_defeated
    ]
    boss2_defeated_region = create_region(world, player, active_locations, RegionName.boss2_defeated,
                                          boss2_defeated_locations)

    t2_main_locations = [
        LocationName.t2_n_of_portal,
        LocationName.t2_s_of_portal,
        LocationName.t2_w_spike_trap_1,
        LocationName.t2_w_spike_trap_2,
        LocationName.t2_nw_puzzle_cache_1,
        LocationName.t2_nw_puzzle_cache_2,
        LocationName.t2_nw_puzzle_cache_3,
        LocationName.t2_nw_puzzle_cache_4,
        LocationName.t2_nw_puzzle_cache_5,
        LocationName.t2_nw_of_s_ice_turret,
        LocationName.t2_w_hall_dead_end_1,
        LocationName.t2_w_hall_dead_end_2,
        LocationName.t2_w_hall_dead_end_3,
        LocationName.t2_w_hall_dead_end_4,
        LocationName.t2_w_hall_dead_end_5,
        LocationName.t2_n_of_sw_gate_1,
        LocationName.t2_n_of_sw_gate_2,
        LocationName.t2_fire_trap_maze_1,
        LocationName.t2_fire_trap_maze_2,
        LocationName.t2_fire_trap_maze_3,
        LocationName.t2_fire_trap_maze_4,
        LocationName.t2_fire_trap_maze_5,
        LocationName.t2_fire_trap_maze_6,
        LocationName.t2_teleporter,
        LocationName.t2_e_outside_gold_beetle_cage_1,
        LocationName.t2_e_outside_gold_beetle_cage_2,
        LocationName.t2_boulder_chamber_1,
        LocationName.t2_boulder_chamber_2,
        LocationName.t2_boulder_chamber_3,
        LocationName.t2_boulder_chamber_4,
        LocationName.t2_s_balcony_1,
        LocationName.t2_s_balcony_2,
        LocationName.t2_se_banner_chamber_1,
        LocationName.t2_se_banner_chamber_2,
        LocationName.t2_se_banner_chamber_3,
        LocationName.t2_se_banner_chamber_4,
        LocationName.t2_se_banner_chamber_5,
        LocationName.t2_se_fireball_hall,
        LocationName.ev_t2_ne_bridge_switch,
        LocationName.ev_t2_se_bridge_switch,
    ]
    t2_main_region = create_region(world, player, active_locations, RegionName.t2_main, t2_main_locations)

    t2_melt_ice_locations = [
        LocationName.t2_w_ice_block_gate,
        LocationName.t2_e_ice_block_gate,
    ]
    t2_melt_ice_region = create_region(world, player, active_locations, RegionName.t2_melt_ice, t2_melt_ice_locations)

    t2_n_gate_locations = [
        LocationName.t2_nw_ice_turret_1,
        LocationName.t2_nw_ice_turret_2,
        LocationName.t2_nw_ice_turret_3,
        LocationName.t2_nw_ice_turret_4,
        LocationName.t2_nw_under_block,
        LocationName.t2_nw_gate_1,
        LocationName.t2_nw_gate_2,
        LocationName.t2_nw_gate_3,
    ]
    t2_n_gate_region = create_region(world, player, active_locations, RegionName.t2_n_gate, t2_n_gate_locations)

    t2_s_gate_locations = [
        LocationName.t2_sw_gate,
        LocationName.t2_s_node_room_1,
        LocationName.t2_s_node_room_2,
        LocationName.t2_s_node_room_3,
        LocationName.t2_s_sunbeam_1,
        LocationName.t2_s_sunbeam_2,
        LocationName.t2_sw_jail_1,
        LocationName.t2_sw_jail_2,
        LocationName.t2_left_of_pof_switch_1,
        LocationName.t2_left_of_pof_switch_2,
        LocationName.t2_right_of_pof_switch,
        LocationName.ev_t2_sw_bridge_switch,
        LocationName.ev_temple2_pof_switch,
    ]
    t2_s_gate_region = create_region(world, player, active_locations, RegionName.t2_s_gate, t2_s_gate_locations)

    t2_n_node_locations = [
        LocationName.t2_boulder_room_1,
        LocationName.t2_boulder_room_2,
        LocationName.t2_boulder_room_block,
        LocationName.t2_mana_drain_fire_trap_1,
        LocationName.t2_mana_drain_fire_trap_2,
        LocationName.t2_jones_hallway,
        LocationName.t2_gold_beetle_barricade,
        LocationName.t2_w_gold_beetle_room_1,
        LocationName.t2_w_gold_beetle_room_2,
        LocationName.t2_w_gold_beetle_room_3,
        LocationName.t2_w_gold_beetle_room_4,
        LocationName.ev_t2_n_node,
        LocationName.ev_t2_w_bridge_switch
    ]
    t2_n_node_region = create_region(world, player, active_locations, RegionName.t2_n_node, t2_n_node_locations)

    t2_s_node_locations = [
        LocationName.ev_t2_s_node
    ]
    t2_s_node_region = create_region(world, player, active_locations, RegionName.t2_s_node, t2_s_node_locations)

    t2_ornate_locations = [
        LocationName.ev_t2_n_bridge_switch
    ]
    t2_ornate_region = create_region(world, player, active_locations, RegionName.t2_ornate, t2_ornate_locations)

    t2_light_bridges_locations = [
        LocationName.t2_se_light_bridge_1,
        LocationName.t2_se_light_bridge_2,
        LocationName.t2_s_light_bridge_1,
        LocationName.t2_s_light_bridge_2,
        LocationName.t2_portal_gate,
    ]
    t2_light_bridges_region = create_region(world, player, active_locations, RegionName.t2_light_bridges,
                                            t2_light_bridges_locations)

    t2_ornate_t3_locations = [
        LocationName.t2_floor3_cache_1,
        LocationName.t2_floor3_cache_2,
        LocationName.t2_floor3_cache_3,
        LocationName.t2_floor3_cache_4,
        LocationName.t2_floor3_cache_5,
        LocationName.t2_floor3_cache_6,
        LocationName.t2_floor3_cache_gate,
    ]
    t2_ornate_t3_region = create_region(world, player, active_locations, RegionName.t2_ornate_t3,
                                        t2_ornate_t3_locations)

    t3_main_locations = [
        LocationName.t3_s_balcony_turret_1,
        LocationName.t3_s_balcony_turret_2,
        LocationName.t3_n_turret_1,
        LocationName.t3_n_turret_2,
        LocationName.t3_boulder_block,
        LocationName.t3_e_turret_spikes,
    ]
    t3_main_region = create_region(world, player, active_locations, RegionName.t3_main, t3_main_locations)

    t3_n_node_blocks_locations = [
        LocationName.t3_s_gate,
        LocationName.t3_n_node_blocks_1,
        LocationName.t3_n_node_blocks_2,
        LocationName.t3_n_node_blocks_3,
        LocationName.t3_n_node_blocks_4,
        LocationName.t3_n_node_blocks_5,
    ]
    t3_n_node_blocks_region = create_region(world, player, active_locations, RegionName.t3_n_node_blocks,
                                            t3_n_node_blocks_locations)

    t3_n_node_locations = [
        LocationName.ev_t3_n_node
    ]
    t3_n_node_region = create_region(world, player, active_locations, RegionName.t3_n_node, t3_n_node_locations)

    t3_s_node_blocks_1_locations = [
        LocationName.t3_s_node_cache_1,
        LocationName.t3_s_node_cache_2,
        LocationName.t3_s_node_cache_3,
    ]
    t3_s_node_blocks_1_region = create_region(world, player, active_locations, RegionName.t3_s_node_blocks_1,
                                              t3_s_node_blocks_1_locations)

    t3_s_node_blocks_2_locations = [
        LocationName.t3_m_balcony_corridor,
    ]
    t3_s_node_blocks_2_region = create_region(world, player, active_locations, RegionName.t3_s_node_blocks_2,
                                              t3_s_node_blocks_2_locations)

    t3_s_node_locations = [
        LocationName.t3_n_node_1,
        LocationName.t3_n_node_2,
        LocationName.t3_n_node_3,
        LocationName.ev_t3_s_node,
    ]
    t3_s_node_region = create_region(world, player, active_locations, RegionName.t3_s_node, t3_s_node_locations)

    t3_boss_fall_1_locations = [
        LocationName.t3_boss_fall_1_1,
        LocationName.t3_boss_fall_1_2,
        LocationName.t3_boss_fall_1_3,
    ]
    t3_boss_fall_1_region = create_region(world, player, active_locations, RegionName.t3_boss_fall_1,
                                          t3_boss_fall_1_locations)

    t3_boss_fall_2_locations = [
        LocationName.t3_boss_fall_2_1,
        LocationName.t3_boss_fall_2_2,
        LocationName.t3_boss_fall_2_3,
    ]
    t3_boss_fall_2_region = create_region(world, player, active_locations, RegionName.t3_boss_fall_2,
                                          t3_boss_fall_2_locations)

    t3_boss_fall_3_locations = [
        LocationName.t3_boss_fall_3_1,
        LocationName.t3_boss_fall_3_2,
        LocationName.t3_boss_fall_3_3,
        LocationName.t3_boss_fall_3_4,
    ]
    t3_boss_fall_3_region = create_region(world, player, active_locations, RegionName.t3_boss_fall_3,
                                          t3_boss_fall_3_locations)

    pof_1_main_locations = [
        LocationName.pof_1_ent_1,
        LocationName.pof_1_ent_2,
        LocationName.pof_1_ent_3,
        LocationName.pof_1_ent_4,
        LocationName.pof_1_ent_5,
        LocationName.pof_1_sw_left_1,
        LocationName.pof_1_sw_left_2,
        LocationName.pof_1_sw_left_3,
        LocationName.pof_1_sw_left_4,
        LocationName.pof_1_sw_left_5,
        LocationName.pof_1_sw_left_6,
        LocationName.pof_1_sw_left_7,
        LocationName.pof_1_sw_left_8,
        LocationName.pof_1_sw_left_9,
        LocationName.pof_1_sw_left_10,
        LocationName.pof_1_sw_left_11,
    ]
    pof_1_main_region = create_region(world, player, active_locations, RegionName.pof_1_main, pof_1_main_locations)

    pof_1_se_room_locations = [
        LocationName.pof_1_s_1,
        LocationName.pof_1_s_2,
        LocationName.pof_1_s_3,
        LocationName.pof_1_s_4,
        LocationName.pof_1_s_5,
        LocationName.pof_1_s_6,
        LocationName.pof_1_s_7,
        LocationName.pof_1_s_8,
        LocationName.pof_1_s_9,
        LocationName.pof_1_s_10,
        LocationName.pof_1_s_11,
        LocationName.pof_1_s_12,
        LocationName.pof_1_s_13,
    ]
    pof_1_se_room_region = create_region(world, player, active_locations, RegionName.pof_1_se_room,
                                         pof_1_se_room_locations)

    pof_gate_1_locations = [
        LocationName.pof_1_confuse_corner_1,
        LocationName.pof_1_confuse_corner_2,
        LocationName.pof_1_confuse_corner_3,
        LocationName.pof_1_confuse_corner_4,
        LocationName.pof_1_c_hall_1,
        LocationName.pof_1_c_hall_2,
        LocationName.pof_1_c_hall_3,
        LocationName.pof_1_c_hall_4,
        LocationName.pof_1_c_hall_5,
        LocationName.pof_1_c_hall_6,
    ]
    pof_gate_1_region = create_region(world, player, active_locations, RegionName.pof_1_gate_1, pof_gate_1_locations)

    pof_1_n_room_locations = [
        LocationName.pof_1_n_1,
        LocationName.pof_1_n_2,
        LocationName.pof_1_n_3,
        LocationName.pof_1_n_4,
        LocationName.pof_1_n_5,
        LocationName.pof_1_n_6,
        LocationName.pof_1_n_7,
        LocationName.pof_1_n_8,
        LocationName.pof_1_n_9,
    ]
    pof_1_n_room_region = create_region(world, player, active_locations, RegionName.pof_1_n_room,
                                        pof_1_n_room_locations)

    pof_1_gate_2_locations = [
        LocationName.pof_1_end_1,
        LocationName.pof_1_end_2,
        LocationName.pof_1_end_3,
        LocationName.pof_1_end_4,
        LocationName.pof_1_end_5,
    ]
    pof_1_gate_2_region = create_region(world, player, active_locations, RegionName.pof_1_gate_2,
                                        pof_1_gate_2_locations)

    pof_2_main_locations = [
        LocationName.pof_2_ent_1,
        LocationName.pof_2_ent_2,
        LocationName.pof_2_ent_3,
        LocationName.pof_2_ent_4,
        LocationName.pof_2_ent_5,
        LocationName.pof_2_ent_6,
        LocationName.pof_2_confuse_hall_1,
        LocationName.pof_2_confuse_hall_2,
        LocationName.pof_2_confuse_hall_3,
        LocationName.pof_2_confuse_hall_4,
        LocationName.pof_2_sw_1,
        LocationName.pof_2_sw_2,
        LocationName.pof_2_sw_3,
        LocationName.pof_2_sw_4,
    ]
    pof_2_main_region = create_region(world, player, active_locations, RegionName.pof_2_main, pof_2_main_locations)

    pof_2_n_locations = [
        LocationName.pof_2_ne_1,
        LocationName.pof_2_ne_2,
        LocationName.pof_2_ne_3,
        LocationName.pof_2_ne_4,
    ]
    pof_2_n_region = create_region(world, player, active_locations, RegionName.pof_2_n, pof_2_n_locations)

    pof_3_main_locations = [
        LocationName.pof_3_safety_room_1,
        LocationName.pof_3_safety_room_2,
        LocationName.pof_3_safety_room_3,
        LocationName.pof_3_end_1,
        LocationName.pof_3_end_2,
        LocationName.pof_3_end_3,
        LocationName.pof_3_end_4,
        LocationName.pof_3_end_5,
        LocationName.ev_pof_end
    ]
    pof_3_main_region = create_region(world, player, active_locations, RegionName.pof_3_main, pof_3_main_locations)

    b3_main_region = create_region(world, player, active_locations, RegionName.b3_main, [])
    b3_platform_1_region = create_region(world, player, active_locations, RegionName.b3_platform_1, [])
    b3_platform_2_region = create_region(world, player, active_locations, RegionName.b3_platform_2, [])
    b3_platform_3_region = create_region(world, player, active_locations, RegionName.b3_platform_3, [])

    b3_defeated_locations = [
        LocationName.ev_victory
    ]
    b3_defeated_region = create_region(world, player, active_locations, RegionName.b3_defeated, b3_defeated_locations)

    world.regions += [
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
        t1_telariana_melt_ice_region,
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
    ]

    connect_tots_regions(world, player, active_locations)


def connect_tots_regions(world, player: int, active_locations):
    used_names: typing.Dict[str, int] = {}

    def has_pan(state):
        return state.has(ItemName.pan, player) \
               or state.has(ItemName.pan_fragment, player, world.pan_fragments[player].value)

    def has_lever(state):
        return state.has(ItemName.lever, player) \
               or state.has(ItemName.lever_fragment, player, world.lever_fragments[player].value)

    def has_pickaxe(state):
        return state.has(ItemName.pickaxe, player) \
               or state.has(ItemName.pickaxe_fragment, player, world.pickaxe_fragments[player].value)

    connect(world, player, used_names, RegionName.menu, RegionName.hub_main)

    connect(world, player, used_names, RegionName.hub_main, RegionName.hub_rocks, has_pickaxe)
    connect(world, player, used_names, RegionName.hub_main, RegionName.cave_3_fall, has_pickaxe)
    # For the temple entrances in the hub
    connect(world, player, used_names, RegionName.hub_rocks, RegionName.t3_main)
    connect(world, player, used_names, RegionName.hub_main, RegionName.temple_entrance)

    connect(world, player, used_names, RegionName.hub_main, RegionName.library)
    connect(world, player, used_names, RegionName.library, RegionName.cave_3_main)
    connect(world, player, used_names, RegionName.cave_3_main, RegionName.cave_3_fields, has_lever)

    connect(world, player, used_names, RegionName.cave_3_main, RegionName.cave_2_main)
    connect(world, player, used_names, RegionName.cave_2_main, RegionName.cave_2_pumps, has_lever)

    connect(world, player, used_names, RegionName.cave_2_main, RegionName.cave_1_main)
    connect(world, player, used_names, RegionName.cave_1_main, RegionName.cave_1_blue_bridge)
    connect(world, player, used_names, RegionName.cave_1_blue_bridge, RegionName.cave_1_red_bridge)
    connect(world, player, used_names, RegionName.cave_1_main, RegionName.cave_1_pumps, has_lever)
    connect(world, player, used_names, RegionName.cave_1_pumps, RegionName.cave_1_green_bridge)
    connect(world, player, used_names, RegionName.cave_1_green_bridge, RegionName.boss2_main)
    connect(world, player, used_names, RegionName.boss2_main, RegionName.boss2_defeated)

    connect(world, player, used_names, RegionName.cave_1_red_bridge, RegionName.boss_1_main)
    connect(world, player, used_names, RegionName.boss_1_main, RegionName.boss_1_defeated,
            lambda state: (state.has(ItemName.key_gold, player, 1)))

    connect(world, player, used_names, RegionName.boss_1_defeated, RegionName.passage_entrance)
    connect(world, player, used_names, RegionName.passage_entrance, RegionName.passage_mid)
    connect(world, player, used_names, RegionName.passage_mid, RegionName.passage_end)

    connect(world, player, used_names, RegionName.passage_end, RegionName.temple_entrance_back)
    connect(world, player, used_names, RegionName.temple_entrance_back, RegionName.temple_entrance,
            lambda state: (state.has(ItemName.open_temple_entrance_shortcut, player)))
    connect(world, player, used_names, RegionName.temple_entrance_back, RegionName.t1_main)

    connect(world, player, used_names, RegionName.t1_main, RegionName.t1_sw_cache,
            lambda state: (state.has(ItemName.key_silver, player, 1)))
    connect(world, player, used_names, RegionName.t1_main, RegionName.t1_node_1,
            lambda state: (state.has(ItemName.mirror, player, 3)))
    connect(world, player, used_names, RegionName.t1_node_1, RegionName.cave_3_secret)
    connect(world, player, used_names, RegionName.t1_node_1, RegionName.t1_sun_turret,
            lambda state: (state.has(ItemName.key_silver, player, 2)))
    connect(world, player, used_names, RegionName.t1_node_1, RegionName.t1_ice_turret,
            lambda state: (state.has(ItemName.key_gold, player, 2)))
    connect(world, player, used_names, RegionName.t1_ice_turret, RegionName.t1_telariana_melt_ice,
            lambda state: (state.has(ItemName.krilith_defeated, player)))
    t1_key_ordering = world.random.randint(0, 1)
    connect(world, player, used_names, RegionName.t1_ice_turret, RegionName.t1_n_of_ice_turret,
            lambda state: (state.has(ItemName.key_silver, player, 3 + t1_key_ordering)))
    connect(world, player, used_names, RegionName.t1_ice_turret, RegionName.t1_s_of_ice_turret,
            lambda state: (state.has(ItemName.key_silver, player, 3 - t1_key_ordering)))
    connect(world, player, used_names, RegionName.t1_ice_turret, RegionName.t1_east,
            lambda state: (state.has(ItemName.key_gold, player, 3)))
    connect(world, player, used_names, RegionName.t1_east, RegionName.t1_sun_block_hall,
            lambda state: (state.has(ItemName.mirror, player, 6)))
    connect(world, player, used_names, RegionName.t1_east, RegionName.t1_node_2,
            lambda state: (state.has(ItemName.mirror, player, 7)))
    connect(world, player, used_names, RegionName.t1_east, RegionName.t1_ice_chamber_melt_ice,
            lambda state: (state.has(ItemName.krilith_defeated, player)))

    connect(world, player, used_names, RegionName.t1_east, RegionName.t2_main)
    connect(world, player, used_names, RegionName.t2_main, RegionName.t2_melt_ice,
            lambda state: (state.has(ItemName.krilith_defeated, player)))
    t2_key_ordering = world.random.randint(0, 1)
    connect(world, player, used_names, RegionName.t2_main, RegionName.t2_n_gate,
            lambda state: (state.has(ItemName.key_silver, player, 5 + t2_key_ordering))
                          and (state.has(ItemName.krilith_defeated, player)))
    connect(world, player, used_names, RegionName.t2_main, RegionName.t2_s_gate,
            lambda state: (state.has(ItemName.key_silver, player, 5 - t2_key_ordering))
                          and (state.has(ItemName.krilith_defeated, player)))
    connect(world, player, used_names, RegionName.t2_main, RegionName.t2_ornate,
            lambda state: (state.has(ItemName.key_gold, player, 4)))
    connect(world, player, used_names, RegionName.t2_n_gate, RegionName.t2_n_node,
            lambda state: (state.has(ItemName.mirror, player, 10)))
    connect(world, player, used_names, RegionName.t2_s_gate, RegionName.t2_s_node,
            lambda state: (state.has(ItemName.mirror, player, 14)))
    connect(world, player, used_names, RegionName.t2_main, RegionName.t2_light_bridges,
            lambda state: (state.has(ItemName.t2_bridge_switch, player, 5)))
    connect(world, player, used_names, RegionName.t2_light_bridges, RegionName.cave_3_portal)
    connect(world, player, used_names, RegionName.t2_light_bridges, RegionName.cave_1_temple)

    connect(world, player, used_names, RegionName.t3_main, RegionName.t2_ornate_t3)
    mirrors_needed_n = 14
    mirrors_needed_s = 14
    node_dir = world.random.randrange(2)
    if node_dir == 0:
        mirrors_needed_s = 17
    else:
        mirrors_needed_n = 17
    connect(world, player, used_names, RegionName.t3_main, RegionName.t3_n_node_blocks,
            lambda state: (state.has(ItemName.mirror, player, mirrors_needed_n + 2)))
    connect(world, player, used_names, RegionName.t3_n_node_blocks, RegionName.t3_n_node,
            lambda state: (state.has(ItemName.mirror, player, mirrors_needed_n + 3)))
    connect(world, player, used_names, RegionName.t3_main, RegionName.t3_s_node_blocks_1,
            lambda state: (state.has(ItemName.mirror, player, mirrors_needed_s + 1)))
    connect(world, player, used_names, RegionName.t3_s_node_blocks_1, RegionName.t3_s_node_blocks_2,
            lambda state: (state.has(ItemName.mirror, player, mirrors_needed_s + 2)))
    connect(world, player, used_names, RegionName.t3_s_node_blocks_2, RegionName.t3_s_node,
            lambda state: (state.has(ItemName.mirror, player, mirrors_needed_s + 3)))

    connect(world, player, used_names, RegionName.hub_main, RegionName.pof_1_main,
            lambda state: (state.has(ItemName.pof_switch, player, 6)))
    connect(world, player, used_names, RegionName.pof_1_main, RegionName.pof_1_se_room)
    connect(world, player, used_names, RegionName.pof_1_se_room, RegionName.pof_1_gate_1,
            lambda state: (state.has(ItemName.bonus_key, player, 1)))
    connect(world, player, used_names, RegionName.pof_1_gate_1, RegionName.pof_1_n_room)
    connect(world, player, used_names, RegionName.pof_1_n_room, RegionName.pof_1_gate_2,
            lambda state: (state.has(ItemName.bonus_key, player, 2)))
    connect(world, player, used_names, RegionName.pof_1_gate_2, RegionName.pof_2_main)
    connect(world, player, used_names, RegionName.pof_2_main, RegionName.pof_2_n)
    connect(world, player, used_names, RegionName.pof_2_n, RegionName.pof_3_main)
    connect(world, player, used_names, RegionName.pof_3_main, RegionName.hub_pyramid_of_fear,
            lambda state: (state.has(ItemName.pof_complete, player)))

    connect(world, player, used_names, RegionName.hub_main, RegionName.b3_main,
            lambda state: (state.has(ItemName.solar_node, player, 6)))
    connect(world, player, used_names, RegionName.b3_main, RegionName.b3_platform_1)
    connect(world, player, used_names, RegionName.b3_platform_1, RegionName.b3_platform_2)
    connect(world, player, used_names, RegionName.b3_platform_2, RegionName.b3_platform_3)
    connect(world, player, used_names, RegionName.b3_platform_3, RegionName.b3_defeated)


def create_region(world: MultiWorld, player: int, active_locations: typing.Dict[str, LocationData], name: str,
                  locations: typing.List[str]) -> Region:
    region = Region(name, RegionType.Generic, name, player, world)
    if locations:
        for location in locations:
            if location not in active_locations.keys():
                continue
            region.locations.append(HammerwatchLocation(player, location, active_locations[location].code, region))
    return region


def connect(world: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

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
