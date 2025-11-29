# Time:  O(m * n * k) = O(m * n)
# Space: O(n * k) = O(n)
# dp
class Solution2(object):
    def maximumAmount(self, coins):
        """
        """
        K = 2
        dp = [[float("-inf")]*(K+1) for _ in range(len(coins[0]))] 
        for i in range(len(coins)):
            new_dp = [[float("-inf")]*(K+1) for _ in range(len(coins[0]))]
            for j in range(len(coins[0])):
                for k in range((K+1)):
                    if i == 0 and j == 0:
                        new_dp[j][k] = max(coins[i][j], 0) if k-1 >= 0 else coins[i][j]
                        continue
                    if i-1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], dp[j][k]+coins[i][j])
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k-1])
                    if j-1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k]+coins[i][j])
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k-1])
            dp = new_dp
        return dp[-1][-1]
