from datastructures.nodes.SNode import Node
from datastructures.linear.SLL import SinglyLinkedList


def test_insert_head():
    sll = SinglyLinkedList()
    sll.insertHead(Node(1))
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.insertHead(Node(2))
    assert sll.head.val == 2
    assert sll.tail.val == 1
    assert sll.size == 2


def test_insert_tail():
    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.insertTail(Node(2))
    assert sll.head.val == 1
    assert sll.tail.val == 2
    assert sll.size == 2
    sll.insertTail


def test_insert():
    sll = SinglyLinkedList()
    sll.insert(Node(1), 0)
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.insert(Node(2), 0)
    assert sll.head.val == 2
    assert sll.tail.val == 1
    assert sll.size == 2
    sll.insert(Node(3), 1)
    assert sll.head.val == 2
    assert sll.tail.val == 1
    assert sll.size == 3
    assert sll.head.next.val == 3
    assert sll.head.next.next.val == 1
    sll.insert(Node(4), 3)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 4
    assert sll.head.next.val == 3
    assert sll.head.next.next.val == 1
    assert sll.head.next.next.next.val == 4

    raisedException = False
    try:
        sll.insert(Node(5), 5)
    except IndexError:
        raisedException = True
    assert raisedException

    raisedException = False
    try:
        sll.insert(Node(5), -1)
    except IndexError:
        raisedException = True
    assert raisedException


def test_is_sorted():
    not_sorted_sll = SinglyLinkedList()
    not_sorted_sll.insertTail(Node(2))
    not_sorted_sll.insertTail(Node(4))
    not_sorted_sll.insertTail(Node(6))
    not_sorted_sll.insertTail(Node(8))
    not_sorted_sll.insertTail(Node(7))
    assert not_sorted_sll.isSorted() == False
    sorted_sll = SinglyLinkedList()
    sorted_sll.insertTail(Node(2))
    sorted_sll.insertTail(Node(4))
    sorted_sll.insertTail(Node(6))
    sorted_sll.insertTail(Node(8))
    sorted_sll.insertTail(Node(9))
    assert sorted_sll.isSorted() == True
    sorted_sll.print_list()
