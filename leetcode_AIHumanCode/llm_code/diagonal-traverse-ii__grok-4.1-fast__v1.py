class Solution:
    def findDiagonalOrder(self, mat):
        items = []
        for row_idx, line in enumerate(mat):
            for col_idx, value in enumerate(line):
                items.append((row_idx + col_idx, -row_idx, value))
        items.sort()
        return [v for _, _, v in items]
