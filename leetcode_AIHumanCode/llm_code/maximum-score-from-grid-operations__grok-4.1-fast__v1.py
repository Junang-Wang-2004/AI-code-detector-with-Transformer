class Solution:
    def maximumScore(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        prev_s = [0] * (n + 1)
        for r in range(n):
            prev_s[r + 1] = prev_s[r] + grid[r][0]
        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)
        for c in range(1, m):
            cur_s = [0] * (n + 1)
            for r in range(n):
                cur_s[r + 1] = cur_s[r] + grid[r][c]
            max_complete = max(dp1)
            best_left = float('-inf')
            new_dp0 = [0] * (n + 1)
            for i in range(n + 1):
                best_left = max(best_left, dp0[i] - prev_s[i])
                new_dp0[i] = prev_s[i] + best_left
                new_dp0[i] = max(new_dp0[i], max_complete)
            suf_best = [float('-inf')] * (n + 2)
            for k in range(n, -1, -1):
                suf_best[k] = max(suf_best[k + 1], dp1[k] + cur_s[k])
            new_dp1 = [0] * (n + 1)
            for i in range(n + 1):
                new_dp1[i] = suf_best[i + 1] - cur_s[i]
                new_dp1[i] = max(new_dp1[i], new_dp0[i])
            dp0 = new_dp0
            dp1 = new_dp1
            prev_s = cur_s
        return max(dp1)
