#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return
    for i in range(0, len(my_list)-1):
        if i == int(idx):
            return (my_list[1])
if __name__ == '__main__':
    element_at([], int)
