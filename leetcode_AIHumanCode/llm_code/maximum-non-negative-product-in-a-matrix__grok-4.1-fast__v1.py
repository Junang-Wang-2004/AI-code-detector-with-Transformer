class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        if not grid or not grid[0]:
            return 0
        r, c = len(grid), len(grid[0])
        best = [[0] * c for _ in range(r)]
        worst = [[0] * c for _ in range(r)]
        best[0][0] = worst[0][0] = grid[0][0]
        for j in range(1, c):
            val = grid[0][j]
            cand1 = best[0][j - 1] * val
            cand2 = worst[0][j - 1] * val
            best[0][j] = max(cand1, cand2)
            worst[0][j] = min(cand1, cand2)
        for i in range(1, r):
            val = grid[i][0]
            cand1 = best[i - 1][0] * val
            cand2 = worst[i - 1][0] * val
            best[i][0] = max(cand1, cand2)
            worst[i][0] = min(cand1, cand2)
        for i in range(1, r):
            for j in range(1, c):
                val = grid[i][j]
                up_best = best[i - 1][j] * val
                up_worst = worst[i - 1][j] * val
                left_best = best[i][j - 1] * val
                left_worst = worst[i][j - 1] * val
                candidates = [up_best, up_worst, left_best, left_worst]
                best[i][j] = max(candidates)
                worst[i][j] = min(candidates)
        res = best[r - 1][c - 1]
        return res % MOD if res >= 0 else -1
