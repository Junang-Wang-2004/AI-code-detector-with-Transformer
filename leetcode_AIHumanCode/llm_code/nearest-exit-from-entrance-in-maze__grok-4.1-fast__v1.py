from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        sr, sc = entrance
        vis = set([(sr, sc)])
        q = deque([(sr, sc, 0)])
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            r, c, d = q.popleft()
            if d > 0 and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return d
            for dr, dc in deltas:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in vis:
                    vis.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1
