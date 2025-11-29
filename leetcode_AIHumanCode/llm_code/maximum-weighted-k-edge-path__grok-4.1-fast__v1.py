class Solution(object):
    def maxWeight(self, n, edges, k, t):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        curr = [[False] * t for _ in range(n)]
        for i in range(n):
            curr[i][0] = True
        for _ in range(k):
            nxt = [[False] * t for _ in range(n)]
            for u in range(n):
                for c in range(t):
                    if curr[u][c]:
                        for v, wt in graph[u]:
                            nc = c + wt
                            if nc < t:
                                nxt[v][nc] = True
            curr = nxt
        res = -1
        for u in range(n):
            for c in range(t - 1, -1, -1):
                if curr[u][c]:
                    res = max(res, c)
                    break
        return res
