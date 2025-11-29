# Time:  O(n)
# Space: O(n)
# dfs, tree dp
class Solution2(object):
    def maximumScoreAfterOperations(self, edges, values):
        """
        """
        def dfs(u, p):
            if len(adj[u]) == (1 if u else 0):
                return values[u]
            return min(sum(dfs(v, u) for v in adj[u] if v != p), values[u])  # min(pick u, not pick u)

        adj = [[] for _ in range(len(values))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return sum(values)-dfs(0, -1)
