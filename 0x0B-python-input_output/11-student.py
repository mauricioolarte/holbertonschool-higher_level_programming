#!/usr/bin/python3
""" this file is for comvert files to json"""


class Student:
    """ this file is for comvert files to json"""

    def __init__(self, first_name, last_name, age):
        """doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """doc"""
        dict = {}
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['age'] = self.age
        return (dict)
