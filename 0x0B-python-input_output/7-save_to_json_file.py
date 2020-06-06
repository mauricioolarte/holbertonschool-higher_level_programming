#!/usr/bin/python3
""" this file is for comvert files to json"""

import json


def save_to_json_file(my_obj, filename):
    """ this file is for comvert files to json"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
