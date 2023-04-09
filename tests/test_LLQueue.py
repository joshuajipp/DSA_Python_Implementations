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
