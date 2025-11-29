import heapq
from collections import defaultdict

class C1:

    def __init__(self, a1, a2):
        self.neighbors = defaultdict(list)
        for v1, v2, v3 in a2:
            self.neighbors[v1].append((v2, v3))

    def addEdge(self, a1):
        v1, v2, v3 = a1
        self.neighbors[v1].append((v2, v3))

    def shortestPath(self, a1, a2):
        v1 = {node: float('inf') for v2 in self.neighbors}
        v1[a1] = 0
        v3 = [(0, a1)]
        while v3:
            v4, v2 = heapq.heappop(v3)
            if v4 > v1[v2]:
                continue
            for v5, v6 in self.neighbors[v2]:
                v7 = v4 + v6
                if v7 < v1.get(v5, float('inf')):
                    v1[v5] = v7
                    heapq.heappush(v3, (v7, v5))
        return v1.get(a2, -1)
