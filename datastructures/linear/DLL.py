from datastructures.nodes.DNode import DNode


class DoublyLinkedList:
    def __init__(self, node: DNode = None):
        """
        Initializes an empty doubly linked list
        """
        self.head = node
        self.tail = node
        self.size = 1 if node else 0
        if node:
            node.prev = None
            node.next = None

    def insertHead(self, node: DNode):
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

    def insertTail(self, node: DNode):
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

    def insert(self, node: DNode, index: int):
        """
        Inserts a node at a specified index in the doubly linked list
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.insertHead(node)
        elif index == self.size:
            self.insertTail(node)
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            node.next = curr
            node.prev = curr.prev
            curr.prev.next = node
            curr.prev = node
            self.size += 1

    def sortedInsert(self, node: DNode):
        """
        Inserts a node in the linked list in a sorted order.

        Args:
            node (DNode): The node to be inserted in the linked list.

        Returns:
            None

        """
        if not self.isSorted():
            self.sort()
        if self.head is None or node.val < self.head.val:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.val < node.val:
                current_node = current_node.next
            node.next = current_node.next
            node.prev = current_node
            current_node.next = node
            if node.next is not None:
                node.next.prev = node
            else:
                self.tail = node
        self.size += 1

    def sort(self):
        """
        Sorts the linked list in ascending order using insertion sort algorithm.

        Returns:
            None: If the linked list is empty or contains only one node.
        """
        if self.size <= 1:
            # An empty or single-element list is already sorted
            return

        sorted_head = self.head
        unsorted_head = self.head.next
        sorted_head.prev = None
        sorted_head.next = None
        i = 1
        while unsorted_head is not None and i < self.size:
            node = unsorted_head
            unsorted_head = unsorted_head.next
            node.prev = None
            node.next = None

            if node.val < sorted_head.val:
                node.next = sorted_head
                sorted_head.prev = node
                sorted_head = node
            else:
                current = sorted_head
                j = 1
                while current.next is not None and current.next.val < node.val and j < self.size:
                    current = current.next
                    j += 1
                node.next = current.next
                node.prev = current
                current.next = node
                if node.next is not None and node.next != self.head:
                    node.next.prev = node
                else:
                    self.tail = node
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
        i = 1
        while current_node.next is not None and i < self.size:
            if current_node.val > current_node.next.val:
                # If the current node's value is greater than the next node's value, the list is not sorted
                return False
            current_node = current_node.next
            i += 1

        # If we have reached the end of the list without finding any out-of-order nodes, the list is sorted
        return True

    def delete(self, target):
        """Removes the first node containing the target value."""
        if self.head is None:
            return  # List is empty

        if self.head.val == target:
            if self.size == 1:  # Only one node in the list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return

        current_node = self.head.next
        i = 1
        while current_node is not None and i < self.size:
            if current_node.val == target:
                if current_node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                self.size -= 1
                return
            current_node = current_node.next
            i += 1

    def search(self, val):
        """
        Searches for a node with the given value in the linked list.

        Args:
            val: The value to search for.

        Returns:
            The node with the given value if found, None otherwise.
        """
        current_node = self.head
        while current_node is not None:
            if current_node.val == val:
                return current_node
            current_node = current_node.next
        return None

    def deleteHead(self):
        """
        Deletes the head node of the linked list.

        Returns:
            None
        """
        if self.head is None:
            return
        if self.head.next is None or self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def deleteTail(self):
        """
        Removes the tail node from the linked list.

        Returns:
            The value of the tail node that was removed.
        """
        if self.size == 0:
            return
        elif self.size == 1:
            val = self.head.val
            self.head = None
            self.tail = None
        else:
            val = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return val

    def clear(self):
        """
        Removes all nodes from the linked list.
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
                print(current.val, end=" <-> ")
            current = current.next
