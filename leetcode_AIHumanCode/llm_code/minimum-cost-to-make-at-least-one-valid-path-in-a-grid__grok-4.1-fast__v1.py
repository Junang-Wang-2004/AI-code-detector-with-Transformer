import collections

class Solution:
    def minCost(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        INF = float('inf')
        distance = [[INF] * cols for _ in range(rows)]
        distance[0][0] = 0
        queue = collections.deque([(0, 0)])
        moves = [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]
        while queue:
            cr, cc = queue.popleft()
            if cr == rows - 1 and cc == cols - 1:
                return distance[cr][cc]
            for dr, dc, move_id in moves:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    step_cost = 0 if move_id == grid[cr][cc] else 1
                    alt_dist = distance[cr][cc] + step_cost
                    if alt_dist < distance[nr][nc]:
                        distance[nr][nc] = alt_dist
                        if step_cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
        return -1
