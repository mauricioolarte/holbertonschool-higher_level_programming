#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        print('{}'.format(my_list[i]))
if __name__ == '__main__':
    print_list_integer()