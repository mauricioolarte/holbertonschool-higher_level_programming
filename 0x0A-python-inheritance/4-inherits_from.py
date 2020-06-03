#!/usr/bin/python3
""" this module have a fuction tha evalue if a obje is intance of class"""


def inherits_from(obj, a_class):
    """return a tru if objecs is part of class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return (True)
    return(False)
