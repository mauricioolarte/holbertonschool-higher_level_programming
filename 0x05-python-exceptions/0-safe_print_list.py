#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in range(0, x):
            print('{}'.format(my_list[i]), end='')
            counter = counter +  1
        print()
    except:
        print()
        return(counter)
        # counter = 0
        # for i in my_list:
        #     print('{}'.format(i), end='')
        #     counter = counter +  1
        # print()
    return(counter)
