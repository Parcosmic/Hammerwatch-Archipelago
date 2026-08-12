import logging
from typing import ClassVar, Dict, List, Set, Any

from .names import item_name, location_name, region_name, const, entrance_name
from .items import SWD2Item, item_table, filler_items, trap_items, active_filler_items
from .locations import LocationData, all_locations, setup_locations, artifact_locations
from .regions import create_and_connect_regions, SWD2Entrance, ExitData, get_etr_name, region_data, REGIONS
from .rules import set_rules
from .util import is_using_universal_tracker, get_random_element, get_random_elements, get_goal_type, GoalType
from .options import SWD2Options, client_required_options, option_groups, option_presets
from settings import Group, FilePath

from BaseClasses import Item, Tutorial, ItemClassification, CollectionState
from ..AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type, launch_subprocess, icon_paths


def launch_client() -> None:
    from .client import launch
    launch_subprocess(launch, name="SteamWorldDig2Client")


components.append(
    Component(
        "SteamWorld Dig 2 Client",
        "SteamWorldDig2Client",
        icon=const.game,
        component_type=Type.CLIENT,
        func=launch_client,
        game_name=const.game,
    )
)

icon_paths[const.game] = f"ap:{__name__}/assets/component_icon.png"


class SWD2Settings(Group):
    class GamePath(FilePath):
        description = "SteamWorld Dig 2 executable"

    game_path: GamePath = GamePath("Dig2.exe")


class SWD2Web(WebWorld):
    theme = "stone"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the SteamWorld Dig 2 randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Parcosmic"]
    )]

    option_groups = option_groups
    options_presets = option_presets


class SWD2World(World):
    """
    Dig deep, gain riches and unearth the terrors of the underworld in this platform mining adventure influenced by
    classic Metroidvania style games.
    """
    game = const.game
    options_dataclass = SWD2Options
    options: SWD2Options
    settings_key = "steamworld_dig_2_settings"
    settings: ClassVar[SWD2Settings]
    topology_present: bool = True
    remote_start_inventory: bool = True

    web = SWD2Web()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    item_name_groups = item_name.item_groups
    # location_name_groups = location_groups.location_groups

    active_location_list: Set[str]
    excluded_loc_ids: Set[int]
    item_counts: Dict[str, int]
    world_itempool: List[Item]
    swapped_entrances: List[ExitData]
    swapped_doors: Dict[str, str]

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            **self.options.as_dict(*client_required_options),
            "APWorld Version": const.apworld_version,
            "Client Mod Version": const.hw_client_version,
            "Entrance Swaps": {entrance_name.DOORS.index(vanilla_door): entrance_name.DOORS.index(new_door)
                               for vanilla_door, new_door in self.swapped_doors.items()},
        }

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        state_changed = super().collect(state, item)
        if state_changed and item.name in item_name.artifacts_set:
            state.add_item(item_name.artifacts_name, self.player, 1)
        return state_changed

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        state_changed = super().remove(state, item)
        if state_changed and item.name in item_name.artifacts_set:
            state.remove_item(item_name.artifacts_name, self.player, 1)
        return state_changed

    def generate_early(self):
        # Validate options
        if self.options.start_with_portal:
            self.options.start_inventory.value[item_name.up_bag_portal] = 1

    def create_regions(self) -> None:
        self.active_location_list, event_locations, self.item_counts = setup_locations(self)
        create_and_connect_regions(self, self.active_location_list, event_locations)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return SWD2Item(name, data.classification, data.code, self.player)

    def create_item_with_flags(self, name: str, classification: ItemClassification) -> Item:
        data = item_table[name]
        return SWD2Item(name, classification, data.code, self.player)

    def create_event(self, event: str):
        return SWD2Item(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        self.world_itempool = []

        self.place_locked_items()

        unfilled = self.multiworld.get_unfilled_locations(self.player)
        total_required_locations = len(unfilled)

        # Remove progression items if the player starts with them
        for precollected in self.multiworld.precollected_items[self.player]:
            if precollected.classification & ItemClassification.progression:
                if precollected.name in self.item_counts and self.item_counts[precollected.name] > 0:
                    self.item_counts[precollected.name] -= 1

        item_counts = self.item_counts

        # Add items
        total_items = 0
        present_filler_item_counts = {}
        for item in item_counts:
            total_items += item_counts[item]
            if item_table[item].classification == ItemClassification.filler and item_counts[item] > 0:
                present_filler_item_counts[item] = item_counts[item]

        # Add/remove junk items depending if we have not enough/too many locations
        junk: int = total_required_locations - total_items
        if junk > 0:
            if len(present_filler_item_counts) > 0:
                for junk_name in get_random_elements(self, present_filler_item_counts, junk):
                    item_counts[junk_name] += 1
            else:
                filler_item = self.get_filler_item_name()
                if filler_item not in item_counts:
                    item_counts[filler_item] = 0
                item_counts[filler_item] += junk
        else:
            while junk < 0:
                junk += 1
                junk_item = get_random_element(self, present_filler_item_counts)
                item_counts[junk_item] -= 1
                present_filler_item_counts[junk_item] -= 1
                if item_counts[junk_item] == 0:
                    present_filler_item_counts.pop(junk_item)
                    if len(present_filler_item_counts) == 0:
                        break
            # Remove trap items if we've run out of filler
            present_trap_item_counts = {trap_item: item_counts[trap_item] for trap_item in trap_items if trap_item in item_counts}
            while junk < 0:
                junk += 1
                trap_item = get_random_element(self, present_trap_item_counts)
                item_counts[trap_item] -= 1
                present_trap_item_counts[trap_item] -= 1
                if item_counts[trap_item] == 0:
                    present_trap_item_counts.pop(trap_item)
                    if len(present_trap_item_counts) == 0:
                        logging.warning(f"SWD2World for player {self.multiworld.player_name[self.player]} "
                                        f"(slot {self.player}) ran out of filler and trap items to remove. Some items "
                                        f"will remain unplaced!")
                        break

        # Create items and add to item pool
        for item in item_counts:
            for i in range(item_counts[item]):
                self.world_itempool.append(self.create_item(item))

        self.multiworld.itempool += self.world_itempool

    def get_filler_item_name(self) -> str:
        return self.random.choice(tuple(active_filler_items))

    def place_locked_items(self):
        events = {
            location_name.ev_totd_treasure_brazier_top: item_name.ev_totd_treasure_brazier,
            location_name.ev_totd_treasure_brazier_right: item_name.ev_totd_treasure_brazier,
            location_name.ev_totd_treasure_brazier_left: item_name.ev_totd_treasure_brazier,
            location_name.ev_tog_cistern_button_l: item_name.ev_tog_cistern_button,
            location_name.ev_tog_cistern_button_r: item_name.ev_tog_cistern_button,
            location_name.ev_device_of_doom: item_name.ev_dampener_destroyed,
            location_name.ev_device_of_destruction: item_name.ev_dampener_destroyed,
            location_name.ev_device_of_devastation: item_name.ev_dampener_destroyed,
            location_name.ev_device_of_disaster: item_name.ev_dampener_destroyed,
            location_name.ev_defeat_rosie: item_name.ev_blastoff,
        }

        if not self.options.randomize_artifacts:
            artifact_locs = dict(zip(artifact_locations, item_name.artifacts))
            artifact_locs.pop(location_name.c_hell_end)
            events.update(artifact_locs)

        for loc, itm in events.items():
            location = self.multiworld.get_location(loc, self.player)
            location.place_locked_item(self.create_event(itm))

    def set_rules(self) -> None:
        set_rules(self)

    def generate_basic(self) -> None:
        # all_state = self.multiworld.get_all_state(False)
        # reg = all_state.reachable_regions[self.player]
        # visualize_regions(self.multiworld.get_region(region_name.menu, self.player), "test.puml",
        #                   highlight_regions=reg)
        pass

    def pre_fill(self) -> None:
        pass

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        swapped_regions = {}
        for swapped_entrance in self.swapped_entrances:
            swapped_regions[swapped_entrance.target_region.name] = swapped_entrance.connected_region.name

        hint_extensions: Dict[int, str] = {}
        for loc_name in self.active_location_list:
            location = self.multiworld.get_location(loc_name, self.player)
            loc_region = location.parent_region

            if loc_region.name not in swapped_regions:
                continue

            loc_id = all_locations[loc_name].code
            hint_extensions[loc_id] = swapped_regions[loc_region.name]

    def write_spoiler(self, spoiler_handle) -> None:
        pass

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data
