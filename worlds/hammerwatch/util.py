import typing
from enum import Enum
from BaseClasses import MultiWorld
from ..AutoWorld import World
from .names import item_name, option_names


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


def get_option(multiworld: MultiWorld, player: int, option_name: str):
    return getattr(multiworld, option_name)[player]


def get_campaign(multiworld: MultiWorld, player: int) -> Campaign:
    return Campaign(get_option(multiworld, player, option_names.goal) // 10)


def get_goal_type(multiworld: MultiWorld, player: int) -> GoalType:
    return GoalType(get_option(multiworld, player, option_names.goal) % 10)


def get_active_key_names(multiworld: MultiWorld, player: int) -> typing.Set[str]:
    campaign = get_campaign(multiworld, player)
    if campaign == Campaign.Castle:
        if get_option(multiworld, player, option_names.act_specific_keys):
            key_names = {
                item_name.key_bronze_prison,
                item_name.key_bronze_armory,
                item_name.key_bronze_archives,
                item_name.key_bronze_chambers,
                item_name.key_silver_prison,
                item_name.key_silver_armory,
                item_name.key_silver_archives,
                item_name.key_silver_chambers,
                item_name.key_gold_prison,
                item_name.key_gold_armory,
                item_name.key_gold_archives,
                item_name.key_gold_chambers,
            }
            if get_option(multiworld, player, option_names.randomize_bonus_keys):
                key_names.update({
                    item_name.key_bonus_prison,
                    item_name.key_bonus_armory,
                    item_name.key_bonus_archives,
                    item_name.key_bonus_chambers,
                    })
        else:
            key_names = {
                item_name.key_bronze,
                item_name.key_silver,
                item_name.key_gold,
            }
            if get_option(multiworld, player, option_names.randomize_bonus_keys):
                key_names.add(item_name.key_bonus)
    else:
        key_names = {
            item_name.key_silver,
            item_name.key_gold,
            item_name.mirror,
        }
        if get_option(multiworld, player, option_names.randomize_bonus_keys):
            key_names.add(item_name.key_bonus)
    return key_names


def get_random_element(world: World, dictionary: typing.Dict):
    total = 0
    for item, value in dictionary.items():
        total += value
    index = world.random.randint(0, total-1)
    for item, value in dictionary.items():
        if index < value:
            return item
        index -= value
    return None
