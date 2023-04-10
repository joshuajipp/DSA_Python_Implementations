from datastructures.linear.singlyCLL import SinglyCircularLinkedList
from datastructures.nodes.SNode import SNode


def test_insertHead():
    sll = SinglyCircularLinkedList()
    sll.insertHead(SNode(1))
    sll.insertHead(SNode(2))
    sll.insertHead(SNode(3))
    assert sll.head.val == 3
    assert sll.tail.val == 1
    assert sll.head.next.val == 2
    assert sll.tail.next.val == 3
    assert sll.size == 3
    assert sll.head.next.next.val == 1
    assert sll.tail.next.next.val == 2
