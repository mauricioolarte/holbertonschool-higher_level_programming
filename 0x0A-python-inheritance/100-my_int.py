#!/usr/bin/python3
""" this module have a fuction tha evalue if a obje is intance of class"""


class MyInt(int):
    """doc"""
    def __init__(self, a):
        """doc"""
        self.a = a

    def __eq__(self, a):
        """doc"""
        if(self.a == a):
            return False
        else:
            return True

    def __ne__(self, a):
        """doc"""
        if(self.a != a):
            return False
        else:
            return True
