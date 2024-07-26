import typing
from enum import Enum
from ..AutoWorld import World
from worlds.generic.Rules import add_rule, CollectionRule
from .names import item_name

if typing.TYPE_CHECKING:
    from . import HammerwatchWorld


castle_act_names = [
    "Prison",
    "Armory",
    "Archives",
    "Chambers",
]


class Campaign(Enum):
    Castle = 0
    Temple = 1


class GoalType(Enum):
    KillBosses = 0
    PlankHunt = 1
    FullCompletion = 2
    AltCompletion = 3


class PlayerClass(Enum):
    Paladin = 1
    Wizard = 2
    Ranger = 3
    Warlock = 4
    Thief = 5
    Priest = 6
    Sorcerer = 7


class ShopType(Enum):
    Vitality = 0
    Combo = 1
    Offense = 2
    Defense = 3
    Powerup = 4
    Gamble = 5


class ShopInfo:
    shop_type: ShopType
    level: int

    def __init__(self, shop_type, level):
        self.shop_type = shop_type
        self.level = level

    def to_str(self):
        shop_str = self.shop_type.name
        if self.level > 0:
            return f"{shop_str} Level {self.level}"
        return shop_str


class Counter:
    def __init__(self, start: int = 0):
        self.counter = start

    def count(self, amount: int = 1):
        self.counter += amount
        return self.counter


def get_campaign(world: "HammerwatchWorld") -> Campaign:
    return Campaign(world.options.goal.value // 10)


def get_goal_type(world: "HammerwatchWorld") -> GoalType:
    return GoalType(world.options.goal.value % 10)


def get_buttonsanity_insanity(world: "HammerwatchWorld") -> bool:
    return world.options.buttonsanity.value == world.options.buttonsanity.option_insanity
    # or world.options.buttonsanity.value == world.options.buttonsanity.option_shuffle)


def get_class_from_option_value(option_value: int):
    return PlayerClass(option_value)


def get_shopsanity_classes(world: "HammerwatchWorld") -> typing.List[PlayerClass]:
    classes = []
    if world.options.shopsanity_p1 > 0:
        p1_class = get_class_from_option_value(world.options.shopsanity_p1.value)
        classes.append(p1_class)
    if world.options.shopsanity_p2 > 0:
        p2_class = get_class_from_option_value(world.options.shopsanity_p2.value)
        if p2_class not in classes:
            classes.append(p2_class)
    if world.options.shopsanity_p3 > 0:
        p3_class = get_class_from_option_value(world.options.shopsanity_p3.value)
        if p3_class not in classes:
            classes.append(p3_class)
    if world.options.shopsanity_p4 > 0:
        p4_class = get_class_from_option_value(world.options.shopsanity_p4.value)
        if p4_class not in classes:
            classes.append(p4_class)
    return classes


def get_key_code(key_name: str):
    if key_name == "bronze":
        return 0
    if key_name == "silver":
        return 1
    if key_name == "gold":
        return 2
    if key_name == "bonus":
        return 10


def get_active_key_names(world: "HammerwatchWorld") -> typing.List[str]:
    campaign = get_campaign(world)
    if campaign == Campaign.Castle:
        if world.options.key_mode.value == world.options.key_mode.option_floor_master:
            key_names = []
            if world.options.randomize_bonus_keys == world.options.randomize_bonus_keys.option_false:
                key_names.extend([
                    item_name.key_bonus_prison,
                    item_name.key_bonus_armory,
                    item_name.key_bonus_archives,
                    item_name.key_bonus_chambers,
                ])
        elif world.options.key_mode.value == world.options.key_mode.option_act_specific:
            key_names = [
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
                item_name.key_bonus_prison,  # Even if bonus keys aren't randomized we need to set logic for them!
                item_name.key_bonus_armory,
                item_name.key_bonus_archives,
                item_name.key_bonus_chambers,
            ]
        else:
            key_names = [
                item_name.key_bronze,
                item_name.key_silver,
                item_name.key_gold,
                item_name.key_bonus,
            ]
    else:
        key_names = [
            item_name.mirror,
            item_name.key_teleport,
            item_name.key_bonus,
        ]
        if world.options.key_mode.value != world.options.key_mode.option_floor_master:
            key_names.extend([
                item_name.key_silver,
                item_name.key_gold,
            ])
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


def get_random_elements(world: World, dictionary: typing.Dict, amount: int):
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
