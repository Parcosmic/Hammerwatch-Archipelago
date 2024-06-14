import typing

from . import HammerwatchTestBase
from .. import item_name, castle_region_names, option_names
from .. import options, locations, items
from .. import castle_location_names
from ..regions import castle_regions

bonus1_regions = [
    castle_region_names.n1_start,
    castle_region_names.n1_room1,
    castle_region_names.n1_room2,
    castle_region_names.n1_room3,
    castle_region_names.n1_room4,
    castle_region_names.n1_exit,
]


class TestBonusLevelAccess(HammerwatchTestBase):
    options = {
        option_names.key_mode: options.KeyMode.option_act_specific,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_true,
    }

    def test_can_complete_bonus1_with_minimal_keys(self):
        self.collect_by_name([item_name.key_bronze_prison, item_name.key_gold_prison])
        for i in range(len(bonus1_regions)-1):
            self.assertTrue(self.can_reach_region(bonus1_regions[i]))
            self.assertFalse(self.can_reach_region(bonus1_regions[i+1]))
            self.collect(self.world.create_item(item_name.key_bonus_prison))


class TestBonusLevelAccessButtonsanityNoBonusKeyRando(HammerwatchTestBase):
    options = {
        option_names.key_mode: options.KeyMode.option_act_specific,
        option_names.randomize_bonus_keys: options.RandomizeBonusKeys.option_false,
        option_names.buttonsanity: options.Buttonsanity.option_normal,
    }

    def test_can_complete_bonus1_with_minimal_keys(self):
        self.collect_by_name([item_name.key_bronze_prison,
                              item_name.key_gold_prison,
                              item_name.btnc_p3_start,
                              item_name.btnc_p3_open_bonus,
                              item_name.btnc_p3_portal])
        self.assertTrue(self.can_reach_region(castle_region_names.n1_start))
        # Bonus keys will be swept as an event
        self.assertTrue(self.can_reach_region(castle_region_names.n1_room1))
        self.assertTrue(self.can_reach_region(castle_region_names.n1_room2))
        # However now we need the room 2 unlock to reach the bonus key so we can't get farther
        self.assertFalse(self.can_reach_region(castle_region_names.n1_room2_unlock))
        self.assertFalse(self.can_reach_region(castle_region_names.n1_room3))
        # Collect the room 2 unlock, so now we can access the north treasure rooms and get the key
        self.collect_by_name(item_name.btnc_n1_cache_n)
        self.assertTrue(self.can_reach_region(castle_region_names.n1_room2_unlock))
        self.assertTrue(self.can_reach_region(castle_region_names.n1_room3))
        # But now we need the east room unlock, so we can't continue
        self.assertFalse(self.can_reach_region(castle_region_names.n1_room3_unlock))
        self.assertFalse(self.can_reach_region(castle_region_names.n1_room3_hall))
        # Collect the room 3 unlock, so now we can access the east treasure room and get the key
        self.collect_by_name(item_name.btnc_n1_cache_ne)
        self.assertTrue(self.can_reach_region(castle_region_names.n1_room3_unlock))
        self.assertFalse(self.can_reach_region(castle_region_names.n1_room3_hall))
        # Collect the hallway unlock so we can access the last room and then we can exit!
        self.collect_by_name(item_name.btnc_n1_hall_top)
        self.assertTrue(self.can_reach_region(castle_region_names.n1_room3_hall))
        self.assertTrue(self.can_reach_region(castle_region_names.n1_room4))
        self.assertTrue(self.can_reach_region(castle_region_names.n1_exit))
