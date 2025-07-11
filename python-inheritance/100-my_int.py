#!/usr/bin/python3
"""
Module that defines the MyInt class
"""


class MyInt(int):
    """
    MyInt is a rebel class that inherits from int.
    It has == and != operators inverted.
    """
    
    def __eq__(self, other):
        """
        Override equality operator to return the opposite of normal behavior
        
        Args:
            other: The object to compare with
            
        Returns:
            bool: The inverted result of normal equality comparison
        """
        return super().__ne__(other)
    
    def __ne__(self, other):
        """
        Override inequality operator to return the opposite of normal behavior
        
        Args:
            other: The object to compare with
            
        Returns:
            bool: The inverted result of normal inequality comparison
        """
        return super().__eq__(other)
