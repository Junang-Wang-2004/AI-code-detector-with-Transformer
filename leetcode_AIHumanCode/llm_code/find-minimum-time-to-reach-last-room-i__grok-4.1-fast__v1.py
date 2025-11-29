import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        rows, cols = len(moveTime), len(moveTime[0])
        INF = float('inf')
        costs = [[INF] * cols for _ in range(rows)]
        costs[0][0] = 0
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while pq:
            dist_now, row, col = heapq.heappop(pq)
            if dist_now > costs[row][col]:
                continue
            if row == rows - 1 and col == cols - 1:
                return dist_now
            for dr, dc in deltas:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    candidate = max(moveTime[nr][nc], dist_now) + 1
                    if candidate < costs[nr][nc]:
                        costs[nr][nc] = candidate
                        heapq.heappush(pq, (candidate, nr, nc))
        return costs[rows - 1][cols - 1]
