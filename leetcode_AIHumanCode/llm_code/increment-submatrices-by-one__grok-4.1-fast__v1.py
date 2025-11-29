class Solution:
    def rangeAddQueries(self, n, queries):
        board = [[0] * n for _ in range(n)]
        for r_start, c_start, r_end, c_end in queries:
            board[r_start][c_start] += 1
            if c_end + 1 < n:
                board[r_start][c_end + 1] -= 1
            if r_end + 1 < n:
                board[r_end + 1][c_start] -= 1
            if r_end + 1 < n and c_end + 1 < n:
                board[r_end + 1][c_end + 1] += 1
        for row in range(n):
            accum = 0
            for col in range(n):
                accum += board[row][col]
                board[row][col] = accum
        for col in range(n):
            accum = 0
            for row in range(n):
                accum += board[row][col]
                board[row][col] = accum
        return board
