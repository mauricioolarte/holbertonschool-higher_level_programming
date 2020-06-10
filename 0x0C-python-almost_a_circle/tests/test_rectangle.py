#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""

import unittest
from models.rectangle import Rectangle

class TestBaseMethods(unittest.TestCase):
    """ this tests methods of base
        Atributes:
            All
    """

    @classmethod
    def test_setUpClass(self):
        print("Base setUpClass")

    @classmethod
    def test_tearDownClass(self):
        print("base tearDownClass")
  
    def test_setUp(self):
        print("base setUp")

    def test_tearDown(self):
        print("base tearDown")

    def test_foo(self):
        self.assertTrue(True)

    
if __name__ == '__main__':
    unittest.main()
