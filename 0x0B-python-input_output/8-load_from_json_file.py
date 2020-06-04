#!/usr/bin/python3
""" this file is for comvert files to json"""

import json


def load_from_json_file(filename):
    """ this file is for comvert files to json"""
    with open(filename) as f:
        string = f.read()
    return(json.loads(string))
