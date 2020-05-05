#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return ("None")
    for i in range(0, len(my_list)):
        if i == int(idx):
            return (my_list[i])
if __name__ == '__main__':
    element_at([], int)
