import typing

from . import HammerwatchTestBase
from .. import item_name, castle_location_names, temple_location_names, option_names
from .. import options


class TestHammerwatch(HammerwatchTestBase):
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
            "act_specific_keys": options.ActSpecificKeys.option_true,
        },
        "Castle test act-specific keys with extra keys": {
            "act_specific_keys": options.ActSpecificKeys.option_true,
            "extra_keys_percent": options.ExtraKeysPercent.range_end,
        },
        "Castle test act-specific keys with big keys": {
            "act_specific_keys": options.ActSpecificKeys.option_true,
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
    }

    def test_options(self):
        for option_set, options in TestHammerwatch.option_sets.items():
            test_world = HammerwatchTestBase()
            test_world.options = options
            test_world.world_setup()
            test_world.test_all_locations_are_active(option_set)

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

