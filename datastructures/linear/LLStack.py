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
        super().insertHead(node)

    def pop(self) -> SNode:
        """
        Remove the head node and return it.

        Returns:
            Node: Head node of the linked list.
        """
        node = self.head
        super().deleteHead()
        return node.val

    def peek(self):
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

    def contains(self, targetValue) -> bool:
        """
        Check if the linked list contains a node with the given target value.

        Args:
            targetValue (int): The value to be searched in the linked list.

        Returns:
            bool: True if the linked list contains the target value, False otherwise.
        """
        return super().search(targetValue) is not None

    def printList(self):
        super().printList()

    def clear(self):
        super().clear()

    def insertHead(self, node: SNode):
        pass

    def insertTail(self, node: SNode):
        pass

    def deleteHead(self):
        pass

    def deleteTail(self):
        pass

    def insert(self, node: SNode, position: int):
        pass

    def sortedInsert(self, node: SNode):
        pass

    def isSorted(self):
        pass

    def sort(self):
        pass

    def search(self, search_target):
        pass

    def delete(self, targetValue):
        pass
