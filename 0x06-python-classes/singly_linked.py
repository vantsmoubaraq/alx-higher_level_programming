#!/usr/bin/python3

"""class Node
    Implements a singly_linked list"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if (isinstance(value,int) is False):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    
    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (value is None or isinstance(value,Node) is True):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

"""class Singly_linked_list:
        Implements a singly_linked_list"""

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):

        if (self.__head is None):
            self.__head = Node(value, None)

        elif (value <= self.__head.data):
            new = Node(value,self.__head)
            self.__head = new
        else:

            tmp = self.__head

            while(tmp.next_node is not None and tmp.next_node.data <= value):
                tmp = tmp.next_node

            ptr = tmp.next_node
            tmp.next_node = Node(value,ptr)

    def __str__(self):
        current = self.__head
        objects = ""

        while(current is not None):
            objects = objects + str(current.data) + '\n'
            current = current.next_node
        return objects[:-1]
            
