from datastructures.linear.singlyCLL import SinglyCircularLinkedList
from datastructures.nodes.SNode import SNode


def test_insertHead():
    singlyCLL = SinglyCircularLinkedList()
    singlyCLL.insertHead(SNode(1))
    singlyCLL.insertHead(SNode(2))
    singlyCLL.insertHead(SNode(3))
    assert singlyCLL.head.val == 3
    assert singlyCLL.tail.val == 1
    assert singlyCLL.head.next.val == 2
    assert singlyCLL.tail.next.val == 3
    assert singlyCLL.size == 3
    assert singlyCLL.head.next.next.val == 1
    assert singlyCLL.tail.next.next.val == 2


def test_insertTail():
    singlyCLL = SinglyCircularLinkedList()
    singlyCLL.insertTail(SNode(10))
    singlyCLL.insertTail(SNode(11))
    singlyCLL.insertTail(SNode(12))
    singlyCLL.insertTail(SNode(13))

    assert singlyCLL.head.val == 10
    assert singlyCLL.tail.val == 13
    assert singlyCLL.head.next.val == 11
    assert singlyCLL.tail.next.val == 10
    assert singlyCLL.size == 4
    assert singlyCLL.head.next.next.val == 12
    assert singlyCLL.tail.next.next.val == 11


def test_insert():
    singlyCLL = SinglyCircularLinkedList()
    singlyCLL.insert(SNode(2), 0)
    singlyCLL.insert(SNode(1), 0)
    singlyCLL.insert(SNode(5), 2)
    singlyCLL.insert(SNode(3), 2)
    singlyCLL.insert(SNode(4), 3)
    singlyCLL.insert(SNode(0), 0)
    singlyCLL.insert(SNode(7), 6)
    singlyCLL.insert(SNode(6), 6)

    assert singlyCLL.head.val == 0
    assert singlyCLL.tail.val == 7
    assert singlyCLL.head.next.val == 1
    assert singlyCLL.tail.next.val == 0
    assert singlyCLL.size == 8
    assert singlyCLL.head.next.next.val == 2
    assert singlyCLL.tail.next.next.val == 1
    assert singlyCLL.head.next.next.next.val == 3
    assert singlyCLL.tail.next.next.next.val == 2
    assert singlyCLL.head.next.next.next.next.val == 4

    exception_raised = False
    try:
        singlyCLL.insert(SNode(8), 8)
    except IndexError:
        exception_raised = True
    assert exception_raised == False

    exception_raised = False
    try:
        singlyCLL.insert(SNode(8), -1)
    except IndexError:
        exception_raised = True
    assert exception_raised

    exception_raised = False
    try:
        singlyCLL.insert(SNode(9), 10)
    except IndexError:
        exception_raised = True
    assert exception_raised
