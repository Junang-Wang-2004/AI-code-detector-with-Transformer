class Solution:
    def gameOfLife(self, board):
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x in range(rows):
            for y in range(cols):
                neighbors = sum(
                    board[x + dx][y + dy] & 1
                    for dx, dy in deltas
                    if 0 <= x + dx < rows and 0 <= y + dy < cols
                )
                alive = board[x][y] & 1
                if (alive and 2 <= neighbors <= 3) or (not alive and neighbors == 3):
                    board[x][y] |= 2
        for x in range(rows):
            for y in range(cols):
                board[x][y] >>= 1
