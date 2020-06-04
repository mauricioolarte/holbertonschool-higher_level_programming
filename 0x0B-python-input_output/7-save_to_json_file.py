#!/usr/bin/python3
""" this file is for comvert files to json"""

import json


def save_to_json_file(my_obj, filename):
    """ this file is for comvert files to json"""
    string = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(string)
