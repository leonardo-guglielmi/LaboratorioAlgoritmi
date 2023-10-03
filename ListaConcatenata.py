class Element:
    def __init__(self, name):
        self.name = name
        self.set = None
        self.next = None


# lista concatenata standard ===========================================================================================


class ChainedList:
    def __init__(self, e):
        self.head = e
        self.tail = e


def make_set(e):
    s = ChainedList(e)
    e.set = s
    e.next = None


def find(e):
    return e.set.head.name


def union(A, B):
    # accodo all'insieme A l'insieme B
    if A is not B:
        A.tail.next = B.head
        A.tail = B.tail

        i = B.head
        while i is not None:
            i.set = A
            i = i.next


# lista concatenata pesata =============================================================================================


class HeuristicsChainedList:
    def __init__(self, e):
        self.head = e
        self.tail = e
        self.length = 1


def heuristics_make_set(e):
    s = HeuristicsChainedList(e)
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
