class Solution:
    def updateBoard(self, board, click):
        def reveal(i, j):
            mine_count = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 'M':
                        mine_count += 1
            if mine_count > 0:
                board[i][j] = str(mine_count)
                return
            board[i][j] = 'B'
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 'E':
                        reveal(ni, nj)

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            reveal(row, col)
        return board
