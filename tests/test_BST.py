import io
import sys

from datastructures.nodes.TNode import TNode
from datastructures.trees.BST import BST



def test_insert():
    tree = BST()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    assert tree.root.data == 5
    assert tree.root.left.data == 3
    assert tree.root.right.data == 7
    assert tree.root.left.left.data == 2
    assert tree.root.left.right.data == 4
    assert tree.root.right.left.data == 6
    assert tree.root.right.right.data == 8

def test_insertNode():
    tree = BST()
    node1 = TNode(5)
    node2 = TNode(3)
    node3 = TNode(7)
    node4 = TNode(2)
    node5 = TNode(4)
    node6 = TNode(6)
    node7 = TNode(8)
    tree.insertNode(node1)
    tree.insertNode(node2)
    tree.insertNode(node3)
    tree.insertNode(node4)
    tree.insertNode(node5)
    tree.insertNode(node6)
    tree.insertNode(node7)
    assert tree.root.data == 5
    assert tree.root.left.data == 3
    assert tree.root.right.data == 7
    assert tree.root.left.left.data == 2
    assert tree.root.left.right.data == 4
    assert tree.root.right.left.data == 6
    assert tree.root.right.right.data == 8

# def test_delete():
#     tree = BST()
#     tree.insert(5)
#     tree.insert(3)
#     tree.insert(7)
#     tree.insert(2)
#     tree.insert(4)
#     tree.insert(6)
#     tree.insert(8)
#     tree.delete(4)
#     assert tree.root.left.right is None
#     tree.delete(7)
#     assert tree.root.right.data == 8
#     tree.delete(5)
#     assert tree.root.data == 6

def test_search():
    tree = BST()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    assert tree.search(4).data == 4
    assert tree.search(7).data == 7
    assert tree.search(10) is None

# def test_print_in_order(capsys):
#     tree = BST()
#     tree.insert(5)
#     tree.insert(3)
#     tree.insert(7)
#     tree.insert(2)
#     tree.insert(4)
#     tree.insert(6)
#     tree.insert(8)
#     tree.print_in_order()
#     captured = capsys.readouterr()
#     assert captured.out == "2 3 4 5 6 7 8 "

# def test_printBF():
#     tree = BST()
#     tree.insert(5)
#     tree.insert(3)
#     tree.insert(7)
#     tree.insert(2)
#     tree.insert(4)
#     tree.insert(6)
#     tree.insert(8)
#     output = io.StringIO()
#     sys.stdout = output
#     tree.printBF()
#     sys.stdout = sys.__stdout__
#     output_str = output.getvalue()
#     assert output_str == "5 \n3 7 \n2 4 6 8 \n"
