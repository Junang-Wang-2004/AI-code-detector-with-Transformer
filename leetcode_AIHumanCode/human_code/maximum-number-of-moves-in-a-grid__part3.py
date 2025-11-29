# Time:  O(m * n)
# Space: O(m)
# bfs
class Solution3(object):
    def maxMoves(self, grid):
        """
        """
        q = set(range(len(grid)))
        for c in range(len(grid[0])-1):
            new_q = set()
            for r in q:
                if grid[r][c] < grid[r][c+1]:
                    new_q.add(r)
                if r-1 >= 0 and grid[r][c] < grid[r-1][c+1]:
                    new_q.add(r-1)
                if r+1 < len(grid) and grid[r][c] < grid[r+1][c+1]:
                    new_q.add(r+1)
            q = new_q
            if not q:
                break
        else:
            c = len(grid[0])-1
        return c
