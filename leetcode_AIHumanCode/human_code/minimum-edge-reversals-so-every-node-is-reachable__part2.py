# Time:  O(n)
# Space: O(n)
# dfs, tree dp
class Solution2(object):
    def minEdgeReversals(self, n, edges):
        """
        """
        def dfs1(u, p):
            return sum(adj[u][v]+dfs1(v, u) for v in adj[u] if v != p)

        def dfs2(u, curr):
            result[u] = curr
            for v in adj[u]:
                if result[v] == -1:
                    dfs2(v, curr-adj[u][v]+adj[v][u])
    
        adj = collections.defaultdict(dict)
        for u, v in edges:
            adj[u][v] = 0
            adj[v][u] = 1
        result = [-1]*n
        dfs2(0, dfs1(0, -1))
        return result
