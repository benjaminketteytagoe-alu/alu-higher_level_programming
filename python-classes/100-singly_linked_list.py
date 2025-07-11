#!/usr/bin/python3
"""
Module that defines Node and SinglyLinkedList classes
"""


class Node:
    """
    Node class that defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node

        Args:
            data: The data value for the node (must be integer)
            next_node: The next node in the list (must be Node or None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data value
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value

        Args:
            value: The data value (must be integer)

        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node

        Args:
            value: The next node (must be Node or None)

        Raises:
            TypeError: If value is not a Node object or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class that defines a singly linked list
    """

    def __init__(self):
        """
        Initialize an empty singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list

        Args:
            value: The value to insert (must be integer)
        """
        new_node = Node(value)

        # If list is empty or new value is smaller than head
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Find the correct position to insert
        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        # Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        String representation of the linked list
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
