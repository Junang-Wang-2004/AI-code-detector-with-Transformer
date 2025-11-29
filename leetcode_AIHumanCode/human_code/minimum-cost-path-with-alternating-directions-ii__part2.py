# Time:  O(m * n)
# Space: O(n)
# dp
class Solution2(object):
    def minCost(self, m, n, waitCost):
        """
        """
        waitCost[0][0] = waitCost[m-1][n-1] = 0
        dp = [0]*n
        for i in range(m):
            for j in range(n):
                prev = 0 if (i, j) == (0, 0) else float("inf")
                if i-1 >= 0:
                    prev = min(prev, dp[j])
                if j-1 >= 0:
                    prev = min(prev, dp[j-1])
                dp[j] = prev+waitCost[i][j]+(i+1)*(j+1)
        return dp[n-1]
