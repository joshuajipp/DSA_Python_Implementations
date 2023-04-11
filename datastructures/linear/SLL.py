from datastructures.nodes.SNode import SNode


class SinglyLinkedList:
    """
    A singly linked list implementation with methods to insert nodes at head, tail or a given position.
    """

    def __init__(self, head: SNode = None):
        """
        Initialize the linked list with a head node (optional). Set tail to head and size to 0 or 1.

        Args:
            head (Node, optional): Head node of the linked list. Defaults to None.
        """
        self.head = head
        self.tail = head
        self.size = 0
        if head is not None:
            self.size = 1

    def insertHead(self, node: SNode):
        """
        Insert a node at the head of the linked list.

        Args:
            node (Node): Node to be inserted at the head.
        """
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insertTail(self, node: SNode):
        """
        Insert a node at the tail of the linked list.

        Args:
            node (Node): Node to be inserted at the tail.
        """
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node: SNode, position: int):
        """
        Insert a node at a given position in the linked list.

        Args:
            node (Node): Node to be inserted.
            position (int): Index position at which the node is to be inserted.

        Raises:
            IndexError: If the given position is out of range (less than 0 or greater than size).

        """
        if position < 0 or position > self.size:
            raise IndexError('Position out of range')
        if position == 0:
            self.insertHead(node)
        elif position == self.size:
            self.insertTail(node)
        else:
            current = self.head
            for i in range(position-1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def sortedInsert(self, node: SNode):
        """
        Inserts a node in the linked list in a sorted order.

        Args:
            node (Node): The node to be inserted in the linked list.

        Returns:
            None

        """
        if not self.isSorted():
            self.sort()
        if self.head is None or node.val < self.head.val:
            node.next = self.head
            self.head = node
            if node.next is None:
                self.tail = node
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.val < node.val:
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            if node.next is None:
                self.tail = node
        self.size += 1

    def search(self, search_target: int):
        """
        Searches the linked list for a node with a specific value.

        Args:
            search_target (int): The value to be searched for in the linked list.

        Returns:
            Node: The node with the searched value or None if it is not found.

        """
        i = 0
        current = self.head
        while current is not None and i < self.size:
            if current.val == search_target:
                return current
            current = current.next
            i += 1
        return None

    def deleteHead(self):
        """
        Deletes the head node of the linked list.

        Returns:
            None

        """
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def deleteTail(self):
        """
        Deletes the tail node of the linked list.

        Returns:
            None

        """
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.size -= 1

    def delete(self, targetValue: int):
        """
        Deletes the node with the given target value from the linked list.

        Args:
            targetValue (int): The value of the node to be deleted.

        Returns:
            None: If the linked list is empty or the target node is not found.
        """
        if self.head is None:
            return
        if self.head.val == targetValue:
            self.deleteHead()
            return
        current = self.head
        i = 0
        while current.next is not None and current.next.val != targetValue and i < self.size:
            current = current.next
            i += 1
        if current.next is None or i == self.size:
            return
        if current.next == self.tail:
            self.deleteTail()
        else:
            current.next = current.next.next
            self.size -= 1

    def sort(self):
        """
        Sorts the linked list in ascending order using insertion sort algorithm.

        Returns:
            None: If the linked list is empty or contains only one node.
        """
        if self.head is None:
            return
        if self.size == 1:
            return
        sorted_head = self.head
        unsorted_head = self.head.next
        sorted_head.next = None
        i = 1
        while unsorted_head is not None and i < self.size:
            node = unsorted_head
            unsorted_head = unsorted_head.next
            if node.val < sorted_head.val:
                node.next = sorted_head
                sorted_head = node
            else:
                current = sorted_head
                j = 1
                while current.next is not None and current.next.val < node.val and j < self.size:
                    current = current.next
                    j += 1
                node.next = current.next
                current.next = node
            i += 1
        self.head = sorted_head
        current = self.head
        i = 1
        while current.next is not None and i < self.size:
            current = current.next
            i += 1

        self.tail = current

    def isSorted(self) -> bool:
        """
        Checks if the linked list is sorted in ascending order.

        Returns:
            bool: True if the linked list is sorted in ascending order, False otherwise.
        """
        if self.size <= 1:
            # An empty or single-element list is always sorted
            return True

        current_node = self.head
        i = 0
        while current_node.next is not None and i < self.size - 1:
            if current_node.val > current_node.next.val:
                # If the current node's value is greater than the next node's value, the list is not sorted
                return False
            current_node = current_node.next
            i += 1

        # If we have reached the end of the list without finding any out-of-order nodes, the list is sorted
        return True

    def clear(self):
        """
        Clears the linked list by setting head, tail and size to None and 0, respectively.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def printList(self):
        """
        Prints the values of all nodes in the linked list, separated by '->'.
        Also prints the length of the linked list and whether it is sorted or not.
        """
        print(f"List length: {self.size}")

        if self.isSorted():
            print("Sorted: Yes")
        else:
            print("Sorted: No")

        current = self.head

        while current is not None:
            if current.next is None:
                print(current.val)
            else:
                print(current.val, end=" -> ")
            current = current.next
