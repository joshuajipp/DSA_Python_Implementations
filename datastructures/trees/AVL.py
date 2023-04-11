from datastructures.nodes.TNode import TNode
from datastructures.trees.BST import BST
class AVL(BST):
    def __init__(self, val: int = None, obj: TNode = None):
        if obj is not None:
            self.root = obj
        elif val is not None:
            self.root = TNode(val)
            self.__balance(obj)
        else:
            self.root = None


    def insert(self, val : int):
        super().insert(val)
        #balance tree

    def insertNode(self, node : TNode ):
        super().insertNode(node)
        #balance tree

    def search(self, val : int) -> TNode:
        super().search(val)

    def printInOrder(self):
        super().printInOrder()
    
    def printBF(self):
        super().printBF()
