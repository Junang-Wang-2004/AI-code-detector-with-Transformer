class Solution:
    def minimumOperations(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        costs = [[0] * 10 for _ in range(m)]
        for col in range(m):
            freq = [0] * 10
            for row in range(n):
                freq[grid[row][col]] += 1
            for val in range(10):
                costs[col][val] = n - freq[val]
        prev_costs = [0] * 10
        for col in range(m):
            curr_costs = [float('inf')] * 10
            for p in range(10):
                for c in range(10):
                    if p != c:
                        curr_costs[c] = min(curr_costs[c], prev_costs[p] + costs[col][c])
            prev_costs = curr_costs
        return min(prev_costs)
