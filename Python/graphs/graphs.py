class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        pass

    def remove_edge(self, u, v):
        pass

    def remove_vertex(self, vertex):
        pass

    def __repr__(self):
        pass