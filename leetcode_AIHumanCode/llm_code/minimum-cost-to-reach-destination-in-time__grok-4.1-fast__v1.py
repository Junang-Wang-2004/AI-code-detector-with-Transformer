import heapq

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        g = [[] for _ in range(n)]
        for a, b, t in edges:
            g[a].append((b, t))
            g[b].append((a, t))
        min_t = [float('inf')] * n
        min_t[0] = 0
        pq = []
        heapq.heappush(pq, (passingFees[0], 0, 0))
        while pq:
            c, u, tm = heapq.heappop(pq)
            if tm > maxTime:
                continue
            if u == n - 1:
                return c
            for v, dt in g[u]:
                nt = tm + dt
                if nt < min_t[v]:
                    min_t[v] = nt
                    heapq.heappush(pq, (c + passingFees[v], v, nt))
        return -1
