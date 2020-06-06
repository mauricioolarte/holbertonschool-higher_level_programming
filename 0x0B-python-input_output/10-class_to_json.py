#!/usr/bin/python3
""" this file is for comvert files to json"""

import json


def class_to_json(obj):
    """ this file is for comvert files to json"""
    return(json.dumps(obj.__dict__))