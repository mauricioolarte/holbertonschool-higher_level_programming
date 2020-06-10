#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""

import unittest
import pep8
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
    
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
