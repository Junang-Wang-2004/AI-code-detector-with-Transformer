import heapq

class Solution:
    def minimumObstacles(self, grid):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        end_r, end_c = rows - 1, cols - 1
        costs = [[float('inf')] * cols for _ in range(rows)]
        costs[0][0] = 0
        pq = [(0, 0, 0)]
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while pq:
            dist, r, c = heapq.heappop(pq)
            if dist > costs[r][c]:
                continue
            if r == end_r and c == end_c:
                return dist
            for dr, dc in deltas:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    add_cost = grid[nr][nc]
                    new_dist = dist + add_cost
                    if new_dist < costs[nr][nc]:
                        costs[nr][nc] = new_dist
                        heapq.heappush(pq, (new_dist, nr, nc))
        return -1
