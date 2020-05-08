#!/usr/bin/python3
def roman_to_int(roman_string):
    tabconv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    i = 0
    while i < len(roman_string) - 1:
        if tabconv[roman_string[i]] < tabconv[roman_string[i + 1]]:
            integer = integer - tabconv[roman_string[i]]
        else:
            integer = integer + tabconv[roman_string[i]]
        i = i + 1
    integer = integer + tabconv[roman_string[i]]
    return (integer)
