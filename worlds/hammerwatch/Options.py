import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList


class Map(Choice):
    """
    Determines the map of the seed
    Castle Hammerwatch: Defeat the dragon that lies at the top of Castle Hammerwatch
    Temple of the Sun: Stop the Sun Guardian Sha'Rand in the Temple of the Sun
    """
    display_name = "Map"
    option_castle_hammerwatch = 0
    option_temple_of_the_sun = 1
    default = 1


class RandomizeRecoveryItems(Toggle):
    """
    Randomize if recovery items (such as apples and mana crystals) are shuffled into the pool
    """
    display_name = "Randomize Recovery Items"
    default = True

class RandomizeShops(Toggle):
    """
    Randomize if shop upgrades are shuffled into the pool
    """
    display_name = "Randomize Shops"


class StartingLifeCount(Range):
    """
    How many extra lives to start the game with
    """
    display_name = "Starting Life Count"
    range_start = 0
    range_end = 99
    default = 1


class DeathLink(DeathLink):
    """
    When you die, everyone dies. Of course the reverse is true too.
    """
    display_name = "Death Link"


hammerwatch_options: typing.Dict[str, type(Option)] = {
    "map": Map,
    "randomize_recovery_items": RandomizeRecoveryItems,
    "randomize_shops": RandomizeShops,
    "starting_life_count": StartingLifeCount,
    "death_link": DeathLink
}
