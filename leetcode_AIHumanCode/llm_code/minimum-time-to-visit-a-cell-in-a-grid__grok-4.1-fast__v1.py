import heapq

class Solution:
    def minimumTime(self, grid):
        rows, cols = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        costs = [[float('inf')] * cols for _ in range(rows)]
        costs[0][0] = 0
        prio_queue = [(0, 0, 0)]
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while prio_queue:
            time_now, x, y = heapq.heappop(prio_queue)
            if time_now > costs[x][y]:
                continue
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    add = 1 if grid[nx][ny] % 2 == time_now % 2 else 0
                    next_time = max(grid[nx][ny] + add, time_now + 1)
                    if next_time < costs[nx][ny]:
                        costs[nx][ny] = next_time
                        heapq.heappush(prio_queue, (next_time, nx, ny))
        return costs[rows - 1][cols - 1]
