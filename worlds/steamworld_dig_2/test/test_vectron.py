from .test import SWD2TestBase
from ..names import option_name, item_name, location_name
from ..options import SkipVectron, RandomizeOres

class TestNoSkipVectronWithOreRando(SWD2TestBase):
    options = {
        option_name.skip_vectron: SkipVectron.option_false,
        option_name.randomize_ores: RandomizeOres.option_true
    }

    def test_vectron_items_and_locations_exist_in_pool(self) -> None:
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_1)), 1)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_2)), 1)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_3)), 1)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_4)), 1)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_5)), 1)
        vectron_locs = [
            location_name.v_ore_1,
            location_name.v_ore_2,
            location_name.v_ore_3,
            location_name.v_ore_4,
            location_name.v_ore_5,
        ]
        for vectron_loc in vectron_locs:
            try:
                self.world.get_location(vectron_loc)
            except KeyError:
                self.fail(f"{vectron_loc} doesn't exist when it should!")


class TestSkipVectronWithNoOreRando(SWD2TestBase):
    options = {
        option_name.skip_vectron: SkipVectron.option_true,
        option_name.randomize_ores: RandomizeOres.option_false
    }

    run_default_tests = False  # These options are default, so skip running the default tests on this case

    def test_vectron_items_and_locations_do_not_exist_in_pool(self) -> None:
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_1)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_2)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_3)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_4)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_5)), 0)
        vectron_locs = [
            location_name.v_ore_1,
            location_name.v_ore_2,
            location_name.v_ore_3,
            location_name.v_ore_4,
            location_name.v_ore_5,
        ]
        for vectron_loc in vectron_locs:
            self.assertRaises(KeyError, self.world.get_location, vectron_loc)


class TestNoSkipVectronWithNoOreRando(SWD2TestBase):
    options = {
        option_name.skip_vectron: SkipVectron.option_false,
        option_name.randomize_ores: RandomizeOres.option_false
    }

    def test_vectron_items_and_locations_do_not_exist_in_pool(self) -> None:
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_1)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_2)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_3)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_4)), 0)
        self.assertEqual(len(self.get_items_by_name(item_name.vectron_ore_5)), 0)
        vectron_locs = [
            location_name.v_ore_1,
            location_name.v_ore_2,
            location_name.v_ore_3,
            location_name.v_ore_4,
            location_name.v_ore_5,
        ]
        for vectron_loc in vectron_locs:
            self.assertRaises(KeyError, self.world.get_location, vectron_loc)