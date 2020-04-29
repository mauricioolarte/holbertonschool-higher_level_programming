#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            ascii_stri = ord(str[i]) - 32
        else:
            ascii_stri = ord(str[i])
        print('{:c}'.format(ascii_stri), end='')
    print()
