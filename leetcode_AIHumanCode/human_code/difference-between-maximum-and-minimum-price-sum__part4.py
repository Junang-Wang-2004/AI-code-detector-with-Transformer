# Time:  O(n)
# Space: O(n)
# dfs, tree dp
class Solution4(object):
    def maxOutput(self, n, edges, price):
        """
        """
        def dfs(u, p):
            dp[u] = price[u]
            for v in adj[u]:
                if v == p:
                    continue
                dp[u] = max(dp[u], dfs(v, u)+price[u])
            return dp[u]
        
        def dfs2(u, p, curr):
            result[0] = max(result[0], curr, dp[u]-price[u])
            top2 = [[curr, p], [0, -1]]
            for v in adj[u]:
                if v == p:
                    continue
                curr = [dp[v], v]
                for i in range(len(top2)):
                    if curr > top2[i]:
                        top2[i], curr = curr, top2[i]
            for v in adj[u]:
                if v == p:
                    continue
                dfs2(v, u, (top2[0][0] if top2[0][1] != v else top2[1][0])+price[u])
    
        result = [0]
        dp = [0]*n  # max_sum
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dfs(0, -1)
        dfs2(0, -1, 0)
        return result[0]
