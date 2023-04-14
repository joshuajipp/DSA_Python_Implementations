from collections import deque
from datastructures.nodes.TNode import TNode

class BST:

    def __init__(self, val: int = None, obj: TNode = None):
        if obj is not None:
            self.root = obj
        elif val is not None:
            self.root = TNode(val)
        else:
            self.root = None

  
    def setRoot(self, node: TNode):
        self.root = node

    def getRoot(self) -> TNode:
        return self.root
    

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

    def delete(self, val: int):
        node = self.search(val)
        if node is None:
            print("Value not found in the tree")
        elif node.getLeft() is None and node.getRight() is None:
           
            parent = node.getParent()
            if parent is None:
             
                self.root = None
            elif parent.getLeft() == node:
                parent.setLeft(None)
            else:
                parent.setRight(None)
        elif node.getLeft() is None:
            
            parent = node.getParent()
            rightChild = node.getRight()
            if parent is None:
             
                self.root = rightChild
                rightChild.setParent(None)
            elif parent.getLeft() == node:
                parent.setLeft(rightChild)
                rightChild.setParent(parent)
            else:
                parent.setRight(rightChild)
                rightChild.setParent(parent)
        elif node.getRight() is None:
          
            parent = node.getParent()
            leftChild = node.getLeft()
            if parent is None:
                
                self.root = leftChild
                leftChild.setParent(None)
            elif parent.getLeft() == node:
                parent.setLeft(leftChild)
                leftChild.setParent(parent)
            else:
                parent.setRight(leftChild)
                leftChild.setParent(parent)
        else:
          
            successor = node.getRight()
            while successor.getLeft() is not None:
                successor = successor.getLeft()
            node.setData(successor.getData())
            if successor.getRight() is not None:
                successor.getRight().setParent(successor.getParent())
            if successor.getParent().getLeft() == successor:
                successor.getParent().setLeft(successor.getRight())
            else:
                successor.getParent().setRight(successor.getRight())
   

    def search(self, val: int) -> TNode:
        current = self.root
        while current is not None:
            if val == current.getData():
                return current
            elif val < current.getData():
                current = current.getLeft()
            else:
                current = current.getRight()
        return None
    
    def printInOrder(self):
        if self.root is None:
            return

        stack = []
        node = self.root

        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.getLeft()
            else:
                node = stack.pop()
                print(node.getData(), end=" ")
                node = node.getRight()

   
    def printBF(self):
        if self.root is None:
            return

        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
        
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                print(node.getData(), end=" ")
                if node.getLeft() is not None:
                    queue.append(node.getLeft())
                if node.getRight() is not None:
                    queue.append(node.getRight())
        
            print()

 
