#!/usr/bin/python3
"""
Module that defines the add_attribute function
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible

    Args:
        obj: The object to add the attribute to
        attribute: The name of the attribute to add
        value: The value of the attribute

    Raises:
        TypeError: If the object can't have new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
