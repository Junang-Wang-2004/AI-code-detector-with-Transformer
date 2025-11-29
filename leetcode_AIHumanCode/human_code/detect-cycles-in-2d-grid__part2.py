# Time:  O(m * n)
# Space: O(m * n)
class Solution2(object):
    def containsCycle(self, grid):
        """
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                val = grid[i][j]
                q = [(i, j)]
                while q:
                    new_q = []
                    for r, c in q:
                        if not grid[r][c]:
                            return True
                        grid[r][c] = 0
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if not (0 <= nr < len(grid) and
                                    0 <= nc < len(grid[0]) and
                                    grid[nr][nc] == val):
                                continue
                            new_q.append((nr, nc))
                    q = new_q
        return False
