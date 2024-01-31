# Adjacency Matrix Representation

class Graph:
    def __init__(self, vertex_count=None):
        self.vertex_count = vertex_count
        self.adj_matrix = [[0] * vertex_count for e in range(vertex_count)]

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertex")

    def print_adj_matrix(self):
        i = 0
        for row_list in self.adj_matrix:
            print(i, "->", " ".join(map(str, row_list)))
            i += 1


graph = Graph(5)
# graph.add_edge(0, 1)
# graph.add_edge(0, 2)
# graph.add_edge(1, 4)
# graph.add_edge(2, 4)
# graph.add_edge(2, 3)
# graph.add_edge(3, 4)

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_adj_matrix()

print(graph.has_edge(0, 1))
graph.remove_edge(0, 1)
print(graph.has_edge(0, 1))

graph.print_adj_matrix()
