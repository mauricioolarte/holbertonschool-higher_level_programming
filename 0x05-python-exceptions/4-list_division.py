#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    mens = ""
    for i in range(list_length):
        new_list.append(0)
    for i in range(0, list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            new_list[i] = 0
            mens = "division by 0"
        except TypeError:
            new_list[i] = 0
            mens = "wrong type"
        except IndexError:
            new_list[i] = 0
            mens = "out of range"
        finally:
            print (mens)
    return (new_list)
            