class Solution:
    def maxPathScore(self, grid, k):
        if not grid or not grid[0]:
            return 0
        h, w = len(grid), len(grid[0])
        dp = [[[-1 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
        dp[0][0][0] = 0
        for r in range(h):
            for c in range(w):
                if r == 0 and c == 0:
                    continue
                incr = 1 if grid[r][c] != 0 else 0
                if c > 0:
                    for rem in range(incr, k + 1):
                        p_rem = rem - incr
                        p_val = dp[r][c - 1][p_rem]
                        if p_val != -1:
                            n_val = p_val + grid[r][c]
                            if dp[r][c][rem] == -1 or n_val > dp[r][c][rem]:
                                dp[r][c][rem] = n_val
                if r > 0:
                    for rem in range(incr, k + 1):
                        p_rem = rem - incr
                        p_val = dp[r - 1][c][p_rem]
                        if p_val != -1:
                            n_val = p_val + grid[r][c]
                            if dp[r][c][rem] == -1 or n_val > dp[r][c][rem]:
                                dp[r][c][rem] = n_val
        return max(dp[-1][-1])
