import typing
from schema import Schema, Optional, And
from dataclasses import dataclass
from Options import Choice, Range, Option, Toggle, DeathLink, OptionDict, FreeText, PerGameCommonOptions
from .names import option_names
from .items import trap_table


class Goal(Choice):
    """Determines the goal of the seed. Some goals are specific to certain campaigns
    Options starting with "Castle" are played in the Castle Hammerwatch campaign, while "Temple" options are played in the Temple of the Sun Campaign
    Castle All Bosses: Defeat all the bosses in Castle Hammerwatch. Escaping is NOT required
    Castle Escape: Find at least 12 Strange Planks, defeat Worldfire, and escape with your life
    Castle Plank Hunt: Find a certain number of Strange Planks in Castle Hammerwatch
    Temple All Bosses: Defeat all the bosses in the Temple of the Sun
    Temple Plank Hunt: Find a certain number of Strange Planks in the Temple of the Sun
    Temple Pyramid of Fear: Unlock and complete the Pyramid of Fear"""
    display_name = "Goal"
    # category = "Hammerwatch"
    option_castle_all_bosses = 0
    alias_castle_kill_worldfire = 0
    alias_castle_kill_dragon = 0
    option_castle_escape = 2
    option_castle_plank_hunt = 1  # 1 is always plank hunt
    option_temple_all_bosses = 10
    alias_temple_kill_sharand = 10
    option_temple_plank_hunt = 11
    option_temple_pyramid_of_fear = 13
    alias_temple_pof = 13
    default = 2


class Difficulty(Choice):
    """What difficulty the game will be played on"""
    display_name = "Difficulty"
    # category = "Hammerwatch"
    option_easier = 0
    alias_easy = 0
    option_medium = 1
    option_hard = 2
    default = 1


class BonusChestLocationBehavior(Choice):
    """Determines how bonus chest locations in bonus levels are handled
    None: Don't include any bonus chest items/locations
    Necessary: Include bonus level locations for each extra item in the pool
    All: Include all bonus chest items/locations. Extra items will replace junk items as normal"""
    display_name = "Bonus Level Location Behavior"
    # category = "Generation"
    option_none = 0
    option_necessary = 1
    option_all = 2
    default = 1


class PlankCount(Range):
    """Determines the amount of Strange Planks in the game
    If a Plank Hunt goal is chosen, the minimum value is the value of the Planks to Win setting
    If the Castle Escape goal is chosen, the minimum value is 12
    This option does nothing in other goals"""
    display_name = "Number of Strange Planks"
    # category = "Generation"
    range_start = 1
    range_end = 25
    default = 12


class PlanksRequiredCount(Range):
    """Determines the amount of Strange Planks required to win the game for the Plank Hunt goals.
    This option does nothing in other goals"""
    display_name = "Planks to Win"
    # category = "Generation"
    range_start = 1
    range_end = 25
    default = 12


class ExtraPlankPercent(Range):
    """Determines the percentage of extra Strange Planks in the item pool
    For the Castle Escape goal, the required planks count is 12
    For the Plank Hunt goals, the required planks count is determined by the Planks to Win setting
    Formula: Total Planks = required planks * (1 + Extra Plank Percentage / 100)
    This option does nothing in other goals"""
    display_name = "Extra Plank Percentage"
    # category = "Generation"
    range_start = 0
    range_end = 100
    default = 0


class RandomizeBonusKeys(Toggle):
    """Whether bonus keys are shuffled into the pool"""
    display_name = "Randomize Bonus Keys"
    # category = "Generation"
    default = False


class RemoveExtraLives(Toggle):
    """Removes extra lives (Ankhs) from the item pool and replaces them with filler.
    Recommended to have enabled when playing with the infinite lives or no extra lives modifiers"""
    display_name = "Remove Extra Lives"
    # category = "Generation"
    default = False


class RandomizeRecoveryItems(Toggle):
    """Whether recovery items (such as apples and mana crystals) are shuffled into the pool"""
    display_name = "Randomize Recovery Items"
    # category = "Generation"
    default = False


class RandomizeSecrets(Toggle):
    """(TotS only) Whether items from random secrets (small rooms with cracked walls in the cave levels) are shuffled into the item pool
    """
    display_name = "Randomize Random Secrets"
    # category = "Generation"
    default = False


class RandomizePuzzles(Toggle):
    """Whether items from peg puzzles are shuffled into the item pool"""
    display_name = "Randomize Peg Puzzles"
    # category = "Generation"
    default = False


class RandomizeEnemyLoot(Toggle):
    """Whether items dropped by minibosses and towers are shuffled into the item pool"""
    display_name = "Randomize Major Enemy Loot"
    # category = "Generation"
    default = False


class Buttonsanity(Choice):
    """Whether the effects of buttons and switches are shuffled into the item pool
    Normal: button effects can be found anywhere in the multiworld
    Insanity: button effects will be split into progressive versions based on the number of buttons required to trigger the effect in vanilla
    """
    # Shuffle: all effects from buttons and switches will be shuffled only amongst your own button and switch locations
    display_name = "Buttonsanity"
    # category = "Generation"
    option_off = 0
    # option_shuffle = 1  # Disabled for now, keeps failing fill due to how restrictive button placements are
    # Would likely need to use item rules on every location to make this work, but this'll be insanely slow
    option_normal = 2
    option_insanity = 3
    default = 0


class ExitRandomization(Choice):
    """Randomizes where level exits and portals lead
    No Boss Exits: exits to boss levels will not be shuffled
    All: all exits including bosses will be shuffled"""
    display_name = "Exit Randomization"
    # category = "Generation"
    option_off = 0
    option_no_boss_exits = 1
    option_all = 2
    alias_on = 2
    default = 0


class ERActRange(Range):
    """Determines the maximum number of acts away levels will try to be connected to each other in exit randomization
    For example with an act range of 1 Prison exits will mostly only connect to other Prison exits or Armory exits"""
    display_name = "ER Act Connection Range"
    # category = "Generation"
    range_start = 1
    range_end = 3
    default = 1


class StartExit(Toggle):
    """If Exit Randomization is on, will place you at a random exit at the start of the game
    Use the /t command in game to return if you get stuck!"""
    display_name = "Randomize Start Location"
    # category = "Generation"
    default = False


class StartExitAct(Range):
    """Determines the act in which you start if Randomize Start Location is on"""
    display_name = "Start Location Act"
    # category = "Generation"
    range_start = 1
    range_end = 4
    default = 1


class GateShuffle(Toggle):  # Maybe someday I'll add a mode so the number of keys are randomized too
    """Shuffles the type of bronze, silver, and gold gates"""
    display_name = "Gate Shuffle"
    # category = "Generation"
    default = False


class ShuffleShops(Toggle):
    """Shuffles the shop vendors around so that they may be different from their normal locations"""
    display_name = "Shop Location Shuffle"
    # category = "Generation"
    default = False


class ShopUpgradeCategoryShuffle(Choice):
    """Shuffles the shop upgrades between different categories of shops
    Group: upgrades sharing the same base name (Damage 1, 2, 3, etc.) are shuffled together in the same category
    All: upgrades are shuffled amongst all categories, regardless of prerequisites"""
    display_name = "Shop Upgrade Category Shuffle"
    # category = "Generation"
    option_off = 0
    option_group = 1
    option_all = 2
    default = 0


class ShopUpgradePrereqShuffle(Choice):
    """Shuffles the prerequisites of shop upgrades. If Shop Upgrade Level Shuffle is off prerequisite levels will stay the same
    Same Category: upgrade prerequisites are only shuffled within the same category
    All: all upgrade prerequisites are shuffled, even between categories"""
    display_name = "Shop Upgrade Prerequisite Shuffle"
    # category = "Generation"
    option_off = 0
    option_same_category = 1
    option_all = 2
    default = 0


class ShopUpgradeLevelShuffle(Toggle):
    """Shuffles the level each shop upgrade is found"""
    display_name = "Shop Upgrade Level Shuffle"
    # category = "Generation"
    default = False


class ShopCostRandoMin(Range):
    """The lowest percent each shop upgrade cost can be multiplied by"""
    display_name = "Minimum Shop Cost Percent"
    range_start = 0
    range_end = 500
    default = 100


class ShopCostRandoMax(Range):
    """The highest percent each shop upgrade cost can be multiplied by"""
    display_name = "Maximum Shop Cost Percent"
    range_start = 0
    range_end = 500
    default = 100


class EnemyShuffle(Toggle):
    """Shuffles the locations of enemies, spawners, mini-bosses, and towers in each level"""
    display_name = "Enemy Shuffle"
    # category = "Generation"
    default = False


class EnemyShuffleBalancing(Range):
    """How many acts away enemies can be shuffled to
    When set to 0 only enemies on the same act will be shuffled
    When set to 3 enemies can be shuffled to any act"""
    display_name = "Enemy Shuffle Act Range"
    # category = "Generation"
    range_start = 0
    range_end = 3
    default = 0


class ExtraKeysPercent(Range):
    """Determines the percentage of extra silver and gold keys (and mirrors in the TotS campaign) that are added to the item pool
    """
    display_name = "Extra Keys Percentage"
    # category = "Generation"
    range_start = 0
    range_end = 50
    default = 0


class OpenCastle(Toggle):
    """(Castle only) Unlocks travel to/from all floors at the start of the game. Pairs well with Act Specific Keys!
    """
    display_name = "Open Castle"
    # category = "Generation"
    default = False


class ActSpecificKeys(Toggle):
    """(Castle only) Separates keys into versions that can only be used on a specific act.
    Mainly improves hinting for keys, as with generic keys you could hint for a gold key at the end of the seed that you can't get"""
    display_name = "Act Specific Keys"
    # category = "Generation"
    default = True


class KeyMode(Choice):
    """Changes the behavior of keys
    Vanilla: keys can be used anywhere on their respective gates
    Act Specific: (castle only) replaces keys with versions that can only be used on a specific act
    Floor Master: consolidates keys on a floor into a single item that unlocks all gates of that type on an entire floor
    """
    display_name = "Key Mode"
    option_vanilla = 0
    option_act_specific = 1
    option_floor_master = 2
    default = 1


class BigBronzeKeyPercent(Range):
    """(Castle only) What percentage of bronze keys get converted into big bronze keys, which act as 3 bronze keys each
    """
    display_name = "Big Bronze Key Conversion Percent"
    # category = "Generation"
    range_start = 0
    range_end = 100
    default = 0


class ShortcutTeleporter(Toggle):
    """(Castle only) Enables the use of the shortcut portal at the beginning of the game. This allows early access
    to Prison Floor 3 before the bronze gate, preventing a potential early BK
    A return portal will also be placed so that the first two floors can be fully completed"""
    display_name = "Enable Shortcut Portal"
    # category = "Generation"
    default = False


class PortalAccessibility(Toggle):
    """(TotS only) Ensures rune keys will be placed locally on the floor they would normally appear so that portals are
    more easily accessible"""
    display_name = "Portal Accessibility"
    # category = "Generation"
    default = True


class NoSunbeamDamage(Toggle):
    """(TotS only) Disables sunbeam damage, removing much of the long and awkward backtracking inside the temple"""
    display_name = "Pleasant Sunbeams"
    # category = "QoL"
    default = False


class TreasureShuffle(Toggle):
    """Shuffles the locations of minor treasure such as coins, crates, pots, and vegetation"""
    display_name = "Treasure Shuffle"
    # category = "Generation"
    default = False


class ConsumableMerchantChecks(Range):
    """(TotS only) Add a number of locations to the powerup vendor after giving them the frying pan
    Items in these locations get given out one by one after you reach specific milestones in the game"""
    display_name = "Consumables Vendor Locations"
    # category = "Hammerwatch"
    range_start = 0
    range_end = 10
    default = 0


class PanFragments(Range):
    """(TotS only) If greater than 1 separates the pan into multiple fragments that are shuffled into the item pool
    All fragments must be collected in order to purchase from the consumables merchant"""
    display_name = "Pan Fragments"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 5
    default = 1


class LeverFragments(Range):
    """(TotS only) If greater than 1 separates the pumps lever into multiple fragments that are shuffled into the item pool
    All fragments must be collected in order to turn on the pumps"""
    display_name = "Pumps Lever Fragments"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 5
    default = 1


class PickaxeFragments(Range):
    """(TotS only) If greater than 1 separates the pickaxe into multiple fragments that are shuffled into the item pool
    All fragments must be collected in order to break the rocks outside the temple"""
    display_name = "Pickaxe Fragments"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 5
    default = 1


class TrapItemPercentage(Range):
    """What percentage of junk items are replaced with traps"""
    display_name = "Trap Percentage"
    # category = "Hammerwatch"
    range_start = 0
    range_end = 100
    default = 5


class TrapItemWeights(OptionDict):
    """The relative weights of trap items in the item pool"""
    display_name = "Trap Item Weights"
    schema = Schema({Optional(trap): And(int, lambda n: n >= 0) for trap in trap_table.keys()})
    default = {trap: 100 for trap in trap_table.keys()}


class StartingLifeCount(Range):
    """How many extra lives each player will start the game with"""
    display_name = "Starting Life Count"
    # category = "Hammerwatch"
    range_start = 0
    range_end = 99
    default = 2


class GameModifiers(OptionDict):
    """Enforces game modifiers to be set either true or false"""
    display_name = "Game Modifiers"
    schema = Schema({Optional(mod): bool for mod in option_names.game_modifier_names})


class ERSeed(FreeText):
    """Determines the seed for generating the exit randomization layout. If blank the seed will be random"""
    display_name = "Exit Randomization Seed"


class DeathLink(DeathLink):
    """When anybody dies, everyone dies. This also applies to all multiplayer players within a single game"""
    display_name = "Death Link"


@dataclass
class HammerwatchOptions(PerGameCommonOptions):
    goal: Goal
    planks_required_count: PlanksRequiredCount
    extra_plank_percent: ExtraPlankPercent
    difficulty: Difficulty
    exit_randomization: ExitRandomization
    er_act_range: ERActRange
    random_start_exit: StartExit
    random_start_exit_act: StartExitAct
    gate_shuffle: GateShuffle
    shop_shuffle: ShuffleShops
    shop_upgrade_category_shuffle: ShopUpgradeCategoryShuffle
    # shop_upgrade_level_shuffle: ShopUpgradeLevelShuffle
    shop_cost_min: ShopCostRandoMin
    shop_cost_max: ShopCostRandoMax
    enemy_shuffle: EnemyShuffle
    enemy_shuffle_act_range: EnemyShuffleBalancing
    bonus_behavior: BonusChestLocationBehavior
    randomize_bonus_keys: RandomizeBonusKeys
    remove_lives: RemoveExtraLives
    randomize_recovery_items: RandomizeRecoveryItems
    randomize_secrets: RandomizeSecrets
    randomize_puzzles: RandomizePuzzles
    randomize_enemy_loot: RandomizeEnemyLoot
    buttonsanity: Buttonsanity
    open_castle: OpenCastle
    key_mode: KeyMode
    extra_keys_percent: ExtraKeysPercent
    big_bronze_key_percent: BigBronzeKeyPercent
    shortcut_teleporter: ShortcutTeleporter
    portal_accessibility: PortalAccessibility
    no_sunbeam_damage: NoSunbeamDamage
    treasure_shuffle: TreasureShuffle
    # consumables_vendor_locations: ConsumableMerchantChecks
    pan_fragments: PanFragments
    lever_fragments: LeverFragments
    pickaxe_fragments: PickaxeFragments
    trap_item_percent: TrapItemPercentage
    trap_item_weights: TrapItemWeights
    starting_life_count: StartingLifeCount
    game_modifiers: GameModifiers
    er_seed: ERSeed
    death_link: DeathLink


client_required_options = [
    option_names.goal,
    option_names.planks_required_count,
    option_names.extra_plank_percent,
    option_names.difficulty,
    option_names.exit_randomization,
    option_names.er_act_range,
    option_names.random_start_exit,
    option_names.random_start_exit_act,
    option_names.gate_shuffle,
    option_names.shop_shuffle,
    option_names.shop_upgrade_category_shuffle,
    # option_names.shop_upgrade_level_shuffle,
    option_names.shop_cost_min,
    option_names.shop_cost_max,
    option_names.enemy_shuffle,
    option_names.enemy_shuffle_act_range,
    option_names.randomize_bonus_keys,
    option_names.randomize_recovery_items,
    option_names.randomize_secrets,
    option_names.randomize_puzzles,
    option_names.randomize_enemy_loot,
    option_names.buttonsanity,
    option_names.open_castle,
    option_names.key_mode,
    option_names.shortcut_teleporter,
    option_names.portal_accessibility,
    option_names.no_sunbeam_damage,
    option_names.treasure_shuffle,
    # option_names.consumables_vendor_locations,
    option_names.pan_fragments,
    option_names.lever_fragments,
    option_names.pickaxe_fragments,
    option_names.starting_life_count,
    option_names.game_modifiers,
    option_names.death_link,
]
