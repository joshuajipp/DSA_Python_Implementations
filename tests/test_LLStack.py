from datastructures.nodes.SNode import SNode
from datastructures.linear.SLL import SinglyLinkedList


def test_push():
    sll = SinglyLinkedList()
    sll.push(SNode(1))
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.push(SNode(2))
    assert sll.head.val == 2
    assert sll.tail.val == 1
    assert sll.size == 2
    sll.push(SNode(3))
    assert sll.head.val == 3
    assert sll.tail.val == 1
    assert sll.size == 3
    sll.push(SNode(4))
    assert sll.head.val == 4
    assert sll.tail.val == 1
    assert sll.size == 4
    sll.push(SNode(5))
    assert sll.head.val == 5
    assert sll.tail.val == 1
    assert sll.size == 5


def test_peek():
    sll = SinglyLinkedList()
    sll.push(SNode(1))
    sll.push(SNode(2))
    sll.push(SNode(3))
    sll.push(SNode(4))
    sll.push(SNode(5))
    assert sll.peek().val == 5
    assert sll.size == 5


def test_pop():
    sll = SinglyLinkedList()
    sll.push(SNode(7))
    sll.push(SNode(5))
    sll.push(SNode(3))
    sll.push(SNode(1))
    sll.push(SNode(-1))
    assert sll.pop().val == -1
    assert sll.size == 4
    assert sll.head.val == 1
    assert sll.tail.val == 7
    assert sll.pop().val == 1
    assert sll.size == 3
    assert sll.head.val == 3
    assert sll.tail.val == 7
    assert sll.pop().val == 3
    assert sll.size == 2
    assert sll.head.val == 5
    assert sll.tail.val == 7
    assert sll.pop().val == 5
    assert sll.size == 1
    assert sll.head.val == 7
    assert sll.tail.val == 7
    assert sll.pop().val == 7
    assert sll.size == 0
    assert sll.head == None
    assert sll.tail == None
