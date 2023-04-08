from DSA_Python_Implementations.datastructures.nodes import TNode
from collections import deque

class BST:
    def __init__(self):
        self.root = None

    def __init__(self, val):
        self.root = TNode(val)

    def __init__(self, obj):
        self.root = obj
        
    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root
    
    def insert(self, val):
        new_node = TNode(val)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.get_data():
                    if current.get_left() is None:
                        current.set_left(new_node)
                        new_node.set_parent(current)
                        break
                    else:
                        current = current.get_left()
                else:
                    if current.get_right() is None:
                        current.set_right(new_node)
                        new_node.set_parent(current)
                        break
                    else:
                        current = current.get_right()

    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if node.get_data() < current.get_data():
                    if current.get_left() is None:
                        current.set_left(node)
                        node.set_parent(current)
                        break
                    else:
                        current = current.get_left()
                else:
                    if current.get_right() is None:
                        current.set_right(node)
                        node.set_parent(current)
                        break
                    else:
                        current = current.get_right()

    def delete(self, val):
        node = self.search(val)
        if node is None:
            print(f"{val} is not in the tree")
            return

        if node.get_left() is None and node.get_right() is None:
            if node == self.root:
                self.root = None
            elif node == node.get_parent().get_left():
                node.get_parent().set_left(None)
            else:
                node.get_parent().set_right(None)
        elif node.get_left() is None:
            if node == self.root:
                self.root = node.get_right()
                self.root.set_parent(None)
            elif node == node.get_parent().get_left():
                node.get_parent().set_left(node.get_right())
                node.get_right().set_parent(node.get_parent())
            else:
                node.get_parent().set_right(node.get_right())
                node.get_right().set_parent(node.get_parent())
        elif node.get_right() is None:
            if node == self.root:
                self.root = node.get_left()
                self.root.set_parent(None)
            elif node == node.get_parent().get_left():
                node.get_parent().set_left(node.get_left())
                node.get_left().set_parent(node.get_parent())
            else:
                node.get_parent().set_right(node.get_left())
                node.get_left().set_parent(node.get_parent())
        else:
            successor = self.successor(node)
            node.set_data(successor.get_data())
            self.delete(successor.get_data())

    def search(self, val):
        current = self.root
        while current is not None and current.get_data() != val:
            if val < current.get_data():
                current = current.get_left()
            else:
                current = current.get_right()
        return current
    
    def print_in_order(self):
        self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.get_left())
            print(node.get_data(), end=" ")
            self.in_order_traversal(node.get_right())

    def printBF(self):
        if self.root is None:
            return
        
        q = deque()
        q.append(self.root)
        
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                print(node.data, end=' ')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print()