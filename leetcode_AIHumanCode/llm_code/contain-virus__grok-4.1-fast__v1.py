from collections import deque

class Solution:
    def containVirus(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = 0
        while True:
            vis = set()
            groups = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in vis:
                        component = []
                        borders = set()
                        walls = 0
                        q = deque([(i, j)])
                        vis.add((i, j))
                        while q:
                            x, y = q.popleft()
                            component.append((x, y))
                            for dx, dy in deltas:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if grid[nx][ny] == 1 and (nx, ny) not in vis:
                                        vis.add((nx, ny))
                                        q.append((nx, ny))
                                    elif grid[nx][ny] == 0:
                                        borders.add((nx, ny))
                                        walls += 1
                        groups.append((len(borders), walls, component))
            if not groups:
                break
            groups.sort(key=lambda g: -g[0])
            _, cost, quarantine = groups[0]
            ans += cost
            for x, y in quarantine:
                grid[x][y] = -1
            for _, _, spread in groups[1:]:
                for x, y in spread:
                    for dx, dy in deltas:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                            grid[nx][ny] = 1
        return ans
