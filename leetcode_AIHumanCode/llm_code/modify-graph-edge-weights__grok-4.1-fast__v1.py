import heapq

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        graph_min = [[] for _ in range(n)]
        graph_fixed = [[] for _ in range(n)]
        for u, v, w in edges:
            if w != -1:
                graph_min[u].append((v, w))
                graph_min[v].append((u, w))
                graph_fixed[u].append((v, w))
                graph_fixed[v].append((u, w))
            else:
                graph_min[u].append((v, 1))
                graph_min[v].append((u, 1))

        def shortest(graph, start):
            INF = float('inf')
            distances = [INF] * n
            distances[start] = 0
            pq = [(0, start)]
            while pq:
                distance, u = heapq.heappop(pq)
                if distance > distances[u]:
                    continue
                for v, weight in graph[u]:
                    alt = distances[u] + weight
                    if alt < distances[v]:
                        distances[v] = alt
                        heapq.heappush(pq, (alt, v))
            return distances

        min_distances = shortest(graph_min, source)
        if min_distances[destination] > target:
            return []

        fixed_distances = shortest(graph_fixed, destination)
        if fixed_distances[source] < target:
            return []

        for u, v, w in edges:
            if w == -1:
                cand1 = target - min_distances[u] - fixed_distances[v]
                cand2 = target - min_distances[v] - fixed_distances[u]
                edges[edges.index([u, v, w])][2] = max(cand1, cand2, 1)
        return edges
