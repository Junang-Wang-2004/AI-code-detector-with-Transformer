# Time:  O(n * b)
# Space: O(n + b)
import collections


# dfs, tree dp
class Solution2(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        """
        def dfs(u):
            dp = [collections.defaultdict(int) for _ in range(2)]
            dp[0][0] = dp[1][0] = 0
            for v in adj[u]:
                new_dp = dfs(v)
                for i in range(2):
                    for j1, v1 in list(dp[i].items()):
                        for j2, v2 in new_dp[i].items():
                            if j1+j2 <= budget:
                                dp[i][j1+j2] = max(dp[i][j1+j2], v1+v2)
            result = [collections.defaultdict(int) for _ in range(2)]
            for i in range(2):
                for j, v in dp[0].items():
                    result[i][j] = max(result[i][j], v)
                cost = present[u]>>i
                if cost > budget:
                    continue
                profit = future[u]-cost
                for j, v in dp[1].items():
                    if j+cost <= budget:
                        result[i][j+cost] = max(result[i][j+cost], v+profit)
            return result  # result[i][j]: max profit for budget j with i discount

        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u-1].append(v-1)
        return max(dfs(0)[0].values())
