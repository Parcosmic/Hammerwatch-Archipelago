import typing

from . import HammerwatchTestBase
from .. import item_name, option_names
from .. import options, locations, items
from ..rules import get_unique_entrance_id
from ..util import get_active_key_names
from ..items import castle_item_counts, temple_item_counts


def _test_no_bonus_keys(self):
    self.world_setup()
    self.test_fill()
    for item in self.multiworld.itempool:
        if "Bonus Key" in item.name:
            self.assertTrue(item.location.locked,
                            "Bonus Key found in not locked location when not randomized!")


class TestCastleNoBonusVanillaKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_all_bosses,
        option_names.key_mode: options.KeyMode.option_vanilla,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
    }

    def test_no_free_bonus_keys(self):
        _test_no_bonus_keys(self)


class TestCastleNoBonusActKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_all_bosses,
        option_names.key_mode: options.KeyMode.option_act_specific,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
    }

    def test_no_free_bonus_keys(self):
        _test_no_bonus_keys(self)


class TestCastleNoBonusMasterKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_all_bosses,
        option_names.key_mode: options.KeyMode.option_floor_master,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
    }

    def test_no_free_bonus_keys(self):
        _test_no_bonus_keys(self)


class TestTempleNoBonusVanillaKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_all_bosses,
        option_names.key_mode: options.KeyMode.option_vanilla,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
    }

    def test_no_free_bonus_keys(self):
        _test_no_bonus_keys(self)


class TestTempleNoBonusActKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_all_bosses,
        option_names.key_mode: options.KeyMode.option_act_specific,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
    }

    def test_no_free_bonus_keys(self):
        _test_no_bonus_keys(self)


class TestTempleNoBonusMasterKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_all_bosses,
        option_names.key_mode: options.KeyMode.option_floor_master,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
    }

    def test_no_free_bonus_keys(self):
        _test_no_bonus_keys(self)
