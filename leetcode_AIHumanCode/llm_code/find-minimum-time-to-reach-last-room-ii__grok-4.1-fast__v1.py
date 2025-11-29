class Solution:
    def minTimeToReach(self, grid):
        rows, cols = len(grid), len(grid[0])
        INF = float('inf')
        costs = [[INF] * cols for _ in range(rows)]
        costs[0][0] = 0
        import heapq
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        end_r, end_c = rows - 1, cols - 1
        while pq:
            elapsed, x, y = heapq.heappop(pq)
            if elapsed > costs[x][y]:
                continue
            if x == end_r and y == end_c:
                return elapsed
            incr = 1 + ((x + y) % 2)
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_elapsed = max(grid[nx][ny], elapsed) + incr
                    if new_elapsed < costs[nx][ny]:
                        costs[nx][ny] = new_elapsed
                        heapq.heappush(pq, (new_elapsed, nx, ny))
        return costs[end_r][end_c]
