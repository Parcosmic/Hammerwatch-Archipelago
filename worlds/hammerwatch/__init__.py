import typing

from .Items import *
from .Locations import *
from .Regions import create_regions
from .Rules import set_rules
from .Util import *

from .Names import ItemName, TempleLocationNames, TempleRegionNames

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

    hw_client_version = "1.0"
    data_version = 3

    web = HammerwatchWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    item_name_groups = ItemName.item_groups

    campaign: Campaign = Campaign.Castle
    active_location_list: typing.Dict[str, LocationData]
    item_counts: typing.Dict[str, int]
    random_locations: typing.Dict[str, int]
    shop_locations: typing.Dict[str, str]
    door_counts: typing.Dict[str, int] = {}
    gate_types: typing.Dict[str, str] = {}

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
        return slot_data

    def generate_early(self):
        self.campaign = get_campaign(self.multiworld, self.player)

        # Door type randomization
        if self.campaign == Campaign.Castle:
            item_counts = Items.castle_item_counts
        else:
            item_counts = Items.temple_item_counts
        for key in get_active_key_names(self.multiworld, self.player):
            if key in item_counts.keys():
                self.door_counts[key] = item_counts[key]
        self.active_location_list, self.item_counts, self.random_locations = setup_locations(self.multiworld, self.campaign, self.player)

    def generate_basic(self) -> None:
        self.multiworld.get_location(TempleLocationNames.ev_victory, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_victory))

        if self.campaign == Campaign.Castle:
            self.place_castle_locked_items()
        else:
            self.place_tots_locked_items()

        # Shop shuffle
        self.shop_locations = {}
        if self.multiworld.shop_shuffle[self.player] > 0:
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
                    shop_type = self.multiworld.random.choice(list(shop_counts.keys()))
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
                    self.shop_locations[loc] = self.multiworld.random.choice(remaining_shops)
                    remaining_shops.remove(self.shop_locations[loc])

        # Shop cost setting validation, swap if max is higher than min
        if self.multiworld.shop_cost_max[self.player] < self.multiworld.shop_cost_min[self.player]:
            swap = self.multiworld.shop_cost_max[self.player]
            self.multiworld.shop_cost_max[self.player] = self.multiworld.shop_cost_min[self.player]
            self.multiworld.shop_cost_min[self.player] = swap

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.campaign, self.player, self.active_location_list, self.random_locations)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return HammerwatchItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str):
        return HammerwatchItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        item_names: typing.List[str] = []
        itempool: typing.List[Item] = []

        # Get the total number of locations we need to fill
        total_required_locations = len(self.active_location_list)
        total_required_locations -= len(common_event_locations)
        if self.campaign == Campaign.Castle:
            total_required_locations -= len(castle_event_locations)
            if not self.multiworld.randomize_bonus_keys[self.player]:
                total_required_locations -= 18  # Preplaced bonus keys
        elif self.campaign == Campaign.Temple:
            total_required_locations -= len(temple_event_locations)
            if not self.multiworld.randomize_bonus_keys[self.player]:
                total_required_locations -= 2  # Preplaced bonus keys
            # If Portal Accessibility is on, we create/place the Rune Keys elsewhere
            if self.multiworld.portal_accessibility[self.player]:
                total_required_locations -= 6

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
            for item_name in self.multiworld.random.choices(present_filler_items, k=junk):
                self.item_counts[item_name] += 1
        else:
            for j in range(-junk):
                junk_item = self.multiworld.random.choice(present_filler_items)
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
        return self.multiworld.random.choice(tuple(filler_items))

    def place_castle_locked_items(self):
        # Prison 1 Switches
        self.multiworld.get_location(CastleLocationNames.btn_p1_floor, self.player) \
            .place_locked_item(self.create_event(ItemName.btnc_p1_floor))

        # Prison 2 Switches
        self.multiworld.get_location(CastleLocationNames.ev_p2_gold_gate_room_ne_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_p2_switch))
        self.multiworld.get_location(CastleLocationNames.ev_p2_gold_gate_room_nw_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_p2_switch))
        self.multiworld.get_location(CastleLocationNames.ev_p2_gold_gate_room_se_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_p2_switch))
        self.multiworld.get_location(CastleLocationNames.ev_p2_gold_gate_room_sw_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_p2_switch))

        # Prison Boss Switches
        self.multiworld.get_location(CastleLocationNames.ev_p1_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b1_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_p2_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b1_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_p3_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b1_boss_switch))

        # Armory Boss Switches
        self.multiworld.get_location(CastleLocationNames.ev_a1_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b2_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_a2_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b2_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_a3_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b2_boss_switch))
        # Event items
        self.multiworld.get_location(CastleLocationNames.btnc_n2_blue_spikes, self.player) \
            .place_locked_item(self.create_event(ItemName.btnc_a2_blue_spikes))

        # Archives Boss Switches
        self.multiworld.get_location(CastleLocationNames.ev_r1_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b3_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_r2_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b3_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_r3_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b3_boss_switch))

        # Chambers Event Items
        self.multiworld.get_location(CastleLocationNames.btnc_c2_n_open_wall, self.player) \
            .place_locked_item(self.create_event(ItemName.btnc_c2_n_wall))
        self.multiworld.get_location(CastleLocationNames.ev_c2_n_shops_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c2_n_shops_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_rspikes_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c3_rspikes_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_sw_hidden_switch_1, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c3_sw_hidden_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_sw_hidden_switch_2, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c3_sw_hidden_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_sw_hidden_switch_3, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c3_sw_hidden_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_sw_hidden_switch_4, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c3_sw_hidden_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_sw_hidden_switch_5, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c3_sw_hidden_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_sw_hidden_switch_6, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c3_sw_hidden_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c1_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b4_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c2_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b4_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_c3_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b4_boss_switch))

        # Bonus Key Locations
        if not self.multiworld.randomize_bonus_keys[self.player]:
            self.multiworld.get_location(CastleLocationNames.n1_room1, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n1_room3_sealed_room_1, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n1_room2_small_box, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n1_entrance, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n1_room4_m, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))

            self.multiworld.get_location(CastleLocationNames.n2_m_n, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n2_m_m_3, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n2_ne_4, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n2_m_e, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n2_start_1, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n2_m_se_5, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))

            self.multiworld.get_location(CastleLocationNames.n3_exit_sw, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n3_m_cluster_5, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n3_se_cluster_5, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))

            self.multiworld.get_location(CastleLocationNames.n4_ne, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n4_by_w_room_1, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n4_by_w_room_2, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(CastleLocationNames.n4_by_exit, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))

    def place_tots_locked_items(self):
        # Portal event items/locations
        def portal_rule(state) -> bool:
            return state.has(ItemName.key_teleport, 6)
        c1_portal_loc = self.multiworld.get_location(TempleLocationNames.ev_c1_portal, self.player)
        # c1_portal_loc.access_rule = portal_rule
        c1_portal_loc.place_locked_item(self.create_event(ItemName.ev_c1_portal))
        c2_portal_loc = self.multiworld.get_location(TempleLocationNames.ev_c2_portal, self.player)
        # c2_portal_loc.access_rule = portal_rule
        c2_portal_loc.place_locked_item(self.create_event(ItemName.ev_c2_portal))
        c3_portal_loc = self.multiworld.get_location(TempleLocationNames.ev_c3_portal, self.player)
        # c3_portal_loc.access_rule = portal_rule
        c3_portal_loc.place_locked_item(self.create_event(ItemName.ev_c3_portal))
        t1_portal_loc = self.multiworld.get_location(TempleLocationNames.ev_t1_portal, self.player)
        # t1_portal_loc.access_rule = portal_rule
        t1_portal_loc.place_locked_item(self.create_event(ItemName.ev_t1_portal))
        t2_portal_loc = self.multiworld.get_location(TempleLocationNames.ev_t2_portal, self.player)
        # t2_portal_loc.access_rule = portal_rule
        t2_portal_loc.place_locked_item(self.create_event(ItemName.ev_t2_portal))
        t3_portal_loc = self.multiworld.get_location(TempleLocationNames.ev_t3_portal, self.player)
        # t3_portal_loc.access_rule = portal_rule
        t3_portal_loc.place_locked_item(self.create_event(ItemName.ev_t3_portal))

        # Temple shortcut
        self.multiworld.get_location(TempleLocationNames.ev_temple_entrance_rock, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_open_temple_entrance_shortcut))

        # Pyramid of fear
        self.multiworld.get_location(TempleLocationNames.ev_hub_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_switch))
        self.multiworld.get_location(TempleLocationNames.ev_cave1_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_switch))
        self.multiworld.get_location(TempleLocationNames.ev_cave2_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_switch))
        self.multiworld.get_location(TempleLocationNames.ev_cave3_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_switch))
        self.multiworld.get_location(TempleLocationNames.ev_temple1_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_switch))
        self.multiworld.get_location(TempleLocationNames.ev_temple2_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_switch))

        self.multiworld.get_location(TempleLocationNames.ev_pof_1_unlock_exit, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_1_unlock_exit))
        self.multiworld.get_location(TempleLocationNames.ev_pof_2_unlock_exit, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_2_unlock_exit))
        self.multiworld.get_location(TempleLocationNames.ev_pof_end, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_complete))

        # Krilith defeated
        self.multiworld.get_location(TempleLocationNames.ev_krilith_defeated, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_krilith_defeated))

        # Temple Floor 2 buttons
        self.multiworld.get_location(TempleLocationNames.btn_t2_floor_blue, self.player) \
            .place_locked_item(self.create_event(ItemName.btn_t2_blue_spikes))
        # Temple Floor 2 light bridge switches
        self.multiworld.get_location(TempleLocationNames.btn_t2_rune_n, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_rune_switch))
        self.multiworld.get_location(TempleLocationNames.btn_t2_rune_w, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_rune_switch))
        self.multiworld.get_location(TempleLocationNames.btn_t2_rune_e, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_rune_switch))
        self.multiworld.get_location(TempleLocationNames.btn_t2_rune_se, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_rune_switch))
        self.multiworld.get_location(TempleLocationNames.btn_t2_rune_sw, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_rune_switch))

        # Temple solar nodes
        self.multiworld.get_location(TempleLocationNames.ev_t1_n_node, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_solar_node))
        self.multiworld.get_location(TempleLocationNames.ev_t1_s_node, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_solar_node))
        self.multiworld.get_location(TempleLocationNames.ev_t2_n_node, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_solar_node))
        self.multiworld.get_location(TempleLocationNames.ev_t2_s_node, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_solar_node))
        self.multiworld.get_location(TempleLocationNames.ev_t3_n_node, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_solar_node))
        self.multiworld.get_location(TempleLocationNames.ev_t3_s_node, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_solar_node))

        # Pyramid of Fear Bonus Keys
        if not self.multiworld.randomize_bonus_keys[self.player]:
            self.multiworld.get_location(TempleLocationNames.pof_1_n_5, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))
            self.multiworld.get_location(TempleLocationNames.pof_1_ent_5, self.player) \
                .place_locked_item(self.create_item(ItemName.key_bonus))

        # Portal Accessibility rune keys
        if self.multiworld.portal_accessibility[self.player]:
            rune_key_locs: typing.List[str] = []

            def get_region_item_locs(region: str):
                return [loc.name for loc in self.multiworld.get_region(region, self.player).locations
                        if loc.name not in temple_event_locations]

            # Cave Level 3 Rune Key
            c3_locs = get_region_item_locs(TempleRegionNames.cave_3_main)
            rune_key_locs.append(self.multiworld.random.choice(c3_locs))

            # Cave Level 2 Rune Key
            c2_locs = get_region_item_locs(TempleRegionNames.cave_2_main)
            rune_key_locs.append(self.multiworld.random.choice(c2_locs))

            # Cave Level 1 Rune Key
            c1_locs = []
            c1_locs += get_region_item_locs(TempleRegionNames.cave_1_main)
            c1_locs += get_region_item_locs(TempleRegionNames.cave_1_blue_bridge)
            c1_locs += get_region_item_locs(TempleRegionNames.cave_1_red_bridge)
            rune_key_locs.append(self.multiworld.random.choice(c1_locs))

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
            rune_key_locs.append(self.multiworld.random.choice(t1_locs))

            # Temple Floor 2 Rune Key
            t2_locs = []
            t2_locs += get_region_item_locs(TempleRegionNames.t2_main)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_n_gate)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_s_gate)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_n_node)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_s_node)
            t2_locs += get_region_item_locs(TempleRegionNames.t2_ornate)
            rune_key_locs.append(self.multiworld.random.choice(t2_locs))

            # Temple Floor 3 Rune Key
            t3_locs = []
            t3_locs += get_region_item_locs(TempleRegionNames.t3_main)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_n_node_blocks)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_s_node_blocks_1)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_s_node_blocks_2)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_s_node)
            t3_locs += get_region_item_locs(TempleRegionNames.t3_n_node)
            rune_key_locs.append(self.multiworld.random.choice(t3_locs))

            for loc in rune_key_locs:
                self.multiworld.get_location(loc, self.player).place_locked_item(
                    self.create_item(ItemName.key_teleport))

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player, self.door_counts)

    def write_spoiler(self, spoiler_handle) -> None:
        if self.multiworld.shop_shuffle[self.player] > 0:
            spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Shop Shuffle Locations:\n")
            for loc, shop in self.shop_locations.items():
                spoiler_handle.write(f"\n{loc}: {shop}")
