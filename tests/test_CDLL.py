from datastructures.linear.CDLL import CircularDoublyLinkedList
from datastructures.nodes.DNode import DNode


def test_insertHead():
    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(3))
    cdll.insertHead(DNode(2))
    cdll.insertHead(DNode(1))
    cdll.insertHead(DNode(0))
    assert cdll.head.val == 0
    assert cdll.head.next.val == 1
    assert cdll.head.next.next.val == 2
    assert cdll.head.next.next.next.val == 3
    assert cdll.head.next.next.next.next.val == 0
    assert cdll.head.prev.val == 3
    assert cdll.head.prev.prev.val == 2
    assert cdll.head.prev.prev.prev.val == 1
    assert cdll.tail.next.val == 0
    assert cdll.tail.val == 3
