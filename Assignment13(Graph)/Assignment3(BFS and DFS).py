# List Representation
class Graph:
    def __init__(self, vertex_count=None):
        self.vertex_count = vertex_count
        self.adj_list = {v: [] for v in range(vertex_count)}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Vertex")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u] = [(vertex, weight) for vertex, weight in self.adj_list[u] if vertex != v]
            self.adj_list[v] = [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u]
        else:
            print("Invalid Vertex")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex == v for vertex, w in self.adj_list[u])
        else:
            print("Invalid Vertex")

    def print_adj_list(self):
        for vertex, list in self.adj_list.items():
            print(vertex, "->", list)
        print()

    def bfs(self):
        vis = [False for e in range(self.vertex_count)]
        queue = [0]
        vis[0] = True
        bfsList = []
        while len(queue) > 0:
            data = queue.pop(0)
            bfsList.append(data)
            for d in self.adj_list[data]:
                if vis[d[0]] is False:
                    queue.append(d[0])
                    vis[d[0]] = True
        print('BFS Traversal is :', bfsList)

    def dfs(self):
        vis = [False for e in range(self.vertex_count)]
        stack = [0]
        vis[0] = True
        dfsList = []
        while len(stack) > 0:
            data = stack.pop()
            dfsList.append(data)
            for d in self.adj_list[data]:
                if vis[d[0]] is False:
                    stack.append(d[0])
                    vis[d[0]] = True
        print('DFS Traversal is :', dfsList)


graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)
graph.print_adj_list()
graph.bfs()
graph.dfs()
