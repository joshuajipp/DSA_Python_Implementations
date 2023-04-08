import io
import sys

from DSA_Python_Implementations.datastructures.nodes.TNode import TNode


def test_getters_and_setters():
    node = TNode(5)

    # Test getters
    assert node.get_data() == 5
    assert node.get_left() == None
    assert node.get_right() == None
    assert node.get_parent() == None
    assert node.get_balance() == 0

    # Test setters
    node.set_data(10)
    assert node.get_data() == 10

    left_node = TNode(3)
    node.set_left(left_node)
    assert node.get_left() == left_node

    right_node = TNode(7)
    node.set_right(right_node)
    assert node.get_right() == right_node

    parent_node = TNode(15)
    node.set_parent(parent_node)
    assert node.get_parent() == parent_node

    node.set_balance(-1)
    assert node.get_balance() == -1


def test_print_node():
    node = TNode(5, 0)

    captured_output = io.StringIO()
    sys.stdout = captured_output
    node.print_node()
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue().strip() == "Data: 5, Balance: 0"


def test___str__():
    node = TNode(5, 0)
    assert str(node) == "5"

