class Solution:
    def maxMoves(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        reachable = set(range(m))
        col = 0
        while col < n - 1 and reachable:
            next_reachable = set()
            for r in reachable:
                current = grid[r][col]
                for delta in (-1, 0, 1):
                    nr = r + delta
                    if 0 <= nr < m and current < grid[nr][col + 1]:
                        next_reachable.add(nr)
            reachable = next_reachable
            col += 1
        return col
