import heapq

class Solution:
    def swimInWater(self, grid):
        rows = len(grid)
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        costs = [[float('inf')] * rows for _ in range(rows)]
        costs[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        while heap:
            elev, row, col = heapq.heappop(heap)
            if elev > costs[row][col]:
                continue
            if row == rows - 1 and col == rows - 1:
                return elev
            for dr, dc in offsets:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < rows:
                    new_elev = max(elev, grid[nr][nc])
                    if new_elev < costs[nr][nc]:
                        costs[nr][nc] = new_elev
                        heapq.heappush(heap, (new_elev, nr, nc))
