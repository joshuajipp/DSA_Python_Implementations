from datastructures.nodes.SNode import SNode
from datastructures.linear.SLL import SinglyLinkedList


class LinkedListQueue(SinglyLinkedList):
    """
    A queue implementation with the linked list implementation.
    """

    def __init__(self):
        """
        Initializes the queue with an empty SinglyLinkedList.
        """
        super().__init__()

    def enqueue(self, node: SNode):
        """
        Adds a node to the end of the queue.

        Args:
            node (Node): Node to be added to the end of the queue.
        """
        self.insertTail(node)

    def dequeue(self):
        """
        Removes and returns the first node in the queue.

        Returns:
            Node: The first node in the queue.
        """
        if self.head is None:
            return None
        first_node = self.head
        self.deleteHead()
        return first_node.val

    def isEmpty(self):
        """

                    Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.head is None

    def peek(self):
        """
        Returns the first node in the queue without removing it.

        Returns:
            Node: The first node in the queue.
        """
        if self.head is not None:
            return self.head.val

        return None

    def clear(self):
        return super().clear()

    def printList(self):
        return super().printList()
