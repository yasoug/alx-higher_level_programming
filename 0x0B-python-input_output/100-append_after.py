#!/usr/bin/python3
"""append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    temp = ""
    with open(filename, mode="r+", encoding="utf-8") as f:
        for i in f:
            temp += i
            if search_string in i:
                temp += new_string

    with open(filename, mode="w") as File:
        File.write(temp)
