import unittest

from src.create_character import (get_stat_mod, get_class, get_background,
                                  get_alignment, get_ancestry, get_stat,
                                  get_hp, get_gold, CLASSES,
                                  BACKGROUND, ALIGNMENT, ANCESTRY)


class TestGetStatMod(unittest.TestCase):
    """Testing get_stat_mod function"""

    def test_ten_score_gives_zero(self):
        """
        Testing that when a 10 is rolled
        it returns zero
        """
        self.assertEqual(get_stat_mod(10), 0)

    def test_highest_roll_is_bound(self):
        """
        Testing that when a 20 is rolled, the
        stat mod correctly enforces the bounds.
        So nothing over 4 or under -4 is returned.
        """
        self.assertEqual(get_stat_mod(20), 4)


class TestGetClass(unittest.TestCase):
    """Testing get_class function"""

    def test_returns_class_from_classes(self):
        """
        Testing that the returned class
        is actually present in the CLASSES list
        """
        self.assertIn(get_class(CLASSES), CLASSES)

    def test_class_is_string(self):
        """
        Testing that when it retrieves from CLASSES
        the variable returned is actually an instance
        of string
        """
        self.assertIsInstance(get_class(CLASSES), str)


class TestGetBackground(unittest.TestCase):
    """Tests for get_background function"""

    def test_returns_background_from_background(self):
        """
        Testing that the returned background
        is actually present in the BACKGROUND list
        """
        self.assertIn(get_background(BACKGROUND), BACKGROUND)

    def test_background_is_string(self):
        """
        Testing that when it retrieves from BACKGROUND
        the variable returned is actually an instance
        of string
        """
        self.assertIsInstance(get_background(BACKGROUND), str)


class TestGetAlignment(unittest.TestCase):
    """Tests for get_alignment function"""

    def test_returns_alignment_from_alignment(self):
        """
        Testing that the returned alignment
        is actually present in the ALIGNMENT list
        """
        self.assertIn(get_alignment(ALIGNMENT), ALIGNMENT)

    def test_alignment_is_string(self):
        """
        Testing that when it retrieves from ALIGNMENT
        the variable returned is actually an instance
        of string
        """
        self.assertIsInstance(get_alignment(ALIGNMENT), str)


class TestGetAncestry(unittest.TestCase):
    """Tests for get_ancestry function"""

    def test_returns_ancestry_from_ancestry(self):
        """
        Testing that the returned ancestry
        is actually present in the ANCESTRY list
        """
        self.assertIn(get_ancestry(ANCESTRY), ANCESTRY)

    def test_returns_dict_with_name_and_talent(self):
        """
        Testing that the dictionary retrieved using
        get_ancestry returns dictionary with name
        and talent keys
        """
        ancestry = get_ancestry(ANCESTRY)
        self.assertIn("name", ancestry)
        self.assertIn("talent", ancestry)


class TestGetStat(unittest.TestCase):
    """Tests for get_stat function"""

    def test_always_within_3_to_18(self):
        """
        Testing roll 100 times and the result
        of a 3d6 roll that the returned value
        is always between 3 and 18
        """
        for _ in range(100):
            result = get_stat()
            self.assertGreaterEqual(result, 3)
            self.assertLessEqual(result, 18)

    def test_returns_integer(self):
        """
        Testing that get_stat returns int type
        """
        self.assertIsInstance(get_stat(), int)


class TestGetHp(unittest.TestCase):
    """Tests for get_hp function"""

    def test_negative_con_level_0_character_still_has_1_hp(self):
        """
        Testing character that is not classed at level 0
        with a con mod of -3 gets 1 health point
        """
        self.assertEqual(get_hp(-3, None), 1)

    def test_classed_character_hp_between_hit_dice(self):
        """
        Testing roll 100 times that when
        creating classed character passing the constitution mod,
        and pulling the hit dice for the class from the HIT_DICE
        dictionary that the returned hp value is between the
        hit dice range plus constitution mod
        """
        for _ in range(100):
            hp = get_hp(2, "Fighter")
            self.assertGreaterEqual(hp, 3)
            self.assertLessEqual(hp, 10)


class TestGetGold(unittest.TestCase):
    """Tests for get_gold function"""

    def test_within_2d6_range(self):
        """
        Testing by rolling 100 times that when
        it rolls the dice it always returns a
        number between 2 and 12
        """
        for _ in range(100):
            result = get_gold()
            self.assertGreaterEqual(result, 2)
            self.assertLessEqual(result, 12)

    def test_returns_integer(self):
        """
        Testing that the returned integer of the
        function is always an instance of integer
        """
        self.assertIsInstance(get_gold(), int)


if __name__ == "__main__":
    unittest.main()
