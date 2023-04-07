
from DSA_Python_Implementations.datastructures.nodes.TNode import TNode


class BST:
    def __init__(self):
        self.root = None

    def __init__(self, val):
        self.root = TNode(val)

    def __init__(self, obj):
        self.root = obj
        
    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root
    