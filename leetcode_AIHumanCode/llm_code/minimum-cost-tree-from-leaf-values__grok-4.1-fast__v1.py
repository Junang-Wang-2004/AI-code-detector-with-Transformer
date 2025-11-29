class Solution:
    def mctFromLeafValues(self, arr):
        n = len(arr)
        maxv = [[0] * n for _ in range(n)]
        for i in range(n):
            maxv[i][i] = arr[i]
        for leng in range(2, n + 1):
            for i in range(n - leng + 1):
                j = i + leng - 1
                maxv[i][j] = max(maxv[i][j - 1], arr[j])
        dp = [[0] * n for _ in range(n)]
        for leng in range(2, n + 1):
            for i in range(n - leng + 1):
                j = i + leng - 1
                best = float('inf')
                for k in range(i, j):
                    temp = dp[i][k] + dp[k + 1][j] + maxv[i][k] * maxv[k + 1][j]
                    if temp < best:
                        best = temp
                dp[i][j] = best
        return dp[0][n - 1]
