from timeit import default_timer as timer


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


# funzioni con registro de tempo
def timed_make_set(e, log):
    timestamp = timer()
    make_set(e)
    log.t += timer() - timestamp


def timed_find(e, log):
    timestamp = timer()
    res = find(e)
    log.t += timer() - timestamp


def timed_union(A, B, log):
    timestamp = timer()
    union(A, B)
    log.t += timer() - timestamp