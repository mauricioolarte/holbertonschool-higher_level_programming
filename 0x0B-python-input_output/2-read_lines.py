#!/usr/bin/python3
"""this module open a file"""


def read_lines(filename="", nb_lines=0):
    """this module open a file"""
    with open(filename) as f:
        number_lines = 0
        for line in f:
            number_lines += 1
    with open(filename) as f:
        if nb_lines <= 0 or nb_lines > number_lines:
            a_file = f.read()
            print(a_file, end='')
        else:
            for line in range(nb_lines):
                a_line = f.readline()
                print(a_line, end='')
