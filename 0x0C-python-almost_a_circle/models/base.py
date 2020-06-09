#!/usr/bin/python3
"""doc"""


import json
"""doc"""


class Base:
    """doc"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """doc"""
        if list_dictionaries is None:
            return ('[]')
        else:
            return json.dumps(str(list_dictionaries))
