class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        if u not in self.graph:
            return
        if v not in self.graph:
            return

        if v in self.graph[u]:
            self.graph[u].remove(v)
        if u in self.graph[v]:
            self.graph[v].remove(u)

    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            return

        for neighbour in self.graph[vertex][:]:
            self.remove_edge(neighbour, vertex)

        self.graph.pop(vertex)

    def __repr__(self):
        pass