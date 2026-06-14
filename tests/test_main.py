import unittest

from main import valid_name_input, valid_id_input


class TestValidNameInput(unittest.TestCase):
    """Tests for valid_name_input function"""

    def test_non_empty_name_is_valid(self):
        """
        Testing that valid name passes validation
        """
        self.assertTrue(valid_name_input("Borin"))

    def test_empty_name_is_invalid(self):
        """
        Testing that invalid name (all whitespace)
        does not pass validation
        """
        self.assertFalse(valid_name_input("   "))


class TestValidIdInput(unittest.TestCase):
    """Tests for valid_id_input function"""

    def test_numeric_string_is_valid(self):
        """
        Testing that when user inputs a number
        as a string it passes validation
        """
        self.assertTrue(valid_id_input("5"))

    def test_alphabetic_string_is_invalid(self):
        """
        Testing that when user inputs alphabetic
        string that it does not pass validation
        """
        self.assertFalse(valid_id_input("abc"))


if __name__ == "__main__":
    unittest.main()
