from datastructures.nodes.SNode import Node


class SinglyLinkedList:
    """
    A singly linked list implementation with methods to insert nodes at head, tail or a given position.
    """

    def __init__(self, head: Node = None):
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

    def insertHead(self, node: Node):
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

    def insertTail(self, node: Node):
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

    def insert(self, node: Node, position):
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

    def sortedInsert(self, node: Node):
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
        current = self.head
        while current is not None:
            if current.val == search_target:
                return current
            current = current.next
        return None

    def deleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def deleteTail(self):
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

    def deleteNode(self, targetValue: int):
        if self.head is None:
            return
        if self.head.val == targetValue:
            self.deleteHead()
            return
        current = self.head
        while current.next is not None and current.next.val != targetValue:
            current = current.next
        if current.next is None:
            return
        if current.next == self.tail:
            self.deleteTail()
        else:
            current.next = current.next.next
            self.size -= 1

    def sort(self):
        if self.head is None:
            return
        if self.head == self.tail:
            return
        sorted_head = self.head
        unsorted_head = self.head.next
        sorted_head.next = None
        while unsorted_head is not None:
            node = unsorted_head
            unsorted_head = unsorted_head.next
            if node.val < sorted_head.val:
                node.next = sorted_head
                sorted_head = node
            else:
                current = sorted_head
                while current.next is not None and current.next.val < node.val:
                    current = current.next
                node.next = current.next
                current.next = node
        self.head = sorted_head
        current = self.head
        while current.next is not None:
            current = current.next
        self.tail = current

    def isSorted(self) -> bool:
        if self.head is None or self.head.next is None:
            # An empty or single-element list is always sorted
            return True

        current_node = self.head
        while current_node.next is not None:
            if current_node.val > current_node.next.val:
                # If the current node's value is greater than the next node's value, the list is not sorted
                return False
            current_node = current_node.next

        # If we have reached the end of the list without finding any out-of-order nodes, the list is sorted
        return True

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printList(self):
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
