#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""


import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """ this tests methods of base
        Atributes:
            All
    """

    @classmethod
    def setUpClass(self):
        print("Base setUpClass")
    
    @classmethod
    def tearDownClass(self):
        print("base tearDownClass")
    def setUp(self):
        print("base setUp")
    def tearDown(self):
        print("base tearDown")
    def test_foo(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

