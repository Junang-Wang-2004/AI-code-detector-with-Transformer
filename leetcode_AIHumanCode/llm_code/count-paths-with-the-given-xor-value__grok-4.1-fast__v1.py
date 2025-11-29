class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        MOD = 10**9 + 7
        BITS = 16
        rows = len(grid)
        cols = len(grid[0])
        prev = [[0] * BITS for _ in range(cols)]
        prev[0][0] = 1
        for r in range(rows):
            curr = [[0] * BITS for _ in range(cols)]
            for c in range(cols):
                val = grid[r][c]
                for x in range(BITS):
                    nx = val ^ x
                    curr[c][nx] = (curr[c][nx] + prev[c][x]) % MOD
            for c in range(1, cols):
                val = grid[r][c]
                for x in range(BITS):
                    nx = val ^ x
                    curr[c][nx] = (curr[c][nx] + curr[c - 1][x]) % MOD
            prev = curr
        return prev[cols - 1][k]
