#!/usr/bin/python3
"""Define a function that checks if object is exactly instance of class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) is a_class
