import heapq

class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for a, b, time in roads:
            graph[a].append((b, time))
            graph[b].append((a, time))
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(pq, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n - 1]
