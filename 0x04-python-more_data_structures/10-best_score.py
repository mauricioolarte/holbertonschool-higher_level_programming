#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = ''
    if a_dictionary:
        max_score = 0
        for a, b in a_dictionary.items():
            if max_score < b:
                best_key = a
                max_score = b
    else:
        return (None)
    return (best_key)
