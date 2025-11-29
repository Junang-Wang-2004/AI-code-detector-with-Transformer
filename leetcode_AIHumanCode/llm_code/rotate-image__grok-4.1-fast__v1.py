class Solution:
    def rotate(self, matrix):
        size = len(matrix)
        for x in range(size):
            for y in range(x + 1, size):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        for row_idx in range(size):
            matrix[row_idx].reverse()
        return matrix
