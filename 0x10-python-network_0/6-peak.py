#!/usr/bin/python3
"""Module for find_peak function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""

    size = len(list_of_integers)
    if size == 0:
        return None

    left = 0
    right = size - 1
    li = list_of_integers

    while left < right:
        mid = (left + right) // 2
        if li[mid] > li[mid - 1] and li[mid] > li[mid + 1]:
            return li[mid]
        elif li[mid] < li[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return li[left]
