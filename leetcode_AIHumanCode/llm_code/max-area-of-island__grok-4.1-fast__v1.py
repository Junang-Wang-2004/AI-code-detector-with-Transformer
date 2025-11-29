class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maximum = 0
        
        def flood(row, col):
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                grid[row][col] != 1):
                return 0
            grid[row][col] = 0
            return (1 + flood(row - 1, col) + 
                       flood(row + 1, col) + 
                       flood(row, col - 1) + 
                       flood(row, col + 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maximum = max(maximum, flood(r, c))
        return maximum
