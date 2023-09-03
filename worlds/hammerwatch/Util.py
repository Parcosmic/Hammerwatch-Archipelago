import typing
from enum import Enum
from BaseClasses import MultiWorld
from .Names import ItemName, OptionNames


class Campaign(Enum):
    Castle = 0
    Temple = 1


class GoalType(Enum):
    KillBosses = 0
    PlankHunt = 1
    FullCompletion = 2
    AltCompletion = 3


class Counter:
    def __init__(self, start: int = 0):
        self.counter = start

    def count(self, amount: int = 1):
        self.counter += amount
        return self.counter


def get_option(multiworld, option_name, player):
    return getattr(multiworld, option_name)[player]


def get_campaign(multiworld: MultiWorld, player: int) -> Campaign:
    return Campaign(get_option(multiworld, OptionNames.goal, player) // 10)


def get_goal_type(multiworld: MultiWorld, player: int) -> GoalType:
    return GoalType(get_option(multiworld, OptionNames.goal, player) % 10)


def get_active_key_names(multiworld: MultiWorld, player: int) -> typing.Set[str]:
    campaign = get_campaign(multiworld, player)
    if campaign == Campaign.Castle:
        if get_option(multiworld, OptionNames.act_specific_keys, player):
            key_names = {
                ItemName.key_bronze_prison,
                ItemName.key_bronze_armory,
                ItemName.key_bronze_archives,
                ItemName.key_bronze_chambers,
                ItemName.key_silver_prison,
                ItemName.key_silver_armory,
                ItemName.key_silver_archives,
                ItemName.key_silver_chambers,
                ItemName.key_gold_prison,
                ItemName.key_gold_armory,
                ItemName.key_gold_archives,
                ItemName.key_gold_chambers,
            }
            if get_option(multiworld, OptionNames.randomize_bonus_keys, player):
                key_names.update({
                    ItemName.key_bonus_prison,
                    ItemName.key_bonus_armory,
                    ItemName.key_bonus_archives,
                    ItemName.key_bonus_chambers,
                    })
        else:
            key_names = {
                ItemName.key_bronze,
                ItemName.key_silver,
                ItemName.key_gold,
            }
            if get_option(multiworld, OptionNames.randomize_bonus_keys, player):
                key_names.add(ItemName.key_bonus)
    else:
        key_names = {
            ItemName.key_silver,
            ItemName.key_gold,
            ItemName.mirror,
        }
        if get_option(multiworld, OptionNames.randomize_bonus_keys, player):
            key_names.add(ItemName.key_bonus)
    return key_names


def get_random_element(multiworld: MultiWorld, dictionary: typing.Dict):
    total = 0
    for item, value in dictionary.items():
        total += value
    index = multiworld.random.randint(0, total-1)
    for item, value in dictionary.items():
        if index < value:
            return item
        index -= value
    return None
