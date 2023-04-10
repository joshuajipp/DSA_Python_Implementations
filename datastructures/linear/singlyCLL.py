from datastructures.linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode


class SinglyCircularLinkedList(SinglyLinkedList):
    """
    A singly circular linked list implementation that inherits from SinglyLinkedList.
    """

    def __init__(self, head: SNode = None):
        """
        Initialize the linked list with a head node (optional). Set tail to head and size to 0 or 1.

        Args:
            head (Node, optional): Head node of the linked list. Defaults to None.
        """
        super().__init__(head)
        if self.head is not None:
            self.tail.next = self.head  # Set tail's next to head to make it circular

    def insertHead(self, node: SNode):
        """
        Insert a node at the head of the linked list.

        Args:
            node (Node): Node to be inserted at the head.
        """
        super().insertHead(node)
        self.tail.next = self.head

    def insertTail(self, node: SNode):
        """
        Insert a node at the tail of the linked list.

        Args:
            node (Node): Node to be inserted at the tail.
        """
        super().insertTail(node)
        self.tail.next = self.head
