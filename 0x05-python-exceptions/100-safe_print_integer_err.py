#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    mes = ""
    try:
        print('{:d}'.format(value))
        return(True)
    except ValueError as err:
        sys.stderr.write('Exception: %s\n' % str(err))
        return(False)
