#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if len_sentence:
        first_char = sentence[0]
    else:
        first_char = 'None'
    mul_retu = (len_sentence, first_char)
    return (mul_retu)
