class Solution:
    def minAbsDiff(self, grid, k):
        if not grid or k == 0:
            return []
        m, n = len(grid), len(grid[0])
        res = []
        for row in range(m - k + 1):
            subrow = []
            for col in range(n - k + 1):
                window = []
                for x in range(row, row + k):
                    for y in range(col, col + k):
                        window.append(grid[x][y])
                window.sort()
                diff = float('inf')
                for idx in range(1, len(window)):
                    if window[idx] != window[idx - 1]:
                        diff = min(diff, window[idx] - window[idx - 1])
                subrow.append(0 if diff == float('inf') else diff)
            res.append(subrow)
        return res
