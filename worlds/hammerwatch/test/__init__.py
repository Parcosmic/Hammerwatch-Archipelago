import typing
from argparse import Namespace
from test.general import gen_steps
from worlds import AutoWorld
from worlds.AutoWorld import call_all

from test.TestBase import WorldTestBase
from BaseClasses import MultiWorld, Item
from ..Locations import all_locations


class HammerwatchTestBase(WorldTestBase):
    game = "Hammerwatch"

    def test_all_locations_are_active(self, option_set_name=None):
        if option_set_name is None:
            option_set_name = "Default option set"
        for player in self.multiworld.get_game_players("Hammerwatch"):
            # name_list = []
            remaining_locs = self.multiworld.worlds[player].active_location_list.copy()
            for region in self.multiworld.get_regions(player):
                for loc in region.locations:
                    # name_list.append(loc.name)
                    if loc.name not in all_locations.keys():
                        continue  # Don't test event locations
                    assert loc.name in remaining_locs, f"{option_set_name}: '{loc.name}' exists even though it isn't " \
                                                       f"an active location. "
                    remaining_locs.pop(loc.name)
            assert len(remaining_locs) == 0, f"{option_set_name}: The following locations are active but have not " \
                                             f"been created: {remaining_locs.keys()}"
