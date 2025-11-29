import heapq
import sys

class Solution(object):
    def minTime(self, n, edges):
        INF = sys.maxsize
        g = [[] for _ in range(n)]
        for a, b, opn, cls in edges:
            g[a].append((b, opn, cls))
        tm = [INF] * n
        tm[0] = 0
        pq = [(0, 0)]
        while pq:
            t, u = heapq.heappop(pq)
            if t > tm[u]:
                continue
            for v, s, e in g[u]:
                if t > e:
                    continue
                leave = max(t, s)
                nt = leave + 1
                if nt < tm[v]:
                    tm[v] = nt
                    heapq.heappush(pq, (nt, v))
        res = tm[n - 1]
        return res if res != INF else -1
