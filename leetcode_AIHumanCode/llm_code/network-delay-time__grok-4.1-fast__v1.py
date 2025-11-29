import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        dist = [float('inf')] * n
        dist[k - 1] = 0
        pq = [(0, k - 1)]
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            for v, wt in graph[u]:
                cand = cost + wt
                if cand < dist[v]:
                    dist[v] = cand
                    heapq.heappush(pq, (cand, v))
        mx = max(dist)
        return mx if mx < float('inf') else -1
