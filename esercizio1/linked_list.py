class Element:
    def __init__(self, name):
        self.name = name
        self.set = None
        self.next = None


class LinkedList:
    def __init__(self, e):
        self.head = e
        self.tail = e


def make_set(e):
    s = LinkedList(e)
    e.set = s
    e.next = None


def find(e):
    return e.set.head.name


def union(A, B):
    if A is not B:
        A.tail.next = B.head
        A.tail = B.tail

        i = B.head
        while i is not None:
            i.set = A
            i = i.next


class HeuristicsLinkedList:
    def __init__(self, e):
        self.head = e
        self.tail = e
        self.length = 1


def heuristics_make_set(e):
    s = HeuristicsLinkedList(e)
    e.set = s
    e.next = None


def heuristics_union(A, B):
    if A is not B:
        if A.length >= B.length:
            A.length = A.length + B.length
            union(A, B)
        else:
            B.length = B.length + A.length
            union(B, A)
