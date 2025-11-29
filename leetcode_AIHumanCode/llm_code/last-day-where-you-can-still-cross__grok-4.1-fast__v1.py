from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        def possible(days):
            obstacle = set((cells[k][0] - 1, cells[k][1] - 1) for k in range(days))
            seen = [[False] * col for _ in range(row)]
            queue = deque()
            for j in range(col):
                cell = (0, j)
                if cell not in obstacle:
                    queue.append(cell)
                    seen[0][j] = True
            deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while queue:
                x, y = queue.popleft()
                if x == row - 1:
                    return True
                for dx, dy in deltas:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and not seen[nx][ny] and (nx, ny) not in obstacle:
                        seen[nx][ny] = True
                        queue.append((nx, ny))
            return False

        l, r = 0, len(cells)
        while l < r:
            m = (l + r + 1) // 2
            if possible(m):
                l = m
            else:
                r = m - 1
        return l
