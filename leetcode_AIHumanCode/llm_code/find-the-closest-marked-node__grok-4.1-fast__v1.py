import heapq
from collections import defaultdict

class Solution:
    def minimumDistance(self, n, edges, s, marked):
        targets = set(marked)
        graph = defaultdict(list)
        for start, end, weight in edges:
            graph[start].append((end, weight))
        INF = 10**18
        shortest = [INF] * n
        shortest[s] = 0
        pq = [(0, s)]
        while pq:
            distance, vertex = heapq.heappop(pq)
            if distance > shortest[vertex]:
                continue
            if vertex in targets:
                return distance
            for adj_vertex, edge_weight in graph[vertex]:
                candidate = distance + edge_weight
                if candidate < shortest[adj_vertex]:
                    shortest[adj_vertex] = candidate
                    heapq.heappush(pq, (candidate, adj_vertex))
        return -1
