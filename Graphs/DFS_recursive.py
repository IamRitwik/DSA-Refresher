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

    def depth_first_search(self, start):
        if start not in self.adjacency_list:
            raise Exception("Vertex is not in the graph!")
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}

        def _traverse(current):
            explored[current] = True
            visited.append(current)
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    _traverse(adjacent)
            return

        _traverse(start)
        return visited





graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')

graph.add_edge('A', 'B')

graph.add_edge('A', 'C')

graph.add_edge('B', 'D')

graph.add_edge('B', 'E')

graph.add_edge('C', 'F')

graph.add_edge('E', 'F')


print(graph.adjacency_list)

print(graph.depth_first_search('A'))
