#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigi = number % 10
else:
    lastDigi = -((-number) % 10)
if lastDigi > 5:
    (print('Last digit of {} is {} and is greater than 5'.format(
        number, lastDigi)))
elif lastDigi == 0:
    print('Last digit of {} is {} and is 0'.format(number, lastDigi))
else:
    (print('Last digit of {} is {} and is less than 6 and not 0'.format(
        number, lastDigi)))
