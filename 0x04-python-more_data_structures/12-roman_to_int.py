#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    total = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dic.keys():
            return 0
        elif dic[i] >= dic[j]:
            total += dic[i]
        else:
            total -= dic[i]
    total += dic[roman_string[-1]]
    return total
