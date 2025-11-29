class Solution:
    def candyCrush(self, board):
        h, w = len(board), len(board[0])
        while True:
            crushed = False
            for i in range(h):
                for j in range(w - 2):
                    v = abs(board[i][j])
                    if v > 0 and v == abs(board[i][j + 1]) and v == abs(board[i][j + 2]):
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -v
                        crushed = True
            for j in range(w):
                for i in range(h - 2):
                    v = abs(board[i][j])
                    if v > 0 and v == abs(board[i + 1][j]) and v == abs(board[i + 2][j]):
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -v
                        crushed = True
            if not crushed:
                break
            for j in range(w):
                candies = [board[i][j] for i in range(h) if board[i][j] > 0]
                num_zeros = h - len(candies)
                for i in range(num_zeros):
                    board[i][j] = 0
                for idx, i in enumerate(range(num_zeros, h)):
                    board[i][j] = candies[idx]
        return board
