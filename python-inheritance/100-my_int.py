#!/usr/bin/python3
"""
Module that defines the MyInt class
"""


class MyInt(int):
    """
    MyInt is a rebel class that inherits from int
    with inverted == and != operators
    """

    def __eq__(self, other):
        """
        Inverted equality operator
        Returns False when values are equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality operator
        Returns True when values are equal
        """
        return super().__eq__(other)
