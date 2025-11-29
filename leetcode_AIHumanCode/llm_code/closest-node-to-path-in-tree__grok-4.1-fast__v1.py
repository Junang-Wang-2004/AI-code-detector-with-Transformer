from collections import deque
from typing import List

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        LOG = 18
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        depth = [0] * n
        par = [[-1] * n for _ in range(LOG)]
        
        vis = [False] * n
        queue = deque([0])
        vis[0] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    depth[v] = depth[u] + 1
                    par[0][v] = u
                    queue.append(v)
        
        for k in range(1, LOG):
            for i in range(n):
                if par[k - 1][i] != -1:
                    par[k][i] = par[k - 1][par[k - 1][i]]
        
        def lift(node: int, steps: int) -> int:
            k = 0
            while steps > 0:
                if steps & 1:
                    node = par[k][node]
                steps >>= 1
                k += 1
            return node
        
        def get_lca(x: int, y: int) -> int:
            if depth[x] > depth[y]:
                x, y = y, x
            y = lift(y, depth[y] - depth[x])
            if x == y:
                return x
            for k in range(LOG - 1, -1, -1):
                if par[k][x] != par[k][y]:
                    x = par[k][x]
                    y = par[k][y]
            return par[0][x]
        
        ans = []
        for s, e, node in query:
            lca1 = get_lca(s, e)
            lca2 = get_lca(s, node)
            lca3 = get_lca(e, node)
            opts = [lca1, lca2, lca3]
            best = max(opts, key=lambda z: depth[z])
            ans.append(best)
        return ans
