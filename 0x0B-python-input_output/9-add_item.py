#!/usr/bin/python3
""" this file is for comvert files to json"""


import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

def load_save:
    """ this file is for comvert files to json"""
    with open("add_item.json",'w+') as f:
        count = 0
        for line in f:
            count += 1
    if count == 0:
        my_list = []
        for i in range(1, len(sys.argv)):
            my_list.append(sys.argv[i])
            save_to_json_file(my_list,"add_item.json")

    if len(load_from_json_file("add_item.json")) != 0:
        my_list = load_from_json_file("add_item.json")
        for i in range(1, len(sys.argv)):
            my_list.append(sys.argv[i])
    save_to_json_file(my_list,"add_item.json")
if __name__ = '__main__':
    def load_save