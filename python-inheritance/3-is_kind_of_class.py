#!/usr/bin/python3
"""Define function checking if object is instance of or inherits from class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or inherits from it."""
    return isinstance(obj, a_class)
