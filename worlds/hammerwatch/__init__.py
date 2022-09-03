import os
import typing

from Items import HammerwatchItem, ItemData, item_table, junk_table, get_item_counts
from Locations import HammerwatchLocation, setup_locations, all_locations
from Regions import create_regions
from Rules import set_rules

from Names import ItemName, LocationName

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
    remote_start_inventory: bool = False

    data_version = 0

    web = HammerwatchWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = all_locations

    active_location_list: typing.Dict[str, int]

    def _get_slot_data(self):
        return {
            "active_levels": self.active_location_list,
        }

    def fill_slot_data(self) -> dict:
        slot_data = self._get_slot_data()
        for option_name in hammerwatch_options:
            option = getattr(self.world, option_name)[self.player]
            slot_data[option_name] = option.value

        return slot_data

    def generate_basic(self) -> None:
        self.active_location_list = setup_locations(self.world, self.player)

        self.world.get_location(LocationName.victory, self.player)\
            .place_locked_item(self.create_event(ItemName.victory))
        self.world.completion_condition[self.player] = lambda state: state.has(ItemName.victory, self.player)

    def create_regions(self) -> None:
        locations = setup_locations(self.world, self.player)
        create_regions(self.world, self.player, locations)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return HammerwatchItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str):
        return HammerwatchItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        item_names: typing.List[str] = []
        itempool: typing.List[Item] = []

        # Get the total number of locations we need to fill
        total_required_locations = 39
        if self.world.randomize_recovery_items[self.player].value:
            total_required_locations += 2

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
        for item_name in self.world.random.choices(list(junk_table.keys()), k=junk):
            junk_pool += [self.create_item(item_name)]

        itempool += junk_pool

        self.world.itempool += itempool

    def set_rules(self) -> None:
        set_rules(self.world, self.player)
