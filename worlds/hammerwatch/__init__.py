import typing

from .names import item_name, castle_region_names, castle_location_names, temple_region_names, temple_location_names,\
    entrance_names, option_names
from .items import HammerwatchItem, item_table, key_table, filler_items, castle_item_counts, temple_item_counts
from .locations import LocationData, all_locations, setup_locations
from .regions import create_regions, HWEntrance, HWExitData
from .rules import set_rules
from .util import Campaign, get_option, get_campaign, get_active_key_names
from .options import hammerwatch_options

from BaseClasses import Item, Tutorial, ItemClassification, CollectionState
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

    hw_client_version = "1.0"
    data_version = 5

    web = HammerwatchWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    item_name_groups = item_name.item_groups

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
        slot_data["portal_accessibility"] = 0  # For backwards compatibility, we removed this option
        return slot_data

    def generate_early(self):
        self.campaign = get_campaign(self.multiworld, self.player)

        # Door type randomization
        if self.campaign == Campaign.Castle:
            item_counts = castle_item_counts
        else:
            item_counts = temple_item_counts
        self.door_counts = {}
        for key in get_active_key_names(self.multiworld, self.player):
            if key in item_counts.keys():
                self.door_counts[key] = item_counts[key]
        self.active_location_list, self.item_counts, self.random_locations =\
            setup_locations(self.multiworld, self.campaign, self.player)

    def generate_basic(self) -> None:
        # Shop shuffle
        self.shop_locations = {}
        if get_option(self.multiworld, self.player, option_names.shop_shuffle):
            if self.campaign == Campaign.Castle:
                shop_counts = {
                    "Combo": [1, 2, 2, 3, 4, 4, 5],
                    "Offense": [1, 1, 2, 3, 3, 4, 5],
                    "Defense": [1, 2, 3, 4, 5],
                    "Vitality": [1, 2, 3, 4, 4, 5],
                    "Powerup": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                }
                self.shop_locations = {
                    castle_location_names.shop_p1_combo: "",
                    castle_location_names.shop_p1_misc: "",
                    castle_location_names.shop_p2_off: "",
                    castle_location_names.shop_p2_combo: "",
                    castle_location_names.shop_p3_power: "",
                    castle_location_names.shop_p3_off: "",
                    castle_location_names.shop_p3_def: "",
                    castle_location_names.shop_p3_combo: "",
                    castle_location_names.shop_p3_misc: "",
                    castle_location_names.shop_b1_power: "",
                    castle_location_names.shop_a1_power: "",
                    castle_location_names.shop_a1_combo: "",
                    castle_location_names.shop_a1_misc: "",
                    castle_location_names.shop_a1_off: "",
                    castle_location_names.shop_a1_def: "",
                    castle_location_names.shop_a3_power: "",
                    castle_location_names.shop_b2_power: "",
                    castle_location_names.shop_r1_power: "",
                    castle_location_names.shop_r1_misc: "",
                    castle_location_names.shop_r2_combo: "",
                    castle_location_names.shop_r2_off: "",
                    castle_location_names.shop_r3_misc: "",
                    castle_location_names.shop_r3_def: "",
                    castle_location_names.shop_r3_power: "",
                    castle_location_names.shop_r3_off: "",
                    castle_location_names.shop_r3_combo: "",
                    castle_location_names.shop_b3_power: "",
                    castle_location_names.shop_c1_power: "",
                    castle_location_names.shop_c2_power: "",
                    castle_location_names.shop_c2_combo: "",
                    castle_location_names.shop_c2_off: "",
                    castle_location_names.shop_c2_def: "",
                    castle_location_names.shop_c2_misc: "",
                    castle_location_names.shop_c3_power: "",
                    castle_location_names.shop_c2_off_2: "",
                    castle_location_names.shop_c2_def_2: "",
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
                    temple_location_names.shop_combo: "",
                    temple_location_names.shop_misc: "",
                    temple_location_names.shop_off: "",
                    temple_location_names.shop_def: "",
                }
                remaining_shops = []
                for shop_type in shop_counts.keys():
                    for s in range(shop_counts[shop_type]):
                        remaining_shops.append(shop_type)

                for loc in self.shop_locations.keys():
                    self.shop_locations[loc] = self.random.choice(remaining_shops)
                    remaining_shops.remove(self.shop_locations[loc])

        # Shop cost setting validation, swap if max is higher than min
        cost_max = get_option(self.multiworld, self.player, option_names.shop_cost_max)
        cost_min = get_option(self.multiworld, self.player, option_names.shop_cost_min)
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
        itempool: typing.List[Item] = []

        # First create and place our locked items so we know how many are left over
        self.multiworld.get_location(temple_location_names.ev_victory, self.player) \
            .place_locked_item(self.create_event(item_name.ev_victory))
        if self.campaign == Campaign.Castle:
            self.place_castle_locked_items()
        else:
            self.place_tots_locked_items()

        # More efficient and foolproof method to get number of required locations
        total_required_locations = len([loc for loc in self.multiworld.get_locations(self.player) if not loc.item])

        # Remove progression items if the player starts with them
        for precollected in self.multiworld.precollected_items[self.player]:
            if precollected.classification & ItemClassification.progression:
                if precollected.name in self.item_counts and self.item_counts[precollected.name] > 0:
                    self.item_counts[precollected.name] -= 1

        # Add items
        items = 0
        present_filler_items = []
        for item in self.item_counts:
            items += self.item_counts[item]
            # item_names_to_create += [item] * self.item_counts[item]
            if item_table[item].classification == ItemClassification.filler and self.item_counts[item] > 0:
                present_filler_items.append(item)

        # Add/remove junk items depending if we have not enough/too many locations
        junk: int = total_required_locations - items
        if junk > 0:
            for name in self.random.choices(present_filler_items, k=junk):
                self.item_counts[name] += 1
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

    def collect(self, state: CollectionState, item: Item) -> bool:
        prog = super(HammerwatchWorld, self).collect(state, item)
        spaces = item.name.count(" ")
        if item.name.endswith("Key") and spaces > 1:
            add_name = key_table[item.name][0]
            count = key_table[item.name][1]
            state.prog_items[add_name, self.player] += count
            if item.name.startswith("Big") and spaces == 3:
                state.prog_items[key_table[add_name][0], self.player] += count * key_table[add_name][1]
        return prog

    def remove(self, state: CollectionState, item: Item) -> bool:
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
            castle_location_names.btn_p1_floor: item_name.btnc_p1_floor,
            castle_location_names.ev_p2_gold_gate_room_ne_switch: item_name.ev_castle_p2_switch,
            castle_location_names.ev_p2_gold_gate_room_nw_switch: item_name.ev_castle_p2_switch,
            castle_location_names.ev_p2_gold_gate_room_se_switch: item_name.ev_castle_p2_switch,
            castle_location_names.ev_p2_gold_gate_room_sw_switch: item_name.ev_castle_p2_switch,
            castle_location_names.btnc_p3_sw: item_name.btnc_p3_e_passage,
            castle_location_names.btnc_p3_arrow_hall_wall: item_name.btnc_p3_s_passage,
            castle_location_names.btnc_n2_blue_spikes: item_name.btnc_a2_blue_spikes,
            castle_location_names.btnc_a2_bspikes_tp: item_name.btnc_a2_bspikes_tp,
            castle_location_names.btnc_c2_n_open_wall: item_name.btnc_c2_n_wall,
            castle_location_names.ev_c2_n_shops_switch: item_name.ev_castle_c2_n_shops_switch,
            castle_location_names.ev_c3_rspikes_switch: item_name.ev_castle_c3_rspikes_switch,
            castle_location_names.ev_c3_sw_hidden_switch_1: item_name.ev_castle_c3_sw_hidden_switch,
            castle_location_names.ev_c3_sw_hidden_switch_2: item_name.ev_castle_c3_sw_hidden_switch,
            castle_location_names.ev_c3_sw_hidden_switch_3: item_name.ev_castle_c3_sw_hidden_switch,
            castle_location_names.ev_c3_sw_hidden_switch_4: item_name.ev_castle_c3_sw_hidden_switch,
            castle_location_names.ev_c3_sw_hidden_switch_5: item_name.ev_castle_c3_sw_hidden_switch,
            castle_location_names.ev_c3_sw_hidden_switch_6: item_name.ev_castle_c3_sw_hidden_switch,

            castle_location_names.ev_p1_boss_switch: item_name.ev_castle_b1_boss_switch,
            castle_location_names.ev_p2_boss_switch: item_name.ev_castle_b1_boss_switch,
            castle_location_names.ev_p3_boss_switch: item_name.ev_castle_b1_boss_switch,
            castle_location_names.ev_a1_boss_switch: item_name.ev_castle_b2_boss_switch,
            castle_location_names.ev_a2_boss_switch: item_name.ev_castle_b2_boss_switch,
            castle_location_names.ev_a3_boss_switch: item_name.ev_castle_b2_boss_switch,
            castle_location_names.ev_r1_boss_switch: item_name.ev_castle_b3_boss_switch,
            castle_location_names.ev_r2_boss_switch: item_name.ev_castle_b3_boss_switch,
            castle_location_names.ev_r3_boss_switch: item_name.ev_castle_b3_boss_switch,
            castle_location_names.ev_c1_boss_switch: item_name.ev_castle_b4_boss_switch,
            castle_location_names.ev_c2_boss_switch: item_name.ev_castle_b4_boss_switch,
            castle_location_names.ev_c3_boss_switch: item_name.ev_castle_b4_boss_switch,

            castle_location_names.ev_beat_boss_1: item_name.evc_beat_boss_1,
            castle_location_names.ev_beat_boss_2: item_name.evc_beat_boss_2,
            castle_location_names.ev_beat_boss_3: item_name.evc_beat_boss_3,
            castle_location_names.ev_beat_boss_4: item_name.evc_beat_boss_4,
        }

        # Bonus Key Locations
        if not get_option(self.multiworld, self.player, option_names.randomize_bonus_keys):
            castle_bonus_keys = [
                castle_location_names.n1_room1,
                castle_location_names.n1_room3_sealed_room_1,
                castle_location_names.n1_room2_small_box,
                castle_location_names.n1_entrance,
                castle_location_names.n1_room4_m,
                castle_location_names.n2_m_n,
                castle_location_names.n2_m_m_3,
                castle_location_names.n2_ne_4,
                castle_location_names.n2_m_e,
                castle_location_names.n2_start_1,
                castle_location_names.n2_m_se_5,
                castle_location_names.n3_exit_sw,
                castle_location_names.n3_m_cluster_5,
                castle_location_names.n3_se_cluster_5,
                castle_location_names.n4_ne,
                castle_location_names.n4_by_w_room_1,
                castle_location_names.n4_by_w_room_2,
                castle_location_names.n4_by_exit,
            ]
            for loc in castle_bonus_keys:
                self.multiworld.get_location(loc, self.player).place_locked_item(self.create_item(item_name.key_bonus))

        for loc, itm in castle_locked_items.items():
            self.multiworld.get_location(loc, self.player).place_locked_item(self.create_event(itm))

    def place_tots_locked_items(self):
        temple_locked_items = {
            temple_location_names.ev_c1_portal: item_name.ev_c1_portal,
            temple_location_names.ev_c2_portal: item_name.ev_c2_portal,
            temple_location_names.ev_c3_portal: item_name.ev_c3_portal,
            temple_location_names.ev_t1_portal: item_name.ev_t1_portal,
            temple_location_names.ev_t2_portal: item_name.ev_t2_portal,
            temple_location_names.ev_t3_portal: item_name.ev_t3_portal,
            temple_location_names.ev_temple_entrance_rock: item_name.ev_open_temple_entrance_shortcut,
            temple_location_names.ev_t1_n_node_n_mirrors: item_name.evt_t1_n_mirrors,
            temple_location_names.ev_t1_n_node_s_mirror: item_name.evt_t1_s_mirror,
            temple_location_names.ev_hub_pof_switch: item_name.ev_pof_switch,
            temple_location_names.ev_cave1_pof_switch: item_name.ev_pof_switch,
            temple_location_names.ev_cave2_pof_switch: item_name.ev_pof_switch,
            temple_location_names.ev_cave3_pof_switch: item_name.ev_pof_switch,
            temple_location_names.ev_temple1_pof_switch: item_name.ev_pof_switch,
            temple_location_names.ev_temple2_pof_switch: item_name.ev_pof_switch,
            temple_location_names.ev_pof_1_se_room_panel: item_name.ev_pof_1_s_walls,
            temple_location_names.ev_pof_1_unlock_exit: item_name.ev_pof_1_unlock_exit,
            temple_location_names.ev_pof_2_unlock_exit: item_name.ev_pof_2_unlock_exit,
            temple_location_names.ev_pof_end: item_name.ev_pof_complete,
            temple_location_names.btn_t2_floor_blue: item_name.btn_t2_blue_spikes,
            temple_location_names.btn_t2_rune_n: item_name.ev_t2_rune_switch,
            temple_location_names.btn_t2_rune_w: item_name.ev_t2_rune_switch,
            temple_location_names.btn_t2_rune_e: item_name.ev_t2_rune_switch,
            temple_location_names.btn_t2_rune_se: item_name.ev_t2_rune_switch,
            temple_location_names.btn_t2_rune_sw: item_name.ev_t2_rune_switch,
            temple_location_names.ev_t1_n_node: item_name.ev_solar_node,
            temple_location_names.ev_t1_s_node: item_name.ev_solar_node,
            temple_location_names.ev_t2_n_node: item_name.ev_solar_node,
            temple_location_names.ev_t2_s_node: item_name.ev_solar_node,
            temple_location_names.ev_t3_n_node: item_name.ev_solar_node,
            temple_location_names.ev_t3_s_node: item_name.ev_solar_node,
            temple_location_names.ev_beat_boss_1: item_name.evt_beat_boss_1,
            temple_location_names.ev_beat_boss_2: item_name.evt_beat_boss_2,
            temple_location_names.ev_beat_boss_3: item_name.evt_beat_boss_3,
        }

        # Pyramid of Fear Bonus Keys
        if not get_option(self.multiworld, self.player, option_names.randomize_bonus_keys):
            temple_bonus_keys = [
                temple_location_names.pof_1_n_5,
                temple_location_names.pof_1_ent_5,
            ]
            for loc in temple_bonus_keys:
                self.multiworld.get_location(loc, self.player).place_locked_item(self.create_item(item_name.key_bonus))

        for loc, itm in temple_locked_items.items():
            self.multiworld.get_location(loc, self.player).place_locked_item(self.create_event(itm))

    def set_rules(self) -> None:
        self.exit_swaps = {}
        self.exit_spoiler_info = []
        set_rules(self.multiworld, self.player, self.door_counts)

    def write_spoiler(self, spoiler_handle) -> None:
        if get_option(self.multiworld, self.player, option_names.shop_shuffle):
            spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Shop Shuffle Locations:\n")
            for loc, shop in self.shop_locations.items():
                spoiler_handle.write(f"\n{loc}: {shop}")
        if get_option(self.multiworld, self.player, option_names.exit_randomization):
            spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Exit Randomization Connections:\n")
            for entry in self.exit_spoiler_info:
                spoiler_handle.write(f"\n{entry}")

    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        pass
