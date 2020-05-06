#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) or len(my_list) == 0:
        return (my_list)
    for i in range(0, len(my_list)):
        if i == idx:
            del my_list[i]
    return(my_list)
