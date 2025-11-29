import heapq

class Solution(object):
    def maxSum(self, grid, limits, k):
        pool = []
        num_rows = len(grid)
        for idx in range(num_rows):
            max_take = min(k, limits[idx])
            top_row = heapq.nlargest(max_take, grid[idx])
            pool.extend(top_row)
        best_k = heapq.nlargest(k, pool)
        return sum(best_k)
