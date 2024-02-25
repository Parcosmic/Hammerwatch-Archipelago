import typing

from . import HammerwatchTestBase
from .. import item_name, option_names
from .. import options, locations, items


class TestPlankGoal(HammerwatchTestBase):

    def test_plank_hunt_default(self):
        default_plank_hunt_options = {
            "goal": options.Goal.option_castle_plank_hunt,
        }
        default_plank_hunt_test = HammerwatchTestBase()
        default_plank_hunt_test.options = default_plank_hunt_options
        default_plank_hunt_test.world_setup()
        default_plank_hunt_test.assertBeatable(False)
        default_plank_hunt_test.collect_by_name([item_name.plank] * 12)
        default_plank_hunt_test.assertBeatable(True)
        # default_plank_hunt_test.assertAccessDependency([castle_location_names.ev_victory], [[item_name.plank] * 12])

    def test_plank_hunt_double(self):
        double_planks_options = {
            "goal": options.Goal.option_castle_plank_hunt,
            "plank_count": 24,
            "planks_required_count": 24,
        }
        double_planks_test = HammerwatchTestBase()
        double_planks_test.options = double_planks_options
        double_planks_test.world_setup()
        double_planks_test.assertBeatable(False)
        double_planks_test.collect_by_name([item_name.plank] * 24)
        double_planks_test.assertBeatable(True)

    def test_plank_hunt_not_enough(self):
        not_enough_planks_options = {
            "goal": options.Goal.option_castle_plank_hunt,
            "plank_count": 6,
            "planks_required_count": 24,
        }
        not_enough_planks_test = HammerwatchTestBase()
        not_enough_planks_test.options = not_enough_planks_options
        not_enough_planks_test.world_setup()
        not_enough_planks_test.assertBeatable(False)
        not_enough_planks_test.collect_by_name([item_name.plank] * 24)
        not_enough_planks_test.assertBeatable(True)

    def test_plank_hunt_extra(self):
        extra_planks_options = {
            "goal": options.Goal.option_castle_plank_hunt,
            "plank_count": 24,
            "planks_required_count": 12,
        }
        extra_planks_test = HammerwatchTestBase()
        extra_planks_test.options = extra_planks_options
        extra_planks_test.world_setup()
        extra_planks_test.assertBeatable(False)
        extra_planks_test.collect_by_name([item_name.plank] * 12)
        extra_planks_test.assertBeatable(True)


class TestHammerwatchOptions(HammerwatchTestBase):
    option_sets: typing.Dict[str, typing.Dict[str, typing.Any]] = {
        "Castle max locations": {
            "goal": options.Goal.option_castle_escape,
            "bonus_behavior": options.BonusChestLocationBehavior.option_all,
            "randomize_bonus_keys": options.RandomizeBonusKeys.option_true,
            "randomize_recovery_items": options.RandomizeRecoveryItems.option_true,
            "randomize_secrets": options.RandomizeSecrets.option_true,
            "randomize_puzzles": options.RandomizePuzzles.option_true,
            "randomize_enemy_loot": options.RandomizeEnemyLoot.option_true,
            "extra_keys_percent": options.ExtraKeysPercent.range_end,
            "big_bronze_key_percent": options.BigBronzeKeyPercent.range_start,
            "shortcut_teleporter": options.ShortcutTeleporter.option_true,
        },
        "Temple max locations": {
            "goal": options.Goal.option_temple_all_bosses,
            "bonus_behavior": options.BonusChestLocationBehavior.option_all,
            "randomize_bonus_keys": options.RandomizeBonusKeys.option_true,
            "randomize_recovery_items": options.RandomizeRecoveryItems.option_true,
            "randomize_secrets": options.RandomizeSecrets.option_true,
            "randomize_puzzles": options.RandomizePuzzles.option_true,
            "randomize_enemy_loot": options.RandomizeEnemyLoot.option_true,
            "extra_keys_percent": options.ExtraKeysPercent.range_end,
            "big_bronze_key_percent": options.BigBronzeKeyPercent.range_start,
        },
        "Castle min locations": {
            "goal": options.Goal.option_castle_plank_hunt,
            "bonus_behavior": options.BonusChestLocationBehavior.option_none,
            "randomize_bonus_keys": options.RandomizeBonusKeys.option_false,
            "randomize_recovery_items": options.RandomizeRecoveryItems.option_false,
            "randomize_secrets": options.RandomizeSecrets.option_false,
            "randomize_puzzles": options.RandomizePuzzles.option_false,
            "randomize_enemy_loot": options.RandomizeEnemyLoot.option_false,
            "extra_keys_percent": options.ExtraKeysPercent.range_start,
            "shortcut_teleporter": options.ShortcutTeleporter.option_false,
        },
        "Temple min locations": {
            "goal": options.Goal.option_temple_plank_hunt,
            "bonus_behavior": options.BonusChestLocationBehavior.option_none,
            "randomize_bonus_keys": options.RandomizeBonusKeys.option_false,
            "randomize_recovery_items": options.RandomizeRecoveryItems.option_false,
            "randomize_secrets": options.RandomizeSecrets.option_false,
            "randomize_puzzles": options.RandomizePuzzles.option_false,
            "randomize_enemy_loot": options.RandomizeEnemyLoot.option_false,
            "extra_keys_percent": options.ExtraKeysPercent.range_start,
        },
        "Castle kill bosses goal": {
            "goal": options.Goal.option_castle_all_bosses,
        },
        "Temple complete Pyramid of Fear": {
            "goal": options.Goal.option_temple_pyramid_of_fear,
        },
        "Castle test act-specific keys": {
            option_names.key_mode: options.KeyMode.option_act_specific,
        },
        "Castle test act-specific keys with extra keys": {
            option_names.key_mode: options.KeyMode.option_act_specific,
            "extra_keys_percent": options.ExtraKeysPercent.range_end,
        },
        "Castle test act-specific keys with big keys": {
            option_names.key_mode: options.KeyMode.option_act_specific,
            "big_bronze_key_percent": options.BigBronzeKeyPercent.range_end,
        },
        "Full act range castle exit rando": {
            "exit_randomization": options.ExitRandomization.option_all,
            option_names.er_act_range: options.ERActRange.range_end,
        },
        "Full act range temple exit rando": {
            "goal": options.Goal.option_temple_all_bosses,
            "exit_randomization": options.ExitRandomization.option_all,
            option_names.er_act_range: options.ERActRange.range_end,
        },
        "Basic castle exit rando": {
            "exit_randomization": options.ExitRandomization.option_all,
        },
        "Basic temple exit rando": {
            "goal": options.Goal.option_temple_all_bosses,
            "exit_randomization": options.ExitRandomization.option_all,
        },
        "Castle exit rando with start randomized": {
            "exit_randomization": options.ExitRandomization.option_all,
            option_names.random_start_exit: options.StartExit.option_true,
        },
        "Temple exit rando with start randomized": {
            "goal": options.Goal.option_temple_all_bosses,
            "exit_randomization": options.ExitRandomization.option_all,
            option_names.random_start_exit: options.StartExit.option_true,
        },
        "Castle Floor Master Keys": {
            option_names.key_mode: options.KeyMode.option_floor_master,
        },
        "Temple Floor Master Keys": {
            option_names.goal: options.Goal.option_temple_all_bosses,
            option_names.key_mode: options.KeyMode.option_floor_master,
        },
        "Castle buttonsanity": {
            option_names.buttonsanity: options.Buttonsanity.option_normal,
        },
        "Castle buttonsanity insanity": {
            option_names.buttonsanity: options.Buttonsanity.option_insanity,
        },
        "Castle buttonsanity with exit randomization and random start": {
            option_names.buttonsanity: options.Buttonsanity.option_normal,
            option_names.exit_randomization: options.ExitRandomization.option_all,
            option_names.random_start_exit: options.StartExit.option_true,
        },
        "Temple buttonsanity": {
            option_names.goal: options.Goal.option_temple_all_bosses,
            option_names.buttonsanity: options.Buttonsanity.option_normal,
        },
        "Temple buttonsanity insanity": {
            option_names.goal: options.Goal.option_temple_all_bosses,
            option_names.buttonsanity: options.Buttonsanity.option_insanity,
        },
        "Temple buttonsanity with exit randomization and random start": {
            option_names.goal: options.Goal.option_temple_all_bosses,
            option_names.buttonsanity: options.Buttonsanity.option_normal,
            option_names.exit_randomization: options.ExitRandomization.option_all,
            option_names.random_start_exit: options.StartExit.option_true,
        },
    }

    def test_options(self):
        for option_set, options_ in TestHammerwatchOptions.option_sets.items():
            with self.subTest(option_set):
                test_world = HammerwatchTestBase()
                test_world.options = options_
                test_world.world_setup()
                test_world.test_all_locations_are_active(option_set)


class TestCastleButtonsanityOff(HammerwatchTestBase):
    options = {
        option_names.buttonsanity: options.Buttonsanity.option_off,
    }

    def test_castle_no_button_items_in_non_button_locations(self):
        self.test_fill()

        for location in self.multiworld.get_locations(1):
            if location.name not in locations.all_locations:
                continue
            loc_type = locations.all_locations[location.name].classification
            if (loc_type == locations.LocationClassification.Button
                    or loc_type == locations.LocationClassification.Buttoninsanity):
                self.assertTrue(location.item.name in items.castle_button_table)


class TestTempleButtonsanityOff(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_all_bosses,
        option_names.buttonsanity: options.Buttonsanity.option_off,
    }

    def test_temple_no_button_items_in_non_button_locations(self):
        self.test_fill()

        for location in self.multiworld.get_locations(1):
            if location.name not in locations.all_locations:
                continue
            loc_type = locations.all_locations[location.name].classification
            if (loc_type == locations.LocationClassification.Button
                    or loc_type == locations.LocationClassification.Buttoninsanity):
                self.assertTrue(location.item.name in items.temple_button_table)
            else:
                self.assertFalse(location.item.name in items.temple_button_table)


class TestGameModifiers(HammerwatchTestBase):
    options = {
        option_names.game_modifiers: {
             option_names.mod_infinite_lives: True,
             option_names.mod_hp_regen: True,
             option_names.mod_1_hp: True,
             option_names.mod_no_extra_lives: True,
             option_names.mod_double_lives: True,
             option_names.mod_double_damage: False,
        }
    }

    def test_disable_correct_modifiers(self):
        # noinspection PyTypeChecker
        world_options: options.HammerwatchOptions = self.multiworld.worlds[1].options

        self.assertTrue(world_options.game_modifiers.value[option_names.mod_infinite_lives],
                        "The game modifier \"infinite lives\" should be True")
        self.assertTrue(world_options.game_modifiers.value[option_names.mod_hp_regen],
                        "The game modifier \"hp regen\" should be True")
        self.assertFalse(world_options.game_modifiers.value[option_names.mod_1_hp],
                         "The game modifier \"1 hp\" should be changed to False")
        self.assertFalse(world_options.game_modifiers.value[option_names.mod_no_extra_lives],
                         "The game modifier \"no extra lives\" should be changed to False")
        self.assertFalse(world_options.game_modifiers.value[option_names.mod_double_lives],
                         "The game modifier \"double lives\" should be changed to False")
        self.assertFalse(world_options.game_modifiers.value[option_names.mod_double_damage],
                         "The game modifier \"double damage\" should not be changed from False")


class TestTrapItems(HammerwatchTestBase):
    options = {
        option_names.trap_item_percent: 100,
    }

    def test_no_filler_if_all_trap_items(self):
        filler_items = [item for item in self.multiworld.itempool if item.classification == item.classification.filler]
        self.assertEquals(len(filler_items), 0,
                          f"Filler items found when {option_names.trap_item_percent} is 100%!")
