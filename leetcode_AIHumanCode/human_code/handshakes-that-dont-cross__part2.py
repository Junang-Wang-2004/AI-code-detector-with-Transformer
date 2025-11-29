# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    def numberOfWays(self, num_people):
        """
        """
        MOD = 10**9+7
        dp = [0]*(num_people//2+1)
        dp[0] = 1
        for k in range(1, num_people//2+1):
            for i in range(k):
                dp[k] = (dp[k] + dp[i]*dp[k-1-i]) % MOD
        return dp[num_people//2]
