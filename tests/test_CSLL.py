from datastructures.linear.CSLL import CircularSinglyLinkedList
from datastructures.nodes.SNode import SNode


def test_insertHead():
    singlyCLL = CircularSinglyLinkedList()
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
    singlyCLL = CircularSinglyLinkedList()
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
    singlyCLL = CircularSinglyLinkedList()
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


def test_deleteHead():
    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(1))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(3))
    singlyCLL.insertTail(SNode(4))
    singlyCLL.insertTail(SNode(5))

    singlyCLL.deleteHead()
    assert singlyCLL.head.val == 2
    assert singlyCLL.tail.val == 5
    assert singlyCLL.tail.next.val == 2
    assert singlyCLL.size == 4
    assert singlyCLL.tail.next.next.val == 3
    assert singlyCLL.tail.next.next.next.next.val == 5

    singlyCLL.deleteHead()
    assert singlyCLL.head.val == 3
    assert singlyCLL.tail.val == 5
    assert singlyCLL.tail.next.val == 3
    assert singlyCLL.size == 3
    assert singlyCLL.tail.next.next.val == 4
    assert singlyCLL.tail.next.next.next.next.val == 3

    singlyCLL.deleteHead()
    singlyCLL.deleteHead()
    assert singlyCLL.head.val == 5
    assert singlyCLL.head.next.val == 5
    assert singlyCLL.tail.val == 5
    assert singlyCLL.tail.next.val == 5
    assert singlyCLL.size == 1

    singlyCLL.deleteHead()
    assert singlyCLL.head is None
    assert singlyCLL.tail is None
    assert singlyCLL.size == 0


def test_deleteTail():
    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(1))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(3))
    singlyCLL.insertTail(SNode(4))
    singlyCLL.insertTail(SNode(5))

    singlyCLL.deleteTail()
    assert singlyCLL.head.val == 1
    assert singlyCLL.tail.val == 4
    assert singlyCLL.tail.next.val == 1
    assert singlyCLL.size == 4
    assert singlyCLL.tail.next.next.val == 2
    assert singlyCLL.tail.next.next.next.val == 3

    singlyCLL.deleteTail()
    assert singlyCLL.head.val == 1
    assert singlyCLL.tail.val == 3
    assert singlyCLL.tail.next.val == 1
    assert singlyCLL.size == 3
    assert singlyCLL.tail.next.next.val == 2
    assert singlyCLL.tail.next.next.next.next.val == 1

    singlyCLL.deleteTail()
    singlyCLL.deleteTail()
    assert singlyCLL.head.val == 1
    assert singlyCLL.head.next.val == 1
    assert singlyCLL.tail.val == 1
    assert singlyCLL.tail.next.val == 1
    assert singlyCLL.size == 1

    singlyCLL.deleteTail()
    assert singlyCLL.head is None
    assert singlyCLL.tail is None
    assert singlyCLL.size == 0


def test_delete():
    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(100))
    singlyCLL.insertTail(SNode(200))
    singlyCLL.insertTail(SNode(300))
    singlyCLL.insertTail(SNode(400))
    singlyCLL.insertTail(SNode(500))

    singlyCLL.delete(50)
    assert singlyCLL.head.val == 100
    assert singlyCLL.tail.val == 500
    assert singlyCLL.tail.next.val == 100
    assert singlyCLL.size == 5

    singlyCLL.delete(200)
    assert singlyCLL.head.val == 100
    assert singlyCLL.tail.val == 500
    assert singlyCLL.tail.next.val == 100
    assert singlyCLL.size == 4
    assert singlyCLL.tail.next.next.val == 300

    singlyCLL.delete(500)
    assert singlyCLL.head.val == 100
    assert singlyCLL.tail.val == 400
    assert singlyCLL.tail.next.val == 100
    assert singlyCLL.size == 3
    assert singlyCLL.tail.next.next.val == 300

    singlyCLL.delete(100)
    assert singlyCLL.head.val == 300
    assert singlyCLL.tail.val == 400
    assert singlyCLL.tail.next.val == 300
    assert singlyCLL.size == 2
    assert singlyCLL.tail.next.next.val == 400

    singlyCLL.delete(400)
    assert singlyCLL.head.val == 300
    assert singlyCLL.tail.val == 300
    assert singlyCLL.tail.next.val == 300
    assert singlyCLL.size == 1

    singlyCLL.delete(300)
    assert singlyCLL.head is None
    assert singlyCLL.tail is None
    assert singlyCLL.size == 0


def test_search():
    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(100))
    singlyCLL.insertTail(SNode(200))
    singlyCLL.insertTail(SNode(300))
    singlyCLL.insertTail(SNode(400))
    singlyCLL.insertTail(SNode(500))

    assert singlyCLL.search(50) == None
    assert singlyCLL.search(100) == singlyCLL.tail.next
    assert singlyCLL.search(200) == singlyCLL.head.next
    assert singlyCLL.search(300) == singlyCLL.head.next.next
    assert singlyCLL.search(400) == singlyCLL.head.next.next.next
    assert singlyCLL.search(500) == singlyCLL.tail


def test_isSorted():
    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(0))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(4))
    singlyCLL.insertTail(SNode(6))
    singlyCLL.insertTail(SNode(8))
    assert singlyCLL.isSorted() == True

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(5))
    singlyCLL.insertTail(SNode(4))
    singlyCLL.insertTail(SNode(3))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(1))
    assert singlyCLL.isSorted() == False

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(1))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(3))
    singlyCLL.insertTail(SNode(4))
    singlyCLL.insertTail(SNode(1))
    assert singlyCLL.isSorted() == False

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(5))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(3))
    singlyCLL.insertTail(SNode(4))
    singlyCLL.insertTail(SNode(5))
    assert singlyCLL.isSorted() == False


def test_sort():
    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(5))
    singlyCLL.insertTail(SNode(4))
    singlyCLL.insertTail(SNode(3))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(1))
    singlyCLL.sort()
    assert singlyCLL.head.val == 1
    assert singlyCLL.head.next.val == 2
    assert singlyCLL.head.next.next.val == 3
    assert singlyCLL.head.next.next.next.val == 4
    assert singlyCLL.head.next.next.next.next.val == 5
    assert singlyCLL.tail.val == 5
    assert singlyCLL.tail.next.val == 1
    assert singlyCLL.size == 5

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(5))
    singlyCLL.insertTail(SNode(2))
    singlyCLL.insertTail(SNode(8))
    singlyCLL.insertTail(SNode(0))
    singlyCLL.insertTail(SNode(15))
    singlyCLL.sort()
    assert singlyCLL.head.val == 0
    assert singlyCLL.head.next.val == 2
    assert singlyCLL.head.next.next.val == 5
    assert singlyCLL.head.next.next.next.val == 8
    assert singlyCLL.head.next.next.next.next.val == 15
    assert singlyCLL.tail.val == 15
    assert singlyCLL.tail.next.val == 0
    assert singlyCLL.size == 5

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(100))
    singlyCLL.insertTail(SNode(250))
    singlyCLL.insertTail(SNode(150))
    singlyCLL.insertTail(SNode(50))
    singlyCLL.insertTail(SNode(200))
    singlyCLL.insertTail(SNode(300))
    singlyCLL.insertTail(SNode(250))
    singlyCLL.sort()
    assert singlyCLL.head.val == 50
    assert singlyCLL.head.next.val == 100
    assert singlyCLL.head.next.next.val == 150
    assert singlyCLL.head.next.next.next.val == 200
    assert singlyCLL.head.next.next.next.next.val == 250
    assert singlyCLL.head.next.next.next.next.next.val == 250
    assert singlyCLL.head.next.next.next.next.next.next.val == 300
    assert singlyCLL.tail.val == 300
    assert singlyCLL.tail.next.val == 50
    assert singlyCLL.size == 7

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(100))
    singlyCLL.insertTail(SNode(200))
    singlyCLL.insertTail(SNode(300))
    singlyCLL.insertTail(SNode(400))
    singlyCLL.insertTail(SNode(500))
    singlyCLL.sort()
    assert singlyCLL.head.val == 100
    assert singlyCLL.head.next.val == 200
    assert singlyCLL.head.next.next.val == 300
    assert singlyCLL.head.next.next.next.val == 400
    assert singlyCLL.head.next.next.next.next.val == 500
    assert singlyCLL.tail.val == 500
    assert singlyCLL.tail.next.val == 100
    assert singlyCLL.size == 5


def test_sortedInsert():
    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.insertTail(SNode(40))
    singlyCLL.insertTail(SNode(30))
    singlyCLL.insertTail(SNode(50))
    singlyCLL.insertTail(SNode(20))
    singlyCLL.insertTail(SNode(10))
    singlyCLL.sortedInsert(SNode(25))
    assert singlyCLL.head.val == 10
    assert singlyCLL.head.next.val == 20
    assert singlyCLL.head.next.next.val == 25
    assert singlyCLL.head.next.next.next.val == 30
    assert singlyCLL.head.next.next.next.next.val == 40
    assert singlyCLL.head.next.next.next.next.next.val == 50
    assert singlyCLL.tail.val == 50
    assert singlyCLL.tail.next.val == 10
    assert singlyCLL.size == 6

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.sortedInsert(SNode(100))
    singlyCLL.sortedInsert(SNode(200))
    singlyCLL.sortedInsert(SNode(300))
    singlyCLL.sortedInsert(SNode(400))
    singlyCLL.sortedInsert(SNode(500))
    assert singlyCLL.head.val == 100
    assert singlyCLL.head.next.val == 200
    assert singlyCLL.head.next.next.val == 300
    assert singlyCLL.head.next.next.next.val == 400
    assert singlyCLL.head.next.next.next.next.val == 500
    assert singlyCLL.tail.val == 500
    assert singlyCLL.tail.next.val == 100
    assert singlyCLL.size == 5

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.sortedInsert(SNode(100))
    singlyCLL.sortedInsert(SNode(200))
    singlyCLL.sortedInsert(SNode(300))
    singlyCLL.sortedInsert(SNode(400))
    singlyCLL.sortedInsert(SNode(500))
    singlyCLL.sortedInsert(SNode(50))
    singlyCLL.sortedInsert(SNode(600))
    singlyCLL.sortedInsert(SNode(350))
    singlyCLL.sortedInsert(SNode(250))
    singlyCLL.sortedInsert(SNode(150))
    assert singlyCLL.head.val == 50
    assert singlyCLL.head.next.val == 100
    assert singlyCLL.head.next.next.val == 150
    assert singlyCLL.head.next.next.next.val == 200
    assert singlyCLL.head.next.next.next.next.val == 250
    assert singlyCLL.head.next.next.next.next.next.val == 300
    assert singlyCLL.head.next.next.next.next.next.next.val == 350
    assert singlyCLL.head.next.next.next.next.next.next.next.val == 400
    assert singlyCLL.head.next.next.next.next.next.next.next.next.val == 500
    assert singlyCLL.head.next.next.next.next.next.next.next.next.next.val == 600
    assert singlyCLL.tail.val == 600
    assert singlyCLL.tail.next.val == 50
    assert singlyCLL.size == 10

    singlyCLL = CircularSinglyLinkedList()
    singlyCLL.sortedInsert(SNode(4000))
    singlyCLL.sortedInsert(SNode(3000))
    singlyCLL.sortedInsert(SNode(8000))
    singlyCLL.sortedInsert(SNode(1000))
    singlyCLL.sortedInsert(SNode(5000))
    singlyCLL.sortedInsert(SNode(2000))
    singlyCLL.sortedInsert(SNode(7000))
    singlyCLL.sortedInsert(SNode(6000))
    assert singlyCLL.head.val == 1000
    assert singlyCLL.head.next.val == 2000
    assert singlyCLL.head.next.next.val == 3000
    assert singlyCLL.head.next.next.next.val == 4000
    assert singlyCLL.head.next.next.next.next.val == 5000
    assert singlyCLL.head.next.next.next.next.next.val == 6000
    assert singlyCLL.head.next.next.next.next.next.next.val == 7000
    assert singlyCLL.head.next.next.next.next.next.next.next.val == 8000
    assert singlyCLL.tail.val == 8000
    assert singlyCLL.tail.next.val == 1000
    assert singlyCLL.size == 8
