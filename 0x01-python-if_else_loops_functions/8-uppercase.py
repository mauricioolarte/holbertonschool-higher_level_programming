#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            ascii_stri = ord(str[i]) - 32
            # print('{:c}'.format(ord(str[i]) - 32), end='')
        else:
            ascii_stri = ord(str[i])
            # print(str[i], end='')
        print('{:c}'.format(ascii_stri), end='')
    print()
uppercase("Holberton School 98 Battery street")
