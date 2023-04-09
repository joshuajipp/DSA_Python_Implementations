from datastructures.nodes.DNode import Node


class DoublyLinkedList:
    def __init__(self):
        """
        Initializes an empty doubly linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def insertHead(self, node: Node):
        """
        Inserts a node at the beginning of the doubly linked list
        """
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insertTail(self, node: Node):
        """
        Inserts a node at the end of the doubly linked list
        """
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
