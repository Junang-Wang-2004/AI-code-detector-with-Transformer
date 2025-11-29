class Solution:
    def allCellsDistOrder(self, rows, cols, sr, sc):
        grid = [[i, j] for i in range(rows) for j in range(cols)]
        grid.sort(key=lambda p: (abs(p[0] - sr) + abs(p[1] - sc), p[0], p[1]))
        return grid
