class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        board = [[0.0] * n for _ in range(n)]
        board[row][column] = 1.0
        for _ in range(k):
            next_board = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    contrib = board[i][j] / 8
                    for di, dj in moves:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            next_board[ni][nj] += contrib
            board = next_board
        return sum(sum(r) for r in board)
