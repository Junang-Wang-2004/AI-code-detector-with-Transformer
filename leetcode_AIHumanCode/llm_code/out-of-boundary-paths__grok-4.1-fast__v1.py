class Solution(object):
    def findPaths(self, m, n, N, x, y):
        MOD = 10**9 + 7
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        prev = [[0] * n for _ in range(m)]
        prev[x][y] = 1
        ans = 0
        for _ in range(N):
            curr = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    ways = prev[i][j]
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            curr[ni][nj] = (curr[ni][nj] + ways) % MOD
                        else:
                            ans = (ans + ways) % MOD
            prev = curr
        return ans
