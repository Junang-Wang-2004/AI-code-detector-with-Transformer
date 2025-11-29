class Solution:
    def numSubmat(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ht = [0] * n
        total = 0

        def calc_mins(hgt):
            sz = len(hgt)
            dpp = [0] * sz
            stck = []
            for idx in range(sz):
                while stck and hgt[stck[-1]] >= hgt[idx]:
                    stck.pop()
                prvv = stck[-1] if stck else -1
                dpp[idx] = (dpp[prvv] if prvv >= 0 else 0) + hgt[idx] * (idx - prvv)
                stck.append(idx)
            return sum(dpp)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ht[c] += 1
                else:
                    ht[c] = 0
            total += calc_mins(ht)
        return total
