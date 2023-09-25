class QuickFindElement:
    def __init__(self, value, father):
        self.value = value
        self.father = father

elementsSet = set()

def makeSet(e):
    elementsSet.add(e)

# da aggiungere la path compression
def union(a,b):
    pass