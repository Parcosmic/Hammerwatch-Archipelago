import typing

from .names import item_name, castle_region_names, castle_location_names, temple_region_names, temple_location_names, \
    entrance_names, option_names
from .items import (HammerwatchItem, item_table, key_table, filler_items, castle_item_counts, temple_item_counts,
                    castle_button_table, temple_button_table)
from .locations import (LocationData, all_locations, setup_locations, castle_event_buttons, temple_event_buttons,
                        castle_button_locations, temple_button_locations, castle_button_items, temple_button_items)
from .regions import create_regions, HWEntrance, HWExitData
from .rules import set_rules
from .util import Campaign, get_campaign, get_active_key_names
from .options import HammerwatchOptions, client_required_options

from BaseClasses import Item, Tutorial, ItemClassification, CollectionState
from ..AutoWorld import World, WebWorld
from Utils import visualize_regions
from Fill import fill_restrictive


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
    options_dataclass = HammerwatchOptions
    options: HammerwatchOptions
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
    world_itempool: typing.List[Item]
    random_locations: typing.Dict[str, int]
    shop_locations: typing.Dict[str, str]
    door_counts: typing.Dict[str, int]
    gate_types: typing.Dict[str, str]
    level_exits: typing.List[HWEntrance]
    exit_swaps: typing.Dict[str, str]
    exit_spoiler_info: typing.List[str]
    start_exit: str
    key_item_counts: typing.Dict[str, int]

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        return {
            **self.options.as_dict(*client_required_options),
            **self.random_locations,
            **self.shop_locations,
            option_names.act_specific_keys: 1 if self.options.key_mode.value == 1 else 0,
            "Hammerwatch Mod Version": self.hw_client_version,
            "Gate Types": self.gate_types,
            "Exit Swaps": self.exit_swaps,
            "Start Exit": self.start_exit
        }

    def generate_early(self):
        self.campaign = get_campaign(self)

        exclusive_mod_groups = [[option_names.mod_no_extra_lives, option_names.mod_infinite_lives, option_names.mod_double_lives],
                                [option_names.mod_1_hp, option_names.mod_no_hp_pickups],
                                [option_names.mod_1_hp, option_names.mod_reverse_hp_regen, option_names.mod_hp_regen],
                                [option_names.mod_no_mana_regen, option_names.mod_5x_mana_regen]]

        # Validate game modifiers
        exclude_mods = []
        for mod, value in self.options.game_modifiers.value.items():
            if value:
                if mod in exclude_mods:
                    self.options.game_modifiers.value[mod] = False
                    continue
                for ex_list in exclusive_mod_groups:
                    if mod not in ex_list:
                        continue
                    for ex_mod in ex_list:
                        if ex_mod in exclude_mods:
                            continue
                        exclude_mods.append(ex_mod)

        # Door type randomization
        if self.campaign == Campaign.Castle:
            item_counts = castle_item_counts
        else:
            item_counts = temple_item_counts
        self.key_item_counts = {}
        self.door_counts = {}
        active_keys = get_active_key_names(self)
        for key in active_keys:
            if key in item_counts.keys():
                self.door_counts[key] = item_counts[key]

        self.active_location_list, self.item_counts, self.random_locations = setup_locations(self, self.campaign)

    def create_regions(self) -> None:
        self.level_exits = []
        self.gate_types = create_regions(self, self.campaign, self.active_location_list, self.random_locations)
        # Dumb hack to make sure everything is connected before other worlds try to do logic stuff
        self.exit_swaps = {}
        self.exit_spoiler_info = []
        set_rules(self, self.door_counts)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return HammerwatchItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str):
        return HammerwatchItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        self.world_itempool = []

        # First create and place our locked items so we know how many are left over
        if self.campaign == Campaign.Castle:
            self.place_castle_locked_items()
            button_item_names = list(castle_button_table.keys())
        else:
            self.place_tots_locked_items()
            button_item_names = list(temple_button_table.keys())

        total_required_locations = len(self.multiworld.get_unfilled_locations(self.player))

        # Add key items to item_counts
        self.item_counts.update(self.key_item_counts)

        # Remove progression items if the player starts with them
        for precollected in self.multiworld.precollected_items[self.player]:
            if precollected.classification & ItemClassification.progression:
                if precollected.name in self.item_counts and self.item_counts[precollected.name] > 0:
                    self.item_counts[precollected.name] -= 1

        # If buttonsanity is set to shuffle prevent button items from being created here
        items_to_place_later = 0
        item_counts = {}
        if self.options.buttonsanity.value == self.options.buttonsanity.option_shuffle:
            for item, count in self.item_counts.items():
                if item in button_item_names:
                    items_to_place_later += count
                    continue
                item_counts[item] = count
            # item_counts = {item: count for item, count in self.item_counts.items() if item not in button_item_names}
        else:
            item_counts = self.item_counts

        # Add items
        items = 0
        present_filler_items = []
        for item in item_counts:
            items += item_counts[item]
            if item_table[item].classification == ItemClassification.filler and item_counts[item] > 0:
                present_filler_items.append(item)

        # Add/remove junk items depending if we have not enough/too many locations
        junk: int = total_required_locations - items - items_to_place_later
        if junk > 0:
            for name in self.random.choices(present_filler_items, k=junk):
                item_counts[name] += 1
        else:
            for j in range(-junk):
                junk_item = self.random.choice(present_filler_items)
                item_counts[junk_item] -= 1
                if item_counts[junk_item] == 0:
                    present_filler_items.remove(junk_item)

        # Create items and add to item pool
        for item in item_counts:
            for i in range(item_counts[item]):
                self.world_itempool.append(self.create_item(item))

        self.multiworld.itempool += self.world_itempool

    def collect(self, state: CollectionState, item: Item) -> bool:
        prog = super(HammerwatchWorld, self).collect(state, item)
        spaces = item.name.count(" ")
        if item.name.endswith("Key") and spaces > 1 and item.name in key_table:
            add_name = key_table[item.name][0]
            count = key_table[item.name][1]
            state.prog_items[self.player][add_name] += count
            if item.name.startswith("Big") and spaces == 3:
                state.prog_items[self.player][key_table[add_name][0]] += count * key_table[add_name][1]
        return prog

    def remove(self, state: CollectionState, item: Item) -> bool:
        prog = super(HammerwatchWorld, self).remove(state, item)
        spaces = item.name.count(" ")
        if item.name.endswith("Key") and spaces > 1:
            add_name = key_table[item.name][0]
            count = key_table[item.name][1]
            state.prog_items[self.player][add_name] -= count
            if item.name.startswith("Big") and spaces == 3:
                state.prog_items[self.player][key_table[add_name][0]] -= count * key_table[add_name][1]
        return prog

    def get_filler_item_name(self) -> str:
        return self.random.choice(tuple(filler_items))

    def place_castle_locked_items(self):
        castle_events = {
            castle_location_names.ev_beat_boss_1: item_name.evc_beat_boss_1,
            castle_location_names.ev_beat_boss_2: item_name.evc_beat_boss_2,
            castle_location_names.ev_beat_boss_3: item_name.evc_beat_boss_3,
            castle_location_names.ev_beat_boss_4: item_name.evc_beat_boss_4,
        }
        if self.options.goal == self.options.goal.option_castle_escape:
            castle_events[castle_location_names.ev_escape] = item_name.evc_escaped

        # Bonus Key Locations
        if not self.options.randomize_bonus_keys.value:
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

        for loc, itm in castle_events.items():
            location = self.multiworld.get_location(loc, self.player)
            location.address = None
            location.place_locked_item(self.create_event(itm))
        if not self.options.buttonsanity.value:
            for loc, itm in castle_event_buttons.items():
                location = self.multiworld.get_location(loc, self.player)
                location.address = None
                location.place_locked_item(self.create_event(itm))

    def place_tots_locked_items(self):
        temple_events = {
            temple_location_names.ev_c1_portal: item_name.ev_c1_portal,
            temple_location_names.ev_c2_portal: item_name.ev_c2_portal,
            temple_location_names.ev_c3_portal: item_name.ev_c3_portal,
            temple_location_names.ev_t1_portal: item_name.ev_t1_portal,
            temple_location_names.ev_t2_portal: item_name.ev_t2_portal,
            temple_location_names.ev_t3_portal: item_name.ev_t3_portal,
            temple_location_names.ev_temple_entrance_rock: item_name.ev_open_temple_entrance_shortcut,
            temple_location_names.ev_t1_n_node_n_mirrors: item_name.evt_t1_n_mirrors,
            temple_location_names.ev_t1_n_node_s_mirror: item_name.evt_t1_s_mirror,
            temple_location_names.ev_pof_end: item_name.ev_pof_complete,
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
        if not self.options.randomize_bonus_keys.value:
            temple_bonus_keys = [
                temple_location_names.pof_1_n_5,
                temple_location_names.pof_1_ent_5,
            ]
            for loc in temple_bonus_keys:
                self.multiworld.get_location(loc, self.player).place_locked_item(self.create_item(item_name.key_bonus))

        # Event/button items
        for loc, itm in temple_events.items():
            location = self.multiworld.get_location(loc, self.player)
            location.address = None
            location.place_locked_item(self.create_event(itm))
        if not self.options.buttonsanity.value:
            for loc, itm in temple_event_buttons.items():
                location = self.multiworld.get_location(loc, self.player)
                location.address = None
                location.place_locked_item(self.create_event(itm))

        # Portal Accessibility rune keys
        if self.options.portal_accessibility.value:
            rune_key_locs: typing.List[str] = []

            def get_region_item_locs(region: str):
                if self.options.buttonsanity.value == self.options.buttonsanity.option_shuffle:
                    return [loc.name for loc in self.multiworld.get_region(region, self.player).locations
                            if not loc.event and loc.name not in temple_button_locations]
                else:
                    return [loc.name for loc in self.multiworld.get_region(region, self.player).locations
                            if not loc.event]

            # Cave Level 3 Rune Key
            c3_locs = get_region_item_locs(temple_region_names.c3_e)
            # If playing exit rando we need to ensure we can always return if falling from the temple
            if not self.options.exit_randomization.value:
                c3_locs.extend(get_region_item_locs(temple_region_names.cave_3_main))
            rune_key_locs.append(self.random.choice(c3_locs))

            # Cave Level 2 Rune Key
            c2_locs = get_region_item_locs(temple_region_names.cave_2_main)
            rune_key_locs.append(self.random.choice(c2_locs))

            # Cave Level 1 Rune Key
            c1_locs = []
            c1_locs += get_region_item_locs(temple_region_names.cave_1_main)
            c1_locs += get_region_item_locs(temple_region_names.cave_1_blue_bridge)
            c1_locs += get_region_item_locs(temple_region_names.cave_1_red_bridge)
            rune_key_locs.append(self.random.choice(c1_locs))

            # Temple Floor 1 Rune Key
            t1_locs = []
            t1_locs += get_region_item_locs(temple_region_names.t1_main)
            t1_locs += get_region_item_locs(temple_region_names.t1_sw_sdoor)
            t1_locs += get_region_item_locs(temple_region_names.t1_node_1)
            t1_locs += get_region_item_locs(temple_region_names.t1_node_2)
            t1_locs += get_region_item_locs(temple_region_names.t1_sun_turret)
            t1_locs += get_region_item_locs(temple_region_names.t1_ice_turret)
            t1_locs += get_region_item_locs(temple_region_names.t1_n_of_ice_turret)
            t1_locs += get_region_item_locs(temple_region_names.t1_s_of_ice_turret)
            t1_locs += get_region_item_locs(temple_region_names.t1_east)
            t1_locs += get_region_item_locs(temple_region_names.t1_sun_block_hall)
            rune_key_locs.append(self.random.choice(t1_locs))

            # Temple Floor 2 Rune Key
            t2_locs = []
            t2_locs += get_region_item_locs(temple_region_names.t2_main)
            t2_locs += get_region_item_locs(temple_region_names.t2_n_gate)
            t2_locs += get_region_item_locs(temple_region_names.t2_s_gate)
            t2_locs += get_region_item_locs(temple_region_names.t2_n_node)
            t2_locs += get_region_item_locs(temple_region_names.t2_s_node)
            t2_locs += get_region_item_locs(temple_region_names.t2_ornate)
            rune_key_locs.append(self.random.choice(t2_locs))

            # Temple Floor 3 Rune Key
            t3_locs = []
            t3_locs += get_region_item_locs(temple_region_names.t3_main)
            t3_locs += get_region_item_locs(temple_region_names.t3_n_node_blocks)
            t3_locs += get_region_item_locs(temple_region_names.t3_s_node_blocks_1)
            t3_locs += get_region_item_locs(temple_region_names.t3_s_node_blocks_2)
            t3_locs += get_region_item_locs(temple_region_names.t3_s_node)
            t3_locs += get_region_item_locs(temple_region_names.t3_n_node)
            rune_key_locs.append(self.random.choice(t3_locs))

            for loc in rune_key_locs:
                self.multiworld.get_location(loc, self.player).place_locked_item(
                    self.create_item(item_name.key_teleport))

    def set_rules(self) -> None:
        # self.exit_swaps = {}
        # self.exit_spoiler_info = []
        # set_rules(self, self.door_counts)
        pass

    def generate_basic(self) -> None:
        # Shop shuffle
        self.shop_locations = {}
        if self.options.shop_shuffle.value:
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
        if self.options.shop_cost_max.value < self.options.shop_cost_min.value:
            swap = self.options.shop_cost_max.value
            self.options.shop_cost_max.value = self.options.shop_cost_min.value
            self.options.shop_cost_min.value = swap

    def pre_fill(self) -> None:
        if self.options.buttonsanity.value == self.options.buttonsanity.option_shuffle:
            if get_campaign(self) == Campaign.Castle:
                button_locations = list(castle_button_locations.keys())
                button_item_names = list(castle_button_table.keys())
            else:
                button_locations = list(temple_button_locations.keys())
                button_item_names = list(temple_button_table.keys())
            valid_locs = list(self.multiworld.get_unfilled_locations_for_players(button_locations, [self.player]))
            # state = self.multiworld.get_all_state(False)
            # for loc_name, itm_name in castle_button_items.items():
            #     if itm_name not in self.item_counts:
            #         continue
            #     loc = self.multiworld.get_location(loc_name, self.player)
            #     itm = self.create_item(itm_name)
            #     loc.place_locked_item(itm)
            #     state.collect(itm, False, loc)
            # state.update_reachable_regions(self.player)
            # visualize_regions(self.multiworld.get_region("Menu", self.player), "_testing.puml", show_locations=False,
            #                   highlight_regions=state.reachable_regions[self.player])
            button_items = []
            for item in button_item_names:
                if item not in self.item_counts:
                    continue
                for i in range(self.item_counts[item]):
                    button_items.append(self.create_item(item))
            non_button_prog_items = [item for item in self.world_itempool
                                    if item.classification & ItemClassification.progression]
            non_button_state = CollectionState(self.multiworld)
            for prog_item in non_button_prog_items:
                non_button_state.collect(prog_item)
            self.random.shuffle(valid_locs)
            self.random.shuffle(button_items)
            fill_restrictive(self.multiworld, non_button_state, valid_locs, button_items,
                             True, False, True, None, False, False, "Button Shuffle")

    def write_spoiler(self, spoiler_handle) -> None:
        if self.options.shop_shuffle.value:
            spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Shop Shuffle Locations:\n")
            for loc, shop in self.shop_locations.items():
                spoiler_handle.write(f"\n{loc}: {shop}")
            # spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Exit Randomization Connections:\n")
            # for entry in self.exit_spoiler_info:
            #     spoiler_handle.write(f"\n{entry}")

    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        pass
