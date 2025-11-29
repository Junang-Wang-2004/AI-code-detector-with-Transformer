# Time:  O(m * n)
# Space: O(m * n)
# dfs + memoization solution
class Solution2(object):
    def longestIncreasingPath(self, matrix):
        """
        """
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def longestpath(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]
            max_depth = 0
            for di, dj in directions:
                x, y = i+di, j+dj
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
                   matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, longestpath(matrix, x, y, max_lengths))
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]

        if not matrix:
            return 0
        result = 0
        max_lengths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, longestpath(matrix, i, j, max_lengths))
        return result
