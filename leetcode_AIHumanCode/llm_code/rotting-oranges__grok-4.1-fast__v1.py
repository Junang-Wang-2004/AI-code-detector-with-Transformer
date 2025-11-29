import collections

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        fresh_cnt = 0
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1
        minutes = 0
        while q:
            level_len = len(q)
            for _ in range(level_len):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_cnt -= 1
                        q.append((nx, ny))
            if q:
                minutes += 1
        return minutes if fresh_cnt == 0 else -1
