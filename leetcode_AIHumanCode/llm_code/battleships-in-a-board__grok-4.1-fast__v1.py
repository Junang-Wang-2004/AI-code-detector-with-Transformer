class Solution:
    def countBattleships(self, grid):
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        ships = 0
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell == 'X':
                    above = r == 0 or grid[r-1][c] != 'X'
                    left = c == 0 or grid[r][c-1] != 'X'
                    if above and left:
                        ships += 1
        return ships
