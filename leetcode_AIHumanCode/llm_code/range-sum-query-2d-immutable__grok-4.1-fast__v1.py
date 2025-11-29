class NumMatrix:
    def __init__(self, matrix):
        h, w = len(matrix), len(matrix[0])
        self.prefix = [[0] * (w + 1) for _ in range(h + 1)]
        for x in range(h):
            for y in range(w):
                self.prefix[x + 1][y + 1] = matrix[x][y] + self.prefix[x][y + 1] + self.prefix[x + 1][y] - self.prefix[x][y]

    def sumRegion(self, row1, col1, row2, col2):
        return self.prefix[row2 + 1][col2 + 1] + self.prefix[row1][col1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1]
