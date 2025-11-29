# Time:  O(m * n)
# Space: O(m * n)
# dp solution
class Solution2(object):
    def updateMatrix(self, matrix):
        """
        """
        dp = [[float("inf")]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
        for i in reversed(range(len(matrix))):
            for j in reversed(range(len(matrix[i]))):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i < len(matrix)-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                    if j < len(matrix[i])-1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
        return dp


