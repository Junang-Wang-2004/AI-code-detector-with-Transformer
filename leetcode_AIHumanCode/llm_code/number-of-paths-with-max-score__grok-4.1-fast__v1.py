class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        m, n = len(board), len(board[0])
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        if board[0][0] not in "XS":
            val = 0 if board[0][0] == 'E' else int(board[0][0])
            dp[0][0] = [val, 1]
        for i in range(m):
            for j in range(n):
                if board[i][j] in "XS":
                    continue
                max_score = -1
                ways = 0
                for di, dj in [(0, -1), (-1, 0), (-1, -1)]:
                    pi, pj = i + di, j + dj
                    if 0 <= pi < m and 0 <= pj < n and dp[pi][pj][1] > 0:
                        cand = dp[pi][pj][0]
                        if cand > max_score:
                            max_score = cand
                            ways = dp[pi][pj][1]
                        elif cand == max_score:
                            ways = (ways + dp[pi][pj][1]) % MOD
                if max_score != -1:
                    add = 0 if board[i][j] == 'E' else int(board[i][j])
                    dp[i][j] = [max_score + add, ways]
        return dp[m - 1][n - 1]
