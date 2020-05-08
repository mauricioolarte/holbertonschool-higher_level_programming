#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_element = 0
    new_list = set(my_list)
    for ele in new_list:
        add_element = add_element + ele
    return (add_element)
