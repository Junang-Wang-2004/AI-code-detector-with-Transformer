class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        largest = 0
        
        for c in range(cols):
            dp[0][c] = 1 if matrix[0][c] == '1' else 0
            largest = max(largest, dp[0][c])
        
        for r in range(1, rows):
            dp[r][0] = 1 if matrix[r][0] == '1' else 0
            largest = max(largest, dp[r][0])
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    largest = max(largest, dp[r][c])
                else:
                    dp[r][c] = 0
        
        return largest * largest
