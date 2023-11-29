from collections import defaultdict

class Hamiltonian_Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.path = []
        self.vertex_mapping = {}  # Dictionary to map string vertices to integer indices
        self.index_mapping = {}  # Dictionary to map integer indices back to string vertices

    def addEdge(self, u, v):
        # If u or v is not already mapped to an index, create a new index
        if u not in self.vertex_mapping:
            index_u = len(self.vertex_mapping)
            self.vertex_mapping[u] = index_u
            self.index_mapping[index_u] = u
        else:
            index_u = self.vertex_mapping[u]

        if v not in self.vertex_mapping:
            index_v = len(self.vertex_mapping)
            self.vertex_mapping[v] = index_v
            self.index_mapping[index_v] = v
        else:
            index_v = self.vertex_mapping[v]

        # Add the edge to the graph
        self.graph[index_u].append(index_v)
        self.graph[index_v].append(index_u)

    def isHamiltonian(self, path, pos):
        # Check if the last vertex in the path is connected to the current vertex
        if len(path) == self.V:
            return True
        for v in self.graph[pos]:
            if v not in path:
                path.append(v)
                if self.isHamiltonian(path, v):
                    return True
                path.pop()
        return False

    def hamiltonianPath(self):
        for vertex in range(self.V):
            path = [vertex]
            if self.isHamiltonian(path, vertex):
                return "Graph has a Hamiltonian path", path
        return "Graph does not have a Hamiltonian path", None

    def test(self):
        status, path = self.hamiltonianPath()
        print(status)
        if path:
            mapped_path = [self.index_mapping[vertex] for vertex in path]
            print("Hamiltonian Path:", ' -> '.join(map(str, mapped_path)))


# Test case
# g1 = Graph(4)
# g1.addEdge('e', 'f')
# g1.addEdge('f', 'g')
# g1.addEdge('g', 'h')
# g1.addEdge('h', 'f')
# g1.addEdge('h', 'e')
# g1.test()
