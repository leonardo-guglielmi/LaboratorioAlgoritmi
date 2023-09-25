# probabilmente dovrai fare un dizionario per tenere traccia di tutti gli insiemi

class Element:
    def __init__(self, name):
        self.name = name
        self.head = None
        # self.tail = None >tail mi serve? negli appunti la trovo, ma nel libro non c'è e per le operazioni neanche mi serve
# ======================================================================================================================
class QuickUnionTree:
    def __init__(self, e):
        self.rep = e

def make_set(e):
    return QuickUnionTree(e)

# vuole solo il nome
def union(a, b):
    b.rep.head = a.rep

def find(e):
    if e.head is not None:
        return find(e.head)
    else:
        return e.name

# ========================================================================================
class BalancedQuickUnionTree:
    def __init__(self, e):
        self.rank = 0
        self.rep = e

def balanced_make_set(e):
    return BalancedQuickUnionTree(e)

def balanced_union(a, b):
    if a.rank > b.rank:
        union(a, b)
    elif a.rank < b.rank:
        union(b, a)
    else:
        union(a, b)
        a.rank = a.rank + 1