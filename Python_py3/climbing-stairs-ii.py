# Time:  O(n)
# Space: O(1)

# dp
class Solution(object):
    def climbStairs(self, n, costs):
        """
        """
        a, b, c = float("inf"), float("inf"), 0
        for i in range(n):
            a, b, c = b, c, costs[i]+min(a+3**2, b+2**2, c+1**2)
        return c


# Time:  O(n)
# Space: O(n)
# dp
class Solution2(object):
    def climbStairs(self, n, costs):
        """
        """
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(n):
            dp[i+1] = costs[i]+min(dp[i-j]+(j+1)**2 for j in range(min(3, i+1)))
        return dp[n]
