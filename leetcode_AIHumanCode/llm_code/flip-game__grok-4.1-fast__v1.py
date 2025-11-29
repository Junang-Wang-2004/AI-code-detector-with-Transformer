class Solution:
    def generatePossibleNextMoves(self, s):
        moves = []
        board = list(s)
        size = len(board)
        for pos in range(size - 1):
            if board[pos] == '+' and board[pos + 1] == '+':
                copy_board = board[:]
                copy_board[pos] = '-'
                copy_board[pos + 1] = '-'
                moves.append(''.join(copy_board))
        return moves
