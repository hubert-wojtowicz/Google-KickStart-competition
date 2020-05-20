from collections import deque


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

    def DFS(self):
        color = {key: 0 for key, val in self.vertex.items()}
        ancesty = {key: None for key, val in self.vertex.items()}
        tin = {key: None for key, val in self.vertex.items()}
        tout = {key: None for key, val in self.vertex.items()}
        time = 0

        for s in self.vertex:
            if color[s] is 0:
                time = self.DFSVisit(s, color, ancesty, tin, tout, time)

        return (ancesty, tin, tout)

    def DFSVisit(self, u, color, ancesty, tin, tout, time):
        color[u] = 1
        time += 1
        tin[u] = time
        for v in self.vertex[u]:
            if color[v] is 0:
                ancesty[v] = u
                time = self.DFSVisit(v, color, ancesty, tin, tout, time)
        color[u] = 2
        time += 1
        tout[u] = time
        return time


g = Graph()
g.addOneWayEdge('z', 'z')
g.addOneWayEdge('u', 'x')
g.addOneWayEdge('v', 'y')
g.addOneWayEdge('w', 'y')
g.addOneWayEdge('w', 'z')
g.addOneWayEdge('u', 'v')
g.addOneWayEdge('x', 'v')
g.addOneWayEdge('y', 'x')

(ancesty, tin, tout) = g.DFS()

print(ancesty)
print(tin)
print(tout)
