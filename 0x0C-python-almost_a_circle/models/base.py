#!/usr/bin/python3
"""doc"""


import json
"""doc"""


class Base:
    """doc"""

    __nb_objects = 0

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
            

