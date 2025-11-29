from collections import deque
from typing import List

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MAX_W = 26
        LOG = 18
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            w -= 1
            adj[u].append((v, w))
            adj[v].append((u, w))
        depth = [0] * n
        parent = [[-1] * LOG for _ in range(n)]
        cnt = [[0] * MAX_W for _ in range(n)]
        visited = [False] * n
        q = deque([0])
        visited[0] = True
        while q:
            u = q.popleft()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[v][0] = u
                    cnt[v] = cnt[u][:]
                    cnt[v][w] += 1
                    q.append(v)
        for k in range(1, LOG):
            for u in range(n):
                p = parent[u][k - 1]
                if p != -1:
                    parent[u][k] = parent[p][k - 1]
        def get_lca(a: int, b: int) -> int:
            if depth[a] > depth[b]:
                a, b = b, a
            diff = depth[b] - depth[a]
            for k in range(LOG):
                if (diff & (1 << k)):
                    b = parent[b][k]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if parent[a][k] != parent[b][k]:
                    a = parent[a][k]
                    b = parent[b][k]
            return parent[a][0]
        result = [0] * len(queries)
        for i, (a, b) in enumerate(queries):
            l = get_lca(a, b)
            dist = depth[a] + depth[b] - 2 * depth[l]
            max_freq = max(cnt[a][w] + cnt[b][w] - 2 * cnt[l][w] for w in range(MAX_W))
            result[i] = dist - max_freq
        return result
