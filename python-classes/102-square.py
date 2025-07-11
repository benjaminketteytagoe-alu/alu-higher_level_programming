#!/usr/bin/python3
"""
Module that defines a Square class with comparison operators
"""


class Square:
    """
    Square class that defines a square by size with comparison operators
    """

    def __init__(self, size=0):
        """
        Initialize a new Square

        Args:
            size: The size of the square (default 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value: The size value (must be number >= 0)

        Raises:
            TypeError: If value is not a number
            ValueError: If value is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Equal comparison based on area
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not equal comparison based on area
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison based on area
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison based on area
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison based on area
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison based on area
        """
        return self.area() >= other.area()
