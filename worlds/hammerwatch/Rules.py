import math

from BaseClasses import MultiWorld
from .Names import LocationName, RegionName, ItemName
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import add_rule, set_rule, forbid_item


def set_rules(multiworld: MultiWorld, player: int):

    multiworld.completion_condition[player] = lambda state: state.has(ItemName.victory, player)
