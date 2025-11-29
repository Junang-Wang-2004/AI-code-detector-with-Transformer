class Solution(object):
    def maxTrailingZeros(self, grid):
        def count_factors(val):
            if val == 0:
                return 0, 0
            twos = 0
            while val % 2 == 0:
                twos += 1
                val //= 2
            fives = 0
            while val % 5 == 0:
                fives += 1
                val //= 5
            return twos, fives

        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        hleft = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            hleft[r][0] = count_factors(grid[r][0])
            for c in range(1, cols):
                cf = count_factors(grid[r][c])
                hleft[r][c] = (hleft[r][c-1][0] + cf[0], hleft[r][c-1][1] + cf[1])
        hright = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            hright[r][cols-1] = count_factors(grid[r][cols-1])
            for c in range(cols-2, -1, -1):
                cf = count_factors(grid[r][c])
                hright[r][c] = (hright[r][c+1][0] + cf[0], hright[r][c+1][1] + cf[1])
        vup = [[(0, 0) for _ in range(rows)] for _ in range(cols)]
        for c in range(cols):
            for r in range(1, rows):
                cf = count_factors(grid[r-1][c])
                vup[c][r] = (vup[c][r-1][0] + cf[0], vup[c][r-1][1] + cf[1])
        vdown = [[(0, 0) for _ in range(rows)] for _ in range(cols)]
        for c in range(cols):
            for r in range(rows-2, -1, -1):
                cf = count_factors(grid[r+1][c])
                vdown[c][r] = (vdown[c][r+1][0] + cf[0], vdown[c][r+1][1] + cf[1])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                t2, t5 = hleft[r][c][0] + vup[c][r][0], hleft[r][c][1] + vup[c][r][1]
                ans = max(ans, min(t2, t5))
                t2, t5 = hright[r][c][0] + vup[c][r][0], hright[r][c][1] + vup[c][r][1]
                ans = max(ans, min(t2, t5))
                t2, t5 = hleft[r][c][0] + vdown[c][r][0], hleft[r][c][1] + vdown[c][r][1]
                ans = max(ans, min(t2, t5))
                t2, t5 = hright[r][c][0] + vdown[c][r][0], hright[r][c][1] + vdown[c][r][1]
                ans = max(ans, min(t2, t5))
        return ans
