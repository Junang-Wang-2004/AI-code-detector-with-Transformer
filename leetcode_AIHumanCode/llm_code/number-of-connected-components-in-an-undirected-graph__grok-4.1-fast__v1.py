class Solution:
    def countComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [False] * n
        
        def explore(start):
            stack = [start]
            vis[start] = True
            while stack:
                curr = stack.pop()
                for nxt in adj[curr]:
                    if not vis[nxt]:
                        vis[nxt] = True
                        stack.append(nxt)
        
        parts = 0
        for i in range(n):
            if not vis[i]:
                explore(i)
                parts += 1
        return parts
