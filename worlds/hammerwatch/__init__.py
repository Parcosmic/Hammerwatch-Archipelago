from typing import Dict

from .Items import *
from .Locations import *
from .Regions import create_regions, HWEntrance, HWExitData
from .Rules import set_rules
from .Util import *

from .Names import TempleLocationNames, TempleRegionNames, EntranceNames

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from .Options import *
from ..AutoWorld import World, WebWorld


class HammerwatchWeb(WebWorld):
    theme = "stone"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Hammerwatch randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Parcosmic"]
    )]


class HammerwatchWorld(World):
    """
    Hammerwatch is a hack and slash action adventure.
    Play as a hero that is one of seven classes as you fight your way through Castle Hammerwatch to defeat the dragon
    or the Temple of the Sun to stop the evil Sun Guardian Sha'Rand.
    """
    game: str = "Hammerwatch"
    option_definitions = hammerwatch_options
    topology_present: bool = True
    remote_start_inventory: bool = True

    hw_client_version = "0.9"
    data_version = 5

    web = HammerwatchWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    item_name_groups = ItemName.item_groups

    campaign: Campaign
    active_location_list: typing.Dict[str, LocationData]
    item_counts: typing.Dict[str, int]
    random_locations: typing.Dict[str, int]
    shop_locations: typing.Dict[str, str]
    door_counts: typing.Dict[str, int]
    gate_types: typing.Dict[str, str]
    level_exits: typing.List[HWEntrance]
    exit_swaps: typing.Dict[str, str]
    exit_spoiler_info: typing.List[str]
    start_exit: str

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        slot_data: typing.Dict[str, object] = {}
        for option_name in self.option_definitions:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value
        for loc, value in self.random_locations.items():
            slot_data[loc] = value
        for loc, value in self.shop_locations.items():
            slot_data[loc] = value
        slot_data["Hammerwatch Mod Version"] = self.hw_client_version
        slot_data["Gate Types"] = self.gate_types
        slot_data["Exit Swaps"] = self.exit_swaps
        slot_data["Start Exit"] = self.start_exit
        return slot_data

    def generate_early(self):
        self.campaign = get_campaign(self.multiworld, self.player)

        # Door type randomization
        if self.campaign == Campaign.Castle:
            item_counts = Items.castle_item_counts
        else:
            item_counts = Items.temple_item_counts
        self.door_counts = {}
        for key in get_active_key_names(self.multiworld, self.player):
            if key in item_counts.keys():
                self.door_counts[key] = item_counts[key]
        self.active_location_list, self.item_counts, self.random_locations =\
            setup_locations(self.multiworld, self.campaign, self.player)

    def generate_basic(self) -> None:

        # Shop shuffle
        self.shop_locations = {}
        if get_option(self.multiworld, self.player, OptionNames.shop_shuffle):
            if self.campaign == Campaign.Castle:
                shop_counts = {
                    "Combo": [1, 2, 2, 3, 4, 4, 5],
                    "Offense": [1, 1, 2, 3, 3, 4, 5],
                    "Defense": [1, 2, 3, 4, 5],
                    "Vitality": [1, 2, 3, 4, 4, 5],
                    "Powerup": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                }
                self.shop_locations = {
                    CastleLocationNames.shop_p1_combo: "",
                    CastleLocationNames.shop_p1_misc: "",
                    CastleLocationNames.shop_p2_off: "",
                    CastleLocationNames.shop_p2_combo: "",
                    CastleLocationNames.shop_p3_power: "",
                    CastleLocationNames.shop_p3_off: "",
                    CastleLocationNames.shop_p3_def: "",
                    CastleLocationNames.shop_p3_combo: "",
                    CastleLocationNames.shop_p3_misc: "",
                    CastleLocationNames.shop_b1_power: "",
                    CastleLocationNames.shop_a1_power: "",
                    CastleLocationNames.shop_a1_combo: "",
                    CastleLocationNames.shop_a1_misc: "",
                    CastleLocationNames.shop_a1_off: "",
                    CastleLocationNames.shop_a1_def: "",
                    CastleLocationNames.shop_a3_power: "",
                    CastleLocationNames.shop_b2_power: "",
                    CastleLocationNames.shop_r1_power: "",
                    CastleLocationNames.shop_r1_misc: "",
                    CastleLocationNames.shop_r2_combo: "",
                    CastleLocationNames.shop_r2_off: "",
                    CastleLocationNames.shop_r3_misc: "",
                    CastleLocationNames.shop_r3_def: "",
                    CastleLocationNames.shop_r3_power: "",
                    CastleLocationNames.shop_r3_off: "",
                    CastleLocationNames.shop_r3_combo: "",
                    CastleLocationNames.shop_b3_power: "",
                    CastleLocationNames.shop_c1_power: "",
                    CastleLocationNames.shop_c2_power: "",
                    CastleLocationNames.shop_c2_combo: "",
                    CastleLocationNames.shop_c2_off: "",
                    CastleLocationNames.shop_c2_def: "",
                    CastleLocationNames.shop_c2_misc: "",
                    CastleLocationNames.shop_c3_power: "",
                    CastleLocationNames.shop_c2_off_2: "",
                    CastleLocationNames.shop_c2_def_2: "",
                }

                for loc in self.shop_locations.keys():
                    shop_type = self.random.choice(list(shop_counts.keys()))
                    tier = shop_counts[shop_type].pop(0)
                    if len(shop_counts[shop_type]) == 0:
                        shop_counts.pop(shop_type)
                    if tier > 0:
                        self.shop_locations[loc] = f"{shop_type} Level {tier}"
                    else:
                        self.shop_locations[loc] = f"{shop_type}"
            else:
                shop_counts = {
                    "Combo": 1,
                    "Offense": 1,
                    "Defense": 1,
                    "Vitality": 1,
                }
                self.shop_locations = {
                    TempleLocationNames.shop_combo: "",
                    TempleLocationNames.shop_misc: "",
                    TempleLocationNames.shop_off: "",
                    TempleLocationNames.shop_def: "",
                }
                remaining_shops = []
                for shop_type in shop_counts.keys():
                    for s in range(shop_counts[shop_type]):
                        remaining_shops.append(shop_type)

                for loc in self.shop_locations.keys():
                    self.shop_locations[loc] = self.random.choice(remaining_shops)
                    remaining_shops.remove(self.shop_locations[loc])

        # Shop cost setting validation, swap if max is higher than min
        cost_max = get_option(self.multiworld, self.player, OptionNames.shop_cost_max)
        cost_min = get_option(self.multiworld, self.player, OptionNames.shop_cost_min)
        if cost_max < cost_min:
            swap = self.multiworld.shop_cost_max[self.player]
            self.multiworld.shop_cost_max[self.player] = self.multiworld.shop_cost_min[self.player]
            self.multiworld.shop_cost_min[self.player] = swap

    def create_regions(self) -> None:
        self.level_exits = []
        self.gate_types = create_regions(self.multiworld, self.campaign, self.player, self.active_location_list,
                                         self.random_locations)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return HammerwatchItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str):
        return HammerwatchItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        item_names: typing.List[str] = []
        itempool: typing.List[Item] = []

        self.multiworld.get_location(TempleLocationNames.ev_victory, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_victory))

        if self.campaign == Campaign.Castle:
            self.place_castle_locked_items()
        else:
            self.place_tots_locked_items()

        # More efficient and foolproof method to get number of required locations
        total_available_locations = [loc for loc in self.multiworld.get_locations(self.player) if not loc.item]
        total_required_locations = len(total_available_locations)

        # Remove items if the player starts with them
        for precollected in self.multiworld.precollected_items[self.player]:
            if precollected.name in self.item_counts:
                if self.item_counts[precollected.name] <= 1:
                    self.item_counts.pop(precollected.name)
                else:
                    self.item_counts[precollected.name] -= 1

        # Add items
        items = 0
        present_filler_items = []
        for item in self.item_counts:
            items += self.item_counts[item]
            item_names += [item] * self.item_counts[item]
            if item_table[item].classification == ItemClassification.filler and self.item_counts[item] > 0:
                present_filler_items.append(item)

        # Add/remove junk items depending if we have not enough/too many locations
        junk: int = total_required_locations - items
        if junk > 0:
            for item_name in self.random.choices(present_filler_items, k=junk):
                self.item_counts[item_name] += 1
        else:
            for j in range(-junk):
                junk_item = self.random.choice(present_filler_items)
                self.item_counts[junk_item] -= 1
                if self.item_counts[junk_item] == 0:
                    present_filler_items.remove(junk_item)

        # Create items and add to item pool
        for item in self.item_counts:
            for i in range(self.item_counts[item]):
                itempool.append(self.create_item(item))

        self.multiworld.itempool += itempool

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        prog = super(HammerwatchWorld, self).collect(state, item)
        spaces = item.name.count(" ")
        if item.name.endswith("Key") and spaces > 1:
            add_name = key_table[item.name][0]
            count = key_table[item.name][1]
            state.prog_items[add_name, self.player] += count
            if item.name.startswith("Big") and spaces == 3:
                state.prog_items[key_table[add_name][0], self.player] += count * key_table[add_name][1]
        return prog

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        prog = super(HammerwatchWorld, self).remove(state, item)
        spaces = item.name.count(" ")
        if item.name.endswith("Key") and spaces > 1:
            add_name = key_table[item.name][0]
            count = key_table[item.name][1]
            state.prog_items[add_name, self.player] -= count
            if item.name.startswith("Big") and spaces == 3:
                state.prog_items[key_table[add_name][0], self.player] -= count * key_table[add_name][1]
        return prog

    def get_filler_item_name(self) -> str:
        return self.random.choice(tuple(filler_items))

    def place_castle_locked_items(self):
        castle_locked_items = {
            CastleLocationNames.btn_p1_floor: ItemName.btnc_p1_floor,
            CastleLocationNames.ev_p2_gold_gate_room_ne_switch: ItemName.ev_castle_p2_switch,
            CastleLocationNames.ev_p2_gold_gate_room_nw_switch: ItemName.ev_castle_p2_switch,
            CastleLocationNames.ev_p2_gold_gate_room_se_switch: ItemName.ev_castle_p2_switch,
            CastleLocationNames.ev_p2_gold_gate_room_sw_switch: ItemName.ev_castle_p2_switch,
            CastleLocationNames.btnc_p3_sw: ItemName.btnc_p3_e_passage,
            CastleLocationNames.btnc_p3_arrow_hall_wall: ItemName.btnc_p3_s_passage,
            CastleLocationNames.btnc_n2_blue_spikes: ItemName.btnc_a2_blue_spikes,
            CastleLocationNames.btnc_a2_bspikes_tp: ItemName.btnc_a2_bspikes_tp,
            CastleLocationNames.btnc_c2_n_open_wall: ItemName.btnc_c2_n_wall,
            CastleLocationNames.ev_c2_n_shops_switch: ItemName.ev_castle_c2_n_shops_switch,
            CastleLocationNames.ev_c3_rspikes_switch: ItemName.ev_castle_c3_rspikes_switch,
            CastleLocationNames.ev_c3_sw_hidden_switch_1: ItemName.ev_castle_c3_sw_hidden_switch,
            CastleLocationNames.ev_c3_sw_hidden_switch_2: ItemName.ev_castle_c3_sw_hidden_switch,
            CastleLocationNames.ev_c3_sw_hidden_switch_3: ItemName.ev_castle_c3_sw_hidden_switch,
            CastleLocationNames.ev_c3_sw_hidden_switch_4: ItemName.ev_castle_c3_sw_hidden_switch,
            CastleLocationNames.ev_c3_sw_hidden_switch_5: ItemName.ev_castle_c3_sw_hidden_switch,
            CastleLocationNames.ev_c3_sw_hidden_switch_6: ItemName.ev_castle_c3_sw_hidden_switch,

            CastleLocationNames.ev_p1_boss_switch: ItemName.ev_castle_b1_boss_switch,
            CastleLocationNames.ev_p2_boss_switch: ItemName.ev_castle_b1_boss_switch,
            CastleLocationNames.ev_p3_boss_switch: ItemName.ev_castle_b1_boss_switch,
            CastleLocationNames.ev_a1_boss_switch: ItemName.ev_castle_b2_boss_switch,
            CastleLocationNames.ev_a2_boss_switch: ItemName.ev_castle_b2_boss_switch,
            CastleLocationNames.ev_a3_boss_switch: ItemName.ev_castle_b2_boss_switch,
            CastleLocationNames.ev_r1_boss_switch: ItemName.ev_castle_b3_boss_switch,
            CastleLocationNames.ev_r2_boss_switch: ItemName.ev_castle_b3_boss_switch,
            CastleLocationNames.ev_r3_boss_switch: ItemName.ev_castle_b3_boss_switch,
            CastleLocationNames.ev_c1_boss_switch: ItemName.ev_castle_b4_boss_switch,
            CastleLocationNames.ev_c2_boss_switch: ItemName.ev_castle_b4_boss_switch,
            CastleLocationNames.ev_c3_boss_switch: ItemName.ev_castle_b4_boss_switch,

            CastleLocationNames.ev_beat_boss_1: ItemName.evc_beat_boss_1,
            CastleLocationNames.ev_beat_boss_2: ItemName.evc_beat_boss_2,
            CastleLocationNames.ev_beat_boss_3: ItemName.evc_beat_boss_3,
            CastleLocationNames.ev_beat_boss_4: ItemName.evc_beat_boss_4,
        }

        # Bonus Key Locations
        if not get_option(self.multiworld, self.player, OptionNames.randomize_bonus_keys):
            castle_locked_items.update({
                CastleLocationNames.n1_room1: ItemName.key_bonus,
                CastleLocationNames.n1_room3_sealed_room_1: ItemName.key_bonus,
                CastleLocationNames.n1_room2_small_box: ItemName.key_bonus,
                CastleLocationNames.n1_entrance: ItemName.key_bonus,
                CastleLocationNames.n1_room4_m: ItemName.key_bonus,
                CastleLocationNames.n2_m_n: ItemName.key_bonus,
                CastleLocationNames.n2_m_m_3: ItemName.key_bonus,
                CastleLocationNames.n2_ne_4: ItemName.key_bonus,
                CastleLocationNames.n2_m_e: ItemName.key_bonus,
                CastleLocationNames.n2_start_1: ItemName.key_bonus,
                CastleLocationNames.n2_m_se_5: ItemName.key_bonus,
                CastleLocationNames.n3_exit_sw: ItemName.key_bonus,
                CastleLocationNames.n3_m_cluster_5: ItemName.key_bonus,
                CastleLocationNames.n3_se_cluster_5: ItemName.key_bonus,
                CastleLocationNames.n4_ne: ItemName.key_bonus,
                CastleLocationNames.n4_by_w_room_1: ItemName.key_bonus,
                CastleLocationNames.n4_by_w_room_2: ItemName.key_bonus,
                CastleLocationNames.n4_by_exit: ItemName.key_bonus,
            })

        for loc, itm in castle_locked_items.items():
            self.multiworld.get_location(loc, self.player).place_locked_item(self.create_event(itm))

    def place_tots_locked_items(self):
        temple_locked_items = {
            TempleLocationNames.ev_c1_portal: ItemName.ev_c1_portal,
            TempleLocationNames.ev_c2_portal: ItemName.ev_c2_portal,
            TempleLocationNames.ev_c3_portal: ItemName.ev_c3_portal,
            TempleLocationNames.ev_t1_portal: ItemName.ev_t1_portal,
            TempleLocationNames.ev_t2_portal: ItemName.ev_t2_portal,
            TempleLocationNames.ev_t3_portal: ItemName.ev_t3_portal,
            TempleLocationNames.ev_temple_entrance_rock: ItemName.ev_open_temple_entrance_shortcut,
            TempleLocationNames.ev_t1_n_node_n_mirrors: ItemName.evt_t1_n_mirrors,
            TempleLocationNames.ev_t1_n_node_s_mirror: ItemName.evt_t1_s_mirror,
            TempleLocationNames.ev_hub_pof_switch: ItemName.ev_pof_switch,
            TempleLocationNames.ev_cave1_pof_switch: ItemName.ev_pof_switch,
            TempleLocationNames.ev_cave2_pof_switch: ItemName.ev_pof_switch,
            TempleLocationNames.ev_cave3_pof_switch: ItemName.ev_pof_switch,
            TempleLocationNames.ev_temple1_pof_switch: ItemName.ev_pof_switch,
            TempleLocationNames.ev_temple2_pof_switch: ItemName.ev_pof_switch,
            TempleLocationNames.ev_pof_1_se_room_panel: ItemName.ev_pof_1_s_walls,
            TempleLocationNames.ev_pof_1_unlock_exit: ItemName.ev_pof_1_unlock_exit,
            TempleLocationNames.ev_pof_2_unlock_exit: ItemName.ev_pof_2_unlock_exit,
            TempleLocationNames.ev_pof_end: ItemName.ev_pof_complete,
            TempleLocationNames.btn_t2_floor_blue: ItemName.btn_t2_blue_spikes,
            TempleLocationNames.btn_t2_rune_n: ItemName.ev_t2_rune_switch,
            TempleLocationNames.btn_t2_rune_w: ItemName.ev_t2_rune_switch,
            TempleLocationNames.btn_t2_rune_e: ItemName.ev_t2_rune_switch,
            TempleLocationNames.btn_t2_rune_se: ItemName.ev_t2_rune_switch,
            TempleLocationNames.btn_t2_rune_sw: ItemName.ev_t2_rune_switch,
            TempleLocationNames.ev_t1_n_node: ItemName.ev_solar_node,
            TempleLocationNames.ev_t1_s_node: ItemName.ev_solar_node,
            TempleLocationNames.ev_t2_n_node: ItemName.ev_solar_node,
            TempleLocationNames.ev_t2_s_node: ItemName.ev_solar_node,
            TempleLocationNames.ev_t3_n_node: ItemName.ev_solar_node,
            TempleLocationNames.ev_t3_s_node: ItemName.ev_solar_node,
            TempleLocationNames.ev_beat_boss_1: ItemName.evt_beat_boss_1,
            TempleLocationNames.ev_beat_boss_2: ItemName.evt_beat_boss_2,
            TempleLocationNames.ev_beat_boss_3: ItemName.evt_beat_boss_3,
        }

        # Pyramid of Fear Bonus Keys
        if not get_option(self.multiworld, self.player, OptionNames.randomize_bonus_keys):
            temple_locked_items.update({
                TempleLocationNames.pof_1_n_5: ItemName.key_bonus,
                TempleLocationNames.pof_1_ent_5: ItemName.key_bonus,
            })

        # Portal Accessibility rune keys
        if get_option(self.multiworld, self.player, OptionNames.portal_accessibility):
            rune_key_locs: typing.List[str] = []

            def get_region_item_locs(region: str):
                return [loc.name for loc in self.multiworld.get_region(region, self.player).locations if not loc.event]

            # Cave Level 3 Rune Key
            c3_locs = get_region_item_locs(TempleRegionNames.c3_e)
            # If playing exit rando we need to ensure we can always return if falling from the temple
            if not get_option(self.multiworld, self.player, OptionNames.exit_randomization):
                c3_locs.extend(get_region_item_locs(TempleRegionNames.cave_3_main))
            rune_key_locs.append(self.random.choice(c3_locs))

            # Cave Level 2 Rune Key
            c2_locs = get_region_item_locs(TempleRegionNames.cave_2_main)
            rune_key_locs.append(self.random.choice(c2_locs))

            # Cave Level 1 Rune Key
            c1_locs = []
            c1_locs += get_region_item_locs(TempleRegionNames.cave_1_main)
            c1_locs += get_region_item_locs(TempleRegionNames.cave_1_blue_bridge)
            c1_locs += get_region_item_locs(TempleRegionNames.cave_1_red_bridge)
            rune_key_locs.append(self.random.choice(c1_locs))

            # Temple Floor 1 Rune Key
            t1_locs = []
            t1_locs += get_region_item_locs(TempleRegionNames.t1_main)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_sw_sdoor)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_node_1)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_node_2)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_sun_turret)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_ice_turret)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_n_of_ice_turret)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_s_of_ice_turret)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_east)
            t1_locs += get_region_item_locs(TempleRegionNames.t1_sun_block_hall)
            rune_key_locs.append(self.random.choice(t1_locs))

            # Temple Floor 2 Rune Key
            t2_locs = []
            t2_locs += get_region_item_locs(TempleRegionNames.t2_main)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_n_gate)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_s_gate)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_n_node)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_s_node)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_ornate)
            rune_key_locs.append(self.random.choice(t2_locs))

            # Temple Floor 3 Rune Key
            t3_locs = []
            t3_locs += get_region_item_locs(TempleRegionNames.t3_main)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_n_node_blocks)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_s_node_blocks_1)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_s_node_blocks_2)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_s_node)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_n_node)
            rune_key_locs.append(self.random.choice(t3_locs))

            for loc in rune_key_locs:
                self.multiworld.get_location(loc, self.player).place_locked_item(self.create_item(ItemName.key_teleport))

        for loc, itm in temple_locked_items.items():
            self.multiworld.get_location(loc, self.player).place_locked_item(self.create_event(itm))

    def set_rules(self) -> None:
        self.exit_swaps = {}
        self.exit_spoiler_info = []
        set_rules(self.multiworld, self.player, self.door_counts)

    def write_spoiler(self, spoiler_handle) -> None:
        if get_option(self.multiworld, self.player, OptionNames.shop_shuffle):
            spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Shop Shuffle Locations:\n")
            for loc, shop in self.shop_locations.items():
                spoiler_handle.write(f"\n{loc}: {shop}")
        # if self.multiworld.exit_randomization[self.player]:
        if get_option(self.multiworld, self.player, OptionNames.exit_randomization):
            spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Exit Randomization Connections:\n")
            for entry in self.exit_spoiler_info:
                spoiler_handle.write(f"\n{entry}")

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        pass
