from typing import TYPE_CHECKING
from .names import item_name
from .util import GoalType, get_goal_type
from rule_builder.rules import Has

if TYPE_CHECKING:
    from . import SWD2World


def set_rules(world: "SWD2World"):
    goal = get_goal_type(world)

    if goal == GoalType.FinalBoss:
        world.set_completion_rule(Has(item_name.ev_blastoff))
    else:
        raise Exception(f"Selected goal type is not implemented: {goal}")
