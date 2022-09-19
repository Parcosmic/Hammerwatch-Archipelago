import typing

from BaseClasses import Location
from .Names import LocationName, ItemName
from .Util import Counter
from .Items import castle_item_counts, temple_item_counts
from random import Random
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


castle_pickup_locations: typing.Dict[str, LocationData] = {

}

castle_shop_locations: typing.Dict[str, LocationData] = {

}

castle_event_locations: typing.Dict[str, LocationData] = {

}

castle_locations: typing.Dict[str, LocationData] = {
    **castle_pickup_locations,
    **castle_event_locations
}

counter = Counter(0x130000)
temple_pickup_locations: typing.Dict[str, LocationData] = {
    LocationName.hub_field_nw: LocationData(counter.count(0)),
    LocationName.hub_on_rock: LocationData(counter.count()),
    LocationName.hub_pof_reward: LocationData(counter.count()),
    LocationName.hub_west_pyramid: LocationData(counter.count()),
    LocationName.hub_rocks_south: LocationData(counter.count()),
    LocationName.hub_field_north: LocationData(counter.count()),
    LocationName.hub_behind_temple_entrance: LocationData(counter.count()),
    LocationName.hub_behind_shops: LocationData(counter.count()),
    LocationName.hub_front_of_pof: LocationData(counter.count()),
    LocationName.hub_field_south: LocationData(counter.count()),

    LocationName.cave3_portal_r: LocationData(counter.count()),
    LocationName.cave3_n: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave3_outside_guard: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave3_portal_l: LocationData(counter.count()),
    LocationName.cave3_fall_se: LocationData(counter.count()),
    LocationName.cave3_ne: LocationData(counter.count()),
    LocationName.cave3_nw: LocationData(counter.count()),
    LocationName.cave3_m: LocationData(counter.count()),
    LocationName.cave3_se: LocationData(counter.count()),
    LocationName.cave3_captain: LocationData(counter.count()),
    LocationName.cave3_fall_sw: LocationData(counter.count()),
    LocationName.cave3_squire: LocationData(counter.count()),
    LocationName.cave3_captain_dock: LocationData(counter.count()),
    LocationName.cave3_fall_ne: LocationData(counter.count()),
    LocationName.cave3_fields_r: LocationData(counter.count()),
    LocationName.cave3_trapped_guard: LocationData(counter.count()),
    LocationName.cave3_secret_n: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave3_secret_nw: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave3_secret_s: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave3_secret_6: LocationData(counter.count()),
    LocationName.cave3_secret_7: LocationData(counter.count()),
    LocationName.cave3_secret_8: LocationData(counter.count()),
    LocationName.cave3_secret_5: LocationData(counter.count()),
    LocationName.cave3_secret_2: LocationData(counter.count()),
    LocationName.cave3_secret_3: LocationData(counter.count()),
    LocationName.cave3_secret_4: LocationData(counter.count()),
    LocationName.cave3_secret_1: LocationData(counter.count()),
    LocationName.cave3_secret_9: LocationData(counter.count()),
    LocationName.cave3_secret_10: LocationData(counter.count()),
    LocationName.cave3_secret_11: LocationData(counter.count()),
    LocationName.cave3_secret_12: LocationData(counter.count()),
    LocationName.cave3_fall_nw: LocationData(counter.count()),
    LocationName.cave3_half_bridge: LocationData(counter.count()),
    LocationName.cave3_guard: LocationData(counter.count()),

    LocationName.cave2_sw_hidden_room_3: LocationData(counter.count()),
    LocationName.cave2_pumps_wall_r: LocationData(counter.count()),
    LocationName.cave2_below_pumps_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_below_pumps_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_double_bridge_l_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_double_bridge_l_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_nw_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_nw_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_pumps_wall_l: LocationData(counter.count()),
    LocationName.cave2_water_n_r_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_water_s: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_w_miniboss_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_w_miniboss_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_w_miniboss_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_red_bridge_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_red_bridge_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_e_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_guard_n: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave2_red_bridge_2: LocationData(counter.count()),
    LocationName.cave2_double_bridge_m: LocationData(counter.count()),
    LocationName.cave2_nw_2: LocationData(counter.count()),
    LocationName.cave2_red_bridge_4: LocationData(counter.count()),
    LocationName.cave2_double_bridge_r: LocationData(counter.count()),
    LocationName.cave2_water_n_r_1: LocationData(counter.count()),
    LocationName.cave2_green_bridge: LocationData(counter.count()),
    LocationName.cave2_sw_hidden_room_1: LocationData(counter.count()),
    LocationName.cave2_guard_s: LocationData(counter.count()),
    LocationName.cave2_nw_3: LocationData(counter.count()),
    LocationName.cave2_w_miniboss_4: LocationData(counter.count()),
    LocationName.cave2_red_bridge_3: LocationData(counter.count()),
    LocationName.cave2_below_pumps_3: LocationData(counter.count()),
    LocationName.cave2_secret_ne: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave2_secret_w: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave2_secret_m: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave2_water_n_l: LocationData(counter.count()),
    LocationName.cave2_nw_1: LocationData(counter.count()),
    LocationName.cave2_sw: LocationData(counter.count()),
    LocationName.cave2_double_bridge_secret: LocationData(counter.count()),
    LocationName.cave2_sw_hidden_room_2: LocationData(counter.count()),
    LocationName.cave2_pumps_n: LocationData(counter.count()),
    LocationName.cave2_guard: LocationData(counter.count()),
    LocationName.cave2_red_bridge_1: LocationData(counter.count()),
    LocationName.cave2_sw_hidden_room_4: LocationData(counter.count()),

    LocationName.cave1_secret_tunnel_1: LocationData(counter.count()),
    LocationName.cave1_temple_end_3: LocationData(counter.count()),
    LocationName.cave1_n_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_w_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_w_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_temple_hall_2: LocationData(counter.count()),
    LocationName.cave1_water_s_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_water_s_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_bridges_4: LocationData(counter.count()),
    LocationName.cave1_double_room_l: LocationData(counter.count()),
    LocationName.cave1_e_3: LocationData(counter.count()),
    LocationName.cave1_green_bridge_2: LocationData(counter.count()),
    LocationName.cave1_n_bridges_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_secret_tunnel_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_room_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_se_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_se_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_s_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_ne_5: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_w_by_water_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_e_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_double_room_r: LocationData(counter.count()),
    LocationName.cave1_krilith_ledge_n: LocationData(counter.count()),
    LocationName.cave1_red_bridge_e: LocationData(counter.count()),
    LocationName.cave1_ne_hidden_room_3: LocationData(counter.count()),
    LocationName.cave1_water_s_shore: LocationData(counter.count()),
    LocationName.cave1_temple_end_2: LocationData(counter.count()),
    LocationName.cave1_krilith_door: LocationData(counter.count()),
    LocationName.cave1_temple_end_4: LocationData(counter.count()),
    LocationName.cave1_ne_grubs: LocationData(counter.count()),
    LocationName.cave1_w_by_water_2: LocationData(counter.count()),
    LocationName.cave1_m: LocationData(counter.count()),
    LocationName.cave1_secret_nw: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_n_hidden_room: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_ne: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_w: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_m: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_secret_e: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.cave1_temple_hall_1: LocationData(counter.count()),
    LocationName.cave1_temple_hall_3: LocationData(counter.count()),
    LocationName.cave1_n_bridges_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_temple_end_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_secret_tunnel_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.cave1_n_3: LocationData(counter.count()),
    LocationName.cave1_ne_hidden_room_4: LocationData(counter.count()),
    LocationName.cave1_n_bridges_1: LocationData(counter.count()),
    LocationName.cave1_krilith_ledge_e: LocationData(counter.count()),
    LocationName.cave1_green_bridge_1: LocationData(counter.count()),
    LocationName.cave1_e_2: LocationData(counter.count()),
    LocationName.cave1_s_3: LocationData(counter.count()),
    LocationName.cave1_ne_hidden_room_5: LocationData(counter.count()),
    LocationName.cave1_ne_hidden_room_1: LocationData(counter.count()),
    LocationName.cave1_ne_hidden_room_2: LocationData(counter.count()),
    LocationName.cave1_n_bridges_5: LocationData(counter.count()),

    LocationName.boss1_bridge: LocationData(counter.count()),
    LocationName.boss1_guard_r_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.boss1_guard_r_2: LocationData(counter.count(), LocationClassification.Recovery),
    # LocationName.boss1_drop_2: LocationData(counter.count()),
    # LocationName.boss1_drop: LocationData(counter.count()),
    LocationName.boss1_guard_l: LocationData(counter.count(3), LocationClassification.Recovery),
    LocationName.boss1_bridge_n: LocationData(counter.count()),
    LocationName.boss1_secret: LocationData(counter.count(), LocationClassification.Secret),

    LocationName.p_mid4_2: LocationData(counter.count()),
    LocationName.p_end3_1: LocationData(counter.count()),
    LocationName.p_mid4_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.p_mid4_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.p_mid2_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.p_mid2_2: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.p_mid2_3: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.p_mid2_4: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.p_mid4_1: LocationData(counter.count(), LocationClassification.Recovery),
    LocationName.p_mid5_2: LocationData(counter.count()),
    LocationName.p_end3_2: LocationData(counter.count()),
    LocationName.p_ent2_secret: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.p_mid3_secret_1: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.p_mid3_secret_2: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.p_mid3_secret_3: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.p_mid3_secret_4: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.p_end1_secret: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.p_mid5_secret: LocationData(counter.count(), LocationClassification.Secret),
    LocationName.p_mid1_2: LocationData(counter.count()),
    LocationName.p_mid1_1: LocationData(counter.count()),
    LocationName.p_mid5_1: LocationData(counter.count()),

    LocationName.temple_entrance_l: LocationData(counter.count()),
    LocationName.temple_entrance_r: LocationData(counter.count()),

    LocationName.t1_double_gate_behind_block: LocationData(counter.count()),
    LocationName.t1_sw_hidden_room_3: LocationData(counter.count()),
    LocationName.t1_telariana_ice: LocationData(counter.count()),
    LocationName.t1_sun_turret_1: LocationData(counter.count()),
    LocationName.t1_telariana_2: LocationData(counter.count()),
    LocationName.t1_boulder_hallway_by_ice_turret_2: LocationData(counter.count()),
    LocationName.t1_boulder_hallway_by_ice_turret_1: LocationData(counter.count()),
    LocationName.t1_boulder_hallway_by_ice_turret_3: LocationData(counter.count()),
    LocationName.t1_telariana_3: LocationData(counter.count()),
    LocationName.t1_node_2_passage_3: LocationData(counter.count()),
    LocationName.t1_node_2_passage_1: LocationData(counter.count()),
    LocationName.t1_fire_trap_by_sun_turret_1: LocationData(counter.count()),
    LocationName.t1_fire_trap_by_sun_turret_2: LocationData(counter.count()),
    LocationName.t1_e_of_double_gate_room_4: LocationData(counter.count()),
    LocationName.t1_e_of_double_gate_room_3: LocationData(counter.count()),
    LocationName.t1_sw_sun_room_1: LocationData(counter.count()),
    LocationName.t1_sw_sun_room_2: LocationData(counter.count()),
    LocationName.t1_ice_block_chamber_ice: LocationData(counter.count()),
    LocationName.t1_sun_turret_2: LocationData(counter.count()),
    LocationName.t1_n_cache_by_ice_turret_5: LocationData(counter.count()),
    LocationName.t1_s_cache_by_ice_turret_3: LocationData(counter.count()),
    LocationName.t1_sw_cache_2: LocationData(counter.count()),
    LocationName.t1_sw_hidden_room_4: LocationData(counter.count()),
    LocationName.t1_sun_turret_3: LocationData(counter.count()),
    LocationName.t1_s_bridge_4: LocationData(counter.count()),
    LocationName.t1_s_bridge_5: LocationData(counter.count()),
    LocationName.t1_s_bridge_6: LocationData(counter.count()),
    LocationName.t1_n_cache_by_ice_turret_1: LocationData(counter.count()),
    LocationName.t1_n_sunbeam_treasure_2: LocationData(counter.count()),
    LocationName.t1_s_cache_by_ice_turret_2: LocationData(counter.count()),
    LocationName.t1_sw_cache_1: LocationData(counter.count()),
    LocationName.t1_sw_cache_4: LocationData(counter.count()),
    LocationName.t1_sw_cache_5: LocationData(counter.count()),
    LocationName.t1_ledge_after_block_trap_2: LocationData(counter.count()),
    LocationName.t1_ice_block_chamber_3: LocationData(counter.count()),
    LocationName.t1_ice_block_chamber_2: LocationData(counter.count()),
    LocationName.t1_double_gate_1: LocationData(counter.count()),
    LocationName.t1_ice_block_chamber_1: LocationData(counter.count()),
    LocationName.t1_sun_block_hall_3: LocationData(counter.count()),
    LocationName.t1_fire_trap_by_sun_turret_4: LocationData(counter.count()),
    LocationName.t1_behind_bars_entrance: LocationData(counter.count()),
    LocationName.t1_mana_drain_fire_trap: LocationData(counter.count()),
    LocationName.t1_e_gold_beetles: LocationData(counter.count()),
    LocationName.t1_sun_block_hall_1: LocationData(counter.count()),
    LocationName.t1_sw_hidden_room_2: LocationData(counter.count()),
    LocationName.t1_mana_drain_fire_trap_reward_2: LocationData(counter.count()),
    LocationName.t1_mana_drain_fire_trap_reward_1: LocationData(counter.count()),
    LocationName.t1_sun_block_hall_4: LocationData(counter.count()),
    LocationName.t1_fire_trap_by_sun_turret_3: LocationData(counter.count()),
    LocationName.t1_ledge_after_block_trap_1: LocationData(counter.count()),
    LocationName.t1_sw_cache_3: LocationData(counter.count()),
    LocationName.t1_n_sunbeam_treasure_3: LocationData(counter.count()),
    LocationName.t1_boulder_hallway_by_ice_turret_4: LocationData(counter.count()),
    LocationName.t1_ice_turret_1: LocationData(counter.count()),
    LocationName.t1_ice_turret_2: LocationData(counter.count()),
    LocationName.t1_above_s_bridge: LocationData(counter.count()),
    LocationName.t1_e_of_double_gate_room_2: LocationData(counter.count()),
    LocationName.t1_sw_corner_room: LocationData(counter.count()),
    LocationName.t1_s_bridge_1: LocationData(counter.count()),
    LocationName.t1_sun_block_hall_2: LocationData(counter.count()),
    LocationName.t1_mana_drain_fire_trap_passage: LocationData(counter.count()),
    LocationName.t1_n_sunbeam: LocationData(counter.count()),
    LocationName.t1_n_cache_by_ice_turret_4: LocationData(counter.count()),
    LocationName.t1_node_2_passage_2: LocationData(counter.count()),
    LocationName.t1_double_gate_hidden: LocationData(counter.count()),
    LocationName.t1_ice_turret_boulder_break_block: LocationData(counter.count()),
    LocationName.t1_e_of_double_gate_room_1: LocationData(counter.count()),
    LocationName.t1_sw_hidden_room_1: LocationData(counter.count()),
    LocationName.t1_n_cache_by_ice_turret_2: LocationData(counter.count()),
    LocationName.t1_n_cache_by_ice_turret_3: LocationData(counter.count()),
    LocationName.t1_n_sunbeam_treasure_1: LocationData(counter.count()),
    LocationName.t1_telariana_4: LocationData(counter.count()),
    LocationName.t1_telariana_1: LocationData(counter.count()),
    LocationName.t1_node_2_1: LocationData(counter.count()),
    LocationName.t1_node_2_2: LocationData(counter.count()),
    LocationName.t1_s_of_sun_turret: LocationData(counter.count()),
    LocationName.t1_double_gate_2: LocationData(counter.count()),
    LocationName.t1_double_gate_3: LocationData(counter.count()),
    LocationName.t1_s_cache_by_ice_turret_1: LocationData(counter.count()),
    LocationName.t1_s_bridge_2: LocationData(counter.count()),
    LocationName.t1_s_bridge_3: LocationData(counter.count()),
    LocationName.t1_telariana_5: LocationData(counter.count()),
}

temple_shop_locations: typing.Dict[str, LocationData] = {

}

temple_event_locations: typing.Dict[str, LocationData] = {
    LocationName.ev_temple_entrance_rock: LocationData(None),
    LocationName.ev_hub_pof_switch: LocationData(None),
    LocationName.ev_cave3_pof_switch: LocationData(None),
    LocationName.ev_cave2_pof_switch: LocationData(None),
    LocationName.ev_cave1_pof_switch: LocationData(None),
    LocationName.ev_temple1_pof_switch: LocationData(None),
    LocationName.ev_pof_end: LocationData(None),
    LocationName.ev_krilith_defeated: LocationData(None),
}

temple_locations: typing.Dict[str, LocationData] = {
    **temple_pickup_locations
}

common_event_locations: typing.Dict[str, LocationData] = {
    LocationName.ev_victory: LocationData(None),
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


def setup_locations(world, player: int):
    location_table: typing.Dict[str, LocationData]

    if world.map[player] == 0:  # Castle Hammerwatch
        location_table = {}
        for name, data in castle_locations.items():
            if data.classification != LocationClassification.Recovery or world.randomize_recovery_items[player].value:
                location_table.update({name: data})
        if world.random_location_behavior[player] == 0:
            location_table = choose_castle_random_locations(world, player, location_table)
            pass
        # if world.randomize_shops[player].value:
        #    location_table.update({**castle_shop_locations})
        location_table.update(castle_event_locations)
    else:  # Temple of the Sun
        location_table = {}
        for name, data in temple_locations.items():
            if data.classification != LocationClassification.Recovery\
                    or world.randomize_recovery_items[player].value == 1:
                location_table.update({name: data})
        if world.random_location_behavior[player] == 0:
            location_table = choose_tots_random_locations(world, player, location_table)
            pass
        # if world.randomize_shops[player].value:
        #    location_table.update({**temple_shop_locations})
        location_table.update(temple_event_locations)

    location_table.update(common_event_locations)

    return location_table


random_locations: typing.Dict[str, int] = {
}


def choose_castle_random_locations(world, player: int, location_table: typing.Dict[str, LocationData]):
    return location_table


def choose_tots_random_locations(world, player: int, location_table: typing.Dict[str, LocationData]):
    if world.random_location_behavior[player].value == 0:
        random = Random(world.seed)

        def remove_location(location: str, item: str):
            location_table.pop(location)
            temple_item_counts[item] -= 1

        def remove_secret(secret_location: str):
            if secret_location in location_table.keys():
                remove_location(secret_location, ItemName.secret)

        # Secrets
        if world.randomize_secrets[player].value:
            random_locations[LocationName.rloc_c3_secret_n] = random.randrange(2)
            random_locations[LocationName.rloc_c3_secret_nw] = random.randrange(2)
            random_locations[LocationName.rloc_c3_secret_s] = random.randrange(2)
            random_locations[LocationName.rloc_c2_secret_1] = random.randrange(2)
            random_locations[LocationName.rloc_c2_secret_2] = random.randrange(2)
            random_locations[LocationName.rloc_c2_secret_3] = random.randrange(2)
            random_locations[LocationName.rloc_c1_secret_1] = random.randrange(2)
            random_locations[LocationName.rloc_c1_secret_2] = random.randrange(2)
            random_locations[LocationName.rloc_c1_secret_3] = random.randrange(2)
            random_locations[LocationName.rloc_c1_secret_4] = random.randrange(2)
            random_locations[LocationName.rloc_c1_secret_5] = random.randrange(2)
            random_locations[LocationName.rloc_c1_secret_6] = random.randrange(2)
            random_locations[LocationName.rloc_b1_secret] = random.randrange(2)
            random_locations[LocationName.rloc_p_secret_1] = random.randrange(2)
            random_locations[LocationName.rloc_p_secret_2] = random.randrange(2)
            random_locations[LocationName.rloc_p_secret_3] = random.randrange(2)
            random_locations[LocationName.rloc_p_secret_4] = random.randrange(2)
            random_locations[LocationName.rloc_p_secret_5] = random.randrange(2)
            random_locations[LocationName.rloc_p_secret_6] = random.randrange(2)
            random_locations[LocationName.rloc_p_secret_7] = random.randrange(2)
        else:
            random_locations[LocationName.rloc_c3_secret_n] = 0
            random_locations[LocationName.rloc_c3_secret_nw] = 0
            random_locations[LocationName.rloc_c3_secret_s] = 0
            random_locations[LocationName.rloc_c2_secret_1] = 0
            random_locations[LocationName.rloc_c2_secret_2] = 0
            random_locations[LocationName.rloc_c2_secret_3] = 0
            random_locations[LocationName.rloc_c1_secret_1] = 0
            random_locations[LocationName.rloc_c1_secret_2] = 0
            random_locations[LocationName.rloc_c1_secret_3] = 0
            random_locations[LocationName.rloc_c1_secret_4] = 0
            random_locations[LocationName.rloc_c1_secret_5] = 0
            random_locations[LocationName.rloc_c1_secret_6] = 0
            random_locations[LocationName.rloc_b1_secret] = 0
            random_locations[LocationName.rloc_p_secret_1] = 0
            random_locations[LocationName.rloc_p_secret_2] = 0
            random_locations[LocationName.rloc_p_secret_3] = 0
            random_locations[LocationName.rloc_p_secret_4] = 0
            random_locations[LocationName.rloc_p_secret_5] = 0
            random_locations[LocationName.rloc_p_secret_6] = 0
            random_locations[LocationName.rloc_p_secret_7] = 0
        if random_locations[LocationName.rloc_c3_secret_n] == 0:
            remove_secret(LocationName.cave3_secret_n)
        if random_locations[LocationName.rloc_c3_secret_nw] == 0:
            remove_secret(LocationName.cave3_secret_nw)
        if random_locations[LocationName.rloc_c3_secret_s] == 0:
            remove_secret(LocationName.cave3_secret_s)
        if random_locations[LocationName.rloc_c2_secret_1] == 0:
            remove_secret(LocationName.cave2_secret_ne)
        if random_locations[LocationName.rloc_c2_secret_2] == 0:
            remove_secret(LocationName.cave2_secret_w)
        if random_locations[LocationName.rloc_c2_secret_3] == 0:
            remove_secret(LocationName.cave2_secret_m)
        if random_locations[LocationName.rloc_c1_secret_1] == 0:
            remove_secret(LocationName.cave1_secret_nw)
        if random_locations[LocationName.rloc_c1_secret_2] == 0:
            remove_secret(LocationName.cave1_secret_n_hidden_room)
        if random_locations[LocationName.rloc_c1_secret_3] == 0:
            remove_secret(LocationName.cave1_secret_ne)
        if random_locations[LocationName.rloc_c1_secret_4] == 0:
            remove_secret(LocationName.cave1_secret_w)
        if random_locations[LocationName.rloc_c1_secret_5] == 0:
            remove_secret(LocationName.cave1_secret_m)
        if random_locations[LocationName.rloc_c1_secret_6] == 0:
            remove_secret(LocationName.cave1_secret_e)
        if random_locations[LocationName.rloc_b1_secret] == 0:
            remove_secret(LocationName.boss1_secret)
        if random_locations[LocationName.rloc_p_secret_1] == 0:
            remove_secret(LocationName.p_ent2_secret)
        if random_locations[LocationName.rloc_p_secret_2] == 0:
            remove_secret(LocationName.p_mid3_secret_1)
        if random_locations[LocationName.rloc_p_secret_3] == 0:
            remove_secret(LocationName.p_mid3_secret_2)
        if random_locations[LocationName.rloc_p_secret_4] == 0:
            remove_secret(LocationName.p_mid3_secret_3)
        if random_locations[LocationName.rloc_p_secret_5] == 0:
            remove_secret(LocationName.p_mid3_secret_4)
        if random_locations[LocationName.rloc_p_secret_6] == 0:
            remove_secret(LocationName.p_end1_secret)
        if random_locations[LocationName.rloc_p_secret_7] == 0:
            remove_secret(LocationName.p_mid5_secret)
        # Cave level 3
        random_locations[LocationName.rloc_squire] = random.randrange(6)
        if random_locations[LocationName.rloc_squire] != 1:
            remove_location(LocationName.cave3_squire, ItemName.stat_upgrade)
        # Pan location
        random_locations[LocationName.rloc_pan] = random.randrange(9)
        pan_locations: typing.List[str] = [
            LocationName.cave3_nw,
            LocationName.cave3_m,
            LocationName.cave3_se,
            LocationName.cave2_nw_2,
            LocationName.cave2_red_bridge_4,
            LocationName.cave2_double_bridge_r,
            LocationName.cave1_n_bridges_4,
            LocationName.cave1_double_room_l,
            LocationName.cave1_e_3,
        ]
        location_table = keep_one_location(location_table, pan_locations, random_locations[LocationName.rloc_pan])
        # Cave level 2
        random_locations[LocationName.rloc_c2_keystone] = random.randrange(5)
        c2_keystone_locations: typing.List[str] = [
            LocationName.cave2_guard_s,
            LocationName.cave2_nw_3,
            LocationName.cave2_w_miniboss_4,
            LocationName.cave2_red_bridge_3,
            LocationName.cave2_below_pumps_3
        ]
        location_table = keep_one_location(location_table, c2_keystone_locations,
                                           random_locations[LocationName.rloc_c2_keystone])
        random_locations[LocationName.rloc_c2_portal] = random.randrange(3)
        if random_locations[LocationName.rloc_c2_portal] == 0:
            remove_location(LocationName.cave2_nw_4, ItemName.apple)
            remove_location(LocationName.cave2_nw_5, ItemName.apple)
        elif random_locations[LocationName.rloc_c2_portal] == 1:
            remove_location(LocationName.cave2_pumps_n, ItemName.vendor_coin)
        random_locations[LocationName.rloc_c2_hidden_room] = random.randrange(4)
        if random_locations[LocationName.rloc_c2_hidden_room] >= 2:
            remove_location(LocationName.cave2_sw_hidden_room_1, ItemName.vendor_coin)
            remove_location(LocationName.cave2_sw_hidden_room_2, ItemName.stat_upgrade)
            remove_location(LocationName.cave2_sw_hidden_room_3, ItemName.ankh)
            remove_location(LocationName.cave2_sw_hidden_room_4, ItemName.chest_wood)
        # Cave level 1
        random_locations[LocationName.rloc_c1_keystone] = random.randrange(3)
        c1_keystone_locations: typing.List[str] = [
            LocationName.cave1_ne_grubs,
            LocationName.cave1_w_by_water_2,
            LocationName.cave1_m
        ]
        location_table = keep_one_location(location_table, c1_keystone_locations,
                                           random_locations[LocationName.rloc_c1_keystone])
        random_locations[LocationName.rloc_c1_portal] = random.randrange(3)
        if random_locations[LocationName.rloc_c1_portal] == 0:
            remove_location(LocationName.cave1_n_bridges_5, ItemName.chest_wood)
        random_locations[LocationName.rloc_c1_hidden_room] = random.randrange(4)
        if random_locations[LocationName.rloc_c1_hidden_room] >= 2:
            remove_location(LocationName.cave1_ne_hidden_room_1, ItemName.chest_wood)
            remove_location(LocationName.cave1_ne_hidden_room_2, ItemName.chest_wood)
            remove_location(LocationName.cave1_ne_hidden_room_3, ItemName.stat_upgrade)
            remove_location(LocationName.cave1_ne_hidden_room_4, ItemName.vendor_coin)
            remove_location(LocationName.cave1_ne_hidden_room_5, ItemName.chest_wood)
            remove_secret(LocationName.cave1_secret_n_hidden_room)
        # Passage
        random_locations[LocationName.rloc_passage_entrance] = random.randrange(2)
        if random_locations[LocationName.rloc_passage_entrance] == 0:
            remove_secret(LocationName.p_ent2_secret)
        random_locations[LocationName.rloc_passage_middle] = random.randrange(5)
        mid_locations_to_remove: typing.List[str] = [
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
        temple_item_counts[ItemName.ankh] -= 2
        temple_item_counts[ItemName.apple] -= 2
        temple_item_counts[ItemName.mana_2] -= 1
        temple_item_counts[ItemName.mana_1] -= 3
        temple_item_counts[ItemName.orange] -= 1
        temple_item_counts[ItemName.stat_upgrade] -= 2
        temple_item_counts[ItemName.chest_wood] -= 3
        if random_locations[LocationName.rloc_passage_middle] == 0:
            mid_locations_to_remove.remove(LocationName.p_mid1_1)
            mid_locations_to_remove.remove(LocationName.p_mid1_2)
            temple_item_counts[ItemName.chest_wood] += 2
        elif random_locations[LocationName.rloc_passage_middle] == 1:
            mid_locations_to_remove.remove(LocationName.p_mid2_1)
            mid_locations_to_remove.remove(LocationName.p_mid2_2)
            mid_locations_to_remove.remove(LocationName.p_mid2_3)
            mid_locations_to_remove.remove(LocationName.p_mid2_4)
            temple_item_counts[ItemName.mana_2] += 1
            temple_item_counts[ItemName.mana_1] += 3
        elif random_locations[LocationName.rloc_passage_middle] == 2:
            mid_locations_to_remove.remove(LocationName.p_mid3_secret_1)
            mid_locations_to_remove.remove(LocationName.p_mid3_secret_2)
            mid_locations_to_remove.remove(LocationName.p_mid3_secret_3)
            mid_locations_to_remove.remove(LocationName.p_mid3_secret_4)
        elif random_locations[LocationName.rloc_passage_middle] == 3:
            mid_locations_to_remove.remove(LocationName.p_mid4_1)
            mid_locations_to_remove.remove(LocationName.p_mid4_2)
            mid_locations_to_remove.remove(LocationName.p_mid4_3)
            mid_locations_to_remove.remove(LocationName.p_mid4_4)
            temple_item_counts[ItemName.ankh] += 1
            temple_item_counts[ItemName.orange] += 1
            temple_item_counts[ItemName.apple] += 2
        else:
            mid_locations_to_remove.remove(LocationName.p_mid5_1)
            mid_locations_to_remove.remove(LocationName.p_mid5_2)
            temple_item_counts[ItemName.chest_wood] += 1
            temple_item_counts[ItemName.stat_upgrade] += 1
            mid_locations_to_remove.remove(LocationName.p_mid5_secret)
        for loc in mid_locations_to_remove:
            if temple_locations[loc].classification == LocationClassification.Secret:
                remove_secret(loc)
            else:
                location_table.pop(loc)
        random_locations[LocationName.rloc_passage_end] = random.randrange(3)
        random_locations[LocationName.rloc_p_alley] = random.randrange(4)
        end_locations_to_remove: typing.List[str] = [
            LocationName.p_end1_secret,
            LocationName.p_end3_1,
            LocationName.p_end3_2,
        ]
        if random_locations[LocationName.rloc_passage_end] == 0:
            end_locations_to_remove.remove(LocationName.p_end1_secret)
        elif random_locations[LocationName.rloc_passage_end] == 2\
                and random_locations[LocationName.rloc_p_alley] < 2:
            end_locations_to_remove.remove(LocationName.p_end3_1)
            end_locations_to_remove.remove(LocationName.p_end3_2)
            temple_item_counts[ItemName.ankh] += 1
            temple_item_counts[ItemName.stat_upgrade] += 1
        for loc in end_locations_to_remove:
            if temple_locations[loc].classification == LocationClassification.Secret:
                remove_secret(loc)
            else:
                location_table.pop(loc)
        # Temple level 1
        random_locations[LocationName.rloc_t1_keystone] = random.randrange(4)
        t1_keystone_locations: typing.List[str] = [
            LocationName.t1_sun_block_hall_4,
            LocationName.t1_fire_trap_by_sun_turret_3,
            LocationName.t1_ledge_after_block_trap_1,
            LocationName.t1_sw_cache_3
        ]
        location_table = keep_one_location(location_table, t1_keystone_locations,
                                           random_locations[LocationName.rloc_t1_keystone])
        if random_locations[LocationName.rloc_t1_keystone] == 2:  # Remove the diamond that would spawn there
            temple_item_counts[ItemName.diamond_small] -= 1
        random_locations[LocationName.rloc_t1_portal] = random.randrange(3)
        if random_locations[LocationName.rloc_t1_portal] == 2:
            remove_location(LocationName.t1_sun_turret_3, ItemName.chest_green)
        random_locations[LocationName.rloc_t1_silver_key_s] = random.randrange(3)
        t1_silver_key_s_locations: typing.List[str] = [
            LocationName.t1_s_bridge_1,
            LocationName.t1_above_s_bridge,
            LocationName.t1_sw_corner_room,
        ]
        location_table = keep_one_location(location_table, t1_silver_key_s_locations,
                                           random_locations[LocationName.rloc_t1_silver_key_s])
        random_locations[LocationName.rloc_t1_silver_key_n] = random.randrange(2)
        t1_silver_key_n_locations: typing.List[str] = [
            LocationName.t1_n_sunbeam_treasure_3,
            LocationName.t1_boulder_hallway_by_ice_turret_4,
        ]
        location_table = keep_one_location(location_table, t1_silver_key_n_locations,
                                           random_locations[LocationName.rloc_t1_silver_key_n])
        random_locations[LocationName.rloc_t1_silver_key_ice_turret] = random.randrange(2)
        t1_silver_key_ice_turret_locations: typing.List[str] = [
            LocationName.t1_ice_turret_1,
            LocationName.t1_ice_turret_2,
        ]
        location_table = keep_one_location(location_table, t1_silver_key_ice_turret_locations,
                                           random_locations[LocationName.rloc_t1_silver_key_ice_turret])
        random_locations[LocationName.rloc_t1_silver_key_funky] = random.randrange(2)
        if random_locations[LocationName.rloc_t1_silver_key_funky] == 0:
            location_table.pop(LocationName.t1_e_of_double_gate_room_2)
            random_locations[LocationName.rloc_t1_ore_funky] = random.randrange(2)
        else:
            random_locations[LocationName.rloc_t1_ore_funky] = -1
        if random_locations[LocationName.rloc_t1_ore_funky] != 0:
            location_table.pop(LocationName.t1_fire_trap_by_sun_turret_4)
        if random_locations[LocationName.rloc_t1_ore_funky] != 1:
            location_table.pop(LocationName.t1_mana_drain_fire_trap)
        random_locations[LocationName.rloc_t1_gold_key] = random.randrange(2)
        t1_gold_key_locations: typing.List[str] = [
            LocationName.t1_n_cache_by_ice_turret_5,
            LocationName.t1_s_cache_by_ice_turret_3,
        ]
        location_table = keep_one_location(location_table, t1_gold_key_locations,
                                           random_locations[LocationName.rloc_t1_gold_key])
        random_locations[LocationName.rloc_t1_ore_e] = random.randrange(2)
        t1_ore_e_locations: typing.List[str] = [
            LocationName.t1_sun_block_hall_3,
            LocationName.t1_e_gold_beetles,
        ]
        location_table = keep_one_location(location_table, t1_ore_e_locations,
                                           random_locations[LocationName.rloc_t1_ore_e])
        random_locations[LocationName.rloc_t1_mirror] = random.randrange(3)
        t1_mirror_locations: typing.List[str] = [
            LocationName.t1_ledge_after_block_trap_2,
            LocationName.t1_ice_block_chamber_3,
            LocationName.t1_ice_block_chamber_2
        ]
        location_table = keep_one_location(location_table, t1_mirror_locations,
                                           random_locations[LocationName.rloc_t1_mirror])
        random_locations[LocationName.rloc_t1_sw_hidden_room] = random.randrange(5)
        if random_locations[LocationName.rloc_t1_sw_hidden_room] != 1:
            remove_location(LocationName.t1_sw_hidden_room_1, ItemName.vendor_coin)
            remove_location(LocationName.t1_sw_hidden_room_2, ItemName.stat_upgrade)
            remove_location(LocationName.t1_sw_hidden_room_3, ItemName.ankh)
            remove_location(LocationName.t1_sw_hidden_room_4, ItemName.chest_green)
        random_locations[LocationName.rloc_t1_puzzle_spawn] = random.randrange(2)
        random_locations[LocationName.rloc_t1_exit] = random.randrange(2)
    return location_table


def keep_one_location(location_table, locations, index):
    locations.pop(index)
    for loc in locations:
        location_table.pop(loc)
    return location_table


lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in all_locations.items() if
                                            data.code}
