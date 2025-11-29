class Solution:
    def largestIsland(self, grid):
        if not grid or not grid[0]:
            return 1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        sz = {}

        def comp_size(x, y, label):
            stk = [(x, y)]
            total = 0
            grid[x][y] = label
            total += 1
            while stk:
                cx, cy = stk.pop()
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = label
                        total += 1
                        stk.append((nx, ny))
            return total

        lbl = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sz[lbl] = comp_size(i, j, lbl)
                    lbl += 1

        ans = max(sz.values()) if sz else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    adj_ids = set()
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] >= 2:
                            adj_ids.add(grid[ni][nj])
                    cand = 1 + sum(sz.get(k, 0) for k in adj_ids)
                    ans = max(ans, cand)
        return ans
