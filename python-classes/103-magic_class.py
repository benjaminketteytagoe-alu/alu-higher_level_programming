#!/usr/bin/python3
"""
MagicClass that replicates the given bytecode behavior.
This class represents a circle with radius validation.
"""

import math


class MagicClass:
    """A class that represents a circle with radius validation."""
    
    def __init__(self, radius=0):
        """
        Initialize MagicClass with a radius.
        
        Args:
            radius: The radius of the circle (must be int or float)
            
        Raises:
            TypeError: If radius is not a number (int or float)
        """
        self.__radius = 0
        
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        
        self.__radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return self.__radius ** 2 * math.pi
    
    def circumference(self):
        """
        Calculate the circumference of the circle.
        
        Returns:
            float: The circumference of the circle (2 × π × radius)
        """
        return 2 * math.pi * self.__radius
