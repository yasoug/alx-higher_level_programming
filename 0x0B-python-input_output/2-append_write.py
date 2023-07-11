#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a str at the end of a text file and returns the num of chars"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
