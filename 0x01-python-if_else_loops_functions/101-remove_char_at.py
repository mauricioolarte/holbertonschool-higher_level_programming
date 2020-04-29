#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) == 0:
        str_new = ""
        return (str_new)
    str_new = str[0:n] + str[n+1:]
    return (str_new)
