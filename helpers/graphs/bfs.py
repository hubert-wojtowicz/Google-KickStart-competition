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

    def BFS(self, source):
        color = {key: 0 for key, val in self.vertex.items()}
        ancesty = {key: None for key, val in self.vertex.items()}
        dist = {key: None for key, val in self.vertex.items()}

        color[source] = 1
        dist[source] = 0
        ancesty[source] = None
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in self.vertex[u]:
                if color[v] is 0:
                    color[v] = 1
                    ancesty[v] = u
                    dist[v] = dist[u] + 1
                    queue.append(v)
            color[u] = 2
        return (ancesty, dist)

    def getShortestPath(self, s, v, ancesty):
        if s is v:
            return s
        elif ancesty[v] is None:
            return "Path does not exist."
        else:
            return self.getShortestPath(s, ancesty[v], ancesty) + " -> {}".format(v)


g = Graph()
g.addTwoWayEdge('r', 'v')
g.addTwoWayEdge('r', 's')
g.addTwoWayEdge('s', 'w')
g.addTwoWayEdge('w', 't')
g.addTwoWayEdge('w', 'x')
g.addTwoWayEdge('t', 'x')
g.addTwoWayEdge('t', 'u')
g.addTwoWayEdge('t', 'x')
g.addTwoWayEdge('x', 'y')
g.addTwoWayEdge('u', 'y')

(ancesty, dist) = g.BFS('s')

print(g.getShortestPath('s', 'x', ancesty))
print(dist)
print(ancesty)
