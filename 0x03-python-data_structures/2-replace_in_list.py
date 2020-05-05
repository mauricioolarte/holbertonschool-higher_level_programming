#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    for i in range(0, len(my_list)):
        if i == int(idx):
            my_list[i] = element
            return (my_list)
if __name__ == '__main__':
    replace_in_list([], int, int)
