import heapq
import bisect

class Solution:
    def maxPoints(self, grid, queries):
        if not grid or not grid[0]:
            return [0] * len(queries)
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))
        visited = set([(0, 0)])
        current_max = 0
        bottlenecks = []
        while pq:
            cell_val, row, col = heapq.heappop(pq)
            current_max = max(current_max, cell_val)
            bottlenecks.append(current_max)
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))
        bottlenecks.sort()
        return [bisect.bisect_left(bottlenecks, q) for q in queries]
