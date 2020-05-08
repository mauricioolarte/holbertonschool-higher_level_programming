#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = []
    for a, b in a_dictionary.items():
        new_list.append((a, (b * 2)))
    return(dict(new_list))
