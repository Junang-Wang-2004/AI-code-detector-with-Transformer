class Solution:
    def minCost(self, grid, k):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        max_val = max(max(row) for row in grid)
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        suf = [float('inf')] * (max_val + 2)
        for _ in range(k + 1):
            for i in range(rows):
                for j in range(cols):
                    dist[i][j] = min(dist[i][j], suf[grid[i][j]])
            for i in range(rows):
                for j in range(cols):
                    cost = grid[i][j]
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + cost)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + cost)
            suf = [float('inf')] * (max_val + 2)
            for i in range(rows):
                for j in range(cols):
                    suf[grid[i][j]] = min(suf[grid[i][j]], dist[i][j])
            for v in range(max_val, -1, -1):
                suf[v] = min(suf[v], suf[v + 1])
        return dist[rows - 1][cols - 1]
