#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class to implement
a singly linked list data structure.

- Node: Represents a node of the singly linked list, storing integer data
  and a reference to the next node.
- SinglyLinkedList: Represents the singly linked list itself, supporting
  sorted insertion of nodes and printing the list.
"""


class Node:
    """Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): Reference to the next node.
                Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node ensuring it is an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node ensuring it is a Node object or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list with one node per line."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the list maintaining sorted order.

        Args:
            value (int): The data value for the new node.
        """
        new_node = Node(value)

        # If list is empty or new node should be first
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse the list to find insertion point
        current = self.__head
        while (
            current.next_node is not None
            and current.next_node.data < value
        ):
            current = current.next_node

        # Insert new node
        new_node.next_node = current.next_node
        current.next_node = new_node

