

from datastructures.nodes.TNode import TNode
from datastructures.trees.BST import BST


class AVL(BST):

    def __init__(self, val: int = None, obj: TNode = None):
        if obj is not None:
            self.root = obj
            if obj.left is not None or obj.right is not None:
                self._rebalance(obj)
        elif val is not None:
            self.root = TNode(val)
        else:
            self.root = None
            
            

    def _getHeight(self, node: TNode) -> int:
        if node is None:
            return 0
        return max(self._getHeight(node.getLeft()), self._getHeight(node.getRight())) + 1

    def _getBalanceFactor(self, node: TNode) -> int:
        if node is None:
            return 0
        return self._getHeight(node.getLeft()) - self._getHeight(node.getRight())

    def _rotateLeft(self, node: TNode) -> TNode:
        pivot = node.getRight()
        node.setRight(pivot.getLeft())
        if pivot.getLeft() is not None:
            pivot.getLeft().setParent(node)
        pivot.setLeft(node)
        pivot.setParent(node.getParent())
        node.setParent(pivot)
        if node == self.root:
            self.root = pivot
        return pivot

    def _rotateRight(self, node: TNode) -> TNode:
        pivot = node.getLeft()
        node.setLeft(pivot.getRight())
        if pivot.getRight() is not None:
            pivot.getRight().setParent(node)
        pivot.setRight(node)
        pivot.setParent(node.getParent())
        node.setParent(pivot)
        if node == self.root:
            self.root = pivot
        return pivot

    def _rebalance(self, root):
        if root is None:
            return None

        # Recursively balance subtrees
        root.left = self._rebalance(root.left)
        root.right = self._rebalance(root.right)

        # Calculate the balance factor
        balance_factor = self._getBalanceFactor(root)

        # Left subtree is heavier
        if balance_factor > 1:
            # Left-Right case
            if self._getBalanceFactor(root.left) < 0:
                root.left = self._rotateLeft(root.left)
            # Left-Left case
            root = self._rotateRight(root)
        # Right subtree is heavier
        elif balance_factor < -1:
            # Right-Left case
            if self._getBalanceFactor(root.right) > 0:
                root.right = self._rotateRight(root.right)
            # Right-Right case
            root = self._rotateLeft(root)

        return root

    def insert(self, val: int):
        super().insert(val)
        self.root = self._rebalance(self.root)

    def insertNode(self, node: TNode):
        super().insertNode(node)
        self.root = self._rebalance(self.root)

    def setRoot(self, node: TNode):
        super().setRoot(node)
        # if node.left is not None or node.right is not None:
            # self.root = self._create_balanced_tree(self.root)

    def delete(self, val: int):
        super().delete(val)
        self.root = self._rebalance(self.root)

    def printBF(self):
        super().printBF()

    def printInOrder(self):
        return super().printInOrder()