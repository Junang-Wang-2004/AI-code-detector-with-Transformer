class Solution:
    def projectionArea(self, grid):
        top = sum(1 for row in grid for h in row if h)
        rows = sum(max(row) for row in grid)
        cols = sum(max(col) for col in zip(*grid))
        return top + rows + cols
