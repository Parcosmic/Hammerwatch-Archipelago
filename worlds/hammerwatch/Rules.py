import math

from BaseClasses import MultiWorld
from Names import LocationName, RegionName, ItemName
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import add_rule, set_rule, forbid_item


def set_rules(world: MultiWorld, player: int):

    # set_rule(world.get_entrance(RegionName.hub_rocks, player), lambda state: state.has(ItemName.pickaxe, player))
    # set_rule(world.get_entrance(RegionName.cave_3_fields, player), lambda state: state.has(ItemName.lever, player))

    world.completion_condition[player] = lambda state: state.has(ItemName.victory, player)
