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


def test_sorted_insert():
    not_sorted_sll = SinglyLinkedList()
    not_sorted_sll.insertTail(Node(6))
    not_sorted_sll.insertTail(Node(5))
    not_sorted_sll.insertTail(Node(4))
    not_sorted_sll.insertTail(Node(1))
    not_sorted_sll.insertTail(Node(2))
    not_sorted_sll.sortedInsert(Node(3))
    assert not_sorted_sll.isSorted() == True
    assert not_sorted_sll.size == 6
    assert not_sorted_sll.head.val == 1
    assert not_sorted_sll.head.next.val == 2
    assert not_sorted_sll.head.next.next.val == 3
    assert not_sorted_sll.tail.val == 6


def test_search():
    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(2))
    sll.insertTail(Node(3))
    sll.insertTail(Node(4))
    sll.insertTail(Node(5))
    assert sll.search(1) == sll.head
    assert sll.search(2) == sll.head.next
    assert sll.search(5) == sll.tail
    assert sll.search(6) == None


def test_deleteHead():
    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(2))
    sll.insertTail(Node(3))
    sll.insertTail(Node(4))
    sll.insertTail(Node(5))
    sll.deleteHead()
    assert sll.head.val == 2
    assert sll.tail.val == 5
    assert sll.size == 4
    sll.deleteHead()
    assert sll.head.val == 3
    assert sll.tail.val == 5
    assert sll.size == 3
    sll.deleteHead()
    assert sll.head.val == 4
    assert sll.tail.val == 5
    assert sll.size == 2
    sll.deleteHead()
    assert sll.head.val == 5
    assert sll.tail.val == 5
    assert sll.size == 1
    sll.deleteHead()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0


def test_deleteTail():
    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(2))
    sll.insertTail(Node(3))
    sll.insertTail(Node(4))
    sll.insertTail(Node(5))
    sll.deleteTail()
    assert sll.head.val == 1
    assert sll.tail.val == 4
    assert sll.size == 4
    sll.deleteTail()
    assert sll.head.val == 1
    assert sll.tail.val == 3
    assert sll.size == 3
    sll.deleteTail()
    assert sll.head.val == 1
    assert sll.tail.val == 2
    assert sll.size == 2
    sll.deleteTail()
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.deleteTail()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0


def test_deleteNode():
    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(2))
    sll.insertTail(Node(3))
    sll.insertTail(Node(4))
    sll.insertTail(Node(5))
    sll.deleteNode(1)
    sll.deleteNode(5)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 3
    sll.deleteNode(3)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 2

    sll.insertHead(Node(1))
    sll.insertTail(Node(5))
    sll.deleteNode(sll.tail.val)
    assert sll.head.val == 1
    assert sll.tail.val == 4
    assert sll.size == 3
    sll.deleteNode(sll.head.val)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 2
    sll.deleteNode(2)
    assert sll.head.val == 4
    assert sll.tail.val == 4
    assert sll.size == 1
    sll.deleteNode(sll.head.val)
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0


def test_sort():
    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(2))
    sll.insertTail(Node(3))
    sll.insertTail(Node(4))
    sll.insertTail(Node(5))
    sll.sort()
    assert sll.head.val == 1
    assert sll.tail.val == 5
    assert sll.size == 5

    sll = SinglyLinkedList()
    sll.insertTail(Node(5))
    sll.insertTail(Node(4))
    sll.insertTail(Node(3))
    sll.insertTail(Node(2))
    sll.insertTail(Node(1))
    sll.sort()
    assert sll.head.val == 1
    assert sll.tail.val == 5
    assert sll.size == 5

    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(3))
    sll.insertTail(Node(2))
    sll.insertTail(Node(5))
    sll.insertTail(Node(4))
    sll.sort()
    assert sll.head.val == 1
    assert sll.tail.val == 5
    assert sll.size == 5

    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(9))
    sll.insertTail(Node(2))
    sll.insertTail(Node(8))
    sll.insertTail(Node(3))
    sll.insertTail(Node(7))
    sll.insertTail(Node(4))
    sll.insertTail(Node(6))
    sll.insertTail(Node(5))
    sll.sort()

    assert sll.head.val == 1
    assert sll.head.next.val == 2
    assert sll.head.next.next.val == 3
    assert sll.head.next.next.next.val == 4
    assert sll.head.next.next.next.next.val == 5
    assert sll.tail.val == 9
    assert sll.size == 9


def test_isSorted():
    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(2))
    sll.insertTail(Node(3))
    sll.insertTail(Node(4))
    sll.insertTail(Node(5))
    assert sll.isSorted() == True

    sll = SinglyLinkedList()
    sll.insertTail(Node(5))
    sll.insertTail(Node(4))
    sll.insertTail(Node(3))
    sll.insertTail(Node(2))
    sll.insertTail(Node(1))
    assert sll.isSorted() == False

    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(3))
    sll.insertTail(Node(2))
    sll.insertTail(Node(5))
    sll.insertTail(Node(4))
    assert sll.isSorted() == False

    sll = SinglyLinkedList()
    sll.insertTail(Node(1))
    sll.insertTail(Node(9))
    sll.insertTail(Node(2))
    sll.insertTail(Node(8))
    sll.insertTail(Node(3))
    sll.insertTail(Node(7))
    sll.insertTail(Node(4))
    sll.insertTail(Node(6))
    sll.insertTail(Node(5))
    assert sll.isSorted() == False
