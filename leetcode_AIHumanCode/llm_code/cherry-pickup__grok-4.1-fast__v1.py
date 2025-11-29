class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        prev = [[-1] * n for _ in range(n)]
        prev[0][0] = grid[0][0]
        total = 2 * (n - 1)
        for t in range(1, total + 1):
            curr = [[-1] * n for _ in range(n)]
            lo = max(0, t - n + 1)
            hi = min(t, n - 1)
            for r1 in range(lo, hi + 1):
                c1 = t - r1
                if grid[r1][c1] == -1:
                    continue
                for r2 in range(lo, hi + 1):
                    c2 = t - r2
                    if grid[r2][c2] == -1:
                        continue
                    val = grid[r1][c1]
                    if r1 != r2:
                        val += grid[r2][c2]
                    mx = -1
                    for dr1 in (0, -1):
                        for dr2 in (0, -1):
                            pr1 = r1 + dr1
                            pr2 = r2 + dr2
                            if pr1 >= 0 and pr2 >= 0 and prev[pr1][pr2] != -1:
                                mx = max(mx, prev[pr1][pr2] + val)
                    curr[r1][r2] = mx
            prev = curr
        return max(prev[n - 1][n - 1], 0)
