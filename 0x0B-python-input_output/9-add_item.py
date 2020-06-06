#!/usr/bin/python3
""" this file is for comvert files to json"""


import json
import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
""" this file is for comvert files to json"""
if not os.path.isfile("add_item.json") :
    with open('add_item.json', 'w+') as f:
        my_list = []
        for i in range(1, len(sys.argv)):
            my_list.append(sys.argv[i])
        save_to_json_file(my_list, 'add_item.json')
        print(my_list)
else:
    my_list = load_from_json_file('add_item.json')
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, 'add_item.json')
    print(my_list)
    

