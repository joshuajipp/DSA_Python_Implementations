from datastructures.nodes.SNode import SNode
from datastructures.linear.SLL import SinglyLinkedList


class LinkedListQueue(SinglyLinkedList):
    """
    A queue implementation with the linked list implementation.
    """

    def __init__(self, head: SNode = None):
        """
        Initializes the queue with an empty SinglyLinkedList.
        """
        super().__init__(head)

    def enqueue(self, node: SNode):
        """
        Adds a node to the end of the queue.

        Args:
            node (Node): Node to be added to the end of the queue.
        """
        super().insertTail(node)

    def dequeue(self) -> SNode:
        """
        Removes and returns the first node in the queue.

        Returns:
            Node: The first node in the queue.
        """
        if self.head is None:
            return None
        first_node = self.head
        super().deleteHead()
        return first_node.val

    def isEmpty(self) -> bool:
        """

        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.head is None

    def peek(self) -> SNode:
        """
        Returns the first node in the queue without removing it.

        Returns:
            Node: The first node in the queue.
        """
        if self.head is not None:
            return self.head.val

        return None

    def contains(self, targetValue: int) -> bool:
        """
        Checks if the queue contains a node with the given value.

        Args:
            targetValue (int): The value to be searched for in the queue.

        Returns:
            bool: True if the queue contains a node with the given value, False otherwise.
        """
        return super().search(targetValue) is not None

    def clear(self):
        return super().clear()

    def printList(self):
        return super().printList()

    def insertHead(self, node: SNode):
        pass

    def insertTail(self, node: SNode):
        pass

    def deleteHead(self):
        pass

    def deleteTail(self):
        pass

    def insert(self, node: SNode):
        pass

    def sortedInsert(self, node: SNode):
        pass

    def isSorted(self):
        pass

    def sort(self):
        pass

    def search(self, search_target: int):
        pass

    def delete(self, targetValue: int):
        pass
