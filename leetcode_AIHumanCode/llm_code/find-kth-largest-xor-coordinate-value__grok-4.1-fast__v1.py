class Solution(object):
    def kthLargestValue(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i > 0:
                    matrix[i][j] ^= matrix[i - 1][j]
                if j > 0:
                    matrix[i][j] ^= matrix[i][j - 1]
                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i - 1][j - 1]
        vals = [matrix[i][j] for i in range(m) for j in range(n)]
        vals.sort(reverse=True)
        return vals[k - 1]
