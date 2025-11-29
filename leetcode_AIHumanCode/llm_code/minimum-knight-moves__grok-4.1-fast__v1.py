from collections import deque

class Solution:
    def minKnightMoves(self, x, y):
        tx = abs(x)
        ty = abs(y)
        moves = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
        q = deque([(0, 0, 0)])
        vis = {(0, 0)}
        while q:
            cx, cy, steps = q.popleft()
            if cx == tx and cy == ty:
                return steps
            for dx, dy in moves:
                nx = cx + dx
                ny = cy + dy
                if nx >= 0 and ny >= 0 and (nx, ny) not in vis:
                    if nx == tx and ny == ty:
                        return steps + 1
                    vis.add((nx, ny))
                    q.append((nx, ny, steps + 1))
