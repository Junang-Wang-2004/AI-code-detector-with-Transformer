from functools import reduce
# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)
# knapsack dp, combinatorics, sliding window, two pointers
class Solution3(object):
    def numberOfPermutations(self, n, requirements):
        """
        """
        MOD = 10**9+7
        lookup = [-1]*n
        for i, c in requirements:
            lookup[i] = c
        dp = [0]*(lookup[-1]+1)
        dp[0] = 1
        for i in range(n):
            new_dp = [0]*len(dp)
            curr = 0
            for j in range(len(dp)):
                curr = (curr+dp[j])%MOD
                if j-(i+1) >= 0:
                    curr = (curr-dp[j-(i+1)])%MOD
                new_dp[j] = curr if lookup[i] == -1 or lookup[i] == j else 0
            dp = new_dp
        return dp[-1]


