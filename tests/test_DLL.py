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
