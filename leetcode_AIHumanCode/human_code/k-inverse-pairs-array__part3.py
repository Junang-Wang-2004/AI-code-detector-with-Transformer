from functools import reduce
# Time:  O(n * k)
# Space: O(k)
# knapsack dp, combinatorics, sliding window, two pointers
class Solution3(object):
    def kInversePairs(self, n, k):
        """
        """
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for i in range(n):
            new_dp = [0]*len(dp)
            curr = 0
            for j in range(len(dp)):
                curr = (curr+dp[j])%MOD
                if j-(i+1) >= 0:
                    curr = (curr-dp[j-(i+1)])%MOD
                new_dp[j] = curr
            dp = new_dp
        return dp[-1]


