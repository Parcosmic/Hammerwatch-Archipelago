import typing
from enum import Enum
from BaseClasses import MultiWorld
from .Names import ItemName


class Campaign(Enum):
    Castle = 0
    Temple = 1


class GoalType(Enum):
    KillFinalBoss = 0
    PlankHunt = 1
    FullCompletion = 2
    AltCompletion = 3


class Counter:
    def __init__(self, start: int = 0):
        self.counter = start

    def count(self, amount: int = 1):
        self.counter += amount
        return self.counter


def get_campaign(multiworld: MultiWorld, player: int) -> Campaign:
    return Campaign(multiworld.goal[player] // 10)


def get_goal_type(multiworld: MultiWorld, player: int) -> GoalType:
    return GoalType(multiworld.goal[player] % 10)


def get_key_names(multiworld: MultiWorld, player: int) -> typing.Set[str]:
    campaign = get_campaign(multiworld, player)
    if campaign == Campaign.Castle:
        key_names = {ItemName.key_bronze}
    else:
        key_names = {ItemName.mirror}
    key_names.update({
        ItemName.key_silver,
        ItemName.key_gold,
        ItemName.bonus_key,
                          })
    return key_names
