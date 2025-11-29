class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        def compute_length(x, y):
            pos = (x, y)
            if pos in memo:
                return memo[pos]
            curr_max = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                    curr_max = max(curr_max, 1 + compute_length(nx, ny))
            memo[pos] = curr_max
            return curr_max
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, compute_length(i, j))
        return ans
