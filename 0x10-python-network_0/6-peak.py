#!/usr/bin/python3
""" max of  list """


def find_peak(list_of_integers):
    """ peak of a list"""
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        peak = list_of_integers[-1]
        return(peak)
    else:
        return(None)
