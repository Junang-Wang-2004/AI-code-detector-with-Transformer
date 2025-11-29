from collections import deque

class Solution:
    def maximumMinutes(self, grid):
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 10**9
        fire_t = [[INF] * cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fire_t[i][j] = 0
                    q.append((i, j, 0))
        while q:
            r, c, t = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 2 and fire_t[nr][nc] == INF:
                    fire_t[nr][nc] = t + 1
                    q.append((nr, nc, t + 1))
        person_t = [[INF] * cols for _ in range(rows)]
        q = deque([(0, 0, 0)])
        person_t[0][0] = 0
        er, ec = rows - 1, cols - 1
        while q:
            r, c, t = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 2:
                    arr = t + 1
                    safe = (nr == er and nc == ec and arr <= fire_t[nr][nc]) or (arr < fire_t[nr][nc])
                    if safe and arr < person_t[nr][nc]:
                        person_t[nr][nc] = arr
                        q.append((nr, nc, arr))
        p_exit = person_t[er][ec]
        if p_exit == INF:
            return -1
        f_exit = fire_t[er][ec]
        if f_exit == INF:
            return INF
        delta = f_exit - p_exit
        dr1, dc1 = er, ec - 1
        dr2, dc2 = er - 1, ec
        delta1 = fire_t[dr1][dc1] - person_t[dr1][dc1]
        delta2 = fire_t[dr2][dc2] - person_t[dr2][dc2]
        return delta if delta + 2 == delta1 or delta + 2 == delta2 else delta - 1
