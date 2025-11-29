class Solution:
    def queensAttacktheKing(self, queens, king):
        grid = [[0] * 8 for _ in range(8)]
        for row, col in queens:
            grid[row][col] = 1
        attacks = []
        krow, kcol = king
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for drow, dcol in moves:
            row, col = krow + drow, kcol + dcol
            while 0 <= row < 8 and 0 <= col < 8:
                if grid[row][col] == 1:
                    attacks.append([row, col])
                    break
                row += drow
                col += dcol
        return attacks
