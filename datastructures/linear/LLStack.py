from datastructures.linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode


class LinkedListStack(SinglyLinkedList):
    """
    A linked list implementation of a stack data structure.
    """

    def __init__(self):
        super().__init__()

    def push(self, val):
        """
        Add an element to the top of the stack.

        Args:
            val: The value to be added to the stack.
        """
        node = SNode(val)
        self.insertHead(node)

    def pop(self):
        """
        Remove and return the top element of the stack.

        Returns:
            The value of the top element of the stack.
        """
        if self.head is None:
            return None
        val = self.head.val
        self.deleteHead()
        return val

    def peek(self):
        """
        Return the value of the top element of the stack without removing it.

        Returns:
            The value of the top element of the stack.
        """
        if self.head is None:
            return None
        return self.head.val
