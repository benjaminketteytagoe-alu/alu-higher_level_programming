#!/usr/bin/python3

class Node:
    """Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data            # Will invoke setter for validation
        self.next_node = next_node  # Will invoke setter for validation

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list."""

    def __init__(self):
        self.__head = None

    def __str__(self):
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        new_node = Node(value)

        # If list is empty or new node should be first
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse to find the insertion point
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert new_node
        new_node.next_node = current.next_node
        current.next_node = new_node

