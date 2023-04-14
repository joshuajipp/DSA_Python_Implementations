from datastructures.nodes.TNode import TNode
from datastructures.trees.BST import BST
from datastructures.trees.AVL import AVL

def test_avl_insert():
    avl = AVL()

    # Insert 10, 20, 30, 40, 50, 25
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    assert avl.root.data == 20
    assert avl.root.right.data == 30
    assert avl.root.left.data == 10
    avl.insert(40)
    assert avl.root.data == 20
    assert avl.root.right.data == 30
    assert avl.root.left.data == 10
    assert avl.root.right.right.data == 40
    assert avl.root.left.left is None
    avl.insert(50)
    assert avl.root.data == 20
    assert avl.root.right.data == 40
    assert avl.root.left.data == 10
    assert avl.root.right.right.data == 50
    assert avl.root.right.left.data == 30


    avl.insert(25)
    assert avl.root.data == 30


def test_avl_balance():
    avl = AVL()
    avl.insert(63)
    assert avl.root.data == 63
    avl.insert(9)
    assert avl.root.data == 63
    assert avl.root.left.data == 9
    avl.insert(19)
    assert avl.root.data == 19
    assert avl.root.right.data == 63
    assert avl.root.left.data == 9
    avl.insert(27)
    assert avl.root.data == 19
    assert avl.root.right.left.data == 27
    avl.insert(18)
    assert avl.root.data == 19
    assert avl.root.left.right.data == 18
    avl.insert(108)
    assert avl.root.data == 19

    # Check that the tree is balanced
    assert avl._getHeight(avl.root.getLeft()) == 2
    assert avl._getHeight(avl.root.getRight()) == 2


    avl.insert(99)
    assert avl.root.data == 19
    avl.insert(81)
    assert avl.root.data == 19
    assert avl.root.right.data == 63
    assert avl.root.left.data == 9
    assert avl.root.left.right.data == 18
    assert avl.root.right.left.data == 27
    assert avl.root.right.right.data == 99
    assert avl.root.right.right.right.data == 108
    assert avl.root.right.right.left.data == 81


    # Check that the tree is balanced
    assert avl._getHeight(avl.root.getLeft()) == 2
    assert avl._getHeight(avl.root.getRight()) == 3

    # Insert 35 and balance the tree
    avl.insert(35)
    assert avl.root.data == 19
    assert avl.root.right.left.right.data == 35

    # Check that the tree is balanced
    assert avl._getHeight(avl.root.getLeft()) == 2
    assert avl._getHeight(avl.root.getRight()) == 3

    # Insert 15 and balance the tree
    avl.insert(15)
    assert avl.root.data == 19
    assert avl.root.left.data == 15
    assert avl.root.left.right.data == 18
    assert avl.root.left.left.data == 9

    # Check that the tree is balanced
    assert avl._getHeight(avl.root.getLeft()) == 2
    assert avl._getHeight(avl.root.getRight()) == 3

    avl.insert(17)
    assert avl.root.data == 19
    assert avl.root.left.right.left.data == 17
    assert avl._getHeight(avl.root.getLeft()) == 3
    assert avl._getHeight(avl.root.getRight()) == 3

def test_avl_search():
    avl = AVL()

    # Insert 10, 20, 30, 40, 50, 25
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(25)

    # Search for nodes in the tree
    node_20 = avl.search(20)
    assert node_20 is not None
    assert node_20.data == 20

    node_25 = avl.search(25)
    assert node_25 is not None
    assert node_25.data == 25

    node_60 = avl.search(60)
    assert node_60 is None

def test_constructor():
    bst = BST(8)
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.insert(25)
    bst.insert(30)
    bst.insert(40)
    bst.insert(50)
    bst.insert(60)
    bst.insert(69)
    bst.insert(690)

    avl = AVL(obj = bst.root)
    assert avl.root.data == 25
    assert avl.root.right.data == 50
    assert avl.root.left.data == 8
    assert avl.root.right.right.data == 69
    assert avl.root.left.right.data == 10
    assert avl.root.right.right.right.data == 690
    assert avl.root.left.right.right.right.data == 20

def test_delete():
    avl = AVL()
    avl.insert(55)
    avl.insert(45)
    avl.insert(35)
    avl.insert(60)
    avl.insert(103)
    avl.insert(121)
    assert avl.root.data == 60
    assert avl.root.right.right.data == 121
    avl.delete(121)
    assert avl.root.right.right is None



