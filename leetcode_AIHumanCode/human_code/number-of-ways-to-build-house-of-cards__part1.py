# Time:  O(n^2)
# Space: O(n)

# dp
class Solution(object):
    def houseOfCards(self, n):
        """
        """
        dp = [0]*(n+1)  # dp[i]: number of ways with i cards and at most t triangles in the first row
        dp[0] = 1
        for t in range(1, (n+1)//3+1):
            for i in reversed(range(3*t-1, n+1)):
                dp[i] += dp[i-(3*t-1)]
        return dp[n]


