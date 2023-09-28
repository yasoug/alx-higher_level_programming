#!/usr/bin/python3
"""Module for find_peak function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""

    size = len(list_of_integers)
    if size == 0:
        return None

    if size == 1:
        return list_of_integers[0]

    if list_of_integers[0] > list_of_integers[size - 1]:
        return find_peak(list_of_integers[:(size + 1)//2])
    else:
        return find_peak(list_of_integers[size//2:])
