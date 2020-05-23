#!/usr/bin/python3
"""


"""


def text_indentation(text):
    if not text:
        raise TypeError('text must be a string')
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in text:
        if i is ' ' and previo in ['.', '?', ':']:
                continue
        if i in ['.', '?', ':']:
            print("{}\n".format(i))
        else:
            print(i, end='')
        previo = i
if __name__ == '__main__':
    import doctest
    doctest.testfile(5-text_indentation)
