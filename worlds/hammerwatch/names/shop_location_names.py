# Shop location names
import typing
from . import option_names
from .. import util

vitality_shop_location_count = [2, 2, 3, 3, 3]
combo_shop_location_count = [5, 4, 4, 4, 4]

shop_class_base_location_names: typing.Dict[util.PlayerClass, typing.Dict[util.ShopType, typing.List[int]]] = {
    util.PlayerClass.Paladin: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 5, 6, 4],
            util.ShopType.Defense: [3, 4, 4, 2, 2],
        },
    util.PlayerClass.Ranger: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 5, 6, 5],
            util.ShopType.Defense: [2, 3, 3, 4, 3],
        },
    util.PlayerClass.Wizard: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 7, 7, 7],
            util.ShopType.Defense: [2, 2, 3, 3, 2],
        },
    util.PlayerClass.Warlock: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 5, 6, 7, 6],
            util.ShopType.Defense: [2, 3, 4, 4, 2],
        },
    util.PlayerClass.Thief: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 5, 5, 5, 1],
            util.ShopType.Defense: [2, 4, 5, 4, 3],
        },
    util.PlayerClass.Priest: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 5, 6, 6, 5],
            util.ShopType.Defense: [3, 3, 5, 4, 4],
        },
    util.PlayerClass.Sorcerer: {
            util.ShopType.Vitality: vitality_shop_location_count,
            util.ShopType.Combo: combo_shop_location_count,
            util.ShopType.Offense: [2, 4, 7, 7, 7],
            util.ShopType.Defense: [2, 3, 4, 3, 2],
        },
}
shop_class_location_names: typing.Dict[util.PlayerClass, typing.Dict[util.ShopType, typing.List[typing.List[str]]]] = {}
for _player_class, shop_type_locs in shop_class_base_location_names.items():
    shop_class_location_names[_player_class] = {}
    for shop_type, shop_counts in shop_type_locs.items():
        shop_class_location_names[_player_class][shop_type] = []
        for level, shop_level_count in enumerate(shop_counts, start=1):
            shop_class_location_names[_player_class][shop_type].append([
                f"{_player_class.name} {shop_type.name} {level} Shop Item {i}" for i in range(1, shop_level_count+1)
            ])
# for player_class, shop_types in shop_class_base_location_names.items():
#     total_shops = 0
#     for shop_type in shop_types:
#         total_shops += sum(shop_types[shop_type])
#     print(f"{player_class.name} {total_shops}")
