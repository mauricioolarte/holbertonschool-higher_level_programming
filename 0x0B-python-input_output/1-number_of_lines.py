#!/usr/bin/python3
"""this module open a file"""


def number_of_lines(filename=""):
    """this module open a file"""
    with open(filename) as f:
        number_lines = 0
        for line in f:
            number_lines += 1
    return number_lines
