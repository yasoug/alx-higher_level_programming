#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        f = sum(b for a, b in my_list)
        return (sum(a*b for a, b in my_list)/f) if f > 0 else 0
    return (0)
