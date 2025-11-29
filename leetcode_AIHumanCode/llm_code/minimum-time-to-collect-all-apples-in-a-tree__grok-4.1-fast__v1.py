class Solution:
    def minTime(self, n, edges, hasApple):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(u, p):
            cost = 0
            for v in adj[u]:
                if v == p:
                    continue
                subcost = dfs(v, u)
                if subcost > 0 or hasApple[v]:
                    cost += subcost + 2
            return cost
        
        return dfs(0, -1)
