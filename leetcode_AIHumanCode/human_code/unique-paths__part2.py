# Time:  O(m * n)
# Space: O(min(m, n))
class Solution2(object):
    def uniquePaths(self, m, n):
        """
        """
        if m < n:
            m, n  = n, m

        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]
