class Solution:
    def numDistinctIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def traverse(x, y, ox, oy):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != 1:
                return False
            grid[x][y] = 0
            path.append(str(x - ox) + str(y - oy))
            for dx, dy in deltas:
                traverse(x + dx, y + dy, ox, oy)
            return True
        patterns = set()
        for r in range(rows):
            for c in range(cols):
                current_path = []
                if traverse(r, c, r, c):
                    patterns.add(''.join(current_path))
        return len(patterns)
