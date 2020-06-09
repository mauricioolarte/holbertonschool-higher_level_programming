#!/usr/bin/python3
"""Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


import json
"""doc"""


class Base:
    """doc"""

    __nb_objects = 0
    """doc"""

    def __init__(self, id=None):
        """doc"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """doc"""
        if list_dictionaries is None:
            return ([])
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """doc"""
        if json_string is None:
            return ([])
        else:
            return json.loads(json_string)

    # @classmethod
    # def create(cls, **dictionary):
    #     return 
            

