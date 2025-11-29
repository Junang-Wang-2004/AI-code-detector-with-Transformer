class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        m = len(grid)
        if m == 0:
            return []
        n = len(grid[0])
        record = {}
        for r in range(m):
            cm = 0
            for c in range(n):
                if grid[r][c]:
                    cm |= 1 << c
            if cm == 0:
                return [r]
            for pm, pr in record.items():
                if pm & cm == 0:
                    return [pr, r]
            record[cm] = r
        return []
