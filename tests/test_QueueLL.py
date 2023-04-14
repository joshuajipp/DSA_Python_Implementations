from datastructures.linear.QueueLL import LinkedListQueue
from datastructures.nodes.SNode import SNode


def test_enqueue():
    queue = LinkedListQueue()
    queue.enqueue(SNode(1))
    assert queue.size == 1
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    assert queue.size == 3
    queue.enqueue(SNode(4))
    queue.enqueue(SNode(5))
    assert queue.size == 5
    assert queue.isEmpty() == False


def test_integration():
    queue = LinkedListQueue()
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(4))
    queue.enqueue(SNode(5))
    assert queue.isEmpty() == False
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.size == 4
    assert queue.peek() == 2
    assert queue.dequeue() == 2
    assert queue.size == 3
    assert queue.dequeue() == 3
    assert queue.size == 2
    assert queue.dequeue() == 4
    assert queue.size == 1
    assert queue.dequeue() == 5
    assert queue.size == 0
    assert queue.isEmpty() == True


def test_peek():
    queue = LinkedListQueue()
    assert queue.peek() == None
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(4))
    queue.enqueue(SNode(5))
    assert queue.peek() == 1
    assert queue.size == 5


def test_dequeue():
    queue = LinkedListQueue()
    queue.enqueue(SNode(7))
    queue.enqueue(SNode(5))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(-1))
    assert queue.dequeue() == 7
    assert queue.size == 4
    assert queue.dequeue() == 5
    assert queue.size == 3
    assert queue.dequeue() == 3
    assert queue.size == 2
    assert queue.dequeue() == 1
    assert queue.size == 1
    assert queue.dequeue() == -1
    assert queue.size == 0


def test_isEmpty():
    queue = LinkedListQueue()
    assert queue.isEmpty() == True
    queue.enqueue(SNode(1))
    assert queue.isEmpty() == False
    queue.enqueue(SNode(2))
    assert queue.isEmpty() == False
    queue.enqueue(SNode(3))
    assert queue.isEmpty() == False
    queue.enqueue(SNode(4))
    assert queue.isEmpty() == False
    queue.enqueue(SNode(5))
    assert queue.isEmpty() == False


def test_contains():
    queue = LinkedListQueue()
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(4))
    queue.enqueue(SNode(5))
    assert queue.contains(1) == True
    assert queue.contains(2) == True
    assert queue.contains(3) == True
    assert queue.contains(4) == True
    assert queue.contains(5) == True
    assert queue.contains(6) == False
    assert queue.contains(7) == False
    assert queue.contains(8) == False
    assert queue.contains(9) == False
    assert queue.contains(10) == False


def test_clear():
    queue = LinkedListQueue()
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(4))
    queue.enqueue(SNode(5))
    assert queue.size == 5
    queue.clear()
    assert queue.size == 0
    assert queue.isEmpty() == True


def test_insertHead_override():
    queue = LinkedListQueue()
    assert queue.insertHead(SNode(1)) is None
    assert queue.size == 0
    assert queue.isEmpty() == True


def test_deleteHead_override():
    queue = LinkedListQueue()
    queue.enqueue(SNode(1))
    assert queue.deleteHead() is None
    assert queue.size == 1
    assert queue.isEmpty() == False


def test_deleteTail_override():
    queue = LinkedListQueue()
    queue.enqueue(SNode(1))
    assert queue.deleteTail() is None
    assert queue.size == 1
    assert queue.isEmpty() == False


def test_insertTail_override():
    queue = LinkedListQueue()
    assert queue.insertTail(SNode(1)) is None
    assert queue.size == 0
    assert queue.isEmpty() == True


def test_insert_override():
    queue = LinkedListQueue()
    assert queue.insert(SNode(1), 0) is None
    assert queue.size == 0
    assert queue.isEmpty() == True


def test_sortedInsert_override():
    queue = LinkedListQueue()
    assert queue.sortedInsert(SNode(1)) is None
    assert queue.size == 0
    assert queue.isEmpty() == True


def test_isSorted_override():
    queue = LinkedListQueue()
    assert queue.isSorted() == None


def test_sort_override():
    queue = LinkedListQueue()
    queue.enqueue(SNode(5))
    queue.enqueue(SNode(8))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(1))

    assert queue.sort() == None
    assert queue.peek() == 5


def test_search_override():
    queue = LinkedListQueue()
    queue.enqueue(SNode(5))
    queue.enqueue(SNode(8))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(1))

    assert queue.search(5) == None
    assert queue.search(8) == None
    assert queue.search(3) == None
    assert queue.search(1) == None
    assert queue.search(0) == None
    assert queue.search(4) == None
    assert queue.search(6) == None
    assert queue.search(7) == None
    assert queue.search(9) == None
    assert queue.search(10) == None


def test_delete_override():
    queue = LinkedListQueue()
    queue.enqueue(SNode(5))
    queue.enqueue(SNode(8))
    queue.enqueue(SNode(3))
    queue.enqueue(SNode(1))

    queue.delete(5)
    assert queue.size == 4
    assert queue.peek() == 5
