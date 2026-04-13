from dataclasses import dataclass
from Options import Choice, Range, Toggle, DeathLink, FreeText, PerGameCommonOptions, OptionGroup, NamedRange
from .names import option_name


class Goal(Choice):
    """Determines the goal of your world"""
    display_name = "Goal"
    option_final_boss = 0
    default = 0


class StartLocation(Choice):
    """Determines where you start in the world"""
    display_name = "Start Location"
    option_vanilla = 0
    option_el_machino = 1
    option_the_oasis = 2
    option_temple_of_the_destroyer = 3
    alias_temple_of_guidance = 0
    default = 0
# Don't forget to update the patcher if adding new start locations!


class EntranceRandomization(Choice):
    """Determines which entrances are shuffled
    Dead End Caves: only shuffle entrances to caves without an exit
    All Caves: shuffle all entrances to caves whether they have exits or not
    All Transitions: shuffles all level transitions"""
    display_name = "Entrance Randomization"
    option_off = 0
    option_dead_end_caves = 1
    # option_all_caves = 2
    # option_all_transitions = 3
    default = 0


class ShuffleResources(Toggle):
    """Shuffles the types of resources found in different layers"""
    display_name = "Shuffle Resources"
    default = False


class CogUpgradeShuffle(Choice):
    """Shuffles the order in which you receive Cog Mods"""
    display_name = "Cog Mod Shuffle"
    option_vanilla = 0
    option_shuffle_purchase = 1
    default = 0


class RandomizeCogCosts(NamedRange):
    """Randomize the costs of Cog Mod, the value is the sum of all cog costs. Vanilla is 116
    Special values:
    -1: Costs are not randomized
    -2: Vanilla costs are shuffled between available upgrades"""
    display_name = "Randomize Cog Mod Costs"
    range_start = 0
    range_end = 250
    default = -1
    special_range_names = {
        "vanilla": -1,
        "shuffle": -2
    }


class ShopCostRandoMax(Range):
    """The highest percent each shop upgrade cost can be multiplied by"""
    display_name = "Maximum Shop Cost Percent"
    range_start = 0
    range_end = 200
    default = 100


class ShopCostRandoMin(Range):
    """The lowest percent each shop upgrade cost can be multiplied by"""
    display_name = "Minimum Shop Cost Percent"
    range_start = 0
    range_end = 200
    default = 100


class AddUnusedBlueprints(Toggle):
    """Enables the use of a few functional Cog Mods that didn't make it in the vanilla game"""
    display_name = "Add Unused Cog Mods"
    default = False


class RandomizeCogs(Toggle):
    """Adds cogs to the pool of randomized items and locations"""
    display_name = "Randomize Cogs"
    default = False


class RandomizeArtifacts(Toggle):
    """Adds artifacts to the pool of randomized items and locations"""
    display_name = "Randomize Artifacts"
    default = False


class RandomizeShopUpgrades(Choice):
    """Determines if and how Cog Mods are randomized
    Shuffle: the order that Cog Mods are unlocked will be shuffled
    Randomize: adds Cog Mods to the item pool, and purchasing tool upgrades will grant a check
    """
    display_name = "Randomize Shop Upgrade Mode"
    option_off = 0
    option_shuffle = 1
    option_randomize = 2
    default = 0


class RandomizeOres(Toggle):
    """Determines if ore blocks that have a consistent location are randomized into the item pool"""
    display_name = "Randomize Static Ores"
    default = False


class RandomizeOrbs(Toggle):
    """Determines if floating orb containers (health, lamp, and omni) are randomized into the item pool"""
    display_name = "Randomize Orb Containers"
    default = False


class RandomizeTrialReward(Toggle):
    """Determines if the reward at the end of the trials is randomized
    WARNING: the Trials are stupidly hard, enable at risk to the multiworld!
    """
    display_name = "Randomize Trials Reward"
    default = False


class StartingLevel(Range):
    """What level you start the game as
    Note some introductory quests are skipped that would normally grant experience putting you up to level 3"""
    display_name = "Starting Level"
    range_start = 1
    range_end = 20
    default = 3


class StartingMoney(Range):
    """How much money you start with"""
    display_name = "Starting Money"
    range_start = 0
    range_end = 50000
    default = 0


class StartWithPortal(Toggle):
    """Start the game with the Portal of Pardon blueprint and 3 cogs to equip it"""
    display_name = "Start With Portal of Pardon"
    default = False


class SkipVectron(Toggle):
    """Adds a passage to the podium in the Mysterious Cave, preventing the need to struggle through Vectron"""
    display_name = "Skip Vectron"
    default = True


class ERSeed(FreeText):
    """Determines the seed for generating the entrance randomization layout. If "random" the seed will be random"""
    display_name = "Entrance Randomization Seed"
    default = "random"


@dataclass
class SWD2Options(PerGameCommonOptions):
    goal: Goal
    start_location: StartLocation
    entrance_rando: EntranceRandomization
    randomize_cogs: RandomizeCogs
    randomize_artifacts: RandomizeArtifacts
    randomize_ores: RandomizeOres
    randomize_orbs: RandomizeOrbs
    randomize_shops: RandomizeShopUpgrades
    randomize_trials_reward: RandomizeTrialReward
    shuffle_resources: ShuffleResources
    randomize_cog_costs: RandomizeCogCosts
    shop_cost_max: ShopCostRandoMax
    shop_cost_min: ShopCostRandoMin
    add_unused_cog_upgrades: AddUnusedBlueprints
    starting_level: StartingLevel
    starting_money: StartingMoney
    start_with_portal: StartWithPortal
    skip_vectron: SkipVectron
    er_seed: ERSeed


client_required_options = [
    option_name.goal,
    option_name.start_location,
    option_name.entrance_rando,
    option_name.randomize_cogs,
    option_name.randomize_artifacts,
    option_name.randomize_ores,
    option_name.randomize_orbs,
    option_name.randomize_shops,
    option_name.shuffle_resources,
    option_name.shop_cost_max,
    option_name.shop_cost_min,
    option_name.randomize_cog_costs,
    option_name.add_unused_cog_upgrades,
    option_name.starting_level,
    option_name.starting_money,
    option_name.skip_vectron,
    option_name.er_seed,
]

option_presets = {
    "All Random": {
        option_name.goal: "random",
    },
}

option_groups = [
    OptionGroup("Generation", [
        Goal
    ]),
]
