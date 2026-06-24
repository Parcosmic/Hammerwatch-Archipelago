from .base import HammerwatchTestBase
from .. import option_names
from .. import options


class TestCastleShopsanity(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_plank_hunt,
        option_names.shopsanity_p1: options.ShopsanityP1Class.option_paladin,
    }


class TestTempleShopsanity(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_plank_hunt,
        option_names.shopsanity_p1: options.ShopsanityP1Class.option_paladin,
    }


class TestCastleShopsanityShopShuffle(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_castle_plank_hunt,
        option_names.shopsanity_p1: options.ShopsanityP1Class.option_paladin,
        option_names.shop_shuffle: options.ShuffleShops.option_true,
    }


class TestTempleShopsanityShopShuffle(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_plank_hunt,
        option_names.key_mode: options.KeyMode.option_act_specific,
        option_names.shopsanity_p1: options.ShopsanityP1Class.option_paladin,
        option_names.shop_shuffle: options.ShuffleShops.option_true,
    }
