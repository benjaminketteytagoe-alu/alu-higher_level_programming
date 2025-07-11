#!/usr/bin/python3
"""Define a function that returns available attributes and methods."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
