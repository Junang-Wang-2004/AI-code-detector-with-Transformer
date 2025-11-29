import heapq

class Solution:
    def shortestPathWithHops(self, n, edges, s, d, k):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[s][0] = 0
        pq = [(0, s, 0)]
        while pq:
            cost, u, used = heapq.heappop(pq)
            if cost > dist[u][used]:
                continue
            if u == d:
                return cost
            for v, w in graph[u]:
                if cost + w < dist[v][used]:
                    dist[v][used] = cost + w
                    heapq.heappush(pq, (dist[v][used], v, used))
                if used < k and cost < dist[v][used + 1]:
                    dist[v][used + 1] = cost
                    heapq.heappush(pq, (dist[v][used + 1], v, used + 1))
        return -1
