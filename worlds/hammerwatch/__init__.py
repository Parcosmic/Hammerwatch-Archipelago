import os
import typing

from .Items import HammerwatchItem, ItemData, item_table, junk_items, trap_items, get_item_counts
from .Locations import *
from .Regions import create_regions
from .Rules import set_rules

from .Names import ItemName, LocationName

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
    remote_items: bool = False
    remote_start_inventory: bool = True

    data_version = 0

    web = HammerwatchWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    active_location_list: typing.Dict[str, LocationData]

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        slot_data: typing.Dict[str, object] = {}
        for option_name in self.option_definitions:
            option = getattr(self.world, option_name)[self.player]
            slot_data[option_name] = option.value
        for loc, value in random_locations.items():
            slot_data[loc] = value
        return slot_data

    def generate_early(self):
        self.active_location_list = setup_locations(self.world, self.player)

    def generate_basic(self) -> None:
        self.world.get_location(LocationName.ev_victory, self.player)\
            .place_locked_item(self.create_event(ItemName.victory))
        self.world.completion_condition[self.player] = lambda state: state.has(ItemName.victory, self.player)

        if self.world.map[self.player] == 0:
            pass
        else:
            self.place_tots_event_items()

    def create_regions(self) -> None:
        create_regions(self.world, self.player, self.active_location_list)

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
        if self.world.map[self.player] == 0:
            total_required_locations -= len(castle_event_locations)
        else:
            total_required_locations -= len(temple_event_locations)

        if not self.world.randomize_recovery_items[self.player].value:
            recovery_locations = 0
            for location, data in self.active_location_list.items():
                if data.classification == LocationClassification.Recovery:
                    recovery_locations += 1
            total_required_locations -= recovery_locations
        total_required_locations += self.world.consumable_merchant_checks[self.player].value

        # Get the counts of each item we'll put in
        item_counts: typing.Dict[str, int] = get_item_counts(self.world, self.player)

        # Add items
        for item in item_table:
            if item in item_counts:
                item_names += [item] * item_counts[item]

        # Exclude items if the player starts with them
        exclude = [item for item in self.world.precollected_items[self.player]]
        for item in map(self.create_item, item_names):
            if item in exclude:
                exclude.remove(item)
            else:
                itempool.append(item)

        # Add junk items if there aren't enough items to fill the locations
        junk: int = total_required_locations - len(itempool)
        junk_pool: typing.List[Item] = []
        for item_name in self.world.random.choices(junk_items, k=junk):
            junk_pool += [self.create_item(item_name)]

        itempool += junk_pool

        self.world.itempool += itempool

    def place_tots_event_items(self):
        self.world.get_location(LocationName.ev_temple_entrance_rock, self.player) \
            .place_locked_item(self.create_event(ItemName.open_temple_entrance_shortcut))

        # Pyramid of fear
        self.world.get_location(LocationName.ev_hub_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.ev_cave1_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.ev_cave2_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.ev_cave3_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.ev_temple1_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.ev_temple2_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))

        self.world.get_location(LocationName.ev_pof_end, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_complete))

        # Krilith defeated
        self.world.get_location(LocationName.ev_krilith_defeated, self.player) \
            .place_locked_item(self.create_event(ItemName.krilith_defeated))

        # Temple Floor 2 light bridge switches
        self.world.get_location(LocationName.ev_t2_n_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.t2_bridge_switch))
        self.world.get_location(LocationName.ev_t2_w_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.t2_bridge_switch))
        self.world.get_location(LocationName.ev_t2_ne_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.t2_bridge_switch))
        self.world.get_location(LocationName.ev_t2_se_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.t2_bridge_switch))
        self.world.get_location(LocationName.ev_t2_sw_bridge_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.t2_bridge_switch))

        # Temple solar nodes
        self.world.get_location(LocationName.ev_t1_n_node, self.player) \
            .place_locked_item(self.create_event(ItemName.solar_node))
        self.world.get_location(LocationName.ev_t1_s_node, self.player) \
            .place_locked_item(self.create_event(ItemName.solar_node))
        self.world.get_location(LocationName.ev_t2_n_node, self.player) \
            .place_locked_item(self.create_event(ItemName.solar_node))
        self.world.get_location(LocationName.ev_t2_s_node, self.player) \
            .place_locked_item(self.create_event(ItemName.solar_node))
        self.world.get_location(LocationName.ev_t3_n_node, self.player) \
            .place_locked_item(self.create_event(ItemName.solar_node))
        self.world.get_location(LocationName.ev_t3_s_node, self.player) \
            .place_locked_item(self.create_event(ItemName.solar_node))

    def set_rules(self) -> None:
        set_rules(self.world, self.player)
