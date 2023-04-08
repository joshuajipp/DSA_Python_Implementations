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


def test_sorted():
    not_sorted_sll = SinglyLinkedList()
    not_sorted_sll.insertHead(Node(2))
    not_sorted_sll.insertHead(Node(4))
    not_sorted_sll.insertHead(Node(6))
    not_sorted_sll.insertHead(Node(8))
    not_sorted_sll.insertHead(Node(7))
    assert not_sorted_sll.isSorted() == False
    sorted_sll = SinglyLinkedList()
    sorted_sll.insertHead(Node(2))
    sorted_sll.insertHead(Node(4))
    sorted_sll.insertHead(Node(6))
    sorted_sll.insertHead(Node(8))
    sorted_sll.insertHead(Node(9))
    assert sorted_sll.isSorted() == True
