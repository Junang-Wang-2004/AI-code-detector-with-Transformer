# Time:  O(n)
# Space: O(n)
# dfs, tree dp
class Solution2(object):
    def maxOutput(self, n, edges, price):
        """
        """
        def dfs(u, p):
            dp = [price[u], 0]  # [max_path_sum, max_path_sum_without_last_node]
            for v in adj[u]:
                if v == p:
                    continue
                new_dp = dfs(v, u)
                result[0] = max(result[0], dp[0]+new_dp[1], dp[1]+new_dp[0])
                dp[0] = max(dp[0], new_dp[0]+price[u])
                dp[1] = max(dp[1], new_dp[1]+price[u])
            return dp
        
        result = [0]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dfs(0, -1)
        return result[0]


