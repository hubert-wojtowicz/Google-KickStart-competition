#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict


class StableWallGraph:
    def __init__(self, pict, R, C):
        self.vertex = dict()
        for r in range(R-1, 0, -1):
            for c in range(C):
                self.addVertex(pict[r][c])
                if (pict[r][c] != pict[r-1][c]):
                    self.addEdge(pict[r][c], pict[r-1][c])
        for c in range(C):
            self.addVertex(pict[R-1][c])

    def addEdge(self, u, v):
        if not self.containsVertex(u):
            self.vertex[u] = set()
        if not self.containsVertex(v):
            self.vertex[v] = set()
        self.vertex[u].add(v)

    def addVertex(self, u):
        if not self.containsVertex(u):
            self.vertex[u] = set()

    def containsVertex(self, v):
        return v in self.vertex

    def DFS(self):
        color = {key: 0 for key, val in self.vertex.items()}
        ancesty = {key: None for key, val in self.vertex.items()}
        tin = {key: None for key, val in self.vertex.items()}
        tout = {key: None for key, val in self.vertex.items()}
        time = 0
        hasCycle = False

        for s in self.vertex:
            if color[s] == 0:
                stack = [s]
                color[s] = 1
                time += 1
                tin[s] = time

                while stack:
                    n_white = next((
                        e for e in self.vertex[stack[-1]] if color[e] == 0), None)

                    n_already_visited = next((
                        e for e in self.vertex[stack[-1]] if color[e] == 1), [])

                    if (any(n_already_visited)):
                        return (None, None, None, True)
                    elif n_white:
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

        return (ancesty, tin, tout, hasCycle)


for t in range(int(input())):
    R, C = [int(k) for k in input().split()]
    pict = []
    for i in range(R):
        pict.append([char for char in input()])

    g = StableWallGraph(pict, R, C)
    (ancesty, tin, tout, hasCycle) = g.DFS()

    if hasCycle:
        print("Case #{}: {}".format(t+1, -1))
    else:
        sorted_topology = OrderedDict(
            sorted({v: k for k, v in tout.items()}.items(), reverse=True)).values()
        print("Case #{}: {}".format(
            t+1, "".join(v for v in sorted_topology)))
