import logging
import typing

from .names import item_name, castle_region_names, castle_location_names, temple_region_names, temple_location_names, \
    entrance_names, option_names, gate_names, location_groups
from .items import (HammerwatchItem, item_table, key_table, filler_items, trap_items,
                    castle_item_counts, temple_item_counts, castle_button_table, temple_button_table)
from .locations import (LocationData, all_locations, setup_locations, castle_event_buttons, temple_event_buttons,
                        castle_button_locations, temple_button_locations, castle_button_items, temple_button_items)
from .regions import create_regions, HWEntrance, HWExitData, get_etr_name, connect_shops
from .rules import set_rules, connect_regions_er
from .util import (Campaign, get_campaign, get_active_key_names, ShopInfo, ShopType, get_shopsanity_classes,
                   is_using_universal_tracker, get_random_element, get_random_elements)
from .options import HammerwatchOptions, client_required_options, option_groups, option_presets

from BaseClasses import Item, Tutorial, ItemClassification, CollectionState, MultiWorld
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

    option_groups = option_groups
    options_presets = option_presets


class HammerwatchWorld(World):
    """
    Hammerwatch is a hack and slash action adventure.
    Play as a hero that is one of seven classes as you fight your way through Castle Hammerwatch to defeat the dragon
    or the Temple of the Sun to stop the evil Sun Guardian Sha'Rand.
    """
    game = "Hammerwatch"
    options_dataclass = HammerwatchOptions
    options: HammerwatchOptions
    topology_present: bool = True
    remote_start_inventory: bool = True

    apworld_version = "3.0"
    hw_client_version = "1.2"

    web = HammerwatchWeb()

    tracker_world = {"map_page_folder": "HammerwatchTrackerPack",
                     "map_page_maps": "maps/maps.json",
                     "map_page_locations": "locations/castle_locations.json"}

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    item_name_groups = item_name.item_groups
    location_name_groups = location_groups.location_groups

    campaign: Campaign
    active_location_list: typing.Dict[str, LocationData]
    item_counts: typing.Dict[str, int]
    world_itempool: typing.List[Item]
    random_locations: typing.Dict[str, int]
    shop_locations: typing.Dict[str, ShopInfo]
    door_counts: typing.Dict[str, int]
    gate_types: typing.Dict[str, int]
    level_exits: typing.List[HWEntrance]
    exit_swaps: typing.Dict[str, str]
    start_exit: str
    key_item_counts: typing.Dict[str, int]

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        return {
            **self.options.as_dict(*client_required_options),
            "Random Locations": self.random_locations,
            "Shop Locations": {s_loc: s_info.to_slot_data() for s_loc, s_info in self.shop_locations.items()},
            "APWorld Version": self.apworld_version,
            "Hammerwatch Mod Version": self.hw_client_version,
            "Gate Types": {gate_names.gate_name_indices[gate]: typ for gate, typ in self.gate_types.items()},
            "Exit Swaps": {entrance_names.entrance_name_indices[orig]: entrance_names.entrance_name_indices[new]
                           for orig, new in self.exit_swaps.items()},
            "Start Exit": entrance_names.entrance_name_indices[self.start_exit],
        }

    def generate_early(self):
        self.campaign = get_campaign(self)

        # Hack to test if we can hotswap the maps and locations for UT map tracking
        if self.campaign == Campaign.Temple:
            self.tracker_world["map_page_maps"] = "maps/maps_temple.json"
            self.tracker_world["map_page_locations"] = "locations/temple_locations.json"

        # Validate act specific keys option
        if self.campaign == Campaign.Temple and self.options.key_mode == self.options.key_mode.option_act_specific:
            slot_name = self.multiworld.player_name[self.player]
            logging.warning(f"Slot \"{slot_name}\": Act Specific Keys option not compatible with temple campaign, "
                            f"switching to vanilla")
            self.options.key_mode.value = self.options.key_mode.option_vanilla

        # Validate game modifiers
        exclusive_mod_groups = ((option_names.mod_no_extra_lives, option_names.mod_infinite_lives,
                                 option_names.mod_double_lives),
                                (option_names.mod_1_hp, option_names.mod_no_hp_pickups),
                                (option_names.mod_1_hp, option_names.mod_reverse_hp_regen, option_names.mod_hp_regen),
                                (option_names.mod_no_mana_regen, option_names.mod_5x_mana_regen))
        exclude_mods = []
        for mod, value in self.options.game_modifiers.value.items():
            if value:
                if mod in exclude_mods:
                    logging.warning(f"Game Modifier '{mod}' for player {self.player} incompatible with other "
                                    f"modifiers selected, it is now disabled")
                    self.options.game_modifiers.value[mod] = False
                    continue
                for ex_list in exclusive_mod_groups:
                    if mod not in ex_list:
                        continue
                    for ex_mod in ex_list:
                        if ex_mod in exclude_mods:
                            continue
                        exclude_mods.append(ex_mod)

        # Validate trap item weight option
        all_zero = True
        for item, weight in self.options.trap_item_weights.value.items():
            if weight > 0:
                all_zero = False
                break
        if all_zero:
            logging.info(f"Trap weights for player {self.player} were set to all zero, resetting them all to 100")
            self.options.trap_item_weights.value = {item: 100 for item in trap_items}

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
        if hasattr(self.multiworld, "re_gen_passthrough"):
            self.gate_types = self.multiworld.re_gen_passthrough["Hammerwatch"]["Gate Types"]
        self.gate_types = create_regions(self, self.campaign, self.active_location_list)
        self.exit_swaps = {}
        connect_regions_er(self)
        connect_shops(self)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return HammerwatchItem(name, data.classification, data.code, self.player)

    def create_item_with_flags(self, name: str, classification: ItemClassification) -> Item:
        data = item_table[name]
        return HammerwatchItem(name, classification, data.code, self.player)

    def create_event(self, event: str):
        return HammerwatchItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        self.world_itempool = []

        # Add floor master key items to item_counts
        if self.options.key_mode.value == self.options.key_mode.option_floor_master:
            if self.options.randomize_bonus_keys.value:
                self.item_counts.update(self.key_item_counts)
            else:
                self.item_counts.update({key: num for key, num in self.key_item_counts.items() if "Bonus" not in key})

        # First create and place our locked items so we know how many are left over
        if self.campaign == Campaign.Castle:
            self.place_castle_locked_items()
        else:
            self.place_tots_locked_items()
            # If we're playing with enemy loot on and key mode is floor master we already place this key
            if self.options.randomize_enemy_loot.value == 0:
                if self.options.key_mode.value == self.options.key_mode.option_floor_master:
                    self.item_counts[item_name.key_gold_b1] = 0
                    self.item_counts[item_name.key_silver_b1] = 0

        # If we're using UT we don't need to create any items
        if is_using_universal_tracker(self):
            return

        total_required_locations = len(self.multiworld.get_unfilled_locations(self.player))

        # Remove progression items if the player starts with them
        for precollected in self.multiworld.precollected_items[self.player]:
            if precollected.classification & ItemClassification.progression:
                if precollected.name in self.item_counts and self.item_counts[precollected.name] > 0:
                    self.item_counts[precollected.name] -= 1

        item_counts = self.item_counts

        # Add items
        total_items = 0
        # present_filler_items = []
        present_filler_item_counts = {}
        for item in item_counts:
            total_items += item_counts[item]
            if item_table[item].classification == ItemClassification.filler and item_counts[item] > 0:
                # present_filler_items.append(item)
                present_filler_item_counts[item] = item_counts[item]

        # Add/remove junk items depending if we have not enough/too many locations
        junk: int = total_required_locations - total_items
        if junk > 0:
            # for name in self.random.choices(present_filler_items, k=junk):
            #     item_counts[name] += 1
            for junk_name in get_random_elements(self, present_filler_item_counts, junk):
                item_counts[junk_name] += 1
        else:
            while junk < 0:
                junk += 1
                # junk_item = self.random.choice(present_filler_items)
                junk_item = get_random_element(self, present_filler_item_counts)
                item_counts[junk_item] -= 1
                present_filler_item_counts[junk_item] -= 1
                if item_counts[junk_item] == 0:
                    # present_filler_items.remove(junk_item)
                    # if len(present_filler_items) == 0:
                    #     break
                    present_filler_item_counts.pop(junk_item)
                    if len(present_filler_item_counts) == 0:
                        break
            # Remove trap items if we've run out of filler
            # present_trap_items = [trap_item for trap_item in trap_items if trap_item in item_counts]
            present_trap_item_counts = {trap_item: item_counts[trap_item] for trap_item in trap_items if trap_item in item_counts}
            while junk < 0:
                junk += 1
                # trap_item = self.random.choice(present_trap_items)
                trap_item = get_random_element(self, present_trap_item_counts)
                item_counts[trap_item] -= 1
                present_trap_item_counts[trap_item] -= 1
                if item_counts[trap_item] == 0:
                    # present_trap_items.remove(trap_item)
                    present_trap_item_counts.pop(trap_item)
                    if len(present_trap_item_counts) == 0:
                    # if len(present_trap_items) == 0:
                        logging.warning(f"HammerwatchWorld for player {self.multiworld.player_name[self.player]} "
                                        f"(slot {self.player}) ran out of filler and trap items to remove. Some items "
                                        f"will remain unplaced!")
                        break

        # If shopsanity is on we need ore to be progression
        if self.campaign == Campaign.Temple and len(get_shopsanity_classes(self)) > 0:
            ore_count = item_counts.pop(item_name.ore)
            for i in range(ore_count):
                self.world_itempool.append(self.create_item_with_flags(item_name.ore, ItemClassification.progression))

        # Create items and add to item pool
        for item in item_counts:
            for i in range(item_counts[item]):
                self.world_itempool.append(self.create_item(item))

        self.multiworld.itempool += self.world_itempool

    def get_filler_item_name(self) -> str:
        return self.random.choice(tuple(filler_items))

    def place_castle_locked_items(self):
        castle_events = {
            castle_location_names.ev_beat_boss_1: item_name.evc_beat_boss_1,
            castle_location_names.ev_beat_boss_2: item_name.evc_beat_boss_2,
            castle_location_names.ev_beat_boss_3: item_name.evc_beat_boss_3,
            castle_location_names.ev_beat_boss_4: item_name.evc_beat_boss_4,
            castle_location_names.ev_entrance_bridge: item_name.ev_all_planks,
            castle_location_names.ev_escape: item_name.evc_escaped
        }

        for loc, itm in castle_events.items():
            location = self.multiworld.get_location(loc, self.player)
            location.address = None
            location.place_locked_item(self.create_event(itm))
        if not self.options.buttonsanity.value:
            for loc, itm in castle_event_buttons.items():
                location = self.multiworld.get_location(loc, self.player)
                location.address = None
                location.place_locked_item(self.create_event(itm))

        # Don't place non-event items if we're using Universal Tracker
        if is_using_universal_tracker(self):
            return

        # Bonus Key Locations
        if not self.options.randomize_bonus_keys.value:
            act_bonus_key_locs = (
                (
                    castle_location_names.n1_room1,
                    castle_location_names.n1_room3_sealed_room_1,
                    castle_location_names.n1_room2_small_box,
                    castle_location_names.n1_entrance,
                    castle_location_names.n1_room4_m,
                ),
                (
                    castle_location_names.n2_m_n,
                    castle_location_names.n2_m_m_3,
                    castle_location_names.n2_ne_4,
                    castle_location_names.n2_m_e,
                    castle_location_names.n2_start_1,
                    castle_location_names.n2_m_se_5,
                ),
                (
                    castle_location_names.n3_exit_sw,
                    castle_location_names.n3_m_cluster_5,
                    castle_location_names.n3_se_cluster_5,
                ),
                (
                    castle_location_names.n4_ne,
                    castle_location_names.n4_by_w_room_1,
                    castle_location_names.n4_by_w_room_2,
                    castle_location_names.n4_by_exit,
                )
            )
            if self.options.key_mode == self.options.key_mode.option_vanilla:
                bonus_key_locs = [
                    *act_bonus_key_locs[0],
                    *act_bonus_key_locs[1],
                    *act_bonus_key_locs[2],
                    *act_bonus_key_locs[3],
                ]
                for loc_name in bonus_key_locs:
                    loc = self.multiworld.get_location(loc_name, self.player)
                    loc.place_locked_item(self.create_item(item_name.key_bonus))
            else:
                bonus_key_names = (
                    item_name.key_bonus_prison,
                    item_name.key_bonus_armory,
                    item_name.key_bonus_archives,
                    item_name.key_bonus_chambers,
                )
                for k in range(len(bonus_key_names)):
                    for loc_name in act_bonus_key_locs[k]:
                        loc = self.multiworld.get_location(loc_name, self.player)
                        loc.place_locked_item(self.create_item(bonus_key_names[k]))

        # Add a starting item to local_early_items to get out of an overly restrictive start with buttonsanity
        if (self.options.buttonsanity.value > 0 and self.start_exit == entrance_names.c_p1_start
                and self.options.randomize_recovery_items.value == 0):
            start_gate_name = get_etr_name(castle_region_names.p1_start, castle_region_names.p1_s)
            start_gate = self.multiworld.get_entrance(start_gate_name, self.player)
            assert isinstance(start_gate, HWEntrance)
            start_item_name = self.random.choice((start_gate.pass_item, item_name.btnc_p1_floor))
            if start_item_name.endswith(item_name.key_bronze) and start_item_name != item_name.key_bronze_prison_1:
                if self.random.random() < (self.options.big_bronze_key_percent.value / 100):
                    start_item_name = f"Big {start_item_name}"
            self.multiworld.local_early_items[self.player][start_item_name] = 1

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
            temple_location_names.ev_planks: item_name.ev_all_planks,
        }

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

        # Don't place non-event items if we're using Universal Tracker
        if is_using_universal_tracker(self):
            return

        # Force Dune Shark key location to be the correct key if randomize enemy loot is off
        if self.options.randomize_enemy_loot.value == 0:
            if self.options.key_mode.value == self.options.key_mode.option_floor_master:
                dune_shark_key_name = item_name.key_gold_b1
            else:
                dune_shark_key_name = item_name.key_gold
            dune_shark_key_loc = self.multiworld.get_location(temple_location_names.b1_boss_worm_key, self.player)
            dune_shark_key_loc.place_locked_item(self.create_item(dune_shark_key_name))

        # Pyramid of Fear Bonus Keys
        if not self.options.randomize_bonus_keys.value:
            temple_bonus_keys = (
                temple_location_names.pof_1_n_5,
                temple_location_names.pof_1_ent_5,
            )
            for loc in temple_bonus_keys:
                self.multiworld.get_location(loc, self.player).place_locked_item(self.create_item(item_name.key_bonus))

        # Portal Accessibility rune keys
        if self.options.portal_accessibility.value:
            rune_key_locs: typing.List[str] = []

            def get_region_item_locs(region: str):
                # if self.options.buttonsanity.value == self.options.buttonsanity.option_shuffle:
                #     return [__loc.name for __loc in self.multiworld.get_region(region, self.player).locations
                #             if not __loc.event and not __loc.item and __loc.name not in temple_button_locations]
                # else:
                return [__loc.name for __loc in self.multiworld.get_region(region, self.player).locations
                        if not __loc.event and not __loc.item]

            # Cave Level 3 Rune Key
            c3_locs = get_region_item_locs(temple_region_names.c3_e)
            # If playing exit rando we need to ensure we can always return if falling from the temple
            if not self.options.exit_randomization.value:
                c3_locs.extend(get_region_item_locs(temple_region_names.cave_3_main))
            if len(c3_locs) == 0:
                c3_locs = [temple_location_names.cave3_trapped_guard]
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

            for _loc in rune_key_locs:
                self.multiworld.get_location(_loc, self.player).place_locked_item(
                    self.create_item(item_name.key_teleport))

    def set_rules(self) -> None:
        set_rules(self, self.door_counts)

    def generate_basic(self) -> None:
        # Shop cost setting validation, swap if max is higher than min
        if self.options.shop_cost_max.value < self.options.shop_cost_min.value:
            logging.info(f"Maximum Shop Cost Percent is lower than the minimum for player {self.player}, swapping both")
            swap = self.options.shop_cost_max.value
            self.options.shop_cost_max.value = self.options.shop_cost_min.value
            self.options.shop_cost_min.value = swap

    def pre_fill(self) -> None:
        # Fill keeps failing here and I can't think of a good way to fix it so here it will sit
        # if self.options.buttonsanity.value == self.options.buttonsanity.option_shuffle:
        #     if get_campaign(self) == Campaign.Castle:
        #         button_locations = list(castle_button_locations.keys())
        #         button_item_names = list(castle_button_table.keys())
        #     else:
        #         button_locations = list(temple_button_locations.keys())
        #         button_item_names = list(temple_button_table.keys())
        #     valid_locs = list(self.multiworld.get_unfilled_locations_for_players(button_locations, [self.player]))
        #     button_items = []
        #     for item in button_item_names:
        #         if item not in self.item_counts:
        #             continue
        #         for i in range(self.item_counts[item]):
        #             button_items.append(self.create_item(item))
        #     exclude_items = {
        #         item_name.ore
        #     }
        #     non_button_prog_items = [item for item in self.world_itempool
        #                              if item.classification & ItemClassification.progression
        #                              and item.name not in button_item_names
        #                              and item.name not in exclude_items]
        #     non_button_state = CollectionState(self.multiworld)
        #     for prog_item in non_button_prog_items:
        #         non_button_state.collect(prog_item)
        #     self.random.shuffle(valid_locs)
        #     self.random.shuffle(button_items)
        #     fill_restrictive(self.multiworld, non_button_state, valid_locs, button_items,
        #                      True, False, True, None, False, True, "Button Shuffle")

        # state = self.multiworld.get_all_state(False)
        # state.update_reachable_regions(self.player)
        # visualize_regions(self.multiworld.get_region("Menu", self.player), "_testing.puml", show_locations=False,
        #                   highlight_regions=state.reachable_regions[self.player])

        # In the castle campaign if buttonsanity is on, make the ChF12 blue wall button have a chance of a trap
        blue_button_trap_chance = 0.5
        if (get_campaign(self) == Campaign.Castle and self.options.buttonsanity > 0
                and self.random.random() > blue_button_trap_chance):
            button_loc = self.multiworld.get_location(castle_location_names.btn_c3_wall_blue, self.player)
            trap_pool = [item for item in self.multiworld.itempool if item.classification == ItemClassification.trap]
            trap_item: Item = self.random.choice(trap_pool)
            self.multiworld.itempool.remove(trap_item)
            button_loc.place_locked_item(trap_item)

    @classmethod
    def stage_post_fill(cls, multiworld: MultiWorld):
        # If buttonsanity is on for a given Hammerwatch world swap shop upgrades so the base upgrade is always first
        world_shopsanity_items: typing.Dict[int, typing.Dict[str, typing.Optional[typing.Tuple]]] = {}
        for world in multiworld.get_game_worlds("Hammerwatch"):
            assert isinstance(world, HammerwatchWorld)
            if len(get_shopsanity_classes(world)):
                world_shopsanity_items[world.player] = {}

        if len(world_shopsanity_items) == 0:
            return

        spheres = multiworld.get_spheres()
        for sphere_num, sphere in enumerate(spheres, 0):
            for loc in sphere:
                if loc.game != "Hammerwatch":  # or loc.player not in world_shopsanity_items:
                    continue
                loc_item = loc.item
                # Is this a shopsanity item that has a prerequisite or is it a root upgrade?
                if loc_item.name in item_name.shop_upgrade_prereqs:
                    item_prereq = item_name.shop_upgrade_prereqs[loc_item.name]
                    if item_prereq in world_shopsanity_items[loc_item.player]:
                        continue
                    world_shopsanity_items[loc_item.player][item_prereq] = (sphere_num, loc_item)
                elif loc_item.name in item_name.shop_upgrade_roots:
                    # If an upgrade was found earlier swap it with the base upgrade
                    if loc_item.name in world_shopsanity_items[loc_item.player]:
                        swap_data = world_shopsanity_items[loc_item.player][loc_item.name]
                        if swap_data is None:  # Should never happen but here just in case
                            continue
                        swap_sphere = swap_data[0]
                        # If the swap item and our base upgrade are located in the same sphere we don't need to swap
                        if swap_sphere == sphere_num:
                            continue
                        swap_item = swap_data[1]
                        swap_loc = swap_item.location
                        swap_loc.item = None
                        root_loc = loc_item.location
                        swap_loc.place_locked_item(loc_item)
                        root_loc.item = swap_item
                        swap_item.location = root_loc
                    else:
                        # This is the first item we found and it's already first
                        world_shopsanity_items[loc_item.player][loc_item.name] = None

    def write_spoiler(self, spoiler_handle) -> None:
        if self.options.shop_shuffle.value:
            spoiler_handle.write(f"\n\n{self.multiworld.get_player_name(self.player)}'s Shop Shuffle Locations:\n")
            for loc, shop in self.shop_locations.items():
                spoiler_handle.write(f"\n{loc}: {shop.shop_type.name} Shop")

    def interpret_slot_data(self, slot_data: typing.Dict[str, typing.Any]):
        # self.gate_types = slot_data["Gate Types"]
        return {"Gate Types": {int(gate_index): key_type for gate_index, key_type in slot_data["Gate Types"].items()},
                "er_seed": slot_data["er_seed"],
                "Random Locations": slot_data["Random Locations"],
                "Shop Locations": slot_data["Shop Locations"]}

    def get_random_location(self, rloc_name: str):
        # If UT is generating the first time we just pass a dummy value as it'll restart gen anyway
        if is_using_universal_tracker(self):
            if hasattr(self.multiworld, "re_gen_passthrough"):
                return self.multiworld.re_gen_passthrough["Hammerwatch"]["Random Locations"][rloc_name]
            return 0
        return self.random_locations[rloc_name]
