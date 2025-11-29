# Time:  O(n)
# Space: O(n)
# dfs, tree dp
class Solution5(object):
    def lastMarkedNodes(self, edges):
        """
        """
        def increase(x):
            return (x[0]+1, x[1])

        def dfs1(u, p):
            for v in adj[u]:
                if v == p:
                    continue
                dfs1(v, u)
                curr = increase(dp[v][0])
                for i in range(len(dp[u])):
                    if curr > dp[u][i]:
                        curr, dp[u][i] = dp[u][i], curr

        def dfs2(u, p, curr):
            for v in adj[u]:
                if v == p:
                    continue
                dfs2(v, u, increase(max(dp[u][dp[u][0][1] == dp[v][0][1]], curr)))
            result[u] = max(dp[u][0], curr)[1]
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = [[(0, u)]*2 for u in range(len(adj))]
        dfs1(0, -1)
        result = [-1]*len(adj)
        dfs2(0, -1, (0, -1))
        return result
