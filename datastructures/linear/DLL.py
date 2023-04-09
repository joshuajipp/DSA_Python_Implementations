from datastructures.nodes.DNode import Node


class DoublyLinkedList:
    def __init__(self):
        """
        Initializes an empty doubly linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def insertHead(self, node: Node):
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

    def insertTail(self, node: Node):
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

    def insert(self, node: Node, index: int):
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

    def sortedInsert(self, node: Node):
        """
        Inserts a node in sorted order in the doubly linked list
        """
        if not self.head:
            self.head = node
            self.tail = node
        elif node.val <= self.head.val:
            self.insertHead(node)
        elif node.val >= self.tail.val:
            self.insertTail(node)
        else:
            curr = self.head
            while curr.next and curr.next.val < node.val:
                curr = curr.next
            node.next = curr.next
            node.prev = curr
            curr.next.prev = node
            curr.next = node
            self.size += 1

    def delete(self, target):
        """Removes the first node containing the target value."""
        if self.head is None:
            return  # List is empty

        if self.head.val == target:
            if self.head.next is None:  # Only one node in the list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return

        current_node = self.head.next
        while current_node is not None:
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

    def isSorted(self):
        """
        Checks if the doubly linked list is sorted in non-descending order
        """
        if not self.head:
            return True
        curr = self.head
        while curr.next:
            if curr.val > curr.next.val:
                return False
            curr = curr.next
        return True

    def printList(self):
        """
        Prints the doubly linked list
        """
        if not self.head:
            print("Empty list")
        else:
            curr = self.head
            while curr:
                print(curr.val, end=" ")
                curr = curr.next
            print()
