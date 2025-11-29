from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        adj_rev = [[] for _ in range(n)]
        deg = [0] * n
        for u in range(n):
            deg[u] = len(graph[u])
            for v in graph[u]:
                adj_rev[v].append(u)
        q = deque(u for u in range(n) if deg[u] == 0)
        vis = [False] * n
        while q:
            u = q.popleft()
            vis[u] = True
            for v in adj_rev[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        return [i for i in range(n) if vis[i]]
