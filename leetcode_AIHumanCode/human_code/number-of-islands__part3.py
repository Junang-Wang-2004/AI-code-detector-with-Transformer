# Time:  O(m * n)
# Space: O(m * n)
import collections


# bfs solution
class Solution3(object):
    def numIslands(self, grid):
        """
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(grid, i, j):
            if grid[i][j] == '0':
                return False
            grid[i][j] ='0'
            q = collections.deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(grid) and
                            0 <= nc < len(grid[0]) and
                            grid[nr][nc] == '1'):
                        continue
                    grid[nr][nc] = '0'
                    q.append((nr, nc))
            return True

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if bfs(grid, i, j):
                    count += 1
        return count
