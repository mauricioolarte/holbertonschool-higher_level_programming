#!/usr/bin/python3
"""this module if for a class base
Attributes:
            def __init__: constructor method
"""


import json


class Base():
    """ this a base class
    Attributes:
    __init__: construct method
    to_json_string(list_dictionaries): conver dir in json file.
    def from_json_string(json_string): import json file.
    """

    __nb_objects = 0
    """ this count number of objects created"""

    def __init__(self, id=None):
        """ constructor method
        Args:
            id: is the number of the subslass.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        if json_string is None:
            return ([])
        else:
            return json.loads(json_string)
