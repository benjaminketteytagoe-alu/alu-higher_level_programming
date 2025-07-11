#!/usr/bin/python3
"""
Module that defines a Square class
"""


class Square:
    """
    Square class that defines a square by size and position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square

        Args:
            size: The size of the square (default 0)
            position: The position of the square (default (0, 0))
        """
        self.size = size
        self.position = position

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
            value: The size value (must be integer >= 0)

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square

        Args:
            value: The position tuple (must be tuple of 2 positive integers)

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character #
        Position is used for spacing
        """
        if self.__size == 0:
            print()
            return

        # Print vertical spacing (position[1] empty lines)
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal spacing
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        String representation of the square
        Same behavior as my_print()
        """
        result = []

        if self.__size == 0:
            return ""

        # Add vertical spacing (position[1] empty lines)
        for _ in range(self.__position[1]):
            result.append("")

        # Add the square with horizontal spacing
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(result)
