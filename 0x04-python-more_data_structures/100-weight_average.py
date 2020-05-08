#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    sum_prom = 0
    sum_div = 0
    for i in range(len(my_list)):
        sum_prom += (my_list[i][0] * my_list[i][1])
        sum_div += my_list[i][1]
    weigt_a = sum_prom / sum_div
    return(weigt_a)
