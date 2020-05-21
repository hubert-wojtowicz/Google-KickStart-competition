from collections import deque
from collections import OrderedDict


class Graph:
    def __init__(self):
        self.vertex = dict()

    def addOneWayEdge(self, u, v):
        if not self.containsVertex(u):
            self.vertex[u] = set()
        if not self.containsVertex(v):
            self.vertex[v] = set()
        self.vertex[u].add(v)

    def addTwoWayEdge(self, u, v):
        if not self.containsVertex(u):
            self.vertex[u] = set()
        if not self.containsVertex(v):
            self.vertex[v] = set()
        self.vertex[u].add(v)
        self.vertex[v].add(u)

    def addVertex(self, u):
        if not self.containsVertex(u):
            self.vertex[u] = set()

    def containsVertex(self, v):
        return v in self.vertex

    def containsEdge(self, u, v):
        ug = self.vertex.get(u)
        return ug and (v in ug)

    def TopologicalSort(self):
        tout = self.DFS()[2]
        return OrderedDict(sorted({v: k for k, v in tout.items()}.items(), reverse=True)).values()

    def DFS(self):
        color = {key: 0 for key, val in self.vertex.items()}
        ancesty = {key: None for key, val in self.vertex.items()}
        tin = {key: None for key, val in self.vertex.items()}
        tout = {key: None for key, val in self.vertex.items()}
        time = 0

        for s in self.vertex:
            if color[s] is 0:
                stack = [s]
                color[s] = 1
                time += 1
                tin[s] = time

                while stack:
                    n_white = next((
                        e for e in self.vertex[stack[-1]] if color[e] == 0), None)

                    if n_white:
                        ancesty[n_white] = stack[-1]
                        color[n_white] = 1
                        time += 1
                        tin[n_white] = time
                        stack.append(n_white)
                    else:
                        v = stack.pop()
                        time += 1
                        tout[v] = time
                        color[v] = 2

        return (ancesty, tin, tout)


acyclic = Graph()
acyclic.addOneWayEdge("slips", "shoes")
acyclic.addOneWayEdge("slips", "trousers")
acyclic.addOneWayEdge("trousers", "shoes")
acyclic.addOneWayEdge("trousers", "belt")
acyclic.addOneWayEdge("shirt", "belt")
acyclic.addOneWayEdge("shirt", "tie")
acyclic.addOneWayEdge("tie", "jacket")
acyclic.addOneWayEdge("belt", "jacket")
acyclic.addOneWayEdge("socks", "shoes")
acyclic.addVertex("watch")

print("Topological sort")
print(acyclic.TopologicalSort())
