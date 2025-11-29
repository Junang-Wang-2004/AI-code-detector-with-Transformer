from functools import reduce
# Time:  O(n * k)
# Space: O(k)

# knapsack dp, combinatorics, sliding window, two pointers
class Solution(object):
    def kInversePairs(self, n, k):
        """
        """
        MOD = 10**9+7
        dp = [1]
        for i in range(n):
            new_dp = [0]*min(len(dp)+((i+1)-1), k+1)
            for j in range(len(new_dp)):
                new_dp[j] = dp[j] if j < len(dp) else 0
                if j-1 >= 0:
                    new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                if j-(i+1) >= 0:
                    new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[k] if k < len(dp) else 0


