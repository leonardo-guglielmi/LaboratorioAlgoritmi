class SetTreeElement:
    def __init__(self, name):
        self.name = name
        self.father = None


def make_set(e):
    e.father = e


def union(A, B):
    B.father = A


def find(e):
    if e is not e.father:
        e.father = find(e.father)
    return e.father
