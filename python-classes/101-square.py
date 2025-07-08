#!/usr/bin/python3
"""
Defines a Square class with size and position attributes,
including area calculation and printing capabilities.
"""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides. Defaults to 0.
            position (tuple): Tuple of two positive integers representing
                the position offset. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): Tuple of two positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' considering position.

        If size is 0, prints an empty line.
        Position defines the offset (spaces and newlines).
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print square rows with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation of the square for printing."""
        if self.__size == 0:
            return ""

        lines = []
        # Vertical offset (newlines)
        lines.extend([""] * self.__position[1])

        # Square lines with horizontal offset
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)


