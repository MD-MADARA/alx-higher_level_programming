#!/usr/bin/python3
""" Singly linked list """


class Node:
    """ Node class """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

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
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ SinglyLinkedList class """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            if self.__head.data > new.data:
                new.next_node = self.__head
                self.__head = new
            else:
                tmp = self.__head
                while tmp.next_node is not None:
                    if tmp.next_node.data > new.data:
                        new.next_node = tmp.next_node
                        tmp.next_node = new
                        return
                    tmp = tmp.next_node
                tmp.next_node = new

    def __str__(self):
        tmp = self.__head
        list_string = ""
        while tmp is not None:
            list_string += str(tmp.data)
            if tmp.next_node is not None:
                list_string += "\n"
            tmp = tmp.next_node
        return list_string
