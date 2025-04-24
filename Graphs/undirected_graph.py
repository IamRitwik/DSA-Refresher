class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            raise Exception("Vertex is already in the graph!")
        self.adjacency_list[vertex] = []
        return self

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.adjacency_list or vertex_2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex_1].append(vertex_2)
        self.adjacency_list[vertex_2].append(vertex_1)
        return self

    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.adjacency_list or vertex_2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        if vertex_1 in self.adjacency_list[vertex_2]:
            self.adjacency_list[vertex_2].remove(vertex_1)
        if vertex_2 in self.adjacency_list[vertex_1]:
            self.adjacency_list[vertex_1].remove(vertex_2)
        return self

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            raise Exception("Vertex is already in the graph!")
        for neighbour in self.adjacency_list[vertex]:
            self.adjacency_list[neighbour].remove(vertex)
        self.adjacency_list.pop(vertex)
        return self



graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'D')


print(graph.adjacency_list)

graph.remove_vertex('B')

print(graph.adjacency_list)
