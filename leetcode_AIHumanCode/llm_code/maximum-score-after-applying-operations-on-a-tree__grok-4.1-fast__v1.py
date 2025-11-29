from collections import deque

class Solution:
    def maximumScoreAfterOperations(self, edges, values):
        n = len(values)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        ch = [[] for _ in range(n)]
        vis = [False] * n
        q = deque([0])
        vis[0] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    ch[u].append(v)
                    q.append(v)
        tot = sum(values)

        def get_dp(nd):
            if not ch[nd]:
                return values[nd]
            sm = sum(get_dp(c) for c in ch[nd])
            return min(sm, values[nd])

        return tot - get_dp(0)
