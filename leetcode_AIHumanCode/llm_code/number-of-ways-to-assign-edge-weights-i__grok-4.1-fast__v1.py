from collections import deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)
        depths = [-1] * n
        depths[0] = 0
        q = deque([0])
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if depths[neighbor] == -1:
                    depths[neighbor] = depths[node] + 1
                    q.append(neighbor)
        max_dist = max(depths)
        return pow(2, max_dist - 1, MOD)
