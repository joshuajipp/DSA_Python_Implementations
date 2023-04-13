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
    assert cdll.size == 4


def test_insertTail():
    cdll = CircularDoublyLinkedList()
    cdll.insertTail(DNode(0))
    cdll.insertTail(DNode(1))
    cdll.insertTail(DNode(2))
    cdll.insertTail(DNode(3))
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
    assert cdll.size == 4


def test_insert():
    cdll = CircularDoublyLinkedList()
    cdll.insert(DNode(2), 0)
    cdll.insert(DNode(4), 1)
    cdll.insert(DNode(0), 0)
    cdll.insert(DNode(1), 1)
    cdll.insert(DNode(3), 3)
    assert cdll.head.val == 0
    assert cdll.head.next.val == 1
    assert cdll.head.next.next.val == 2
    assert cdll.head.next.next.next.val == 3
    assert cdll.head.next.next.next.next.val == 4
    assert cdll.head.next.next.next.next.next.val == 0
    assert cdll.head.prev.val == 4
    assert cdll.head.prev.prev.val == 3
    assert cdll.head.prev.prev.prev.val == 2
    assert cdll.tail.next.val == 0
    assert cdll.tail.val == 4
    assert cdll.size == 5

    exception_raised = False
    try:
        cdll.insert(DNode(5), 6)
    except IndexError:
        exception_raised = True
    assert exception_raised

    exception_raised = False
    try:
        cdll.insert(DNode(5), -1)
    except IndexError:
        exception_raised = True
    assert exception_raised
