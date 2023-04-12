from datastructures.linear.LLQueue import LinkedListQueue
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
