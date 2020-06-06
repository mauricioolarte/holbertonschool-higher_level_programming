#!/usr/bin/python3
""" this file is for comvert files to json"""

def class_to_json(obj):
    """ this file is for comvert files to json"""
    d = {}
    for attr, value in obj.__dict__.items():
        d[attr] = value
    return d
