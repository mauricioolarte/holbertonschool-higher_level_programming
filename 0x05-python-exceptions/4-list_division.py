#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        new_list.append(0)
    for i in range(0, list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            new_list[i] = 0
            print("division by 0")
        except TypeError:
            new_list[i] = 0
            print("wrong type")
        except IndexError:
            new_list[i] = 0
            print("out of range")
    return(new_list)
