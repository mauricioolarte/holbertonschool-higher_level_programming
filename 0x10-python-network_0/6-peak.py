#!/bin/bash/python3
""" max of  list """


def find_peak(list_of_integers):
    """ peak of a list"""
    if len(list_of_integers) > 0:
        peak = max(list_of_integers)
        return(peak)
    else:
        return(None)
