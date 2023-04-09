from collections import deque
from typing import Optional
from datastructures.nodes.TNode import TNode

class BST:

    def __init__(self, val: Optional[int] = None, obj: Optional[TNode] = None):
        if obj is not None:
            self.root = obj
        elif val is not None:
            self.root = TNode(val)
        else:
            self.root = None

    # Setter and getter for root
    def setRoot(self, node: TNode):
        self.root = node

    def getRoot(self) -> Optional[TNode]:
        return self.root
    
    # Insert a new node with data val into the tree
    def insert(self, val: int):
        newNode = TNode(val)
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while True:
                if val < current.getData():
                    if current.getLeft() is None:
                        current.setLeft(newNode)
                        newNode.setParent(current)
                        break
                    else:
                        current = current.getLeft()
                else:
                    if current.getRight() is None:
                        current.setRight(newNode)
                        newNode.setParent(current)
                        break
                    else:
                        current = current.getRight()

    # Insert the node passed as argument into the tree
    def insertNode(self, node: TNode):
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if node.getData() < current.getData():
                    if current.getLeft() is None:
                        current.setLeft(node)
                        node.setParent(current)
                        break
                    else:
                        current = current.getLeft()
                else:
                    if current.getRight() is None:
                        current.setRight(node)
                        node.setParent(current)
                        break
                    else:
                        current = current.getRight()

   

    # Search for the node with data val in the tree
    def search(self, val: int) -> Optional[TNode]:
        current = self.root
        while current is not None:
            if val == current.getData():
                return current
            elif val < current.getData():
                current = current.getLeft()
            else:
                current = current.getRight()
        return None
 

 