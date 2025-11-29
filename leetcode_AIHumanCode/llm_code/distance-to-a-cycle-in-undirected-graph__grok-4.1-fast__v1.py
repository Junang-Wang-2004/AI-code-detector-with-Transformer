from collections import deque

class Solution:
    def distanceToCycle(self, n, edges):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        deg = [len(graph[i]) for i in range(n)]
        q = deque(i for i in range(n) if deg[i] == 1)
        while q:
            u = q.popleft()
            deg[u] = 0
            for v in graph[u]:
                if deg[v] > 0:
                    deg[v] -= 1
                    if deg[v] == 1:
                        q.append(v)
        sources = [i for i in range(n) if deg[i] > 0]
        res = [-1] * n
        qq = deque(sources)
        for s in sources:
            res[s] = 0
        while qq:
            u = qq.popleft()
            for v in graph[u]:
                if res[v] == -1:
                    res[v] = res[u] + 1
                    qq.append(v)
        return res
