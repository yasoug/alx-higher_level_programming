#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    list_args = load_from_json_file(filename)
except FileNotFoundError:
    list_args = []

for arg in args:
    list_args.append(arg)

save_to_json_file(list_args, filename)
