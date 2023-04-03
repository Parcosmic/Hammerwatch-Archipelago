import typing

from . import HammerwatchTestBase
from .. import ItemName, CastleLocationNames, TempleLocationNames
from .. import Options


class TestHammerwatch(HammerwatchTestBase):
    option_sets: typing.Dict[str, typing.Dict[str, typing.Any]] = {
        "Castle max locations": {
            "goal": Options.Goal.option_castle_escape,
            "bonus_behavior": Options.BonusChestLocationBehavior.option_all,
            "randomize_bonus_keys": Options.RandomizeBonusKeys.option_true,
            "randomize_recovery_items": Options.RandomizeRecoveryItems.option_true,
            "randomize_secrets": Options.RandomizeSecrets.option_true,
            "randomize_puzzles": Options.RandomizePuzzles.option_true,
            "randomize_enemy_loot": Options.RandomizeEnemyLoot.option_true,
            "shortcut_teleporter": Options.ShortcutTeleporter.option_true,
        },
        "Temple max locations": {
            "goal": Options.Goal.option_temple_kill_sharand,
            "bonus_behavior": Options.BonusChestLocationBehavior.option_all,
            "randomize_bonus_keys": Options.RandomizeBonusKeys.option_true,
            "randomize_recovery_items": Options.RandomizeRecoveryItems.option_true,
            "randomize_secrets": Options.RandomizeSecrets.option_true,
            "randomize_puzzles": Options.RandomizePuzzles.option_true,
            "randomize_enemy_loot": Options.RandomizeEnemyLoot.option_true,
        },
        "Castle min locations": {
            "goal": Options.Goal.option_castle_plank_hunt,
            "bonus_behavior": Options.BonusChestLocationBehavior.option_none,
            "randomize_bonus_keys": Options.RandomizeBonusKeys.option_false,
            "randomize_recovery_items": Options.RandomizeRecoveryItems.option_false,
            "randomize_secrets": Options.RandomizeSecrets.option_false,
            "randomize_puzzles": Options.RandomizePuzzles.option_false,
            "randomize_enemy_loot": Options.RandomizeEnemyLoot.option_false,
        },
        "Temple min locations": {
            "goal": Options.Goal.option_temple_plank_hunt,
            "bonus_behavior": Options.BonusChestLocationBehavior.option_none,
            "randomize_bonus_keys": Options.RandomizeBonusKeys.option_false,
            "randomize_recovery_items": Options.RandomizeRecoveryItems.option_false,
            "randomize_secrets": Options.RandomizeSecrets.option_false,
            "randomize_puzzles": Options.RandomizePuzzles.option_false,
            "randomize_enemy_loot": Options.RandomizeEnemyLoot.option_false,
        },
        "Castle kill final boss goal": {
            "goal": Options.Goal.option_castle_kill_dragon,
        },
        "Temple complete Pyramid of Fear": {
            "goal": Options.Goal.option_temple_pyramid_of_fear,
        },
    }

    def testOptions(self):
        for option_set, options in TestHammerwatch.option_sets.items():
            test_world = HammerwatchTestBase()
            test_world.options = options
            test_world.world_setup()
            test_world.test_all_locations_are_active(option_set)

    def testPlankHuntDefault(self):
        default_plank_hunt_options = {
            "goal": Options.Goal.option_castle_plank_hunt,
        }
        default_plank_hunt_test = HammerwatchTestBase()
        default_plank_hunt_test.options = default_plank_hunt_options
        default_plank_hunt_test.world_setup()
        default_plank_hunt_test.assertAccessDependency([CastleLocationNames.ev_victory], [[ItemName.plank] * 12])

    def testPlankHuntDouble(self):
        double_planks_options = {
            "goal": Options.Goal.option_castle_plank_hunt,
            "plank_count": 24,
            "planks_required_count": 24,
        }
        double_planks_test = HammerwatchTestBase()
        double_planks_test.options = double_planks_options
        double_planks_test.world_setup()
        double_planks_test.assertAccessDependency([CastleLocationNames.ev_victory], [[ItemName.plank] * 24])

    def testPlankHuntNotEnough(self):
        not_enough_planks_options = {
            "goal": Options.Goal.option_castle_plank_hunt,
            "plank_count": 6,
            "planks_required_count": 24,
        }
        not_enough_planks_test = HammerwatchTestBase()
        not_enough_planks_test.options = not_enough_planks_options
        not_enough_planks_test.world_setup()
        not_enough_planks_test.assertAccessDependency([CastleLocationNames.ev_victory], [[ItemName.plank] * 24])

    def testPlankHuntExtra(self):
        extra_planks_options = {
            "goal": Options.Goal.option_castle_plank_hunt,
            "plank_count": 24,
            "planks_required_count": 12,
        }
        extra_planks_test = HammerwatchTestBase()
        extra_planks_test.options = extra_planks_options
        extra_planks_test.world_setup()
        extra_planks_test.assertAccessDependency([CastleLocationNames.ev_victory], [[ItemName.plank] * 12])

