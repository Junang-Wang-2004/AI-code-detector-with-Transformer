# Time:  O(m * n)
# Space: O(1)

# dp
class Solution(object):
    def minCost(self, m, n, waitCost):
        """
        """
        waitCost[0][0] = waitCost[m-1][n-1] = 0
        for i in range(m):
            for j in range(n):
                prev = 0 if (i, j) == (0, 0) else float("inf")
                if i-1 >= 0:
                    prev = min(prev, waitCost[i-1][j])
                if j-1 >= 0:
                    prev = min(prev, waitCost[i][j-1])
                waitCost[i][j] += prev+(i+1)*(j+1)
        return waitCost[m-1][n-1]


