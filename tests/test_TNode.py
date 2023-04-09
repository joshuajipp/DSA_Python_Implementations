import io
import sys

from datastructures.nodes.TNode import TNode

def testGettersAndSetters():
    node = TNode(5)

    # Test getters
    assert node.getData() == 5
    assert node.getLeft() == None
    assert node.getRight() == None
    assert node.getParent() == None
    assert node.getBalance() == 0

    # Test setters
    node.setData(10)
    assert node.getData() == 10

    leftNode = TNode(3)
    node.setLeft(leftNode)
    assert node.getLeft() == leftNode

    rightNode = TNode(7)
    node.setRight(rightNode)
    assert node.getRight() == rightNode

    parentNode = TNode(15)
    node.setParent(parentNode)
    assert node.getParent() == parentNode

    node.setBalance(-1)
    assert node.getBalance() == -1

def testPrintNode():
    node = TNode(5, 0)

    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    node.printNode()
    sys.stdout = sys.__stdout__

    assert capturedOutput.getvalue().strip() == "Data: 5, Balance: 0"

def test___str__():
    node = TNode(5, 0)
    assert str(node) == "5"

