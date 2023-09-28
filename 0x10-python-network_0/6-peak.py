#!/usr/bin/python3
"""Module for find_peak function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""

    if len(list_of_integers) == 0:
        return None

    left = 0
    for i in range(len(list_of_integers)):
        if i:
            left = list_of_integers[i - 1]
        if i < len(list_of_integers) - 1:
            right = list_of_integers[i + 1]
        else:
            right = 0
        if list_of_integers[i] >= left and list_of_integers[i] >= right:
            return list_of_integers[i]
