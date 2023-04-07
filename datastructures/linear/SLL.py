from datastructures.nodes.SNode import Node


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if head is not None:
            self.size = 1

    def insert_head(self, node: Node):
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insert_tail(self, node: Node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position < 0 or position > self.size:
            raise IndexError('Position out of range')
        if position == 0:
            self.insert_head(node)
        elif position == self.size:
            self.insert_tail(node)
        else:
            current = self.head
            for i in range(position-1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def sort(self):
        if self.size > 1:
            current = self.head.next
            while current is not None:
                node_to_insert = current
                current = current.next
                self.sorted_insert(node_to_insert)

    def sorted_insert(self, node: Node):
        if self.head is None:
            self.insert_head(node)
            return
        elif node.val < self.head.val:
            self.insert_head(node)
            return
        elif node.val >= self.tail.val:
            self.insert_tail(node)
            return
        else:
            current = self.head
            while current.next.val <= node.val:
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def search(self, node: Node):
        current = self.head
        while current is not None:
            if current.data == node.data:
                return current
            current = current.next
        return None
