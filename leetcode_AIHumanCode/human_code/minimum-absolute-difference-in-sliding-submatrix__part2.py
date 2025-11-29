# Time:  O(m * n * k^2 * logk)
# Space: O(k^2)
# brute force, sort
class Solution2(object):
    def minAbsDiff(self, grid, k):
        """
        """
        result = [[-1]*(len(grid[0])-(k-1)) for _ in range(len(grid)-(k-1))]
        for i in range(len(grid)-(k-1)):
            for j in range(len(grid[0])-(k-1)):
                vals = sorted({grid[i+di][j+dj] for di in range(k) for dj in range(k)})
                result[i][j] = min(vals[x+1]-vals[x] for x in range(len(vals)-1)) if len(vals) != 1 else 0
        return result
