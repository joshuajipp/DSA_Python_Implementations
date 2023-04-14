from datastructures.nodes.SNode import SNode
from datastructures.linear.SLL import SinglyLinkedList


def test_insertHead():
    sll = SinglyLinkedList()
    sll.insertHead(SNode(1))
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.insertHead(SNode(2))
    assert sll.head.val == 2
    assert sll.tail.val == 1
    assert sll.size == 2


def test_insertTail():
    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.insertTail(SNode(2))
    assert sll.head.val == 1
    assert sll.tail.val == 2
    assert sll.size == 2
    sll.insertTail


def test_insert():
    sll = SinglyLinkedList()
    sll.insert(SNode(1), 0)
    assert sll.head.val == 1
    assert sll.tail.val == 1
    assert sll.size == 1
    sll.insert(SNode(2), 0)
    assert sll.head.val == 2
    assert sll.tail.val == 1
    assert sll.size == 2
    sll.insert(SNode(3), 1)
    assert sll.head.val == 2
    assert sll.tail.val == 1
    assert sll.size == 3
    assert sll.head.next.val == 3
    assert sll.head.next.next.val == 1
    sll.insert(SNode(4), 3)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 4
    assert sll.head.next.val == 3
    assert sll.head.next.next.val == 1
    assert sll.head.next.next.next.val == 4

    raisedException = False
    try:
        sll.insert(SNode(5), 5)
    except IndexError:
        raisedException = True
    assert raisedException

    raisedException = False
    try:
        sll.insert(SNode(5), -1)
    except IndexError:
        raisedException = True
    assert raisedException


def test_sortedInsert():
    not_sorted_sll = SinglyLinkedList()
    not_sorted_sll.insertTail(SNode(6))
    not_sorted_sll.insertTail(SNode(5))
    not_sorted_sll.insertTail(SNode(4))
    not_sorted_sll.insertTail(SNode(1))
    not_sorted_sll.insertTail(SNode(2))
    not_sorted_sll.sortedInsert(SNode(3))
    assert not_sorted_sll.isSorted() == True
    assert not_sorted_sll.size == 6
    assert not_sorted_sll.head.val == 1
    assert not_sorted_sll.head.next.val == 2
    assert not_sorted_sll.head.next.next.val == 3
    assert not_sorted_sll.tail.val == 6


def test_search():
    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(5))
    assert sll.search(1) == sll.head
    assert sll.search(2) == sll.head.next
    assert sll.search(5) == sll.tail
    assert sll.search(6) == None


def test_deleteHead():
    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(5))
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
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(5))
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


def test_delete():
    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(5))
    sll.delete(1)
    sll.delete(5)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 3
    sll.delete(3)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 2

    sll.insertHead(SNode(1))
    sll.insertTail(SNode(5))
    sll.delete(sll.tail.val)
    assert sll.head.val == 1
    assert sll.tail.val == 4
    assert sll.size == 3
    sll.delete(sll.head.val)
    assert sll.head.val == 2
    assert sll.tail.val == 4
    assert sll.size == 2
    sll.delete(2)
    assert sll.head.val == 4
    assert sll.tail.val == 4
    assert sll.size == 1
    sll.delete(sll.head.val)
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0


def test_sort():
    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(5))
    sll.sort()
    assert sll.head.val == 1
    assert sll.tail.val == 5
    assert sll.size == 5

    sll = SinglyLinkedList()
    sll.insertTail(SNode(5))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(1))
    sll.sort()
    assert sll.head.val == 1
    assert sll.tail.val == 5
    assert sll.size == 5

    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(5))
    sll.insertTail(SNode(4))
    sll.sort()
    assert sll.head.val == 1
    assert sll.tail.val == 5
    assert sll.size == 5

    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(9))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(8))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(7))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(6))
    sll.insertTail(SNode(5))
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
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(5))
    assert sll.isSorted() == True

    sll = SinglyLinkedList()
    sll.insertTail(SNode(5))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(1))
    assert sll.isSorted() == False

    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(5))
    sll.insertTail(SNode(4))
    assert sll.isSorted() == False

    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(9))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(8))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(7))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(6))
    sll.insertTail(SNode(5))
    assert sll.isSorted() == False


def test_clear():
    sll = SinglyLinkedList()
    sll.insertTail(SNode(1))
    sll.insertTail(SNode(2))
    sll.insertTail(SNode(3))
    sll.insertTail(SNode(4))
    sll.insertTail(SNode(5))
    sll.clear()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0
