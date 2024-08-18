import typing

from . import HammerwatchTestBase
from .. import item_name, option_names
from .. import options

if typing.TYPE_CHECKING:
    from .. import HammerwatchWorld


def _get_floor_master_keys_in_itempool(test: HammerwatchTestBase):
    keys_used: typing.Set[str] = set()
    for item in test.multiworld.itempool:
        if "Master" not in item.name:
            continue
        keys_used.add(item.name)
    return keys_used


def _test_no_duplicate_floor_master_keys(test: HammerwatchTestBase):
    test.world_setup()
    keys_used: typing.Set[str] = set()
    duplicate_keys = []
    for item in test.multiworld.itempool:
        if "Master" not in item.name:
            continue
        if item.name in keys_used:
            if item.name not in duplicate_keys:
                duplicate_keys.append(item.name)
            continue
        keys_used.add(item.name)
    test.assertTrue(len(duplicate_keys) == 0,
                    f"Found duplicate floor master keys in itempool: {duplicate_keys}")


def _test_no_useless_floor_master_keys(test: HammerwatchTestBase):
    test.world_setup()
    world: HammerwatchWorld = test.multiworld.worlds[1]
    existing_keys = _get_floor_master_keys_in_itempool(test)
    gate_keys: typing.Set[str] = set()
    for entr in world.multiworld.get_entrances(world.player):
        if entr.pass_item is None or entr.pass_item in gate_keys:
            continue
        if "Master" in entr.pass_item:
            gate_keys.add(entr.pass_item)
    test.assertSetEqual(existing_keys, gate_keys,
                        "Unequal number of floor master keys than what are needed by gates!")


class TestCastleFloorMasterKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_escape,
        option_names.key_mode: options.KeyMode.option_floor_master,
    }

    def test_no_duplicate_floor_master_keys(self):
        _test_no_duplicate_floor_master_keys(self)

    def test_no_duplicate_floor_master_keys_start_inventory(self):
        self.options.update({
            "start_inventory": {item_name.key_bronze_prison_1: 1}
        })
        _test_no_duplicate_floor_master_keys(self)

    def test_no_useless_floor_master_keys(self):
        _test_no_useless_floor_master_keys(self)

    def test_no_useless_floor_master_keys_gate_shuffle(self):
        self.options.update({
            option_names.gate_shuffle: options.GateShuffle.option_true
        })
        _test_no_useless_floor_master_keys(self)


class TestTempleFloorMasterKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_all_bosses,
        option_names.key_mode: options.KeyMode.option_floor_master,
    }

    def test_no_duplicate_floor_master_keys(self):
        _test_no_duplicate_floor_master_keys(self)

    def test_no_duplicate_floor_master_keys_start_inventory(self):
        self.options.update({
            "start_inventory": {item_name.key_gold_b1: 1}
        })
        _test_no_duplicate_floor_master_keys(self)

    def test_no_useless_floor_master_keys(self):
        _test_no_useless_floor_master_keys(self)

    def test_no_useless_floor_master_keys_gate_shuffle(self):
        self.options.update({
            option_names.gate_shuffle: options.GateShuffle.option_true
        })
        _test_no_useless_floor_master_keys(self)


class TestCastleMasterBonusKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_escape,
        option_names.key_mode: options.KeyMode.option_floor_master,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
    }

    def test_no_bonus_floor_master_keys_exist_in_pool(self):
        self.world_setup()
        for item in self.multiworld.itempool:
            self.assertFalse(item.name.endswith("Master Bonus Key"),
                             f"{item.name} exists in itempool when only bonus act keys should!")

