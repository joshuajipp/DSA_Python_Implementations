from datastructures.linear.SLL import SinglyLinkedList
from datastructures.linear.LLStack import LinkedListStack
from datastructures.nodes.SNode import SNode


def test_integration():
    stack = LinkedListStack()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.push(SNode(4))
    stack.push(SNode(5))

    assert stack.isEmpty() == False
    assert stack.size == 5
    assert stack.peek() == 5
    assert stack.pop() == 5
    assert stack.peek() == 4
    assert stack.size == 4
    assert stack.pop() == 4
    assert stack.peek() == 3
    assert stack.size == 3
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.size == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.size == 1
    assert stack.pop() == 1
    assert stack.size == 0
    assert stack.isEmpty() == True


def test_peek():
    stack = LinkedListStack()
    assert stack.peek() == None
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.push(SNode(4))
    stack.push(SNode(5))
    assert stack.peek() == 5
    assert stack.size == 5


def test_pop():
    stack = LinkedListStack()
    stack.push(SNode(7))
    stack.push(SNode(5))
    stack.push(SNode(3))
    stack.push(SNode(1))
    stack.push(SNode(-1))
    assert stack.pop() == -1
    assert stack.size == 4
    assert stack.pop() == 1
    assert stack.size == 3
    assert stack.pop() == 3
    assert stack.size == 2
    assert stack.pop() == 5
    assert stack.size == 1
    assert stack.pop() == 7
    assert stack.size == 0


def test_push():
    stack = LinkedListStack()
    stack.push(SNode(1))
    assert stack.size == 1
    stack.push(SNode(2))
    stack.push(SNode(3))
    assert stack.size == 3
    stack.push(SNode(4))
    stack.push(SNode(5))
    assert stack.size == 5


def test_isEmpty():
    stack = LinkedListStack()
    assert stack.isEmpty() == True
    stack.push(SNode(1))
    assert stack.isEmpty() == False
    stack.push(SNode(2))
    assert stack.isEmpty() == False
    stack.push(SNode(3))
    assert stack.isEmpty() == False
    stack.push(SNode(4))
    assert stack.isEmpty() == False
    stack.push(SNode(5))
    assert stack.isEmpty() == False


def test_contains():
    stack = LinkedListStack()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.push(SNode(4))
    stack.push(SNode(5))
    assert stack.contains(1) == True
    assert stack.contains(2) == True
    assert stack.contains(3) == True
    assert stack.contains(4) == True
    assert stack.contains(5) == True
    assert stack.contains(6) == False
    assert stack.contains(7) == False
    assert stack.contains(8) == False
    assert stack.contains(9) == False
    assert stack.contains(10) == False


def test_clear():
    stack = LinkedListStack()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.push(SNode(4))
    stack.push(SNode(5))
    assert stack.size == 5
    stack.clear()
    assert stack.size == 0
    assert stack.isEmpty() == True
