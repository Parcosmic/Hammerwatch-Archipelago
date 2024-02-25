import typing

from . import HammerwatchTestBase
from .. import item_name, option_names
from .. import options, locations, items
from ..rules import get_unique_entrance_id
from ..util import get_active_key_names
from ..items import castle_item_counts, temple_item_counts


def _test_gate_keys(self):
    self.world_setup()
    world = self.multiworld.worlds[1]
    active_keys = get_active_key_names(world)
    if self.options[option_names.goal] < options.Goal.option_temple_all_bosses:
        item_counts = castle_item_counts
    else:
        item_counts = temple_item_counts
        active_keys.remove(item_name.key_teleport)
    gate_key_counts = {key_name: item_counts[key_name] if key_name in item_counts else 1 for key_name in active_keys}
    gate_counts = {key_name: 0 for key_name in gate_key_counts.keys()}
    seen_gate_entr_ids = {key_name: [] for key_name in gate_key_counts.keys()}
    for entr in world.multiworld.get_entrances(world.player):
        entr_id = get_unique_entrance_id(entr)
        if entr.pass_item in gate_key_counts.keys() and entr_id not in seen_gate_entr_ids[entr.pass_item]:
            gate_counts[entr.pass_item] += entr.item_count
            seen_gate_entr_ids[entr.pass_item].append(entr_id)
    for key_name in gate_key_counts.keys():
        # if gate_counts[key_name] != gate_key_counts[key_name]:
        #     print(seen_gate_entr_ids)
        self.assertTrue(gate_counts[key_name] == gate_key_counts[key_name],
                        f"World has incorrect number of gates of type \"{key_name}\""
                        f" (found {gate_counts[key_name]}, expected {gate_key_counts[key_name]})")


class TestCastleGateKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_all_bosses,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_true,
    }

    def test_keys(self):
        self.options[option_names.key_mode] = options.KeyMode.option_vanilla
        _test_gate_keys(self)

    def test_act_keys(self):
        self.options[option_names.key_mode] = options.KeyMode.option_act_specific
        _test_gate_keys(self)

    def test_buttonsanity(self):
        self.options[option_names.key_mode] = options.KeyMode.option_vanilla
        self.options[option_names.buttonsanity] = options.Buttonsanity.option_normal
        _test_gate_keys(self)


class TestTempleGateKeys(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_all_bosses,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_true,
    }

    def test_keys(self):
        self.options[option_names.key_mode] = options.KeyMode.option_vanilla
        _test_gate_keys(self)

    def test_act_keys(self):
        self.options[option_names.key_mode] = options.KeyMode.option_act_specific
        _test_gate_keys(self)

    def test_buttonsanity(self):
        self.options[option_names.key_mode] = options.KeyMode.option_vanilla
        self.options[option_names.buttonsanity] = options.Buttonsanity.option_normal
        _test_gate_keys(self)
