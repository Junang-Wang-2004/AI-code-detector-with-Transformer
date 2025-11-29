class Solution:
    def findDiagonalOrder(self, grid):
        if not grid or not grid[0]:
            return []
        r, c = len(grid), len(grid[0])
        output = []
        for k in range(r + c - 1):
            diag = [grid[i][k - i] for i in range(max(0, k - c + 1), min(k, r - 1) + 1)]
            if k % 2 == 0:
                diag.reverse()
            output.extend(diag)
        return output
