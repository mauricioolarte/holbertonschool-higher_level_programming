#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_expectec_function(self):
        max = max_integer([1, 2, 3, 4])

        # validate the result expected
        self.assertEqual(4, max)

    def test_negative_list(self):
        max = max_integer([-1, -2, -5, -7])

        # validate the result expected
        self.assertEqual(-1, max)

    def test_all_equals(self):
        max = max_integer([0, 0, 0, 0, 0])

        # validate the result expected
        self.assertEqual(0, max)

        # validate the result expected
    #     self.assertnotEqual(5, max)
if __name__ == '__main__':
    unittest.main()
