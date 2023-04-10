from datastructures.nodes.DNode import DNode
from datastructures.linear.DLL import DoublyLinkedList as DLL


def test_insertHead():
    dll = DLL()
    node = DNode(1)
    dll.insertHead(node)
    assert dll.head == node
    assert dll.tail == node
    assert dll.size == 1
    assert node.prev == None
    assert node.next == None

    dll.insertHead(DNode(2))
    assert dll.head.val == 2
    assert dll.head.next == node
    assert dll.tail == node
    assert dll.size == 2
    assert node.prev == dll.head
    assert node.next == None


def test_insertTail():
    dll = DLL()
    node = DNode(1)
    dll.insertTail(node)
    assert dll.head == node
    assert dll.tail == node
    assert dll.size == 1
    assert node.prev == None
    assert node.next == None

    dll.insertTail(DNode(2))
    assert dll.head == node
    assert dll.tail.val == 2
    assert dll.size == 2
    assert node.prev == None
    assert node.next == dll.tail
    assert dll.tail.prev == node
    assert dll.tail.next == None

    dll.insertTail(DNode(2))
    dll.insertTail(DNode(0))
    dll.insertTail(DNode(1))
    dll.insertTail(DNode(2))
    dll.insertTail(DNode(3))
    assert dll.head.val == 1
    assert dll.tail.val == 3
    assert dll.size == 7
    assert dll.head.prev == None
    assert dll.head.next.val == 2
    assert dll.head.next.next.val == 2
    assert dll.head.next.next.next.val == 0
    assert dll.tail.prev.val == 2
    assert dll.tail.prev.prev.val == 1


def test_insert():
    dll = DLL()
    node = DNode(1)
    dll.insert(node, 0)
    assert dll.head == node
    assert dll.tail == node
    assert dll.size == 1
    assert node.prev == None
    assert node.next == None

    dll.insert(DNode(2), 0)
    assert dll.head.val == 2
    assert dll.head.next == node
    assert dll.tail == node
    assert dll.size == 2
    assert node.prev == dll.head
    assert node.next == None

    dll.insert(DNode(3), 1)
    assert dll.head.val == 2
    assert dll.tail.val == 1
    assert dll.size == 3
    assert dll.head.next.val == 3
    assert dll.head.next.next.val == 1
    assert dll.head.next.next.prev.val == 3
    assert dll.head.next.next.prev.prev.val == 2
    assert dll.head.next.next.prev.prev.next.val == 3
    assert dll.tail.val == 1
    assert dll.tail.prev.val == 3
    assert dll.tail.prev.prev.val == 2

    exception_raised = False
    try:
        dll.insert(DNode(4), 4)
    except IndexError:
        exception_raised = True
    assert exception_raised

    exception_raised = False
    try:
        dll.insert(DNode(4), -1)
    except IndexError:
        exception_raised = True
    assert exception_raised


def test_sortedInsert():
    not_sorted_dll = DLL()
    not_sorted_dll.insertTail(DNode(6))
    not_sorted_dll.insertTail(DNode(5))
    not_sorted_dll.insertTail(DNode(4))
    not_sorted_dll.insertTail(DNode(1))
    not_sorted_dll.insertTail(DNode(2))
    not_sorted_dll.sortedInsert(DNode(3))
    assert not_sorted_dll.isSorted() == True
    assert not_sorted_dll.size == 6
    assert not_sorted_dll.head.val == 1
    assert not_sorted_dll.head.next.val == 2
    assert not_sorted_dll.head.next.next.val == 3
    assert not_sorted_dll.tail.val == 6
    assert not_sorted_dll.tail.prev.val == 5


def test_sort():
    not_sorted_dll = DLL()
    not_sorted_dll.insertTail(DNode(6))
    not_sorted_dll.insertTail(DNode(5))
    not_sorted_dll.insertTail(DNode(4))
    not_sorted_dll.insertTail(DNode(1))
    not_sorted_dll.insertTail(DNode(2))
    not_sorted_dll.sort()
    assert not_sorted_dll.isSorted() == True
    assert not_sorted_dll.size == 5
    assert not_sorted_dll.head.val == 1
    assert not_sorted_dll.head.next.val == 2
    assert not_sorted_dll.head.next.next.val == 4
    assert not_sorted_dll.tail.val == 6
    assert not_sorted_dll.tail.prev.val == 5

    not_sorted_dll = DLL()
    not_sorted_dll.insertTail(DNode(1))
    not_sorted_dll.insertTail(DNode(7))
    not_sorted_dll.insertTail(DNode(3))
    not_sorted_dll.insertTail(DNode(4))
    not_sorted_dll.insertTail(DNode(2))
    not_sorted_dll.insertTail(DNode(5))
    not_sorted_dll.insertTail(DNode(6))
    not_sorted_dll.sort()
    assert not_sorted_dll.isSorted() == True
    assert not_sorted_dll.size == 7
    assert not_sorted_dll.head.val == 1
    assert not_sorted_dll.head.next.val == 2
    assert not_sorted_dll.head.next.next.val == 3
    assert not_sorted_dll.tail.val == 7
    assert not_sorted_dll.tail.prev.val == 6


def test_isSorted():
    sorted_dll = DLL()
    sorted_dll.insertTail(DNode(1))
    sorted_dll.insertTail(DNode(2))
    sorted_dll.insertTail(DNode(3))
    sorted_dll.insertTail(DNode(4))
    sorted_dll.insertTail(DNode(5))
    sorted_dll.insertTail(DNode(6))
    assert sorted_dll.isSorted() == True

    not_sorted_dll = DLL()
    not_sorted_dll.insertTail(DNode(6))
    not_sorted_dll.insertTail(DNode(5))
    not_sorted_dll.insertTail(DNode(4))
    not_sorted_dll.insertTail(DNode(1))
    not_sorted_dll.insertTail(DNode(2))
    assert not_sorted_dll.isSorted() == False


def test_delete():
    dll = DLL()
    dll.insertTail(DNode(100))
    dll.insertTail(DNode(101))
    dll.insertTail(DNode(106))
    dll.insertTail(DNode(102))
    dll.insertTail(DNode(103))
    dll.deleteNode(101)
    dll.deleteNode(103)

    assert dll.size == 3
    assert dll.head.val == 100
    assert dll.head.next.val == 106
    assert dll.head.next.next.val == 102
    assert dll.tail.val == 102
    assert dll.tail.prev.val == 106
    assert dll.tail.prev.prev.val == 100

    dll.deleteNode(100)
    assert dll.size == 2
    assert dll.head.val == 106
    assert dll.head.next.val == 102
    assert dll.tail.val == 102
    assert dll.tail.prev.val == 106

    dll.deleteNode(102)
    assert dll.size == 1
    assert dll.head.val == 106
    assert dll.tail.val == 106
    assert dll.head.next == None
    assert dll.tail.prev == None

    dll.deleteNode(106)
    assert dll.size == 0
    assert dll.head == None
    assert dll.tail == None


def test_clear():
    dll = DLL()
    dll.insertTail(DNode(100))
    dll.insertTail(DNode(101))
    dll.insertTail(DNode(106))
    dll.insertTail(DNode(102))
    dll.insertTail(DNode(103))
    dll.clear()
    assert dll.size == 0
    assert dll.head == None
    assert dll.tail == None


def test_deleteHead():
    dll = DLL()
    dll.insertTail(DNode(100))
    dll.insertTail(DNode(101))
    dll.insertTail(DNode(106))
    dll.insertTail(DNode(102))
    dll.insertTail(DNode(103))
    dll.deleteHead()
    assert dll.size == 4
    assert dll.head.val == 101
    assert dll.head.next.val == 106
    assert dll.head.next.next.val == 102
    assert dll.tail.val == 103
    assert dll.tail.prev.val == 102
    assert dll.tail.prev.prev.val == 106

    dll.deleteHead()
    assert dll.size == 3
    assert dll.head.val == 106
    assert dll.head.next.val == 102
    assert dll.tail.val == 103
    assert dll.tail.prev.val == 102
    assert dll.tail.prev.prev.val == 106

    dll.deleteHead()
    assert dll.size == 2
    assert dll.head.val == 102
    assert dll.head.next.val == 103
    assert dll.tail.val == 103
    assert dll.tail.prev.val == 102

    dll.deleteHead()
    assert dll.size == 1
    assert dll.head.val == 103
    assert dll.tail.val == 103
    assert dll.head.next == None
    assert dll.tail.prev == None

    dll.deleteHead()
    assert dll.size == 0
    assert dll.head == None
    assert dll.tail == None


def test_deleteTail():
    dll = DLL()
    dll.insertTail(DNode(75))
    dll.insertTail(DNode(69))
    dll.insertTail(DNode(150))
    dll.insertTail(DNode(111))
    dll.insertTail(DNode(103))
    dll.deleteTail()
    assert dll.size == 4
    assert dll.head.val == 75
    assert dll.head.next.val == 69
    assert dll.head.next.next.val == 150
    assert dll.tail.val == 111
    assert dll.tail.prev.val == 150
    assert dll.tail.prev.prev.val == 69

    dll.deleteTail()
    assert dll.size == 3
    assert dll.head.val == 75
    assert dll.head.next.val == 69
    assert dll.tail.val == 150
    assert dll.tail.prev.val == 69
    assert dll.tail.prev.prev.val == 75

    dll.deleteTail()
    assert dll.size == 2
    assert dll.head.val == 75
    assert dll.head.next.val == 69
    assert dll.tail.val == 69
    assert dll.tail.prev.val == 75

    dll.deleteTail()
    assert dll.size == 1
    assert dll.head.val == 75
    assert dll.tail.val == 75
    assert dll.head.next == None
    assert dll.tail.prev == None

    dll.deleteTail()
    assert dll.size == 0
    assert dll.head == None
    assert dll.tail == None


def test_search():
    dll = DLL()
    dll.insertTail(DNode(75))
    dll.insertTail(DNode(69))
    dll.insertTail(DNode(150))
    dll.insertTail(DNode(111))
    dll.insertTail(DNode(103))
    assert dll.search(69) == dll.head.next
    assert dll.search(150) == dll.head.next.next
    assert dll.search(111) == dll.tail.prev
    assert dll.search(103) == dll.tail
    assert dll.search(75) == dll.head
    assert dll.search(100) == None
