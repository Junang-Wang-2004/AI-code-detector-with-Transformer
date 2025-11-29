from collections import defaultdict
from heapq import heappop, heappush
v1 = int(input())

class C1(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, a1, a2, a3=1):
        self.graph[a1].append((a2, a3))

    def get_nodes(self):
        return self.graph.keys()

class C2(object):

    def __init__(self, a1, a2):
        v1 = a1.graph
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[a2] = 0
        self.prev = defaultdict(lambda: None)
        v2 = []
        heappush(v2, (self.dist[a2], a2))
        while v2:
            v3, v4 = heappop(v2)
            if self.dist[v4] < v3:
                continue
            for v5, v6 in v1[v4]:
                v7 = v3 + v6
                if self.dist[v5] > v7:
                    self.dist[v5] = v7
                    self.prev[v5] = v4
                    heappush(v2, (v7, v5))

    def shortest_distance(self, a1):
        return self.dist[a1]

    def shortest_path(self, a1):
        v1 = []
        v2 = a1
        while v2 is not None:
            v1.append(v2)
            v2 = self.prev[v2]
        return v1[::-1]
v2 = C1()
for v3 in range(v1 - 1):
    v4, v5 = map(int, input().split())
    v2.add_edge(v4 - 1, v5 - 1)
    v2.add_edge(v5 - 1, v4 - 1)
v6 = C2(v2, 0)
v7 = C2(v2, v1 - 1)
v8, v9 = (0, 0)
for v10 in range(v1):
    if v6.shortest_distance(v10) <= v7.shortest_distance(v10):
        v8 += 1
    else:
        v9 += 1
if v8 > v9:
    print('Fennec')
else:
    print('Snuke')
