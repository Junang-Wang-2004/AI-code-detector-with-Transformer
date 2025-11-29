class Solution:
    def rotateGrid(self, grid, k):
        rows, cols = len(grid), len(grid[0])
        for layer in range(rows // 2):
            up = layer
            down = rows - layer - 1
            lft = layer
            rgt = cols - layer - 1
            cycle_size = 2 * ((down - up) + (rgt - lft))
            shift = k % cycle_size
            if shift == 0:
                continue
            border = []
            for rw in range(up, down):
                border.append(grid[rw][lft])
            for cl in range(lft, rgt):
                border.append(grid[down][cl])
            for rw in range(down, up, -1):
                border.append(grid[rw][rgt])
            for cl in range(rgt, lft, -1):
                border.append(grid[up][cl])
            border = border[-shift:] + border[:-shift]
            pos = 0
            for rw in range(up, down):
                grid[rw][lft] = border[pos]
                pos += 1
            for cl in range(lft, rgt):
                grid[down][cl] = border[pos]
                pos += 1
            for rw in range(down, up, -1):
                grid[rw][rgt] = border[pos]
                pos += 1
            for cl in range(rgt, lft, -1):
                grid[up][cl] = border[pos]
                pos += 1
        return grid
