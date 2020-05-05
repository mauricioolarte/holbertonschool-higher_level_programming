#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    new_list = my_list.copy()
    for i in range(0, len(my_list)):
        if i == int(idx):
            new_list[i] = element
            return (new_list)
if __name__ == '__main__':
    new_in_list([], int, int)
