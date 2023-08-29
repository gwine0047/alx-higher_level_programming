#!/bin/usr/python3
"""Module"""


class Node:
    """Declaration of the node class"""
    def __init__(self, data, next_node=None):
        """
        Initialization of the node class
        Args:
            data: input value
            next_node: address of the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Allot data to self"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    def next_node(self):
        """Allot next_node to self"""
        return self.__next_node

    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Declaration of a singly linked list"""
    def __init__(self) -> None:
        """"Initializing the private field"""
        self.__head = None

    def __str__(self) -> str:
        """returning string for SinglyLinkedList printing"""
        result = list()
        temp = self.__head

        while temp is not None:
            result.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
            Sorts nodes data
            Args:
                value: data value
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        temp1, temp2 = self.__head.next_node, self.__head
        while temp1 is not None:
            if value < temp1.data:
                temp2.next_node = Node(value, temp1)
                return
            temp2 = temp1
            temp1 = temp1.next_node
        temp2.next_node = Node(value)
