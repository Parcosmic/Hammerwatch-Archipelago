import typing

from . import HammerwatchTestBase
from .. import item_name, castle_region_names, option_names
from .. import options, locations, items
from .. import castle_location_names
from ..regions import castle_regions


class TestTempleShopsanity(HammerwatchTestBase):
    options = {
        option_names.goal: options.Goal.option_temple_plank_hunt,
        option_names.shopsanity_p1: options.ShopsanityP1Class.option_paladin,
    }
