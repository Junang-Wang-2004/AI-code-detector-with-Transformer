from collections import deque

class Solution:
    def highestPeak(self, isWater):
        if not isWater or not isWater[0]:
            return []
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]:
                    height[i][j] = 0
                    q.append((i, j))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                        height[nr][nc] = height[r][c] + 1
                        q.append((nr, nc))
        return height
