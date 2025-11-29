import heapq
from collections import defaultdict

class Graph:
    def __init__(self, num_vertices, edge_list):
        self.neighbors = defaultdict(list)
        for u, v, weight in edge_list:
            self.neighbors[u].append((v, weight))

    def addEdge(self, edge):
        source, dest, cost = edge
        self.neighbors[source].append((dest, cost))

    def shortestPath(self, source, dest):
        dists = {node: float('inf') for node in self.neighbors}
        dists[source] = 0
        pq = [(0, source)]
        while pq:
            distance, node = heapq.heappop(pq)
            if distance > dists[node]:
                continue
            for neighbor, edge_cost in self.neighbors[node]:
                alt_dist = distance + edge_cost
                if alt_dist < dists.get(neighbor, float('inf')):
                    dists[neighbor] = alt_dist
                    heapq.heappush(pq, (alt_dist, neighbor))
        return dists.get(dest, -1)
