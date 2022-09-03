import math

from BaseClasses import MultiWorld
from .Names import LocationName, RegionName, ItemName
from ..AutoWorld import LogicMixin
from ..generic.Rules import add_rule, set_rule, forbid_item


def set_rules(world: MultiWorld, player: int):

    set_rule(world.get_entrance(RegionName.hub_rocks, player), lambda state: state.has(ItemName.pickaxe, player))

    world.completion_condition[player] = lambda state: state.has(ItemName.victory, player)
