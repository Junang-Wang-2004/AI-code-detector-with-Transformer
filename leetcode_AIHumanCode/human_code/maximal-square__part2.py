# Time:  O(n^2)
# Space: O(n^2)
# DP.
class Solution2(object):
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in range(n)] for i in range(m)]
        max_size = 0

        for j in range(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in range(1, m):
            if matrix[i][0] == '1':
                size[i][0] = 1
            else:
                size[i][0] = 0
            for j in range(1, n):
                if matrix[i][j] == '1':
                    size[i][j] = min(size[i][j - 1],  \
                                     size[i - 1][j],  \
                                     size[i - 1][j - 1]) + 1
                    max_size = max(max_size, size[i][j])
                else:
                    size[i][j] = 0

        return max_size * max_size


