class Solution:
    def getRow(self, rowIndex):
        pascal_row = [1] * (rowIndex + 1)
        for level in range(2, rowIndex + 1):
            for idx in range(level - 1, 0, -1):
                pascal_row[idx] += pascal_row[idx - 1]
        return pascal_row
