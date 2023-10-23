class Element:
    def __init__(self, name):
        self.name = name
        self.father = None


def make_set(e):
    e.father = e


def union(A, B):
    find(B).father = find(A)


def find(e):
    if e.father is not e:
        e.father = find(e.father)
    return e.father
