class Solution(object):
    def sortMatrix(self, grid):
        if not grid or not grid[0]:
            return grid
        rows = len(grid)
        cols = len(grid[0])
        min_d = 1 - cols
        max_d = rows - 1
        diags = {d: [] for d in range(min_d, max_d + 1)}
        for r in range(rows):
            for c in range(cols):
                diags[r - c].append(grid[r][c])
        for d in range(min_d, max_d + 1):
            if d < 0:
                diags[d].sort(reverse=True)
            else:
                diags[d].sort()
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = diags[r - c].pop()
        return grid
