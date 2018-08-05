"""
This module is part og assignment 9.1 and
the final project
"""

import unittest
from src import utils as utils
import datetime


class UnitTest(unittest.TestCase):

    def setUp(self):
        """
        :return: NA
        Set Up test data required
        """
        self.x = {'a': 1, 'b': 52, 'd': 6}
        self.y = ['a', 'c', 'd']

    def test_float_str(self):
        """
        :return: NA
        Float is converted to Int
        """
        self.assertEqual(utils.to_int(123.08734569873456), int(123))

    def test_invalid_str(self):
        """
        :return: NA
        String cannot be converted to int. Returns None
        """
        self.assertEqual(utils.to_int('TEST STRING'), 'None')

    def test_int_input(self):
        """
        :return: NA
        Int is returned as Int
        """
        self.assertEqual(utils.to_int(986220943), int(986220943))

    def test_get_value_xq(self):
        """
        :return: NA
        Search for the corresponding value of q in x
        """
        self.assertEqual(utils.get_value(self.x, 'q'), 'None')

    def test_get_value_xa(self):
        """
        :return: NA
        Search for the corresponding value of a in x
        """
        self.assertEqual(utils.get_value(self.x, 'a'), 1)

    def test_get_value_xb(self):
        """
        :return: NA
        Search for the corresponding value of b in x
        """
        self.assertEqual(utils.get_value(self.x, 'b'), 52)

    def test_get_value_yb(self):
        """
        :return: NA
        Search for the corresponding value of b in y
        """
        self.assertEqual(utils.get_value(self.y, 'b'), 'None')

    def test_get_value_yd(self):
        """
        :return: NA
        Search for the corresponding value of d in y
        """
        self.assertEqual(utils.get_value(self.y, 'd'), 2)

    def test_get_value_missingoneinput(self):
        """
        :return: NA
        Missing one input
        """
        with self.assertRaises(TypeError):
            utils.get_value(self.y)

    def test_get_value_missingallinputs(self):
        """
        :return: NA
        Missing all inputs
        """
        with self.assertRaises(TypeError):
            utils.get_value()

    def test_get_value_randomstringsinput(self):
        """
        :return: NA
        Search for a random string
        """
        self.assertEqual(utils.get_value('asdlk;jasdjasdljasdljasd','125nj15knjhpo1n5+++++'), 'None')

    def test_get_date_joined_valid(self):
        """
        :return: NA
        Try joining different input year and date format
        """
        self.assertEqual(utils.get_date_joined(2010, 'Sep-1'), datetime.date(2010,9,1))

    def test_get_date_joined_invalidinputs(self):
        """
        :return: NA
        Date function with no matching input type
        """
        with self.assertRaises(TypeError):
            utils.get_date_joined(2010, 'xx')

    def test_get_date_joined_missingallinputs(self):
        """
        :return: NA
        Date function missing all inputs
        """
        with self.assertRaises(TypeError):
            utils.get_date_joined()

if __name__ == '__main__':
    unittest.main()
