#!/usr/bin/python3
""" this module print a list of method"""


class MyList(list):
    """ this module print a list of method"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
if __name__ == "__main__":
    import doctest
    doctest.testfile(tests/1-my_list.txt)
