#!/usr/bin/python3
"""this module open a file"""


def write_file(filename="", text=""):
    """this module open a file"""
    with open(filename, 'w') as f:
        s_towrite = str(text)
        number_character = f.write(s_towrite)
    return number_character
