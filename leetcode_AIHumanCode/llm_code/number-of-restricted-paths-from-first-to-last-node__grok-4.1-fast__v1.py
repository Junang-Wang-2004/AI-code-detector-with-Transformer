import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for a, b, c in edges:
            graph[a-1].append((b-1, c))
            graph[b-1].append((a-1, c))
        dist = [float('inf')] * n
        dist[n-1] = 0
        pq = [(0, n-1)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        order = sorted(range(n), key=lambda i: dist[i])
        cnt = [0] * n
        cnt[n-1] = 1
        for u in order:
            for v, _ in graph[u]:
                if dist[v] > dist[u]:
                    cnt[v] = (cnt[v] + cnt[u]) % MOD
        return cnt[0]
