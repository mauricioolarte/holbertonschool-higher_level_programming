#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            if i == 0 and j == 1:
                print('01', end='')
            else:
                print(', {}{}'.format(i, j), end='')
print()