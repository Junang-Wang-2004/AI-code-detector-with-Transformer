from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        MAXD = rows + cols
        mindist = [[MAXD] * cols for _ in range(rows)]
        que = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    mindist[i][j] = 0
                    que.append((i, j))
        while que:
            x, y = que.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and mindist[nx][ny] > mindist[x][y] + 1:
                    mindist[nx][ny] = mindist[x][y] + 1
                    que.append((nx, ny))

        def feasible(val):
            if mindist[0][0] < val or mindist[rows - 1][cols - 1] < val:
                return False
            vis = [[False] * cols for _ in range(rows)]
            que2 = deque([(0, 0)])
            vis[0][0] = True
            while que2:
                cx, cy = que2.popleft()
                if cx == rows - 1 and cy == cols - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not vis[nx][ny] and mindist[nx][ny] >= val:
                        vis[nx][ny] = True
                        que2.append((nx, ny))
            return False

        l, r = 0, max(map(max, mindist)) + 1
        while l < r:
            m = (l + r + 1) // 2
            if feasible(m):
                l = m
            else:
                r = m - 1
        return l
