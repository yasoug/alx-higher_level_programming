#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a str to a text file (UTF8) and returns the number of chars"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
