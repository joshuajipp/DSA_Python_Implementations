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

    def insert(self, node: SNode, position: int):
        """
        Insert a node at a given position in the linked list.

        Args:
            node (Node): Node to be inserted.
            position (int): Index position at which the node is to be inserted.

        Raises:
            IndexError: If the given position is out of range (less than 0 or greater than size).
        """
        super().insert(node, position)
        self.tail.next = self.head

    def deleteHead(self):
        """
        Delete the head node of the linked list.
        """
        super().deleteHead()
        if not (self.head is None or self.tail is None):
            self.tail.next = self.head

    def deleteTail(self):
        """
        Delete the tail node of the linked list.
        """
        super().deleteTail()
        if not (self.head is None or self.tail is None):
            self.tail.next = self.head

    def delete(self, targetValue: int):
        """
        Deletes the node with the given target value from the linked list.

        Args:
            targetValue (int): The value of the node to be deleted.

        Returns:
            None: If the linked list is empty or the target node is not found.
        """
        super().delete(targetValue)
        if not (self.head is None or self.tail is None):
            self.tail.next = self.head

    def search(self, search_target: int):
        """
        Searches the linked list for a node with a specific value.

        Args:
            search_target (int): The value to be searched for in the linked list.

        Returns:
            Node: The node with the searched value or None if it is not found.

        """
        return super().search(search_target)
