class Solution:
    def solveNQueens(self, n):
        board = [['.'] * n for _ in range(n)]
        solutions = []

        def place_queen(r):
            if r == n:
                solutions.append([''.join(row) for row in board])
                return
            for c in range(n):
                if can_place(r, c):
                    board[r][c] = 'Q'
                    place_queen(r + 1)
                    board[r][c] = '.'

        def can_place(r, c):
            for prev_row in range(r):
                if board[prev_row][c] == 'Q':
                    return False
                d1 = r + c - prev_row
                if 0 <= d1 < n and board[prev_row][d1] == 'Q':
                    return False
                d2 = prev_row - r + c
                if 0 <= d2 < n and board[prev_row][d2] == 'Q':
                    return False
            return True

        place_queen(0)
        return solutions
