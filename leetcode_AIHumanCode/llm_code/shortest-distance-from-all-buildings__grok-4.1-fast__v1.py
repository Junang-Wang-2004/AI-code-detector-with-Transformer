from collections import deque

class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1
        
        h, w = len(grid), len(grid[0])
        num_bld = sum(1 for i in range(h) for j in range(w) if grid[i][j] == 1)
        total_d = [[0] * w for _ in range(h)]
        reaches = [[0] * w for _ in range(h)]
        
        def explore(sr, sc):
            vis = [[False] * w for _ in range(h)]
            q = deque([(sr, sc, 0)])
            vis[sr][sc] = True
            while q:
                r, c, d = q.popleft()
                if grid[r][c] == 0:
                    total_d[r][c] += d
                    reaches[r][c] += 1
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 0 and not vis[nr][nc]:
                        vis[nr][nc] = True
                        q.append((nr, nc, d + 1))
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    explore(i, j)
        
        ans = float('inf')
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and reaches[i][j] == num_bld:
                    ans = min(ans, total_d[i][j])
        
        return ans if ans != float('inf') else -1
