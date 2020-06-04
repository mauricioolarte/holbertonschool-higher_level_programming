#!/usr/bin/python3
""" this file is for comvert files to json"""

import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

# def save_to_json_file(my_obj, filename):
#     """ this file is for comvert files to json"""
#     string = json.dumps(my_obj)
#     with open(filename, 'w') as f:
#         f.write(string)


# def load_from_json_file(filename):
#     """ this file is for comvert files to json"""
#     with open(filename, 'r') as f:
#         string = f.read()
#     return(json.loads(string))
with open("add_item.json", 'w+') as f:
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
# else:
#     my_list = []
#     for i in range(1, len(sys.argv)):
#         my_list.append(sys.argv[i])
#         save_to_json_file(my_list,"add_item.json")
