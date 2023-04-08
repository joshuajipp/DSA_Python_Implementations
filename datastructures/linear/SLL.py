from datastructures.nodes.SNode import Node


class SinglyLinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.tail = head
        self.size = 0
        if head is not None:
            self.size = 1

    def insertHead(self, node: Node):
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insertTail(self, node: Node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node: Node, position):
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

    def search(self, node: Node):
        current = self.head
        while current is not None:
            if current.val == node.val:
                return current
            current = current.next
        return None

    def delete_head(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def delete_tail(self):
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

    def delete_node(self, node: Node):
        if self.head is None:
            return
        if self.head == node:
            self.delete_head()
            return
        current = self.head
        while current.next is not None and current.next != node:
            current = current.next
        if current.next == node:
            current.next = node.next
            if node == self.tail:
                self.tail = current
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

    def print_list(self):

        # Print the list length
        print(f"List length: {self.size}")

        # Check if the list is sorted
        if self.isSorted():
            print("Sorted: Yes")
        else:
            print("Sorted: No")

        # Print the list content
        current = self.head

        while current is not None:
            if current.next is None:
                print(current.val)
            else:
                print(current.val, end=" -> ")
            current = current.next
