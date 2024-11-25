from typing import Dict, TYPE_CHECKING
from enum import Enum
from ..AutoWorld import World
from worlds.generic.Rules import add_rule, CollectionRule

if TYPE_CHECKING:
    from . import SWD2World


class GoalType(Enum):
    FinalBoss = 0
    ArtifactHunt = 1
    Gauntlet = 2


class Counter:
    def __init__(self, start: int = 0):
        self.counter = start

    def count(self, amount: int = 1):
        self.counter += amount
        return self.counter


def get_goal_type(world: "SWD2World") -> GoalType:
    return GoalType(world.options.goal.value)


def get_random_element(world: World, dictionary: Dict):
    total = 0
    for item, value in dictionary.items():
        total += value
    index = world.random.randint(0, total-1)
    for item, value in dictionary.items():
        if index < value:
            return item
        index -= value
    return None


def get_random_elements(world: World, dictionary: Dict, amount: int):
    total = 0
    for value in dictionary.values():
        total += value
    elements = []
    for k in range(amount):
        index = world.random.randint(0, total-1)
        for item, value in dictionary.items():
            if index < value:
                elements.append(item)
                break
            index -= value
    return elements


def add_loc_rule(world: World, loc_name: str, rule: CollectionRule):
    loc = world.multiworld.get_location(loc_name, world.player)
    add_rule(loc, rule, "and")


def add_loc_item_rule(world: World, loc_name: str, item: str, item_count=1):
    add_loc_rule(world, loc_name, lambda state: state.has(item, world.player, item_count))


def is_using_universal_tracker(world: World):
    return hasattr(world.multiworld, "generation_is_fake")
