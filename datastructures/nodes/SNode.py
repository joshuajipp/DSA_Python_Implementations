import datastructures.nodes.SNode as Node


class Node:
    def __init__(self, val: int = 0, next: Node = None):
        self.val = val
        self.next = next
