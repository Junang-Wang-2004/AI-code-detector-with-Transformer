import heapq

class Solution:
    def maxSpending(self, grid):
        rows, cols = len(grid), len(grid[0])
        pq = []
        for r in range(rows):
            heapq.heappush(pq, (-grid[r][0], r, 0))
        ans = 0
        turn = rows * cols
        while pq:
            _, ridx, cidx = heapq.heappop(pq)
            val = -_
            ans += val * turn
            turn -= 1
            if cidx + 1 < cols:
                nxt = grid[ridx][cidx + 1]
                heapq.heappush(pq, (-nxt, ridx, cidx + 1))
        return ans
