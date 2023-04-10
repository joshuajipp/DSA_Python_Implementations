from datastructures.linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode


class LinkedListStack(SinglyLinkedList):
    def __init__(self, head: SNode = None):
        """
        Initialize the linked list with a head node (optional). Set tail to head and size to 0 or 1.

        Args:
            head (Node, optional): Head node of the linked list. Defaults to None.
        """
        super().__init__(head)

    def push(self, node: SNode):
        """
        Insert a node at the head of the linked list.

        Args:
            node (Node): Node to be inserted at the head.
        """
        self.insertHead(node)

    def pop(self) -> SNode:
        """
        Remove the head node and return it.

        Returns:
            Node: Head node of the linked list.
        """
        node = self.head
        self.deleteHead()
        return node.val

    def peek(self) -> int:
        """
        Return the head node.

        Returns:
            Node: Head node of the linked list.
        """
        if self.head is None:
            return None
        return self.head.val

    def isEmpty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def printList(self):
        return super().printList()
