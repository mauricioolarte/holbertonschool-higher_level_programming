#!/usr/bin/python3
""" this module print a list of method"""
def lookup(obj):
    """ this fuction return list of method and instances of obj"""
    return (dir(obj))
