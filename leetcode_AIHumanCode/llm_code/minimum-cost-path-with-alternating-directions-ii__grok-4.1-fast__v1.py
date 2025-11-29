class Solution:
    def minCost(self, m, n, waitCost):
        waitCost[0][0] = waitCost[m - 1][n - 1] = 0
        waitCost[0][0] += 1
        for j in range(1, n):
            waitCost[0][j] += waitCost[0][j - 1] + 1 * (j + 1)
        for i in range(1, m):
            waitCost[i][0] += waitCost[i - 1][0] + (i + 1) * 1
        for i in range(1, m):
            for j in range(1, n):
                best = min(waitCost[i - 1][j], waitCost[i][j - 1])
                waitCost[i][j] += best + (i + 1) * (j + 1)
        return waitCost[m - 1][n - 1]
