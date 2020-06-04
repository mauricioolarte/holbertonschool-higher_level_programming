#!/usr/bin/python3
"""this module open a file"""


def append_write(filename="", text=""):
    """this module open a file"""
    with open(filename, 'a') as f:
        s_towrite = str(text)
        number_character = f.write(s_towrite)
    return number_character
