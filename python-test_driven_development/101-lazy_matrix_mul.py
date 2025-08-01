#!/usr/bin/python3
"""
Lazy matrix multiplication module using NumPy.
Contains a function to multiply two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers or floats)
        m_b: Second matrix (list of lists of integers or floats)

    Returns:
        A NumPy array representing the multiplication of m_a and m_b

    Raises:
        ValueError: If matrices don't meet requirements or can't be multiplied
    """
    return np.matmul(m_a, m_b)
