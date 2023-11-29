from collections import defaultdict

class Euler_Graph:
    path = []
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0
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

    def rmvEdge(self, u, v):
        # Remove edge u-v from the graph
        index_u, index_v = self.vertex_mapping[u], self.vertex_mapping[v]

        self.graph[index_u].remove(index_v)
        self.graph[index_v].remove(index_u)

    def DFSCount(self, v, visited):
        # Count reachable vertices from v using DFS
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count += self.DFSCount(i, visited)
        return count

    def isValidNextEdge(self, u, v):
        # Check if edge u-v can be considered as the next edge in the Euler Tour
        index_u, index_v = self.vertex_mapping[u], self.vertex_mapping[v]

        if len(self.graph[index_u]) == 1:
            return True
        else:
            visited = [False] * self.V
            count1 = self.DFSCount(index_u, visited)

            self.rmvEdge(u, v)

            visited = [False] * self.V
            count2 = self.DFSCount(index_u, visited)

            self.addEdge(u, v)

            return False if count1 > count2 else True

    def printEulerUtil(self, u):
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            if self.isValidNextEdge(self.index_mapping[u], self.index_mapping[v]):
                print("%s-%s " % (self.index_mapping[u], self.index_mapping[v])),
                self.rmvEdge(self.index_mapping[u], self.index_mapping[v])
                edge = []
                edge.append(self.index_mapping[u])
                edge.append(self.index_mapping[v])
                self.path.append(edge)
                self.printEulerUtil(v)

    def printEulerTour(self):
        # Find a vertex with an odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break

        # Print the tour starting from the odd vertex
        print("\n")
        self.printEulerUtil(u)


# Example usage:
# g1 = Graph(4)
# g1.addEdge('e', 'f')
# g1.addEdge('f', 'g')
# g1.addEdge('g', 'h')
# g1.addEdge('h', 'f')
# g1.addEdge('h', 'e')
# g1.printEulerTour()

# print(g1.path)



