from datastructures.linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode


class CircularDoublyLinkedList(DoublyLinkedList):
    """
    A circular doubly linked list is a doubly linked list where the last node points to the first node and the first node points to the last node.
    """

    def __init__(self, head: DNode = None):
        """
        Initializes an empty circular doubly linked list
        """
        super().__init__(head)
        if head:
            self.tail.next = self.head
            self.head.prev = self.tail

    def insertHead(self, node: DNode):
        super().insertHead(node)
        self.tail.next = self.head
        self.head.prev = self.tail

    def insertTail(self, node: DNode):
        super().insertTail(node)
        self.tail.next = self.head
        self.head.prev = self.tail

    def insert(self, node: DNode, position: int):
        super().insert(node, position)
        self.tail.next = self.head
        self.head.prev = self.tail
