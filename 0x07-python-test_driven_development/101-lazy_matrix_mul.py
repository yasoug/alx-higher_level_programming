#!/usr/bin/python3
"""module that multiplies 2 matrices using np"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """fct multiplies 2 matrices using the module NumPy"""

    return np.dot(m_a, m_b)
