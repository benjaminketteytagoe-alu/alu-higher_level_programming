#!/usr/bin/python3
"""Define a class MyList that inherits from list."""


class MyList(list):
    """A list with a method to print sorted elements."""

    def print_sorted(self):
        """Print the list in sorted order (ascending)."""
        print(sorted(self))
