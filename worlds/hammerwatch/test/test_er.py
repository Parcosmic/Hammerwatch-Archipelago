import typing

from . import HammerwatchTestBase
from .. import HammerwatchWorld, item_name, option_names
from .. import options, locations, items


class TestERSeedOption(HammerwatchTestBase):

    def test_er_seed_creates_consistent_connections(self):
        er_seed_options = {
            option_names.er_seed: "test_er_seed",
        }
        test_mw_1 = HammerwatchTestBase()
        test_mw_1.options = er_seed_options
        test_mw_1.world_setup()
        test_mw_2 = HammerwatchTestBase()
        test_mw_2.options = er_seed_options
        test_mw_2.world_setup()
        test_world_1: HammerwatchWorld = test_mw_1.multiworld.worlds[1]
        test_world_2: HammerwatchWorld = test_mw_2.multiworld.worlds[1]
        for exit_code, connection in test_world_1.exit_swaps.items():
            self.assertEquals(connection, test_world_2.exit_swaps[exit_code],
                              "Two worlds with the same er_seed have different ER layouts!")
