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
