from collections import deque

class Solution:
    def minimumVisitedCells(self, grid):
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        INF = 10**9 + 7
        distance = [[INF] * cols for _ in range(rows)]
        distance[0][0] = 1
        queue = deque([(0, 0)])
        while queue:
            r, c = queue.popleft()
            curr_dist = distance[r][c]
            jump_len = grid[r][c]
            down_end = min(r + jump_len + 1, rows)
            right_end = min(c + jump_len + 1, cols)
            for nr in range(r + 1, down_end):
                if distance[nr][c] > curr_dist + 1:
                    distance[nr][c] = curr_dist + 1
                    queue.append((nr, c))
            for nc in range(c + 1, right_end):
                if distance[r][nc] > curr_dist + 1:
                    distance[r][nc] = curr_dist + 1
                    queue.append((r, nc))
        return distance[rows - 1][cols - 1] if distance[rows - 1][cols - 1] < INF else -1
