#!/usr/bin/python3
"""this module open a file"""


def read_file(filename=""):
    """this module open a file"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
