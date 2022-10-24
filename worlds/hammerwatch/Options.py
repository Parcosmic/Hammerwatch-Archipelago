import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList


class Map(Choice):
    """Determines the map of the seed.
    Castle Hammerwatch: Defeat the dragon that lies at the top of Castle Hammerwatch.
    Temple of the Sun: Stop the Sun Guardian Sha'Rand in the Temple of the Sun."""
    display_name = "Map"
    option_castle_hammerwatch = 0
    option_temple_of_the_sun = 1
    default = 1


class RandomLocationBehavior(Choice):
    """Determines how certain items that are randomized in Vanilla are handled in the Archipelago randomizer.
    Vanilla: Random locations behave as vanilla, and will only exist if an item is randomly placed there normally.
    All Checks: All potential locations are added to the pool, adding junk items for excess locations."""
    display_name = "Random Location Behavior"
    option_vanilla = 0
    option_all_checks = 2
    default = 0


class BonusChestLocationBehavior(Choice):
    """
    Determines how bonus chest locations in bonus levels are handled.
    None: Don't include any bonus chest items/locations.
    Necessary: Include bonus level locations for each extra item in the pool.
    All: Include all bonus chest items/locations. Extra items will replace junk items as normal.
    """
    display_name = "Bonus Level Location Behavior"
    option_none = 0
    option_necessary = 1
    option_all = 2
    default = 1


class RandomizeRecoveryItems(Toggle):
    """Determines if recovery items (such as apples and mana crystals) are shuffled into the pool."""
    display_name = "Randomize Recovery Items"
    default = True


class RandomizeSecrets(Toggle):
    """Determines if items from secrets are shuffled into the item pool."""
    display_name = "Randomize Secrets"
    default = False


class RandomizePuzzles(Toggle):
    """Determines if items from puzzles are shuffled into the item pool."""
    display_name = "Randomize Puzzles"
    default = False


class PortalAccessibility(Toggle):
    """TotS Only: Ensures rune keys will be placed on the floor they would normally appear so that portals are more easily accessible.
    """
    display_name = "Portal Accessibility"
    default = True


class ConsumableMerchantChecks(Range):
    """TotS Only: Add a number of checks that you can receive from the consumable merchant after giving them the pan.
    These get given out one by one after you reach specific milestones in the game."""
    display_name = "Consumable Merchant Checks"
    range_start = 0
    range_end = 10
    default = 0


class PanFragments(Range):
    """TotS Only: Separates the pan into multiple fragments that are shuffled into the item pool.
    All fragments must be collected in order to purchase from the consumables merchant."""
    display_name = "Pan Fragments"
    range_start = 0
    range_end = 5
    default = 0


class LeverFragments(Range):
    """TotS Only: Separates the pumps lever into multiple fragments that are shuffled into the item pool.
    All fragments must be collected in order to turn on the pumps."""
    display_name = "Pumps Lever Fragments"
    range_start = 0
    range_end = 5
    default = 0


class PickaxeFragments(Range):
    """TotS Only: Separates the pickaxe into multiple fragments that are shuffled into the item pool.
    All fragments must be collected in order to break the rocks outside the temple."""
    display_name = "Pickaxe Fragments"
    range_start = 0
    range_end = 5
    default = 0


class TrapItemPercentage(Range):
    """Determines what percentage of junk items are replaced with traps."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 5


class StartingLifeCount(Range):
    """How many extra lives to start the game with."""
    display_name = "Starting Life Count"
    range_start = 0
    range_end = 99
    default = 1


class DeathLink(DeathLink):
    """When you die, everyone dies. Of course the reverse is true too."""
    display_name = "Death Link"


hammerwatch_options: typing.Dict[str, type(Option)] = {
    "map": Map,
    "random_location_behavior": RandomLocationBehavior,
    "bonus_behavior": BonusChestLocationBehavior,
    "randomize_recovery_items": RandomizeRecoveryItems,
    "randomize_secrets": RandomizeSecrets,
    # "randomize_puzzles": RandomizePuzzles,
    "portal_accessibility": PortalAccessibility,
    # "randomize_shops": RandomizeShops,
    # "consumable_merchant_checks": ConsumableMerchantChecks,
    "pan_fragments": PanFragments,
    "lever_fragments": LeverFragments,
    "pickaxe_fragments": PickaxeFragments,
    "trap_item_percent": TrapItemPercentage,
    "starting_life_count": StartingLifeCount,
    "death_link": DeathLink
}
