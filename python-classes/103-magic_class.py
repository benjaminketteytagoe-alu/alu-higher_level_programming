#!/usr/bin/python3
"""
Defines a MagicClass that mimics the behavior described
by the given Python bytecode for radius validation,
area calculation, and circumference.
"""

import math


class MagicClass:
    """A class that represents a circle with radius,
    providing methods to calculate area and circumference."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a given radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius

