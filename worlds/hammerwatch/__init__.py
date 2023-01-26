import os
import typing

from .Items import HammerwatchItem, ItemData, item_table, junk_items, trap_items, get_item_counts, filler_items
from .Locations import *
from .Regions import create_regions
from .Rules import set_rules
from .Util import *

from .Names import ItemName, TempleLocationNames, TempleRegionNames

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from .Options import hammerwatch_options
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

    data_version = 0

    web = HammerwatchWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    campaign: Campaign = Campaign.Castle
    active_location_list: typing.Dict[str, LocationData]
    item_counts: typing.Dict[str, int]

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        slot_data: typing.Dict[str, object] = {}
        for option_name in self.option_definitions:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value
        for loc, value in random_locations.items():
            slot_data[loc] = value
        return slot_data

    def generate_early(self):
        self.campaign = get_campaign(self.multiworld, self.player)
        # self.item_counts, extra_items = get_item_counts(self.multiworld, self.campaign, self.player)
        self.active_location_list, self.item_counts = setup_locations(self.multiworld, self.campaign, self.player)

    def generate_basic(self) -> None:
        self.multiworld.get_location(TempleLocationNames.ev_victory, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_victory))
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.ev_victory, self.player)

        if self.campaign == Campaign.Castle:
            self.place_castle_locked_items()
        else:
            self.place_tots_locked_items()

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.campaign, self.player, self.active_location_list)

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
            if self.multiworld.randomize_bonus_keys[self.player].value == 0:
                total_required_locations -= 18  # Preplaced bonus keys
        elif self.campaign == Campaign.Temple:
            total_required_locations -= len(temple_event_locations)
            if self.multiworld.randomize_bonus_keys[self.player].value == 0:
                total_required_locations -= 2  # Preplaced bonus keys

            # If Portal Accessibility is on, we create/place the Rune Keys elsewhere
            if self.multiworld.portal_accessibility[self.player].value > 0:
                total_required_locations -= 6

        # Get the counts of each item we'll put in
        # item_counts: typing.Dict[str, int] = get_item_counts(self.multiworld, self.campaign, self.player)

        # Add items
        for item in item_table:
            if item in self.item_counts:
                item_names += [item] * self.item_counts[item]

        # Exclude items if the player starts with them
        exclude = [item for item in self.multiworld.precollected_items[self.player]]
        for item in map(self.create_item, item_names):
            if item in exclude:
                exclude.remove(item)
            else:
                itempool.append(item)

        # Add junk items if there aren't enough items to fill the locations
        junk: int = total_required_locations - len(itempool)
        junk_pool: typing.List[Item] = []
        for item_name in self.multiworld.random.choices(junk_items, k=junk):
            junk_pool += [self.create_item(item_name)]

        itempool += junk_pool

        self.multiworld.itempool += itempool

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(tuple(filler_items))

    def place_castle_locked_items(self):
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
        # self.multiworld.get_location(CastleLocationNames.ev_p3_boss_switch_skip, self.player) \
        #    .place_locked_item(self.create_event(ItemName.ev_castle_b1_boss_switch))

        # Armory Boss Switches
        self.multiworld.get_location(CastleLocationNames.ev_a1_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b2_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_a2_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b2_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_a3_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b2_boss_switch))

        # Archives Boss Switches
        self.multiworld.get_location(CastleLocationNames.ev_r1_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b3_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_r2_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b3_boss_switch))
        self.multiworld.get_location(CastleLocationNames.ev_r3_boss_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_b3_boss_switch))

        # Chambers Event Items
        self.multiworld.get_location(CastleLocationNames.ev_c2_n_tp_button, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_castle_c2_n_tp_button))
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
        if self.multiworld.randomize_bonus_keys[self.player].value == 0:
            self.multiworld.get_location(CastleLocationNames.n1_room1, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n1_room3_sealed_room_1, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n1_room2_small_box, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n1_entrance, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n1_room4_m, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))

            self.multiworld.get_location(CastleLocationNames.n2_m_n, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n2_m_m_3, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n2_ne_4, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n2_m_e, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n2_start_1, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n2_m_se_5, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))

            self.multiworld.get_location(CastleLocationNames.n3_exit_sw, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n3_m_cluster_5, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n3_se_cluster_5, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))

            self.multiworld.get_location(CastleLocationNames.n4_ne, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n4_by_w_room_1, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n4_by_w_room_2, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(CastleLocationNames.n4_by_exit, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))

    def place_tots_locked_items(self):
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

        self.multiworld.get_location(TempleLocationNames.ev_pof_end, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_pof_complete))

        # Krilith defeated
        self.multiworld.get_location(TempleLocationNames.ev_krilith_defeated, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_krilith_defeated))

        # Temple Floor 2 light bridge switches
        self.multiworld.get_location(TempleLocationNames.ev_t2_n_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_bridge_switch))
        self.multiworld.get_location(TempleLocationNames.ev_t2_w_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_bridge_switch))
        self.multiworld.get_location(TempleLocationNames.ev_t2_ne_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_bridge_switch))
        self.multiworld.get_location(TempleLocationNames.ev_t2_se_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_bridge_switch))
        self.multiworld.get_location(TempleLocationNames.ev_t2_sw_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.ev_t2_bridge_switch))

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
        if self.multiworld.randomize_bonus_keys[self.player].value == 0:
            self.multiworld.get_location(TempleLocationNames.pof_1_n_5, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))
            self.multiworld.get_location(TempleLocationNames.pof_1_ent_5, self.player) \
                .place_locked_item(self.create_item(ItemName.bonus_key))

        # Portal Accessibility rune keys
        if self.multiworld.portal_accessibility[self.player].value > 0:
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
                self.multiworld.get_location(loc, self.player).place_locked_item(self.create_item(ItemName.key_teleport))

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)
