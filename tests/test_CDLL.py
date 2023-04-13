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


def test_deleteHead():
    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(3))
    cdll.insertHead(DNode(2))
    cdll.insertHead(DNode(1))
    cdll.insertHead(DNode(0))
    cdll.deleteHead()
    assert cdll.head.val == 1
    assert cdll.head.next.val == 2
    assert cdll.head.next.next.val == 3
    assert cdll.head.next.next.next.val == 1
    assert cdll.head.prev.val == 3
    assert cdll.head.prev.prev.val == 2
    assert cdll.head.prev.prev.prev.val == 1
    assert cdll.tail.next.val == 1
    assert cdll.tail.val == 3
    assert cdll.size == 3

    cdll.deleteHead()
    assert cdll.head.val == 2
    assert cdll.head.next.val == 3
    assert cdll.head.next.next.val == 2
    assert cdll.head.prev.val == 3
    assert cdll.head.prev.prev.val == 2
    assert cdll.tail.next.val == 2
    assert cdll.tail.val == 3
    assert cdll.size == 2

    cdll.deleteHead()
    assert cdll.head.val == 3
    assert cdll.head.next.val == 3
    assert cdll.head.prev.val == 3
    assert cdll.tail.next.val == 3
    assert cdll.tail.val == 3
    assert cdll.size == 1

    cdll.deleteHead()
    assert cdll.head is None
    assert cdll.tail is None
    assert cdll.size == 0


def test_deleteTail():
    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(1))
    cdll.insertHead(DNode(3))
    cdll.insertHead(DNode(5))
    cdll.insertHead(DNode(7))
    cdll.insertHead(DNode(9))

    cdll.deleteTail()
    assert cdll.head.val == 9
    assert cdll.head.next.val == 7
    assert cdll.head.next.next.val == 5
    assert cdll.head.next.next.next.val == 3
    assert cdll.head.next.next.next.next.val == 9
    assert cdll.head.prev.val == 3
    assert cdll.head.prev.prev.val == 5
    assert cdll.head.prev.prev.prev.val == 7
    assert cdll.tail.next.val == 9
    assert cdll.tail.val == 3
    assert cdll.size == 4

    cdll.deleteTail()
    cdll.deleteTail()
    assert cdll.head.val == 9
    assert cdll.head.next.val == 7
    assert cdll.head.next.next.val == 9
    assert cdll.head.prev.val == 7
    assert cdll.head.prev.prev.val == 9
    assert cdll.tail.next.val == 9
    assert cdll.tail.val == 7
    assert cdll.size == 2

    cdll.deleteTail()
    assert cdll.head.val == 9
    assert cdll.head.next.val == 9
    assert cdll.head.prev.val == 9
    assert cdll.tail.next.val == 9
    assert cdll.tail.val == 9
    assert cdll.size == 1

    cdll.deleteTail()
    assert cdll.head is None
    assert cdll.tail is None
    assert cdll.size == 0


def test_delete():
    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(50))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(10))

    cdll.delete(40)
    assert cdll.head.val == 10
    assert cdll.head.next.val == 20
    assert cdll.head.next.next.val == 30
    assert cdll.head.next.next.next.val == 50
    assert cdll.head.next.next.next.next.val == 10
    assert cdll.head.prev.val == 50
    assert cdll.head.prev.prev.val == 30
    assert cdll.head.prev.prev.prev.val == 20
    assert cdll.tail.next.val == 10
    assert cdll.tail.val == 50
    assert cdll.size == 4

    cdll.delete(10)
    assert cdll.head.val == 20
    assert cdll.head.next.val == 30
    assert cdll.head.next.next.val == 50
    assert cdll.head.next.next.next.val == 20
    assert cdll.head.prev.val == 50
    assert cdll.head.prev.prev.val == 30
    assert cdll.head.prev.prev.prev.val == 20
    assert cdll.tail.next.val == 20
    assert cdll.tail.val == 50
    assert cdll.size == 3

    cdll.delete(50)
    assert cdll.head.val == 20
    assert cdll.head.next.val == 30
    assert cdll.head.next.next.val == 20
    assert cdll.head.prev.val == 30
    assert cdll.head.prev.prev.val == 20
    assert cdll.tail.next.val == 20
    assert cdll.tail.val == 30
    assert cdll.size == 2

    cdll.delete(20)
    assert cdll.head.val == 30
    assert cdll.head.next.val == 30
    assert cdll.head.prev.val == 30
    assert cdll.tail.next.val == 30
    assert cdll.tail.val == 30
    assert cdll.size == 1

    cdll.delete(15)
    assert cdll.head.val == 30
    assert cdll.head.next.val == 30
    assert cdll.head.prev.val == 30
    assert cdll.tail.next.val == 30
    assert cdll.tail.val == 30
    assert cdll.size == 1

    cdll.delete(30)
    assert cdll.head is None
    assert cdll.tail is None
    assert cdll.size == 0


def test_sort():
    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(50))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(10))

    cdll.sort()
    assert cdll.head.val == 10
    assert cdll.head.next.val == 20
    assert cdll.head.next.next.val == 30
    assert cdll.head.next.next.next.val == 40
    assert cdll.head.next.next.next.next.val == 50
    assert cdll.head.prev.val == 50
    assert cdll.head.prev.prev.val == 40
    assert cdll.head.prev.prev.prev.val == 30
    assert cdll.tail.next.val == 10
    assert cdll.tail.val == 50
    assert cdll.size == 5

    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(50))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(10))
    cdll.insertHead(DNode(60))
    cdll.insertHead(DNode(70))
    cdll.insertHead(DNode(80))
    cdll.insertHead(DNode(90))
    cdll.insertHead(DNode(100))

    cdll.sort()
    assert cdll.head.val == 10
    assert cdll.head.next.val == 20
    assert cdll.head.next.next.val == 30
    assert cdll.head.next.next.next.val == 40
    assert cdll.head.next.next.next.next.val == 50
    assert cdll.head.next.next.next.next.next.val == 60
    assert cdll.head.next.next.next.next.next.next.val == 70
    assert cdll.head.next.next.next.next.next.next.next.val == 80
    assert cdll.head.next.next.next.next.next.next.next.next.val == 90
    assert cdll.head.next.next.next.next.next.next.next.next.next.val == 100
    assert cdll.head.prev.val == 100
    assert cdll.head.prev.prev.val == 90
    assert cdll.head.prev.prev.prev.val == 80
    assert cdll.head.prev.prev.prev.prev.val == 70
    assert cdll.head.prev.prev.prev.prev.prev.val == 60
    assert cdll.head.prev.prev.prev.prev.prev.prev.val == 50
    assert cdll.head.prev.prev.prev.prev.prev.prev.prev.val == 40
    assert cdll.head.prev.prev.prev.prev.prev.prev.prev.prev.val == 30
    assert cdll.head.prev.prev.prev.prev.prev.prev.prev.prev.prev.val == 20

    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(10))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(50))

    cdll.sort()
    assert cdll.head.val == 10
    assert cdll.head.next.val == 20
    assert cdll.head.next.next.val == 30
    assert cdll.head.next.next.next.val == 40
    assert cdll.head.next.next.next.next.val == 50
    assert cdll.head.prev.val == 50
    assert cdll.head.prev.prev.val == 40
    assert cdll.head.prev.prev.prev.val == 30
    assert cdll.head.prev.prev.prev.prev.val == 20
    assert cdll.tail.next.val == 10
    assert cdll.tail.val == 50
    assert cdll.size == 5


def test_isSorted():
    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(50))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(10))

    assert cdll.isSorted() == True

    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(50))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(10))
    cdll.insertHead(DNode(60))
    cdll.insertHead(DNode(70))
    cdll.insertHead(DNode(80))
    cdll.insertHead(DNode(90))
    cdll.insertHead(DNode(100))

    assert cdll.isSorted() == False

    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(10))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(50))

    assert cdll.isSorted() == False

    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(10))
    cdll.insertHead(DNode(500))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(50))

    assert cdll.isSorted() == False


def test_sortedInsert():
    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(50))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(10))

    cdll.sortedInsert(DNode(25))
    assert cdll.head.val == 10
    assert cdll.head.next.val == 20
    assert cdll.head.next.next.val == 25
    assert cdll.head.next.next.next.val == 30
    assert cdll.head.next.next.next.next.val == 40
    assert cdll.head.next.next.next.next.next.val == 50
    assert cdll.head.prev.val == 50
    assert cdll.head.prev.prev.val == 40
    assert cdll.head.prev.prev.prev.val == 30
    assert cdll.head.prev.prev.prev.prev.val == 25
    assert cdll.head.prev.prev.prev.prev.prev.val == 20
    assert cdll.tail.next.val == 10
    assert cdll.tail.val == 50
    assert cdll.size == 6

    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(50))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(20))
    cdll.insertHead(DNode(10))
    cdll.insertHead(DNode(60))
    cdll.insertHead(DNode(70))
    cdll.insertHead(DNode(80))
    cdll.insertHead(DNode(90))
    cdll.insertHead(DNode(100))

    cdll.sortedInsert(DNode(25))
    assert cdll.head.val == 10
    assert cdll.head.next.val == 20
    assert cdll.head.next.next.val == 25
    assert cdll.head.next.next.next.val == 30
    assert cdll.head.next.next.next.next.val == 40
    assert cdll.head.next.next.next.next.next.val == 50
    assert cdll.head.next.next.next.next.next.next.val == 60
    assert cdll.head.next.next.next.next.next.next.next.val == 70
    assert cdll.head.next.next.next.next.next.next.next.next.val == 80
    assert cdll.tail.val == 100
    assert cdll.tail.prev.val == 90
    assert cdll.tail.prev.prev.val == 80
    assert cdll.tail.prev.prev.prev.val == 70
    assert cdll.tail.prev.prev.prev.prev.val == 60
    assert cdll.tail.prev.prev.prev.prev.prev.val == 50
    assert cdll.tail.prev.prev.prev.prev.prev.prev.val == 40
    assert cdll.tail.prev.prev.prev.prev.prev.prev.prev.val == 30
    assert cdll.tail.prev.prev.prev.prev.prev.prev.prev.prev.val == 25
    assert cdll.tail.prev.prev.prev.prev.prev.prev.prev.prev.prev.val == 20
    assert cdll.head.prev.val == 100
    assert cdll.size == 11

    cdll = CircularDoublyLinkedList()
    cdll.insertHead(DNode(10))
    cdll.insertHead(DNode(500))
    cdll.insertHead(DNode(30))
    cdll.insertHead(DNode(40))
    cdll.insertHead(DNode(25))

    cdll.sortedInsert(DNode(501))
    assert cdll.head.val == 10
    assert cdll.head.next.val == 25
    assert cdll.head.next.next.val == 30
    assert cdll.head.next.next.next.val == 40
    assert cdll.head.next.next.next.next.val == 500
    assert cdll.head.next.next.next.next.next.val == 501
    assert cdll.head.prev.val == 501
    assert cdll.head.prev.prev.val == 500
    assert cdll.tail.val == 501
    assert cdll.tail.next.val == 10
    assert cdll.tail.prev.prev.val == 40
    assert cdll.head.prev.val == 501
    assert cdll.size == 6
