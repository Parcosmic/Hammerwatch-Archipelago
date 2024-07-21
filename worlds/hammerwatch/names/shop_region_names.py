# Shop region names
import typing
from .. import util

shop_vitality_1 = "Vitality 1 Shop"
shop_vitality_2 = "Vitality 2 Shop"
shop_vitality_3 = "Vitality 3 Shop"
shop_vitality_4 = "Vitality 4 Shop"
shop_vitality_5 = "Vitality 5 Shop"
shop_combo_1 = "Combo 1 Shop"
shop_combo_2 = "Combo 2 Shop"
shop_combo_3 = "Combo 3 Shop"
shop_combo_4 = "Combo 4 Shop"
shop_combo_5 = "Combo 5 Shop"
shop_offense_1 = "Offense 1 Shop"
shop_offense_2 = "Offense 2 Shop"
shop_offense_3 = "Offense 3 Shop"
shop_offense_4 = "Offense 4 Shop"
shop_offense_5 = "Offense 5 Shop"
shop_defense_1 = "Defense 1 Shop"
shop_defense_2 = "Defense 2 Shop"
shop_defense_3 = "Defense 3 Shop"
shop_defense_4 = "Defense 4 Shop"
shop_defense_5 = "Defense 5 Shop"
shop_misc = "Miscellaneous Shop"
shop_gamble = "Gambling Shop"

shop_vitality = [
    shop_vitality_1,
    shop_vitality_2,
    shop_vitality_3,
    shop_vitality_4,
    shop_vitality_5,
]
shop_combo = [
    shop_combo_1,
    shop_combo_2,
    shop_combo_3,
    shop_combo_4,
    shop_combo_5,
]
shop_offense = [
    shop_offense_1,
    shop_offense_2,
    shop_offense_3,
    shop_offense_4,
    shop_offense_5,
]
shop_defense = [
    shop_defense_1,
    shop_defense_2,
    shop_defense_3,
    shop_defense_4,
    shop_defense_5,
]

shop_regions: typing.Dict[util.ShopType, typing.List[str]] = {
    util.ShopType.Vitality: shop_vitality,
    util.ShopType.Combo: shop_combo,
    util.ShopType.Offense: shop_offense,
    util.ShopType.Defense: shop_defense,
}
