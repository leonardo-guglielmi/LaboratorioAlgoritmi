class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


class Graph:
    def __init__(self):
        self.vertices = set()   # non c'è bisogno di creare un oggetto apposta
        self.edges = set()

    def create_vertex(self, v):
        self.vertices.add(v)

    def create_edge(self,  v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.edges.add(Edge(v1, v2))
