#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """inverts operators == and !="""
    def __init__(self, num):
        """initialize input"""
        self.num = num

    def __ne__(self, value):
        """override != to =="""
        return self.num == value

    def __eq__(self, value):
        """override == to !="""
        return self.num != value
