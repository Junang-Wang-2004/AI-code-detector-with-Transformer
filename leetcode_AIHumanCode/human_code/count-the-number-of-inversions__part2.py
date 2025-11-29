from functools import reduce
# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)
# knapsack dp, combinatorics, sliding window, two pointers
class Solution2(object):
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
            if lookup[i] != -1:  # optimized
                new_dp[lookup[i]] = reduce(lambda total, i: (total+dp[i])%MOD, range(max(lookup[i]-i, 0), lookup[i]+1), 0)
            else:
                for j in range(len(dp)):
                    new_dp[j] = dp[j]
                    if j-1 >= 0:
                        new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                    if j-(i+1) >= 0:
                        new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[-1]


